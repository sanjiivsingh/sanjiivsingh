<div align="center">

<!-- Hero Banner (Spotless Light Foundation · Fair Filter Studio Portrait · Zero Dots) -->
<a href="https://sanjeevsingh.oneps.in" target="_blank" rel="noopener noreferrer">
  <img src="./assets/banner.png" alt="Sanjeev Singh - Freelance Azure Cloud Engineer | Terraform & Platform Infrastructure" width="100%">
</a>

<br><br>

<!-- Minimalist Call-to-Action Bar (Clutter-Free, Direct Business Inquiries) -->
<p align="center">
  <a href="https://sanjeevsingh.oneps.in" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/🌐_Portfolio-sanjeevsingh.oneps.in-0078D4?style=for-the-badge&logoColor=white" alt="View Portfolio" />
  </a>
  &nbsp;
  <a href="https://linkedin.com/in/sanjiivsingh" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Connect-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" />
  </a>
  &nbsp;
  <a href="https://github.com/sanjiivsingh?tab=repositories" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Explore-Repositories-0F172A?style=for-the-badge&logo=github&logoColor=white" alt="Explore Repositories" />
  </a>
  &nbsp;
  <a href="mailto:sanjeevsinghred@gmail.com">
    <img src="https://img.shields.io/badge/Discuss_a_Project-sanjeevsinghred@gmail.com-DC2626?style=for-the-badge&logo=gmail&logoColor=white" alt="Discuss a Project" />
  </a>
</p>

<!-- Live Animated Architecture & Status Radar (Dark Colored Typography · Real-Time Cycling) -->
<p align="center">
  <img src="./assets/header-animation.svg" alt="Live Architecture Radar & Consulting Status" width="100%">
</p>

</div>

---

## 🏛️ 1. Executive Summary & Value Proposition

I am an independent **Freelance Azure Cloud Engineer** and **Infrastructure Consultant** with **10+ years of professional engineering and institutional governance experience**, including **5+ years dedicated to Microsoft Azure architecture, modular Terraform IaC, container platforms (AKS), and shift-left DevSecOps automation**.

I partner with seed-to-scale startups, fintech platforms, and engineering leaders to resolve infrastructure reliability, cloud security, and deployment bottlenecks:

* **Eliminating Configuration Drift:** Replacing manual Azure portal operations with 100% code-driven, modular Terraform configurations backed by remote state lease locking in Azure Blob Storage and automated PR validation gates.
* **Enterprise Cloud Foundations (CAF):** Architecting compliant multi-subscription Azure Landing Zones with hierarchical Management Groups, centralized transit Hub-and-Spoke firewalls, and User-Defined Routes (UDR) for default route inspection.
* **Enterprise AI & GenAI Landing Zones:** Designing Zero-Trust perimeters for Generative AI workloads—integrating private Azure OpenAI (GPT-4o), internal API Management as an **AI Gateway** (token rate-limiting, semantic caching), and Azure AI Search for vector RAG grounding.
* **High-Throughput Operational Experience:** Supported infrastructure automation and DevOps operations for a high-volume US-based futures proprietary trading platform, emphasizing low-drift IaC and rapid disaster recovery runbooks.
* **Institutional Governance Heritage:** 4+ years as **Assistant Manager – Banking Operations / Risk & Compliance at State Bank of India (SBI)**. This tenure instilled an authentic background in operational risk controls, least-privilege RBAC, and audit trail integrity that I translate directly into Zero-Trust cloud defense.

---

## 🎯 2. Primary Navigation & Direct Links

| Destination | Purpose | Direct Action |
| :--- | :--- | :---: |
| **Consulting Portfolio** | Case studies, interactive architecture walkthroughs, and live video player | [**sanjeevsingh.oneps.in →**](https://sanjeevsingh.oneps.in) |
| **Featured Projects** | Production-ready Terraform Landing Zones and DevSecOps pipelines | [**Inspect Codebases ↓**](#-4-featured-engineering-projects) |
| **Professional Network** | Connect for consulting inquiries, industry insights, and client references | [**LinkedIn Profile →**](https://linkedin.com/in/sanjiivsingh) |
| **Project Inquiries** | Discuss freelance, contract, or architecture advisory engagements | [**Direct Email →**](mailto:sanjeevsinghred@gmail.com) |

---

## 💼 3. Core Freelance Services & Business Outcomes

<p align="center">
  <img src="./assets/services-matrix.png" alt="Consulting Pillars & Freelance Engagement Sprints" width="100%">
</p>

I provide fixed-price sprint engagements and milestone deliverables with clear business outcomes:

| Consulting Service | Client Problem Solved | Core Deliverables & Business Outcome | Typical Timeline |
| :--- | :--- | :--- | :---: |
| **Azure Landing Zone Foundation (CAF)** | Fragmented subscriptions, uninspected traffic, and manual network provisioning. | • Management Group hierarchy & subscription governance<br>• Central Azure Firewall, Bastion, & GatewaySubnet<br>• Bidirectional VNet peering with UDR `0.0.0.0/0` traffic inspection<br>**Outcome:** Clean, auditable multi-account platform ready for workloads. | **1 – 2 Weeks**<br>(Fixed-Price Sprint) |
| **Enterprise AI & GenAI Private Perimeter** | Exposing proprietary company data to public LLM endpoints without token governance or rate limits. | • Private Azure OpenAI (GPT-4o & text-embedding-3)<br>• Internal APIM AI Gateway (TPM/RPM token rate limiting)<br>• Semantic caching reducing repetitive GenAI prompt costs by up to 40%<br>• Azure AI Search vector database for enterprise RAG grounding<br>**Outcome:** Enterprise-grade GenAI foundation with zero public ingress. | **1 – 2 Weeks**<br>(Fixed-Price Sprint) |
| **Shift-Left DevSecOps & Security Automation** | Security misconfigurations and hardcoded credentials reaching production environments undetected. | • GitHub Actions / Azure DevOps CI/CD with passwordless OIDC auth<br>• Pre-commit linters (**TFLint**, **Gitleaks**) on every PR<br>• Automated IaC security scanning (**Checkov** & **tfsec**)<br>• Container image vulnerability scanning (**Trivy**) & approval gates<br>**Outcome:** Automated security quality gates enforcing policy before deployment. | **2 – 3 Weeks**<br>(Milestone Delivery) |
| **Production Kubernetes (AKS) Enablement** | Unhardened container clusters, node sprawl, and complex ingress configurations. | • Production AKS cluster provisioning via modular Terraform<br>• Microsoft Entra Workload Identity federation<br>• Hardened Pod Security Contexts & default-deny NetworkPolicies<br>• Horizontal Pod Autoscaler (HPA) & minimal distroless container builds<br>**Outcome:** Secure, auto-scaling microservices infrastructure. | **2 – 4 Weeks**<br>(Project Milestone) |

---

## 🌟 4. Featured Engineering Projects

A curated selection of production-grade reference architectures, modular IaC frameworks, and automation tooling:

<table>
<tr>
<td width="50%" valign="top">

### 🤖 [Azure Enterprise AI Landing Zone](https://github.com/sanjiivsingh/azure-enterprise-ai-landing-zone-terraform)
**Production Generative AI & LLM Infrastructure with Terraform**
- **Problem Solved:** Enterprise AI adoption requires strict data boundary governance, token rate limiting, and zero public internet exposure.
- **Engineering Approach:** Zero-Trust architecture provisioning **Azure OpenAI (GPT-4o & text-embedding-3)** mediated through **Azure API Management (APIM)** acting as an AI Gateway with token rate throttling (TPM/RPM), semantic caching, and vector grounding over **Azure AI Search**.
- **Verification Evidence:** Passed Checkov SAST, tfsec, and TFLint validations with `public_network_access_enabled = false` and private DNS zone links. Verified passing GitHub Actions run ID `4043186...`.
- **Stack:** Azure OpenAI · APIM AI Gateway · AI Search Vector RAG · Key Vault · Terraform · OIDC

👉 [**Inspect AI Landing Zone Repository →**](https://github.com/sanjiivsingh/azure-enterprise-ai-landing-zone-terraform)

</td>
<td width="50%" valign="top">

### 🏛️ [Azure Enterprise Hub-and-Spoke Landing Zone](https://github.com/sanjiivsingh/azure-enterprise-landing-zone-terraform)
**Enterprise Cloud Adoption Framework (CAF) Network Mesh**
- **Problem Solved:** Growing organizations need centralized traffic inspection, perimeter protection, and consistent routing between spoke workloads.
- **Engineering Approach:** Modular Terraform provisioning a central transit Hub with **Azure Firewall**, **Azure Bastion**, and hybrid GatewaySubnet. Automated bidirectional VNet peering connects spoke networks with custom **User-Defined Routes (UDRs)** forcing default `0.0.0.0/0` traffic inspection.
- **Verification Evidence:** Validated with TFLint, Checkov CIS Azure Benchmarks, and automated GitHub Actions workflow (`ci-cd.yml`). Verified passing GitHub Actions run ID `4045002...`.
- **Stack:** Azure Firewall · Hub-and-Spoke · UDR Routing · Bastion · VNet Peering · Terraform

👉 [**Inspect Hub-and-Spoke Repository →**](https://github.com/sanjiivsingh/azure-enterprise-landing-zone-terraform)

</td>
</tr>

<tr>
<td width="50%" valign="top">

### 🛡️ [Azure AKS DevSecOps Pipeline](https://github.com/sanjiivsingh/azure-aks-devsecops-pipeline)
**Production CI/CD: Terraform · SonarQube · Trivy · Docker · ACR · AKS**
- **Problem Solved:** Bridging the gap between software delivery and security controls to stop vulnerabilities from reaching production.
- **Engineering Approach:** End-to-end continuous delivery pipeline integrating pre-flight linters, static security analysis (**Checkov** & **tfsec**), container vulnerability scanning (**Trivy**), minimal distroless builds, and automated rolling deployments to **Azure Kubernetes Service (AKS)** with default-deny network policies.
- **Verification Evidence:** Integrated GitHub Actions workflow enforcing strict quality gates and manual sign-offs. Verified passing GitHub Actions run ID `4019564...`.
- **Stack:** Azure AKS · Docker · ACR · Trivy · Checkov · SonarQube · Terraform · GitHub Actions

👉 [**Inspect DevSecOps Pipeline Repository →**](https://github.com/sanjiivsingh/azure-aks-devsecops-pipeline)

</td>
<td width="50%" valign="top">

### 📦 [Terraform Azure Reusable Resource Modules](https://github.com/sanjiivsingh/terraform-azure-resource-modules)
**Enterprise Multi-Tier Azure IaC Child-Module Library**
- **Problem Solved:** Code duplication, hardcoded configurations, and state collisions across multi-environment deployments.
- **Engineering Approach:** Engineered 11+ independent, enterprise-grade child modules (Resource Group, VNet, Subnet, NSG, Public IP, NIC, Linux VM, Bastion, Key Vault, and Application Gateway) architected for implicit dependency resolution and multi-environment decoupling.
- **Verification Evidence:** Automated GitHub Actions pipeline validating formatting (`terraform fmt`), syntax, and plan generation on every PR.
- **Stack:** Terraform 1.9+ · AzureRM Provider · Modular IaC · Key Vault · App Gateway · CI/CD

👉 [**Inspect Reusable Modules Repository →**](https://github.com/sanjiivsingh/terraform-azure-resource-modules)

</td>
</tr>

<tr>
<td width="50%" valign="top">

### ⚡ [PropEdge Trading Platform Infrastructure Lab](https://github.com/sanjiivsingh/propedge-docker-lab)
**High-Concurrency Multi-Tier Containerized Workload Deployment**
- **Problem Solved:** Operating a high-throughput financial trading application requiring private service networking and zero exposed public database ports.
- **Engineering Approach:** Multi-container stack orchestrated via Docker Compose with segregated bridge networks separating the React frontend, FastAPI backend, and PostgreSQL database on hardened Azure Virtual Machines, fronted securely by Cloudflare Tunnel.
- **Verification Evidence:** Verified private network isolation, persistent database volume leasing, and automated container lifecycle scripts.
- **Stack:** Azure VMs · Docker Compose · FastAPI · PostgreSQL · React · Cloudflare Tunnel

👉 [**Inspect PropEdge Trading Lab →**](https://github.com/sanjiivsingh/propedge-docker-lab)

</td>
<td width="50%" valign="top">

### 🛠️ [CREP — Code Repository Environment Provisioner](https://github.com/sanjiivsingh/CREP)
**CLI Tool for Standardized Git & GitHub Lifecycle Automation**
- **Problem Solved:** Inconsistent repository bootstrapping, missing branch protection rules, and manual configuration overhead across teams.
- **Engineering Approach:** Developed a modular Bash command-line utility automating repository provisioning, visibility toggling, `.gitignore` templating, and remote Git synchronization via the GitHub CLI (`gh`).
- **Verification Evidence:** Built with modular sub-command architecture, comprehensive error trapping, 20+ automated unit tests (`tests/test_runner.sh`), ShellCheck static analysis, and multi-OS CI matrix.
- **Stack:** Bash · GitHub CLI · Git · ShellCheck · CI Automation

👉 [**Inspect CREP Provisioner Repository →**](https://github.com/sanjiivsingh/CREP)

</td>
</tr>
</table>

---

## 📐 5. Architecture & Delivery Workflow Visuals

### 1. Enterprise AI & GenAI Landing Zone Architecture

A production Zero-Trust blueprint for private Generative AI workloads with API Management AI Gateway governance and vector RAG grounding:

```mermaid
flowchart LR
    subgraph Client["💻 Application Tier"]
        APP[Enterprise Apps / Microservices]
    end

    subgraph Gateway["⚡ AI Gateway (Azure APIM Internal)"]
        AUTH[Managed Identity Token Auth]
        THROTTLE[TPM / RPM Token Throttling]
        CACHE[Semantic Response Cache]
        FAILOVER[Multi-Region Model Failover]
    end

    subgraph AIWorkload["🧠 Private AI Workload Perimeter"]
        OAI[Azure OpenAI Service\nGPT-4o & text-embedding-3]
        SEARCH[Azure AI Search\nVector Store & RAG Reranker]
        LAKE[Data Lake Storage Gen2\nGrounding Knowledge Base]
        KV[Azure Key Vault HSM\nCMK Encryption & Secrets]
    end

    APP -->|Private VNet Link| AUTH
    AUTH --> THROTTLE --> CACHE --> FAILOVER
    FAILOVER -->|Private Endpoint| OAI
    FAILOVER -->|Context Retrieval| SEARCH
    SEARCH -->|Grounding Chunks| LAKE
    KV -.->|Hardware Secrets| OAI

    style Client fill:#0f172a,stroke:#38bdf8,stroke-width:1.5px,color:#fff
    style Gateway fill:#1e1b4b,stroke:#818cf8,stroke-width:1.5px,color:#fff
    style AIWorkload fill:#064e3b,stroke:#10b981,stroke-width:1.5px,color:#fff
    style OAI fill:#082f49,stroke:#38bdf8,stroke-width:1.5px,color:#fff
```

### 2. Automated Shift-Left DevSecOps Delivery Gates

<p align="center">
  <img src="./assets/devsecops-gates.png" alt="Automated Shift-Left DevSecOps Delivery Gates" width="100%">
</p>

### 3. End-to-End DevSecOps Pipeline Flow Diagram

Security controls are embedded directly into every stage of the infrastructure and container delivery lifecycle:

<p align="center">
  <img src="./assets/devsecops-pipeline.svg" alt="Enterprise DevSecOps Pipeline Architecture" width="100%">
</p>

### 4. Interactive Video Walkthrough & Platform Architecture Reel

A visual demonstration of enterprise Azure architecture patterns, container delivery, and security scanning:

<div align="center">

<p align="center">
  <a href="https://sanjeevsingh.oneps.in" target="_blank" rel="noopener noreferrer">
    <img src="./assets/intro_preview.webp" alt="Platform Architecture Reel" width="85%" style="border-radius: 12px; border: 1px solid rgba(226, 232, 240, 0.8);">
  </a>
</p>

<p align="center">
  <a href="https://sanjeevsingh.oneps.in" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/▶_Launch_Interactive_Player-sanjeevsingh.oneps.in-0078D4?style=for-the-badge&logoColor=white" alt="Live Player" />
  </a>
  &nbsp;
  <a href="./assets/intro.mp4" target="_blank">
    <img src="https://img.shields.io/badge/🎬_Stream_1080p_Video-Local_MP4-10B981?style=for-the-badge&logoColor=white" alt="Stream MP4" />
  </a>
  &nbsp;
  <a href="https://github.com/sanjiivsingh" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/GitHub-Repository_Source-0F172A?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

</div>

---

## 🧰 6. Technical Skills & Core Competencies

| Domain | Verified Technologies & Practical Specialization |
| :--- | :--- |
| **Cloud Platforms** | **Microsoft Azure** (Enterprise Cloud Adoption Framework, Multi-Subscription Governance, Management Groups, Resource Hierarchies) |
| **Infrastructure as Code** | **Terraform (1.9+)**, OpenTofu, Reusable Child Modules, Azure Blob Remote State with Lease Locking, Dynamic Blocks, Strict Input Validation |
| **CI/CD & Automation** | **GitHub Actions**, **Azure DevOps Pipelines**, Passwordless Azure OIDC Workload Identity Federation, Automated Plan/Apply, Approval Gates |
| **DevSecOps & SAST** | **Checkov**, **tfsec**, **TFLint**, **Trivy** (Container Scanning), **Gitleaks**, **SonarQube**, Azure Key Vault HSM & CMK, CIS Azure Benchmarks |
| **Containers & Kubernetes** | **Docker**, **Docker Compose**, **Azure Kubernetes Service (AKS)**, Azure Container Registry (ACR), Helm, Workload Identity, K8s NetworkPolicies |
| **Cloud Networking & Security** | Hub-and-Spoke VNets, **Azure Firewall**, **Azure Bastion**, User-Defined Routes (UDR), **Private Endpoints**, **Private DNS Zones**, NSG Micro-segmentation |
| **Observability & Operations** | **Azure Monitor**, **Log Analytics Workspaces**, Application Insights, KQL (Kusto Query Language), Alerts & Action Groups, FinOps Cost Governance |
| **Scripting & Tooling** | Linux Administration, **Bash Shell Scripting**, **Python**, ShellCheck, Git, GitHub CLI (`gh`) |

---

## 📖 7. Selected Technical Articles & Architecture Guides

Deep-dive architectural documentation written from hands-on infrastructure engineering lessons:

* 📄 **[Storage Account Implicit Dependency Architecture](https://github.com/sanjiivsingh/terraform-azure-foundation/blob/main/docs/architecture/storage-account-implicit-dependency.md)**  
  *Eliminating manual `depends_on` anti-patterns in Terraform by designing clean output-to-input local value transformation pipelines for automated graph sequencing.*
* 📄 **[Reusable Terraform Child-Module Design Standards](https://github.com/sanjiivsingh/terraform-azure-foundation/blob/main/docs/architecture/module-design-principles.md)**  
  *Enterprise standards for input maps, optional attribute schemas, standardized output maps, and predictable resource naming.*
* 📄 **[Architecture Decision Record: CI & Main Branch Governance (ADR-001)](https://github.com/sanjiivsingh/CREP/blob/main/docs/adr/ADR-001-ci-and-main-branch-governance.md)**  
  *Designing automated pull request validation gates, branch protection baselines, and semantic release tagging.*
* 📄 **[Zero-Trust Private Endpoints & DNS Resolution Guide](https://github.com/sanjiivsingh/azure-landing-zone-private-networking/blob/main/docs/architecture.md)**  
  *Establishing private PaaS perimeters and preventing split-brain DNS resolution across multi-spoke Azure networks.*
* 📄 **[Shift-Left DevSecOps: Policy-as-Code with Checkov & Trivy](https://github.com/sanjiivsingh/azure-aks-devsecops-pipeline#readme)**  
  *Implementing automated security checks directly inside CI/CD workflows to catch vulnerabilities before infrastructure provisioning.*

---

## 💼 8. Career History & Institutional Governance Heritage

```text
├── FREELANCE / CONTRACT CLOUD & DEVSECOPS ENGINEER (2021 – Present)
│   ├── Multiple Enterprise Client Engagements | Gurugram, India
│   └── High-Throughput US Futures Proprietary Trading Platform
│       ├── Supported Azure infrastructure automation & DevOps for a high-volume platform
│       ├── Engineered modular Terraform modules for networking, compute, Key Vault, and AKS
│       ├── Implemented DevSecOps pipelines with Checkov, tfsec, TFLint, Trivy, and Gitleaks
│       └── Centralized Terraform remote state backend in Azure Storage with automated locking
│
└── STATE BANK OF INDIA (2012 – 2016)
    └── Assistant Manager – Banking Operations / Risk & Compliance
        ├── Managed banking operations involving operational risk controls, audit & regulatory compliance
        ├── Supervised dual-control access authorization processes for high-value financial transactions
        └── Established the institutional risk-management and zero-trust mindset applied to Cloud Security today
```

### 🎓 Verified Education & Professional Recognition
* **Google AI Essentials** — Google (2025)
* **DevSecOps Initiative Award** — Engineering Recognition (2023)
* **JAIIB** — Indian Institute of Banking & Finance (2014)
* **Spotlight Award (Operational Excellence)** — State Bank of India (2015)
* **Bachelor of Computer Applications (BCA)** — Indira Gandhi National Open University (IGNOU, 2009)

---

## 🤝 9. Discuss a Project / Professional Contact

Whether you need to architect **Enterprise Azure Landing Zones**, adopt **Modular Terraform Infrastructure as Code**, harden **Kubernetes (AKS)** workloads, or establish **Shift-Left DevSecOps Pipelines**, I am available for high-impact freelance consulting and client engagements.

<div align="center">

<p align="center">
  <a href="mailto:sanjeevsinghred@gmail.com">
    <img src="./assets/footer.png" alt="Let's Build Reliable Cloud Platforms Together - Sanjeev Singh" width="100%">
  </a>
</p>

<p align="center">
  <a href="mailto:sanjeevsinghred@gmail.com">
    <img src="https://img.shields.io/badge/Email-sanjeevsinghred@gmail.com-DC2626?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  &nbsp;
  <a href="https://linkedin.com/in/sanjiivsingh" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/LinkedIn-sanjiivsingh-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  &nbsp;
  <a href="https://github.com/sanjiivsingh" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/GitHub-sanjiivsingh-0F172A?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  &nbsp;
  <a href="https://sanjeevsingh.oneps.in" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Portfolio-sanjeevsingh.oneps.in-0078D4?style=for-the-badge&logoColor=white" alt="Website" />
  </a>
</p>

</div>
