---
id: oWTEiYpxl80
title: "Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind"
slug: why-ai-agents-should-have-their-own-sandbox-philipp-schmid
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Philipp Schmid"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-10-07T17:00:07Z
video_id: oWTEiYpxl80
url: https://www.youtube.com/watch?v=oWTEiYpxl80
youtube_url: https://www.youtube.com/watch?v=oWTEiYpxl80
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Gemini API", "Google DeepMind", "Gemini", "Interactions API", "AI agents", "agent sandbox", "managed agents", "Antigravity", "Google AI Studio", "agent skills", "AGENTS.md", "Nano Banana", "tool use", "Philipp Schmid", "AI Engineer"]
topics: ["Agents & orchestration"]
transcript: true
---

# Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind

**Philipp Schmid**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Gemini API` `#Google DeepMind` `#Gemini` `#Interactions API` `#AI agents` `#agent sandbox` `#managed agents` `#Antigravity` `#Google AI Studio` `#agent skills` `#AGENTS.md` `#Nano Banana` `#tool use` `#Philipp Schmid` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=oWTEiYpxl80) · [Conference site](https://www.ai.engineer/)

## Description

Your agent shouldn't run on your laptop. Give it its own computer in the cloud, with one API call.

Philipp Schmid from Google DeepMind walks through the Gemini Interactions API, Google's new API for both models and agents. It handles server-side state, long-running background jobs, and built-in plus custom tools across text, audio and images, and it replaces user/model turns with a timeline of steps. Then he shows the Antigravity agent in the Gemini API, which runs the same harness as Antigravity in its own managed cloud sandbox. Agents can run code, install tools, share environments with other agents and pick up skills and AGENTS.md files automatically. He covers the Agents API for packaging reusable agents, the new Gemini API CLI, and demos an AI talk radio show generated from one prompt.

In this talk:
• The Interactions API: one interface for models and agents
• Why steps replace user/model turns for agentic apps
• Managed sandboxes: persistent, shareable environments with skills built in
• Demo: an AI talk radio agent built from an AGENTS.md file and skills

SPEAKER
Philipp Schmid, Google DeepMind
X: https://x.com/_philschmid

LINKS
Gemini Interactions API: https://ai.google.dev/gemini-api/docs/interactions-overview
Gemini API agents: https://ai.google.dev/gemini-api/docs/agents
Antigravity agent docs: https://ai.google.dev/gemini-api/docs/antigravity-agent
Gemini API CLI (GitHub): https://github.com/google-gemini/gemini-api-cli
Google AI Studio: https://aistudio.google.com

CHAPTERS
0:00 Intro
0:52 New: Nano Banana Lite and Omni Flash
1:17 From text completion to agents
2:47 Get an API key in AI Studio
3:21 The Interactions API
4:21 Server-side state and background jobs
4:56 Code: state, audio and images
5:56 Tool use: a CVE agent
6:45 From turns to steps
8:10 The Antigravity agent
9:14 Every agent gets its own sandbox
10:04 Sharing environments between agents
10:29 Sources, skills and AGENTS.md
11:14 The Agents API
12:23 The Gemini API CLI
12:58 Demo: AI Talk Radio
14:43 Demo: listening to the show
16:46 Inside the agent: just files
18:05 Demo: exploring the sandbox
19:00 Downloading the environment
19:29 How the managed agent loop works

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,608 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=oWTEiYpxl80&t=12s)** So, hi everyone. Uh, welcome to why agents should have their own sandbox. Uh, I'm Philip. I'm part of the Google DeepMind team, mostly working on AI studio and Gemini API. Uh, we have a small crew, so I try to keep the boring stuff short and like the exciting demo stuff long. And we can also ask some questions I guess at the end. Maybe you need to sit a little bit further at the front so I can understand you. Um so I want to start with a little bit of a background. I'm not sure if you have seen that slide but that's a very popular slide when you do like Google presentations um to show a little bit um what we have achieved in the last two year with like the Gemini models but also our open models with Gemma and the slide is already outdated since yesterday. So yesterday we shipped Nano Banana Light uh which is our new image generation model. Super fast

**[1:02](https://www.youtube.com/watch?v=oWTEiYpxl80&t=62s)** uh sorry super fast uh super cheap. Um it's like 4 cent per image and then also we shipped Omni flash on the interactions API. So you can now programmatically use Omni to create videos to edit videos to yeah build gen media applications. And to give a little bit of a brief history, I assume everyone has heard about agent has heard about large language models. But to really quickly reflect where we are coming from. So I think around 2018 19 with the first bird models and GBT models, we were super excited because we could continue sentences, right? We were able to generate poems without uh with providing like a first few words and then the model coherently continue the text which was nice but not very useful or helpful for any one of us to build

**[1:50](https://www.youtube.com/watch?v=oWTEiYpxl80&t=110s)** something. Then we we moved into the the instruction uh way. Before we had pre-trained models which could continue text and then with instruction following we basically trained models to answer questions more or less. So we told ask a question and the model correctly responded. Um and then with with chat GPT um everything changed a little bit. I think most of the people probably got started with that and we went into this user model turnbased conversation where we had a user input, a model input, a user input, a model output. Then afterwards we combine that with function calling because we wanted the model to take actions for us. And now we are in like this black box with goals, thinking and functions where we no longer just prompt the model. We basically give a goal to the model, tell them how to verify its goal or how to like deploy it

**[2:38](https://www.youtube.com/watch?v=oWTEiYpxl80&t=158s)** and like hopefully have it running for multiple hours or even days and come back with the results we want to achieve. Um, so if you haven't used Gemini API or AI studio before, you can go to AI.studio or toi.dev. So very quick, very short URLs. H, get your own API key. So if you have your computer with you and you if you want to follow along a little bit later on like trying out a few things we have shipped recently you can do that. Um no setup required can use your Gmail account. Um can start start experimenting. If you want to use bigger models more usage enter your credit card and we improved that a lot. So you don't need to leave AI studio anymore to go into Google Cloud. You can do everything inside of AI Studio. You can set up your own budgets that nothing gets out of control. And I want to start about or talk about the interactions API which is

**[3:27](https://www.youtube.com/watch?v=oWTEiYpxl80&t=207s)** our new uh API for Gemini models and Gemini agents. And on the right side sorry left side we have some code snippets. So if you never have heard about the interactions API you can think a little bit about that's our answers to like the responses API from OpenI. It is much more developer focused, much more simpler, much more web developer friendly. And you can already tell in like the two snippets here uh to call a model like Gemini or to call an agent here like the anti-gravity agent, it's like literally the same interface. And this works for all of the modalities Gemini offers. So you have a model or an agent, you have an input. The input can be a basic string or it can be multimodal data. And then you have tools or environment which uh I'm very excited and why which we are going to talk about

**[4:17](https://www.youtube.com/watch?v=oWTEiYpxl80&t=257s)** later why every model or agent should have its own box. Uh new with the interactions API is you have serverside state management. So if you don't want to manage the state on the client you can hand it over to the server. We have long running operations. So async requests basically you start something. If we talk about omni video generation takes quite a long time and you might not want to keep your HTTP connection open. So you send a request get back an ID can set up streaming or polling to wait uh until the the generation is completed and then um it comes with a lot of simplifications for building agents and tool use. So you can combine built-in tools like Google search uh with custom function calling and to look at some code examples. So for serverside state it looks very similar if you have used the responses API we call it

**[5:05](https://www.youtube.com/watch?v=oWTEiYpxl80&t=305s)** interactions because we just not get a response anymore. We interact with models and agents. You send an input and if you want to do a follow-up turn you provide a new input and basically just the ID from the previous turn and then on the server we um concatenate all of like the different inputs and make sure that the model really reh sees what has been done so far. And this goes for all modalities. So for audio generation you have a model. We have our Gemini TTS model. We have our input and since we want audio back not text you define a response modality with audio and some generation configuration which was you for example want to use the same pattern works for image generation. So our image generation model uh nano banana here our input some generation uh generation

**[5:55](https://www.youtube.com/watch?v=oWTEiYpxl80&t=355s)** config and then you get back your image and for tool use uh also much better I would say than previously. You just define your tools with like Google search URL context or your own custom function and then you send your request and the model decides on it on its own. do I first need to like run Google search or call the function and all of the code you see here is basically enough to create a very simple small CVE agent to detect if there are like any CVE um for react in this case and then like it uses Google search it uses URL context to visit those websites and then function calling to basically give structure to it so you can like save it in your database or look it up for example um and something new and maybe different to other model

**[6:44](https://www.youtube.com/watch?v=oWTEiYpxl80&t=404s)** providers is that we moved away from this user model term principle. So if you build an application with another LLM provider or with open models, you have always this uh user model user model turn concept. So you as a user provide an input and expect the model to return an output. This worked until like one or two years ago I would say where we just got back responses from those models. But with agents and with reasoning, all of that changed, right? Models now think for a very long time where they might expose some thoughts directly or might just expose a signature. Function calling is not very uh a user role, right? With normal or like with previous APIs, you would need to use the user turn to return some function output, which for me always

**[7:33](https://www.youtube.com/watch?v=oWTEiYpxl80&t=453s)** felt a little bit weird because the output or the new input is coming from the environment and not from the user. So that's why we moved away from like those turns into steps or like to um like synchronous timeline of steps where every action or generation is its own type which makes it very easy to extend to new features and capabilities which might come in the future but also makes it still like very simple to use because you really define what it is done. So if you build a function calling agent, you return a function result and not like a a user role user with some content which might be a function result or not. And at Google IO we ship the anti-gravity agent uh which comes with its own sandbox. So the anti-gravity remote agent inside the Gemini API is powered

**[8:22](https://www.youtube.com/watch?v=oWTEiYpxl80&t=502s)** by the same agent harness which is used with the anti-gravity product. So if you have used the IDE or the new anti-gravity 2.0 O or the CLI, you might have used that harness already. Very important here. When we talk about harness, we don't mean the same agent. The harness is basically the the back end of our agent, but it might be different between different products. So the anti-gravity IDE is a coding agent. So it might have a little bit of different tools or a little bit of of a different system instruction than the anti-gravity agent we have in the Gemini API, but it's still the same harness. Meaning if we improve Gemini to become better with that harness, we benefit inside anti-gravity, but we also benefit inside of the Gemini API. And with that new agent, we also introduce this uh environment field. And an environment

**[9:11](https://www.youtube.com/watch?v=oWTEiYpxl80&t=551s)** here remote is basically for that API call, your agent gets a sandbox managed by us. Meaning if you send a request, our back end starts a cloud sandbox where the agent can run code, can create files, write files, um, install dependencies, install your own tools or maybe call your own APIs and it's all managed and stateless on our side, meaning that you just send the API request. You don't need to manage the infrastructure and those environments stay persistent. So if you have multi-turn conversation where the agent um you set user input I don't know like um research the latest tech news and create a file and then you want to do like a follow-up interaction you can

**[9:59](https://www.youtube.com/watch?v=oWTEiYpxl80&t=599s)** like use the same environment from your previous turn with that new interaction but also this means that you can share environments between different agents. So if you have like three agents working inside the same environment, they can share context through the file system or you can like even use sub agents to basically pick up a work uh another agent has been done and then of course environments are very good but the model needs the right context and the right information or the right tools to work inside those environments. So you can provide sources uh sources can be um GCS buckets, GitHub repositories or inline files. It's very useful if you want to integrate skills. So the anti-gravity agent is skills or file system native I would say. So if you store skills inside the skills directory, it will

**[10:47](https://www.youtube.com/watch?v=oWTEiYpxl80&t=647s)** automatically picked up and uh be pro uh included into the system instruction. But also if you have an agents MD file from your coding agent or from your existing agents, it will also be automatically appended to the system instruction. and then um you can create an agent because like sending a request is nice and having all of the configuration stateless is also very good but what if you want to share it or what if team one builds an agent team two wants to use um therefore we created the agents API where you can define the base agent so what's the underlying brain so to speak you can define instruction and then also the uh environment um and the environment can be a raw environment like with sources or you and uh use an existing environment. So you can think about I have some kind of a scaffolding to do

**[11:35](https://www.youtube.com/watch?v=oWTEiYpxl80&t=695s)** where I need to install like the GitHub CLI uh add some skills and maybe do some like sanity checks. I can use the agent to create its own environment. And after the agent is done, I get back an environment ID. I can use that environment ID to create the new agent. And every time I call this new agent, it will start from that already pre-loaded, preconfigured environment. And so it's like very easy for you to use agents to build their own environments and then like to create agents out of them which you can share with your users or with your customers without writing any Terraform without thinking about Kubernates microservices firecracker or anything else. And to make it easier for you and for your coding agents, we

**[12:24](https://www.youtube.com/watch?v=oWTEiYpxl80&t=744s)** created a CLI for the Gemini API. So it's it's not a coding agent. It's not Gemini CLI. It's really an a CLI that your agent can use to call the Gemini API. Meaning it can call Nano Banana or Omni if you want to generate some assets. But you can also use it to create those agents, iterate on those agents, and improve those agents. The QR code should bring you to like the GitHub repository and then also we have dedicated skills for working with the interactions API and the agents API um if you want to to play around with it later. And now let's let's do some some demos. So I'm in AI Studio inside the AI talk radio. If you have seen or attended the

**[13:14](https://www.youtube.com/watch?v=oWTEiYpxl80&t=794s)** Google IO developer keynote, you might have seen uh this already. Um that's just a simple UI on top of managed agents. We manage agent. We are going to look at the agent in a little bit, but it's basically a talk show radio and that talk show u agent has access to all of the different Gemini models. So it can generate a thumbnail, it can generate um speech, it can generate music, it can do research and it's basically a one short radio generator and we give it a try. And I want a talk show radio on whether pineapples belong on a pizza or not. And it's free to use. So if you go to the applet later uh you can like have

**[14:01](https://www.youtube.com/watch?v=oWTEiYpxl80&t=841s)** free daily usage to create create your own um AI talk show radio and what happens is like first step we start our environment and then the model starts thinking on what it needs to do and then the first step is like it installs our Python dependencies and it reads our skills and then it continues to work. Since this will take a little bit, I already ran a talk show radio on whether we should put in cereal first or milk first. And the very interesting part about a talk show radio, it's not like a podcast you listen to. It's really you have multiple um people like reasoning and like sharing their opinions on it and we give it a quick listen. Is there a correct physical order to preparing your breakfast bowl or are we flirting

**[14:49](https://www.youtube.com/watch?v=oWTEiYpxl80&t=889s)** with culinary chaos? [music] Welcome to AI Talk Radio. I'm Paul broadcasting from our London studio. Today we are exploring the great breakfast debate. Cereal first versus milk first. We will objectively break down the pros and cons of both methods. Let's go to our lines. We have David calling from Boston. David, you're on the air. >> Yeah, thanks Paul. Look, it's got to be cereal first. It's basic logic, right? Cereal is the independent variable. You pour it, you see the volume, then you add milk to compliment it. Plus, like if you pour dry cereal into a bowl of milk, it splashes everywhere. It's a total mess. And the mashed potato analogy, you wouldn't put gravy in a bowl and drop a

**[15:38](https://www.youtube.com/watch?v=oWTEiYpxl80&t=938s)** lump of potatoes on top, right? A striking analogy, David. Cleanliness and portion control are certainly strong arguments. Let's hear the counterpoint. We have Sarah on the line from Sydney. Sarah welcome. >> Hi, Paul. Okay, look, David has it all wrong. Milk first is it's a total game changer for texture. >> Okay, cool. So, if you want to play around with it yourself, you can go to AI.studio. And on AI. studio you have that build section on the left side and there's a gallery and gallery is basically pre-built applets use cases for Gemini and if you scroll down to it uh you have new build experience with and there's the talk show radio if you click on it you will find the applet you can uh remix it meaning you can like adjust it

**[16:28](https://www.youtube.com/watch?v=oWTEiYpxl80&t=988s)** so if you don't like talk show radios and you would rather have I don't know some real podcast uh application you can like very easily together with Gemini adjust it to their own needs. And since applets are all open uh in terms of code, we can also take a quick look on like how our agent really is. And our agent is just files. So we have an agents MD file inside our environment. That file will be loaded on environment startup which is then included into the system instruction. Very basic agent file. It has all of like the instructions for our agent to do. So it should do some research, write some scripts for the different people, generate music, generate a speech, mix everything together. And to do all of those works, we have skills for it. So

**[17:15](https://www.youtube.com/watch?v=oWTEiYpxl80&t=1035s)** if we look into like the TDS generation, we have a skill on how to run it. We have a Python file. That Python file itself allows the Gemini agent to call other Gemini models. So it uses the interactions API to generate some speech which we can then use. And that that's all it takes for our agent. And if you want to take that agent from the UI to like a back end, it's really you just need to copy that file and create the agent and then use it. And if you want to play around with the uh agent itself uh inside the playground, we have uh inside the model pickers a new agent section. So if you want to test deep research, go test deep research. But there's also the anti-gravity agent. And on the anti-gravity agent, we have six different uh agent templates uh which

**[18:03](https://www.youtube.com/watch?v=oWTEiYpxl80&t=1083s)** you can like very easily test, select and and see how it works. We go into like the the standard one. And what I really like to do is like explore the environment like let's see what the agent finds out about where it is running. We send our prompt and now it starts the environment should take for the first request like 7 to 10 seconds and then we see the agent like doing its work. So we have some reasoning, we have some bash commands. So it runs so it checks what uh version west version I'm running on what CPU memory I have and then we get back a response from our agent that is runs on Ubuntu um has 8 vCPU 16 GB of memory python installed pip installed and then you can like really continue let's see um do you have do we have node installed

**[18:53](https://www.youtube.com/watch?v=oWTEiYpxl80&t=1133s)** um so you can like very easily follow up um and it just continues based on like my prompt and then also you have the option on the right side to download the environment. So if your agent has created some files you want to extract out of the environment, share it, can very easily download it or there's an API for it as well. And then um uh what else? Uh to quickly show you again how it works, I can make that a little bit bigger. So when you when we send a request um we like start the sandbox and it loads all of our files and then we have like this agent loop completely on our server. So when you build agents normally a lot of times you need to manage the function calling on your client right you need to passse

**[19:40](https://www.youtube.com/watch?v=oWTEiYpxl80&t=1180s)** the function call run it some somewhere and then send back the function result and with the managed agents it's really just a single API call and everything runs inside that remote sandbox you can also connect remote MCP servers or run uh local MCP servers inside of that environment and um yeah really get started so if you are interested about it uh we have great documentation inside the Gemini API under agents with a quick start which walks you through how to send your first request, build your first agent and get started and then of course uh install the coding skills to have claude codeex or whatever model you use to to help you get started. Uh thank you for for coming. If you have some questions I'm like here
