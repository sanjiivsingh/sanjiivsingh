<!--
Profile README for @sanjiivsingh
Positioning: Azure DevOps / Cloud Platform Engineer | Terraform | CI/CD | DevSecOps
Keep claims tied to repository evidence and clearly distinguish lab/reference work from production delivery.
-->

<div align="center">

<img src="./assets/banner.png" alt="Sanjeev Singh — Azure Cloud & DevOps Engineering" width="100%" />

# Sanjeev Singh

### Azure Cloud & DevOps Engineer
**Infrastructure Automation · Terraform · CI/CD · Azure Platform Engineering · DevSecOps**

<p>
  <a href="https://sanjeevsingh.oneps.in"><img src="https://img.shields.io/badge/Portfolio-OnePS-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/sanjiivsingh"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://sanjeevsingh.oneps.in/#contact"><img src="https://img.shields.io/badge/Contact-Project%20%26%20Role%20Enquiries-16A34A?style=for-the-badge&logo=maildotru&logoColor=white" alt="Contact" /></a>
</p>

**Open to:** Azure DevOps / Cloud Engineering roles · Contract work · Freelance infrastructure projects

</div>

---

## About

I’m a DevOps Engineer focused on **Azure infrastructure automation, Infrastructure as Code, and CI/CD engineering**. I bring a cross-functional background spanning banking operations and IT, with hands-on experience building and maintaining cloud automation workflows.

My engineering work centres on making infrastructure **repeatable, secure, reviewable, and easier to operate**. I work with Terraform modules, environment-specific deployments, remote state, Azure networking and identity, and pipeline quality gates. I’m particularly interested in enterprise platform foundations, landing zones, private connectivity, and secure workload delivery.

I document architecture decisions, implementation steps, validation, and operational considerations so that a project can be understood and maintained by another engineer—not just deployed once.

## What I work on

| Focus area | Practical engineering scope |
|---|---|
| **Azure platform engineering** | Resource groups, VNets, subnets, NSGs, private endpoints, Private DNS, Key Vault, Storage, compute and platform foundations |
| **Infrastructure as Code** | Reusable Terraform modules, input validation, environment composition, state management, drift-aware workflows |
| **CI/CD engineering** | GitHub Actions and Azure DevOps YAML, reusable templates, plan/apply separation, approvals and artifacts |
| **DevSecOps** | TFLint, Checkov, tfsec, Gitleaks, Trivy, policy checks and security scanning in delivery pipelines |
| **Containers & Kubernetes** | Docker, Docker Compose, Kubernetes and Azure Kubernetes Service (AKS) learning/reference implementations |
| **Operations & governance** | Azure Monitor, Log Analytics, runbooks, cost guardrails, tagging and least-privilege access |

## Selected engineering work

These public repositories are the best starting points for reviewing my engineering approach. Each project README describes its scope, architecture, setup, and current verification status. Reference implementations and static validation are labelled as such; they should not be confused with a claim of production deployment.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>01 · Azure Enterprise Landing Zone</h3>
      <a href="https://github.com/sanjiivsingh/azure-enterprise-landing-zone-terraform"><img src="https://img.shields.io/badge/Explore-Repository-0078D4?style=flat-square&logo=github" alt="Explore repository" /></a>
      <p>Terraform reference architecture for a hub-and-spoke network with Azure Firewall, UDRs, VNet peering, Bastion and spoke segmentation.</p>
      <sub>Azure · Terraform · Hub & Spoke · Network Security · GitHub Actions</sub>
    </td>
    <td width="50%" valign="top">
      <h3>02 · Terraform Bootstrap & OIDC</h3>
      <a href="https://github.com/sanjiivsingh/azure-terraform-bootstrap-oidc"><img src="https://img.shields.io/badge/Explore-Repository-0078D4?style=flat-square&logo=github" alt="Explore repository" /></a>
      <p>Remote-state foundation with Azure Blob versioning, soft delete, lease-based locking concepts, Entra federation and passwordless GitHub Actions authentication.</p>
      <sub>Terraform · Azure Storage · Entra ID · OIDC · Identity & Access</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>03 · Azure AKS DevSecOps Pipeline</h3>
      <a href="https://github.com/sanjiivsingh/azure-aks-devsecops-pipeline"><img src="https://img.shields.io/badge/Explore-Repository-0078D4?style=flat-square&logo=github" alt="Explore repository" /></a>
      <p>End-to-end pipeline reference covering secret detection, tests, IaC scanning, container vulnerability scanning and Kubernetes deployment guardrails.</p>
      <sub>GitHub Actions · Terraform · Docker · Trivy · Checkov · AKS</sub>
    </td>
    <td width="50%" valign="top">
      <h3>04 · Azure Resource Module Library</h3>
      <a href="https://github.com/sanjiivsingh/terraform-azure-resource-modules"><img src="https://img.shields.io/badge/Explore-Repository-0078D4?style=flat-square&logo=github" alt="Explore repository" /></a>
      <p>Reusable Terraform child modules for core Azure networking, compute, security and gateway resources, with environment examples.</p>
      <sub>Terraform · AzureRM · Modules · Reusability · Validation</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>05 · Azure Enterprise AI Landing Zone</h3>
      <a href="https://github.com/sanjiivsingh/azure-enterprise-ai-landing-zone-terraform"><img src="https://img.shields.io/badge/Explore-Repository-0078D4?style=flat-square&logo=github" alt="Explore repository" /></a>
      <p>Reference design for private Azure AI services, API Management gateway patterns, AI Search, Key Vault and telemetry.</p>
      <sub>Azure · Terraform · Private Link · API Management · AI Platform</sub>
    </td>
    <td width="50%" valign="top">
      <h3>06 · PropEdge Container Lab</h3>
      <a href="https://github.com/sanjiivsingh/propedge-docker-lab"><img src="https://img.shields.io/badge/Explore-Repository-0078D4?style=flat-square&logo=github" alt="Explore repository" /></a>
      <p>Multi-service container lab with a reverse proxy, backend services, simulator, ingestion worker and isolated PostgreSQL networking.</p>
      <sub>Docker Compose · Python · PostgreSQL · Nginx · Networking</sub>
    </td>
  </tr>
</table>

**More work:** [Terraform Azure Foundation](https://github.com/sanjiivsingh/terraform-azure-foundation) · [Azure Observability Baseline](https://github.com/sanjiivsingh/azure-observability-baseline) · [Azure FinOps Guardrails](https://github.com/sanjiivsingh/azure-finops-guardrails) · [Azure DR Runbooks](https://github.com/sanjiivsingh/azure-dr-runbooks) · [CREP — GitHub repository automation](https://github.com/sanjiivsingh/CREP)

## Technology stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=azure,terraform,githubactions,docker,kubernetes,linux,bash,python,git,postgresql,vscode" alt="Azure, Terraform, GitHub Actions, Docker, Kubernetes, Linux, Bash, Python, Git, PostgreSQL and VS Code" />
</p>

**Cloud & platform:** Microsoft Azure, Azure networking, Azure Storage, Key Vault, Entra ID, Azure Monitor  
**IaC & automation:** Terraform, HCL, Bash, Python  
**CI/CD & security:** GitHub Actions, Azure DevOps Pipelines, TFLint, Checkov, tfsec, Gitleaks, Trivy  
**Containers:** Docker, Docker Compose, Kubernetes, AKS  
**Ways of working:** Git, pull requests, code review, modular design, documentation and iterative delivery

## How I approach delivery

1. **Understand the outcome** — clarify requirements, constraints, ownership, environments and operational needs.
2. **Design before deployment** — document architecture, dependencies, identity, network boundaries and state strategy.
3. **Automate repeatably** — build reusable Terraform modules and parameterised CI/CD workflows.
4. **Validate continuously** — run formatting, validation, linting and security checks before promotion.
5. **Handover responsibly** — provide deployment instructions, evidence, troubleshooting guidance and runbooks.

## Let's work together

I’m interested in opportunities where I can help teams automate Azure infrastructure, improve Terraform practices, build CI/CD pipelines, and strengthen platform security.

- **Employment:** Azure DevOps Engineer · DevOps Engineer · Cloud Infrastructure Engineer
- **Contracts:** Terraform module development · Azure foundations · CI/CD implementation · Pipeline security and automation
- **Portfolio:** [sanjeevsingh.oneps.in](https://sanjeevsingh.oneps.in)
- **LinkedIn:** [linkedin.com/in/sanjiivsingh](https://www.linkedin.com/in/sanjiivsingh)
- **GitHub:** [@sanjiivsingh](https://github.com/sanjiivsingh)

For a project or role enquiry, please reach out through my [portfolio contact page](https://sanjeevsingh.oneps.in/#contact).

---

<div align="center">
  <sub>Building reliable cloud foundations through automation, security and clear engineering practices.</sub>
</div>
