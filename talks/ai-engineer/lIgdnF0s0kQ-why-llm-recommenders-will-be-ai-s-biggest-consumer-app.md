---
id: lIgdnF0s0kQ
title: "Why LLM Recommenders Will Be AI's Biggest Consumer App — Devansh Tandon, Meta"
slug: why-llm-recommenders-will-be-ai-s-biggest-consumer-app
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Devansh Tandon"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-09-25T14:00:27Z
video_id: lIgdnF0s0kQ
url: https://www.youtube.com/watch?v=lIgdnF0s0kQ
youtube_url: https://www.youtube.com/watch?v=lIgdnF0s0kQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "LLM recommender systems", "recsys", "recommendation systems", "generative recommendation", "semantic IDs", "generative retrieval", "scaling laws", "Devansh Tandon", "Meta", "Instagram Reels", "Instagram algorithm", "LLM ranking", "steerable recommendations", "consumer AI", "personalization", "AI Engineer", "AI Engineer World's Fair"]
topics: ["Classic ML & data science", "RAG, retrieval & knowledge", "Training, fine-tuning & model building"]
transcript: true
---

# Why LLM Recommenders Will Be AI's Biggest Consumer App — Devansh Tandon, Meta

**Devansh Tandon**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#LLM recommender systems` `#recsys` `#recommendation systems` `#generative recommendation` `#semantic IDs` `#generative retrieval` `#scaling laws` `#Devansh Tandon` `#Meta` `#Instagram Reels` `#Instagram algorithm` `#LLM ranking` `#steerable recommendations` `#consumer AI` `#personalization` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=lIgdnF0s0kQ) · [Conference site](https://www.ai.engineer/)

## Description

Four of the 10 most-used apps in the world are content feeds, and for an hour of engagement they can be up to 100x cheaper to run than AI chat apps. The reason is that a feed decodes pointers to existing content instead of generating every token itself. Devansh Tandon, who leads Meta Recommendations Research, argues that recommendation systems scale just like LLMs, that the field is still early on that curve, and that the LLM recommender will become one of the biggest consumer applications of AI.

Tandon lays out four S-curves the industry is climbing: traditional recsys, LLM-inspired, LLM-native and agentic. He then walks through the recipe for building an LLM recommender. First, tokenize content with semantic IDs, which turns a three-minute Reel from about 10,000 tokens into about 10. Next, make the model bilingual in English and your catalog. Then post-train it to rank, with chain-of-thought reasoning you can read. He also shows how this makes feeds steerable, like Instagram's Your Algorithm, where you can see and edit what the algorithm thinks you like.

Speaker info:
X/Twitter: @devanshtandon_ (https://x.com/devanshtandon_)

Related links:
Meta AI: https://ai.meta.com

Timestamps:
0:00 Intro: two big arguments
0:45 About Devansh
1:30 Semantic IDs and generative retrieval go mainstream
2:15 Scaling laws, from LLMs to recommenders
3:45 Real scaling curves at Meta
4:15 Instagram Reels: 30% more watch time
4:55 The tokens in, engagement out flywheel
5:40 Four S-curves of recommendation
6:35 LLM-native recommenders
6:50 Agentic recommenders
8:05 The three-step recipe for an LLM recommender
8:35 The five-layer cake
9:35 Semantic IDs: a Reel in 10 tokens
10:45 Pre-training on English and semantic IDs
11:25 Post-training: an LLM re-ranker with chain of thought
12:25 Steerable feeds: talking to your Instagram algorithm
13:15 Explaining recommendations
13:50 Prompted playlists, custom feeds and Ask DoorDash
14:05 Feeds vs. chat apps: the same flywheel
14:50 Why feeds are 100x cheaper per hour of engagement
16:25 Why LLM recsys is AI's biggest consumer app
17:40 Wrap-up

## Transcript

*2,676 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=1s)** [music] Welcome everyone. Thank you for coming out to the LM Rexus track. Um I'll be sharing the first talk. Uh my talk is titled tokens and engagement out training LM recommenders. Um, and I want to make two big arguments today. The first is that recommendation systems scale just like LMS do and that the field is very early in that scaling curve. Um, and the second is that the LM recommener is going to be one of the biggest consumer applications of AI. Um, okay. So, quickly about me. Uh, I

**[0:50](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=50s)** currently work at Meta on research and product. Uh I lead a team called Meta Recommendations Research uh which is this group that's training frontier models, LLMs and recommenders that power Instagram, Facebook ads, the meta family of apps. Uh before this I was at Google for a long time uh working on a lot of the key ML teams including deep mind and YouTube. Last year I gave a talk at AI engineer called teaching Gemini to speak YouTube about two ideas semantic IDs and generative retrieval which we also wrote two papers about which I've linked here. Um it was really fun and it led to a lot of discussions and collaborations. Uh the ideas behind semantic ID and generative retrieval have really taken off in the industry over the last year.

**[1:38](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=98s)** Um and they've moved from more research to now scaled production systems. And I've seen exciting launches and papers from YouTube, Meta, Spotify, Door Dash across the industry. And we have a couple of examples of that later today. This year I want to talk about four uh sections. Recommendation scaling curves, a framework of four, recommendation paradigm scurves that we are climbing as an industry. um sharing the recommener recipe and finally this consumer AI app framework. Um let's start with scaling curves. So I wanted to start with this landmark scaling curve paper from 2020 which feels like a lifetime ago. This is when Daario was still at OpenAI and Anthropic

**[2:26](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=146s)** didn't exist yet. But the core idea that this paper shared is the power law of scaling. As you increase model size, data, the amount of compute flops trained uh for model training, the loss falls on this log linear scale. And this clean and predictable curve is what really set off the race for the AI frontier because you can forecast what model quality and capability improvements will look like. And this is what's underwriting the massive capex investments and the AI buildout today. It turns out that recommendation systems follow a very similar scaling law. In fact, before this wave of LLMs, Rexs were the largest production ML models in big tech companies. And they're still some of the largest models that are

**[3:13](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=193s)** served at a scale of a billion plus daily active users. And they follow this similar power loss scaling curve. On the x-axis, you have data, compute, and model size. And on the Y ais you would see falling loss or in this chart uh an improvement in recommendation quality. In offline evals it's net entropy or AU gains and then when it's translated to a real production launch it's engagement impact revenue impact at some of the biggest consumer app scale. Here's a real example from Meta that demonstrates these power loss scaling curves. uh there's a paper the first is a paper HSTU from 2024 and the second is a followup from this year both

**[4:01](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=241s)** demonstrate that as we scale model size compute and data we see this clear improvement in offline eval of recommendation quality scaling curves aren't just academic research they're driving real product impact at scale for some of the biggest consumer businesses in the world here's a couple of examples I have from Meta's recent earnings reports. Um, Instagram reels had a strong quarter, 30% year-on-year watch time. And, uh, the optimizations we made to improve the quality of recommendations included simplifying our ranking architecture to enable efficient model scaling and longer interaction histories to identify a person's interests. uh we doubled the length of user interaction sequences used for training

**[4:48](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=288s)** Instagram and increased the richness of each user interaction. So these are direct parallels to the power loss scaling curves for LLMs. And I want to introduce this idea of a flywheel of tokens in engagement out which is what's powering all of these Rex model scaling. You train a model. You then run inference on it which is the tokens in that recommendation model results in better content recommendations. It drives consumer engagement, daily active users time spent. It translates to monetization and ads or subscription which pays for the next model training run. And so every step on the scaling curve is one loop around this flywheel. And a lot of consumer apps are spinning this core

**[5:35](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=335s)** flywheel at the heart of their business. So we have a long way to scale these recommener systems. I want to talk about the four paradigms that I see the industry progressing through. The first scurve was more traditional Rexus where this scurve focused more on feature engineering and user and content embeddings. Most production systems are still sitting on this curve. they're running some type of two tower sparse network rankers scaling the embedding models. I don't think this curve is going to go away but model development here will be accelerated with auto research and things like feature engineering will be handled by agents uh rather than real ML engineers. The next curve is kind of LM inspired models where you are scaling models ideally end to end. HSTU and one wreck papers are

**[6:25](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=385s)** examples in this paradigm. I think this is where the leading recommener systems in the industry are largely operating today. I think the next scurve will be this paradigm of LLM native where you adapt a base model that understands and can reason uh and adapt it for recommendation tasks. The tiger and plum papers are some examples of this paradigm. And I think the final paradigm that I start to see emerging is agentic where LLMs will start to orchestrate Rex systems in a loop. I think there's a parallel here with coding agents. So the LM native models are like improving the core capabilities of the model going from opus 45 to 48 versus the agentic curve will be like improving the coding harness behind claw code or codeex. Um

**[7:14](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=434s)** and so instead of just having a single forward pass through the recommener, you can imagine a loop where agents plan, retrieve, rank and then critique the recommendations. They can refine them by calling models again and finally deliver the recommendations. This I think is an interesting area of research. Now let me jump into so here here's kind of the framework of all the four Rex paradigms. I think companies are scaling across each of these curves in parallel. Most of recommendations I think lives in LM inspired today and is trying to graduate into LM native. Uh but then a lot of companies are still using traditional models uh and climbing that scurve. Let me shift gears a bit to share the

**[8:05](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=485s)** recipe of how to actually build a LLM recommener. I think it's pretty simple. It's three steps. Uh you start with tokenizing your content and creating a language for your domain. Then you want to adapt the LLM so that it understands both English and your domain language and becomes this bilingual model. Finally, you can prompt this model with user information and it will directly decode recommendations from your content corpus. Let's go a bit deeper. This is the LLM recommener as a five layer cake. Um, we'll start at the bottom. Uh, that's semantic ID where you're converting your content corpus into tokens that the LLM can understand and reason over. Then you have kind of the base LLM foundation

**[8:54](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=534s)** model. This can be an open weights model or an internal first party model. Then the core training stages. Pre-training is around bridging English and these recommener tokens. Post-raining is about steering the model towards recommendation tasks like predicting engagement or reasoning over recommendations. And then finally, you can just do some light surface specific fine-tuning to deploy it on a product surface. The exciting thing about this paradigm is most of the compute is shared across all of the product surfaces. So you don't have to train individual models from scratch for every product surface. I'll go a bit deeper into each stage for semantic ids. I think this has seen incredible adoption. A lot of teams are

**[9:42](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=582s)** just replacing their hash ID with the SID in traditional models and seeing good impact. I think there's two big reasons to tokenize content. The first is it gives you the stable representation for models to learn over rather than a constantly shifting hash that the model can only memorize. And the second is compression. You want to be reasoning over these long sequences of user interactions. And if you don't compress the content, for example, a threeminut Instagram real video would be 10,000 tokens and it will just fill up the content context window too quickly. So you have to to compress it into about 10 tokens. And so here I have some examples of Instagram reels about tennis. You can see that the semantic token shares the prefix of the first three tokens because they're very

**[10:30](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=630s)** similar reels. You can imagine the first token representing sports um and the second two tokens representing tennis and then the final token making these videos individual. Once you have a semantic ID, you can train it to understand both English and semantic ID. And so the task I have on the left for pre-training here is an example of where you prompt with a video with semantic ID ABC has the description blank and the output is a shot that was instantly iconic from Wimbledon. Here you're teaching the model to connect these semantic tokens with synthetic English natural language text. The example on the right is about reasoning over sequences of semantic IDs. And so in a user's interaction history, you can

**[11:17](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=677s)** mask some parts of the sequence and the model learns to predict them and understand what videos are watched together in sequence. Here I have an example of post training where we're teaching the model how to rerank content. So the input is a bunch of user information and 30 candidate videos that are then ranked to be the top five recommendations from this LLM ranker. What's really interesting here is that you can see the chain of thought reasoning of this model. And because this model knows both English and recommendations, you can simply just inspect the model and understand why it made the decisions that it did. In this example, the model understands the user's topic interests like comedy, food, DIY, wellness. It understands the

**[12:06](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=726s)** engagement style and what creators this user has an affinity towards. and then it reranks the content based on this chain of thought reasoning. I think this is super exciting because once you have a model that can understand both English and recommendations, it opens up new product surfaces and new experiences where users can steer their feed. Here's an example from your algorithm on Instagram where users can talk to the algorithm while they're consuming content. It's a screenshot from scrolling through reels or when you click in you can understand what the Instagram algorithm thinks about you and your interests and then you can add or remove interest and talk to it in natural language. And so we're

**[12:54](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=774s)** going to see this shift I think from blackbox recommendations algorithms to giving users more control over their algorithm and algorithms becoming more interactive and steerable. I'm really excited that users can direct it towards their own goals that's expressed in language rather than just likes or comments. Um, and I think this can this foundation model can also start to explain its recommendations. And so for this example, I've added an interest that I want to follow the FIFA World Cup at this time. And the model would get both my user history and this new input and then be able to decode recommendations that are personalized to me like this free cake that Messi scored recently.

**[13:44](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=824s)** I think these interactive recommenders are going to be a really interesting new product surface and we're seeing this across the industry. We have some examples of prompted playlists from Spotify, custom feeds from YouTube, Ask Door Dash, and we'll be hearing more from speakers about these. Um, finally, I want to talk about kind of the framework of tokens in engagement out this flywheel that I started with um of model training, inference, consumer engagement, and then monetization. This is actually the same flywheel that's shared by content feeds and the AI chat apps. And this is a lens that you can use to evaluate any consumer app. What'll make an app successful on

**[14:32](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=872s)** the training ROI side is how well can it translate compute into a frontier model. On the inference side, how well can the inference tokens translate into engagement and then monetization. And so if you try to compare content feeds and AI chat apps, I think that LM recommenders are actually structurally more token efficient than the AI chat. So on the left you have content feeds like Instagram, Facebook, Tik Tok and YouTube. On the right you have the big AI chat apps like Gemini, ChatGpt and Claude. Content feeds are currently using models that are around 1 to 10 billion active parameters. The chat apps are serving much larger models 10 to 100 billion active parameters. Um the output for the content feed is a semantic ID token

**[15:22](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=922s)** which is a pointer or an address to existing content because the content supplied on these content feeds is uploaded by creators. There's a very healthy creator economy and so the supply of content is effectively free or it's uploaded by creators. For the AI chat apps, they have to decode every token of content themselves and the amount of tokens output in every turn of an LM chat interaction is a few thousand tokens. Uh, and the the big difference here is that every token has to be manufactured by the app at inference time. And so what that means is if you compare these two apps on how much inference cost and compute is spent to generate an hour of consumer engagement,

**[16:10](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=970s)** there's a huge structural gap where content feeds are significantly cheaper up to 100 times or more cheaper than AI chat apps because they're decoding pointers to content rather than content itself. Um, finally I want to kind of end with why I think LM Rexus is one of the most significant consumer AI applications. If you look at the top apps by daily active users, these are the top 10 apps. Four out of 10 of them are content feeds. And so this is a really significant consumer uh application. If you look at the content feeds, almost all of the consumer app growth on both the engagement and monetization side is driven by the recommener and ads models. And these are going to be entirely

**[16:59](https://www.youtube.com/watch?v=lIgdnF0s0kQ&t=1019s)** transformed by LLM recommenders. It's a very large and very token efficient application of AI for consumer apps. We're going to see a lot of new product experiences come through with steerable and interactive recommendations, explanation of recommendations, and just putting more users in control of their experience on these apps. I think we're going to see some really exciting research on consumer agents and recommendation agents that come out over the next year or so. Um and so this is why I think this is a super exciting area of both research and product uh at this intersection of LLM and recommendations. That's all. Thank you so much.
