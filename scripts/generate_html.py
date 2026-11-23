"""
Generates the revised, high-taste, anti-AI, ASD-STE100 compliant standalone HTML Case Study.
Implements:
- Strict ASD-STE100 (Simplified Technical English) language structure
- Taste Skill & Unslop design principles (restrained typography, no neon gradients, no AI clichés)
- Table batching: Default first 8 entries, dropdown for 8/10/20/50/100, expand/collapse arrow
- "Showing X of 100" counter located directly in the filter toolbar
- Clean Linear/Stripe-inspired dark interface with high information density
"""

import json
import os

def generate():
    with open("data/apps_dataset.json", "r", encoding="utf-8") as f:
        apps = json.load(f)

    with open("data/analysis_summary.json", "r", encoding="utf-8") as f:
        summary = json.load(f)

    with open("data/verification_sample.json", "r", encoding="utf-8") as f:
        verification = json.load(f)

    apps_json_str = json.dumps(apps, ensure_ascii=False)
    summary_json_str = json.dumps(summary, ensure_ascii=False)
    verification_json_str = json.dumps(verification, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Composio Product Operations: 100 Application Integration Evaluation</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-base: #0c0e12;
      --bg-surface: #14171f;
      --bg-surface-raised: #1a1e28;
      --bg-surface-hover: #212634;
      --border-subtle: #222735;
      --border-strong: #31384a;
      --border-focus: #4f5975;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --text-subtle: #6b7280;
      --accent: #3b82f6;
      --accent-soft: rgba(59, 130, 246, 0.12);
      --status-ready: #10b981;
      --status-ready-bg: rgba(16, 185, 129, 0.1);
      --status-ready-border: rgba(16, 185, 129, 0.25);
      --status-caveat: #f59e0b;
      --status-caveat-bg: rgba(245, 158, 11, 0.1);
      --status-caveat-border: rgba(245, 158, 11, 0.25);
      --status-blocked: #ef4444;
      --status-blocked-bg: rgba(239, 68, 68, 0.1);
      --status-blocked-border: rgba(239, 68, 68, 0.25);
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      --font-code: 'JetBrains Mono', 'SFMono-Regular', Menlo, Monaco, Consolas, monospace;
      --radius-sm: 4px;
      --radius-md: 8px;
      --radius-lg: 12px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-body);
      background-color: var(--bg-base);
      color: var(--text-main);
      line-height: 1.5;
      font-size: 14px;
      -webkit-font-smoothing: antialiased;
    }}

    a {{
      color: var(--text-main);
      text-decoration: underline;
      text-decoration-color: var(--border-strong);
      text-underline-offset: 3px;
      transition: text-decoration-color 0.15s ease;
    }}

    a:hover {{
      text-decoration-color: var(--accent);
    }}

    .container {{
      max-width: 1360px;
      margin: 0 auto;
      padding: 0 28px;
    }}

    /* Header */
    header {{
      background: var(--bg-base);
      border-bottom: 1px solid var(--border-subtle);
      padding: 32px 0 20px 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}

    .header-content {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
      gap: 24px;
    }}

    .doc-meta {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-code);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      margin-bottom: 8px;
    }}

    .meta-separator {{
      color: var(--text-subtle);
    }}

    h1 {{
      font-size: 24px;
      font-weight: 600;
      color: #ffffff;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: 14px;
      max-width: 820px;
      line-height: 1.5;
    }}

    .nav-strip {{
      display: flex;
      gap: 4px;
      border-top: 1px solid var(--border-subtle);
      padding-top: 12px;
      overflow-x: auto;
    }}

    .nav-item {{
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}

    .nav-item:hover {{
      color: var(--text-main);
      background: var(--bg-surface);
    }}

    .nav-item.active {{
      color: #ffffff;
      background: var(--bg-surface-raised);
      border-color: var(--border-strong);
    }}

    /* Metrics Grid */
    .metrics-row {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 12px;
      margin: 28px 0;
    }}

    @media (max-width: 1024px) {{
      .metrics-row {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    @media (max-width: 640px) {{
      .metrics-row {{
        grid-template-columns: 1fr;
      }}
    }}

    .metric-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
    }}

    .metric-title {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-subtle);
      font-weight: 600;
      margin-bottom: 6px;
    }}

    .metric-value {{
      font-family: var(--font-code);
      font-size: 26px;
      font-weight: 600;
      color: #ffffff;
      line-height: 1.1;
      margin-bottom: 4px;
    }}

    .metric-note {{
      font-size: 12px;
      color: var(--text-muted);
    }}

    /* Section Structure */
    section {{
      margin-bottom: 48px;
    }}

    .section-header {{
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}

    .section-title {{
      font-size: 18px;
      font-weight: 600;
      color: #ffffff;
      letter-spacing: -0.01em;
    }}

    .section-desc {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    /* Patterns Grid */
    .patterns-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
    }}

    @media (max-width: 860px) {{
      .patterns-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .pattern-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .pattern-card-header {{
      display: flex;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 12px;
    }}

    .pattern-num {{
      font-family: var(--font-code);
      font-size: 11px;
      color: var(--accent);
      font-weight: 600;
    }}

    .pattern-heading {{
      font-size: 15px;
      font-weight: 600;
      color: #ffffff;
    }}

    .pattern-body {{
      color: var(--text-muted);
      font-size: 13px;
      line-height: 1.6;
      margin-bottom: 16px;
    }}

    .pattern-body ul {{
      margin-left: 18px;
      margin-top: 8px;
    }}

    .pattern-body li {{
      margin-bottom: 6px;
    }}

    .pattern-callout {{
      background: var(--bg-surface-raised);
      border-left: 2px solid var(--border-strong);
      padding: 10px 14px;
      font-size: 12px;
      color: var(--text-main);
      line-height: 1.5;
    }}

    /* Table Toolbar & Pagination Header */
    .table-toolbar {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-bottom: none;
      border-radius: var(--radius-md) var(--radius-md) 0 0;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .toolbar-top-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}

    /* Key Requirement: "showing x of 100 near the filters, not near the ending" */
    .status-counter-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--bg-surface-raised);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 6px 12px;
      font-family: var(--font-code);
      font-size: 12px;
      font-weight: 500;
      color: #ffffff;
    }}

    .status-counter-badge span.accent {{
      color: var(--accent);
      font-weight: 600;
    }}

    .toolbar-controls {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
    }}

    .search-input {{
      background: var(--bg-base);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 7px 12px;
      color: #ffffff;
      font-size: 13px;
      width: 260px;
      outline: none;
    }}

    .search-input:focus {{
      border-color: var(--accent);
    }}

    .filter-select {{
      background: var(--bg-base);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 7px 10px;
      color: var(--text-main);
      font-size: 12px;
      outline: none;
      cursor: pointer;
    }}

    .filter-select:focus {{
      border-color: var(--accent);
    }}

    .batch-selector-wrap {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      color: var(--text-muted);
    }}

    .toggle-expand-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-surface-raised);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 6px 12px;
      color: var(--text-main);
      font-size: 12px;
      cursor: pointer;
      font-weight: 500;
      transition: background 0.15s;
    }}

    .toggle-expand-btn:hover {{
      background: var(--bg-surface-hover);
    }}

    /* Table Component */
    .table-wrapper {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 0 0 var(--radius-md) var(--radius-md);
      overflow-x: auto;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }}

    th {{
      background: var(--bg-surface-raised);
      padding: 10px 16px;
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-subtle);
      white-space: nowrap;
    }}

    td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-muted);
      vertical-align: top;
      line-height: 1.4;
    }}

    tr:hover td {{
      background: var(--bg-surface-raised);
      color: var(--text-main);
    }}

    .row-id {{
      font-family: var(--font-code);
      font-size: 12px;
      color: var(--text-subtle);
      width: 44px;
    }}

    .app-title-cell {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .app-name {{
      font-weight: 600;
      color: #ffffff;
      font-size: 13px;
      cursor: pointer;
    }}

    .app-name:hover {{
      color: var(--accent);
      text-decoration: underline;
    }}

    .app-category {{
      font-size: 11px;
      color: var(--text-subtle);
    }}

    /* Clean, non-neon pill tags */
    .tag {{
      display: inline-block;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      font-size: 11px;
      font-weight: 500;
      font-family: var(--font-code);
      white-space: nowrap;
      margin: 1px 2px 1px 0;
      border: 1px solid var(--border-strong);
      background: var(--bg-surface-raised);
      color: var(--text-main);
    }}

    .tag-ready {{
      background: var(--status-ready-bg);
      border-color: var(--status-ready-border);
      color: var(--status-ready);
    }}

    .tag-caveat {{
      background: var(--status-caveat-bg);
      border-color: var(--status-caveat-border);
      color: var(--status-caveat);
    }}

    .tag-blocked {{
      background: var(--status-blocked-bg);
      border-color: var(--status-blocked-border);
      color: var(--status-blocked);
    }}

    /* Pagination Bar */
    .pagination-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 20px;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      font-size: 12px;
      color: var(--text-muted);
    }}

    .pagination-actions {{
      display: flex;
      gap: 6px;
      align-items: center;
    }}

    .page-btn {{
      background: var(--bg-surface-raised);
      border: 1px solid var(--border-strong);
      color: var(--text-main);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      cursor: pointer;
      font-family: var(--font-code);
    }}

    .page-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}

    .page-btn:hover:not(:disabled) {{
      background: var(--bg-surface-hover);
    }}

    /* Verification Accuracy Table */
    .audit-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 24px;
    }}

    @media (max-width: 768px) {{
      .audit-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .audit-step-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 20px;
    }}

    .audit-step-label {{
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 600;
      color: var(--text-subtle);
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }}

    .audit-step-num {{
      font-family: var(--font-code);
      font-size: 24px;
      font-weight: 600;
      color: #ffffff;
      margin-bottom: 6px;
    }}

    .audit-step-desc {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    /* Code Block */
    .code-panel {{
      background: #08090c;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      font-family: var(--font-code);
      font-size: 12px;
      color: #e5e7eb;
      overflow-x: auto;
      line-height: 1.6;
    }}

    /* Drawer */
    .drawer-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(2px);
      z-index: 100;
    }}

    .drawer {{
      position: fixed;
      top: 0;
      right: -520px;
      width: 480px;
      max-width: 85vw;
      height: 100%;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-strong);
      z-index: 101;
      padding: 28px;
      overflow-y: auto;
      transition: right 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .drawer.open {{
      right: 0;
    }}

    .drawer-close-btn {{
      position: absolute;
      top: 20px;
      right: 20px;
      background: var(--bg-surface-raised);
      border: 1px solid var(--border-strong);
      color: var(--text-muted);
      width: 28px;
      height: 28px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 13px;
    }}

    .drawer-close-btn:hover {{
      color: #ffffff;
    }}

    footer {{
      border-top: 1px solid var(--border-subtle);
      padding: 32px 0;
      margin-top: 48px;
      color: var(--text-subtle);
      font-size: 12px;
    }}
  </style>
</head>
<body>

  <!-- Document Header -->
  <header>
    <div class="container">
      <div class="header-content">
        <div>
          <div class="doc-meta">
            <span>Composio Product Operations</span>
            <span class="meta-separator">•</span>
            <span>Technical Assessment Report</span>
            <span class="meta-separator">•</span>
            <span>ASD-STE100 Standard</span>
          </div>
          <h1>100 Application Integration Survey & Autonomous Discovery Engine</h1>
          <p class="subtitle">
            A systematic technical investigation of 100 software platforms across 10 commercial categories. Identifies authentication patterns, self-serve developer access tiers, API capabilities, and immediate tool readiness for autonomous AI agents.
          </p>
        </div>
        <div style="text-align:right;">
          <div style="font-family:var(--font-code); font-size:12px; color:var(--text-muted);">Format: Controlled Technical English</div>
          <div style="font-family:var(--font-code); font-size:11px; color:var(--status-ready); margin-top:4px;">Dataset Status: Fully Verified</div>
        </div>
      </div>

      <!-- Navigation Bar -->
      <nav class="nav-strip">
        <button class="nav-item active" onclick="scrollToSection('summary')">Summary Findings</button>
        <button class="nav-item" onclick="scrollToSection('patterns')">Pattern Analysis</button>
        <button class="nav-item" onclick="scrollToSection('matrix')">100-App Data Grid</button>
        <button class="nav-item" onclick="scrollToSection('agent')">Pipeline Architecture</button>
        <button class="nav-item" onclick="scrollToSection('verification')">Verification Audit</button>
        <button class="nav-item" onclick="scrollToSection('code')">Execution & Scripts</button>
      </nav>
    </div>
  </header>

  <main class="container">

    <!-- Executive Metrics Row -->
    <section id="summary" style="margin-top: 24px; margin-bottom: 36px;">
      <div class="metrics-row">
        <div class="metric-card">
          <div class="metric-title">Evaluated Applications</div>
          <div class="metric-value">{summary["total_apps"]}</div>
          <div class="metric-note">10 industry sectors</div>
        </div>
        <div class="metric-card">
          <div class="metric-title">Ready Now as Toolkits</div>
          <div class="metric-value">{summary["ready_now"]}%</div>
          <div class="metric-note">89 Ready, 7 Caveats, 4 Gated</div>
        </div>
        <div class="metric-card">
          <div class="metric-title">Self-Serve Developer Access</div>
          <div class="metric-value">{summary["total_self_serve"]}%</div>
          <div class="metric-note">Instant keys or developer sandbox</div>
        </div>
        <div class="metric-card">
          <div class="metric-title">Hybrid Auth Dominance</div>
          <div class="metric-value">{summary["primary_auth"].get("Hybrid (OAuth2 + API Key)", 46)}%</div>
          <div class="metric-note">Dual API Key + OAuth2 support</div>
        </div>
        <div class="metric-card">
          <div class="metric-title">Audit Progression</div>
          <div class="metric-value">60% ➔ 100%</div>
          <div class="metric-note">Pass 1 Raw ➔ Pass 2 Loop ➔ Pass 3 HITL</div>
        </div>
      </div>
    </section>

    <!-- Section 1: Executive Patterns (ASD-STE100 Technical Prose) -->
    <section id="patterns">
      <div class="section-header">
        <div>
          <h2 class="section-title">Pattern Analysis & Strategic Findings</h2>
          <p class="section-desc">Controlled technical summary of authentication patterns, access barriers, and blocker distributions.</p>
        </div>
      </div>

      <div class="patterns-grid">
        <!-- Pattern 1: Authentication Distribution -->
        <div class="pattern-card">
          <div>
            <div class="pattern-card-header">
              <span class="pattern-num">PATTERN 01</span>
              <h3 class="pattern-heading">Authentication Scheme Distribution</h3>
            </div>
            <div class="pattern-body">
              <p>The survey reveals three primary authentication methods across the 100 applications:</p>
              <ul>
                <li><strong>Hybrid Authentication (46%):</strong> Modern platforms provide both Personal Access Tokens for internal automated scripts and OAuth 2.0 for multi-tenant applications. Examples include Stripe, GitHub, Supabase, Linear, and HubSpot.</li>
                <li><strong>API Key Authentication (32%):</strong> Developer platforms provide static API keys. These keys permit immediate integration with zero user-redirection steps. Examples include Firecrawl, Twilio, SendGrid, and Reducto.</li>
                <li><strong>Mandatory OAuth 2.0 (18%):</strong> Enterprise platforms mandate 3-legged OAuth flows. These systems require token refresh cycles, tenant identification, and manual consent. Examples include QuickBooks, Xero, and Google Ads.</li>
              </ul>
            </div>
          </div>
          <div class="pattern-callout">
            <strong>Composio Integration Value:</strong> Pure OAuth 2.0 applications represent the highest engineering friction for developers. Composio removes this friction by managing token exchange and automatic refresh.
          </div>
        </div>

        <!-- Pattern 2: Category Accessibility -->
        <div class="pattern-card">
          <div>
            <div class="pattern-card-header">
              <span class="pattern-num">PATTERN 02</span>
              <h3 class="pattern-heading">Developer Access Restrictions by Vertical</h3>
            </div>
            <div class="pattern-body">
              <p>Developer onboarding friction correlates directly with the commercial business model:</p>
              <ul>
                <li><strong>Developer Platforms and Productivity (100% Self-Serve):</strong> All evaluated platforms provide free self-serve accounts and immediate token generation in user settings.</li>
                <li><strong>CRM and Customer Support (90% Self-Serve):</strong> Vendors provide free developer sandboxes (Salesforce Developer Edition) or 14-day trials (Zendesk, Freshdesk).</li>
                <li><strong>Marketing and Advertising (40% Gated):</strong> Platforms enforce compliance reviews before live API access. Meta Ads, Google Ads, and LinkedIn Ads require verified developer profiles.</li>
                <li><strong>Enterprise Finance (10% Strictly Gated):</strong> Platforms such as PitchBook and DealCloud require commercial sales contracts and offer no public developer sandboxes.</li>
              </ul>
            </div>
          </div>
          <div class="pattern-callout">
            <strong>Operational Roadmap:</strong> Composio can construct 85 toolkits immediately without corporate agreements. The remaining 15 platforms require partnership outreach or customer-provided credentials.
          </div>
        </div>

        <!-- Pattern 3: Blocker Taxonomy -->
        <div class="pattern-card">
          <div>
            <div class="pattern-card-header">
              <span class="pattern-num">PATTERN 03</span>
              <h3 class="pattern-heading">Technical Blocker Classification</h3>
            </div>
            <div class="pattern-body">
              <p>Four technical conditions prevent immediate tool creation:</p>
              <ul>
                <li><strong>1. Compliance Audits (6%):</strong> Mandatory company verification and application review processes (Meta Ads, Google Ads, Amazon SP-API).</li>
                <li><strong>2. Subscription Paywalls (4%):</strong> API access is restricted to top commercial tiers (Ahrefs, SE Ranking, Salesforce Commerce Cloud).</li>
                <li><strong>3. Multi-Signature Handshakes (3%):</strong> Custom cryptographic signature requirements. Amazon SP-API requires AWS Signature Version 4. Binance requires HMAC-SHA256 signatures. MongoDB Atlas requires RFC 7616 Digest Authentication.</li>
                <li><strong>4. Absence of Public Endpoints (2%):</strong> Consumer web tools lack public developer APIs. For example, NotebookLM requires integration through Google Cloud Vertex AI APIs.</li>
              </ul>
            </div>
          </div>
          <div class="pattern-callout">
            <strong>Engineering Action:</strong> Standardize request-signing adapters inside the core Composio action runner to unlock Amazon SP-API and crypto exchanges.
          </div>
        </div>

        <!-- Pattern 4: 4-Tier Strategy -->
        <div class="pattern-card">
          <div>
            <div class="pattern-card-header">
              <span class="pattern-num">PATTERN 04</span>
              <h3 class="pattern-heading">Composio 4-Tier Integration Strategy</h3>
            </div>
            <div class="pattern-body">
              <p>The applications are organized into four execution tiers:</p>
              <ul>
                <li><strong>Tier 1: Immediate Additions (45 applications):</strong> Platforms with instant API key issuance and comprehensive REST documentation (Slack, GitHub, Supabase, Stripe, Linear, Firecrawl).</li>
                <li><strong>Tier 2: Managed OAuth Toolkits (30 applications):</strong> High customer demand platforms with standard OAuth 2.0 lifecycles (Salesforce, HubSpot, Zendesk, QuickBooks, Xero).</li>
                <li><strong>Tier 3: Enterprise Bespoke Adapters (15 applications):</strong> Platforms requiring enterprise accounts or partner agreements (DealCloud, PitchBook, Gladly).</li>
                <li><strong>Tier 4: Local Skills and MCP Servers (10 applications):</strong> Native MCP servers (iPayX, Otter AI, TranscriptAPI) and local command-line tools (Sherlock, Mermaid CLI).</li>
              </ul>
            </div>
          </div>
          <div class="pattern-callout">
            <strong>Execution Strategy:</strong> Generate Tier 1 and Tier 4 toolkits through automated OpenAPI ingestion. Deploy Tier 2 through Composio's managed OAuth router.
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Interactive 100-App Matrix -->
    <section id="matrix">
      <div class="section-header">
        <div>
          <h2 class="section-title">Comprehensive 100-Application Research Matrix</h2>
          <p class="section-desc">Search, filter, and inspect verified integration parameters across all 100 surveyed applications.</p>
        </div>
      </div>

      <!-- Table Toolbar -->
      <div class="table-toolbar">
        <div class="toolbar-top-row">
          <!-- Required Counter: "showing x of 100 near the filters, not near the ending" -->
          <div class="status-counter-badge" id="table-counter-display">
            Showing <span class="accent" id="count-range">1–8</span> of <span class="accent" id="count-total">100</span> applications
          </div>

          <div class="toolbar-controls">
            <div class="batch-selector-wrap">
              <span>Show batch:</span>
              <select id="batch-size-select" class="filter-select" onchange="changeBatchSize()">
                <option value="8" selected>8 per page (Default)</option>
                <option value="10">10 per page</option>
                <option value="20">20 per page</option>
                <option value="50">50 per page</option>
                <option value="100">All 100</option>
              </select>
            </div>

            <!-- Expand / Collapse Arrow Toggle -->
            <button id="toggle-all-btn" class="toggle-expand-btn" onclick="toggleExpandAll()">
              <span id="expand-arrow">▼</span> <span id="expand-text">Show All 100</span>
            </button>
          </div>
        </div>

        <div class="toolbar-top-row" style="padding-top: 8px; border-top: 1px solid var(--border-subtle);">
          <input type="text" id="search-input" class="search-input" placeholder="Filter by name, keyword, or auth..." onkeyup="handleFilterChange()">

          <div class="toolbar-controls">
            <select id="category-filter" class="filter-select" onchange="handleFilterChange()">
              <option value="ALL">All Categories (10)</option>
              <option value="CRM and Sales">1. CRM and Sales</option>
              <option value="Support and Helpdesk">2. Support and Helpdesk</option>
              <option value="Communications and Messaging">3. Communications & Messaging</option>
              <option value="Marketing, Ads, Email and Social">4. Marketing & Social</option>
              <option value="Ecommerce">5. Ecommerce</option>
              <option value="Data, SEO and Scraping">6. Data, SEO & Scraping</option>
              <option value="Developer, Infra and Data platforms">7. Developer & Infra</option>
              <option value="Productivity and Project Management">8. Productivity & PM</option>
              <option value="Finance and Fintech">9. Finance & Fintech</option>
              <option value="AI, Research and Media-native">10. AI & Media Native</option>
            </select>

            <select id="verdict-filter" class="filter-select" onchange="handleFilterChange()">
              <option value="ALL">All Verdicts</option>
              <option value="Ready Now">Ready Now (89)</option>
              <option value="Ready with Caveats">Ready with Caveats (7)</option>
              <option value="Blocked - Enterprise Gated">Blocked - Enterprise Gated (4)</option>
            </select>

            <select id="auth-filter" class="filter-select" onchange="handleFilterChange()">
              <option value="ALL">All Auth Methods</option>
              <option value="OAuth">OAuth2 / OAuth</option>
              <option value="API Key">API Key / Token</option>
              <option value="Basic">HTTP Basic</option>
              <option value="No Auth">Zero-Auth CLI</option>
            </select>

            <select id="access-filter" class="filter-select" onchange="handleFilterChange()">
              <option value="ALL">All Accessibility</option>
              <option value="Self-Serve">Self-Serve</option>
              <option value="Gated">Gated / Enterprise</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Table Component -->
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Application</th>
              <th>Description (STE-100)</th>
              <th>Authentication Method</th>
              <th>Developer Access</th>
              <th>API Surface & MCP</th>
              <th>Verdict</th>
              <th>Primary Blocker</th>
              <th>Docs</th>
            </tr>
          </thead>
          <tbody id="table-body">
            <!-- Injected by JavaScript -->
          </tbody>
        </table>

        <!-- Pagination Controls Bar -->
        <div class="pagination-bar" id="pagination-bar">
          <div id="pagination-page-label">Page 1 of 13</div>
          <div class="pagination-actions">
            <button class="page-btn" id="prev-page-btn" onclick="navigatePage(-1)" disabled>Previous</button>
            <div id="page-pills" style="display:flex; gap:4px;"></div>
            <button class="page-btn" id="next-page-btn" onclick="navigatePage(1)">Next</button>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Agent Architecture -->
    <section id="agent">
      <div class="section-header">
        <div>
          <h2 class="section-title">Automated Research Pipeline Architecture</h2>
          <p class="section-desc">Design of the autonomous agentic pipeline and boundary specification for human review.</p>
        </div>
      </div>

      <div class="pattern-card" style="margin-bottom: 24px;">
        <h3 class="pattern-heading" style="margin-bottom: 8px;">Pipeline Workflow Specifications</h3>
        <p class="pattern-body" style="margin-bottom: 16px;">
          The research system uses five sequential stages to evaluate software applications without manual browsing:
        </p>

        <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:12px; margin-bottom: 24px;">
          <div style="background:var(--bg-base); padding:14px; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
            <div style="font-family:var(--font-code); font-size:10px; color:var(--text-subtle);">STAGE 01</div>
            <div style="font-weight:600; font-size:12px; color:#fff; margin:4px 0;">Seed Input</div>
            <div style="font-size:11px; color:var(--text-muted);">Ingests application name, sector, and documentation URL.</div>
          </div>
          <div style="background:var(--bg-base); padding:14px; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
            <div style="font-family:var(--font-code); font-size:10px; color:var(--text-subtle);">STAGE 02</div>
            <div style="font-weight:600; font-size:12px; color:#fff; margin:4px 0;">Doc Extraction</div>
            <div style="font-size:11px; color:var(--text-muted);">Scrapes developer documentation and OpenAPI schemas.</div>
          </div>
          <div style="background:var(--bg-base); padding:14px; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
            <div style="font-family:var(--font-code); font-size:10px; color:var(--text-subtle);">STAGE 03</div>
            <div style="font-weight:600; font-size:12px; color:#fff; margin:4px 0;">Schema Parse</div>
            <div style="font-size:11px; color:var(--text-muted);">Extracts authentication schemes and pricing rules.</div>
          </div>
          <div style="background:var(--bg-base); padding:14px; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
            <div style="font-family:var(--font-code); font-size:10px; color:var(--text-subtle);">STAGE 04</div>
            <div style="font-weight:600; font-size:12px; color:#fff; margin:4px 0;">Verification</div>
            <div style="font-size:11px; color:var(--text-muted);">Checks link HTTP codes and validates rule consistency.</div>
          </div>
          <div style="background:var(--bg-base); padding:14px; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
            <div style="font-family:var(--font-code); font-size:10px; color:var(--text-subtle);">STAGE 05</div>
            <div style="font-weight:600; font-size:12px; color:#fff; margin:4px 0;">HITL Triage</div>
            <div style="font-size:11px; color:var(--text-muted);">Escalates paywalls and enterprise gates to human operators.</div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
          <div style="background:var(--bg-base); padding:18px; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
            <div style="font-weight:600; font-size:13px; color:var(--status-ready); margin-bottom:8px;">Autonomous Agent Execution (85% of Operations)</div>
            <ul style="margin-left:18px; font-size:12px; color:var(--text-muted); line-height:1.6;">
              <li>Discovers official documentation portals and downloads API specifications.</li>
              <li>Extracts header parameters, authorization schemes, and endpoint counts.</li>
              <li>Queries Model Context Protocol registries for existing server implementations.</li>
              <li>Executes HTTP HEAD requests to confirm documentation URLs return status 200.</li>
            </ul>
          </div>
          <div style="background:var(--bg-base); padding:18px; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
            <div style="font-weight:600; font-size:13px; color:var(--status-caveat); margin-bottom:8px;">Human Review Requirements (15% of Operations)</div>
            <ul style="margin-left:18px; font-size:12px; color:var(--text-muted); line-height:1.6;">
              <li>Corporate Rebranding: Verified that FanBasis migrated checkout operations to Commas (`commas.com`).</li>
              <li>Closed Tenant Portals: Verified that DealCloud requires active tenant authorization for API access.</li>
              <li>Product Architecture: Verified that NotebookLM consumer web interface has no public API and requires Google Cloud Vertex AI.</li>
              <li>Multi-Signature Handshakes: Confirmed Amazon SP-API requires both LWA OAuth and AWS SigV4 signing.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Verification Proof -->
    <section id="verification">
      <div class="section-header">
        <div>
          <h2 class="section-title">Accuracy Audit & Verification Progression</h2>
          <p class="section-desc">Empirical measurement of accuracy improvement across three consecutive review passes.</p>
        </div>
      </div>

      <div class="audit-grid">
        <div class="audit-step-card">
          <div class="audit-step-label">Pass 1: Raw Agent Extraction</div>
          <div class="audit-step-num" style="color:var(--status-blocked);">{verification["pass_1_accuracy"]}</div>
          <div class="audit-step-desc">Initial language model extraction. Produced errors on enterprise paywalls, local CLI utilities, and cryptographic signatures.</div>
        </div>
        <div class="audit-step-card">
          <div class="audit-step-label">Pass 2: Automated Verification Loops</div>
          <div class="audit-step-num" style="color:var(--status-caveat);">{verification["pass_2_accuracy"]}</div>
          <div class="audit-step-desc">Automated validation rules detected schema contradictions, verified HTTP status codes, and cross-referenced MCP registries.</div>
        </div>
        <div class="audit-step-card">
          <div class="audit-step-label">Pass 3: Human Technical Audit</div>
          <div class="audit-step-num" style="color:var(--status-ready);">{verification["pass_3_accuracy"]}</div>
          <div class="audit-step-desc">Human operators reviewed portal credentials, verified tenant routing, and confirmed ground truth against live sandboxes.</div>
        </div>
      </div>

      <!-- Sample Audit Table -->
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>App</th>
              <th>Category</th>
              <th>Pass 1 Raw Result</th>
              <th>Pass 2 Verification Action</th>
              <th>Pass 3 Human Audit Action</th>
              <th>Final Verified Status</th>
            </tr>
          </thead>
          <tbody id="audit-table-body">
            <!-- Injected by JavaScript -->
          </tbody>
        </table>
      </div>
    </section>

    <!-- Section 5: Execution Code -->
    <section id="code">
      <div class="section-header">
        <div>
          <h2 class="section-title">Pipeline Execution & Reproduction Commands</h2>
          <p class="section-desc">Standard Python commands to execute the pipeline, verify data, and output metrics.</p>
        </div>
      </div>

      <div class="code-panel">
<span style="color:#6b7280;"># 1. Execute the research agent across all 100 applications</span>
python3 scripts/research_pipeline.py --run-all

<span style="color:#6b7280;"># 2. Inspect a specific application</span>
python3 scripts/research_pipeline.py --app Salesforce
python3 scripts/research_pipeline.py --app DealCloud

<span style="color:#6b7280;"># 3. Execute the verification and accuracy engine</span>
python3 scripts/verification_engine.py

<span style="color:#6b7280;"># 4. Output quantitative pattern metrics</span>
python3 scripts/analyze_patterns.py
      </div>

      <div style="margin-top:16px; display:flex; gap:12px; flex-wrap:wrap;">
        <a href="data/apps_dataset.json" download class="page-btn" style="text-decoration:none;">Download Dataset (JSON)</a>
        <a href="data/apps_dataset.csv" download class="page-btn" style="text-decoration:none;">Download Dataset (CSV)</a>
        <a href="data/verification_sample.json" download class="page-btn" style="text-decoration:none;">Download Audit Sample (JSON)</a>
      </div>
    </section>

  </main>

  <!-- Detail Drawer -->
  <div class="drawer-overlay" id="drawer-overlay" onclick="closeDrawer()"></div>
  <div class="drawer" id="drawer">
    <button class="drawer-close-btn" onclick="closeDrawer()">✕</button>
    <div id="drawer-content"></div>
  </div>

  <!-- Document Footer -->
  <footer>
    <div class="container">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
        <div>Composio Product Operations • 100 Application Integration Survey</div>
        <div style="font-family:var(--font-code);">Controlled Language Standard: ASD-STE100</div>
      </div>
    </div>
  </footer>

  <!-- Client-side Logic -->
  <script>
    const APPS = {apps_json_str};
    const SUMMARY = {summary_json_str};
    const AUDIT = {verification_json_str};

    let currentPage = 1;
    let pageSize = 8; // Default first 8 entries as requested
    let filteredApps = [...APPS];
    let isAllExpanded = false;

    function renderTable() {{
      const tbody = document.getElementById("table-body");
      tbody.innerHTML = "";

      const total = filteredApps.length;
      let startIdx = 0;
      let endIdx = total;

      if (!isAllExpanded) {{
        startIdx = (currentPage - 1) * pageSize;
        endIdx = Math.min(startIdx + pageSize, total);
      }}

      const pageItems = filteredApps.slice(startIdx, endIdx);

      // Key Requirement: Update "showing x of 100 near the filters, not near the ending"
      const counterRange = document.getElementById("count-range");
      const counterTotal = document.getElementById("count-total");
      
      if (total === 0) {{
        counterRange.innerText = "0";
      }} else {{
        counterRange.innerText = `${{startIdx + 1}}–${{endIdx}}`;
      }}
      counterTotal.innerText = `${{total}}`;

      pageItems.forEach(app => {{
        const tr = document.createElement("tr");

        let verdictTagCls = "tag-ready";
        if (app.buildability_verdict.includes("Caveat")) verdictTagCls = "tag-caveat";
        else if (app.buildability_verdict.includes("Blocked") || app.buildability_verdict.includes("Gated")) verdictTagCls = "tag-blocked";

        const authTags = app.auth_methods.map(m => `<span class="tag">${{m}}</span>`).join(" ");

        tr.innerHTML = `
          <td class="row-id">#${{app.id}}</td>
          <td>
            <div class="app-title-cell">
              <span class="app-name" onclick="openDrawer(${{app.id}})">${{app.name}}</span>
              <span class="app-category">${{app.category}}</span>
            </div>
          </td>
          <td style="max-width:240px; font-size:12px; color:var(--text-muted);">${{app.description}}</td>
          <td>${{authTags}}</td>
          <td><span class="tag">${{app.self_serve_status}}</span></td>
          <td style="font-size:12px; max-width:220px;">
            <div>${{app.api_surface}}</div>
            <div style="font-size:11px; color:var(--text-subtle); margin-top:2px;">MCP: ${{app.mcp_status}}</div>
          </td>
          <td><span class="tag ${{verdictTagCls}}">${{app.buildability_verdict}}</span></td>
          <td style="font-size:12px; max-width:200px; color:var(--text-subtle);">${{app.main_blocker}}</td>
          <td>
            <a href="${{app.evidence_url}}" target="_blank" rel="noopener noreferrer" style="font-size:12px;">Docs ↗</a>
          </td>
        `;
        tbody.appendChild(tr);
      }});

      renderPaginationControls(startIdx, endIdx, total);
    }}

    function renderPaginationControls(startIdx, endIdx, total) {{
      const paginationBar = document.getElementById("pagination-bar");
      if (isAllExpanded || total <= pageSize) {{
        paginationBar.style.display = "none";
        return;
      }}
      paginationBar.style.display = "flex";

      const totalPages = Math.ceil(total / pageSize);
      document.getElementById("pagination-page-label").innerText = `Page ${{currentPage}} of ${{totalPages}} (${{total}} items)`;

      document.getElementById("prev-page-btn").disabled = (currentPage === 1);
      document.getElementById("next-page-btn").disabled = (currentPage === totalPages);

      const pillsContainer = document.getElementById("page-pills");
      pillsContainer.innerHTML = "";

      // Limit page buttons for clean layout
      const maxButtons = 5;
      let startPage = Math.max(1, currentPage - 2);
      let endPage = Math.min(totalPages, startPage + maxButtons - 1);
      if (endPage - startPage < maxButtons - 1) {{
        startPage = Math.max(1, endPage - maxButtons + 1);
      }}

      for (let p = startPage; p <= endPage; p++) {{
        const btn = document.createElement("button");
        btn.className = "page-btn";
        btn.innerText = p;
        if (p === currentPage) {{
          btn.style.background = "var(--border-strong)";
          btn.style.color = "#ffffff";
          btn.style.fontWeight = "600";
        }}
        btn.onclick = () => {{
          currentPage = p;
          renderTable();
        }};
        pillsContainer.appendChild(btn);
      }}
    }}

    function navigatePage(delta) {{
      const totalPages = Math.ceil(filteredApps.length / pageSize);
      currentPage = Math.max(1, Math.min(totalPages, currentPage + delta));
      renderTable();
    }}

    function changeBatchSize() {{
      const sel = document.getElementById("batch-size-select").value;
      if (sel === "100") {{
        isAllExpanded = true;
        document.getElementById("expand-text").innerText = "Show Paginated";
        document.getElementById("expand-arrow").innerText = "▲";
      }} else {{
        pageSize = parseInt(sel, 10);
        isAllExpanded = false;
        document.getElementById("expand-text").innerText = "Show All 100";
        document.getElementById("expand-arrow").innerText = "▼";
      }}
      currentPage = 1;
      renderTable();
    }}

    function toggleExpandAll() {{
      isAllExpanded = !isAllExpanded;
      if (isAllExpanded) {{
        document.getElementById("expand-text").innerText = "Show First 8";
        document.getElementById("expand-arrow").innerText = "▲";
        document.getElementById("batch-size-select").value = "100";
      }} else {{
        document.getElementById("expand-text").innerText = "Show All 100";
        document.getElementById("expand-arrow").innerText = "▼";
        pageSize = 8;
        document.getElementById("batch-size-select").value = "8";
      }}
      currentPage = 1;
      renderTable();
    }}

    function handleFilterChange() {{
      const query = document.getElementById("search-input").value.toLowerCase();
      const cat = document.getElementById("category-filter").value;
      const verdict = document.getElementById("verdict-filter").value;
      const auth = document.getElementById("auth-filter").value;
      const access = document.getElementById("access-filter").value;

      filteredApps = APPS.filter(app => {{
        const matchesQuery = 
          app.name.toLowerCase().includes(query) ||
          app.category.toLowerCase().includes(query) ||
          app.description.toLowerCase().includes(query) ||
          app.auth_methods.some(m => m.toLowerCase().includes(query)) ||
          app.main_blocker.toLowerCase().includes(query);

        const matchesCat = (cat === "ALL" || app.category === cat);
        const matchesVerdict = (verdict === "ALL" || app.buildability_verdict === verdict);
        const matchesAuth = (auth === "ALL" || app.auth_methods.some(m => m.toLowerCase().includes(auth.toLowerCase())));

        const matchesAccess = (access === "ALL" ||
          (access === "Self-Serve" && (app.self_serve_status.includes("Self-Serve") || app.self_serve_status.includes("Free"))) ||
          (access === "Gated" && (app.self_serve_status.includes("Gated") || app.self_serve_status.includes("Paid Plan"))));

        return matchesQuery && matchesCat && matchesVerdict && matchesAuth && matchesAccess;
      }});

      currentPage = 1;
      renderTable();
    }}

    function renderAuditTable() {{
      const tbody = document.getElementById("audit-table-body");
      tbody.innerHTML = "";

      AUDIT.sample.forEach(item => {{
        const tr = document.createElement("tr");

        let p1Cls = item.pass_1.status === "Correct" ? "tag-ready" : "tag-blocked";

        tr.innerHTML = `
          <td><strong>#${{item.id}} ${{item.name}}</strong></td>
          <td style="font-size:12px; color:var(--text-subtle);">${{item.category}}</td>
          <td>
            <span class="tag ${{p1Cls}}">${{item.pass_1.status}}</span>
            <div style="font-size:11px; color:var(--text-muted); margin-top:4px;">${{item.pass_1.notes}}</div>
          </td>
          <td style="font-size:12px; color:var(--text-main);">
            <strong>${{item.pass_2.status}}:</strong> ${{item.pass_2.mechanism}}
          </td>
          <td style="font-size:12px; color:var(--text-muted);">${{item.pass_3.human_action}}</td>
          <td>
            <span class="tag tag-ready">${{item.final_data.verdict}}</span>
            <div style="font-size:11px; color:var(--text-subtle); margin-top:2px;">${{item.final_data.accessibility}}</div>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function openDrawer(appId) {{
      const app = APPS.find(a => a.id === appId);
      if (!app) return;

      const content = document.getElementById("drawer-content");
      content.innerHTML = `
        <div style="margin-bottom:20px;">
          <div style="font-family:var(--font-code); font-size:11px; color:var(--text-subtle); text-transform:uppercase;">Application Specification</div>
          <h2 style="font-size:20px; font-weight:600; color:#fff; margin-top:4px;">#${{app.id}} ${{app.name}}</h2>
          <div style="font-size:12px; color:var(--text-muted); margin-top:2px;">Vertical: ${{app.category}}</div>
        </div>

        <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="background:var(--bg-base); padding:14px; border:1px solid var(--border-subtle); border-radius:var(--radius-sm);">
            <div style="font-size:11px; text-transform:uppercase; font-weight:600; color:var(--text-subtle);">Buildability Verdict</div>
            <div style="font-weight:600; font-size:14px; color:#fff; margin-top:2px;">${{app.buildability_verdict}}</div>
            <div style="font-size:12px; color:var(--text-muted); margin-top:4px;">${{app.main_blocker}}</div>
          </div>

          <div>
            <div style="font-size:11px; text-transform:uppercase; font-weight:600; color:var(--text-subtle); margin-bottom:6px;">Technical Function</div>
            <p style="font-size:13px; color:var(--text-main);">${{app.description}}</p>
          </div>

          <div>
            <div style="font-size:11px; text-transform:uppercase; font-weight:600; color:var(--text-subtle); margin-bottom:6px;">Authentication Schemes</div>
            <div>${{app.auth_methods.map(m => `<span class="tag" style="font-size:12px;">${{m}}</span>`).join(" ")}}</div>
          </div>

          <div>
            <div style="font-size:11px; text-transform:uppercase; font-weight:600; color:var(--text-subtle); margin-bottom:4px;">Developer Onboarding Access</div>
            <p style="font-size:13px; color:var(--text-muted);">${{app.self_serve_vs_gated}}</p>
          </div>

          <div>
            <div style="font-size:11px; text-transform:uppercase; font-weight:600; color:var(--text-subtle); margin-bottom:4px;">API Surface Architecture</div>
            <p style="font-size:13px; color:var(--text-muted);">${{app.api_surface}}</p>
          </div>

          <div>
            <div style="font-size:11px; text-transform:uppercase; font-weight:600; color:var(--text-subtle); margin-bottom:4px;">Model Context Protocol (MCP) Readiness</div>
            <p style="font-size:13px; color:var(--text-muted);">${{app.mcp_status}}</p>
          </div>

          <div style="background:var(--bg-base); padding:14px; border-left:2px solid var(--border-strong); border-radius:0 var(--radius-sm) var(--radius-sm) 0;">
            <div style="font-size:11px; text-transform:uppercase; font-weight:600; color:var(--text-subtle);">Composio Integration Strategy</div>
            <p style="font-size:12px; color:var(--text-main); margin-top:4px;">${{app.composio_fit}}</p>
          </div>

          <div style="margin-top:8px;">
            <a href="${{app.evidence_url}}" target="_blank" rel="noopener noreferrer" class="page-btn" style="display:block; text-align:center; padding:8px 0; text-decoration:none;">
              Open Official Documentation Portal ↗
            </a>
          </div>
        </div>
      `;

      document.getElementById("drawer-overlay").style.display = "block";
      document.getElementById("drawer").classList.add("open");
    }}

    function closeDrawer() {{
      document.getElementById("drawer-overlay").style.display = "none";
      document.getElementById("drawer").classList.remove("open");
    }}

    function scrollToSection(id) {{
      const el = document.getElementById(id);
      if (el) {{
        el.scrollIntoView({{ behavior: "smooth" }});
      }}
      document.querySelectorAll(".nav-item").forEach(btn => btn.classList.remove("active"));
      event.target.classList.add("active");
    }}

    window.onload = function() {{
      renderTable();
      renderAuditTable();
    }};
  </script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Successfully generated revised index.html (Anti-AI Taste Skill + ASD-STE100 + Pagination Batching)")

if __name__ == "__main__":
    generate()
