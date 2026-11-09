---
id: WWIFiQi9U4w
title: "The One Thing Every AI Agent Framework Agrees On - Mislav Ivanda, Daytona"
slug: the-one-thing-every-ai-agent-framework-agrees-on-mislav
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Mislav Ivanda"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-11-09T08:00:27Z
video_id: WWIFiQi9U4w
url: https://www.youtube.com/watch?v=WWIFiQi9U4w
youtube_url: https://www.youtube.com/watch?v=WWIFiQi9U4w
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Mislav Ivanda", "Daytona", "AI agents", "sandboxes", "agent frameworks", "LangGraph", "CrewAI", "OpenAI Agents SDK", "code execution", "AI security", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration"]
transcript: true
---

# The One Thing Every AI Agent Framework Agrees On - Mislav Ivanda, Daytona

**Mislav Ivanda**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Mislav Ivanda` `#Daytona` `#AI agents` `#sandboxes` `#agent frameworks` `#LangGraph` `#CrewAI` `#OpenAI Agents SDK` `#code execution` `#AI security` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=WWIFiQi9U4w) · [Conference site](https://www.ai.engineer/)

## Description

Mislav Ivanda of Daytona has integrated sandboxes into most of the major agent frameworks, and noticed that frameworks that disagree on almost everything all ended up in the same place. He compares three ways to run agent-generated code: allow lists and approval prompts, embedded runtimes, and a separate sandboxed computer. He explains why only the last one keeps a compromised step from compromising your app, and shows frameworks like CrewAI, AG2 and the OpenAI Agents SDK moving to sandboxes. His advice: models, prompts and even frameworks are easy to swap, so choose where your agent's code runs before you choose a framework.

Chapters:
0:00 Intro
0:52 Guess the framework
2:20 Frameworks that agree on nothing
3:42 Where should agent code run?
4:12 Option 1: allow lists and approvals
5:23 Option 2: embedded runtimes
6:46 Option 3: a separate computer
7:54 Frameworks are moving to sandboxes
9:19 How sandbox use has changed
10:33 Which framework should I pick?
12:46 The one choice you can't easily swap
14:09 Frameworks are opinions, boundaries are commitments

Mislav Ivanda

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,103 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=1s)** [music] [music] >> Thank you all for being here. My name is Mislav. I'm a developer experience engineer at Daytona. And for the last year, my main my main task and goal there was to integrate Daytona basically everywhere where where Sandbox makes sense because we at Daytona are Sandbox provider. And these are spanning from agent frameworks, coding agent harnesses, workflow tools, development developer products and stuff like that. And during this process, I noticed the pattern that was repeating all the time and it may be it made me stop a bit, think about some things that eventually led to

**[0:49](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=49s)** this talk. So yeah, I would need your help on this slide. Does anyone have a guess which AI agent framework is this? If somebody has a guess, LangChain, LangGraph, Google ADK. Okay. Okay, let let's say LangChain, but the the main thing about this is that whatever you you told can basically be correct and defensible. Why do I say that? It's because during the integration of Daytona into these AI agent frameworks, there I noticed that they I can barely differentiate the Daytona related

**[1:38](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=98s)** code contribution part between these. So in some of these you integrate as a tool, in others you integrate as external plugin that you can install to you know, make your agent use Sandbox capabilities. In other ones, you extend the Sandbox client class and do some internal framework API stuff. But the hood all all of these ways speak the three same lines. So it's sandbox creation, running some code or task inside the sandbox, and sandbox deletion. And this this is pretty weird because most of these frameworks are competitors and they barely agree on some fundamental things or concepts. What do I mean by that? So for example, they don't even agree on what what an agent

**[2:25](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=145s)** is. For example, LangGraph defines an agent as a traversable traversable graph. CrewAI framework defines agents as, you know, bunch of role-playing agents that do do stuff on their own. OpenAI agent SDK is defining agent as a loop around LLM model. And for example, Cloud Agent SDK ships the whole wholly finished product that you just like use and have all full capabilities, no customization. Also they differ in between the languages they are implemented in, mostly between Python and and TypeScript. And they also don't agree on who who's in charge of specifying what an agent does, agent behavior. For example, in Mastra or

**[3:15](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=195s)** or LangGraph you explicitly define your agent workflows and trajectories, while for example in CrewAI agents do things on their own and they decide on their own to achieve the end goal. And yeah, when companies like or companies like this that don't agree on basically anything agree on something that probably isn't just a fashion, it's a necessity. So why why they agree do they agree on this thing? So as I like to say, whenever you're doing something with your AI agents that's useful, you eventually come up to the state where your agent agent needs to execute some kind of a code or needs to have shell access. And the next question is where where will this happen in which execution environment?

**[4:01](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=241s)** So I would say are basically three types of possible isolation in these environments, and let's now have a brief overview around these. So, number one is the most basic one, and it's probably the one you're using locally when development with your agent. So, you define certain allow list of commands. Uh you also get some approval prompts where you know Claude asks you, hey, are you sure you want to run this command? Although probably most of us just click yes and don't don't even read what does he say. And you can also add some interception hooks. But the problem at this approach is I would say the obvious. Uh so, when you allow your Claude agent to run Python command with Python uh dash C, he

**[4:50](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=290s)** can literally open any sockets, uh modify a file system, execute code, or do basically everything uh which you probably don't think about in in in the background. And you essentially defined what your model should use, but you didn't define what your model can actually use. And if the model is compromised, you can, I guess, sense that you essentially opened backdoors for it to to, let's say, do malicious commands on your local device. Second most more advanced option is shifting all of this coding execution stuff inside embedded engine runtimes like V8 or QuickJS. And this approach is better because you

**[5:38](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=338s)** have certain network and file system isolation. But the quirk with this approach is probably even more, you know, subtle because, let's say, your agent has access to certain tools like query database or send email. And your agent will probably generate a Python script which uses these tools, and you will execute this script inside this embedded runtime. But the problem is that these tools that your agent will call inside that runtime will actually run on your device outside that runtime. So basically your maliciously malicious agent can act through these tools, not directly but through these tools, which most of people like probably don't think about.

**[6:25](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=385s)** And as it says it you isolate the glue code that your agent generates but you're not actually isolating the actual tool tool calls. So for example, agent can use these email sending tool or database query tools to perform some of its malicious commands. For example, also if you had delete database tool you you can sense how can you get into problems with this approach. And the third one and recommended approach is to use a separate computer or VM for these kind of purposes. And yeah, you interact with this VM via API, control its life cycle or do any kind of stuff inside it. And this VM never touches or interferes with your local infrastructure, network, file system, etc. And the best part of this approach and why is it the best approach is

**[7:15](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=435s)** contained in this last sentence compromise the app is not compromise the app is not a compromise app. What do I mean by that is because in prior two approaches when your tool calls misbehave or you your agent misbehaves through let's say Python command you approved that compromise step is is literally compromising your whole application and can you know make really bad stuff. But in this step you can run the most the worst code on the planet inside a sandbox and it can't interfere with your application logic. You can just throw out that sandbox and spin up another one. And to back up this that I'm not just talking you know some nonsense here's the proof like the direction of frameworks

**[8:03](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=483s)** the direction that AI frameworks are moving at. So in April 2026, Crew AI removed the code interpreter tool, which essentially did uh local code execution on your device. And they now point to dedicated sandbox services. AG 2 also retired their old local coding executors and now have this new sandbox code tool class [snorts] that explicitly requires from you to define the environment where you want to use this. Cloud agent SDK is by default using sandbox, but it is special only sandbox. What do I mean by that? It's like a process level sandboxing which you can do for example with tools like

**[8:50](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=530s)** bubble wrap on Linux machines. Open AI agents SDK has this sandbox agent which has native you know support for some of the sandbox provider integrated inside and also for Docker, but it also allows you local code execution with you know transparently listed flaws of this approach and it's similar to with Mastra. And you can notice that they are not adding sandboxes. They already had them, but they are deleting all the alternatives. And parallelly with this shifts in AI agents frameworks direct isolation direction basically there also happen a shift between how these sandboxes are actually used. So firstly when first agent started to you know evolve and got into picture the sandboxes were mostly used

**[9:38](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=578s)** as short-lived machines where your agent was would spin it up on demand, run some code or task inside it and shut it down. But then when the models became more capable, the people realized they could literally shift hold the agent and run it inside the sandbox as the execution runtime and give it access to file system, network calls and basically everything. And since recently there's also a shift where people also like understood that if they can run thousands of these execution environments concurrently, they can do really interesting stuff, especially regarding reinforcement learning, fine tuning, post training, benchmarks, you can also spawn different sub agents

**[10:26](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=626s)** for while solving some problems and stuff like that. And yeah, now back to the to the question. So this whole shift from AI frameworks regarding execution environments and boundary made me also rethink the common question which me myself and I probably a lot of you are asked like which framework should I pick? And based on the this whole story, I think this is essentially the wrong question. Why do I say that? That's because some of most of the items that you compare frameworks between are swappable and you know, can be easily done. And stuff that's not that easily swappable is normally or often not even considering to the picture between before choosing you know, development

**[11:13](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=673s)** stack. So what do I mean by swappable? For example, you can essentially swap between if your multiple frameworks use same language, you can essentially swap between frameworks with you know, you give your coding agent a task and it's like a refactor and developers do it all the time. Second one is you can also swap between models and prompts. This can be a bit more trickier if you're you know, fine tuned to you fine tune your system prompts and stuff to certain model, but it requires some fine tuning and regression testing and it's I mean completely doable. Same with missing features. So sometimes people decide on which framework to choose based on some features that one framework has, another doesn't. But nowadays, yeah, you can essentially

**[12:01](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=721s)** vibe code missing feature or just plug it as an external plugin for certain framework. I would say this probably doesn't only count for the feature called durable execution which some frameworks provide. That's kind of not that easy to you know replicate and vibe code in an afternoon with cloud because it affects the architecture and stuff but all of the others like I mentioned here Evals tracing a memory you can easily you know implement by yourself or just plug in an external tool. And you can also swap the SAMOX provider because all of us speak the same language so all of us speak, create, run some stuff inside and delete. Although I mean some of us have distinct features and different performances. And the stuff you can't

**[12:49](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=769s)** change easily or swap later is the execution partial I would mention in here. So that's like deciding will you run your ex coding stuff locally or will you use external sandbox. Why you can swap this easily? Well the reason is that this defines your whole arc system architecture and how do you develop other parts of your system. For example when you're developing some kind of a tools if you're guessing that you will use first approach where everything runs locally then you write all of your tools to use your host or app process environments using your file system without separation and stuff like that. And problem is that most of the people start with this approach as a POC phase

**[13:38](https://www.youtube.com/watch?v=WWIFiQi9U4w&t=818s)** but unfortunately continue all up until the production stuff and they don't come back to it and then when well bad stuff happens it's probably too late and some of the times by bad stuff I mean something that can literally kill your product. And that's why I would like to say from this talk that you should probably consider picking up the execution choosing the best execution boundary before deciding which framework you should pick. And as I as I like to say it then send that side would maybe like for you all of here to remember out of this talk is frameworks are opinions and the boundaries >> all of here to remember out of this
