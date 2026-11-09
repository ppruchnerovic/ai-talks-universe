---
id: ws9XcGGPBDk
title: "Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard"
slug: your-agent-is-a-lethal-trifecta-and-what-to-do-about-it-kim
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Kim Maida"]
channel: "AI Engineer"
duration_min: 25
published_at: 2026-10-12T13:00:35Z
video_id: ws9XcGGPBDk
url: https://www.youtube.com/watch?v=ws9XcGGPBDk
youtube_url: https://www.youtube.com/watch?v=ws9XcGGPBDk
tags: ["AIE NYC 2026", "Keynote", "Livestream Priority 02", "Online Talk"]
topics: ["Agents & orchestration"]
transcript: true
---

# Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard

**Kim Maida**

`AI Engineer` · `AI Engineer` · `2026` · `25 min`

`#AIE NYC 2026` `#Keynote` `#Livestream Priority 02` `#Online Talk`

[Watch the recording](https://www.youtube.com/watch?v=ws9XcGGPBDk) · [Conference site](https://www.ai.engineer/)

## Description

An on call agent drops a billing database, restarts a production server and scales a service from four pods to 40, adding $420 an hour to the bill. Kim Maida's staged triage demo shows what happens when an agent receives standing API keys and an administrator's database credentials. Private data, untrusted tickets and access to external services combine into the lethal trifecta. The agent can do useful work, but its credentials give it far more authority than any one ticket requires. A human approval button alone cannot tell it which actions the user is actually authorized to approve.

Maida walks through delegated authorization using OAuth token exchange: carry the user's identity through the agent and MCP server, evaluate policy at a security token service and issue short lived credentials scoped to the requested access. She also explains Keycard's approach to intent based authorization, which she identifies as a proposal rather than a finalized standard. The second demo uses task based policy instead. Customer data access and database deletion are denied, certificate renewal is allowed, and a server restart stays blocked even after approval because the user's role cannot authorize it. Scaling proceeds when the user has the required authority. The demos make identity, delegation and policy decisions visible throughout the request chain, while keeping authorization distinct from whether an agent's answer is correct.

Speaker info:
- https://www.linkedin.com/in/kimmaida/
- https://github.com/kmaida
- https://maida.kim/

Timestamps:
00:00 - An overprivileged on call agent
2:32 - Database deletion, restart and scaling
4:16 - The lethal trifecta
6:21 - Access control and standing credentials
8:43 - Missing identities and token exchange
10:25 - Following the agent and MCP execution path
12:18 - Subject tokens and the security token service
14:11 - Intent based authorization as a proposal
16:05 - Ephemeral credentials and delegation chains
17:37 - Repeating the demo with task based policy
20:01 - Data access, renewal and deletion decisions
22:28 - Approval constrained by the user's authority

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*3,641 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1s)** Today I'm going to talk to you about how your agent is a lethal trifecta and what to do about it. Now we're going to start out right off the bat with a demo. Some context on this demo. We're going to look at an on call triage agent that reads and writes to an incident pager and resolves or escalates tickets. This agent has full access to a cloud hosting API, a customer data warehouse as well as a billing database. So here we have our on call triage agent and it has an incident queue of tickets that it's going to read and then if it can resolve them it's going to call the available services that it has access to and it's going to do so things that it can't resolve it's going to escalate for the morning team. So if we take a look at this first ticket this is a billing

**[0:51](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=51s)** anomaly. It says a batch of customers were overcharged last night. So the first thing the agent does is it directly calls the incidex API in order to read the ticket. And if you look here, you can see that it authorized access to this API using an API key. It then uses a snowflake key to query the customer data warehouse and it's going to decide to escalate the ticket for morning review. And it writes a report for the morning team. And as you can see, it's sharing customer data. Right? These are rows directly pulled from the customer data warehouse. and it is sending personally identifiable information to the team that is going to be on staff in the morning. Now this next ticket is a backup power

**[1:39](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=99s)** supply failed in the server room. The agent is going to read the ticket again. It's using an API key to call the ticket API. It determines that this is a physical problem. So it escalates for morning review without calling any additional services. This one is the TLS certificate is expiring soon for the website. It reads the ticket. It determines that the alert is clear. It has access to the cloud hosting API and it calls that API at the certificate renew endpoint using again an API key. It resolves this by renewing the certificate and it leaves a report for the morning crew by calling the pager uh incident API as well.

**[2:32](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=152s)** This next one is the billing database is broken and payments are failing. So the documented recovery for this is to drop and restore the database. The agent does this using the database connection string that includes the admin password and then it advises the morning team to make sure that the snapshot recovery worked. Now this is not something that it has access to directly. So it is essentially assuming that the morning team is going to verify that this did in fact work and the information was restored. Now an overprivileged agent dropping a production database is basically a nightmare that several companies have actually lived.

**[3:19](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=199s)** So this is something that we need to be very careful of. Now the next one is orders are stuck. The main server is frozen. So the agent is again is going to read the ticket. After reading the ticket, the agent calls the cloud hosting API using again its static API key. It calls the endpoint to restart the server which brings production offline. Finally, site is failing for one in three visitors. Agent reads the ticket. It determines that it should call the cloud hosting API and scale the service from four pods to 40. It then incurs a charge of $420 per hour for doing this. And then it

**[4:09](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=249s)** kindly leaves a note for the morning team informing them that this has happened. Now, what makes an agent useful? Well, typically we want agents to have a minimum set of capabilities and often this includes things like the ability to read data that you own or have access to. This might be like your email, your documents, maybe a customer CRM. We want the agent to be able to do its own research. So this might include searching the web, maybe reading documentation or pulling issues from GitHub. And we usually want it to be able to use external tools, for example, MCP servers or APIs, maybe SAS platforms. And useful agents might do these things with a human in the loop or they might be doing it autonomously in the

**[4:55](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=295s)** background. But the thing that makes the things that make agents useful also make them dangerous. In fact, together these three capabilities make what Simon Willis coined as a lethal trifecta. This is a combination of access to private data like the on call agents ability to query the customer data warehouse and interact with the billing database. exposure to untrusted content like reading user submitted tickets or reports from other agents or externally documented processes and the ability to communicate externally like reading and writing with third party APIs or SAS services. Now together these capabilities throw the doors wide open for attackers. Now agents are designed to get the job done and they'll use all the powers that

**[5:43](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=343s)** they have to do it sometimes with very serious consequences. But here's the thing. These incidents happen because humans give agents way more access than they need. Overprivileged agents can act freely on decisions that they make, even if they do have supervision. Now, forcing a human in the loop approval just kind of passes the access control on to a consent fatigued user. Now, we've spent decades solving access management for humans. So shifting responsibility to the user just sort of moves the security problem up the chain. So what should we do about the lethal trifecta? How do we address it without compromising the agents usefulness? Well, just removing one or more of these

**[6:30](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=390s)** capabilities is going to cause the agent to be significantly less useful. So how can we keep all three but still be safe about it? Well, instead of breaking the trifecta by removing capabilities, we really need to control the agents access. So, the attack surface is minimized and the blast radius is contained, but the agent still has capability and autonomy. So, how do we do that? Well, some options for controlling access among others are things like using OOTH, maybe using a vendor MCP gateway or containing execution in sandboxes. Now, OOTH binds access to a grant. At grant time, the user consents to all of the permissions that the agent could possibly use. Now, consent is granted

**[7:18](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=438s)** before any task exists. So, if you give a broad grant, then you end up withstanding access. Your agent is over permissioned for any single specific task. If you narrow the grant and you don't give it very many permissions, then the agent just becomes less capable. Either way, OOTH alone doesn't provide task scoped access control. An enthusiastic agent can both read and write in the same run, even if you only want it to read on this specific task. Now, an MCP gateway binds enforcement to a route. You get things like observability and rate limits, and you also get one policy decision point at the MCP layer. Now policy runs per request and access is granted per user but the agents granted access outlives any single task because the gateway

**[8:06](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=486s)** still holds standing credentials. Now a sandbox binds execution to a process. This controls the blast radius but useful work has to reach outside the sandbox and when it does so you end up with standing access again. Now we've also seen plenty of stories about agents breaking sandbox containment. Sandboxes bound what the processes can do, but they don't control what is authorized to act outside the sandbox itself. Now, even if you combine all three of the solutions, the agent still doesn't receive a runtime credential that's downscoped to only one task. So, let's recap the problems, especially the ones that we saw in the demo. If you remember the audit log, we couldn't tell who was using the API keys. So the first problem is that credentials

**[8:55](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=535s)** weren't attributed to a user or an agent's identity. The agent had unrestricted access to any and all permissions that were granted by the API keys. And finally, we can't just slap human in the loop everywhere because humans make mistakes, too. Plus, many agents run autonomously and they don't even have a human in the loop. So to solve these problems, we can start by using something called token exchange. Now this is an existing standard that was published in 2020 and it extends OOTH 2. Now first we need to know who the user is. Now an authorization server verifies identities and issues tokens. Identity providers like Google, Octa, Ozero etc provide authorization servers. So if we want an identity chain in our agent execution path then the user has got to

**[9:44](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=584s)** log in first. The authorization server is going to prompt the user for consent to delegate access to resources with some subset of their permissions. Now, these permissions are called scopes. This is the first narrowing of access. We're only delegating some of the user's total scopes to the agent. The authorization server issues tokens identifying the user and their level of access. And at this point, we're already doing better than the demo because we actually know who the user is and we actually know what they can access. So this brings us into the agentic execution path. Now we have our authenticated user. So we have a known identity of a person who wants to use an LLM to interact with a

**[10:31](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=631s)** resource. Now in the demo the resources are the incident pager, the production database, snowflake and the cloud hosting service. An agent is a control loop that calls an LM. Often we have an MCP server that sits between the agent and its resources, providing defined tools that connect to those downstream services. An MCP client dispatches the agent's proposed tool calls to its MCP server. Now, in the demo, the on call triage agent called resources directly with long live static credentials like API keys or database connection strings. So what we're going to do is we're going to give the on call agent an MCP server. This is going to provide tools and is also going to serve to broker access to resources.

**[11:23](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=683s)** Now an agent runtime is a process that runs the agent loop and executes calls. The runtime might be a CLI like clouded code or an agent SDK which might be implemented in a custom application like the on call agent. So let's follow a prompt through this execution path. The user submits the prompt to the runtime which calls the model and sends the prompt to the LLM. The model then proposes tool calls which are dispatched by the MCP client to its MCP server which executes tools and then calls the resource API. The API returns the response to the MCP server. The MCP client delivers the response to the runtime which calls the model again. And this loop repeats until the model is satisfied and returns a

**[12:12](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=732s)** response to the user. Now the authenticated user's token becomes what we call a subject token. This identifies who the agent is acting on behalf of, who it acts for. Now token exchange needs an ooth client that can execute code. So this might be a gateway that sits between the MCP client and the third party MCP server or it might be your custom app. Now a custom MCP server can also exchange tokens for downstream resources. The on call agents MCP server should provide a defined set of production infrastructure tools. The prompt and the subject token are sent to the runtime. The agent loop runs and the model proposes a tool call.

**[13:04](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=784s)** The runtime authenticates with a special authorization server called a security token service. It does this using its app client credentials or workload identity. It also sends the subject token that contains the user's identity and access. It creates a token exchange request asking for permission to access the MCP server for that tool call and only that tool call. So now we have three pieces of info that we're missing from the demo. We know the identity of the agent that's requesting access. We know the identity of the user it's acting on behalf of. And we know the level of access that the user granted to the agent. Now we need to decide if the requested token should be issued. And we can do this with governance policy which is evaluated against what access is

**[13:54](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=834s)** requested from what resource, the identity of the agent and the identity of the user. But policies are ceilings. Agents can do things you didn't intend even when policy overall allows them. This brings us to something called intentbased authorization or IBA. Now, IBA checks what you mean before the agent acts. Now, it's not a finalized standard. They're still accepting proposals. So, this is Keycard's approach to implementing intentbased authorization. Now, IBA can use a gateway as a policy enforcement point. When you send the prompt to the agent, it proposes a mission. Now, this mission includes a goal, maybe allowed actions

**[14:43](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=883s)** as well as limits to what the agent is allowed to do. So, a goal of triage incident 2294 means read that ticket, summarize or escalate, but don't read other tickets and don't use other services. So, the security token service receives this mission. In this case, a low-risk activity like just assessing a ticket might be auto approved under admin policy. On the other hand, if we've already read the ticket and then we ask to remediate a usage spike, then the mission adds the permission to scale the service once but not use other tools or APIs. Now, in this case, the mission is presented for the user to review and approve. Once approved, the security token

**[15:31](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=931s)** service gives the mission an ID which is sent to the agent. The tool calls include this mission ID and are proxied by the gateway which uses the ID to ask the security token service if this tool call fits the mission. If it does, then the gateway requests a token exchange for access to the MCP server for that specific tool call. The STS evaluates policy. It evaluates the delegation chain and it looks at the requested access. Now, if everything looks good, it issues an access token for the MCP server and it keeps the user subject as well as adds the app that performed the exchange, which is in this case our on call agent. Now, this token should expire within minutes and we should never store it.

**[16:19](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=979s)** It's ephemeral. The STS sends it to the gateway, which calls the MCP server. The server then validates the token and authorizes the tool call. Now, some tools need external resources. So, the MCP server then asks the security token service to exchange the token that it just received for a token for the downstream resource. Now, the STS evaluates the request against policy and if it passes, then it mints a resource token that's scoped again to that tool call. It keeps the user subject which extends the delegation chain and allows us to be able to track all of the activity. The STS sends the token to the gateway

**[17:07](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1027s)** which proxies the request to the MCP server which then calls the resource. The resource validates the token and authorizes access. Now the MCP server should never store the token. It should discard it immediately after the call. The resource response then flows back up and the agentic loop repeats until the model returns the answer to the user. So now we're going to look at the same demo except we are going to use a security token service to manage agent access control with delegated authorization. The demo uses task based policy governance, not intentbased authorization, but if you're going to Agent Con later this month, we'll have

**[17:54](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1074s)** IBA demos there. Now, we also now have an MCP server that establishes tools and it provides brokering access to the resources. So, now we're back to our on call triage agent again, only this time we have authentication. Now I'm going to go ahead and sign into the on call agent triage app. I'm going to log in with Google to do so. And then I get another login screen. Now this is where I'm going to sign into the Incidex pager platform. So, I get a prompt to grant the on call

**[18:43](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1123s)** agent access to my Incidex account. I'm going to let it escalate incidents on my behalf, post notes and summaries, and read the queue. Now, I'm being prompted to log into the cloud hosting platform. So, I am going to do that. And I get another consent screen now which allows me to authorize the agent to access some capabilities of compost on my behalf. Now finally I am back on the on call dashboard. Now we have the same queue of tickets only now the audit log looks

**[19:31](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1171s)** different. The agent is probably going to try to behave the same way it did before. Only now every request is going to go through the STS and policy valuation before a token is granted and the agent will be authorized to act. So we have the same queue of tickets only now the audit log looks different and the agent is probably going to behave the same way that it did before only now every request is going to go through the STS and policy evaluation before a token will be granted and the agent can be authorized to act. So the first ticket is that billing anomaly. Again the agent tries to read the so the agent is reading the ticket and

**[20:21](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1221s)** we can see that it is trying to do the same thing that it did before. It tries to query the customer warehouse but policy doesn't allow a credential to be issued for this because customer PII doesn't belong in an agent's context or in an incident ticket. So the agent proceeds without the customer data and it escalated it to the morning team. Now we have the website security certificate expiring. Now this is something that the agent has permission to do. So when it requests

**[21:09](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1269s)** credentials to do this from the STS access is granted and it can call the cloud hosting API and resolve this ticket. Now you can see all of the calls that it's making and who is making them. So we have the on call triage agent that is requesting to renew the certificate. It's asking for permission to call the appropriate tool from the prod infra MCP server. So it gets a token for that. After that, the MCP server is going to request access to that cloud hosting service in order to renew the certificate using the API. So, if we move on to the billing

**[21:59](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1319s)** database, it's going to read the ticket through the incident API. It's going to come to the same conclusion that it did before. The agent knows that this is a drop and restore procedure, but this time policy forbids an agent to drop a production database. A human's got to do this manually. And we can see this in the audit log where the STS refused to grant the token exchange for access to the database delete. So now we have our orders are stuck. The main server is frozen. The agent's going to go ahead and read the ticket.

**[22:49](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1369s)** It wants to restart the main server. This takes production briefly offline. It informs me about this and this time it's actually asking for my approval to do this. So I'm going to click approve. However, this was also blocked by policy and the reason for this is because my user does not have the role necessary to take this action. Right? So the agent can't do it but I can't do it either and the agent is acting on my behalf. If we move to the site failing for one in three users again, the agent wants to add more servers and it's going to ask for permission. It's going to say what we're committing to when we do this. I'm going

**[23:39](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1419s)** to go ahead and approve this. And this is something that my role does have the authority to do. So the scale goes through and this ticket is resolved. So we can see that the agent access problems are solved. We know the user and the agent identity all the way down the chain. The agent has task scoped ephemeral access to the MCP server and downstream resources. And we have human in the loop with access control that's actually backed by policy. Now access is controlled at the task level by the security token service and policy and we retain all key capabilities. Now token exchange is an open standard.

**[24:28](https://www.youtube.com/watch?v=ws9XcGGPBDk&t=1468s)** It's well researched and it's public so anyone can implement it and it interoperates with existing policy engines and standards compliant identity providers as well as things like gateways sandboxes ooth offtheshelf and custom agents CLIs MCP servers software factories agent to agent crossapp access plus whatever comes out next week so I hope you'll consider it to make your agents useful safe and future friendly now my name is Kim Maida. I'm the founding GTM engineer and head of Devril at Keycard. And I really appreciate your time today. So, thank you very much.
