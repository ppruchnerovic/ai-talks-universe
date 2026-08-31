---
id: 4loPnxvWWhg
title: "Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End"
slug: your-fine-tuned-model-is-tech-debt-a-50x-roi-house-of-cards
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Dan Bjornn"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-08-20T16:00:22Z
video_id: 4loPnxvWWhg
youtube_url: https://www.youtube.com/watch?v=4loPnxvWWhg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End

**Dan Bjornn**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=4loPnxvWWhg) · [Conference site](https://www.ai.engineer/)

## Description

A customer replied good morning to an outreach text and the model called him immediately. Another confirmed a Thursday appointment, said sounds good, and was told a call was happening right now. Both reached production, from a finetuned classifier that had also generated $12 million of revenue at 50 times return inside a year. Dan Bjornn's talk is about what that model was quietly costing underneath those numbers, which he calls the calcification tax.

The repair loop is where it accrued. Gather examples of the new failure, synthesize more when there are too few, validate those by hand, sort them into intent buckets, review again, and only then train, which took about an hour and was the shortest step in a process that ran a week. Each round fixed its target and reintroduced something older, so bugs ended up ranked by how much customer pain was tolerable while they waited. The promised portability never arrived either, since training data does not transfer cleanly between model versions, let alone between providers, so they stayed put and could not adopt newer architectures while busy keeping the old one alive. The rebuild swapped the tuned model for skills, prompts, and context on a model agnostic framework. Fixes now ship in under an hour as files uploaded to a bucket, accuracy went up, cost per message went up, and total cost went down.

Speaker info:
- https://www.linkedin.com/in/dkbjornn

Timestamps:
0:00 - Classifying customer intent with retrieval
1:54 - Four reasons to finetune, all of them reasonable
3:32 - The pipeline, and $12 million at 50x return
4:24 - The confused confirmer, and the overeager puppy
6:04 - A week per retrain, with training the shortest step
8:39 - Ranking bugs by tolerable customer pain
9:31 - The calcification tax, in model and architecture
11:18 - The realization from changing skills, not models
12:14 - Rebuilding on skills, tools, and context
13:08 - Fixes in under an hour, deployed as files
14:54 - Cross your reason off the list before you finetune

## Transcript

*2,399 words · source: supa (en, exact timings)*

**[0:14](https://www.youtube.com/watch?v=4loPnxvWWhg&t=14s)** All right. Hello everybody. Thank you for coming. I'm Dan Bujorn. I'm a senior data scientist at Lease End. Lease End. We connect people who are coming to the end of their auto lease with financing uh options so that they can buy out their lease and keep their car. Now, as part of this uh we uh built a an LLM based application in late 2024 to help our customers connect with uh with our sales team. This application allowed them to send messages through text. uh they could ask questions about the sales process, they could schedule calls, uh they could get reminders, all of this stuff. Our first solution used a workflowbased approach uh built on top

**[1:04](https://www.youtube.com/watch?v=4loPnxvWWhg&t=64s)** of uh a rag system where we searched a vector database of messages that we had already seen and classified with the customer's intent. So for example, uh a message saying call me tomorrow would be classified as the customer wants to uh wants to talk later. A message saying I've got time now would be classified as uh the customer wants to talk right now. U this has worked but not super amazing. there's a lot of nuance in in messages and and conversation and this rags approach just couldn't quite pick up on that nuance and so we started to look for uh for new options to improve this and naturally being a data scientist my

**[1:54](https://www.youtube.com/watch?v=4loPnxvWWhg&t=114s)** first thought was hey let's start fine-tuning this seemed like a fun thing to do and I was sure that this was the right call um there's a few reasons for that first of all uh we needed better accuracy Our entire system uh was built upon us getting the user's intent correct. Did they want to talk now? Do they want to schedule a call? Do they want to opt out? All of this hinged on that decision. And so we needed to make sure that we got that first and foremost. Next, uh we could use smaller models with fine-tuning. And so this would lower the cost and also lower latency. So this was really important for us because we were uh responding to thousands of messages a day in real time and so it it uh would help us scale a

**[2:44](https://www.youtube.com/watch?v=4loPnxvWWhg&t=164s)** lot. Then next like I said we were classifying the intent of the user and so this was a very narrow structured task that we were trying to do and so it lent itself very nicely to supervised fine-tuning. uh we would bucket uh that conversation in one of six different categories and the model would learn the differences between those. Uh so seemed like a great option there. Lastly, uh I believe that this would help us have a little bit more control over our destiny with the the model providers. The idea was that we had the data and all we would need to do is pass that into a new model, go through the fine-tuning process and we could get similar results no matter uh what we decided to use. So

**[3:35](https://www.youtube.com/watch?v=4loPnxvWWhg&t=215s)** we could be model agnostic. So this was the approach that we took. Um, and I built a pipeline to collect examples, run LLM as judge, uh, classifications to label our data. I'd manually review that, create holdout sets, go through the fine-tuning process, check my metrics. This was a data scientist's dream. And, uh, the numbers sure helped. Within a year, this application had helped us bring in $12 million of revenue at a 50x ROI. Um, it was pretty awesome, but uh, the whole time it was quietly accumulating debt underneath that we didn't see. So, I want to show a couple examples of how

**[4:24](https://www.youtube.com/watch?v=4loPnxvWWhg&t=264s)** this application could get things wrong. Uh first of all uh the confused confirmer is a situation where um when customers set up an appointment with a sales rep, we send them a confirmation message to let them know that it's been scheduled and give them the details of that. Uh so a conversation may look like this. We reach out and say, "Hi Tracy, just confirming your lease and call with your advisor is set for Thursday at 2 p.m. We'll call you then." Tracy then sends us a message back saying, "Sounds good." And then our LLM responds with, "Great. I'm calling you right now. Uh, it's not what we want. We just confirmed a an appointment for a following day." And then all of a sudden, we start calling

**[5:13](https://www.youtube.com/watch?v=4loPnxvWWhg&t=313s)** them. This led to frustrated customers and some missed opportunities. The next one, um, I've come to lovingly call the overeager puppy. Um the the conversation looks like this. So first, hi James, this is Alex with Lease End reaching out about your upcoming lease maturity. James then says, hi, good morning. And good morning. I'm giving you a call. Um just like a puppy that gets so excited that somebody's giving it attention, our model decided to to give a call right there. Um, obviously this is not what James wanted. This actually did happen in production. Um, very embarrassing there. Uh, but this is a these are a

**[6:04](https://www.youtube.com/watch?v=4loPnxvWWhg&t=364s)** couple examples of of where it went wrong. And and don't get me wrong, the the app did well. The revenue numbers show that that it was working, but it could also mess up pretty spectacularly. Um the big issue wasn't how to fix it, but how to make it the fix manageable. The the fine-tuning process was pretty complex. Uh first we needed to gather examples of the problems that we started to see. Um then we needed to ask ourselves uh do we have enough examples for uh to go through fine-tuning? If not, we synthesized those examples. uh we passed it through an LLM, it created some some possible examples there. We'd have to

**[6:52](https://www.youtube.com/watch?v=4loPnxvWWhg&t=412s)** validate those, which was a very manual process uh because we wanted to make sure it had the best training data possible. And then once we had enough, uh we labeled those with the the categorization bins and we validated validated those through a manual review. Surprisingly, the fine-tuning process was the shortest part of all of this. uh normally took about an hour depending on the size of the data that we had but uh we never got it on the first iteration. Uh normally what happened was we would uh we would fine-tune and we'd evaluate this and uh we fix the problem that we were just trying to solve but then we caused regressions and other things. And so this turned into kind of a whack-a-mole process where we would

**[7:40](https://www.youtube.com/watch?v=4loPnxvWWhg&t=460s)** solve something new, but then other old issues kept popping up that we had to to whack down. Um, this whole process took about a week to gather the data, label everything, go through the fine-tuning process, and iterate and then deploy. So it was costly. Um, therefore, we needed to triage all of these issues that we ran into. We asked ourselves three questions before we did any any retraining. How frequent is the issue? Is it something that customers are seeing every day? Is it one off? Um, one big exception to this was if it was hurting the customer experience too much. So for example of this would be uh somebody repeatedly stating what their

**[8:29](https://www.youtube.com/watch?v=4loPnxvWWhg&t=509s)** uh their preference for a call time is and then the uh the model ignoring that. Another one would be a customer scheduling a call. We tell them that we've scheduled it for them but we don't return the payload in in the proper way and so the the call never gets scheduled and so we don't follow up with them. So these kinds of things needed to be fixed right away. But before we did that, uh we asked the last question, is there any thing that we can do in order to prevent a retrain? Can we have some kind of a band-aid fix to get out there so we don't have to go through a whole week-long process uh for one or two issues? And so we we ranked our own bugs uh based on how much customer pain we could tolerate at the moment. Um, so not

**[9:20](https://www.youtube.com/watch?v=4loPnxvWWhg&t=560s)** a great situation to be in with a production system. This led to what I've come to call the calcification tax. Uh, the more we used the model, the more rigid everything became. This manifested in a couple different ways. First, we were locked into our model. You remember when I said that uh fine-tuning would give us uh more freedom in what model we did? That was not the case. Um within providers there's nuance between one model version to another and so that changes the the training data that you need to provide it. Um across model provisors uh it's extremely different the structure of the data you need to pass to it be different. The amount of the training data to get good results

**[10:08](https://www.youtube.com/watch?v=4loPnxvWWhg&t=608s)** the way to interact with the training interface. All of this caused a lot of complexity and so it was just too costly for us to switch. And so um to we kept it the same model for consistency because we already had a lot to do with uh with each retraining process and we couldn't afford to uh upgrade the model. So uh the other way that this locked in was architecture. We built this app in uh late 2024 when workflows were kind of the um gold standard if you wanted good u production results and uh the AI world moves very fast and we couldn't adapt to

**[10:59](https://www.youtube.com/watch?v=4loPnxvWWhg&t=659s)** that because we were so locked into this just trying to keep it running and we couldn't take advantage of the new architectures um and and improve performance that Okay, so earlier this year I had an aha moment. Um, we started using cloud code for our coding tasks and I noticed that we never needed to change the model depending on what task we're using. Um, we just changed the skill, the resources that we passed it, the context. Um, you drop in the better better context, you get better results. And I thought, why can't we do this with our messaging app? Um, this was obviously difficult for me to admit because I was the

**[11:47](https://www.youtube.com/watch?v=4loPnxvWWhg&t=707s)** champion for fine-tuning. And, uh, luckily we were able to piggyback on a project that was already happening. Um, and so we migrated our workflow approach to a series of skills, tools, and resources that the skills could could load into or load up. um and get that context. And so we pushed this as one of our first production tests of our our new agentic framework that that was being built already. Now uh I want to compare the process before and after our rebuild. Uh before we already went through the kind of the training cycle, but there was this triage cycle beforehand where we needed to make sure that we had reached a critical mass of problems before we

**[12:37](https://www.youtube.com/watch?v=4loPnxvWWhg&t=757s)** would even attempt to uh fine-tune again to improve everything. Like I said, this took about a week, so it was a long process, costly. Uh after the rebuild um it was a simple process of you find a problem you adjust the simp system prompt or the skill that was affected. We validated performance on a curated set that we have been collecting over the time that this was in production. We iterate a few times and then we deploy that simply by uploading MD files to an S3 bucket. um this whole process from discovering a problem to deploying the fix we reduced down to less than an hour. So it extremely improved all of this and we could be far

**[13:27](https://www.youtube.com/watch?v=4loPnxvWWhg&t=807s)** more reactive give our our customers way better performance or better experience there. Now I'll be honest it did cost us a little bit more per message. we were using better models. Um, so the API costs were a little higher, but accuracy went way up. I said before that accuracy was the key to to getting all of this right. Um, and we did that. Accuracy uh was far better with this than it ever was with fine-tuning. Um, next, like I said, we reduced our uh our fixed process from days down to minutes. Next, we were able to unfreeze our model and finally get that freedom from a

**[14:15](https://www.youtube.com/watch?v=4loPnxvWWhg&t=855s)** vendor that we never had with fine-tuning. Um, our agentic framework was built model agnostic. So, we could use open AI, we can use uh anthropic, we can use any other model that we want. The important part is the context that we're providing to that model. And then lastly, while it cost us a little more per message, the total cost went down because we were spending far less time trying to keep it up and running and fine-tuning to uh to keep it working properly. So before you fine-tune, I'd ask you, can you cross your reason off of this list? So, I thought we would get better accuracy. Uh, the rebuild beat the fine-tuned model.

**[15:04](https://www.youtube.com/watch?v=4loPnxvWWhg&t=904s)** I thought we would get lower cost of the volume we were doing. Um, I was looking at the wrong costs. We we paid more per message, but the total cost ended up going down with our rebuild, lower latency. We we did see marginal gains on these smaller models, but they were so small that in practice it really didn't make any difference. And then maybe you've got a narrow or structured task. Our textbook case still became tech debt. And lastly, vendor control. It's not as simple as just plugging the data in. The other two situations where you you might have privacy and data control or you need some offline offline solution. I would say this these are the situations

**[15:52](https://www.youtube.com/watch?v=4loPnxvWWhg&t=952s)** where a fine-tuned model may be useful. But you need to be cautious. There are other solutions out there. Um but um you need to make sure that it's not uh not causing issues in the long run. So finally fine-tune only when you literally cannot call a frontier model and even then your decision still has to beat the the tax. Thank you.
