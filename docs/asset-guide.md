# Visual Asset Guide & Media Inventory

**Repository:** `sanjiivsingh/sanjiivsingh`  
**Maintainer:** Sanjeev Singh (`@sanjiivsingh`)  
**Design Theme:** Premium Minimalist Light Architecture (White/Light Foundation, Charcoal Typography, Red & Green Accents, Zero Dots)

---

## 1. Primary Profile Assets

| Asset Name | Relative Path | File Format | Dimensions / Size | Source / Creation Method | Intended Use & Placement |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Hero Banner** | `assets/banner.png` | PNG | 1200 × 420 px (~209 KB) | Custom Python PIL compositor using authentic studio portrait (`profile.png`), status indicator, and domain badges. Pure light background with **zero dots**. | Top of GitHub profile README. Represents primary personal brand and value proposition. |
| **Hero Banner (Master)** | `assets/banner-light.png` | PNG | 1200 × 420 px (~209 KB) | Identical high-resolution light-theme master. | Static fallback and high-DPI display asset. |
| **Live Header Animation** | `assets/header-animation.svg` | SVG | Scalable Vector (~5.1 KB) | Pure CSS-animated live radar card featuring real-time pulse beacon, stream progress bar, and 4 scannable specialization pillars. Zero text collision bugs. | Top header section directly under contact buttons. |
| **Consulting Services Matrix** | `assets/services-matrix.png` | PNG | 1200 × 330 px (~42 KB) | 4-column modular infographic card highlighting consulting pillars (Azure CAF, GenAI, DevSecOps, AKS Platform). | Section 3: Core Freelance Services & Business Outcomes. |
| **DevSecOps Quality Gates** | `assets/devsecops-gates.png` | PNG | 1200 × 250 px (~31 KB) | 6-stage shift-left security verification gates card with geometric checkmarks. | Section 5: Automated Shift-Left DevSecOps Delivery Gates. |
| **AI Landing Zone Thumbnail** | `assets/project-ai-landing-zone.png` | PNG | 960 × 540 px 16:9 (~79 KB) | High-DPI architecture visual for Azure OpenAI, APIM AI Gateway, and Vector RAG Grounding with verified CI badge. | Section 4: Featured Engineering Projects. |
| **Hub-and-Spoke Thumbnail** | `assets/project-hub-spoke.png` | PNG | 960 × 540 px 16:9 (~86 KB) | High-DPI network architecture visual for Azure Firewall, Bastion, and UDR 0.0.0.0/0 route inspection. | Section 4: Featured Engineering Projects. |
| **DevSecOps Pipeline Thumbnail** | `assets/project-devsecops.png` | PNG | 960 × 540 px 16:9 (~59 KB) | High-DPI workflow visual for Checkov SAST, TFLint, Trivy container CVE scanning, and AKS deployments. | Section 4: Featured Engineering Projects. |
| **Terraform Modules Thumbnail** | `assets/project-terraform-modules.png` | PNG | 960 × 540 px 16:9 (~81 KB) | High-DPI architecture visual for 11+ reusable child modules with implicit dependency resolution. | Section 4: Featured Engineering Projects. |
| **Architecture Pillars** | `assets/architecture-pillars.png` | PNG | 1200 × 280 px (~39 KB) | 4-column production standards card (100% Code-Driven, Zero-Trust, Governance, Resilience). | Reference asset for engineering standards. |
| **Profile Photograph** | `assets/profile.png` | PNG | 1086 × 1448 px (747 KB) | Original authentic studio portrait of Sanjeev Singh in formal business attire. | Base image for composite header banners, portfolio avatars, and media previews. |
| **DevSecOps Pipeline Diagram** | `assets/devsecops-pipeline.svg` | SVG | Scalable Vector (13.0 KB) | Hand-crafted light-foundation vector graphic with CSS dash-stream flow animations and status indicators. | Section 5: DevSecOps pipeline visualization inside README. |
| **Platform Video Preview** | `assets/intro_preview.webp` | WebP | 960 × 540 px 16:9 (27.5 KB) | High-DPI 16:9 video player poster card with centered play indicator. Optimized from 5.9 MB (99.5% reduction). | Section 5: Video reel poster image linking to portfolio video player and MP4 stream. |
| **Platform Video Reel** | `assets/intro.mp4` | MP4 | 1080p HD (13.0 MB) | Master video recording featuring platform architecture overview. | Linked direct media file for high-bandwidth client streaming. |
| **Footer Contact Banner** | `assets/footer.png` | PNG | 1200 × 260 px (~20 KB) | Custom Python PIL composition with 4 modular contact cards (Email, LinkedIn, GitHub, Portfolio). Zero dots. | Bottom of README as a cohesive professional closing invitation. |
| **Contribution Grid Snake** | `assets/snake.svg` | SVG | Scalable Vector (27.2 KB) | GitHub Actions automated contribution graph animation generator. | Profile activity and continuous engineering proof. |

---

## 2. Architecture Visuals Across Portfolio Repositories

| Repository | Diagram Path / Asset | Diagram Type | Description |
| :--- | :--- | :---: | :--- |
| `azure-enterprise-ai-landing-zone-terraform` | `architectures/ai-landing-zone-architecture.svg` | SVG + Mermaid | Zero-Trust Azure OpenAI, APIM AI Gateway, and Azure AI Search Vector RAG architecture. |
| `azure-landing-zone-enterprise` | `docs/architecture.md` | Mermaid | Multi-tier Management Group hierarchy (Platform, Workloads, Sandboxes) and RBAC inheritance. |
| `azure-landing-zone-hub-spoke` | `docs/architecture.md` | Mermaid | Hub-and-Spoke topology with Azure Firewall inspection and UDR default route tunneling. |
| `azure-landing-zone-private-networking` | `docs/architecture.md` | Mermaid | Private Endpoint, Private DNS Zone, and micro-segmentation flow. |
| `azure-landing-zone-management` | `docs/architecture.md` | Mermaid | Central Log Analytics workspace, diagnostic settings, and metric alerting mesh. |

---

## 3. Ownership & Licensing

- All profile graphics, diagrams, and written documentation in this repository are original engineering work created by and for **Sanjeev Singh**.
- Profile photography is the exclusive personal property of Sanjeev Singh.
- Open-source infrastructure code across repositories is licensed under the MIT License.
