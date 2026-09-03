---
id: 9Z_FGK6lDxE
title: "AI Launchpad 2026: Sutro"
slug: ai-launchpad-2026-sutro
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "Practitioner AI conferences"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: null
duration_min: 9
published_at: 2026-06-23T22:57:04Z
video_id: 9Z_FGK6lDxE
url: https://www.youtube.com/watch?v=9Z_FGK6lDxE
youtube_url: https://www.youtube.com/watch?v=9Z_FGK6lDxE
tags: ["AI"]
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# AI Launchpad 2026: Sutro

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `9 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=9Z_FGK6lDxE) · [Conference site](https://www.aicouncil.com/)

## Description

Sutro enables AI teams to build high-volume, expert-aligned models they can trust at scale, reducing manual review time by 90% and inference costs by 80%

SPEAKERS:
Seth Kimmel - Founder & CEO, Sutro
Colin Parsons - COO, Sutro

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*1,620 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=0s)** Hi, I'm Seth and this is Colin. We're building Sutro. Uh we got our start building a high-performance batch inference service selling to data ops and research teams using it for tasks like classification, extraction, synthetic data generation, and eval of LLMs as a judge specifically. But as we worked with teams, a more insidious problem kept showing up. Teams didn't actually trust models to make the right decisions at scale. I'll say it again. AI teams don't actually trust models to make decisions like they or their experts do when run at an unsupervised scale. And as a result, AI teams have become QA teams. 20% of the effort goes into building product and 80% of the effort goes into

**[0:48](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=48s)** just getting models to behave consistently as teams want them to. Teams who are supposed to be ideating, building, talking to customers are spending their time sharing spreadsheets of model outputs and bickering over [clears throat] results in Slack, adding edge cases to prompts in endless loops, building golden data sets by hand or worse, just using a big model, creating judges for judges and judges for those judges. And of course, the famous gaslighting or threatening tactics to get models to behave. We call this eval hell. It wastes a ton of time and leaves companies with brittle, underperforming models that don't generalize in production. Can you raise your hand if you found yourself in something that looks like

**[1:35](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=95s)** eval hell for more than a few hours at a time? Okay. Um so unfortunately, this problem won't solve itself. Models continue to improve in general capabilities, but these tasks almost always require subjective decision-making and thus the judgment of a domain expert. So GPT-6, 7, or 8 is not coming to save you. We believe there had to be a more rigorous, systems-driven approach to grounding models in human judgment without all the pain. No more vibes-based AI engineering. So, we rolled up our sleeves and built exactly that. We created a solution that requires zero prompt engineering, zero fine-tuning, and zero upfront data labeling. It results in a 90% decrease in time

**[2:24](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=144s)** spent on QA and manual review. I'll say that again, a 10x reduction or more in time spent on QA and manual review for evals. An 80% decrease or greater in at-scale inference costs, all while dramatically increasing accuracy, alignment, and enabling continuous improvement after deployment. Colin will show you what that looks like. >> All right, cool. So, I'm building an agent to help people find long-term medical care. This is people's health, so I really care where my agent gets things wrong, or when users ask it for things that are out of scope. And to detect those cases, I'm going to align an LM as a judge of my agent. When I'm doing that in Sutro, it's pretty simple. I care about three things. Number one, what's my task? Pretty basic here, did my agent do the

**[3:12](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=192s)** right things to find matching long-term care providers? The second thing I care about, what should the output look like? Pretty basic right here, the agent got it right, the agent got it wrong, or the ask was out of scope. And the last thing I care about is what are the inputs? So, Sutro supports multimodal inputs, but for this case, we're just going to drop in a CSV of some agent traces. I can look at, you know, each of the input columns that I'm passing in, scan over these guys, and start my function. Cool. While this is running, what's happening behind the scenes is this LM as a judge function is finding my highest value cases. So, there's zero upfront data labeling for this. The philosophy behind this is we really, really want to capture

**[4:00](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=240s)** your last miles of preferences. If you think about getting an agent to make decisions like you would, rule-following has become increasingly good with with better and better models, but actually capturing your internal decision logic, your hard preferences for how would I approach this problem? What do I think? I'm the real expert here. We need to capture that rule set in a way that models can consistently follow it in production. So, we're speed running the discovery of these edge cases. And, you know, you can see right here we're using an ensemble of models to drain the biases of any one individual model, so no overfitting to Claude Code's preferences or Codex's biases. This is alignment grounded in real quantifiable metrics, not just vibes. Colin, can you remind me one more time why I can't just use Claude Code for this? Yeah. Well, if you use Claude Code for

**[4:48](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=288s)** this, uh you're going to have a model that really learns Claude Code's preferences. But, I'm the expert here. I know what's best for my patients. I know what's best for my users. And so, I wanted to capture my preferences, not just what Claude Code thinks. And why can't I just build something like this myself? Yeah, I also love building one-off projects that I maintain and use alone for 2 years. Understood. All right, cool. So, all I do to use this is I tell Sutro whether the LLM is aligned with my thinking. I'll skip through some of these examples until I find an interesting one, but you can sort of see we're looking at some low confidence examples and telling, you know, did the agent get it right? Did it get it wrong? Why or why not? Right here we've kind of got an interesting example. So, a user asked us for a pain management doctor who does ketamine infusions. We can see that the LLM as a judge generally thinks that this was

**[5:34](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=334s)** wrong, and it's highlighted the reasons why. So, it's highlighted the ask. Uh you know, we searched through a database to try to find matching providers. Uh we searched the web, and we found that like the web search results may or may not have been good. We started to get reviews. So, I'm going to agree with this. I'll say that yeah, I got it wrong, but I'll say I got it wrong because the agent did not look for providers that match my implicit needs. Okay, cool. You can see we've got 10 examples right here, but I'll skip through most of them. For each of these, you can check, "Hey, is the LLM aligned correctly or not?" Um the idea behind this is this is a just diagnostics. This is drawing judged behavior directly from my internal preferences, from my feedback,

**[6:22](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=382s)** and grounding that in my subject expertise and knowledge. Once I'm done with this, I can add in the labels, and I just click optimize prompt. So, what's going to happen right here is you're going to see a live diff of how my prompt is changing to capture the implicit preferences and rules that I have behind my decision-making. You can see that right down here. I'm not going to make everyone watch as this evolves live. I'll just skip to the end, and you can see what the end result is. So, I've built an aligned judge right here. You can see it's aligned because it has this nice ready for deployment sticker. You can see all the rich rule set that's been evolved just by taking my feedback and going back and forth and testing it over the data set. You can see overall performance. A way that I can tell it's done is I can look at a learning overview and see that

**[7:10](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=430s)** A, there's a lot of consensus between models and how to approach this problem. This means that my task is very specific, so it's easier for them to follow, and there's a high degree of user model alignment. So, not only is my task specific, but the models are actually aligned with how I'd approach this. So, now the performance has plateaued, I should deploy. There's two things I can do. I can either go to data review, and I can look at a golden data set and export it, or I can just click this deploy button and actually deploy the model that I built here in production. So, I've already done that. I'll just toggle to the batch tab over here, and I've run that model that I just built in production already. You can see I ran 27,000 rows, 110 million input tokens. It took 45 minutes and it cost me six bucks. You can even click in here and audit like how it looks. So, you can see that new edge cases are flagged and I can keep seeing where my agent is getting things right or wrong. So, I can find

**[7:58](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=478s)** when my agent is recommending the wrong medical care or has asked for things that are out of scope. To recap, I started with a simple task definition. I provided a minimal set of labels and I quickly iterated to a production-ready model. And this really matters for my business because I am recommending long-term care for people. I need it to be right. >> Our customers are already succeeding on Sutro. They're building quality and intent judges, support ticket classifiers, multimodal classifiers over healthcare data sets, PHI scrubbers, AI search tools, NER models, clinical trial data analytics, and much more. They're not just building evals. They're driving behavior directly into models via their our feedback-driven mechanism.

**[8:48](https://www.youtube.com/watch?v=9Z_FGK6lDxE&t=528s)** Now that you've seen what Sutro can do, it only leaves one question for the audience. What will you scale on Sutro? Thanks for listening and come find us after. >> [applause]
