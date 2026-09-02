---
id: p-znSwtxito
title: "Can GenAI predict code’s energy use and why should we care? by Wilco Burggraaf"
slug: can-genai-predict-codes-energy-use-and-why-should-we-care
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2026
speakers: ["Wilco Burggraaf"]
channel: "Devoxx"
duration_min: 16
published_at: 2026-04-09T21:33:21Z
video_id: p-znSwtxito
url: https://www.youtube.com/watch?v=p-znSwtxito
youtube_url: https://www.youtube.com/watch?v=p-znSwtxito
tags: []
topics: ["Governance, ethics & regulation", "Science, healthcare & applied ML"]
transcript: true
---

# Can GenAI predict code’s energy use and why should we care? by Wilco Burggraaf

**Wilco Burggraaf**

`Devoxx` · `Devoxx` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=p-znSwtxito) · [Conference site](https://devoxx.com/)

## Description

Please subscribe to our YouTube channel @ https://www.youtube.com/@DevoxxForever

This 15-minute demo shows how AI helps you spot and shrink the hidden energy and CO₂ footprint in “mature” Java code.

We use a simple, transparent theoretical model for sustainable decision making.

Micro-ops map to CPU work at one to five gigahertz, which we convert to milliwatt-hours bandwidth. Multiply that by your grid’s carbon intensity to estimate CO2. This matters because much of the marginal electricity on the grid still comes from gas turbines, so every milliwatt-hour you avoid cuts indirect emissions.

The AI annotates code line-by-line with uOps and mWh, flags smells/SOLID issues, predicts boost/threads risks, etc.

You’ll see how this works on small, widely used open-source Java libraries (think helpers, IO, logging, JSON).

We apply a lightweight playbook focused on under-utilization, waiting patterns, and bottlenecks. Using our ten DevOps++ open-source principles, like eliminate idle compute, right-size memory, prioritize I/O before scaling, prune work at the source, etc.

Key takeaways
A practical AI-assisted method to estimate a theoretical energy from code.
A repeatable playbook for low-risk patches that save watts without sacrificing speed.
A governance hook to make “less energy” a default quality bar in your CI/CD pipelines.

Target audience
Java engineers, tech leads, SRE/DevEx, FinOps/Sustainability owners, or anyone who wants measurable, low-effort energy wins in code and CI.

## Transcript

*2,418 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=p-znSwtxito&t=4s)** Yeah. Um, oh, sorry. No issue at all. Uh, the next 15 minutes will be over very quickly because there will be a jumping artist for inside of you in front of you. I mean, let me see if this Oh, it's not then we do it this way. So intro in introduce yourself. Um who is Sparky? >> Hi everyone. I am Sparky, your AI assistant. I inspect code, connect it to runtime evidence, estimate waste, and infer likely energy significance. >> So everybody says hi to Sparky. That worked. Nice. So Sparky, are you uh

**[0:54](https://www.youtube.com/watch?v=p-znSwtxito&t=54s)** nervous for today's talk? only in the way a toaster is nervous near a bathtub. I am calibrated, caffeinated by electricity and ready to behave just suspiciously well. >> I mean, yeah, her name is Sparky. Um, >> Wilco, before we begin, please introduce yourself. >> Yes, of course. So, I'm Wilbur Bergraph. Uh, I work for High-Tech Innovators. uh my key work is on lead development and architecture around sustainability and I try to help large enterprises to make their IT operation more sustainable. So what is in the core of this presentation today? Software choices change hardware use,

**[1:42](https://www.youtube.com/watch?v=p-znSwtxito&t=102s)** electricity and CO2. So the real question is whether AI can spot waste early enough to help. That's a very good question. So for who this is new this is electricity electricitymaps.com and this shows the emissions uh per kilowatt hour per country and for me the main focus I want to have is that the software we design and we write it runs on hardware it uses electricity and it has an indirect impact. If you want to debate it or want more answers about this come after the talk to me we can talk about this but for now we're going to continue to the next one. So frame the main question si uh simply >> can AI help us find code patterns that probably waste energy before we spend time measuring everything directly. >> Yeah, that's a good question. So before

**[2:32](https://www.youtube.com/watch?v=p-znSwtxito&t=152s)** I answer that with yes, I want to explain a paradox first. >> I got you. >> It's a question that has perplexed humanity from as early as the ancient Greeks all the way to the 21st century. And we're still dying to know which came first, the chicken or the egg, >> Wilco. Why did we watch this? >> That's a good question. So if you want to know how code behaves, static code on itself doesn't tell you the whole story. So code in its kind of the the egg. And if you want to know how it behave, you also need observability data. and uh to see how it like we all had like this this this code that didn't perform. We tried to improve it and then we tested it and there was no difference in time or performance. So um yeah, you cannot

**[3:22](https://www.youtube.com/watch?v=p-znSwtxito&t=202s)** kind of have this perspective without both. So if you uh can estimate energy, can you also estimate digital waste? I can classify waste as underutilization, waiting patterns, or bottlenecks. Then test whether the evidence supports a useful estimate. >> Okay, cool. But map those categories to something concrete. >> Here is the explainer. >> You mean that I have to explain it? Oh, we went a little bit too quickly. >> Nice vibe coding. Um but the left side is often the CPU. So what you see in production that most CPUs are only on a whole year basis utilized for 20 to 30%.

**[4:10](https://www.youtube.com/watch?v=p-znSwtxito&t=250s)** The ideal situation is 70 80%. The middle thing with with waiting we built a lot of waiting patterns from code to architecture like you can build a loop that does just waiting but actually use uses the full core. And the last one, who have you ever added like extra CPU or memory to their virtual machine or container while actually the database or something else was the thing that slowed the whole thing down? So those three patterns, you see this all the time and they're very connected to energy. So here is the theoretical model that I came up with if you seen also the abstract and um it's a theoretical model and the theoretical model is is one herz is equal to one micro operation the smallest thing that a core computes and um one core is equal to 1 ghahz and in

**[4:58](https://www.youtube.com/watch?v=p-znSwtxito&t=298s)** this case um also one core is equal to 1.2 twofold. Why is this important? That if you give this >> from now I will use your decision model. >> Nice. If you give this to kind of any model, it understands in which space it is. I mean AI is not that smart but it understands on what it's trained in which kind of dictionary domain it now should look at. Tada. Everything I was trained on is in here. So I can just add whatever you want inline in this example code. Just don't tell the kernel and runtime nerds. They'll say it's so wrong. >> Yes, because you can't do theoretical estimations. But people who know actually how things are executed on the lowest level know that runtime uh the

**[5:47](https://www.youtube.com/watch?v=p-znSwtxito&t=347s)** operating system and hardware has a big influence on the actually microperations. But I dare you that for most juniors and meteor developers, if you would ask them up front like which line is the one who computes the most and also in this case consumes the most energy, they probably didn't instantly would say like the last one in this case the totals merge uh with a 560 billion of estimated uh microperations and the first one the line split with 240 billion microperations. So it gives you also an idea where compute is and how you can do certain optimizations and this is exactly why why I created this theoretical model. So can you show CPU activity uh becomes an energy estimate >> here two cores work hard while four sit

**[6:38](https://www.youtube.com/watch?v=p-znSwtxito&t=398s)** idle. So what what happens if you only use like one thread or maybe two threads? The CPU can especially of the package can boost it up right to in this case 5 GHz. But that same code >> when every core runs flat out the chip works harder gets hotter. >> Yeah, that same code can also run over of course multiple if you make it async or in a parallel pattern, but you cannot boost them all because then you're probably going to burn out the CPU. So that's not going to work. >> CPU cores also change speed dynamically. Lower frequency often means less work. >> So we probably never thought about the fact that how we ceue up code that is like all the people you see standing there the coding part how we wait with our code and how we async in parallel

**[7:28](https://www.youtube.com/watch?v=p-znSwtxito&t=448s)** code has influence on the frequencies. >> Voltage changes too with frequency. You could say that it's probably the other way around that if the voltage change that the frequency changes but here again so you can have the same code but based on the uh CPU behavior you can have different energy patterns >> power over time becomes energy >> and now it becomes interesting because if you have a function that runs like for 10 seconds or for a second if you understand based on even with virtually on what hardware it runs on you can calculate the amount of adventurally emissions for that software and that is something we do in sustainability but it also means that you can if you can give it to the AI it can start doing

**[8:16](https://www.youtube.com/watch?v=p-znSwtxito&t=496s)** estimates like I said it's not perfect but for decision making it can really help >> finally real code yay >> so well we had some code but can you show uh the prepared open GDK example >> I found the article you asked for that explains the open JDK K bug fix. >> I hope not everybody's running away, but the first example is going to be open the ADK and then some C++ in this example. So, show the code from before the bug fix. This C++ snippet is the old Open JDK Linux implementation behind get current thread user time before the fix discussed in the article. >> So, it's kind of cool that this is two things at the same time. So one is um

**[9:06](https://www.youtube.com/watch?v=p-znSwtxito&t=546s)** utilization is one of the things to kind of understand how much energy you're calculating. But here there was an issue and this was a while back and there was also a nice YouTube video about it by the premigen and there are two key things in here here that slow kind of everything down. One is it is using a virtual file. Uh you could do the same of course with Java but this for OpenGDK the original of course codebase was in C++ and um yeah the the opening and the the closing on itself you will see has an impact but also to get just one number out there the user time. So to know the utilization for user time so since the booting of the system it keeps track of all the um idle all the kernel time and the user time. So if you know like okay this process had 500 millisec

**[9:54](https://www.youtube.com/watch?v=p-znSwtxito&t=594s)** seconds of user time and it run over a second and 50% uh utilization occurred. These are the core focuses for now. So label the waste type. >> Using your theoretical model the top three waste points in this original code are proxs open proxs read and CPU time string parse. So when in this case ch looked at this it didn't knew the article it didn't know any other context except the model and the same code and it already I will also zoom it a little bit down and you see also see the amount of estimated microperations there uh in the the open and the read probably between the open and the read there is some

**[10:41](https://www.youtube.com/watch?v=p-znSwtxito&t=641s)** overlap there and also in this case in the string manipulation developer test one. >> So when developers tested it with a flame graph, they actually saw indeed that just for this one function to get the user time out there and maybe you use it in a certain um how do you say it? Um live benchmarking to see how the utilization is going on. Um in all itself just opening the virtual file was 43% of this function. Developer test two >> and just closing it was 40 what is it 40 of 34%. >> Developer test three >> and just the string manipulation on its own kind of the business logic was 3.9%. So not the only thing it did kind of was

**[11:31](https://www.youtube.com/watch?v=p-znSwtxito&t=691s)** just getting the number. So now show the improved code after the bug fix >> after open JDK gets a thread clocked flips it to VRT and calls clock_get time for user time directly. >> So what it now eventually is doing is just getting the uh process ID and just in memory instead of going to the virtual file just get it there and it was a lot quicker. So estimate with the model first is go probably. >> The article benchmark shows about 11.186 UOPS before and 0.279 UOPS after around 40x faster on average. >> Yeah. And here is a nice example that

**[12:20](https://www.youtube.com/watch?v=p-znSwtxito&t=740s)** GPT can hallucinate because the above part is not the correct part. The correct part is the amount of time in in combination with the operations because the um disk uh operation was way more expensive in this case than the memory um operation. But it it went a lot faster in this case >> at 100 watts. That is about 0.0000311 millwatt hours before and 0.775 after. Roughly 3.2 2 versus 129 billion calls per kilowatt hour. >> Is there a chance that you're probably going to call this function that many times? Probably not. But if you think about how everything in software scales and and this is just a very small example. Um yeah, there is difference

**[13:09](https://www.youtube.com/watch?v=p-znSwtxito&t=789s)** eventually in the software that you write in the actually energy that is consumed. So now find a bottleneck example that shows the power of scaling further. >> JSON Java JSON object to string is a strong match. Same contract, less helper overhead, strong measured improvement. >> I mean we all like nice u formatted uh JSON. JSON and object dot to string int indent factor formats JSON so humans can read nested data indent factor controls spaces per level two means child fields indent 2 grandchildren 4. >> Yeah. So let's see how the code looks like. >> String writer uses synchronized string

**[13:56](https://www.youtube.com/watch?v=p-znSwtxito&t=836s)** buffer. String builder writer removes lock cost and initial sizing reduces growth copies allocations and later GC cleanup. So just um different type in this case of um string string build from string writer to string builder and predicting the amount of size because if you have a large file and going to add a lot of indent to it it's going to grow um can have a big impact on the actually um yeah computation >> scale matters larger JSON means more characters deeper nesting more buffer growth, more copying, more UOOPS, and more modeled MW. Runtime drops from 120 to 81 cumulative

**[14:46](https://www.youtube.com/watch?v=p-znSwtxito&t=886s)** CPU hours. On a 32thread server, the wall clock time drops from 3.75 hours to 2.53 hours. At 250 W average server it load, energy drops from about 0.94 kwatt hours to 0.63 63 kwatt hours saving about 0.31 kwatt hours. >> So yeah, I mean >> at 200 g CO2 per kilowatt hour that modeled saving is about 79 g CO2e per terabyte serialized. >> And although that 79 g is only like 700 m in my Ford Focus, it is still um yeah it is still an impact. So also because of I'm already over the time.

**[15:34](https://www.youtube.com/watch?v=p-znSwtxito&t=934s)** >> So let's see the core thing is >> we all do kind of things on per call. There is a workload in your whole organization. Every skills up to complete feed fleet. You have often like more than thousands of containers and virtual machines in organization a large organization. So the impact is real and that was kind of the core of my talk.
