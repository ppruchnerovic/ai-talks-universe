---
id: 5sb9iA2v78g
title: "How Duolingo Built an AI Slackbot With 180+ MCP Tools"
slug: how-duolingo-built-an-ai-slackbot-with-180-mcp-tools
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 13
published_at: 2026-04-13T14:00:06Z
video_id: 5sb9iA2v78g
url: https://www.youtube.com/watch?v=5sb9iA2v78g
youtube_url: https://www.youtube.com/watch?v=5sb9iA2v78g
tags: []
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Enterprise adoption & strategy", "Evals, observability & reliability"]
transcript: true
---

# How Duolingo Built an AI Slackbot With 180+ MCP Tools

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=5sb9iA2v78g) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Aaron Wang, Software Engineer on Duolingo's DevXAI team, shares how they built an AI-powered Slack assistant that connects to 180+ MCP tools across 30+ servers. This keynote from MCP Dev Summit North America 2026 walks through Duolingo's full journey: from painful manual MCP setup, to a centralized app store, to standardization, and finally to bringing AI directly to employees via Slack.

The MCP adoption problem - Why even a one-click setup was too much friction for most engineers
MCP standardization strategy - How Duolingo categorized and hosted 30+ servers behind a unified HTTP config
Building with FastMCP - The internal Python library that lets any team convert their service into an MCP server
Slack app architecture - Using Claude Agent SDK and Slack Bot SDK to connect 15+ MCP servers with read-only tools
Auto-responding to help desk and incidents - The bot triages PagerDuty alerts using Grafana, Honeycomb, and Sentry behind the scenes
Human-in-the-loop for write operations - Approval workflows for creating PRs, Jira tickets, and staging deploys via Temporal
Per-channel customization - Custom skills, sub-agents, and system prompts tailored to individual team needs
Security and privacy model - Role-based access, sandboxed VMs, no cross-user data leakage, no logging of DMs
Eval tests and feedback loops - 20+ eval tests, upvote/downvote tracking, and iterative improvement to reach 80% approval
Adoption results - Growing from 20 to 250+ weekly active users, roughly 30% of the company
Open source announcement - Duolingo is releasing the core Slack AI agent code publicly
This talk is for engineering leaders, platform teams, and developers exploring how to deploy MCP-based AI agents at the enterprise level.

Links & Resources

Duolingo Slack AI Agent (open source): https://github.com/duolingo/slack-ai-agent
Duolingo Engineering Blog: https://blog.duolingo.com
Model Context Protocol: https://modelcontextprotocol.io
Claude Agent SDK: https://docs.anthropic.com/en/docs/agents-and-tools/claude-agent-sdk
Timestamps (approximate, may need adjusting)
0:00 - Introduction
0:17 - The early MCP adoption problem (Nov 2024)
1:04 - Centralized MCP setup page (May 2025)
1:45 - The MCP server fragmentation problem
2:27 - MCP standardization effort (Aug 2025)
4:58 - 30 servers, 300+ tools today
5:44 - If they won't configure it, bring it to them: the Slack app (Sep 2025)
5:57 - Slack app architecture: Claude Agent SDK + Slack Bot SDK
6:30 - Key features: auto-respond, human-in-the-loop, per-channel customization
7:33 - Feedback collection and eval tests
8:19 - Security and privacy principles
9:58 - Demo: help desk auto-response
10:26 - Demo: PagerDuty alert triage
11:02 - Demo: human-in-the-loop PR creation
11:51 - Adoption and approval rate results (April 2026)
12:50 - Open source announcement
13:20 - Closing

#MCP

## Transcript

*2,007 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=5sb9iA2v78g&t=0s)** All right. Good morning, everyone. My name is Aaron, engineer a software engineer from Duolingo. And today we'll share how we built a AI Slack app using MCP and the journey on how we got there. So, our journey started back in November 2024 when David introduced from my topic to introduce MCP. So, when it first introduced, a couple of our engineers got excited and so immediately saw the potential and started connecting various MCP servers to their local editors. However, the setup was very painful. For each individual server, you had to do your own research to find the GitHub repo, figure out the correct config for it,

**[0:47](https://www.youtube.com/watch?v=5sb9iA2v78g&t=47s)** get the necessary credentials, and manually create your mcp.json file. The barrier to entry is very high that very few engineers bothered. So, we knew this wouldn't scale and we need to lower the friction. In May 2025, we tried to fix the discovery problem by creating a centralized web page with instructions on how to set up various MCP servers. And here's a screenshot of what the setup page looks like. It's basically an app store where you can shop for different MCP servers with supporting house. And you just need to follow the instructions, select the MCP you want to set up for, follow instructions to get the credentials, and here's a generic config. I will show you a screenshot like the one on the right

**[1:35](https://www.youtube.com/watch?v=5sb9iA2v78g&t=95s)** where you have the mcp.json file, you can just click copy and put into Cursor, Cloud Code, whatever AI tool you use. But we still have one problem, the MCP servers themselves. Every single MCP server was built and run differently. Some are written in Python, some run are served in like UV X or others like maybe written in TypeScript and served as a Docker image. So, this causes problems for different people because they often run into like dependency issues or Docker issues. And in those days we got a lot of reports where like we tested all the MCP servers on our machine, but when we try to roll out to different people, they kind of report like, "Hey, it doesn't work on my machine because I have different NPX version or Docker just has issues as they always do."

**[2:26](https://www.youtube.com/watch?v=5sb9iA2v78g&t=146s)** That's when in August 2025, we started a MCP standardization effort within the company. So, here is our standardization strategy. Um For external first-party MCP servers like GitHub, Atlassian, we allow people to connect them directly to their first-party servers directly from their AI editors like Cursor, Cloud Code. For the open-source ones, we try to fork them in-house and added some like authentication um We have like internal ways to do authentications, so we added those to the MCP servers. We added tracking so we know who's using them and how they use it. We host it internally behind our VPC via HTTP. One thing to note here is that for some

**[3:14](https://www.youtube.com/watch?v=5sb9iA2v78g&t=194s)** of the external open-source services where people share similar credentials like with Funnel or Jenkins, we try to simplify the config for people where we use a shared service token on the on the internal server side. So, people just like use an internal JWT token to do the OAuth to them and they don't have to do OAuth in Cursor or Cloud Code and once in a while. Whereas for some of the MCP servers that different people have different access like Google or Slack, we have to do the we have to run the internal servers via OAuth also. And in addition to the public services, we also have a bunch of internal service where we try to get information on like how is the Duolingo latest app release or what people are

**[4:02](https://www.youtube.com/watch?v=5sb9iA2v78g&t=242s)** saying about Duolingo on Reddit and things like that. To integrate those company information, we we created an internal Python library built on top of FastMCP where people people from different teams can easily convert their services to MCP server and we also host those internally via HTTP. Also, for the external contacts where we can control the permission at the IAM level like AWS or BigQuery, um we do not use MCPs for those, so we just allow people to use AI tools to call their CLI directly. And lastly, for things where people have to run locally like Playwright or Simulator, we support them via we still support

**[4:51](https://www.youtube.com/watch?v=5sb9iA2v78g&t=291s)** those MCP tools that people can run locally via STDI or As of today, we have like around 30 MCP servers supported at Duolingo with 300 plus tools. And half of those are served internally with a very standardized HTTP configuration. You basically put your JWT token in the header and you just set the URL to be the MCP name internal.duolingo.com. And to use different MCP servers, you just replace the name. So, we thought this is this setup is simple enough for people, but even with this, we still do not see a lot of adoptions inside the company. So, even like a single click to copy this to your um

**[5:39](https://www.youtube.com/watch?v=5sb9iA2v78g&t=339s)** local config is still too much for people. So, we thought in September 2025, if people do not configure MCP servers themselves, we can try to bring MCPs to them. And this is when we started to introduce the Duolingo AI Slack app. The Slack app is built on two main components, the Cloud Agent SDK where the AI talks to different MCP servers as well as the Slack Bot SDK where it's doing the messaging with the Slack threads. So, it's basically Agent SDK connected a bunch of read-only tools from 15 plus MCP servers and it also has the ability to run AWS BigQuery commands to diagnostic different things or get metrics

**[6:28](https://www.youtube.com/watch?v=5sb9iA2v78g&t=388s)** internally. A few key features of the Slack app we built, it can auto-respond in help desk channels as well as incidents channels that we have. So, this significantly helped to reduce toil for on-call engineers. For write for write operations like creating pull requests or creating Jira tickets, we offer a way to do human-in-the-loop verification so the AI agent doesn't just go crazy and destroy the whole code base or whatever. We also have a general system prompt where we teach the AI on how to get internal information from different places. That also helps to make sure the AI does not hallucinate and write essays on Slack.

**[7:16](https://www.youtube.com/watch?v=5sb9iA2v78g&t=436s)** We also support per channel. Different Slack channels can have their own customization to satisfy different the needs of different individual teams. It also supports call skills and sub agents to improve the um Slack bot's response quality. We have a feedback button as as shown on the as shown in the screen where we collect feedback from people over time so we know how the bot is doing across different channels, across different use cases, and across um across the whole company. We also have a set of eval tests making sure the Slack app does not regress over time as we introduce new features or update models. So, we know for those like 20 sets of eval tests, it always return the correct

**[8:05](https://www.youtube.com/watch?v=5sb9iA2v78g&t=485s)** answer no matter how we update. And for a lot of the downvoted answers we got, we gradually add those to the eval sets to make sure things are improving over time. And the first question we after we launched the Slack app we got was around security and privacy. So, here is our approach to it. So our principle behind security and privacy is that we want to make sure the bot is not a way to for people to bypass permission issues. For example, non-engineers should not have access to the engineering tools. So, we have different access layer depending on their role. And second, like we kind of mentioned, the bot should not perform write operations to

**[8:53](https://www.youtube.com/watch?v=5sb9iA2v78g&t=533s)** the outside world without human approve. The only write operations it can do is to respond in the Slack threads. For any other write operations like creating Jira tickets or modify PRs pull requests, we we need explicit human approval for this. And third, the bot is running in a sandbox environment on a VM that it does not have access it does not have access to other things on the remote machine to not expose any potential sensitive credentials like your MCP server credentials on the machine. And lastly, the app should not use as a side channel between users. So, every individual messages need to be sandboxed so that person A should not use the bot to get

**[9:41](https://www.youtube.com/watch?v=5sb9iA2v78g&t=581s)** information about person B's DM message with the bot. And for privacy, we do not log anything for DM or private channel messages. That's that's done to protect the privacy for people within the company. So, that is enough concept and to better show how it looks like, uh here's a screenshot uh where someone came to our help desk asking for some cursor issues they ran into and the Slack bot was able to search both internally across different Slack channels, across screen, and also uh with things publicly on the internet to provide like, you can try those three things to hopefully help resolve your issue. And this is another uh Slack slide another screenshot where we have some

**[10:30](https://www.youtube.com/watch?v=5sb9iA2v78g&t=630s)** PagerDuty alerts uh that failed, um on-call engineers uh get paged, and the Slack bot can automatically respond uh with like the automatic trash. It runs like it runs commands, look at uh various observability tools like Grafana, uh Honeycomb, or Sentry behind the scenes and provide this uh uh like root cause analysis, and also suggesting next step for the on-call engineers to take uh on how to resolve or alleviate it. And this is a screenshot on the human loop step we talked about. So, um this is a screenshot on the uh the screenshot on the left is a screenshot where uh I asked it to address a a address a some discussion uh you know, Slack stories, and it will show me this

**[11:20](https://www.youtube.com/watch?v=5sb9iA2v78g&t=680s)** like confirmation box with two buttons, approve or cancel. So, if I click approve, it will then trigger a temporal workflow to uh actually go and make a commit and make the code to the create a pull request to address the the comment. So, for all the write operations like creating pull request, deploy to staging, or um yeah, creating Jira tickets, we have this human in the loop uh uh like feature offered for those. So, that brings us to today, uh April 2026. This graph kind of shows the adoption of the Slack bot after since we introduced in September last year. Um So, we were when we first introduced, we have around like 20 uh weekly active

**[12:09](https://www.youtube.com/watch?v=5sb9iA2v78g&t=729s)** users, and as of today, we have more than 250 people using uh the bot on a weekly basis. It may not sound a lot, but for a small company uh like Duolingo, that's more around like 30% of the company. And this graph uh shows the uh upvote rate on the response where uh I think as we gradually add more skills, uh change the prompts, add more NLP connections, you can see the bot's response is getting better and better over time, and recently, I think it stabilizes around 80%. Uh it's not perfect, but it definitely provides value to people. And finally, if your company also uses Slack or uh and use Slack called, we have good news for you.

**[12:57](https://www.youtube.com/watch?v=5sb9iA2v78g&t=777s)** Uh we actually decided to open source the core application code of the Slack bot. So, feel free to check it out at Duolingo slack-ai-agent um if you want to reuse this. And if your company does not use Slack or uh cloud SDK agent, then feel free to fork it and ask AI to write a different version. Um so, that's it for That's all I have for today, and thank you. [applause]
