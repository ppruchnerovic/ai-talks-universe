---
id: dFsws_PfGUk
title: "Hallucinations: Harvesting Uncertainty - Aygalic Jara - Paris-Saclay × SCIAM - dotAI 2026"
slug: hallucinations-harvesting-uncertainty-aygalic-jara-paris
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Aygalic Jara"]
channel: "dotconferences"
duration_min: 10
published_at: 2026-09-28T14:00:21Z
video_id: dFsws_PfGUk
url: https://www.youtube.com/watch?v=dFsws_PfGUk
youtube_url: https://www.youtube.com/watch?v=dFsws_PfGUk
tags: []
topics: ["Evals, observability & reliability"]
transcript: true
---

# Hallucinations: Harvesting Uncertainty - Aygalic Jara - Paris-Saclay × SCIAM - dotAI 2026

**Aygalic Jara**

`dotAI` · `dot conferences` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=dFsws_PfGUk) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Aygalic Jara, PhD researcher at Université Paris-Saclay × SCIAM: https://www.dotai.io/

Aygalic is a PhD researcher at Université Paris-Saclay × SCIAM, where he researches LLM reliability, focusing on hallucination detection, evaluation, and mitigation.

Lightning talk: "Hallucinations: Harvesting Uncertainty"

LLMs are startlingly confident even when they're completely wrong, and disclaimers, RAG, and tool use only take you so far. But there's a signal we mostly ignore: models carry a usable internal sense of when they're about to hallucinate, readable before generation starts and token by token as it proceeds.

This talk covers why hallucinations are structural rather than accidental, how uncertainty can be harvested from the model's internals, and what you can do with it: fine-grained hallucination detection, model and human escalation, abstention, and observability into the queries your system handles badly.

The goal: reframe model uncertainty as an engineering tool, not a research curiosity.

## Transcript

*1,714 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=dFsws_PfGUk&t=7s)** [music] [music] [music] [applause] >> How much do you trust AI? Please raise your hand if you ever used AI to plan a holiday trip. So a lot of people. I'm guilty as well. Um picture this. You want to plan a weekend trip in the mountain. You want to go for your first real hike. You're

**[0:54](https://www.youtube.com/watch?v=dFsws_PfGUk&t=54s)** thinking doing it for real, so you'll sleep in a refuge. You'll go and see a lake. And a pretty easy good trip. So you start researching everything. Um you stumble on to blog posts from the 2015 era. Everything is really long. Um half of the links are dead. Nobody agrees on how long anything takes. So you do the natural thing. You ask your favorite AI to come up with a plan for you. And it does. Now you know where to park, um where is the lake on the way. There's even a refuge to sleep in, so it's going to look great on the family pictures. Two hikers did exactly that in July, 18 and 19 years old. Um obviously they got lost. Um two out of the trail, they flagged down a park ranger, and they asked him for direction. He asked to see the map, and he discovered the AI-generated map. The lake were moved in The lake were moved in the wrong valley.

**[1:43](https://www.youtube.com/watch?v=dFsws_PfGUk&t=103s)** The walking time was straight out of nowhere. In his word, there was nothing right about this map. And the map never said it wasn't sure. It just drew a line. And hiking is the harmless version of that. Um sure that park ranger may have found like 30 people with similar map. But now this behavior is baked into healthcare, law, and defense. And the question is uh is this normal? Um nothing Notice what didn't happen out there. Nothing broke, no outage, no broken file. The LLM did exactly what it was supposed to do. Um it predicted the next plausible next thing. It's just that plausible and true were different. So, what is um is the training supposed to do that? If

**[2:31](https://www.youtube.com/watch?v=dFsws_PfGUk&t=151s)** you think about it, that is the training to predict the most possible next thing. Uh you know it works. It's next token prediction over and over. And when you go on data sets such as Wikipedia, it doesn't say I don't know. Um it just give you the answer. And so the LLM is never trying to express uncertainty. And sure, you can train it back in. But if you push this too far, it starts to refuse to answer to question it might have had the answer to. And so when you're benchmarking something, you want your model to try to answer instead of saying I don't know. So you want it to take shots. But the thing is this is uh a worse behavior, but it enhances yeah, enhances your performance. So, there's little incentive to teach your model to say I don't know. What are the common tactics to go around

**[3:18](https://www.youtube.com/watch?v=dFsws_PfGUk&t=198s)** it? The industry has been set on putting better guideline to make better guesses. And we have tools such as retrieved retrieval augmented generation to use web search and many other. And don't get me wrong, they work really well for what they're supposed to do. They lower the error rate, but they don't flag down the error. Do you remember back in the day of statistical learning when you had some nice confidence interval for your prediction? We used to be able to do that. We had them grounded in statistic, very easily computable. And since we moved to deep learning, this is not possible anymore. And now that we are deep into the generative AI era, it's even worse. So, the question is how do we put the error bar back into our models? Um we're pretty good at knowing when a

**[4:06](https://www.youtube.com/watch?v=dFsws_PfGUk&t=246s)** model is wrong or right. That's what benchmarks are for. But benchmark, you need to know the answer. In production, you cannot work in hindsight. You need to flag the error before someone start to work the wrong value. So, the signal has to come from the inside. And this raises the obvious question, do the model know when there is an error? And yes, they do. They they know they're lying to us. And so, we want to be able to harvest this signal if we can have access to it. And the obvious question is where do we look? So, here you have a a beautiful depiction of a simplified LM. The obvious first answer would be the token probabilities. They are easily accessible. But the thing is, they also give a signal about the wording. So, for

**[4:53](https://www.youtube.com/watch?v=dFsws_PfGUk&t=293s)** instance, if the LM is saying the next refuge is in roughly 2 hours, it might have hesitated between roughly, about, approximately 2 hours. And if we have a signal here, it's not really what we want. So, this end up being a very noisy signal. Not going to tease you too long. The actual signal you want to go for is the latent space. So, you had a talk this morning about mechanistic interpretability. Um this is rooted in those idea. And the question is, you know it's the latent space. Now, what do we do with it? Most simple way to attack this problem is a a simple logistic regression. So, now we have a probability of whether the answer might be right or wrong. And it comes from inside the model. So, it's

**[5:41](https://www.youtube.com/watch?v=dFsws_PfGUk&t=341s)** the model directly telling us whether we think the answer is going to be good or bad. Next, how do we train the logistic regression? Very simple way to do that. You go through some well-known data set such as TriviaQA, and you're going to ask question like, um what is the capital of Devon? Probably you don't know. It's Exeter. Uh if it gets the right answer, you flag it at as correct, and you have the latent space associated to it. So, you have your features, which are your latents, and the targets, which are whether it's correct or not. And that's it. Now, you have a very cheap, simple, and mostly reliable proxy to know if the answer that you're generating is going to be correct. What do we do with this now? First thing we worked on, um this is a very recent project we we just built. We

**[6:31](https://www.youtube.com/watch?v=dFsws_PfGUk&t=391s)** just published a paper. Um the task was hallucination detection, and more precisely, we had to detect which spans of the text is hallucinated or not. So, we had to flag down the exact error into the generation. Uh we also have to find which category area of error it is, and we're going to have through we're going to go through a few example. I'm sorry I wasn't brave enough to do a demo. So, here are some sample from the test set. So, the prompt is, "What is the name of the building outside the window?" So, we all see the window. Um I don't know about you, but I'm not seeing any name on the building. And so, the LLM did what he what he's very used to. It's going to invent an answer. So, based on the image, "The name of the building outside the window appear to be Starbucks." And now it does the

**[7:19](https://www.youtube.com/watch?v=dFsws_PfGUk&t=439s)** classical thing of doubling down. "You can see the Starbucks logo clearly on the building's facade." So, on red, you have our prediction of what's wrong, and underline is the gold reference from the annotator. And so, we do have a pretty good match here. Next example, how many people are wearing a watch in this example? So, the model outputs is, "One person is wearing a watch and our system correctly identifies that there are two watches and two people wearing them. So, it's working fairly well and I'll let you imagine what kind of application you could have if you had the power of detecting hallucination in such a way. Another thing that you can get from hallucination detection, we've had a talk right before lunch about speculative

**[8:06](https://www.youtube.com/watch?v=dFsws_PfGUk&t=486s)** decoding, so I'm not going to go too deep into the detail, but in a nutshell, you have a big, slow, and expensive model that you want to generate token with. And so, you're going to be clever about it. You're going to use a smaller model that is cheap and efficient to draft some token ahead and you're just going to use the big one to verify them. And verifying can be done in parallel, so it's faster. It's still expensive, but at least it's faster. So, what you can do is you do the exact same system with the logistic regression and now you have a confidence head on your token. So, you know which one are worthy of being verified. The one that are drafted and you don't trust them, you just throw them away. And this is a quite clever technique done by DeepMind with DeepSpark and gives you a 60 to 85% speedup. Not on decoding alone, but on speculative

**[8:57](https://www.youtube.com/watch?v=dFsws_PfGUk&t=537s)** decoding. So, pretty powerful. It's already used in production by DeepMind, Equi AI, and probably many other labs. Now, the last one, purely in the realm of speculation, you've probably seen the AI overview, the barcode from Google. Um a user was struggling with cheese not sticking on pizza and the LLM told him to put glue on the pizza sauce. That's probably what not what you would want to do. And so, you can imagine that the if you had a problem for uncertainty, something would have been flagged there. Like I can't believe that the LLM was confident writing this answer. So, it's probably a good way to use this kind of things. So, coming back to our original question,

**[9:45](https://www.youtube.com/watch?v=dFsws_PfGUk&t=585s)** how much we trust AI? The point I'm trying to make is you don't have to trust an AI that doesn't believe in itself. I hope you find ways to harvest the signal in your workflows. And on top of all, please don't use an LLM to plan your holiday yet. Thank you very much. >> [applause] [music]
