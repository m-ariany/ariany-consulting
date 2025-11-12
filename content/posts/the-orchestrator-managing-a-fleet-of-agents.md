---
title: "The Orchestrator: Managing a Fleet of Agents"
date: 2025-10-28T10:00:00+01:00
description: "Most of us still pair with one AI at a time. The next step is dispatching several agents in parallel and reviewing their pull requests later. That is the shift an orchestrator brings."
tags: ["Orchestration", "Agentic AI", "GenAI", "LLM"]
type: "post"
weight: 10
showTableOfContents: true
---

{{< postcover src="https://substackcdn.com/image/fetch/$s_!xumY!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faeb45e5d-d4fd-4f87-b6cc-8e49d07b7830_1678x936.png"
alt="Descriptive alt text"
caption="Engineer as Orchestrator" >}}

Most of us still pair with one AI at a time. The next step is running several agents in parallel and reviewing their pull requests later. An **orchestrator** makes that shift real.

We have moved from autocomplete to agents that plan, edit, test, and open pull requests on their own. With an orchestrator, AI work runs in the background while we focus on design, integration, and quality. The promise is simple, not magic: delegate well so review time replaces long prompt loops.

## How the workflow runs

An **orchestrator** sets the high‑level goal, defines tasks, and lets autonomous agents execute end to end. These agents clone the repo, create branches, change many files, run tests, and iterate before asking for review. Work lands in version control with **Continuous Integration (CI)**, so it is logged, reviewable, and easy to revert.

We do not watch every step. We care that the outcome matches the spec, passes tests, and fits the architecture. Because agents run in the background and often in parallel, three tasks sent before lunch can return as three **PRs** later the same day.

## Tools that already work this way

- GitHub Copilot Coding Agent. Best for GitHub‑native teams that live in Issues and Actions. Start from an issue or VS Code. It spins up a clean environment, checks out a branch, runs linters and tests, and opens a PR with clear commits. Review normally, or comment “@copilot update tests for edge case Z” to iterate on the same branch.

- Google’s Jules. Best for teams on Google Cloud that want a visible plan and clear control. Connect a repo, request a task (“Upgrade to the latest Node.js and fix compatibility issues”), review the plan, then approve. Jules runs in a secure VM, commits on a new branch, and opens the PR. It can run several jobs in parallel and even produces audio changelogs for summaries.

- Cursor Background Agents. Best when we want a small cloud workforce from the editor. Cursor clones the repo into a temporary workspace and runs the full loop: edit, install, test, build, and search docs. A live dashboard shows progress from desktop or mobile. Several agents can run at once—one on UI polish while another fixes flaky tests—each ending with a detailed PR.

Also in play: OpenAI’s hosted coding agent (trigger from ChatGPT or editor; returns a diff or PR—names change fast, check the latest docs), and Anthropic’s Claude Code for Web (runs long jobs in a managed container with sandboxing; “teleport” the session to local when we need to take over).

## Platforms for running many agents

Open‑source tools make multi‑agent setups feel local. Conductor by Melty Labs runs several Claude Code agents in parallel, each with an isolated Git worktree and a “who’s doing what” dashboard. After a merge, it marks the task “Merged” and offers an Archive button—small, but it keeps the loop tight. Claude Squad splits Claude Code across tmux panes so we can assign tasks to separate instances. On the cloud side, Azure’s agent tooling supports multiple specialized agents that can share context and talk to one another for complex flows.

## Conductor vs orchestrator: what actually changes

Scope of control. A **conductor** guides one agent through a narrow task. An **orchestrator** sets broader objectives for several agents or one powerful agent that runs many steps.

Degree of autonomy. In conductor mode, the agent waits for the next prompt. In orchestrator mode, it plans and executes dozens of steps before asking for feedback.

Sync vs async. Conductor work is a tight loop. Orchestrator work is dispatch‑and‑review minutes or hours later.

Artifacts and traceability. Orchestrators create branches, commits, and PRs tied to issues. There is a clear Git trail. Chat‑style work often leaves less record unless we commit as we go.

Human effort profile. Conductor time sits in the middle—prompt, review, repeat. Orchestrator time is front‑loaded (a good spec) and back‑loaded (review and merge), which scales across many tasks.

## What we saw in practice

On Tuesday, we asked an agent to “add optimistic updates to the todo list,” with acceptance criteria and two edge cases. It proposed a plan, opened a branch, and submitted a PR in 22 minutes. CI flagged a failing test on rapid toggles; we commented with the failing seed and asked it to retry. The agent adjusted the debounce logic, pushed a fix, and the PR merged. In our pilots, time‑to‑PR dropped from 45 to 18 minutes (P95) for this class of change.

```js
// Intent: reduce flake from rapid toggles by ignoring thrash
// Before
function toggleItem(id) {
  setDone(id, !state[id]);
}

// After (agent fix)
const toggleItem = debounce((id) => {
  setDone(id, !state[id]);
}, 120); // milliseconds, tuned to pass the failing seed
```

Caption: A tiny debounce change cleared the rapid‑toggle test and kept behavior smooth.

## Why orchestrators change our day

Each wave in programming removed manual work: assembly to high‑level languages, then frameworks, then AI in the editor. Autonomous coding agents are the next abstraction. In our pilots, small teams handed off 10+ PRs in a day during focused sprints, then spent time on system design and integration. This is not universal yet, but the pattern is clear: agents draft more, humans decide, shape, and verify.

## Toward an “AI team” of specialists

We can sketch a full flow with specialized agents coordinated by a human orchestrator: a Planning Agent breaks work into tasks; Coding Agents implement; a Testing Agent writes and runs tests; a Code Review Agent checks PR quality and standards; a Documentation Agent updates READMEs; and a Deployment/Monitoring Agent ships and watches in prod. Early signs are here: Azure’s building blocks for multi‑agent workflows, internal PR‑by‑agent loops with agent reviewers, and efforts like Model Context Protocol (MCP) so agents can share state.

## Challenges and the human role

Quality and trust. We will not see every change as it happens. Keep humans as the final gate. Review PRs, write clear acceptance tests, and run security checks. Agents can be correct in syntax but wrong in design; build a trust model for when to accept, request changes, or stop and rethink.

Coordination and conflicts. Many agents on one repo can collide. Today’s guardrails are isolation—one task per branch—and task boundaries that reduce overlap. Some tools auto‑rebase, but humans still do the last mile. Agent‑to‑agent negotiation may help over time.

Context and hand‑offs. Teams run on shared state: repo layout, build, tests, style rules, and release steps. Without a workflow layer that passes metadata and tags branches, seams will split. Invest in a central orchestration surface, even if it is light at first.

Prompts and specs. As agents write more code, our “code” becomes specs. Vague prompts drift. Write short design notes and acceptance criteria. Treat agents like contractors: define “done,” list edge cases, and pin constraints.

Tooling and debugging. When an agent stalls or opens a failing PR, we debug the process: weak spec, wrong test, or the agent got lost. Checkpointing and rollback help. Dashboards show long jobs or errors. Expect to drop into conductor mode to untie a knot, then go back to orchestration.

Ethics and responsibility. We still own what ships. That includes licenses, security, and bias. Run scans on generated code and pin safe dependencies. Some agents avoid known vulnerable versions and can run audits, but “trust, then verify” remains the rule.

## How to try it this week

- Pick one repo with CI and a medium‑size task we would give a junior.
- Write a crisp issue with acceptance criteria and edge cases.
- Assign it to a hosted agent that opens PRs; avoid babysitting.
- Review like any teammate’s PR; request one change; check the loop.
- Repeat with two tasks in parallel and measure our review time.

## Where this is going

Many of us will work in both modes. We might queue an async agent for a feature and, the same afternoon, pair with a chat agent on a tricky algorithm. Junior engineers may start as conductors; seasoned engineers lean into orchestration. The tools—Copilot’s agent, Jules, OpenAI’s hosted agent, Claude Code for Web, Cursor—lower the barrier month by month.

A note of caution: multi‑agent UX can feel clunky today, and product names change fast. Verify commands and versions in the docs before installing anything. Still, the direction is steady. As CI and automated tests became standard, continuous delegation is joining the stack.

---

We will still type, but we will also direct a small swarm of helpers. The future is not AI or human; it is AI and human—with humans at the helm. Start small this week: one well‑scoped task, one agent, one PR. Build the muscle to delegate, review, and integrate; the gains compound from there.
