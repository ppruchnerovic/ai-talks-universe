---
id: UPukeLcIWrM
title: "More Team Automation, Less Agent Autonomy"
slug: more-team-automation-less-agent-autonomy
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "AI DevCon NYC 2026"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 19
published_at: 2026-11-06T21:29:02Z
video_id: UPukeLcIWrM
url: https://www.youtube.com/watch?v=UPukeLcIWrM
youtube_url: https://www.youtube.com/watch?v=UPukeLcIWrM
tags: []
topics: ["Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# More Team Automation, Less Agent Autonomy

**Speaker not identified**

`AI DevCon (Tessl)` · `AI DevCon NYC 2026` · `2026` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=UPukeLcIWrM) · [Conference site](https://tessl.io/devcon/)

## Description

JetBrains ships IntelliJ IDEA three times a year, and in an agentic world the team wants to move faster. Katharina Dzialets, Product Manager at JetBrains working on Air, shares how three internal software factories evolved through a year of dogfooding: a cloud-based dark factory with preconfigured environments that proved costly and unpredictable, tightly scoped automations that teams chained into end-to-end pipelines, and a new team-first factory with human nodes, a shared inbox, cost forecasting and verification. Recorded at AI DevCon New York 2026.

What we cover:
– Why JetBrains is exploring software factories, and its dogfooding culture
– A cloud dark factory with preconfigured environments for a huge monorepo
– Why individual setups made factory output unpredictable
– Scoped automations running 35K times a day across the SDLC
– Chaining automations into end-to-end pipelines, from ticket to production
– A team-first factory: workflows, human nodes, a shared inbox and cost forecasting

Chapters:
00:00:00 - Introduction: JetBrains Air
00:02:16 - Why JetBrains wants to ship faster
00:03:32 - Dogfooding at JetBrains
00:04:39 - Factory 1: a cloud dark factory
00:06:32 - Where the dark factory fell short
00:08:41 - Factory 2: scoped automations
00:11:25 - Chaining automations together
00:12:22 - End-to-end pipelines in practice
00:14:38 - Factory 3: team workflows with human nodes
00:17:26 - Q&A

Register now for AI DevCon London 2027, June 7–8 at The Brewery, Moorgate:

Try Tessl today and build a software factory you can trust:

🔔 Subscribe for weekly videos on AI-native development

Where would you put the human in your team's software factory? Tell us in the comments.

## Transcript

*2,315 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=UPukeLcIWrM&t=0s)** So welcome to my talk. I'm Katharina and I work at JetBrains Air as a product manager. I also have a research background in software engineering, and I'm based in Munich. That's why I put pressure on you. And today, I'd like to tell you about the adoption of AI tools in JetBrains, especially about software factory adoption. So JetBrains is kind of old money in the world of developer tools. I believe everyone knows IntelliJ IDEA or PyCharm. And tools are changed. Coding tools are changing. Coding is changing. We are changing as well. So currently we are working on Air, and Air is a platform for agentic development. And I work in this team and we have three parts: Air in IDEs,

**[0:54](https://www.youtube.com/watch?v=UPukeLcIWrM&t=54s)** basically IntelliJ, PyCharm; Air Teams, tools for team collaboration; and Air Governance. Everything about our control, organization, management and spend. Our customers can try our tools in internal preview and for individuals. Air in IDEs plugin is available and we are going to have a listen. So please stay tuned and feel free to try. Well, as you can see on the slide, we utilize AI tools a lot. That's basically our spend for the last year and it grown significantly like a lot. I believe if we won't stop utilize AI so

**[1:47](https://www.youtube.com/watch?v=UPukeLcIWrM&t=107s)** much we are going to have troubles, but still. Also about the usage distribution. It's bimodal, which means as other companies on the market, we have a vast majority with the lowest spend and the high spenders which utilize almost 70% of the all tokens. And well, you'll ask me like, why do we spend so much? And I'd like to ask you, well, maybe someone remember her. How often do we ship IntelliJ? So be prepared. We still ship IntelliJ IDEA three times a year.

**[2:39](https://www.youtube.com/watch?v=UPukeLcIWrM&t=159s)** Like. Yeah. So. And for the agentic world, we can't afford this anymore. So we want to ship faster. Of course. And AI is a great helper here. Basically that's why we started to explore different tools, different formats and specially software factories. So today I'd like to share how our internal factories evolved, which lessons we learned. What exactly did we automate and where are we going next? And of course, I'll share it on a practical examples of the three internal tools. We'll start with a completely dark factory, then the opposite side of the spectrum automations, and then we'll go back to factory, but with a kind of different vision.

**[3:32](https://www.youtube.com/watch?v=UPukeLcIWrM&t=212s)** Very important side note, I said that I'm a product manager. By the way, do we have a product managers in the room? Hello. So a very important side note about how do we work at JetBrains. So we have a very, very strong dogfooding culture. Is everyone familiar with the term? Nice. So yeah. Our colleagues are so software developers. They love to dogfood this stuff. And well, if you survive the dog food then you're pretty ready to go. External. We have a lot of feedback, usually very direct one basically you're flooded with a bug reports feature requests. So all these internal factories, they were tested a lot by our developers.

**[4:25](https://www.youtube.com/watch?v=UPukeLcIWrM&t=265s)** This is a timeline how we tried the factories. And as you can see, there is a kind of every four months. We had the change in the approach. Let me start with the Dark Factory first. As I said, we are on a mission to ship faster, but it's kind of complex. If you develop in a monorepo which is 40 gigabytes, and if you'd like to run five sessions simultaneous, you you like, any laptop will die. So the local resources will be completely exhausted. Also, since the monorepo is huge and very complex, we will. We needed a different dependencies and tools for agents in order to able to run

**[5:19](https://www.youtube.com/watch?v=UPukeLcIWrM&t=319s)** tasks. And as I said, we were interested in tries. So first we were very eager to figure out with unattended runs. And in order to solve all this stuff, we built our first dark factory. That's how it looked like. It had preconfigured environments with environment variables, warm ups, all the necessary tools. That agent will perform basic observability. And of course it was in a cloud. That's how you can overcome all the local limitations. And it was kind of nice. As a first attempt, it solved lots of issues and folks were utilizing it a lot. But sometimes this happened. We had this like this run was lasted for

**[6:16](https://www.youtube.com/watch?v=UPukeLcIWrM&t=376s)** six hours. It failed like it produced nothing. It cost a lot. And we started to have such situations more and more. And yeah, that's not the optimal way. How to live with the factories. There were four key limitations, as you can see on the slide. So we had a lack of context management and orchestration was not so deep as requested by our users. As I showed in the previous slide, sometimes it was too costly and it was hard to control. But from my perspective, the key limitation was in different setups. This factory was intended as an individual tool, but it turned out that teams were interested in it and with a different setup, it was really hard to converge on the

**[7:13](https://www.youtube.com/watch?v=UPukeLcIWrM&t=433s)** same quality of the code output, which made output of the factory unpredictable. And we can't afford this if we build idea with the factory. So yeah. We decided to build a new factory on a new principles. But as I said, dogfood is very important part of our culture. And you can see the traces of this factory on production. For example, the Junie agent. It has observability. And artifacts and logs inspired by this factory. Air Governance also benefited from this factory as well. AI DevCon is coming back to London.

**[8:03](https://www.youtube.com/watch?v=UPukeLcIWrM&t=483s)** Our first London event sold out in June. After our second New York event this November, we're heading back to The Brewery, Moorgate, in 2027, with a bigger lineup and two full days of talks from the people actually building with agents. You'll hear honest takes on where the industry is at, real stories from teams adopting AI, the wins as well as the messy bits, and where they think things are heading next. It's on June 7th and 8th, and don't tell anyone, but we've got a really great deal for you. Scan this QR code to grab an early bird ticket for just £100. See you in London. The next step in the direction of the delegation. All the tool was automations, and on the contrary, automations were very, very scoped. We wanted to have a more control around it, and

**[8:59](https://www.youtube.com/watch?v=UPukeLcIWrM&t=539s)** the easiest approach was to decomposing, to start decompose as much as possible. That's how the UI looks like. And as you can see, that's a team tool. Basically, I have this automations stored in a project and there is not so much personnel. And also speaking of the names, they are very, very specific. It's easier code review, documentation maintenance. Pretty much of the runs. And yeah, I personally call it token consumption machine because once you set up the automation you forget about it, but it still runs until your quota and you're like, you can appear without tokens one day if you forget about completely.

**[9:52](https://www.youtube.com/watch?v=UPukeLcIWrM&t=592s)** So the design of this factory was the following. So it was one very scope task by run. It had a reusable environment, reusable instructions, skills whatsoever. Basically common. Grab all your context. And speaking of the context, the most important from my point of view, is access to tools and internal services that help to enrich the context a lot and make automations actually adopted across the whole company. Also, we had Observability layer and the set of all necessary triggers to run. People liked it. They started to adopt it. So now it's around 35K per day and across SDLC, I mean like traditional one, we have a such distribution,

**[10:47](https://www.youtube.com/watch?v=UPukeLcIWrM&t=647s)** so it tends more to test and deliver part. And it's kind of obvious. Well, because it's all shifted either extremely right or extremely left. And especially QAs suffered a lot with lots of generated code. That's why they were our first users. In terms of teams, I would say that very different teams adopted it. Product teams, security, legal, everyone was welcome. We helped a lot with the setup, so but at some point we started to see that some things are interconnected and they are literally connected in a chain.

**[11:36](https://www.youtube.com/watch?v=UPukeLcIWrM&t=696s)** Automations. Our tool was not built for that, but using external services like Issue Tracker or GitHub or some kind of internal tool for like bug collection or production management. We were able I mean, users were able to leave the comments, store the state, and pass the context from one automation to another. And that was quite popular. I listed like a top scenarios that people utilized and highlighted this human review. Human review was somewhere else. Despite all this limitations, we even had end to end chains.

**[12:28](https://www.youtube.com/watch?v=UPukeLcIWrM&t=748s)** I mean, from the ticket to like PR on the prod. And I'd like to share the two cases. The one is from their IntelliJ IDEA team. They. They wanted to somehow maintain a list of the plugins that they had no capacity to. And they made this wonderful setup with own review and share review. As far as I know, around 30 plugins will maintain this way and there they contributed a lot to the solution. Thanks to the folks. The second example of such almost factory is the development. Again, the problem is quite common.

**[13:20](https://www.youtube.com/watch?v=UPukeLcIWrM&t=800s)** You receive the new priorities from the management and you need to redistribute your team's capacity. And that's what they had. But they had a share and users and they needed to support it. And they built a nice pipeline that created tickets from the market research under the oversee of the product manager, of course, till implementation and PR in production. They used to have eight folks to support the CLI development. And with this pipeline, they managed to reduce it to the three and had no issues with the quality, which is quite impressive. Of course, soon we discovered the limitations of such approach as well.

**[14:13](https://www.youtube.com/watch?v=UPukeLcIWrM&t=853s)** As you probably figured out, there was a lot of manual orchestrations. People created scoped automations and they started to connect it. There was also a review trap, again, because they looked like too much in outcomes, and cost control was still cost problem, cost control problem was still not solved. And this led us to the next iteration as well. And surprise, we are going back to factory again. Yes, this one with the end-to-end pipeline. And on the contrary, this factory has completely different principles

**[15:06](https://www.youtube.com/watch?v=UPukeLcIWrM&t=906s)** that we were using in the Dark one. Here is the UI and the. As you can see, we have the the human node here. Because we still need human to intervene. We also have steps, runs, observability layer, etc. it's a work in progress. We experimented a lot. We lived with this POC for a couple of weeks. So it's changing, like every day. And that's how dog food is. Is performance in the company like there is no stable UI state or something else? Everything. Everything has changed every day. And the principles that we would like to build this version are the following. So we would like to have teams to encode their processes into the workflows,

**[16:02](https://www.youtube.com/watch?v=UPukeLcIWrM&t=962s)** because we find out that the factory is primary team tool. We also would love to have some kind of a smart notification mechanism here. I mentioned it as a shared inbox. And by this inbox I mean you have a different notifications from the agent or from the pipeline or new tasks, comment, etc. there are lots of signals and developers are overloaded and float is like somewhere in the hell. And to build some kind of nice notification system would be helpful. Also, we'd like to invest a lot in cost management and here I mean this management persona. I as a manager would love to figure it out. Figure out which factory line should I start and which is not by a predicted cost in

**[16:59](https://www.youtube.com/watch?v=UPukeLcIWrM&t=1019s)** advance. That's how I can allocate resources better. It would be really interesting to solve this. And last but not least, it's not on the slide. But I believe everyone was thinking about it. It's about verification. So we need verification nodes to be able to continue maintain the same quality as we need. That was it. Thank you so much for your attention. If you'd like to ask any questions, please let me know. Know I was very curious. So at the end you see the I guess even the title here. I'm just curious what is the biggest difference between the categories,

**[17:55](https://www.youtube.com/watch?v=UPukeLcIWrM&t=1075s)** because it seems like you still need a visual with you to write. Or is that just completely automated? I would say that the difference is in kind of balance between the human intervention and the automated work. There should be not so much human intervention from my point of view, and I would expect to have it on the very, very beginning of the pipeline. When do you verify the specification or some kind of different form of input? But still, if something goes wrong, it would be very nice to have a smart handoff between local and the cloud so you can, as a user, steer the factory in a way that you do your average local task with your setup, but you're using the common setup.

**[18:51](https://www.youtube.com/watch?v=UPukeLcIWrM&t=1131s)** Thank you, thank you. All right. I guess that's it. Yeah. Thanks so much, Katharina. Another round of applause, please. That was a fantastic.
