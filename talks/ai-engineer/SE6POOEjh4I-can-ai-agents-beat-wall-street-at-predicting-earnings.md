---
id: SE6POOEjh4I
title: "Can AI Agents Beat Wall Street at Predicting Earnings? - Ashwin Paranjape, Samaya AI"
slug: can-ai-agents-beat-wall-street-at-predicting-earnings
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Ashwin Paranjape"]
channel: "AI Engineer"
duration_min: 15
published_at: 2026-11-09T08:00:11Z
video_id: SE6POOEjh4I
url: https://www.youtube.com/watch?v=SE6POOEjh4I
youtube_url: https://www.youtube.com/watch?v=SE6POOEjh4I
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Ashwin Paranjape", "Samaya AI", "earnings prediction", "financial agents", "AI in finance", "consensus estimates", "forecasting", "AI evals", "agent harness", "frontier models", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration", "Science, healthcare & applied ML"]
transcript: true
---

# Can AI Agents Beat Wall Street at Predicting Earnings? - Ashwin Paranjape, Samaya AI

**Ashwin Paranjape**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Ashwin Paranjape` `#Samaya AI` `#earnings prediction` `#financial agents` `#AI in finance` `#consensus estimates` `#forecasting` `#AI evals` `#agent harness` `#frontier models` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=SE6POOEjh4I) · [Conference site](https://www.ai.engineer/)

## Description

Ashwin Paranjape, founding AI lead at Samaya AI, explains why stock prediction is too noisy to learn from, and why earnings prediction makes a better test for financial agents: it has hard numbers, an expert baseline and an explanation for every surprise. He walks through a point-in-time environment that blocks any look at future data, then results across more than 450 earnings reports where the latest frontier models start to beat analyst consensus. He shows where agents win and miss, and why live data matters more than anything else.

Chapters:
0:00 Intro
0:39 About Ashwin
1:52 Finance's big unsolved problem
2:19 Why not predict stocks?
3:18 Earnings prediction as a task
4:32 A point-in-time environment
6:31 Results: AI vs. consensus
9:30 Where agents win
10:35 Where agents miss
11:46 Why live data matters most
13:09 Expert guidance and hiding consensus
14:11 What's next

Ashwin Paranjape

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,553 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=SE6POOEjh4I&t=1s)** [music] >> I'm Ashwin Paranjpe. I am the founding AI lead at Sumaya. Uh and today I'm going to talk about you know, if agents can rewrite compilers, why can't they pick stocks? So I give I had this title um couple of months ago, but AI moves so fast that I now need to change this title to agents can solve Navier-Stokes and why can't they pick stocks? So just a brief background about me. So I did my PhD from Stanford. One of the highlights was you know, fine-tuning GPT-2 in 2019 and putting it in production with real users with tens

**[0:48](https://www.youtube.com/watch?v=SE6POOEjh4I&t=48s)** of thousands of interactions every day. Uh when I joined Sumaya, I was focused on training our retrieval stack, working with long context models. In fact, you might have seen a paper called Lost in the Middle that was led by my intern Nelson when he was interning with us. Um but yeah, so this allowed us to have high-quality retrieval over messy customer data. Last year, I kind of changed my focus into designing our financial agent harness. So this allows contact context efficient unified access to data sources and it's rolled out to like 12,000 users across Morgan Stanley and hundreds of other users in hedge funds and asset management firms. Uh finally this year, we released a benchmark which is the largest and the hardest open source benchmark for you know, deep research financial workflows. Um I led the design of this benchmark a

**[1:38](https://www.youtube.com/watch?v=SE6POOEjh4I&t=98s)** couple of years ago when we started collecting it. Please check it out if that's of interest to you. Um so yeah, so I was thinking well, you know, worked on training the retrieval stack, the harness, eval. So what's next, right? Um So in math, you have like this marquee problem, like the millennium prize problem. Can you get a solution to Navier-Stokes? There are hundreds of open math problems like that. So, what could something like this look for finance, right? Um so, like the kind of zoomed out answer is can we forecast the future? Can we forecast it better than what we do today? And that's really like the the highest level challenge we can focus on here. So, you know, in my naivety, I went around asking people, "Well, what if we try to predict stocks?" Um so,

**[2:26](https://www.youtube.com/watch?v=SE6POOEjh4I&t=146s)** just to show of hands like how many people try to predict stocks or are adjacent to it in this audience? Wow, that's like over over half of us. Um and so, um so, I was like, "Okay, well, you know, how hard could it be? Like everybody's trying to do this." So, uh I went to Arash, who's a colleague here at Sumaya. He was previously at Bridgewater and Verition, and he says, like, you know, you just don't simply start with stock prediction. It's very noisy. It um doesn't tell you why certain model is behaving in certain ways. It doesn't tell you if, you know, the reasoning is right or not. Nobody really knows why stock moves a lot of times. So, then, um by the way, he's sitting here. Uh close collaborator. >> [laughter] >> Uh come chat with us afterwards. So,

**[3:15](https://www.youtube.com/watch?v=SE6POOEjh4I&t=195s)** um yeah, so he suggested, "Let's instead do earnings prediction." So, what is earnings, right? So, every quarter, a company uh comes out and reports its earnings. It gives revenue, gross margin, operating income, uh EPS, a bunch of other metrics. And then it also gives guidance for the next quarter. Um analysts uh across buy-side and sell-side try to predict these numbers in the coming quarter. Uh a lot of the sell-side analysts publish this, right? So, it gets pooled as what is called a consensus estimate. And then the next quarter, the company reports. Now, if it's above the consensus, it's a beat and it's a surprise. If it's below the consensus, it's a miss. Uh and then during the call and after the call in the commentary, they also talk about why these uh like, you know, surprises happened. So, this is from a from a AI

**[4:03](https://www.youtube.com/watch?v=SE6POOEjh4I&t=243s)** and ML perspective, this is a great task. It has quality like quantitative ground truth. You know what exactly happened afterwards. You have an expert human baseline to compare against. And you also have the qualitative ground truth that tells you, you know, why the agent was right if it was right. And so, the then the question is, well, can an agent do this task? Can they make good predictions? And this is this is going to be the focus of today's talk. So, to be able to do this, we had to work on building an environment and a harness. So, just to give you background on environments, whenever you have these agentic models, they need to be in an environment where, you know, they are given the right data, they are given a task, and then you can evaluate it at the end. And you might have heard it in the context of training, so RL training,

**[4:51](https://www.youtube.com/watch?v=SE6POOEjh4I&t=291s)** but you need the same environment for evaluation as well. And then that environment needs to provide a harness to the agent. So, here's how the environment schematically looks like. So, you have an AI model that's sitting inside a a harness, so we provided the harness. This harness we constructed such that it brings point-in-time information. So, if we are trying to predict, say, 7 days or five sessions before earnings, the context only includes information up to that point, up to this minute. And okay, so with this harness, the AI agent researches and makes a prediction, and come the earnings day, we compare the differences and then see how good its prediction was. Now, to build this harness, what we did was we started from Samaya's production-grade harness. So, this

**[5:39](https://www.youtube.com/watch?v=SE6POOEjh4I&t=339s)** includes all the real-world data that we provide through our system. It includes company documents, prices, consensus, also news. Then we have an point-in-time gate. And so, it's a programmatic gate that enforces no access to future information, and it's enforced with an authentication token, so there is no way for the agent to hack around this. We modify all of our document retrieval and structured data tools to support this point in time gate. And web is one of the trickier ones where it's very hard to have this gate. So instead we get a reasonable proxy by adding more news streams and making sure that they are time stamped. So finally we add some expert guidance that helps with making better use of the context and

**[6:26](https://www.youtube.com/watch?v=SE6POOEjh4I&t=386s)** also helps with the predictive task. So this is the headline. So we found that AI is able starting to outperform consensus in predicting earning surprises. Here we looked at more than 450 earning sprints. This had to be from July onwards because the latest model that we were testing was Fable 5.1 which had a knowledge cutoff of June. So we looked at seven frontier models to compare and here are some of the results. Um So the first thing we looked at was prediction error. So this is when your agent is making a prediction, how far is it from the actual normalized by the company's historical volatility. As a comparison point we looked at consensus. It had an error of 1.5

**[7:16](https://www.youtube.com/watch?v=SE6POOEjh4I&t=436s)** times historical volatility. But we also know that a lot of consensus is under reported and at earnings you know the companies outperform more often than not. So we corrected for that bias and we have a much better bias corrected error which is 1.18. And here's how the progression of models looks like. So you start from Claude Sonnet which is you know Kimiko 3 some of the weaker models but then as you go to the latest models Opus 5.5, Fable 5.1, GPT-6 Astra you start this seeing the error go down. And in fact this is the graph with all the metrics together but if you look at revenue which has the least amount of adjustments you actually start seeing GPT-6 Astra is significantly better than

**[8:05](https://www.youtube.com/watch?v=SE6POOEjh4I&t=485s)** even the bias corrected consensus. We also looked at hit rates. So, uh in simple terms, let's say if the consensus is $1.1 and 4 cents, the print is $1 and 9 cents. So, did the model call it above consensus? If so, that's a hit, otherwise it's a miss. So, here also we see the latest models are starting to do better. And interestingly, looking at just the below consensus calls, which tend to be harder typically to make, we see that newer models are starting to outperform historical majority baseline. So, just to talk about the baseline, we looked at last eight quarters and saw what was the majority, did it on the whole beat or miss consensus in the last eight quarters. So, yeah. So, Astra again doing significantly better.

**[8:51](https://www.youtube.com/watch?v=SE6POOEjh4I&t=531s)** And then we also have a new metric, which is, you know, surprise correlation. So, was a big predicted beat also a big actual beat versus a big uh predicted miss a big actual miss. So, that allows us to combine both the magnitude as well as the direction together and gives us more statistical power over all of these models. And so, here we see again Astra, Opus, and Fable are significantly outperforming the baseline and they are you know, they are within statistical significance of each other. Okay, so we looked at a bunch of numbers. You know, the numbers tell one part of the story. But we also want to know what's really happening under the hood right?

**[9:39](https://www.youtube.com/watch?v=SE6POOEjh4I&t=579s)** So uh Here's here's an example. Um What we find is that agents win when they are gathering evidence and they are being they are able to adjust away from consensus. So, in this example, we have Macom, which is a semi-manufacturer that supplies data centers. And then the agent found one of its suppliers, a small UK wafer manufacturer, it it revealed sort of Macom's data center improvements like in revenue. And it adjusted for it, went all the way down to the P&L, and found and predicted a forecast that was significantly higher than consensus or bias corrected consensus, and very close to actual. So, this is the kind of reasoning these

**[10:26](https://www.youtube.com/watch?v=SE6POOEjh4I&t=626s)** models are doing where they're able to find data that is very timely over a large scale and then are able to adjust for it. On the other hand, we also find that they miss when they see the evidence, but they don't have enough conviction to act on it. So, this is Ross Stores, the dress for less Ross. And here the agent found that one of its peers had booked a tariff refund, but then it decided to leave it out of its uh prediction for gross margin. And then the prediction like very was very close to the consensus, but the actual came out much higher. And so, we see sort of them them missing when they don't work with conviction. These are two examples. There are more examples on the online blog post,

**[11:14](https://www.youtube.com/watch?v=SE6POOEjh4I&t=674s)** but yeah, this is just to give a flavor of sort of what's happening behind the scenes. Okay. So, here's the last interesting thing before we kind of jump into some of the applications. So, if you look at, you know, these predictions which are significantly above or below consensus, we find that the models tend to outperform when the surprises are bigger, which is also very interesting. Like you can look at the things that these models tend to have on the extremes and then learn sort of what they're doing there. Okay. So, we looked at how a model can change our predictions, but what about the data and the harness that goes into it right? So, we found that access to live data is the most important factor in accurate financial predictions. So, we ran two

**[12:04](https://www.youtube.com/watch?v=SE6POOEjh4I&t=724s)** comparisons. One is with just the parametric knowledge. So, no data access, just the model itself. And this gives us a good comparison point because Fable was trained until June 2026. And so technically it should have memorized all the documents that came out before that. But even with all of that in its pre-training it's not able to be like it's not any good at all. Okay, so that's the parametric version. What about if you give it stale data? So if you give it data that is 11 weeks before the earnings call, it still has the previous earnings result and it's like you know the guidance and other analyst consensus, but it's around 12 to 15 points lower. And to put this in a context, this is the same gap you would

**[12:51](https://www.youtube.com/watch?v=SE6POOEjh4I&t=771s)** see between Sonnet and Fable 5.1 in terms of the quality you would get out of these two models. Uh yeah, so latest data is important. Also another proof point that they are actually, you know, finding information and adjusting for it in the for the latest information. Then we looked at the effect of expert guidance. So without expert guidance fewer tokens used, fewer minutes spent on research. But with expert guidance we see significantly more research being put into things. And in the case of Astra, we have a significant difference improvement in the predicted error. Finally, we wanted to see what happens if you don't give any consensus to these models. So we created a setting where we

**[13:39](https://www.youtube.com/watch?v=SE6POOEjh4I&t=819s)** removed access to all the consensus. We even had like document extraction tools redact any mentions of consensus from any sort of news sources as well. And what we see here is that the the best models don't really need consensus anymore. So they are able to reconstruct the consensus view. In fact, in the case of Astra, there is no significant difference between with and without consensus. Whereas for the older models you did like see a big jump with access to consensus. Um So yeah, so we are seeing frontier models outperforming consensus. So the question is, you know, what's next? This is available for alpha testing in the product. We're also working with customers to see if their internal data is useful for some of these predictive tasks. So feel free to get in touch. We

**[14:27](https://www.youtube.com/watch?v=SE6POOEjh4I&t=867s)** are doing research on model reasoning. So trying to understand if this reasoning is the same way as humans do their reasoning. If not, is there a way to complement human reasoning to try and you know, get the best of both worlds. And then we're looking at post training and continual learning. So these agents, just like humans, right? You can learn through experience. You can learn by the mistakes you've made in the past. And so can the models keep learning from the mistakes in the past. I think that's the other interesting question. You have a couple of QR codes. We have the blog post. There's a lot more details there. Also linked to frontier finance. It might be of interest if you're trying to evaluate your own sort of harnesses. Yeah, and Arash and I will be here. We'd love to chat with you. Thank you.
