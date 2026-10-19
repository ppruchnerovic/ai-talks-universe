---
id: fhNZWExzlqU
title: "How to Be Correct at Scale With No Ground Truth - Diane Le Douaron - Mirakl - dotAI 2026"
slug: how-to-be-correct-at-scale-with-no-ground-truth-diane-le
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Diane Le Douaron"]
channel: "dotconferences"
duration_min: 9
published_at: 2026-09-28T14:00:21Z
video_id: fhNZWExzlqU
url: https://www.youtube.com/watch?v=fhNZWExzlqU
youtube_url: https://www.youtube.com/watch?v=fhNZWExzlqU
tags: []
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# How to Be Correct at Scale With No Ground Truth - Diane Le Douaron - Mirakl - dotAI 2026

**Diane Le Douaron**

`dotAI` · `dot conferences` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=fhNZWExzlqU) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Diane Le Douaron, Staff AI PM at Mirakl: https://www.dotai.io/

Diane Le Douaron is Staff AI Product Manager at Mirakl, where she leads the AI Catalog product suite as well as new product initiatives. She combines a technical and business background to build scalable AI products.

Lightning talk "How to Be Correct at Scale With No Ground Truth"

Most LLM work tolerates a near miss. Catalog transformation cannot afford it: expected outputs like fixed value lists and fixed rules demand a deterministic standard of correctness. This talk covers how we evaluate correctness when capabilities span several pipeline blocks and no ground truth exists.

## Transcript

*1,404 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=fhNZWExzlqU&t=7s)** [music] [music] [music] [applause] >> Hello everyone. So, I was speaking to you to you about correctness when there is no ground truth. So, by speaking with some of you earlier, I realized there was some interest in the topic. So, I'm very pleased, but I'm also aware that I'm the only thing standing between you and your lunch, so I'll get to it.

**[0:56](https://www.youtube.com/watch?v=fhNZWExzlqU&t=56s)** Um so, Mirakl is a big player in the e-commerce space, and one of the main products that we have e- is this e-commerce e-commerce platform for marketplace operators, and each operator defines their taxonomy. So, what is the taxonomy? It's effectively the structure in which they expect the product data to come in. And these taxonomies can be incredibly precise. So, there are required attributes, there are fixed value lists, exact formats, and we have developed um a Mirakl and AI product called Transformer that converts effectively the seller's raw data into these target taxonomies. And the seller raw data can come in many different forms, and this is why a simple mapping wouldn't have done. So,

**[1:45](https://www.youtube.com/watch?v=fhNZWExzlqU&t=105s)** some of the data is all into one field, usually the description where you have the color, the sizes, all of the information. And on the other hand, sometimes you have 200 structured fields. And so I'll show you an example now on the screen with um the color example. So, it's dark blue here in the seller catalog. And then we see that in the operator's taxonomy, there are only four choices of which and they are fixed and of which navy is the only acceptable proxy. And catalog transformer has to understand that and pick navy. If it doesn't, then that was most likely a required attribute. The product will just get rejected and we'll get a very unhappy seller on our hand. So, this is really to illustrate that

**[2:33](https://www.youtube.com/watch?v=fhNZWExzlqU&t=153s)** even though catalog transformer is an LLM-based pipeline of capabilities, the correctness is expected at deterministic standards and for most of our capabilities, there are there isn't any ground truth. So, we had to develop a method um in order to tackle this. So, before I run you through the three steps that we've developed, I'll introduce our rapidly the example. So, we'll use the example of translation for two reasons. A because it doesn't have any ground truth, as you've guessed, and also because um we could have used we could have done translation I just decided to handle it in the very traditional way, which is have the full catalog ready and then um use you know, do the translation step towards the end. But we have actually realized that since

**[3:21](https://www.youtube.com/watch?v=fhNZWExzlqU&t=201s)** it's a language-model-based pipeline, handling the language is what is most important. So, it's less a translation problem that it is a comprehension one. So, we've decided to run translation from the get-go, from the beginning, to see how well the model can extract the information, preserve the integrity of the information, preserve the meaning, and make choices in that language all along the way. So, the first step is really the definition of success. It's like what are the metrics that define correctness? And this step is often overlooked and really shouldn't because it really sets the bar for what you're trying to achieve. So, we work backwards from really understanding the user very well. What is the expected behavior that the

**[4:10](https://www.youtube.com/watch?v=fhNZWExzlqU&t=250s)** user wants? Understand the perimeter of that and defining metrics that cover the entire perimeter while keeping them to a minimum. You don't want to have a laundry list of metrics. You want to be very crisp, very sharp, and keep the signal. But you also So, obviously in to define them, you also want them to not be overlapping, to be measurable, obviously. And this is a really important exercise. And we found that defining a good metric is the same as defining a good strategy. When you look in hindsight, it makes all the sense in the world. Nothing would have been a benefit, but actually articulating it well is quite a bit of work. The second step is task decomposition. So, the metrics that we saw before measure the correctness of the output. Then we go also

**[4:59](https://www.youtube.com/watch?v=fhNZWExzlqU&t=299s)** another level down and we we break down the work into tasks. And for each of this task, we ask one and only one question. It's like had what had to happen here in order for a translation to be correct? And for example, here we'll use, you know, the decomposition of translation. The first step in the catalog transformer pipeline will be the locale detection. The taxonomy of the operator will say, "I want this language in output." Say Japanese. And catalog transformer needs to understand that at the beginning. If that step didn't happen, if it didn't understand Japanese, look no further. It's very, very unlikely that your output will be correct. But obviously we measure each individual one of them. And that really helps us understand

**[5:47](https://www.youtube.com/watch?v=fhNZWExzlqU&t=347s)** where things went wrong. And for example, for languages specifically, what we've done is sometimes because again, it's how the ability of the model to handle that language and that task in that language. So, for some of the more difficult tasks, we've used a more powerful model. That's usually what we've done to you know, to you make things better where it was a little bit weak. And then the third step is we've built our own judges and for continuous monitoring and for a lot of other purposes that I will describe in a minute. So, we couldn't simply put the output of catalog transformer into a plain LLM because it simply doesn't have the context. So, we'll go through through some of the examples here. Like

**[6:34](https://www.youtube.com/watch?v=fhNZWExzlqU&t=394s)** for example, we have a function in catalog transformer where we rewrite with the marketing attributes, so the descriptions, you know, that the intent, the way you can use the product. And plain LLM would just consider this to be an hallucination, will not understand that it was, you know, an intended rewrite. So, go back to our initial example with the dark blue and the navy. Again, it will think it's an error. It said dark blue, why did you change it to navy? It doesn't understand the concept of constrained choice. Same goes for the description. Often operators have a fixed limit for characters and so we have to condense the information a little bit in this case and then just think, "But you've lost some of the information." But we had to. So, the way we've developed our judges

**[7:21](https://www.youtube.com/watch?v=fhNZWExzlqU&t=441s)** is we have refined and refined and refined the prompts. We have tried to convey in those prompts how catalog transformer works, you know, what is the purpose of the different capabilities and also try to convey the you know, the the guidelines of the operator that are in the taxonomy. We've also made, you know, extensive use of human annotations, and we keep on doing so. We do it on a weekly basis, and we really want to prevent any drift. And also, we have given to our human annotators the very like ambiguous gnarly difficult um examples. And I know that for an audience that is not familiar with this on a daily basis, one can legitimately think, like, how hard is it to fill this product data? Well, it is quite difficult, I'll tell you. We don't have

**[8:09](https://www.youtube.com/watch?v=fhNZWExzlqU&t=489s)** a judge at Catalog Transformer, so we keep on improving on a daily basis. So, the judges, as I was saying, we use them in four different purposes. So, one is, obviously, to power investigations. Then, we use them to improve the code, because we see where things are breaking, you know, periodically. And, um, we also use them for, um, for What is the last one? >> [laughter] >> Yes, for the drift detection. And um so, this is So, to recap for what we said today, we define the metrics, we decompose the task, and then we use the judges for, um, for a continuous monitoring and the drift detection. So, thank you very much for your

**[8:56](https://www.youtube.com/watch?v=fhNZWExzlqU&t=536s)** attention. Please come and find us at our stand. We happy to share more learnings, we'd love to know more about yours, and enjoy your lunch. >> [applause] >> HEY! >> [music] >> HEY!
