"""
Content source for the blog.

To add a new post:
1. Copy one of the dicts in POSTS below.
2. Give it a unique "slug" (used as the filename: posts/<slug>.html).
3. Fill in title, dek, tags, date, author, body_html, and footer_html.
4. Run: python generate_site.py

Posts are listed on the homepage in the order they appear in this list
(newest first is the convention used here).
"""

POSTS = [
    {
        "slug": "i-have-a-name-now-what",
        "title": "I Have a Name. Now What?",
        "dek": "A founder's-note post about starting Freiya Studio with nothing but a name and a reason. It's honest about not knowing the practical next steps (website, branding, registration) and lands on the idea that most things worth building start messy, not with a full plan.",
        "tags": ["Freiya Studio", "Founder Notes", "Small Business"],
        "date": "2026-08-10",
        "date_display": "August 10, 2026",
        "author": "Freilla Espinola",
        "author_url": "https://www.linkedin.com/in/freillamae",
        "body_html": """
  <p>I have a name. Freiya Studio.</p>

  <p>I've said it out loud to myself more times than I'd like to admit. I've typed it into notes apps, scribbled it on the back of receipts, imagined it on a website, on an invoice, on a business card I don't have yet. It feels right, even though right now it belongs to nothing but a Google Doc and a lot of half-finished thoughts.</p>

  <p>I don't know what to do next, and I'm just going to say that plainly.</p>

  <p>I know why I want to build this. I've watched business owners, smart and capable people, drown under everything nobody tells you comes with running a business. The admin that piles up at midnight. The marketing that gets postponed because there's no time to think, let alone create. The website that's been "almost done" for eight months. The feeling of doing it all alone, even when you technically have help, because nothing feels fully taken care of.</p>

  <p>I want Freiya Studio to change that. A place where business owners can hand off the behind-the-scenes work, the operations, the content, the systems, the tech, to someone who actually treats it like it matters. Someone they can rely on, not just another service they have to manage.</p>

  <p>That part I'm sure of. Everything else, I'm not.</p>

  <p>Do I start with a website or a service list first? Do I need a logo before I take on a single client, or is that just procrastination dressed up as productivity? Am I building a brand or an offer? Do I register the business first, or figure out who it's actually for first? I've opened and closed the same blank document so many times it probably doesn't trust me anymore.</p>

  <p>If you're a business owner reading this, you already know this feeling. It's the same one your future clients have when they're staring at a to-do list with forty tabs open and no idea which fire to put out first. It's a little ironic that the thing I want to help people escape is exactly where I'm standing right now.</p>

  <blockquote>Nobody starts with a full plan. They start with a name, a reason, and the willingness to figure it out one decision at a time.</blockquote>

  <p>So this is me starting. Not with a perfect strategy, not with a five year plan, just with the truth: I have a name, I have a reason, and I honestly don't know what the "right" first step looks like. I think that's fine. Most things worth building start in the mess before things get clear, not after.</p>

  <p>If Freiya Studio is supposed to help business owners stay organized, show up consistently, and keep moving forward even when things feel unclear, maybe it makes sense that it's starting this way too. Unclear. Unfinished. Moving forward anyway.</p>

  <p>I don't have the services page yet. I don't have the brand colors or the tagline or a polished "About" section. What I do have is a name I believe in, a problem I understand because I'm living a version of it right now, and a decision to stop waiting until I feel ready.</p>

  <div class="closing">
    <p>So here's to the blank page, and to not knowing what's next and doing it anyway. This isn't a finished idea. It's a beginning. If you're building something of your own and you're stuck in that same foggy "I have no idea where to start" place, that discomfort doesn't mean you're doing it wrong. It usually just means you're doing it first.</p>
    <p>More soon. For now, this is step one.</p>
  </div>
""",
        "footer_html": 'Freiya Studio &middot; Philippines',
    },
    {
        "slug": "spotting-the-pattern",
        "title": 'Spotting the Pattern: What a "Normal" Job Application Should Never Ask For',
        "dek": "A job-search safety post breaking down a red flag Freilla noticed while applying to roles: postings that bundle a subject-line test with a full personal data form and a self-recorded video before any verifiable human or company is on the other end. It backs the warning with FTC and industry data on job scams and deepfake fraud, then closes with a concrete checklist of what to verify before handing over any personal information.",
        "tags": ["Job Search", "Project Management", "Hiring", "Community"],
        "date": "2026-08-09",
        "date_display": "August 7, 2026",
        "author": "Freilla Espinola",
        "author_url": "https://www.linkedin.com/in/freillamae",
        "body_html": """
  <p>I have been job hunting for a while now, tailoring resumes, writing cover letters, and going through the usual motions of trying to land the right role. Along the way, I started noticing a pattern that bothered me enough to write about it.</p>

  <p>A "keyword in the subject line" instruction is a fair test. It tells a recruiter you actually read the posting instead of mass-applying. I have no issue with that.</p>

  <p>What I do have an issue with is when that instruction shows up bundled with something else: a form asking for your full name, contact number, email address, complete home address, and birthdate, plus a self-recorded video introduction, all before there is any human on the other end you can name. No company name in the posting. No founder or hiring manager you can look up. No way to verify who is actually asking for this information.</p>

  <p>Individually, none of these asks is unheard of. Together, on a first-contact application with zero verifiable identity behind it, they start to look less like hiring and more like collection.</p>

  <h2>Why this combination is the red flag, not any single item</h2>

  <p>A real hiring process almost always gives you something to verify: a company domain, a named recruiter, a LinkedIn profile with an actual work history, an office you could look up on a map. Scam-adjacent postings tend to strip all of that away while asking for more from you in return.</p>

  <blockquote>Verification should flow both ways. If a company will not tell you who they are, you should not be handing over who you are.</blockquote>

  <p>The FTC has pointed out that legitimate employers generally do not request sensitive personal information before an actual interview takes place, and they do not run hiring entirely through chat apps like WhatsApp or Telegram. When a posting asks for your full contact details, home address, birthdate, and a video of your face and voice before you have even spoken to a real person, that is backwards.</p>

  <p>This is not just an inconvenience. Full personal data forms and video recordings are exactly the raw material used for identity theft, account takeovers, and increasingly, deepfake generation. A single clear video of your face and voice is enough training material for a voice clone or a face-swap filter. Once that is out there, it can be reused in ways that have nothing to do with your job search.</p>

  <h2>The scam landscape has changed, and it moves in both directions</h2>

  <p>Most of what gets written about AI and hiring fraud right now focuses on companies worrying about fake candidates: deepfake interviewees, proxy hires, and AI-generated identities gaming the process. Industry researchers have tracked a sharp jump in this kind of fraud in the past year.</p>

  <div class="stats">
    <div class="stat">
      <span class="num">1,000%+</span>
      <span class="label">rise in deepfake attempts in hiring, year over year, per industry trackers</span>
    </div>
    <div class="stat">
      <span class="num">$500M+</span>
      <span class="label">consumer losses to job scams in 2024, up from $90M in 2020, per FTC data</span>
    </div>
  </div>

  <p>But the same tools work in the other direction, against job seekers. Fraudsters use AI-generated job postings, cloned company websites, and increasingly convincing recruiter personas, complete with polished profiles and realistic video calls, to harvest personal information at scale. What used to be obvious, bad grammar, a Gmail address, a vague company name, is now much harder to spot, because generative AI has closed that gap.</p>

  <p>The uncomfortable part is that the underlying job can be completely real, and the process can still be exploitative. A company does not need to be a total fabrication to be running a careless or predatory intake process. Sometimes it is simply a low-effort operation that never bothered to build a legitimate verification step, and personal data collection became the path of least resistance.</p>

  <h2>What I am doing differently now</h2>

  <div class="flag-row">
    <span class="flag-tag">Check</span>
    <p><strong>I look for a name before I hand over anything.</strong> A recruiter, a hiring manager, a founder, someone with a LinkedIn history and a role I can cross-check against the company's actual site. No name, no data.</p>
  </div>

  <div class="flag-row">
    <span class="flag-tag">Check</span>
    <p><strong>I check the domain, not just the logo.</strong> Scammers frequently register lookalike domains that differ from the real company by a hyphen or a letter. I check the sender's email domain against the company's actual website before replying to anything.</p>
  </div>

  <div class="flag-row">
    <span class="flag-tag">Check</span>
    <p><strong>I treat "record a video of yourself" like "hand over my full personal details."</strong> Both are identity data. I do not send either without a named point of contact and a verifiable company behind the request.</p>
  </div>

  <div class="flag-row">
    <span class="flag-tag">Check</span>
    <p><strong>I never send financial details or IDs over chat apps.</strong> If the entire process happens over WhatsApp or Telegram with no company email in sight, that alone is enough for me to step back.</p>
  </div>

  <div class="flag-row">
    <span class="flag-tag">Check</span>
    <p><strong>I slow down when there's urgency.</strong> Scam recruiting counts on job search fatigue and the pressure to respond quickly. A legitimate process can wait a day for me to verify who I am talking to.</p>
  </div>

  <div class="verify-block">
    <span class="stamp">Keep vs. drop</span>
    <ul>
      <li><span><strong>Keep:</strong> the subject-line keyword. It costs nothing and proves you read the posting.</span></li>
      <li><span><strong>Drop:</strong> handing over your full contact details, home address, birthdate, and a self-recorded video before a single named human is on the other end.</span></li>
    </ul>
  </div>

  <div class="closing">
    <p>Part of why I am active in <strong>Python Asia Organization</strong> and <strong>Python Philippines</strong> is that so much of what protects our community comes down to sharing what we have already figured out, so the next person does not have to learn it the hard way. Job hunting is stressful enough without also having to run a fraud investigation on every posting that lands in your inbox. If this pattern sounds familiar to you, it is worth naming it out loud, and worth pausing before you send anything you cannot take back.</p>
  </div>
""",
        "footer_html": (
            '<a href="https://www.linkedin.com/in/freillamae" target="_blank">Freilla Espinola</a> '
            '&middot; Philippines &middot; '
            '<a href="https://pythonasia.org/" target="_blank">Python Asia Organization</a> &middot; '
            '<a href="https://python.ph/" target="_blank">Python PH</a>'
        ),
    },
]
