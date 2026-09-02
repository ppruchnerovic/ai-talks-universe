---
id: UTcKagbKp4A
title: "Aayush Agrawal - Evals: The Engine for Agent Improvement"
slug: aayush-agrawal-evals-the-engine-for-agent-improvement
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Aayush Agrawal"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T07:53:22Z
video_id: UTcKagbKp4A
url: https://www.youtube.com/watch?v=UTcKagbKp4A
youtube_url: https://www.youtube.com/watch?v=UTcKagbKp4A
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Aayush Agrawal - Evals: The Engine for Agent Improvement

**Aayush Agrawal**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=UTcKagbKp4A) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,107 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=UTcKagbKp4A&t=1s)** AAYUSH AGRAWAL: Well, give a round to you all because you're here till the end. This is a full-day event, and I'm really proud of you all for being here. So just thank you for being here towards the end. I'm well aware that I'm the one who's in between you all, from being here and a beautiful Berkeley day outside. So let's try to warm up the room and see who's here. So firstly, super simple one who took an Uber today? Quick raise of hands. We have a few. That's great. But more importantly, who actually wrote an eval for an agent in production? Let's see who are the real builders. Cool. And now, the last one You have to be proud of this. Did those evals tell you something that changed the way that you shipped your product? Great great.

**[0:50](https://www.youtube.com/watch?v=UTcKagbKp4A&t=50s)** So that the difference between having evals as a checkbox versus an eval actually changing your product direction, that's what we spent over a year at Uber trying to make sure that every agent team was able to do. And I'm going to talk to you all about that today. So, at Uber, we've been shipping agents throughout our ecosystem, both for external agents so you can book a ride through your voice, as well as internally. And the thing that's powering all of that at enterprise scale is our Uber agent platform, which I manage. And there's a bunch of different components across that to help agent teams not worry about the infrastructure. And the thing that I'm going to talk about today is evals, which is what this room is all focused on, which is really exciting. So, one thing that we saw across the board is that every team wanted high quality production agents, but they started to do one common thing.

**[1:39](https://www.youtube.com/watch?v=UTcKagbKp4A&t=99s)** They said that, hey, let me just ship the agent, and I'll think about evals later. And it was a very rational decision. Because for them, they just wanted to go prove product market fit. They wanted to see if it even worked. But what that did was that-- then they got caught in this relentless loop of retrofitting evals later and trying to figure out, why did that agent break? And so what we found was that there were true fiction points that teams had that were preventing them from getting to that state earlier on. And we, as a platform team, decided to make that frictionless for them. So let's talk about those to make evals default. So the first thing, and this was kind of mentioned across the board, is the starting is tracing. And so what we did was we made sure that as soon as the first development started, they had tracing at every single environment. And what that allowed teams to do

**[2:27](https://www.youtube.com/watch?v=UTcKagbKp4A&t=147s)** is understand and have a foundation for setting up the rest of their evaluations. They could just build an agent vibe with it, send it out. And all of the information of how it's been changing over time is there and not something they have to add retrofit. The second was that once they were able to get their data, how to get insights out of it. Teams didn't know how to start with developing an eval. They didn't know what was the best way to write it or where. And so what we did was that we had the context of how the agent was built, the documentation around it. And we figured out what is the best starter kit evaluators and send those insights directly to the builders in Slack so that they could understand, hey, I don't know what an LLM judge is, but I do know what it means to have a tool contradiction

**[3:16](https://www.youtube.com/watch?v=UTcKagbKp4A&t=196s)** and make a change because of that. What we also saw is that evals with agents is very different. They are not QA tests that are purely engineering. But we needed to bridge that gap so that the teams that are closest to the customer, like product and customer teams, had an ability to understand those. CLI experiences really democratized that. And so by building skills that managed the eval, we saw that teams were able to allow their product teams to own this entire process. Finally, this is something that we couldn't build a tool away for. It was changing the narrative around what an eval is meant to do. So we changed teams' narratives from, hey, is your evals 90% plus? To do you actually trust your evals? What have you done and changed about your roadmap

**[4:06](https://www.youtube.com/watch?v=UTcKagbKp4A&t=246s)** because your evals have told you that? And how quickly have you been able to update your data sets? Is your data set five months old and not really up to date with your product? All of this helped us ship products faster and catch issues much earlier in the product lifecycle. So, what we're launching really soon is a rider voice booking in Uber. And what we saw with our evals was that although we had a 95% plus offline eval, when we saw a production eval showing us that the number of turns per session were way higher than average, we looked into that deeply and saw that, hey, there's actually customer that is trying to book a ride to SFO. But somebody in the background said, hey, I want pizza. And the agent took that as an input and started rerouting them to the nearest pizza space.

**[4:56](https://www.youtube.com/watch?v=UTcKagbKp4A&t=296s)** And so, we realized that we needed to have the agent understand true intent and have no ops where it was not needing to be listened to. So that was only possible because we had evals as well as the products teams in the loop. So this is the evolution we had at Uber, where we had evals of the default come in because of these interventions. And now, we're moving to evals as this engine. And this is where we're really excited, where traces go into failures which are automatically categorized, and then get proposed as updates to the agent, to the evaluators. And the teams are basically accepting and rejecting that. And that improvement feedback loop is what really helps teams bring agents that customers really love. And so that's the difference between having an eval metric. That's a score for something that you know,

**[5:45](https://www.youtube.com/watch?v=UTcKagbKp4A&t=345s)** versus an engine that helps you continuously improve agents tune towards what the customer cares about. That's what makes each of your trips magical at Uber. And we're excited to continue building this out. Thank you. [APPLAUSE]
