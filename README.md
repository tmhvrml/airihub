# ai.ri.gov — website prototype

Built from **AI_RI_Hub_Website_Outline_v3.0.docx**. Every page in the outline is here,
with the draft copy in place and labelled placeholders standing in for images.

## Viewing it

Open **`index.html`** in a browser. Everything is local — no server, no internet needed.

Working: navigation, dropdowns, breadcrumbs, hero carousel, dark mode, text-size control,
accordions, mobile menu. Forms render but are not connected to anything.

## The review checklist

**`_review.html`** lists all 26 open items from Appendix B — 7 blockers, 12 facts to verify,
7 decisions — each mapped to the pages it affects and the source file that produces the copy.
There is a link to it in the yellow bar at the top of every page.
`open-items.json` is the same data, machine-readable.

## Making changes

The site is generated, so a fix is one edit in one place instead of the same edit across
25 HTML files.

```
cd _source
python3 build.py          # rebuilds everything into ../
```

| File | Holds |
|---|---|
| `lib.py` | Navigation, and the component functions (cards, forms, tables, placeholders) |
| `shell.py` | Header, ribbon, breadcrumbs, newsletter block, footer |
| `pg_home.py` | Home |
| `pg_about.py` | About, Overview, Team, Partners, FAQs, Contact |
| `pg_programs.py` | The six programme pages |
| `pg_rest.py` | Education/Training, Jobs, News/Events |
| `register.py` | The open-items register behind `_review.html` |
| `assets/style.css` | Design system — eCMS palette anchors, dark mode, responsive rules |

To resolve an item, quote its ID (e.g. `B1-05`) and say what the answer is. The register's
`src` field names the file and function to change.

## What this prototype is not

Static HTML modelled on eCMS conventions — not built in eCMS itself. The palette, type scale,
and component set follow the outline's conformance notes so the design translates, but the real
build happens in the State's CMS. Confirm theme, component availability, and publishing
workflow with ETSS first (item `B3-05`).
# airihub
