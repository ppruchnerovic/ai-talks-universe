---
id: Emo5FGGY-wM
title: "Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab"
slug: why-80-reliability-isn-t-good-enough-felipe-blanes-amazon
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Felipe Blanes"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-10-09T00:30:02Z
video_id: Emo5FGGY-wM
url: https://www.youtube.com/watch?v=Emo5FGGY-wM
youtube_url: https://www.youtube.com/watch?v=Emo5FGGY-wM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "LLM evals", "AI evaluation", "benchmarks", "agent reliability", "customer trust", "browser agents", "Amazon Nova Act", "Amazon AGI", "AWS", "eval flywheel", "AI product management", "computer use", "Felipe Blanes", "AI engineering", "AI Engineer"]
topics: ["Evals, observability & reliability"]
transcript: true
---

# Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab

**Felipe Blanes**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#LLM evals` `#AI evaluation` `#benchmarks` `#agent reliability` `#customer trust` `#browser agents` `#Amazon Nova Act` `#Amazon AGI` `#AWS` `#eval flywheel` `#AI product management` `#computer use` `#Felipe Blanes` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=Emo5FGGY-wM) · [Conference site](https://www.ai.engineer/)

## Description

Your agent scores great on benchmarks. Then real customers use it and it breaks.

Felipe Blanes from the Amazon AGI Lab shares what he learned working directly with customers of Nova Act, Amazon's service for building browser agents, from research preview to general availability on AWS. He calls the core problem the benchmark illusion: static evals look great until customers do things nobody expected, and then all you have left is hope. His fix is an eval flywheel built around the customer: define success the way the customer does, capture signals (including by talking to customers), diagnose gaps in the model, harness or product, and feed them into decisions. He explains the trust cliff (80% reliability feels like more work; around 92% feels trustworthy), why being open about limits builds more trust than higher benchmarks, surprising use cases from Amazon Leo, Hertz and Sola, and four principles for keeping evals fresh.

In this talk:
• The benchmark illusion, and why static evals leave you hoping
• A four-step eval flywheel driven by real customer signals
• The trust cliff: why 80% reliability isn't enough
• Why being open about limits builds more trust than higher scores

SPEAKER
Felipe Blanes, Amazon AGI Lab

LINKS
Amazon Nova Act: https://nova.amazon.com/act
Nova Act docs: https://docs.aws.amazon.com/nova-act/latest/userguide/what-is-nova-act.html

CHAPTERS
0:00 Intro
0:47 What Nova Act is
1:57 Working directly with customers
2:22 The benchmark illusion
3:21 Static evals and hope
4:26 Close the customer loop
4:41 The eval flywheel
4:56 Step 1: define success
5:11 Step 2: capture signals
5:31 Talk to your customers
5:51 Step 3: diagnose gaps
6:56 Step 4: feed decisions
7:26 Four stages of the customer journey
9:35 Lesson 1: the trust cliff
11:10 Lesson 2: be open about limits
12:45 Lesson 3: surprising use cases (Amazon Leo, Hertz, Sola)
14:44 Four principles
15:59 Evals should get smarter every week
16:14 Two takeaways

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,639 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=1s)** [music] Can everybody hear me? Okay, perfect. So, first thanks for joining everyone. Uh, my name is Filipe and I am a member of technical staff at the Amazon AGI lab. Um, as part of my role, I help us to build the next generation. I manage the programs to build the next generation of products our lab is building. And today I will talk to you about designing evolves that earn customer trust. Before talking about evolves, I just need to give you some context about what our lab was doing the past year. So everything started in March last year

**[0:50](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=50s)** where we launched our Nova research preview. for context like Nova is a tool that we build as part of our lab and it's a tool that helps you to build browser agents. So basically everything that you do in a web browser you can use Nova to automate those tasks. Uh and as part of the research preview our main goal was we wanted to ship a product to get as much feedback as we could from our customers. Uh in March we launched that. Then in July we made one additional improvement in our product which was basically develop a whole new developer experience and this was because basically during the first couple months we noticed like some gaps in the developer experiment experience

**[1:38](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=98s)** and we wanted to make sure customer had the best experience building agents. Then in December we finally launched our service on AWS. So today Novax is a top tier service on AWS that anyone can use to build production level agents and during this period I was basically responsible for the customer enablement piece of that. What's customer enablement just for context? It's basically I was working daytoday with all of our customers to understand what was their problem and how we were helping them to solve that. So that was my main uh role uh during last year. And then let's go to uh the problem that we will be discussing today. So I like to call this is the benchmark illusion.

**[2:26](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=146s)** So you all working on AI. You are probably working on and building things based on benchmarks, right? It could be public benchmarks that everybody's using and everybody's trying to optimize the products on that and also benchmarks that you are creating your own synthetic data that you are creating and you are evaluating your product. Uh and the main goal here is you want to optimize right you want to be the best as you can there in those benchmarks but then when you ship that to production and your customers start using that what happen is it's this right they start seeing problems and it's basically everything that you were not expecting them to do they try to do that and they break your product and this is happening because you

**[3:16](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=196s)** basically most of us we are doing we are working on evals that that are static. So what are static evals? Basically let's talk a little bit about what's the standard development process of a product right first thing that you do you receive uh the requirements from your product chain and you start building right everybody does that I hope then when you have a product in a good shape the next thing that you will do is running your evals again public benchmark synthetic data that you generated and you optimize for that when you start feeling comfortable you're like okay now I will ship that and you ship that to the customers but if you have a static evals what's the only thing that you can do after that

**[4:04](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=244s)** it's basically this is hope right you just hope your evals were reflecting exactly what your customers would do with your product and if not it will start failing right and this is the gap this is exactly what we will be discussing today and what we were doing in our lab to solve this problem. And just a spoiler, so this is not about better benchmarks. It's about closing the customer loop. So what we want you to do here is get the feedback from your customer and close the loop. So with that in mind, what we did in our lab was basically propose an eval flywheel. So if you are not aware about the terminology but flywheel is basically a loop that you keep repeating like all the time and the first step of

**[4:55](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=295s)** this evolve is define success and very important here. So define success here it's not what you think it's success it's what your customer think it's success. Okay. So next step as soon as you understand what your customer really needs and the problem you are trying to solve you go to capture signals and we as engineers what's the first thing that comes to your mind it's like instrumentation right let's get metrics let's get data as much as you can about what your customer is doing but one very important piece of that that we are missing is you should talk to your customer like talk to your customer go schedule meetings uh visit them and understand exactly what

**[5:43](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=343s)** they are trying to do. Your data might be a little bit misleading. You might be missing exactly what's the problem that your customer is trying to solve. Third step, you go to diagnose gaps. That's easy. That's basically you get all these signals from customers. Could be instrumentation but also your inputs, your insights from the meetings that you had with them. And you just start categorizing those. And when I say categorizing there are basically very high level but there are three things that you could find from those discussions. First it's basically inputs about your model. So where your model is failing there and this feeds into evals right to your model. The the second point it's inputs to your engineering team. So basically what uh is the gap in your hardness that you should fix. This

**[6:33](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=393s)** is more traditional bug fixing. And the third one is also on the product side. So what are you missing in terms of product like do your customer understand exactly what your product is trying to solve? Is your product like properly positioned? So that's very important. So as soon as you have the gaps di the gaps categorized you just feed that into decisions. So feed that into decisions is basically you prioritize that and you ask your science, your engineering, your product team to address those. That's basic, right? And then you just continue repeating this loop over and over. So with that in mind, like in our lab, we repeated this flywheel several several times since March last year. And what I also noticed is basically as part

**[7:24](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=444s)** of my journey as a product, each of my c each customer will have their own journey using my product. What that means? So my customer evolves as they use my product, right? So there are basically four things that you can learn while your customer use your product. The first one is that's the first thing that you will do the first time that you meet a customer. It's basically use case discovery. So what you want to do here at this first step it's basically understand what's their problem. So what's the problem of your customer and make sure what you are building solves that. Right? Then after that you will have couple early adopters. Right? from these early adopters the main signal

**[8:15](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=495s)** that you want to get. It's basically what's possible. So that's the time where customer will try crazy things. You will find things that you cannot help them at at all, right? But you will also find things that your customers are using your product to solve and many times you will be surprised because it's something that you would never imagine. Third point, this is when you start scaling, right? You get your early adopters but now you start scaling. you are getting more customers and you are able to identify some patterns, right? What are the patterns? The pattern is basically your hero use case, right? That's the case, that's the problem that everybody is using your product to solve. And last one, this is more future looking, but these are your product

**[9:04](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=544s)** gaps. So when you were working with early adopters and also after you start scaling you will also be finding some gaps on your product. Your product team can help you to prioritize those and these are the bats for your future right what you should build next. Um as I said I work with several several customers during this journey and there are a couple learnings that I want to share that some might be obvious but others it's very very insightful. So the first one is the the trust cliff that I I like to call. So what's the trust cliff? So imagine you build a product, you are ready to ship and you and you measure the reliability of this product

**[9:53](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=593s)** and you found 80% reliability. That seems fine, right? You're like, okay, I can give that to my customer and they they can start using it, right? But what your customer thinks when you say you are 80% of reliability is I cannot trust this product. I cannot trust. Uh and why? Because when you show 9 80% reliability, what they will think is oh okay so if it's 80% I still have to monitor this agent. If they fail I will need to do some manual work. So in fact it's actually more work for me not less work. I need to build this agent plus monitor that and also do some manual work after but when you get

**[10:42](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=642s)** to a point around 90% reliability the message changes to your customer and what they think it's okay 90% I can actually trust this right to handle my tasks and I completely hand over like a workflow to my customer. So it's basically reliability is a zero to one, right? Or you trust or you don't. There is nothing like in the middle there. Second learning, it's the eval transparency. So every time that you start working with a customer, you basically need to be transparent about three things that your product does. First thing is that's easy. Everybody likes to do that. So what works? So you basically show to your customer I am

**[11:32](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=692s)** really good doing this. That's the level of reliability. You can trust my product. Just use my agent and it will give you the reliability that you need. Second point is these are the things that I'm doing to improve my product. Okay. So there are some things that I know it's a gap but I am investing time right now to make this better. And the third thing that's the tough one. Nobody wants to do that that it's what is out of scope. So you really need to be transparent. Like if something doesn't work for your product, just go ahead and tell your customer. Don't let them try. Otherwise, like there are so many tools in the market right now that if you do some if you show something for them that doesn't work, they will just forget about our product and they will move to the next. So be transparent.

**[12:22](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=742s)** And the main learning here is transparent on product limitation increase trust more than higher benchmarks. That's a very interesting finding, right? Be transparent about what your product is capable of doing and in more important what's not capable of. That's how you earn customer trust. Third learning is if you work work very close with customers, you might find a lot of use case that you would never expected. So some examples here is Amazon Leo. It's the satellite internet satellite company from Amazon. Working with them, we actually learn some inputs uh about creating features to do caching of trajectories. So instead of doing inference all the time that they use our product, we cache trajectories. If it

**[13:11](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=791s)** fail, we just fall back to the model. So we optimize the cost for them. Second learning is with Herz, the car rental company. So they were also using our product for QA automation and we learned that as part of their company they had some QA engineers that were very technical and were capable of building like scripts with Python and other coding languages. However, some technical uh some people from QA they are not that technical. So that was the input that we needed to actually build a whole non-technical experience for our product that would enable more customers to use it. Last one, this is a startup called Sol. Solar is basically a RPA company. If you are not familiar with

**[14:02](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=842s)** the term, RPA is repetitive process automation and they offer tools to automate process for other companies. So imagine the variety of use cases that they might have. It's a lot of different use cases. And what we learned from then is we could give some additional flexibility in our product for them to customize especially the actuation stack of our tool. The learnings here are less important than keeping in mind that you will learn a lot about what your customers is trying to do here, right? and what should be the next features you should build for your product and then like running this flywheel several times we came up with four principles for this flywheel.

**[14:51](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=891s)** First one is derive eval uh eval scenarios from production not imagination. So again like creating synthetic data might be very important at the beginning of the process but as soon as you start getting customer signals make sure that feeds your eval second categorize into actionable areas. Again product issues, engineering issues, research issues, make sure you prioritize that well to your team. Third one shared capabilities honestly. Again, transparency builds trust. Make sure you share to your customer, especially what your product is not good at. Third one is run the flywheel as fast as you can. So here it's basically the

**[15:41](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=941s)** faster you run that flywheel, faster your product will improve, right? That's almost obvious, right? But keep it that in mind like run your flywheel as fast as you can. And then like with those four principles what you will see is uh your evals will should get smarter every week. But very important if you are not seeing your evals getting smarter every week that means your evals are getting stale. Okay. And just to finalize the talk here there are two ideas that I want you guys to take home. Just two. So first idea is eval must reflect what customer cares about not what you think they care about. Okay. All about getting

**[16:30](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=990s)** customer input here and make sure your evals reflects what's their problem. Second is evals are not built once. It's a flywheel that evolves as your customer evolves. One note here, remember that customer journey, as your customer moves through that customer journey, what they are trying to do with your product will also change. Like it will get more complex, right? So your evals needs to be up to date and reflecting exactly what your customer is trying to do right now. And with that what you have to do is simply like build the loop ship evolves that matter and then you earn your customer trust. And that's all that I have for today. Uh thanks very much for

**[17:20](https://www.youtube.com/watch?v=Emo5FGGY-wM&t=1040s)** joining. Uh I will stay in our booth after for more discussions. But again enjoy the conference.
