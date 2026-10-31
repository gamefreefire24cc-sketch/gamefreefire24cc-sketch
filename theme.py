"""Re-colour every SVG in assets/ with a different palette.
Usage:  python generate_assets.py && python theme.py ocean      (themes: violet, ocean, sunset, emerald)
Run generate_assets.py first each time, so colours always start from the default violet theme."""
import glob, sys
THEMES = {
    "violet":  {},
    "ocean":   {"#7c5cff": "#0ea5e9", "#6c63ff": "#0284c7", "#00d4ff": "#2dd4bf", "#ff6ac1": "#34d399", "#aab0ff": "#9bd6ff", "#b9bdff": "#bfe7ff", "#ffc2e8": "#b8f5dc"},
    "sunset":  {"#7c5cff": "#f97316", "#6c63ff": "#ea580c", "#00d4ff": "#fbbf24", "#ff6ac1": "#f43f5e", "#aab0ff": "#ffc9a0", "#b9bdff": "#ffd9b8", "#ffc2e8": "#ffc2cc"},
    "emerald": {"#7c5cff": "#10b981", "#6c63ff": "#059669", "#00d4ff": "#a3e635", "#ff6ac1": "#22d3ee", "#aab0ff": "#a7f3d0", "#b9bdff": "#c8f7e1", "#ffc2e8": "#c5f6fa"},
}
name = sys.argv[1] if len(sys.argv) > 1 else "violet"
mapping = THEMES[name]
for f in glob.glob("assets/*.svg"):
    s = open(f, encoding="utf-8").read()
    for a, b in mapping.items():
        s = s.replace(a, b).replace(a.upper(), b)
    open(f, "w", encoding="utf-8").write(s)
print("theme applied:", name)
