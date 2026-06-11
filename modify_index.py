import re

with open('C:/xampp/htdocs/webtoolkit-pro/abusufyan-xyz/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero
html = html.replace('<div class="hero-tag"><span class="nav-dot"></span>Indie Maker · 5 Live Projects · Building in Public · Pakistan</div>',
                    '<div class="hero-tag"><span class="nav-dot"></span>Solo Maker · Lahore, Pakistan</div>')

html = html.replace('<h1 class="hero-h reveal" data-delay="1" id="hero-heading">Free Tools <em>That</em> Work.</h1>',
                    '<h1 class="hero-h reveal" data-delay="1" id="hero-heading">The person who needs a tool most usually can\'t <em>afford</em> a lawyer.</h1>')

html = html.replace('<p class="hero-desc">Hi, I\'m <strong>Abu Sufyan</strong>. I build free professional tools for people who need quick, reliable answers — HR managers, developers, CFOs, employees. <strong>No sign-up. No paywall. Just the answer.</strong></p>',
                    '<p class="hero-desc">Hi, I\'m <strong>Abu Sufyan</strong>. I build free professional tools for people who need quick, reliable answers. When I couldn\'t find clean, sign-up-free utilities for HR managers, developers, and CFOs, I decided to build them myself. <strong>No sign-up. No paywall. Just the answer.</strong></p>')

# 2. Add New CSS
new_css = """
/* ── STORY LISTING ── */
.story-listing { display: flex; flex-direction: column; gap: 48px; }
.story-item h3 { font-family: 'Playfair Display', serif; font-size: 28px; margin-bottom: 12px; }
.story-item h3 a { color: var(--text); text-decoration: none; transition: color 0.2s; }
.story-item h3 a:hover { color: var(--accent2); }
.story-item p { font-size: 15px; color: var(--muted); line-height: 1.8; max-width: 700px; }
.story-item:active { transform: scale(0.99); transition: transform 160ms var(--ease-out); }

/* ── IMPACT GRID ── */
.impact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.impact-item { background: var(--surface); border: 1px solid var(--border); padding: 32px; border-radius: 4px; }
.impact-quote { font-size: 15px; color: var(--text); line-height: 1.7; font-style: italic; }
@media(max-width: 700px) { .impact-grid { grid-template-columns: 1fr; } }
"""
html = html.replace('</style>', new_css + '\n</style>')

# 3. Replace Tools section
tools_old = re.search(r'<div class="listing" style="margin-top:2px" id="tools-listing">.*?</section>', html, re.DOTALL)
if tools_old:
    tools_new = """<div class="story-listing" style="margin-top:40px">
    <div class="story-item reveal" data-delay="1">
      <h3><a href="https://wtkpro.site" target="_blank" rel="noopener">WebToolkit Pro ↗</a></h3>
      <p>I got tired of pasting sensitive JSON payloads into random ad-filled sites just to format them. So I built a client-side only toolkit. No servers, no data logging. It started with 12 utilities and has organically grown to 150+ tools used by developers and writers daily.</p>
    </div>
    <div class="story-item reveal" data-delay="2">
      <h3><a href="https://severancecalculator.xyz" target="_blank" rel="noopener">Severance Calculator ↗</a></h3>
      <p>I couldn't find a clean severance calculator for Pakistan that didn't require an email sign-up. I built one in a weekend. Then HR managers started asking for UAE, then the UK, then the US. It now covers 30+ countries with official 2026 labor law formulas and gets used globally every single day.</p>
    </div>
    <div class="story-item reveal" data-delay="3">
      <h3><a href="https://tradeconvert.pro" target="_blank" rel="noopener">TradeConvert ↗</a></h3>
      <p>Construction workers and engineers spend hours looking at unreadable PDF conversion tables on job sites. TradeConvert turns NIST-verified technical reference data into a clean, mobile-first interface they can actually tap with gloves on.</p>
    </div>
    <div class="story-item reveal" data-delay="4">
      <h3><a href="https://slabreachcalculator.site/" target="_blank" rel="noopener">SLA Breach Calculator ↗</a></h3>
      <p>Computing financial penalties and service credits for B2B IT contracts is a nightmare of spreadsheet formulas. I built this to instantly calculate uptime shortfalls for procurement teams and IT managers so they don't have to hire expensive consultants.</p>
    </div>
    <div class="story-item reveal" data-delay="5">
      <h3><a href="https://crawl-scope.vercel.app/" target="_blank" rel="noopener">CrawlScope ↗</a></h3>
      <p>As AI started scraping the web, I needed a way to audit how GPTBot and Anthropic actually read my sites. CrawlScope is a dashboard that simulates AI crawlers and checks your robots.txt defenses. Built primarily for technical SEOs.</p>
    </div>
  </div>
</section>"""
    html = html.replace(tools_old.group(0), tools_new)

# 4. Replace Proof section
proof_old = re.search(r'<div class="proof-grid" style="margin-top:28px">.*?</div>\s*</div>\s*</section>', html, re.DOTALL)
if proof_old:
    proof_new = """<div class="impact-grid" style="margin-top:28px">
    <div class="impact-item reveal" data-delay="0">
      <div class="impact-quote">"An HR manager in Qatar used the Severance Calculator at 2am to figure out a payout. That's the product."</div>
    </div>
    <div class="impact-item reveal" data-delay="1">
      <div class="impact-quote">"TradeConvert is actively bookmarked on iPads at construction sites because the official reference PDFs are unreadable on mobile."</div>
    </div>
    <div class="impact-item reveal" data-delay="2">
      <div class="impact-quote">"A developer formatted a sensitive JWT token on WebToolkit Pro because it strictly runs client-side. Zero trust architecture matters."</div>
    </div>
    <div class="impact-item reveal" data-delay="3">
      <div class="impact-quote">"Over 150 tools built without a single marketing dollar spent. Just spotting gaps and out-executing the SEO competition."</div>
    </div>
  </div>
</section>"""
    html = html.replace(proof_old.group(0), proof_new)

# 5. Update Build Log descriptions
html = html.replace('<div class="tl-d">Dev tools hub, grew to 150+ live utilities</div>',
                    '<div class="tl-d">Launched with 12 tools. Now at 150+. Zero marketing budget.</div>')
html = html.replace('<div class="tl-d">Trade unit converters for construction &amp; engineering</div>',
                    '<div class="tl-d">Built because finding reliable density formulas on mobile was impossible.</div>')
html = html.replace('<div class="tl-d">8 countries · 2026 laws · Global HR tool</div>',
                    '<div class="tl-d">Built for Pakistan first. Expanded to 30+ countries after global HR requests.</div>')
html = html.replace('<div class="tl-d">SLA penalty and service credit calculator</div>',
                    '<div class="tl-d">Saving IT managers from writing complex Excel formulas for downtime.</div>')
html = html.replace('<div class="tl-d">GEO & AI Crawler Audit Dashboard</div>',
                    '<div class="tl-d">Needed a way to see how GPTBot was reading my own portfolio.</div>')
html = html.replace('<div class="tl-d">For CFOs and financial analysts</div>',
                    '<div class="tl-d">Building this because CFOs asked for it after using the Severance tool.</div>')
html = html.replace('<div class="tl-d">LTL logistics tool for US shippers</div>',
                    '<div class="tl-d">Democratizing freight class data hidden behind carrier portals.</div>')

# 6. Remove Ripple JS
html = re.sub(r'/\* ── 7\. BUTTON CLICK RIPPLE \(lightweight\) ── \*/.*?document\.head\.appendChild\(rStyle\);', '/* ── 7. REMOVED RIPPLE FOR EMIL DESIGN POLISH ── */', html, flags=re.DOTALL)

with open('C:/xampp/htdocs/webtoolkit-pro/abusufyan-xyz/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modification complete.")
