---
id: YXb2Wx1r_Pk
title: "Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal"
slug: keyword-search-is-dying-is-your-catalog-ready-for-ai-agents
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 16
published_at: 2026-10-04T18:00:25Z
video_id: YXb2Wx1r_Pk
url: https://www.youtube.com/watch?v=YXb2Wx1r_Pk
youtube_url: https://www.youtube.com/watch?v=YXb2Wx1r_Pk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "agentic commerce", "AI shopping agents", "product catalog", "semantic search", "keyword search", "hybrid search", "product data enrichment", "ecommerce AI", "AI SEO", "GEO", "PayPal", "vector search", "conversational commerce", "Nixon Dinh", "AI Engineer"]
topics: ["Agents & orchestration", "RAG, retrieval & knowledge"]
transcript: true
---

# Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#agentic commerce` `#AI shopping agents` `#product catalog` `#semantic search` `#keyword search` `#hybrid search` `#product data enrichment` `#ecommerce AI` `#AI SEO` `#GEO` `#PayPal` `#vector search` `#conversational commerce` `#Nixon Dinh` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=YXb2Wx1r_Pk) · [Conference site](https://www.ai.engineer/)

## Description

Shoppers are moving from typing keywords to describing what they need, and agents are doing the searching.

Nixon Dinh, director of product for agentic commerce at PayPal, explains how shopping is moving from the search era to the intent era and then the delegation era, and why product catalogs built for keyword SEO aren't ready for AI agents. He breaks down keyword vs semantic search and shares the results of PayPal's experiments enriching merchant product data. Enrichment consistently improved agent recommendations and thin catalogs gained the most, but over-enriching with unstructured boilerplate diluted the signal and made agents hallucinate.

In this talk:
• Search era, intent era, delegation era: how shopping behavior is shifting
• Why catalogs syndicated for ads aren't readable by agents
• Keyword vs semantic search, and why hybrid wins
• Enrichment patterns that help, and why more text isn't better

SPEAKER
Nixon Dinh, Director of Product, Agentic Commerce, PayPal

LINKS
PayPal Agentic Commerce Services: https://developer.paypal.com/agentic-commerce-services/about
Agentic commerce docs: https://docs.paypal.ai/growth/agentic-commerce/overview

CHAPTERS
0:00 Intro
0:12 Agentic commerce at PayPal
0:52 How commerce evolves
2:16 From the search era
3:01 To the intent era
3:51 Then the delegation era
4:31 Why this matters now
5:21 The market opportunity
6:01 What merchants are seeing
6:51 What changes for merchants
7:40 Catalogs weren't built for agents
8:20 Models are a black box
8:55 Running experiments
9:20 Keyword vs semantic search
11:10 Enrichment patterns
12:05 Example: enriching a running shoe
13:20 Results: does enrichment help?
13:54 Content quality beats more text
14:29 Key learnings
15:14 Takeaways

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,428 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=1s)** [music] Hi everyone. Um, welcome. I I'm Nixon Den. I'm the director of product for Aenticcommerce at PayPal. And what that really means is I lead a lot of our efforts on how AI agents are reshaping shopping and payments. Um, and you know, most of my career has been on commerce and payments. And right now, I'm really excited about helping merchants navigate this shift uh towards like agent-driven commerce. And specifically, what we're going to talk about today is um the catalog piece and it being agentic ready and sharing some of our learnings on this on this journey. So I think it's very important we just

**[0:52](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=52s)** kind of level set a little bit when we look at the evolution of commerce. We've seen it transform from you install brick and mortar transactions to the advent of e-commerce where this started off quite linear. Um a user would simply search and buy from e-commerce sites and then through like internet 2.0 O we've seen that transform further into more complex uh channels that involve email, SMS and like now social commerce for us like we see AI as the next evolution in that journey and with any evolution we know two things to be true. The first like all change it can seem like a threat to a business. Um but on the flip side of that can also be seen as a big opportunity. And the second thing that we know is that whenever we have seen consumer

**[1:41](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=101s)** behavior change because of a new technology, commerce tends to evolve alongside with it. And so we are starting to see that now with Aentic where not only is the new this is a new channel that's enabling uh merchants to engage with customers in a very deeply personalized way, but also how customers are searching and finding products is changing. And uh now is really the time that merchants are starting to look to invest on how to to change with with their customers and and uh succeed in the agentic era. So earlier I touched on how the consumer behavior is starting to change. Um but I just want to dive deeper a little bit on

**[2:28](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=148s)** this. So we, you know, when we first uh when we think about consumer shopping, that behavior up to today has been now what we're calling the search era. Um it goes through a phase where like it's keywords, you're navigating a catalog, there's SEO strategies, and this is what most businesses have optimized towards over the last decade. And while for many businesses this worked, this model put the burden on the shopper to really find what they needed. Um, now what we're seeing is that we're moving into this phase called the intent error. So instead of typing keywords like I want school supplies, um, I might say something like, you know, my daughter's starting school in September in fifth grade and I need uh to to shop

**[3:16](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=196s)** back to school. And that's a very completely different interaction. Um, so you're now expressing your needs in your own words and AI is now asked to meet you where you are. And so the brands are coming to you instead of you having to go find them. And that's a very very different interaction model. Um, and most businesses now are starting to find that they need to set themselves up for this interaction model. Um so what we believe will happen next is after we go through the intent error what will have to happen is customers need to start trusting the recommendations that they're getting from the from the agents and once that trust starts to build we do start to

**[4:05](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=245s)** believe that they will start delegating more and more actions to their agents and that's also where as PayPal we're building towards is um continue to build on that trust and moving to a world where humans start to delegate more and more of their task in commerce and shopping to their agents. So although we talk about this delegation era and we think it sounds like it's so far into the future, you might be asking like why this matters now. And so we have couple pretty big data points that we want to share to really underscore why this matters. The first is uh through a study at Bay & Co. um they project that by 2030 15 to 25% of all commerce will be executed by an agent and furthermore within a decade

**[4:55](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=295s)** agents are predicted to outnumber humans online and so these numbers don't just indicate that this is like not meaningful now it is a very marginal shift that businesses can't ignore and that this is a very structural transformation happening entire entire e-commerce ecosystem So to go further I think it's very good to understand why PayPal feels like we are bullish on this opportunity. Um as a industry we expect uh to be some very tangible opportunities coming forward. We expect 1.1 trillion dollars of uh commerce to happen uh in US retail to be agentic and then we expect that to

**[5:44](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=344s)** be 3 to 5 trillion globally and what we've have seen is that there are over two billion users um projected to use like AI to start their shopping journey over the next few years. And so when we think through this, what does this actually mean for businesses and merchants? When we talk to our customers and what we talk to our partners, what we've seen is six they what they've reported is that over 693% uh referral traffic from AI engines. And when we did consumer studies, we found that 39% of US shoppers are already using AI for shopping today. Um, and I'm sure many of you have probably defaulted to that pattern today. And what we have found also is that when you

**[6:32](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=392s)** do start and interact with an agent first, businesses have tend to see up to four times higher conversion on a completion of an order because now they can get more rich and in-depth data on a product. And so with that all happening and the traffic moving, we want to break this down further onto like what this really means ac deeper for merchants. In the search era, this was very like SEO based and you might optimize for like a sum dress. In the intent era, you have to think through how do I be discoverable for where an agent is representing my my business. And then in

**[7:21](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=441s)** the delegation era, we need to think through uh how I can convert that demand safely and trusted in a trusted way. And so the challenge becomes to think through is like as COVID moves to AI agents, how do you as a business be visible where the consumers interact? The issue with this is that cataloges weren't really built for agents. Um most merchants today maybe advertise on Google. Um they have a catalog they syndicate to there or maybe to Meta or Facebook or other advertising platforms. But the spec wasn't built for agents. And so agents now um you know if you it's not optimized for agents to

**[8:08](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=488s)** discover products. Um it's not as readable for agents as well. And they're really just built for humans search. And then to compound that even more, the models that agents use are still for the most part a black box. Agents can use different varying models to make their decisions. Um, different models use different ranking and recommendations and and and uh algorithms to to determine their recommendation. Uh, vector database retrieval is also not always deterministic. And because of all of this, how do you decide as a business what model do you do to you optimize for? In the old SEO world, there was a clear strategy. In this new world, the strategies are still remain largely unclear.

**[8:58](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=538s)** And so what do you do when you don't know? You run experiments. And so we we ran some experiments. We enriched uh some of our merchant product data. And we ran experiments to see how agents uh uh searched uh and and recommended products. And before I get into the experiments that we ran, um I think very good to level set with everyone how like the differences between keyword and semantic search and it it trickles through to the themes I talked through earlier with keyword search being you know very matching the the search that the user is entering in. So, in a classic search, it might match literal words. Um, for example, I'm searching for blue running shoes, and you only get results that

**[9:46](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=586s)** contain those words. The good part about this, it's very precise, it's fast, it's predictable. But the downside is it misses intent. And so, if you ever search footwear for jogging, it may not even return those shoes. Uh, and that's only simply because the words don't match. Whereas with semantic search, it matches based off meaning. Um, what it does is it converts the query into vectors that create uh meanings of intent. And so you might type something, oh, I'm searching for something comfortable for marathon training. And you might find your running shoes even though none of those words exist in the search query. Um so the good part about the that is it broadens and how it can search but the

**[10:35](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=635s)** downside is if you inject too much meaning it can lose focus and hallucinate. So there is a balance of how much you want to enrich and how much you want to inject into your enrichment. So to sum it up keyword search is quite precise. It's it's very literal. Semantic search is just it's smart but it's very fuzzy. And realistically, the real answer isn't an either or. It's it's combining both, which is exactly what our hybrid approach does. Um, and that's kind of where we're headed next. So, now that we understand what semantic search is, it's important to highlight that there is no singular way to really enrich product data for semantic search. I think it's really important for you as a business to understand the kind kind of catalog data you already have.

**[11:25](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=685s)** um do you have a thin catalog? Do you have a catalog of products that are more spec heavy? Depending on where your business is today, you should think through what you might want to enrich. And so for the experiment though, we thought through different patterns of enrichment. Um and I won't go through all of them in detail, but things around like filling attributes, making sure there's description depth, um make sure there's buyer context and trust signals, and even some product identity. I think the main take away from this slide is that enrichment isn't one sizefits-all. The right approach really depends on the catalog you're starting with and that's the framing we'll build on next. And so here's just an example of enrichment in action for us. Um example on we're starting with we have

**[12:12](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=732s)** men's uh men's shoe model 8543 that's blue and then the description will be I have blue running shoes. um available multiple sizes. there's an attribute that's blue keyword matches maybe blue running or shoe and then um the semant for semantic there's you know very little context for that when you enrich there now we might have the title as a men's lightweight running shoe um the description is now more enriched like it's cushion it's breathable uh there are further attributes we've pumped into that as well so there's like true to size it's it's the the material is mesh um we also put in some reviews here as well so enrich that with some review data and now what the search sees is um it matches running, it matches training, it matches meshes. There's a lot more

**[12:59](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=779s)** that it matches. So with semantic there's a lot of rich meaning that's put there uh to kind of enhance the search. And so here the the some of the examples we use was attribute filling or bio context or even uh the trust signals around the reviews as well. And so ultimately at the end of the experiment um you know our thesis was generally speaking does enrichment help boost uh recommendations and at its core yes it does. Um what we saw was an unenriched baseline like when it went headto-head um it just completely underperformed. We found that merchants with the thinnest cataloges tend to gain the most. Uh merchants with weak product data also had the most room

**[13:48](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=828s)** to improve. Um but I think what we needed to also understand is that it's all about content quality that drives the results and it's not the schema that actually and actually piling on you unstructured data can actually dilute the signal as well. And so what do we mean by like unstructured data? like we just don't want to stuff the the context of anything any words we want. We don't want to put any boilerplate messaging around um potential like you know welcome to our store. We're familyowned business. Those things are irrelevant to an agent at times. And so how you enrich what you structure into the data really really matters as well. And so just generally speaking a sum up of our

**[14:35](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=875s)** learnings was enrichment helps keyword search. Semantic retrieval requires a very different set of data structures. But there is a balance to how much you want to enrich uh to improve semantic retrieval. And while this was only one set of experiments, we did find that enriching just yeah head-to-head always improved recommendations. Um what we had found in some cases when we overenriched the agent tended to hallucinate more and it underperformed. Um and we don't have a concrete recommendation for every business but a good place to start is just assess your catalog and then figure out the right strategy for that. Um and so just to wrap up you know enrichment works assess your catalog structure and more text isn't better. um

**[15:24](https://www.youtube.com/watch?v=YXb2Wx1r_Pk&t=924s)** structured quality content, structured quality content is the one thing that wins out and AI will reward content quality and not brands. Um but it does optimize for other trust signals as well. So thank you everyone. Uh if you want to learn more about PayPal's Agent Commerce Services, please visit our booth at P11.
