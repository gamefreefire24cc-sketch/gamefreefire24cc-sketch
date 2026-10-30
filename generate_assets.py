"""Generates the animated SVG assets for the profile README. Edit the values below and re-run: python generate_assets.py"""
import random, os, math
random.seed(7)
os.makedirs("assets", exist_ok=True)
NS = 'xmlns="http://www.w3.org/2000/svg"'
FONT = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'Fira Code','SFMono-Regular',Consolas,'Liberation Mono',monospace"

def w(name, s):
    open(f"assets/{name}", "w", encoding="utf-8").write(s)

def cyc(a, b, c, dur="7s"):
    return f'<animate attributeName="stop-color" values="{a};{b};{c};{a}" dur="{dur}" repeatCount="indefinite"/>'

# ---------- HEADER ----------
parts = []
for i in range(28):
    x = random.randint(10, 890); y = random.randint(30, 250)
    r = random.choice([1.5, 2, 2.5, 3]); d = random.randint(4, 9); o = random.choice([0.35, 0.5, 0.7])
    parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity="{o}"><animate attributeName="cy" values="{y};{y-28};{y}" dur="{d}s" repeatCount="indefinite"/><animate attributeName="opacity" values="{o};0.1;{o}" dur="{d}s" repeatCount="indefinite"/></circle>')
header = f'''<svg {NS} width="900" height="280" viewBox="0 0 900 280">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f0c29"/><stop offset="0.55" stop-color="#2b2660"/><stop offset="1" stop-color="#17172f"/></linearGradient>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#8f94fb">{cyc("#8f94fb","#00d4ff","#ff6ac1")}</stop>
<stop offset="0.5" stop-color="#00d4ff">{cyc("#00d4ff","#ff6ac1","#8f94fb")}</stop>
<stop offset="1" stop-color="#ff6ac1">{cyc("#ff6ac1","#8f94fb","#00d4ff")}</stop>
</linearGradient>
<linearGradient id="bd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6c63ff"/><stop offset="0.5" stop-color="#00d4ff"/><stop offset="1" stop-color="#ff6ac1"/></linearGradient>
<filter id="blur"><feGaussianBlur stdDeviation="38"/></filter>
<clipPath id="clip"><rect x="2" y="2" width="896" height="276" rx="20"/></clipPath>
</defs>
<rect x="2" y="2" width="896" height="276" rx="20" fill="url(#bg)"/>
<g clip-path="url(#clip)">
<circle cx="150" cy="60" r="90" fill="#6c63ff" opacity="0.45" filter="url(#blur)"><animate attributeName="cx" values="150;300;150" dur="12s" repeatCount="indefinite"/></circle>
<circle cx="760" cy="230" r="100" fill="#ff6ac1" opacity="0.30" filter="url(#blur)"><animate attributeName="cx" values="760;600;760" dur="14s" repeatCount="indefinite"/></circle>
<circle cx="480" cy="140" r="80" fill="#00d4ff" opacity="0.18" filter="url(#blur)"><animate attributeName="cy" values="140;200;140" dur="10s" repeatCount="indefinite"/></circle>
{''.join(parts)}
</g>
<rect x="2" y="2" width="896" height="276" rx="20" fill="none" stroke="url(#bd)" stroke-width="2"/>
<text x="450" y="78" text-anchor="middle" font-family="{MONO}" font-size="15" fill="#a5a8ff" letter-spacing="6" opacity="0"><animate attributeName="opacity" from="0" to="0.9" dur="1.2s" fill="freeze"/>&lt; HELLO, WORLD /&gt;</text>
<text x="450" y="152" text-anchor="middle" font-family="{FONT}" font-size="64" font-weight="800" letter-spacing="5" fill="url(#tg)" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.3s" dur="1.2s" fill="freeze"/>JABER ISLAM</text>
<text x="450" y="192" text-anchor="middle" font-family="{FONT}" font-size="21" fill="#d9dbff" letter-spacing="2" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.8s" dur="1.2s" fill="freeze"/>Full-Stack Developer  ·  Python Enthusiast</text>
<line x1="330" y1="212" x2="570" y2="212" stroke="url(#bd)" stroke-width="2" stroke-linecap="round" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="1.1s" dur="1s" fill="freeze"/></line>
<text x="450" y="244" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#8c90d9" letter-spacing="2" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="1.4s" dur="1s" fill="freeze"/>PYTHON  •  TYPESCRIPT  •  GO  •  REACT  •  FASTAPI  •  POSTGRESQL</text>
</svg>'''
w("header.svg", header)

# ---------- DIVIDER ----------
w("divider.svg", f'''<svg {NS} width="900" height="12" viewBox="0 0 900 12">
<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6c63ff" stop-opacity="0"/><stop offset="0.2" stop-color="#6c63ff"/><stop offset="0.5" stop-color="#00d4ff"/><stop offset="0.8" stop-color="#ff6ac1"/><stop offset="1" stop-color="#ff6ac1" stop-opacity="0"/></linearGradient>
<radialGradient id="r"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
</defs>
<rect x="0" y="5" width="900" height="2" rx="1" fill="url(#g)"/>
<circle cx="0" cy="6" r="6" fill="url(#r)"><animate attributeName="cx" values="0;900" dur="4s" repeatCount="indefinite"/></circle>
</svg>''')

# ---------- SECTION TITLES ----------
def title(name, text):
    wd = 90 + len(text) * 15
    s = f'''<svg {NS} width="{wd}" height="54" viewBox="0 0 {wd} 54">
<defs>
<linearGradient id="b" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6c63ff">{cyc("#6c63ff","#00d4ff","#ff6ac1","6s")}</stop><stop offset="1" stop-color="#ff6ac1">{cyc("#ff6ac1","#6c63ff","#00d4ff","6s")}</stop></linearGradient>
<linearGradient id="t" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#aab0ff"/><stop offset="1" stop-color="#ffb3e1"/></linearGradient>
</defs>
<rect x="2" y="2" width="{wd-4}" height="50" rx="25" fill="#12122a" stroke="url(#b)" stroke-width="2"/>
<circle cx="28" cy="27" r="5" fill="#00d4ff"><animate attributeName="opacity" values="1;0.25;1" dur="2s" repeatCount="indefinite"/></circle>
<circle cx="{wd-28}" cy="27" r="5" fill="#ff6ac1"><animate attributeName="opacity" values="0.25;1;0.25" dur="2s" repeatCount="indefinite"/></circle>
<text x="{wd/2}" y="33" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="700" letter-spacing="4" fill="url(#t)">{text}</text>
</svg>'''
    w(f"title-{name}.svg", s)

for n, t in [("about", "ABOUT ME"), ("services", "WHAT I DO"), ("stack", "TECH STACK"), ("focus", "CORE FOCUS"),
             ("learning", "LEARNING &amp; GOALS"), ("projects", "FEATURED PROJECTS"), ("stats", "GITHUB ANALYTICS"),
             ("activity", "CONTRIBUTIONS"), ("contact", "LET'S CONNECT")]:
    title(n, t)

# ---------- TERMINAL ----------
lines = [
    (75, "$", "whoami", 0.03),
    (101, None, "jaber-islam · full-stack developer · python enthusiast", 0.10),
    (143, "$", "cat focus.txt", 0.22),
    (169, None, "scalable web apps · clean automation · readable code", 0.29),
    (211, "$", "./ship --clean --fast", 0.42),
    (237, None, "✔ shipping things that actually work", 0.49),
]
tl = ""
for y, pr, txt, f in lines:
    kt = f"0;{f};{f+0.02};0.93;0.98"
    anim = f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="{kt}" dur="16s" repeatCount="indefinite"/>'
    if pr:
        tl += f'<text x="30" y="{y}" font-family="{MONO}" font-size="16" opacity="0"><tspan fill="#7ee787">{pr}</tspan><tspan fill="#e6edf3" dx="10">{txt}</tspan>{anim}</text>\n'
    else:
        col = "#7ee787" if txt.startswith("✔") else "#79c0ff"
        tl += f'<text x="30" y="{y}" font-family="{MONO}" font-size="15" fill="{col}" opacity="0">{txt}{anim}</text>\n'
w("terminal.svg", f'''<svg {NS} width="900" height="270" viewBox="0 0 900 270">
<rect x="1" y="1" width="898" height="268" rx="14" fill="#0d1117" stroke="#30363d" stroke-width="2"/>
<path d="M1 15a14 14 0 0 1 14-14h870a14 14 0 0 1 14 14v26H1z" fill="#161b22"/>
<circle cx="26" cy="22" r="6" fill="#ff5f56"/><circle cx="48" cy="22" r="6" fill="#ffbd2e"/><circle cx="70" cy="22" r="6" fill="#27c93f"/>
<text x="450" y="27" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#8b949e">jaber@dev: ~/profile</text>
{tl}
<rect x="30" y="250" width="10" height="3" fill="#e6edf3"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>
</svg>''')

# ---------- SERVICES ----------
cards = [("01", "WEB APPS", "React · Next.js · Vue · Nuxt"),
         ("02", "BACKEND &amp; APIs", "FastAPI · NestJS · GraphQL"),
         ("03", "AUTOMATION", "Python scripts &amp; tooling"),
         ("04", "DATA &amp; ML", "Pandas · NumPy · scikit-learn")]
sv = ""
for i, (n, t, sub) in enumerate(cards):
    x = i * 231
    sv += f'''<g transform="translate({x},0)">
<rect x="1" y="1" width="205" height="168" rx="14" fill="#13132b" stroke="#2c2c58" stroke-width="2"/>
<rect x="1" y="1" width="205" height="5" rx="2.5" fill="url(#b)"><animate attributeName="opacity" values="1;0.35;1" dur="3s" begin="{i*0.5}s" repeatCount="indefinite"/></rect>
<text x="22" y="62" font-family="{FONT}" font-size="40" font-weight="800" fill="#6c63ff" opacity="0.35">{n}</text>
<text x="22" y="100" font-family="{FONT}" font-size="16" font-weight="700" letter-spacing="2" fill="#eceeff">{t}</text>
<text x="22" y="128" font-family="{FONT}" font-size="12.5" fill="#9aa0d8">{sub}</text>
</g>'''
w("services.svg", f'''<svg {NS} width="900" height="170" viewBox="0 0 900 170">
<defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6c63ff"/><stop offset="0.5" stop-color="#00d4ff"/><stop offset="1" stop-color="#ff6ac1"/></linearGradient></defs>
{sv}</svg>''')

# ---------- FOCUS BARS (edit the percentages) ----------
bars = [("Backend Development", 90), ("Frontend Development", 85), ("Python &amp; Automation", 92),
        ("Data &amp; Machine Learning", 70), ("DevOps &amp; Tooling", 75)]
bs = ""
for i, (lab, p) in enumerate(bars):
    y = 20 + i * 52
    bs += f'''<text x="24" y="{y+17}" font-family="{FONT}" font-size="15" font-weight="600" fill="#e1e3ff">{lab}</text>
<rect x="270" y="{y}" width="520" height="22" rx="11" fill="#1a1a3a" stroke="#2c2c58"/>
<rect x="270" y="{y}" width="0" height="22" rx="11" fill="url(#f)"><animate attributeName="width" from="0" to="{520*p/100:.0f}" dur="1.6s" begin="{i*0.25}s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1" keyTimes="0;1"/></rect>
<text x="876" y="{y+17}" text-anchor="end" font-family="{MONO}" font-size="15" fill="#aab0ff">{p}%</text>
'''
w("focus.svg", f'''<svg {NS} width="900" height="{20+len(bars)*52}" viewBox="0 0 900 {20+len(bars)*52}">
<defs><linearGradient id="f" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6c63ff"/><stop offset="0.6" stop-color="#00d4ff"/><stop offset="1" stop-color="#ff6ac1"/></linearGradient></defs>
{bs}</svg>''')

# ---------- FOOTER WAVE ----------
def wave(amp, base):
    pts = []
    for x in range(0, 1801, 25):
        pts.append(f"{x},{base + amp*math.sin(x/450*2*math.pi):.1f}")
    return "M" + " L".join(pts) + " L1800,130 L0,130 Z"
w("footer.svg", f'''<svg {NS} width="900" height="130" viewBox="0 0 900 130">
<defs><linearGradient id="w" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6c63ff"/><stop offset="0.5" stop-color="#00d4ff"/><stop offset="1" stop-color="#ff6ac1"/></linearGradient></defs>
<path d="{wave(14,70)}" fill="url(#w)" opacity="0.35"><animateTransform attributeName="transform" type="translate" from="0 0" to="-450 0" dur="9s" repeatCount="indefinite"/></path>
<path d="{wave(10,90)}" fill="url(#w)" opacity="0.6"><animateTransform attributeName="transform" type="translate" from="-450 0" to="0 0" dur="13s" repeatCount="indefinite"/></path>
</svg>''')
print("assets generated")
