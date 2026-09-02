---
id: BIBDhLDgMdE
title: "Srijith Rajamohan - Spec Driven Agents: Hierarchical Specs, Tooling, and Trajectory Based Evaluation"
slug: srijith-rajamohan-spec-driven-agents-hierarchical-specs
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Srijith Rajamohan"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-12T02:13:26Z
video_id: BIBDhLDgMdE
url: https://www.youtube.com/watch?v=BIBDhLDgMdE
youtube_url: https://www.youtube.com/watch?v=BIBDhLDgMdE
tags: []
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Srijith Rajamohan - Spec Driven Agents: Hierarchical Specs, Tooling, and Trajectory Based Evaluation

**Srijith Rajamohan**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=BIBDhLDgMdE) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,763 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=1s)** SRIJITH RAJAMOHAN: All right, good afternoon, everyone. My name is Srijith Rajamohan, and until recently, I had an AI research at Redis. And today, I wanted to talk a little bit about the diagnostic and remediation agent that we built for diagnosing issues with the Redis Query Engine. So we primarily built this as an agent to help our customer support agents with many of our customer queries. So Redis does provide a pretty rich suite of tools and pretty extensive documentation for these issues. What we really noticed is that at the end of the day, many of these complex queries get escalated all the way to the development team, which is, obviously, not conducive. So we built this to see if we can unblock many of them and reduce the time to solution for many of our customers. So what makes us challenging in particular

**[0:51](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=51s)** is that unlike something like SQL, the parametric knowledge within an LLM is pretty limited. And we see that it gets wrong quite often. And some of these queries are pretty context-dependent anyway, where the agent must know what's actually missing from a query. So we had to build this spectrum of an agent with skills and tools that goes through this clarify, diagnose, confirm loop in order to make this more reliable. So some of the things that we learned in doing this is that evaluating the final result is often pretty insufficient. How you get there or the trajectories matter quite a lot. And obviously, correctness is pretty important, but so is consistency. I like to say that the only thing worse than a system that doesn't work is something that just works occasionally.

**[1:38](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=98s)** So this is something we really want to avoid. And lastly, inefficient trajectories are obviously expensive. One of the things that we learned the hard way is that these are also pretty error-prone downstream as well, because of the length or context exhaustion as well. Obviously, using a more frontier model or more capable model will resolve some of these issues would actually move the needle for us was actually restructuring some of this knowledge and how agents access information. So essentially, we wanted to make sure that we provide sufficient information, that it knows how to identify and access information and when to use it. So a couple of things I actually want to call out here is these are some of the failure modes that we saw, when we're building these agents. And I classify into four buckets, roughly. The first three, correctness, completeness, and usefulness

**[2:27](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=147s)** relates to the final results, and efficiency relates to the trajectory. Correctness is pretty obvious. Obviously, if your result is wrong, that's a problem. It can stem from a number of reasons, such as paths being wrong. It reads symmetric incorrectly, and so on. So these are just hallucinations. Completeness, this is when it diagnoses only part of the issue and leaves the others unresolved, which is a pretty commonly occurring issue that we've seen. So usefulness actually falls into two buckets. The first one is when actually gives you plenty of information, actually, too much information, or very generic information to the point that it's really not actionable for the user. It's just overwhelmed with information. And the second one that was actually pretty interesting for us is when

**[3:13](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=193s)** it provides information or advice that violates semantic intent. For example, telling a user, who asks why my query is slow, to reduce the number of search terms is technically correct, but it doesn't actually serve the purpose at all. The last one has to do with efficiency, when the agent actually has repeated reads, backtracking, or does dead end searches, thereby resulting in wasted tokens. But also, as I mentioned earlier, one of the things we noticed that this also affected accuracy negatively as well. And most of these things can only be resolved by looking at the trajectory they don't show up in the final result alone. So we addressed this in two ways or two dimensions. The first one was, can we actually take a look at the tool architecture, and what can we do there?

**[4:03](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=243s)** So there are two things that we actually did here was, primarily, can we split up the tools into two categories of setup tools and discretionary tools. So setup tools are always called at startup, as opposed to discretionary tools, as the name indicates are called by the model, based on the problem that you're solving. So a way to think about it is if you're starting on a new role, you might go through an onboarding process, where they teach you what's happening there, who's doing what, who to talk to, and so on. So you can think of it that way, where the setup tools provide enough context for an agent, so it knows how to proceed correctly and use the discretionary tools correctly, and it knows when to use it correctly. The second one was actually how we organize our knowledge base. Obviously, you can use the raw documents by themselves, but we saw better performance when

**[4:53](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=293s)** we reorganized this into what we called a diagnostic playbook. This is nothing but a router, plus a set of handbooks. And you can think of the router as-- I've shown a small structure or snippet here is you have symptoms, and you have a problem type associated with that symptom, en route to a handbook or a set of handbooks. So users don't come to you with saying, I have a certain symptom. They have concerns. It's the agent's job to actually map the concern to a symptom or set of symptoms. Our job is to make it easy for the agent to do that. So that's what this serves. And in order to understand the effect of these interventions, we study these separately. So we learned in doing this-- so we tested over a number of data sets is we measured the end to end latency, but we also looked at the number of tool calls

**[5:42](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=342s)** and the quality of the results. So the first one was a baseline setup, which was automatically generated a set of tools. We noticed that it didn't exactly perform as expected. It was slow, and the quality of results were actually pretty debatable. The last two, I call minimal and full, they were actually generated by domain knowledge that were informed by our domain knowledge of how readers query engine works. So the difference between minimal and full is that full is a superset of all the tools you might find in minimal. So way to think about it is if you have a tool such as get start info, and you want to find out what the slowest start is, you might have to call that, and then perform some processing on top of it, as opposed to full, which might have getchar info and get slow start. So you just simply have to call it.

**[6:31](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=391s)** Interestingly enough, that one did not perform any better. In fact, it was slower, and the quality was just marginally worse. So this goes to show that tool overload is very much a real thing. And more importantly, what I'd call tool orthogonality or separability is pretty important. So at any point, if an agent is unable to determine, if I should call B or C, it's problematic. So with setup tools, we found out is that this is simply just minimal, except what we do is we move a subset of those tools into the startup time. So what happens there is, now, it only has to make a selection between a smaller set of tools, as it solves a problem. And here, what set of tools and minimal they perform pretty similarly 'till we took a closer look

**[7:20](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=440s)** or drill down into the trajectories themselves. So what's interesting here is that with minimum, with that set of tools, the trajectory is actually way more inconsistent. You have a lot more unique number of sequences. Obviously, not every unique sequence is an issue, but some of them can be problematic. The takeaway here is that reducing the number of variants-- reducing the decision making that an LLM has to make at any point reduces variance and also improves the consistency. And we were able to do this by providing a set of tools which force an onboarding context. The second dimension was actually organizing information to playbook. So how did that impact our results? So we organized this into two sets of buckets, roughly, which is the answer quality and the trajector

**[8:10](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=490s)** quality. So answer grounding and specificity relates to the final results. Whereas, first past success and dead end rates relate to the trajectory themselves. Across the board, we see improvement in performance, when we're actually using playbooks, as opposed to reading the raw guides. We also saw a 43% reduction in the total number of tokens, and a 48% reduction in the total error rate. If you look at the last row there, what's interesting is that it also enforces instruction, following a little better as well. The call out here is that reducing making it easier for it to actually access the information, not only reduce costs, but also reduce forgetfulness and thereby improved reliability.

**[8:59](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=539s)** So obviously, not everything is working as expected. There are things to be improved there. One of the things this is actually a prime candidate for are things recursive self-improvement, which has been a pretty common theme at the summit here, so we'll probably have to look into something like that to improve performance even further. But we do see a reduction in many of the common failure modes. And lastly, to wrap up, if I can leave you guys with any takeaways here, there are two things I want to call out is measure the trajectory, not just the final answer. Because many of the issues that we saw did not show up in the final result yet. We had to inspect the trajectories themselves. And if it is possible, structure the knowledge in a way that it's easy for an agent to identify and access. And take a look at your tooling to see what is mandatory baseline context versus what's

**[9:49](https://www.youtube.com/watch?v=BIBDhLDgMdE&t=589s)** discretionary or exploratory context. And the final thing I'll add is, if you can get to correctness, completeness, and usefulness of your result, and efficient trajectories, you're more likely to have production reliable agents. Thank you.
