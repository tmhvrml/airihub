# -*- coding: utf-8 -*-
from lib import *
from shell import page

P = ("Programs &amp; Initiatives", "programs.html")

def hdr(title, lede):
    return section(h(1, title) + p(lede, "lede"), cls="tight", narrow=True)

def build():
    out = {}

    body = hdr("Programs &amp; Initiatives",
               "Six programmes, built around the same idea: give Rhode Island organisations access to things they "
               "could not afford or could not evaluate on their own.") + section(
        h(2, "Our programmes")
        + cards([
            dict(title="AI Compute Resources", body="Rhode Island&rsquo;s share of a near-zero-carbon AI supercomputer, open to institutions, agencies, nonprofits, and businesses.", href="programs-ai-compute-resources.html"),
            dict(title="Statewide AI Workforce &amp; Credentialing", body="Micro-credentials, cohort training, and a statewide credentialing seal built with employers.", href="programs-workforce-credentialing.html"),
            dict(title="Small Business &amp; Nonprofit AI Innovation", body="Reserved compute, workshops, readiness assessments, and referrals for organisations without an IT department.", href="programs-small-business-nonprofit.html"),
            dict(title="AI Solution Registry", body="Independent evaluation of AI products against published criteria, sector by sector.", href="programs-solution-registry.html"),
            dict(title="Responsible AI &amp; Governance", body="Honest guidance on where AI fails, and the frameworks and policy support to manage it.", href="programs-responsible-ai-governance.html"),
            dict(title="Grants &amp; Funding Opportunities", body="Federal, state, foundation, and industry funding &mdash; pursued with partners, not alone.", href="programs-grants.html"),
        ]))
    out["programs.html"] = page("programs.html", "Programs & Initiatives", body, trail=[P],
        desc="The AI RI Hub's programmes for compute, workforce, small business, solution vetting, governance, and funding.")

    # ---------- Compute ----------
    body = hdr("World-class AI computing, available to Rhode Island",
               "Rhode Island holds a share of the AI Computing Resource (AICR) &mdash; a fully managed, near-zero-carbon "
               "AI supercomputer operated through the Massachusetts Green High Performance Computing Center.") + section(
        p("It gives Rhode Island institutions, agencies, nonprofits, and businesses access to infrastructure of the kind "
          "normally available only to large research universities, without building or running any of it themselves.")
        + h(2, "What Rhode Island&rsquo;s share includes")
        + ul([
            "<strong>97,762 hours per year</strong> of NVIDIA B200 GPU compute.",
            "<strong>59,918 hours per year</strong> of NVIDIA RTX Pro 6000 GPU compute.",
            "Additional compute beyond the base allocation at preferred rates: <strong>$4.00 per hour</strong> for B200 nodes and <strong>$1.50 per hour</strong> for RTX Pro 6000 nodes &mdash; substantially below commercial cloud pricing.",
            "High-performance VAST storage and professional operational support.",
            "Near-zero-carbon operation: more than 90 percent clean energy, in a LEED Platinum certified facility.",
        ]), narrow=True) + section(
        ph("Photograph", "One licensed photograph of the MGHPCC facility or a data-hall interior, requested from MGHPCC. "
           "This is the one page where a piece of hardware genuinely is the subject. Do not substitute generic "
           "server-rack stock photography &mdash; request the real thing or use none.",
           alt="The Massachusetts Green High Performance Computing Center in Holyoke, Massachusetts.",
           priority="Launch if licensed"), cls="alt") + section(
        h(2, "Why it matters")
        + h(3, "Cost")
        + p("The AICR partnership delivers a two- to three-fold cost advantage over building and hosting the same "
            "capability in Rhode Island, and more than a two-and-a-half-fold advantage over commercial cloud &mdash; with "
            "expert operations included.")
        + h(3, "Speed")
        + p("Access begins years earlier than any self-hosted alternative could deliver, which moves the Action Plan&rsquo;s "
            "timelines forward rather than waiting on construction.")
        + h(3, "Access")
        + p("A share of the allocation and of the Hub&rsquo;s training capacity is reserved for small businesses, "
            "nonprofits, and startups. New infrastructure should not simply deepen the advantages of institutions that "
            "already have infrastructure."),
        narrow=True) + section(
        h(2, "Who can apply")
        + ul([
            "Rhode Island public colleges and universities, for research and student training.",
            "State and local government agencies, for AI pilot projects.",
            "Nonprofit organisations and community partners.",
            "Rhode Island&ndash;based startups and small businesses.",
        ])
        + h(2, "How it is run")
        + p("The University of Rhode Island leads the technical and operational relationship with MGHPCC and manages "
            "allocation tracking, governance, and reporting. Rhode Island College coordinates statewide access, "
            "onboarding, and engagement. Allocation priorities are guided by the Statewide Advisory Board."),
        cls="alt", narrow=True) + section(
        form("Request compute access", [
            field("Organisation", req=True),
            field("Contact name", req=True),
            field("Email", kind="email", req=True),
            field("Organisation type", options=["College or university", "State or local government agency",
                                                "Nonprofit", "Startup", "Small business", "Other"]),
            field("Project description", kind="textarea", req=True, hint="200 words is plenty. What are you trying to do?"),
            field("Estimated GPU hours"),
            field("Data sensitivity", options=["No sensitive data", "Contains personal data",
                                               "Contains health or student records", "Not sure &mdash; please advise"]),
            field("Timeline"),
        ], "Submit request", note="This is a prototype. The form is not connected."), narrow=True)
    out["programs-ai-compute-resources.html"] = page("programs-ai-compute-resources.html", "AI Compute Resources", body,
        active="programs.html", trail=[P, ("AI Compute Resources", "programs-ai-compute-resources.html")],
        desc="Rhode Island's share of the AI Computing Resource at MGHPCC.")

    # ---------- Workforce ----------
    body = hdr("AI skills that mean something",
               "Rhode Island&rsquo;s AI Action Plan named an AI-ready workforce as the state&rsquo;s single highest "
               "priority. This programme is how we get there.") + section(
        p("A coordinated statewide set of micro-credentials, cohort training, and education pathways, built with "
          "employers and recognised across institutions.")
        + p("The problem we are solving is not a shortage of AI courses. It is that no two of them mean the same thing. "
            "Today each Rhode Island institution defines its own credentials, so certificates are not comparable, "
            "learners cannot stack them, and an employer looking at a certificate has no reliable way to know what the "
            "holder can do. We are fixing that."),
        narrow=True) + section(
        h(2, "Three levels of training")
        + cards([
            dict(tag="Tier 1", title="AI Literacy",
                 body="What AI is, how to use common AI tools, and the ethical and social implications of using them. No prerequisites. Delivered through workshops and online modules. Competencies drawn from the U.S. Department of Labor&rsquo;s AI Literacy Framework. <strong>Leads to a statewide AI literacy certification.</strong>"),
            dict(tag="Tier 2", title="Applied AI Skills",
                 body="Sector-specific applications, hands-on tool use, and data interpretation. Delivered through higher education and partner programmes. <strong>Leads to stackable certificates</strong> &mdash; industry-specific and general &mdash; recognised by Rhode Island employers and carrying transferable credit toward degrees."),
            dict(tag="Tier 3", title="AI Leadership and Innovation",
                 body="AI strategy, deployment leadership, responsible-AI governance, and advanced technical skills. Delivered by universities and selected partners for industry professionals and senior government staff. <strong>Leads to a professional AI leadership certificate.</strong>"),
        ]), cls="alt") + section(
        h(2, "Cohort training for public and nonprofit teams")
        + p("We run three cohorts a year for state agency employees, municipal staff, and nonprofit professionals. "
            "Cohorts are hybrid, run roughly twenty to twenty-five participants, and use the AICR for hands-on computing "
            "exercises &mdash; so participants work on their own organisation&rsquo;s problems, not toy examples.")
        + p("Public-sector and nonprofit seats are subsidised. Private-sector and custom employer training is available "
            "at market rates, and revenue from it helps keep the public-sector seats affordable.")
        + callout(p("<strong>Pricing.</strong> Subsidised rates for public-sector and nonprofit participants are set "
                    'annually. <a href="about-contact.html">Contact us</a> for current pricing and cohort dates.')),
        narrow=True) + section(
        ph("Photograph", "One photograph of an actual cohort session, added after the first cohort has run. Until then "
           "this page carries no image &mdash; a stock photo of people around a laptop adds nothing and quietly signals "
           "that the programme has not happened yet.",
           alt="Participants in an AI RI Hub cohort session.", priority="After first cohort"),
        cls="alt") + section(
        h(2, "Micro-credentials")
        + ul([
            "AI Literacy &mdash; all sectors, all experience levels.",
            "Applied AI for Public Sector Professionals.",
            "AI in Healthcare Operations.",
            "AI for Small Business and Nonprofit Leaders.",
            "Technical AI and Machine Learning Practitioner tracks.",
        ])
        + p("Every credential is developed with employer advisory panels and validated by the Statewide Advisory Board. "
            "Credentials are issued under a statewide credentialing seal, so a certificate earned at one Rhode Island "
            "institution carries the same meaning at another.")
        + h(2, "Annual convenings")
        + p("<strong>Higher Education AI Convening, each October</strong> &mdash; faculty and administrators share "
            "curriculum practice, get professional development on new tools, and connect to compute resources.")
        + p("<strong>K-12 Educator AI Convening, each April</strong> &mdash; classroom teachers and district leaders "
            "build a statewide community of practice around AI-ready education.")
        + btns([("Join a cohort", "#join", "btn"), ("Become an employer partner", "#employer", "btn btn--navy")]),
        narrow=True) + section(
        '<div class="cards cards--2" style="align-items:start"><div id="join">'
        + form("Join a cohort", [
            field("Name", req=True, name="cj-name"), field("Organisation", req=True, name="cj-org"),
            field("Email", kind="email", req=True, name="cj-email"),
            field("Sector", options=["State agency", "Municipality", "Nonprofit", "Private sector", "Higher education"], name="cj-sector"),
            field("Which tier interests you?", options=["Tier 1 — AI Literacy", "Tier 2 — Applied AI Skills", "Tier 3 — AI Leadership"], name="cj-tier"),
        ], "Register interest")
        + '</div><div id="employer">'
        + form("Become an employer partner", [
            field("Organisation", req=True, name="ce-org"), field("Contact name", req=True, name="ce-name"),
            field("Email", kind="email", req=True, name="ce-email"),
            field("What AI skills are you hiring for?", kind="textarea", req=True, name="ce-skills",
                  hint="This is the signal that keeps our credentials aligned with real demand."),
        ], "Get in touch")
        + '</div></div>', cls="alt")
    out["programs-workforce-credentialing.html"] = page("programs-workforce-credentialing.html",
        "Statewide AI Workforce & Credentialing", body, active="programs.html",
        trail=[P, ("Workforce &amp; Credentialing", "programs-workforce-credentialing.html")],
        desc="Micro-credentials, cohort training, and a statewide credentialing seal.")

    # ---------- Small business ----------
    body = hdr("AI for organisations without an IT department",
               "Small businesses employ 51.1 percent of Rhode Island&rsquo;s private workforce &mdash; a larger share "
               "than the nation as a whole.") + section(
        p("They are also the organisations least likely to have a training budget, a data team, or the time to evaluate "
          "a crowded AI marketplace. Nonprofits face the same squeeze with even less margin.")
        + p("This programme exists for them. We reserve part of Rhode Island&rsquo;s compute allocation and part of our "
            "training capacity specifically for small businesses, nonprofits, and startups.")
        + h(2, "What is available")
        + ul([
            "<strong>AI readiness assessments and adoption roadmaps</strong> &mdash; a structured look at where AI would actually help your organisation, and where it would not.",
            "<strong>Sector-specific workshops</strong> in retail, healthcare, human services, and manufacturing.",
            "<strong>Affordable and subsidised compute access</strong>, so cost is not what stops a good idea.",
            "<strong>Referral to the right partner</strong> &mdash; the Rhode Island Small Business Development Center, Social Enterprise Greenhouse, Rhode Island Commerce, or a higher education partner &mdash; when hands-on help is what you need.",
            "<strong>Competitive AI innovation micro-grants</strong>, subject to available funding, to offset compute costs and provide technical assistance.",
        ]), narrow=True) + section(
        cards([
            dict(tag="Pilot cohort", tagcls="tag--gold", title="AI Adoption Workshop Series",
                 body="A three-workshop pilot cohort for Rhode Island small businesses, focused on picking one real problem and getting a working answer to it. Practical, hands-on, and free of vendor pitches."),
            dict(tag="Pilot cohort", tagcls="tag--gold", title="Building AI Readiness in Nonprofits",
                 body="A parallel track for nonprofit organisations, with an emphasis on transparency about how AI is used and on measuring whether it actually improved anything."),
        ], cols=2), cls="alt") + section(
        form("Register your interest", [
            field("Organisation", req=True, name="sb-org"),
            field("Contact name", req=True, name="sb-name"),
            field("Email", kind="email", req=True, name="sb-email"),
            field("Organisation type", options=["Small business", "Nonprofit", "Startup"], name="sb-type"),
            field("Sector", options=["Retail", "Healthcare", "Human services", "Manufacturing",
                                     "Professional services", "Other"], name="sb-sector"),
            field("Number of employees", options=["1–5", "6–20", "21–50", "51–100", "More than 100"], name="sb-size"),
            field("What would you most like AI to help with?", kind="textarea", name="sb-need"),
        ], "Join the waitlist", note="Collected so cohorts can be grouped sensibly. This is a prototype; the form is not connected."),
        narrow=True)
    out["programs-small-business-nonprofit.html"] = page("programs-small-business-nonprofit.html",
        "Small Business & Nonprofit AI Innovation", body, active="programs.html",
        trail=[P, ("Small Business &amp; Nonprofit", "programs-small-business-nonprofit.html")],
        desc="Reserved compute, workshops, and readiness support for Rhode Island small businesses and nonprofits.")

    # ---------- Solution Registry ----------
    body = hdr("Vetted AI solutions, in plain terms",
               "The AI marketplace is crowded, fast-moving, and full of claims that are hard to check.") + section(
        p("A superintendent choosing a classroom AI tool and a plant manager choosing a process-optimisation platform "
          "are both being asked to evaluate technology that did not exist two years ago, against vendors with far more "
          "information than they have.")
        + p("The Hub does that evaluation instead. We assess AI products against published criteria &mdash; "
            "effectiveness, data security, responsible use, and fit with Rhode Island&rsquo;s regulatory and operational "
            "requirements &mdash; and publish the results in the AI RI Hub Solution Registry.")
        + callout(p("<strong>What a listing means.</strong> We do not sell software, we take no vendor fees, and a "
                    "listing is a starting point for your own diligence, not a substitute for it. "
                    '<a href="#">Read our evaluation criteria and conflict-of-interest policy</a>.')),
        narrow=True) + section(
        h(2, "Sectors we cover")
        + p("The Registry covers all six sectors identified by the Governor&rsquo;s AI Task Force.")
        + cards([
            dict(title="Education", body="Classroom platforms, evaluated against Rhode Island&rsquo;s student data privacy and instructional effectiveness standards."),
            dict(title="Health", body="Clinical decision support, administrative applications, and healthcare data ethics."),
            dict(title="Finance", body="AI risk management, compliance, and algorithmic transparency."),
            dict(title="Small business, startups &amp; nonprofits", body="Accessible tools for organisations without technical staff."),
            dict(title="Government", body="Deployment, procurement guidance, and responsible-AI policy fit."),
            dict(title="Defense industries &amp; maritime technologies", body="Production optimisation, predictive maintenance, and cybersecurity for connected systems."),
        ]), cls="alt") + section(
        h(2, "Manufacturing")
        + p("Real-time AI platforms now integrate directly with existing industrial control systems to monitor "
            "operations, optimise performance, reduce energy use, and increase uptime. We look for sector-specific "
            "expertise, integration with standard industrial protocols, strong data security, and a demonstrated "
            "operational track record &mdash; so a Rhode Island manufacturer can start without hiring a data scientist first.")
        + h(2, "K-12 education")
        + p("We evaluate classroom AI platforms against Rhode Island&rsquo;s standards for student data privacy, "
            "instructional effectiveness, and responsible use. That means FERPA and COPPA compliance, independent "
            "security certification, a commitment not to use student or teacher data to train models, and integration "
            "with the learning management systems districts already run. We work directly with the Rhode Island "
            "Department of Education to align our criteria with state policy, and we give preference to platforms that "
            "help students understand and question the AI they are using."),
        narrow=True) + section(
        h(2, "How vetting works")
        + ol([
            "A vendor applies, or a Rhode Island organisation nominates a product it is considering.",
            "The Hub evaluates it against the published criteria for that sector, with technical input from partners at URI and the Institute at RIC.",
            "Products that meet the criteria are listed in the Registry with a plain-language summary of what they do, what they cost, and what the evaluation found.",
            "Listings are reviewed on a fixed cycle. AI products change fast; a listing is not permanent.",
        ])
        + btns([("Browse the Registry", "#registry", "btn"), ("Submit a solution for review", "#submit", "btn btn--navy")]),
        cls="alt", narrow=True) + section(
        h(2, "The Registry", ) + '<div id="registry"></div>'
        + p("Filter by sector, organisation type, and cost model.")
        + table(["Solution", "Sector", "Cost model", "Reviewed", "Status"], [
            ["<em>No listings yet</em>", "&mdash;", "&mdash;", "&mdash;",
             "The Registry opens once the evaluation criteria are published and the first review cycle completes."],
        ])
        + p("<em>Build note: this must be a filterable eCMS listing, not a PDF. Evaluation criteria for each sector "
            "should be published as linked documents so the process is inspectable.</em>", "hint"),
        narrow=True) + section(
        '<div id="submit"></div>' + form("Submit a solution for review", [
            field("Company", req=True, name="sr-co"), field("Product name", req=True, name="sr-prod"),
            field("Contact email", kind="email", req=True, name="sr-email"),
            field("Sector", options=["Education", "Health", "Finance", "Small business / nonprofit",
                                     "Government", "Defense &amp; maritime"], name="sr-sector"),
            field("What does the product do?", kind="textarea", req=True, name="sr-desc"),
            field("Relevant certifications and compliance", kind="textarea", name="sr-cert",
                  hint="FERPA, COPPA, SOC 2, HIPAA, and any independent security certification."),
        ], "Submit for review", note="This is a prototype. The form is not connected."), cls="alt", narrow=True)
    out["programs-solution-registry.html"] = page("programs-solution-registry.html", "AI Solution Registry", body,
        active="programs.html", trail=[P, ("AI Solution Registry", "programs-solution-registry.html")],
        desc="Independent evaluation of AI products for Rhode Island organisations.")

    # ---------- Responsible AI ----------
    body = hdr("Using AI well means knowing where it fails",
               "Part of the Hub&rsquo;s job is to be honest about risk.") + section(
        p("We track the harms that matter in practice &mdash; job disruption, data privacy, algorithmic bias, "
          "environmental impact, and intellectual property &mdash; along with the guardrails that actually mitigate "
          "them, and we tell Rhode Island companies, nonprofits, policymakers, and residents what we find.")
        + p("This is not a disclaimer at the bottom of the page. It is one of the reasons the Hub exists. A state that "
            "adopts AI without understanding where it fails will get worse outcomes than one that adopts it more slowly "
            "and more carefully.")
        + h(2, "What we provide")
        + ul([
            "Common responsible-AI guidance that applies across Rhode Island institutions, so organisations are not each inventing their own standard.",
            "Policy analysis and advisory support for state agencies, municipalities, and organisations developing their own AI policies.",
            "Guidance aligned with the Rhode Island Department of Administration&rsquo;s AI policy.",
            "A shared library of best practices, drawn from Rhode Island partners and from the national network the Hub participates in.",
            "Panels and briefings on responsible adoption and governance.",
            "Technical advice on data readiness, model selection, and secure deployment, through partners at URI and Rhode Island College.",
        ]), narrow=True) + section(
        h(2, "Frameworks we work from")
        + cards([
            dict(title="NIST AI Risk Management Framework", body="The reference framework for identifying, measuring, and managing AI risk."),
            dict(title="NIST Cybersecurity Framework 2.0", body="The security baseline underneath any responsible AI deployment."),
            dict(title="OWASP Top 10 for LLM Applications &amp; MITRE ATLAS", body="Threat models specific to large language models and adversarial machine learning."),
            dict(title="U.S. Department of Labor worker-centered AI principles", body="The standard we apply when AI touches how people are hired, managed, or evaluated."),
        ], cols=2), cls="alt")
    out["programs-responsible-ai-governance.html"] = page("programs-responsible-ai-governance.html",
        "Responsible AI & Governance", body, active="programs.html",
        trail=[P, ("Responsible AI &amp; Governance", "programs-responsible-ai-governance.html")],
        desc="Guidance, policy support, and frameworks for responsible AI adoption in Rhode Island.")

    # ---------- Grants ----------
    body = hdr("Funding, and partners to pursue it with",
               "The Hub pursues federal, state, foundation, and industry funding to expand what Rhode Island can offer "
               "&mdash; and we would rather do it with you than alone.") + section(
        p("If you are an employer, an institution, or a community organisation with a proposal that needs a "
          "coordinating partner, tell us.")
        + h(2, "Current and pending")
        + p("<strong>NSF TechAccess: AI-Ready America (NSF 26-508).</strong> The programme funds one coordination hub "
            "per state &mdash; up to $1 million a year for three years &mdash; to accelerate AI readiness, connect "
            "partners, and scale what works. It is co-sponsored by the National Science Foundation, the U.S. Department "
            "of Labor, the U.S. Small Business Administration, and the USDA National Institute of Food and Agriculture, "
            "and connects each state to a national network of 56 state and territory hubs.")
        + p("<strong>Workforce upskilling programmes</strong> aligned to employer demand, pursued with the Department of "
            "Labor and Training and the Governor&rsquo;s Workforce Board.")
        + p("<strong>Foundation and corporate grants</strong> supporting training access and nonprofit AI readiness, "
            "including work with the Rhode Island Foundation.")
        + h(2, "How we use funding")
        + p("The Hub runs on a mix of state appropriations, fee-for-service training revenue, compute service revenue, "
            "grants, academic partnerships, and event sponsorship. That mix is deliberate: a programme that depends on a "
            "single grant disappears when the grant does, and the relationships this work requires take longer to build "
            "than one funding cycle."),
        narrow=True) + section(
        form("Partner on a proposal", [
            field("Organisation", req=True, name="gp-org"), field("Contact name", req=True, name="gp-name"),
            field("Email", kind="email", req=True, name="gp-email"),
            field("Funding opportunity", req=True, name="gp-opp", hint="Name and solicitation number if you have it."),
            field("Deadline", kind="date", name="gp-deadline"),
            field("What role do you need the Hub to play?", kind="textarea", req=True, name="gp-role"),
        ], "Start the conversation", note="This is a prototype. The form is not connected."), cls="alt", narrow=True)
    out["programs-grants.html"] = page("programs-grants.html", "Grants & Funding Opportunities", body,
        active="programs.html", trail=[P, ("Grants &amp; Funding", "programs-grants.html")],
        desc="Grant and funding opportunities pursued by the AI RI Hub with partners.")
    return out
