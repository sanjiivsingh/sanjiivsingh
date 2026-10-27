# Visual Asset Guide & Media Inventory

**Repository:** `sanjiivsingh/sanjiivsingh`  
**Maintainer:** Sanjeev Singh (`@sanjiivsingh`)  
**Design Theme:** Premium Minimalist Light Architecture (White/Light Foundation, Charcoal Typography, Red & Green Accents, Zero Dots)

---

## 1. Primary Profile Assets

| Asset Name | Relative Path | File Format | Dimensions / Size | Source / Creation Method | Intended Use & Placement |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Hero Banner** | `assets/banner.png` | PNG | 1200 × 420 px (~205 KB) | Custom Python PIL compositor using authentic profile photo (`profile.png`), Avenir Next typography, status indicator, and domain badges. Pure light background with **zero dots**. | Top of GitHub profile README. Represents primary personal brand and value proposition. |
| **Hero Banner (Master)** | `assets/banner-light.png` | PNG | 1200 × 420 px (~205 KB) | Identical high-resolution light-theme master. | Static fallback and high-DPI display asset. |
| **Consulting Services Matrix** | `assets/services-matrix.png` | PNG | 1200 × 330 px (~85 KB) | 4-column modular infographic card highlighting consulting pillars (Azure CAF, GenAI, DevSecOps, AKS Platform). | Section 4: Freelance Services & Business Outcomes. |
| **DevSecOps Quality Gates** | `assets/devsecops-gates.png` | PNG | 1200 × 250 px (~65 KB) | 6-stage shift-left security verification gates card with geometric checkmarks. | Section 6: Automated Shift-Left DevSecOps Delivery Gates. |
| **Architecture Pillars** | `assets/architecture-pillars.png` | PNG | 1200 × 280 px (~75 KB) | 4-column production standards card (100% Code-Driven, Zero-Trust, Governance, Resilience). | Section 4: Production Standards & Engineering Pillars. |
| **Profile Photograph** | `assets/profile.png` | PNG | 1086 × 1448 px (747 KB) | Original authentic studio portrait of Sanjeev Singh in formal business attire. | Base image for composite header banners, portfolio avatars, and media previews. |
| **DevSecOps Pipeline Diagram** | `assets/devsecops-pipeline.svg` | SVG | Scalable Vector (13.4 KB) | Hand-crafted vector graphic with CSS dash-stream flow animations and status indicators. | Section 6: DevSecOps pipeline visualization inside README. |
| **Platform Video Preview** | `assets/intro_preview.webp` | WebP | 720 × 405 px (5.9 MB) | Video frame grab with typography overlay and player preview. | Section 9: Video reel poster image linking to portfolio video player and MP4 stream. |
| **Platform Video Reel** | `assets/intro.mp4` | MP4 | 1080p HD (13.0 MB) | Master video recording featuring platform architecture overview. | Linked direct media file for high-bandwidth client streaming. |
| **Footer Contact Banner** | `assets/footer.png` | PNG | 1200 × 260 px (~21 KB) | Custom Python PIL composition with 4 modular contact cards (Email, LinkedIn, GitHub, Portfolio). Zero dots. | Bottom of README as a cohesive professional closing invitation. |
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
