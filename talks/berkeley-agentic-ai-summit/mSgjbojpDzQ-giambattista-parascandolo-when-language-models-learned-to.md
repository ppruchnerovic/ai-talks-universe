---
id: mSgjbojpDzQ
title: "Giambattista Parascandolo - When Language Models Learned to Reason"
slug: giambattista-parascandolo-when-language-models-learned-to
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Giambattista Parascandolo"]
channel: "Berkeley RDI"
duration_min: 8
published_at: 2026-08-11T05:07:06Z
video_id: mSgjbojpDzQ
url: https://www.youtube.com/watch?v=mSgjbojpDzQ
youtube_url: https://www.youtube.com/watch?v=mSgjbojpDzQ
tags: []
transcript: true
---

# Giambattista Parascandolo - When Language Models Learned to Reason

**Giambattista Parascandolo**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=mSgjbojpDzQ) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,564 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=1s)** GIAMBATTISTA PARASCANDOLO: There's this saying that there is nothing more stale than yesterday's newspaper. Well, these slides are five years old. Every single one is from four to five years old. So why are these slides old? I'm basically going to show you some of the earliest presentations that we had internally at OpenAI, when we started work on reasoning. So this talk is not about the future. The slides are also really ugly, because these were never meant to be presented in any occasion like this one. So these are just slides for our teams from a long time ago. So think about it more as a, whatever, time traveling and seeing what was like to work on reasoning a while ago. So first, what is reasoning? Again, these are the old slides.

**[0:48](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=48s)** So maybe one way to think about it is to say, there's a big space of problems of all kinds of subjects. And then you could think of this colorful wheel as all the different things you could be thinking about. So there's AI, and math, and physics, and biology. And then let's say, the central radial axis is difficulty. So as you move the angle, you change the subject. As you move away from the center, you change the difficulty. And so the main thing we're having at the time is that we were pre-training all of these models, like GPT-2, and 3, and 4. And then the circle of problems they could solve would expand from the middle. And they would cover all of the subjects a little bit and solve slightly harder and harder problems as we went. But then the main issue is, when were we

**[1:35](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=95s)** going to solve the really hard problems, and then if you think about some of the human experts in different subjects, for example, Andrew Wiles, who solved Fermat's last theorem, but this guy thought about this problem for seven years. But it's not like he could solve everything at the same time that took seven years to solve. He could solve one problem that took seven years. And most of the hard problems are like that. And so in some way, there was something about this process of just pre-training models to be better at general knowledge that seemed unlikely to eventually expand the circle all the way to cover all the hardest problems. So what do we do as humans? We think. We reason. So can we give models the same capabilities? So now, we're going to do something a little fancy. We're going to move this wheel in 3D. So we're going to tilt it this way. So pay attention, because it's only going to happen once.

**[2:25](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=145s)** So now, it's on the side. And we're going to move it to the side of the screen. And now, we can add the third axis, which didn't exist before, which is time, so thinking time. And then the question becomes, how do we expand these cylinders that don't really cover anything else, given more time? Maybe it might look a bit ridiculous today, but there was a time where you would give a model more time to think, and it would give you the exact same answer. Because after a few milliseconds, you would get the answer, and you would not know what to do with the extra time. And so thinking was this idea of, well, can we expand this cone over time? And not all at once. Again, you have to pick one little thing to focus on and then discover that. And so there were lots of practical problems. I'm not going to talk about almost any of them. But the thing to also think about

**[3:15](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=195s)** is, well, how long is this reasoning? Because again, Andrew Wiles thought about this for seven years. And so in terms of our models, well, at the time, they only had a context of a few thousand tokens, maybe 8,000 tokens. And then what can you do with 8,000 tokens? Well, at most, a few seconds of reasoning. And so there are lots of interesting questions of-- even if we get them to reason, then how is it going to happen? Now, the other issue was, we didn't know what reasoning would use as a substrate. There were lots of different ways you could spend test time compute. You can have a recurrent neural network and do lots of steps internally. What turns out, that text worked really well. And so again, these are some very old slides. Actually, it was my first project when I joined OpenAI. And then it's going to show you a little exploration of what models could do, but just asking them to think when they were not

**[4:07](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=247s)** ever trained to think. And this is one of the pieces that gave us confidence to scale things up. And so again, these are the old slides. The pitch was, what if we just ask them all to think about it? And so I had a bunch of examples. We're going to go through them. Again, they're very silly for today's standards, but it's good to see how far we went in such a short amount of time and where we used to be at the time. So at the time, you could ask GPT-3 a simple math problem. There are 29 bags of potatoes, and then 17 more. And there's plenty of bags. And the model would say that there is 46 kilos of potatoes. It's obviously completely wrong. And so one of the first exploration was to just add-- let's think about it before getting the answer. And then the thing you would get is you wouldn't get an answer right away. The model would start to output some extra text. But then eventually, you would get the right answer.

**[4:57](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=297s)** And of course, not all the time, but at least, sometimes, compared to never. So then we kept going. A bunch of questions of a clarinet, a piano, a dog. How many musical instruments do I have? Model said one. That's, of course, wrong. Clarinet and pianos are both instruments. You would break it down to think about it step by step. And then you would get-- a dog, it's not a musical instrument. A clarinet is a musical instrument, but a piano is not, so it's still one. And so then you would try to think, OK, well, if this model only thought a little longer. And so you add. Well, also break it down step by step. And then say, well, first, we have a dog. A dog is not a musical instrument. And then a piano is a musical instrument, a clarinet is. And so then you get the right answer. Here's one more example. There's a chair lamp, an oven, lots of things.

**[5:46](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=346s)** And then the model would say 20. And the answer is 14. Back in the days, you could check, what was the probability of getting the answer 14 out of the model? And the probability was 2%. So basically, almost never. Then again, you add, let's think about it, break it down step by step. And then you would get this long list when the model counts one by one. And somehow, you get a better answer. So this intuition seems good. Then how do we make it quantitative? And this was one of the first plots about, what happens if we get this model to think for longer? And so these are the last two plots I have to show you. This is just if you do this trick of asking the model, think step by step, and then think step by step, break it down, and keep adding sentences to say, look, I really want you to do all the work, and show all your work, and make sure there are no mistakes. And so we went from this model that could barely solve problems

**[6:35](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=395s)** by just adding things get to models that could solve more and more problems by thinking longer. And so the last plot I want to add is this one, which should have gone with the other one. And this is the average length of the solutions generated by the model when you ask it to solve a problem. And so again, at the beginning, you would get almost nothing if you just ask to solve. And then as you kept adding instruction, and you had to use this trick of saying, first, comma, so the model wouldn't, again, just try to answer and get into this mindset of, OK, it's going to be a long list of things I need to do. So first, there's something, then there must be a second and a third. And so let's try to output a lot of text. And so as the amount of text the model was outputting was increasing, then the accuracy of the model was going up. Yeah. And so since then, lots of other people worked on this. We did a big project.

**[7:22](https://www.youtube.com/watch?v=mSgjbojpDzQ&t=442s)** And then lots of other components we can't talk about yet, but yeah, very humble beginnings, one of many. And I thought it was interesting maybe for you guys to see this in the midst of this talks about the future. All right. That's all. Thank you. [APPLAUSE]
