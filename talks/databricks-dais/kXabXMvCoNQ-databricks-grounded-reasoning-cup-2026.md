---
id: kXabXMvCoNQ
title: "Databricks Grounded Reasoning Cup 2026"
slug: databricks-grounded-reasoning-cup-2026
conference: databricks-dais
conference_name: "Databricks Data + AI Summit"
category: "Vendor events"
edition: "DAIS 2026"
year: 2026
speakers: []
channel: "Databricks"
duration_min: 11
published_at: 2026-08-07T23:56:41Z
video_id: kXabXMvCoNQ
url: https://www.youtube.com/watch?v=kXabXMvCoNQ
youtube_url: https://www.youtube.com/watch?v=kXabXMvCoNQ
tags: ["Databricks"]
topics: ["Data engineering & MLOps", "Evals, observability & reliability"]
transcript: true
---

# Databricks Grounded Reasoning Cup 2026

**Speaker not identified**

`Databricks Data + AI Summit` · `DAIS 2026` · `2026` · `11 min`

`#Databricks`

[Watch the recording](https://www.youtube.com/watch?v=kXabXMvCoNQ) · [Conference site](https://www.databricks.com/dataaisummit)

## Description

How well do AI agents generalize to unfamiliar, enterprise-style grounded reasoning tasks?

This is the question that inspired the inaugural Databricks Grounded Reasoning Cup, which brought together 11 academic teams to compete live on OfficeQA Pro V2, a new grounded-reasoning benchmark built from approximately 1,400 U.S. Treasury PDFs spanning more than 200 years.

In this video we go behind the scenes to learn what led the Databricks Research team to develop OfficeQA, and watch as AI Agents are evaluated in real time at the Grounded Reasoning Cup. Which teams came out ahead? Watch to find out.

Evaluating AI Agents Live on OfficeQA Pro V2
Interested in learning more? Check out our blog post & the OfficeQA Pro V2 benchmark on Github

Introducing OfficeQA Pro V2: A New Benchmark for Enterprise Grounded-Reasoning:

OfficeQA Github: https://github.com/databricks/officeqa

## Transcript

*1,826 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=0s)** Benchmarks have always driven [music] progress in machine learning from ImageNet to AlphaFold to StarCraft [music] and Dota. To drive progress in the field that matters most for Databricks and our customers, we introduced Office QA a few months ago. >> We find all our customers are trying to use AI to understand complex documents data in their company and it's really hard to tell if you got the right answer or the wrong answer because you just get back a number or text or something. So we really want to make sure that AI can really nail that and we wanted to design ways to measure that. >> Our goal in developing Office QA [music] in the first place was to make sure it proxied as closely as possible the core challenges that our customers [music] really care about solving with AI on a day-to-day basis.

**[0:47](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=47s)** >> So tons of customers are ingesting millions of documents and trying to pull out information from it and unlike something like a coding agent or like you run the code and see yeah it's it's doing what I want. With these you just get back a number. So how do you know it's correct? So that's why we want to do research and encourage research on this problem. >> One of the great benefits [music] of releasing a benchmark is that people will make their models and harnesses get better on it which is exactly what we want for our customers. But it also means it's hard to tell how much better it gets for things that [music] are adjacent but not exactly the same as the benchmark. We decided that a competition would be the most exciting and also [music] accurate way to judge the performance of all of the models and harnesses in real time at one specific point before anyone's [music] ever seen the documents or the questions and had

**[1:37](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=97s)** any chance to train [music] or fit to the new data set. >> We've created this grounded reasoning cup where we're [music] bringing together the three frontier model providers and 12 student teams who will compete live on a new set of questions and [music] on a new data corpus provided by the Treasury. >> The data set is a fascinating one. Though, it's really been scattered across multiple different government websites. The power [music] of this data, why it's so special, is that it does provide a nearly uninterrupted view of 230 years worth of spending and revenue data on behalf of the United [music] States. >> We went from in some cases handwritten ledger statements to modern tabular accounting standards. >> Because the corpus is so long-standing,

**[2:26](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=146s)** [music] I think it also reflects this really interesting challenge that we have within enterprises where there is just tons and tons of institutional knowledge that accumulates over time. >> So, the US Treasury corpus that we decided to use for Office QA was actually originally suggested in a conversation we had with USA Facts. It's a really interesting data set that is so big and [music] and has been so hard to use computers to sort of track down what's inside it before that it's never really been used. >> Hi, I'm Steve Ballmer, founder of USA Facts. [music] We launched USA Facts in 2017 because I wanted to help people understand what's happening in America by the numbers. It's critical that the AI systems Americans rely on can [music]

**[3:14](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=194s)** interpret that data correctly. And that's why I love what this event represents. [music] It brings together three things I care deeply about. Data, AI, yeah, and some competition. >> Your teams will be the first to apply cutting-edge AI agents to answer complex questions whose answers are buried in these documents. >> get several months of preparation for starting to work in a data set. You really have maybe sometimes a few hours and maybe sometimes a few days. So, we wanted to create questions that we could evaluate things like parsing faithfulness, uh reasoning capabilities, things like retrieval quality.

**[4:02](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=242s)** >> This question asks for the total 1928 revenue from the Grand Canyon, Yellowstone, and Yosemite National Parks. To answer it, an Asian must search a 120,000 page corpus, extract values from the scanned documents, and accurately calculate the final total. >> Over the next 2 hours, you're going to witness six high-stakes rounds where 11 teams will use AI agents to tackle real-world enterprise challenges. >> So, these 11 academic teams have been working incredibly hard to uh with their mentor labs, OpenAI, Google, and Anthropic. >> I think our overall strategy, without giving too much away, is just [music] prediction is compression, and we just believe in Kaigo. >> When the question [music] requires calculation or structured reasoning, we use tools instead of asking the models [music] to do everything by itself. >> Now, here's what's on the line. $120,000 in total. First place, $60,000 in

**[4:53](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=293s)** Databricks credits. Second place, 30,000. Third place, 10,000. As well, top teams will also receive $10,000 prizes from each of the sponsors. >> The type of database problem that we've been wanting to solve [music] for the for the last 40 years, but was not able to because we are, you know, we're a system that wants uh clear, precise input in structured query languages. >> Prior to the six rounds, there's going to be uh 15 [music] minutes for each round, and it is one point for the correct answer, an extra point 25 points for a speed bonus [music] for the first team to get the answer correct across all of the rounds. And if there's a tiebreaker, speed wins. >> Grounded reasoning depends not only on the reasoning model itself, but also on the quality and reliability of every earlier step in the pipeline. >> They built their agents, optimized their pipelines, and now the day is finally

**[5:42](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=342s)** here to see who will be crowned the champion of the Grounded Reasoning Cup. >> Round one is officially live. This is our warm-up round, but do not let that fool you. These questions are still tougher than your average trivia night at the pub. >> UMass Amherst came out strong, taking early lead with an approach built for speed. Their agent, powered by Claude Opus fast mode, was designed to move quickly and claim the speed bonuses. >> They blazed out to a quick lead in the opening round, winning all but one of the speed bonuses, and maintained the lead through halftime. >> We're past the halfway point, and the stakes are getting real. >> Round four is our advanced capability round. Think web search and multi-modal reasoning. >> This round specifically is doing a lot more work with reading graphs, reading figures, even having things that need to access the web to find specific uh

**[6:29](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=389s)** information. So, you could see now, I think Stanford, UBC, and U Chicago lead this round. >> UMass led at halftime by 10.25 points, but Stanford began to slowly close the gap as the rounds carried on. >> Wow, top four has all three different models present. This is a tight competition. >> Awesome, awesome, awesome. THIS IS IT, THE FINAL ROUND, THE FINAL COUNTDOWN. THIS ROUND is filled with challenge questions, the ones even our agents struggle with now. If you can crack these, you're not just winning the competition, you're pushing the entire field forward. >> Because round six was double jeopardy, the point values were doubled. Correct questions were two points, and the speed bonus was half a point. It took more than five minutes for the first point to be notched on the hardest questions of the sixth round, and slowly Stanford started to claw back more of the lead. >> Stanford and Amherst are really close,

**[7:18](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=438s)** neck to neck right now, okay? And [music] there's only a 0.25 difference between these two schools, and Stanford has one resubmission left. >> They originally had a slow verification agent that they turned off after round one. It had prevented them from claiming any of the speed bonuses, and on the easiest questions, hadn't flagged any errors. >> They turned it back on and went over their incorrect answers, hoping [music] it would find something in the 2 minutes they had left. Then, with 56 seconds left, boom, they submitted their final answer, and it was right. Stanford passed UMass and won the Grounded Reasoning Cup in literally the last minute. >> Let's go ahead and reveal the results. All right. Boom. So, number three is Yale, number two is Amherst, and number one IS STANFORD. CONGRATULATIONS!

**[8:05](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=485s)** >> [screaming] >> UMASS AMHERST, WOOHOO! >> UMASS AMHERST, COME ON UP! >> WHAT WAS YOUR TEAM'S approach for the Grounded Reasoning Cup? >> I think yours really close. That was a very impressive, seriously. Head-to-head like that, that was really cool. >> We spent a lot of time on pre-processing the corpus, so that basically our search methods can find things quicker, much quicker. >> All right, the first team placed, we're backing them to come on stage. All right, BELIEVE IT'S STANFORD. CONGRATULATIONS! >> [screaming] >> INITIALLY, the verification engine was on, and it was slowing us down, and it was not changing the answer. So, after the first couple of rounds, we turned it off, saying that it's not helpful. And it was off till the last round. But in the last round, we noticed that the difference was very less, so we manually ran the verification engine. It flipped

**[8:52](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=532s)** the answer, and we just resubmitted. >> What is the most important thing for students to learn in terms of building responsible grounded AI systems? >> So, multiple iterations over the evals, run it 10 times, 100 times, make sure the results are consistent. >> I think at Anthropic, we really believe in doing the simple thing that works. [music] >> I've always believed in starting with the numbers. It was important for me to understand where the country was and was not allocating its resources. >> This benchmark is probably one of the best AI benchmarks in terms of how to handle unstructured data, and which tool to use, the scaffold, the harness, which part should go to memory, how to index. >> There are great technologists and great data stewards all across the US

**[9:41](https://www.youtube.com/watch?v=kXabXMvCoNQ&t=581s)** government and bringing them together with the AI labs is really an opportunity for all of us to benefit. >> The really interesting thing is that we kind of release this in collaboration with the Treasury and the USAFacts and this really kind of coincides with the 250th anniversary of the United States of America and in some sense [music] this dataset kind of describes how the economy of the United States developed over the last 250 years and also just the history of the country. >> [music] [music]
