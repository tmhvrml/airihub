# -*- coding: utf-8 -*-
"""Rendering helpers for the ai.ri.gov prototype."""
import html, json, os, re

SITE = "AI RI Hub"

NAV = [
    ("About", "about.html", [
        ("About the AI RI Hub", "about-overview.html"),
        ("Leadership &amp; Team", "about-team.html"),
        ("Partners", "about-partners.html"),
        ("FAQs", "about-faqs.html"),
        ("Contact", "about-contact.html"),
    ]),
    ("Programs &amp; Initiatives", "programs.html", [
        ("AI Compute Resources", "programs-ai-compute-resources.html"),
        ("Workforce &amp; Credentialing", "programs-workforce-credentialing.html"),
        ("Small Business &amp; Nonprofit", "programs-small-business-nonprofit.html"),
        ("AI Solution Registry", "programs-solution-registry.html"),
        ("Responsible AI &amp; Governance", "programs-responsible-ai-governance.html"),
        ("Grants &amp; Funding", "programs-grants.html"),
    ]),
    ("Education/Training", "education-training.html", [
        ("Grow with Google — Rhode Island", "education-training-grow-with-google.html"),
        ("Additional AI Training Resources", "education-training-additional-resources.html"),
        ("Cybersecurity &amp; AI Practicum", "education-training-cyber-ai-practicum.html"),
        ("Future Ready (K-12) &amp; Summer Academy", "education-training-future-ready.html"),
    ]),
    ("Jobs Board", "jobs.html", []),
    ("News/Events", "news-events.html", [
        ("News", "news-events-news.html"),
        ("Events", "news-events-events.html"),
        ("Rhode Island AI Summit", "news-events-ai-summit.html"),
        ("Activity &amp; Impact", "news-events-activity.html"),
    ]),
]

# Display text is authored by us and may contain intentional HTML entities
# (&mdash;, &rsquo;, &amp;). Passing it through html.escape() a second time
# would render them literally, so display text is emitted raw and only
# attribute values are escaped.
e = lambda t: t

def att(t):
    """Escape a string for use inside an HTML attribute, decoding any
    entities first so they are not double-escaped."""
    return html.escape(html.unescape(str(t)), quote=True)

def slug(t):
    """Stable id/name from a label."""
    t = html.unescape(str(t)).lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

# ---------------- block renderers ----------------
def ph(kind, desc, alt=None, cls="", priority="Launch"):
    """Placeholder image standing in for a planned asset."""
    later = priority != "Launch"
    k = f'<span class="ph__kind{" ph__kind--later" if later else ""}">{e(kind)}{"" if not later else " · " + e(priority)}</span>'
    a = f'<p class="ph__alt"><b>Alt text:</b> {e(alt)}</p>' if alt else ""
    return f'<figure class="ph {cls}" role="img" aria-label="Placeholder image. {att(desc)}">{k}<p class="ph__desc">{e(desc)}</p>{a}</figure>'

def h(level, text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<h{level}{c}>{text}</h{level}>"

def p(text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<p{c}>{text}</p>"

def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

def btns(items):
    out = []
    for label, href, style in items:
        out.append(f'<a class="btn {style}" href="{href}">{e(label)}</a>')
    return '<div class="btn-row">' + "".join(out) + "</div>"

def cards(items, cols=3):
    out = []
    for c in items:
        tag = f'<span class="tag {c.get("tagcls","")}">{e(c["tag"])}</span>' if c.get("tag") else ""
        thumb = c.get("thumb", "")
        more = f'<a class="more" href="{c["href"]}">{e(c.get("more","Learn more"))}</a>' if c.get("href") else ""
        out.append(f'<article class="card">{thumb}<div class="card__body">{tag}<h3>{e(c["title"])}</h3><p>{c["body"]}</p>{more}</div></article>')
    return f'<div class="cards cards--{cols}">' + "".join(out) + "</div>"

def stats(items):
    out = "".join(f'<div class="stat"><b>{e(n)}</b><p>{t}</p></div>' for n, t in items)
    return f'<div class="stats">{out}</div>'

def pillars(items):
    out = ""
    for i, (num, title, body) in enumerate(items, 1):
        out += f'<div class="pillar"><div class="ico" aria-hidden="true">{num}</div><h3>{e(title)}</h3><p>{body}</p></div>'
    return f'<div class="pillars">{out}</div>'

def acc(items):
    out = "".join(
        f"<details><summary>{e(q)}</summary><div class='accbody'>{a}</div></details>" for q, a in items
    )
    return f'<div class="acc">{out}</div>'

def table(headers, rows):
    th = "".join(f"<th>{e(x)}</th>" for x in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="data"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

def callout(body):
    return f'<div class="callout">{body}</div>'

def feed(items):
    out = ""
    for d, t, b, href in items:
        link = f'<a href="{href}">{e(t)}</a>' if href else e(t)
        out += f'<li><div class="date">{e(d)}</div><div><h3>{link}</h3><p>{b}</p></div></li>'
    return f'<ul class="feed">{out}</ul>'

def linklist(items):
    out = "".join(f'<li><a href="{href}"><strong>{e(t)}</strong><span>{d}</span></a></li>' for t, d, href in items)
    return f'<ul class="linklist">{out}</ul>'

def field(label, kind="text", req=False, hint="", options=None, name=""):
    r = ' <span class="req">(required)</span>' if req else ""
    nm = name or slug(label)
    if options:
        opts = "".join(f"<option>{att(o)}</option>" for o in options)
        ctl = f'<select id="{nm}" name="{nm}"><option value="">Choose one…</option>{opts}</select>'
    elif kind == "textarea":
        ctl = f'<textarea id="{nm}" name="{nm}" rows="5"></textarea>'
    else:
        ctl = f'<input id="{nm}" name="{nm}" type="{kind}">'
    hn = f'<p class="hint">{e(hint)}</p>' if hint else ""
    return f'<div class="field"><label for="{nm}">{e(label)}{r}</label>{ctl}{hn}</div>'

def form(title, fields, submit, note=""):
    n = f'<p class="hint" style="margin-top:14px">{note}</p>' if note else ""
    return (f'<form class="form" onsubmit="return false"><h2 style="margin-top:0;font-size:1.3rem">{e(title)}</h2>'
            + "".join(fields) + f'<button class="btn" type="submit">{e(submit)}</button>{n}</form>')

def section(inner, cls="", id=None, narrow=False):
    i = f' id="{id}"' if id else ""
    w = "wrap narrow" if narrow else "wrap"
    return f'<section class="{cls}"{i}><div class="{w}">{inner}</div></section>'

def metrics(items):
    out = "".join(f'<div class="metric"><b>{e(v)}</b><span>{e(l)}</span><em>{e(n)}</em></div>' for v, l, n in items)
    return f'<div class="metrics">{out}</div>'

def person(initials, name, role, bio, avatar_desc=None):
    av = f'<div class="initials" aria-hidden="true">{e(initials)}</div>'
    if avatar_desc:
        av = (f'<figure class="ph ph--sq" role="img" aria-label="Placeholder for a headshot of {att(name)}.">'
              f'<span class="ph__kind">Headshot</span></figure>')
    return (f'<div class="person"><div class="avatar">{av}</div><div><h3>{e(name)}</h3>'
            f'<p class="role">{e(role)}</p><p>{bio}</p></div></div>')

def people(items):
    return '<div class="people">' + "".join(items) + "</div>"

def job(title, org, body, chips):
    ch = "".join(f'<span class="chip">{e(c)}</span>' for c in chips)
    return (f'<div class="job"><h3>{e(title)}</h3><p class="org">{e(org)}</p><p style="font-size:.94rem">{body}</p>'
            f'<div class="chips">{ch}</div></div>')
