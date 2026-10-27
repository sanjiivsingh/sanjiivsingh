#!/usr/bin/env python3
"""
Generate professional 16:9 architecture project showcase thumbnails & video poster.
Theme: Clean White/Slate Foundation, Deep Navy Typography, Azure Highlights.
Dimensions: 960 x 540 px (16:9 Aspect Ratio)
"""

import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "/Users/sanjeevsingh/DevOps/sanjiivsingh/assets"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_MONO = "/System/Library/Fonts/SFNSMono.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def draw_rounded_rect(draw, coords, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(coords, radius=radius, fill=fill, outline=outline, width=int(width))

def draw_check_badge(draw, x, y, size=16, color="#059669"):
    # Outer circle
    draw.ellipse((x, y, x + size, y + size), fill="#D1FAE5", outline="#A7F3D0", width=1)
    # Checkmark lines
    p1 = (x + int(size * 0.26), y + int(size * 0.52))
    p2 = (x + int(size * 0.44), y + int(size * 0.74))
    p3 = (x + int(size * 0.78), y + int(size * 0.28))
    draw.line([p1, p2, p3], fill=color, width=2)

# ==============================================================================
# 1. AI LANDING ZONE (960 x 540)
# ==============================================================================
def generate_ai_landing_zone():
    w, h = 960, 540
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=18, fill="#FFFFFF", outline="#E2E8F0", width=2)
    draw_rounded_rect(draw, (36, 12, 180, 16), radius=2, fill="#7C3AED")

    # Eyebrow Pill
    draw_rounded_rect(draw, (36, 30, 290, 54), radius=12, fill="#F5F3FF", outline="#DDD6FE", width=1)
    f_eyebrow = get_font(FONT_BOLD, 11)
    draw.text((48, 35), "ENTERPRISE GENAI INFRASTRUCTURE", fill="#6D28D9", font=f_eyebrow)

    # Title
    f_title = get_font(FONT_BOLD, 25)
    draw.text((36, 64), "Azure Enterprise AI & GenAI Landing Zone", fill="#0F172A", font=f_title)

    # Subtitle
    f_sub = get_font(FONT_REGULAR, 14)
    draw.text((36, 98), "Zero-Trust Private Perimeter · APIM AI Gateway · Vector RAG Grounding · Modular Terraform", fill="#475569", font=f_sub)

    # Architecture Blueprint Canvas
    diag_box = (36, 126, w - 36, 450)
    draw_rounded_rect(draw, diag_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    f_box_title = get_font(FONT_BOLD, 11)
    f_box_desc = get_font(FONT_REGULAR, 10)
    f_badge = get_font(FONT_BOLD, 9)

    # Node 1: Workload Client
    draw_rounded_rect(draw, (56, 150, 205, 425), radius=10, fill="#FFFFFF", outline="#CBD5E1", width=1)
    draw_rounded_rect(draw, (56, 150, 205, 176), radius=10, fill="#0F172A")
    draw.rectangle((56, 166, 205, 176), fill="#0F172A")
    draw.text((68, 158), "CLIENT WORKLOAD", fill="#FFFFFF", font=f_badge)
    draw.text((68, 196), "Enterprise Apps", fill="#0F172A", font=f_box_title)
    draw.text((68, 218), "• Internal APIs / Web\n• Managed Identity\n• Private VNet Peering\n• TLS 1.3 Encryption", fill="#64748B", font=f_box_desc)
    draw_rounded_rect(draw, (68, 360, 190, 385), radius=4, fill="#F1F5F9")
    draw.text((76, 367), "VNet Peered Ingress", fill="#475569", font=f_badge)

    # Arrow 1 -> 2
    draw.line((205, 280, 240, 280), fill="#94A3B8", width=2)
    draw.polygon([(240, 280), (232, 275), (232, 285)], fill="#94A3B8")

    # Node 2: APIM AI Gateway
    draw_rounded_rect(draw, (240, 145, 480, 430), radius=10, fill="#FFFFFF", outline="#7C3AED", width=2)
    draw_rounded_rect(draw, (240, 145, 480, 175), radius=10, fill="#7C3AED")
    draw.rectangle((240, 165, 480, 175), fill="#7C3AED")
    draw.text((255, 155), "AZURE APIM — AI GATEWAY", fill="#FFFFFF", font=f_badge)

    policies = [
        ("Token Rate Limiting", "Strict TPM & RPM quotas per client", "#EDE9FE", "#6D28D9"),
        ("Semantic Caching", "Up to 40% LLM inference savings", "#ECFDF5", "#047857"),
        ("Multi-Region Failover", "Automated model endpoint routing", "#EFF6FF", "#1D4ED8"),
        ("Zero-Trust IAM", "Entra ID & Key Vault CMK auth", "#FEF2F2", "#B91C1C")
    ]
    y_p = 190
    for p_title, p_sub, p_bg, p_col in policies:
        draw_rounded_rect(draw, (254, y_p, 466, y_p + 48), radius=6, fill=p_bg)
        draw.text((264, y_p + 8), p_title, fill=p_col, font=f_box_title)
        draw.text((264, y_p + 27), p_sub, fill="#475569", font=f_box_desc)
        y_p += 56

    # Arrow 2 -> 3
    draw.line((480, 240, 520, 215), fill="#0284C7", width=2)
    draw.polygon([(520, 215), (512, 212), (516, 222)], fill="#0284C7")

    draw.line((480, 335, 520, 350), fill="#059669", width=2)
    draw.polygon([(520, 350), (514, 343), (510, 353)], fill="#059669")

    # Node 3A: Azure OpenAI Service
    draw_rounded_rect(draw, (520, 150, 720, 275), radius=8, fill="#FFFFFF", outline="#0284C7", width=1)
    draw_rounded_rect(draw, (520, 150, 720, 176), radius=8, fill="#0284C7")
    draw.rectangle((520, 166, 720, 176), fill="#0284C7")
    draw.text((532, 157), "AZURE OPENAI SERVICE", fill="#FFFFFF", font=f_badge)
    draw.text((532, 188), "GPT-4o & text-embedding-3", fill="#0F172A", font=f_box_title)
    draw.text((532, 208), "• Public Access: Disabled (0.0.0.0/0)\n• Private Endpoint + Central DNS\n• Hardware CMK Secret Auth", fill="#64748B", font=f_box_desc)

    # Node 3B: Azure AI Search
    draw_rounded_rect(draw, (520, 295, 720, 425), radius=8, fill="#FFFFFF", outline="#059669", width=1)
    draw_rounded_rect(draw, (520, 295, 720, 321), radius=8, fill="#059669")
    draw.rectangle((520, 311, 720, 321), fill="#059669")
    draw.text((532, 302), "AZURE AI SEARCH", fill="#FFFFFF", font=f_badge)
    draw.text((532, 333), "Vector Database & RAG", fill="#0F172A", font=f_box_title)
    draw.text((532, 353), "• HNSW Vector Indexing & Hybrid\n• Private Link Grounding Pipeline\n• Chunk Retrieval from Storage Gen2", fill="#64748B", font=f_box_desc)

    # Node 4: Private Governance Perimeter
    draw_rounded_rect(draw, (740, 150, 904, 425), radius=10, fill="#FFFFFF", outline="#94A3B8", width=1)
    draw_rounded_rect(draw, (740, 150, 904, 176), radius=10, fill="#0F172A")
    draw.rectangle((740, 166, 904, 176), fill="#0F172A")
    draw.text((752, 157), "ZERO-TRUST GOVERNANCE", fill="#FFFFFF", font=f_badge)

    gov_items = [
        ("Azure Key Vault HSM", "FIPS 140-2 Level 3 CMK keys"),
        ("Storage Gen2 RAG", "Data Lake with private endpoint"),
        ("Log Analytics Mesh", "Diagnostic telemetry & audit"),
        ("Checkov SAST Gate", "Automated CI/CD policy audit")
    ]
    y_g = 192
    for g_t, g_d in gov_items:
        draw.text((752, y_g), f"• {g_t}", fill="#0F172A", font=f_box_title)
        draw.text((762, y_g + 16), g_d, fill="#64748B", font=f_box_desc)
        y_g += 54

    # Bottom Footer Row inside Card
    draw_rounded_rect(draw, (36, 470, 400, 508), radius=8, fill="#ECFDF5", outline="#A7F3D0", width=1)
    draw_check_badge(draw, 48, 481, size=16, color="#059669")
    draw.text((72, 482), "Verified: Checkov SAST Passed (CI Run #4043186)", fill="#065F46", font=get_font(FONT_BOLD, 11))

    f_tag = get_font(FONT_BOLD, 10)
    tags = ["Azure OpenAI", "APIM Gateway", "Vector RAG", "Terraform 1.9+"]
    x_tag = 418
    for t in tags:
        tw = int(draw.textlength(t, font=f_tag)) + 16
        draw_rounded_rect(draw, (x_tag, 474, x_tag + tw, 504), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
        draw.text((x_tag + 8, 482), t, fill="#334155", font=f_tag)
        x_tag += tw + 8

    f_link = get_font(FONT_BOLD, 12)
    draw.text((780, 481), "Open Source Repo →", fill="#0078D4", font=f_link)

    out_path = os.path.join(ASSETS_DIR, "project-ai-landing-zone.png")
    img.save(out_path, "PNG", optimize=True)
    print(f"Generated {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")


# ==============================================================================
# 2. HUB-AND-SPOKE LANDING ZONE (960 x 540)
# ==============================================================================
def generate_hub_spoke():
    w, h = 960, 540
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=18, fill="#FFFFFF", outline="#E2E8F0", width=2)
    draw_rounded_rect(draw, (36, 12, 180, 16), radius=2, fill="#0078D4")

    # Eyebrow Pill
    draw_rounded_rect(draw, (36, 30, 270, 54), radius=12, fill="#EFF6FF", outline="#BFDBFE", width=1)
    f_eyebrow = get_font(FONT_BOLD, 11)
    draw.text((48, 35), "CAF ENTERPRISE NETWORK TOPOLOGY", fill="#1D4ED8", font=f_eyebrow)

    # Title
    f_title = get_font(FONT_BOLD, 25)
    draw.text((36, 64), "Azure Enterprise Hub-and-Spoke Landing Zone", fill="#0F172A", font=f_title)

    # Subtitle
    f_sub = get_font(FONT_REGULAR, 14)
    draw.text((36, 98), "Central Azure Firewall · Bastion Host · Bidirectional Peering · UDR 0.0.0.0/0 Inspection", fill="#475569", font=f_sub)

    # Diagram Canvas
    diag_box = (36, 126, w - 36, 450)
    draw_rounded_rect(draw, diag_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    f_box_title = get_font(FONT_BOLD, 11)
    f_box_desc = get_font(FONT_REGULAR, 10)
    f_badge = get_font(FONT_BOLD, 9)

    # Zone 1: Hybrid / On-Prem Ingress (Left)
    draw_rounded_rect(draw, (56, 150, 210, 425), radius=10, fill="#FFFFFF", outline="#CBD5E1", width=1)
    draw_rounded_rect(draw, (56, 150, 210, 176), radius=10, fill="#0F172A")
    draw.rectangle((56, 166, 210, 176), fill="#0F172A")
    draw.text((68, 157), "HYBRID CONNECTIVITY", fill="#FFFFFF", font=f_badge)
    draw.text((68, 192), "On-Premises WAN", fill="#0F172A", font=f_box_title)
    draw.text((68, 214), "• Corporate Data Center\n• ExpressRoute / VPN Link\n• Edge Security Appliance\n• Dual WAN Redundancy", fill="#64748B", font=f_box_desc)

    draw_rounded_rect(draw, (68, 320, 198, 395), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
    draw.text((76, 332), "GatewaySubnet", fill="#0F172A", font=f_box_title)
    draw.text((76, 354), "• S2S IPsec VPN Tunnel\n• 10.0.255.0/27", fill="#64748B", font=f_box_desc)

    # Arrow 1 -> 2
    draw.line((210, 285, 250, 285), fill="#0078D4", width=2)
    draw.polygon([(250, 285), (242, 280), (242, 290)], fill="#0078D4")

    # Zone 2: Central Transit Hub VNet (Middle)
    draw_rounded_rect(draw, (250, 145, 520, 430), radius=10, fill="#FFFFFF", outline="#0078D4", width=2)
    draw_rounded_rect(draw, (250, 145, 520, 175), radius=10, fill="#0078D4")
    draw.rectangle((250, 165, 520, 175), fill="#0078D4")
    draw.text((264, 155), "TRANSIT HUB VNET (10.0.0.0/16)", fill="#FFFFFF", font=f_badge)

    hub_boxes = [
        ("Azure Firewall Premium", "Central L4/L7 Threat Defense & IDPS\nPrivate IP: 10.0.1.4 (UDR Next Hop)", "#EFF6FF", "#1D4ED8"),
        ("Azure Bastion Host", "Zero-Public IP Secure Browser Ingress\nRDP / SSH Management Tunnel", "#F8FAFC", "#0F172A"),
        ("Private DNS Resolver", "Centralized Private Link Resolution\nPrevents Split-Brain across Spokes", "#ECFDF5", "#047857")
    ]
    y_h = 188
    for hb_t, hb_d, hb_bg, hb_col in hub_boxes:
        draw_rounded_rect(draw, (264, y_h, 506, y_h + 68), radius=6, fill=hb_bg, outline="#E2E8F0", width=1)
        draw.text((276, y_h + 8), hb_t, fill=hb_col, font=f_box_title)
        draw.text((276, y_h + 28), hb_d, fill="#475569", font=f_box_desc)
        y_h += 75

    # Connectors Hub -> Spokes
    draw.line((520, 220, 560, 205), fill="#059669", width=2)
    draw.polygon([(560, 205), (552, 201), (555, 211)], fill="#059669")

    draw.line((520, 350, 560, 365), fill="#7C3AED", width=2)
    draw.polygon([(560, 365), (555, 358), (552, 368)], fill="#7C3AED")

    # Zone 3A: Production Workload Spoke
    draw_rounded_rect(draw, (560, 150, 735, 275), radius=8, fill="#FFFFFF", outline="#059669", width=1)
    draw_rounded_rect(draw, (560, 150, 735, 176), radius=8, fill="#059669")
    draw.rectangle((560, 166, 735, 176), fill="#059669")
    draw.text((572, 157), "WORKLOAD SPOKE (10.1.0.0/16)", fill="#FFFFFF", font=f_badge)
    draw.text((572, 186), "AKS & Container Tier", fill="#0F172A", font=f_box_title)
    draw.text((572, 206), "• Hardened AKS Node Subnet\n• Internal Load Balancer\n• UDR: 0.0.0.0/0 -> Azure Firewall", fill="#64748B", font=f_box_desc)
    draw_rounded_rect(draw, (572, 248, 715, 266), radius=3, fill="#DCFCE7")
    draw.text((578, 251), "Bidirectional VNet Peering", fill="#15803D", font=get_font(FONT_BOLD, 8.5))

    # Zone 3B: AI & Data Platform Spoke
    draw_rounded_rect(draw, (560, 295, 735, 425), radius=8, fill="#FFFFFF", outline="#7C3AED", width=1)
    draw_rounded_rect(draw, (560, 295, 735, 321), radius=8, fill="#7C3AED")
    draw.rectangle((560, 311, 735, 321), fill="#7C3AED")
    draw.text((572, 302), "AI & DATA SPOKE (10.2.0.0/16)", fill="#FFFFFF", font=f_badge)
    draw.text((572, 331), "GenAI Workload Tier", fill="#0F172A", font=f_box_title)
    draw.text((572, 351), "• Azure OpenAI Private Endpoints\n• Azure AI Search Vector Subnet\n• Key Vault & Storage Gen2 RAG", fill="#64748B", font=f_box_desc)
    draw_rounded_rect(draw, (572, 396, 715, 414), radius=3, fill="#F3E8FF")
    draw.text((578, 399), "Forced Tunneling via Firewall", fill="#7E22CE", font=get_font(FONT_BOLD, 8.5))

    # Zone 4: CAF Governance Hierarchy
    draw_rounded_rect(draw, (755, 150, 904, 425), radius=10, fill="#FFFFFF", outline="#94A3B8", width=1)
    draw_rounded_rect(draw, (755, 150, 904, 176), radius=10, fill="#0F172A")
    draw.rectangle((755, 166, 904, 176), fill="#0F172A")
    draw.text((766, 157), "CAF GOVERNANCE", fill="#FFFFFF", font=f_badge)

    caf_items = [
        ("Root Management Group", "Hierarchical policy inheritance"),
        ("Platform Subscriptions", "Connectivity, Identity, Management"),
        ("Workload Subscriptions", "Autonomous Spoke Dev/Prod"),
        ("Azure Policy Baselines", "Deny public IP & audit tags")
    ]
    y_c = 192
    for c_t, c_d in caf_items:
        draw.text((766, y_c), f"• {c_t}", fill="#0F172A", font=f_box_title)
        draw.text((776, y_c + 16), c_d, fill="#64748B", font=f_box_desc)
        y_c += 54

    # Bottom Footer Row
    draw_rounded_rect(draw, (36, 470, 400, 508), radius=8, fill="#ECFDF5", outline="#A7F3D0", width=1)
    draw_check_badge(draw, 48, 481, size=16, color="#059669")
    draw.text((72, 482), "Verified: CIS Azure Benchmark (CI Run #4045002)", fill="#065F46", font=get_font(FONT_BOLD, 11))

    f_tag = get_font(FONT_BOLD, 10)
    tags = ["Azure Firewall", "Hub-and-Spoke", "UDR Routing", "Terraform 1.9+"]
    x_tag = 418
    for t in tags:
        tw = int(draw.textlength(t, font=f_tag)) + 16
        draw_rounded_rect(draw, (x_tag, 474, x_tag + tw, 504), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
        draw.text((x_tag + 8, 482), t, fill="#334155", font=f_tag)
        x_tag += tw + 8

    f_link = get_font(FONT_BOLD, 12)
    draw.text((780, 481), "Open Source Repo →", fill="#0078D4", font=f_link)

    out_path = os.path.join(ASSETS_DIR, "project-hub-spoke.png")
    img.save(out_path, "PNG", optimize=True)
    print(f"Generated {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")


# ==============================================================================
# 3. DEVSECOPS PIPELINE (960 x 540)
# ==============================================================================
def generate_devsecops():
    w, h = 960, 540
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=18, fill="#FFFFFF", outline="#E2E8F0", width=2)
    draw_rounded_rect(draw, (36, 12, 180, 16), radius=2, fill="#E11D48")

    # Eyebrow Pill
    draw_rounded_rect(draw, (36, 30, 280, 54), radius=12, fill="#FFF1F2", outline="#FECDD3", width=1)
    f_eyebrow = get_font(FONT_BOLD, 11)
    draw.text((48, 35), "SHIFT-LEFT SECURITY & K8S CI/CD", fill="#BE123C", font=f_eyebrow)

    # Title
    f_title = get_font(FONT_BOLD, 25)
    draw.text((36, 64), "Azure AKS DevSecOps Automated Delivery Pipeline", fill="#0F172A", font=f_title)

    # Subtitle
    f_sub = get_font(FONT_REGULAR, 14)
    draw.text((36, 98), "Terraform IaC · SonarQube · Checkov SAST · Trivy Vulnerability Gates · Distroless AKS Deploy", fill="#475569", font=f_sub)

    # Diagram Canvas
    diag_box = (36, 126, w - 36, 450)
    draw_rounded_rect(draw, diag_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    f_box_title = get_font(FONT_BOLD, 10.5)
    f_box_desc = get_font(FONT_REGULAR, 9.5)
    f_badge = get_font(FONT_BOLD, 9)

    stages = [
        ("01 • PR & AUTH", "#0078D4", "Passwordless SCM", [
            ("GitHub Actions PR", "Event-driven workflow trigger"),
            ("Azure OIDC Login", "Zero long-lived secret keys"),
            ("Branch Protection", "Signed commits & required checks")
        ]),
        ("02 • PRE-FLIGHT LINT", "#7C3AED", "Syntax & Secrets", [
            ("TFLint Linter", "AzureRM module rule validation"),
            ("Gitleaks Scan", "High-entropy secret detection"),
            ("Terraform fmt", "Strict code style enforcement")
        ]),
        ("03 • SAST SECURITY", "#E11D48", "IaC Security Gates", [
            ("Checkov Policies", "CIS benchmark compliance scan"),
            ("tfsec Static Analysis", "Deep misconfiguration checks"),
            ("SonarQube Gate", "Application quality & code coverage")
        ]),
        ("04 • BUILD & AKS", "#059669", "Container & Deploy", [
            ("Trivy Vulnerability", "Container CVE scanning on ACR"),
            ("Manual Sign-off", "Environment production sign-off"),
            ("AKS Zero-Downtime", "Distroless pods + NetworkPolicies")
        ])
    ]

    x_s = 56
    stage_w = 195
    for idx, (st_name, st_color, st_sub, st_items) in enumerate(stages):
        draw_rounded_rect(draw, (x_s, 150, x_s + stage_w, 425), radius=10, fill="#FFFFFF", outline=st_color, width=1)
        draw_rounded_rect(draw, (x_s, 150, x_s + stage_w, 178), radius=10, fill=st_color)
        draw.rectangle((x_s, 168, x_s + stage_w, 178), fill=st_color)
        draw.text((x_s + 12, 158), st_name, fill="#FFFFFF", font=f_badge)

        draw.text((x_s + 12, 190), st_sub, fill="#0F172A", font=f_box_title)

        y_it = 216
        for it_title, it_desc in st_items:
            draw_rounded_rect(draw, (x_s + 10, y_it, x_s + stage_w - 10, y_it + 50), radius=6, fill="#F8FAFC", outline="#E2E8F0", width=1)
            draw.text((x_s + 18, y_it + 8), it_title, fill="#0F172A", font=f_box_title)
            draw.text((x_s + 18, y_it + 27), it_desc, fill="#64748B", font=f_box_desc)
            y_it += 58

        if idx < 3:
            ax = x_s + stage_w
            draw.line((ax, 280, ax + 25, 280), fill="#94A3B8", width=2)
            draw.polygon([(ax + 25, 280), (ax + 17, 275), (ax + 17, 285)], fill="#94A3B8")

        x_s += stage_w + 25

    # Bottom Footer Row
    draw_rounded_rect(draw, (36, 470, 400, 508), radius=8, fill="#ECFDF5", outline="#A7F3D0", width=1)
    draw_check_badge(draw, 48, 481, size=16, color="#059669")
    draw.text((72, 482), "Verified: Quality Gates Passed (CI Run #4019564)", fill="#065F46", font=get_font(FONT_BOLD, 11))

    f_tag = get_font(FONT_BOLD, 10)
    tags = ["Azure AKS", "Docker", "Trivy Scan", "Checkov", "GitHub Actions"]
    x_tag = 418
    for t in tags:
        tw = int(draw.textlength(t, font=f_tag)) + 16
        draw_rounded_rect(draw, (x_tag, 474, x_tag + tw, 504), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
        draw.text((x_tag + 8, 482), t, fill="#334155", font=f_tag)
        x_tag += tw + 8

    f_link = get_font(FONT_BOLD, 12)
    draw.text((780, 481), "Open Source Repo →", fill="#0078D4", font=f_link)

    out_path = os.path.join(ASSETS_DIR, "project-devsecops.png")
    img.save(out_path, "PNG", optimize=True)
    print(f"Generated {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")


# ==============================================================================
# 4. TERRAFORM RESOURCE MODULES (960 x 540)
# ==============================================================================
def generate_terraform_modules():
    w, h = 960, 540
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=18, fill="#FFFFFF", outline="#E2E8F0", width=2)
    draw_rounded_rect(draw, (36, 12, 180, 16), radius=2, fill="#059669")

    # Eyebrow Pill
    draw_rounded_rect(draw, (36, 30, 290, 54), radius=12, fill="#ECFDF5", outline="#A7F3D0", width=1)
    f_eyebrow = get_font(FONT_BOLD, 11)
    draw.text((48, 35), "ENTERPRISE IAC COMPONENT LIBRARY", fill="#047857", font=f_eyebrow)

    # Title
    f_title = get_font(FONT_BOLD, 25)
    draw.text((36, 64), "Terraform Azure Reusable Resource Modules", fill="#0F172A", font=f_title)

    # Subtitle
    f_sub = get_font(FONT_REGULAR, 14)
    draw.text((36, 98), "11+ Reusable Child Modules · Remote State Lease Locking · Implicit Graph Sequencing", fill="#475569", font=f_sub)

    # Diagram Canvas
    diag_box = (36, 126, w - 36, 450)
    draw_rounded_rect(draw, diag_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    f_box_title = get_font(FONT_BOLD, 10.5)
    f_box_desc = get_font(FONT_REGULAR, 9.5)
    f_badge = get_font(FONT_BOLD, 9)

    # Left: Root Environment Consumer
    draw_rounded_rect(draw, (56, 150, 240, 425), radius=10, fill="#FFFFFF", outline="#0F172A", width=1)
    draw_rounded_rect(draw, (56, 150, 240, 178), radius=10, fill="#0F172A")
    draw.rectangle((56, 168, 240, 178), fill="#0F172A")
    draw.text((68, 158), "ROOT ENVIRONMENT", fill="#FFFFFF", font=f_badge)
    draw.text((68, 192), "Consumer Manifests", fill="#0F172A", font=f_box_title)

    envs = [
        ("environments/dev", "Development sandbox root"),
        ("environments/prod", "High-availability production root"),
        ("backend.tf (Azure Blob)", "Lease locking & state encryption"),
        ("versions.tf", "Terraform 1.9+ & AzureRM ~> 3.0")
    ]
    y_e = 216
    for e_t, e_d in envs:
        draw_rounded_rect(draw, (68, y_e, 228, y_e + 45), radius=5, fill="#F8FAFC", outline="#E2E8F0", width=1)
        draw.text((76, y_e + 6), e_t, fill="#0F172A", font=f_box_title)
        draw.text((76, y_e + 24), e_d, fill="#64748B", font=f_box_desc)
        y_e += 52

    # Arrow Consumer -> Modules
    draw.line((240, 280, 275, 280), fill="#059669", width=2)
    draw.polygon([(275, 280), (267, 275), (267, 285)], fill="#059669")

    # Center Grid: 11 Child Modules
    draw_rounded_rect(draw, (275, 145, 690, 430), radius=10, fill="#FFFFFF", outline="#059669", width=2)
    draw_rounded_rect(draw, (275, 145, 690, 175), radius=10, fill="#059669")
    draw.rectangle((275, 165, 690, 175), fill="#059669")
    draw.text((288, 155), "11+ STANDARDIZED CHILD MODULES (IMPLICIT GRAPH)", fill="#FFFFFF", font=f_badge)

    modules = [
        ("Resource Group", "rg-module", "Tagging & Lifecycle"),
        ("Virtual Network", "vnet-module", "Address Space & DNS"),
        ("Subnet & Delegation", "subnet-module", "Service Endpoints"),
        ("Network Sec Group", "nsg-module", "Micro-segmentation"),
        ("Public IP (Standard)", "pip-module", "Zone-Redundant SKU"),
        ("Network Interface", "nic-module", "IP Configurations"),
        ("Linux Virtual Machine", "vm-module", "SSH Keys & Cloud-init"),
        ("Azure Bastion Host", "bastion-module", "Managed RDP/SSH"),
        ("Key Vault HSM", "kv-module", "Purge Protection & CMK"),
        ("App Gateway v2", "appgw-module", "WAF & SSL Offloading"),
        ("Storage Account", "storage-module", "TLS 1.2+ & Blob Lease")
    ]

    for i, (m_name, m_dir, m_tag) in enumerate(modules):
        col = i % 3
        row = i // 3
        mx = 288 + col * 132
        my = 188 + row * 58
        draw_rounded_rect(draw, (mx, my, mx + 124, my + 50), radius=6, fill="#F8FAFC", outline="#E2E8F0", width=1)
        draw.text((mx + 6, my + 6), m_name, fill="#0F172A", font=get_font(FONT_BOLD, 9.5))
        draw.text((mx + 6, my + 21), m_dir, fill="#0078D4", font=get_font(FONT_REGULAR, 8.5))
        draw.text((mx + 6, my + 34), m_tag, fill="#64748B", font=get_font(FONT_REGULAR, 8))

    # Right: Principles / Architecture Standards
    draw_rounded_rect(draw, (710, 150, 904, 425), radius=10, fill="#FFFFFF", outline="#94A3B8", width=1)
    draw_rounded_rect(draw, (710, 150, 904, 176), radius=10, fill="#0F172A")
    draw.rectangle((710, 166, 904, 176), fill="#0F172A")
    draw.text((722, 157), "DESIGN STANDARDS", fill="#FFFFFF", font=f_badge)

    standards = [
        ("Implicit Dependency", "Zero manual depends_on graph anti-patterns"),
        ("Input Validation", "Strict type constraints & regex validation rules"),
        ("Standardized Outputs", "Consistent attribute maps for root consumption"),
        ("Zero Portal Drift", "100% code-driven state with remote lease locking")
    ]
    y_std = 192
    for s_t, s_d in standards:
        draw.text((722, y_std), f"• {s_t}", fill="#0F172A", font=f_box_title)
        draw.text((732, y_std + 16), s_d, fill="#64748B", font=f_box_desc)
        y_std += 54

    # Bottom Footer Row
    draw_rounded_rect(draw, (36, 470, 400, 508), radius=8, fill="#ECFDF5", outline="#A7F3D0", width=1)
    draw_check_badge(draw, 48, 481, size=16, color="#059669")
    draw.text((72, 482), "Verified: TFLint & Plan Matrix Passed (CI Automated)", fill="#065F46", font=get_font(FONT_BOLD, 11))

    f_tag = get_font(FONT_BOLD, 10)
    tags = ["Terraform 1.9+", "11 Child Modules", "State Locking", "AzureRM"]
    x_tag = 418
    for t in tags:
        tw = int(draw.textlength(t, font=f_tag)) + 16
        draw_rounded_rect(draw, (x_tag, 474, x_tag + tw, 504), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
        draw.text((x_tag + 8, 482), t, fill="#334155", font=f_tag)
        x_tag += tw + 8

    f_link = get_font(FONT_BOLD, 12)
    draw.text((780, 481), "Open Source Repo →", fill="#0078D4", font=f_link)

    out_path = os.path.join(ASSETS_DIR, "project-terraform-modules.png")
    img.save(out_path, "PNG", optimize=True)
    print(f"Generated {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")


# ==============================================================================
# 5. VIDEO REEL POSTER CARD (960 x 540)
# ==============================================================================
def generate_video_poster():
    w, h = 960, 540
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    # Outer Card
    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=18, fill="#FFFFFF", outline="#E2E8F0", width=2)

    # Window Header Bar (like the Next.js portfolio video player)
    draw_rounded_rect(draw, (12, 12, w - 12, 60), radius=18, fill="#0F172A")
    draw.rectangle((12, 45, w - 12, 60), fill="#0F172A")

    # Traffic light dots
    draw.ellipse((32, 28, 44, 40), fill="#EF4444")
    draw.ellipse((52, 28, 64, 40), fill="#F59E0B")
    draw.ellipse((72, 28, 84, 40), fill="#10B981")

    # Header title
    f_head = get_font(FONT_BOLD, 12)
    draw.text((105, 27), "PLATFORM ARCHITECTURE REEL // SANJEEV SINGH", fill="#38BDF8", font=f_head)

    # Header badges
    draw_rounded_rect(draw, (w - 230, 24, w - 120, 46), radius=6, fill="#082F49", outline="#0284C7", width=1)
    draw.text((w - 220, 29), "SYSTEM REEL", fill="#38BDF8", font=get_font(FONT_BOLD, 9.5))

    draw_rounded_rect(draw, (w - 110, 24, w - 32, 46), radius=6, fill="#1E293B")
    draw.text((w - 100, 29), "1080p HD", fill="#E2E8F0", font=get_font(FONT_BOLD, 9.5))

    # Inner Video Preview Canvas
    vid_box = (36, 80, w - 36, 460)
    draw_rounded_rect(draw, vid_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    # 4 Architectural Pillars Preview Grid
    pillars = [
        ("Azure Landing Zones", "CAF Hub & Spoke · Azure Firewall · Bastion · UDR 0.0.0.0/0", "#0078D4", (56, 100, 460, 245)),
        ("Modular Terraform", "11+ Reusable Child Modules · State Lease Locking · No Drift", "#7C3AED", (500, 100, 904, 245)),
        ("Shift-Left DevSecOps", "Checkov SAST · TFLint · Trivy CVE · Azure OIDC Workload ID", "#E11D48", (56, 265, 460, 410)),
        ("Enterprise GenAI", "Azure OpenAI · APIM AI Gateway · Vector RAG Grounding", "#059669", (500, 265, 904, 410))
    ]

    for p_title, p_desc, p_accent, coords in pillars:
        draw_rounded_rect(draw, coords, radius=8, fill="#FFFFFF", outline="#E2E8F0", width=1)
        draw_rounded_rect(draw, (coords[0], coords[1], coords[0] + 6, coords[3]), radius=3, fill=p_accent)
        draw.text((coords[0] + 20, coords[1] + 20), p_title, fill="#0F172A", font=get_font(FONT_BOLD, 15))
        draw.text((coords[0] + 20, coords[1] + 50), p_desc, fill="#64748B", font=get_font(FONT_REGULAR, 11))
        draw_rounded_rect(draw, (coords[0] + 20, coords[1] + 90, coords[0] + 160, coords[1] + 115), radius=4, fill="#F1F5F9")
        draw.text((coords[0] + 28, coords[1] + 96), "Production Validated", fill="#475569", font=get_font(FONT_BOLD, 9))

    # High-Impact Centered Play Button Overlay
    cx, cy = w // 2, 260
    # Semi-transparent backdrop for play button
    draw_rounded_rect(draw, (cx - 190, cy - 65, cx + 190, cy + 65), radius=16, fill="#0F172ACC", outline="#0078D4", width=2)

    # Play Icon Circle
    draw.ellipse((cx - 36, cy - 50, cx + 36, cy + 22), fill="#0078D4", outline="#38BDF8", width=2)
    # Triangle Play
    draw.polygon([(cx - 10, cy - 30), (cx - 10, cy + 2), (cx + 18, cy - 14)], fill="#FFFFFF")

    # Button Text
    draw.text((cx - 130, cy + 30), "Watch Architecture Reel (00:20)", fill="#FFFFFF", font=get_font(FONT_BOLD, 14))

    # Bottom Console / Player Status Bar
    draw_rounded_rect(draw, (36, 480, w - 36, 520), radius=8, fill="#0F172A")
    draw_check_badge(draw, 50, 492, size=16, color="#059669")
    draw.text((74, 494), "Interactive Player Online: sanjeevsingh.oneps.in", fill="#E2E8F0", font=get_font(FONT_BOLD, 11))
    draw.text((w - 280, 494), "Click Thumbnail to Launch Player →", fill="#38BDF8", font=get_font(FONT_BOLD, 11))

    # Save as WebP
    out_path = os.path.join(ASSETS_DIR, "intro_preview.webp")
    img.save(out_path, "WEBP", quality=90)
    print(f"Generated {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")


if __name__ == "__main__":
    generate_ai_landing_zone()
    generate_hub_spoke()
    generate_devsecops()
    generate_terraform_modules()
    generate_video_poster()
