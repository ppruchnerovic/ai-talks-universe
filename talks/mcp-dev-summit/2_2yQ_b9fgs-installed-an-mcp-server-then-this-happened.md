---
id: 2_2yQ_b9fgs
title: "Installed an MCP Server... Then This Happened"
slug: installed-an-mcp-server-then-this-happened
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 11
published_at: 2026-06-02T14:00:06Z
video_id: 2_2yQ_b9fgs
url: https://www.youtube.com/watch?v=2_2yQ_b9fgs
youtube_url: https://www.youtube.com/watch?v=2_2yQ_b9fgs
tags: []
transcript: true
---

# Installed an MCP Server... Then This Happened

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=2_2yQ_b9fgs) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Cecilia Liu is a product manager at Docker working on MCP Gateway. In this keynote she skips the architecture diagrams and walks through two real MCP horror stories: an intern who installed an unreviewed MCP server and leaked the codebase three weeks later, and a senior developer whose fully autonomous agent obediently wiped local branches and closed in-progress PRs on an approved GitHub MCP. Her point: this is already happening at scale, and the question is not if it happens at your org, but when, and whether you will know.

What you will learn in this keynote:

- Horror story one: The unauthorized MCP server. How a new hire self-serving a shady MCP from Google leads to a data leak with no audit trail, no review, and no way to investigate.
- Horror story two: The obedient autonomous agent. An approved GitHub MCP plus a fully autonomous agent equals merged PRs, deleted branches, and lost local work. Nothing malicious happened, and everything was permitted.
- The four questions every org needs to answer: What is allowed, who is doing what, what is flowing through, and what happened.
- The three essentials for closing the gap: A control plane (MCP Gateway), an OS-level sandbox, and a deployment model that fits the stack you already run.
- What an MCP Gateway actually does: Curated catalog as the entry point, authentication and secret handling at the perimeter, fine-grained policy and access control per team or agent, and full audit logging.
- Why the gateway is not enough: It controls what the agent is allowed to call, not what the agent will do. Agents are non-deterministic, and governance has to extend below the application layer.
- How the sandbox closes the loop: Each agent gets its own container, the whole stack runs inside a microVM with its own kernel and hypervisor isolation, and file-system and network limits are enforced at the OS level.
- The Nanoclaw collaboration: Why a security-first personal AI framework uses Docker sandboxes, and the founder's line that security must be enforced outside the agentic surface, not by trusting the agent to behave.
- Deployment that meets you where you are: Local or remote, Azure AD or Okta for identity, AWS Secrets Manager for secrets, Splunk or Datadog for observability, single-cloud or multi-cloud, on-prem or air-gapped via a single Helm install.

Who this is for: Platform and security leads rolling out MCP across a real organization, MCP server authors who care about how their servers get governed, and anyone who has watched an agent do exactly what it was told and wished it had asked first.

Links and Resources:
- Docker MCP Gateway open source repo: https://github.com/docker/mcp-gateway
- Docker MCP Gateway docs: https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/
- Docker MCP Catalog: https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/
- Docker MCP Gateway launch post: https://www.docker.com/blog/docker-mcp-gateway-secure-infrastructure-for-agentic-ai/
- MCP Horror Stories series: https://www.docker.com/blog/mcp-security-issues-threatening-ai-infrastructure/
- MCP Horror Stories, Supply Chain Attack (CVE-2025-6514): https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/
- MCP Horror Stories, GitHub Prompt Injection: https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/
- Docker and E2B collaboration on trusted AI: https://www.docker.com/blog/docker-e2b-building-the-future-of-trusted-ai/
- Agentic AI Foundation: https://agenticaifoundation.org/

Timestamps:
00:00 - Intro: Cecilia Liu, PM on Docker MCP Gateway
00:30 - Horror story one: The intern, the unauthorized MCP server, and the data leak
01:50 - Horror story two: The autonomous agent that deleted the repo
03:00 - This is happening at scale: Four questions every org needs to answer
04:20 - The three essentials: Control plane, sandbox, easy deploy
04:37 - MCP Gateway as the control layer
04:50 - Curated catalog: Blocking the random server at step zero
05:53 - Authentication, policy management, fine-grained access control
06:42 - Audit logging: Who did what, what policies fired, what flowed through
07:00 - Why the gateway is not enough on its own
07:34 - Sandboxing as a capability ceiling at the OS level
08:28 - Two hard walls: Per-agent containers inside a microVM
08:57 - Nanoclaw: Security enforced outside the agentic surface
09:29 - Deployment that adapts to your environment, not the other way around
10:06 - Identity providers, secret managers, observability, and your cloud
10:45 - Recap and the three essentials to solve your horror stories
11:00 - Find Docker at their booth

## Transcript

*1,709 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=0s)** Hello everyone. Thanks Angie. Um, I'm Cecilia. I'm a product manager at Docker. I don't have a fancy technical title like any anyone else in the room. So, instead of talking architectural diagrams or sharing like different concepts, today I'm going to talk through some horror stories. Um, so again, I'm Cecilia. I'm a product manager working on MCP Gateway. So, because of that, I spend a lot of time thinking about what happens when agents go wrong. And actually Docker has published a series blogs on it. We called it MCP horror stories. And I'm going to share it to you today. The first horror story is about an unauthorized server. So, it starts with an intern at a startup. The intern just joins the company

**[0:48](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=48s)** um, and really wanted to get productive quickly. Naturally, like they just go to the AI agent and go online to find MCP servers, anything that could help with their productivity. Um, the intern just search with Google and finds an MCP server that seems pretty legit. It has all the readmes and everything. So, then it just install it and start using it. Everything seems pretty smooth, but in the process, there's no review, no one approved it, no one know it even exist. So, what happens in 3 weeks? The security team discovers a data leak. Uh, code base, API secrets, everything at risk. So, the data team just discovers this data leak, but it doesn't know what happens

**[1:38](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=98s)** exactly because there was never an audit log, nothing to investigate. Nobody knows. The second story starts in a much safer place. So, this is about a larger company that already know that MCP server needs to be regulated. Um, so they have a list of approved MCV server. So we have an experienced developer and as using an approved MCV server say like GitHub and then it tells the agent to clean up the repo for them. However, this developer is a strong believer of a fully autonomous agent. So it lets the agent execute everything without confirming. So the agent just gets a list of approved tools and start to plan his execution and emerge all the

**[2:27](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=147s)** open PRs, delete branches, close issues and in like a few minutes the dev go check out the results of the agent and realize everything is gone. The working progress PR that they that was in the local never push it and never save it in the cloud disappeared and branches deleted. Nothing malicious really happened with the agent's execution. Everything was permitted, but it doesn't mean that everything is intended. So I didn't tell these horror stories just to scare everyone this early in the morning for people coming from the West Coast. I'm telling this because this is actually happening at scale. How many developers today in the

**[3:14](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=194s)** organization is using AI? The answer is no longer like dozens. It's going to be hundreds and thousands or even more and the number keeps growing. So the question is not if this security leak will happen, the question is really when this will happen and when this happens if you will know about it. But the good news is all of these are preventable. So you just have to answer four questions for your organization. What is allowed? So which MCV servers, which tools are allowed? Who is doing what? Which user is calling what MCV server, what tool from what from what client at what time. What is flowing through? So, whether whether credential is leaking or flowing through your model contacts. And then

**[4:02](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=242s)** lastly, what happened? Whether you have a track record of everything that we just described. And a lot of organization doesn't have answers to those four questions, and that's the gap. And if you want to resolve this gap, close the gap, it's also very easy. So, I just pointed out three essentials, a control layer, a sandbox, and a very easy way to deploy the two of them. I'm going to talk through these two these three things one by one. So, first, you will need to have a control layer. That's what we call MCP gateway. MCP gateway is a layer that sits between your AI agents and your MCP servers. Everything has to flow through it. So, that that makes governance really

**[4:50](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=290s)** possible. Remember the horror story number one that unauthorized server, this can be easily solved if you have a curated catalog for organization. So, if you look to the left the right hand side, um organization defines your curated catalog, picks the servers. This includes your custom tools that's only available in the organization. You can also mix match with the available tools that you can find in the market, but the trusted one, third party ones. Docker also has a curated catalog for for organization to choose and mix match. So, once you have a curated catalog, you you combine it with the MCP gateway. Any MCP server that doesn't exist in the catalog, the MCP gateway just blocks it. So, the random server

**[5:37](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=337s)** that intern finds, it just stops at step zero. It will never happen because the gateway blocks it. It's just as simple as that. Um And having a curated catalog is just a first step. It's just an entry point to the gateway. The MCP gateway does way more than that. Um so, it handles authentication for you um for all your secrets flowing through, um it will never reach the MCP server. Everything stays within your perimeter. It also handles policy management and access control. Those two things come hand in hand. Um if your organization has a curated catalog, it only is a blank statement saying your developer has this list of tools. Um but, what you can do with policy management and access control is that you can provide

**[6:25](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=385s)** fine-grained control and saying that you can give this set of tools to your developers and that set of tools to, let's say, like your HR department and any other user groups. You can even define policies on uh specific agents or sessions. And lastly, you would need um the gateway handles audit logging. So, that includes everything, a track record of who did who did what, what policies get triggered um what are allowed or what is flowing through. Um so, that is the gateway. Um it controls visibility. It provides controls and visibility. A lot of people stops at this step um and thinking that with the gateway everything is safe. But, I would tell you it's not um because the gateway controls what the agent is allowed to

**[7:13](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=433s)** call, but it doesn't control is what the agent will do. We all know that agents is kind of like have their own minds. It's like a different person. Um it's pretty non-deterministic in one way or another. Um I'm not going to solve the determinist non-deterministic problem for you, but I think we can ground the agents in a way that with sandboxes. So, Docker sandboxes are in general um sandboxes is a capability ceiling that defines what the agent can do the maximum of what the agents can do. Um, how it works is that, um, a sandbox defines, uh, controls file systems and network access. It's not at a policy level, but at OS level, um, below application

**[8:02](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=482s)** layer. So, if a sandbox say, um, "I don't I don't want write access for my file system at this directory." The MCP server just cannot access it. The agent just cannot access it. Cannot delete the file. Um, so that what that's what makes a double layer sandbox plus MCP server gateway um really reliable. So, in practice, this means two hard walls. One is that we're running agents in two in different containers. So, each agent will have its own container, own file system. Um, each agent will have no access to other sessions, no access to other hosts, um, to the host. And then there is a Docker sandbox running in a micro VM um contains all the containers. And the

**[8:49](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=529s)** micro VM has its own, um, kernel, has its own, um, own hypervisor isolation. Um, this is also what, uh, our partner Nanocloud, which is a personal AI framework that is designed security as the first principle, um, uses Docker to to to implement their their security principle. So, as the founder of Nanocloud said, security has to be enforced outside of the agentic surface, not depending on the agent behaving correctly. And then lastly, what I just described needs to be very easy to deploy and operationalize. Um, so for a lot of organization, the governance stops if you want to um,

**[9:38](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=578s)** throw away your existing text tag or do everything from scratch. This is not the solution that you'll be looking for. The solution you've been looking for is not asking you to adapt to that solution. The solution is to adapt to your environment. So, you'll be looking for something that works in your environment whether you want to run it local or run it at a remote environment, it should work. It also will work with your text tag. For MCP, you'll be thinking about identity provider like Azure AD or Octa. You'll be thinking about secret manager, AWS secret manager, and whatever that you're using. You'll be thinking about your observability stack. Your dashboard is that Splunk or Data Dog still work if you want to integrate MCP audit logging. And lastly, it works in your

**[10:26](https://www.youtube.com/watch?v=2_2yQ_b9fgs&t=626s)** cloud. It works with your workload. So, if you want to bring your own cloud, you want to do it on prem, uh air gap, with one home and so on, you should be able to install everything. Whether single cloud, multi cloud, your infrastructure, your choice. So, that's what I wanted to cover. Just to recap, three essentials. You need MCP gateway, you need a sandbox, and then the easy way to deploy it. If any of these resonate, you want to solve all your horror stories, come find us at Docker's booth. I'm happy to talk to you in more detail. Thank you. >> [applause]
