---
id: BT1Mo-fD-g0
title: "Your Coding Agent Can't Undo Its Own Mistakes - Tanmay Sah & Dolly Sah"
slug: your-coding-agent-can-t-undo-its-own-mistakes-tanmay-sah
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Tanmay Sah", "Dolly Sah"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-11-08T08:00:03Z
video_id: BT1Mo-fD-g0
url: https://www.youtube.com/watch?v=BT1Mo-fD-g0
youtube_url: https://www.youtube.com/watch?v=BT1Mo-fD-g0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Tanmay Sah", "Dolly Sah", "coding agents", "AI agents", "agent reliability", "undo", "recovery", "UndoBench", "EvoUndo", "AI safety", "AI research", "AI Engineer", "AIE CODE"]
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# Your Coding Agent Can't Undo Its Own Mistakes - Tanmay Sah & Dolly Sah

**Tanmay Sah, Dolly Sah**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Tanmay Sah` `#Dolly Sah` `#coding agents` `#AI agents` `#agent reliability` `#undo` `#recovery` `#UndoBench` `#EvoUndo` `#AI safety` `#AI research` `#AI Engineer` `#AIE CODE`

[Watch the recording](https://www.youtube.com/watch?v=BT1Mo-fD-g0) · [Conference site](https://www.ai.engineer/)

## Description

Tanmay Sah and Dolly Sah look at a capability today's coding agents are missing: undoing what they've done. Drawing on their research projects UndoBench and EvoUndo, they show that an agent that completes a task can't necessarily put things back when something breaks, because Git doesn't cover external API calls, runtime config or notifications, and retrying doesn't reverse side effects. In EvoUndo, 197 of 478 changes that made an agent more capable (about 42%) also broke its ability to recover. They lay out an approach that captures the original state, picks the right response (retry, restore, compensate or escalate) and independently verifies the result.

Tanmay Sah

Dolly Sah

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*1,933 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=1s)** Hi everyone. I am Tanmay. Today joining me is Dolly and we will be presenting the missing undo button for coding agents. So, imagine a coding agent working on a repository issue. It applies patch, runs the tests, and everything passes. It even creates a release tag, but then a downstream integration fails. Now, here is the question. Can the agent actually get everything back to the estate it was in before? So, Git can tell us what changed in the repository, but what about changes outside Git, such as external API calls,

**[0:52](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=52s)** or runtime configurations, or notifications? And simply retrying an operation does not necessarily undo what already happened. So, we wanted to understand not just whether agents can complete tasks, but whether they can recover when something goes wrong. This brings us to our first research work, Undo Bench. We wanted to investigate whether an agent's ability to complete a task also translates into its ability to recover from failure. We evaluated agents across 2,880 paired trials,

**[1:43](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=103s)** comparing normal execution with execution under an injected failure. So, under normal conditions, the agent achieved an 84%success rate, but when we introduced failures, only 47%of the normally successful trials recovered successfully. Notice that these two percentage do have different denominators, but yeah, so even when an agent uh can complete a task successfully, recovery remains a significant challenge. Now, let's look at a specific failure scenario. Imagine a coding agent sending a request to an external system to

**[2:31](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=151s)** create a ticket. The request has been sent and the agent is waiting for a response. Next, the server receives the request and successfully creates ticket number 781, but the acknowledgement gets lost on its way to the agent. From the agent's perspective, the request has timed out, but the agent does not know that that ticket has already been created. A timeout tells us that the response didn't arrive, not that the operation failed. So, the agent tries the request without checking whether the whether the first operation committed.

**[3:20](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=200s)** And now we have two tickets even though the agent intended to create only one. So, in Undo Bench, naive retries produced duplicate effects in 54%of these kind of trials. That's why we need to distinguish a failed response from a failed operations. Now, the failure phase also changes the answer. What do I mean is that recovery also depends on when the failure happens. Before the mutation, retrying is generally safe because nothing has changed. But, during the mutation, the

**[4:10](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=250s)** system has maybe partially modified, so we need to inspect its estate. And after the mutation, the operation may have committed even if the acknowledgement was lost. As we just saw, retrying could create duplicates. So, we need different recovery strategies depending on the failure phase. Now, why can't we just use Git revert? So, Git can restore repository changes, but coding agents also modify their runtime state, including tool registries,

**[4:58](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=298s)** middleware, and configurations. They can also trigger external effects such as deployment or database writes. So, Git revert does not reverse all these changes. The recovery mechanism has to match the type of effect the agent created. And this becomes particularly important when coding agents start modifying their own execution environment, or what we call the agent hardness. This includes prompts tools middleware event listeners, resources, and routing configurations. Such changes may improve the agent's

**[5:46](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=346s)** performance, but they can also make recovery more difficult. In other words, an agent can become more capable while becoming less recoverable. And that's why And that's why undo needs more than an inverse command. Uh now, uh like undoing a change is not always as simple as reversing a command. Suppose an agent changes a timeout from 30 to 60. To undo that change, it needs to know that the original value was 30. That's why Evo undo captures a pre-state witness before applying the mutation.

**[6:36](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=396s)** And that witness provides the information to restore the original uh state and later verify that uh verify that recovery actually worked. Now, question comes, how often uh do improved hardnesses fail? So, in Evo undo, we evaluated 600 evolution tasks. Out of those, 478 produced capability improvements, but 197 of those improvements had recovery defects. That is around 42%of the capability positive cases. So, here key takeaway is that a mutation can improve an agent's capability and still

**[7:27](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=447s)** leave the system unable to recover reliably. Now, now we can say that why please fix the undo did not work. So, naturally, we wanted to use prompting and wanted to tell agent that, "Hey, could you simply repair all these recovery failures?" So, we tested four verifier-guided repair strategies, but under the original recovery language, none recovered the 197 naturally occurring failures. The problem was not necessarily the agent's reasoning. In some cases, the agent lacked precise information about the original state. In

**[8:17](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=497s)** uh in others, the recovery language could not express the operation needed to reverse the chain. So, we investigated these two limitations separately. So, two bottlenecks. First is state grounding and another one is recovery expressivity. The when we provided like precise information about what had changed and where, then recovery improved from 0 to 38 out of 48 cases. And the second is recovery expressivity. So, when we introduce richer and do operation, recovery improved significantly from 0 to 142 out of 143

**[9:07](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=547s)** cases. So, these results come from the two different experimental subgroups, but together they show why recovery needs both accurate state information and ability to perform the required undo operation. Now, question comes to our mind that can better undo mechanism rescue failed mutations. So, what happens like when we give the agent better recovery capabilities? So, with the original recovery language, none of the 197 recovery defective mutations could be restored, but after extending the recovery language, we successfully

**[9:55](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=595s)** recovered 180 out of 197 cases. That is around 92%. As a result, the number of admissible improvement increased from 281 to 461 out of 600 tasks. That is a 30 percentage point improvement and that brings us to the next question. How do we build these recovery checks into the agent's evolution process? I will now hand it over to Dolly to walk through the Evo and do algorithm. >> All right. Thanks, Tanmay. Uh so, let's get into the working on how Evo and do actually works. So, first we will start with the agent pro uh first

**[10:46](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=646s)** the agent will start. The agent pro- processes the mutation on which state it is currently in along with the effect contract and the recovery plan. And before applying the mutation, we capture the state witness representing the original state. And even before that, the then attesting in the testing environment, agent will apply the mutation and execute the recovery plan. Uh an independent verifier will also verify the original uh if verify to check if the original state has been restored or not. If the mutation improves uh the capability based on the user-defined criteria and passes the recovery um check, the agents admit the changes. Otherwise, well,

**[11:36](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=696s)** uh the agent attempt to repair, or the verifier itself rejects the mutation altogether. This way, the recoverability becomes a part of the admission decision rather than something that we strategize on even plan once we are uh deployed the deployed the AI agent. Okay, so with thanks. Next, we will walk through as as Tanmay have already explained in an given an example. Let Let me walk through how the ex-uh how that example of a time or changing from 30 to 60 would look like in action. So, let's take Let's start with the original state, a simple example that simple example of our agent having the time value of 30. Before changing anything, the Evo undo

**[12:25](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=745s)** would first read the original value. And then it will save the it will capture the original value as a state witness. We know exact We So, we know exactly what need to be restored when when an when if we have to restore it, we would know what what need to be restored or which state would be the true state to return back to. Now, the agent So, next comes the mutation. Now, the agent changes the time out from 30 to 60 as we want it to do. And if recovery is required if recovery is required, the undo uses the saved witness to restore the time out to 60. Now, independently the verifier finally independent verifier would also confirm that the

**[13:11](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=791s)** recovered value matches the original value. So, the recovery isn't considered successful simply because an undo command was run, but also the verifier would verify the resulting state to make sure that we are in fact doing the recovery those in the state we want it to be. Well, now comes the bigger question. So, So, we have this capability of recovery in our arsenal. Should we be using it for uniformly and applying the recovery mechanism to all the failures? Well, of course not. Not every failures can be recovered the same way. If nothing has changed, then the then simply if if nothing has changed in the in the system, we would simply want it to

**[14:00](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=840s)** recover we would simply want it to safely retry. We would want the agent to simply retry if and try to achieve the state that we want to be. However, if we have the original state Uh, we have the original state, we can restore it if the external action has already been committed and we need uh, it's then when we would need a compensation mechanism, compensation action to compensating action to reverse its effect. And if we cannot recover the recovery uh, and we cannot if and if we cannot the cannot verify that recovery is safe or the verify have rejected the recovery, then the agent should stop and escalate.

**[14:46](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=886s)** The right response definitely depends on what actually happened and what we what can be safely reversed or not. That brings me to the almost the last slide, which is about bringing everything together on our two paper undo bench and Evo undo. The so the key takeaways here's are first, the engine undo bench shows the successful task execution. Uh, the undo bench shows that the successful task execution doesn't guarantee doesn't always guarantee the successful recovery of it. Uh, secondly, the Evo undo algorithm provides a structured process, capture the original state, apply the mutation, recover independently verify and restoration. So it the Evo undo

**[15:35](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=935s)** algorithm does work in the in the fashion in the way we intended it to. And third, we should admit self-evolution changes only when the when both the capability and the recoverability requirements are met. So, ultimately, as we give agents more autonomy, we should also give them more reliable ways to recover from their actions. All right. So, uh, finally, I hope you remember the agent from the beginning. It was looking for an undo button. Well, now it has one. We have started building this capability through our research project Evo undo. And you can explore the world through the in in the GitHub repository. You can scan the QR code on the screen to get to the page. Our goal is to make the recovery a

**[16:23](https://www.youtube.com/watch?v=BT1Mo-fD-g0&t=983s)** fundamental capability of AI agents so that we not only have agent does not even does not only execute the action but also recover when something goes wrong as well. Thank you so much.
