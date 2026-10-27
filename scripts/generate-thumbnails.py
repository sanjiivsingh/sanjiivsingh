#!/usr/bin/env python3
"""
Generate bold, readable, visually consistent 16:9 architecture project showcase thumbnails
and the visual centerpiece video poster card.
Theme: Clean White/Slate Foundation, Deep Charcoal Typography, Consistent Azure & Security Accents.
Dimensions: 960 x 540 px (16:9 Aspect Ratio)
Minimum Font Size: 13px for crystal-clear readability on all devices.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "/Users/sanjeevsingh/DevOps/sanjiivsingh/assets"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, int(size))
    except Exception:
        return ImageFont.load_default()

def draw_rounded_rect(draw, coords, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(coords, radius=radius, fill=fill, outline=outline, width=int(width))

def draw_check_badge(draw, x, y, size=18, color="#059669"):
    # Outer circle
    draw.ellipse((x, y, x + size, y + size), fill="#D1FAE5", outline="#A7F3D0", width=1)
    # Checkmark lines
    p1 = (x + int(size * 0.26), y + int(size * 0.52))
    p2 = (x + int(size * 0.44), y + int(size * 0.74))
    p3 = (x + int(size * 0.78), y + int(size * 0.28))
    draw.line([p1, p2, p3], fill=color, width=2)

def draw_arrow(draw, start, end, color="#64748B", width=3):
    width_int = int(width)
    draw.line([start, end], fill=color, width=width_int)
    # Arrowhead
    sx, sy = start
    ex, ey = end
    if ex > sx:  # Right pointing
        draw.polygon([(ex, ey), (ex - 10, ey - 6), (ex - 10, ey + 6)], fill=color)
    elif ey > sy:  # Down pointing
        draw.polygon([(ex, ey), (ex - 6, ey - 10), (ex + 6, ey - 10)], fill=color)


# ==============================================================================
# 1. AI LANDING ZONE (960 x 540)
# ==============================================================================
def generate_ai_landing_zone():
    w, h = 960, 540
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    # Base Card
    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=16, fill="#FFFFFF", outline="#E2E8F0", width=2)
    # Top Accent Line
    draw_rounded_rect(draw, (36, 12, 200, 16), radius=2, fill="#7C3AED")

    # Eyebrow Pill
    draw_rounded_rect(draw, (36, 28, 305, 54), radius=12, fill="#F5F3FF", outline="#DDD6FE", width=1)
    draw.text((48, 33), "ENTERPRISE GENAI INFRASTRUCTURE", fill="#6D28D9", font=get_font(FONT_BOLD, 12))

    # Title & Subtitle
    draw.text((36, 62), "Azure Enterprise AI & GenAI Landing Zone", fill="#0F172A", font=get_font(FONT_BOLD, 26))
    draw.text((36, 96), "Zero-Trust Private Perimeter · APIM AI Gateway · Vector RAG Grounding · Modular Terraform", fill="#475569", font=get_font(FONT_REGULAR, 15))

    # Diagram Canvas
    diag_box = (36, 128, w - 36, 452)
    draw_rounded_rect(draw, diag_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    f_title = get_font(FONT_BOLD, 16)
    f_body = get_font(FONT_REGULAR, 13)
    f_badge = get_font(FONT_BOLD, 11)

    # Node 1: Client Ingress (Left)
    draw_rounded_rect(draw, (56, 152, 235, 428), radius=10, fill="#FFFFFF", outline="#CBD5E1", width=1.5)
    draw_rounded_rect(draw, (56, 152, 235, 184), radius=10, fill="#0F172A")
    draw.rectangle((56, 172, 235, 184), fill="#0F172A")
    draw.text((70, 160), "1. APPLICATION TIER", fill="#FFFFFF", font=f_badge)
    draw.text((70, 202), "Enterprise Clients", fill="#0F172A", font=f_title)
    draw.text((70, 230), "• Web & Mobile Apps\n• Microservice APIs\n• Private VNet Peering\n• Entra ID Auth Tokens", fill="#475569", font=f_body)
    
    draw_rounded_rect(draw, (70, 365, 220, 395), radius=6, fill="#F1F5F9")
    draw.text((78, 372), "Private VNet Link", fill="#334155", font=f_badge)

    # Arrow 1 -> 2
    draw_arrow(draw, (235, 290), (280, 290), color="#7C3AED", width=3)

    # Node 2: APIM AI Gateway (Center)
    draw_rounded_rect(draw, (280, 146, 560, 434), radius=10, fill="#FFFFFF", outline="#7C3AED", width=2)
    draw_rounded_rect(draw, (280, 146, 560, 180), radius=10, fill="#7C3AED")
    draw.rectangle((280, 168, 560, 180), fill="#7C3AED")
    draw.text((295, 155), "2. AZURE APIM — AI GATEWAY", fill="#FFFFFF", font=f_badge)

    gateways = [
        ("Token Rate Limiting", "Strict TPM & RPM quotas per client", "#EDE9FE", "#6D28D9"),
        ("Semantic Response Cache", "Up to 40% inference cost savings", "#ECFDF5", "#047857"),
        ("Zero-Trust Private DNS", "100% private link endpoints", "#EFF6FF", "#1D4ED8"),
        ("Key Vault HSM CMK", "FIPS 140-2 Level 3 security", "#FEF2F2", "#B91C1C")
    ]
    y_g = 196
    for g_t, g_d, g_bg, g_col in gateways:
        draw_rounded_rect(draw, (296, y_g, 544, y_g + 50), radius=6, fill=g_bg)
        draw.text((308, y_g + 8), g_t, fill=g_col, font=get_font(FONT_BOLD, 14))
        draw.text((308, y_g + 28), g_d, fill="#475569", font=f_body)
        y_g += 58

    # Arrow 2 -> 3A & 3B
    draw_arrow(draw, (560, 220), (605, 220), color="#0284C7", width=3)
    draw_arrow(draw, (560, 360), (605, 360), color="#059669", width=3)

    # Node 3A: Azure OpenAI (Right Top)
    draw_rounded_rect(draw, (605, 152, 904, 280), radius=10, fill="#FFFFFF", outline="#0284C7", width=1.5)
    draw_rounded_rect(draw, (605, 152, 904, 184), radius=10, fill="#0284C7")
    draw.rectangle((605, 172, 904, 184), fill="#0284C7")
    draw.text((620, 160), "3A. AZURE OPENAI SERVICE", fill="#FFFFFF", font=f_badge)
    draw.text((620, 196), "GPT-4o & text-embedding-3", fill="#0F172A", font=f_title)
    draw.text((620, 224), "• Public Access: 100% Disabled\n• Private Endpoint in isolated subnet", fill="#475569", font=f_body)

    # Node 3B: AI Search & Data Lake (Right Bottom)
    draw_rounded_rect(draw, (605, 300, 904, 428), radius=10, fill="#FFFFFF", outline="#059669", width=1.5)
    draw_rounded_rect(draw, (605, 300, 904, 332), radius=10, fill="#059669")
    draw.rectangle((605, 320, 904, 332), fill="#059669")
    draw.text((620, 308), "3B. AZURE AI SEARCH & RAG", fill="#FFFFFF", font=f_badge)
    draw.text((620, 344), "Vector Database & Data Lake", fill="#0F172A", font=f_title)
    draw.text((620, 372), "• HNSW Vector Search & Grounding\n• Chunk retrieval from Storage Gen2", fill="#475569", font=f_body)

    # Footer Row inside Card
    draw_rounded_rect(draw, (36, 472, 420, 514), radius=8, fill="#ECFDF5", outline="#A7F3D0", width=1)
    draw_check_badge(draw, 50, 484, size=18, color="#059669")
    draw.text((76, 485), "Verified: Checkov SAST Passed (CI Validated)", fill="#065F46", font=get_font(FONT_BOLD, 13))

    f_tag = get_font(FONT_BOLD, 12)
    tags = ["Azure OpenAI", "APIM Gateway", "Vector RAG", "Terraform 1.9+"]
    x_tag = 438
    for t in tags:
        tw = int(draw.textlength(t, font=f_tag)) + 18
        draw_rounded_rect(draw, (x_tag, 476, x_tag + tw, 510), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
        draw.text((x_tag + 9, 485), t, fill="#334155", font=f_tag)
        x_tag += tw + 10

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

    # Base Card
    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=16, fill="#FFFFFF", outline="#E2E8F0", width=2)
    # Top Accent Line
    draw_rounded_rect(draw, (36, 12, 200, 16), radius=2, fill="#0078D4")

    # Eyebrow Pill
    draw_rounded_rect(draw, (36, 28, 290, 54), radius=12, fill="#EFF6FF", outline="#BFDBFE", width=1)
    draw.text((48, 33), "CAF ENTERPRISE NETWORK MESH", fill="#1D4ED8", font=get_font(FONT_BOLD, 12))

    # Title & Subtitle
    draw.text((36, 62), "Azure Enterprise Hub-and-Spoke Landing Zone", fill="#0F172A", font=get_font(FONT_BOLD, 26))
    draw.text((36, 96), "Central Azure Firewall · Bastion Host · Bidirectional Peering · UDR 0.0.0.0/0 Inspection", fill="#475569", font=get_font(FONT_REGULAR, 15))

    # Diagram Canvas
    diag_box = (36, 128, w - 36, 452)
    draw_rounded_rect(draw, diag_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    f_title = get_font(FONT_BOLD, 16)
    f_body = get_font(FONT_REGULAR, 13)
    f_badge = get_font(FONT_BOLD, 11)

    # Zone 1: Hybrid On-Prem (Left)
    draw_rounded_rect(draw, (56, 152, 240, 428), radius=10, fill="#FFFFFF", outline="#CBD5E1", width=1.5)
    draw_rounded_rect(draw, (56, 152, 240, 184), radius=10, fill="#0F172A")
    draw.rectangle((56, 172, 240, 184), fill="#0F172A")
    draw.text((70, 160), "1. HYBRID EDGE", fill="#FFFFFF", font=f_badge)
    draw.text((70, 202), "On-Premises WAN", fill="#0F172A", font=f_title)
    draw.text((70, 230), "• Corporate Data Center\n• S2S IPsec VPN Tunnel\n• GatewaySubnet (10.0.255.0/27)\n• Resilient BGP Peering", fill="#475569", font=f_body)

    draw_rounded_rect(draw, (70, 365, 226, 395), radius=6, fill="#F1F5F9")
    draw.text((78, 372), "IPsec S2S Tunnel", fill="#334155", font=f_badge)

    # Arrow 1 -> 2
    draw_arrow(draw, (240, 290), (285, 290), color="#0078D4", width=3)

    # Zone 2: Central Transit Hub (Center)
    draw_rounded_rect(draw, (285, 146, 565, 434), radius=10, fill="#FFFFFF", outline="#0078D4", width=2)
    draw_rounded_rect(draw, (285, 146, 565, 180), radius=10, fill="#0078D4")
    draw.rectangle((285, 168, 565, 180), fill="#0078D4")
    draw.text((300, 155), "2. TRANSIT HUB VNET (10.0.0.0/16)", fill="#FFFFFF", font=f_badge)

    hub_boxes = [
        ("Azure Firewall Premium", "Central 0.0.0.0/0 Egress Inspection\nPrivate IP: 10.0.1.4 (UDR Next Hop)", "#EFF6FF", "#1D4ED8"),
        ("Azure Bastion Host", "Zero-Public IP Secure Browser Ingress\nEncrypted SSH & RDP Jumpbox", "#F8FAFC", "#0F172A"),
        ("Private DNS Resolver", "Centralized Private Link Resolution\nPrevents Split-Brain DNS across Spokes", "#ECFDF5", "#047857")
    ]
    y_h = 196
    for hb_t, hb_d, hb_bg, hb_col in hub_boxes:
        draw_rounded_rect(draw, (300, y_h, 550, y_h + 68), radius=6, fill=hb_bg, outline="#E2E8F0", width=1)
        draw.text((312, y_h + 10), hb_t, fill=hb_col, font=get_font(FONT_BOLD, 15))
        draw.text((312, y_h + 32), hb_d, fill="#475569", font=f_body)
        y_h += 76

    # Arrow 2 -> 3A & 3B
    draw_arrow(draw, (565, 220), (610, 220), color="#059669", width=3)
    draw_arrow(draw, (565, 360), (610, 360), color="#7C3AED", width=3)

    # Zone 3A: Workload Spoke (Right Top)
    draw_rounded_rect(draw, (610, 152, 904, 280), radius=10, fill="#FFFFFF", outline="#059669", width=1.5)
    draw_rounded_rect(draw, (610, 152, 904, 184), radius=10, fill="#059669")
    draw.rectangle((610, 172, 904, 184), fill="#059669")
    draw.text((625, 160), "3A. WORKLOAD SPOKE (10.1.0.0/16)", fill="#FFFFFF", font=f_badge)
    draw.text((625, 196), "AKS & Application Tier", fill="#0F172A", font=f_title)
    draw.text((625, 224), "• UDR default 0.0.0.0/0 -> Firewall\n• Bidirectional VNet Peering to Hub", fill="#475569", font=f_body)

    # Zone 3B: AI & Data Spoke (Right Bottom)
    draw_rounded_rect(draw, (610, 300, 904, 428), radius=10, fill="#FFFFFF", outline="#7C3AED", width=1.5)
    draw_rounded_rect(draw, (610, 300, 904, 332), radius=10, fill="#7C3AED")
    draw.rectangle((610, 320, 904, 332), fill="#7C3AED")
    draw.text((625, 308), "3B. DATA PLATFORM SPOKE", fill="#FFFFFF", font=f_badge)
    draw.text((625, 344), "Private PaaS & Databases", fill="#0F172A", font=f_title)
    draw.text((625, 372), "• Zero Public IPs on Database Subnets\n• Private Endpoints & CMK Encryption", fill="#475569", font=f_body)

    # Footer Row inside Card
    draw_rounded_rect(draw, (36, 472, 420, 514), radius=8, fill="#ECFDF5", outline="#A7F3D0", width=1)
    draw_check_badge(draw, 50, 484, size=18, color="#059669")
    draw.text((76, 485), "Verified: CAF Egress Standards (CI Validated)", fill="#065F46", font=get_font(FONT_BOLD, 13))

    f_tag = get_font(FONT_BOLD, 12)
    tags = ["Azure Firewall", "Hub & Spoke", "UDR 0.0.0.0/0", "Azure Bastion"]
    x_tag = 438
    for t in tags:
        tw = int(draw.textlength(t, font=f_tag)) + 18
        draw_rounded_rect(draw, (x_tag, 476, x_tag + tw, 510), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
        draw.text((x_tag + 9, 485), t, fill="#334155", font=f_tag)
        x_tag += tw + 10

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

    # Base Card
    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=16, fill="#FFFFFF", outline="#E2E8F0", width=2)
    # Top Accent Line
    draw_rounded_rect(draw, (36, 12, 200, 16), radius=2, fill="#E11D48")

    # Eyebrow Pill
    draw_rounded_rect(draw, (36, 28, 280, 54), radius=12, fill="#FFF1F2", outline="#FECDD3", width=1)
    draw.text((48, 33), "CONTINUOUS DELIVERY & SECURITY", fill="#BE123C", font=get_font(FONT_BOLD, 12))

    # Title & Subtitle
    draw.text((36, 62), "Azure AKS DevSecOps Automated Pipeline", fill="#0F172A", font=get_font(FONT_BOLD, 26))
    draw.text((36, 96), "Checkov SAST · TFLint · Trivy Container CVEs · Azure OIDC Workload ID · Hardened AKS", fill="#475569", font=get_font(FONT_REGULAR, 15))

    # Diagram Canvas
    diag_box = (36, 128, w - 36, 452)
    draw_rounded_rect(draw, diag_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    f_title = get_font(FONT_BOLD, 15)
    f_body = get_font(FONT_REGULAR, 13)
    f_badge = get_font(FONT_BOLD, 11)

    stages = [
        ("STAGE 1", "Developer PR", "• GitHub Pull Request\n• Branch Protection\n• Mandatory Sign-off", "#0F172A", (56, 152, 235, 428)),
        ("STAGE 2", "Pre-Flight Lint", "• TFLint Syntax Check\n• Gitleaks Interception\n• terraform fmt check", "#0284C7", (265, 152, 445, 428)),
        ("STAGE 3", "Shift-Left SAST", "• Checkov Security Scan\n• tfsec CIS Benchmarks\n• Automated Policy Gate", "#E11D48", (475, 152, 655, 428)),
        ("STAGE 4", "AKS Cloud Delivery", "• Trivy Container Scan\n• Distroless Docker Build\n• NetworkPolicy Rollout", "#059669", (685, 152, 904, 428))
    ]

    for st_num, st_name, st_desc, st_col, coords in stages:
        draw_rounded_rect(draw, coords, radius=10, fill="#FFFFFF", outline=st_col, width=1.5)
        draw_rounded_rect(draw, (coords[0], coords[1], coords[2], coords[1] + 32), radius=10, fill=st_col)
        draw.rectangle((coords[0], coords[1] + 20, coords[2], coords[1] + 32), fill=st_col)
        draw.text((coords[0] + 12, coords[1] + 8), st_num, fill="#FFFFFF", font=f_badge)
        draw.text((coords[0] + 12, coords[1] + 48), st_name, fill="#0F172A", font=f_title)
        draw.text((coords[0] + 12, coords[1] + 80), st_desc, fill="#475569", font=f_body)

    # Draw Arrows between stages
    draw_arrow(draw, (235, 290), (265, 290), color="#64748B", width=2.5)
    draw_arrow(draw, (445, 290), (475, 290), color="#64748B", width=2.5)
    draw_arrow(draw, (655, 290), (685, 290), color="#64748B", width=2.5)

    # Footer Row inside Card
    draw_rounded_rect(draw, (36, 472, 420, 514), radius=8, fill="#ECFDF5", outline="#A7F3D0", width=1)
    draw_check_badge(draw, 50, 484, size=18, color="#059669")
    draw.text((76, 485), "Verified: End-to-End Pipeline Passed (CI Validated)", fill="#065F46", font=get_font(FONT_BOLD, 13))

    f_tag = get_font(FONT_BOLD, 12)
    tags = ["Checkov SAST", "Trivy CVEs", "Azure AKS", "GitHub Actions"]
    x_tag = 438
    for t in tags:
        tw = int(draw.textlength(t, font=f_tag)) + 18
        draw_rounded_rect(draw, (x_tag, 476, x_tag + tw, 510), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
        draw.text((x_tag + 9, 485), t, fill="#334155", font=f_tag)
        x_tag += tw + 10

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

    # Base Card
    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=16, fill="#FFFFFF", outline="#E2E8F0", width=2)
    # Top Accent Line
    draw_rounded_rect(draw, (36, 12, 200, 16), radius=2, fill="#0284C7")

    # Eyebrow Pill
    draw_rounded_rect(draw, (36, 28, 280, 54), radius=12, fill="#F0F9FF", outline="#BAE6FD", width=1)
    draw.text((48, 33), "REUSABLE INFRASTRUCTURE AS CODE", fill="#0369A1", font=get_font(FONT_BOLD, 12))

    # Title & Subtitle
    draw.text((36, 62), "Terraform Azure Reusable Resource Modules", fill="#0F172A", font=get_font(FONT_BOLD, 26))
    draw.text((36, 96), "11+ Decoupled Child Modules · Implicit Dependency Pipelines · Multi-Environment Support", fill="#475569", font=get_font(FONT_REGULAR, 15))

    # Diagram Canvas
    diag_box = (36, 128, w - 36, 452)
    draw_rounded_rect(draw, diag_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    f_title = get_font(FONT_BOLD, 16)
    f_body = get_font(FONT_REGULAR, 13)
    f_badge = get_font(FONT_BOLD, 11)

    # Left Box: Consumer Environments
    draw_rounded_rect(draw, (56, 152, 250, 428), radius=10, fill="#FFFFFF", outline="#CBD5E1", width=1.5)
    draw_rounded_rect(draw, (56, 152, 250, 184), radius=10, fill="#0F172A")
    draw.rectangle((56, 172, 250, 184), fill="#0F172A")
    draw.text((70, 160), "ROOT CONSUMER LAYERS", fill="#FFFFFF", font=f_badge)
    draw.text((70, 202), "Environments", fill="#0F172A", font=f_title)
    draw.text((70, 230), "• environments/dev\n• environments/prod\n• Strict input variables\n• Remote Blob State Lock", fill="#475569", font=f_body)

    draw_rounded_rect(draw, (70, 365, 236, 395), radius=6, fill="#F1F5F9")
    draw.text((78, 372), "Zero Hardcoded Values", fill="#334155", font=f_badge)

    # Arrow Left -> Center
    draw_arrow(draw, (250, 290), (295, 290), color="#0284C7", width=3)

    # Center Box: 11 Child Modules Grid
    draw_rounded_rect(draw, (295, 146, 640, 434), radius=10, fill="#FFFFFF", outline="#0284C7", width=2)
    draw_rounded_rect(draw, (295, 146, 640, 180), radius=10, fill="#0284C7")
    draw.rectangle((295, 168, 640, 180), fill="#0284C7")
    draw.text((310, 155), "11+ ENTERPRISE CHILD MODULES LIBRARY", fill="#FFFFFF", font=f_badge)

    mod_categories = [
        ("Network Tier", "azurerm_vnet, subnet, nsg, nsg_association, public_ip", "#EFF6FF", "#1D4ED8"),
        ("Compute Tier", "azurerm_linux_virtual_machine, nic, bastion_host", "#F0FDF4", "#15803D"),
        ("Security & Edge", "azurerm_key_vault, application_gateway, resource_group", "#FAF5FF", "#7E22CE")
    ]
    y_m = 196
    for mc_t, mc_d, mc_bg, mc_col in mod_categories:
        draw_rounded_rect(draw, (310, y_m, 625, y_m + 68), radius=6, fill=mc_bg, outline="#E2E8F0", width=1)
        draw.text((322, y_m + 10), mc_t, fill=mc_col, font=get_font(FONT_BOLD, 15))
        draw.text((322, y_m + 32), mc_d, fill="#475569", font=f_body)
        y_m += 76

    # Arrow Center -> Right
    draw_arrow(draw, (640, 290), (680, 290), color="#059669", width=3)

    # Right Box: Architectural Standards
    draw_rounded_rect(draw, (680, 152, 904, 428), radius=10, fill="#FFFFFF", outline="#059669", width=1.5)
    draw_rounded_rect(draw, (680, 152, 904, 184), radius=10, fill="#059669")
    draw.rectangle((680, 172, 904, 184), fill="#059669")
    draw.text((695, 160), "ARCHITECTURAL STANDARDS", fill="#FFFFFF", font=f_badge)
    draw.text((695, 202), "Design Principles", fill="#0F172A", font=f_title)
    draw.text((695, 230), "• Implicit dependencies\n  (no depends_on anti-patterns)\n• Dynamic blocks for optional rules\n• Reusable outputs contract\n• Automated TFLint CI gates", fill="#475569", font=f_body)

    # Footer Row inside Card
    draw_rounded_rect(draw, (36, 472, 420, 514), radius=8, fill="#ECFDF5", outline="#A7F3D0", width=1)
    draw_check_badge(draw, 50, 484, size=18, color="#059669")
    draw.text((76, 485), "Verified: TFLint & Plan Matrix Passed (CI Validated)", fill="#065F46", font=get_font(FONT_BOLD, 13))

    f_tag = get_font(FONT_BOLD, 12)
    tags = ["Terraform 1.9+", "11 Child Modules", "State Locking", "AzureRM"]
    x_tag = 438
    for t in tags:
        tw = int(draw.textlength(t, font=f_tag)) + 18
        draw_rounded_rect(draw, (x_tag, 476, x_tag + tw, 510), radius=6, fill="#F1F5F9", outline="#E2E8F0", width=1)
        draw.text((x_tag + 9, 485), t, fill="#334155", font=f_tag)
        x_tag += tw + 10

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
    draw_rounded_rect(draw, (12, 12, w - 12, h - 12), radius=16, fill="#FFFFFF", outline="#E2E8F0", width=2)

    # Window Header Bar (dark terminal aesthetic)
    draw_rounded_rect(draw, (12, 12, w - 12, 60), radius=16, fill="#0F172A")
    draw.rectangle((12, 42, w - 12, 60), fill="#0F172A")

    # Traffic light dots
    draw.ellipse((32, 28, 44, 40), fill="#EF4444")
    draw.ellipse((52, 28, 64, 40), fill="#F59E0B")
    draw.ellipse((72, 28, 84, 40), fill="#10B981")

    # Header title
    draw.text((105, 25), "PLATFORM ARCHITECTURE & ENGINEERING REEL // SANJEEV SINGH", fill="#38BDF8", font=get_font(FONT_BOLD, 13))

    # Header badges
    draw_rounded_rect(draw, (w - 230, 22, w - 120, 46), radius=6, fill="#082F49", outline="#0284C7", width=1)
    draw.text((w - 218, 28), "SYSTEM REEL", fill="#38BDF8", font=get_font(FONT_BOLD, 11))

    draw_rounded_rect(draw, (w - 110, 22, w - 32, 46), radius=6, fill="#1E293B")
    draw.text((w - 100, 28), "1080p HD", fill="#E2E8F0", font=get_font(FONT_BOLD, 11))

    # Inner Video Preview Canvas
    vid_box = (36, 80, w - 36, 462)
    draw_rounded_rect(draw, vid_box, radius=12, fill="#F8FAFC", outline="#E2E8F0", width=1)

    # 4 Architectural Pillars Preview Grid
    pillars = [
        ("Azure Landing Zones", "CAF Hub & Spoke · Azure Firewall · Bastion · UDR 0.0.0.0/0", "#0078D4", (56, 100, 460, 245)),
        ("Modular Terraform", "11+ Reusable Child Modules · State Lease Locking · No Drift", "#7C3AED", (500, 100, 904, 245)),
        ("Shift-Left DevSecOps", "Checkov SAST · TFLint · Trivy CVEs · Azure OIDC Workload ID", "#E11D48", (56, 265, 460, 410)),
        ("Enterprise GenAI", "Azure OpenAI · APIM AI Gateway · Vector RAG Grounding", "#059669", (500, 265, 904, 410))
    ]

    for p_title, p_desc, p_accent, coords in pillars:
        draw_rounded_rect(draw, coords, radius=8, fill="#FFFFFF", outline="#E2E8F0", width=1)
        draw_rounded_rect(draw, (coords[0], coords[1], coords[0] + 6, coords[3]), radius=3, fill=p_accent)
        draw.text((coords[0] + 20, coords[1] + 20), p_title, fill="#0F172A", font=get_font(FONT_BOLD, 17))
        draw.text((coords[0] + 20, coords[1] + 52), p_desc, fill="#64748B", font=get_font(FONT_REGULAR, 13))
        draw_rounded_rect(draw, (coords[0] + 20, coords[1] + 92, coords[0] + 180, coords[1] + 120), radius=4, fill="#F1F5F9")
        draw.text((coords[0] + 28, coords[1] + 98), "Production Validated", fill="#334155", font=get_font(FONT_BOLD, 11))

    # High-Impact Centered Play Button Overlay
    cx, cy = w // 2, 260
    # Semi-transparent dark container
    draw_rounded_rect(draw, (cx - 200, cy - 65, cx + 200, cy + 65), radius=16, fill="#0F172ACC", outline="#0078D4", width=2)

    # Play Icon Circle
    draw.ellipse((cx - 36, cy - 50, cx + 36, cy + 22), fill="#0078D4", outline="#38BDF8", width=2)
    # Triangle Play
    draw.polygon([(cx - 10, cy - 30), (cx - 10, cy + 2), (cx + 18, cy - 14)], fill="#FFFFFF")

    # Button Text
    draw.text((cx - 140, cy + 30), "Watch Architecture Reel (00:20)", fill="#FFFFFF", font=get_font(FONT_BOLD, 15))

    # Bottom Console / Player Status Bar
    draw_rounded_rect(draw, (36, 480, w - 36, 520), radius=8, fill="#0F172A")
    draw_check_badge(draw, 50, 491, size=18, color="#059669")
    draw.text((78, 492), "Interactive Player Online: sanjeevsingh.oneps.in", fill="#E2E8F0", font=get_font(FONT_BOLD, 12))
    draw.text((w - 290, 492), "Click Thumbnail to Launch Player →", fill="#38BDF8", font=get_font(FONT_BOLD, 12))

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
