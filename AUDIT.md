# Technical Audit Report: GitHub Account @sanjiivsingh

**Auditor:** Senior Azure Cloud, Terraform & DevSecOps Architecture Lead  
**Evaluation Date:** October 30, 2026  
**Target Profile:** `https://github.com/sanjiivsingh`  
**Guiding Principle:** Truth over polish. Zero fabricated evidence, zero unverified metrics.

---

## 1. Executive Summary & Verification Matrix

| Category | Total Checked | Verified (Truth) | Partly Verified | False / Unverified (Action Needed) |
| :--- | :---: | :---: | :---: | :---: |
| **Profile Claims & Metrics** | 18 | 9 | 4 | 5 (Must remove/relabel) |
| **Repository Code vs Text** | 6 featured | 2 | 2 | 2 (Major mismatches in AKS & AI LZ) |
| **Public Repositories** | 24 | 13 (Keep/Refactor) | 3 (Flagged) | 8 (Propose Archive / Delete) |
| **Documentation & External Links** | 22 | 20 | 2 (Truncated IDs) | 0 (Zero 404s) |

---

## 2. Public Repository Audit (All 24 Public Repositories)

| # | Repository Name | Primary Tech | Purpose & Assessment | CI Workflow Status | License | Recommendation |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **`sanjiivsingh`** | Markdown / Python | GitHub Profile README & automated stats generation. | ✅ Passing (`snake.yml`) | None | **Keep & Optimize** (Rewrite to <250 lines) |
| 2 | **`azure-enterprise-ai-landing-zone-terraform`** | Terraform (HCL) | GenAI landing zone (APIM AI Gateway, Azure OpenAI, Vector RAG, Key Vault). | ✅ Passing (`40450338890`) | MIT | **Keep (Featured #1)** (Fix claims on HSM, 40% savings) |
| 3 | **`azure-enterprise-landing-zone-terraform`** | Terraform (HCL) | CAF Hub-and-Spoke transit network mesh, Azure Firewall, Bastion, UDR. | ✅ Passing (`40450305601`) | MIT | **Keep (Featured #2)** (Reconcile FW SKU, add 2nd spoke) |
| 4 | **`azure-aks-devsecops-pipeline`** | Terraform / Python | CI/CD pipeline for containerized microservice on AKS. | ✅ Passing (`40195648287`) | MIT | **Keep (Featured #3)** (Add Gitleaks/SonarQube or align text) |
| 5 | **`terraform-azure-resource-modules`** | Terraform (HCL) | Enterprise library of 11+ reusable child modules. | ❌ Failing (Old OIDC PR) | MIT | **Keep (Featured #4)** (Fix CI to test syntax/validation) |
| 6 | **`azure-landing-zone-governance`** | Terraform (HCL) | Azure Policy as Code definitions, initiatives, compliance guardrails. | ✅ Passing (`40440582416`) | MIT | **Keep (Featured #5)** (Promote to flagship governance) |
| 7 | **`CREP`** | Bash / Shell | Code Repository Environment Provisioner CLI automation tool. | ✅ Passing (`CREP CI`) | MIT | **Keep** (Strong evidence of Linux/Git automation) |
| 8 | **`propedge-docker-lab`** | Docker / Compose | Multi-tier containerized trading platform lab. | ✅ Passing (`Docker CI`) | None | **Keep** (Add MIT license) |
| 9 | **`azure-landing-zone-enterprise`** | Terraform (HCL) | Platform landing zone (Management Group hierarchy, subscription vending). | ✅ Passing | MIT | **Keep** (Module for enterprise governance) |
| 10 | **`azure-landing-zone-private-networking`** | Terraform (HCL) | Zero-trust private endpoints and private DNS zone automation. | ✅ Passing | MIT | **Keep** (Referenced in architecture guides) |
| 11 | **`azure-landing-zone-management`** | Terraform (HCL) | Centralized Log Analytics, Azure Monitor diagnostic settings, alerts. | ✅ Passing | MIT | **Keep** (Observability baseline) |
| 12 | **`terraform-azure-foundation`** | Terraform (HCL) | Foundational reusable modules and ADR architectural documentation. | ✅ Passing | MIT | **Keep** (Holds deep-dive technical articles) |
| 13 | **`workflow-tutorial`** | GitHub Actions | Educational tutorial repository for GitHub Actions primitives. | ✅ Passing | MIT | **Keep** (Reference learning repo) |
| 14 | **`workflow-basic-1`** | Terraform / Actions | Basic Terraform GitHub Actions pipeline demo. | ✅ Passing | MIT | **Keep** (Hands-on CI/CD experiment) |
| 15 | **`azure-landing-zone-hub-spoke`** | Terraform (HCL) | Standalone hub-and-spoke module. | ❌ Failing (`validate`) | MIT | **Consolidate** into `azure-enterprise-landing-zone-terraform` |
| 16 | **`docker-learning`** | HTML / Docker | Early container learning notes. | ⚠️ No CI | None | **Keep as Learning / Mark as Archive** |
| 17 | **`azure-generic-child-modules`** | Terraform (HCL) | Older duplicate of child modules. | ❌ Failing | MIT | **Propose Archive** (Superseded by `terraform-azure-resource-modules`) |
| 18 | **`terraform-generic-modules-azure`** | Terraform (HCL) | Older duplicate of generic modules. | ⚠️ No CI | None | **Propose Archive** (Superseded by `terraform-azure-foundation`) |
| 19 | **`github-actions-login-demo`** | Actions / HCL | 0-byte README, failing CI. | ❌ Failing | None | **Propose Archive / Delete** (Embarrassing empty repo) |
| 20 | **`github-actions-jobs`** | GitHub Actions | Workflow job orchestration demo. | ⚠️ Cancelled | None | **Propose Archive** (Superseded by `workflow-tutorial`) |
| 21 | **`terraform-github-actions-demo-2`** | Terraform / Actions | Early experiment with PR comments. | ✅ Passing | None | **Propose Archive** (Superseded by `workflow-basic-1`) |
| 22 | **`terraform-github-actions-demo-1`** | Terraform / Actions | Early experiment with failing apply. | ❌ Failing | None | **Propose Archive** (Superseded by `workflow-basic-1`) |
| 23 | **`azure-terraform-modular-vm-lab`** | Terraform (HCL) | Basic VM lab without automated tests. | ⚠️ No CI | None | **Propose Archive** (Superseded by landing zones) |
| 24 | **`terraform-azurerm-resource-group`** | Terraform (HCL) | 1-resource module from May 2026. | ⚠️ No CI | None | **Propose Archive** (Trivial single-resource module) |

---

## 3. Profile README Link Audit

| Target Link in Profile | HTTP Status | Code / Asset Exists | Notes |
| :--- | :---: | :---: | :--- |
| `https://sanjeevsingh.oneps.in` | 200 OK | Verified | Active live consulting portfolio. |
| `https://linkedin.com/in/sanjiivsingh` | 200 OK | Verified | Active LinkedIn profile. |
| `https://github.com/sanjiivsingh` | 200 OK | Verified | Active GitHub profile. |
| `./assets/banner.png` | Local File | Verified (209.2 KB) | Clean studio portrait banner. |
| `./assets/header-animation.svg` | Local File | Verified (5.1 KB) | Animated SVG status radar. |
| `./assets/intro_preview.webp` | Local File | Verified (1.9 MB) | Video walkthrough preview image. |
| `./assets/introduction.mp4` | Local File | Verified (14.3 MB) | 40-second introduction video. |
| `./assets/project-ai-landing-zone.png` | Local File | Verified (77.6 KB) | Architecture diagram card. |
| `./assets/project-hub-spoke.png` | Local File | Verified (81.4 KB) | Hub-spoke diagram card. |
| `./assets/project-devsecops.png` | Local File | Verified (47.4 KB) | DevSecOps diagram card. |
| `./assets/project-terraform-modules.png`| Local File | Verified (60.8 KB) | Reusable modules card. |
| `./assets/devsecops-pipeline.svg` | Local File | Verified (13.0 KB) | Animated pipeline graphic. |
| `./assets/snake.svg` | Local File | Verified (27.2 KB) | Animated contribution snake. |
| `terraform-azure-foundation/.../storage-account-implicit-dependency.md` | 200 OK | Verified | Architecture article exists. |
| `terraform-azure-foundation/.../module-design-principles.md` | 200 OK | Verified | Architecture article exists. |
| `CREP/.../ADR-001-ci-and-main-branch-governance.md` | 200 OK | Verified | ADR article exists. |
| `azure-landing-zone-private-networking/.../architecture.md` | 200 OK | Verified | Architecture guide exists. |
| `azure-aks-devsecops-pipeline#readme` | 200 OK | Verified | Repository README exists. |
| Truncated Run ID `4043186...` | Ambiguous | Matched `40431864943` | Must replace with full clickable link. |
| Truncated Run ID `4045002...` | Ambiguous | Matched `40450027709` | Must replace with full clickable link. |
| Truncated Run ID `4019564...` | Ambiguous | Matched `40195648287` | Must replace with full clickable link. |

---

## 4. Claim vs. Reality Code Audit (Line-by-Line)

### A. Repository: `azure-enterprise-landing-zone-terraform`
* **Claim 1:** "Azure Firewall Premium \n Central 0.0.0.0/0 Inspection" (Profile README Line 223)  
  * **Evidence:** `modules/hub_network/main.tf` Lines 43-44: `sku_name = "AZFW_VNet"`, `sku_tier = "Standard"`.  
  * **Verdict:** ❌ **FALSE**. Standard SKU is deployed in code, not Premium.
* **Claim 2:** "TLS 1.3 Inspection" (Repo README Line 29)  
  * **Evidence:** `modules/hub_network/main.tf`: No TLS inspection certificate or policy configured. Standard SKU cannot perform TLS termination.  
  * **Verdict:** ❌ **FALSE**. Must remove TLS 1.3 claim.
* **Claim 3:** "Cross-Spoke (East-West) Traffic Inspection" (Repo README Line 43)  
  * **Evidence:** `environments/dev/main.tf` Lines 33-42: Only a single spoke (`module "spoke"`) is instantiated. Spoke-to-spoke routing is not implemented.  
  * **Verdict:** ❌ **FALSE**. Must add a second spoke (`module "spoke_b"`) or remove east-west inspection claim.
* **Claim 4:** "Forced to Azure Firewall's private IP (10.0.1.4)" (Repo README Line 133)  
  * **Evidence:** While `modules/hub_network/outputs.tf` outputs `firewall_private_ip`, docs still cite the hardcoded `10.0.1.4`.  
  * **Verdict:** ⚠️ **PARTLY VERIFIED**. Code uses module output; docs must remove the hardcoded IP reference.
* **Claim 5:** "Tagged Release: v1.0.0" (Repo README Line 144)  
  * **Evidence:** `gh release list --repo sanjiivsingh/azure-enterprise-landing-zone-terraform` returns 0 releases.  
  * **Verdict:** ❌ **FALSE**. No tag or release exists.
* **Claim 6:** Authentication via Service Principal Secret  
  * **Evidence:** `README.md` Line 55 cites `ARM_CLIENT_SECRET`.  
  * **Verdict:** ⚠️ **PARTLY VERIFIED**. Must replace with passwordless GitHub OIDC.

### B. Repository: `azure-aks-devsecops-pipeline`
* **Claim 1:** "Production CI/CD: Terraform · SonarQube · Checkov · Trivy · Docker · ACR · AKS" (Profile Line 136)  
  * **Evidence:** `.github/workflows/devsecops-pipeline.yml`: Does NOT run SonarQube, does NOT run Gitleaks, does NOT push to ACR, does NOT deploy to AKS.  
  * **Verdict:** ❌ **FALSE**. Workflow only runs unit tests, Checkov/tfsec with `soft_fail: true`, and Trivy with `exit-code: 0`.
* **Claim 2:** "Automated IaC security scanning (Checkov & tfsec)"  
  * **Evidence:** `devsecops-pipeline.yml` Lines 59 & 65: `soft_fail: true`.  
  * **Verdict:** ⚠️ **PARTLY VERIFIED**. Scanners run but do not fail on HIGH/CRITICAL findings. Must set strict exit codes.
* **Claim 3:** "Kubernetes (AKS) Deployment"  
  * **Evidence:** Only local `docker build` occurs. No Azure CLI login, no Terraform apply, no `kubectl apply` step in CI.  
  * **Verdict:** ❌ **FALSE**. Needs a real automated deployment job or must be relabeled as "Static Validation & Quality Gate Pipeline".

### C. Repository: `azure-enterprise-ai-landing-zone-terraform`
* **Claim 1:** "Semantic response cache reducing prompt costs by up to 40%" (Profile Line 89, 111)  
  * **Evidence:** `modules/ai_gateway_apim/policies/ai-gateway-policy.xml` Line 10 contains `<azure-openai-semantic-cache-lookup>`, but `modules/ai_gateway_apim/main.tf` never provisions Azure Cache for Redis or attaches the policy. No benchmark or empirical cost reduction calculation exists.  
  * **Verdict:** ❌ **FALSE**. 40% cost reduction is an unverified speculative claim.
* **Claim 2:** "Key Vault HSM FIPS 140-2 Level 3" (Profile Line 113 & Asset Card)  
  * **Evidence:** `modules/key_vault/main.tf` Line 11: `sku_name = "standard"`.  
  * **Verdict:** ❌ **FALSE**. Standard Key Vault uses software multi-tenant key isolation, not hardware HSM. Must rephrase to Standard Key Vault CMK.
* **Claim 3:** "Token Rate Limiting (TPM/RPM)"  
  * **Evidence:** XML policy file defines `<azure-openai-token-limit>`, but is not hooked to APIM via `azurerm_api_management_policy`.  
  * **Verdict:** ⚠️ **PARTLY VERIFIED**. Policy XML exists but is disconnected from the Terraform resource lifecycle.

### D. Repository: `terraform-azure-resource-modules`
* **Claim 1:** "CI-Validated Component Library"  
  * **Evidence:** The only CI run on GitHub Actions failed due to invalid `actions/checkout@v6` and missing OIDC credentials on PR.  
  * **Verdict:** ❌ **FALSE**. CI is currently red. Must fix workflow to perform linting, format check, and `terraform validate` cleanly without requiring live Azure credentials.

### E. Profile README: `sanjiivsingh/sanjiivsingh`
* **Claim 1:** "10+ years of professional engineering experience"  
  * **Evidence:** Career history details 2012-2016 at State Bank of India (banking operations, operational risk) and 2021-present (freelance cloud & DevSecOps).  
  * **Verdict:** ⚠️ **PARTLY VERIFIED**. True calendar span across banking risk & cloud, but must clearly distinguish 5+ years dedicated to Azure/DevOps from 4+ years institutional banking operations.
* **Claim 2:** Personal Email Exposure  
  * **Evidence:** `sanjeevsinghred@gmail.com` is committed in plaintext across `README.md` and Terraform `common_tags`.  
  * **Verdict:** ⚠️ **RULE VIOLATION**. Must replace with contact links / GitHub issues to prevent scraping.

