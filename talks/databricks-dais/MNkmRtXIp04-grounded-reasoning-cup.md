---
id: MNkmRtXIp04
title: "Grounded Reasoning Cup"
slug: grounded-reasoning-cup
conference: databricks-dais
conference_name: "Databricks Data + AI Summit"
category: "Vendor events"
edition: "DAIS 2026"
year: 2026
speakers: []
channel: "Databricks"
duration_min: 10
published_at: 2026-08-17T20:15:45Z
video_id: MNkmRtXIp04
url: https://www.youtube.com/watch?v=MNkmRtXIp04
youtube_url: https://www.youtube.com/watch?v=MNkmRtXIp04
tags: ["Databricks"]
topics: ["Evals, observability & reliability"]
transcript: true
---

# Grounded Reasoning Cup

**Speaker not identified**

`Databricks Data + AI Summit` · `DAIS 2026` · `2026` · `10 min`

`#Databricks`

[Watch the recording](https://www.youtube.com/watch?v=MNkmRtXIp04) · [Conference site](https://www.databricks.com/dataaisummit)

## Description

How well do AI agents generalize to unfamiliar, enterprise-style grounded reasoning tasks?

This is the question that inspired the inaugural Databricks Grounded Reasoning Cup, which brought together 11 academic teams to compete live on OfficeQA Pro V2, a new grounded-reasoning benchmark built from approximately 1,400 U.S. Treasury PDFs spanning more than 200 years.

In this video, we go behind the scenes to learn what led the Databricks Research team to develop OfficeQA, and watch as AI Agents are evaluated in real time at the Grounded Reasoning Cup. Which teams came out ahead? Watch to find out.

Evaluating AI Agents Live on OfficeQA Pro V2
Interested in learning more? Check out our blog post & the OfficeQA Pro V2 benchmark on Github

Introducing OfficeQA Pro V2: A New Benchmark for Enterprise Grounded-Reasoning:

OfficeQA Github: https://github.com/databricks/officeqa

## Transcript

*1,658 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=MNkmRtXIp04&t=7s)** [music] [music] >> Benchmarks have always driven progress in machine learning from ImageNet to AlphaFold to StarCraft and Dota. To drive progress in the field that matters most for Databricks and our customers, we introduced OfficeQA a few months ago. >> We find all our customers are trying to

**[0:55](https://www.youtube.com/watch?v=MNkmRtXIp04&t=55s)** use AI to understand complex documents, data in their company, and uh it's really hard to tell if you got the right answer or the wrong answer because you just get back a number or text or something. So, we really want to make sure that AI can really nail that, uh and we wanted to design ways to measure that. >> Our goal in developing OfficeQA in the first place was to make sure it proxied as closely as possible the core challenges that our customers uh really care about solving with AI on a day-to-day basis. >> So, tons of customers are ingesting millions of documents and trying to pull out information from it. And unlike something like a coding agent where like you run the code and see, "Yeah, it's doing what I want." With these, you just get back a number. So, how do you know it's correct? So, that's why we want to do research and encourage research on

**[1:43](https://www.youtube.com/watch?v=MNkmRtXIp04&t=103s)** this problem. >> One of the great benefits of releasing a benchmark is that people will make their models and harnesses get better on it, which is exactly what we want for our customers. >> [music] >> But, it also means it's hard to tell how much better it gets for things that [music] are adjacent but not exactly the same as the benchmark. >> that a really fun and reliable way of being able to evaluate [music] that was having a live competition where teams actually needed to deploy their agents on a new fully unseen corpus in real time. >> We've created this grounded reasoning cup where we're bringing together the three frontier model providers and 12 student teams who will compete live on a new set of questions and [music] on a new data corpus provided by the Treasury. >> The data set is a fascinating one.

**[2:31](https://www.youtube.com/watch?v=MNkmRtXIp04&t=151s)** Though it's really been scattered across multiple different government websites. The [music] power of this data, why it's so special, is that it does provide a nearly uninterrupted view of 230 years worth of spending and revenue data on behalf of the United States. >> We went from some cases handwritten ledger statements to modern tabular accounting standards. >> [music] >> Hi, I'm Steve Ballmer, founder of USAFacts. I went looking for something simple, a clear accounting of what the government is spending and what results we're getting. It didn't exist. The data was there, but scattered across hundreds of agencies, reports, [music] databases, and even DVDs. >> It's a really interesting data set that

**[3:19](https://www.youtube.com/watch?v=MNkmRtXIp04&t=199s)** is so big and and [music] it's been so hard to use computers to sort of track down what's inside it before that it's never really been used. >> It's critical that the AI systems Americans rely on can [music] interpret that data correctly. And that's why I love what this event represents. It brings together three things I care deeply about. Data, AI, yeah, and some competition. >> [music] >> Your teams will be the first to apply cutting-edge AI agents to answer complex questions whose answers are buried in these documents.

**[4:07](https://www.youtube.com/watch?v=MNkmRtXIp04&t=247s)** >> You don't get several months of preparation for starting to work in a data set. You really have maybe sometimes a few hours and maybe sometimes a few days. >> So, we wanted to create questions that we could evaluate things like parsing faithfulness, uh reasoning capabilities, things like retrieval >> retrieval quality. >> This question asks for the total 1928 revenue from the Grand Canyon, Yellowstone, and Yosemite National Parks. To answer it, an agent must search a 120,000 page corpus, >> [music] >> extract values from the scanned documents, and accurately calculate the final total. >> Over the next 2 hours, you're going to witness six high-stakes rounds where 11 teams will use AI agents to tackle real-world enterprise challenges. >> So, these 11 academic teams have been working incredibly hard to uh with their mentor labs, OpenAI, Google, Anthropic. >> on the line. $120,000 in total.

**[4:55](https://www.youtube.com/watch?v=MNkmRtXIp04&t=295s)** >> First place, $60,000 in Databricks credits. >> Second place, 30,000. Third place, 10,000. And as well, top teams >> will also receive $10,000 prizes from each of the sponsors. >> For each of the six rounds, there's going to be uh 15 minutes for each round, and it is one point for the correct answer, and extra point 25 points for a speed bonus for the first team to get the answer correct across all of the rounds. And if there's a tiebreaker, speed wins. >> They built their agents, optimized their pipelines, and now the day is finally here to see who will be crowned the champion of the Grounded Reasoning Cup. >> Round one is officially live. This is [music] our warm-up round, but do not let that fool you. These questions are still tougher than your average trivia night at the pub. >> UMass [music] Amherst came out strong, taking early lead with an approach built

**[5:43](https://www.youtube.com/watch?v=MNkmRtXIp04&t=343s)** for speed. Their agent, powered by Claude Opus fast mode, was designed to move quickly and claim [music] the speed bonuses. >> They blazed out to a quick lead in the opening round, winning all but one of the speed bonuses, and maintained the lead through halftime. >> We're past the halfway point, and the stakes are getting real. >> Round four is our advanced capability round. Think web search [music] and multimodal reasoning. >> This round specifically is doing a lot more work with reading graphs, reading figures, even having things that need to access the web to find specific information. So, you can see now, I think Stanford, UBC, and U Chicago lead this round. >> UMass led at halftime by 10.25 points, but Stanford began to slowly close the gap as the rounds carried on. >> Wow, top four has all three different models present. This is a tight competition.

**[6:29](https://www.youtube.com/watch?v=MNkmRtXIp04&t=389s)** >> Awesome, awesome, awesome. >> This is it. THE FINAL ROUND, THE FINAL COUNTDOWN. THIS ROUND is filled with challenge questions, the ones even our agents struggle with now. If you can crack these, you're not just winning the competition, you're pushing the entire field forward. >> Because round six was double jeopardy, the point values were doubled. Correct questions were two points, and the speed bonus was half a point. It took more than five minutes for the first point to be notched on the hardest questions of the sixth round, and slowly Stanford started to claw back more of the lead. >> Stanford and Amherst are really close, neck to neck right now, okay? And there's only a 0.25 difference between these two schools, and Stanford has one resubmission left. >> They originally had a slow verification agent they had turned off after round

**[7:16](https://www.youtube.com/watch?v=MNkmRtXIp04&t=436s)** one. It had prevented them from claiming any of the speed bonuses, and on the easiest questions, hadn't flagged any errors. >> They turned it back on and went over their incorrect answers, hoping it would find something in the two minutes they had left. Then, with 56 seconds left, boom, they submitted their final answer, and it was right. Stanford passed UMass and won the grounded reasoning cup in literally the last minute. >> Let's go ahead and reveal the results. All right. Boom. So, number three is Yale, number two is Amherst, and number one IS STANFORD. CONGRATULATIONS. >> UMASS AMHERST. >> WOOHOO. UMass Amherst, coming up. >> What was your team's approach for the Grounded Reasoning Camp? >> Because yours really close. That was a very impressive, seriously. Head-to-head like that, that was really cool.

**[8:02](https://www.youtube.com/watch?v=MNkmRtXIp04&t=482s)** >> We spent a lot of time on pre-processing the corpus, so that basically our search methods can find things quicker, much quicker. >> All right. The first team place, we're beckoning them to come on stage. All right, I believe it was Stanford. Congratulations. [screaming] >> Initially, the verification uh engine was on, and it was slowing us down. And it was not changing the answer. So, after the first couple of rounds, we turned it off, saying that it's not helpful. >> [laughter] >> And it was off till the last round. But in the last round, we noticed that the difference was very less, so we manually ran the verification engine, it flipped the answer, and we just resubmitted. >> What is the most important thing for students to learn in terms of building responsible grounded AI systems? >> So, multiple iterations over the evals, run it 10 times, 100 times, make sure the results are consistent.

**[8:51](https://www.youtube.com/watch?v=MNkmRtXIp04&t=531s)** >> I think at Anthropic, we really believe in doing the simple thing that works. >> I've always believed in starting with the numbers. It was important for me to understand where the country was and was not allocating its resources. >> This benchmark is probably one of the best AI benchmarks in terms of how to handle unstructured data, and which tool to use, the scaffold, the harness, which part should go to memory, how to index. >> There are great technologists and great data stewards all across the US government, and bringing them together with the AI labs is really an opportunity for all of us to benefit. >> The really interesting thing is that we kind of released this in collaboration with the Treasury and the USAFacts. And this really kind of

**[9:39](https://www.youtube.com/watch?v=MNkmRtXIp04&t=579s)** coincides with the 250th anniversary of the United States of America. And in some sense, this data set kind of describes how the economy of the United States developed over the last 250 years, and also just the history of the country. >> [music] [music]
