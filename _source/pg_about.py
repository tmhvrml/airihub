# -*- coding: utf-8 -*-
from lib import *
from shell import page

A = ("About", "about.html")

def hdr(title, lede):
    return section(h(1, e(title)) + p(lede, "lede"), cls="tight", narrow=True)

def build():
    out = {}

    # ---------- About landing ----------
    body = hdr("About the AI RI Hub",
               "What the Hub is, who leads it, who its partners are, and how to reach us.") + section(
        linklist([
            ("About the AI RI Hub", "Why the Hub exists, what it does, and how it works.", "about-overview.html"),
            ("Leadership &amp; Team", "The people running the Hub and the board that guides it.", "about-team.html"),
            ("Partners", "Who does what across Rhode Island&rsquo;s institutions, agencies, and industry.", "about-partners.html"),
            ("FAQs", "Short answers to the questions we are asked most.", "about-faqs.html"),
            ("Contact", "Tell us what you are trying to do.", "about-contact.html"),
        ]))
    out["about.html"] = page("about.html", "About", body, trail=[A],
                             desc="About the AI RI Hub, Rhode Island's statewide AI coordination hub.")

    # ---------- Overview ----------
    body = hdr("About the AI RI Hub",
               "Rhode Island&rsquo;s statewide coordinating body for artificial intelligence.") + section(
        h(2, "What the Hub is")
        + p("In 2024, Governor Dan McKee appointed the Rhode Island AI Task Force. Six sector teams &mdash; defense and "
            "manufacturing, government, finance, education, healthcare, and small business, startups and nonprofits &mdash; "
            "worked through surveys, research, national best practices, and public input, and produced the Rhode Island "
            "AI Action Plan in January 2026. The Plan set four priorities for the state: education and workforce "
            "upskilling, government leadership, framework development, and collaboration and scale. It named an "
            "AI-ready workforce as the single highest priority, and it named the AI RI Hub as the statewide resource "
            "responsible for delivering it.")
        + p("The Hub is that resource. It is funded by the State and it is deliberately neutral: it operates as the AI "
            "arm of the Office of the Postsecondary Commissioner, which allows it to convene competing and complementary "
            "institutions on common ground, and it is physically housed at the Institute for Cybersecurity and Emerging "
            "Technologies at Rhode Island College. The University of Rhode Island leads the technical side, through its "
            "Institute for AI and Computational Research.")
        + p("Our job is not to compete with the colleges, agencies, and companies already doing this work. It is to "
            "connect them, to fill the gaps none of them can fill alone, and to make sure the benefits of AI reach the "
            "Rhode Islanders most likely to be left out."),
        narrow=True) + section(
        h(2, "What we do &mdash; our four pillars")
        + pillars([
            ("1", "Workforce development and credentialing",
             "Training and credentials that make AI skills legible. Micro-credentials aligned to what employers actually "
             "need, cohort training for public and nonprofit staff, and a statewide credentialing seal."),
            ("2", "AI compute access",
             "Rhode Island&rsquo;s share of the AI Computing Resource at the Massachusetts Green High Performance Computing "
             "Center, available at a fraction of commercial cloud pricing."),
            ("3", "Community engagement and access",
             "Making sure Rhode Islanders know what is available, and designing access so smaller campuses and community "
             "organisations get the same quality of support as the largest research universities."),
            ("4", "AI expertise and solution vetting",
             "Evaluating AI products and publishing what we find, so a school district or a manufacturer does not have to "
             "navigate a crowded marketplace alone."),
        ])
        + p("<em>The four-pillar graphic above uses eCMS icon cards rather than commissioned illustration &mdash; faster to "
            "build, easier to translate, and accessible by default.</em>", "hint"),
        cls="alt") + section(
        h(2, "How we work")
        + h(3, "We coordinate; our partners deliver")
        + p("The Hub convenes, maps the state&rsquo;s needs and assets, routes requests to the right provider, aligns "
            "training and credentials, and measures what happens. The teaching, advising, and technical assistance are "
            "delivered by the institutions and organisations that already do it well.")
        + h(3, "We start from what exists")
        + p("Rhode Island already has strong institutions, real compute infrastructure, and experienced workforce "
            "partners. The Hub&rsquo;s value is in making them function as one system, not in building a parallel one.")
        + h(3, "We measure, and we publish what we measure")
        + p('Progress against the Action Plan is tracked on a <a href="news-events-activity.html">public dashboard</a> '
            "on this site."),
        narrow=True)
    out["about-overview.html"] = page("about-overview.html", "About the AI RI Hub", body,
        active="about.html", trail=[A, ("About the AI RI Hub", "about-overview.html")],
        desc="What the AI RI Hub is, why it exists, and how it works.")

    # ---------- Team ----------
    body = hdr("Leadership &amp; Team",
               "The Hub is led by a small team and guided by a Statewide Advisory Board drawn from higher education, "
               "industry, government, and community organisations.") + section(
        h(2, "Leadership")
        + people([
            person("TH", "Dr. Timothy M. Henry, Ph.D., PMP", "Interim Director",
                   "Dr. Henry serves as Interim Director of the AI RI Hub. He is Professor and Chair of Computer Science "
                   "and Information Systems at Rhode Island College, the architect of Rhode Island&rsquo;s first "
                   "undergraduate artificial intelligence degree, and the academic lead on the Governor&rsquo;s AI Task Force.",
                   avatar_desc="Headshot. Consistent crop and background across all four leaders."),
            person("JL", "Congressman James R. Langevin (ret.)", "Distinguished Chair",
                   "Congressman Langevin is Distinguished Chair of the Institute for Cybersecurity and Emerging "
                   "Technologies. He brings national visibility and a deep network across cybersecurity, AI policy, and government.",
                   avatar_desc="Headshot. Consistent crop and background."),
            person("DA", "Douglas Alexander, CISSP", "Director, Institute for Cybersecurity and Emerging Technologies",
                   "Mr. Alexander leads the Institute&rsquo;s cybersecurity programmes and community engagement work, and "
                   "coordinates closely with the Hub on shared workforce and outreach programmes.",
                   avatar_desc="Headshot. Consistent crop and background."),
            person("&mdash;", "AI RI Hub Director", "Search underway",
                   "A permanent Hub Director is being recruited through a national search, with preference for candidates "
                   "experienced in applied AI, higher education leadership, and public-private partnership."),
        ])
        + p("<em>Headshots use a consistent crop and background. Where a headshot is unavailable, initials in a "
            "theme-coloured circle are used rather than a placeholder silhouette.</em>", "hint")) + section(
        h(2, "Programme and technical staff")
        + p("Two programme staff at Rhode Island College lead statewide outreach, workforce training delivery, community "
            "programming, and K-12 partnerships. Two technical staff at the University of Rhode Island lead compute "
            "onboarding, allocation management, and advanced technical support.")
        + h(2, "Statewide Advisory Board")
        + p("The Board brings together provosts, industry executives, workforce development professionals, state agency "
            "leaders, and community representatives. It validates micro-credential competency frameworks, guides compute "
            "allocation priorities, connects the Hub to employer needs, and supports strategic planning and resource development."),
        cls="alt", narrow=True)
    out["about-team.html"] = page("about-team.html", "Leadership & Team", body,
        active="about.html", trail=[A, ("Leadership &amp; Team", "about-team.html")],
        desc="Leadership and staff of the AI RI Hub.")

    # ---------- Partners ----------
    def grp(title, rows):
        return h(2, title) + "".join(p(f"<strong>{n}</strong> &mdash; {d}") for n, d in rows)

    body = hdr("Partners",
               "The Hub works because Rhode Island&rsquo;s institutions were already working together. Below is who does what.") + section(
        grp("Higher education", [
            ("University of Rhode Island", "the state&rsquo;s flagship public research, land-grant and sea-grant university. URI contributes Rhode Island&rsquo;s deepest concentration of AI, high-performance computing, data science, and quantum expertise through its Institute for AI and Computational Research, and leads the technical relationship with the regional compute partnership."),
            ("Rhode Island College", "a central workforce-facing institution producing a large share of the state&rsquo;s educators and public-sector workforce. RIC&rsquo;s Institute for Cybersecurity and Emerging Technologies is the physical home of the AI RI Hub."),
            ("Brown University", "nationally recognised depth in AI, machine learning, and computing education research; a standards, best-practices, and research-translation partner."),
            ("Bryant University", "a business- and workforce-facing perspective connecting higher education to employer needs, professional upskilling, and small-business adoption, including its Applied AI Academy and Center for Applied Artificial Intelligence."),
            ("Community College of Rhode Island", "the state&rsquo;s only community college and its highest-volume workforce and access pipeline, reaching adult learners, first-generation students, and career-changers statewide."),
            ("New England Institute of Technology", "applied, hands-on technical education with strong employer alignment, and a partner for experiential and apprenticeship pathways."),
        ])
        + grp("Compute and infrastructure", [
            ("Massachusetts Green High Performance Computing Center and the AI Computing Resource (AICR)", "Rhode Island&rsquo;s frontier-scale, near-zero-carbon GPU computing, through URI&rsquo;s membership in the MGHPCC consortium."),
        ])
        + grp("State government and policy", [
            ("Office of Governor Dan McKee and the Governor&rsquo;s AI Task Force", "the mandate and the Action Plan the Hub implements."),
            ("Office of the Postsecondary Commissioner", "statewide convening authority across public and independent institutions."),
            ("Rhode Island Commerce and its Science and Technology Advisory Council", "economic-development reach and sector intelligence."),
            ("Department of Labor and Training and the Governor&rsquo;s Workforce Board", "the state&rsquo;s workforce system, American Job Centers, and labour-market data."),
            ("Department of Education and Department of Health", "sector leadership in education and healthcare."),
            ("Enterprise Technology Strategy and Services", "hosts this site."),
        ])
        + grp("Workforce, small business, and community", [
            ("Skills for Rhode Island&rsquo;s Future", "demand-driven workforce expertise, employer relationships, and job placement pathways."),
            ("Rhode Island Small Business Development Center", "the state&rsquo;s SBA-designated network for small-business advising and technical assistance."),
            ("USDA NIFA and URI Cooperative Extension", "trusted reach into agricultural, coastal, rural, and municipal communities."),
            ("Social Enterprise Greenhouse", "reach into nonprofits, social enterprises, and community-based organisations."),
            ("Rhode Island Foundation", "philanthropic partnership on small business, nonprofit, and startup readiness."),
        ])
        + grp("Research coordination", [
            ("Rhode Island NSF EPSCoR", "whose statewide coordination model &mdash; partnership specialists, jurisdiction-wide convening, seed grants, and the SURF and SHORE student research programmes &mdash; the Hub builds on directly."),
        ])
        + grp("Industry", [
            ("Google, NVIDIA, CIC New England, Slalom, and Infused Innovation", "technical expertise, tool and platform access, guest instruction, mentorship, and potential internship and project placements."),
        ]),
        narrow=True) + section(
        h(2, "Partner logos")
        + ph("Logo wall", "Partner logos, displayed only after written permission is obtained for each. Note that the "
             "Google co-marketing agreement gives Google approval rights over any use of Google's marks. A plain text "
             "list is an acceptable launch state.", priority="Pending permissions"),
        cls="alt")
    out["about-partners.html"] = page("about-partners.html", "Partners", body,
        active="about.html", trail=[A, ("Partners", "about-partners.html")],
        desc="The institutions, agencies, and companies the AI RI Hub works with.")

    # ---------- FAQs ----------
    body = hdr("Frequently asked questions", "Short answers to the questions we are asked most.") + section(
        acc([
            ("What is the AI RI Hub?",
             p("Rhode Island&rsquo;s statewide coordinating body for artificial intelligence. We provide access to AI "
               "computing power, workforce training and credentials, guidance on responsible use, and independent "
               "evaluation of AI products. We were created to carry out the recommendations of the Governor&rsquo;s AI "
               'Task Force. <a href="about-overview.html">Read more about the Hub</a>.')),
            ("Who can use the Hub&rsquo;s programmes?",
             p("Rhode Island residents, public agencies, municipalities, schools and colleges, nonprofits, startups, and "
               "small businesses. Different programmes have different eligibility rules, which are listed on each "
               '<a href="programs.html">programme page</a>.')),
            ("Is the training really free?",
             p("Some of it. Google AI and career certificate licences are provided at no cost to selected Rhode "
               "Islanders, subject to a limited number of licences and eligibility criteria we set. Public-sector cohort "
               "training is subsidised rather than free, and free self-paced resources from other providers are listed on "
               'our <a href="education-training-additional-resources.html">Additional Training Resources</a> page.')),
            ("What is AICR?",
             p("The AI Computing Resource &mdash; a fully managed, near-zero-carbon AI supercomputer at the Massachusetts "
               "Green High Performance Computing Center. Rhode Island holds a share of it, which the Hub makes available "
               'to institutions, agencies, nonprofits, and businesses in the state. <a href="programs-ai-compute-resources.html">See the compute programme</a>.')),
            ("Does the Hub sell or build AI products?",
             p("No. We do not sell software and we do not compete with vendors. We evaluate AI products against published "
               "criteria and publish the results, and we route organisations to the partner best suited to help them. "
               '<a href="programs-solution-registry.html">See the Solution Registry</a>.')),
            ("How do I get involved?",
             p("Use the Engage With Us form, sign up for the newsletter, or contact us directly. If you are an employer, "
               'we especially want to hear what AI skills you are hiring for. <a href="about-contact.html">Get in touch</a>.')),
        ]), narrow=True)
    out["about-faqs.html"] = page("about-faqs.html", "FAQs", body,
        active="about.html", trail=[A, ("FAQs", "about-faqs.html")],
        desc="Frequently asked questions about the AI RI Hub.")

    # ---------- Contact ----------
    body = hdr("Get in touch",
               "Tell us what you are trying to do. If we are not the right resource, we will connect you with the "
               "partner who is &mdash; that is a large part of what the Hub is for.") + section(
        '<div class="cards cards--2" style="align-items:start"><div>'
        + form("Contact the Hub", [
            field("Name", req=True),
            field("Organisation"),
            field("Email", kind="email", req=True),
            field("Area of interest", options=["Compute", "Training", "Small Business",
                                               "K-12 & Education", "Partnership", "Media", "Something else"],
                  hint="This routes your message to the right member of staff."),
            field("Message", kind="textarea", req=True),
        ], "Send message", note="This is a prototype. The form is not connected.")
        + '</div><div>'
        + h(2, "AI RI Hub")
        + p("Institute for Cybersecurity and Emerging Technologies<br>Rhode Island College<br>"
            "600 Mount Pleasant Avenue<br>Providence, Rhode Island 02908")
        + h(3, "Email")
        + p('<a href="mailto:info@ai.ri.gov">info@ai.ri.gov</a>')
        + callout(p("<strong>Media enquiries.</strong> Select &ldquo;Media&rdquo; above and include your deadline. "
                    "Announcements involving partner organisations may require their approval before we can comment."))
        + '</div></div>', narrow=False)
    out["about-contact.html"] = page("about-contact.html", "Contact", body,
        active="about.html", trail=[A, ("Contact", "about-contact.html")],
        desc="Contact the AI RI Hub.")
    return out
