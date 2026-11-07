---
id: _0SQh8a1Osk
title: "Don't Vibe Code Your Agent Infrastructure - Akshat Bubna, Modal"
slug: don-t-vibe-code-your-agent-infrastructure-akshat-bubna-modal
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Akshat Bubna"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-11-07T20:00:13Z
video_id: _0SQh8a1Osk
url: https://www.youtube.com/watch?v=_0SQh8a1Osk
youtube_url: https://www.youtube.com/watch?v=_0SQh8a1Osk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Akshat Bubna", "Modal", "AI agents", "sandboxes", "agent infrastructure", "cloud computing", "GPUs", "serverless", "AI security", "observability", "Ramp", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# Don't Vibe Code Your Agent Infrastructure - Akshat Bubna, Modal

**Akshat Bubna**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Akshat Bubna` `#Modal` `#AI agents` `#sandboxes` `#agent infrastructure` `#cloud computing` `#GPUs` `#serverless` `#AI security` `#observability` `#Ramp` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=_0SQh8a1Osk) · [Conference site](https://www.ai.engineer/)

## Description

Akshat Bubna, CTO of Modal, explains what AI agents actually need from the infrastructure underneath them, starting with a spreadsheet where every cell is backed by its own agent. He walks through the building blocks: a workspace for each agent, state that persists for days without paying for idle compute, resources that stretch and shrink as the agent works, GPUs on demand, shared file systems for agents that collaborate, network controls that keep credentials and data from leaking, and observability agents can read themselves. He makes the case against vibe coding your own sandbox platform, shares what scale looks like today, and describes where agent infrastructure is heading.

Chapters:
0:00 Intro
0:24 Every spreadsheet cell backed by an agent
1:33 What that architecture needs
3:15 What is Modal?
4:03 Agents need a workspace
5:03 Workspaces that persist
6:21 Agents need elastic resources
7:41 Agents need GPUs
9:02 Agents collaborating through shared files
9:57 Keeping agents from leaking data
11:20 Observability for agents
12:12 Why not to vibe code a sandbox platform
13:31 What scale looks like
14:54 Separating the brain from the hands
15:37 From pets to cattle to microbes

Akshat Bubna

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,705 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=12s)** Hey everyone. I'm Akshat, CTO of Modal. And I'm going to talk about what do agents really need from their infrastructure? So I'm told this audience is very finance adjacent. So I thought I'd talk about what if every cell in a spreadsheet could be backed by an agent? And imagine your a financial analyst at a fund. You want to run complex analysis on every company in your portfolio. Normally in the past this would take days. You'd have to connect every portfolio company, look at their data sources,

**[0:59](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=59s)** run some Python for each of them. And now obviously with agents this should be much easier. Well, actually one of our customers Heavy AI built something that's exactly this. You can go in right now in their product, you can you have a spreadsheet and you can run a query where literally every cell is backed by a different agent. And I wanted to talk about what does building this really look like? Well, first every agent is backed by a Modal sandbox. So sandbox is a secure environment for running untrusted code.

**[1:48](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=108s)** And it used to be that every sandbox was one-to-one with a container or micro VM. That's actually no longer the case. Today actually uh, has this, uh, feature where you can run multiple containers or micro VMs inside a sandbox. And you actually need to do that for doing something like this, where, um, in this architecture, you run the harness. Uh, the harness is the agent loop that does things like running the calling the Modal API for inference, uh, running the tool calls, and then looping over it. Uh, you want to separate that from the place where the tool calls actually run. Uh, for security and isolation and a bunch of other things. Uh, so you have the sandbox that's

**[2:35](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=155s)** running multiple containers, including a sidecar. Uh, you also want shared storage, uh, because you want your agents to be able to talk to each other. And it's up to you how you uh, stripe it. Like maybe you have every row uh, gets the same volume, and agents in that row in the spreadsheet can collaborate. Uh, and you also want to share storage between your main container and the sidecar for some cases. And finally, you need all of this to spin up really, really fast, because your spreadsheet can have lots of cells. If someone has a query, you want to launch thousands of agents, and then you want to spin them back down when it's over. So, before I talk more about, uh, that, uh, just wanted to take a quick aside to talk about what is Modal. Uh, Modal is a platform of primitives

**[3:25](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=205s)** that is built for AI applications. Uh, so we've basically built this platform for, uh, from scratch. We've built our own file systems and scheduling and, uh, the runtime, uh, to give you really great performance and dev ex for use cases like inference, including LM inference, sandboxes training and uh functions running a lot of batch processing and whatnot. Uh, and today in particular, I'm going to talk about sandboxes, what this primitive is, and how it's evolving. Uh, so if you want to build something like this, uh, or even further, and we'll talk more about what that means, uh, what are the primitives you need for that? So, the first thing is if you're building an agent, you need a workspace. And I have some examples from some of our current customers. Uh, you might have heard of Ramp

**[4:12](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=252s)** Inspect. Uh, Ramp Inspect is uh, Ramp's internal coding agent that, uh, I think at this point, pushes almost every single PR at Ramp. Uh, and if you're building a coding agent, you need your, uh, repo, uh, your GitHub repo. You need your dependencies. You need your dev services all in the same workspace, uh, for each agent. Uh, another example is Basis. They're an uh accounting agent. And if you're building that, you need your, uh, documents. You need your accounting work papers. You need scripts you've written, uh, all in one work workspace. Uh, and we have another, uh, very interesting company. They're game dev company. And if you're doing game dev with agents, you need your game engine. You need your assets, uh, all in

**[5:01](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=301s)** one place. The next step is you need these workspaces to persist. Uh, so going back to the accounting example with Basis, what it looks like is your documents might arrive. Your, uh, agent is then triggered to work on them. But then it's waiting for a response from the accountant. And you don't know how long this could take. Could take many days. Uh, when the accountant responds, you want the agent to start up again and continue from that last place where things were left off. Uh, so you want to persist the state over time, uh, potentially indefinitely. But you don't want to run the compute the entire time because compute is expensive. So, um, you only want compute to run when the agent is actually

**[5:50](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=350s)** working. Uh, this is something we support in Modal, and we've realized that there's a bunch of different flavors of persistence that people need. Uh, sometimes you might want to snapshot your whole root file system. Uh, sometimes you might want to snapshot just a single directory. And uh, maybe it's like your node modules folder. But then you want to upgrade your base image over time. And sometimes you might need something that looks more like shared file system like a volume. A very interesting thing that's been showing up is agents actually need a lot of elasticity in resource consumption. So we got permission from Ramp to share some of the data from Ramp Inspect. And if you look at random sandboxes running

**[6:38](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=398s)** in their workload, they actually all have a huge amount of variance both >> [snorts] >> versus each other but also over time within the same sandbox for how much CPU and memory the agent is using. And it makes sense. I mean, what if you're compiling something that's very resource-intensive or doing some analysis needs a lot of memory. Your usage is going to change. And in the second chart, you can see peak usage for each sandbox. And there's definitely some consistent trends but it's all over the place. So if you were provisioning this for the peak, you would end up provisioning like 15 CPU cores and 15 gigs of RAM for every sandbox, which is just doesn't make sense economically.

**[7:26](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=446s)** And something we've worked on a lot in Modal is letting users basically not have to request these resources up front and then reliably get them when the sandbox needs them and only pay for them for for that duration. The other interesting emerging thing is agents need a lot more interesting compute. Like they need GPUs over time, they might need TPUs, AMD, who knows. And great example of this is Cloud Science where Cloud Science actually ships with a Modal integration out of the box. And the way it's used is when Cloud needs to do some intensive compute like pre-process some data on CPUs or spin up GPUs for running a scientific model, it will offload that to a model

**[8:15](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=495s)** sandbox. And we're seeing this show up in things like game design, video editing, 3D dev, like CAD, all of those things need GPUs for your agent. And of course, the the thing that everyone's really excited about right now is RSI or recursive self-improvement. And that's something that GPU sandboxes are really good at and agents are really good at using them. So we have this blog post about what happens when you give an agent sandboxes to hill climb over training a model. And it turns out they're very good. They can swap GPUs, they can run ablations in parallel, run lots of experiments, and then really get to the target very quickly. The next emerging thing is agents are

**[9:05](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=545s)** collaborating a lot more. And that means that you share a file system with your sub-agent, you share file systems and files with your human where you're all collaborating with the same thing. And this needs file systems that are fast, have consistency, and dev acts you can reason about. Something we're working on with model volumes. Related thing is we're seeing a lot more self-improvement. So agents will save and update memory, they'll run background tasks, which is now called dreaming, to update this memory over time. And actually, this also just looks like files in a file system. But again, you want really good performance from this file system.

**[9:57](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=597s)** And the scary thing about agents is they can mess up and they don't really know when they might leak your sensitive data to a German forum or something. So you need to have a lot of control over what they can and cannot do. Uh and you need things like controlling what IPs can even talk to the agent, how do you authenticate it? Uh what domains can it talk to? Uh and also if you're using credentials for talking to services, um basically you want to inject them in a way that the agent cannot actually see them and then exfiltrate them somewhere later. And the interesting evolution of this is we've realized that domain uh related allow lists are actually uh not enough.

**[10:46](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=646s)** You uh a lot of our users actually want very specific control over even like what paths can I talk to uh on let's say DataDog or GitHub. Like maybe I want to reason about specific operations that the agent is doing. And going back to sidecars, we've seen this emerging as a pattern where users actually write their own lightweight proxy that has custom rules about what exactly it can do. And Ramp is another example of uh company that's been using this successfully. Uh and the final underrated thing is it's really important to have really great observability. Uh so, going back to the example of auto research and an agent doing a lot of training, uh what happens when the training run fails? Uh you're you want your agent to

**[11:35](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=695s)** be able to easily look at the logs of the failure, uh reason about what happened, and do another iteration with uh different set of parameters. And while training is running, you want it to be able to look at the metrics. You want to look at GPU utilization and make sure it's not stalled. Uh maybe you want to look at the budget and make sure you're not spending too much in your sandbox. Uh and obviously all of this is really important for humans, uh but as agents are driving a lot more compute, uh it's we're spending a lot of time exposing all of this to the agents themselves so they can reason about all of this. All right. I think uh we know what we need. Why don't we have Astra build us an agent platform? Well, I don't think it's a good idea. I don't think you should vibe code a

**[12:23](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=743s)** sandbox platform. And there's three main reasons for that. Number one is reliability. I think we're all painfully aware how hard it is to get right. Certain websites we use every day keep going down. And the reason for that is even with AI, it's actually really hard to reason about the feedback loop of like what happens in the case of this tail event when the system breaks. And this is why you need to be very careful in building systems. Security is another one. You could vibe code a sandbox platform, but who is going to do all the work to like continually reason about the security boundaries and make sure it's defensible in in an age when everything is evolving very fast.

**[13:10](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=790s)** And finally scale. We have a blog post about how we scale to a million sandboxes, which involves a lot of very interesting engineering design and reasoning about systems. And this is again something that you kind of don't want to leave up to a vibe coded platform because when you get to scale, you want it to work. And on that point, we're we're actually seeing massive scale for for a lot of things I mentioned. So, for example, for the snapshots I mentioned uh it's growing quite fast. We're seeing 20 million snapshots a week. We're processing about 8 petabytes of data a day for for each of these snapshots. And our users are creating almost 2.6 million volumes a week. And all of this is growing super fast.

**[14:00](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=840s)** And just to take a customer workload for personal assistant, you need to create 10,000 sandboxes a second. You need to run um almost a million sandboxes. And they're They're going to last very long. They'll just last for like two or three minutes. Uh but when they come up, you want them to be interactive in in less than a second. That's that's what this workload really demands. And the other interesting thing on scale is you actually cannot get all of the scale from a single cloud platform. The world is actually getting crunched on CPUs as well, not just GPUs. Uh so one thing we spent a lot of time doing is actually aggregating cloud capacity from a bunch of hyper scalers and neo clouds. Uh so our users have access to CPU capacity across the

**[14:48](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=888s)** world when they need it. Uh but we cannot rely on one cloud provider to do that. Okay, so where is all this going? I I hinted at this earlier, but the harnesses are really good at making use of dynamic environments. And what this is leading to is a lot of separation of the brains, which is the harness, uh from the hands, which is the sandbox or the runtime where stuff is running. And um what this means, I have an example here, is the harnesses are going to be able to spin up environments based on what they need right now. They they they're good at snapshotting them and keeping them around for uh as artifacts that they need later. Uh and again, adjusting all of this as necessary.

**[15:37](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=937s)** So I I think this points at an interesting evolution of the pets to cattle uh analogy we're all familiar with. Uh to recap, in the olden days, uh people thought of services like pets. Uh each one was bespoke. You had to manage it. Uh you had to reason about this individual deployment uh specifically. Uh and then over time, it um with containerization and Kubernetes, uh people started to think about it as um homogeneous uh templates uh of uh these servers are all the same. You can scale them up and down. If one of them fails, it's It's an issue because our system can heal from that. And I think this is where a lot of people deploying agents are today. They're kind of using these homogeneous

**[16:25](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=985s)** environments and scaling up these agents. But but I think that's really limiting because the models are so good at reasoning about dynamic environments, snapshotting, uh creating lots of environments when needed, and working across them. Uh so what what does the new world look like? Uh one analogy here is it kind of looks like an ocean of microbes, of all these organisms that are self-evolving and working with each other. Uh and credit to Six for the analogy here. Um but one thing I'm really excited about is as you give agents these really rock-solid primitives for compute and storage and networking, they will be able to actually do a lot more um by doing the stuff I talked about, like spinning up

**[17:11](https://www.youtube.com/watch?v=_0SQh8a1Osk&t=1031s)** lots of environments, working with each other, and being very dynamic. So yeah, I and us at Model really think that great primitives let your agents do more. And uh yeah, if you're interested in talking about this more, reach out to us. Thank you.
