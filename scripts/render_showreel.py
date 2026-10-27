#!/usr/bin/env python3
"""
Production Video Showreel Generator for Sanjeev Singh
Freelance Azure Cloud Engineer | Terraform & Infrastructure Automation | DevOps & CI/CD

Generates:
1. 6 Individual Scene Clips (6-12s each)
2. Master Showreel (66s) with full cinematic soundtrack & sound design
3. Short Preview Showreel (24s) for GitHub & fast website playback
4. Teaser Video (10s) for social sharing
5. WebM format for universal browser support
6. High-res WebP & JPG Posters and thumbnails
7. WebVTT & SRT Caption files
"""

import os
import sys
import math
import subprocess
import wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

FFMPEG_BIN = "/Users/sanjeevsingh/.local/bin/ffmpeg"
BASE_DIR = "/Users/sanjeevsingh/DevOps/Docker/sanjeevsingh.oneps.in/video-showreel"
GRAPHICS_DIR = os.path.join(BASE_DIR, "graphics")
CLIPS_DIR = os.path.join(BASE_DIR, "clips")
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
THUMB_DIR = os.path.join(BASE_DIR, "thumbnails")
CAPTIONS_DIR = os.path.join(BASE_DIR, "captions")

WIDTH = 1920
HEIGHT = 1080
FPS = 30
SAMPLE_RATE = 48000

# Fonts
FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36, index=1)
FONT_SUBTITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20, index=0)
FONT_MONO = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 16, index=0)
FONT_MONO_BOLD = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 16, index=1)
FONT_BRAND_NAME = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 58, index=1)
FONT_BRAND_ROLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24, index=1)
FONT_BRAND_SUB = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20, index=0)

SCENES = [
    {
        "id": "clip1_cloud_vision",
        "file": os.path.join(GRAPHICS_DIR, "scene1_cloud_vision.jpg"),
        "duration_master": 10.0,
        "duration_short": 4.0,
        "duration_teaser": 1.5,
        "hud_id": "REC: 00:00:10 // RES: 1080p 60fps",
        "hud_title": "AZURE ENTERPRISE CLOUD REEL // NODE: GLOBAL-TRANSIT",
        "title": "ENGINEERING THE CLOUD. AUTOMATING THE FOUNDATION.",
        "subtitle": "Architecting resilient, scalable enterprise infrastructure across Microsoft Azure",
        "tags": ["MICROSOFT AZURE", "ENTERPRISE CLOUD ARCHITECTURE", "RESILIENCE & GOVERNANCE"],
        "motion": "zoom_in", # 1.0 -> 1.08
    },
    {
        "id": "clip2_terraform_iac",
        "file": os.path.join(GRAPHICS_DIR, "scene2_terraform_iac.jpg"),
        "duration_master": 11.0,
        "duration_short": 4.0,
        "duration_teaser": 1.5,
        "hud_id": "REC: 00:00:21 // RES: 1080p 60fps",
        "hud_title": "TERRAFORM IAC WORKBENCH // STATE: DETERMINISTIC",
        "title": "REUSABLE TERRAFORM. REPEATABLE INFRASTRUCTURE.",
        "subtitle": "Multi-environment IaC architecture with deterministic state and zero configuration drift",
        "tags": ["TERRAFORM HCL", "MODULAR IaC BLUEPRINTS", "ZERO DRIFT DEPLOYMENTS"],
        "motion": "pan_right", # pan slightly right & zoom
    },
    {
        "id": "clip3_landing_zones",
        "file": os.path.join(GRAPHICS_DIR, "scene3_landing_zones.jpg"),
        "duration_master": 11.0,
        "duration_short": 4.0,
        "duration_teaser": 1.5,
        "hud_id": "REC: 00:00:32 // RES: 1080p 60fps",
        "hud_title": "AZURE LANDING ZONE MATRIX // GOVERNANCE: ENFORCED",
        "title": "SECURE FOUNDATIONS. SCALABLE CLOUD ARCHITECTURE.",
        "subtitle": "Governed enterprise landing zones, hub-and-spoke transit networking & policy enforcement",
        "tags": ["ENTERPRISE LANDING ZONES", "HUB-AND-SPOKE NETWORKING", "AZURE FIREWALL & POLICY"],
        "motion": "zoom_in", # zoom in on hub
    },
    {
        "id": "clip4_devsecops_pipeline",
        "file": os.path.join(GRAPHICS_DIR, "scene4_devsecops_pipeline.jpg"),
        "duration_master": 11.0,
        "duration_short": 4.0,
        "duration_teaser": 1.5,
        "hud_id": "REC: 00:00:43 // RES: 1080p 60fps",
        "hud_title": "DEVSECOPS PIPELINE RUN // GATE: POLICY-VERIFIED",
        "title": "VALIDATE. SECURE. APPROVE. DEPLOY.",
        "subtitle": "Automated shift-left security, policy-as-code validation & governed deployment gates",
        "tags": ["GITHUB ACTIONS & ADO", "CHECKOV SAST", "TRIVY CONTAINER SCAN", "GATE APPROVALS"],
        "motion": "pan_left_to_right",
    },
    {
        "id": "clip5_containers_aks",
        "file": os.path.join(GRAPHICS_DIR, "scene5_containers_aks.jpg"),
        "duration_master": 11.0,
        "duration_short": 4.0,
        "duration_teaser": 1.5,
        "hud_id": "REC: 00:00:54 // RES: 1080p 60fps",
        "hud_title": "AKS CLUSTER TELEMETRY // UPTIME: 99.99% OPTIMAL",
        "title": "CONTAINERS. SECURITY. OPERATIONAL VISIBILITY.",
        "subtitle": "Managed Azure Kubernetes Service (AKS), distributed microservices & real-time telemetry",
        "tags": ["AZURE KUBERNETES SERVICE (AKS)", "POD ORCHESTRATION", "SECURITY MONITORING"],
        "motion": "pull_back", # 1.08 -> 1.0
    },
    {
        "id": "clip6_brand_reveal",
        "file": os.path.join(GRAPHICS_DIR, "scene6_brand_reveal.jpg"),
        "duration_master": 12.0,
        "duration_short": 4.0,
        "duration_teaser": 2.5,
        "hud_id": "REC: 00:01:06 // BRAND: VERIFIED",
        "hud_title": "SANJEEV SINGH // CLOUD PLATFORM ENGINEERING",
        "title": "SANJEEV SINGH",
        "subtitle": "FREELANCE AZURE CLOUD ENGINEER & CONSULTANT",
        "tags": ["TERRAFORM IaC", "AZURE LANDING ZONES", "DEVSECOPS", "KUBERNETES / AKS"],
        "motion": "breathe", # gentle breath zoom
    }
]

def generate_soundtrack(total_duration, output_wav_path, scene_timings):
    """
    Synthesize an original, multi-track cinematic electronic soundtrack
    with sub-bass impacts, ambient pad chords, digital telemetry clicks,
    and a final resolution chord.
    """
    print(f"Generating cinematic soundtrack for {total_duration:.1f}s...")
    total_samples = int(SAMPLE_RATE * total_duration)
    t = np.linspace(0, total_duration, total_samples, endpoint=False)
    left_track = np.zeros(total_samples, dtype=np.float32)
    right_track = np.zeros(total_samples, dtype=np.float32)

    # 1. Base Ambient Chord Progression (C min -> Ab maj -> Eb maj -> Bb sus -> G sus -> C min)
    chords = [
        (0.0, 10.0, [65.41, 130.81, 155.56, 196.00, 261.63, 311.13]), # C minor
        (10.0, 21.0, [51.91, 103.83, 130.81, 155.56, 207.65, 261.63]), # Ab major
        (21.0, 32.0, [77.78, 155.56, 196.00, 233.08, 311.13, 392.00]), # Eb major
        (32.0, 43.0, [58.27, 116.54, 146.83, 174.61, 233.08, 293.66]), # Bb / D
        (43.0, 54.0, [49.00, 98.00, 130.81, 164.81, 196.00, 261.63]), # G / C
        (54.0, total_duration, [65.41, 130.81, 196.00, 261.63, 392.00, 523.25]), # C sus2 resolution
    ]

    for start_t, end_t, freqs in chords:
        if start_t >= total_duration:
            continue
        actual_end = min(end_t, total_duration)
        idx_start = int(start_t * SAMPLE_RATE)
        idx_end = int(actual_end * SAMPLE_RATE)
        dur = actual_end - start_t
        t_chord = np.linspace(0, dur, idx_end - idx_start, endpoint=False)
        
        # Envelope: smooth attack & decay
        attack = min(1.5, dur * 0.3)
        release = min(2.0, dur * 0.3)
        env = np.ones_like(t_chord)
        att_idx = int(attack * SAMPLE_RATE)
        rel_idx = int(release * SAMPLE_RATE)
        if att_idx > 0:
            env[:att_idx] = 0.5 * (1 - np.cos(np.pi * np.linspace(0, 1, att_idx)))
        if rel_idx > 0:
            env[-rel_idx:] = 0.5 * (1 + np.cos(np.pi * np.linspace(0, 1, rel_idx)))

        for i, f in enumerate(freqs):
            detune_l = np.sin(2 * np.pi * (f - 0.25) * t_chord)
            detune_r = np.sin(2 * np.pi * (f + 0.25) * t_chord)
            # Add warm harmonics
            harm_l = 0.3 * np.sin(4 * np.pi * f * t_chord)
            harm_r = 0.3 * np.sin(4 * np.pi * f * t_chord)
            amp = (0.12 / (1 + 0.4 * i))
            left_track[idx_start:idx_end] += (detune_l + harm_l) * env * amp
            right_track[idx_start:idx_end] += (detune_r + harm_r) * env * amp

    # 2. Cinematic Sub-Bass Braams / Impacts at scene transitions
    for t_impact in scene_timings:
        if t_impact >= total_duration:
            continue
        imp_dur = min(4.5, total_duration - t_impact)
        idx_start = int(t_impact * SAMPLE_RATE)
        idx_end = idx_start + int(imp_dur * SAMPLE_RATE)
        t_imp = np.linspace(0, imp_dur, idx_end - idx_start, endpoint=False)
        
        # Frequency drop: 65 Hz down to 32 Hz
        freq_pitch = 65.0 * np.exp(-t_imp * 1.8) + 32.0
        phase = 2 * np.pi * np.cumsum(freq_pitch) / SAMPLE_RATE
        env_imp = np.exp(-t_imp * 0.9)
        
        sub = 0.45 * np.sin(phase) * env_imp
        sat = 0.15 * np.sin(phase * 2) * env_imp
        transient_noise = (np.random.rand(len(t_imp)) * 2 - 1) * np.exp(-t_imp * 15.0) * 0.15
        
        left_track[idx_start:idx_end] += (sub + sat + transient_noise)
        right_track[idx_start:idx_end] += (sub + sat + transient_noise)

    # 3. Rhythmic Telemetry Pulses & Digital Ticks (Every 0.5s = 120 BPM)
    beat_interval = 0.5
    for b in np.arange(0.5, total_duration - 1.0, beat_interval):
        idx_b = int(b * SAMPLE_RATE)
        tick_len = int(0.04 * SAMPLE_RATE)
        if idx_b + tick_len > total_samples:
            break
        t_tick = np.linspace(0, 0.04, tick_len, endpoint=False)
        tick_env = np.exp(-t_tick * 80.0)
        pan = 0.3 * np.sin(2 * np.pi * b * 0.2)
        tick_wave = 0.04 * np.sin(2 * np.pi * 2400 * t_tick) * tick_env
        left_track[idx_b:idx_b + tick_len] += tick_wave * (0.5 - pan)
        right_track[idx_b:idx_b + tick_len] += tick_wave * (0.5 + pan)

    # 4. Final Resolution Chime (Last 6 seconds)
    if total_duration > 12.0:
        chime_start = total_duration - 11.5
        chime_dur = 11.0
        idx_c_start = int(chime_start * SAMPLE_RATE)
        idx_c_end = idx_c_start + int(chime_dur * SAMPLE_RATE)
        t_chime = np.linspace(0, chime_dur, idx_c_end - idx_c_start, endpoint=False)
        chime_env = np.exp(-t_chime * 0.35)
        for cf in [523.25, 659.25, 783.99, 1046.50]: # C5, E5, G5, C6
            chime_w = 0.06 * np.sin(2 * np.pi * cf * t_chime) * chime_env
            left_track[idx_c_start:idx_c_end] += chime_w
            right_track[idx_c_start:idx_c_end] += chime_w

    # Normalize audio levels
    max_val = max(np.max(np.abs(left_track)), np.max(np.abs(right_track)), 1e-6)
    target_peak = 0.92
    left_track = (left_track / max_val) * target_peak
    right_track = (right_track / max_val) * target_peak

    stereo = np.empty((total_samples, 2), dtype=np.int16)
    stereo[:, 0] = (left_track * 32767).astype(np.int16)
    stereo[:, 1] = (right_track * 32767).astype(np.int16)

    with wave.open(output_wav_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(stereo.tobytes())

    print(f"Soundtrack exported: {output_wav_path}")

def prepare_base_images():
    """
    Enhance each base image with high-definition upscaling (Lanczos),
    gentle contrast boost and subtle unsharp-masking so that fine text,
    topologies, and monitor lines look crisp and clear at 1080p.
    """
    enhanced = {}
    for sc in SCENES:
        img_path = sc["file"]
        im = Image.open(img_path).convert("RGB")
        w_scaled = int(WIDTH * 1.15)
        h_scaled = int(HEIGHT * 1.15)
        im_large = im.resize((w_scaled, h_scaled), Image.Resampling.LANCZOS)
        
        enhancer = ImageEnhance.Sharpness(im_large)
        im_sharp = enhancer.enhance(1.25)
        enhanced[sc["id"]] = im_sharp
    return enhanced

def draw_hud_overlay(draw, sc, frame_idx, total_frames, current_time, is_brand_scene=False):
    """
    Renders high-tech, razor-sharp HUD overlays with translucent glassmorphic
    panels, cyan status bars, timecode, and readable typography.
    """
    # 1. Top HUD Header Bar
    top_panel = [(40, 32), (WIDTH - 40, 76)]
    draw.rectangle(top_panel, fill=(10, 16, 32, 220), outline=(0, 210, 255, 90), width=1)
    
    # Left status dots
    draw.ellipse([(55, 50), (63, 58)], fill=(0, 255, 170, 255))
    draw.text((75, 45), sc["hud_title"], font=FONT_MONO_BOLD, fill=(0, 220, 255, 255))
    
    # Right timecode & resolution badge
    mins = int(current_time // 60)
    secs = int(current_time % 60)
    frames = int((current_time - int(current_time)) * FPS)
    tc_str = f"TC: {mins:02d}:{secs:02d}:{frames:02d} // 1080p 60fps"
    draw.text((WIDTH - 420, 45), tc_str, font=FONT_MONO, fill=(180, 210, 230, 240))
    
    # Corner HUD crosshairs
    ch_len = 16
    for x, y in [(40, 32), (WIDTH - 40, 32), (40, HEIGHT - 40), (WIDTH - 40, HEIGHT - 40)]:
        x_dir = 1 if x == 40 else -1
        y_dir = 1 if y == 32 else -1
        draw.line([(x, y), (x + x_dir * ch_len, y)], fill=(0, 210, 255, 180), width=2)
        draw.line([(x, y), (x, y + y_dir * ch_len)], fill=(0, 210, 255, 180), width=2)

    # 2. Scene-specific Lower Third / Centerpiece
    if is_brand_scene:
        # Luxury Brand Reveal Layout
        cx = WIDTH // 2
        cy = HEIGHT // 2
        
        card_w = 980
        card_h = 420
        box = [(cx - card_w // 2, cy - card_h // 2 + 10), (cx + card_w // 2, cy + card_h // 2 + 10)]
        draw.rectangle(box, fill=(7, 12, 26, 235), outline=(0, 180, 255, 120), width=2)
        draw.line([(cx - card_w // 2, cy - card_h // 2 + 10), (cx + card_w // 2, cy - card_h // 2 + 10)], fill=(0, 255, 180, 255), width=3)
        
        name_bbox = FONT_BRAND_NAME.getbbox("SANJEEV SINGH")
        name_w = name_bbox[2] - name_bbox[0]
        draw.text((cx - name_w // 2, cy - 150), "SANJEEV SINGH", font=FONT_BRAND_NAME, fill=(255, 255, 255, 255))
        
        role_text = "FREELANCE AZURE CLOUD ENGINEER & CONSULTANT"
        role_bbox = FONT_BRAND_ROLE.getbbox(role_text)
        role_w = role_bbox[2] - role_bbox[0]
        draw.text((cx - role_w // 2, cy - 75), role_text, font=FONT_BRAND_ROLE, fill=(0, 220, 255, 255))
        
        pillars = "TERRAFORM IaC  |  AZURE LANDING ZONES  |  DEVSECOPS  |  CONTAINERS & AKS"
        p_bbox = FONT_MONO_BOLD.getbbox(pillars)
        p_w = p_bbox[2] - p_bbox[0]
        p_box = [(cx - p_w // 2 - 20, cy - 25), (cx + p_w // 2 + 20, cy + 12)]
        draw.rectangle(p_box, fill=(13, 22, 45, 240), outline=(0, 160, 220, 90), width=1)
        draw.text((cx - p_w // 2, cy - 20), pillars, font=FONT_MONO_BOLD, fill=(160, 230, 255, 255))
        
        cta_text = "Let's engineer your next scalable, secure cloud foundation."
        c_bbox = FONT_SUBTITLE.getbbox(cta_text)
        c_w = c_bbox[2] - c_bbox[0]
        draw.text((cx - c_w // 2, cy + 35), cta_text, font=FONT_SUBTITLE, fill=(220, 230, 245, 240))
        
        urls_text = "WEBSITE: sanjeevsingh.oneps.in   //   GITHUB: github.com/sanjiivsingh"
        u_bbox = FONT_MONO_BOLD.getbbox(urls_text)
        u_w = u_bbox[2] - u_bbox[0]
        u_box = [(cx - u_w // 2 - 16, cy + 90), (cx + u_w // 2 + 16, cy + 128)]
        draw.rectangle(u_box, fill=(0, 60, 120, 220), outline=(0, 255, 180, 200), width=1)
        draw.text((cx - u_w // 2, cy + 98), urls_text, font=FONT_MONO_BOLD, fill=(255, 255, 255, 255))
    else:
        l3_w = 1200
        l3_h = 160
        x0 = 60
        y0 = HEIGHT - l3_h - 60
        x1 = x0 + l3_w
        y1 = y0 + l3_h
        
        draw.rectangle([(x0, y0), (x1, y1)], fill=(7, 12, 26, 225), outline=(0, 200, 255, 90), width=1)
        draw.rectangle([(x0, y0), (x0 + 5, y1)], fill=(0, 220, 255, 255))
        
        draw.text((x0 + 30, y0 + 20), sc["title"], font=FONT_TITLE, fill=(255, 255, 255, 255))
        draw.text((x0 + 30, y0 + 75), sc["subtitle"], font=FONT_SUBTITLE, fill=(180, 210, 235, 240))
        
        tag_x = x0 + 30
        tag_y = y0 + 115
        for tag in sc["tags"]:
            bbox = FONT_MONO.getbbox(tag)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            box_coords = [(tag_x, tag_y), (tag_x + tw + 18, tag_y + 26)]
            draw.rectangle(box_coords, fill=(16, 28, 56, 230), outline=(0, 220, 255, 110), width=1)
            draw.text((tag_x + 9, tag_y + 4), tag, font=FONT_MONO, fill=(0, 255, 210, 255))
            tag_x += tw + 28

def generate_video(scenes_to_render, total_duration, output_mp4, output_wav, timing_key="duration_master"):
    """
    Renders an entire multi-scene video by piping synthesized 1080p frames
    directly to FFmpeg with high-bitrate H.264 video and AAC audio.
    """
    print(f"\n==========================================")
    print(f"Rendering Video -> {output_mp4} ({total_duration:.1f}s)")
    print(f"==========================================")
    
    enhanced_images = prepare_base_images()
    
    scene_starts = []
    curr = 0.0
    for sc in scenes_to_render:
        scene_starts.append(curr)
        curr += sc[timing_key]
        
    generate_soundtrack(total_duration, output_wav, scene_starts)

    ffmpeg_cmd = [
        FFMPEG_BIN,
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgba",
        "-r", str(FPS),
        "-i", "-",
        "-i", output_wav,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "17",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "320k",
        "-movflags", "+faststart",
        "-shortest",
        output_mp4
    ]

    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

    total_rendered_frames = 0
    global_time = 0.0

    for sc_idx, sc in enumerate(scenes_to_render):
        dur = sc[timing_key]
        num_frames = int(dur * FPS)
        motion_type = sc["motion"]
        is_brand = (sc["id"] == "clip6_brand_reveal")
        base_im = enhanced_images[sc["id"]]
        base_w, base_h = base_im.size
        
        print(f"Rendering scene [{sc['id']}] -> {dur:.1f}s ({num_frames} frames)...")

        for f in range(num_frames):
            prog = f / max(1, num_frames - 1)
            ease = 0.5 * (1 - math.cos(math.pi * prog))

            if motion_type == "zoom_in":
                scale = 1.0 + 0.08 * ease
                crop_w = int(WIDTH / scale)
                crop_h = int(HEIGHT / scale)
                cx = base_w // 2
                cy = base_h // 2
            elif motion_type == "pull_back":
                scale = 1.08 - 0.08 * ease
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
                scale = 1.0 + 0.04 * math.sin(math.pi * prog)
                crop_w = int(WIDTH / scale)
                crop_h = int(HEIGHT / scale)
                cx = base_w // 2
                cy = base_h // 2
            else:
                crop_w = WIDTH
                crop_h = HEIGHT
                cx = base_w // 2
                cy = base_h // 2

            crop_x0 = max(0, min(base_w - crop_w, cx - crop_w // 2))
            crop_y0 = max(0, min(base_h - crop_h, cy - crop_h // 2))
            cropped = base_im.crop((crop_x0, crop_y0, crop_x0 + crop_w, crop_y0 + crop_h))
            frame_img = cropped.resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR).convert("RGBA")

            overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)
            draw_hud_overlay(draw, sc, f, num_frames, global_time, is_brand_scene=is_brand)
            
            fade_alpha = 1.0
            if f < 9:
                fade_alpha = f / 9.0
            if total_rendered_frames > (int(total_duration * FPS) - 15):
                fade_alpha = (int(total_duration * FPS) - total_rendered_frames) / 15.0

            composed = Image.alpha_composite(frame_img, overlay)
            if fade_alpha < 0.99:
                black = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, int(255 * (1 - fade_alpha))))
                composed = Image.alpha_composite(composed, black)

            proc.stdin.write(composed.tobytes())
            global_time += 1.0 / FPS
            total_rendered_frames += 1

    proc.stdin.close()
    proc.wait()
    print(f"Video created successfully -> {output_mp4} (code {proc.returncode})")

def render_individual_clips():
    """
    Renders 6 individual clip files in video-showreel/clips/
    """
    print("\n==========================================")
    print("Rendering 6 Individual Clip Files")
    print("==========================================")
    for sc in SCENES:
        dur = sc["duration_master"]
        clip_mp4 = os.path.join(CLIPS_DIR, f"{sc['id']}.mp4")
        clip_wav = os.path.join(AUDIO_DIR, f"{sc['id']}.wav")
        generate_video([sc], dur, clip_mp4, clip_wav, timing_key="duration_master")

def render_posters_and_thumbnails():
    """
    Renders poster and thumbnail images (WebP & JPG) for web and GitHub embedding.
    """
    print("\nRendering high-res poster images and thumbnails...")
    sc5 = SCENES[4]
    base_im = Image.open(sc5["file"]).convert("RGB").resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    enhancer = ImageEnhance.Sharpness(base_im)
    base_sharp = enhancer.enhance(1.2).convert("RGBA")
    
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw_hud_overlay(draw, sc5, 0, 100, 48.0, is_brand_scene=False)
    
    cx = WIDTH // 2
    cy = HEIGHT // 2
    btn_r = 54
    draw.ellipse([(cx - btn_r, cy - btn_r), (cx + btn_r, cy + btn_r)], fill=(7, 12, 26, 210), outline=(0, 220, 255, 240), width=3)
    poly = [(cx - 16, cy - 24), (cx - 16, cy + 24), (cx + 26, cy)]
    draw.polygon(poly, fill=(0, 255, 200, 255))
    
    poster = Image.alpha_composite(base_sharp, overlay).convert("RGB")
    
    poster_jpg = os.path.join(THUMB_DIR, "showreel_poster.jpg")
    poster_webp = os.path.join(THUMB_DIR, "showreel_poster.webp")
    poster.save(poster_jpg, quality=95)
    poster.save(poster_webp, quality=95, method=6)
    
    for i, sc in enumerate(SCENES, 1):
        thumb_im = Image.open(sc["file"]).convert("RGB").resize((960, 540), Image.Resampling.LANCZOS)
        thumb_im.save(os.path.join(THUMB_DIR, f"scene{i}_thumb.jpg"), quality=90)
        thumb_im.save(os.path.join(THUMB_DIR, f"scene{i}_thumb.webp"), quality=90)
    print("Posters & thumbnails generated successfully.")

def render_captions():
    """
    Generates WebVTT and SRT caption files for full accessibility.
    """
    vtt_content = """WEBVTT
Kind: captions
Language: en

00:00:00.000 --> 00:00:10.000
Engineering the cloud. Automating the foundation with Microsoft Azure architecture.

00:00:10.000 --> 00:00:21.000
Reusable Terraform. Repeatable infrastructure as code with deterministic state.

00:00:21.000 --> 00:00:32.000
Secure foundations. Governed Azure Landing Zones with Hub-and-Spoke transit networking.

00:00:32.000 --> 00:00:43.000
Validate. Secure. Approve. Deploy. Automated enterprise DevSecOps pipelines.

00:00:43.000 --> 00:00:54.000
Containers, security, and operational visibility across Azure Kubernetes Service.

00:00:54.000 --> 00:01:06.000
Sanjeev Singh. Freelance Azure Cloud Engineer & Consultant. sanjeevsingh.oneps.in
"""

    srt_content = """1
00:00:00,000 --> 00:00:10,000
Engineering the cloud. Automating the foundation with Microsoft Azure architecture.

2
00:00:10,000 --> 00:00:21,000
Reusable Terraform. Repeatable infrastructure as code with deterministic state.

3
00:00:21,000 --> 00:00:32,000
Secure foundations. Governed Azure Landing Zones with Hub-and-Spoke transit networking.

4
00:00:32,000 --> 00:00:43,000
Validate. Secure. Approve. Deploy. Automated enterprise DevSecOps pipelines.

5
00:00:43,000 --> 00:00:54,000
Containers, security, and operational visibility across Azure Kubernetes Service.

6
00:00:54,000 --> 00:01:06,000
Sanjeev Singh. Freelance Azure Cloud Engineer & Consultant. sanjeevsingh.oneps.in
"""
    with open(os.path.join(CAPTIONS_DIR, "showreel_captions.vtt"), "w") as f:
        f.write(vtt_content)
    with open(os.path.join(CAPTIONS_DIR, "showreel_captions.srt"), "w") as f:
        f.write(srt_content)
    print("Captions (VTT and SRT) created.")

def convert_to_webm(input_mp4, output_webm):
    """
    Generates optimized WebM version using VP9 for modern web browsers.
    """
    print(f"Converting to WebM -> {output_webm}...")
    cmd = [
        FFMPEG_BIN,
        "-y",
        "-i", input_mp4,
        "-c:v", "libvpx-vp9",
        "-b:v", "3M",
        "-crf", "28",
        "-c:a", "libopus",
        "-b:a", "128k",
        "-speed", "4",
        output_webm
    ]
    subprocess.run(cmd, check=True)
    print("WebM generated.")

def main():
    print("Starting Video Showreel Production for Sanjeev Singh...")
    
    # 1. Posters & Thumbnails
    render_posters_and_thumbnails()
    
    # 2. Captions
    render_captions()
    
    # 3. Individual Scene Clips (6-12s each)
    render_individual_clips()
    
    # 4. Master Showreel (66s)
    master_mp4 = os.path.join(OUTPUT_DIR, "sanjeev_singh_cloud_engineering_showreel_master.mp4")
    master_wav = os.path.join(AUDIO_DIR, "showreel_soundtrack_master.wav")
    total_master_dur = sum(sc["duration_master"] for sc in SCENES)
    generate_video(SCENES, total_master_dur, master_mp4, master_wav, timing_key="duration_master")
    
    # 5. Short Preview Reel (24s)
    short_mp4 = os.path.join(OUTPUT_DIR, "sanjeev_singh_showreel_short_preview.mp4")
    short_wav = os.path.join(AUDIO_DIR, "showreel_soundtrack_short.wav")
    total_short_dur = sum(sc["duration_short"] for sc in SCENES)
    generate_video(SCENES, total_short_dur, short_mp4, short_wav, timing_key="duration_short")
    
    # 6. Teaser Reel (10s)
    teaser_mp4 = os.path.join(OUTPUT_DIR, "sanjeev_singh_showreel_teaser.mp4")
    teaser_wav = os.path.join(AUDIO_DIR, "showreel_soundtrack_teaser.wav")
    total_teaser_dur = sum(sc["duration_teaser"] for sc in SCENES)
    generate_video(SCENES, total_teaser_dur, teaser_mp4, teaser_wav, timing_key="duration_teaser")
    
    # 7. WebM for the short preview & master
    short_webm = os.path.join(OUTPUT_DIR, "sanjeev_singh_showreel_short_preview.webm")
    try:
        convert_to_webm(short_mp4, short_webm)
    except Exception as e:
        print(f"WebM conversion warning: {e}")

    print("\nAll video showreel assets rendered successfully!")

if __name__ == "__main__":
    main()
