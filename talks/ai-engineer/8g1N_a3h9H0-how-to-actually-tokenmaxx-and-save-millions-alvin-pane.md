---
id: 8g1N_a3h9H0
title: "How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival"
slug: how-to-actually-tokenmaxx-and-save-millions-alvin-pane
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Alvin Pane"]
channel: "AI Engineer"
duration_min: 11
published_at: 2026-10-14T15:00:14Z
video_id: 8g1N_a3h9H0
url: https://www.youtube.com/watch?v=8g1N_a3h9H0
youtube_url: https://www.youtube.com/watch?v=8g1N_a3h9H0
tags: ["AIE NYC 2026", "Livestream Priority 18", "Online Talk"]
topics: ["Evals, observability & reliability", "Prompting & context engineering"]
transcript: true
---

# How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival

**Alvin Pane**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#AIE NYC 2026` `#Livestream Priority 18` `#Online Talk`

[Watch the recording](https://www.youtube.com/watch?v=8g1N_a3h9H0) · [Conference site](https://www.ai.engineer/)

## Description

A cheaper candidate model disagrees with the production model on 18% of examples. Reject it immediately, or first ask how often production disagrees with itself? Alvin Pane uses that question to frame a token optimization workflow at OutRival. Repeated runs of the existing model reveal a reported 7% disagreement rate, making simple model to model agreement an incomplete quality measure. His HarborBite example is a synthetic proxy for a large instruction prompt, used to show the mechanics of reducing cost while preserving the application's required behavior. It is not evidence of realized million dollar savings.

Pane starts with observability: record prompt versions, model choices, tokens, latency and costs before changing them. Prefix caching removes avoidable repeated work. DSPy and GEPA can then search for shorter instructions, preserving the interface and scoring contract rather than simply deleting text. The illustrated prompt shrinks by 51%, but that reduction still needs a quality test. A smaller model may fit a narrow benchmark and fail on unfamiliar inputs. Shadow evaluation therefore compares production with itself, the candidate with itself and both systems on the same requests. Human review of disagreements separates regressions from improvements and ambiguous cases. A paired confidence interval around the net gain supplies a release criterion, with critical customer categories checked separately so an overall average cannot hide damage to an important task. The closing rule is to keep measuring after release: cheaper instructions and tokens matter only when the system continues to perform the work users need.

Speaker info:
- https://www.linkedin.com/in/alvin-pane/

Timestamps:
00:00 - A synthetic prompt and the cost of redundant work
1:34 - Observe tokens, latency and prompt versions
2:26 - Candidate disagreement and production variance
4:00 - Prefix caching and optimizing instructions with DSPy and GEPA
6:00 - Smaller models and benchmark overfitting
7:30 - Three comparisons in a shadow evaluation
8:46 - Human review and paired release criteria

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*1,585 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=0s)** Hey everyone, I'm Alvin, the head of agent intelligence at OutReval. By now, everyone's heard of token maxing. People have built leaderboards inside companies for who's using the most AI tokens. At Meta, they even had a title for this, tooken legend, a badge of honor for whoever's burning the most compute. It's a funny meme, but if you're actually shipping a product, token usage is a bizarre measurement of success. Tokens aren't the work. They're what you pay to get the work done. At OutRrival, our digital workers handle complex tasks over phone, text, and email. At the application layer, we're processing billions of tokens every single day. And when you operate at that scale, every redundant model call compounds into massive latency and millions of dollars

**[0:48](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=48s)** in compute costs. Take a look at this prompt. I've built a synthetic proxy that mirrors what structural bloat looks like in a pipeline. Let's pretend we're classifying customer intents for a fictional company called HarborBite. We've all seen one of these. It's got 20 edge cases, overly pedantic definitions, and a paragraph practically begging the model not to hallucinate. When you're sending this much text on every single request, millions of times a day, it isn't just a prompt anymore. It's a massive self-inflicted compute tax. If you want to give your agents more capabilities, you need the architectural headroom to do it. So today, we're reclaiming token maxing. It shouldn't be about burning the most tokens, but about extracting the maximum surface area of intelligence from the absolute minimum

**[1:36](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=96s)** token payload. So here's how to actually token max. Let's get into the playbook. First, observe. You can't fix what you can't measure. Instrument your shared model client so each attempt becomes part of a trace connecting the model calls, tools, and retries for a single task. Record the prompt version, model settings, token usage, latency, and cost. Open telemetry is a great framework for tracking this. Now that you have that telemetry, you can actually build a benchmark of how production is behaving. But here's where most optimization efforts hit a wall. Let me tell you how it usually goes. You take your massive prompt, you hand it to a smaller, cheaper model, and you run it

**[2:26](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=146s)** against a few thousand of those historical production examples. We did this. Our cheaper candidate model disagreed with our expensive production baseline about 18% of the time. So naturally, we threw it out. It wasn't good enough. But what does that 18% actually represent? Because language models in production are dealing with inherently ambiguous real life inputs, that 18% is actually a composite metric. It introduces a critical hidden variable, the baseline variance of the model itself. When the input is messy, your production prompt will inevitably disagree with its own past decisions.

**[3:14](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=194s)** So to isolate that hidden variable and understand what your rewrite actually changed, we asked a really dumb question. Does prod even agree with prod? We ran an AA test. We call this the ceiling test. We took our massive expensive production model and ran it three separate times on the same inputs and compared the answers. We discovered that it disagreed with itself roughly 7% of the time. Production's own agreement was only about 93%. So we were demanding a standard of perfection from the cheap candidate that our existing expensive system couldn't even hit. Once you establish that ceiling test benchmark, you finally have

**[4:02](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=242s)** a measured baseline. Now you can start making the work cheaper. There are three technical levers I like to pull and they run in a sequence. The very first is caching. Specifically, structuring your prompts to maximize your prefix cache rate is a really easy and really effective way to bring down the cost to run given tasks. The second lever is to actually shrink the footprint of the prompt itself. So, let's bring that Harborbite prompt example back up. This prompt is almost 5,000 tokens long. And why? Because over time, developers kept bolting on paragraphs of rules. For example, do not confuse enthusiasm with authorization is one such example.

**[4:54](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=294s)** Uh, plus massive hard-coded transcripts that were acting as worked examples. Nobody wants to be the one who deletes a line and breaks prod. So what do you do? You automate it. You turn prompting into a search problem. With a framework like DSPI, you can actually stop manually writing instructions. You define the exact interface contract, the inputs, the required output schema, and the scoring function. And then you hand it off to an optimizer like Jeepa. The optimizer treats your prompt as a search space. It runs against your benchmark attempting to match those historical labels. And it uses feedback on failures to revise the instructions.

**[5:43](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=343s)** It stripped out almost all of our long worked examples and replaced them with compact rules. A 51% reduction in instruction tokens with the same application contract. Now we can move to test whether quality holds. That is instant margin. The third lever is to actually downsize the model. Now that you have a tight prompt and a measurable search loop, you don't always need a massive frontier model. You can start aggressively cutting compute. There are two interesting strategies here. First, you can break a massive prompt into smaller components. you use a cheaper model to handle something like initial routing or data extraction and only wake up your expensive frontier models for

**[6:33](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=393s)** heavy reasoning. Second, you can use that exact same DSPI search loop we just built, but plug a smaller model into it. You let the smaller model search its own prompt space to match the benchmark answers generated by your large production model. You're essentially using Jeepa to teach a tiny model to match the task performance of a massive one for your specific data set. But the reality of optimization is not quite so easy when it comes to these small models. Um if you're trying to compress the behavior of a large model into a smaller one, you'll notice that you introduce new points of failure and overfitting. Um, and in many of our downsizing experiments, uh, we found that the prompts weren't good enough to

**[7:22](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=442s)** release, which brings us to the final hurdle. We've cut Harbor's prompt in half, but now we have to prove that we actually didn't break the product. Remember, these models are probabilistic. Production doesn't always agree with itself. And likewise, our new cheaper candidate is also going to have its own internal variance. So you run a massive shadow deployment on the exact same inputs and measure the system from three angles. Production against production, candidate against candidate, and candidate against production. There's a useful bit of math here. You take the disagreement between the two versions and subtract the average disagreement inside each one. What's left gives you a measure of how different their decision

**[8:12](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=492s)** probabilities are. This is where that ceiling test pays off. We aren't guessing. We have a mathematical baseline for how much these answers move around when we haven't changed a thing. And here's the secret about that drift. Different doesn't automatically mean wrong. If your optimizer did his job, the distributions should be different because the cheaper prompt is actually doing a better job. We aren't necessarily trying to build a perfect clone of a production system that may already have some flaws baked into it. So, you stop panicking about the raw differences, you pull the diffs, and you manually review some of them. Was the candidate better? Was production better? or were they just two different equally acceptable ways to handle an ambiguous

**[9:00](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=540s)** input? For Harbor Bite, let's say the completed review confirmed 443 regressions, but it also found 2,463 outright improvements. That is almost six improvements for every one regression from a prompt that is half the size. But you do not ship on a point estimate. You have to account for sampling noise. We measured a massive gain on this specific batch of requests, but we need to know exactly how much statistical confidence we can put behind it. So, we calculate a confidence interval around that net gain. You keep the comparison strictly paired, both versions answering the exact same request, and you keep the repeated runs of the same conversations grouped together. To say the candidate

**[9:47](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=587s)** is better, we want the lower confidence bound above zero. If the interval crosses zero, we need more evidence before making that claim. And one final sanity check is that you have to run this math on your critical categories separately. A great global average can actually uh silently hide that one vital customer intent is tanking. If your critical categories hold up and your lower confidence bound is above zero, you have your answer. Ship it and keep measuring. So this process is how you can replace the guesswork of prompt engineering with an explicit release rule. Cache the obvious stuff. Let an optimizer shrink your instructions. Rightize your model and use the ceiling test to understand the variation. Then

**[10:37](https://www.youtube.com/watch?v=8g1N_a3h9H0&t=637s)** test whether quality holds. So here's your homework for Monday morning. Go pick your most expensive task. Measure your baseline variance. put it through a search loop and find out exactly how much bloat you're paying for. We need to reclaim token maxing. Let the rest of the industry fight for the high score on the leaderboard. The real token legends are the ones making every single token count.
