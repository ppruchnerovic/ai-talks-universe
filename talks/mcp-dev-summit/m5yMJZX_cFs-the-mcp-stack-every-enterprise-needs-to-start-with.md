---
id: m5yMJZX_cFs
title: "The MCP Stack Every Enterprise Needs to Start With"
slug: the-mcp-stack-every-enterprise-needs-to-start-with
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 10
published_at: 2026-04-13T23:19:13Z
video_id: m5yMJZX_cFs
youtube_url: https://www.youtube.com/watch?v=m5yMJZX_cFs
tags: ["Enterprise MCP", "MCP adoption", "MCP"]
transcript: true
---

# The MCP Stack Every Enterprise Needs to Start With

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `10 min`

`#Enterprise MCP` `#MCP adoption` `#MCP`

[Watch the recording](https://www.youtube.com/watch?v=m5yMJZX_cFs) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Keynote: Lessons Learned from Driving Enterprise MCP Adoption

**Sheng Liang, CEO of Obot AI and former founder of Rancher Labs (acquired by SUSE) and Cloud.com (acquired by Citrix), delivers a keynote on the lessons learned from driving Model Context Protocol adoption inside the enterprise.** In ten minutes he lays out the minimum viable stack every company needs to get started with MCP, and then shows why the architecture is already evolving past it.

- **The MCP starter kit:** why an MCP Gateway plus an MCP Registry are the two non-negotiable pieces of enterprise infrastructure
- **Ten months of MCP Dev Summit growth:** from 200 attendees and one track to a packed industry event
- **Agents are no longer SDKs:** how agent development shifted from RAG chatbots to workflow agents to code loops to skills libraries
- **The rise of the agent runtime:** why the SDK and framework layer is being replaced by MCP, CLIs, agentic browsers, and skills catalogs
- **Security and governance at the gateway layer:** secrets management, LLM gateway visibility, and software supply chain filtering
- **Why enterprise agents cannot run on your desktop:** the case for secure, isolated runtimes for third-party agents
- **Access control gets elevated:** how policy is moving out of the application layer (think Salesforce) and into the gateway layer for agent-era permissions
- **Where MCP gateways are heading:** skills, supply chain filtering, and unified catalogs beyond traditional registries

If you are an enterprise architect, platform engineer, or AI infrastructure leader trying to figure out how to deploy agents safely at scale, this keynote is your map.

LINKS AND RESOURCES
- Obot AI: https://obot.ai
- Introducing the Obot MCP Gateway: https://obot.ai/introducing-the-obot-mcp-gateway/
- Agentic AI Foundation: https://aaif.io
- Sheng Liang on LinkedIn: https://www.linkedin.com/in/shengliang

TIMESTAMPS (approximate, please adjust)
00:00 Ten months of the MCP Dev Summit
00:45 Following Amazon and Uber on stage
01:30 The two pieces every MCP beginner needs: gateway and registry
02:25 The MCP gateway vendor landscape
03:07 Where the architecture is heading next
03:40 How agents evolved: RAG, workflows, code loops, skills
05:01 SDKs and frameworks give way to MCP, CLIs, and agentic browsers
05:50 Security and governance as a new layer
06:25 Secrets management and software supply chain attacks
07:10 Why you do not want third-party agents on your desktop
08:09 Access control elevated from app layer to gateway layer
09:20 The expanded gateway: skills, supply chain, catalog
09:54 Wrap up and booth info

## Transcript

*1,601 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=0s)** So, I'm so excited to be here because it was it was just about this time last year Shannon and David uh uh uh uh uh had had the idea initially had the idea of having an MCP summit, dev summit. And it it it it took them like a little bit of a month. So, the summit really didn't happen until late May. So, we we we we we we we're we're just over 10 months from the first summit. And the first summit was was really cool. Uh it was small. It was like 200 people, one track. I know some of you were there. And one day and just look at how much this uh community has grown. It's it's so exciting. So, uh so it's also great to be following, you know, uh Amazon and uh

**[0:50](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=50s)** Uber, uh the the giants of our industry. And it's great to see they're adopting MCP. And as a startup, we help uh the rest of the enterprise and the startup ecosystem. So, some of our customers are, you know, financial institutions or reasonably sized companies. But many of folks we work with, they're literally just getting started in the AI and MCP and and agent journey as well. So, in many in many cases, MCP dev seems actually the first entry into uh their AI and agent journey. So, I really I love to I just have to thank uh the two engineers from Uber because uh uh they said exactly what I wanted to

**[1:38](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=98s)** say. Because I mean, for honestly, for those of you who are just starting you're in a you're in a business, you're just starting to look at MCP or agents, those are the two pieces of technology you got to think about. Um uh MCP gateway and an MCP registry, which is exactly what Uber did. And that's how you get yourself started. And the reason you want to get these things started is because they give the admin, or if you're an enterprise and IT, a point of control. So, you know what's going on. Otherwise, you really don't know what's happening in all these MCP clients and hosts that spread all over your organization anymore.

**[2:28](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=148s)** So, and and and and and this show, you know, if you go out, talk to sponsors in the exhibit hall, I would say a good maybe a third, maybe even half of the vendors will be providing solutions that look kind of just like this, a variation of this. So, there's plenty of choices. Definitely, you know, go Uber makes one, but we're not we're certainly not the only one. Um There There are many registries and gateways in there. You don't have to build from scratch anymore. And and they provide the obvious kind of functionalities that you would expect. And and and I want to talk about for for the rest of the you know, for the next 5 3 minutes 5 minutes, I just want to talk about where this thing is going because we we built this literally

**[3:16](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=196s)** maybe 6 months ago. We started marketing this and selling this. And and and and the world has already changed. And a lot of it is caused by the change in the agent development framework itself. So, as you know, like MCPs for for for for whatever it is, it's fundamentally needs to serve agents. That's what people need MCPs for. And the way you build agents has changed quite a lot. You know, couple years ago, agents were you know, like a rag chat chatbot. That was an agent, right? Um and then we we saw I I mean I think these days we see a lot of workflow agents. Um and workflows you can certainly write with workflow tools um uh with, you know, N N N, Temporal.

**[4:06](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=246s)** There's many many workflow tools on the market today, very powerful. Uh uh and and there's also coding tools uh code tools. Not Sorry, not coding tools. Uh I think people realize I think I I I I read it somewhere uh in one of the MCP summits someone said, "Oh, agent is basically just a code loop." Makes a lot of sense, you know, some Python code that that that repeatedly loops around and uh tries to achieve a goal. But nowadays with with code generation, with with coding assistance, and with MCP, none of this stuff is even necessary anymore. Uh the code the the agents I see people develop today, I see our customers develop it today, they kind of look like skills. They look like They look like skills, some

**[4:53](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=293s)** markdown files, and code that's generated by some code generator. And on top of that, uh what used to be the SDK and framework, now it kind of seems to be taken over by things like MCP layer. But of course, it's more than just an MCP. Could be the CLI, could be the agentic browser, could be a skills library, and could be many many other things. So So where definitely see Again, that's a that's that's that's a word I saw from the Uber folks. Like the just the word runtime. Uh It it it started to happen. You know, now instead of calling these things as just an SDK and framework, it has these entities that that's running. And uh and and and it it really doesn't matter how

**[5:41](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=341s)** you access them. Many of these things like MCP have standard protocols. So so they can be accessed um by you know, whatever agent you develop. And then underneath the runtime, what we're seeing is is security and governance layers started to form, you know, out of technologies like the MCP gateway. But that's not the only control point either because for some of the access control and and and governance, uh you also need to know, frankly, what the model is doing. So, so the gateway doesn't necessarily see everything that's sent to the model. So, so the LL having some visibility into the LLM gateway direct uh things that send, that's kind of useful, too. Uh secrets management. Oh, uh I mean, recently there's been uh there's been

**[6:31](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=391s)** quite a few incidents where the software supply chain was attacked by um um you know, by some well-known uh libraries. And it would be extremely bad if those compromised software getting to your, say, MCP or getting to your skills library. So, software supply chain filtering is now also becoming a key part of the gateway layer. And with that, the security and governance of enterprise agents are achieving a great deal of attention. And the you got to deal with those two areas. You need both a secure isolated runtime, which means, you know, for most of the enterprise customers we talk to, it is not really desirable to run the

**[7:20](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=440s)** enterprise grade agents on the desktop. Like, you know, engineers run cloud code, which is great, but if it's if it's a agent run developed by the third party, you don't want to let it take over the whole desktop. Then on top of that, you want to make sure you you you want to know who the agent is running on behalf of. And then you probably don't even agents running on behalf of you and then that has access say to your Outlook account. You want to make sure it cannot really access uh the Outlook account the same way you can get access to like it cannot just send emails like the way you can. You probably still want another level of access control to make sure the sensitive emails you you approve those emails before they get sent. Um

**[8:08](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=488s)** it with these kind of architecture there's some interesting uh uh opportunities are beginning to rise because these agents are written a little bit differently from traditional monolithic SaaS applications like a Salesforce app does all the access control for itself. Like if you're you know if you're a sales VP you see all your deals you you're sales director you see the deals in your territory. If you're maybe if you're if you're um a account executive you see your own deals. So they have all of that. But nowadays with agents uh the surface area that these that data needs to get access by AI nowadays is a lot wider. So as a result of that we're seeing

**[8:57](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=537s)** the access control and policy layer getting elevated out of the application layer out of the agent layer and now into the gateway layer. So that's a great place that something like MCP gateway can come into play. So with all of that we're seeing the the the the the MCP gateway and MCP registry uh architecture that I saw in the beginning evolving. So we're like if you kind of look at our latest product we've gone far beyond what a MCP gateway and traditional MCP gateway and MCP um registry can do. Uh the agent runtime layer is becoming quite important uh and the gateway itself see nowadays in involves things that we do to the to the

**[9:44](https://www.youtube.com/watch?v=m5yMJZX_cFs&t=584s)** skills to the software supply chain and from the catalog you don't just see MCP registry anymore. You see things like skills. So with that I just like to wrap up. If you need more information, please feel free to drop by our booth. I'll be at the booth most of the time and also send me an email. Thank you very much.
