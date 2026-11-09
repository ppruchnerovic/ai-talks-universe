---
id: oWqsBuhRRZ4
title: "How We Mapped a 35-Million-Line Mainframe in 4 Days - Stephen Chin, Neo4j & Neeraj Deshmukh, Blitzy"
slug: how-we-mapped-a-35-million-line-mainframe-in-4-days-stephen
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Stephen Chin"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-11-06T20:00:10Z
video_id: oWqsBuhRRZ4
url: https://www.youtube.com/watch?v=oWqsBuhRRZ4
youtube_url: https://www.youtube.com/watch?v=oWqsBuhRRZ4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Stephen Chin", "Neeraj Deshmukh", "Neo4j", "Blitzy", "legacy modernization", "COBOL", "mainframe", "knowledge graph", "AI agents", "code migration", "financial services", "banking", "testing", "AI Engineer", "AIE NYC"]
topics: ["AI in the SDLC & engineering orgs", "Science, healthcare & applied ML"]
transcript: true
---

# How We Mapped a 35-Million-Line Mainframe in 4 Days - Stephen Chin, Neo4j & Neeraj Deshmukh, Blitzy

**Stephen Chin**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Stephen Chin` `#Neeraj Deshmukh` `#Neo4j` `#Blitzy` `#legacy modernization` `#COBOL` `#mainframe` `#knowledge graph` `#AI agents` `#code migration` `#financial services` `#banking` `#testing` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=oWqsBuhRRZ4) · [Conference site](https://www.ai.engineer/)

## Description

Stephen Chin of Neo4j and Neeraj Deshmukh of Blitzy show why AI struggles to modernize the decades-old systems underneath banks and insurers, and how a knowledge graph fixes it. Using a COBOL interest calculation as the running example, they explain that AI can convert a formula but misses the batch jobs, data layouts and other places the logic is used, and that bigger context windows don't solve it. They walk through Blitzy's approach of mapping the whole codebase as a graph, giving thousands of agents the right slice of context, testing at every step, and proving the new code matches the old down to the cent, with results from a tier-one bank, a 35-million-line mainframe and a Fortune 100 insurer.

Chapters:
0:00 Intro
0:14 The old systems under modern finance
1:58 Example: computing interest on a mainframe
3:06 Why AI misses the rest of the system
4:02 Why bigger context windows don't fix it
6:03 Turning code into a graph
7:08 Giving every agent the right context
7:53 Blitzy's process, with a human in the lead
9:32 Thousands of agents and constant testing
11:35 Proving the new code matches the old
13:28 The one-cent rounding bug
14:27 Results from banks and insurers
16:37 Beyond modernization
18:47 Resources

Stephen Chin

Neeraj Deshmukh

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*3,009 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=1s)** [music] >> We have a really exciting session for you guys. So, um you probably don't realize how many systems and how much of the infrastructure which drives modern finance, which drives all the things which happen in the financial district in New York City are driven off very old systems which can use a lot of modernization. And you probably interact with them on your on your cell phone, you maybe you're banking on a mobile app, but you don't realize that underneath the covers there's business rules, there's batch jobs running in nightly processes. You have all these different

**[0:49](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=49s)** data contracts and things running under the covers. And it's running on infrastructure which people are frankly afraid to touch, right? If you if you make one little line of code change, you risk breaking the whole system. And um so this is um fun fact about myself. So, um you know, now I'm I'm known for doing a lot of developer relations, AI conferences, book writing. Um back 30 years ago, I was a Java developer who was migrating COBOL code off mainframes and like, you know, figuring out how to modernize applications. And it was multi-year projects, very challenging work which inevitably you hit little bugs and issues. You couldn't test it thoroughly enough to hit all the

**[1:36](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=96s)** different corner cases and very very challenging projects which often failed. So, I think that what we're going to show you today is amazing cuz it's a new path forward where you can drive the change and you can actually do this, but um why don't you tell us a little bit about how this works, Neeraj? >> Thank you, Steve. So, we're going to do this with an example, right? Uh, in the context of a public demo system which Amazon developed a few years ago. This is the AWS card demo. And going to take a specific example here where we are trying to compute interest, right? And so, as you can see in this little

**[2:24](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=144s)** chart, we have a batch job that's calling the interest program which is getting the copybooks and layouts and then generating basically VSAM data, right? And so, the output here is money and of course, the result depends on the inputs, the job that runs it, the account updates, not just the formula for computing the interest, right? So, let's remember this example. We're going to keep coming back to this, hit that theme over and over again as we progress through the talk. So, when I want to modernize this and I tell AI, hey, change that formula from Cobalt to Java,

**[3:12](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=192s)** all it's going to do is find the formula, try to convert that, right? What it doesn't find is the the record precision, the account updates, the transaction output, the batch contract. And if you miss any of these, you're not guaranteed to get the right outcomes. So, the failure here is not that AI can't write the code. It's that AI doesn't know the 14 other places where that logic, that code is being used. >> Okay, and this this looks pretty scary. I mean, besides the AI not knowing the code, that pipe looks like it's about to burst. >> Yeah, and of course, the AI doesn't know that it's going to happen any moment now. So, Stephen, you would think that a context

**[3:59](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=239s)** expansion would fix this. Why doesn't that >> Yeah. So I I think that one of the things actually the previous presenter talked a bit about this, how we're we've all been relying on better models, on having better systems, a better AI systems to solve this. And frankly, it hasn't been working for these sorts of use cases and the reason is context. So you can do vector databases to get and you know expand your context, but all it gives you is similarity searches. You can do relational databases as well and this gives you a much bigger repository. You can hook it up via an MCP server, but again, you're you're limited on kind of single hop and like looking up facts and information by SQL queries. What a graph gives you is a graph gives you this

**[4:47](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=287s)** multi hop accurate information and context for your model. And the reason why this context is so important is because your model cannot possibly give you the right results because it can't utilize its own context. So most models, you know, nowadays are advertised with a million token context windows. Um but what do they actually how much usable context do you actually get? And the reality is you get 200k or less usable context, right? So it's by by study the accuracy goes down dramatically as you fill the context more and this means you have to give precise and accurate context. >> Yeah, the effective context these days is about like 20 to 30% which means about

**[5:36](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=336s)** 200 to 300,000 lines of code. If your software is bigger than that, too bad. You're going to start losing information. >> So context is serial, but information has relationships. Information has connections between it. And this is the key to how you can actually line up your data. >> Yeah. So I mean here so code becomes a graph, right? You can see all of these relationships that are being mapped here now. Uh, and like the the program is there. It has the the job that's executing it, the copy book that are getting included, so on and so forth, the outputs. The important part here is

**[6:25](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=385s)** the stuff on the right. So, every edge in the graph keeps its identity, right? Where did it come from in the repo? What revision was it? What symbols does it touch? There is evidence for the file and the and the source span, how it was extracted. And the graph keeps getting updated on on every merge as the code changes, so does the uh the graph. And that way you keep it fresh, you keep it current, you invalidate stuff that is no longer valid. >> Yeah, and you can see that the code is very much a graph-shaped problem. So just from the structure and the relationships, it's something where you have a lot of interconnects. Um, and then when you what why don't you talk about how this works for agents? >> Sure. So, each agent uh in Blitzz has a specific

**[7:15](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=435s)** task context packet, right? And that includes what the task description is, uh but also where does it belong to in that graph, right? There's the slice of the source, right? What constraints it has imposed, what evidence it has available, and what questions are still not answered that that agent is now supposed to work on. Uh, and this is what we mean by infinite code context, right? It's not remembering the entire uh information in in your code base, in your software estate. It's basically having access to the right information at the right time, in the right place. So, Blitzz effectively works like a compiler for the entire knowledge in the enterprise, right? You start off by reverse engineering the entire software

**[8:03](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=483s)** estate. You extract the business logic, uh the workflows, the dependencies. Then you get the requirements and the rules from the user to say, what do you want to do with this? And you convert that into an actionable agent action plan, right? This is the spec that you're going to use to make that forward change. Note that next block there, there is a human approval, right? Nothing happens without a human in the lead making decisions at every key point, right? But once you have that plan reviewed and approved by the human, now the agents go off, they do the code generation. But there is also validation that is baked into it at every step. And so the end result is you get tested and validated code in the form of

**[8:52](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=532s)** a pull request and an evidence documentation for what has happened and how it has been validated in the form of a project guide. So there is a human approval at every step that matters. And because you have access to the full repository and you also have the instructions about how to build the environment, how to run the code, you are not restricted to just static information. You can actually observe the runtime behavior and make changes accordingly. So the the knowledge graph basically drives all of this, right? But that's not the only thing that helps here. There are two other things that compound the impact that this has. One is

**[9:42](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=582s)** hyperscale orchestration. Like we have thousands of agents who all share that plan. Every agent has access to the effective context and there is nothing lost between them. And couple that with extreme validation, right? You have testing happening at every stage of code generation. We actually spend more computes on testing than we do on code gen. And this results in what is effectively production safe code, that has been tested, validated at enterprise scale and so it is safe to make merges into your production systems. So the agent action plan is is the spec, right? That's the plan before you start doing any actual work

**[10:29](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=629s)** and it decides what the scope is, what gets transformed and what must be preserved, right? And a domain expert, a human would review this, make sure that it's aligned with their expectations, approve it and this is coupled with the four controls that are inherent at every step. There is system level context, that's the knowledge graph we talked about, right? Every change impacts the entire estate, so everybody needs to be aware of that, right? There is continuous validation, so testing testing testing right? There's no substitute for that. You have explicit guardrails in place to address your security, your governance, your compliance requirements. These are inherent to any regulated industry and of course finance, right? And then the human in the lead because

**[11:17](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=677s)** the decisions that matter are owned by real people. The AI is not making them autonomously. And this of course preserves the behaviors right? The existing behaviors have to be transferred as is to the to the modernized code and how do you verify that? Right. So in this case like we want to preserve the money like the precision, the rounding. We want to preserve the state, the balances and the transaction records, failures operations everything right? If we have defects, they also need to be managed with explicit decisions. The rules have to be preserved as well and you have to prove the parity. You can't

**[12:05](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=725s)** take it as an assumption or as a promise. So the way we do that is there is testing on the baseline. There is equivalent testing happening on the modern system, and we are looking at inputs and outputs, the returned values, what states get persisted, what is the transaction output look like, right? What are the error outcomes? Not just the happy path, but how do you deal with like bad situations? And all of those have to be exactly matching in the context of each operation, and the differences have to be none. That's our promise to deliver this. So this is layer, right? This doesn't happen only in the end. This is baked into the very fabric of the code

**[12:53](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=773s)** generation. Every line of code that gets generated gets built and tested with unit tests. The build has to be compiled. Runtime integration, it has to fit within the existing kind of framework that you have. Your data parity has to be there on every write, and the end-to-end workflow has to be identical. So this is a code from one of the customers where we actually did this, right? The transpiled job produces output that is byte for byte identical to the golden mainframe baseline. This is from a Fortune 100 insurance. Here's a fun example. >> So so this is something I can get into as an old Java developer where we we made lots of errors with big decimals and rounding in our implementation. So AI can do this better, right?

**[13:40](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=820s)** >> Right. I mean you you you would think so, right? Because like you computed a a Java version of this this formula to compute interest, right? Cobol behaves differently than Java. Java has an inherent rounding up built into it. What that means is the modern code compiles, it generates results that you believe are correct because it's behaving like normal Java code, right? But you have this little difference of that 1 cent that happened because of the inherent rounding. If you didn't have that parity test, you wouldn't have caught this. And now imagine this happening over a million transactions. Fun. So that was just one kind of simple example, right? But now you can think of

**[14:28](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=868s)** like a full trade posting engine where this gets applied throughout the entire workflow. This is something that we did for a tier one bank where we had a monolith that had stored procedures uh cross database uh kind of uh write access going on. This got converted into six capability modules uh with PostgreSQL, Java, TypeScript, Python, the fully modern stack uh and with full parity. Right? And took only 18 days uh whereas their original plan was to have uh 18 engineer weeks dedicated to this project. Right? This was doing things the kind of human way. Uh with Blitzz, it got reduced to 18 days. Right? We We wrote 4,000 plus tests. Uh the

**[15:15](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=915s)** modern code was less than half the size of the of the new of the old stack uh and the customer was happy. There is no doubt that we can use Blitzz to modernize the whole system is is what they said. Another example, mapping a 35 million line mainframe. Uh this is something uh that they had spent on an SI about eight months, several million dollars and had nothing to show for it. Uh Blitzz reverse engineered that in a matter of four days and this is what they have to say. They've been in the dark room with a pencil light inspecting each individual module. Blitzz feels like flipping on the overhead light, seeing the whole room at once. This is what AI accompanied by a knowledge layer can do for you. Right?

**[16:02](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=962s)** Uh another example, we modernized a 25 million line monolith. This was a policy admin platform again uh compared to a human aided by AI like your typical IDE based uh agentic tools uh would have taken a certain amount of time. We did it nine times faster. 85% of the code was autonomously completed and almost 90% of that made it into production. This extends to different systems, different companies. As long as you understand the whole system before you change it using AI, you're good. And this doesn't just stop at modernization, right? Ultimately, transformation is the goal. Britezi is not a modernization platform. It is a transformation platform. You can do new product development. You can add new

**[16:50](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=1010s)** features. You can do security remediation and detection. All kinds of use cases open up when you have that entire estate available to you. And so another coming back to the card demo, now that you have modernized it, you may want to add a new feature, a promotional rate to the interest path, right? You already have the upgraded knowledge path now because you already have the modern system. Your knowledge layer got updated. You have your governance rules established. You have your test suite expanded. So now this becomes a lot easier and faster and cheaper to do than it had been before. And then you can do this beyond the code to expand this kind of knowledge to apply to new cases, new use cases

**[17:37](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=1057s)** like providing audience, providing evidence for like audit ready compliance issues. So as you can see, this is heading beyond software and mapping the whole business now. >> Yeah, so I think that you can see the power of building a an modern enterprise layer on top of a knowledge graph. And it starts with a graph, builds out the business rules, business processes, and then allows you to build end-to-end systems which not only solve the modernization use case, but they also give you capabilities to expand your business. So you can now do um for example, Dora compliance on your um entire system to make sure it meets

**[18:26](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=1106s)** regulatory requirements. You can track business rule changes. You can do financial fraud and build um use cases which will track down other sorts of problems and this expands to even further out where you can extend your system and build more value off of it. We want to leave you with a few references to um to take with you. So um one is the Nodes conference, that's the QR code on the left, is a full 24 hours of sessions learning on knowledge graphs on how you can build and apply a bunch of these concepts for our knowledge graphs to your own systems. And um Niraj, you want to talk about >> Yeah, the Blu Age sandbox, that's the QR code on the right, will allow you to in

**[19:13](https://www.youtube.com/watch?v=oWqsBuhRRZ4&t=1153s)** fact bring in your own code and uh see this for yourself. Don't just take our word for it. You can also see the AWS card demo modernization that we showed here uh as an example there. >> Okay, so thanks so much for joining our session at A and G in New York City. And um if you have any more questions, feel free to drop by the Neo for J booth or come up and chat with us after the talk. Thank you. >> Thank you very much.
