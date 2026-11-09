---
id: _dTF3NpPzGo
title: "Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI"
slug: why-ai-writing-still-reads-like-slop-louis-francois
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 19
published_at: 2026-10-22T07:00:28Z
video_id: _dTF3NpPzGo
url: https://www.youtube.com/watch?v=_dTF3NpPzGo
youtube_url: https://www.youtube.com/watch?v=_dTF3NpPzGo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Towards AI", "Louis-François Bouchard", "AI slop", "creative writing", "AI writing", "LLM benchmark", "LLM as a judge", "evals", "prompt engineering", "writing style", "content creation", "AIE NYC"]
topics: ["Evals, observability & reliability", "Prompting & context engineering"]
transcript: true
---

# Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Towards AI` `#Louis-François Bouchard` `#AI slop` `#creative writing` `#AI writing` `#LLM benchmark` `#LLM as a judge` `#evals` `#prompt engineering` `#writing style` `#content creation` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=_dTF3NpPzGo) · [Conference site](https://www.ai.engineer/)

## Description

Louis-François Bouchard of Towards AI breaks down what makes AI writing feel like slop: overused words, vague generalities, saying nothing, repetition, hallucination and a voice that sounds like everyone at once. He then shows how his team built a benchmark to measure whether a model can write a video script in his own voice: 10 scripts, 5 drafts per model, 4 LLM judges, nine scoring metrics and 1,000 human A/B checks. He shares what it cost, why judges favor their own model family, and practical tips for writing with AI: very long prompts full of examples, one review pass from a strong model, many cheap drafts merged together, and always a human edit.

Chapters:
- 00:00 What is slop?
- 02:41 Measuring sloppy writing
- 03:49 Why build another benchmark
- 05:44 Can a model write like me?
- 07:19 10 scripts, 5 drafts, 4 judges
- 09:14 What gets measured
- 11:10 How the judges score
- 12:38 Judges prefer their own models
- 13:46 Human A/B checks
- 14:15 What it cost
- 15:20 What we learned
- 16:21 How to write better with AI

Louis-François Bouchard, Towards AI: https://towardsai.net

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,995 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=1s)** [music] So I'm here to talk about all these words that we call slop and uh more importantly I want to uh try to help fixing what Kerpatim termed as the the slop ap. that he thought would start in 2026. And I think we've seen that on social media. So, uh, to try to fix this and to stop slup, we first need to define it. So, first, what is slop? There are tons of different definitions from the various experts in the field. But what I

**[0:51](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=51s)** think we can all agree is that it really sucks to read something that feels generated. And it usually looks like this with uh the words that we know of the delve and uh the generidities and other things like these. And the main problem is that even as models get better with fable GPT 6.1 and all the the better models slop doesn't seem to go go away. It just keeps on scaling. So we need something different than just training the models more it seems. And I really want to try to at least first define what slop is so that we can understand why it's there. And so to me, slop is made of six main thing. First, there are tons of overused words by language models that we don't really use

**[1:39](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=99s)** like delve that we really know well. Second, it's usually too general. It's always talking about most teams, most projects. It doesn't share nothing specific. And I'm myself guilty of using that on LinkedIn as well, which I guess it's the LinkedIn meta, so it's uh it's normal there. And worse, slop sloppy text usually says nothing. It's just like nice words put together that we don't even usually use. And even worse than that, it says nothing, but it also repeats itself a lot. So it repeats nothing and it's too general. And uh even worse, it hallucinates. As we know, models hallucinate. So the sloppy text also we cannot really fully trust it.

**[2:28](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=148s)** And lastly, the worst to me is that it usually has the wrong tone or at least it has no tone and like everyone's tone at the same time. So it just doesn't really talk like you. It doesn't share stuff that you would share. So my goal here today and with this project that I've been working on is to first measure this sloppy writing not just slop words. I don't want to rebuild EQbench slop score. It's just it's really about measuring how sloppy is a writing. So in order to do that we are well today right now releasing a new benchmark that we called tone bench which the whole goal of the benchmark is to measure if the new models or models are good at creative writing which I will try to define as well. So here's the plan for

**[3:18](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=198s)** today. Uh the plan is to justify do we even need another benchmark then how it works what we measure what how we built it and I want to share like the cost of building it uh our decisions what we learned already from for writing with AI from the benchmark and share some more stuff about this so with that uh let's delve in so the first first thing do we even need another benchmark again and just looking at LinkedIn and X X replies my replies on X I think we do it's like people are spamming more and more generated content so at least have them be decently good and uh more precisely I also really need it

**[4:07](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=247s)** a small team at towards my company and we have one side of the company that is focused on education we build tons of educational content mostly for AI engineering And as a small team, obviously, we use AI as well for that. And it's been extremely annoying to review this slop constantly and try to fix it. We uh I published hundreds of videos. We published thousands of articles. We released a book. We are working on a second one for AI engineering. [snorts] And so we really need to have the best models possible that will help us write better and not be full of slop. And another nice uh addition to that is that I've been sharing about this benchmark on on X for quite some time as I've been building it and it got really

**[4:57](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=297s)** nice engagement and people seem to confirm that we did need some sort of more creative uh writing benchmark like this one. And lastly, just to prove that I think we are the right team to work on this benchmark, we well I've been buil evaluating AI models since my masters and then PhD and now at towards we do build evaluation pipelines for our clients. We have 15 AI engineers with us and we have creative writers, editors uh on board. So we already have that for our content. So I think uh well I wanted to leverage that to build a benchmark and help the community even more. So what did we build exactly? Hopefully

**[5:44](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=344s)** I will try to share as much as possible and I'm happy to chat if we can help even build your own or if I can just share some some of our learnings. So what we built is super subjective. Uh it's a way to measure if a model can write like me. And how I define that is that is just that if I can read it out loud like right now without cringing because of the the the the words that I wouldn't use myself. So the process is very simple. The the benchm the process benchmark the benchmark process is very simple. We have a prompt that is the brief and the research that we send to a model and hopefully it will generate entirely a video script that I could have written. Uh obviously that doesn't happen. It

**[6:34](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=394s)** really sucks usually, but that's the whole goal. And we measure that that final script against our rubrics and um just our whole evaluation pipeline. And the prompt that we send to every model in the benchmark is much more in-depth than that. It it looks more like this where we have a lot of details on how I talk, how I write, all tons of examples of my previous content videos. We have a lot of information on storytelling in general, active sentences and just how to write well. And we have directions on what to generate and what to do for this current task which in the end the model would generate one script. And this is just one of them. In the current benchmark, we have 10 different scripts uh that we

**[7:24](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=444s)** worked really hard to make as good as possible. And we built rubrics for them to help um as we will see LLM judges rate these these generations. So we have 10 different scripts. Some of them are published, some are not. We don't see which ones are the benchmarks so that we check for contamination as well. And then what do we do with these 10 scripts? We take all the models out there and we try to measure their generations. Uh what that means is that for every single model we will do 10 times this process generate the article from the prompt. In fact we generate five of them. I will very soon share why. Then we have four different LLM judges analyze them. I recently added

**[8:13](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=493s)** Jev as a test. Uh not sure if I will keep that but yeah I I I added it just to see if it worked well. And then we calculate in the end a final score for the leaderboard. I I will go through all of these steps from left to right. First, why do we generate even five scripts is to check for intramodel variability which I highly suggest if you are building your own evaluations because especially I guess on a creative task sometimes as we see here with gr 4.7 some of generations are outliers where it's as we see for from the benchmark it's just as good as opus 5.5 but on just one generation out of five. So we want to measure for that and the worse the model is the widest the variance. So uh we have some learnings about that that I'll share at the end as

**[9:03](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=543s)** well. But yeah it's we we found that five drafts seems to be the good middle ground in terms of of cost for us to execute and to measure this this variability. So what do we measure exactly and how do you even quantify writing quality? That's been the challenge and we worked on it for for quite some time. Right now it's all open on the benchmark and there are way more details on the benchmark page as well. But what we measure is nine different metrics that we detailed uh that that we really detailed. But I can condense them in five main aspects. First we measure the tone. So does it sound like me? Which means that like can the model adapt to a specific tone? Second, we measure just pure is it good

**[9:52](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=592s)** writing? Does it have like good hooks, good emotion, emotional transition and all the the aspects that we're looking in a in a good story? Then we measure if it follows instructions. Did it follow the the length, the expected length, the format expected? Uh did it put the right images and right right things in the right place? Fourth, we measure for research accuracy. So uh we have a research brief along with each script and we just measure if it hallucinated or used the research correctly. And lastly we measure for slop using eqbench slop score but also our own measurements. And what uh this looks in terms of what the judges see is more like that. We

**[10:41](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=641s)** have around a thousand words of examples and and instructions and directions around each of the metric that we have along with the script to analyze my own uh script as some sort of of guidance and the brief and the research. So all in all it's a 14,000 prompt that we send to to every judge to then get the feedback that we will dive in next. And uh so so the judge just analyzes the writing quality. It doesn't focus on length uh and doesn't know which model is writing. Uh we just do that after with with code itself. On one metric like tone and voice which is our main metric. It looks a bit like this where we have a lot of detailed

**[11:29](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=689s)** descriptions of what is my tone and what to expect and how to analyze this. Then the judge will categorize between six categories first and after having found a category it will give a rating. Uh we found that this is the best way to measure for this more qualitative task from just binary that we usually suggest to use or directly categories or directly percentage. We found that this actually works really well and uh it has tons of examples of what each score means in terms of of writing for each of the task. And what the judge sent back is something like this. It has the nine different metrics scored with a

**[12:18](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=738s)** justification for for the score and an example of like uh I wrote this score because of this example in particular. But the main thing is that all of this is automated uh obviously because we with 120 models we we generate five drafts each for 10 tasks. It quickly goes to the thousands of scripts to review. So we cannot really review this ourselves. And the problem with LLM judges is that they have preferences. Uh some models prefer themselves. Most models prefer themselves. And particularly OpenAI. And what I found quite funny when studying this is that it seems like entropic and open AI are really in a in a war here where they seem to have post training on

**[13:06](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=786s)** hating each other which is quite funny. But all this to say that you really want to check for when you have when you use LLM judges like using GPD for instance if you want to know which model is best for your task be careful and use different model family just to ensure because we see here that OpenAI really has a strong preference on its own family of models not just one model but all open AI models and so to fix also for that we listen to a few comments that I got on X. suggesting to use human for a creative task which would be ideal but quite impractical. We still tried to to do that in a scalable way where right now we compared manually me and three of my teammates

**[13:56](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=836s)** 1,00 AB pairs of the generated scripts not the full scripts but like a good chunks that is comparable between two scripts two generations and hopefully we'll do more and I want to publicize this also for uh to get help from the community in the future but that's not right now. So what did it cost us and what's the workload behind that? For me, for us, it was a kickoff cost in terms of hours of around 500 hours to build the 10 scripts, uh define all the rubrics, find the examples, uh try to quantify quality, which is very difficult. And then I just iterated myself with uh four different 20x subscription for four months to build the benchmark and all

**[14:44](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=884s)** the other things and experiment and change the the mat the matrix ratio and all these things. And so we just spent thousands of dollars there. And uh if you want to do this a similar type of benchmark you need to know that it cost quite a lot. But right now, if I just change one thing in the rubric, so how the judge rate um generations, it would cost us two more than $2,000. And if I just change one line in an input prompt for a model when it generates, it cost us more than $4,000. So it's very very expensive to experiment and change these things in the prompt. So you want to do this uh carefully. Now what can we get out of this benchmark out of tone bench? Uh you can

**[15:34](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=934s)** get tons of things on the the website itself there's like a lot of details but importantly uh I want to share that what I've learned from the past four months is that you don't want to pick for for creative writing is that you don't want to pick the model that will generate a one-shot amazing post. You just want to find the model that will be the least annoying to you to get to where you want to be. So uh like there won't be any perfection anytime soon I think and what that means right now on the benchmark it means at scale GLM 5.3 flash is extremely good extremely cheap it's 50 times cheaper than the best one which is opus 5.5 extra high which is uh 2.5 times cheaper than max thinking but with same results so you don't want to use

**[16:22](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=982s)** max for writing usually um and otherwise for The best uh how to write with models that we got out of this is to first have an extremely long and detailed prompt. It cannot be long enough and the more the better. You want to add every example you can think of of what to do and how to do it. Same thing for negative examples of things you don't like and that doesn't sound right. the words you don't want everything you you can share every if you write newsletters or whatever you can share it in full and it will just be better as well and what we've seen that really really helps is to use a highinking judge just one time one to three times otherwise it will loop into slap so just one review

**[17:12](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=1032s)** of another model with the same instructions directions that will give feedback to the writer really like I don't quantitative metrics on that but it it helps a lot and for a company if you work with APIs and want to do this at have the best results at scale possible what I suggest is to generate several drafts like 10 drafts of one specific thing with a cheaper model like GLM 5.3 flash and then have a smarter highinking judge like Opus or or whatever you want pick and merge the best parts of each of this these drafts which I think will still land way way less expensive than just one generation by Opus 5.5 and I think will lead to better results from what I've seen

**[18:04](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=1084s)** and lastly you want a human review you cannot really go around that but all of this benchmark measures obviously my voice so it's super subjective but I and it's just one data point you don't want to fully trust it blindly doesn't mean Opus 5.5 is the model. So, but ideally it's a strong signal to find which model is good at writing and which is less sloppy. Um, you I suggest you to build your own evaluation pipelines. If you want, we can help. You can chat or reach out. And regarding the benchmark, it's live. We just like right now published it and released it. So uh there are tons of uh graphs, tons of insights, tons of comparisons uh and details on the implementation full methodology. So just uh check it out and hopefully it's

**[18:52](https://www.youtube.com/watch?v=_dTF3NpPzGo&t=1132s)** useful. Thank you. [applause]
