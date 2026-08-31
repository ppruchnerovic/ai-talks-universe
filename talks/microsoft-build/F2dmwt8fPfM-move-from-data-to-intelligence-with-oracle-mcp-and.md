---
id: F2dmwt8fPfM
title: "Move from data to intelligence with Oracle MCP and Microsoft IQ | ODSP919"
slug: move-from-data-to-intelligence-with-oracle-mcp-and
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 20
published_at: 2026-06-03T09:55:34Z
video_id: F2dmwt8fPfM
youtube_url: https://www.youtube.com/watch?v=F2dmwt8fPfM
tags: ["AI", "API", "Agents", "App Integration", "Data", "Jeff Smith", "MCP", "Move from data to intelligence with Oracle MCP and Microsoft IQ | ODSP919", "ODSP919", "ODSP919_v1", "Ram Kakani", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Move from data to intelligence with Oracle MCP and Microsoft IQ | ODSP919

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `20 min`

`#AI` `#API` `#Agents` `#App Integration` `#Data` `#Jeff Smith` `#MCP` `#Move from data to intelligence with Oracle MCP and Microsoft IQ | ODSP919` `#ODSP919` `#ODSP919_v1` `#Ram Kakani` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=F2dmwt8fPfM) · [Conference site](https://build.microsoft.com/)

## Description

Make the leap from disconnected data to intelligent, AI-driven workflows by combining Oracle managed MCP Servers with Microsoft IQ. See how MCP enables connectivity to Oracle Database@Azure, while Microsoft IQ—Work IQ, Fabric IQ, and Foundry IQ—bring context, reasoning, and orchestration to enterprise data. Together, they power agentic experiences with Oracle handling infrastructure and operations, accelerating time to value, and delivering enterprise-grade solutions at scale.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Jeff Smith
* Ram Kakani

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

ODSP919 | English (US) | Agents & apps

Pre-recorded | (200) Intermediate

#MSBuild

Chapters:
0:00 - Introduction at Microsoft Build 2026 and presenters Jeff Smith and Ram Kakani
00:00:50 - Overview of Oracle and Microsoft AI integration architecture
00:01:16 - Explanation of intelligence layer and governance features with Agent ID and Agent 365
00:02:21 - Detailing development stack components including Foundry agent services and GitHub Copilot
00:03:04 - Jeff explains evolution of Model Context Protocol and Oracle MCP servers
00:04:08 - Step-by-step setup of MCP server connectivity and authentication process
00:07:34 - Live demo setup showing Azure portal and Oracle databases integration
00:12:08 - Running the agent to analyze unpaid invoices using Foundry IQ and Oracle MCP
00:16:25 - Agent provides actionable recommendations and workflow automation using Work IQ
00:18:40 - Closing remarks, community resources, and invitation to explore Oracle at Azure integrations

## Transcript

*2,541 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=0s)** Hey, hello, friends, colleagues and Azure community at Microsoft Build 2026. My name is Jeff Smith, I am a product manager at Oracle. So happy to be here today to share our AI story and how we can make our Oracle database useful in serving your business. So your data stored in our databases goes very well with Microsoft's AI platform. And I'm joined here today by my colleague at Microsoft, RAM Kakani. Ram, why don't you introduce yourself? Hey everyone hope you guys are having fun at build. I'm Ram Kakani, a product manager at Oracle Database of Azure team in Microsoft. And I cover MCP servers for the Oracle database at Oracle, so together we should be able to do some damage today.

**[0:47](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=47s)** So let's move to the next slide. Let's look at basically how it all comes together. As you can see here, you could build business aware enterprise agents that are AI ready with Oracle data. There are four plates as you can see where you have AI at the top, the dev surface, Azure AI, Foundry, Copilot Studio, GitHub Copilot, Procode or Locode. Same runtime. Below that is your intelligence layer where you have Foundry IQ for reasoning and grounding, Fabric IQ for historical analytics, and Work IQ to deliver this into your outlook teams, Excel and also bring your work context. Turn on what your scenario needs.

**[1:38](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=98s)** Then you have Oracle Access. You'll see two patterns, Oracle MCP server for live reads, Fabric Mirroring for historical or cross source analytics if you have more than one source of data and same agent code that runs either ways. Underneath all of that is the governance plan, not bolt on entry. Agent ID gives every agent a first class identity with least privilege. Scoping agent 365 gives you that tenant wide inventory and governments. Oracle data stays safe in Oracle. That's enterprise ready. Let's see now how it all comes together. And let's see what's the dev stack looks like four process pieces of dev stack, if you will.

**[2:27](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=147s)** One is the Foundry agent service that hosts agents and the MCP client that which provides your native MCP support and points to any MCP server, in this case Oracle MCP server. And the next one is the GitHub copilot or copilot studio depending on your choice, pro code versus low code. All of that, as we said is governed by the Microsoft and try Agent ID and Agent 365 governance. As you can see, just four piece of two pieces of code that will take you to life with an agent. Let's see, now Jeff will take you through the MCP server. Thanks MCP. So model Context protocol really came on to the scene in late 2024 and and caught on like wildfire all all throughout 2025.

**[3:17](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=197s)** We had MCP servers for Oracle AI database since July and now for cloud both in our clouded Oracle Cloud infrastructure and for Oracle databases running at Azure. We offer managed hosted MCP servers native into our our our cloud environments. So as a customer or a partner, you can come in and just define the characteristics of the MCP server, what tools you want to be made available, how the authentication is going to work. And we run that for you at no additional cost. So the only thing you're going to be paying for is using your database or using the the AI tooling. The MCP server itself is is no cost.

**[4:08](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=248s)** So the steps that you're going to need to do to set up the connectivity between the, the various Azure IQ pieces and the actual data in your database, we're going to start off with the database connection. So just like any, any time you're working with any database, you, you generally provide a set of credentials. And it's these credentials that basically shape the view of the data that the AI will see. So you can, you can use a a proxy user that's tied to your identity domain and and that can be used to determine like what type of data you can see in the tables or whether the tables are even visible at all. But once you have the connection defined, you can go ahead and create the MCP server and you're going to point it to the identity domain.

**[4:55](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=295s)** And this is where you're going to have your Azure intra ID users defined. And then let's say ROM has an account, I'm going to add him to an MCP server group that will give him privileges to connect to and talk to our MCP server using his existing Azure intra ID login. At that point, I'm going to define the MCP tools. So tools are sort of the AP is that allow clients for the MCP or the agents that are speaking MCP protocol to our server. This is where they can request things to be done on their behalf. And probably the most well known pattern is natural language to sequel. So Ramana's demo, I think is probably going to say something like, hey, Mr.

**[5:43](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=343s)** AI Wizard, show me how many widgets we sold last week. And the LLM will translate that into a query statement that our database will understand, and it'll submit that query to be ran through our MCP tool. Before you can do that, though, we're going to register the agent as an MCP client, and that's what allows the Oauth 2 workflow to work. So the first time you'll go to do this, which we probably won't show in the demo because it's kind of boring, but Ron would login, we would verify the Azure Intra ID credentials, He'll be asked for permission to grant the agent to act on his behalf, sort of. It's called an OBO token. And then at that point, the agent can go grab and access token use using the Oauth 2 workflow and you never see the the login stuff ever again.

**[6:33](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=393s)** So as long as Rom's identity has the group membership required to interact with the resources on the Oracle side, our MCP server and the database good to go to ask questions. And the nice thing is we will propagate Ram's identity, Rom's identity in the database itself. So ROM could be using an agent talking to an Oracle database via AI and the Oracle database will see ROM as as himself. They'll we'll see Rom's Azure intra ID user. So in the security side, we can set up all of the very fancy Oracle security rules. He has a problem too and a BITS team has asked a developer the invoice volume is up 30% on Flathead count cycle times past 45 days in data setting

**[7:24](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=444s)** in Oracle database and dashboards. Tell them what happened. They need an agent that moves the work and the budget that they have is weeks. Not quarters, but weeks. Let's see how we solve it right? Same agent, same Oracle data, zero ETL, built in Foundry, wired with Foundry IQ and work IQ talking to Oracle database through Oracle MCP server. I'll start with my Azure portal. Here is my Oracle database at Azure. As you can see, there's a slew of database services that Oracle offers through Azure portal. Natively integrated Autonomous AI database, Excel data database, Excel data data, Excel data database on Excel scale, Infrastructure based database service and Golden Gate. For this demo purposes, we have our supply chain data

**[8:17](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=497s)** hosted in Exadata database and in this VM cluster and UK South. As you can see the cluster is provisioned in the V net and subnet in your virtual network. Now here is Foundry where I'll go build an agent. So clicking on here, we'll take you to Foundry portal. We've already got that opened. Here is my Foundry portal. I'll go to build. Now we can technically go create an agent from scratch here, give it a name and continue through that. It's self self-serve. I'll just go take for the timing. Let's go look at an agent that I already built. Here is an example agent where you have account payable

**[9:09](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=549s)** and list agent for example that is actually responsible to provide all of the insights for the AP. Now you can see the remote MCP server that's already pre provisioned and it's connected into the tools. Let me also show you how do we do that. So you could go create tools. Now in this you could connect the tool. So from the catalog quickly go look at Oracle. You have Oracle remote MCP server. You'll go create that you'll you'll provide the remote MCP server endpoint, the parameters for the region and the O set and authentication as as Jeff mentioned can be key

**[9:59](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=599s)** based, auto art based and you'll just hit connect. So here is a MCP server connection that's already bugged connected here in the tools can see this MCP server is provisioned in UK S the connection ID and is currently used in these two agents. Now that we are here, let's also look at other tools that we require, right? 1 is basically the foundry IQ and the work IQ. Here is our work IQ that is connected to again to the agent that we'll go demonstrate. But same thing, right? You go to tools, you connect a tool, you look for work IQ here and all you have to do

**[10:54](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=654s)** is you'll use the Work IQ e-mail MCP server. Now let's go look at our agent. So here is an agent that is responsible for our fictions company Zava entity. And as you can see it's connected to the remote MCP server. For the connected to the Oracle database, the work IQ e-mail is already configured as well as the fabric IQ for historical trends. And then for the knowledge base you have, it basically have Zava knowledge IQ that is created here in the knowledge.

**[11:43](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=703s)** And if you can look at this, you have both the compliance reports here that are stored in Microsoft one leg and the vendor policies and our documents, contractual documents that are stored in Azure BLOB storage, which will be used as our knowledge sources that will power this knowledge base and that will power the Java agent. So let's go look at our agent in action now. The first one that I'm going to ask the agent is to show the last 90 days worth of invoices that are unpaid and are over 50,000 and include the reasons and age. Here is the consent.

**[12:43](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=763s)** Authenticated. Now you'll see that the agent is connecting to the MCP server and they'll execute a bunch of queries that are pre populated for you and to get the data. As a developer I used to write 50 lines of boilerplate code and OCISDK setup and connections to get this. But look at this, the magic of MCP life. Yep.

**[13:33](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=813s)** So as you can see, you'll see there are a few suppliers which are which have unpaid invoices over 50,000 at my car has two and others have one each and vendor X has three. Right now. What happened? Let's go look at how these unpaid invoices are and do they have any PO mismatches or any duplicates and which of them can be released or which of them can be held. That's my second prompt here. You would see the Foundry IQ in action where the agent is looking at the vendor agreements, the looking at the policies, compliance policies and it's basically trying to analyse

**[14:29](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=869s)** the the delays and along with the duplicates. So you always need to approve each query with the human in the loop, basically validating that it is talking to the right tables, getting the right data that is required and it has the right authorization and authentication. Thank you for saying that Ron. Just because the stuff is fast and it looks good doesn't mean you can take your your eyes off or your hands off. I like to tell people that you're the actual pilot, not the copilot.

**[15:19](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=919s)** Good one, I like that. I'll pretend that was original with that one. And that's so true because the agent is talking to your mission critical enterprise data residing in Oracle databases. So you may you better be conscious about what the agent is accessing, why is it accessing and what's the outcome of it. All right, looks like the agent is retrieved and the right recommendations. As you can see, it basically is reasoning over all of the invoices and against the documents that are supplied

**[16:14](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=974s)** with the knowledge base and is basically looking at a few invoices, yeah. That's awesome. All right, now you can see best candidate for likely safe to release is Acme Group only after resolving the duplicate resolution. Now I can go ahead and cancel the duplicate payment and let the my AP head release the order for Acme or invoice for Acme. So what I'll do, I'll go ahead and put my work IQ at work. So as you can see, let me go ahead and use my third prompt.

**[17:03](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=1023s)** Here's my third prompt. What I'm saying is hey, look at all my ongoing discussions and emails with about Acme Group for these specific invoices, summarize what was agreed and then draft a reply to James Chen with the latest on the same thread about the cancellation. Great. It is now looking to search so I'm approving the search parameters again. It's trying to retrieve that message additional search parameters with filters to find the right conversation. It'll then look for creating that draft message.

**[18:06](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=1086s)** There you see it's basically created that draft message where the Aqua group order was submitted in error and basically delete the cancel that duplicate and then release it. This will generate a draft in your Outlook that's connected that you can just go ahead and hit send after validating the right message. Over to you, Jeff. I mean, that's the real magic. It wrote the e-mail for us and it dealt the, IT dealt with the human stuff. I'm not good at. This is my first opportunity to speak at this awesome event today. So I just want to thank everyone watching for that opportunity. I'm easy to find online. You can just Google that Jeff Smith if you want. But I do want to leave you or we do

**[18:54](https://www.youtube.com/watch?v=F2dmwt8fPfM&t=1134s)** want to leave you. Some resources you can follow up on. We have a community here on LinkedIn that specializes in all of our friends running Oracle Database at Azure. And if you're looking for pricing or technical details, you can follow the third link there this QR codes I I also want to invite you to work with us to set up a call. Our engineers will happily show you how you can get your traditional on premises Oracle databases running in Oracle at Azure and I would love for them to also help you set up our MCP servers so you can get your agents working just like ROM showed today. Thank you everyone.
