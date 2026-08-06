# -*- coding: utf-8 -*-
from lib import *
from shell import page

E = ("Education/Training", "education-training.html")
N = ("News/Events", "news-events.html")

def hdr(title, lede):
    return section(h(1, title) + p(lede, "lede"), cls="tight", narrow=True)

def build():
    out = {}

    # ================= EDUCATION =================
    body = hdr("Learn AI",
               "Whatever you are starting from, there is something here for you. Some of it is free, some is subsidised, "
               "and all of it has been reviewed by the Hub before we put it on this page.") + section(
        h(2, "Where do I start?")
        + cards([
            dict(tag="Residents", title="I want to learn AI myself",
                 body="Free Google AI and career certificates, plus vetted no-cost courses from other providers.",
                 href="education-training-grow-with-google.html", more="Start here"),
            dict(tag="Employers &amp; agencies", title="I need to train my team",
                 body="Cohort training and micro-credentials for state, municipal, and nonprofit staff.",
                 href="programs-workforce-credentialing.html", more="See cohort training"),
            dict(tag="Educators", title="I teach, and I need to catch up",
                 body="Classroom resources, professional development, and the April K-12 convening.",
                 href="education-training-future-ready.html", more="For educators"),
        ])) + section(
        h(2, "All training pages")
        + linklist([
            ("Grow with Google &mdash; Rhode Island", "Free Google AI and career certificates for selected Rhode Islanders.", "education-training-grow-with-google.html"),
            ("Additional AI Training Resources", "Free courses from Microsoft, Anthropic, and others.", "education-training-additional-resources.html"),
            ("Cybersecurity &amp; AI Practicum", "Hands-on security training on the state&rsquo;s cyber range.", "education-training-cyber-ai-practicum.html"),
            ("Future Ready (K-12) &amp; Summer Career Academy", "For students, teachers, and district leaders.", "education-training-future-ready.html"),
        ]), cls="alt")
    out["education-training.html"] = page("education-training.html", "Education / Training", body, trail=[E],
        desc="AI learning available to Rhode Islanders, at no cost or low cost.")

    # ---------- Grow with Google ----------
    body = hdr("Free Google AI training for Rhode Islanders",
               "The AI RI Hub and Google are offering Rhode Islanders no-cost access to Google&rsquo;s AI and career "
               "certificate programmes.") + section(
        p("You learn online, at your own pace, and you finish with a credential employers recognise.")
        + callout(p("<strong>Licences are limited and are awarded by the Hub.</strong> Apply below and we will let you "
                    "know whether you have a seat. Licences run through 31 December 2027."))
        + h(2, "How it works")
        + ol([
            "<strong>Apply.</strong> Fill out a short form telling us who you are and which programme you want.",
            "<strong>Get your licence.</strong> If you qualify, we send you an access code.",
            "<strong>Learn at your own pace.</strong> Everything is online, and you set the schedule.",
            "<strong>Earn your certificate.</strong> Finish the programme and receive your Google credential.",
            "<strong>Tell us how it went.</strong> With your permission, your story may be featured to encourage others.",
        ]), narrow=True) + section(
        h(2, "Programmes available")
        + cards([
            dict(title="Google AI Professional Certificate", body="A full professional certificate in applied AI.", href="#", more="Course details at Google"),
            dict(title="Google AI Essentials", body="Foundational AI skills for any role.", href="#", more="Course details at Google"),
            dict(title="Accelerate Your Job Search with AI", body="Using AI tools in a job search.", href="#", more="Course details at Google"),
            dict(title="Google Agile Essentials", body="Agile project management fundamentals.", href="#", more="Course details at Google"),
            dict(title="Google Career Certificates", body="Including Data Analytics, IT Support, and Project Management.", href="#", more="Course details at Google"),
        ], cols=3)
        + p("<em>Course structures are maintained by Google and change periodically. We link to Google&rsquo;s own course "
            "pages rather than reproducing curricula that would drift out of date.</em>", "hint"), cls="alt") + section(
        h(2, "Who is eligible")
        + callout(p("<strong>Eligibility criteria are being finalised and will be published here before applications "
                    "open.</strong> This page will state how many licences are available, who gets priority, what the "
                    "deadline is, and what happens if demand exceeds supply."))
        + form("Apply for a licence", [
            field("First name", req=True, name="g-fn"), field("Last name", req=True, name="g-ln"),
            field("Email", kind="email", req=True, name="g-email"),
            field("Rhode Island ZIP code", req=True, name="g-zip"),
            field("Which programme?", options=["Google AI Professional Certificate", "Google AI Essentials",
                                               "Accelerate Your Job Search with AI", "Google Agile Essentials",
                                               "Google Career Certificate — Data Analytics",
                                               "Google Career Certificate — IT Support",
                                               "Google Career Certificate — Project Management"], name="g-prog"),
            field("Current employment status", options=["Employed", "Seeking work", "Student",
                                                        "Not currently in the workforce"], name="g-emp"),
        ], "Apply", note="This is a prototype. The form is not connected."), narrow=True)
    out["education-training-grow-with-google.html"] = page("education-training-grow-with-google.html",
        "Grow with Google — Rhode Island", body, active="education-training.html",
        trail=[E, ("Grow with Google", "education-training-grow-with-google.html")],
        desc="Free Google AI and career certificate training for Rhode Islanders.")

    # ---------- Additional resources ----------
    body = hdr("More free ways to learn",
               "Beyond the Google programmes, several providers offer high-quality AI training at no cost.") + section(
        p("The Hub does not run these and does not endorse the companies behind them &mdash; we list them because they "
          "are free, they are good, and Rhode Islanders should know they exist.")
        + h(2, "Microsoft AI Skills Navigator")
        + p("An AI-powered tool that builds a personalised learning pathway across Microsoft Learn, LinkedIn Learning, "
            "and third-party content, and helps managers plan skilling for a whole team. Tracks are tailored for "
            "everyone, for educators, for nonprofits, and for the public sector.")
        + h(2, "Anthropic Academy &mdash; AI Fluency")
        + p("A free course on collaborating with AI effectively, efficiently, ethically, and safely, organised around "
            "four practices: delegation, description, discernment, and diligence. Two ten-lesson modules cover the "
            "foundations of generative AI and then practical skills &mdash; project planning, prompting, evaluating "
            "outputs, and iterating.")
        + callout(p("This page is reviewed quarterly. If you find a broken link or an out-of-date description, "
                    '<a href="about-contact.html">tell us</a>.')), narrow=True)
    out["education-training-additional-resources.html"] = page("education-training-additional-resources.html",
        "Additional AI Training Resources", body, active="education-training.html",
        trail=[E, ("Additional AI Training Resources", "education-training-additional-resources.html")],
        desc="Free AI training resources from Microsoft, Anthropic, and other providers.")

    # ---------- Cyber practicum ----------
    body = hdr("Hands-on security skills, built in Rhode Island",
               "Security is where AI adoption most often goes wrong, and it is where Rhode Island already has real capability.") + section(
        p("The Institute for Cybersecurity and Emerging Technologies runs hands-on training that uses the state&rsquo;s "
          "cyber-range facilities &mdash; you practise on live exercises, not slides.")
        + ul([
            "CompTIA Security+ certification preparation, paired with a cyber range practicum.",
            "Hands-on exercises through the Institute&rsquo;s cyber range facilities at Rhode Island College.",
            "Alignment with AP Cybersecurity coursework, mapping course skills to hands-on labs for high school programmes.",
        ])
        + btns([("See upcoming sessions", "news-events-events.html", "btn")]), narrow=True)
    out["education-training-cyber-ai-practicum.html"] = page("education-training-cyber-ai-practicum.html",
        "Cybersecurity & AI Practicum", body, active="education-training.html",
        trail=[E, ("Cybersecurity &amp; AI Practicum", "education-training-cyber-ai-practicum.html")],
        desc="Hands-on cybersecurity and AI training on Rhode Island's cyber range.")

    # ---------- Future Ready ----------
    body = hdr("For students and the teachers who prepare them",
               "Rhode Island&rsquo;s schools are being asked to prepare students for an AI-enabled workforce while "
               "managing teacher workload and protecting student privacy.") + section(
        p("The Hub works with the Rhode Island Department of Education and with districts on all three at once.")
        + btns([("For students", "#students", "btn"), ("For educators", "#educators", "btn btn--navy"),
                ("For district leaders", "#districts", "btn btn--navy")]), narrow=True) + section(
        '<div id="educators"></div>' + h(2, "For educators")
        + p("Classroom resources and professional development for K-12 AI literacy, a statewide community of practice, "
            "and the K-12 Educator AI Convening each April. We are also working with RIDE on a statewide AI literacy "
            "certification that can be integrated into K-12 pathways.")
        + '<div id="students"></div>' + h(2, "For students")
        + p("<strong>The Summer Career Academy in AI</strong> &mdash; a high school summer programme on applied AI, "
            "hands-on projects, and the careers this technology is opening up. The Hub also extends AI career awareness "
            "and foundational skills programming to high school students, with particular emphasis on career and "
            "technical education pathways and on communities underrepresented in technology.")
        + '<div id="districts"></div>' + h(2, "For district leaders")
        + p('Vetted classroom AI platforms in the <a href="programs-solution-registry.html">AI Solution Registry</a>, '
            "evaluated against Rhode Island&rsquo;s standards for student data privacy and instructional effectiveness, "
            "with criteria developed alongside RIDE."), cls="alt", narrow=True) + section(
        ph("Photograph", "One classroom or lab photograph, added once the Summer Career Academy has run and signed "
           "student photo releases are on file. Student photography requires district permission and parental consent "
           "&mdash; do not use district photos without them.",
           alt="High school students working on an applied AI project at the Summer Career Academy.",
           priority="After photo releases"))
    out["education-training-future-ready.html"] = page("education-training-future-ready.html",
        "Future Ready (K-12) & Summer Career Academy in AI", body, active="education-training.html",
        trail=[E, ("Future Ready (K-12)", "education-training-future-ready.html")],
        desc="K-12 AI literacy resources, educator support, and the Summer Career Academy in AI.")

    # ================= JOBS =================
    body = hdr("AI and technology jobs in Rhode Island",
               "Training is worth something when it leads to work.") + section(
        p("This board lists AI and technology roles with Rhode Island employers &mdash; full-time positions, "
          "apprenticeships, internships, and project placements.")
        + p("If you have completed a Hub credential, say so in your application. Our employer partners helped define "
            "what those credentials mean, and they know what they are looking at.")
        + btns([("Browse jobs", "#listings", "btn"), ("Post a role", "#post", "btn btn--navy")]), narrow=True) + section(
        '<div id="listings"></div>' + h(2, "Current openings")
        + job("Example listing &mdash; AI Implementation Analyst", "Rhode Island state agency &middot; Providence",
              "Placeholder listing showing the layout. Real listings carry a posting date, a closing date, and a link to "
              "the employer&rsquo;s application system.",
              ["Full time", "Public sector", "Tier 2 credential relevant", "Posted 00 Mon 2026"])
        + job("Example listing &mdash; Machine Learning Apprentice", "Rhode Island manufacturer &middot; Warwick",
              "Placeholder listing. Apprenticeship and internship postings are tagged separately so students can filter for them.",
              ["Apprenticeship", "Manufacturing", "Entry level", "Posted 00 Mon 2026"])
        + callout(p("<strong>The board is not live yet.</strong> The two entries above show the listing layout. "
                    'Once a feed source is confirmed, real openings will appear here. <a href="about-contact.html">'
                    "Tell us if you would use this</a> &mdash; that helps us prioritise it.")), cls="alt", narrow=True) + section(
        '<div id="post"></div>' + h(2, "For employers")
        + p("Post a role at no cost. We are especially interested in hearing what AI skills you are hiring for, whether "
            "or not you have an opening today &mdash; that signal is what keeps our credentials aligned with real demand "
            "rather than with what is convenient to teach.")
        + form("Post a role", [
            field("Organisation", req=True, name="j-org"), field("Contact email", kind="email", req=True, name="j-email"),
            field("Role title", req=True, name="j-title"),
            field("Type", options=["Full time", "Part time", "Apprenticeship", "Internship", "Project placement"], name="j-type"),
            field("Location", name="j-loc"),
            field("Description", kind="textarea", req=True, name="j-desc"),
            field("Which AI skills matter most for this role?", kind="textarea", name="j-skills"),
        ], "Submit posting", note="This is a prototype. The form is not connected."), narrow=True)
    out["jobs.html"] = page("jobs.html", "Jobs Board", body, trail=[("Jobs Board", "jobs.html")],
        desc="AI and technology jobs with Rhode Island employers.")

    # ================= NEWS / EVENTS =================
    body = hdr("News &amp; Events",
               "Announcements, convenings, and what the Hub is actually delivering.") + section(
        linklist([
            ("News", "Announcements, launches, partnerships, and milestones.", "news-events-news.html"),
            ("Events", "Convenings, workshops, information sessions, and partner events.", "news-events-events.html"),
            ("Rhode Island AI Summit", "The statewide gathering where the state&rsquo;s AI strategy is set in public.", "news-events-ai-summit.html"),
            ("Activity &amp; Impact", "What the Hub is delivering, updated quarterly.", "news-events-activity.html"),
        ]))
    out["news-events.html"] = page("news-events.html", "News / Events", body, trail=[N],
        desc="News, events, and impact reporting from the AI RI Hub.")

    # ---------- News ----------
    news_items = [
        ("12 Jul 2026", "Rhode Island secures access to regional AI supercomputing",
         "Through the AICR partnership at the Massachusetts Green High Performance Computing Center, Rhode Island institutions, agencies, nonprofits, and businesses gain access to frontier-scale GPU computing.", "Compute"),
        ("28 Jun 2026", "Statewide Advisory Board holds inaugural meeting",
         "Provosts, employers, workforce professionals, and agency leaders met to set the Hub&rsquo;s first-year credentialing priorities.", "Workforce"),
        ("14 Jun 2026", "Rhode Island AI Action Plan: what it says and what happens next",
         "A plain-language guide to the Governor&rsquo;s AI Task Force recommendations and the Hub&rsquo;s role in delivering them.", "Policy"),
        ("02 Jun 2026", "Institute for Cybersecurity and Emerging Technologies honoured at the Rhode Island Digital Government Summit",
         "Recognition for the Institute&rsquo;s work in cybersecurity workforce development.", "Partnerships"),
        ("20 May 2026", "AI RI Hub and Google partner to bring free AI training to Rhode Islanders",
         "Selected Rhode Islanders will be able to earn Google AI and career certificates at no cost.", "Training"),
    ]
    items = ""
    for date, title, body_, tag in news_items:
        items += (f'<li><div class="date">{e(date)}</div><div>'
                  f'<h3><a href="#">{title}</a></h3><p>{body_}</p>'
                  f'<p style="margin-top:6px"><span class="chip">{e(tag)}</span></p></div></li>')
    body = hdr("News", "Announcements, launches, partnerships, and milestones from the AI RI Hub and its partners.") + section(
        h(2, "Latest")
        + p("<em>Filter by:</em> "
          + " ".join(f'<span class="chip">{t}</span>' for t in
                     ["All", "Compute", "Workforce", "Small business", "K-12", "Partnerships", "Policy"]), "hint")
        + f'<ul class="feed">{items}</ul>'
        + callout(p("<strong>Article thumbnails.</strong> Each article carries one thumbnail at a consistent aspect "
                    "ratio. Where no photograph exists, use a typographic card generated from the eCMS theme. Do not "
                    "source unrelated stock photography to fill thumbnail slots.")), narrow=True)
    out["news-events-news.html"] = page("news-events-news.html", "News", body, active="news-events.html",
        trail=[N, ("News", "news-events-news.html")], desc="News from the AI RI Hub.")

    # ---------- Events ----------
    body = hdr("Events", "Convenings, workshops, information sessions, and partner events.") + section(
        h(2, "Upcoming")
        + p("Each listing carries the date, location, who it is for, and how to register.")
        + feed([
            ("Oct 2026", "Higher Education AI Convening",
             "Faculty and administrators share curriculum practice, get professional development on emerging tools, and connect to compute resources. Annual.", "#"),
            ("Nov 2026", "Small Business AI Adoption Workshop &mdash; Session 1 of 3",
             "The first of three hands-on workshops for Rhode Island small businesses.", "#"),
            ("Dec 2026", "Cohort training information session",
             "For state agency, municipal, and nonprofit staff considering a spring cohort.", "#"),
            ("Feb 2027", "Cybersecurity &amp; AI Practicum &mdash; Security+ preparation",
             "Certification preparation paired with cyber range exercises.", "#"),
            ("Apr 2027", "K-12 Educator AI Convening",
             "Classroom teachers and district leaders build a statewide community of practice around AI-ready education. Annual.", "#"),
        ])
        + h(2, "Past events")
        + p("Materials and recordings from past events are archived here as they become available."), narrow=True)
    out["news-events-events.html"] = page("news-events-events.html", "Events", body, active="news-events.html",
        trail=[N, ("Events", "news-events-events.html")], desc="Events hosted by the AI RI Hub and its partners.")

    # ---------- Summit ----------
    body = hdr("The Rhode Island AI Summit",
               "A statewide gathering of the people building Rhode Island&rsquo;s AI capacity &mdash; educators, "
               "employers, agency leaders, nonprofit directors, and the workers whose jobs are changing.") + section(
        h(2, "What the Summit is")
        + p("The Summit is where the state&rsquo;s AI strategy gets set in public: hands-on workshops and presentations, "
          "partners reporting what is working and what is not, and the annual release of Rhode Island&rsquo;s AI "
          "Strategic Action Plan update and the State of AI in Rhode Island report.")
        + callout(p("<strong>Dates and venue for the inaugural Summit are being confirmed.</strong> "
                    "Sign up below and we will tell you as soon as registration opens."))
        + btns([("Get notified", "#notify", "btn")]), narrow=True) + section(
        ph("Photography", "Once the first Summit has taken place: one wide shot of the room and two or three session "
           "photographs. Before then this page carries no image &mdash; it is an announcement, not a mock-up of an event "
           "that has not occurred.",
           alt="Attendees at the inaugural Rhode Island AI Summit.", priority="After first Summit"), cls="alt") + section(
        '<div id="notify"></div>' + form("Get Summit updates", [
            field("Name", req=True, name="su-name"), field("Organisation", name="su-org"),
            field("Email", kind="email", req=True, name="su-email"),
        ], "Notify me", note="This is a prototype. The form is not connected."), narrow=True)
    out["news-events-ai-summit.html"] = page("news-events-ai-summit.html", "Rhode Island AI Summit", body,
        active="news-events.html", trail=[N, ("Rhode Island AI Summit", "news-events-ai-summit.html")],
        desc="The Rhode Island AI Summit, the state's annual AI convening.")

    # ---------- Activity ----------
    body = hdr("What the Hub is delivering",
               "We publish what we measure. This page tracks the Hub&rsquo;s activity and the state&rsquo;s progress "
               "against the Rhode Island AI Action Plan, updated quarterly.") + section(
        p("<strong>Last updated:</strong> reporting begins with the first full quarter after launch.", "hint")
        + metrics([
            ("—", "People trained", "By category: educators, public-sector workers, small-business owners, residents"),
            ("—", "Credentials awarded", "Under the statewide credentialing seal"),
            ("—", "Compute hours used", "Against the annual allocation"),
            ("—", "Organisations assisted or referred", "Including referrals fulfilled and unmet"),
            ("—", "Convenings held", "With attendance"),
            ("—", "Action Plan recommendations on track", "Progress against each recommendation"),
        ])
        + callout(p("Where a number is disappointing, it stays on the page. A dashboard that only shows good news is "
                    "not a dashboard.")), narrow=True) + section(
        ph("Charts", "eCMS data visualisation components, so charts inherit theme colours and stay accessible in both "
           "light and dark modes. Every chart needs a text alternative &mdash; a data table or a written summary &mdash; "
           "not just alt text. No photographs on this page.", cls="ph--chart"), cls="alt") + section(
        h(2, "How this is measured")
        + p("Data flows from partner reporting on a quarterly cadence. The Hub compiles and quality-checks it, and the "
            "master dataset is maintained with our evaluation partners. Only aggregate, programme-level counts are "
            "published &mdash; no personal data. Individual-level information stays with delivery partners under their "
            "own policies.")
        + h(2, "Action Plan progress")
        + table(["Recommendation", "Owner", "Status", "Last reviewed"], [
            ["<em>Tracking begins with the first full reporting quarter.</em>", "&mdash;", "&mdash;", "&mdash;"],
        ]), narrow=True)
    out["news-events-activity.html"] = page("news-events-activity.html", "Activity & Impact", body,
        active="news-events.html", trail=[N, ("Activity &amp; Impact", "news-events-activity.html")],
        desc="Public dashboard of AI RI Hub activity and progress against the Rhode Island AI Action Plan.")
    return out
