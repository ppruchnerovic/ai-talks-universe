# Superprompt: how to build a ticket factory, from the AI Talks Universe

A research prompt for an agent that has this repository checked out and can
run its terminal tools: Claude Code, Codex, Copilot CLI, OpenCode, Gemini CLI.
It drives the `ai-conference-talks` skill through one big question: how do
practitioners build a pipeline that takes in tickets and ships verified
changes with agents doing most of the work?

**How to use it**

1. Open the agent at the repo root.
2. Fill in the `YOUR CONTEXT` block, or leave it alone to get a general
   blueprint.
3. Paste everything between the two `=====` lines.

The result is a cited build blueprint. Expect about 150-200k tokens of
retrieval. Use the short version at the bottom when you want a fast first
pass.

---

```text
===================================================================== START

ROLE
You are a research analyst and staff engineer. You are writing a build
blueprint for a "ticket factory", and the AI Talks Universe knowledge base
in this repository is your only source. You know nothing about what these
speakers said until you have retrieved it.

MISSION
Pull out of the corpus everything practitioners have said about how to
design, build, roll out, measure and secure a ticket factory. Turn it into a
blueprint I can act on, where every claim traces back to a talk and a moment
in it.

WHAT "TICKET FACTORY" MEANS HERE
A ticket factory is a pipeline. Its unit of work is a ticket (a Jira, Linear
or GitHub issue, a Sentry alert, a support escalation, a Slack request). It
turns that ticket into a merged, verified change, and agents do most of the
work. It has two halves; cover both:

  UPSTREAM  : raw signal → intake → triage, dedup, routing → enrichment and
              context → an agent-ready ticket (a spec or plan with acceptance
              criteria, sized and decomposed)
  DOWNSTREAM: agent-ready ticket → agent execution in a sandbox → automated
              verification (tests, evals, review agents, CI) → human gate or
              auto-merge → deploy → feedback into the harness and into new
              tickets

When I last searched, the corpus had no talk containing the exact phrase
"ticket factory". Check that once:
    python3 tools/query.py '"ticket factory"' --brief
Then work in the corpus's own vocabulary. Speakers describe this as:
software factory, dark factory, agentic factory, lights-out, harness
engineering, background / async / cloud agents, agent fleets and swarms,
triage agent, agentic workflows / continuous AI (GitHub Actions-driven),
spec-driven development, research-plan-implement, plan and review,
issue-to-PR, ticket-to-PR, self-merging repo, Ralph / agent loops,
forward-deployed engineering. Add every new term you find to this list as
you go, and use them in later queries.

YOUR CONTEXT  (edit these; anything left as "unspecified" gets a general answer,
with a note wherever the right choice depends on it)
  - Ticket tracker(s): unspecified        e.g. Jira, Linear, GitHub Issues
  - Ticket sources:    unspecified        e.g. humans, Sentry, support, evals/traces
  - Codebase:          unspecified        languages, monorepo or polyrepo, size, test coverage
  - Team:              unspecified        engineers, PMs, who reviews today
  - Agent platform:    unspecified        Claude Code, Codex, Cursor, Copilot, Devin, in-house
  - Autonomy target:   unspecified        assistive / supervised / lights-out for one ticket class
  - Constraints:       unspecified        regulated domain, security posture, budget
  - Output language:   English

GROUND RULES  (non-negotiable)
 1. Read .claude/skills/ai-conference-talks/SKILL.md first and follow its
    retrieval ladder exactly: query.py to find talks, then excerpt.py
    (or query.py --excerpt) to read them. Run every command from the repo
    root.
 2. Retrieve before you assert. Never answer from memory, never invent a
    speaker's position, and never guess a missing speaker name. Write
    "a speaker at <conference>" instead.
 3. Quote only from transcripts. --quotes is the view for that. Never quote
    a YouTube description: it is marketing copy. A talk that has no
    transcript can be recommended, but it cannot be cited for what it argues.
 4. Never `cat` a talks/*.md file to find what someone said. Never use
    excerpt.py --full on more than one talk.
 5. Never quote corpus counts from memory. Get them from
    `python3 tools/query.py --stats` and `--facets`.
 6. Do not fetch transcripts. When a talk you need has none, list it under
    "Evidence gaps".
 7. Citations: link the talk's `url`. For YouTube, deep-link with
    &t=<seconds>s. A timestamp shown as ~m:ss is interpolated; cite it as
    "around N minutes in". InfoQ pages take no timestamp, so give the time
    in words.
 8. Tag every claim with its evidence:
      [T] supported by a transcript passage you read
      [D] only a title or description says so (weak; say so)
      [S] your own synthesis across sources (say which ones)

CORPUS TRAPS FOR THIS TOPIC  (check each one with --facets before you rely on a result set)
 - Boilerplate inflation. AI DevCon (Tessl) video descriptions carry a
   channel blurb that mentions "software factories", so many of their talks
   match on the description even when the talk is about something else.
   Scope the factory terms to what was said, e.g.
   `transcript:"software factory"`, or add --transcript, and compare the
   --facets for both forms.
 - Vendor concentration. Tessl, Factory, Cursor, GitHub, OpenAI, Cognition
   and others sell factory tooling, so their numbers are self-reported.
   Example: a talk title claiming "850 PRs a week". Mark such numbers as
   vendor claims, and look for an independent practitioner who confirms or
   contradicts them. Use --per-conference so one channel cannot dominate a
   ranking.
 - Name collisions. "Factory" is also a company (Eno Reyes's talks). "AI
   factory" in NVIDIA, AWS and sovereign-infra talks means GPU datacenters,
   which is irrelevant here. "Agent Factory" is a team name at Workday.
   Exclude these, or read them knowing what they are.
 - Time skew. Transcripts cluster in the most recent year. You cannot say
   how thinking evolved over the years from transcripts alone. If you
   describe a trend, say it rests on titles and descriptions for the
   earlier years.
 - Duplicates. The same talk given at several events (e.g. one NDC talk in
   three cities), or the same talk uploaded twice ("(also: …)"), is one
   voice, not a consensus.

RESEARCH PLAN

Phase 0. Orient (cheap).
    python3 tools/query.py --stats
    python3 tools/query.py --list-topics
    python3 tools/query.py '"software factory" OR "dark factory" OR "harness engineering"' --facets
    python3 tools/query.py 'transcript:"software factory" OR transcript:"dark factory"' --facets
  Note which conferences and years actually carry transcripts for this
  subject.

Phase 1. Discover the vocabulary (two or three queries, no more).
  Run a broad OR query with --brief -n 25. From the snippets, collect the
  product names, jargon and recurring phrases, then re-query with them.
  Seed:
    python3 tools/query.py '"software factory" OR "dark factory" OR "background agents" OR "triage agent" OR "spec-driven" OR "agentic workflows" OR "issue to PR"' -n 25 --transcript --brief

Phase 2. Answer one research question per factory stage.
  For each area below: run ONE OR-chained query (adapt the seed with the
  vocabulary from Phase 1), choose the 4-8 best transcript-bearing talks
  from across conferences, and read them with
  `excerpt.py <ids> -q "<area terms>" -n 3` or `--quotes`. Extract:
  practices, concrete numbers, design decisions, disagreements, failure
  stories. If your agent can run subagents, give each area to one
  subagent along with the GROUND RULES and CORPUS TRAPS. Have each one
  return findings with citations, not prose.

  A. Reference architectures. What do the end-to-end factories people
     describe look like, stage by stage? Who runs one in production,
     and at what scale?
     seed: '"software factory" OR "dark factory" OR "agentic factory" OR "lights out"'
  B. Intake and triage. Where tickets come from (humans, incidents,
     traces, evals, support). How they are classified, deduplicated,
     prioritized and routed. Triage agents, tracker MCP servers.
     seed: '"triage agent" OR triage OR backlog OR jira OR linear OR "github issues" OR NEAR(ticket agent, 10)'
  C. Agent-ready tickets. What makes a ticket executable by an agent.
     Specs, acceptance criteria, definition of done, decomposition and
     sizing. Who writes the plan, human or agent, and why.
     Research-plan-implement. Plan review vs. code review.
     seed: '"spec-driven" OR "acceptance criteria" OR "research plan implement" OR "task decomposition" OR "definition of done" OR "plan and review"'
  D. Context and harness. AGENTS.md/CLAUDE.md, skills, rules, codebase
     maps, product and design constraints, memory. Why agents ignore
     instructions. "Harness, not prompt".
     seed: '"harness engineering" OR "agents.md" OR "claude.md" OR "context engineering" OR "codebase context"'
  E. Execution. Background/cloud/async agents. One VM or sandbox per
     agent, worktrees, parallelism and fleets, long-running loops, retries,
     model choice, inference cost for async workloads.
     seed: '"background agents" OR "cloud agents" OR "async agents" OR sandbox OR worktrees OR "parallel agents" OR swarm'
  F. Verification. Tests (and the risk of AI-written tests), evals for
     code-review agents, review bots, CI redesign ("commit-fail-commit"),
     verification loops, what has to be true before a PR is opened.
     seed: 'NEAR(agent "code review", 15) OR "review agent" OR "verification loop" OR "ci/cd" OR "commit-fail-commit"'
  G. Human gates and auto-merge. What humans still review and where in
     the flow. Criteria for auto-merge or a "self-merging repo". Trust
     ladders and autonomy levels. The review bottleneck.
     seed: '"auto-merge" OR "self-merging" OR "human in the loop" OR "levels of autonomy" OR "kill the code review" OR trust'
  H. Event-driven automation. Agents triggered by repo events, schedules
     or alerts (agentic workflows, GitHub Actions, continuous AI).
     Incident-to-PR and self-healing software.
     seed: '"agentic workflows" OR "continuous ai" OR "github actions" OR "self-healing" OR NEAR(incident agent, 10) OR sentry'
  I. Feedback and self-improvement. How failed or rejected tickets
     improve the harness. Demand-driven context, recursively
     self-improving agents, attribution of mistakes, learning loops.
     seed: '"feedback loop" OR "self-improving" OR "demand-driven context" OR "lessons learned" OR retrospective'
     add: --topic sdlc --topic coding --topic agents  (without them, healthcare and career talks crowd in)
  J. Metrics and economics. PR throughput, merge rate, % of PRs handled
     end to end by agents, cycle time, DORA under AI, review debt, cost
     per PR or per ticket.
     seed: '"merge rate" OR throughput OR "cycle time" OR "dora metrics" OR "review debt" OR "cost per"'
  K. Security and governance. Issue text and repo content as untrusted
     input (prompt injection through tickets), least-privilege agents,
     hooks, secrets, hardening GitHub Actions, blast radius, audit trails,
     regulated environments.
     seed: 'NEAR(agent "prompt injection", 20) OR "least privilege" OR "blast radius" OR "github actions" OR hooks'
     add: --topic security --topic coding  (and once without --topic, to compare)
  L. Organization and people. New roles (harness engineer,
     forward-deployed engineer, PM as orchestrator), the
     attention/multi-agent ceiling, standups and planning, adoption
     resistance, skills that change.
     seed: '"forward deployed" OR "engineering org" OR orchestrator OR "attention is the bottleneck" OR "harness engineer"'
  M. Failure modes and anti-patterns. Why factories fail, slop, falling
     merge rates, review overload, over-trusting AI plans, what people
     wish they had not done.
     seed: '"why software factories fail" OR slop OR "failure modes" OR "wish I" OR "what went wrong"'
     add: --topic sdlc --topic coding  (without them, "video slop" and Green IT talks crowd in)

Phase 3. Deep-read the anchors.
  From A-M, choose the 3-5 talks that describe a whole factory end to end,
  with a transcript and from different organizations. Read each with
  `excerpt.py <id> -q "<their own vocabulary>" -n 10 --window 90`, or use
  --outline first for talks over 45 minutes. Reconstruct each one's
  pipeline stage by stage.

Phase 4. Look for disagreements.
  For each key decision (who writes the plan; review the plan or the code;
  auto-merge or not; one big agent or many small ones; spec-first or
  iterate; in-house harness or vendor platform), search for the opposing
  view directly, e.g. 'NEAR(review plan, 10)' vs 'NEAR(review code, 10)'.
  Do not settle a disagreement that the corpus leaves open.

BUDGET
  - Phase 2: about 10-12k tokens per area (--brief -n 15 ≈ 1.5k; six
    excerpts at -n 3 ≈ 6k; --quotes on the same talks ≈ 1k).
  - Phase 3: about 2k per anchor talk. Whole run: about 200k tokens at most.
  - To go wider, run another -q against talks you already have before
    reading new ones end to end.

OUTPUT: "Ticket Factory Blueprint"
  0. Scope note. The corpus slice you used (from --stats and --facets),
     the vocabulary map, and the traps that affected the result.
  1. Executive summary. At most 10 bullets, each tagged [T]/[D]/[S] with
     a link.
  2. Reference architecture. A Mermaid flowchart of the stages from
     signal to merge to feedback. For each stage: its purpose, how
     practitioners build it, the key design choices, and 1-3 cited
     examples.
  3. Case studies. One short section per anchor talk: who, the scale they
     report (marked as self-reported), their pipeline, what they say made
     it work, and what bit them.
  4. Design decisions. A table: Decision | Option A (who, link) | Option B
     (who, link) | What it depends on | Recommendation for MY CONTEXT [S].
  5. Agent-ready ticket template. Fields and rules, with each field
     justified by a cited source. Include a good and a bad example ticket.
  6. Rollout plan. Crawl, walk, run: which ticket classes to automate
     first, the entry and exit criteria for each phase, and the human
     gates at each.
  7. Metrics to instrument. Metric | Why | Who uses it (link) | Target or
     benchmark (marked vendor or independent).
  8. Failure modes and guardrails. Failure | Symptom | Mitigation | Source.
  9. Security and governance checklist.
 10. People and process. Roles, rituals, skills, and how review work
     changes.
 11. Tooling landscape. Only products named in transcripts. Who uses each,
     for which stage, and a flag on vendor-presented claims.
 12. Evidence gaps. What the corpus does not cover or covers thinly,
     description-only areas, and talks worth fetching transcripts for.
 13. Watch list. The top 10 talks: title, speaker or "unnamed",
     conference and year, length, transcript Y/N, why it matters, link.
 14. Appendix. Every query you ran, plus any _note:_ lines that changed
     your interpretation (dropped words, semantic-only hits).

  Return the blueprint in chat. If it runs past about 4,000 words, also
  save it as ticket-factory-blueprint.md outside the repository (do not
  commit it) and give me the path.

SELF-CHECK BEFORE YOU ANSWER
  [ ] Every quote comes from a transcript, with a working deep link.
  [ ] No speaker name is guessed. No corpus count is quoted without
      --stats or --facets behind it.
  [ ] Vendor-reported numbers are labelled. No single channel supplies
      more than about half the citations, or the dominance is disclosed
      in section 0.
  [ ] Both the upstream (ticket creation and triage) and downstream
      (execution, verification, merge) halves are covered, or the gap
      is stated.
  [ ] Every recommendation tagged [S] names the sources it combines.
  [ ] Open disagreements are presented as open.

======================================================================= END
```

---

## Short version

For a quick first pass, in about 30k tokens:

```text
Using the ai-conference-talks skill in this repo (read
.claude/skills/ai-conference-talks/SKILL.md first and follow its ladder),
find out how practitioners build a "ticket factory": a pipeline that turns
tickets (Jira/Linear/GitHub issues, alerts) into verified, merged changes
with agents doing most of the work. The corpus calls it a software factory,
dark factory, harness engineering, background agents, triage agent,
spec-driven development or agentic workflows. Match those terms against
transcripts (`transcript:"software factory"`), because Tessl's channel
descriptions inflate matches. Use --per-conference to diversify. Read the
best 6-8 transcript-bearing talks with excerpt.py -n 3 and --quotes. Give
me: the stage-by-stage pipeline, the 5 key design decisions and who argues
which side, the metrics people track, the top failure modes, and a
watch list of 8 talks. Cite every claim with a deep link. Quote only
transcripts, mark vendor-reported numbers, never guess speaker names, and
say where the corpus is thin.
```

## Follow-ups that work well after the blueprint

- "Take section 5 and write the agent-ready ticket template as a Jira issue
  type / Linear template for MY CONTEXT. Cite which talk motivates each field."
- "Compare the factories described by the anchor talks side by side: intake,
  plan authorship, execution environment, verification, merge policy,
  reported numbers."
- "Go deeper on area K. List every way a ticket's own text can attack the
  agent that executes it, and the mitigation speakers propose for each."
- "Which of the watch-list talks lack a transcript? Give me the fetch
  command for them" (run it on a local machine, not in the cloud).
