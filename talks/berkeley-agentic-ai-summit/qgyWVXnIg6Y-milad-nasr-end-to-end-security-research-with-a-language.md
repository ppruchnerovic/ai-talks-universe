---
id: qgyWVXnIg6Y
title: "Milad Nasr - End to End Security Research with a Language Model"
slug: milad-nasr-end-to-end-security-research-with-a-language
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Milad Nasr"]
channel: "Berkeley RDI"
duration_min: 11
published_at: 2026-08-12T07:29:32Z
video_id: qgyWVXnIg6Y
url: https://www.youtube.com/watch?v=qgyWVXnIg6Y
youtube_url: https://www.youtube.com/watch?v=qgyWVXnIg6Y
tags: []
topics: ["Security, safety & red teaming"]
transcript: true
---

# Milad Nasr - End to End Security Research with a Language Model

**Milad Nasr**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=qgyWVXnIg6Y) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,705 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=2s)** MILAD NASR: So my talk is going to be slightly different from previous talk. It's mostly under research. So the idea starts from about two years ago, where I was in an event similar to this with a bunch of researchers from top frontier labs. And we were, as researchers do, trying to predict the future. And we had two questions at that time, two questions. One is how long it's going to take the agents do more than 90% of our coding. The second one is how long the agent's going to take to do more than 90% of our general research. And for the coding, we had a estimate of two to five years at the best and more than five years on average. And for our end-to-end research, it was more than 10 years. We were kind of wrong on the coding, maybe not that much, but, I'm going to show you, we were maybe very, very wrong on that.

**[0:54](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=54s)** So yeah, this is my talk. I've been trying to answer this question of, can language model do end-to-end research? My background is in security. So I'm going to focus on the security research, but some of these things might apply on other kind of research too. So yeah, by using LLM research, I don't mean using LLM as tools. As we know, many of the conferences, even security conferences, which are very, very conservative, allow you, to some extent, to use LLMs. And what I want to do is doing full end-to-end research, like from having idea, having a hypothesis, coming with a methodology to testing, and go beyond. And you might already have some answers here. Many people disagree.

**[1:40](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=100s)** Many people have a lot of doubts. And many people think this is impossible. I was one of them maybe two years ago. But I'm going to show you maybe we need to change that slightly. This week, actually, we published this work that we showed Claude can do cryptographic analysis. In particular, I'm going to focus on a specific part of it. What I mean by cryptographic analysis here is it can find flaws in cryptographic algorithms. And one of the works that we have is a small-- we found new attacks on a symmetric crypto algorithm called AES. But I'm going to show you, this attack is not possible to-- I don't have the capability of doing this attack.

**[2:31](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=151s)** And we have two authors here, me and Nicholas Carlini. And this is the academic record of us. Nicholas Carlini has a background in system security and recently on machine learning security. My background is on network security and nonmachine learning security. And two of us, plus a copy of internet, plus a bunch of coding agents, shouldn't be essentially do able to come up with a attack on cryptographic systems. And while we both like cryptographic a lot, and we have tried to break simpler things before, this is very, very big. And maybe to give a background on what is the actual AES and how does it work, if you ever used internet, you use the AES.

**[3:19](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=199s)** But it's a very, very interesting algorithm. It's been standardized in 2001 by NIST. And it's an iterative algorithm that has 10 rounds. Essentially, it gets an input and a key from you or from a program. And then it has four main parts. One is called substitution. The other one called-- and the other one is do some permutation. What substitution box does, it gets an input and maps it to another set of outputs. And then I move these bits around and add the function of the key that you add to the input. And it's an iterative algorithm. What it means is it tries to do this thing multiple times. And in the simplest forms of AES, it does this around 10 times.

**[4:09](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=249s)** And just for clarification, we didn't break AES. If someone breaks AES, they break internet. So it's a very academic work that I'm going to present. But in particular, we focused on a reduced run AES. Instead of doing the full 10 rounds of AES, we do seven rounds. This is something that academic usually study. Because it is easier, it might be possible to get some improvement. And when you want to attack seven rounds of AES, the [? dumbest ?] algorithm that exists, that brute force every key, the computation complexity of it is around 2 to the 128 of operations, which is going to take us more than the time that our sun is going to nova. So it's not possible. Our best algorithm that exists, that came in 2013. It takes around 2 to the 99.

**[4:59](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=299s)** So maybe in [? 20,000,000 ?] years or something like that, you're going to finish it. And it's not for lack of trying. There are several works in this area, and they try to break this. It's a fairly well-studied problem. And we have this number now. We showed that we have an attack that can do this break on this reduced run, AES in 2 to the 89 or something like that, depends on how you actually count it. And we actually did some empirical evaluation. It's around 200 to 800 times faster. So maybe in around 1,000 years. I don't know how much important that is, but yeah. So how does this actually work? So the way that attacks on crypto algorithms usually work

**[5:51](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=351s)** is they try to find the relationship between input and output without actually you trying to run the algorithm itself. And in particular, AES uses a specific formula to do this, like substitution. That takes an input, inverts it in some field, and then scales it and shifts it. So assume you have an object and you scale it and shift it. What remains is the ratio between this shape is still the same. It's just shifted and zoomed in. So the model understood that as AES-- this box has this property and uses this to come up with the algorithm. It's a very, very complicated method. I'm trying to give a summary of it in two minutes. So if you are interested, go read the paper.

**[6:40](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=400s)** And actually, we showed that this is not just AES. We can have attacks on other cryptosystems, such as HAWK and LEA, which both are used-- HAWK is one of the post-quantum algorithms. LEA is used in other countries. And none of these attacks has actually changed anything in the internet. But these are academic achievements. And so hopefully, you have an idea what is the attack. And I'm going to give you an idea of how we actually did this. So if I wanted to do this, I would have said somewhere, try to think for a few weeks. Come up with a few ideas, then go talk to a few people. And then maybe we come up with a few of the ideas and then go implement them. But how the model does this is slightly different.

**[7:28](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=448s)** They come with a lot of ideas. And instead of go talk to people, they try to go implement all of them to see which one is actually working. And maybe we had this saying before that ideas were cheap and the execution is everything. Now, maybe ideas is more important, and execution model can do it very, very fast. In particular, for AES, it's hard to do execution, because, as I showed, the complexity of is more than we can have. So we cannot just go implement that to the 89 or whatever algorithm. So instead, we have this harness, which is-- I don't think it's very important, but you need to have a harness right now for the models to not go implement everything. So maybe in future, you don't need this.

**[8:15](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=495s)** But right now, at least, you do. So we have a harness that comes with the research idea. Go talk to a few other agents, think if the idea is good or not, and then go implement and then iterate on the idea. And if I go to show you how many ideas that we had, it's this many idea. If you want to navigate this slide, you have to start from the beginning, where we told the model, go [INAUDIBLE] AES, and then it have many layers of ideas where [INAUDIBLE] actually find an algorithm. This slide might not have that much useful information. This might have more. The model had around more than 3,000 ideas. Off of those, more than 2,000 of those actually applicable to the problem.

**[9:04](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=544s)** Of those, around 200 were actually not-- it was novel ideas. And of all of those things, only four get to the paper. So we spent a lot of compute-- you have to, to get to the paper. So maybe all of the things I showed you was mostly in the cryptographic. And I tell you, so one question that a lot of people have is just, maybe just we are bad at crypto, and that's why we have these cryptographic results. And it might be true. I don't have crypto background. So something that impresses me might not impress anyone else. But we actually showed this result to actual cryptographic people and they actually were interested in the results. But you might also argue, maybe humans, in general,

**[9:54](https://www.youtube.com/watch?v=qgyWVXnIg6Y&t=594s)** bad at crypto. Maybe. I don't know. But we actually not only look at crypto. We are looking at a lot of other security research, which I have more background from, like network and network security, to do more like-- to go to privacy and everything else. And we showed, we have actually promising results in all of them. We are spending most of our time verifying the results. And finally, what I want to say, we used to say we need a novel and good idea at the same time. But as we are showing that-- and one of the beliefs was LLMs are maybe good at each, but not good at them at the same time. But maybe this is a starting to move. Thank you. That's all.
