"""Generates Gojo-themed stats SVG cards from the GitHub API (no third-party service)."""
import json, os, sys, urllib.request
from html import escape
CY, VIO, GOLD, PINK, FUC, TXT, MUTED = '#4CC9FF', '#A78BFA', '#FFD45E', '#F472B6', '#E879F9', '#F2F8FF', '#C7D6EA'
LANG_COL = [CY, VIO, GOLD, PINK, '#4ADE80', FUC]

def api(path, token):
    req = urllib.request.Request('https://api.github.com' + path, headers={'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {token}', 'User-Agent': 'gojo-stats'})
    return json.load(urllib.request.urlopen(req, timeout=30))

def fetch(user, token):
    u = api(f'/users/{user}', token)
    repos = api(f'/users/{user}/repos?per_page=100&type=owner', token)
    langs = {}
    for r in repos:
        if r['fork']: continue
        try:
            for k, v in api(f"/repos/{user}/{r['name']}/languages", token).items(): langs[k] = langs.get(k, 0) + v
        except Exception: pass
    stats = dict(repos=u['public_repos'], stars=sum(r['stargazers_count'] for r in repos), forks=sum(r['forks_count'] for r in repos),
                 followers=u['followers'], since=u['created_at'][:4])
    return stats, langs

HEAD = lambda w, h, title, label: f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#070B1A"/><stop offset=".6" stop-color="#0E1233"/><stop offset="1" stop-color="#090D22"/></linearGradient>
<linearGradient id="edge"><stop stop-color="{CY}"/><stop offset=".55" stop-color="{VIO}"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#9FD8FF" opacity=".14"/></pattern></defs>
<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="22" fill="url(#bg)" stroke="url(#edge)" stroke-width="2"/><rect x="3" y="3" width="{w-6}" height="{h-6}" rx="21" fill="url(#dots)"/>
<text x="28" y="42" fill="{CY}" font-family="Arial,sans-serif" font-size="12" font-weight="700" letter-spacing="2.2">✦  {title}</text>'''

def stats_svg(s, ph):
    rows = [('PUBLIC REPOSITORIES', s['repos'], CY), ('TOTAL STARS', s['stars'], GOLD), ('TOTAL FORKS', s['forks'], VIO), ('FOLLOWERS', s['followers'], PINK)]
    mx = max(max(v for _, v, _ in rows), 1)
    o = HEAD(495, 230, 'CURSED ENERGY STATS', 'GitHub statistics')
    for i, (lab, v, c) in enumerate(rows):
        y = 78 + i * 36
        val = '—' if ph else str(v)
        o += (f'<text x="28" y="{y}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="11" font-weight="700" letter-spacing="1.1">{lab}</text>'
              f'<text x="467" y="{y}" text-anchor="end" fill="{TXT}" font-family="Arial,sans-serif" font-size="18" font-weight="800">{val}</text>'
              f'<rect x="28" y="{y+8}" width="439" height="8" rx="4" fill="#1B2447"/><rect x="28" y="{y+8}" width="{0 if ph else max(10, 439*v/mx):.0f}" height="8" rx="4" fill="{c}"/>')
    foot = 'RUN THE WORKFLOW TO REFRESH' if ph else f'SORCERER SINCE {s["since"]}'
    return o + f'<text x="28" y="218" fill="#7E93B5" font-family="Arial,sans-serif" font-size="10" font-weight="700" letter-spacing="1.1">{foot}</text></svg>'

def langs_svg(l, ph):
    tot = sum(l.values()) or 1
    top = sorted(l.items(), key=lambda kv: -kv[1])[:6]
    o = HEAD(495, 230, 'TOP TECHNIQUES / LANGUAGES', 'Top programming languages')
    if ph or not top: top = [('Run workflow to refresh', 0)]
    for i, (n, b) in enumerate(top):
        y = 74 + i * 24; pct = 100 * b / tot; c = LANG_COL[i % 6]
        o += (f'<text x="28" y="{y}" fill="{TXT}" font-family="Arial,sans-serif" font-size="12" font-weight="700">{escape(n)}</text>'
              f'<text x="467" y="{y}" text-anchor="end" fill="{MUTED}" font-family="Arial,sans-serif" font-size="11" font-weight="700">{"" if ph or not b else f"{pct:.1f}%"}</text>'
              + (f'<rect x="150" y="{y-9}" width="250" height="8" rx="4" fill="#1B2447"/><rect x="150" y="{y-9}" width="{max(6, 250*pct/100):.0f}" height="8" rx="4" fill="{c}"/>' if b and not ph else ''))
    return o + '</svg>'

def write(out, stats, langs, ph=False):
    os.makedirs(out, exist_ok=True)
    open(f'{out}/stats.svg', 'w', encoding='utf-8').write(stats_svg(stats, ph))
    open(f'{out}/langs.svg', 'w', encoding='utf-8').write(langs_svg(langs, ph))

if __name__ == '__main__':
    user, token = os.environ['USERNAME'], os.environ['GITHUB_TOKEN']
    s, l = fetch(user, token); write('profile-stats', s, l); print('stats written', s)
