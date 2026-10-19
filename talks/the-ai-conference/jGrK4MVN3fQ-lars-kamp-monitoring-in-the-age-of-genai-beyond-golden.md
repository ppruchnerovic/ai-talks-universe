---
id: jGrK4MVN3fQ
title: "Lars Kamp: Monitoring in the Age of GenAI: Beyond Golden Signals"
slug: lars-kamp-monitoring-in-the-age-of-genai-beyond-golden
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 11
published_at: 2026-10-07T22:53:56Z
video_id: jGrK4MVN3fQ
url: https://www.youtube.com/watch?v=jGrK4MVN3fQ
youtube_url: https://www.youtube.com/watch?v=jGrK4MVN3fQ
tags: []
topics: ["Security, safety & red teaming"]
transcript: true
---

# Lars Kamp: Monitoring in the Age of GenAI: Beyond Golden Signals

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=jGrK4MVN3fQ) · [Conference site](https://aiconference.com/)

## Description

The four golden signals (Latency, Errors, Traffic, Saturation) have been the foundation of application monitoring for years, and it still matters, but for GenAI applications, these signals alone leave significant blind spots. A request can return 200 OK with low latency while the response hallucinates, leaks PII, or costs much more than expected. This talk will walk you through what changes when you're monitoring non-deterministic, token-priced, prompt-injectable systems. We'll cover three additional monitoring dimensions — Cost (token attribution, model-mix tracking, wasted spend on failed requests), Safety (prompt injection detection, PII scanning, jailbreak attempts), and Quality (hallucination rate, relevance scoring, user satisfaction) — and show why each one is necessary alongside your existing instrumentation.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,879 words · source: supa (en, exact timings)*

**[0:16](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=16s)** So, uh let's talk a little bit about monitoring in the age of agents. Uh I'm part of product engineering senior staff member here at Datadog. And once upon a time, we used four golden signals. If you've read Google's book on uh site reliability engineering, then you will remember this. Um and these were completely spot-on for about a decade. Uh now, my headline is obviously a little bit tongue-in-cheek because these all still apply. But as we're going to see with agents, the game changes a little bit, and we can't really rely on the responses that we get from our monitoring here. So, let's talk a little bit about the detail what changes when we go from software to agents. So, for uh we we built for decades we built software on the assumption that

**[1:04](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=64s)** everything is deterministic, right? So, you built software, it does one thing, and it only does what? One thing. And when something breaks, you know, you would get an exception. Uh and uh success was really binary. Uh for um for your uh security, you would check uh vulnerabilities at runtime, or you would run scans on a periodic basis. And finally, you had some server um fixed compute costs, and yeah, once you control that, nothing would really change. >> [snorts] >> Now, it's really different with agents, where you're shifting from deterministic logic to probabilistic reasoning, right? And so, agents make judgment calls. And uh what changes too is like you can have the same prompt, and maybe a minute later that judgment call changes. Um and in fact, you can experience silent

**[1:51](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=111s)** degradation, hallucinations, right? And so, the output of your responses might degrade over time. And uh it's a spectrum of quality that you have. So, it's not like yes, no, binary, pass, fail. The quality of your output can change over time. Uh on a security from a security perspective, I'm sure you've all heard about prompt injection, but what happens is that we've seen attacks at runtime, injections from various vectors. We'll talk about that in a little bit. And finally, I'm sure everyone is aware of variable token costs. So, really, that's the big switch and um if there's one slide you want to take home, I think it's this one. Okay. So, uh let's talk about these three specific here um cuz we the title of the talk is monitoring in the age of agents. So,

**[2:39](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=159s)** three things. Uh we're going to talk about quality, security, and costs. And in detail, uh why? Well, num- number one, what changes is outputs are non-deterministic, right? So, you kind of want to know is like, "Okay, is it actually right? Is it good? You know, is my model hallucinating?" Evaluations um on the second uh the second point is security. So, we've seen malicious inputs into uh into models uh into my agent overriding system instructions, and that influences what the agent can do all the way to um extracting sensitive data to uh to the outside of the company. And finally, there's cost, right? So, we want to know a little bit like, "What is driven What is driving my token consumption? And what can I do to stay within my uh budget?" All right. So, little bit of a framework

**[3:26](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=206s)** here. Uh I think I have a cool laser pointer. Uh if you can see this, right? So, this is conceptual. Give me some slack, right? To simplify today's talk. So, um an agent can fail and still produce a 200 response, right? And so, everything looks great, but in the middle, there can be lots of things that can go wrong. Um from this model here, so we have our agent, and the agent gets context, the agent gets a prompt in this also config file. Um Um that goes to the agent. Typically, there's an AI gateway that What's that noise? There uh that communicates with the models, multiple models. We've seen that a lot. And um what else? You have sub-agents. In theory, the sub-agents also go through the

**[4:13](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=253s)** AI gateway, but again, you know, this is conceptual. And finally, you have tools and MCPs that the agent can call. So, let's go through this what can go wrong here despite me getting a 200 response. So, let's talk about quality. So, again, we talk about quality, security, and cost, right? And so, quality um in traditional software, if you have a bug, you get a you know, a bug throws a 500 exception. But, inside an agent loop, this thing, you know, quality breaks quietly. Uh so, I've put these handy stars here on the slide. So, what are the things that can change, right? So, models can hallucinate. If you look at uh the context here, um they can produce contradictions. They those might oppose uh uh

**[5:02](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=302s)** retrieved context or make unsupported claims. So, we see that happening. Um prompt and config, right? Uh agent quality is fragile. Um a minor prompt tweak can actually change all the output at the end. And we've seen that a lot like when you try to improve um your agent, like you change one thing and uh those changes silently cause regress- regressions across dozens of others. So, um that that's one thing that can wrong. And then uh yeah, the model itself, right? So, Go on. That's quality. Number two, security. So, our attack vectors move to run time. So, I said like, you know, when you build software, you you do you know, you check for vulnerabilities at uh uh build time. You run periodic checks,

**[5:50](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=350s)** maybe every 24 hours you scan your infrastructure, but that's not enough. What we've seen is that prompt injection happens at runtime. Uh we have seen things to uh inject things into a config file and that just changes the behavior of the agent. On the tool side, MCP, uh what happens is as uh the agent calls MCP servers, that provides access to enterprise data. Um for instance, at Data Dog, you know, we have a very popular um data warehouse, Snowflake, and uh our entire enterprise data is in that data warehouse, and Snowflake has built a marvelous MCP server, and that really expanded usage to um to our own to an internal audience, and we saw some interesting queries, and so a lot of the things that we're building actually solving our own problems.

**[6:38](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=398s)** And uh yeah, finally then, that response might uh carry that extracted data outside of your uh enterprise perimeter. So, that's what can go wrong with security. Costs. Uh well, a model or your agent can just go into an infinite loop and keep spending tokens, and that's going to blow up your bill. I'm sure we've all dealt with that. Um again, the context here uh could be uh an issue. Context bloat is something, you know, at some point you get a you're going to get a response like, "Hey, my window is too big." And so, you're spending things there. >> [snorts] >> Um even um with the AI gateway, like depending on what model you pick, it's going to impact your uh your token bill at the end of the month. So, those are the three things that we care about. So, the question then is, what does good look like for my AI

**[7:27](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=447s)** agents, right? So, for quality, I want to catch my hallucinations. Uh I do want to run experiments, and I want to when I run these experiments, I want to prevent my prompt injection. For security, I have to block these threats at runtime, right? Because once they touch down down stream systems, it's too late. And finally for cost, I just want to have a finger on the pulse and also understand what I can do to reduce my spend, get more ROI from my AI investment. So, we built it. And as I said a couple of seconds ago, a lot of the problems that I talked about, these three problems, we've encountered ourselves as we built our own products here at Data Dog. Especially, we have two products that use agents. Bits AI is one, it's a chat experience that is woven through with the Data Dog product. We have AI

**[8:14](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=494s)** guard. That's a product for security. And as we built these agents, we've run into a lot of these issues. So, what we do is for quality, we try to catch hallucinations. We run a lot of experiments. And when we did that, we noticed like we get these regressions. And like it's like a one step forward, two steps back. And so, what do we do? We want to trace what went wrong, right? We want to know what's going on. In security, block it. Once a malicious prompt, we see it. Tools that are getting called around, say if we want to block all of that. And from a cost perspective, we just want to understand like, you know, what models, what users are driving the cost and what can I do about it. And that's what we built. This is actually an internal example. When you update from Data Dog's internal

**[9:06](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=546s)** product, agent observability, so when you update a prompt or rule, how do you make sure you don't you don't cause silent regressions somewhere else? And we learned that the hard way. And so, what we did now is we built this product where you can run plenty of experiments and just test how this impacts your output and your model's quality. The second one is security, um a product called AI guard, which again started internally as a project because we realized we got the weirdest submissions of the weirdest requests for our agent bits AI and you people try all sorts of things you know we operate at global scale so you find all edge cases that that people try to to break

**[9:54](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=594s)** your agent and so what we do is we evaluate every prompt and every tool call and the model response and we block it at the egg eye gateway if we see something is not working. And we we have unified tracing meaning we can correlate security detections directly with the LLM traces and our logs for fast investigation. And then to close optimize token spend for your company simple analytics understand what models what users are driving your cost what you can do to lower them obviously but it also helps you at the end of the day to understand make a case for your ROI for into your AI investment. And if you want to get started on data

**[10:43](https://www.youtube.com/watch?v=jGrK4MVN3fQ&t=643s)** doc two codes to scan one is agent observability two of the screenshots you saw today you'll get with agent observability and we have a generous free tier 4000 40000 LLM spans and then if you're startup we also give you credits data doc credits and up to 100k if you work for one of our partners and if you want to talk to me after this I'm available here and I think I've stayed within my 10 minutes budget. Thank you. >> [applause]
