---
id: 8ehQZx39OyE
title: "OWASP Agent MAS Threat Modeling"
slug: owasp-agent-mas-threat-modeling
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "Security conferences"
edition: "OWASP GenAI Security"
year: 2026
speakers: []
channel: null
duration_min: 18
published_at: 2026-01-13T00:48:36Z
video_id: 8ehQZx39OyE
url: https://www.youtube.com/watch?v=8ehQZx39OyE
youtube_url: https://www.youtube.com/watch?v=8ehQZx39OyE
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability", "RAG, retrieval & knowledge", "Security, safety & red teaming"]
transcript: true
---

# OWASP Agent MAS Threat Modeling

**Speaker not identified**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=8ehQZx39OyE) · [Conference site](https://genai.owasp.org/)

## Description

🧩🛡️ MAESTRO: Threat Modeling Multi-Agent Systems (Including MCP) Beyond STRIDE
This session from the OWASP GenAI Security Project Virtual Summit (October 2025) introduces MAESTRO—a threat modeling framework designed for agentic and multi-agent systems, where traditional methods (STRIDE, DREAD, PASTA, OCTAVE, LINDDUN) fall short. The speakers explain why agentic AI changes the game: non-determinism, autonomy + tool execution, cross-cloud trust boundaries, ephemeral/token-based identities, agent-to-agent delegation, and blast-radius amplification when one agent is compromised.

MAESTRO uses a seven-layer approach to map threats across an agent’s full stack, including:

Foundation model risk

Data operations (RAG/vector DB/memory; poisoning & leakage)

Agent frameworks (e.g., LangGraph/AutoGen/ClaudeAI)

Deployment infrastructure (Kubernetes/serverless)

Evaluation/observability (logs, monitoring, verifier integrity)

Security & compliance as a vertical layer

Agent ecosystem (marketplaces, discovery, impersonation, protocols like MCP/A2A/ACP)

They also demo an open-source tool that ingests your agent architecture description, generates diagrams, and produces layer-by-layer threat analysis. The second half dives into MCP-specific threat modeling, including transport-layer weaknesses and runtime tool-chain attacks (e.g., injected/poisoned MCP services). A concrete mitigation pattern is discussed: maintaining hash-based baselines for tool calls and enforcing micro-segmentation policy controls to detect and block suspicious tool invocation at runtime.

👉 Learn more about the OWASP GenAI Security Project:

## Transcript

*2,401 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=8ehQZx39OyE&t=3s)** So welcome to our OASP agent mass modeling is multiple agent system. Uh and myself uh will go through this select modeling framework. We also call it as a maestro framework. Uh so we touched three main point it's limitation for existing uh modeling framework and the MO and uh AM will talk about mostly on the SL modeling with MCP uh a little bit about myself AM will introduce uh himself as well when he's uh his section uh he's talking about so I AI wrote a few books and published by

**[0:52](https://www.youtube.com/watch?v=8ehQZx39OyE&t=52s)** Springer Cambridge University Wy I also CSA fellow co-chair two working groups co-member of the AAS top 10 uh recently the instructor of EC console for general AI for cyber security I also leading the uh boutique consulting firm for distributed apps the traditional threat modeling such as stra dread or pasta octave or lindon they are really good framework it's certainly help uh application uh development in the like shift to left uh stage to identify the threat uh so you can manage it

**[1:41](https://www.youtube.com/watch?v=8ehQZx39OyE&t=101s)** uh the problem is with agent AI um it is not sufficient we still can leverage it but there is issue uh that it cannot cover. So I list this five areas that traditional framework are not able to cover. One is nondeterminism. Uh the traditional in the code once you write in the code or this is deterministic computing. So with agentic AI it's based on the model. uh it can hallucinate or it have a prompt injection problem. Uh so that's need a new thinking in terms modeling.

**[2:32](https://www.youtube.com/watch?v=8ehQZx39OyE&t=152s)** Autonomy is also another area that is important because agent has a certain degree of autonomy from time to time and maybe you don't have full autonomy but if you don't have autonomy that's not agent. uh so with autonomy uh especially use of tool to have the action taken that's a new threat model coming up in traditional threat modeling we always assume that there is the threat like security boundary we just need threat model within the security boundary and maybe the connection to our side but not the outside model

**[3:22](https://www.youtube.com/watch?v=8ehQZx39OyE&t=202s)** that is not true with the agent because you have the agent in one environment like uh AWS maybe talk to another agent in GCP using Google A2A agent and you may make payment using Google agent payment protocol. Uh so in terms of threat modeling you need to go far beyond it. Traditionally we do have the identities that you can define the policy in the deployment time. Uh that's not true anymore. So the new uh we also write a paper uh that akam and myself and other people participated and published by crowd circulate alliance. Uh we actually

**[4:13](https://www.youtube.com/watch?v=8ehQZx39OyE&t=253s)** get into very detail about agent AI identity issues. Um the identity usually for agent is epheirmal tax based and dynamic policy uh enforcement and that means the when you threat model it you need to thinking about this way and there's also agent to agent like communications delegations orchestrations that's the complexity and also have the issue with the blast pass radius. If one agent get compromised, it can impact another agent. So all this need a new framework to sync. That's why we're coming up like a with a seven layer framework that it can

**[5:03](https://www.youtube.com/watch?v=8ehQZx39OyE&t=303s)** deal with of uncover potential threat. Um if you think about a wasp top 10, it's identified the threat. The sled modeling is to identify the new slat beyond the sled modeling. So there in our uh paper published by O wasp we actually go further detail and APM also will uh lead us uh to do it for the MCP using this MU framework but uh essentially in the foundation model we look at the uh which model you use uh if there's any potential threat it could uh introduce then in the data operation the second layer We're talking about the uh

**[5:53](https://www.youtube.com/watch?v=8ehQZx39OyE&t=353s)** vector database or rag pipelines or even the memory right uh some of the data poisoning or uh data leak will happen in the data operation layer agent framework uh that the framework you can use like languin um clue AI there's many all those frameworks they are used for orchestration purpose they are not used for security. So you need the thinking about what potential security it could introduce. Um maybe have a zero trust uh plugin on top of the framework. Uh that actually I had a um develop the plug-in for uh autoing and cluei in my GitHub.

**[6:47](https://www.youtube.com/watch?v=8ehQZx39OyE&t=407s)** If interested uh you can reach back to me I have the link in contact at the end take a look. Um yeah deployment infrastructure is really where you deploy you deploying a kubernet to the AWS or you have deploy the serverless. So different deployment infrastructure uh has different threat uh possibilities and so you need a threat to model it evaluation is very important for agent and there is no perfect evaluation model yet uh so if uh there's any threat against the evaluation or observability that could be the issue right so we also

**[7:38](https://www.youtube.com/watch?v=8ehQZx39OyE&t=458s)** need talking about that security is really very important layer I also say it's a vertical layer each layer need talking about security and compliance right but for this agent AI there's a distinctive security and compliance layer that could potentially you have the agent for sock the agent for security operation center and agent for compliance Um and uh if you use it what could be potential threat then the agent ecosystem. So in the future the majority of internet traffic will be the agent to agent leverage maybe Google or Cisco agency or IBM right there's different

**[8:27](https://www.youtube.com/watch?v=8ehQZx39OyE&t=507s)** protocols there um but uh what is the ecosystems vulnerability things like uh if you have a marketplace uh how can you discover the price What if there's impersonation of the agent? So all those is like the key idea is really to uncover all possible vulnerabilities. Maybe in your agent AI application development. You may not reach all these layers, right? You may not have a agent ecosystem. You maybe just a simple tool. Then you just need thinking about six layer the top six layer here. uh right or sometimes maybe you do not using framework you're using

**[9:19](https://www.youtube.com/watch?v=8ehQZx39OyE&t=559s)** your own code maybe right so it's a little bit different but this is trying to cover the base >> [snorts] >> um you know what should should look for in addition to OASP top 10 right uh yeah so how do you perform mix modeling step one is you do layer mapping right so foundation model what it is in like a for your particular application for example entropic then it using a external L or maybe using cloud right or maybe using other models and the data operation layer uh usually is provided the data access through the MCP server maybe right to your uh applications agent framework MCP could be itself as a

**[10:09](https://www.youtube.com/watch?v=8ehQZx39OyE&t=609s)** framework in most case for multiple agent orchestration people using clue AI with MCP or langraph with MCP so you need a threat modeling as well uh then the deployment infrastructure yeah it's where you deploy your MCP server that's could be a big issue uh evaluation is important as well uh so you have to have login monitoring uh security compliance is also important right so design principles uh ecosystem how they connected so then the second layer we already talk about all this nondeterminism this is the second step uh you go through it so the key thing

**[10:59](https://www.youtube.com/watch?v=8ehQZx39OyE&t=659s)** here I have this open source tool you can just get clone here and just add your gemini API in the env file you should be able to run. Uh you basically you could can put anything here in the architecture description like you your agent architecture description then it will generate the diagram and also it you can generate analysis and it will go to each layer to generate analysis. Uh so yeah I think uh this is what I have. If you want to get reached to me that's my linking. Uh with that I hand over to Akam. >> Yeah. Thanks Ken for the great introduction. Hello everyone. I'm Akram

**[11:47](https://www.youtube.com/watch?v=8ehQZx39OyE&t=707s)** Shariff. So this is a brief introduction about myself. Next slide. >> Okay. >> Yeah. At a high level as Ken pointed out Maestro is a seven layered approach which applies to different layers within an agent. And when I say agent, this agent is a runtime agent entity. You have the layer which applies to the uh data operations layer. You have one layer from Maestro framework which is specifically allocated for the uh LLM model. Another layer for the tool calling and things like that. So Maestro it stands for multi-agentic environment security threat risk outcome based threat modeling framework. If you take traditional threat modeling frameworks, pasta, octaves, other legacy frameworks, they may not be useful for agentics

**[12:37](https://www.youtube.com/watch?v=8ehQZx39OyE&t=757s)** security threat modeling. And as you can see here, the kind of security threat attacks which might happen with agentic protocols like Anthropics MCP protocol or Google's A2A protocols, they are pretty new in nature. When I say new, it is the threat vectors which are very new. Some of these agents when they're running as embedded browserbased agents, you could have new kind of threat attack vectors which come which might come in from a Google email based plug-in or it could come from a man-in-the-middle attack or it could come from another uh browser web page or a tab that you might open in the same browser as well. So the kind of nuances involved in doing security threat modeling is very very important and that's where we have

**[13:25](https://www.youtube.com/watch?v=8ehQZx39OyE&t=805s)** focused and built this maestro custom agentic threat modeling. So no matter what kind of agent you're running the role the privilege and the kind of access to the data sources the agent should have at runtime is very very important. So it's important to have a micro segmentation based access control for the kind of grants that you provide to the data and for the tool calls which happen to the agents. Now the agents could be written in any language. All these fundamental paradigms are very important. If you take a fundamental MCP based protocol, MCP client is there and then you have an MCP host and then you have an MCP server and then you have different protocol transmissions which happen either via SGDIO or via other transport layer protocols. Some of these

**[14:12](https://www.youtube.com/watch?v=8ehQZx39OyE&t=852s)** transport layer protocols are very naive and they are ex I mean they're vulnerable to security threat attacks. Now how do we use security threat modeling techniques with maestro so that you can detect such security attacks and then you can do mitigation as well that's what we have covered in some of the research papers and in the open source project next slide and as you can see here this is the detailed summary of the maestro threat modeling so different layers are categorized here the core logic the session and the HTTP layer and then the with respect to the foundation models we have the AP APIs and then the cloud-based services and then deployment infrastructure is very critical. Most of these agents are deployed as containerbased agents, Kubernetes containers. Now you could use frameworks

**[15:01](https://www.youtube.com/watch?v=8ehQZx39OyE&t=901s)** like Spiffy Spire and then workload identity management in combination with Maestro threat modeling framework to achieve better business outcomes. And then the framework that we have written is pretty much agnostic. It can be applicable for langraph, llama index, chat, I mean baby GPT, Microsoft autogen regardless of the agent framework that you select with TypeScript or Python, we could still use Maestro. That's one critical advantage. Next slide, Ken. At a high level, let's say there is a particular security threat attack. As you can see here, this is an injected MCP service-based security attack where there are a list of tools which were there previously and then because of a

**[15:49](https://www.youtube.com/watch?v=8ehQZx39OyE&t=949s)** poisoned context poison context can actually come from the data or it could come from the prompt. Now because of such a threat vector there is a runtime specific security attack which is actually occurring. Now how do we detect this by using the maestro technique is something that we have discussed in the blogs and in the white paper and in the open-source GitHub projects. We would highly recommend and encourage you to read through that and then reach out to us so that we can answer questions and do deep dive sessions. Uh and to keep this session short, I'm going to just give you a highle summary. So for this particular security attack we are actually doing deriving individual hash coursees for each and every agentic tool call and we are creating a list of those hash coursees and if there is a new tool

**[16:38](https://www.youtube.com/watch?v=8ehQZx39OyE&t=998s)** which is actually getting triggered at runtime. We compute the hash score and then we can do the validation check with the existing list to see if that particular tool invocation is genuine or not. If that particular tool invocation is found to be not genuine, we block that straight away by applying the micro segmentation based policy control. That's to give you a highle overview in the interest of time. Next slide. Ken. So pretty much with these kind of techniques you can do MCP based tool shadowing security attacks detection and mitigation. You can do MCP based prompt injection based security that attacks that might be happening or MCP based rugpool security that attacks that might be happening in your environment. Now I have seen some matured applications

**[17:26](https://www.youtube.com/watch?v=8ehQZx39OyE&t=1046s)** where people are trying to integrate MCP protocol with Google A2A protocol to build new kind of agents. Yes, even for such complex agentic workflows, Maestro threat modeling framework could be applicable and you can do threat modeling at ease. And with that, we are happy to take any questions if you might have, but thanks for the opportunity team. >> Great. Yeah, thank you Akam. Um yeah I thank you everyone for participates participate in this uh short talk and uh yeah if any question reach out to LinkedIn and myself also the LinkedIn. Thanks.
