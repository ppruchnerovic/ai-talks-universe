---
id: Zf_e45GiNCE
title: "Zero Cold Starts: Serverless AI Agents on Akamai Functions — Thorsten Hans"
slug: zero-cold-starts-serverless-ai-agents-on-akamai-functions
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Thorsten Hans"]
channel: "AI Engineer"
duration_min: 23
published_at: 2026-10-10T18:00:38Z
video_id: Zf_e45GiNCE
url: https://www.youtube.com/watch?v=Zf_e45GiNCE
youtube_url: https://www.youtube.com/watch?v=Zf_e45GiNCE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "WebAssembly", "Wasm", "Spin", "Fermyon", "Akamai Functions", "MCP", "MCP server", "wasmcp", "edge computing", "serverless", "AI agents", "cold starts", "Vercel AI SDK", "Thorsten Hans", "AI Engineer"]
topics: ["Agents & orchestration", "Inference, serving & GPU infra"]
transcript: true
---

# Zero Cold Starts: Serverless AI Agents on Akamai Functions — Thorsten Hans

**Thorsten Hans**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#WebAssembly` `#Wasm` `#Spin` `#Fermyon` `#Akamai Functions` `#MCP` `#MCP server` `#wasmcp` `#edge computing` `#serverless` `#AI agents` `#cold starts` `#Vercel AI SDK` `#Thorsten Hans` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=Zf_e45GiNCE) · [Conference site](https://www.ai.engineer/)

## Description

Cold starts, proprietary SDKs and one-region deployments slow AI apps down. WebAssembly at the edge removes all three.

Thorsten Hans, senior developer advocate at Akamai, shows how to build and ship MCP servers and AI agents with Spin, the open-source WebAssembly framework, and run them on Akamai Functions, a globally distributed serverless platform with no cold starts. He explains why WebAssembly on the server is fast, portable and sandboxed by default, then live-codes MCP servers with wasmcp: scaffolding tools in TypeScript and Rust, composing them into a full server, testing with MCP Inspector, deploying it worldwide in about 60 seconds with one command, and calling its tools from the Zed editor. He finishes with an agent built on the Vercel AI SDK, backed by a model on a Linode GPU, and explains how memory snapshots keep apps warm.

In this talk:
• Why edge-native beats single-region for AI apps, and how WebAssembly kills cold starts
• What Spin and Akamai Functions are
• Building and composing MCP servers with wasmcp in TypeScript and Rust
• Deploying an MCP server and an AI agent globally with one command

SPEAKER
Thorsten Hans, Senior Developer Advocate, Akamai
X: https://twitter.com/ThorstenHans

LINKS
Spin: https://spinframework.dev
Spin (GitHub): https://github.com/spinframework/spin
Akamai Functions: https://www.akamai.com/products/akamai-functions
wasmcp (GitHub): https://github.com/wasmcp/wasmcp

CHAPTERS
0:00 Intro
0:57 Why edge-native?
1:32 The cold start problem
2:52 WebAssembly on the server
3:37 What is Spin?
4:52 Akamai Functions
5:32 Sandboxed by default
7:32 Demo: scaffolding with wasmcp
9:41 Composing an MCP server
10:16 Testing with MCP Inspector
12:56 Deploying to Akamai Functions
14:16 Using it from an MCP client
16:16 An agent with the Vercel AI SDK
18:21 Memory snapshots
20:56 Key takeaways

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,243 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=1s)** [music] Welcome everybody. Thanks for joining my talk. In the upcoming 20 minutes, I want to give you an introduction on how you can build ultraast agents and MCPs with spin and run them globally distributed. So my name is Tossen. I work as a senior developer advocate with Ecomi and um I guess all of you have already built either MCPS or agents and they are no different than any other kind of application. So they obviously demand super fast response times so that we can deliver the best possible user experience. However, traditional regionbound architectures or

**[0:50](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=50s)** infrastructures fall short when you want to address a global audience and they they come with some frictions which lead to the inception of edge native architectures. So obviously latency is one of the biggest concerns depending on where you deploy your MCPs or your agents. It might be fast for a subset of your global audience, but others might experience a way lower latency and resulting in a way worse user experience. Um, depending on your distributable unit, right? Even so, if you even either choose containers or VMs, you may experience a cold start delay that might range from several seconds up to

**[1:38](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=98s)** multiple minutes, especially when you have to scale dramatically fast to meet unexpected user demand. However, we can overcome that obviously uh by overprovisioning the infrastructure. However, keeping around many many containers or servers and actually not utilizing them results in obviously higher cloud spendings and is not sustainable from an environmental footprint. So there are higher level solutions uh that we can use to run MCPS or agents but they usually or often come with proprietary SDKs or uh deployable units or have their own way on how you should treat them in order to make them work in a production grade environment.

**[2:28](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=148s)** Once you figured out about those constraints, moving away or migrating your workloads, your agents to another hyperscala to another kind of infrastructure, it's often rather complex and extremely costly. So, but there's a solution to that and that solution involves a new way of how we as engineers could build backend or serverside applications and this is done by adopting web assembly on the server side. You can think of web assembly as um as containers relate to virtual machines. So, they are binaries super tiny in size, easy to distribute, super fast to run and portable. What I refer to as the edge native AI stack is a combination of a CNCF project

**[3:18](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=198s)** called spin and echcomi functions. One runtime where you can run those web assembly applications. So let's dive into spin for a minute. Uh spin as I said is a CNCF project that is vendor agnostic and it allows you to build web assembly applications that are meant to be executed on the server or in the cloud. Spin itself consists of three major pillars. So it is a CLI that we as developers use to address all our day-to-day concerns. So everything you know in the realm of the inner loop. It is a runtime. So it's based on WM time um that allows us to run these kinds of applications either locally or on microcontrollers or constrained environments.

**[4:05](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=245s)** Last but not least, Spin gives us language specific SDKs to boost the developer productivity when it comes to day-to-day jobs like for example interacting with HTTP services, integrate interacting with databases or different kind of things. Although we have language specific SDKs, spin itself is language agnostic and you can choose from all the languages that are able to be compiled down to web assembly including the web assembly system interface or shortwi and you can learn more about spin on spin framework.dev. So scan this QR code and you will end up on the spin documentation. So spin is the developer tool that we use for building these kinds of applications.

**[4:52](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=292s)** Echi functions is the first truly serverless computing platform that is globally distributed and has zero cold start at all. So every application that you deploy to Ecomi functions is cold started per request that hits your endpoint and on average we can cold start in less than half a millisecond. It's fully managed and it's again developer centric. Your developers deploy the workload. No knobs to turn, no terraform to write, just a simple oneliner and your app is globally distributed at no extra cost. Security is um is observed by web assembly's sandbox. So there's no way a workload could interact with external resources without us as developers

**[5:40](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=340s)** explicitly granting those permissions to our workloads. And to be a full-fledged serverless computing platform at the edge, we need some kind of persistence layer. So Echami functions comes with a built-in key value store that is again multi-tenant. You don't have to roll credentials. It is automatically associated to your app if your intent is to use it. Again, there is a QR code. Scan that and you can find out more about Echo My Functions. Sign up for a trial or a free a free account there and you know explore it. So these are the technical underpinnings that I want to use in order to build first MCP servers. So instead of handrolling a new MCP server, I mean we can implement the HTTP

**[6:30](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=390s)** protocol or the uh the specified API on top of HTTP to build an MCP. There is a smarter way of doing that and a smarter way is WMCP. WMCP again is a CLI that integrates seamlessly with spin. So what it what this allows us to do is basically to focus just on the business logic and in in the in the realm of an MCP business logic basically means we implement our tools we implement our resources or prompts and we are good to go everything else all those non-functional requirements that we have to tackle right like for example authenticating users using of 2 and OIDC that's done by WMCP and we then take readyto-use components off the shelf and

**[7:19](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=439s)** compose a final MCP server component together and run that on spin or on a myi functions and that's what we are going to do right now. So I have installed wmcp on my machine it's github.com wmcpwasmcp and it gives you a nice little CLI. So we can do womcp new. We can choose a language Rust TypeScript uh Python. And we can choose from templates. The default template is me only caring about tools for now. And let's call this new MCP server hello. We get instructions. Hey, move into hello. Uh, hello. Then let's open up a new terminal on this side. CD into hello over here as

**[8:07](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=487s)** well. And let's run npm install because that takes a few seconds. And let's open this one in the editor and let's do this full screen. So what do we get over here? Uh we get a boiler plate that's uh ready to use and those squirrel lines will go away once mp npm install is done. So all we have to do is we have to express the scheme on which inputs we expect. We have obviously to provide the list of our tools. So again we have to be good citizen over here and have to provide precise descriptions so that humans and LLMs know how to handle these kind of tools. So we list them in a simple array and then there's one ingestion function

**[8:55](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=535s)** that's called call tool and depending on uh the the payload that we receive we have to decide which tool we have to execute. If we jump into handle example tool over here, we can see uh all incoming arguments are validated and if everything's fine, then we basically uh concaten concatenate the received input with a prefix and return that back to the user. Nothing fancy. So let's close the editor over here and follow the instructions. Next on list is make. make goes on and takes the JavaScript code, compiles that down to web assembly. So we end up with a tools web assembly component which is not yet a full-fledged uh MCP server. Next in line would be where MCP compose. Let's

**[9:46](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=586s)** compose a full-fledged MCP by taking our tools and saying hey please give me an MCP for the sake of this demo. I don't care about authentication. Okay, it pulls all the necessary uh other components and composes together an MCP server and gives me instructions on how to run that. I can do a spin up -f server.wazm and we should see that running on localhost 3000. Okay, let's bring back the other terminal and let's run np npx the uh mcp inspector over here. That should fire up in the browser. There we go. Uh it's already pointing to localhost 3000 right here. So let's connect. Let's list tools. There's our example tool. We provide fu as an input

**[10:35](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=635s)** parameter. We run the tool and we should get back foo. Great. Nothing fancy cool works. But that's the local experience. So how can we take that to become a glo or how can we turn that into a globally distributed MCP server? Well, instead of globally distributing uh the hello world MCP server, I have a decision lock MCP server and let me open up this one first. So there is this one is implemented in Rust for the sake of implementing it in Rust. Um so let's go into lip RS over here. There is an equivalent class or structure in Rust. As you can see, we're looking at the call tool function where we branch out and either use one of the CRUD APIs or tools that is provided by my MCP server.

**[11:26](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=686s)** If we dive into the actual implementation um let me no this is wrong. I want this and then I want to do that uh decision. RS if we go to the bottom of the file you can see this is slightly different syntax but the same meaning right I have to define my tools and if we go to line 15 or so yes list decisions you can see over here that I use a store so on my local machine spin recognizes hey toen wants to use the key value store so it automatically creates a key value store using SQLite on my machine for development time purposes and on ecom myi functions it's leveraging the globally distributed um key value store

**[12:15](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=735s)** without me having to configure anything from here it's actually the same story right I have to use that make file and compose the server however I think it's smarter to update the application manifest and concatenate those tasks so that I can remain in the spin developer experience and basically do a spin build to compile compose and compile my MCP server. However, I can also combine this one with spin ecomi deploy. So this right now composes the server asks me hey how do you want to call that MCP server on a my functions? I call it ADR MCP. I allow um my terminal to

**[13:06](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=786s)** interact with the service registry. Now it's taken my Wom file and my application uh manifest generating OCI layers from those files uploading them to Echcomi functions on the server side or on the service side. We receive those two files and we distribute them across the globe through all the service regions. Every region has to confirm a that it received the workload that is capable of running the workload. Then we instantiate the workload once and do a internal health check. And once that came back for all the service regions with an HTTP 200 then we roll a generic subdomain on your behalf so that you that your MCP server

**[13:56](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=836s)** will be on the public internet. Obviously you can shield that with other products and services uh like the property manager to shield it behind whatever you want to enforce before uh forwarding users to the MCP server. So we get that URL. So we are globally distributed in roughly 60 seconds. Let's move over to an uh to a client. I use Z over here but that works with any client that basically supports MCP. I add a server. I go to remote over here and let me replace this one with the URL that we received. Add the server. And we can see I have five tools already. I can go here and say view tools. And these are the CRUD tools that my MCP defined. So I can

**[14:47](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=887s)** go back and chat with my IDE in the context of my project so that it could leverage uh my MCP server. track a decision to use or of 2.0 Hello for awful. Okay, so it should now identify my intent and ask permission to run the insert decision tool. We can see the raw input. Looks good. We allow it. It now calls out to echo my functions has already has already tracked my decision and I can say give me all the decisions please. Now the intent is to use the list decisions tool and again we are uh yes it might want to read uh details to give

**[15:36](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=936s)** me everything that it tracked or and uh with that we have a globally distributed um MCP server that's routing all the requests to the closest service region no matter where your users are and again you can write those tools or prompts or resources using TypeScript, Python or Rust templates. Cool. Uh let's move on with agents. Um so, oops, nope, this one. So, for AI agents, the story is no different. However, instead of using another CLI, uh we can simply pick any kind of SDK that's out there and that's popular. Um I I think the Verscel AI SDK is pretty nice to use. So this allows us basically to create a new spin app using

**[16:27](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=987s)** TypeScript. Just bring in the Versal AI dependencies and to build custom agents. Again, let's move back to the terminal to see how that looks like. Uh so let's move one up and let's CD into a simple game agent over here. And what's going on over here? Obviously, I have created a new spin app using a template so that I can get started pretty quickly. I'm leveraging a large language model deployed to a Lenode instance with a dedicated GPU. And all my spin app does it defines the tools. So, this is a simple game agent for the sake of demonstration purposes that can flip co flip coins that can roll a dice where you can specify how many sides that dice should have. And over here in

**[17:17](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=1037s)** the actual HTTP handler, we load the config and we define our agent, you know, pointing it to the old lama instance running on the node. We give our agent an identity and an instruction on what its intent actually is. We register our tools and we give it some constraints of of how many steps it might take. We generate a response and return it back to the collie. Okay, let's uh go let's do a quit all over here and let's do another spin aka deploy no confirm build and it asks for the name that's the game agent. So while it is uploading let me explain what happens when we compile a lang an interpreted language.

**[18:07](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=1087s)** So during compilation time we load the interpreter, we load your custom JavaScript and then we evaluate the global scope. This has one advantage that not just the runtime is hot also all the dependencies are loaded and then we take a memory snapshot write that to WM store that on disk meaning that every web assembly application written in JavaScript is faster than a native JavaScript application when it comes to cold starts and runtime performance. The only trade-off though is that we have to ship the JavaScript runtime along with our um with our user code. But we use an optimized JavaScript runtime called stalling monkey which is roughly 10 megabytes in size. So we get back an URL.

**[18:55](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=1135s)** Let me replace this URL over here. And let's say toss a coin. And we see um we see a response back. And if we look at these headers, we can see uh the point of presence where we enter the Ecomi network is Santa Clara and the closest service region for our AI agent is LAX. Another interesting header is X envoy upstream service time. And this tells me and you right now as well that it took 33 34 milliseconds to receive the request to run through the business logic to reach out to the large language model to generate a response and to go all the way back to the user. Oh, there's an internal server error. Great.

**[19:42](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=1182s)** Awesome. Let's try this again. Oh, yeah. That was an user error. Sorry. So, the error was staying 30 cmters in front of the screen. Um looking at it now we are 866 milliseconds. Um that is more realistic because we have to go through the LLM to basically see that uh our to our toss resulted in tails. Let's do that again. Tails tails tails tails. Oh, there's a hat. Nice. So roughly 820 milliseconds is what we could achieve with a full loop through the LLM by taking our agent and deploying it to a functions. Okay, so the developer workflow is always the same. No matter if you build any kind of line of business application, if you build an MCP or if

**[20:30](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=1230s)** you build an agent, you implement your application using any language that you could compile down to web assembly. Rust, TypeScript, Python, Go are the most prominent ones these days. You can test it locally with the spin CLI. You deploy it using a single command called spin a deploy. And finally, your you point your clients to your MCP or to your agent. So final or key takeaways from my from my point are portability. You can take those spin apps and run them on any Wii compliant runtime. Echi functions is one runtime and it's the globally distributed runtime. Everything is based on open standards. So spinners, CNCF, Wesi, Web Assembly are governed by the

**[21:17](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=1277s)** bite code alliance. But ultimately you gain speed, right? You have fast response times. Even the time to market for your developers to build MCPs and to build agent goes down because you don't have to roll the infrastructure. You don't have to implement non-functional requirements. That's all taken care of. And in terms of infrastructure, there's no ops. It's spin aka deploy is all you need. There are other commands in the box so that you can g gather metrics that you can retrieve logs that you can upgrade and so on and so forth. But developer experience is our our highest metric when we started spin and while we continue in that direction. Um we have a new website that's called the Ecomi developer hub where we share

**[22:05](https://www.youtube.com/watch?v=Zf_e45GiNCE&t=1325s)** stories and experiments and and experiences like these. So go check out developers.accomi.com. ecomi.com and if you have any further question find me at the Akcomi booth and with that thank you very much. >> [music]
