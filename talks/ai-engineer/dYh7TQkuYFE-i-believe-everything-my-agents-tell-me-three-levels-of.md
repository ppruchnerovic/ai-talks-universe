---
id: dYh7TQkuYFE
title: "I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore"
slug: i-believe-everything-my-agents-tell-me-three-levels-of
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Corey Gallon"]
channel: "AI Engineer"
duration_min: 12
published_at: 2026-10-13T12:00:08Z
video_id: dYh7TQkuYFE
url: https://www.youtube.com/watch?v=dYh7TQkuYFE
youtube_url: https://www.youtube.com/watch?v=dYh7TQkuYFE
tags: ["AIE NYC 2026", "Leadership", "Livestream Priority 08", "Online Talk"]
topics: ["Agents & orchestration"]
transcript: true
---

# I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore

**Corey Gallon**

`AI Engineer` · `AI Engineer` · `2026` · `12 min`

`#AIE NYC 2026` `#Leadership` `#Livestream Priority 08` `#Online Talk`

[Watch the recording](https://www.youtube.com/watch?v=dYh7TQkuYFE) · [Conference site](https://www.ai.engineer/)

## Description

A demand letter passed its drafting agent's own checks, yet two independent reviewer agents found that the supposedly expired contract had renewed less than three weeks earlier. Sending it could have left the business owing thousands of dollars. Corey Gallon uses that case to explain a three level review method for agents that overstate completed work, misread facts or draw the wrong conclusions. His analysis of his own 2026 sessions found a consequential error in about four out of ten sessions; that is a description of his sample, not an error rate for all agents or for the final reviewed outputs.

Level one requires a verified artifact with a fingerprint, or an explicit account of what is missing. Level two has independent agents extract the same material against a control total, then settles every difference against the source. For a year of scanned accounting statements, that process found 56 differences and produced records that balanced to the penny. Level three combines a self audit, cold reviewer agents with reasons to challenge the work and fresh reviewers for the revision. A memory leak investigation exposed a flawed reproduction and an overstated fix before the maintainer merged the corrected change. Gallon reports the time and token costs for these cases and releases the method as agent skills. The evidence supports a concrete checking workflow, rather than a guarantee that review eliminates every error.

Speaker info:
- https://www.linkedin.com/in/coreygallon/
- https://gallon.me/i-believe-everything-my-agents-tell-me
- https://github.com/captivus/agent-review

Timestamps:
00:00 - Three recurring agent failure modes
1:22 - Level one: verify the deliverable
2:03 - Level two: independent extraction and source checks
2:44 - Level three: adversarial and fresh review
4:02 - A memory leak and an overstated fix
6:57 - Accounting that balances to the penny
8:53 - A demand letter and a missed renewal
11:35 - Packaging the review method as agent skills

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*1,878 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=0s)** I believe everything my agents tell me. And yet, my agents get things wrong all the time. I've put over 107 billion tokens through agents this year. So, I analyzed my agent sessions from 2026 year-to-date to see where they went wrong. In about four in 10 sessions, an agent got something wrong that mattered. That's how often agents get things wrong in the first place. It isn't how often those errors made it into work outputs. Catching those errors before they reach me is the job of the agent-based review method that I've been running for most of this year, and that's the method that I'm sharing with you today. This analysis identified three ways agents keep failing. Number one, they overstate what they did. That is, they say it's done or

**[0:49](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=49s)** checked when it isn't. Number two, they get the facts wrong. They misread the source, for example. Or number three, they get the reasoning wrong. So, the facts are right, but the conclusion isn't. The method is comprised of three levels of review, one to address each of the three ways that agents keep failing. I built each level as an agent skill. Here's how each one works, and then I'll show you how each was applied in three real cases. Level one prevents agents overstating what they did. Before an agent starts, the job spells out exactly what it has to hand back. The file, where it goes, and a command that checks it.

**[1:36](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=96s)** It points out the shortcuts agents have taken before, so this one doesn't repeat them. The agent performing the review has to end its review with one of two things. Artifact verified with a fingerprint of the file or files documenting its work, or artifact missing with the reason. Then, the agent that sent the job runs the check itself. Saying done on its own isn't a permissible answer. Level two prevents agents from getting the facts wrong. When correctness matters, first find something in the source that the answer has to agree with. Then, two agents get an identical set of instructions and do the same job independently. Neither one sees the other's work. Each one notes where every fact came

**[2:25](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=145s)** from and checks its result against the facts. Then, a third agent with the original source in front of it compares the work of the two independent agents line by line and settles every difference by going back to the source. It never forces a match. Level three prevents agents getting the reasoning wrong. When clarity of thought really matters, we perform adversarial review in three stages. First, the agent audits its own work. It lists every claim it's making and marks each one as measured, checked against the source, inferred, or assumed. Anything it can't back up gets tested or labeled as a guess. Second, reviewers with none of the

**[3:14](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=194s)** original agent's context, each acting as a persona with reasons to find fault, read it cold. Each one plays a real reader and gets the work and the sources, but no history, no drafts, and no conclusions to agree with. Their findings get checked against the source, too, before anything changes. Third, once the work is revised, brand new reviewers who've never seen it check the final version. Each level adds to the one before as the stakes go up. In these cases, each review took minutes, not hours, and the agents do the checking, not me. At the scale we operate, checking it myself isn't an option. So, let's see each review level applied in three real cases.

**[4:03](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=243s)** First, a memory leak. An open-source dictation app I use was leaking memory. It grew to 9 GB. We set out to find the leak, fix it, and get the fix accepted by the project's maintainer. And to fix it, we had to find out what was really causing it. My agents and I went after it, and three times an agent told me something that wasn't true. First, a sub-agent I sent to measure the leak with one tool used another and reported its work as done without saying it hadn't used the tool as instructed. Nobody caught it at first, including the agent that dispatched the work. It came out when I questioned the results. The file the right tool would have produced didn't exist, and nobody had noticed.

**[4:52](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=292s)** That's what level one of the review is for. In this case, we dispatched a sub-agent to build a specially instrumented version of the app and capture telemetry while it was running. However, the build failed. Because we instructed the sub-agent to provide documentation of all of its work, instead of just done, it said the main deliverable wasn't delivered and explained why. It reported that an artifact was missing, the software build, and that there were 25 compiler [clears throat] errors, and it correctly labeled the what it could deliver as partial. Dispatching the sub-agent with level one review tasking included took 19 minutes and about 16 million tokens. The other two significant inaccuracies by agents were about to go public,

**[5:39](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=339s)** and the stakes were higher, so for those we borrowed from level three, reviewers with none of the agents' context. We'll see all three stages of a level three review in the last example I explain shortly, but here's how it worked for the memory leak fix. In the second case, an agent blamed the wrong code. To find the leak source, it wrote a small test that used the same library the app does. The test leaked, too, so it concluded that the library was to blame. It said, "This is solid enough to file." Reviewers reproduced the test and found that it had skipped an important step that the library requires. Used properly, the library didn't leak. The problem was in how the app used the library. In the third significant error by agents working on the memory leak,

**[6:28](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=388s)** the agent wrote up our fix for the pull request and said that it eliminated the leak completely, but it had measured the leak in a way that missed most of it. Reviewers caught that, also. The fix reduced the leak, but it didn't fully eliminate it. So, the pull request went up with honest numbers, and the maintainer accepted the fix and merged it. Each of these level three reviews took about 15 minutes and, together, cost about 6 million tokens. For the next example, we'll look at portfolio company accounting. Buying and building businesses can be messy. For one of our portfolio companies, we needed a year of scanned statements from a source accounting system turned into a complete, accurate record of every business transaction for financial reporting purposes. An agent extracted the year and handed

**[7:16](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=436s)** it back with, "Hey, I recommend spot-checking a few of these transactions." This put the burden of reviewing the agent's work back on us, which is a non-starter. Extracting data from scans often goes wrong in ways that are tedious and difficult to detect. Transactions are missed entirely, transactions are put in the wrong months, or they're recorded with the wrong details. One agent simply reporting done can't tell you whether any of that's happened. And that's what level two of the review method is for. Here, we use the balance printed on the statements as the control total for each month. Two agents extracted every month independently, and each one went back to the statements until every month balanced.

**[8:04](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=484s)** Then, a third agent compared the two extractions line by line and settled each difference against the statements themselves. Finally, two more agents, tasked identically, checked each of the final transaction records before they were accepted. This fan-out, fan-in pattern of identically tasked agents is highly effective in driving accuracy and reliability. When we ran this level two review, we caught missed transactions, incorrect transactions, and transactions in the wrong months. Comparing the two extractions caught 56 differences in descriptions, dates, and notes. But, ultimately, the whole year balanced to the penny. This entire review took about 20 minutes and cost 7.5 million tokens.

**[8:53](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=533s)** Last, the highest-stakes example. More messy portfolio company business here. One of ours was in a billing dispute with a vendor, and this amounted to thousands of dollars with legal implications. We needed to send a demand letter clearly stating our position and requirements, and every claim in it had to stand up against the contract and each invoice. An agent drafted the letter on the premise that the vendor's contract had expired. Anything with legal or financial stakes gets a level three review before it goes out, and here's how level three ran on this letter. First, the self-audit. The agent checked the claims in the letter against the contract and the invoices, including the dates, and reported them verified. Stage one passed.

**[9:42](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=582s)** Second, cold reviewers, each in a role with a reason to find fault, so in this case our own litigator, the vendor's counsel, and an auditor who trusts none of the numbers. They each got the letter, the contract, and the invoices, and nothing else. The auditor recomputed the financial demand from the invoices, and it was correct down to the cent. But both lawyers independently found something buried deep in the contract's fine print. A three-year auto-renewal clause. The contract had auto-renewed less than three weeks earlier. The letter's demands would have had us walking away from a contract that was still in force and owing the vendor thousands of dollars for leaving early. The two lawyer agents also learned that, while revising, the original agent had

**[10:31](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=631s)** even deleted a line that had the renewal correctly identified. The original agent's own check had agreed with its own error. Just the sort of thing this review method is designed to catch. Our litigator's verdict, though, was do not send the letter. That three-part cold review process took 15 minutes and cost 13 million tokens. So, the letter was rewritten and handed to the third stage of level three review. Brand new reviewers who'd never seen it checked the final version. The flawed version never went out. So, that's three review stories and three levels of review. An agent that couldn't build a customized version of the app said so instead of incorrectly saying that it was done.

**[11:18](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=678s)** Two groups of two agents extracted and accounted for a year of business transactions down to the penny. And cold persona-based reviewers with none of the original agent's context revised a letter that the drafting agents' own check had called verified. I've packaged the three review levels as agent skills, and I've released them as open source. The write-up is at gallon.me. Point your agent at the write-up, and it will know how to check its own work using this review method, so you can rely on it. To learn more of the best ways to do real work with AI agents, subscribe to my newsletter and connect with me here. So, I believe everything my agents tell me. Not because they're right. They get things wrong all the time.

**[12:05](https://www.youtube.com/watch?v=dYh7TQkuYFE&t=725s)** I believe them because everything I rely on has been thoroughly reviewed and validated first. And most importantly, not by me.
