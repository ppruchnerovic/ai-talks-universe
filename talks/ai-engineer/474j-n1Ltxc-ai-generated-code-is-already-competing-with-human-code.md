---
id: 474j-n1Ltxc
title: "AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile"
slug: ai-generated-code-is-already-competing-with-human-code
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Daksh Gupta"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-09-27T18:30:07Z
video_id: 474j-n1Ltxc
url: https://www.youtube.com/watch?v=474j-n1Ltxc
youtube_url: https://www.youtube.com/watch?v=474j-n1Ltxc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Google Antigravity", "Antigravity 2.0", "Kevin Hou", "Google DeepMind", "Gemini 3.5 Flash", "agent teams", "subagents", "multi-agent systems", "generative UI", "sidecars", "agentic coding", "AI coding tools", "Windsurf", "software factories", "AI Engineer", "AI Engineer World's Fair", "Daksh Gupta", "Greptile", "AI code review", "AI generated code", "vibe coding", "pull requests", "code validation", "Claude Code"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile

**Daksh Gupta**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Google Antigravity` `#Antigravity 2.0` `#Kevin Hou` `#Google DeepMind` `#Gemini 3.5 Flash` `#agent teams` `#subagents` `#multi-agent systems` `#generative UI` `#sidecars` `#agentic coding` `#AI coding tools` `#Windsurf` `#software factories` `#AI Engineer` `#AI Engineer World's Fair` `#Daksh Gupta` `#Greptile` `#AI code review` `#AI generated code` `#vibe coding` `#pull requests` `#code validation` `#Claude Code`

[Watch the recording](https://www.youtube.com/watch?v=474j-n1Ltxc) · [Conference site](https://www.ai.engineer/)

## Description

More than a quarter of the pull requests Greptile reviewed in April showed signs of being written largely or entirely by AI agents, up from under 1% a year earlier. Daksh Gupta, co-founder of Greptile, analyzed more than a million pull requests a month from companies like NVIDIA, Coinbase and Scale to test a simple question: are fully vibe-coded PRs actually any good in enterprise codebases?

He compares agent-written PRs (Codex, Claude Code, Devin, Cursor) with human-written ones on four measures: revert rates, revert rates by PR size, the severity of issues Greptile flags (P0/P1/P2), and how many review rounds it takes to get to a mergeable PR. On all four, agent code landed in the same range as human code, and humans were actually more likely to introduce P0 bugs. The differences show up in *how* each one fails: Claude is about 1.5x more likely than humans to introduce SQL injection, Devin is half as likely to cause auth bypasses, and N+1 queries are far more common from Cursor.

Daksh also shares what this means for code review. The median Greptile user makes fewer than 50 commits a month, while the 99th percentile makes close to 1,000, which makes manual review impossible at that scale. He argues that code validation should answer three questions: Does this change violate the user contract? Does it make a future violation more likely? Does it do what the author intended? He then shows how Greptile answers them with blast-radius analysis and sandboxed browser agents that try to break the app.

Speaker info:
- Greptile: https://greptile.com
- Daksh Gupta on X: https://x.com/dakshgup
- Daksh Gupta on LinkedIn: https://www.linkedin.com/in/dakshg/
- Daksh's website: https://dakshgupta.com

Timestamps:
00:00 Intro
00:25 Daksh Gupta & Greptile
00:57 From tab complete to fully autonomous agents
02:09 Are fully vibe-coded PRs any good?
02:29 How to detect vibe-coded PRs: author fields, co-author footers, branch prefixes
03:49 25%+ of PRs vibe coded, up from under 1% a year ago
04:18 What makes a pull request "good"?
04:38 Revert rates: Codex vs. Devin vs. humans
05:28 Do revert rates change with PR size?
06:08 Severity of issues found: P0s, P1s and P2s
07:02 Review rounds to reach a mergeable PR
07:47 Different failure modes: SQL injection, auth bypass, N+1 queries
09:07 Autonomous agents work in enterprise settings
10:01 What this means for code review: 50 vs. 1,000 commits a month
10:51 Rethinking code validation: three questions
11:16 How Greptile validates: blast radius + sandboxed browser agents
11:56 Closing

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*2,460 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=474j-n1Ltxc&t=12s)** How's everyone doing? Awesome. Uh, my name is Du. I'm one of the co-founders of a company called Gravile. And at Grapile, we're working on AI agents that validate poll requests with full context of the codebase. The way Graval does this is every time there's a pull request, we have a swarm of agents and they go and look at every file that's changed, every file that's related to the files that changed to figure out if there's bugs. And it also spins up your code in a sandbox, installs the dependencies, spins up local host, clicks around to try to break things, mocks inputs, and everything else to figure out if the code is broken. But I'm going to talk about something a little bit different, which is fully autonomous coding agents. So I first moved to San Francisco three

**[0:59](https://www.youtube.com/watch?v=474j-n1Ltxc&t=59s)** years ago to work on AI coding. And this is because GBT 3.5 which came out in 2022 was the first model that seemed like it was really good at programming at the time. Code complete tab complete was like the main paradigm for coding. The most exciting thing that was happening was you had tab complete from cursor and you had co-pilots code complete and that was like the way in which AI coding works. In 2024, for the first time, multifile editing started to work. Cursor was the first to do this and then a couple of other products followed. But now, for the first time, AI could simultaneously edit multiple files at once. But things got really interesting in 2025 because for the first time, we had autonomous agents. They could be given a task and they could go and fulfill the task and create entire pull requests all at once. And this came to a precipice in December of last year when coding agents became

**[1:48](https://www.youtube.com/watch?v=474j-n1Ltxc&t=108s)** literally completely autonomous. And anyone that's working in AI coding knows that December when the new models came out was sort of this like watershed moment in the history of AI coding because these products for the first time were like truly autonomous in how they programmed. And all over Twitter were all these crazy stories of people that were having these agents spin off and open a 100 pull requests a day. They were experimenting with polyphasic sleep so they could stay awake to re-trigger their agents from time to time. And as someone that started programming before agents, I was very skeptical that real companies could program this way. So I was really really curious, are these fully vi PRs really actually good? Is this something that's sort of a Twitter hype and you can have independent developers and and maybe like small startups with no real customers do this? But anyone with real customers with an actually commercially viable code base,

**[2:38](https://www.youtube.com/watch?v=474j-n1Ltxc&t=158s)** could they still use these end-to-end coding agents? And at Grubile, we're fortunate to work with some very large companies. We work with Nvidia, with Coinbase, with Scale, with Data Dog, with American Express. And we got really excited to see if these coding agents were being used really at these large companies and if they were any good at doing real world coding. So, as an amateur data scientist, I decided to go and dive into our data. We review more than a million poll requests a month and we tend to get a lot of interesting data on what's good and bad about these poll requests. We do this for thousands and thousands of companies and they're usually enterprises or at least companies with serious products with real customers. And so we figured actually studying this data would yield some really interesting results. Was a surprisingly hard to figure out from all

**[3:25](https://www.youtube.com/watch?v=474j-n1Ltxc&t=205s)** the poll requests that GR was reviewing which of the poll requests was actually generated by AI. Surprisingly difficult to do this. The first thing that I tried was I started looking at the GitHub author field. GitHub every commit has an author field and so went through the authors and turns out that less than 1% of pull requests had codeex or clawed or cursor as the author. But it wasn't intuitive to me that only but 1% of all code was fully AI generated. It just seemed intuitive that that number would be much higher. So I started to look for other signals. Now thankfully Claude and Codex and some other products leave a PR description in the footer. In the PR description, they put something along the lines of co-authored by claude or co-authored by cursor and so on. And this gave me a little bit more signal, a little bit more data on which PRs were ostensibly largely, if not completely AI generated. The third thing I looked at

**[4:14](https://www.youtube.com/watch?v=474j-n1Ltxc&t=254s)** was branch name prefixes. If you use Codex, you know that Codex names as branches. And it seemed reasonable that if someone was using these coding agents in such a sense that they were writing the branch names or writing the PR descriptions that the PRs were largely AI generated. That seemed like a reasonable assumption to me. So now I had a good set of signals to indicate whether a poll request was in fact completely or largely AI generated or not. And I came to the result that about a quarter of all the poll requests that Graal was reviewing in any given month were completely or at least largely generated by AI. Then I backtracked this data to the last 12 months and it turns out that this number is growing really fast. In fact, early last year, fewer than 1% of pull requests had any evidence of being completely AI generated. So this number is going very very fast as model performance is getting better. What's also interesting is that you can't tell

**[5:03](https://www.youtube.com/watch?v=474j-n1Ltxc&t=303s)** when new models came out on this chart. It seemed like the progress is very continuous. These things are just generally diffusing into the economy at a generally high pace. So then came the next question. Everyone's vibe coding. Everyone's producing these PRs that are antiendentic. Not human plus AI but literally AI. The question is are these PRs any good? First question, what does it mean for PR to be good? That seemed like actually a very important question to answer before we got into judging these AI generated PRs. And so I took a few methods to try this. The first one I tried was revert rates. If a pull request reverted, it was probably pretty bad. And so that seemed like a pretty sincere sort of guess at what a bad PR could be. And so I started tracking, okay, which PRs were in fact reverted. GitHub conveniently names its branches with a revert dash PR number and PR

**[5:51](https://www.youtube.com/watch?v=474j-n1Ltxc&t=351s)** name. And so I was able to track the rate at which these things were being reverted. And I found some interesting data. Codex PR is reverted about one out of every thousand poll requests. Devon once every three and a half times every thousand poll requests. Humans right in the middle at about two and a half. So there doesn't seem to be very big difference between the rate at which poll requests were reverted from people versus agents in my study. Now I was very skeptical of this and I figured okay this is probably because humans are making agents do the easier work the simpler well scoped pull requests and the more complex work was being done by humans and of course complex work had a higher propensity to be reverted because the poll requests were more complicated had larger surface areas risks and so on. So I decided to measure the average size of PR and whether the revert rates were sort of aligned for both of those and I found really interesting data. Turns out there's actually very little

**[6:38](https://www.youtube.com/watch?v=474j-n1Ltxc&t=398s)** correlation, if any, between the size of PRs of humans were getting reverted versus size of PRs from agents that were being reverted. So this does not seem like actually very strong evidence that the human PRs are any better than the agent PRs. The second set of signals I started looking at was Graile comments. Now, now Grapple is reviewing all these poll requests and Graile finds P 0's, P1's, P2s across all these changes and it seemed reasonable that if Grapile was finding more bugs in the code that the code was most likely worse. So then I started tracking the counts of P 0, P1's and P2s in all these changes. And interestingly, once again, there was not that much of a difference. In fact, three out of the four agents that we tested performed better than humans in terms of the rate at which they were producing P 0. they were producing fewer P 0 than humans were. Similarly the case with P1's and P2s. Broadly speaking,

**[7:29](https://www.youtube.com/watch?v=474j-n1Ltxc&t=449s)** human generated PRs were about equal in quality to agent generated PRs based on this data. have the agent go and look at those comments, address them, and make a new commit on the pull request branch. That is the most common way to use guptile. And so it seems reasonable that if the pull requests were higher quality, it would require fewer iterations before they would be merged. And so I started tracking the number of iterations, the number of review rounds between when the poll request was opened and when it was merged. Sure enough, very little difference. Devon's PRs 2.1, Codex PR is 2.45, four, five number of review cycles to merge and humans right in the middle. Once again, very little if any statistical

**[8:17](https://www.youtube.com/watch?v=474j-n1Ltxc&t=497s)** difference between human generated and AI generated pull request in terms of how many iterations before they were ready to merge. So now that there wasn't any strong evidence that agent generated PRs were worse than human generated PRs, I got curious if there were qualitative differences. Maybe the types of ways in which agents failed were different from the types of ways that humans failed. And so then I looked at the corpus of reptiles comments. It makes on average about four comments per pull request. So we had this corpus of several million comments across the last several months. And so I started scanning them for specific phrases and words. For instance, SQL injection or N plus1 query. And I plotted the frequency with which these terms occur in graphile comments for these various agents. And so I made this chart of patterns of failure. To interpret this chart, you can assume

**[9:05](https://www.youtube.com/watch?v=474j-n1Ltxc&t=545s)** that 1x is the human propensity for producing that type of error across the entire chart. And you can kind of see that there's actually quite a lot of variation in the types of failures that these agents seem to produce. For instance, Claude is one and a half times more likely to produce a SQL injection error than humans. Devon is about half as likely as humans to produce a off bypass issue. I found it very interesting that there was this much variation in how these agents were performing and how different their failure modes were from humans. So it turns out that in spite of my initial skepticism around the enterprise usability of endto-end coding agents, the evidence seems to suggest that they're here and they probably can contribute in real meaningful ways to enterprise coding environments. And so

**[9:54](https://www.youtube.com/watch?v=474j-n1Ltxc&t=594s)** we started to think a little bit more about what code review would look like in such a world. Here's an interesting stat. Today, Graal is used by several tens of thousands of engineers every single week to review all of their code. So, we also know generally speaking the number of pull requests that each of these people are writing. The median grubile user writes 50 pull requests a month. So, call it about two plus per workday. The 90th percentile writes 500 poll requests per month. That is a drastic difference between the median and the P90. The P99 is in the thousands of pull requests. That is very interesting in its own sense because that means that the people on the margins are actually producing poll requests at the rate at which they're coming up with new ideas. And beyond being interesting, it also makes you wonder well there existing systems for validating this code which is manual code review of course testing maybe you

**[10:43](https://www.youtube.com/watch?v=474j-n1Ltxc&t=643s)** have a QA firm that you work with naturally can scale to that same degree. And at Grav, we decided to take sort of a first principles view at what really good validation could look like. Instead of saying that we wanted to automate QA or automate testing or automate code review, we took a step back and said, what would we need to do for anyone to be able to merge hundreds of pull requests a month in an enterprise environment where it really matters that the code is correct? What would need to happen between when the code was expressed into a pull request and when it was merged and deployed safely? We figured we only actually had to answer three questions. The first one is does this change violate the user contract? The second one, does it increase the propensity of a future violation of the user contract, whatever the user contract might be for that application? And third, does it fulfill the intent that the author described? Did the poll request do the thing that the author wanted to do? And so we started

**[11:32](https://www.youtube.com/watch?v=474j-n1Ltxc&t=692s)** approaching this problem from base ground level and said, okay, agents can probably figure out if something's going to violate the user contract and detect bugs. If you let it spin up the code in a sandbox, have it install the dependencies, mock the inputs, run the browser agents, you can probably start to discover most of the issues that could occur, you get a pretty high degree of confidence on merge. Today, almost a fifth of all the poll request or gravile reviews are merged without any human review or without any human testing, which I find very interesting and that is a number that we care a lot about and want to bring higher and higher, of course, within the guard rails of producing really high quality code. Thank you so much. My name is D, one of the co-founders of Graptile. We have a booth here which you should come to. And if you're interested in trying Graptile, you can find us at gretile.com and try

**[12:19](https://www.youtube.com/watch?v=474j-n1Ltxc&t=739s)** it today for free. And we'd love to hear your feedback. Thank you so much.
