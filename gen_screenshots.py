from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def make_dashboard():
    w, h = 800, 520
    img = Image.new('RGB', (w, h), (10, 10, 15))
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([0, 0, w, 48], fill=(20, 20, 31))

    # Title
    draw.text((20, 14), "🔍  GKWatch Dashboard", fill=(232, 232, 240))

    # Stat cards
    colors = [(108, 92, 231), (0, 206, 201), (0, 184, 148), (253, 203, 110)]
    for i, (val, label, c) in enumerate([
        ("9", "Cibles", colors[0]),
        ("3", "JS render", colors[1]),
        ("14", "Changements", colors[2]),
        ("2.3 Mo", "Logs", colors[3]),
    ]):
        x = 20 + i * 195
        draw.rounded_rectangle([x, 64, x + 180, 114], radius=10, fill=(20, 20, 31), outline=(42, 42, 63))
        draw.text((x + 12, 72), val, fill=c, font=None)
        draw.text((x + 12, 98), label, fill=(136, 136, 160))

    # Table header
    draw.text((20, 130), "🎯  Cibles surveillées", fill=(136, 136, 160))
    draw.text((20, 155), "Nom                   Tags               URL                        Mode     Check", fill=(60, 60, 80))
    draw.line([(20, 172), (w - 20, 172)], fill=(42, 42, 63))

    rows = [
        ("✅  Concurrent A", "ecommerce", "exemple.com/pricing", "HTTP", "10:02"),
        ("✅  Concurrent B", "blog, veille", "exemple.com/blog", "HTTP", "10:02"),
        ("⏳  Show HN",   "prospection", "hn.algolia.com", "HTTP", "08:30"),
    ]
    for i, (name, tags, url, mode, t) in enumerate(rows):
        y = 180 + i * 28
        draw.text((20, y), name, fill=(232, 232, 240))
        draw.text((220, y), tags, fill=(136, 136, 160))
        draw.text((340, y), url, fill=(108, 92, 231))
        draw.text((550, y), mode, fill=(136, 136, 160))
        draw.text((610, y), t, fill=(136, 136, 160))
        draw.line([(20, y + 24), (w - 20, y + 24)], fill=(42, 42, 63))

    # Activity section
    draw.text((20, 275), "📋  Activité récente", fill=(136, 136, 160))
    draw.rounded_rectangle([20, 295, w - 20, 500], radius=10, fill=(20, 20, 31), outline=(42, 42, 63))
    changes = [
        "🔍  show-hn: CHANGEMENT DÉTECTÉ — +5 nouveaux éléments",
        "📨  Alerte envoyée Telegram",
        "🔍  frenchtech: CHANGEMENT DÉTECTÉ",
    ]
    for i, c in enumerate(changes):
        draw.text((32, 305 + i * 28), c, fill=(136, 136, 160))

    # Gradient accent line
    for x in range(w):
        r = int(108 + (0 - 108) * x / w)
        g = int(92 + (206 - 92) * x / w)
        b = int(231 + (201 - 231) * x / w)
        draw.point((x, h - 3), fill=(r, g, b))

    img.save('/tmp/gkwatch-landing/dashboard.webp', 'WEBP', quality=85)
    print("✅ dashboard.webp")

def make_telegram_alert():
    # Mock Telegram message
    w, h = 500, 320
    img = Image.new('RGB', (w, h), (30, 35, 42))
    draw = ImageDraw.Draw(img)

    # Chat header
    draw.rectangle([0, 0, w, 50], fill=(40, 45, 52))

    # Bot avatar circle
    draw.ellipse([12, 10, 42, 40], fill=(108, 92, 231))
    draw.text((20, 19), "🤖", fill=(255, 255, 255))

    # Bot name
    draw.text((50, 12), "GKWatch Bot", fill=(232, 232, 240))

    # Now text
    draw.text((300, 14), "now", fill=(136, 136, 160))

    # Message bubble
    bx, by = 12, 62
    bw, bh = w - 24, 210
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=10, fill=(40, 48, 58))

    # Alert header
    draw.text((24, 70), "🔍  GKWatch — Nouveau prospect détecté", fill=(255, 200, 80))

    items = [
        "Nouveau projet SaaS lancé sur Show HN :",
        "  • OpenClaw CLI — outil IA pour développeurs",
        "  • 23 points, 14 commentaires en 2h",
        "  • Fondateur @johndoe (YC W25)",
        "",
        "💡  Suggestion de contact :",
        "  'Super projet ! On pourrait échanger sur'",
        "  'l'intégration avec notre stack de veille...'",
    ]
    y = 100
    for line in items:
        c = (136, 136, 160) if line.startswith("  ") else (232, 232, 240)
        if line.startswith("💡"):
            c = (108, 92, 231)
        draw.text((24, y), line, fill=c)
        y += 20

    # Footer
    draw.text((20, h - 24), "🔍  GKWatch", fill=(108, 92, 231))

    img.save('/tmp/gkwatch-landing/telegram_alert.webp', 'WEBP', quality=85)
    print("✅ telegram_alert.webp")

os.makedirs('/tmp/gkwatch-landing', exist_ok=True)
make_dashboard()
make_telegram_alert()
