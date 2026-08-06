# -*- coding: utf-8 -*-
from lib import *
from shell import page

def build():
    slides = [
        ("Welcome", "Rhode Island. AI Ready.",
         "The AI RI Hub connects Rhode Islanders to the training, the computing power, and the honest guidance they need to use artificial intelligence well.",
         "Explore our programs", "programs.html"),
        ("Opportunity", "Free AI training, from Google",
         "Through our partnership with Google, Rhode Islanders can earn Google AI and career certificates at no cost.",
         "See if you qualify", "education-training-grow-with-google.html"),
        ("Compute", "Serious computing power, right here in New England",
         "Rhode Island holds a share of the AI Computing Resource &mdash; a near-zero-carbon supercomputer open to our universities, agencies, nonprofits, and startups.",
         "Learn about AI compute", "programs-ai-compute-resources.html"),
        ("Workforce", "Train your team",
         "Cohort training and micro-credentials for state, municipal, and nonprofit staff &mdash; built with employers, recognized statewide.",
         "Get your team trained", "programs-workforce-credentialing.html"),
    ]
    sl = ""
    for i, (eyebrow, head, sub, cta, href) in enumerate(slides):
        # only the first slide carries the page h1; the rest are h2 so the page has a single h1
        tag = "h1" if i == 0 else "h2"
        sl += (f'<div class="slide{" on" if i==0 else ""}" role="group" aria-roledescription="slide" '
               f'aria-label="Slide {i+1} of 4"><span class="eyebrow">{e(eyebrow)}</span>'
               f'<{tag}>{e(head)}</{tag}>'
               f'<p>{sub}</p><a class="btn" href="{href}">{e(cta)}</a></div>')
    dots = "".join(f'<button class="dot" role="tab" aria-selected="{"true" if i==0 else "false"}" '
                   f'aria-label="Show slide {i+1}"></button>' for i in range(4))

    # The placeholder note sits in its own strip below the hero rather than
    # overlaid on it, so it cannot collide with the carousel controls on narrow screens.
    hero = f"""<div class="hero">
  <div class="hero__media">
    <figure class="ph ph--hero" role="img" aria-label="Placeholder for the homepage hero photograph."></figure>
  </div>
  <div class="hero__inner"><div class="wrap">
    {sl}
    <div class="hero__ctrls" role="tablist" aria-label="Hero slides">{dots}
      <button class="pausebtn" id="heroPause" type="button">Pause</button></div>
  </div></div>
</div>
<div class="phnote-bar"><div class="wrap"><strong>PLACEHOLDER &mdash; HERO PHOTOGRAPH.</strong>
  One wide, unposed photograph of Rhode Islanders at work or learning &mdash; a classroom of adult learners,
  a manufacturing floor, or a municipal office &mdash; reused across all four slides with a colour overlay.
  No stock AI imagery. Alt text should describe the people and setting, not the concept.</div></div>"""

    mission = section(
        h(2, "Rhode Island&rsquo;s hub for artificial intelligence")
        + p("<strong>The AI RI Hub helps Rhode Island understand AI, protect against its harms, and use it well.</strong>", "lede")
        + p("We are the state&rsquo;s neutral coordinating body for artificial intelligence, created to carry out the "
            "recommendations of Governor McKee&rsquo;s AI Task Force. We bring together the four things Rhode Island needs: "
            "access to serious computing power, statewide workforce training and credentials, clear-eyed guidance on "
            "responsible use, and a trustworthy signal to employers about what AI skills actually mean.")
        + p("Rhode Island is the smallest state, and that is an advantage. Every college, agency, and major employer is "
            "within forty-five minutes of the others. We can coordinate in months what larger states take years to "
            "attempt &mdash; and what works here can work anywhere."),
        narrow=True)

    statband = section(
        '<p class="eyebrow-h">Why this matters</p>'
        + stats([
            ("1 in 5", "Rhode Island jobs heavily exposed to AI. About 95,000 of the state&rsquo;s 513,700 nonfarm jobs are in occupations where half or more of the tasks could be affected."),
            ("56%", "The average wage premium commanded by workers with AI skills."),
            ("51.1%", "The share of Rhode Island&rsquo;s private workforce employed by small businesses &mdash; and the businesses least likely to have a training budget."),
            ("45 min", "The distance between any two institutions in Rhode Island. Coordination is our competitive advantage."),
        ])
        + p('<a href="#sources">Sources and methodology</a>', "hint"),
        cls="alt")

    ctaband = f"""<div class="ctaband"><div class="wrap">
      <h2>Want to work with us?</h2>
      <p>Whether you are an employer with a hiring need, an agency planning a pilot, an educator building a course, or a
      resident who wants to learn &mdash; tell us what you are trying to do and we will point you to the right resource
      or the right partner.</p>
      <div class="btn-row"><a class="btn" href="about-contact.html">Engage with us</a></div>
    </div></div>"""

    whatsnew = section(
        '<p class="eyebrow-h">What&rsquo;s new</p>' + h(2, "Current opportunities")
        + cards([
            dict(tag="Opportunity", tagcls="tag--gold", title="Free Google AI training for Rhode Islanders",
                 body="Earn a Google AI or career certificate at no cost. Limited licences available &mdash; apply now.",
                 href="education-training-grow-with-google.html", more="Apply"),
            dict(tag="Opportunity", tagcls="tag--gold", title="Apply for AI computing time",
                 body="Rhode Island institutions, agencies, nonprofits, and startups can request an allocation on the regional AI supercomputer.",
                 href="programs-ai-compute-resources.html", more="Request access"),
            dict(tag="Opportunity", tagcls="tag--gold", title="Small Business AI Adoption Workshop Series",
                 body="A hands-on, three-workshop pilot for Rhode Island small businesses. Register your interest for the next cohort.",
                 href="programs-small-business-nonprofit.html", more="Register interest"),
        ]))

    feeds = section(
        '<div class="cards cards--2" style="align-items:start">'
        + '<div>' + h(2, "Latest news")
        + feed([
            ("12 Jul 2026", "Rhode Island secures access to regional AI supercomputing",
             "The Hub&rsquo;s AICR partnership gives Rhode Island institutions frontier-scale GPU computing.", "news-events-news.html"),
            ("28 Jun 2026", "Statewide Advisory Board holds inaugural meeting",
             "Provosts, employers, and agency leaders set the Hub&rsquo;s first-year credentialing priorities.", "news-events-news.html"),
            ("14 Jun 2026", "Rhode Island AI Action Plan: what it says and what happens next",
             "A plain-language guide to the Governor&rsquo;s Task Force recommendations.", "news-events-news.html"),
        ])
        + p('<a href="news-events-news.html"><strong>More news &rarr;</strong></a>')
        + '</div><div>' + h(2, "Upcoming events")
        + feed([
            ("Oct 2026", "Higher Education AI Convening",
             "Faculty and administrators share curriculum practice and connect to compute resources.", "news-events-events.html"),
            ("Nov 2026", "Small Business AI Adoption Workshop &mdash; Session 1",
             "The first of three hands-on workshops for Rhode Island small businesses.", "news-events-events.html"),
            ("Apr 2027", "K-12 Educator AI Convening",
             "Classroom teachers and district leaders build a statewide community of practice.", "news-events-events.html"),
        ])
        + p('<a href="news-events-events.html"><strong>All events &rarr;</strong></a>')
        + '</div></div>', cls="alt")

    highlights = section(
        h(2, "Highlights")
        + cards([
            dict(title="Rhode Island AI Action Plan",
                 thumb=ph("Thumbnail", "Document cover or typographic card generated from the eCMS theme. No stock photography.", cls="ph--thumb"),
                 body="The Governor&rsquo;s AI Task Force report that created the Hub.", href="#", more="Read the plan"),
            dict(title="Rhode Island&ndash;AICR partnership white paper",
                 thumb=ph("Thumbnail", "Document cover or typographic card generated from the eCMS theme.", cls="ph--thumb"),
                 body="How Rhode Island secured a share of regional AI supercomputing.", href="#", more="Read the paper"),
            dict(title="Excellence in Cybersecurity Award",
                 thumb=ph("Thumbnail", "Document cover or typographic card generated from the eCMS theme.", cls="ph--thumb"),
                 body="The Institute for Cybersecurity and Emerging Technologies recognised at the Rhode Island Digital Government Summit.", href="#", more="Read more"),
        ]))

    sources = section(
        h(2, "Sources") +
        p("Job-exposure figures: U.S. Bureau of Labor Statistics and Rhode Island Department of Labor and Training "
          "current employment statistics (513,700 nonfarm jobs, February 2026, seasonally adjusted); exposure "
          "estimates after Eloundou et al. (2024), Felten et al. (2021), and Pew Research Center (2023). "
          "Small-business employment share: U.S. Small Business Administration Office of Advocacy, "
          "2025 Small Business Profile: Rhode Island.", "hint"),
        cls="tight", id="sources", narrow=True)

    body = hero + mission + statband + ctaband + whatsnew + feeds + highlights + sources
    return page("index.html", "Home", body, active="index.html", trail=None,
                desc="Rhode Island's statewide hub for responsible, applied artificial intelligence.")
