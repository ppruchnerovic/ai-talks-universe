---
id: GiqyYQdYoIY
title: "Code with Claude 2026 | Tokyo"
slug: code-with-claude-2026-tokyo
conference: code-with-claude
conference_name: "Code with Claude (Anthropic)"
category: "AI engineering & agents"
edition: "2026 Japan"
year: 2026
speakers: []
channel: "Claude"
duration_min: 527
published_at: 2026-06-09T09:26:25Z
video_id: GiqyYQdYoIY
url: https://www.youtube.com/watch?v=GiqyYQdYoIY
youtube_url: https://www.youtube.com/watch?v=GiqyYQdYoIY
tags: []
transcript: true
---

# Code with Claude 2026 | Tokyo

**Speaker not identified**

`Code with Claude (Anthropic)` · `2026 Japan` · `2026` · `527 min`

[Watch the recording](https://www.youtube.com/watch?v=GiqyYQdYoIY) · [Conference site](https://claude.com/code-with-claude)

## Description

Pull up a chair and watch the main stage live from Code with Claude Tokyo. We're discussing what's new with our models, the Claude Platform, and  Claude Code. After that, listen as Canva, Mizuho and NRI share what they've shipped. Join us as we show you what's been keeping us up (in the good way).

## Transcript

*27,550 words · source: yt (en, exact timings)*

**[0:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15s)** [music] Hey, hey, hey. >> [music] [music] >> Please welcome to the stage head of engineering for the clogged platform at Enthropic. Caitlyn Leso Anthropic called Engineering

**[1:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=68s)** Caitlyn Le. Good morning, Tokyo. This is the first time that we've brought Code with Claude to Japan and we're grateful to spend the next couple of days with all of you. This morning, we'll be talking about our models, our platform, and our products. But before we get into it, I want to start by sharing that just a few hours ago, we released the fifth generation of Claude models, Claude Mythos 5 and Claude Fable 5. These are our two most capable models ever. >> [applause] >> Diane, our head of product for research,

**[1:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=118s)** will join us shortly to share a lot more about why these models are so special. I lead engineering for the Claude platform. The platform gives developers the tools they need to build systems on top of Claude to harness its intelligence. This is the highest leverage way for us to help solve the world's most important problems. And this is why Anthropic is a platform company. Developers all over the world, many in this room today, produce far more value on top of the platform than we could ever build on our own. So, let's start with what I'm seeing from our customers lately. There's an incredible volume of powerful application shipping right now, and a lot of it is coming from right here in Japan. Rakutin is one of our favorite customers

**[2:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=166s)** to work with. Their team went from using cloud code to accelerate development to building on cloud manage agents to power custom internal agents across engineering, product, sales, and finance. One of their product managers coordinates teams of agents exactly the same way a leader manages teams of humans. Now, they're shipping major releases every two weeks instead of only once per quarter. And it's the same across Asia-Pacific. Another great customer is Canva, the Australian design platform that hundreds of millions of people use. Most of their users have never written a line of code. But with the help of Claude, Canva code changes all of this. Within a design, you can just ask for something interactive like a map, a

**[3:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=215s)** calculator, or a widget. And Claude built it into a working mini app ready to drop right into your page. All around the world, people are building new systems and applications powered by Claude that nobody could build before. And we're all feeling this shift. The landscape is changing faster than ever. Things that weren't possible yesterday have become possible today. We're on a mission to keep raising the ceiling of what's possible to build by making models that are increasingly capable. A couple of years ago, the frontier of model development was just the ability to draft a really simple commit message. And then one year ago, we were standing on stage at our first ever code with Claude event. Opus 4 was the headline. And it was mind-blowing at the time that

**[4:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=265s)** Claude could build an entire feature on its own. And then six months ago, agents were able to run overnight to complete longrunning and autonomous tasks. Two months ago, Mythos read the entire OpenBSD source tree and found a 27year-old vulnerability that had slipped past human reviews and static analysis for almost three decades. And earlier today, we released Mythos 5 and Fable 5. Fable 5 is state-of-the-art on nearly all tested benchmarks of AI capability, showing exceptional performance in software engineering, knowledge work, scientific research, vision, and more. These jumps keep getting bigger, but the time intervals keep getting shorter.

**[5:14](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=314s)** But even though these model capabilities are improving on this exponential, most business capabilities are still on a linear. So there's this growing gap between what AI can do and what it's actually doing for people. Closing that gap is our collective opportunity. And that is why we built the cloud platform. It gives developers the tools they need to build more powerful agents. Year-over-year API volume is up nearly 17 times on the platform. We've been shipping a lot and there's a lot more on the way. Over the next couple of days, we'll share where we're headed and we'll learn more about what you're building. Our goal is to make our models, our platform, and our products work better for all of you. So this morning, we'll dive into each.

**[6:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=364s)** First, Diane will talk about our models. She'll share more about our latest frontier models, Mythos 5 and Fable 5, and what's coming next. Next, Angela and I will walk you through how you can build and deploy agents at scale on the Cloud Platform using Cloud Managed agents. And today, we're excited to share that we're shipping brand new cloud managed agents features. You can now schedule deployments to have your agents run on whatever cadence that you need. And you can store environment variables in vaults so your agents can securely make authenticated API requests without giving them access to the keys. Finally, Cat will walk you through the latest in Cloud Code where the average developer is now spending 20 hours per week with Claude. She'll cover the latest features like the new agent view

**[6:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=412s)** and dynamic workflows. And all of this comes back to you and what you're going to build. Because most people will never integrate with the Claude API themselves. They'll never open a terminal and type Claude. They'll experience AI through something that one of you built on the Claude platform like a saleserson walking into a highstakes meeting fully briefed by Slack agents or a lawyer getting a brief out the door faster than ever with Lagora. or a developer using any one of the world's best coding agents. This is why we're a platform company. Every day I'm amazed by the collective impact that you're all having building solutions to the world's most important

**[7:40](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=460s)** problems. So, thank you for being here, for partnering with us, and for showing us what's possible. Aratu go. >> [applause] >> Please welcome Diane from our research product team for your first deep look at our newest models. >> Please welcome to the stage head of product management for research Diane Penn sto anthropic research product management Diane Penn sama >> [music and applause] >> Hi, good morning Tokyo. I'm Diane and I

**[8:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=511s)** joined Anthropic in 2023 and I've been a part of every version of Claude since Claude 2. For those of you who are counting, that's bringing 21 versions of Claude across Haiku, Sonnet, Opus, and now Fable, and Mythos to end users and developers like you. Our most recent launch happened just a few hours ago. We released Claude Fable 5 and Claude Mythos 5, the first generation of our fifth models. Fable 5 is the most capable model we've ever made generally available. It's based on the same foundations as missile 5. These models are already accelerating

**[9:19](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=559s)** our work at Enthropic. And for developers like you, Claude will be able to be stronger and your starting line will move forward. We talk a lot about the exponential at Enthropic, but what does this actually mean? For us, as model intelligence increase, we believe the value of use cases it creates increases exponentially. For example, agented coding that many of you are using today is far more valuable than simple autocomplete from just a few years ago. And we are already seeing this with Fable 5. Let's start with coding because we believe that's where most of you will feel the magic first. Fable 5 performs

**[10:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=608s)** the highest on Sweepbench Pro. But the benchmark itself underscells the story. The longer and the more complicated and sophisticated the task, the farther the gap between Fable and every other model out there. Two things drive that gap. The first singleshot correctness. Give Fable 5 a complex well specified problem and it will nail it on the first pass. Early testers have told us about single prompts that essentially create work that would have taken days or even weeks for a group of teams. The second is long horizon autonomy. Fable 5 can run for days on a single goal and stay coherent the entire way.

**[10:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=658s)** It'll remember your specifications even on tasks that span millions of tokens. And it can dispatch sub agents, keep them on track far more dependably and with more costconsciousness than any other model we shipped. One more thing, Fable 5 isn't just good at writing code, it's even better at reading it. It's better at tree outing outages and better at digging through your repo history to figure out what's broken when, and also to proactively surface suggestions for making it better. Fable 5 is just as much of a step outside of coding. Start with a work that your organizations and companies actually run on. Whether that's

**[11:45](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=705s)** financial analysis, documents, slides, spreadsheets, Fable 5 manages that work end to end. It'll stay follow instructions, stay on scope, and what it creates back for you will be professional grade because this is a model that we built for workflows at scale. It's also better where requests aren't clean. What we've seen is that when you give Fable 5 something messy, multi-threaded, and ask it to figure out what to do next, it could do that work and outshine other versions of Claude. Fable 5's version is also the best in the industry. It can read dense technical images, web applications, plots, diagrams, charts far more

**[12:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=755s)** accurately than any other version of claude we've shipped before. Now, everything I've talked about is about the upside of a model of this capability. But intelligence of this magnitude cuts both ways. Two months ago, we launched Project Glass Wing and made Mythos preview available to a small group of partners because its capabilities in cyber security were strong enough to be potentially misused. Since then, we built a new safeguard system and that safeguard system allows that same intelligence to be shipped and created and used by everyone with Fable 5. This is a little of how it works. When a request first touches cyber security,

**[13:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=805s)** biology or chemistry topics, Fable will route it to our next most capable model, Opus 4.8. The response is clearly labeled and your charged opus prices. We know this is not perfect yet. researchers doing legitimate work in these fields will sometimes hit a block and reroute. And we're continuing to work on that. But that's the type of trade-off that allows our most capable models to be in everyone's hands today as of this morning instead of months from now. And our customers are already finding value with Fable. Rakutin found that the highest effort levels Fable 5 reflects validates his work and for them that makes autonomous

**[14:16](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=856s)** automated operations possible at scale. Cognition ran Fable 5 against their frontier coding eval scored the highest of any model they've tested. They highlighted the long horizon reasoning and how it generalizes to unfamiliar tools, complex context right out of the box. And Jensen Spark told us that Fable 5 came out number one in their evals, winning head-to-head against every version of model they've tested. It's actually the strongest on the hardest tasks such as UI design and game coding. So, what about Mythos 5? It's the same underlying model as Fable 5, but with

**[15:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=905s)** the cyber and bios safeguards lifted. For Mythos preview, we showed what this model class can do, and Mythos 5 is a step beyond that. It's available today for our CL glasswing partners as part of Project Glasswing. Later this month, we'll begin enrolling more researchers from life sciences to access Mythos 5 because those same capabilities that make biology risky are actually the same ones that have the highest impact for real good with AI. So, as developers, what can you do with Fable 5? One metric I like to look at to make sense of all of this change is time horizon.

**[15:53](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=953s)** which is how long a model can work autonomously before losing coherence on what to do next. With Fable 5, we've seen agents that are proactive and know what to do without being told. These agents can be responsible for higher level goals, responsibilities that require judgment, collaboration, and proactive taste. For example, instead of asking Claude to write a project update, you can now ask Fable to make sure the project stays on track for the whole week. Instead of asking Claude to produce a financial forecast, you can tell Fable to own, update, iterate, and improve on the forecast to keep it accurate.

**[16:45](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1005s)** As you've seen today, the exponential keeps moving. We need to build for emerging capabilities, not just for today's current models. We expect future versions of Claude to be more capable than the one that even we are releasing today. And Fable 5 and Mythos 5 are just a glimpse into that future. So, as developers, how do you take advantage of all of this change ahead? First, you should design for the next version of Claude, not just the current one. What we've seen is that countless times, the developers who win are the ones whose architectures, harnesses, and product experiences are ready to absorb this next jump in intelligence.

**[17:36](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1056s)** Claude is intelligent and resourceful. And as models become more intelligent, they can actually do farther with more basic primitives such as a file system or sandbox computing environments and far less with sophisticated or too complex harnesses. As models get more intelligent, you will also need to start making harder eval prototypes for experiences that may not work yet. This is how you actually know that the exponential is moving underneath you. When a task or a prototype or a product experience that wasn't quite always working well starts working, that's a signal to ship something magical that you couldn't have done before. And finally, as the pace continues to

**[18:26](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1106s)** accelerate, the teams who win are the ones that get the most out of quad with model upgrades and treat them as business opportunities. You should make model upgrades easy. This means things like automated evals, testing processes, and making sure that you stay hands-on testing, pushing, creating new things with new versions of Claude. And this is how you'll know new capabilities will be enough to deliver new experiences for your customers. We're seeing the exponential continue, which means that Claude will get smarter and be able to pick up new capabilities at scale. And you as developers are some of the first people to feel that. You're the

**[19:16](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1156s)** ones who actually can experiment, build new products, and are the first to find opportunities for new markets that others don't see. And we can't wait to see what you'll build next with Fable 5. And now, Angela and Caitlyn are going to show you a bit of how the Claude platform can make this a reality come to life. Thank you so much. >> [applause] >> Please welcome to the stage head of product for the Claude platform, Angela Jen. Stage platform, Angela Jang. [music] Last night, while we were all asleep, a

**[20:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1208s)** product somewhere noticed that it was broken. This product read its own error reports. It found the bug and it wrote the fix and rolled it out to all the users. By the time the team actually woke up, the problem was gone and the change log was already written. Now, in this situation, there was no standup. There was no ticket. And this is what a native AI company looks like. This is not a company where people just use AI to do their work, but instead it's a company where work itself runs on the substrate of AI and people decide what the outcome should be. Now, this story can be a reality if you have the right ingredients. And there's three things to that. The first is the harness, the second is the context, and the third is the infrastructure. These three are what turn raw

**[20:57](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1257s)** intelligence into true business outcomes. And that's exactly what the Claude platform provides. We give you aic harnesses, context management tools, and production-grade infrastructure that allows you to become truly AI native. Recently, we packaged all these together through Claude manage agents, our new product offering. Fable 5 is the best model for building longunning agents and manage agents is purpose-built for Claude. This means when you put these two together, you're able to actually get better agent outcomes with significantly less effort. Okay, let's talk about the harness. So the harness is what gives claude models the ability to actually do work. It includes tools, an environment, and the permission to act. With a harness, the model doesn't just tell you about the

**[21:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1306s)** fix. It actually makes it happen. You don't want AI that just gives you helpful suggestions. You want AI that can actually do the work. With quad manage agents, we offer an agentic harness that separates the brain from the hands. The brain decides what to do and then we spin up sandboxes or hands to execute the work as needed. Our harness also has an iterative base ability to operate on an outcome. You specify what that outcome is and then a managed agent is able to iterate until it actually achieves it for you. Second, let's talk about context. Now, a model is only as good as the context that you actually give it. We offer a 1 million context window so that you can

**[22:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1353s)** have agents that consume high amounts of content without any degradation. But that's not all. We also offer our agents memory so they can actually remember what they've been doing. We also give our agents the ability to read and write skills of their own so they can fill in the knowledge gaps that they're missing. And lastly, we give our agents the ability to dream so they can inspect over their own previous trajectories and identify how to self-improve. And lastly, let's talk about infrastructure. Now, if you build really longunning autonomous agents, this requires extreme scale and reliability. This is one of the hardest parts to get right. Cloud manage agents automatically spins up and down sandboxes and has the ability to generate multiple agentic fleets when needed to help you optimize

**[23:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1401s)** for reliable and persistent agents that just get the work done without all the hard work. Building self-improving companies is something that can happen today. And we've worked with so many companies that have built agentic systems on cloud managed agents. And they've been able to do that 10 times faster because they didn't have to roll their own harness or manage their own context or honestly build up all the infrastructure that they need. Notion actually used manage agents to power agent orchestration directly within their product. As a result, their users can delegate complex [music] longunning work to claw directly inside their workspace. And Notion isn't alone. ASA used managed agents to build AI teammates. These are collaborative AI agents that work

**[24:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1448s)** alongside humans inside Asauna projects. And these agents can take on tasks and complete deliverables. Now, I'd love to welcome Caitlyn back to the stage to show what an AI native company can look like if you build on Cloud Manage agents. [cheering and applause] >> [music] >> Back in February, Claude became the official thinking partner of the Atlassian Williams Formula 1 racing team. Competing in F1 racing requires a great driver who knows the track really well. But it also takes a team of engineers and researchers to build a rocket ship on four wheels that can go almost 400 km hour.

**[24:57](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1497s)** To show you an example of cloud managed agents in action, we worked with a fictional racing team called Shankiro Racing. Um, and we helped them build a dashboard to analyze their car. Let's see it in action. So, here we have our dashboard for Shanki Racing. And the way we've set this up is we have these four research projects on the side. Each of these research projects is backed by an agent that was built using cloud managed agents. So, we have our aerodynamics, we have our tire temperature, power unit, and driver safety. And for each of these agents, what they're going to do is research what needs to change in order to make our car better on each of these fronts. So, we can go over here and we can choose to kick off a run. Let's start

**[25:45](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1545s)** one off now. So, while that's running, let me talk about how these agents are built. Like Angela mentioned, we can use the concept of outcomes. outcomes helps us tell each of our agents, here's what good really looks like. And so when our agents run, we provision a separate greater agent that goes and tells the original agent, did you do a good enough job? And if not, keep trying. So one of the new features that we have within cloud manage agents is not only the ability to on demand kick off a run of an agent, but also to schedule an agent. To show you that, I'll use the claw developer console. If I were a developer working to build cloud managed agents, I would use this console for things like observability and tooling to help make my agents really great. And so here you can see within our sessions we

**[26:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1592s)** have the run that I just kicked off. Um, and then maybe we can check out another one here. You can see that uh, you know, we can have richer observability around all of the things that the agent is actually doing. Um, but one of the more important things that we launched today is this concept of deployments. Um, and we are Wi-Fi is not on my side right now. [laughter] Okay, maybe. All right, we'll skip it. The concept of deployments allows us to choose to kick off a scheduled run of an agent on demand. Um, and so what I was going to show you, but I'll just talk through out loud, is the idea that maybe we want to run a nightly driver safety check. We want our driver safety agent to run every night and take all its

**[27:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1641s)** learnings and tell us, you know, like what should we do better for driver safety? We can go ahead and schedule that every night overnight. But it's not enough to make these agents really easy to set up and use. Like Angela mentioned, it's really important that these agents can be really powerful. An interesting thing about agents is most of the time they're starting from scratch. They're not using all the context they had from their past sessions in order to do a better job the next time around. So we've incorporated the concept of memory. So each of these four agents has a file system where it can write learnings to memory as it runs. But even more important than that, we've built the concept of dreaming. So our agents can decide maybe I'll take a look back at all these past sessions and write skills or write additional things to memory so that I can do better next time around. And so I can hit this

**[28:09](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1689s)** stream button. Um, and this is going to be slow because the Wi-Fi again is not on my side. But, uh, what would happen is our agents will look back on their past sessions and write these learnings so that they can do better the next time around. All of the features here, everything to build a dashboard like this to help an F1 team build a really, really highly successful car are available today within cloud manage agents. So everything you just saw like outcomes, schedule deployments and dreaming are available today on the cloud platform. Developers everywhere can start building with Fable 5 and managed agents today. Now Cat will talk about how cloud code is making it even more fun to ship as a

**[28:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1738s)** developer. >> [applause] >> Please welcome to the stage head of product for Cloud Code Cat Woo stage cloud code. [applause] Caitlyn and Angela just showed you how to build production agents on the Cloud Platform. With Cloud Code, we're bring that same leverage to your work as a developer. Not agents you ship to customers, but agents that ship code for you. First, I want to thank all of the developers in the room today here and

**[29:47](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1787s)** watching online. Thank you for trusting Quad Code back when sonnet 3.7 was our frontier model and when our product was rough around the edges. Your support is what makes the team so excited to come in every day and make the product even better. Let's back up to why Quad Code exists. The mission of Quad Code is to bridge the difference between an idea and a shipped product. The way that we enable this is we build tools that elicit the frontier intelligence from our models and we make these tools accessible to every builder. And we we don't think of ourselves as having a finished road map to share with you. We think of ourselves more like

**[30:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1835s)** mountaineers climbing alongside you in terrain that none of us has fully mapped yet, figuring out what works together as we go. and we're growing with you with increasing AI capabilities and helping you navigate new challenges that emerge. I remember just last year I would give Cloud Code a task and I would review every single edit that it made, giving it detailed instructions about what it should do instead, walking through on every little detail of these simple tasks. Now, many of us are using auto mode to delegate permissions to Claude and only checking in after Cloud Code has already tested its changes and put up a PR

**[31:24](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1884s)** that's ready for our review. Quad Code started in the CLI and this is still the place for power users who want a minimal text interface and the most control and customizations. Then we added the IDE for users who want the same powerful agents but want to follow along with all of the code changes. Then we heard from many of you that you're running multiple quad codes in parallel which we you've affectionately called multi-clotting. And we've added two new interfaces to help make that easier. The one that I use most frequently is Claude Code on Cloud Desktop. It's designed for people who want this full

**[32:11](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1931s)** screen graphical interface with built-in previews, a sidebar control plane, and the ability to render images and rich outputs. We've built desktop to be a single view across all your local and cloud sessions with visual indicators of which agents are working and which ones need your input. Next is our newest surface, quad agents view in the CLI. For those of you who want a control plane without having to ever leave the terminal, you can see what's waiting on you, what's running, and what's already done. You can reply in line to unblock or jump in and out of any session without losing your place. The VS Code IDE extension and the cloud

**[33:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=1981s)** code on cloud desktop app are built on the cloud agent SDK. The same one that many of you are building on today. Many enterprises have now adopted these quad code tools wallto-wall. At Enthropic, engineers on average ship 8x more code than they did in past years, even as the size of our engineering team has grown substantially. Together with you all, we're excited to discover and redefine what the future of engineering looks like by embracing new challenges that come and by building automations powered by Quad to attack each one. Here's some of the feedback that we've heard from our users and the products

**[33:49](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2029s)** that we've built to address each one with the help of folks in this community. We heard from you that you want to spend less time on code review. So, we shipped a code review product that deploys a team of agents to catch critical bugs in your PRs. Thousands of companies use this every day and this includes all internal anthropic teams. We heard from you that you really want to code on the go. So, we launched remote control and quad code on iOS and Android. Now, you're no longer walking around with this laptop that's half open or stuck at your desk. You can now go to a park, touch grass, and still get your coding tasks done.

**[34:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2079s)** We and we heard from you that you want to run cloud code on new tickets and so we built routines. You can configure this once and it'll run on a schedule, a web hook or an API call to kick off cloud code on the right task. So the work that used to require a human to manually kick off, routines can take care of for you. and we heard from you that you're landing so much code that your security teams are having a hard time keeping up. So, we built cloud security. It scans your codebase overnight. It flags a range of vulnerabilities, including the ones that it believes are most critical, and lets you kick off a cloud code session to tackle each one.

**[35:29](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2129s)** And then finally, we heard that you want better ways to run ambitious large-scale tasks across your codebase like major refactors and migrations. So, we launched dynamic workflows. This lets you kick off cloud code to run in parallel across tens or hundreds of agents in a deterministic structure to get your most ambitious tasks done. Each of these primitives composed together so that we can more easily adapt to the future of engineering. Everything I've covered is something that an individual developer can pick up today. But it's especially exciting to see how a range of companies are adopting this at the scale of entire engineering orgs. For instance, Spotify uses Quad to

**[36:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2178s)** migrate thousands of repos. The team built a background agent on the quad agent SDK that reads a migration plan in plain English and then kicks off a fleet of agents that opens PRs. They're merging over a thousand PRs a month into production and they've cut migration time down by 90%. Another example is Merkari, Japan's consumer to consumer marketplace. At Merkari, the entire engineering team runs on cloud code and they've measured that engineering output is up 90% year-over-year using the tool. We see this across the industry. Millions of developers are getting more

**[37:06](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2226s)** done and at higher quality than before. Now, let's see what this actually looks like in practice. I'm excited to show you one of my favorite new features in cloud code. For this demo, let's imagine we're Kaizen operations and we create apps for engineering teams. Right now, our marketing website is in English only, but we want to launch to 13 additional markets. So, we need to localize our site before the launch. Let's start with how we would normally do this with one quad code agent. We'll run this prompt asking Quad to convert our website to Japanese. And we'll speed things up as it works. Quad

**[37:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2274s)** explores a codebase, creates a language picker for the website, and translates all the text to Japanese. So, Quad's finished its work and let's check out the results. Here we can see a full marketing site and view the new Japanese translation from Quad. It took Quad about 3 minutes to complete this one translation and we have 12 more to go. If we did this one at a time sequentially, it would take us almost an hour and lots of manual prompting with Claude. So instead, we'll use a dynamic workflow which will let Claude create a repeatable process and run each of the new translations at the same time in parallel. We'll prompt Quad to use a workflow for

**[38:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2324s)** our translation to these 12 new languages. Quad creates a workflow and once it's ready, we can open it in the side pane and watch as it works. This is a powerful feature of the call desktop app. You can see all 12 translation agents running at the same time. After the translation agents complete, it's going to create 12 more agents to verify its work across these new languages. This work would have previously required us to run 12 separate tasks and it can now be done in just one prompt. And we can also save this workflow as JavaScript code and reuse it for future translations.

**[39:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2370s)** Let's check out the output. Quad has now created 12 new versions of the website, all localized with one action. We can see them all in the drop down and check out some of the different languages to see its work. This is just one example of dynamic workflows. We can use them for large-scale migrations, codebase audits, or doing performance optimizations. Any large job that requires running many agents at once in its terministic structure. Everything you just saw is available today, including dynamic workflows and cloud code in the Cloud Desktop app. And our newest model, Quad Fable 5, is available to all Quad Code users. So you

**[40:20](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2420s)** can use the latest intelligence wherever you use Quad Code. We're so excited for you to try out these new features and for you to let us know what you think. We hope they continue to help you close the gap between an idea and a shift product. And this is really what every talk today was pointing at. Dian's capability curve, Anjo's agents that run on infrastructure that you control, and what I just showed you. These are three layers to one story. The remaining gap is just how fast we can put these great capabilities to work for us. I encourage you to spend the rest of today exploring these layers. Join research talks if you want to learn more

**[41:09](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2469s)** about the latest model capabilities. Join cloud platform sessions if you're building your own agents for your end users or join quad code workshops if you want to learn more ways to bring quad code into your day-to-day development work. All of this runs on Quad Fable 5, the best model we've ever shipped for aentic work and it's live today. Thank you all and enjoy code with Claude. [applause] So good. So good.

**[42:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2525s)** >> [music] [music] >> Hey, good to me. [music] Hey, hey, hey. [music] la.

**[43:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2601s)** Mhm. Baby, baby. >> [music] [music] >> Heat. Heat.

**[44:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2686s)** >> [music] >> Hey. Hey. Hey. Hey everybody. Hey Heat. Heat.

**[45:57](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2757s)** Are you >> [music] [music]

**[46:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2816s)** >> Yeah. [music] Yeah. >> [music] [music] >> Oh yeah. [music] >> [music]

**[48:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2880s)** [music] [music] [music] >> Yeah, she's huh? >> [music] [music]

**[49:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=2945s)** >> Hey, hey, hey. >> [music] >> Hey hey [music] oh hey oh hey oh hey oh hey oh Come

**[50:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3004s)** on. Ouch. Hey, [music] hey, hey. Hey,

**[51:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3064s)** hey, hey. Damn it. 1. 1.

**[52:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3147s)** Down down down down down down down down 1 2 3 1 hey 1 3 2 1 I just want you. [music]

**[53:34](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3214s)** Down down down down. Noo. [music] [music] N.

**[54:23](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3263s)** [music] Number n. [music] >> [music]

**[55:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3333s)** [music] [music] >> Number [music] [music] jing. Hello. N.

**[56:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3406s)** Hey, hey, hey. >> [music]

**[58:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3512s)** [music] [music] >> dick. Dick. Down down down [music]

**[59:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3570s)** take down down. [music] Down. [music] Down. Everybody Sh. [music]

**[60:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3641s)** Down. Heat. Heat. N. Down. [music] Under. >> [music]

**[61:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3706s)** >> That's all. >> [music] [music] >> Hey. >> [music] >> Happy.

**[62:49](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3769s)** Heat. [music] Heat. Come >> [music] >> on.

**[63:40](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3820s)** Come on. Hey, [music] for real. for real. For real.

**[64:47](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3887s)** for real. For real. >> [music] >> for me. [music] He feel >> [music]

**[65:36](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=3936s)** >> Heat. [music] Hey, heat. Hey, heat. >> [music] >> We are talking. >> [music]

**[67:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4024s)** >> Hey. Hey. Hey. >> [music] >> Happy happy me. [music] Yeah. [music]

**[68:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4080s)** Yeah. Yeah. >> [music] >> Hey, hey, hey. [music]

**[68:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4134s)** Heat. Heat. N. Heat. Heat. N. Mhm.

**[70:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4201s)** Mhm. >> [music] >> Hey. Hey. Hey. I'm happy.

**[71:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4265s)** One, two, three, four. Hey, hey, hey. 1 2 3 4

**[72:14](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4334s)** Thank you. [music] Hello. Hello. [music] >> [music]

**[73:20](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4400s)** >> Hey, come on. [music] Hey, [music] hey, [music] hey. Hey,

**[74:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4458s)** hey, hey. Yeah. [music] [music] Heat. Hey

**[75:13](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4513s)** girl. Hey I'm a [music] [music] Okay. [music] Heat.

**[76:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4564s)** [music] >> [music] >> I'm a [music] >> [music] [music] [applause] >> Hi everyone, I'm Charmaine and I'm on

**[76:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4614s)** the applied AI team here at Anthropic. Our team sits at the intersection of product research and all of our amazing customers. I'm really excited to be here today to tell you what's new in Claude Code, but I'm also very grateful to be here in Tokyo. I grew up in Hong Kong myself and so it always feels really nice to be closer to home. I used to work at places where we'd spend 45 minutes going over a deep dive of a feature that we built over the span of a quarter. This session is not that. The team shifts so quickly and there's so much to show you and so I'm excited to dive right into it. I'll quickly go over the agenda of what we're going to talk about today. Our new features have largely fallen into one of

**[77:43](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4663s)** two categories. The first one being developer experience. How we're making quad code better for you as you spend more time in it. Second, autonomy. How do we help Claude help you do more while you're away from your keyboard? And then I'll also quickly wrap up with what I don't get to cover today, and I'm sure there's lots of it. So, let's talk about developer experience. First, this is probably the thing that we care about the most. Even as cloud handles more longunning tasks on its own, we are deeply invested in the human experience, the best tool is the one that you actually enjoy using. So, first up is remote control. There's

**[78:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4713s)** this running joke on our team where you kick off a long running session, you need to step away temporarily, and it suddenly feels like you are abandoning your child at daycare. What's even going on in your phone? So remote control fixes that. You start a session on your machine and you can pick it up from your phone or the browser. My favorite pattern is actually kicking off a longunning task, going on a walk, and as ideas come to me, I'll ask sub agents to spin up different tasks or check on my phone. I've actually been doing that during this trip as well. Yesterday, right before dinner, I kicked off a task and then I was able to check on it on my phone while waiting for my delicious pizza. I'm going to quickly jump into a demo here and show you what this actually looks like.

**[79:23](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4763s)** So, I have a running session of cloud code here and I just asked it, can you tell me more about this repo? And then I said, it's demo time. Please run the server. Let's hope the um Wi-Fi works well here. But this is a demo repo of Excal. Excaladraw is a virtual whiteboard that you can draw on. I'll show you what that looks like if you haven't seen it before. Uh you can draw fun diagrams directly on it. You can even type hello code with claw Tokyo. This is a really great um technical architecture drawing uh surface. It's also open source. So really recommend checking it out if you haven't already. Um but I'll go ahead and show you what this looks like if I kicked off slash remote control. So what this will do is actually connect the

**[80:11](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4811s)** session that I have running locally to the remote session. So you'll notice here that remote control is now active. I can continue coding in the cloud mobile app if with the QR code here or you can go back and actually click on this link here to open the session on the web. So I'll show you what that looks like. You'll notice that the same session that I just had running on my local CLI is now running on the web. Let's try it again. So, these two sessions are now hooked up and theoretically I'd be able to access this directly through the web. Here you'll see the same prompts that I just

**[80:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4858s)** shared. Run the app. Can you tell me more about this repo? Run the server again. And these two sessions are now hooked up. I can also then say, can you give me a quick oneliner recap of the repo just so you remember before we head into the rest of the demos what we're looking at. And so you'll see here that it's running the task. And if I go back to my terminal, you'll see the same prompt there. And these two sessions are now hooked up. All right. Now, let's go back to the presentation. I don't think I even need to ask for a show of hands here about who has experienced flickering while you're using cloud code in the terminal. And we are very sorry about that. We are here

**[81:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4906s)** to make amends. For context, our previous rendering approach appended to the existing terminal scrollback and so even a single misalignment would trigger an entire repaint and that caused the flickering. Our new full screen mode virtualizes that scroll back entirely. So you get flicker-free output. You get clickable elements directly inside your terminal. And your memory usage stays flat even for very long running sessions. I'm once again going to go back and show you what that actually looks like. So as I go show you this tab here, you can notice I'm now using Fable 5 after the launch today. And I'm going to run / 2e full screen. So 2E stands for the terminal UI. This preference that I have

**[82:34](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=4954s)** now we will apply to all future sessions. I'm also kind of getting tired of typing. So I'm going to do /voice here and toggle voice mode on. So what's going to happen here is when I press space, it'll start recording the prompt that I have. So write a file containing five friendly jokes about Tokyo. All right, it looks like that work. [laughter] Um, all right. Let me try one more time. I might try to swap the Wi-Fi here and see if that works. Um, if that doesn't, we can move. All right. All right, looks like it's taking a

**[83:38](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5018s)** while. Um, I think we can go ahead and fall back to the video if possible where we show the same thing. All righty. So, uh, this is showing exactly what I showed you there, right? You run /2e full screen. Now, it enter enters into this mode where you're able to look at the diff in line, click on file paths directly and view the file directly within your terminal without exiting. And as your terminal gets really long and your session starts overgrowing what the window is, uh, you can also scroll up and down and not have any flicker. All right. Let's go back to the presentation slides. All right. So, some people on the team really love

**[84:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5067s)** the terminal, but others have been gravitating towards cloud code on desktop and web. So, we've largely redesigned it around one question. What is the difference when I want to manage 10 sessions instead of one? And so once again, I will go back into the demo and see what we can do here. All right. So take a look here. This is Cloud Code Desktop. If you haven't visited it in a while, you'll notice that there are some new changes. This is the code tab within Cloud Desktop. And within it, you can see a series of sessions that I have running on the side. You can even see the session that I had a little bit earlier. And you can actually see the background tasks that I have running as well. the server is running in the background.

**[85:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5115s)** Um, you can also sort by uh different statuses. I like just sorting by active because I want to see uh the active sessions that need my attention instead of everything. You can also group by anything that you want. Um, you'll also notice here that there is a top right you can preview the session. You can view diffs directly in line. You can also once again look at background tasks or the plan that you have or even all the files it has access has has access to. Um so I'm going to go ahead and go here and actually open the plan that Claude generated. Uh so for context I have a prompt here that says I want to add a new shape to the whiteboard drawing tool. Uh and on the top bar I want to create this shape cla logo. And so here you notice that I have the plan on the right. And I actually

**[86:06](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5166s)** want it to have instead of just the pixel art crab, I also want to make it rainbow. And so I can leave that comment directly in line and hit revise. And that'll kick off the edits clawed. You'll also notice that I have another session here and you can view the diff directly in line. You can even pull the sessions next to each other and view them side by side. Um, one more thing here that I really love. There's an effort dial on the very bottom. Um, you can drag it all the way here and see the beauty of Ultra Code, which I'll talk a bit about in a second. All right, let's go back to the slides. All right, now let's talk about

**[86:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5214s)** autonomy. Here's a pattern that's motivated every feature within this session. You hand clawed a test. You come back and Claude was stuck on something really small like a permission prompt, a branch conflict, a missing build command. Feels like you wasted a bunch of time. The frustrating part is that Claude can actually do all of the hard tasks. It gets tripped up on the very small things. So we ask ourselves, what are all the little things that break during a very long running session? And how do we actually go and fix each one of them? Starting with auto mode. Auto mode is a new permissions mode where Claude makes permission decisions for you through a classifier. When a tool call would normally hit a

**[87:42](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5262s)** permission prompt, the classifier checks, is this prompt destructive? Does this look like prompt injection? If it is safe, it'll run. If it is risky, it'll actually get blocked and Claude will either find another way to do it or it'll pump the permission back to you. We've all had that moment where we step off with a very long running task and come back and realize, "Oh no, there's a permission prompt waiting for me." So, auto mode solves that. Work trees, they're one of my favorite features because they solve something that used to burn me constantly. I have multiple cloud sessions running in the same repo and they step on each other's branches. So, I end up with merge conflicts everywhere. Gitword trees have existed for a very long time. They create separate working

**[88:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5312s)** directories each on its own branch, but there are also sharp edges around it. And so we built a friendlier interface for it. You can kick it off with d-workree or -w to start a new session in a new work tree or you can just ask cloud to do it for you. What I love about this is how natural it feels. you stop thinking about what are all the git mechanics. Maybe a new software engineer doesn't even need to know how that works. Claude just handles all of that for you and you can focus on building features and products. Automemory is another one. It lets Claude accumulate knowledge across sessions so you don't have to keep repeating yourself. So everything from build commands, debugging insights, or project

**[89:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5361s)** inferences. Claude decides what's worth remembering based on whether it would help in a future conversation. Memory MD gets loaded in just like your Claude MD would. And recent models like Opus 48 and Fable 5 have been meaningfully better at managing their own memory. As Cat mentioned, at Enthropic, we have been experimenting with a different approach to code review. Instead of one reviewer looking at everything, we spin up teams of clawed agents that review each of them focused on different parts of the codebase. And then a verification pass checks whether the findings are actually valid. Then you can set this up for all of your PRs through our GitHub app or try it

**[90:11](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5411s)** manually with slash ultra review. So stepping back for a second right between auto mode work trees automemory and code review the shape of our workflows have changed quite drastically. You have fewer things to approve, more agents working in parallel without conflicts, and knowledge building over time. And you have a whole team that's reviewing your code before you even get to it. Your job largely shifts from doing the work to steering. Routines shipped in research preview recently and they take a autonomy a step further. You configure a session with a prompt, your repo, and any connectors that you

**[91:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5460s)** want, and then you just pick a trigger, a chron schedule, a GitHub web hook, or an API. From then on, it can run without you. So, you can have a routine that triages GitHub issues that are on your repo and then send you a Slack digest every morning, or one that fires every time your site makes a sale. So, let me jump into another demo to show you what this actually looks like. So, you'll notice here I'm in the routines tab and I have a routine that I've been running for the past couple weeks. What it does is it reviews all of the open issues within my Scala repo, which is here. And it actually goes and triages all of the issues and tries to

**[91:48](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5508s)** label them in order of priority. And so I'll click into one of these routines here. And you will notice that it has a summary of all of the triage statuses. Specifically, you'll see here number five, someone filed an issue that says the canvas goes blank on an iPad. Claude actually went over it and couldn't reproduce it. So it added a label that says needs repro. So, you'll notice that it's really exercising judgment more than just going and naively fixing every issue that you have. As well, if I click back into the actual routine, you'll see the name for it, the instructions that I included for this to run daily. You also have a cron trigger. You just

**[92:36](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5556s)** write a chron expression right here. You can add other triggers as well, whether it be a GitHub web hook or trigger it through hitting an API endpoint. And you can also add any connectors that you'd like it to have access to as well. So this is really great for being able to kick off tasks regularly without managing that. I'm going to go back to the slides for a second. I want to talk about agent view. Agent view is one of our most recent launches. Agent view shows you all of your cloud code sessions in one place. which agent is waiting for you, which are still working, and which are done. You can kick off new agents, send them to the background, and jump in only when

**[93:24](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5604s)** Claude needs you. This is a new interaction model entirely. So, instead of babysitting one session, you get to steer the whole fleet. So, I'll go back and show you what this looks like. All right. So you'll notice here that I ran claude agents and I have a few agents running here at the same time. Um so let's take a look at the completed one first. Um I asked it to write a quick summer code review uh a short haik coup about code review and summer and save it as a haik coup.ext. Once again you'll notice that it's able to write it and you'll see the diff directly in line here. Now if I go back you'll see that there are different sessions that are actively working right now. But I want to take a look at something that needs my input.

**[94:13](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5653s)** So I gave it a task to add a contributing section to the readme. Before you write anything, ask me which audience it should target. Uh I want this for the Excal repo that I just showed. And Claude went ahead and gave me a bunch of different suggestions that it thinks are appropriate. Um I want specifically all open source developers are welcome. That's what we're targeting because we love open source. And so as I go here, once I go back to the agent view, you'll notice that that session went from needs input to actually working. All right, back to the slides. I want to go over finally dynamic workflows. This just went GA this week. You give Claude a really big task like a codebasewide bug hunt or a very large migration.

**[95:03](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5703s)** Claude will go ahead and write an orchestration script, spin up as many sub aents as it needs in parallel, checks their work, and then hands back one coordinated result. A quick note on how to trigger it. We've heard you loud and clear that just triggering based on the keyword workflow has been a bit ambiguous and it'll overtrigger and so now we've made the keyword ultra code. So instead of saying you can uh so instead of saying using kind of a workflow of actually you can still say use a workflow for this and it'll work if it's an explicit um trigger but otherwise ultra code is the reliable way to trigger it. Dynamic workflows means you can stop decomposing tasks yourself. You just describe the outcome and Claude will figure out the plan. We're really excited to see what you tackle with it.

**[95:50](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5750s)** And if you can only try one thing from the session, something that I wasn't able to demo today, you should absolutely try this. It's quite magical. All right, then I want to go through some recent change log items. I'm not going to read over every single one of them, but it's here so you can photograph it if you'd like. I just look at this and really think, wow, we have shipped so much in the past few months, and there are many more to come. I'm just going to draw your attention. For those of you managing cloud code for teams or enterprises, we have shipped better Windows support, cloud provider setup, installation improvements, admin settings management, and plug-in features. You can, as always, follow along in all of our public change log,

**[96:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5797s)** as well as at any time running notes directly within the CLI. A few more ways to keep up with what is new. Follow Claude Devs on X, read what is new in our docs, and of course, subscribe to our amazing developer newsletter. I'll leave you with one thought here. Every feature I showed today started as someone on the team saying, "This is annoying. Let's fix it." Or, "What does this feature or workflow look like in an AI first world? How do we revisit this from first principles?" If you feel that way about something in cloud code today, tell us. That is how the best features get built. We hope you learned something new today and we'd love to hear what you think. Thank you for joining me today. I'm

**[97:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5845s)** Charmaine. I'm on the applied AI team here and I would love to chat with you after. It is an honor to be here. Enjoy the rest of code with Claude Tokyo. [applause] Heat. Heat. N.

**[99:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=5941s)** Hey, hey, hey. Hey, hey, hey. Heat. Heat.

**[101:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6061s)** >> [crying] >> You're Hey,

**[101:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6119s)** [music] hey, hey. Hey. Hey. Hey. Heat.

**[103:17](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6197s)** Hey, Heat. [music] Tell me

**[104:13](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6253s)** what you do. Heat. Hey, Heat. Heat. Hey. Hey. Hey.

**[105:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6315s)** >> [music] >> Dick dick. >> [music] >> D down. Dick. Hey,

**[106:11](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6371s)** don't Happy. [music] Hey. Hey. Hey. down. Down.

**[107:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6441s)** Hey, hey, hey. Hey, hey, hey. Hey,

**[110:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6630s)** Natal. [music] Natal. [music] >> [music]

**[113:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6811s)** >> Hello. Hello. [music] Heat. Heat. N. Happy. Hey. Hey. >> [music]

**[114:40](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6880s)** >> Heat. Heat. N. love. N love up love up love up love up love up love up love up love up love up love up love up love up love up love up love up love up love up love up love up love up love you got happy up happy up happy up happy up happy up happy up happy up happy up happy up happy up love up love up love up love up love up love up love up love up love up love up n Hey,

**[115:47](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6947s)** one. Heat. Heat. N. Hey, one one Please welcome to the stage head of AI products at Canva, Danny Woo sto,

**[116:38](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=6998s)** Canva AI product, Danny Wu. [music] [applause] [music] And hello everyone. Thank you all so much for joining this session at Co with Quad. Um, I'm Danny and I'm head of AI products at Canva. And I'm really excited to be hopefully sharing some of our top learnings from building Canva AI 2.0 with um, Claude with all of you. And hopefully this will be helpful for all of you builders out here. So, let's get started with our agenda. I'll briefly cover a quick overview of what Canai 2.0 L is and share a few of our top lessons including how we actually redefined what our success criteria was as we learned

**[117:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7047s)** things we've learned around building our agent harnesses how we manage cost at scale to serve tens of millions of users um and a little bit around responding to and really listening to community feedback. So I want to first start with a bit of an intro about what Canva AI is. And it really and if you don't know what Cana is, it's a graphic design and visual communication platform that lets you create everything from this docs, presentations, posters, emails, any pretty much anything you can imagine, you can create it with Canva. And Cam AI is really designed to help our user base and help our community achieve all their design and productivity workflows. So, here's a little video. If you have some if you have something like um you can

**[118:14](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7094s)** connect your all your data sources like Slack, Google Drive, Calendar and more and really use Canva AI to get your work done inside Canva like getting all the right context from and then using it to create a doc, create a design that you can edit natively and really really easily and collaborate to get work done. So I also wanted to talk a little bit about claude. Um at Canva we have been using claude since the set 3 model days and as as we've all seen with fable earlier today the frontier intelligence for claude models continuing to advance. We're seeing it continue we're seeing it increasingly solve some of our hardest challenges that was more or less unimaginable just um a few months ago or several months ago. And of course, we

**[119:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7144s)** run fairly comprehensive evals across all sorts of different um all sorts of different tasks, workloads on the trifecta of quality, cost, and latency. And Claude consistently delivers. One thing that's especially good and that we love about Claude models is the visual superpowers. And this goes beyond front-end design. We find that it generalizes really well to everything from creating polish presentations including on brand on brand decks but also all kinds of visual artifacts from to just any from printables to docs and so much more. And another thing that's especially great is the flexible deployment options. And for us, having having Cloud available on Bedrock, Vertex, and Microsoft Foundry is more than just a different API endpoint that

**[119:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7192s)** it's a way for us to build to build and use Claude inside all of our AWS accounts inside of um with our IM roles, permissions, and cost tracking. So, it makes it really really easy to integrate. And now I'll give you a bit of an overview about Cam AI 2.0 which is actually a fairly complex agentic system. So while it looks like just a simple text box on the surface, it is actually something that is something that orchestrates quite a combination of different agents like our design agent or code agent that powers um camera code as you saw as you saw earlier today. But it also has really hundreds of different tools for all kinds of tasks from things like image generation to to background removal, magic layers. Um and

**[120:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7241s)** essentially what we're doing is what we are continuing to do is really baking in all the different features, all the different things that normal user could um do through the Cana platform, but really integrating them and adding them as tools that are that kind of AI and our agents can call. And of course, we've got the platform layer where where you have all of the connectors, all the MCPS, memory, scheduling, and everything else. It it might look a little bit simple on the surface, but getting this to getting this to work and create a and create a cohesive experience for our users is a little bit more complicated, especially with especially with increasing powers of AI models and user tasks. Um, and I want to say a few challenges. So, at Canva, we do have a distributed um distributed AI team. We wanted our

**[121:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7290s)** whole organization to be to be working on AI. for example, we want our video group to be working and have ownership of video AI. We want um we want our print group to really have ownership of all of our print features and everything. Um and so we really need to find patterns that scale across an organization of about 5 and a half thousand people. And Cana handles such a broad range of jobs to be done. And in terms of scale, we um especially with the launch of Can I 2.0 everything has just continued to grow. So scaling is definitely a fun challenge. I'll start with the first lesson and that's really around defining the problem and really building solutions that connect with users. And for us, it's actually learning that empowering empowering our users to design isn't necessarily just about oneshot outputs

**[122:19](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7339s)** or how good it is. And this is because um and while this is obviously a dream, we love to be able to translate a really flex a really broad prompt into an amazing output from the get- go. There's a lot of considerations. For example, design is inherently subjective. Uh different users have different tastes. They have different preferences. We've got um we've different teams and companies. They've got certain brand systems and brand kits that needs to be integrated. And there's not necessarily a right design for that's perfect for a task. There's rubrics, there's evals, and there's user preferences, but design is inherently subjective. And from what we find and from what we find both through internal testing and really talking to our users and early testers of camera AI, the human touch actually does really matter.

**[123:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7390s)** For example, the average camera design is edited about 110 times before it's been published. And what we've sought to build with Canai 2.0 know it's not just an agent that is executing things in the background and able to um complete the designs and just gives you a little down toggle, but it's really something that can work with you, something that you can steer, something that you can really walk alongside as a super design collaborator. And finally, latency and responsiveness is one of the top goals. We actually find really really strong correlations since Canley is interactive and our users expect to be able to complete the design needs quickly and effortlessly. We have we see a huge correlation between like user satisfaction, feature retention, everything with a latency.

**[123:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7439s)** And sometimes there's actually even more than our quality metrics and rubrics. So figuring out how we can make the agentic system just deter not just really good but also really fast matters a lot. And I'll show you an example of um how we've actually applied this to the design agent. If you look at the I guess um start, we've got the we've got what's template and that's um that's obviously not personalized, not customized, but a really really great starting point. And the middle of the pack is what we found is our sweet spot at least for now in terms of the amount of effort and the amount of the design quality we want to get before handing back initial design to the user. we can if we spend a lot if we get the LMS and get the models to work for a lot longer and um and spend a lot more tokens and spend a lot more

**[124:47](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7487s)** effort but also correspondingly more time then we can get a little bit of a more polished output as you can see from the slides but it's that's not necessarily what most of our users prefer and of course if you do answer something really amazing we'll make it for you. So this is really about how the how at least um the way we see it there's a little bit of a efficient frontier or a sweet spot for models and it's not necessarily about quality maxing. It's not necessarily about I guess I'm going for the lowest cost but finding the right effort levels finding the right prompts for you know agentic harness to really get to what is like the right spot where most of our users are the happiest. Now the second lesson and this is around our agent harness and how and how we're increasingly seeing that this as

**[125:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7535s)** disposable I think with the with the rise of um just how powerful agent engineering is and new models like fable but also really like with open with opus empower models um like this is just a quote from me but I think today's clever harness is really tomorrow's dead code like um harnesses and the what boundaries you set it's constantly changing ing with new models, you find new things that work best. Um, and and this is we've seen this a lot with our own with our own like journey. So, we've had some form of cam AI for the past three years and we've essentially rewritten the entire CA hardness at least three times. um as as we adapted to new models. We originally started with um doing internal chain of thought

**[126:23](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7583s)** prompting before moving on to before moving on to taking advantage of native model capabilities. We started leveraging more and more tools. Um the early versions of Kaii maybe only had three or four tools. Now we can have hundreds of tools. And my my whole point here is really um like harnesses are your aging harness is something that you should continue to iterate and something you should continue to evolve. It's not some it's it might be okay to keep on building things and keep on testing things. that especially when there's a big jump in models like um the cloud five family, it's a perfect starting point to really re-evaluate what what you actually need and whether giving models more power can give you better outputs for lower quality sorry better output better outputs for

**[127:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7630s)** lower latency and higher quality. What's really important here and what is not disposable but what is really really valuable are eval specifically we started moving to this recently end to end eval um the way I would think of this is um if you're a software engineer like you might write unit tests and those could be traditional eval measure the performance of say a specific task or a specific feature but when you're building a complex agentic system that has things like user memory that has things like external connectors um that has like things like integrations then you really want to make sure that your end to-end flow is working and behaving the way you expect as you do AB tests as you make as you test different system prompt changes or even test different models different

**[127:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7679s)** effort levels and so much more. These end to end evals are what really gives us confidence in launching new features or rolling out things to 100% as well as really understanding what's the best what's the best way to leverage a model's capabilities and it's a list that we're continuing to grow and expand and really it's kind of on our mode our mode for building better and better camera AI getting there isn't super simple and it is definitely an iterative process it's something that you can start it's we've started like our initial ones maybe had like 10 or like a dozen test cases before we've added um hundreds and hundreds more and then we've started having to only run a portion of these um of these evals um just to make the times work. Um and what we found super helpful is really having surfaces and having

**[128:49](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7729s)** mechanisms to be able to launch features and launch experiments to users to early adopters um beyond your internal team really early. Once you launch to some users, um, every every time we find that users either have different expectations to what we thought, usually not that far off, but usually a little bit different. Um, and the and the feedback and how users actually use your agentic product, not what you have in your say marketing videos or press releases. That's what's that's what's unique. That's what you need to add to your emails to really like um, deliver a great experience. Um and I also give a bit of a call out for signals of success. Um I think it's really important to actually be very deliberate um when you're doing experiments in to measure the right metrics. Um, we found things like um do

**[129:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7777s)** users like spend more turns on cam AI to actually not be that helpful because when you have um when you have say a more power when you have a more powerful AI agent um users might be able to complete the task in less terms or actually get a design faster and spend less time in your platform and get their work done and that's a good thing. So my advice is don't necessarily go for engagement metrics or things like time or time time spent or tone sent but rather like does it help you users get the jobs done? Do they come back to your system? What's your retention? And really like the combination of all these will help you build build agents that really perform. Now getting to a meteor and hopefully exciting topic and that's managing cost at scale. Cam AI is used by tens of

**[130:26](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7826s)** millions of users and growing each and every single month and it's continuing to accelerate. So listen and the vast majority of C users are free and we believe it's really really important to be able to offer AI to everyone to students um to people who might not be able to afford say upgrades to Canva right now. So that's why we that's why we try to make it as efficient as possible. And there's probably probably three key takeaways that we found really helpful. The first one is um setting term budget limits. Um and the task budget feature in the public platform is actually surprisingly effective and has certainly surprised us in terms of how much models scale. Smart model routing is another another really important area. Um there's usually like all the hype is around the most powerful and the

**[131:17](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7877s)** latest models, but honestly across the whole core model family, there's some really really excellent performers. And one of the one of the biggest ways you can you can optimize your cost is to ensure that you are always using the right models for the right workloads and tasks. And finally, I'll talk a little bit about creating a cost aware culture across your organization, especially if you are in a large company where there's many many developers and many many builders making contributing and building to your AI. So the first one is around term but and budget limits. And I guess like why have this in the first place? If you're used to clock coding, you're probably thinking, gee, like it's a bit annoying if um like your product actually interrupts users and stops them before the task is actually completed. But um

**[132:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7925s)** especially for our product which is used by users um of all AI skill and processing levels, we of we often see prompts that um are not entirely super effective. For example, if you look at this prompt, keep working on each and every page in this deck, which could be a 40 page deck or maybe even sometimes a 100 page deck until it's really really good. Um Frontier models will do an amazing job at it with um unlimited time and with unlimited budget. But if you don't have unlimited um usage or budget to offer to users or in a session or when costs matter then setting con then setting constraints and actually the instructing the model and giving a bit of a budget to complete a tone really does help. And finally, like no matter what, no matter how much you test, no matter how much you optimize, especially

**[132:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=7974s)** when you're dealing with external systems or external connectors, um you're probably going to see what we call like doom loops um every once in a while where an agent might keep on trying the same thing again and again and again and that's not really great if it blows past the user's entire budget. So our goal with time budgets is not it's really to help our users get the most value out of the out of the AI limits that they do have and ultimately have a happier experience. The the first thing that I encourage all of you to start with and explore if you haven't is term budgets that was introduced um on anthropic platform um um fairly recently and for the latest models. So here's a So with term budgets, you can basically instruct um instruct Horde, hey, you have like a

**[133:42](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8022s)** 32,000 token budget, you have a 50k token budget, and you leave the decisions up to the model to actually budget itself and manage how it executes the task. So here's some examples um with um with one of our design generation harnesses. Um we're using the same model and giving the same prompts. Nothing else changes in these examples except the town budget. And you can see how Opus like actually scales incredibly well and delivers a delivers a presentation of a form across essentially like half an order of magnitude of town budgets. Um finding I guess determining what the token budget is like that's that's definitely something that's very harness and harness specific. But frontier frontier models, opus and even fable, they do

**[134:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8070s)** scale incredibly well across both effort levels and time budgets. And those are things that you can control to help deliver more optimized AI experiences. Seriously, they're so so powerful. Um and one thing I one thing I will note is that um task budgets um only count tokens and if you have an agentic system you are going you probably do have tool cost tool tool calling costs. So for example image generation cost a little bit of money like things like web search might cost money. So what we have done and found to be actually really effective is to essentially um essentially like follow similar patterns to how task budgeting implemented but also for us track and have costs for all the different tools. Um we send we we we

**[135:19](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8119s)** do this in a very similar way and essentially like every at the start of the task we instruct the model like opens with um with a budget is the session. Every once in a while we um during a turn we give it a reminder of hey you're this way through and we and finally once it has reached a time budget we ask the model to wrap up and finish its work. Um I will note that um generally like these things are these things like do work fairly consistently but not 100% of the time. They are advisory and there are hard limits. So you should be so you should also have hard systems level enforcement if if hard budgets are important to you. And ultimately like um where where you get to how what where the sweet spot is for your application and for your use cases is something that you need to

**[136:07](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8167s)** profile yourselves based on the workloads you want to support and what your cost profile is. Um this is actually uh we the specific numbers here but this actually real from um can I 2.0 know we did an analysis of um our user sessions and really tried to set a good limit that allows for a very very sensible and very decent amount of work but also also use the the latest and most powerful frontier models super effectively and there are a lot of things that you can do to actually make time budgets much more user friendly. So and you can do this just through system prompting um and giving instructions. First, the pattern that we found um that that works really well especially in an interactive agent application is communing helpful next steps like communicating what the

**[136:57](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8217s)** agent has actually performed. if there's any actions that the user has asked for that it has not performed like in this case um where it added 10 slides but did haven't finished things due the time budget um and ask users for either additional context or steers but also offers that they can also offers to simply continue the task and the second part um beyond time budgets and limits is really smart model routing with sub agents and why sub agents I'll take you through an example with um Canva code. So our MV our minimum viable product and version one of Canva code was just using uh just using sonnet which is very simple and very straightforward but for simple crap queries like editing some text or edit

**[137:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8264s)** or replacing a graphic you really don't need set haiku is going to do an excellent job. Um and so we experimented and tried model routing where for when a given user prompt we would either send it depending on how complex it is either send it to opus or sonnet or haiku and this um this initially seemed to work but it actually had some downsides and primarily every time we switch models we have to write the cache again and since um since we're editing code like the context window it might be tainted so the cache is no longer coherent and in a lot of cases the cash rights that were that that we're paying for like not actually override the benefit. Um so we moved on to a more I guess um so we moved to a sub agents approach and this is ultimately what worked best for us

**[138:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8311s)** with camera code. Um we have a main agent that's is that has essentially the canonical context um and plays a little bit of an orchestration role and depending on the task it can choose to delegate that to an open sub agent to perform it or high sub agent to perform it and then send it back to the main Sonic agent thread. This worked really really well because it kept catching rates really high in the high 80s and 90s instead of constant traction and rights. We ultimately like almost half our cost and delivered user satisfaction to boot. And finally the last thing around cost is really having great reporting and monitoring systems. This is not just useful for you, but is also really useful to having having having great dashboards where you have tracing for

**[139:20](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8360s)** all your calls every session and everything that's involved in an agent session is a great way for you to get clawed um to also help you profile and help you find test and experiment with optimizations. Um we also find that surfacing cost in our internal um staff UX to have really helped and this has been especially helpful for discovering edge cases where some what should be simple or um very cheap requests consumed a significant amount of um significant amount of tokens or cost due to edge cases or bugs. Um, I definitely encourage you to not be shy about surfacing like how much every single agent take action or every single every single like interaction costs um to your internal team and maybe even to our use users as well depending on what your customer is. Um, it's some

**[140:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8408s)** it's just so important to know this and have this available with every single action. The last one that I'll cover briefly is around user feedback and I'll share a story of one of our recent launches image upscaler. So we we launching we launched our internal um in-house um image upscaling model uh just a couple months ago um after some exhaust exhausted some great AB test and evals um we rolled it out and we got a little bit of um mixed feedback. So here are some feedback from our comm from our community users around the image upscaler and this was despite the fact that we saw um we had such huge confidence like usage of our upscaling was um up um by a few multiples. Um our eval cases generally look good but we also had we also had um a minority

**[140:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8456s)** amount of user feedback um but really vocal feedback. So what do we listen to? What we found helpful is really leveraging the feedback and support channels um and really like having these um having the systems for capturing and surfacing servicing any user feedback um directly to you and using to categorize and charging them to the relevant teams and tag them with the relevant features. Um so we got hundreds of examples from our community around where the image upscaling model wasn't performing um as well. We added this to our evaluation to our added. So, we learned a lot of things. Um, we learned that in for some specific input, some specific art styles. It didn't work super perfectly. There's some um other other edge cases. And what we ultimately did is um pretty much added all the examples our

**[141:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8504s)** community has has submitted to our evals. We trained and our version two um and then got to 100%. It's and finally close the loop with our users. And if any kind of users um that's still that still has um that still has feedback on upscaler image upscaler right now, please do send and share it to us um because we'd always love to make it better. But really, it's so valuable and so powerful to be channeling your most vocal user feedback and even complaints into learnings. And just because a minority of users, just because it's a few percent, even if your evals look good, even if your metrics look good, that doesn't necessarily mean you've always hit the spot. So very briefly um so you can go grab lunch um some key lessons. It's really about empowering the human and making sure that you are striving for what

**[142:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8552s)** actually helps your users the most. Um harnesses are getting more and more disposable. Don't get attached. Don't fall in love with them. Evals are what really matters. Um cost control like task budgets like um if you haven't tried it, highly recommend you try out. It's incredibly powerful. effort levels um models using the right models for the right task and sub agents and finally listen to your community and all your feedback. Thank you and I got her cuz I'm [applause] >> [music]

**[144:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8670s)** [music] >> Hey, 1.

**[145:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8758s)** Hey. Hey. Down down down down [music] down down down 1. 1

**[147:14](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8834s)** >> [music] >> Hey, hey, hey. Down down down down. Hey,

**[148:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=8895s)** hey, hey. down. Ah! >> [music] >> Heat. Heat.

**[150:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9000s)** >> [music] >> Hey.

**[150:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9056s)** [music] Hey. Hey. >> [music] [music] >> Heat. Heat. Heat. Heat.

**[152:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9141s)** >> [music] >> Hey, hey, hey. >> [music] [music]

**[153:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9224s)** >> Hey. Hey. Hey. Oh, hey. >> [crying]

**[154:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9277s)** >> Hey. Hey. Hey. Hey. Hey. Hey. Beat

**[155:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9341s)** one. 1 >> [music] >> Hey, hey, hey. One, one. One.

**[157:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9450s)** Look at the repeat. >> [music] >> One, one, one, one, one, one, for real. Don't for me.

**[158:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9519s)** for me. For me, for me. [music] For me,

**[159:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9567s)** Keep [music] it. [music] of your day. Your day. Number

**[161:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9664s)** n. >> [music] [music] [music] [music]

**[162:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9730s)** [music] >> Number

**[163:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9798s)** n. Heat. Heat. N. >> [music] >> Please welcome to the stage. Members of technical staff at Enthropic, Jess Yen

**[164:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9848s)** and Michael Cohen stage Yokoso. Enthropic technafu Jessen Sama Michael Cohen sama. [music] [music] [applause] Welcome to code with cloud everyone. I'm Jess product for cloud manage agents >> and I'm Michael engineering for cloud managed agents. >> It has been so exciting to see the organic uptake on cloud manage agents and uh how we're accelerating meaningfully developer workflows. Uh this is a story that we want to share with you today. We've seen uptake from

**[164:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9898s)** disruptive startups all the way to uh the largest enterprises and we want to make sure that you can all benefit from the kind of experiences that they they've had as well. So first we'll go over the exponential that we've seen in AI capabilities and what that implies for building agents. We'll talk through the patterns we saw in agentic development and why that motivated us to build cloud managed agents. We'll go through the building blocks for building an agent, including some of our more recently announced features. And we'll round things out with a fireside chat with one of our hero Japanese users, Rockutin. So, as we've all seen, models are getting exponentially more capable, and so are our expectations. The more advanced our model capabilities, the more sophisticated the work that we're

**[165:45](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9945s)** delegating. We're now seeing that the bottleneck is increasingly the infrastructure and not actually the intelligence. So let's bring this to life. Two years ago when Opus 3 was announced, you might have it right and test a single component. It would take minutes of focused work. Last year when our claude 4 models came out, we leveled up and you could debug an entire set of files. You might be working for an hour or so, but you'd be steering heavily along the way. With our latest models this year, you're now seeing them run overnight across agent teams, listening to your linear backlog and actioning the whole thing before you wake up. And now we suspect that in the near-term future with models as capable as Fable, we'll enter a world where agents are capable enough to

**[166:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=9993s)** accomplish tasks that would have previously taken entire teams of people quarters to achieve. And agents will run this entirely autonomously. So you might see that multi- aent systems could coordinate and run an entire M&A pipeline end to end in a fraction of the time it would take us. And so as tasks have graduated from low-level instructions towards endto-end outcome description, we now need far more than just prompts and tool loop. We need reliable and scalable agentic infrastructure. >> That's exactly right. And the more complex these tasks, the deeper the access we'll need to give these agents in order for them to be effective. With models like uh Fable, we really need these to to uh they're able to do very complex tasks. Um you can't run an

**[167:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10041s)** effective agent without granting it access to your credentials, your internal knowledge bases or your databases. Um, if you want these agents to produce code for you, you need to give them access to your actual code bases so that they can push up PRs and uh go to production. And finally, you need to grant them identity and authentication. Our agents are increasingly acting not just as Claude, but as me or Jess with our emails and our Slack. And as we grant agents these humanlike capabilities, we expect to interact with them in much more humanlike ways. The shape of interactions are changing, not just the duration of these interactions. Some agents are very conversational. You steer provide uh guidance along the way. You might even interrupt it if you think that it's going off path. Some agents uh on new models like Fable uh are really

**[168:12](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10092s)** really outcome oriented. And if you have strong signal or a rubric that of what you want to see get done, you can provide it that rubric and let it iterate until your exit criteria are met. And then finally, you might start a task uh a couple days ago and then want to pick it up much much later. A robust agent platform needs to support all these sorts of um interaction patterns. And the infrastructure and primitives that um that we provide have to give you all of this out of the box while still being very very flexible so that you can customize them to your needs. >> So it's now becoming clear that we expect a lot of our agents and historically this has meant that we've pushed the burden onto you the developer. In research we conducted prior to launching Cloud Manage agents, we saw that developers were genuinely eager to climb the exponential with us, but were struggling with a few key

**[169:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10140s)** areas. So, first, context management. The right context at the right time is actually really difficult to tune even though it's completely necessary and providing context at the wrong time can be a huge distraction for your agents. Half of our developers are citing that infrastructure concerns are their number one production blocker. So agents create bursty workloads. They have unpredictable compute patterns. It's super difficult to scale securely while also hitting latency targets. And lastly, observability is genuinely incredibly difficult. How do you know when your agent is producing quality outputs? These are non-deterministic models and they're producing huge amounts of unstructured data. And so enter claude manage agents. We did the platform work so that you don't

**[169:47](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10187s)** have to. Managed agents combines infrastructure, agentic primitives, and out-of-the-box observability, all available in a package on the cloud platform. We'll dive into each of these components in more detail throughout the course of this presentation along with a couple of demos. >> So, let's talk about the very basic building blocks of cloud managed agents. At the very very core, you have an agent that you define. This would be the system prompt, the model you want to use, uh any skills that you might want to have loaded into uh your agent and tools with permissions for those tools that you want that agent to have. This is like the agent's identity. Next, you have the environment that you configure. This is like a template where you define a network allow list and any pre-install packages that you might want to have. This is like the world that the agent is going to live in. You take that the environment and the agent and you use

**[170:36](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10236s)** that to run a session. A sandbox is provisioned for you. We set up the harness and cloud starts executing. Any credentials and resources that you might want to include in that session are uh mounted into it and are uh available for the cloud to use. Finally, we have events. These are anything that the agent um produces as it's doing actions or any events that you might want to provide upstream in order to steer the agent. And this is how you might want to stay in the loop. events and stateful awareness is really where we're able to um provide a platform so that you can build your own products on top of um and you can use primitives like memory um and other features that we have in order to really optimize the performance of these agents. >> So as Michael mentioned agent uh events are the heart and the crux of what an agentic in uh inter integration entails.

**[171:26](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10286s)** So let's demystify what that means in practice. Everything in managed agents is event-based. So these are durable transcripts that are clearly structured to help you track your agents progress. So first there are user events. These are actually what you're sending to the agent to guide it. Next there are agent events. This is what the agent is actually doing. So this is messaging. This is tool execution, context compaction and even delegation to other agents. Next there are session events. This is how you understand the progress of the unit of work that you've just delegated. So this is the overall life cycle, the status transitions, errors, and outcome process. And lastly, there are span events. There's a lot going on in this event stream. Um, this helps you group related events and just see things in a

**[172:13](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10333s)** more aggregated uh instrumented way. So let's pivot to a realw world example of something that we built using cloud managed agents which is Pascal uh which uses a hypothetical online grocery delivery services order data uh in order to analyze that data and provide insights for our team. The agent produces analytics in minutes leveraging a pre-loaded data set and a a set of Python packages and scripts that we installed and uploaded into the container that it works from. You can see every event in cloud console and even chat with a debug agent in order to further optimize your integration. So going into the video itself, this is the Pascal kind of homepage. We can kick off an agent session and Claude will get started. It'll take it a couple minutes to complete. So while it does

**[173:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10381s)** that, we'll go over to the developer console and we'll actually see the events that Claude is producing in real time and be able to better understand what Claude is doing live. We can also actually look at the um agent configuration and environment configuration that were set up for this session. So this instance that's the system prompt and that's the model. And moving over to the environment configuration, you can see the network uh permissions that were allowed and the packages. Jumping back to the actual page itself, it seems like our analysis is more or less done and we can actually dive into the insights that Claude found. On the product side, it seems like bananas are really really popular. Um as well as a bunch of other products that are really popular, but everybody should get their bananas. Um, looking into customer insights, we see that Sunday afternoons are really, really popular for online orders. So, you might want to schedule your orders for a different time of the day. And then

**[173:49](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10429s)** finally, we set up this um prediction simulator that lets us analyze whether or not a customer is more likely to reorder things. Jumping back to the developer console, we can see here in the side panel that we can kick off an analysis of the session itself where Claude will look at all of the events and um further come up with insights for us on how to optimize the the integration that we built. In this particular instance, we see that some of the scripts that we gave Claude are actually really really slow. Um so we may want to optimize the Python code that we wrote for them in order for them to do better. So uh we just uh looked at uh the developer console and you saw that in action but there are really many different ways for you to get started with cloud manage agents today in order to interact with these agents that you create. You just pick whichever one fits

**[174:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10477s)** your workflow best. My favorite one is the cloud API skill that we have available in cloud code today. All you have to do is ask cloud hey I want to get started with using cloud manage agents and it'll help you with the onboarding flow into your existing code bases. Next, we also have the ANC CLI, which we released recently. Um, that makes it really, really easy to interact with our APIs for scripting and CI/CD pipelines that you might have. And then lastly, we have our developer docs and our cookbooks. These provide a lot of practical examples and copy paste ready um examples of the most common patterns that we have for cloud managed agents. >> So, now that we've covered the basics, I want to touch on some of the more advanced features that we've recently shipped. So first multi- aent orchestration here claude is able to delegate tasks to other agents with independent context windows enabling it

**[175:26](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10526s)** to uh parallelize increasingly complex work with outcomes. Claude iterates on predefined exit criteria or a rubric uh until it satisfies its goal. You're in charge of this goal and Claude is in charge of completing it. With memory, Claude is able to read and write to memory stores. By default, without memory, Claude would be starting fresh on every session. But with memory, it has an awareness of prior runs and can do better this next time. Dreaming is built on top of memory. And here, Claude is reflecting and codifying on the learnings and codifying it into new memories. And this ensures that it can continuously start with a tighter set of more curated and optimized memories. All of these are really exciting

**[176:14](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10574s)** intelligence features and we're really excited to raise the ceiling of what agents can produce. However, we also have heard that we need to meet you where you are and that means making our infrastructure more modular. So with self-hosted sandboxes, you can run the agent loop and have tool execution directly in your infrastructure so files and packages never leave your perimeter. with MCV tunneling clock can access uh private MCP servers that you would not want to expose to the open internet. Each of these things are built so that you can deploy within your enterprise within your own security principles. >> And in addition to all these amazing features that we already have, like Caitlyn mentioned earlier today, we just released two new very exciting features. One is schedule deployments which allow

**[177:02](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10622s)** you to set up a recurring schedule on which we'll trigger new sessions on your behalf um for any recurring work that you might have. And then next we have environment variables inside vaults which allow you to provide secure credentials for any APIs or CLIs that you might want claude to call without actually having any sort of risk about cloud um seeing the actual uh secret tokens. Diving a little bit deeper into how environment variables work in vaults. um we place an opaque placeholder token inside the container itself that Claude has access to. Um and whenever Claude uh it is trying to hit an API or use a CLI, it will just use that environment variable the way that it would use any other um environment variable. And as that network uh request is made, uh we will inject the real secret value as the

**[177:50](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10670s)** request is made um so that Claude may never actually see the the value of the secret token. >> Thank you so much, Michael. It's been so much fun building this platform with you. I am now excited to welcome to stage Yusuke Kajisan, general manager at Rocketin for AI for business, so that we can talk through what he's been building. [applause and music] Welcome. Um so Rocketin calls its AI strategy AIization and agents are the next big phase of that. So what does that look like day-to-day? >> Yeah. Uh first of all uh thanks for having us uh in the stage and welcome to the Japan. And so for Rakuten uh we have

**[178:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10719s)** theization uh activities which is basically uh our effort to fill in the gap between the capability C you mentioned and adoption in reality. So what we do is that we completely uh redesign our workflow from scratch as you release new models every month or every quarters and so that that we can you know basically uh fully unlock the potential of the intelligence or from the new models um by fully fully redesigning our workflows. Yep. >> Got it. Got it. And so what did it take for you to get agents into production at Rockin knowing that you've been on this journey for a while? And what would you skip if you were starting today from scratch? >> Yeah. Uh so when we started uh developing agent ourself, we spend tons of our time and effort uh to manage uh

**[179:28](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10768s)** the infrastructure of the agent. Uh but if we uh if we were starting today's uh we would skip that process and fully put our focus on agent experience and building some uh loop uh and close the roof of the agent instead of spending time for the infrastructure. >> Got it. So I'm excited to hear that manage agents is helping accelerate that work now. >> Um so what has made the biggest difference in the quality of your agents outputs over time? So I would say the self uh evolving capability uh would be the biggest uh differentiation factors. Um so um oh sorry I forget. Okay. So um basically uh in one day uh we deploy the agent and uh initially uh we have some mistake and

**[180:17](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10817s)** our agent makes some mistake but by unlocking by enabling the memory and dreaming you just described uh we are able to let the agent improving their capability by checking their trace pass run and then field uh you know address the problem or the mistake they uh made uh last time. So thanks to that we can actually address 90% of the problem we initially had in our real process and thanks to that our agent became more token efficient and also the latency and cost uh is decreased significantly. >> I'm really glad to hear how much value you're getting out of these features. Uh we just announced also the scheduled deployments feature this morning. So what recurring work at Rockin did you put on a schedule first? Yeah. So first uh we put a lot of uh reporting and

**[181:07](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10867s)** analytics task uh into the schedule deployment. So in our company we have a lot of the uh process uh or the task which require the repetitive the kind of the the work. So for example we have a lot of sales reporting or the marketing reporting which require the presentation uh deck or the spreadsheet and do some uh data analysis. So thanks to schedule deployment we are able to uh automate those repeated task and uh delegate those task to our agent and also sorry our power users also use it uh to take the log and metrics from uh our public cloud so that the our product manager can see the uh uh health status of the application without creating any new dashboard. Very exciting. And I guess

**[181:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10916s)** similarly, we also released environment variables supported in vaults. So agents can use authenticated tools without ever seeing the keys. So what is this unlocking for you? >> So the use case I mentioned now is actually unlocked by this board. uh because uh you know in order to uh make sure that we can use agent safely and align with our governance and the compliance we want to make sure that you know those API key and the credential will not be exposed uh to the the the agent itself. So thanks to this uh board we can actually onboard this uh monitoring agent u so that uh you know uh we can uh see the status of our application in real time. >> Very very exciting. You guys have always been on the frontier of what we've been building and we can't wait to keep

**[182:42](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=10962s)** pushing this platform forward with you. >> Yeah. >> Thank you. >> Thank you. [applause] >> So today you've gotten to hear about cloud manage agents as a platform and how it's accelerating some of our most frontier users work and workflows. You also got to hear from Yusukean at Rockin on how his team's productivity has accelerated meaningfully because of cloud manage agents. If this has resonated with you today, and I hope it has, then please feel free to walk by our demo booths where we will be all day um to show you some demos and to help answer questions about cloud manage agents. And then additionally, these QR codes that you see on the screen right now point you to some of our more tactical resources such as our

**[183:29](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11009s)** documentation and a rich experience in console that lets you build an agent from scratch in minutes. So really really wanted to extend such a thank you to all of you for uh you know staying with us today and hearing about what we've built. Can't wait to see what you've built what you will build going forward. >> [applause] >> Hey, hey, hey.

**[184:26](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11066s)** Give me hey. Follow me. Hey,

**[185:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11141s)** hey, hey. Hey, hey, hey. Hey,

**[186:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11197s)** hey, hey. You good? Love me. Love me. Heat. Heat.

**[187:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11279s)** Baby, baby. Baby. Dick

**[189:03](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11343s)** Dick down. Dick down. Oh,

**[190:19](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11419s)** Hey chick. D. Hey. Hey. Yeah, for real.

**[191:50](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11510s)** For real. for real. For real. for me.

**[193:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11581s)** >> [music] >> for real. Keep [music] your day. Love. [music] Heat. Heat.

**[194:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11679s)** >> [music] >> 1 2 3

**[196:09](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11769s)** Hey, hey, hey. >> [music] >> Heat. Heat.

**[198:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=11880s)** Hey, hey, hey. Happy [music]

**[200:07](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=12007s)** happy. What? Baby, baby.

**[201:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=12087s)** Heat. Heat. N. >> [music]

**[202:48](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=12168s)** >> Hey, hey, hey. >> [music]

**[204:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=12284s)** [music] [music] >> Number n. I'm a

**[206:43](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=12403s)** Hey, be turn over. One, one, one. One, one.

**[208:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=12521s)** One. Hey. Hey. One, one, one. Oh yeah.

**[214:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=12858s)** Hey. Hey. Hey. Hey,

**[215:12](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=12912s)** hey, hey. with me. Hey One, two, three, four. together.

**[217:02](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13022s)** Watch it. Hey.

**[218:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13095s)** Hey. Hey. Hey. Hey. Hey.

**[219:49](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13189s)** Damn it. Damn it. Here's Down

**[220:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13244s)** down down down down down down down. 1. Come on. Get drunk. down down

**[221:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13312s)** down. Hey I'm a [music] Come on.

**[222:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13372s)** Come on. [music] I'm a baby. Hey, hey, hey.

**[223:53](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13433s)** Want [music] [music] to be on about Yeah. [music] Hey. Hey.

**[225:12](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13512s)** >> [music] [music] >> Oh yeah. >> [music]

**[226:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13592s)** >> Heat. Heat. [music] Hey hey

**[227:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13659s)** Hey, let me Come on. Hey. Hey. Hey,

**[228:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13719s)** me. Hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey. Fall

**[229:36](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13776s)** party. Good. Good. Good to me. Baby.

**[231:55](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13915s)** Dick dick. down. D down.

**[233:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=13984s)** Hey. Hey. Hey. Dick down. Hey,

**[234:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14045s)** hey, hey. for Don't for me.

**[235:12](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14112s)** For real, for real. for real.

**[236:02](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14162s)** Heat. Heat. Something. of your day.

**[238:51](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14331s)** 3. Hey. Hey. Hello. Come on. Come on. [music] Heat.

**[240:23](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14423s)** Heat. Heat. Hey. Hey. Hey.

**[241:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14490s)** Hey, hey, hey. >> [music] [music]

**[243:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14585s)** >> Happy you hey. Magn

**[244:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14658s)** happy love happy love happy love happy love happy love happy love happy love happy love happy love happy love happy love happy Hey, >> [music]

**[245:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14739s)** >> Number one, Hey, ah hey. Natal.

**[248:43](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=14923s)** >> [music] >> Hello.

**[250:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15005s)** Hey. Hey. One, one, One, one. Hey

**[251:26](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15086s)** hey. 1 One, one, one.

**[255:19](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15319s)** Hey, hey, hey. Dark. D.

**[257:50](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15470s)** Hey. Hey, hey, hey. Take me.

**[258:55](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15535s)** 2 3 4 Hey, hey, hey. 2 3

**[261:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15670s)** Hey. Hey. Hey. Hey.

**[262:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15759s)** Hey. Hey. Damn it. Damn it. Hey, hey, hey.

**[263:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15826s)** Down down down down down down. 1. Down

**[264:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15896s)** down down down down down. I'm up. All

**[265:57](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=15957s)** right. [music] >> [music] >> Hey, hey, hey. Want to be? [music]

**[267:02](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16022s)** >> [music] [music] >> I want to be down. >> [music] >> Hey. Yeah.

**[268:17](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16097s)** Heat. >> [music] >> Oh yeah. Thank you.

**[269:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16199s)** [music] >> [music] >> Hello. Hello. Hey, hey, hey.

**[271:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16290s)** Please welcome to the stage general manager of AI at Rocken Yusuke Kaji St. Yokoso Raken AIU Malaysia. [music] Generalized. Hi,

**[272:45](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16365s)** this market operation. They must Agent

**[274:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16486s)** Managed agent return value. software engineering

**[277:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16624s)** benchmark. Fore market.

**[278:16](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16696s)** benchmark. Production I don't know. Fore! Foreign! Foreign! Evation benchmark.

**[279:53](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16793s)** managed managed agent agent managed agent solution. Memory session. Investment

**[281:28](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16888s)** agent. It's a Managed agent

**[283:14](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=16994s)** key profile. Foreomy detction detction.

**[284:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17072s)** Engineering foundation. Reliability security.

**[285:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17135s)** Ambient overnight. Forevelop Empowerment.

**[286:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17218s)** Hi. Foreigell. Yes. Do you know?

**[288:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17280s)** Do you know? across a AI agent.

**[290:26](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17426s)** MCP channel agent. Long runningchech.

**[291:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17506s)** Selfification. Foreign speech. Foreign speech. Foreign speech.

**[292:42](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17562s)** efficiency. So managed agent agent capability.

**[293:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17624s)** Memorial Fore

**[295:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17710s)** agent. agent compour. Wired Agent memory.

**[296:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17804s)** Hi.chech. Fore. [applause] Hey,

**[298:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17885s)** hey, hey. [music] Natal

**[299:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=17998s)** la. I'm

**[302:20](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18140s)** be over. Hey What? One. One.

**[304:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18275s)** One. One. You ready?

**[306:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18392s)** Hey. >> [music]

**[307:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18447s)** [music] [music] >> Happy. [music] Hey. Hey. me.

**[309:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18565s)** Happy la. Tonight, Oh yeah.

**[311:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18697s)** Hey Heat. Heat. I'm

**[312:43](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18763s)** a >> [music] >> Hey, hey, hey. Hey,

**[313:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18826s)** hey, hey. >> [music] [music] >> I'm a Hey, hey, hey.

**[316:12](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=18972s)** Hey. Hey. Hey. Please welcome to the stage executive officer, head of digital strategy and chief AI officer at Mizuho, Tatsto Fuji and lab lead at Mizuho Kentaro Sa Yokosoyako Psycho AI >> [music]

**[317:13](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19033s)** >> Hi. Hi. Hi. Fore! Foreign! Foreign! You know, it's not Incubation.

**[318:34](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19114s)** All right. Oh, system.

**[319:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19194s)** Mathematically challenging. Digital transformation. Arabic.

**[321:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19295s)** No exponential. [clears throat] You don't Step one.

**[322:49](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19369s)** Hi AI model. AI, AI oriented architecture. Agent

**[323:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19439s)** agent. Agent factory. You This

**[326:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19581s)** That's nice. [music] Financial [applause] group. Fore

**[327:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19638s)** security engineering. for engineering team. for

**[328:38](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19718s)** security. Favorite Enterprise

**[330:51](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19851s)** Anthony. for Security.chech. agent.

**[332:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=19950s)** Enterprise for Fore speech. >> [snorts]

**[333:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20019s)** >> Foreign speech. Foreign speech. Fore performance. Second opinion.

**[334:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20071s)** Foreign speech. Foreign speech. Foreign speech. main Applic.

**[336:38](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20198s)** It's Security.chech.

**[338:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20315s)** Hi. What is this name? Hypers

**[340:16](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20416s)** foreignch. Coronche.

**[341:45](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20505s)** Agent agent. Fore speech.

**[343:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20584s)** Foregos. [snorts] So

**[344:28](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20668s)** >> [snorts] >> The human in the human transformation. Empower agent. >> [applause]

**[345:46](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20746s)** >> Hallelujah. >> [music] [music] >> Hey, hey, hey. >> [music] >> Hey, [music]

**[346:42](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20802s)** I'm a I'm going to be [music] [music] >> [music] [music] >> I'mma be on the ground.

**[347:38](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20858s)** >> [music] >> Yeah. [music] [music] Down. Damn it. Damn it. Come on.

**[348:26](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20906s)** Come on. Come on. [music] Down down down down down down 1.

**[349:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=20973s)** Come on. Come on. Come on. Come on. Down Down down down down. [music] [music]

**[350:36](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21036s)** Hello. Hello. [music] [music] [music] [music] Happy you happy happy happy

**[351:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21085s)** you. Hey, wait. >> [music] [music] >> Make me baby. [music]

**[352:49](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21169s)** Heat. Heat. N. Dick [music] dick. down. Down.

**[353:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21224s)** [music] >> [music] >> Down. Down. Everybody tick

**[354:45](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21285s)** tock. Hey, hey, hey. Hey. [music] Hey. Hey. Hey.

**[356:19](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21379s)** Hey. Hey. Hey. I want you. Hey. Hey. Hey. [music]

**[357:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21450s)** Hey, hey, hey. Hey. [music]

**[358:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21510s)** >> [music] >> Yeah. Yeah. >> [music] >> Yeah. [music] [music] Yeah. >> [music] [music]

**[359:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21577s)** [music] [music] [music] [music] [music] [music]

**[360:55](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21655s)** >> Hey, hey, hey. >> [music] >> That time come Please welcome to the stage member of technical staff at Anthropic, Theo Chu Yokos, Enthropic Sha Theo Chu Sama.

**[361:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21704s)** [music] Hi everyone. >> [applause] >> Hi everyone, my name is Theo. I'm a research product manager at Anthropic. Uh I work on our long horizon capabilities such as long context and memory capabilities uh in our models. I joined a little uh about two years ago right when sonnet 5 sonnet 35 had recently launched. At the time agents were barely a word that people were using. Um there were just signs of life that the models could even do coding uh

**[362:34](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21754s)** at all. People were still focused on chat completions. Um autonomy and agent autonomy was something that was still kind of a new concept. Around this time last year, uh when I go back to code with claude, uh last year, Opus 4 had just launched. Cloud code was not even GA. Uh it was still a pretty nent thing. We didn't know um if it would, you know, quite take off. Uh it was still pretty new um that models could, you know, be used for autonomous coding. And of course now we have fable, we have mythos uh and recently had also launched opus 84 8. So before I uh go into the talk about the capability curve and how models have improved over time

**[363:22](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21802s)** um I want to ask you all to raise your hand if you've heard of claude. Okay. Uh now raise your hand again if you've used claude. And keep that hand raised if you think Claude makes you twice as efficient. Okay, keep that hand raised one more time if you think Claude makes you 10x as efficient. Okay, pretty good. Um, this time last year, lots of people uh did not even know what Claude was. When I was at Code with Claude uh last year, people were still asking me um you know, tell me a little bit more about large language models. What do they do? How can I best make use of them? And so, it's really

**[364:11](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21851s)** insane to walk around this conference and see how much more awareness there is around AI, how many more people are using it in their day-to-day life, uh and how many more people are not just using it in their day-to-day life, but seeing the gains in their own productivity and efficiency. more code is written by Claude every year. We recently released a blog post about recursive self-improvement. Over 80% of code uh internally at anthropic is merged by Claude. Um and so as you can see uh as models improve over time uh we very much expect that capabilities and the ceiling of those capabilities are only going to get better from here. And so this talk is about how you adapt to this new world and how you as developers can actually think about building for the future instead of just

**[364:58](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21898s)** building for the past. So you can see on this slide uh that we have a series of models and how they've performed on Sweetbench verified. This is a trusted coding eval that we use internally to look at Claude's coding improvements. Uh this eval is made up of a series of GitHub issues. Um and Claude needs to pass these issues and is then uh run on tests to see whether or not it has successfully passed that issue. And if you look all the way back to set 37, you can see that it scored just a little over 60%. With Opus 48, it is now scoring 88%. Uh and with Mythos and Fable models, we have seen that this benchmark is actually saturated.

**[365:48](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21948s)** This is a pretty insane improvement. I don't think the line fully captures how insane of an improvement this is. From 62% to 88% in just 12 months means that Sonnet 37 actually failed three times as often on these tasks. Just think about that for a second. And that is the rate at which models have improved just over the last year. And models are only improving faster and faster. And so what I'm about to show you is the same task done 12 months apart by two different models. So first we'll see sonnet 4 uh performing on this task and then we'll go and look at opus4 on the exact same task.

**[366:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=21997s)** The task that I'm about to show you is rebuilding cloud.ai uh our cloud website in one shot. And so Sonnet 4, as you can see, uh, is writing quite a lot of lines of code. Uh, it's calling a lot of tools. It's jumping right into it. It's acting before it's planning. Um, and when you actually go and run the UI, uh, you can see here that it actually doesn't work. Looks reasonable, um, but not completely functional. Now, uh, the Wi-Fi might be down. I'll voice over what Opus 48 would have done on this instead. Opus48 would have built the exact same UI, uh, but it

**[367:28](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22048s)** would have actually had the same colors that we would have had on the cloud.AI website, would have seen the sidebar, you would have seen the chat interface, you could actually send messages and they would actually respond correctly. and it would plan before acting. Uh, and not only would it plan before acting, but that planning before acting would ultimately lead to far fewer tool uses called, far fewer lines of code written. And so at the end of the day, what you're seeing is that Opus 48 not only does the task more successfully uh, but faster and cheaper. So before I get into the tactics of how you can actually build in this new world, I want to talk about where the intelligence gains are actually landing. So the first thing that we'll talk

**[368:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22095s)** about, again, as I mentioned, is this idea of planning before acting. So old models would, you know, be like me with IKEA furniture. they would jump right in uh not look at the instruction manual, just kind of start building and then kind of fail at doing the thing um and realize that they had to to go back and actually uh look at that instruction manual. So they would just kind of jump right in and act before they started planning. Now models actually plan first and what that means is that they're thinking through what the spec should be before they actually go and execute on it. And by doing so, as you saw uh or would have seen if the Wi-Fi had worked uh with Opus 48 is that the models are actually more efficient by pre-planning that spec. And as it's pre-planning that spec, it's

**[369:03](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22143s)** then able to actually catch mistakes. Um so you might see things like the model saying words like actually or never mind. uh but by catching those mistakes, it can actually uh execute on the plan more efficiently the first time around. And so what this means for you is that you should allow the model to think first before actually doing the task. Build your products in a way where uh that thinking is allowed in the user experience where you are actually giving the model higher effort uh and adaptive thinking so that it can then do that planning up front. The second area where we see a lot of intelligence gains is in error recovery and selfcorrection. What I mean by this is that old models used to do this thing called doom looping. Doom looping is the

**[369:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22192s)** idea that you know the model would be given a task. It would uh go and do that task. It might fail on the task. You would tell it hey I think you should have done this other thing or maybe something in the environment gave it feedback that it should have done this other thing. It would say great let me try it again. And as it tried again, it would just kind of keep running into the exact same solution that it had previously and would not change its approach. Now models are able to actually look at that feedback and react to it and they will actually try something different and try again. And often times this leads to a better outcome. And so what this means for you is that you should think about designing your environments in a way where you can actually give that feedback to the model so that it can actually then recover

**[370:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22241s)** from any errors that it's hitting along the way. This also means that instead of doom looping and just wasting tokens, models are actually able to perform the task with fewer tokens overall. And finally, uh models now are improving at running over longer and longer horizons. What this means is that models are actually able to sustain attention and hold coherence up to often a million tokens, sometimes even more. Old models would lose the thread partway through. They might forget the task. Uh you might have heard people say that sometimes they they see models quote unquote losing the plot. Um this is often what people say when a model kind of forgets the task along the way. Maybe it forgets the instructions along the way. Uh and so it kind of starts going a little bit

**[371:28](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22288s)** off what you expected it to go on. But now we're seeing that this has improved uh significantly more. Of course there's still room to improve here uh as we get better at longer context lengths. Uh but now you can actually allow the model to run up to a full million tokens. And what that means for you is that you don't have to do as much context management. You don't need to chunk up the context window as much as pos uh as much as you used to. Um though of course if you do want to run for much longer than a million tokens, you may still need to do some of this. So I'd recommend as you think about uh models going for longer and longer horizons that you actually just dream more ambitiously and give it much longer tasks uh where you can hand it an entire code base and not just a single file. And what this means is that models now

**[372:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22338s)** can plan a lot better. they run into fewer failures as a result, but when they do run into those failures, they're able to recover more quickly. And finally, they can just run for longer and longer horizons. And so all of this compounds into these agents that are able to run a lot more autonomously. And they can then do longer and longer tasks over time. And so they're able to then do more and more intelligent tasks over time. So what this might look like is something like the chart you see here where agents first plan. After they plan, they then execute on that plan. You might give them some way to verify against that executed plan. Uh so maybe again this is a this is human feedback in a conversation or this is some tool

**[373:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22388s)** that the agent can call to verify their outputs. They then use that verification to then adjust the plan and they kind of go back and loop on this again until finally they are happy with the the final result. But don't just take this from me, take this from some of our users as well. Uh here we have a quote from Shopify who has seen that Claude Opus 48 uh is noticeably better at error recovery at planning before acting. cursor has seen that tool calling and uh token efficiency in our models is much improved um and that opus 4 8 is better than every other opus model that they've they've tested uh and similarly cognition has also seen that opus 48 is much more autonomous can run for much

**[373:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22436s)** longer horizons uh and similarly is also more token efficient so again as models get more and more intelligent you can kind of just let them go uh for longer periods of time uh and they're able to work on tasks more efficiently and effectively than they were previously. So this is the part where everyone's probably most interested in which is tactically how do you actually now build for this future? How do you build for the models that are getting better and better over time? This is not just about Opus 4 or Opus 47 or any of the models that we have today. This is really about helping you guys understand as models improve, what should you be thinking about as a developer so that you can actually give your users those intelligence gains that we're we're seeing in the models. And the first thing before we even get into the

**[374:43](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22483s)** tactics is a mindset shift. Be ambitious with what you try and what you allow Claude to handle. Don't keep testing the same tasks that you think Claude could have done 12 months ago. Start to think about tasks that Claude can't do today and think about how you continue thinking about tasks that Claude can't do today do do today because as models improve uh more and more of those tasks are going to be possible and you want to be able to see as those tasks become possible and the first way that you do this is by building evals uh refreshing your evals if you already have evals uh but oftentimes this is the first step for people to even understand what is possible in models today. So if you don't have evals, uh the way

**[375:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22531s)** to think about this is that they are unit tests for a for the AI area. Uh some of these uh can be regression tests based where these are all tests that the models today can already do. Um and you're just looking to see whether or not uh your harness or future models are able to do the same things. Uh but often what you actually want to do is create eval models do not saturate. And so what this means is looking not just at the current customer experience uh that you're providing to users, but the customer experience that you want to provide to your users over time and the direction that you want to take your application and building for those test cases and putting those test cases in your evals. This also means looking for failure modes that your users are

**[376:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22578s)** reporting to you, adding those to your eval models actually then solve those failure modes. Secondly, uh update your evals that might be saturated. So we sometimes hear from customers uh when we launch new models that they'll say something like, "Hey, on my eval it only really improved by 1%. I don't think this model is that much better." And over time as they start to play around with the model more and more they realize oh actually this model is significantly better on you know a couple of capabilities or maybe this one axis that my eval just didn't test for at all. And so this is a testament that if you're seeing that your eval is not moving very much uh you may want to look at whether or not the

**[377:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22625s)** remaining problems that are not yet uh not yet solved by models in that eval are actually fair and solvable. And if they're not, then your eval might be saturated. And if it's saturated, then it's time to update that eval and look for harder problems. And finally, uh once you do have that eval, the best thing that you can do is just benchmark it so that you understand how various models are performing on it. And as new models come out to actually then look at how those new models are performing on it. Secondly, and I can't say this enough, shrink your scaffolding. Um scaffolding is the prompts around the model, the tools that you might be using around the models. Uh any code that you have. Uh sometimes people also call this the harness. Uh but as you look at your harness and your scaffold, oftent times people are adding new things to it over

**[377:55](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22675s)** time because of various failure modes that maybe prior models ran into. And so an example here is that uh we at one point had um a line in our clawed AI system prompt uh that specified a specific citation format um that was now out of date and was not a citation format that we were using anymore. Uh and our new models uh got significantly better at instruction following and started following that instruction in the system prompt that we had put in there a while ago. And so we thought that citations were broken in this new model uh until we looked at the system prompt and realized that actually the model had just gotten better at instruction following. And what we really needed to do was to just remove that line entirely from the system prompt. Um and this is an example where shrinking the scaffolding and just

**[378:43](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22723s)** letting the model have a little bit more autonomy uh actually helps you to see what that model can do um in practice. And so what you want to do is to write your prompts for intent and what you want the model to ultimately do and not just to write those prompts uh around all of the past failures that you may have run into with prior models. And finally, you want to give the model room to work. So we talked a little bit about this uh when talking about giving the model room to think. Um, you want to use adaptive thinking, which gives the model the ability to decide when it needs to think and how much it needs to think. Uh, and there's also an effort dial that you can use to actually uh dial up or down how hard the model works on problems.

**[379:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22771s)** Secondly, you want to allow your agents to have more access uh to your environment to take more actions um but do so in a controlled way. So, as we talked about, models are becoming more and more autonomous. They're becoming more intelligent. Uh, but to actually take advantage of that, you need to give your model the actions and the capability to take those actions. Um, and one way that we do this internally is that, uh, as we talked about in a recent blog post, we launched auto mode in cloud code, which is a classifier that tells Claude what actions are safe to take. Um, of course you don't want to just allow your uh your model to kind of run wild and maybe delete everything uh in its environment. And so so you do want to be a little bit controlled with what it has access to. Um, but doing it in this kind of classifier way allows us

**[380:20](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22820s)** to uh to kind of strike the right balance of how much control uh we want to take but also how much control we want to give the model. And finally uh you want to close the agent loop. And what I mean by this is that as we talked about before, models are now very good at error recovery, but it needs to know when it has made an error. And so the way that you tell the model whether or not it's made an error is by giving it a way to verify its output. So for example, maybe if you're building a uh an application building agent, um you might want to give it a computer use tool. And with that computer use tool, it can then QA the front end. It can click around. It can see if it actually works. And that way it can then get that feedback from its environment to understand if it should then go and update the code. So with that, thank you so much for

**[381:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=22868s)** listening to my talk on the capability curve. Hopefully you have learned how to think about models improving over time uh and how you can build for that future. [applause] Hey, hey, hey. It's a cruise.

**[383:40](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23020s)** Heat. Hey, Heat. [music] >> [music]

**[384:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23096s)** >> Heat. Hey. Hey. Hey. [music] Hey.

**[386:38](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23198s)** Hey. Hey. We are happy. Hey,

**[387:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23245s)** hey, hey. me. Hey. Three, four. One, two, 3.

**[389:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23350s)** Thank you. [music] 1. Down it drop down Down

**[390:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23427s)** down down down 1. 1 Down

**[391:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23492s)** down down down down. Turn over. Hey,

**[392:32](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23552s)** hey, hey. [music] One. One. 1. >> [music] one. I

**[393:42](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23622s)** need hey. One, one, one, one, one, one. Number

**[394:48](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23688s)** n. >> [music]

**[396:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23770s)** [music] [music]

**[397:11](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23831s)** [music] >> Yeah. Yeah. Oh yeah. >> [music] [music]

**[398:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23911s)** [music] >> Heat. Heat. >> [music] [singing] >> For real.

**[399:29](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=23969s)** For real. For me, for me, Oh no, for real. for real.

**[400:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24052s)** For real. Keep it. of your day. We are [music] >> [music]

**[402:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24130s)** >> Come on. Come on. Come on. Come on. Come on. Come on. Come on. Come on. a beat. Hey [music] I'm a I'm a I'm a

**[403:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24205s)** >> [music] >> Want [music] [music] to be on the morning. Hey,

**[404:20](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24260s)** [music] I love you. Hey. Hey. >> [music]

**[405:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24356s)** >> Hey, hey, hey. Please welcome to the stage general manager at NRI, Yuki Kitamura. >> [music]

**[406:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24414s)** >> Soch. Fore speech. AI

**[407:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24474s)** system. Fore!

**[409:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24550s)** Foreign! Foreign! You know, You know [snorts]

**[410:07](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24607s)** mechan You know, Fore speech. Fore

**[411:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24691s)** [snorts] speech. >> [snorts] >> for application.

**[412:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24774s)** for >> [snorts]

**[414:23](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24863s)** >> Foreign First party.

**[416:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=24985s)** >> [snorts] >> Fore speech.

**[417:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25047s)** Fore speech. Fore impact.

**[419:16](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25156s)** magical. benchmark.

**[420:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25215s)** Okay. >> [snorts] [snorts]

**[421:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25319s)** [snorts] >> Foreignech. for

**[423:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25388s)** YouTube. >> [snorts] >> Foreign speech. Foreign speech. Foreign speech. Okay.

**[425:23](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25523s)** How come out? Fore speech. Fore

**[426:38](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25598s)** transformation. forchech. Fore

**[428:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25688s)** speech. >> [snorts] >> Fore! Foreign! Foreign! Okay.

**[429:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25765s)** Enterprise. Foreign

**[430:28](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25828s)** speech. Foreign speech. Yes. All right. [applause] 1 2 3 1 Down

**[431:57](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25917s)** down down down down down down down down. 2 1 Down.

**[433:02](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=25982s)** Down. Daddy good. So good. Hey [music]

**[433:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26036s)** me. Hey Hey, hey, hey. [music] Baby.

**[435:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26100s)** Baby. Hey. Hey, One, one,

**[436:16](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26176s)** [music] hey. One. One. [music] One.

**[437:40](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26260s)** Hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey. One, one, one, one, one, one. Hey.

**[438:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26339s)** Hey. Hey. Oh, hey. Hey. Hey. Hey.

**[440:09](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26409s)** Hey. Hey. Hey. I'm a [music]

**[441:10](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26470s)** [music] Heat. Heat. I'm a baby. [music] Heat. Heat.

**[442:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26538s)** Want [music] to be on the mountain. [music] Hey, dick.

**[443:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26598s)** Dick down. Dick. Hey. Hey, I'm

**[444:35](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26675s)** >> [music] >> Dick dick down. down. Hey, hey, hey. Down.

**[445:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26741s)** [music] Hey. Hey. Heat. Hey, Heat.

**[446:59](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26819s)** Hey, Hey, hey, hey. For me,

**[448:40](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26920s)** for me, for me. For me, >> [music] >> for me. Hello

**[449:53](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=26993s)** for real. He We are of your day. Oh no.

**[451:30](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27090s)** Please welcome to the stage product management lead for the cloud platform Brad Abrams and member of technical staff of Enthropic Rod Howworth. Claude, Brad Abrams, Enthropic Technafu, Rod Howworth, Sama. [music] >> Well, [music] good afternoon. Thank you for coming. Um, you've almost made it to the end of Code with Claude. Thank you so much for your hard work in pushing through this. Uh and this session is going to be well worth your effort

**[452:18](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27138s)** because in this session we're going to talk about not just building agents but how you deploy agents that are secure, reliable, performant and most importantly cost effective. So you can actually do that at scale. I know many of you have started building agents already. A few of you maybe have agents in production, but only a very few are really happy with the performance, reliability, and cost effectiveness of their agents. So, this talk is really going to drill into that and that will make it well worth your time. So, let's drill in. Um, and first before we talk about any of the other techniques uh and tools that we'll cover today, I want to talk about prompt

**[453:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27185s)** caching. This is the single most important takeaway of the talk is around um how you do prompt caching. You see in longunning agentic applications there are many tool calls many user turns and a very long the transcripts get very long and each request to the API then repeats these long segments of prompt and if we have to recomputee those segments every single time it's expensive and slow. So we offer prompt caching which lets us premputee the shared part of the context. Uh we store those in an intermediate value. We call those K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K K KV values, but we store those premputed parts of the prompt uh up on

**[453:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27236s)** our our servers. Uh and then the next request that comes in, we just have to do the small delta from the previous request. Uh and that saves a lot of compute. uh and we pass that savings on to you. So the most important benefit of prompt caching, it's at a 90% discount. So you pay only 10% of the cost when you use prompt caching. In addition, you get faster uh response times and your rate limits aren't affected by prompt caching. If the for any tokens that are cached, we don't count against that for rate limits in the in the API. And we've got some customers that have done a very good job in prompt caching. If you look at perplexity, cursor,

**[454:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27284s)** replet, uh all of these customers have spent significant engineering effort to bring their cache hit rate up very high. In fact, if if these customers didn't have such a high cache hit rate, we we couldn't even uh uh serve their workload because there's just not enough compute without without prompt caching. So, it's very important. But the good news for you is you can get similarly high cache hit rates with with much less amount of effort. There's two techniques for that. One I'm showing you on the slide here is if you go into our developer console, our our cloud console, you can see this new dashboard that reports where reports on your cache hit rate. The agent I'm showing here has a only a 56% cache hit rate. So, it's

**[455:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27333s)** got some room for improvement. Uh, I invite you to as soon as you get home, uh, go and check out what your agent's cash hit rate is. If it's not up in the 80s, then I would suggest that's the first thing to go work on because, uh, many longunning agents, you can get the cash hit rate that high. The second big tip I'll give you, uh, to get your cash hit rate up is to use our, uh, clawed API skill. So it's a new skill. It's installed by default with cloud code. So if you if you have access to cloud code or if you have another development tool, you can use it because it's just a skill. But it knows very well how to do prompt caching. So if you just go into cloud code, open your project up and say improve my cache hit rate, it will start working with you to modify the prompt,

**[456:24](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27384s)** add the cache control headers and and whatnot in order to get your cash hit rate up this high. Okay. In order to um see what this looks like, I'd like to invite Rod out. Rod has worked on a demo. Uh so Rod, would you like to come out? [applause] Yes. Rod's actually one of the lead engineers on on the API team. So if you've built something with API, you're probably running his his code. Um, so the let's switch over to the demo machine and see what Rod's got for us. So what we're building here is a dashboard for a CEO. A CEO has a set of objectives and what we've done is we've written an agent that goes out and Wait

**[457:13](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27433s)** a second, Rod. Is is this is this the right UI? Well, we're we're Code with Claude Tokyo and you bring this like 90s looking SharePoint UI. I don't know. But I I think we can do better. Do you think we can do better? Let's see if we can do better. Rod, do you have Claude code on that machine? Okay, Rod's got Claw Code. Rod, see if you can give us a better theme. What? Let's think about what might be more appropriate for this audience in Tokyo. Yeah, Brad thinks it's more Yeah, that's exactly right. Um, remember this is the end of the day. We need to keep this exciting. So, Ro Yeah. Okay. Rod's gonna make a superhero theme demo. I think that's much more appropriate. So again, we're using cloud code modifying this the source of our demo locally and we're going to flip back over. Ah, much

**[458:02](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27482s)** better, huh? Okay, so we're no longer the CEO of some boring corporation. This is now the dashboard for the CEO of Hero Corp. And what Hero Corp does is it rents out superheroes for to defend your city, to defeat uh villains, and to show up at kids birthday parties, whatever is necessary. But we still have a set of objectives, and we're reporting on the status of those objectives by scouring all the data that this corporation has. So, we have a bunch of tools that bring in that data. In fact, just to get a sense for what this site looks like, uh, Rod actually put in a nice developer console. So, let's see the developer view of this site. You want to pull that out? Um, here's our dev view here. And you can see we've got a a couple of

**[458:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27532s)** tools there. The Outlook search, we'll get into this later. Um, and you can see how Rod is invested in prompt caching. And wait, Rod, it's a 0% cash hit rate. Dude, we talked about doing pro. I gave the whole thing on prompt caching being so important. 0%. Okay, Rod, maybe you can implement prompt caching real quick. So, Rod's going to go into cloud code and implement prompt caching for us. Um, and what we should see is once we get prompt caching implemented, we're going to reload that site and we should see that cache hit rate go up. Yeah. So you see initially it did a couple of cache writes and now it's um doing some cash hits. So with one little change we got

**[459:40](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27580s)** up to 50 58% cash hit rate. I invite you to look at this over the course of the demo. Uh as we add more uh functionality to it, you'll see that cash hit rate goes up even further. Okay. Yeah. So this demo is looking um pretty good here. Uh we've got the objective one. Let's just scroll down and show there's actually four other objectives. So, this first objective is about retaining top talent. Uh, objective two here, let's see what objective two is. It wait, we didn't even load objective two. It says it it says we like we r we've run out of context and we didn't even get to objective two. You can see the context window indicator here, right? It gave you a million token context. We

**[460:28](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27628s)** only got to one of the four objectives with a million tokens. I I think we can do I think we can do better. You know what I think we need? We need a little context engineering. So, let's switch back to the slides and let me talk about context engineering for a minute. Okay. Um, context engineering is the discipline of deciding what belongs in Claude's context. And it really is an engineering technique as we'll talk about because you want enough in Claude's context for Claude to make good reasoned decisions, but you don't want so much that's distracting and expensive uh and slow. So you want to be thoughtful. You want to know and understand exactly what is in the context. Uh today I'm going to talk

**[461:16](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27676s)** about three different ways tools that you have in order to be able to manage the context and agents that you build. The first is tool search tool and that's going to keep all the tool a bunch of tool definitions out of your context. The second is programmatic tool calling and that's going to keep a bunch of the tool results out of your context. And then finally I'll talk about compaction. So let's drill in. So with tool search tool uh the key problem it solves is that many agents have 10 20 hundred tools in order to do their jobs. And and we want agents to have a lot of tools. We want our agents to be general purpose and productive. We want to

**[462:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27724s)** decompose things in rational ways with tools. So it's not crazy to have 100 plus tools. What's crazy is to put a 100 plus tools in the context because as you see in the without line at the top, if you have a hundred tools, you're going to consume most of your context with just tool definitions, leaving only a little bit for the actual running of the agent. Um, and that's not very wise because most of the trajectories, most of the runs of your agent may only use 10% of those tools, yet you've loaded them all into context. you paid for that in terms of uh cost, you paid for it in terms of latency. Um so tool search tool on the other hand, if you look at the bottom, what we've done is we just loaded one tool, the tool search tool,

**[462:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27772s)** and then when the model decides it needs a tool, it first asks the tool search tool, hey, do you have a tool for this? And then uh the tool search tool searches over its inventory of tools and picks uh the right one for that query uh and loads that into context. And so consequently what you see here is you get much more um agentic space. You're able to use the context much more efficiently because uh you only load exactly the tools you need for any given run. So you can have a lot of tools available and only use the ones you need. And customers like Lovable um have really seen some benefits from this. Just with this change alone, they reduce their token usage by 10%. So imagine

**[463:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27821s)** basically they got a 10% savings uh right off the top. Um but not only that actually much more important to lovable was that the intell the performance the intelligence was was better for everybody because when the model gets so much into context sometimes the judgment isn't quite as good and so by reducing what goes into context um the the model itself performs better. Okay that's tool search tool. Let's switch and talk about programmatic tool calling. Um, and I'll say I had a lot of fun with Fable building out these animated uh diagrams. So I hope you appreciate all the tokens I wasted to do that. Um, so with programmatic tool calling, the goal here is to get the

**[464:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27871s)** intermediate tool results out of the context. You see many tools you you actually want to design the tools so that they return lots of data because you want the model to have whatever context it might need. So you want the tools to return a lot of data. But if you have a tool like say the Outlook tool we saw earlier and it returns a 100 emails, well that's going to eat up a lot of your context when maybe you only needed the header of one of the emails. Um, or if you have an HTML page, maybe you only needed um a small div tag out of it, but you loaded all of that into context. So the the what we did to solve this is actually just lean on the fact that our

**[465:20](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27920s)** models are actually very good at writing code. So rather than um just using a tool call what we do is we do the tool call we get the full results out of the tool call and then the model is able to inspect that schema and then it's able to write code against the schema of whatever that arbitrary block of data is. So in real time it can write code and then pull out just the bits of information say 5% 2% of that data pull out just what it needs and put that result into context. Um and this we for for any tools that return lots and lots of data this is a great benefit. Um, and customers like Kora have seen big

**[466:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=27968s)** benefits from this for for um Kora's agent. They do a lot of HTML. They pull a lot of HTML in and they were pulling full HTML pages in when they only needed just a little bit of the page. And when they moved to this, it really helped their agent perform so much better. Okay, that's programmatic tool calling. Next up is compaction. So even if you do a great job on tool search tool and um uh programmatic tool calling, you may still run out of context because they do still um have have context. So if you're if you have an agent that is very ambitious that needs to run for hours or even days, then you want to do something like

**[466:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28016s)** compaction. And what compaction does is it lets you as the developer set a threshold. You can say I want to use only 400 or 500k of of my 1 million token context window. I want to use some only some part of it. And then when the context gets up to that point, gets close to to that point. What we'll do is we'll pause execution of the agent. We take another model, have it summarize the entire transcript, strip out all the things that are just not needed anymore. All these intermediate tool results and tool calls and whatever they they they're not needed like the res the the decision that needed them was already made. So you don't need to keep them for

**[467:43](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28063s)** historic reasons. Then we just clear all of that out of the context and just put a small tight summary of what happened so far. And then we restart the agent. It just picks up exactly where it left off. And because we have worked on making that summary a really good summary, then the agent has enough context to just pick it up and keep going. So it feels very seamless to to developers. And we saw companies like Hex pick this up. Um turns out Hex had already implemented a version of this. So they were able to uh remove 300 lines of code and just not have that maintenance burden. uh much better to have Rod have the maintenance burden than you. Um okay so that's compaction. So we talked about these three things. I think we should take a look at them live and see if they can improve our Hero

**[468:31](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28111s)** Corp app. So let's switch back to the demo. Okay. When last we left Hero Corp uh yeah let's just leave it. When last we left Hero Corp remember we consumed a million token of context with just one of our four objectives. Um, so we want to see if we can actually make this load uh using this. So Rod, let's just go ahead go into cloud code and let's just enable all of these. We're going to enable tool search tool uh programmatic tool calling and compaction all in one go. Get all these strategies configured. So um okay, so we have all these going. Now if we switch over and reload this, notice a lot more things are happening. Now you see the context window is going up. The um activity stream you're seeing

**[469:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28161s)** lots of tool calls because we're filling in every one of those objectives. So really with just a small bit of additional engineering, we get so much more uh value out of this. So yeah, we got all of all the objectives loaded. Um and we ended up with a much smaller context. So let's uh walk through these one at a time and just make sure we really get each one. So let's go let's start with a tool search tool at the very top. The first thing that happened was the model decided to call a tool to tool search tool and it looked for the query you see is a hero retention metrics. Um and tool search tool would said oh I have a tool like that. Here's the schema for it. Um and it's called hero retention metrics

**[470:09](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28209s)** with the underscores. You see it where it says name there. So let's now scroll and see the model actually called that tool. So if we scroll down just a little bit. Yeah, you see it right there. The model actually called that tool and then got its result. Uh so again, we didn't have to load all these 100 plus tools up front. We could just load one at a time. Okay, next up we have um a programmatic tool calling. So this one's interesting. We have this Gong customer digest. I don't know if you know Gong. it meeting transcribe. So it returns this entire transcription of a meeting which is nice to have but really we only wanted the sentiment of this meeting. And so rather than just that whole transcript um if you we look at the code executing uh the

**[470:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28256s)** programmatic tool calling one you see that it actually wrote this code. It used code executor to write this code. Um, and you can see there's calls to all of those methods. All those tools are there. And then it pulls the JSON out and prints only a little bit of the JSON, only the smallest piece that we actually needed for this run to happen. And that saves a lot of context. Okay. And then finally, we talked about um compaction. So you can see here, here's compaction. It fired. We dropped 9K. um brought it back down to 10K and then you can see the summary that was done. We we're being clear with the model that's pick the agent that's picking this up. Here's the objective.

**[471:44](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28304s)** Here's the data we already gathered. Here's what you need to do next. So, it's a really tight summary. Um so, actually, why don't we run it one more time and just look at that context window line and see if you can see it grow a little bit at a time because we're using convex engineering. And then we set that threshold at 400K. So, as it gets close to 400K, you'll see compaction happen and the um context goes way down and then starts building again. So, let's see if we can see where that happens. If the demo gods are with us. Did I miss it? Did it happen? It already happened. I missed it. Hopefully, you caught it, but I missed it. Okay, beautiful. Okay, we saw all our things. Let's switch back. Oh, yeah. One one thing though, nobody has really commented on this, but I mean I'm not from Japan, but I think

**[472:34](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28354s)** 1,600 yen is a lot for one request. Is that right? Is that a lot of money? That's a lot of money for one request. Yeah, I think we can do better than that. So, let's switch back to slides and talk about how we can optimize that a little bit. So, the way we're going to optimize this is to talk about advis the advisor strategy. Really, the insight from advisor strategy is not going to be new to you if you've ever worked with a development team. You know that you can make a junior engineer on your team more productive just by giving them access to a senior engineer. If you just let a senior engineer review their code, let the junior engineer ask the senior engineer a couple of questions every day, that junior engineer will get way better. Uh, and it will cost the senior engineer just a little bit to do that.

**[473:23](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28403s)** The same thing is true with models. You can take a small inexpensive model um and make it way better by giving it a tool to let it talk to a bigger model. So if you have a model like a sonnet or ha coup, you can make those models way smarter uh by giving them an advisor that's opus or we launched fable today. So you could use fable for that as well. Um, and I know I heard some murmurings about the the cost of Fable being 2x what Opus is. This is a great way you can get some of the reasoning capabilities of Fable for a fraction of the cost because it turns out Haiku and Sonnet are so good at writing code. They're so good at doing tool calling.

**[474:11](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28451s)** The thing they're not as good at is really deep insightful reasoning. So, why not let Haiku and Sonnet do what they're good at for less money and then um only use uh models like Opus and um Fable where we you really need that differentiated reasoning and we see customers like Bolt doing that. So, let's switch back over to the demo and take a look at how that plays out. Um so you can see if you scroll up to the top of the activity stream you see we're uh in the debug view uh and we'll see the model that we're using right now is opus 48. So uh if you go into cloud code and we'll switch on the advisor mode. Um, so now we could do something. We could just

**[475:00](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28500s)** change it to sonnet and that would be cheaper, right? But the problem is this is a dashboard for our CEO making business decisions. We can't afford to be wrong, right? So we need to be inexpensive and we need to be right. Both are important. So now we switched it. Um, and it showed the line again. I probably missed it at the top. It's in the activity stream. It's well, okay. Yeah, let's look at this. So now what we're doing is we're using sonnet to call all these tools sonnet's calling um and what happened is sonnet is calling the advisor periodically through this and this particular example that rod found for us sonnet calls the advisor and uh running opus and opus actually disagreed with the decision

**[475:48](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28548s)** that sonnet had made sonnet had said yeah this metropolis deal green check it's on track. Opus looked over uh the transcripts and actually caught a problem. Said, "Oh, Sonnet, you missed this one case." Turns out the in a buried at the bottom of a Gong transcript, the mayor of Metropolis said he really wanted CL uh Cryane, he really wanted Cryoane to come uh to the to the opening. Um and that got missed by the account team. And so it's actually red. So, if we look at the deal, you see that it's red. There's a a red item there. Um, and that's thanks to Yeah, we can find it. Um, that is thanks to the the Opus Advisor. So, we didn't just save We

**[476:39](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28599s)** save money. That's great. We saved money, but we also kept this level of uh higher level reasoning. And so, if we go ahead and click that, then boom. the uh CEO has now rescheduled Clyophane and we're gonna make it we're going to close this deal. Okay. So, I think what we uh what Rod was able to show us in this demo is uh with Advisor we can use more inexpensive models and use more expensive models only where they're needed. Uh three different context management context engineering techniques and prom caching. So, thanks a lot, Rod. I appreciate it. Okay, back to slides. Okay, let's just wrap up. Yeah, we talked about prompt caching. You should

**[477:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28647s)** be at 80% if you're building an agent. So, definitely check that out. We talked about tool search tool where you can um keep that from filling up your context. Programmatic tool calling to keep the tool results out. And then compaction. And finally, we talked about advisor where you can use more inexpensive models and get the same level of reasoning. But the cloud platform is evolving very fast. Um, and it's a great way to stay up on the latest capabilities. Uh, this is just what we launched in 2026. I can't believe how many items are on this slide. Just in the interest of time, I'll just call out a couple. Um, I'm a real big fan of the workload identity federation or or whiff. What whiff does is it removes the need for an

**[478:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28695s)** API key. So you I I I know a lot of customers maybe check in API keys into source code, leave them lying around. They could be a leak risk. If somebody gets your API key, they can query on your behalf. With um work uh with whiff, that's that's eliminated. And then the other thing I'll mention is just today we launched uh the fable model and in it's a mythosclass model. So we had to put additional safety classifiers on it. Uh and that means the block rates a little bit higher on that model than on other models. And so we launched a fallback feature. So now on the messages API you can just list a few other models. you can say, "Oh, if Fable can't handle it for whatever reason because the classifier fires, then it can it'll just the request will just automatically

**[479:05](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28745s)** fall back." And that makes it have a more reliable, robust experience. So, that's just two of all the many things that we've launched and and we're only halfway through the year. So, with that, I will thank you very much and enjoy the rest of the conference. Thank you. [applause] Hey. Hey. Hey. D.

**[480:17](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28817s)** Hey. Hey. Hey, hey, hey. I feel a

**[481:13](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28873s)** One, two, three, four. Hey. Hey. Hey. One 2 3 4

**[483:02](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=28982s)** >> [music] >> I'm a I'm a [music] Want to be [music]

**[483:54](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29034s)** a >> [music] >> Happy. [music] [music] You want to

**[484:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29096s)** be on for the world. Hey, [music] hey, hey. Hey, take it.

**[485:56](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29156s)** Hey, hey, hey. Hey, hey, hey, hey, hey, hey, hey, hey, hey, hey, hey. Everything.

**[487:24](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29244s)** Hey, it's funny. for real. [music] For real. >> [music]

**[488:23](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29303s)** >> for real. For real. >> [music] >> for me. Oh no. for real.

**[489:27](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29367s)** For real. Keep real for real. We are on [music] your Hey.

**[492:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29524s)** Hey. Hey. Hey, hey, hey. Hey, dick.

**[493:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29581s)** Everything [music] down. Down down down.

**[493:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29632s)** Don't rock. >> [music] >> Sh. D.

**[495:08](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29708s)** Hey, hey, hey. [music] Good. So good. So good. Please welcome to the stage Japan

**[496:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29793s)** developer community lead at Enthropic Junichiro Tsuji stage. Anthropic develop community. [music] Relax. Hi

**[497:47](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29867s)** PlayStation. Engineer community. for

**[499:04](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=29944s)** software. Fore software. software. computer.

**[500:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30033s)** Smartphone. data software. doain.

**[502:03](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30123s)** Fore speech. Africch. San Francisco,

**[503:21](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30201s)** San Francisco. Fore speech.

**[505:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30301s)** Uganda California. Jose.

**[506:25](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30385s)** So I put soft. I know.

**[508:41](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30521s)** Engineers. Bottom up.

**[509:55](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30595s)** Foreign [snorts] speech. Foreign speech. Foreign speech. Fore company. Yeah.

**[511:15](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30675s)** Bottom up. Extension Founders The

**[513:01](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30781s)** community. Community community. Ambassador Ambassador

**[514:34](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30874s)** program I'm speech.

**[515:33](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30933s)** Hi. Evening reception. Fore! [applause] [applause] Feel Hey,

**[516:36](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=30996s)** hey, hey. Hey, hey, hey.

**[517:49](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=31069s)** Hey, hey, hey. Hey, hey, hey. Dick

**[518:36](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=31116s)** dick dick. Dick down. >> [music] >> down.

**[519:37](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=31177s)** Hey >> [music] >> Hey chick down. down. Take

**[520:52](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=31252s)** Yeah. Let's go. >> [music] >> Hello.

**[521:51](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=31311s)** [music] happy up happy up happy up happy up happy up happy up happy up happy up happy up happy up Happy birthday. Hey, hey, hey.

**[523:06](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=31386s)** Hey, hey, hey. Christmas happy. Hey, One, one,

**[524:22](https://www.youtube.com/watch?v=GiqyYQdYoIY&t=31462s)** hey. One, one. One. >> [music] >> Round One. 1.
