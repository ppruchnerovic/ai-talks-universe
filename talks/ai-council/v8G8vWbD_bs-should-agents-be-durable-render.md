---
id: v8G8vWbD_bs
title: "Should agents be durable? | Render"
slug: should-agents-be-durable-render
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "Practitioner AI conferences"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: null
duration_min: 22
published_at: 2026-06-16T18:45:34Z
video_id: v8G8vWbD_bs
url: https://www.youtube.com/watch?v=v8G8vWbD_bs
youtube_url: https://www.youtube.com/watch?v=v8G8vWbD_bs
tags: ["AI"]
topics: ["Agents & orchestration"]
transcript: true
---

# Should agents be durable? | Render

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `22 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=v8G8vWbD_bs) · [Conference site](https://www.aicouncil.com/)

## Description

Most AI agents never make it to production. The infrastructure underneath simply wasn't built for workloads that are unpredictable by design.

In this workshop, Joey Baker walks through why traditional infrastructure breaks down under agentic workloads, what durability actually means at the task level, and how to express operational guarantees directly in your Python code.

You’ll leave with a working production demo of self-orchestrating agents that don’t require any pre-provisioned infrastructure, custom retry logic, or separate config to maintain. Just annotated functions that handle parallel execution, survive failures, and give you full visibility into what happened and why.

If you’ve ever watched an agent nail a demo and then spent months trying to make it reliable in staging, this one is for you.

SPEAKER:
Joey Baker - Senior Engineering Manager, Render

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*3,398 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=0s)** Thank you all so much for coming. I'm Joey. I'm like, I'm Giuseppe and I'm uh work at Render. I work on our uh runtime team uh which this year is really focused on the runtime for people building AI agent infrastructure. Um so, I want to talk a little today about uh the difference between um demos and actual production agents. Um so, everybody in this room has probably seen an agentic demo that blew you away. Um the agent goes through some complex tasks, magically returns the right answer, and it looks amazing. So, then someone inevitably says, "All right, let's ship that off to prod." And then 6 months later, you're still firefighting it in staging because scaling agents is hard. Um so, there's a big gap between a compelling demo and a actual reliable

**[0:49](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=49s)** production system. Um here in May 2026, LLMs are pretty good uh at raw code generation, but a frequent failure mode is the actual architecture of the infrastructure that they run on. Um so, that's what we're here to talk about today. Um before I keep going, uh if you haven't signed up for Render yet and want to build with us in a few minutes, please go sign up for Render right now. Uh that link right here is rndr.me/workshop. And then secondarily, uh if you would like to develop on Render today for free, um please go to this link right here, um and we will make sure that you have uh a workspace that you can work in and build with us for free. Um it will look later on like we're charging you, but we're not if you

**[1:35](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=95s)** follow this flow. Great. Let me resume. Um so, these are charts of the uptimes of models that you have heard of before, I promise. Um there's something that's maybe uh clear here. Um one of the key bits about agents is their inherent unpredictability. Uh everything that goes wrong with agents often traces back to that unpredictability. How long will run, how much compute it will need, the temperature of the model. So, these screens are showing you another part of the unpredictability. The infrastructure that you rely on is also inherently unpredictable. And this randomness is load-bearing. You want agents to have flexibility and to be able to return different things in

**[2:25](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=145s)** different situations. And unfortunately, most of today's modern infrastructure is built for a different world. It's built for a world where the same input produces the same output. That is not the case today. That contract is broken and most infrastructure hasn't really caught up to this reality. To take this to an extreme case, if you extrapolate from those charts I just showed you, there's a very high chance that something goes wrong. For a 20-step workflow, there's a one in five chance that your job is going to fail. That's a problem. Restarting from scratch is expensive in terms of time and money. So, you want to not have to do a full restart every time that you run into a failure.

**[3:12](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=192s)** And that's just on the agent side. You also have your own APIs, your databases, etc. that you have to deal with. Every single step here compounds risk. So, how do we deal with this? Well, one easy way on the infrastructure side to handle this is to make sure that you over provision. Fantastic. You make sure that you have enough worker pools, enough idle compute, make sure that you can respond reasonably when load spikes. Great. Then the bill comes and your finance team comes in and says, "Hey, is there any way we can cut costs?" So, you scale back down and now you're under provisioned and the agent hits some memory ceiling and ooms 40 minutes into the task and the user gets the error and you've lost a user. Um, this fixed infrastructure is the

**[4:00](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=240s)** wrong model for this new non-transactional workloads that we have today. Um, there's no static capacity number. It's a moving target constantly. Great. Um, so what does the right abstraction looks like? Well, um, it really needs to be durable infrastructure that maintains state across failures um, and has three important properties. The first here is, I'll call it elastic compute, meaning you should only have to pay for the capacity that you're actually using. And it should dynamically scale as you need it without having to pre-warm the system or anything like that. You should be able to handle one or 10,000 things all at the same time and it should be transparent. Secondly, you need durability all the way down to the individual task level. A

**[4:50](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=290s)** crash 45 minutes into a long-running agent shouldn't mean a complete failure of the run. Durability means that your system remembers where you were, you can recover at any point of failure not having to go all the way back to the beginning. Last, um, you need full visibility. Um, part of durability is about being able to understand what went wrong and why it went wrong so that you can debug it and fix it for the future. Um, and this is true by the way both for humans and for agents that are doing that debugging for you. Great. Um, so I want to tell you about a thing that we're building at Render that does this. Um, and you're getting a little sneak peek of the thing that we're going to build here in a second. Um, so, um, Render Workflows is a durable layer that's designed specifically for

**[5:37](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=337s)** long-running jobs and agentic workloads. Um, the idea is simple. You just write out your logic in functions and then all you have to do, um, is wrap it with a little bit of code and you're done. Um, you don't have to manage queues, worker pools, build custom retry logic. Um, you just describe in code what you need to happen and Render will take care of all of the rest. So, to go back to the problems I just laid out, here's how we solve this. Um, we have sub-second spin-up times, uh, which means you don't have to over-provision to stay responsive. Um, the declarative retries means that a crash at step eight means that you can retry right there and not have to go all the way back to the beginning. Um, you can support tens of thousands of concurrent tasks all at the same time. One or 10,000 is all the same.

**[6:25](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=385s)** Um, and you get a full run history of everything that goes on so that you can understand what went wrong when it did. There's no guessing here. Um, and we have also state checkpointing, which is not here today. This is a beta product, but it is coming soon. Um, so that you'll be able to eat manually checkpoint any given state. Um, and you're getting this preview on the engine that we're going to work on here. Um, I want to give you a little bit more of a taste of how this actually looks. Um, here's an example of how this could fit in your code base. Um, we support both TypeScript and Python today, so you're getting the same example, two different ways. Um, so this all operates via an SDK. Um, you can install the SDK, you initialize the client, and then really all you have to do for any given task, in Python, you just toss a decorator right on top of

**[7:12](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=432s)** your function. You're done. Um, the mental model here is actually really important because instead of going off somewhere else and configuring your infrastructure, you're annotating the code and that is also your infrastructure right there. Um, this is actually kind of important for people writing code with LLMs because LLMs tend to operate file by file. Um, and that means as much as you can co-locate concerns into one file, the more likely you are setting up your LLM to succeed. Um so that's a huge part of the design here. Um there's um also no framework to learn or like um YAML sidecar config files to manage. It's all right there. It just works.

**[7:59](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=479s)** Great. Um hmm supposed to be a video here. Let's see if that works. Yeah, okay. So this is um another preview of this app that we're about to build, but you can see um how workflows operate here. You define a bunch of different tasks uh and then it works through those tasks both in sequence and in parallel and potentially massively parallel all at once. Um the shape of this product by the way is good for yes, AI agents, but it's also shaped like ETL pipelines, image processing pipelines, um all sorts of things are shaped this way. Um so to run through this example and the video played a little bit too quickly here, but uh this agent um is responsible for producing a website at the end of the day that shows all of the new restaurant openings in San

**[8:47](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=527s)** Francisco cuz I like to go to new restaurants and this is a fun way to detect them. The way this works under the hood is it has to go off and scrape new restaurant information from a bunch of different sources. It then ships all of those things off, which again could be zero, could be a hundred, um to an LLM uh for data extraction and data cleaning. It then uses LLMs to uh deduplicate um and make sure everything is consistent um and then goes off and again by a scraping attempts to discover the menus of all of these new restaurants so that it can then go find via an LLM the dietary information like is it vegetarian, does it have gluten-free options, that sort of thing. Um there's a lot of moving parts and without workflows you would need to configure a job to a worker pool, retry logic, and this is all scattered across

**[9:34](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=574s)** a bunch of different files um and there'd be a lot of like interdependencies that you would have to work out. With workflows, you just decorate your functions, uh, you're done. Okay. Um, a little bit more on the durability here. This is an example of how you can configure retries. Uh, we automatically set this up for you, but if you want more control, it's here for you. Um, and you can see on that like line right there with retry, you can max retries, the wait duration, backoff um the task, um, if it doesn't finish within 2 minutes, we'll kill it, um, and count it as a failure, uh, cuz you don't necessarily want LLMs going off and doing the wrong thing. Um, you don't have to worry about threads or manual state tracking, um, or manual retry logic. The platform will just handle all of this for you.

**[10:24](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=624s)** Great. One last thing here on how it actually looks. Um, >> [clears throat] >> we have this thing for automatic task discovery. So, this is code kind of showing you the start of the agent working. Um, and you can see that it goes off in parallel and fires off a bunch of different tasks. Um, and it's doing this via language primitives. So, in Python, this means asyncio. There's no like other magical thing that you have to use. It's all native to the language. So, your code doesn't have to really change, uh, in order to adopt Render Workflows. Um, it's also important to point out that unlike other orchestration platforms, we don't need a manifest or a DAG of config files. Um, it's all just right there in your code with a few lines.

**[11:13](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=673s)** Um, yeah, that's it. Great. So, let's build something. Um, there's a QR code right here, um, or you can go to render.com/workshop. Um, this is a document, um, which will walk through actually building this app if you're curious to build on with us and I'll demo that right here, too. Um and let's start doing that right now, actually. So, I'm going to demo this for you. Free to follow along and if you followed the steps earlier, you should I believe be invited into a workspace. Great.

**[12:02](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=722s)** I'm saying we should pop up the form one more time, so let me go back. This This one here? Great. Okay. So, if you want to sign up and do this for free with us, please feel free to. >> Awesome. I'm doing that right now as well. Just ask Just ask Chris or why aren't we using Render's SDK? Because we have our back end hosted on you guys. So, >> Absolutely. So, this is This is an example that uses the Render SDK, actually. Yeah. Fantastic. All right. Hopefully everybody's got that. >> Awesome. So, for those of you who want

**[12:54](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=774s)** to go through this build right now, there are three members from Render. You can just raise your hand and then they'll come and help you with any issues. All the Render team who can help, please raise your hands. Awesome. >> Yep. So, if you need help, there's people who actually built this in the room. >> [laughter] >> So, they're happy to help show you what this is. I'm going to start walking through this. So, we've got this GitHub repo right here that has uh this app already built. Um thank you in large part to Claude. Um and um we want Oh, I need to sign in. >> [sighs]

**[13:45](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=825s)** >> Great. Okay. So, we just want to use this template. We'll create a new repository here. Um I'm going to claim ownership. Great. All right. Um in this doc you'll also see sort of an architecture diagram of how this agent works um and how it uses workflows in order to do its job. Uh I'll admit it's a little over-engineered just because we wanted to play with workflows. Um it uses workflows for things like sending out push notifications um which is a totally valid use case of workflows, but as I say, a little over-engineered for such a

**[14:34](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=874s)** simple application. Um great. So, I'm going to keep going down here. All right. So, I've created the repo. And then I need to copy the repo URL. And I need to join the correct workspace. Oh, let's go up here. I'm going to need to sign in. Hopefully everybody was able to sign in okay.

**[15:33](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=933s)** >> If you have any questions about anything I said, please feel free to raise a hand and I can work that through as we talk this or ask answer as we work this through. Yes, please. >> I'm just like on the under the hood, so I'm guessing for the compute like probably talking for that, but can you talk about like state where that's stored and like how, you know once the workflow stops running, how far back can they go and some of those things? >> Yeah. Um so we take care of storing the inputs and the outputs of any given task for you. That's there. We'll show it to you in the dashboard where you can see kind of how every run of the workflow went. We maintain that for paying users for 30 days. Um one other point on state uh you can hand in more or less anything

**[16:22](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=982s)** you want, but for performance reasons we often advise if you have large amounts of data that you want to pass into your workflow that you store that in object storage and then hand into the workflow the URL to the object storage so that the workflow can then go pull that. That actually winds up being way easier for people to debug down the road. Great. Any other questions? Great. Um I'm going to keep working through this doc here then. So it's trying to render. And I Raf, did you already add me in to the workspace?

**[17:13](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=1033s)** All right. Yep. Thank you. Okay. Uh, so in the workspace and then I need to Yep, I already did that. All right, so then I wanted to play the blueprint, which means I need to make a change um over in GitHub. So for non-workflow services, um Render has this concept of blueprints, which is basically um your infrastructure defined as YAML. Um and it's um custom to Render so that you can very fine-grain control um what actually exists on top of Render. Um so we need to make a change to one of

**[18:03](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=1083s)** these things. I forget which one. Oops. Right, we just need to rename the project. Cool. So I'm going to make it Joey. Commit that change. Yep. Thank you, Copilot. All righty. Um and then >> Don't mean to interrupt, Joey, but is Render working on the um added layer of for observability um that's native to Render? >> Yeah, so today Render offers um a number of things in the observability space. Uh we offer um for all of the different

**[18:51](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=1131s)** types of services that we provide, um we offer observability into there and that's everything from like um compute usage uh to the actual application logs that are coming out of that. Um we have also um been working hard within workflows on a different level of observability with we call it our execution viewer, but it's that view I showed you earlier where you can see every step of the workflow, um exactly what was going on there, how long each step took, uh and I in the future we'll be adding things like logging and tracing right there so that you can see, for instance, like when a particular task goes out to an LLM and asks it to do something, uh you want to be able to tell how long that took, maybe how many tokens that consumed, that sort of

**[19:40](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=1180s)** thing. Great. Did I answer your question? >> Yeah, that did. Thank you so much. >> You bet. Okay. Uh yep, we need to create a new blueprint instance. So, that means I can come over here to blueprints and I'm creating a new blueprint. Now, I need to >> Speaking of instances, um how does Render help manage the and scale the workers? Is that something built in within uh >> Yeah. >> workflows? >> Um yeah. So, we automatically scale as

**[20:30](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=1230s)** you need to scale. Um so, for example, the the thing I showed earlier where you can with in Python asyncio create a loop and just run through a bunch of tasks, that loop could be one thing, it could be a thousand things, and we will just take care of that for you. You don't have to preconfigure how many things you want. Going back to the point earlier about you really want, I'll call it elastic compute, um so that you can get as much as you need when you need it. Um historically people have handled this with serverless functions. Um there's a downside to that, though, because serverless functions are usually capped at a max duration on runtime. Um Um, and for a lot of AI agents, you really don't want that restriction. You want to be able to go for as much or as little time as you need. Um, so on

**[21:19](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=1279s)** Render, um, a task has a minimum runtime of 1 second, um, and a maximum runtime we artificially cap it today at 24 hours but that's something that if you need more, talk to us. Um, we can make that happen. Yeah. >> So, the backend access, is it through Render or you bring your own >> It is all through Render. Um, so it's a fully managed service. Um, and as a result of that, it means that we can offer you these performance guarantees, um, that would be much harder if you were bringing your own infra. >> Also, do we have a choice of which LLM to pair up? >> Absolutely, yeah. We're not making any deterministic on how you interface with LLMs or any other third-party APIs. You

**[22:07](https://www.youtube.com/watch?v=v8G8vWbD_bs&t=1327s)** can write whatever code you want, we will execute it. >> [music]
