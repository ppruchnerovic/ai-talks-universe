---
id: n-F_-8n2PIU
title: "Lovedeep Gondara - Trustworthy Agentic AI in Regulated Domains: Robustness, Privacy, and Accountabil"
slug: lovedeep-gondara-trustworthy-agentic-ai-in-regulated
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Lovedeep Gondara"]
channel: "Berkeley RDI"
duration_min: 9
published_at: 2026-08-12T06:42:02Z
video_id: n-F_-8n2PIU
url: https://www.youtube.com/watch?v=n-F_-8n2PIU
youtube_url: https://www.youtube.com/watch?v=n-F_-8n2PIU
tags: []
topics: ["Agents & orchestration", "Governance, ethics & regulation"]
transcript: true
---

# Lovedeep Gondara - Trustworthy Agentic AI in Regulated Domains: Robustness, Privacy, and Accountabil

**Lovedeep Gondara**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=n-F_-8n2PIU) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,285 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=2s)** LOVEDEEP GONDARA: Thanks, everyone, and good morning. So today I'm going to talk about trustworthiness in agentic AI systems. What makes the systems trustworthy? What are some of the properties we want in those systems? And how often some of the properties can be in conflict with each other? So I want you to remember this code, "A model that hallucinates our recommendation is a nuisance. An agent that acts on it is a liability." This is the core thesis of this talk. And this is what I'm going to talk about during most of this presentation. So how did we get here? So on one hand, we have classical machine

**[0:51](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=51s)** learning methods where the output of the model can be a probability, can be a rank, can be a label. What is something that can go wrong in that case? We might get a wrong label, we might have some error in predicted probability, or we might get wrong ranking. We do have a chance to interrupt the model flow and to intervene. After that we have LLMs. The output from LLM is some unstructured text. What can go wrong in that case? We might get some hallucination. We might get wrong information. But then again, we do have the opportunity to detect and correct. And then on the other side, we have agents. With agents, if they are autonomous,

**[1:41](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=101s)** running by themselves, we don't have that luxury to detect and to correct. What can go wrong in that case? I would say sky is the limit. It can be anything from a wrong entry in your calendar to a wiped inbox to a deleted production database. So what makes agent failure is different from the other failure modes that we usually encounter for standalone models, for standalone LLMs. I have six here. But for the interest of time, I'm only going to cover a few. The first one is compounding error. So let's assume we have some long horizon agent that needs to take a bunch of steps to reach its goal. And let's say the first step accuracy is 95%.

**[2:33](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=153s)** In that case, of course, I'm assuming a few things here. In that case, after 10 steps, that accuracy can drop to less than 60%. The second one we have indirect prompt injection. And what do I mean by that, and how it is different than prompt injection with LLMs? When agents are working in an autonomous environment, the tool calls or the results of the tool calls can embed some malicious instructions, and those outputs then become inputs to agents. Similarly, any other content that the agents might be retrieving there can be malicious instructions and that can lead to indirect prompt injection. Goal drift. Again, a long horizon agents often they will decompose their task, their final goal,

**[3:23](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=203s)** into smaller subtasks. And if the agents start to optimize for those smaller subtasks, they can end up getting misaligned from the final goal. Inter-agent manipulation and agent collusion as a whole. As far as research goes, it's a very interesting research area. Just studying these dynamics in a multi-agent system. But I would say when it comes to production, this is something that we need to take seriously where a malicious agent can if, depending on how it is orchestrated, it can convince other agents to do its bidding. Unauthorized tool invocation. Again, when we are designing autonomous systems, what we want to do is we want to design the schemas

**[4:13](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=253s)** in a flexible fashion, whether it be tool calling or it is communicating. And those flexible schemas make auditing harder. And it can also lead to malicious behavior that we don't want. So what do we actually want in an agentic system to make it trustworthy? At a very high level, we want three properties. So we want robustness. And by robustness I mean that our agents should be able to work on long-horizon tasks reducing the error that we talked about. We want privacy. Often, the agents running in our environment are interacting with sensitive private data. So we want the privacy of that data to be preserved.

**[5:03](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=303s)** We want accountability. And by accountability, I mean we should be able to audit the actions of the agents. Because if we cannot audit the chain of actions that led to a certain outcome, we have failed. So now let's talk about how the properties that we want in the agents can be at conflict with each other. And this is what makes these multi-agent systems different from standalone models because the properties that we want in silo for models interact with each other in a multi-agent system. The first one is privacy and auditability. So for us to be able to audit a multi-agent system, we want detailed logs.

**[5:55](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=355s)** But if we are keeping detailed logs, those detailed logs can expose the very information we want to protect. Autonomy and accountability. Autonomous, by the definition, means that the agents should be able to go and do whatever they are doing by themselves without us interrupting. But then who's accountable? To assign accountability or to even have any accountability in there, we need human in the loop. We need some steps where humans can intervene and that reduces autonomy. Similarly, robustness and autonomy. In order for us to build robust systems, we should be able to halt an agent that is either drifting or that is not performing the actions that we wanted to.

**[6:46](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=406s)** But then again, if we are halting, we are reducing autonomy. But if we want robustness, we have to do that. So I hope you get the idea where I'm trying to get at where these contentions are. So where does that lead us? So this slide is very similar to a slide that Vincent presented yesterday. And talking with quite a few folks, I have seen we are all thinking about agent autonomy in a very similar way as we think about self-driving cars. And that's very natural, because at the end of the day, when we talk about autonomy, we think about similar autonomy levels. So for agents, on one hand, we have level 0, where AI only advises. And us as humans then decide if we want to take that advice or if we want to act on that advice.

**[7:38](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=458s)** And then on the opposite side, we have fully autonomous systems where we only observe the output, nothing else. So our research question at a high level for me is not how we make everything more autonomous, how we move everything towards L4. To me, more interesting research question is how we make level 2 and level 3 work for us better? How we make sure that level 2 and level 3 systems are useful, safe, and provably compliant so we can take off as much work as we can from our plate, but at the same time, we can still make sure that whatever is deployed is trustworthy? So at the end, I want to leave you

**[8:25](https://www.youtube.com/watch?v=n-F_-8n2PIU&t=505s)** with two key takeaways from this talk. First one is a regulated domains like finance and health care. They expose some failure modes that are unique to those domains and are also unique to a genetic systems. And the second is that trustworthiness in agentic AI systems. We have to think of it as a systems property, not as a standalone model property, because as we have seen, a lot of those properties often interact and contradict each other. So we have to make sure that when we design these systems, we design keeping all that in mind. And with that, thank you very much. [APPLAUSE]
