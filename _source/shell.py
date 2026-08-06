# -*- coding: utf-8 -*-
"""Page shell: ribbon, masthead, nav, breadcrumbs, footer."""
from lib import NAV, e, att

PROTO = ("<div class='proto'><div class='wrap'><span>Prototype — AI RI Hub website, built from "
         "Website Content Outline &amp; Draft Copy v3.0. All images are placeholders; forms are not wired up.</span>"
         "<a href='_review.html'>Open the editorial review checklist &rarr;</a></div></div>")

RIBBON = """<div class="ribbon"><div class="wrap">
  <div class="grp"><span class="lbl">Language</span>
    <select id="lang" aria-label="Select language"><option>English</option><option>Espa&ntilde;ol</option></select></div>
  <div class="grp"><span class="lbl">Text size</span>
    <select id="textSize" aria-label="Adjust text size">
      <option value="">Default</option><option value="18px">Large</option><option value="20px">Larger</option></select></div>
  <div class="grp"><button id="themeToggle" type="button" aria-pressed="false">Dark mode</button></div>
</div></div>"""

def masthead(active):
    items = ""
    for label, href, kids in NAV:
        on = " class='on'" if active == href or (kids and active in [k[1] for k in kids]) else ""
        cur = ' aria-current="page"' if active == href else ""
        caret = '<span class="caret" aria-hidden="true">▾</span>' if kids else ""
        sub = ""
        if kids:
            links = "".join(f'<a href="{k[1]}">{e(k[0])}</a>' for k in kids)
            sub = f'<div class="sub">{links}</div>'
        items += f'<li{on}><a href="{href}"{cur}>{e(label)}{caret}</a>{sub}</li>'
    home_on = " class='nav-home on'" if active in ("index.html", "") else " class='nav-home'"
    return f"""<header class="masthead"><div class="wrap">
  <a class="brand" href="index.html">
    <span class="brand__mark" aria-hidden="true">AI</span>
    <span class="brand__txt"><small>State of Rhode Island</small><strong>AI RI Hub</strong><span>Statewide AI Coordination Hub</span></span>
  </a>
  <form class="search" role="search" onsubmit="return false">
    <input type="search" aria-label="Search the site" placeholder="Search the site">
    <button type="submit" aria-label="Search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#241D1B" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.5" y2="16.5"></line></svg></button>
  </form>
  <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="primaryNav">Menu</button>
</div></header>
<nav class="nav" id="primaryNav" aria-label="Primary"><div class="wrap"><ul>
  <li{home_on}><a href="index.html" aria-label="Home"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-8 9 8"></path><path d="M5 10v10h14V10"></path></svg></a></li>
  {items}
</ul></div></nav>"""

def crumbs(trail):
    if not trail:
        return ""
    bits = ['<a href="index.html">Home</a>']
    for t in trail[:-1]:
        bits.append(f'<a href="{t[1]}">{e(t[0])}</a>')
    bits.append(f'<span aria-current="page">{e(trail[-1][0])}</span>')
    return ('<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap">'
            + ' <span aria-hidden="true">&rsaquo;</span> '.join(bits) + "</div></nav>")

NEWSLETTER = """<div class="news-sign"><div class="wrap"><div class="inner">
  <div><h2>Stay in the loop</h2><p>Monthly, no more. Training openings, compute deadlines, events, and what the Hub is learning.</p></div>
  <form class="form" onsubmit="return false">
    <div class="grid2">
      <div class="field"><label for="nf">First name</label><input id="nf" type="text"></div>
      <div class="field"><label for="nl">Last name</label><input id="nl" type="text"></div>
    </div>
    <div class="grid2">
      <div class="field"><label for="nt">Title</label><input id="nt" type="text"></div>
      <div class="field"><label for="no">Organization</label><input id="no" type="text"></div>
    </div>
    <div class="field"><label for="ne">Email <span class="req">(required)</span></label><input id="ne" type="email">
      <p class="hint">Only your email is required. Read our <a href="#">privacy statement</a>.</p></div>
    <button class="btn" type="submit">Sign me up</button>
  </form>
</div></div></div>"""

FOOTER = """<footer>
  <div class="foot-res"><div class="wrap">
    <a href="#">Procurements</a><a href="#">Grants</a><a href="#">Public Notices</a>
    <a href="#">Employment</a><a href="about-contact.html">Contact</a>
  </div></div>
  <div class="foot-main"><div class="wrap">
    <div>
      <h3>AI RI Hub</h3>
      <address>Institute for Cybersecurity and Emerging Technologies<br>
        Rhode Island College<br>600 Mount Pleasant Avenue<br>Providence, RI 02908</address>
      <div class="social">
        <a href="#" aria-label="LinkedIn">in</a><a href="#" aria-label="YouTube">YT</a><a href="#" aria-label="RSS feed">RSS</a>
      </div>
    </div>
    <div><h3>Programs</h3><ul>
      <li><a href="programs-ai-compute-resources.html">AI Compute Resources</a></li>
      <li><a href="programs-workforce-credentialing.html">Workforce &amp; Credentialing</a></li>
      <li><a href="programs-small-business-nonprofit.html">Small Business &amp; Nonprofit</a></li>
      <li><a href="programs-solution-registry.html">AI Solution Registry</a></li>
      <li><a href="programs-grants.html">Grants &amp; Funding</a></li>
    </ul></div>
    <div><h3>Get started</h3><ul>
      <li><a href="education-training-grow-with-google.html">Free Google AI training</a></li>
      <li><a href="programs-ai-compute-resources.html">Request compute access</a></li>
      <li><a href="jobs.html">Jobs board</a></li>
      <li><a href="news-events-activity.html">Activity &amp; impact</a></li>
      <li><a href="about-contact.html">Contact the Hub</a></li>
    </ul></div>
  </div></div>
  <div class="foot-priv"><div class="wrap">
    <a href="#">Privacy Policy</a><a href="#">Accessibility</a><span>&copy; 2026 State of Rhode Island</span>
  </div></div>
</footer>"""

def page(slug, title, body, active=None, trail=None, newsletter=True, desc=""):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{att(title)} | AI RI Hub</title>
<meta name="description" content="{att(desc)}">
<link rel="stylesheet" href="assets/style.css">
<script src="assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
{PROTO}
{RIBBON}
{masthead(active or slug)}
{crumbs(trail)}
<main id="main">
{body}
</main>
{NEWSLETTER if newsletter else ""}
{FOOTER}
</body>
</html>"""
