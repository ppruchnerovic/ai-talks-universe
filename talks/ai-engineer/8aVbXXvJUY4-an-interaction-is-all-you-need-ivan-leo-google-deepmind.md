---
id: 8aVbXXvJUY4
title: "An Interaction Is All You Need — Ivan Leo, Google DeepMind"
slug: an-interaction-is-all-you-need-ivan-leo-google-deepmind
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Ivan Leo"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-03T19:30:16Z
video_id: 8aVbXXvJUY4
url: https://www.youtube.com/watch?v=8aVbXXvJUY4
youtube_url: https://www.youtube.com/watch?v=8aVbXXvJUY4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Gemini API", "Interactions API", "Managed Agents", "Google DeepMind", "Gemini", "Antigravity", "AI agents", "agent sandbox", "function calling", "multimodal AI", "Google AI Studio", "Gemini API CLI", "agent infrastructure", "Ivan Leo", "AI Engineer"]
topics: ["Agents & orchestration", "Multimodal, vision, speech & robotics"]
transcript: true
---

# An Interaction Is All You Need — Ivan Leo, Google DeepMind

**Ivan Leo**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Gemini API` `#Interactions API` `#Managed Agents` `#Google DeepMind` `#Gemini` `#Antigravity` `#AI agents` `#agent sandbox` `#function calling` `#multimodal AI` `#Google AI Studio` `#Gemini API CLI` `#agent infrastructure` `#Ivan Leo` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=8aVbXXvJUY4) · [Conference site](https://www.ai.engineer/)

## Description

Models became agents, and the APIs didn't keep up. Google DeepMind rebuilt them.

Ivan Leo, developer experience engineer at Google DeepMind, introduces the Gemini Interactions API and Managed Agents. He traces how we went from single completions to function calling to agents, then shows server-side state with interaction IDs (no more hand-managing thought signatures), strongly typed multimodal outputs, mixing built-in and custom tools, and the new steps data model. He then demos Managed Agents, which run the Antigravity harness in a persistent remote sandbox with environment IDs, loadable sources, a credential-injecting proxy and named agents, plus the open-source Gemini API CLI.

In this talk:
• Why agent workloads need a different API shape
• Server-side state: interaction IDs and thought signatures
• Chaining image, video and audio generation with the same context
• Managed Agents: persistent sandboxes, skills, secure credentials and named agents

SPEAKER
Ivan Leo, Developer Experience Engineer, Google DeepMind
X: https://x.com/ivanleomk

LINKS
Interactions API overview: https://ai.google.dev/gemini-api/docs/interactions-overview
Managed Agents quickstart: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart
Antigravity agent: https://ai.google.dev/gemini-api/docs/antigravity-agent
Gemini API CLI (GitHub): https://github.com/google-gemini/gemini-api-cli
Google AI Studio: https://ai.google.dev/aistudio

CHAPTERS
0:00 Intro
0:12 Interactions API and Managed Agents
0:27 From single completions to agents
1:02 Function calling
1:32 Models that reason and act
2:02 What is an agent?
3:02 Try the models in AI Studio
4:07 Why a new API
5:31 Server-side state and thought signatures
6:21 Demo: chaining image and video generation
7:01 How the code works
7:36 Strongly typed outputs
8:21 Mixing built-in and custom tools
9:01 The steps data model
9:46 Managed Agents: Antigravity in the cloud
10:36 Demo: analyzing a GitHub repo
11:06 Persistent sandboxes with environment IDs
11:41 Loading sources: GCS, GitHub, inline files
12:16 A 2M-token repo analysis
12:56 The same agent locally and in the cloud
13:36 A credential-injecting proxy
14:26 Named agents
15:26 The Gemini API CLI
15:56 Migrating with the Interactions API skill
16:36 Wrap-up

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,507 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=12s)** Hey guys, my name is Ivan. I'm on the developer experience team at Google Demine. And today we're covering the brand new interactions API and our new offering manage agents. And so to take a quote from a very famous paper, an interaction is all you need. Before we move on to what the interactions API is and what the new manage agents offering is let's take a trip down memory lane and let's kind of trace how models have changed and how we've worked with models. So when we first started working with models a lot of times you would have a single interaction you would send a message tell me a joke and then you might get a response for example why don't scientists trust atoms because they make up everything. After a while as models got more and more capable and they understood more about the world this became a bit more complicated. We wanted to take these models, put them in different applications, but to do so, we needed them to be reliable. And so to do

**[1:00](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=60s)** so, we invented function calling, where models could create individual JSON objects with predictable structures. Think like how when you want to register for a website, your web page sends a JSON payload to the back end with a username and a password. And that enables the backend server to say, okay, we have a new user and now we can actually create a new account. that made it possible for us to actually use models in different parts of this application whether it's extracting user information, parsing data and more. But right now we're seeing this incredible cups where models are getting more capable. We're seeing models being able to reason go for very extended periods of time before they come back to people. And so you're moving from a place where we went from completions instruction and functions where we might ask, hey, what's the weather in New York City? and the model has a call weather tool that

**[1:47](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=107s)** it can get that data, ingest it, and generate a response to now a case where models have multiple tools under their belt. They're able to call tools, think and reflect on what the response meant, interact with the environment, and ultimately generate a response. And so this just brings us back to what is an agent. Fundamentally, if you look at what an agent is, it's really a model that powers a huge chunk of it. A lot of people have reduced this to just a language model running in a loop. And for most cases, this is true. If you have a really capable model, you'll find that as we've got models that become more and more capable, a lot of the scaffolding has fallen away. A lot of models, for example, the latest Opus models or fable models are now just immediately just using a bash tool instead of individually specialized tools like a edit file or a read file tool like we used to do. And so really

**[2:37](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=157s)** what we have is a language model that's used to understand the context, the user's intent that's given a bunch of different functions, all different resources that it then interacts with its environment in. It has some short-term memory and some long-term memory to keep track of what it's encountered and then an environment to execute functions in. If you're building a coding agent, but you don't give it an environment where it can actually execute code, for example, it's not going to be able to do anything. And so if you'd like to try any of our models, the easiest way to do so is actually with AI Studio. And so I actually like to point out that my speaker notes today were actually coded on AI Studio. I vived it out 2 minutes before this talk. Uh you'll see the um you can see the conversation history over here. Um I literally said I need a mobile responsive website that I can pass in speaker notes because I found

**[3:24](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=204s)** out I wasn't going to be able to use presenter view. And so what I did, I just gave it some brief instructions and before you know it, you have a simple application that you can use without any hassle deployed on a website that's accessible to all. So we have a really generous uh free tier for most of my presentations. I've just been using the free tier. I haven't been using my Google unlimited tokens thankfully. And I think it's the best way for you to try our models. Whether it's our new speechtospech translation models where you take in some you speak in let's say English and it can translate to any language or you know you want to try our latest models like the Gemini 3.5 flash etc. It makes it very easy for you to do so with simplified UI toggles to just be able to tune all of the different parameters. So let's talk about the interactions API. Now one of the things that we've seen

**[4:12](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=252s)** especially as we've moved from models to a dynamic where now we have models and agents is that the kind of workloads that we want to support have changed significantly right through the Gemini API you have nano banana you have you know Gemini 3.5 flash but you also have very capable agents like the deep research agent that's going to run for anywhere from three minutes and more you interact with it you have some sort of research plan it's going to go out and do its own thing and it comes like a very deep and detailed research reports. Now, it's pretty difficult then to think about consuming models and agents through a whole bunch of these different endpoints. Additionally, for a lot of the older kind of API endpoints, a lot of the data was in in very deeply nested objects. And so you can imagine the kind of difficulties that we had ourselves when we were building in first-party

**[4:59](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=299s)** integrations. And we wanted these use cases where you might be able to generate a nanobanana image, do some research, generate a vo image from there or spawn out all these different agentic kind of like agents that go out and do their own thing. And so the interactions API is our sort of solution to this as we look to build an API that can support all of these different use cases and ones that we can build on ourselves. you look to bring Gemini across the entire surface of the Google ecosystem. So the best place to get started is just with serverside state. One of the things that you'll realize especially as you use the new Gemini series of models is that we essentially have this thing called thought signatures where if you interact with the model, if it calls a function, if it gives a response, it's going to pass back a very opaque series of these numbers. For a lot of people,

**[5:46](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=346s)** manually managing this was very difficult and sometimes when we talked to different startups, we found that they would lose their cache just with a single whites space that they mistakenly added in. So now with the responses API, you can see on the first turn, hi, my name is Phil. And in the response, we give you a interaction ID. And as long as you give us back that same interaction ID under the parameter previous interaction ID that you'll see in the second turn, all that context is preserved. And this is really important with the new Gemini series of models because if you don't give us back those thought signatures, you're going to see a decrease in performance. But what else does this unlock? Here you see a demo built by Vampsy from our team that did an incredible demo where using a single photo, you could generate with Nanovana all these different variations of yourself in different countries and

**[6:33](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=393s)** different locations. Each of these individual photos are a single interaction, but you can think of it from an initial API call. It spawns all these different interaction calls. Using those interactions, the same interaction ID, we then generate a video using the interaction ID and the new Omni model that we just launched. Something like this would not have been possible without the interactions API built by Philip over there. So, actually, it's a really incredible piece of work, I will say. So, to give you an example, an idea of what it would take to build something similar, this is all it would take. First, you pass in Gemini 3.1 flashlight image, generate an image of me in Venice. You take the interaction ID, you chunk it back into the client.create, and this time you specify that you want the Omni flash model instead that we launched on Wednesday. And that allows

**[7:22](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=442s)** you to now use the same Omni model with the same information, the same kind of images, and the same context throughout all these calls. It's making it possible to build more complex, rich, and just these really complex agentic applications. The same thing occurs with audio generation. If you look at the bottom, you see that now we have output.type. In the past, you would have to take this very nested object like completions audio. And it would be very tricky for you to nest it out. I can't even remember it off the top of my head. But now, every single bit of the outputs that come out are clearly demarcated by a strong type. If it's an audio, as you see over here, all you got to do is just parse it and handle it accordingly. Right? But what happens if now I want to generate an image? It's the same method over there, client.interaction.create. All I got to do is just modify the

**[8:11](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=491s)** response modality and the generation config. And now I have an output.type of image. And this makes it very easy for me to start building and experimenting with Gemini. The same thing comes with tool use. You can mix and match different inbuilt tools that wasn't possible before. For example, over here we're trying to get an agent to look up the internet to find the latest security reports for the React application. We've given it access to the same index that Google has with type Google search. We've given it the ability to be essentially retrieve information from web pages using the URL context tool that we ship with. And we've given it a custom tool here called file incident. The model can reason autonomously on its own, figure out what information it needs, and then actually generate a response for you all in a single API call. This makes it very powerful because now you have models that not only can work with information

**[8:58](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=538s)** at their training cut of date but beyond because now they have access to the entirety of the internet. And all this boils down to the new steps data model that we have where instead of a world where we have a single message sent to a model and a response, we're going to have very complex things like async tool calls models working together, right? And we want to make sure we have a strong kind of data structure to support this. And so we've introduced the steps data model which replaces the original legacy outputs array with a tight discriminator that makes it very clear at each step what the model output what the dot signatures were what the functions called were and especially when it comes to the content is being generated. Earlier you saw content.type where it was audio and video and these makes it easy to build these multimodal pipelines in a way that only the Gemini model families can. The second thing that we've launched is

**[9:47](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=587s)** anti-gravity as a remote agent as what we like to call manage agent. So we've standardized around using the anti-gravity harness across all of our Google suite of products. In AI studio, which you saw just now, websites are built with the anti-gravity agent. In the anti-gravity application, you're also using the anti-gravity agent. Now, this is a very capable harness that we've co-rained Gemini on. And moving forward, I think you're going to see many gains if you use this harness out of the box. If you wanted to build a coding agent in the past, you would first have to tune the harness. Then you had to find a sandbox provider, manage the infrastructure, and then kind of figure out way how to preserve the context, especially in between runs. But with the anti-gravity manage agent, you get a persistent sandbox out of the box. With a single API call, you get a sandbox that you can keep hitting and treat as a personal claw without any

**[10:35](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=635s)** sort of modifications. You can see an example over here where we want to analyze what's in a GitHub repository. We then pass it over in an API call over to the anti-gravity agent and it then boots up a remote sandbox and then starts investigating what the repository is about. You can see it calls a list file to get what's in the workspace. It then reads each individual file and then it generates a final report. All of this is happening in a remote sandbox without any sort of intervention from our site. The agent's able to research, reason and handle all of this autonomously. We also handle multi-state persistent sandboxes like what we mentioned earlier where as long as you preserve the environment ID that we returned to you, you're able to route it right back to the original sandbox that you had. So these are two primitives that we given you. The interaction ID where you're

**[11:22](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=682s)** able to preserve and work with context and ensure you're not busting your cache and the environment ID that enables you to route it to the exact same context. And so this way you can use the same sandbox. You don't need to manage any sort of persistence of state and all you need to do is just add a few lines of code. The other way we've tried to make it easy is for you to be able to load in sources. A lot of times you might have custom dependencies. You might have EMD files, helper files that you want to throw on the on this specific sandbox. So we support Google GCS buckets. We support GitHub repositories and inline files. And so what you see over here is a demo whereby it continues off the previous call that we did. We're passing in the environment ID and the model has the exact same files right where we left it. any sort of packages you install, any sort of files you throw and create, the

**[12:10](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=730s)** model has access to it through each and every turn as long as you passes back the interaction ID and the environment ID. This isn't just the sort of constraint to very simple task with the manage agent. What you're seeing over here is a run where the model burnt over two million tokens trying to analyze a repository that we got for a hackathon where someone built from scratch an entire programming language to code reinforcement learning environments. If you've ever used the Scratch programming language, it's a drag and drop language where you can kind of get simple characters to move. But over here with a single API call, we're able to analyze an entire repository that has a custom DSL, a web page, a whole bunch of like schemas, and an RL training loop running inside HUD. And so it really opens up this kind of opportunities for you to build these very custom and performant agents without you having to handle the underlying infrastructure or tune the

**[12:57](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=777s)** harness. The best part about using the anti-gravity agent is that fundamentally it's the same agent running in your anti-gravity IDE, which means that if you have certain workflows that are you've tuned locally, you have skills that you've made sure are great, you can once you're happy with those skills, you just package it into a single folder. We allow you to upload the same way using the sources into into agents folder and that gives your agent the exact same skills with the same agent harness and the same prompt running locally and in the cloud. When you're ready or when you're comfortable with what your agent is doing locally, you can then push it up and everything works as intended. The next question we often get from companies are, "Hey, I need my agent to be secure. What am I going to do if my agent leaks a network credential?" And to do so, we've implemented a man-in-the-middle proxy. So, what does

**[13:45](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=825s)** this mean? A lot of times, you need to make API calls to different providers, say the Gemini API. You might need to download private GitHub repositories, etc. We have a proxy that stands in the middle and so any call your model makes we will look at the header and we can replace items at will. What you see over here is a case where we'll transform every single outbound call to the GitHub API with an inject in the token dynamically. And so even if the model is somehow prompt injected and leaks your GitHub API token, it's never actually going to see the token. It's only going to execute code that will run against the GitHub API and your token is never exposed. Once you're comfortable with how the agent is performing, you've set it up well, we give you two different ways for you to basically configure and set it up as a named agent, much like you've been

**[14:32](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=872s)** using the anti-gravity preview agent. The first one is to freeze it with a certain set of configured files and network sources. That's what you're seeing on the left here. I have a data analyst agent that I'm creating from the anti-gravity preview base agent with some base environment configurations here, just a GCS skill. The other way that we allow you to do so is by chatting iteratively with an agent to set up an environment as you like. For example, you might want certain dependencies, you might want certain packages, and you can freeze an environment as a specific agent and all your subsequent calls kind of go through that. Once you're happy with that, it makes it very easy for you to scale up your workloads. At this point, we support up to a thousand named agents, which means that you can have all these different configurations and you don't pay for any of the storage. You don't pay for you don't pay for the sandbox. you only pay for the model. We've

**[15:21](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=921s)** optimized our infrastructure to be very performant to be able to handle a workload like this. And we're pretty excited to see what people are going to build. Recently, we've also out open sourced a new Gemini API CLI. This is a simple CLI that you can use to get started working with the Gemini models to test out the models locally using simple CLI commands. The other benefit of this is that you're going to be able to iterate on your code on your coding agent or your anti-gravity agent locally. And once you're ready, it packages it as a single folder and uploads it straight and creates an agent for you. Lastly, if you're thinking of switching over to the interactions API, which is where all of our new models will be on, we've also created a new interactions API skill that you can feed to your favorite coding agent and that will then basically allow you to do the migration

**[16:09](https://www.youtube.com/watch?v=8aVbXXvJUY4&t=969s)** without any issues. I'm sure you guys have faced issues where you've asked Gemini to implement a specific kind of uh implementation and it keeps using Gemini 2.5 flash or Gemini 2.0. And so we what we do is we make sure we keep up to date the list of all the different models. We keep up to date all the different methods. We provide a good bunch of skills and like Philip mentioned yesterday, we regularly evaluate these and make sure make sure that they're actually doing what we want them to do, which is allowing you to use Gemini and build on Gemini well. So that's the end of my talk. Uh, thank you so much for coming by and staying around for the round of the conference. And yeah, I hope you guys get started. I'll be on the side if you guys have any questions about the new API. [music]
