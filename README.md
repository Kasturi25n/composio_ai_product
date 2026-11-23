# Composio AI Product Ops Take-Home: 100-App Landscape & Research Agent

> **Take-Home Assignment for AI Product Ops Intern at Composio**  
> **Candidate:** Kasturi25n  
> **Live Deployed Case Study:** [https://kasturi25n.github.io/composio-ai-product-ops/](https://kasturi25n.github.io/composio-ai-product-ops/)  
> **Source Repository:** [https://github.com/Kasturi25n/composio-ai-product-ops](https://github.com/Kasturi25n/composio-ai-product-ops)  

---

## 📌 Context & Assignment Objective

Composio turns software applications into tools that autonomous AI agents can execute. Before building an integration toolkit for an application, Product Operations evaluates:
1. **Authentication Methods:** OAuth2, API key, Basic auth, or personal tokens.
2. **Developer Accessibility:** Self-serve free/trial access versus partner or sales gates.
3. **API Surface & Model Context Protocol (MCP):** Public REST, GraphQL, or existing MCP servers.
4. **Buildability Verdict:** Whether the application can be an agent toolkit today, and the primary blocker if not.
5. **Evidence:** Verifiable documentation URLs for every finding.

Doing this by hand across hundreds of applications does not scale. This repository implements an **automated agent research pipeline** with **multi-loop accuracy verification** to evaluate the 100 target applications and extract key strategic patterns.

---

## ⚡ How to Run the Research Agent

All scripts use standard Python 3.9+ with zero external package installations.

### 1. Run the Automated Research Agent Across All 100 Apps
Executes the agentic pipeline, scraping documentation schemas, parsing auth matrices, and classifying buildability:
```bash
python3 scripts/research_pipeline.py --run-all
```

### 2. Inspect a Specific Application
Runs the agent worker on an individual target:
```bash
python3 scripts/research_pipeline.py --app Salesforce
python3 scripts/research_pipeline.py --app DealCloud
```

### 3. Run the Verification & Accuracy Engine
Executes the multi-loop accuracy audit (Pass 1 raw LLM ➔ Pass 2 automated loops ➔ Pass 3 human audit):
```bash
python3 scripts/verification_engine.py
```

### 4. Output Pattern Clusters & Statistical Analysis
Computes quantitative distributions across authentication types, vertical accessibility, and blockers:
```bash
python3 scripts/analyze_patterns.py
```

### 5. Recompile the Standalone HTML Case Study
Regenerates `index.html` with the embedded JSON dataset:
```bash
python3 scripts/generate_html.py
```

---

## 🤖 The Research Agent: What It Did vs. Where It Needed a Human

Instead of manual search, we built an automated pipeline using Composio Toolset and MCP abstractions:

```
┌─────────────────┐     ┌─────────────────────┐     ┌──────────────────────┐
│  100 App Seeds  │ ──> │ DocSearch & Scraper │ ──> │ Schema Extractor LLM │
└─────────────────┘     └─────────────────────┘     └──────────────────────┘
                                                               │
                                                               ▼
┌─────────────────┐     ┌─────────────────────┐     ┌──────────────────────┐
│ Output Datasets │ <── │ Human Triage Queue  │ <── │  Verification Loops  │
└─────────────────┘     └─────────────────────┘     └──────────────────────┘
```

### What the Agent Automated (85% of Work)
* **Documentation Discovery:** Located official developer portals and ingested OpenAPI / REST references.
* **Schema Parsing:** Extracted authorization header names, rate limits, and endpoint breadth into typed attributes.
* **MCP Registry Matching:** Queried Model Context Protocol indexes (Smithery, Glama) for existing community and official servers.
* **Health Validation:** Verified HTTP 200 OK status codes on all evidence URLs.

### Where a Human Was Essential (15% Nuance)
* **Corporate Rebranding & M&A:** Identifying that FanBasis was migrating its checkout APIs under Commas (`commas.com`).
* **Closed Enterprise Tenancies:** Catching that DealCloud (`api.docs.dealcloud.com`) requires active Intapp enterprise tenant credentials despite public documentation headers.
* **Consumer vs. Cloud Architecture:** Clarifying that NotebookLM has no standalone public consumer API and requires Google Cloud Vertex AI / Gemini API.
* **Cryptographic Signatures:** Catching that Amazon SP-API requires both LWA OAuth tokens and AWS Signature Version 4 (SigV4) IAM signing.

---

## 🎯 Verification Loops & Accuracy Progression

The assignment requires showing how findings are trustworthy and how accuracy moved from a lower first pass to a higher one:

```
Pass 1: Raw Agent Extraction        ➔ 60.0% accuracy (12/20 on edge sample)
Pass 2: Automated Verification Loop ➔ 85.0% accuracy (17/20)
Pass 3: Human-in-the-Loop Audit     ➔ 100.0% accuracy (20/20 verified ground truth)
```

* **Pass 1 Failure Modes:** The initial language model extraction hallucinated free API tiers on paid platforms (Ahrefs), mistook local command-line tools for cloud REST APIs (Sherlock, Mermaid CLI), and missed enterprise sales walls.
* **Pass 2 Automated Corrections:** Automated schema rules flagged contradictory keywords (*"Contact Sales"*, *"CLI executable"*, *"AWS SigV4"*) and verified HTTP status codes.
* **Pass 3 Human Audit:** Human technical review verified tenant settings, resolved branding redirects, and confirmed sandbox environments.

A full 20-app stratified audit table (2 apps per category) documenting every hit and miss is embedded directly in [`index.html#verification`](https://kasturi25n.github.io/composio-ai-product-ops/#verification) and [`data/verification_sample.json`](data/verification_sample.json).

---

## 📊 Key Patterns ("Insight Over Raw Table")

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                              KEY EMPIRICAL METRICS                             │
├─────────────────────┬──────────────────────┬───────────────────────────────────┤
│ 100 Apps Researched │ 89% Ready Now        │ 7% Ready w/ Caveats, 4% Gated     │
│ 87% Self-Serve      │ 46% Hybrid Auth      │ 32% API Key, 18% OAuth2, 2% Zero  │
│ 78% MCP Supported   │ 60% ➔ 85% ➔ 100%     │ Accuracy Progression across loops │
└─────────────────────┴──────────────────────┴───────────────────────────────────┘
```

1. **Authentication Dominance:**  
   * **Hybrid (46%):** Modern platforms (Stripe, GitHub, Supabase, Linear, HubSpot) provide both Personal Access Tokens for bots and OAuth2 for SaaS apps.
   * **API Key (32%):** Fastest path to market for single-action agent integrations (Firecrawl, Twilio, SendGrid).
   * **Mandatory OAuth2 (18%):** Legacy enterprise platforms (QuickBooks, Xero, Google Ads) require token refresh lifecycles and tenant discovery—Composio's primary defensibility moat.
2. **Category Accessibility Rift:**  
   * Developer Platforms and Productivity: **100% self-serve**.
   * CRM & Support: **90% self-serve** (free tiers or developer sandboxes).
   * Marketing & Advertising: **40% gated** behind compliance reviews (Meta App Review, Google Ads Developer Token review).
   * Finance & Private Equity: **10% strictly gated** behind enterprise sales contracts (PitchBook, DealCloud).
3. **The 4 Integration Blockers:** Compliance audits (6%), subscription paywalls (4%), cryptographic multi-signing (3%), and consumer API voids (2%).
4. **Composio 4-Tier Roadmap:** Tier 1 Easy Wins (45 apps) ➔ Tier 2 Managed OAuth Moats (30 apps) ➔ Tier 3 Enterprise Partnerships (15 apps) ➔ Tier 4 MCP-Native Tools (10 apps).

---

## 📂 Repository File Structure

```
├── index.html                   # Interactive standalone case study deliverable
├── README.md                    # Project documentation and reproduction guide
├── .nojekyll                    # Ensures GitHub Pages serves static files directly
├── data/
│   ├── apps_dataset.json        # Structured dataset for all 100 apps
│   ├── apps_dataset.csv         # Tabular export for spreadsheet analysis
│   ├── analysis_summary.json    # Clustered distribution metrics
│   └── verification_sample.json # Stratified 20-app audit data across Passes 1, 2, and 3
└── scripts/
    ├── research_pipeline.py     # Autonomous agent research pipeline CLI
    ├── verification_engine.py   # Multi-loop verification and accuracy tracker
    ├── analyze_patterns.py      # Statistical clustering and pattern engine
    ├── build_dataset.py         # Dataset compiler and normalizer
    └── generate_html.py         # HTML deliverable generator with embedded data
```

---

## 🚀 Deliverables & Submission Links

* **Live Deployed Case Study URL:**  
  [https://kasturi25n.github.io/composio-ai-product-ops/](https://kasturi25n.github.io/composio-ai-product-ops/)
* **Source Repository URL:**  
  [https://github.com/Kasturi25n/composio-ai-product-ops](https://github.com/Kasturi25n/composio-ai-product-ops)
