---
id: lRa9sPaMyy4
title: "Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS"
slug: your-code-has-bugs-lean4-has-proofs-formal-verification-for
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Varun Pant"]
channel: "AI Engineer"
duration_min: 10
published_at: 2026-08-28T18:00:17Z
video_id: lRa9sPaMyy4
youtube_url: https://www.youtube.com/watch?v=lRa9sPaMyy4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS

**Varun Pant**

`AI Engineer` · `AI Engineer` · `2026` · `10 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lRa9sPaMyy4) · [Conference site](https://www.ai.engineer/)

## Description

An AI spent about a week rewriting zlib in Lean and emitted 32,000 lines of proof. Not tests, proof. It decomposed the job into lemmas, closed each one with tactics, assembled them into a single theorem, and a small independent kernel checked the result. Varun Pant opens on the gap that makes this worth caring about now. Coding agents are producing hundreds or thousands of pull requests a week, and none of the usual checks actually clear them. A model grading code is probabilistic, tests cover the inputs someone thought of, and human review does not scale to agent throughput. None of the three can say the code is correct for every input.

His division of labor is the memorable part: humans own the specification, machines own the code and the proof. That puts all the weight on the spec being right, which is why he insists on validating it before anything downstream runs, whether a person reviews it or it gets tested against real inputs. The chess analogy carries the rest, with tactics as moves, a theorem as checkmate, and backtracking when a branch will not close. AWS runs this in production on Cedar, whose authorization semantics live in Lean while the shipping code is Rust, reconciled by roughly 100 million differential tests nightly. Nothing ships until they agree.

Speaker info:
- https://x.com/varun_pant_
- https://www.linkedin.com/in/varunp1/

Timestamps:
0:00 - Why none of the usual checks clear agent output
1:06 - Specifications humans own, proofs machines own
2:00 - Lean as one language for code and proof
3:01 - Tactics, theorems, and the chess analogy
3:58 - A small kernel you can independently rebuild
4:52 - Rewriting zlib into Lean, and 32,000 lines of proof
6:44 - Cedar: Lean semantics, Rust in production
7:40 - Solvers, preconditions, and code erased at runtime
8:37 - Bringing any language into the same core
