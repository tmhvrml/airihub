# -*- coding: utf-8 -*-
import os, json, importlib, html
import lib, shell, register
from lib import e, att, section, h, p, table
import pg_home, pg_about, pg_programs, pg_rest

OUT = os.environ.get("OUTDIR", os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def review_page():
    sevcls = {"BLOCKER": "#B3261E", "VERIFY": "#8A6D0B", "DECISION": "#293557"}
    c = register.counts()
    rows = ""
    for it in register.ITEMS:
        pages = " ".join(
            f'<a href="{pg}">{pg}</a>' if pg != "*" else "<em>site-wide</em>"
            for pg in it["pages"])
        rows += f"""<tr id="{it['id']}">
  <td><strong>{it['id']}</strong><br><span style="color:{sevcls[it['sev']]};font-weight:700;font-size:.78rem">{it['sev']}</span><br>
      <span style="font-size:.78rem;color:#6E6E6E">{att(it['area'])}</span></td>
  <td><strong>{att(it['title'])}</strong>
      <p style="margin:.5rem 0 0;font-size:.88rem;color:#555">{att(it['detail'])}</p></td>
  <td style="font-size:.86rem"><strong>Now:</strong> {att(it['current'])}<hr style="border:0;border-top:1px solid #E6EAF1;margin:.6rem 0">
      <strong>To resolve:</strong> {att(it['fix'])}</td>
  <td style="font-size:.8rem">{pages}<br><br><code style="font-size:.74rem;color:#6E6E6E">{e(it['src'])}</code></td>
</tr>"""

    body = section(
        h(1, "Editorial review checklist")
        + p("Every item that must be resolved before ai.ri.gov goes live, carried over from Appendix B of the "
            "Website Content Outline &amp; Draft Copy v3.0 and mapped to the exact page and generator function that "
            "produces the copy.", "lede")
        + f"""<div class="metrics">
          <div class="metric"><b style="color:#B3261E">{c['BLOCKER']}</b><span>Blockers</span><em>Cannot launch until resolved</em></div>
          <div class="metric"><b style="color:#8A6D0B">{c['VERIFY']}</b><span>Facts to verify</span><em>Carried from outline v2.0, unconfirmed in the source documents</em></div>
          <div class="metric"><b>{c['DECISION']}</b><span>Decisions</span><em>Leadership or build calls still open</em></div>
        </div>"""
        + '<div class="callout"><p><strong>How to use this with Claude.</strong> The whole site is generated from a small '
          'set of Python files, so a fix is a one-line change in one place rather than an edit across twenty-five HTML '
          'files. Quote an item ID (for example <code>B1-05</code>) and say what the answer is; the <em>Source</em> column '
          'names the file and function to change, and the site rebuilds with <code>python3 build.py</code>.</p></div>'
        + f'<table class="data"><thead><tr><th style="width:11%">Item</th><th style="width:31%">Issue</th>'
          f'<th style="width:34%">Current state &amp; resolution</th><th style="width:24%">Pages &amp; source</th></tr></thead>'
          f'<tbody>{rows}</tbody></table>')
    return shell.page("_review.html", "Editorial review checklist", body,
                      active="", trail=None, newsletter=False,
                      desc="Open items to resolve before the AI RI Hub website launches.")

def main():
    os.makedirs(OUT, exist_ok=True)
    pages = {}
    pages["index.html"] = pg_home.build()
    pages.update(pg_about.build())
    pages.update(pg_programs.build())
    pages.update(pg_rest.build())
    pages["_review.html"] = review_page()

    for name, content in pages.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(content)

    # assets
    # assets are edited in place under assets/ and are not regenerated

    # machine-readable register
    with open(os.path.join(OUT, "open-items.json"), "w", encoding="utf-8") as f:
        json.dump(register.ITEMS, f, indent=2)

    print(f"Built {len(pages)} pages -> {OUT}")
    return pages

if __name__ == "__main__":
    main()
