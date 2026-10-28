#!/usr/bin/env python3
"""
Cloud Engineering Master Video Production Engine (Updated Edition)
Creative Direction: Cinematic Futuristic · 90 Seconds · 16:9 Master · Indian Male Deep AI Narration (en-IN-PrabhatNeural)
Updates:
1. Natural deep Indian male voice in his 30s (en-IN-PrabhatNeural @ -4Hz, +6% rate)
2. Removed all OnePS branding from video images completely
3. Featured handsome Indian male engineer portrait in Scene 02 (The Engineer)
"""

import os
import sys
import math
import asyncio
import subprocess
import wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

WIDTH = 1920
HEIGHT = 1080
FPS = 30
SAMPLE_RATE = 48000
TOTAL_DURATION = 90.0
TOTAL_FRAMES = int(FPS * TOTAL_DURATION)
TOTAL_SAMPLES = int(SAMPLE_RATE * TOTAL_DURATION)

FFMPEG_BIN = "/Users/sanjeevsingh/.local/bin/ffmpeg"
WORKSPACE_DIR = "/Users/sanjeevsingh/DevOps/sanjiivsingh"
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets")
SCRIPTS_DIR = os.path.join(WORKSPACE_DIR, "scripts")
CAPTIONS_DIR = os.path.join(WORKSPACE_DIR, "docs")
DOCKER_SHOWREEL_DIR = "/Users/sanjeevsingh/DevOps/Docker/sanjeevsingh.oneps.in/video-showreel"

OUTPUT_MP4 = os.path.join(ASSETS_DIR, "intro.mp4")
OUTPUT_POSTER = os.path.join(ASSETS_DIR, "showreel_poster.jpg")
OUTPUT_WEBP = os.path.join(ASSETS_DIR, "intro_preview.webp")
OUTPUT_WAV = "/tmp/master_soundtrack_90s.wav"

# Fonts
FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36, index=1)
FONT_SUBTITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20, index=0)
FONT_MONO = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 16, index=0)
FONT_MONO_BOLD = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 16, index=1)
FONT_MONO_CODE = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 18, index=0)
FONT_BRAND_NAME = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 62, index=1)
FONT_BRAND_ROLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 25, index=1)
FONT_QUOTE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22, index=2)

# Color Palette (Deep Navy / Electric Cyan / Emerald Green / Amber Gold)
CYAN_ACCENT = (0, 210, 255)
GREEN_ACCENT = (0, 255, 180)
GOLD_ACCENT = (255, 205, 85)
TEXT_WHITE = (255, 255, 255)
TEXT_MUTED = (180, 205, 230)
BORDER_CYAN = (0, 210, 255, 120)
PANEL_BG = (8, 14, 28, 230)

SCENES = [
    {
        "id": "scene_01",
        "num": 1,
        "name": "THE DIGITAL HORIZON",
        "duration": 5.0,
        "title": "BUILD. SECURE. SCALE.",
        "subtitle": "Enterprise Cloud Infrastructure · Platform Automation",
        "overlay": "From Cloud Complexity to Engineering Confidence",
        "tags": ["GLOBAL TRANSIT", "AZURE CLOUD", "TERRAFORM IaC"],
        "base_key": "globe",
        "motion": "zoom_in"
    },
    {
        "id": "scene_02",
        "num": 2,
        "name": "THE ENGINEER",
        "duration": 7.0,
        "title": "SANJEEV SINGH / DEVOPS & CLOUD ARCHITECT",
        "subtitle": "Turning cloud complexity into practical, repeatable engineering solutions.",
        "overlay": "Senior DevOps & Cloud Architecture Consultant",
        "tags": ["10+ YRS GOVERNANCE", "5+ YRS AZURE & IaC", "ZERO-TRUST DEFENSE"],
        "base_key": "engineer",
        "motion": "pan_right"
    },
    {
        "id": "scene_03",
        "num": 3,
        "name": "THE CLOUD JOURNEY",
        "duration": 8.0,
        "title": "FROM COMPLEXITY TO CLARITY",
        "subtitle": "Eliminating manual, fragmented operations with codified cloud architecture.",
        "overlay": "Harmonizing fragmented operations into repeatable systems",
        "tags": ["MANUAL → CODIFIED", "ZERO CONFIG DRIFT", "ENTERPRISE MESH"],
        "base_key": "network",
        "motion": "drift"
    },
    {
        "id": "scene_04",
        "num": 4,
        "name": "INFRASTRUCTURE AS CODE",
        "duration": 7.0,
        "title": "TERRAFORM / REUSABLE MODULES / REPEATABLE INFRASTRUCTURE",
        "subtitle": "From Azure infrastructure to reusable Terraform modules, environments become consistent.",
        "overlay": "Reusable infrastructure. Consistent deployments.",
        "tags": ["MODULAR HCL", "STATE LEASE LOCKING", "ZERO DRIFT"],
        "base_key": "code_bg",
        "motion": "zoom_in"
    },
    {
        "id": "scene_05",
        "num": 5,
        "name": "AZURE ARCHITECTURE",
        "duration": 7.0,
        "title": "AZURE CLOUD FOUNDATIONS",
        "subtitle": "Secure multi-subscription landing zones with centralized transit firewall and private endpoints.",
        "overlay": "Designed around real workloads.",
        "tags": ["HUB-AND-SPOKE VNets", "AZURE FIREWALL", "PRIVATE LINK", "CAF COMPLIANT"],
        "base_key": "network",
        "motion": "pan_left_to_right"
    },
    {
        "id": "scene_06",
        "num": 6,
        "name": "CI/CD IN MOTION",
        "duration": 7.0,
        "title": "AUTOMATE THE PATH TO PRODUCTION",
        "subtitle": "With automated pipelines, validation, security checks, and controlled deployments.",
        "overlay": "Automated workflows. Controlled changes.",
        "tags": ["GITHUB ACTIONS", "AZURE DEVOPS", "CONTROLLED GATES"],
        "base_key": "pipeline",
        "motion": "pan_right"
    },
    {
        "id": "scene_07",
        "num": 7,
        "name": "QUALITY GATES",
        "duration": 6.0,
        "title": "VALIDATE. REVIEW. DEPLOY.",
        "subtitle": "Automated scan output and approval gates guarantee zero vulnerabilities reach production.",
        "overlay": "Validate early. Review intelligently.",
        "tags": ["TFLINT", "CHECKOV SAST", "TFSEC", "GITLEAKS"],
        "base_key": "pipeline",
        "motion": "zoom_in"
    },
    {
        "id": "scene_08",
        "num": 8,
        "name": "MODERN WORKLOADS",
        "duration": 7.0,
        "title": "CONTAINERS / ORCHESTRATION / SCALABILITY",
        "subtitle": "From networking and compute to containers, identity, and secrets management.",
        "overlay": "Production Kubernetes & Microservices.",
        "tags": ["AZURE KUBERNETES SERVICE", "WORKLOAD IDENTITY", "HPA AUTOSCALING"],
        "base_key": "cloud",
        "motion": "pull_back"
    },
    {
        "id": "scene_09",
        "num": 9,
        "name": "SECURITY BY DESIGN",
        "duration": 8.0,
        "title": "SECURE FOUNDATIONS. CONTROLLED ACCESS.",
        "subtitle": "Building secure foundations with least-privilege RBAC, secret protection, and policy enforcement.",
        "overlay": "Defense-in-depth & Least-Privilege Governance.",
        "tags": ["ZERO TRUST", "ENTRA ID OIDC", "KEY VAULT HSM", "POLICY AUDIT"],
        "base_key": "cloud",
        "motion": "drift"
    },
    {
        "id": "scene_10",
        "num": 10,
        "name": "OPERATIONAL VISIBILITY",
        "duration": 8.0,
        "title": "OBSERVE. TROUBLESHOOT. IMPROVE.",
        "subtitle": "And beyond deployment, the goal is clear: improve visibility, simplify operations.",
        "overlay": "Continuous monitoring & Proactive incident reduction.",
        "tags": ["AZURE MONITOR", "LOG ANALYTICS", "PROMETHEUS", "DISTRIBUTED TRACING"],
        "base_key": "cloud",
        "motion": "pan_right"
    },
    {
        "id": "scene_11",
        "num": 11,
        "name": "BUSINESS OUTCOMES",
        "duration": 10.0,
        "title": "CONSISTENCY / VISIBILITY / CONTROL",
        "subtitle": "Transforming fragmented operations into scalable cloud platforms that grow with your business.",
        "overlay": "Scalable cloud engineering that grows with your business.",
        "tags": ["ZERO DRIFT", "FINOPS OPTIMIZATION", "SUSTAINABLE SCALE"],
        "base_key": "network",
        "motion": "zoom_in"
    },
    {
        "id": "scene_12",
        "num": 12,
        "name": "PLATFORM ENGINEERING FINALE",
        "duration": 10.0,
        "title": "SANJEEV SINGH — BUILD. SECURE. SCALE.",
        "subtitle": "One point for your cloud engineering journey.",
        "overlay": "From Cloud Complexity to Engineering Confidence",
        "tags": ["AZURE CLOUD", "MODULAR TERRAFORM", "DEVSECOPS", "KUBERNETES"],
        "base_key": "endcard",
        "motion": "breathe"
    }
]

TAKES = [
    {
        "id": "take1_opening",
        "start": 0.5,
        "text": "Every great digital idea needs more than code. It needs a cloud foundation built to perform, adapt, and grow."
    },
    {
        "id": "take2_intro",
        "start": 10.5,
        "text": "I'm Sanjeev Singh, a DevOps and cloud engineer. Through OnePS, I help businesses turn cloud complexity into practical engineering solutions."
    },
    {
        "id": "take3_iac",
        "start": 22.5,
        "text": "From Azure infrastructure to reusable Terraform modules, I help make environments consistent, repeatable, and easier to manage."
    },
    {
        "id": "take4_cicd",
        "start": 34.5,
        "text": "With automated pipelines, validation, security checks, and controlled deployments, infrastructure changes become more predictable and easier to review."
    },
    {
        "id": "take5_arch_sec",
        "start": 47.5,
        "text": "From networking and compute to containers, identity, and secrets management, I focus on building secure foundations that support real workloads."
    },
    {
        "id": "take6_ops",
        "start": 61.5,
        "text": "And beyond deployment, the goal is clear: improve visibility, simplify operations, and create room for sustainable growth."
    },
    {
        "id": "take7_invite",
        "start": 72.5,
        "text": "Whether you're launching a startup, modernizing infrastructure, or improving your delivery workflows, let's build your next cloud milestone together. OnePS. One point for your cloud engineering journey."
    }
]

async def synthesize_all_narration_takes(temp_dir="/tmp/oneps_audio_indian"):
    import edge_tts
    os.makedirs(temp_dir, exist_ok=True)
    voice_track = np.zeros(TOTAL_SAMPLES, dtype=np.float32)
    
    print("Synthesizing voice narration with deep Indian male neural voice (en-IN-PrabhatNeural)...")
    for take in TAKES:
        mp3_p = os.path.join(temp_dir, f"{take['id']}.mp3")
        wav_p = os.path.join(temp_dir, f"{take['id']}.wav")
        
        # Deep Indian male in his 30s
        tts = edge_tts.Communicate(text=take["text"], voice="en-IN-PrabhatNeural", rate="+6%", pitch="-4Hz")
        await tts.save(mp3_p)
        
        # Convert to 48kHz mono WAV with rich broadcast EQ (subtle warm bass boost + crisp clarity)
        cmd_ff = [
            FFMPEG_BIN, "-y", "-i", mp3_p,
            "-af", "highpass=f=75,equalizer=f=180:t=q:w=1.0:g=2.0,equalizer=f=3200:t=q:w=1.2:g=2.2,alimiter=limit=0.95",
            "-ar", str(SAMPLE_RATE), "-ac", "1", wav_p
        ]
        subprocess.run(cmd_ff, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        with wave.open(wav_p, "rb") as wf:
            data = wf.readframes(wf.getnframes())
            samples = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
            
        start_idx = int(take["start"] * SAMPLE_RATE)
        end_idx = min(start_idx + len(samples), TOTAL_SAMPLES)
        length = end_idx - start_idx
        voice_track[start_idx:end_idx] += samples[:length] * 0.96
        
    return voice_track

def generate_soundtrack():
    print(f"Synthesizing 90-second soundtrack with dynamic ducking...")
    # 1. Voice
    voice_track = asyncio.run(synthesize_all_narration_takes())

    # 2. Cinematic Music Bed
    left = np.zeros(TOTAL_SAMPLES, dtype=np.float32)
    right = np.zeros(TOTAL_SAMPLES, dtype=np.float32)
    
    chords = [
        (0.0, 10.0, [65.41, 130.81, 155.56, 196.00, 261.63, 311.13]),
        (10.0, 20.0, [51.91, 103.83, 130.81, 155.56, 207.65, 261.63]),
        (20.0, 34.0, [77.78, 155.56, 196.00, 233.08, 311.13, 392.00]),
        (34.0, 47.0, [58.27, 116.54, 146.83, 174.61, 233.08, 293.66]),
        (47.0, 55.0, [43.65, 87.31, 130.81, 155.56, 174.61, 261.63]),
        (55.0, 70.0, [65.41, 130.81, 155.56, 196.00, 233.08, 261.63]),
        (70.0, 80.0, [51.91, 103.83, 130.81, 155.56, 207.65, 261.63, 311.13]),
        (80.0, 85.0, [58.27, 116.54, 146.83, 174.61, 233.08, 293.66, 349.23]),
        (85.0, 90.0, [65.41, 130.81, 196.00, 261.63, 329.63, 392.00, 523.25])
    ]
    
    for start_t, end_t, freqs in chords:
        if start_t >= TOTAL_DURATION:
            continue
        actual_end = min(end_t, TOTAL_DURATION)
        idx_s = int(start_t * SAMPLE_RATE)
        idx_e = int(actual_end * SAMPLE_RATE)
        dur = actual_end - start_t
        t_chord = np.linspace(0, dur, idx_e - idx_s, endpoint=False)
        
        attack = min(1.5, dur * 0.25)
        release = min(2.5, dur * 0.3)
        env = np.ones_like(t_chord)
        att_idx = int(attack * SAMPLE_RATE)
        rel_idx = int(release * SAMPLE_RATE)
        if att_idx > 0:
            env[:att_idx] = 0.5 * (1 - np.cos(np.pi * np.linspace(0, 1, att_idx)))
        if rel_idx > 0:
            env[-rel_idx:] = 0.5 * (1 + np.cos(np.pi * np.linspace(0, 1, rel_idx)))
            
        for i, f in enumerate(freqs):
            detune_l = np.sin(2 * np.pi * (f - 0.22) * t_chord)
            detune_r = np.sin(2 * np.pi * (f + 0.22) * t_chord)
            harm_l = 0.25 * np.sin(4 * np.pi * f * t_chord)
            harm_r = 0.25 * np.sin(4 * np.pi * f * t_chord)
            amp = (0.09 / (1 + 0.35 * i))
            left[idx_s:idx_e] += (detune_l + harm_l) * env * amp
            right[idx_s:idx_e] += (detune_r + harm_r) * env * amp

    # Transition braams
    scene_starts = [0.0, 5.0, 12.0, 20.0, 27.0, 34.0, 41.0, 47.0, 54.0, 62.0, 70.0, 80.0]
    for t_imp in scene_starts:
        if t_imp >= TOTAL_DURATION - 2.0:
            continue
        imp_dur = min(4.0, TOTAL_DURATION - t_imp)
        idx_s = int(t_imp * SAMPLE_RATE)
        idx_e = idx_s + int(imp_dur * SAMPLE_RATE)
        t_imp_arr = np.linspace(0, imp_dur, idx_e - idx_s, endpoint=False)
        
        freq_pitch = 60.0 * np.exp(-t_imp_arr * 1.6) + 30.0
        phase = 2 * np.pi * np.cumsum(freq_pitch) / SAMPLE_RATE
        env_imp = np.exp(-t_imp_arr * 0.95)
        
        sub = 0.35 * np.sin(phase) * env_imp
        sat = 0.12 * np.sin(phase * 2) * env_imp
        noise = (np.random.rand(len(t_imp_arr)) * 2 - 1) * np.exp(-t_imp_arr * 16.0) * 0.10
        left[idx_s:idx_e] += (sub + sat + noise)
        right[idx_s:idx_e] += (sub + sat + noise)

    # Rhythmic Pulses
    beat_step = 0.3
    for b in np.arange(10.0, 85.0, beat_step):
        idx_b = int(b * SAMPLE_RATE)
        tick_len = int(0.04 * SAMPLE_RATE)
        if idx_b + tick_len > TOTAL_SAMPLES:
            break
        t_tick = np.linspace(0, 0.04, tick_len, endpoint=False)
        tick_env = np.exp(-t_tick * 85.0)
        pan = 0.25 * np.sin(2 * np.pi * b * 0.3)
        pitch = 2200 if int(b / beat_step) % 2 == 0 else 3300
        tick_wave = 0.035 * np.sin(2 * np.pi * pitch * t_tick) * tick_env
        left[idx_b:idx_b + tick_len] += tick_wave * (0.5 - pan)
        right[idx_b:idx_b + tick_len] += tick_wave * (0.5 + pan)

    # Resolution Chime
    chime_start = 85.0
    idx_c_s = int(chime_start * SAMPLE_RATE)
    idx_c_e = TOTAL_SAMPLES
    t_chime = np.linspace(0, (idx_c_e - idx_c_s)/SAMPLE_RATE, idx_c_e - idx_c_s, endpoint=False)
    chime_env = np.exp(-t_chime * 0.5)
    for cf in [523.25, 659.25, 783.99, 1046.50, 1318.51]:
        chime_w = 0.05 * np.sin(2 * np.pi * cf * t_chime) * chime_env
        left[idx_c_s:idx_c_e] += chime_w
        right[idx_c_s:idx_c_e] += chime_w

    # Dynamic speech ducking
    window_size = int(0.05 * SAMPLE_RATE)
    envelope = np.convolve(np.abs(voice_track), np.ones(window_size) / window_size, mode='same')
    speech_active = (envelope > 0.015).astype(np.float32)
    
    duck_gain = np.ones(TOTAL_SAMPLES, dtype=np.float32)
    curr_gain = 1.0
    att_coeff = 1.0 - np.exp(-1.0 / (0.15 * SAMPLE_RATE))
    rel_coeff = 1.0 - np.exp(-1.0 / (0.40 * SAMPLE_RATE))
    for i in range(TOTAL_SAMPLES):
        target = 0.20 if speech_active[i] > 0.5 else 1.0
        curr_gain += (target - curr_gain) * (att_coeff if target < curr_gain else rel_coeff)
        duck_gain[i] = curr_gain
        
    master_l = left * duck_gain + voice_track * 1.25
    master_r = right * duck_gain + voice_track * 1.25
    peak = max(np.max(np.abs(master_l)), np.max(np.abs(master_r)), 1e-5)
    master_l = (master_l / peak) * 0.92
    master_r = (master_r / peak) * 0.92
    
    stereo = np.empty((TOTAL_SAMPLES, 2), dtype=np.int16)
    stereo[:, 0] = (master_l * 32767).astype(np.int16)
    stereo[:, 1] = (master_r * 32767).astype(np.int16)
    
    with wave.open(OUTPUT_WAV, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(stereo.tobytes())
    print("Soundtrack successfully exported to:", OUTPUT_WAV)

def load_base_graphics():
    print("Loading and preparing high-definition base visuals...")
    g_dir = os.path.join(DOCKER_SHOWREEL_DIR, "graphics")
    w_scaled = int(WIDTH * 1.15)
    h_scaled = int(HEIGHT * 1.15)
    
    def prep_img(path):
        if os.path.exists(path):
            im = Image.open(path).convert("RGB")
            im_large = im.resize((w_scaled, h_scaled), Image.Resampling.LANCZOS)
            return ImageEnhance.Sharpness(im_large).enhance(1.2)
        return Image.new("RGB", (w_scaled, h_scaled), (6, 12, 24))

    graphics = {
        "globe": prep_img(os.path.join(g_dir, "scene1_cloud_vision.jpg")),
        "engineer": prep_img(os.path.join(ASSETS_DIR, "handsome_engineer.jpg")),
        "code_bg": prep_img(os.path.join(g_dir, "scene2_terraform_iac.jpg")),
        "network": prep_img(os.path.join(g_dir, "scene3_landing_zones.jpg")),
        "pipeline": prep_img(os.path.join(g_dir, "scene4_devsecops_pipeline.jpg")),
        "cloud": prep_img(os.path.join(g_dir, "scene5_containers_aks.jpg")),
        "endcard": prep_img(os.path.join(g_dir, "scene6_brand_reveal.jpg"))
    }
    return graphics

def draw_hud_header(draw, sc_num, sc_name, current_time):
    # Top Bar - Zero OnePS branding
    draw.rectangle([(40, 32), (WIDTH - 40, 76)], fill=(7, 12, 26, 220), outline=(0, 210, 255, 80), width=1)
    draw.ellipse([(56, 49), (66, 59)], fill=GREEN_ACCENT)
    hdr_text = f"SCENE {sc_num:02d} // {sc_name}"
    draw.text((80, 45), hdr_text, font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
    
    mins = int(current_time // 60)
    secs = int(current_time % 60)
    fr = int((current_time - int(current_time)) * FPS)
    tc = f"TC {mins:02d}:{secs:02d}:{fr:02d} // 1080p 30fps // CLOUD PLATFORM ARCHITECTURE"
    draw.text((WIDTH - 530, 45), tc, font=FONT_MONO, fill=TEXT_MUTED)

def draw_corner_reticles(draw):
    ch = 18
    for x, y in [(40, 32), (WIDTH - 40, 32), (40, HEIGHT - 40), (WIDTH - 40, HEIGHT - 40)]:
        x_dir = 1 if x == 40 else -1
        y_dir = 1 if y == 32 else -1
        draw.line([(x, y), (x + x_dir * ch, y)], fill=(0, 210, 255, 200), width=2)
        draw.line([(x, y), (x, y + y_dir * ch)], fill=(0, 210, 255, 200), width=2)

def draw_lower_third(draw, title, subtitle, badges, quote_overlay=None):
    w = 1260
    h = 168 if quote_overlay else 152
    x0 = 60
    y0 = HEIGHT - h - 50
    x1 = x0 + w
    y1 = y0 + h
    
    draw.rectangle([(x0, y0), (x1, y1)], fill=PANEL_BG, outline=BORDER_CYAN, width=1)
    draw.rectangle([(x0, y0), (x0 + 6, y1)], fill=CYAN_ACCENT)
    
    draw.text((x0 + 32, y0 + 18), title, font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((x0 + 32, y0 + 68), subtitle, font=FONT_SUBTITLE, fill=TEXT_MUTED)
    
    if quote_overlay:
        draw.text((x0 + 32, y0 + 96), f'"{quote_overlay}"', font=FONT_QUOTE, fill=GREEN_ACCENT)
        tag_y = y0 + 130
    else:
        tag_y = y0 + 104
        
    tag_x = x0 + 32
    for b in badges:
        bbox = FONT_MONO.getbbox(b)
        bw = bbox[2] - bbox[0]
        draw.rectangle([(tag_x, tag_y), (tag_x + bw + 18, tag_y + 24)], fill=(14, 25, 50, 240), outline=(0, 220, 255, 110), width=1)
        draw.text((tag_x + 9, tag_y + 3), b, font=FONT_MONO, fill=GREEN_ACCENT)
        tag_x += bw + 28

def render_scene_overlay(sc, frame_in_scene, total_frames_sc, global_time):
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    
    draw_corner_reticles(d)
    draw_hud_header(d, sc["num"], sc["name"], global_time)
    
    prog = frame_in_scene / max(1, total_frames_sc - 1)
    
    # Custom scene visual centerpiece
    if sc["num"] == 2:
        # Scene 02: Handsome Engineer Reveal & Credential Card
        cx, cy = WIDTH // 2 + 250, HEIGHT // 2 - 25
        cw, ch = 820, 360
        d.rectangle([(cx - cw//2, cy - ch//2), (cx + cw//2, cy + ch//2)], fill=(7, 12, 26, 235), outline=(0, 210, 255, 140), width=2)
        d.line([(cx - cw//2, cy - ch//2), (cx + cw//2, cy - ch//2)], fill=GREEN_ACCENT, width=3)
        d.text((cx - cw//2 + 40, cy - ch//2 + 35), "SANJEEV SINGH", font=FONT_BRAND_NAME, fill=TEXT_WHITE)
        d.text((cx - cw//2 + 40, cy - ch//2 + 115), "SENIOR DEVOPS & AZURE CLOUD ARCHITECT", font=FONT_BRAND_ROLE, fill=CYAN_ACCENT)
        d.text((cx - cw//2 + 40, cy - ch//2 + 165), "Turning cloud complexity into practical, repeatable engineering solutions.", font=FONT_SUBTITLE, fill=TEXT_MUTED)
        d.rectangle([(cx - cw//2 + 40, cy - ch//2 + 215), (cx + cw//2 - 40, cy - ch//2 + 265)], fill=(12, 22, 45, 230), outline=(0, 180, 240, 100), width=1)
        d.text((cx - cw//2 + 55, cy - ch//2 + 228), "10+ YRS GOVERNANCE & ENGINEERING  |  5+ YRS AZURE & TERRAFORM", font=FONT_MONO_BOLD, fill=GREEN_ACCENT)

    elif sc["num"] == 4:
        # Scene 04: Real Terraform Code Window & Resource Graph
        code_x = 80
        code_y = 110
        code_w = 1100
        code_h = 570
        d.rectangle([(code_x, code_y), (code_x + code_w, code_y + code_h)], fill=(10, 15, 28, 245), outline=(0, 200, 255, 130), width=1)
        d.rectangle([(code_x, code_y), (code_x + code_w, code_y + 42)], fill=(14, 22, 40, 255))
        d.ellipse([(code_x + 18, code_y + 16), (code_x + 28, code_y + 26)], fill=(255, 95, 87))
        d.ellipse([(code_x + 36, code_y + 16), (code_x + 46, code_y + 26)], fill=(255, 189, 46))
        d.ellipse([(code_x + 54, code_y + 16), (code_x + 64, code_y + 26)], fill=(39, 201, 63))
        d.text((code_x + 85, code_y + 12), "modules/hub_network/main.tf — Production Terraform Blueprint", font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
        d.rectangle([(code_x + code_w - 280, code_y + 8), (code_x + code_w - 15, code_y + 34)], fill=(0, 60, 100, 200), outline=GREEN_ACCENT, width=1)
        d.text((code_x + code_w - 270, code_y + 13), "● STATE LEASE LOCKED (AZURE)", font=FONT_MONO, fill=GREEN_ACCENT)
        
        code_lines = [
            ('01', 'resource "azurerm_virtual_network" "hub" {', CYAN_ACCENT),
            ('02', '  name                = var.hub_vnet_name', TEXT_WHITE),
            ('03', '  location            = var.location', TEXT_WHITE),
            ('04', '  resource_group_name = var.resource_group_name', TEXT_WHITE),
            ('05', '  address_space       = ["10.0.0.0/16"]', GOLD_ACCENT),
            ('06', '  tags                = var.enterprise_governance_tags', TEXT_WHITE),
            ('07', '}', CYAN_ACCENT),
            ('08', '', TEXT_WHITE),
            ('09', 'resource "azurerm_subnet" "firewall" {', CYAN_ACCENT),
            ('10', '  name                 = "AzureFirewallSubnet"', GOLD_ACCENT),
            ('11', '  virtual_network_name = azurerm_virtual_network.hub.name', TEXT_WHITE),
            ('12', '  address_prefixes     = ["10.0.1.0/26"] # Dedicated Transit Route', GREEN_ACCENT),
            ('13', '}', CYAN_ACCENT),
            ('14', '', TEXT_WHITE),
            ('15', 'resource "azurerm_subnet" "gateway" {', CYAN_ACCENT),
            ('16', '  name                 = "GatewaySubnet"', GOLD_ACCENT),
            ('17', '  address_prefixes     = ["10.0.3.0/27"] # Hybrid VPN / ExpressRoute', GREEN_ACCENT),
            ('18', '}', CYAN_ACCENT),
        ]
        ly = code_y + 60
        for lnum, text, color in code_lines:
            d.text((code_x + 20, ly), lnum, font=FONT_MONO, fill=(100, 130, 160))
            d.text((code_x + 65, ly), text, font=FONT_MONO_CODE, fill=color)
            ly += 27

        side_x = code_x + code_w + 30
        side_w = WIDTH - side_x - 80
        d.rectangle([(side_x, code_y), (side_x + side_w, code_y + code_h)], fill=(10, 15, 28, 245), outline=(0, 200, 255, 130), width=1)
        d.rectangle([(side_x, code_y), (side_x + side_w, code_y + 42)], fill=(14, 22, 40, 255))
        d.text((side_x + 20, code_y + 12), "MODULE RESOURCE GRAPH", font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
        graph_items = [
            ("hub_vnet (10.0.0.0/16)", "ROOT TRANSIT"),
            ("AzureFirewallSubnet", "INSPECTION"),
            ("AzureBastionSubnet", "SECURE MGT"),
            ("GatewaySubnet", "HYBRID CONN"),
            ("UDR 0.0.0.0/0", "TRAFFIC FORCE")
        ]
        gy = code_y + 65
        for title, role in graph_items:
            d.rectangle([(side_x + 20, gy), (side_x + side_w - 20, gy + 52)], fill=(16, 26, 48, 240), outline=(0, 180, 230, 90), width=1)
            d.text((side_x + 35, gy + 9), title, font=FONT_MONO_BOLD, fill=TEXT_WHITE)
            d.text((side_x + 35, gy + 29), role, font=FONT_MONO, fill=GREEN_ACCENT)
            gy += 72

    elif sc["num"] == 5:
        # Scene 05: Azure Architecture CAF Hub-and-Spoke Matrix
        diag_x = 80
        diag_y = 110
        diag_w = 1760
        diag_h = 570
        d.rectangle([(diag_x, diag_y), (diag_x + diag_w, diag_y + diag_h)], fill=(8, 14, 28, 240), outline=(0, 210, 255, 140), width=1)
        d.rectangle([(diag_x, diag_y), (diag_x + diag_w, diag_y + 40)], fill=(14, 22, 40, 255))
        d.text((diag_x + 25, diag_y + 11), "AZURE ENTERPRISE CLOUD ADOPTION FRAMEWORK (CAF) // LANDING ZONE ARCHITECTURE", font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
        
        hub_w = 540
        hub_h = 440
        hx = diag_x + 80
        hy = diag_y + 75
        d.rectangle([(hx, hy), (hx + hub_w, hy + hub_h)], fill=(13, 22, 44, 240), outline=CYAN_ACCENT, width=2)
        d.rectangle([(hx, hy), (hx + hub_w, hy + 38)], fill=(0, 70, 120, 255))
        d.text((hx + 20, hy + 10), "CENTRAL HUB VNet (10.0.0.0/16)", font=FONT_MONO_BOLD, fill=TEXT_WHITE)
        
        hub_subnets = [
            ("Azure Firewall Core", "10.0.1.0/26", "Default Route Inspection 0.0.0.0/0", GREEN_ACCENT),
            ("Azure Bastion Host", "10.0.2.0/26", "Zero Public IP Jumpbox Admin", CYAN_ACCENT),
            ("GatewaySubnet (VPN/ER)", "10.0.3.0/27", "Encrypted Hybrid Site-to-Site", GOLD_ACCENT),
            ("Private DNS Zone Resolver", "10.0.4.0/28", "Split-Brain Resolution Mesh", TEXT_WHITE),
        ]
        s_y = hy + 55
        for sname, scidr, sdesc, scolor in hub_subnets:
            d.rectangle([(hx + 20, s_y), (hx + hub_w - 20, s_y + 75)], fill=(18, 30, 58, 240), outline=(0, 180, 240, 90), width=1)
            d.text((hx + 35, s_y + 12), f"{sname} ({scidr})", font=FONT_MONO_BOLD, fill=scolor)
            d.text((hx + 35, s_y + 40), sdesc, font=FONT_MONO, fill=TEXT_MUTED)
            s_y += 92

        spoke_w = 480
        sx = hx + hub_w + 140
        sy1 = hy
        sy2 = hy + 230
        
        d.line([(hx + hub_w, hy + 120), (sx, sy1 + 90)], fill=CYAN_ACCENT, width=3)
        d.line([(hx + hub_w, hy + 320), (sx, sy2 + 90)], fill=CYAN_ACCENT, width=3)
        d.text((hx + hub_w + 15, hy + 85), "Bi-directional Peering", font=FONT_MONO, fill=CYAN_ACCENT)
        d.text((hx + hub_w + 15, hy + 300), "UDR Traffic Enforced", font=FONT_MONO, fill=GREEN_ACCENT)
        
        d.rectangle([(sx, sy1), (sx + spoke_w, sy1 + 190)], fill=(13, 22, 44, 240), outline=(0, 200, 255, 120), width=1)
        d.rectangle([(sx, sy1), (sx + spoke_w, sy1 + 35)], fill=(0, 60, 100, 255))
        d.text((sx + 20, sy1 + 8), "SPOKE 1: PRODUCTION WORKLOADS (10.1.0.0/16)", font=FONT_MONO_BOLD, fill=TEXT_WHITE)
        d.text((sx + 25, sy1 + 55), "• AKS Cluster Nodes (Pod Network: 10.244.0.0/16)", font=FONT_MONO, fill=CYAN_ACCENT)
        d.text((sx + 25, sy1 + 88), "• Application Gateway Ingress & TLS 1.3 Termination", font=FONT_MONO, fill=TEXT_WHITE)
        d.text((sx + 25, sy1 + 120), "• Private Link Endpoints to Azure OpenAI & APIM", font=FONT_MONO, fill=GREEN_ACCENT)
        d.text((sx + 25, sy1 + 152), "• UDR: 0.0.0.0/0 -> 10.0.1.4 (Firewall Next Hop)", font=FONT_MONO_BOLD, fill=GOLD_ACCENT)

        d.rectangle([(sx, sy2), (sx + spoke_w, sy2 + 190)], fill=(13, 22, 44, 240), outline=(0, 200, 255, 120), width=1)
        d.rectangle([(sx, sy2), (sx + spoke_w, sy2 + 35)], fill=(0, 60, 100, 255))
        d.text((sx + 20, sy2 + 8), "SPOKE 2: DATA & SECRETS PERIMETER (10.2.0.0/16)", font=FONT_MONO_BOLD, fill=TEXT_WHITE)
        d.text((sx + 25, sy2 + 55), "• Azure SQL Database with Private Link (No Public IP)", font=FONT_MONO, fill=CYAN_ACCENT)
        d.text((sx + 25, sy2 + 88), "• Azure Key Vault Hardware HSM (Zero Public Endpoint)", font=FONT_MONO, fill=GREEN_ACCENT)
        d.text((sx + 25, sy2 + 120), "• Azure AI Search Vector Database for Enterprise RAG", font=FONT_MONO, fill=TEXT_WHITE)
        d.text((sx + 25, sy2 + 152), "• Microsegmentation NSG Rules: Default Deny Ingress", font=FONT_MONO_BOLD, fill=GOLD_ACCENT)

    elif sc["num"] == 6:
        # Scene 06: CI/CD Pipeline Stages
        stages = [
            ("1. COMMIT", "git push main", "VALIDATED"),
            ("2. TFLINT", "syntax & schema", "PASSED"),
            ("3. CHECKOV", "SAST compliance", "PASSED"),
            ("4. TFSEC", "shift-left scan", "PASSED"),
            ("5. TF PLAN", "drift verification", "APPROVED"),
            ("6. GATE", "Sanjeev Singh", "AUTHORIZED"),
            ("7. DEPLOY", "Azure Production", "LIVE")
        ]
        st_w = 230
        st_h = 130
        st_start_x = 100
        st_y = 260
        active_stage = int(prog * 7)
        for i, (name, desc, status) in enumerate(stages):
            x = st_start_x + (i % 4) * 260 if i < 4 else st_start_x + 130 + (i - 4) * 260
            y = st_y if i < 4 else st_y + 170
            is_active = (i <= active_stage)
            border = GREEN_ACCENT if is_active else (0, 180, 240, 80)
            d.rectangle([(x, y), (x + st_w, y + st_h)], fill=(9, 16, 32, 240), outline=border, width=2 if is_active else 1)
            d.line([(x, y), (x + st_w, y)], fill=GREEN_ACCENT if is_active else CYAN_ACCENT, width=3)
            d.text((x + 16, y + 18), name, font=FONT_MONO_BOLD, fill=TEXT_WHITE)
            d.text((x + 16, y + 50), desc, font=FONT_MONO, fill=TEXT_MUTED)
            badge_color = (0, 50, 80, 200) if is_active else (15, 25, 45, 200)
            d.rectangle([(x + 16, y + 85), (x + st_w - 16, y + 115)], fill=badge_color, outline=GREEN_ACCENT if is_active else (0, 140, 200, 80), width=1)
            status_text = f"✓ {status}" if is_active else "PENDING"
            d.text((x + 26, y + 92), status_text, font=FONT_MONO_BOLD, fill=GREEN_ACCENT if is_active else TEXT_MUTED)

    elif sc["num"] == 7:
        # Scene 07: Shift-Left DevSecOps Terminal (No OnePS branding)
        term_x = 180
        term_y = 110
        term_w = 1560
        term_h = 570
        d.rectangle([(term_x, term_y), (term_x + term_w, term_y + term_h)], fill=(6, 11, 22, 250), outline=(0, 210, 255, 150), width=1)
        d.rectangle([(term_x, term_y), (term_x + term_w, term_y + 40)], fill=(12, 20, 36, 255))
        d.ellipse([(term_x + 18, term_y + 15), (term_x + 28, term_y + 25)], fill=(255, 95, 87))
        d.ellipse([(term_x + 36, term_y + 15), (term_x + 46, term_y + 25)], fill=(255, 189, 46))
        d.ellipse([(term_x + 54, term_y + 15), (term_x + 64, term_y + 25)], fill=(39, 201, 63))
        d.text((term_x + 85, term_y + 11), "runner@devsecops-pipeline: ~/azure-enterprise-landing-zone (main)", font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
        
        term_lines = [
            ("$ tflint --recursive", CYAN_ACCENT),
            ("  ✓ 4 modules evaluated ... 0 errors, 0 warnings (100% compliant with Azure CAF rules)", GREEN_ACCENT),
            ("", TEXT_WHITE),
            ("$ checkov -d . --framework terraform --compact", CYAN_ACCENT),
            ("  ✓ Check: CKV_AZURE_1: Ensure Azure Firewall has public IP configured ... PASSED", GREEN_ACCENT),
            ("  ✓ Check: CKV_AZURE_109: Ensure Key Vault enables purge protection ... PASSED", GREEN_ACCENT),
            ("  ✓ Check: CKV_AZURE_115: Ensure Workload Identity is enabled for AKS ... PASSED", GREEN_ACCENT),
            ("  Summary: 42 passed, 0 failed, 0 skipped. Compliance score: 100%", GOLD_ACCENT),
            ("", TEXT_WHITE),
            ("$ tfsec .", CYAN_ACCENT),
            ("  ✓ No critical or high vulnerabilities found. 0 issues detected across all resource blocks.", GREEN_ACCENT),
            ("", TEXT_WHITE),
            ("$ gitleaks detect --source . --verbose", CYAN_ACCENT),
            ("  ✓ Scanning completed. 0 leaks found. No plain-text credentials, tokens, or private keys.", GREEN_ACCENT),
            ("", TEXT_WHITE),
            ("[DEPLOYMENT GATE] Approver: Sanjeev Singh (DevOps Lead) -> STATUS: AUTHORIZED FOR PRODUCTION", GREEN_ACCENT),
        ]
        t_y = term_y + 55
        for text, color in term_lines:
            d.text((term_x + 35, t_y), text, font=FONT_MONO_CODE, fill=color)
            t_y += 28

    elif sc["num"] == 10:
        # Scene 10: Observability Matrix Dashboard
        dash_x = 120
        dash_y = 110
        dash_w = 1680
        dash_h = 570
        d.rectangle([(dash_x, dash_y), (dash_x + dash_w, dash_y + dash_h)], fill=(7, 13, 26, 245), outline=(0, 200, 255, 140), width=1)
        d.rectangle([(dash_x, dash_y), (dash_x + dash_w, dash_y + 40)], fill=(13, 21, 38, 255))
        d.text((dash_x + 25, dash_y + 11), "AZURE MONITOR & PROMETHEUS // REAL-TIME OBSERVABILITY MATRIX", font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
        d.rectangle([(dash_x + dash_w - 260, dash_y + 8), (dash_x + dash_w - 20, dash_y + 34)], fill=(0, 60, 90, 200), outline=GREEN_ACCENT, width=1)
        d.text((dash_x + dash_w - 245, dash_y + 13), "● STATUS: ALL SYSTEMS NOMINAL", font=FONT_MONO, fill=GREEN_ACCENT)
        
        metrics = [
            ("CLUSTER THROUGHPUT", "4,850 req/s", "+12% peak traffic handled", CYAN_ACCENT),
            ("P99 LATENCY", "8.2 ms", "Direct private link routing", GREEN_ACCENT),
            ("CPU / MEMORY POOL", "34% / 48%", "Autoscaling headroom optimal", GOLD_ACCENT),
            ("SERVICE AVAILABILITY", "99.99%", "Zero unplanned downtime", GREEN_ACCENT)
        ]
        mw = 380
        mh = 140
        for i, (mtitle, mval, msub, mcol) in enumerate(metrics):
            mx = dash_x + 35 + i * 405
            my = dash_y + 60
            d.rectangle([(mx, my), (mx + mw, my + mh)], fill=(12, 22, 44, 240), outline=(0, 180, 240, 80), width=1)
            d.text((mx + 20, my + 15), mtitle, font=FONT_MONO, fill=TEXT_MUTED)
            d.text((mx + 20, my + 45), mval, font=FONT_BRAND_NAME, fill=mcol)
            d.text((mx + 20, my + 105), msub, font=FONT_MONO, fill=TEXT_WHITE)
            
        cx = dash_x + 35
        cy = dash_y + 230
        cw = 1000
        ch = 300
        d.rectangle([(cx, cy), (cx + cw, cy + ch)], fill=(10, 18, 36, 240), outline=(0, 160, 220, 80), width=1)
        d.text((cx + 20, cy + 15), "TIME-SERIES INGRESS / EGRESS TELEMETRY (LIVE)", font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
        pts = []
        for xi in range(0, cw - 40, 15):
            wave_y = cy + ch//2 + int(45 * math.sin((xi * 0.04) + prog * 10) + 20 * math.cos(xi * 0.08))
            pts.append((cx + 20 + xi, wave_y))
        for j in range(len(pts) - 1):
            d.line([pts[j], pts[j+1]], fill=GREEN_ACCENT, width=2)
            
        lx = cx + cw + 25
        lw = dash_w - cw - 95
        d.rectangle([(lx, cy), (lx + lw, cy + ch)], fill=(10, 18, 36, 240), outline=(0, 160, 220, 80), width=1)
        d.text((lx + 20, cy + 15), "STRUCTURED LOG STREAM", font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
        log_items = [
            "[INFO] AzureFirewallSubnet: 0 traffic drops",
            "[INFO] AKS Node Pool: 6/6 nodes ready",
            "[INFO] Pod replicas: HPA scaled to 8 pods",
            "[INFO] Azure Key Vault: Secret rotated OK",
            "[INFO] Ingress TLS 1.3: 100% encrypted",
            "[INFO] Health check probe: 200 OK (all routes)"
        ]
        ly = cy + 55
        for item in log_items:
            d.text((lx + 20, ly), item, font=FONT_MONO, fill=TEXT_MUTED)
            ly += 38

    elif sc["num"] == 11:
        # Scene 11: Business Outcomes 3 Pillars
        pillars = [
            ("1. CONSISTENCY", [
                "100% Codified Infrastructure",
                "Zero Configuration Drift",
                "Deterministic State Lease Locking",
                "Audited Automated Rollbacks"
            ], CYAN_ACCENT),
            ("2. VISIBILITY", [
                "End-to-End Distributed Tracing",
                "Azure Monitor & Prometheus Health",
                "Shift-Left Security Compliance",
                "Institutional Audit Trail Integrity"
            ], GREEN_ACCENT),
            ("3. CONTROL", [
                "FinOps Cloud Cost Governance",
                "Zero Trust Micro-Segmentation",
                "Production Quality Gates",
                "Sustainable Engineering Velocity"
            ], GOLD_ACCENT)
        ]
        pw = 510
        ph = 440
        py = 180
        for i, (ptitle, pitems, pcol) in enumerate(pillars):
            px = 120 + i * 570
            d.rectangle([(px, py), (px + pw, py + ph)], fill=(8, 14, 28, 245), outline=pcol, width=2)
            d.rectangle([(px, py), (px + pw, py + 48)], fill=(14, 24, 46, 255))
            d.text((px + 25, py + 14), ptitle, font=FONT_BRAND_ROLE, fill=TEXT_WHITE)
            iy = py + 75
            for itm in pitems:
                d.ellipse([(px + 28, iy + 6), (px + 36, iy + 14)], fill=pcol)
                d.text((px + 48, iy), itm, font=FONT_SUBTITLE, fill=TEXT_WHITE)
                iy += 80

    elif sc["num"] == 12:
        # Scene 12: Sanjeev Singh Platform Engineering Finale (Zero OnePS branding)
        cx, cy = WIDTH // 2, HEIGHT // 2 - 20
        bw, bh = 1080, 500
        d.rectangle([(cx - bw//2, cy - bh//2), (cx + bw//2, cy + bh//2)], fill=(6, 11, 24, 245), outline=(0, 220, 255, 160), width=2)
        d.line([(cx - bw//2, cy - bh//2), (cx + bw//2, cy - bh//2)], fill=GREEN_ACCENT, width=4)
        
        d.text((cx - 240, cy - 200), "SANJEEV SINGH", font=FONT_BRAND_NAME, fill=TEXT_WHITE)
        d.text((cx - 300, cy - 130), "FREELANCE AZURE CLOUD ARCHITECT & CONSULTANT", font=FONT_BRAND_ROLE, fill=CYAN_ACCENT)
        
        tagline = "FROM CLOUD COMPLEXITY TO ENGINEERING CONFIDENCE"
        d.text((cx - 330, cy - 80), tagline, font=FONT_SUBTITLE, fill=GREEN_ACCENT)
        
        cta = "Whether you're launching a startup, modernizing infrastructure, or improving delivery workflows:"
        d.text((cx - 410, cy - 35), cta, font=FONT_SUBTITLE, fill=TEXT_MUTED)
        cta2 = "Let's build your next cloud milestone together."
        d.text((cx - 220, cy - 5), cta2, font=FONT_TITLE, fill=TEXT_WHITE)
        
        links = [
            ("🌐 PORTFOLIO", "sanjeevsingh.oneps.in"),
            ("💼 LINKEDIN", "linkedin.com/in/sanjiivsingh"),
            ("🐙 GITHUB", "github.com/sanjiivsingh"),
            ("✉️ DIRECT", "sanjeevsinghred@gmail.com")
        ]
        lx = cx - 440
        for label, val in links:
            d.rectangle([(lx, cy + 60), (lx + 210, cy + 125)], fill=(12, 22, 44, 240), outline=(0, 200, 255, 100), width=1)
            d.text((lx + 15, cy + 70), label, font=FONT_MONO_BOLD, fill=CYAN_ACCENT)
            d.text((lx + 15, cy + 96), val, font=FONT_MONO, fill=TEXT_WHITE)
            lx += 225

    draw_lower_third(d, sc["title"], sc["subtitle"], sc["tags"], sc["overlay"])
    return overlay

def render_master_video():
    print(f"\n========================================================")
    print(f"Rendering Master 90s Video (Indian Male Neural AI) -> {OUTPUT_MP4}")
    print(f"========================================================")
    
    generate_soundtrack()
    base_bg = load_base_graphics()
    
    ffmpeg_cmd = [
        FFMPEG_BIN,
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgba",
        "-r", str(FPS),
        "-i", "-",
        "-i", OUTPUT_WAV,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "320k",
        "-movflags", "+faststart",
        "-shortest",
        OUTPUT_MP4
    ]
    
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    
    global_time = 0.0
    total_rendered_frames = 0
    poster_frame = None
    
    for sc in SCENES:
        dur = sc["duration"]
        num_frames = int(dur * FPS)
        motion_type = sc["motion"]
        base_im = base_bg[sc["base_key"]]
        base_w, base_h = base_im.size
        
        print(f"Rendering Scene {sc['num']:02d}/12 [{sc['name']}] -> {dur:.1f}s ({num_frames} frames)...")
        
        for f in range(num_frames):
            prog = f / max(1, num_frames - 1)
            ease = 0.5 * (1 - math.cos(math.pi * prog))
            
            if motion_type == "zoom_in":
                scale = 1.0 + 0.07 * ease
                crop_w = int(WIDTH / scale)
                crop_h = int(HEIGHT / scale)
                cx = base_w // 2
                cy = base_h // 2
            elif motion_type == "pull_back":
                scale = 1.07 - 0.07 * ease
                crop_w = int(WIDTH / scale)
                crop_h = int(HEIGHT / scale)
                cx = base_w // 2
                cy = base_h // 2
            elif motion_type == "pan_right":
                scale = 1.05
                crop_w = int(WIDTH / scale)
                crop_h = int(HEIGHT / scale)
                shift = (base_w - crop_w) * 0.4 * ease
                cx = int(crop_w // 2 + shift)
                cy = base_h // 2
            elif motion_type == "pan_left_to_right":
                scale = 1.04
                crop_w = int(WIDTH / scale)
                crop_h = int(HEIGHT / scale)
                shift = (base_w - crop_w) * (0.1 + 0.5 * ease)
                cx = int(shift + crop_w // 2)
                cy = base_h // 2
            elif motion_type == "breathe":
                scale = 1.0 + 0.03 * math.sin(math.pi * prog)
                crop_w = int(WIDTH / scale)
                crop_h = int(HEIGHT / scale)
                cx = base_w // 2
                cy = base_h // 2
            else: # drift
                scale = 1.03
                crop_w = int(WIDTH / scale)
                crop_h = int(HEIGHT / scale)
                cx = int(base_w // 2 + 15 * math.sin(math.pi * prog))
                cy = int(base_h // 2 + 10 * math.cos(math.pi * prog))
                
            crop_x0 = max(0, min(base_w - crop_w, cx - crop_w // 2))
            crop_y0 = max(0, min(base_h - crop_h, cy - crop_h // 2))
            cropped = base_im.crop((crop_x0, crop_y0, crop_x0 + crop_w, crop_y0 + crop_h))
            frame_img = cropped.resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR).convert("RGBA")
            
            overlay = render_scene_overlay(sc, f, num_frames, global_time)
            composed = Image.alpha_composite(frame_img, overlay)
            
            fade_alpha = 1.0
            if f < 8:
                fade_alpha = f / 8.0
            if total_rendered_frames > (TOTAL_FRAMES - 15):
                fade_alpha = (TOTAL_FRAMES - total_rendered_frames) / 15.0
                
            if fade_alpha < 0.99:
                black = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, int(255 * (1 - fade_alpha))))
                composed = Image.alpha_composite(composed, black)
                
            # Capture poster frame at Scene 02 (handsome engineer reveal)
            if sc["num"] == 2 and f == num_frames // 2:
                poster_frame = composed.convert("RGB")
                
            proc.stdin.write(composed.tobytes())
            global_time += 1.0 / FPS
            total_rendered_frames += 1

    proc.stdin.close()
    proc.wait()
    print(f"Master video rendered successfully -> {OUTPUT_MP4} (status {proc.returncode})")
    
    # Save High-Res Poster and WebP with play button badge
    if poster_frame is None:
        poster_frame = base_bg["engineer"].copy().resize((WIDTH, HEIGHT))
        
    p_rgba = poster_frame.convert("RGBA")
    ov = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    d_btn = ImageDraw.Draw(ov)
    cx, cy = WIDTH // 2, HEIGHT // 2 - 20
    btn_r = 56
    d_btn.ellipse([(cx - btn_r - 10, cy - btn_r - 10), (cx + btn_r + 10, cy + btn_r + 10)], outline=(0, 210, 255, 90), width=2)
    d_btn.ellipse([(cx - btn_r, cy - btn_r), (cx + btn_r, cy + btn_r)], fill=(7, 12, 26, 215), outline=(0, 220, 255, 240), width=3)
    d_btn.polygon([(cx - 18, cy - 26), (cx - 18, cy + 26), (cx + 28, cy)], fill=(0, 255, 180, 255))
    final_poster = Image.alpha_composite(p_rgba, ov).convert("RGB")
    
    final_poster.save(OUTPUT_POSTER, quality=95)
    final_poster.save(OUTPUT_WEBP, quality=95, method=6)
    print("Poster and WebP preview saved.")

def mirror_to_docker():
    out_dir = os.path.join(DOCKER_SHOWREEL_DIR, "output")
    if os.path.exists(out_dir):
        dest_mp4 = os.path.join(out_dir, "sanjeev_singh_cloud_engineering_showreel_master.mp4")
        subprocess.run(["cp", OUTPUT_MP4, dest_mp4], check=False)
        print(f"Mirrored to Docker showreel: {dest_mp4}")

def main():
    print("Starting Updated Master Video Production Pipeline...")
    render_master_video()
    mirror_to_docker()
    print("\nUpdated production complete! All video assets ready.")

if __name__ == "__main__":
    main()
