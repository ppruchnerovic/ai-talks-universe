---
id: HWR6cE_hynM
title: "Keynote: The Boring Seams"
slug: keynote-the-boring-seams
conference: sans-ai-summit
conference_name: "SANS AI Cybersecurity Summit"
category: "AI security"
edition: "AI Cybersecurity Summit 2026"
year: 2026
speakers: []
channel: "SANS Institute"
duration_min: 24
published_at: 2026-05-04T18:47:58Z
video_id: HWR6cE_hynM
url: https://www.youtube.com/watch?v=HWR6cE_hynM
youtube_url: https://www.youtube.com/watch?v=HWR6cE_hynM
tags: ["sans institute", "information security", "cyber security", "cybersecurity", "information security training", "cybersecurity training", "cyber security training"]
transcript: true
---

# Keynote: The Boring Seams

**Speaker not identified**

`SANS AI Cybersecurity Summit` · `AI Cybersecurity Summit 2026` · `2026` · `24 min`

`#sans institute` `#information security` `#cyber security` `#cybersecurity` `#information security training` `#cybersecurity training` `#cyber security training`

[Watch the recording](https://www.youtube.com/watch?v=HWR6cE_hynM) · [Conference site](https://www.sans.org/cyber-security-summit/)

## Description

Keynote: The Boring Seams

🎙️ Julie Davila, Vice President of Product Security at GitLab
📍 Presented at SANS AI Cybersecurity Summit 2026

The industry is fixated on the model. Jailbreaking it, guarding it, aligning it. But the most consequential AI security vulnerabilities aren't in the AI. They reside in the orchestration layer: serialization boundaries, state management, credential stores, and trust boundaries between agents. Old bug classes, new topology.

Julie Davila (VP of Product Security, GitLab) opens with a confession: her own team found two critical RCEs in GitLab's AI agent platform, one before and one after general availability. Neither was caused by prompt injection. Both lived in the plumbing. From there, she traces the same structural pattern across LangChain, MCP tooling, and cross-platform agent integrations, and borrows an idea from early twentieth-century mathematics to explain why this class of failure keeps showing up, why most security teams haven't threat-modeled the layer that produces it, and what to do about it on Monday.

Explore upcoming SANS Summits to continue learning from leading voices in cybersecurity: https://go.sans.org/summits

## Transcript

*2,764 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=HWR6cE_hynM&t=2s)** Good morning. Thank you, Rob. Thank you to the organizers. Thanks to the AV team. Um I'm glad to be here. Um as he said, I'm Julie Davila. I currently lead product security at GitLab. Before that, I've held a number of different roles across infrastructure engineering, software engineering, ran an automation practice for a little bit at Red Hat, and even ran my own tech startup for a couple of years, also in the security space. But the thing that has shaped the way I view security more than any job title is something that stems from a side interest of mine. And actually has nothing to do with technology. I've spent a lot of time studying permaculture. How ecosystems sustain themselves. How soil health determines everything

**[0:52](https://www.youtube.com/watch?v=HWR6cE_hynM&t=52s)** above it, even though nobody photographs the soil. In permaculture, there is a principle, use edges and value the marginal. You can imagine the boundary between a forest and a meadow, the shoreline between the water and land. This is where the most activity happens. Where all the growth occurs. But it's also where the system is most vulnerable. And it's this framing that has really influenced how I view security today. Because I think the most interesting security problems aren't in the components that everyone's watching.

**[1:40](https://www.youtube.com/watch?v=HWR6cE_hynM&t=100s)** It's in the seams between them. And that's what this talk is about. And I want to start with something that actually happened. A few weeks before going generally available with GitLab's Geo agent platform, we found a pickle deserialization RCE um in our systems. We hardened the serializer. We blocked the fallback paths. Closed the ticket. It was good work. It was thorough. But then, a few weeks after we launched in January, the same thing. Same surface. Same layer. But a different attack surface. This is the platform that I'm

**[2:30](https://www.youtube.com/watch?v=HWR6cE_hynM&t=150s)** responsible for security. But neither incident had anything to do with the model. There was no prompt injection. There was no jailbreak. The models did exactly what they were supposed to do. The deserialization path didn't care. And what bothers me the most about these two incidents isn't that they happened. It's that they represent a broader a broader trend that I've been observing in our industry. For the past 2 years or so, the security community has built tools, frameworks, and threat models, all largely oriented around what the model outputs. And it's true

**[3:28](https://www.youtube.com/watch?v=HWR6cE_hynM&t=208s)** that model security is important. Prompt injection is real. Jailbreaks are real. And in recent recent history, the research community has made significant, impressive strides to bring us collectively forward across these problem domains. But look at what the field has actually built in that time. Red teaming frameworks pointed out what the model outputs. OWASP categories organized around what the model says, what it reveals, how it can be manipulated, the vendors, the certifications, the conference tracks, all oriented around the most visible, most discussed part of the stack.

**[4:17](https://www.youtube.com/watch?v=HWR6cE_hynM&t=257s)** The new and unknown one. And this work is important. It really is, and I believe this room and the folks listening online understand this better than most. From 2017 to 2022, research into AI safety grew by over 300%, a number that only keeps growing. In the history of computing, no other attack surface has garnered this much academic attention in such a constrained time frame. But the challenge with all of this is that when it comes to complex systems, failures rarely occur where you're watching. They occur in the seams between the

**[5:05](https://www.youtube.com/watch?v=HWR6cE_hynM&t=305s)** components. And the orchestration layers that often wrap the models that we've all grown accustomed to often times haven't been through a single threat model. I want to take a little bit of a detour and take us back to the early 20th century when physics was at a really interesting place. It was a little bit chaotic. There were really brilliant people and amazing discoveries made at the time. There was also a growing list of conservation laws that nobody could quite fully explain. You have things like energy is conserved, momentum is conserved. Angular momentum is conserved. But nobody could quite explain how all

**[5:53](https://www.youtube.com/watch?v=HWR6cE_hynM&t=353s)** of these things were connected or how to determine whether a given quantity would be conserved at all. But then Emmy Noether, working out of Göttingen at a time where she couldn't even lecture under her own name, made a discovery that changed the foundations of physics forever. She couldn't hold a formal title, but she published her proof anyway. Every symmetry in a system corresponds to a conserved quantity. I'll explain this. It's a little bit simpler than it sounds. If I were to pick up a ball here today and drop it, and then drop it again tomorrow, the same thing will happen. The physics doesn't care what day it is. This indifference is the symmetry. It's what guarantees that energy will be

**[6:43](https://www.youtube.com/watch?v=HWR6cE_hynM&t=403s)** conserved. If I roll the ball across the stage here or I roll it across the stage in Tokyo, same thing. The physics doesn't care where where you are. So, what Noether proved was that anytime the rules are indifferent to something, there will be a quantity that is guaranteed to be conserved. So, what this means is that if you can identify the symmetry in a system, you can generally, with pretty high degree of accuracy, predict what that system will conserve, even in systems that nobody has studied yet. I want to propose that the same kind of thing holds true in security. Whenever untrusted data crosses into a

**[7:32](https://www.youtube.com/watch?v=HWR6cE_hynM&t=452s)** privileged execution boundary, the same class of failure will be preserved across frameworks, across organizations, different years, every time, same outcome. AI security is in pre-Newtonian physics right now. We've all spent a lot of time documenting our own set of conservation laws, some in this conference this week. But, what we haven't really paid attention to is the symmetry that produces all of them. And that symmetry exists. We just haven't named it yet. Let me show you what I mean.

**[8:19](https://www.youtube.com/watch?v=HWR6cE_hynM&t=499s)** The orchestration layer is something that exists on most architecture diagrams. It's usually a box with some arrows pointing to the model and everything the model touches. Whether you build this orchestration layer yourself because you're at GitLab or something like this, or you get it through the platform you've procured. That box is actually a cross-system trust broker. It oftentimes holds credentials to your CI pipeline. It usually has access to your source code and also your IDE connections. It inherits the trust boundary of every system that connects to it. And the security posture of the system oftentimes reflects how it was drawn, as plumbing, not as a boundary worth hardening.

**[9:09](https://www.youtube.com/watch?v=HWR6cE_hynM&t=549s)** This trust broker in GitLab is a dual workflow service. It is a Python and LangGraph LangGraph-based service that sits at the heart of our um AI engine. It manages agent state. It orchestrates agents. It passes credentials from the execution side and maintains communication with developer workstations over long-running persistent connections. Compromise at this layer is in getting chatbot to say something it shouldn't. It's a compromise of every agent that connects to it. The first vulnerability had to do with how agents resume their work. So, if you have an agent and it needs to

**[9:58](https://www.youtube.com/watch?v=HWR6cE_hynM&t=598s)** execute a multi-step workflow, a very important piece of functionality is that agent's ability to be able to save where it's at and then be able to pick up where it left off whenever the workflow resumes. And that is the deserialization process. The LangChain library we were using had a custom deserializer, which would allow for arbitrary method calls via JSON with a fallback to pickle. So, we replaced the deserializer with a hardened one. We created an explicit allow list of permitted types with no fallback paths. And we even submitted a patch upstream to LangChain to ensure the fix was present in the library for everybody

**[10:45](https://www.youtube.com/watch?v=HWR6cE_hynM&t=645s)** that used it going forward. Then, a few weeks after we launched in January, same thing. This time it was in our template rendering pipeline. User-supplied content would go into the templating engine. This Jinja 2 that was getting processed. And the deserialization mechanism could be triggered on user-supplied checkpoint data, which could then lead to code execution. Think about that for a moment. Checkpoint data as an attack surface. And this is simply a piece of data that tells the agent where to pick up its work that it left off. This time the fix wasn't in the median

**[11:35](https://www.youtube.com/watch?v=HWR6cE_hynM&t=695s)** patch upstream to a library. It was a process-wide ban on unpickling combined with a hardened template sandbox that would prevent callable methods from the template context objects from being executed. We went from fixing a surface to banning the mechanism. That escalation is the lesson. And this pattern isn't unique to GitLab. All across the AI landscape the structural relationship between privileged execution boundaries and untrusted data is everywhere. One example is LangChain Core which dealt with its own critical

**[12:22](https://www.youtube.com/watch?v=HWR6cE_hynM&t=742s)** severity CVE which allowed for attacker-influenced model to steer an AI agent into executing a malicious payload which when deserialized could lead to the leakage of environment variables and in some cases um code execution. The failure mode was in an output field of the model. But the true failure was in the serialization underneath. MCP MCP remote another critical flaw. And this is a proxy service that allows AI applications to communicate with remote MCP servers. The way it works during its authorization process is it'll take

**[13:10](https://www.youtube.com/watch?v=HWR6cE_hynM&t=790s)** server-provided URLs and pass them through to operating system commands. All you had to do was point this at a malicious server with a specially crafted authorization endpoint and you could effectively own every machine that connect to it. This is the of vulnerability that could lead to the full system compromise of a connecting machine. And it was in a proxy that hardly anybody was looking. Then you have MCP Inspector. Anthropic's own developer tool for testing MCP servers. Also critical. In fact, it was a tool used by many to check the security of their own servers and it itself became the attack surface. And across all of these incidents, both

**[14:01](https://www.youtube.com/watch?v=HWR6cE_hynM&t=841s)** internal external, the cellular motive is the same. Different companies, different frameworks, same outcome. And each one of these was a different team. Each one of these happened during a different time of the year. But they all shared the same thing in common. The models did exactly what they were told. And that's the problem. They were following instructions from a system without ever without ever verifying where the instructions came from. And they all made the same implicit assumption, or bet, if you will, that the seam in between the model and the system didn't need the same amount of vetting as the model itself.

**[14:52](https://www.youtube.com/watch?v=HWR6cE_hynM&t=892s)** And if your organization doesn't build the orchestration layer, cuz that's not your bread and butter, and you use something like Claude, Copilot, N8N, or some other managed service, that orchestration layer still exists. You just don't own it. It's written in somebody else's service, somebody else's trust boundaries, but with your data. No true would recognize this immediately. The symmetry is there. It's the same structural relationship between untrusted data and privileged execution boundaries. The conservation law holds. Anytime there is symmetry in a system,

**[15:42](https://www.youtube.com/watch?v=HWR6cE_hynM&t=942s)** the failure modes are what's being conserved. So, why is this orchestration layer so often overlooked by security teams? I want to posit that there's three high-level reasons. And they compound. The first one is that the most brittle code in an organization is often not where your security investment is. I'll give you an example. At GitLab, our primary application is a Ruby on Rails monolith with over a decade of security investment behind it. The processes, the tools, the scanners. Combine that with the institutional knowledge of thousands of engineers. The new stack,

**[16:32](https://www.youtube.com/watch?v=HWR6cE_hynM&t=992s)** Python, LangChain Jinja2 different framework, different language ecosystem. And every organization building AI agents today has a similar type of system with similar types of gaps. The second challenge is that behavior is not in code. It's in data. System prompts are stored in the database. Tool configurations live in JSON. And you cannot grep for behavior the same way that you grep a controller. The attack surface of a of the orchestration layer is a function of what it accepts and what it executes.

**[17:20](https://www.youtube.com/watch?v=HWR6cE_hynM&t=1040s)** Not method signatures, not lines of code. Traditional code review security review wouldn't catch this. It's the third one that keeps me up at night. And it's not a vulnerability. It's a visibility problem. Your logging probably wasn't built for the way agents operate. With persistent connections with how they resume the work off of checkpoint data. And our own incidents during incident response we observed the gap in the telemetry we could observe and the telemetry we actually had. That itself became its own work stream. It's been a long ongoing project.

**[18:12](https://www.youtube.com/watch?v=HWR6cE_hynM&t=1092s)** And something I want to make clear is that the absence of evidence in your logs is not the evidence of absence. If your telemetry architecture was built for a world of web applications and APIs it probably wasn't built for the access patterns of agents. The seams are where your logging stops. Noether didn't set out to prove or to explain any particular particular conservation law. She sought to explain the pattern that connect connected all of them. And she found it. The structural symmetry of a system dictates what's conserved.

**[19:03](https://www.youtube.com/watch?v=HWR6cE_hynM&t=1143s)** Break the symmetry and the conservation law changes. Oh, want to propose the same playbook, the same idea, but apply it to security. Not Not because this is simple. It isn't. But because across all of um all of the incidents that I described today, the same patterns hold. We're going to walk through them. The first one is to take a look at serialization services. Every time where untrusted data becomes a privileged object. These are your checkpoint data stores, your tool outputs. The second are the trust assumptions

**[19:52](https://www.youtube.com/watch?v=HWR6cE_hynM&t=1192s)** between components. What does your orchestrator trust without verifying? The authorization gap we found in our own platform where the scope and permissions implied by the UI didn't quite match up to what we found in the back end. Wasn't a flaw introduced by any one person intentionally. It was due to a result of unchecked assumptions. Undeclared trust assumptions are the most dangerous kind. Because they don't show up in your traditional security review. They show up in the seams. Token scope versus the user mental model.

**[20:39](https://www.youtube.com/watch?v=HWR6cE_hynM&t=1239s)** What do your users think they're authorizing? And what are you actually granting them? Divergence between these two at scale is a confused deputy problem with an AI sized blast radius. Telemetry coverage versus attack surface. Where can an attacker move that your logging can't see? Every high performance agent that trades standard HTTP or long running persistent connections needs purpose-built telemetry to get the same level of visibility. You should find the gaps before somebody else does. So, we have four symmetries for conserved risks. So, what what should you do about this

**[21:30](https://www.youtube.com/watch?v=HWR6cE_hynM&t=1290s)** when you get back to work, whether it's Monday or later on this week? Map your orchestration layer before you need to. Every service that manages agent state. Every place that checkpoint data stored. Your template rendering pipelines. Diagram them. And then ask two questions. Which of these have been threat modeled? And which of these fall outside of your standard security pipeline? You can't answer the question or the answer is unsatisfactory, that's where you start. Second, treat serialization like your perimeter used to be. The old faulty assumption was to trust the network inside the

**[22:17](https://www.youtube.com/watch?v=HWR6cE_hynM&t=1337s)** firewall. The new faulty assumption is to trust what the database hands you. The framework defaults. The checkpoint data. And second, fix the class, not the instance. We first replaced the serializer before realizing we needed to fix the templating engine underneath it. The fix that mattered was the fix that asked, "What is the mechanism that causes this, and how do we remove it wholesale from the underlying system?" >> And I want to propose

**[23:08](https://www.youtube.com/watch?v=HWR6cE_hynM&t=1388s)** that we all stop fixating on the shine on the shiny AI and instead audit the plumbing. If you're working on problems similar to this, have faced similar challenges in your org, or just kind of want to nerd out, I'm happy to chat. Come find me. Thank you.
