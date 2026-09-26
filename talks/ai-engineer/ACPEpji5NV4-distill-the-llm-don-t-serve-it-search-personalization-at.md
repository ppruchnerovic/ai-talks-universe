---
id: ACPEpji5NV4
title: "Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash"
slug: distill-the-llm-don-t-serve-it-search-personalization-at
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Raghav Saboo"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-09-25T13:30:37Z
video_id: ACPEpji5NV4
url: https://www.youtube.com/watch?v=ACPEpji5NV4
youtube_url: https://www.youtube.com/watch?v=ACPEpji5NV4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "DoorDash", "search and personalization", "LLM recommender systems", "recsys", "semantic IDs", "LLM distillation", "relevance labeling", "LLM as a judge", "e-commerce search", "retrieval and ranking", "consumer memory", "personalization", "query reformulation", "Ask DoorDash", "Raghav Saboo", "AI Engineer", "AI Engineer World's Fair"]
topics: ["Science, healthcare & applied ML", "Training, fine-tuning & model building"]
transcript: true
---

# Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash

**Raghav Saboo**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#DoorDash` `#search and personalization` `#LLM recommender systems` `#recsys` `#semantic IDs` `#LLM distillation` `#relevance labeling` `#LLM as a judge` `#e-commerce search` `#retrieval and ranking` `#consumer memory` `#personalization` `#query reformulation` `#Ask DoorDash` `#Raghav Saboo` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=ACPEpji5NV4) · [Conference site](https://www.ai.engineer/)

## Description

Search for gluten-free pasta and a ranker trained on engagement may show you regular spaghetti, because it sells well. Raghav Saboo, Staff ML Engineer and Tech Lead for Search & Personalization at DoorDash, argues that the real bottleneck in marketplace discovery is semantic understanding, not engagement. As DoorDash grows into grocery, retail, pets and gifting across billions of store-level items, it uses LLMs to understand what items mean and what shoppers actually intend.

His core pattern: do the expensive LLM reasoning once, offline, and then distill it into small, fast models for serving. He covers four building blocks. The first is LLM-generated relevance labels, which improved retrieval NDCG by 2.3%. The second is semantic IDs, a learned taxonomy of the catalog that raised ranking MRR by 4–5% and powers query reformulation. The third is consumer memory at three timescales, stored as text, vectors and a graph. The fourth is steerable, LLM-generated personalized collections, which lifted order rate by nearly 1% in the pets category.

Speaker info:
Substack: https://buildshipai.substack.com/

Timestamps:
0:00 Intro
0:47 Discovery's real bottleneck is semantic understanding
1:42 Beyond restaurants: broad shopping missions
2:52 The four primitives
3:17 Primitive 1: LLM supervision
3:27 Why engagement ranks the wrong pasta
4:11 Human labels vs. behavioral signals
4:46 Building a golden labeled dataset
5:46 A fine-tuned LLM labeler for the whole catalog
6:11 Reason offline, serve cheaply
6:21 Two-stage contrastive retrieval
8:00 Adding a relevance tower to rankers
9:00 Distill, don't replace
9:30 Primitive 2: catalog semantics with semantic IDs
11:00 A learned taxonomy
11:50 Cross-category, cold start and tail coverage
12:55 Results: 4–5% MRR gains in ranking
13:20 Query reformulation
14:05 Primitive 3: consumer memory
15:15 Three timescales of memory
15:55 Memory blocks: text, vectors and graphs
17:04 Context graphs
17:55 Where memory shows up
18:20 Primitive 4: steerable content generation
19:05 Personalized collections on store pages
20:33 Results in the pets category
20:48 Three takeaways

## Transcript

*3,038 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=ACPEpji5NV4&t=12s)** Thank you everyone for coming to this talk and Devanch for organizing this. Uh I'm Ragav. I'm a staff uh machine learning engineer at Door Dash. I work on search and personalization and uh today I'm going to talk about uh the ways that we're integrating LLMs for you know our marketplace discovery uh specifically in four pieces and um how these primitives are kind of uh uh working towards our integration of LLMs into traditional uh Rexus as well. So I'll start off uh today uh with a simple claim. Uh the claim is that to build effective discovery in this case for a marketplace like Door Dash the real bottleneck is semantic understanding. So that is knowing what you know actually

**[1:05](https://www.youtube.com/watch?v=ACPEpji5NV4&t=65s)** what items mean uh for users given some context and what a shopper actually intends to do on you know an app like Door Dash. And historically we have treated these uh as engagement optimization problems. Um however LLMs give us a genuinely new lever to extend this. So this talk is about uh you know the four primitives that have allowed us to start leveraging LLMs for problems at Door Dash. As you may know Door Dash is now grown uh well beyond restaurants. So we're in grocery, retail, pets, gifting and more. And our goal is to capture every shoppable moment. Uh and we know that

**[1:56](https://www.youtube.com/watch?v=ACPEpji5NV4&t=116s)** across these verticals, the users frequently have very broad shopping missions, right? So for example, a consumer may say when they come to our app is, you know, I just adopted a puppy. What do I need to get started this week? And this consumer start may start on like searching for puppy food because they just adopted the puppy. That one query could unfold into further query reformulations. Um they land on collections for you know other shopping needs, complimentary items such as crates, leashes, uh training pads all the way to checkout. And this could happen over multiple sessions, mult multiple days, right? And capturing that whole arc is pretty hard

**[2:46](https://www.youtube.com/watch?v=ACPEpji5NV4&t=166s)** because it spans multiple models. Um, and this is where the four primitives I will cover come in. Specifically supervision catalog semantics, semantic personalization, and steerable content generation. As we heard previously as well, it's a system of shared representations that help us map this customer's journey uh with the use of LLMs. Now, with supervision, the question we're asking or looking to address is how do we teach our retrieval and ranking systems what good means for different tasks? And here's a simple example, right? A shopper searches for gluten-free pasta. And if we only rank from engagement, very popular regular spaghettes might show up and because it

**[3:36](https://www.youtube.com/watch?v=ACPEpji5NV4&t=216s)** sells well, you know, it may continue to show up. Even gluten-free white bread might be retrieved and, you know, show up because it overlaps with gluten-free. But neither of these are clearly the right answer. What we actually want is graded relevance. A true, you know, gluten-free pasta should be a high relevance item. Chickpea pasta might be a reasonable substitute and regular spaghetti while it's popular it fails the constraint that the user has. Now to solve this there are obviously two sources of truth. We could look at human annotation but that's expensive slow and becomes quickly stale because our catalog changes quite rapidly. Second is behavioral signals. They're

**[4:23](https://www.youtube.com/watch?v=ACPEpji5NV4&t=263s)** abundant but obviously as I mentioned biased by exposure, position, price, promotions and you know previous model choices. So the missing signal is a scalable reasoning signal. This is where LLMs are very useful as they offer a way to produce that supervision for such tasks. So in our case, you know, the PIP pipeline starts with human ground truths. uh we build a high quality seed set of example query item pairs and on a three three uh level relevant scale 012. We audit the suspicious cases. For example, if a human label says you know that an item is irrelevant but that item performs very well on add to cart or conversions, we send that case to a

**[5:12](https://www.youtube.com/watch?v=ACPEpji5NV4&t=312s)** stronger LLM uh to re-evaluate with more granular prompts. We also reconcile with other models. You know, for example, our query to taxonomy or category models. And if a query, you know, query maps to a set of valid categories and the items belong to those valid categories, we may adjust the label accordingly. And through this process, we're able to achieve a pretty high precision golden data set that we then fine-tune a lightweight LLM, let's say, for example, a GPD 40 mini on top of it. And that's when it, you know, really pays off. We are able to use that fine-tuned labeler offline across, you know, our full catalog to generate uh full graded query item pairs. And those labels become one shared target for both

**[6:02](https://www.youtube.com/watch?v=ACPEpji5NV4&t=362s)** retrieval and ranking systems. This pattern has been pretty important for us over the past uh few years. um use you know expensive reasoning once offline then distill it into models that can you know be served cheaply and quickly. Now let's take retrieval first. The challenge is you know standard embeddings um at e-commerce scale quickly collapse the relevance uh distinction. items that are merely related sit close to items that actually match and the model uh may know two items are related but not be able to separate uh exact matches, substitutes, compliments. So our fix is a two-stage contrastive method um trained on uh the same graded

**[6:51](https://www.youtube.com/watch?v=ACPEpji5NV4&t=411s)** labels. Stage one, which we call mining, does a global geometry shaping. We use two tower encoders uh with multi-level supervised contrastive loss. Um after that we use that base model to mine harder negatives and uh these are items that the model confuses hard negatives that are ranked too high or strong positives ranked too low. And the second stage after that is where we really put the model through curriculum training. uh use those hard negatives, relabel them and our uh you know relevance of the retrieval layer improves sharply after that. So after stage one we see overlaps between you know relevant and uh moderately relevant but after stage

**[7:40](https://www.youtube.com/watch?v=ACPEpji5NV4&t=460s)** two there is a significant difference and this has been one of like our biggest uh levers in retrieval improvement uh across the board. um you know we've improved NDCG of relevance by 2.3%. And uh that's also been true with our downstream business metrics and we did the same with uh uh exercise with our ranking models as well distilling LM reason labels into our rankers. However, combining this with uh business and engagement objectives. Here we add a new tower uh in this case an ordinal uh relevance tower on top of the LLM graded labels and uh this prediction sits right alongside existing engagement towers uh click add to cart

**[8:30](https://www.youtube.com/watch?v=ACPEpji5NV4&t=510s)** and conversion and since they share the same uh bottom layers the semantic fit and relevance fit gets distilled in the same backward pass and uh our model is able to predict uh you know probability of relevance across the different levels and we are able to blend uh through a value function on on top of this that allows us to uh fine-tune between engagement and relevance for different surfaces. Now these two examples are part of a larger theme of our work across similar projects uh where it seems right. We're not replacing the retrieval and ranking system with an LLM, but rather distilling the uh reasoning and understanding into some production ranking architecture. And this allows us to kind of quickly test and also

**[9:20](https://www.youtube.com/watch?v=ACPEpji5NV4&t=560s)** scalably improve our models uh with LLMs while keeping uh you know the business and system objectives uh of these surfaces in mind. So once we have supervision, the next question is how do we represent a very large and constantly changing catalog uh in a way that every model be it language models or uh you know traditional retrieval and ranking models uh that they can understand and at you know Door Dash's scale uh you can imagine we're kind of surfacing items across stores across internationally actually uh now and you know that's easily a few billion items at the store item level and for these items you obviously have unique skew ids but it says nothing semantically. So we also have a human

**[10:09](https://www.youtube.com/watch?v=ACPEpji5NV4&t=609s)** curated taxonomy that helps us classify and categorize these items into meaningful spaces. But often this is too coarse and too rigid. So for example something like hot sauces may just have like sauces hot sauces in the taxonomy uh but it doesn't tell you anything about the relationship between hoof or franks or tobasco. So that's where we've also adapted uh or adopted um semantic ids. Uh it's been introduced previously already. It's a backbone for a lot of our uh work uh now. And uh what it does is it gives us a you know a short hierarchical code that's analogous to our taxonomy but uh the ability to control the fine grain

**[10:59](https://www.youtube.com/watch?v=ACPEpji5NV4&t=659s)** nature of it. And the result of this learn taxonomy is that each item gets this hierarchical code and the prefix captures broad neighborhoods and you know the later tokens capture finer distinctions. So for example in the map over on on the slide you'll see hot sauces and the structure emerging from the data with zero labels. each one share the same first and second prefix in this uh ID sequence but then split by specialtity. So now you've got Mexican, Caribbean, Korean hot sauces uh being split up. And the important property is that this code that's learned is you know comparable by as I said by prefix but also usable by all of our downstream models

**[11:50](https://www.youtube.com/watch?v=ACPEpji5NV4&t=710s)** and that unlocks a few things for us. So the first is cross-category comparisons or relationships. You know chips, salsa, guacamole may live in different taxonomy branches but a shared semantic ID neighborhood can uh indicate that they belong together and maybe a shopping mission. Second cold start problems. uh oftentimes we get new catalog items added by stores and with techniques like engram and bite parent coding of these tokens we're able to scalably add these to our models as sparse ID features third tail coverage so sparse items uh and uh inherit a lot of signal from semantically related items and uh you know we don't have to wait for the volume or exposure uh to you um for to

**[12:40](https://www.youtube.com/watch?v=ACPEpji5NV4&t=760s)** consumers for these items. And then lastly, nice to have is the fact that we can actually also do a reverse audit. So we can audit our catalog and how well our human labels agree with the semantically learned labels. So a couple of examples of where we're using it today uh just to get give some real metrics. Um it has been one of our biggest improvements to our ranker. Um in in this case it's actually improved our uh ranker by uh improving MRR between four to 5% and that's translated to pretty big conversion uh wins as well. The second one that I'm particularly fond of is query reformulation. So again going back to the hot sauce example, Sriracha can lead to garlic chili garlic

**[13:29](https://www.youtube.com/watch?v=ACPEpji5NV4&t=809s)** sauce or sambell Ole and because these queries map onto like our catalog grounded semantic neighborhood uh that results in much more relevant queries that we're suggesting to users. Um ultimately if these are queries that we don't have inventory for on Door Dash, they're meaningless. And with the addition of semantic ids in this query graph, we were actually able to see pretty massive um MR gains as well uh for for this piece of work. So for now we've talked about you know item mapping and relevance and the next question is consumer context. What does the system know about the shopper and can that knowledge be reused across models again? And this is where uh our

**[14:19](https://www.youtube.com/watch?v=ACPEpji5NV4&t=859s)** third primitive comes in memory. So memory in the agent context is pretty well understood now. Um we apply the same concepts to uh our recommendation systems. So user embeddings are clearly very useful. uh we have many representations of our consumers but they don't necessarily get to uh why a consumer may have certain intents um and why they might have certain preferences. Additionally, LLMs cannot uh readily use these uh embeddings. You could tokenize and like uh train these models to learn it. But oftentimes having some explicit LM native counterpart is very useful and that's what we found. So the idea of memory is to represent uh the consumer

**[15:09](https://www.youtube.com/watch?v=ACPEpji5NV4&t=909s)** in multiple forms semantic in you know inspectable and reusable and uh the way we think about memory is uh in three time scales. So long-term memory captures durable preferences from orders searches browsing support interactions. Real-time context captures uh agentic inter interactions um oh sorry in session interactions so cart state active searches and then we have stated preferences which come from agentic interactions so something like ask door dash for example where consumers are able to explicitly state their constraints and preferences as well and the way we represent consumers in uh

**[15:57](https://www.youtube.com/watch?v=ACPEpji5NV4&t=957s)** in uh this long-term memory is through uh memory blocks. And these are structured in a way that allows uh us to add new dimensions of the user, you know, from dietary preferences to dining preferences to uh substitute pre uh preferences um as we learn more about the consumer and that is uh decoupled from like the downstream system that u that doesn't need to reinterpret uh this for their own use cases. So each consumer's memory is multi materialized in multiple forms. So first is text that's human readable. It's uh captures the consumer in a compact way. Second is are latent vectors embeddings of those memory blocks that can be fed into retrieval and ranking systems. And

**[16:45](https://www.youtube.com/watch?v=ACPEpji5NV4&t=1005s)** third are graph and tree or hierarchical approaches. So uh you know type relationships between consumers and brands taxonomies and memory uh revealed um preferences and these are assembled into you know composite memory objects that both ML models and LLM use downstream. So an example is you know this context graph uh where we connect consumers with extracted memory concepts and a graph needs fits neatly into shopping journeys because you know oftent times uh consumer item interactions are sparse and multihop. And in this case these context graphs are able to link consumers across memory concepts that we previously did not have uh relationships

**[17:34](https://www.youtube.com/watch?v=ACPEpji5NV4&t=1054s)** for. And it's particularly helpful uh at fine grain taxonomy levels. In our case, we're seeing uh for retrieval uh uh using uh graph uh based embeddings outperforming our uh existing taxonomy based embeddings. And today this memory framework shows up in three places. The first is personalized collections. I'll talk about that a bit later. Uh second is agentic personalization. So ask door dash for example uses this to personalize its sessions uh for you. And third in uh retrieval and ranking models as I said we encode these memory blocks and feed them as features in in downstream models as well. So the fourth primitive is steerable

**[18:24](https://www.youtube.com/watch?v=ACPEpji5NV4&t=1104s)** content generation. We heard quite a bit about it in the previous talk and this slide is my take on how we're p piecing all these uh primitives together. So all of these inputs, semantic ids, memory blocks um and graded relevance or um LLM supervision feed into multiple models you know be it LLMs or small language models or um uh you know traditional models and from these inputs we can generate different output shapes you know ranked semantic ID lists, carousel titles subcopies and these show up across different surfaces today on Gord Dash and A direct example of this is uh our um personalized collections on store pages. So historically collections on store

**[19:14](https://www.youtube.com/watch?v=ACPEpji5NV4&t=1154s)** pages uh on Door Dash have been a fixed library or attribute-based um and we've been able to kind of expand that through uh consumer level collection generation. And today this is an offline uh LLM process where we take in consumer memory semantic ids and syni syn synthesize uh collections um all the way from title subtitle to the actual items. And the important part is that control and steerability. We're able to react to occasions and moments um and build those collections as needed uh for different consumers at serving time. uh because this is all batch and uh generated offline through LLMs, we are able to

**[20:03](https://www.youtube.com/watch?v=ACPEpji5NV4&t=1203s)** still use our uh existing retrieval and ranking stack for item hydration, collection ranking, etc. And you know this is for example what a shopper actually sees, right? For a shopper with plant-based affinity, the system can generate plant-based pantry rows. For cat-only households, it can generate cat dry food rows. And if a session indicates that you know a person is going through pantry restocking it can bias towards pantry staples. And our early tests show that you know consumers are feeling the benefits of these tailored experiences. Uh an example is uh within our pets vertical we've been able to drive uh close to 1% uh order rate increases and 6% in uh active users. So to conclude uh there are three

**[20:51](https://www.youtube.com/watch?v=ACPEpji5NV4&t=1251s)** takeaways I would love for you to take away from this talk and how LLM fit into search and recommendations. First discovery is a semantic understanding problem. It's not only about engagement. LMS give us a way to reason about item meaning and shopper intent. Uh in in Door Dash's case for example. Second uh distill LM reasoning into primitives. capture you know reasoning uh offline as labels, semantic ids, memory and then let smaller and faster models serve it. The online LLM call is often not the product architecture you need. Third, shared representations create many use cases. Uh once you have these primitives, they can power, you know,

**[21:38](https://www.youtube.com/watch?v=ACPEpji5NV4&t=1298s)** retrieval, ranking, content generation, etc. So last but not least, thank you and thank you to all the collaborators at Door Dash who have helped ship a lot of these things as well.
