---
id: YiFqcu9YA38
title: "Dashboards Are Dead — Sarah Simionescu, Composio"
slug: dashboards-are-dead-sarah-simionescu-composio
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Dashboards Are Dead", "Sarah Simionescu"]
channel: "AI Engineer"
duration_min: 11
published_at: 2026-10-04T01:30:36Z
video_id: YiFqcu9YA38
url: https://www.youtube.com/watch?v=YiFqcu9YA38
youtube_url: https://www.youtube.com/watch?v=YiFqcu9YA38
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "MCP", "Model Context Protocol", "AI agents", "agent experience", "AX", "dashboards", "Composio", "Claude", "tool calling", "agent tools", "developer tools", "product design", "observability", "Sarah Simionescu", "AI Engineer"]
topics: ["Agents & orchestration", "Classic ML & data science", "Evals, observability & reliability"]
transcript: true
---

# Dashboards Are Dead — Sarah Simionescu, Composio

**Dashboards Are Dead, Sarah Simionescu**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#MCP` `#Model Context Protocol` `#AI agents` `#agent experience` `#AX` `#dashboards` `#Composio` `#Claude` `#tool calling` `#agent tools` `#developer tools` `#product design` `#observability` `#Sarah Simionescu` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=YiFqcu9YA38) · [Conference site](https://www.ai.engineer/)

## Description

Sarah used Datadog every day for six months without ever opening the dashboard.

Sarah Simionescu, member of technical staff at Composio and on the team behind the Composio dashboard, makes the case that the dashboard is dead. She traces how we got here: five tools and five query languages, then the AI 'sparkle button', then MCP. She explains why MCP alone is still a mess (agents don't learn, too many tools drown the model, every app is isolated) and shows how an interface designed for agents fixes it. Live demos go from a Slack bug report to a fix PR, and run a cross-app analysis across PostHog and Metabase without loading full results into context.

In this talk:
• Why every dashboard and query language was a translation layer
• Three reasons wiring up a dozen MCP servers falls apart
• How tool search plus execution plans help agents work across apps
• Building products for a new kind of user: agents

SPEAKER
Sarah Simionescu, Member of Technical Staff, Composio

LINKS
Composio: https://composio.dev/
Composio MCP: https://composio.dev/mcp-gateway

CHAPTERS
0:00 Intro
0:12 A confession about dashboards
1:02 The dashboard is dead
1:17 A postmortem
1:27 2022: five tools, five query languages
2:17 You wanted the answer, not the dashboard
2:37 2023: the sparkle button
3:02 2024: MCP arrives
3:31 Why MCP alone is a mess
3:51 Agents don't learn
4:06 Too many tools drown the model
4:31 Every app is isolated
4:56 Demo: from Slack bug report to fix PR
6:25 Results vs native MCP servers
6:45 An interface designed for agents
7:20 Demo: cross-app analysis
8:59 What this means for every product
9:44 A new kind of user
10:14 Wrap-up

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*1,774 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=YiFqcu9YA38&t=12s)** Hello everyone. My name is Sarah and I have a confession to make. So, I've been using Data Dog every day for the last six months. And the other day my co-orker comes up to me and he's like, "Hey Sarah, can I look at this alert?" I'm like, "Okay." So, I open up Data Dog and I'm logged out. It's kind of awkward, so I have to log in and he's like looking over my shoulder and I'm like overly conscious about everything that I'm doing on my computer. And I open up the data the data dog dashboard and I just froze. I had no idea where anything was. And this is actually not a knock on data dog. The problem was I had genuinely never opened the dashboard. I've been using it every day without ever looking at it. And so today, I want to make an argument that sounds kind of

**[1:02](https://www.youtube.com/watch?v=YiFqcu9YA38&t=62s)** insane and then show you that it's obvious. The dashboard is dead. And I think that's great news for everyone in this room except probably for me because I am my team is responsible for the Composio dashboard. Alas, how did we get here? I believe a postmortem is in order. Shall we? The year is 2022. It is the dark ages. Someone pings me on Slack. They say, "Hey, I get this error when I try and search for prod." I would have instantly spawned five different windows. Read the context in Slack. Write a query in data dog. Check post for this session. Uh, fix the bug in VS Code. Open the PR in GitHub. That is five tools and five UIs I have to learn and relearn every time they ship a

**[1:50](https://www.youtube.com/watch?v=YiFqcu9YA38&t=110s)** new redesign. But frankly, redesigns are the least of my problems because every single tool has its own query language. So, data dog has its own query syntax. Jira has JQL, search, Slack has its search modifiers. And it gets worse because even when these tools claim to speak the same language, let's say SQL, they don't even agree on SQL. Every dashboard you've ever used, every weird obscure query language ever written was a translation device between you and your data because the machines on the other end could not understand what you actually wanted. You never wanted a dashboard or it's cursed query language. You wanted the answer. And in 2023, everything changed. The sparkle button.

**[2:40](https://www.youtube.com/watch?v=YiFqcu9YA38&t=160s)** The sparkle button was born. And with a click of this magical button, an LLM would write a sometimes correct query to get you the answer you need. That is if your question does not require more than two database joins. And soon enough, these sparkling buttons were everywhere. So dashboards became AI native. Problem solved, right? Well, not quite. In November of 2024, Enthropic announced the MCP protocol with a promise to create an open standard for connecting AI systems with its data sources and that it did. Instead of using a sparkle button, your own agent, Claude, whom you've already been using every day, could generate the query for you, execute it on your behalf, and give you the answer directly. And you might be thinking, problem solved, right? This is the end

**[3:28](https://www.youtube.com/watch?v=YiFqcu9YA38&t=208s)** of the story. Well, far from it, because MCP is a protocol. It's a channel for communication between agents and your service. And it's up to you, the service, to choose how to communicate with the agent. And it turns out that makes all the difference. If you've ever actually wired up a dozen MCP servers, you will know the reality is a mess for three reasons. Agents don't learn. Every conversation starts from zero. It has no memory of how it fumbled formatting links properly in Slack yesterday, and so it's just going to fumble again today. And we patched this with skills, but skills is just a band-aid because agents become dumber with the more context you provide. And loading more tools, more skills takes more context. And if you connect enough servers, you're dumping thousands of tool

**[4:15](https://www.youtube.com/watch?v=YiFqcu9YA38&t=255s)** definitions straight into the context window. I mean, our GitHub like toolkit alone has over 200 tools. The model just drowns. It grabs the wrong tool or struggles to resolve dependencies and it can't figure out which one it needs to call first. And third, every app is isolated. Each MCP server knows about itself and nothing else. So the moment a task spans two apps and like they always do, it is your job to piece that together. And so MCP gave agents a door into every app. But it left them standing in thousands of separate rooms with no map and no memory of ever being there. I'm going to show you a mockup demo here of how I would solve this bug report uh from the very beginning how I would solve it in 2026.

**[5:03](https://www.youtube.com/watch?v=YiFqcu9YA38&t=303s)** So imagine in this mockup I have my claude connected to the composio MCP. What I would do is I would literally just copy and paste the link to the message from Slack and say please use century data dog find the root cause a draft PR make no mistakes. And the first thing it does is it calls composio search to state the task it wants to accomplish. So in this case it stated three. It wants to fetch slack messages. It wants to search sentry issues. It wants to search data dog logs. And for each of these three, Composeio returns not only the correct tools it needs, but actually a plan of how to use them. So for example, for Slack, you actually have to find the Slack channel ID before you can start quering for messages. Now that it's armed with all the context it needs, it has a plan. It starts pulling the message from Slack to see

**[5:52](https://www.youtube.com/watch?v=YiFqcu9YA38&t=352s)** what the user complaint was. Then it begins pulling from data sources in parallel. Data dog sentry and it begins scanning the codebase. Once it identifies the root cause, PR is up with a fix in less than five minutes. I didn't have to build a workflow or write a skill to teach it how to do this. This is literally just claude using Composeio's MCP. And it has become so much easier to do things this way that opening up Cloud has just become like muscle memory for me to do literally anything. And the dashboards I used to open every day are becoming increasingly unfamiliar to me. And the impact of designing for agents is measurable. So these are some early unreleased uh results comparing Composio against each app's own native MCP that's listed in the clawed uh marketplace. So it's the same tasks, it's the same

**[6:40](https://www.youtube.com/watch?v=YiFqcu9YA38&t=400s)** model, and we see a clear difference. But why? Why is this experience so much better than native MCPs? It's because at Composeio, we are developing a brand new interface specifically designed for agents. We translate messy, sparsely documented, everchanging APIs from all of the apps that you live in every day into something that agents really love to use. So, we build on top of MCP CLI and native tools to deliver a cohesive, unified, and excellent experience for your agents that allows them to perform complex operations across these apps seamlessly. I'm going to show you a more classic example of like what I usually use it for every day. So, let's say I want to dig into some user data. I want to see the distribution of what vertical my

**[7:28](https://www.youtube.com/watch?v=YiFqcu9YA38&t=448s)** users select during onboarding. I can simply just ask Claude. Claude will again run Composio search. It will write a query in Post Hog, execute it nice and simple. There's my results. But what if I wanted to take this up a notch? So I want to look at that e-commerce section right there. And I want to see what tool kits they like to use. Toolkits is another word for apps we like to use at Composio. So let's see if cloud can figure out how it can pull this data from metabase uh given the user ids in post hog. So once again it uses composio search. It queries the user ids of those who selected e-commerce from post hog and it actually saves it without loading the full results into its context. Then it makes some queries uh in

**[8:17](https://www.youtube.com/watch?v=YiFqcu9YA38&t=497s)** metabase to get the database schema sample some data get a feel for how things are structured. And once it's confident, it actually uses a very cool tool called Composio Remote Workbench to dynamically generate an SQL query with a reax string to search for all those user IDs again without ever loading the entire thing into its context window. And there we go. So we can see the most popular toolkits amongst this user persona in less than a few minutes. Uh and that's data pulled from both sources. If you want to play with the live version, come visit us at the Composio booth. Uh, I'd love to have you play with this live. And so, the dashboard has died. And I'm thinking more and more about what this means for the future. Many startups have

**[9:05](https://www.youtube.com/watch?v=YiFqcu9YA38&t=545s)** begun making their landing pages and their websites AI friendly for GEO purposes. But so few have really prepared their applications to be used by agents. Compose began as a tool to help developers. We were taking these popular apps that users like and turn them into these tools that agents could use. But the humans are tired of dashboards and their agents are tired of poorly designed MCP servers. And now we're getting requests from startups saying their clients are begging for a way to use their services through their agents. So this is a lesson for everyone building anything right now. You are now serving a new species of user. They don't have eyes. They are not going to click your sparkle button. It shows up with a goal and a set of tools and it

**[9:54](https://www.youtube.com/watch?v=YiFqcu9YA38&t=594s)** judges you on exactly one thing, whether it can get the job done. For a decade, we've built pro uh we've built products to be easy for humans to use. And the next era belongs to those that are easy for agents to use. So, picture me again. I'm frozen in front of that data dog dashboard. And I was thinking to myself in that moment that I'm falling behind. Uh, but now I think of that moment as a preview of what's to come. Thank you. [music] >> [music]
