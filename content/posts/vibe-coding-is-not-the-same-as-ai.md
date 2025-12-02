---
title: "Vibe coding is not the same as AI-Assisted engineering"
date: 2025-10-01T10:00:00+01:00
description: "Teams keep mixing up vibe coding with AI‑assisted engineering. Here’s why the difference matters, where each approach shines, and how to move from ideas to production without pain."
tags: ["Vibe Coding", "Agentic AI", "GenAI", "LLM"]
type: "post"
weight: 10
image: "https://substackcdn.com/image/fetch/$s_!iddJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6122dc48-ab21-46f4-a005-f709ecb3550d_1688x1182.jpeg"
showTableOfContents: true
---

{{< postcover src="https://substackcdn.com/image/fetch/$s_!iddJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6122dc48-ab21-46f4-a005-f709ecb3550d_1688x1182.jpeg"
alt="Descriptive alt text"
caption="Reddit post about how engineers vibe code at a FAANG" >}}

Teams keep mixing up vibe coding with AI‑assisted engineering. Here’s why the difference matters, where each approach shines, and how to move from ideas to production without pain.

A recent Reddit post about “how we vibe code at FAANG” sparked debate. It actually described a disciplined workflow: design docs, code review, and tests. That is not vibe coding. That is **AI‑assisted engineering**. Conflating the two devalues engineering and misleads newcomers about what it takes to ship safe, maintainable software.

Vibe coding is great for speed and learning, but it collapses under production demands if you skip structure.

## What “vibe coding” really is

“Vibe coding” means you ride the creative flow with an AI. You prompt at a high level, accept suggestions, and keep iterating fast. You focus on ideas, not on every line of code. It is perfect for prototypes, MVPs, weekend hacks (as Karpathy says), and flattening the early learning curve.

The trade‑off is clear: it prioritizes speed and exploration over **correctness** and **maintainability**. Without guardrails, the output often hides sharp edges.

## The spectrum of AI‑assisted development

There is a spectrum. On one end, pure vibes. In the middle, planning, specs, and enough context to steer the model. On the far end, **AI‑assisted engineering** across the lifecycle: design, tests, small PRs, review, and operations. The human stays in control, uses AI as a force multiplier, and reviews every change.

{{< imagelink url="#"
image="https://substackcdn.com/image/fetch/$s_!cYxB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bb76118-dc78-43e6-8bdb-8b9c6703753f_1536x1024.webp"
width="600px" >}}

The “30% faster” gains often shared come from strengthening a solid process, not skipping it.

### Quick contrast at a glance

| Aspect   | Vibe coding             | AI‑assisted engineering |
| -------- | ----------------------- | ----------------------- |
| Goal     | Explore fast            | Ship safely             |
| Driver   | Prompts and flow        | Specs and tests         |
| Review   | Light or after-the-fact | Rigorous and continuous |
| Fit      | Prototypes, spikes      | Production systems      |
| Key risk | Hidden flaws            | Process overhead        |

Vibe coding accelerates discovery; AI‑assisted engineering sustains delivery.

## Rope, risk, and developer personas

Think of “rope” as freedom and risk.

Vibe Coders have plenty of rope. They describe outcomes in plain language and trust the AI to fill in details. The upside is speed and creativity. The downside is weak review and sparse tests, so code can be brittle and opaque.

Rodeo Cowboys move fast with minimal oversight. Some use AI, some trust their gut. They ship at 2 AM and patch in production. It works—until it does not.

Prisoners have almost no rope. Heavy process or fear of errors slows change to a crawl. Safety is high, but innovation suffers. In both extremes, someone else calls the shots—checklists or the model—not the engineer.

{{< imagelink url="#"
image="https://substackcdn.com/image/fetch/$s_!CX6m!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa52f32d-d2fe-4c08-86f2-f99da6e28d88_1536x1536.jpeg"
width="600px" >}}

Real engineers move across these modes by context. The lesson from the Venn: too much freedom or too many constraints both fail at scale. Balance wins.

## Where vibe coding breaks in production

Leaders and teams keep seeing the same pattern: fast wins followed by hidden liabilities. Common failures include:

- Security gaps: hard‑coded keys, naive auth, or unsanitized inputs.
- Performance surprises: code that passes tests but melts at scale.
- Opaque logic: reviewers cannot reason about dense AI output.
- Team drag: seniors become “code detectives” cleaning up trust debt.

Vibe coding creates an illusion of correctness that cracks under real workloads.

## Will you vibe code your way to production?

Many engineering leaders give a simple answer: not if you value quality, safety, and long‑term maintainability. AI is a **copilot**, not an autopilot. It accelerates good process. It does not replace engineering judgment.

Several reported incidents illustrate the risks:

- Performance meltdown: a query fine in tests throttled production under real traffic. The fix took a week and a full design review.
- Security lapse: an inverted truthy check left deactivated users with access. The bug hid in a sea of AI‑written code.
- Maintainability crash: a vibe‑built auth flow worked until new roles and regional rules arrived. No mental model, scattered middleware, full rewrite.
- False confidence: tidy code and passing unit tests hid edge cases. A thousand‑line PR from an LLM is still hard to review well.

In short, vibe coding puts security, clarity, and shared knowledge at risk when you skip design and review.

## What the community is saying

Developers on Reddit and Hacker News share both pain and nuance. A common complaint: “Please stop submitting huge AI‑generated PRs you have not even read.” Trust and peer review break when authors outsource understanding.

Yet many also report wins in the right scope. Internal tools, one‑off scripts, and glue code get done in hours, not days. The pattern is consistent: it works when an experienced engineer stays in the loop and verifies the output.

## Where vibe coding helps

Used with intention, vibe coding shines in a few places:

- Rapid prototyping and hackathons: get to a demo today, then refactor later.
- One‑off scripts and internal tools: automate boring tasks you control end‑to‑end.
- Greenfield spikes: explore options early, then switch to structure.

The key is ownership. Treat the AI like a fast junior. You still plan, test, and review.

## From vibes to engineering: go spec‑driven

One antidote to prompt chaos is a **spec‑driven** workflow. Start with the intent. Write a short design and acceptance criteria with the AI, then implement in small, testable steps. Agentic tools can also run code, execute tests, and iterate inside boundaries—but they still work best with a clear spec.

Here is a simple pattern:

1. Write the spec and happy‑path tests.
2. Ask the AI to implement one slice that makes a test pass.
3. Run tests locally and in Continuous Integration (CI).
4. Repeat with small PRs and human review.

Small increments reduce surprise. Tests make intent executable.

{{< imagelink url="#"
image="https://substackcdn.com/image/fetch/$s_!F8pz!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F339d50d3-4daa-43c4-8392-97da564101db_1866x708.png"
width="600px" >}}

### Tiny example: test first, then implement

```python
# test_auth.py
# Deactivated users must never access admin tools.
def test_deactivated_user_cannot_access_admin():
    user = {"active": False, "roles": ["admin"]}
    assert can_access_admin(user) is False

# app/auth.py
def can_access_admin(user):
    # Start simple and pass the test. Extend with policy as needed.
    return bool(user.get("active")) and "admin" in user.get("roles", [])
```

Encode intent in a test, then let the AI implement the simplest pass.

## A lightweight flow you can adopt this week

- Require a one‑page design for any non‑trivial AI‑generated change. Write it with the model if you like.
- Generate unit tests and property tests first. Run them in CI. See GitHub Actions docs for setup.
- Keep dependencies within an approved set. Ask the AI to explain every new import in the PR description.
- Prefer in‑IDE assistants (for context and diffs) over blind copy‑paste. See GitHub Copilot docs.
- Add a security pass. Run a scanner and ask the AI to outline likely threats. Cross‑check with OWASP guidance.

References:

- GitHub Copilot docs: https://docs.github.com/en/copilot
- GitHub Actions (CI) docs: https://docs.github.com/en/actions
- OWASP Top Ten: https://owasp.org/www-project-top-ten/

## Where agentic tools fit

Agentic systems can run code, inspect failures, and try fixes. They help with rote checks and boilerplate. They do not remove the need for human decisions about architecture, data flow, or risk. Keep humans in the approval loop. Treat agents like CI assistants, not auto‑deploy robots.

### From sandbox to ship: the hand‑off

Vibe freely to explore options and shape ideas. When you commit to ship, change modes:

- Freeze the design. Write down interfaces, data shapes, and constraints.
- Replace scaffolding with clean modules. Add tests and benchmarks.
- Keep PRs small. Demand clear diffs and rationale.
- Document the why, not just the what.

A simple transition diagram:

```
Ideas → Prototype (vibes) → Spec → Tests → Small PRs → Review → Deploy → Observe
```

Creativity up front, discipline on the way to prod.

## The bottom line

Vibe coding accelerates exploration; AI‑assisted engineering sustains delivery. Mix them on purpose, not by accident. The trade‑off is speed now versus stability later. Your job is to choose when to switch modes.

If you try one change this week, pick a feature and run a spec‑first loop: write a one‑page design, add two tests, and ask your AI to implement only what makes those tests pass. You will feel the pace—and keep the rigor.
