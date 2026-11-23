"""
Pattern Analysis Engine for Composio 100-App Assessment
Computes analytical clusters, auth dominance, gated-vs-self-serve ratios,
and blocker taxonomy across the research set.
"""

import json
from collections import Counter, defaultdict

def analyze():
    with open("data/apps_dataset.json", "r", encoding="utf-8") as f:
        apps = json.load(f)

    total_apps = len(apps)
    print(f"Total Apps Analyzed: {total_apps}\n" + "="*50)

    # 1. Buildability Verdicts
    verdict_counts = Counter(app["buildability_verdict"] for app in apps)
    print("\n1. BUILDABILITY VERDICTS:")
    for verdict, count in verdict_counts.most_common():
        pct = (count / total_apps) * 100
        print(f"  - {verdict}: {count} ({pct:.1f}%)")

    # 2. Auth Methods Distribution
    auth_counter = Counter()
    primary_auth_counter = Counter()
    for app in apps:
        methods = app["auth_methods"]
        # Determine dominant primary auth type
        primary = "Other"
        has_oauth = any("OAuth" in m for m in methods)
        has_api_key = any("API Key" in m or "Token" in m for m in methods)
        has_basic = any("Basic" in m for m in methods)
        has_zero = any("No Auth" in m for m in methods)

        if has_oauth and has_api_key:
            primary_auth_counter["Hybrid (OAuth2 + API Key)"] += 1
        elif has_oauth:
            primary_auth_counter["OAuth2"] += 1
        elif has_api_key:
            primary_auth_counter["API Key / Bearer Token"] += 1
        elif has_basic:
            primary_auth_counter["HTTP Basic Auth"] += 1
        elif has_zero:
            primary_auth_counter["Zero Auth / CLI"] += 1
        else:
            primary_auth_counter["Proprietary / Other"] += 1

        for m in methods:
            if "OAuth2" in m or "OAuth" in m:
                auth_counter["OAuth2"] += 1
            elif "API Key" in m:
                auth_counter["API Key"] += 1
            elif "Basic" in m:
                auth_counter["Basic Auth"] += 1
            elif "Token" in m or "Bearer" in m:
                auth_counter["Bearer / Personal Token"] += 1
            elif "No Auth" in m:
                auth_counter["Zero Auth (CLI)"] += 1
            elif "JWT" in m:
                auth_counter["JWT / Keypair"] += 1
            else:
                auth_counter["Other"] += 1

    print("\n2. PRIMARY AUTH CLUSTERS:")
    for auth, count in primary_auth_counter.most_common():
        pct = (count / total_apps) * 100
        print(f"  - {auth}: {count} ({pct:.1f}%)")

    # 3. Self-Serve vs Gated by Category
    category_data = defaultdict(lambda: {"total": 0, "self_serve": 0, "gated": 0, "paid_gated": 0})
    for app in apps:
        cat = app["category"]
        category_data[cat]["total"] += 1
        status = app["self_serve_status"].lower()
        if "gated" in status or "enterprise" in status or "sales" in status:
            category_data[cat]["gated"] += 1
        elif "paid plan" in status or "add-on only" in status:
            category_data[cat]["paid_gated"] += 1
        else:
            category_data[cat]["self_serve"] += 1

    print("\n3. ACCESSIBILITY BY CATEGORY (Self-Serve vs Gated):")
    total_self = sum(d["self_serve"] for d in category_data.values())
    total_gated = sum(d["gated"] for d in category_data.values())
    total_paid_gated = sum(d["paid_gated"] for d in category_data.values())
    print(f"  Overall: Self-Serve {total_self}% | Gated/Enterprise {total_gated}% | Paid-Gated {total_paid_gated}%")
    print("-" * 50)
    for cat, d in sorted(category_data.items(), key=lambda x: x[1]["self_serve"], reverse=True):
        self_pct = (d["self_serve"] / d["total"]) * 100
        print(f"  - {cat:40s}: {d['self_serve']:2d}/{d['total']} self-serve ({self_pct:5.1f}%) | {d['gated']} gated | {d['paid_gated']} paid-gated")

    # 4. MCP Status Distribution
    mcp_counter = Counter()
    for app in apps:
        m = app["mcp_status"].lower()
        if "official" in m and "mcp" in m:
            mcp_counter["Official MCP Server"] += 1
        elif "community mcp" in m:
            mcp_counter["Community MCP Available"] += 1
        elif "native mcp" in m:
            mcp_counter["Native MCP Server"] += 1
        elif "cli" in m:
            mcp_counter["CLI / Skill Wrapped"] += 1
        else:
            mcp_counter["No Published MCP (Standard REST/GraphQL)"] += 1

    print("\n4. MCP (MODEL CONTEXT PROTOCOL) READINESS:")
    for status, count in mcp_counter.most_common():
        pct = (count / total_apps) * 100
        print(f"  - {status}: {count} ({pct:.1f}%)")

    # Save summary stats to JSON for HTML rendering
    stats_summary = {
        "total_apps": total_apps,
        "ready_now": verdict_counts.get("Ready Now", 0),
        "ready_caveats": verdict_counts.get("Ready with Caveats", 0),
        "blocked_gated": verdict_counts.get("Blocked - Enterprise Gated", 0),
        "total_self_serve": total_self,
        "total_gated": total_gated,
        "total_paid_gated": total_paid_gated,
        "primary_auth": dict(primary_auth_counter.most_common()),
        "category_breakdown": dict(category_data),
        "mcp_readiness": dict(mcp_counter.most_common())
    }

    with open("data/analysis_summary.json", "w", encoding="utf-8") as f:
        json.dump(stats_summary, f, indent=2)
    print("\nSaved analysis summary to data/analysis_summary.json")

if __name__ == "__main__":
    analyze()
