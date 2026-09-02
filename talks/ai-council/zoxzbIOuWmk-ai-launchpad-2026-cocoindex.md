---
id: zoxzbIOuWmk
title: "AI Launchpad 2026: CocoIndex"
slug: ai-launchpad-2026-cocoindex
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 11
published_at: 2026-06-23T22:57:04Z
video_id: zoxzbIOuWmk
url: https://www.youtube.com/watch?v=zoxzbIOuWmk
youtube_url: https://www.youtube.com/watch?v=zoxzbIOuWmk
tags: ["AI"]
transcript: true
---

# AI Launchpad 2026: CocoIndex

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `11 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=zoxzbIOuWmk) · [Conference site](https://www.aicouncil.com/)

## Description

CocoIndex fills the gap of context layer for AI where it continuously takes source and transforms it incrementally on source change or logic change to serve live AI agents, at scale

SPEAKERS:
Linghua Jin - Co-founder & CEO, CocoIndex
George He - Co-founder & CTO, CocoIndex

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*1,493 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=0s)** Hello everybody. We are Coco Index and we build fresh data view for agents and let's give the coconut some love today. Agents runs 50 times faster than humans, but the tools they rely on were built for human speed. Batch rebuilt overnight was built for humans who check a dashboard every morning, not for agents running 50 times faster. Agents is in the data loop. Agents reasons over code base, conversation graph, documents. They need data to be fresh, organized through the run. Agents write code. The artifacts they produce become the source data for the next reasoning step. Agents make

**[0:48](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=48s)** decisions and record them, traces, plans, audit logs. Agents update data while they run. A long horizon agents added its own context as it proceeds and source data arrives faster. Code bases, logs, Slack, PR tickets all updating in the background. Agents need continuous fresh data views. View has always been a part of the decision process. If we step back, at the beginning of the web, people use server-side render on every interaction waiting the page to reload. With more interactions, people wanted instant update on the view so they can do subsequent interactions and make decisions quicker. jQuery DOM operations were needed for incremental updates. It gets harder when

**[1:38](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=98s)** there are more interactions and the state is complicated. React enabled a state-driven model where we define states and the framework handles the incremental re-render. Today, agents interact with data and the view is not the UI anymore, but the data view is from the source. So agents want to interact with the data and get the view faster, too. And it's tend to be hard at the scale. So, George, what do you think? >> Yeah. Uh we are thinking about uh processing state-driven model. Uh the target is a function of the source. And the function is a transformation. And the you are the agent declare the state of the target instead of renders to the web, it renders to the this face targets or even the some agent actions.

**[2:29](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=149s)** And the end agent the engine uh keeps everything in sync with minimum reprocessing across time horizon at scale. >> So, Cocoa Index continuously builds fresh views from the source data, especially unstructured data that are dynamically changing. Your code base, meeting notes, Slack, and targets are different views of the raw data, relational database, data warehouse, vector database, graph database, message queues. Many great products here today are ecosystem partners. The pipeline shapes from Cocoa Index are not built for analytics. They're built to create different data views for agents. So, you can use it to build search index, build knowledge graphs, pipelines with high fan outs where join and nest

**[3:19](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=199s)** group by from traditional data frames are hard to a stretch. And pipelines with multiple stages where data views rely on relationship between entities of the systems. There are a lot of infra components to build on your own. And Cocoa Index ship all of this in one engine. We spent years building large-scale data infra and search. From building the largest incremental engine powering the web, we're now building the incremental engine for agents. So, let's go to the demo. And so, um for today's demo, we're going to show um how to use Coco Index to build context for coding agents. The client of Coco Index is a agent. Enterprise runs hundreds gigabytes mono repos or hundreds of

**[4:07](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=247s)** thousands repos. 1% of the corpus is changed daily. So, how do I build different kind of fresh views to help your own coding agents, code review agents, and security agents? We will demo using Coco Index to build code blocks semantic search with native AST parsers that came out of box. We will build call graphs for blast radius search. For example For example, if you're refactoring a function, and I need to quickly know which parts are impacted, files import other files, call functions from other files. And to build this, you can use Coco Index to build a multi-stage pipeline with symbol resolution, where processing cannot be independent between files. You can use to build mini maps, a hierarchical index of your code base, like Google Maps. And you can zoom in and zoom out at different level of

**[4:56](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=296s)** granularity of your code base. So, uh let's do some demo. So, everybody use Open Claw here. And I don't like it's a medium-size code base, 1 gig running on my Mac. And I just want George help me to disable some dangerous actions globally, so it doesn't accidentally delete all of my private data. >> Yeah, I think that we can start from a code search. And this code search is built uh on top of Coco Index. And uh we search by a keyword. For example, uh this allow uh to buy environment both. And then start to search.

**[5:46](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=346s)** >> So, we show couple of our Some comes from the mini map, which is a hierarchical summary, then we have generated the index base. Some of them are directly come from the code blocks and came from the AST parser trees. And I don't find the results I have. So uh George, maybe we can modify the code. >> Yeah, we can go to modify the code of um open claw and the for example we we find the find this uh file and we add a global variable um to pass the environment variable and uh expose to a function and we check this uh function in the using another using functions here. Basically we we make a change to the

**[6:34](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=394s)** open claw of a huge code base. >> So now I go back and let's redo the search again. So CCC stands for Google Index Code. And like we can see the uh new function was surfaced from the code search. >> Yeah, this is the function we just I did. This is a function we just I did and the um it surfaced in the search result immediately. >> So what else can we provide to the coding agents? >> Yeah, I think we can create a code graph on top of this one.

**[7:23](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=443s)** >> So code graphs helps you understand the blast radius and the influence of what you change the code to all of these code chains. >> Yeah, then we run this command CCC code graph and the it renders a code graph. So basically code that code creates a code graph continuously on top of source change but it render immediately. No. This is from the function we just created and the whole code chain. >> So, this looks great. So finally how can we use this, right? Like can you show us what does the effect we have for the coding agents?

**[8:10](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=490s)** >> Yeah, um this can be a tool used by the cloud code for example. Uh on the left side this is switch to another uh cloud out code base. The same exactly the same code but uh doesn't install with the Cocoa index code. You you'll see that uh it's not initialized in this directory so when we run uh cloud code here its result needs to We ask the question on on on the other side. This is Cocoa index code too. We ask the same question and uh run two both side by side. >> So, as you can see we're building a

**[9:03](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=543s)** three-dimensional understanding for the code base and helps cloud code navigate faster around the larger corpus. >> Yeah. The right side already got the answer cuz it did a bunch of uh search and uh the left side is uh kind of uh need need to go through each file and they try to guess the sometimes try to guess the remember variable name but no luck so they try different and they graph through the whole code base. So, they spend much more time here. >> If I don't navigate in there there you'll find a lot of fun and a lot of gripes. I think it's uh sometimes a hard job in a large code base without a

**[9:51](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=591s)** without some mini some minimized navigation. >> Yeah, so without Coco Index code understanding, we're just here watching Cloud Code go wild and uh keep guessing. Good luck. Almost done. >> Yeah, I think >> Yep, so like uh to wrap it up, as you see like uh providing a good context for coding agents actually helps speed up the coding agent and potentially can improve the quality as well cuz it knows your code base better, especially to navigate around larger corpus. So uh that's pretty much it. Uh thanks a lot. >> Yeah, thank you. >> can find us to get some stickers and uh cute coconuts. And then let's give

**[10:39](https://www.youtube.com/watch?v=zoxzbIOuWmk&t=639s)** the coconut another laugh. Thank you so much. >> Thank you. >> [music]
