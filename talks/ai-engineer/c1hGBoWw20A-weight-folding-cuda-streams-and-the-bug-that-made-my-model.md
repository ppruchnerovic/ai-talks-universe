---
id: c1hGBoWw20A
title: "Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards — Filip Makraduli"
slug: weight-folding-cuda-streams-and-the-bug-that-made-my-model
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Weight Folding", "Filip Makraduli"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-09-19T19:00:02Z
video_id: c1hGBoWw20A
url: https://www.youtube.com/watch?v=c1hGBoWw20A
youtube_url: https://www.youtube.com/watch?v=c1hGBoWw20A
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards — Filip Makraduli

**Weight Folding, Filip Makraduli**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=c1hGBoWw20A) · [Conference site](https://www.ai.engineer/)

## Description

An RMS norm layer does almost none of the arithmetic in a transformer, yet a single decode step can launch it around 33 times, and a GPU is fast at math and slow at everything else: starting work, moving data, waiting. That gap is what FlashNorm attacks. Filip Makraduli wrote the paper with Nils Graef, and the idea fits in two lines of algebra. Fold the norm's gain into the projection weights offline so one matrix absorbs both. Defer the scalar divide so the matrix unit and the vector unit run at once instead of one idling for the other. And in newer architectures that normalize twice in a row, drop one, because the operation is scale invariant and the second adds nothing. Together they buy a 33 to 35 percent speedup on the norm plus projection operation, and the folded checkpoint works with torch compile and quantized models.

The deferral is where it got interesting, because you cannot do it from Python. He wrote the CUDA to run the matmul on tensor cores and the RMS reduction on CUDA cores in parallel. Unit tests passed, perplexity looked normal, and then over a long generation the model began repeating itself with a one step lag, outputs from the past. The join between the two streams was implicit. One stream had not finished, so the post scale read a stale buffer from an unfinished multiply. The fix was to mark the end of each stream explicitly and make the post scale wait on both. He closes on why the second half needed Superlinked's open inference engine to deploy a modified checkpoint, since you cannot do kernel surgery on a rented endpoint.

Speaker info:
- https://x.com/f_makraduli
- https://www.linkedin.com/in/filipmakraduli/
- https://filipmakraduli.substack.com/

Timestamps:
0:00 - Two lines of algebra for RMS norm
2:07 - Why a layer with no math costs so much time
3:44 - Weight folding, deferred division, dropped pre norm
6:33 - The output that came from the past
7:25 - Tensor cores and CUDA cores in parallel
8:45 - An implicit join and a race condition
9:58 - Making the post scale wait on both streams
10:42 - Results on open models, and what works out of the box
13:54 - Why you cannot do kernel work on a rented endpoint
16:00 - Paper, repo, and where to find him

## Transcript

*2,500 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=c1hGBoWw20A&t=12s)** Hello everyone. Uh Thank you for coming and uh I'll start the talk now. So This talk is uh around a paper that I did um which is very simple. The proposition is very clear. It's basically two lines of algebra that make uh the RMS norm layer in transformers cheaper, quicker, and kind of improve improve it as like a layer in the transformer architecture. Similar to how layer norm once used to be the standard and then it was substituted by RMS norm. This follows along um this way of

**[1:04](https://www.youtube.com/watch?v=c1hGBoWw20A&t=64s)** thinking. And I got the chance to kind of meet some people from the open source world and um I co-authored this paper together with uh Niels Graf who was the kind of the creator of this. And the work follows from there. So this is uh presented on archive. You can have a look, read it, test it out. There is a repo as well. And the concept the let's say the idea and the way of thinking it's easiest to explain with maybe flash attention. So in a similar way of how um flash attention kind of weights until there's a multiplication and tries to limit this uh communications between memory so that

**[1:53](https://www.youtube.com/watch?v=c1hGBoWw20A&t=113s)** the whole process is faster. This is kind of a similar thought along those lines and it does certain improvements that make the RMS norm process much quicker and in in effect improve the whole transformer. And one question is okay, why RMS norm since that layer does almost none of the math? And that's true. So the share of the kind of math portion if you look at it is quite small. However the clock time or wall time as they say is quite big and for example in one decode step. So right when like inference is performed

**[2:43](https://www.youtube.com/watch?v=c1hGBoWw20A&t=163s)** the RMS norm can be started like 33 times. Of course, it depends on the model and so on. In the paper, you have the specific models and how this was tested. Um and the question is how this can be improved and how this wait for the matrix multiplication can be kind of avoided. And the reason why this is slow is because the GPUs are not slow or bad at math, but they're bad at everything else around the actual math. So that means starting the work, the actual work. So for example, starting the process as it happens in some of the experiments

**[3:31](https://www.youtube.com/watch?v=c1hGBoWw20A&t=211s)** 33 times that takes a long time and for example, fusing um each normalization into the matrix multiplication can help avoid this. Also doing weight folding can help in kind of moving data between memory and um that's a process that's also slow for GPUs. And also waiting. Uh so, for example, deferring the division that's done in the RMS norm layer is also a way to avoid this waiting step. So, basically, what this paper does is it improves all these three aspects by doing a few algebraic tricks in the way RMS norm is computed.

**[4:19](https://www.youtube.com/watch?v=c1hGBoWw20A&t=259s)** That's it. And math-wise, these are the tricks. Uh it's mainly around the first two propositions. One is weightless normalization. Uh you can see that here. Um and deferred normalization, so um that's the second one. And now in more newer architectures, there is a situation where um RMS can be kind of can appear twice. Uh for example, in Gemma 4, this happens. So, canceling the pre-normalization also works. Um and all of this is algebraically proven in the paper. And the first proposition is this where kind of the the gain and the weight fold folded to one matrix W, uh you can see here with an asterisk.

**[5:09](https://www.youtube.com/watch?v=c1hGBoWw20A&t=309s)** And that is computed offline, similar to how maybe in flash attention, you compute some stuff on the side so that there is no uh communication between memory all the time. So, this is one step that's kind of um done, this weight folding. And the other step is um deferring um the scalar the scalar divide of the matmul so that they can be done in parallel. So, in a normal case, you would have to compute once, then wait, and compute again. In this case, the idea is to kind of split this so that it can be parallelized. And the third one, which is kind of a version of this is that um there is kind of if there are two um because this is scale invariant, one

**[5:58](https://www.youtube.com/watch?v=c1hGBoWw20A&t=358s)** of them can be dropped and this still works. And this is applicable to newer models um that can have this architecture and implementation. So, in order to make this happen in real life especially this proposition number two, um so for this one, for example, it's easy. There is a repo called Transformer Tricks. You can just apply this to any model and it works. But in order to do this, there is some kernel work. So, it's not as straightforward to do. So, in order for me to do that, I was implementing this and I came out with this experiment once. So, it looks okay in general, where it's like, "Okay, the prompt is the

**[6:47](https://www.youtube.com/watch?v=c1hGBoWw20A&t=407s)** Transformer architecture revolutionally revolutionized NLP because and then there is some kind of expected output." But in the output I got, I saw this repetition and one-step lag, as you can see here, the word because appears again. And there was something happening with the GPU streams and I was trying to figure out what was happening. And I was getting this one-step lag and kind of um outputs that were from the past in a way. Um and in debugging all of this, I realized that um in the process of building something like this, so as I explained the proposition two or deferring these two operations, um in CUDA, you can do two things. You

**[7:35](https://www.youtube.com/watch?v=c1hGBoWw20A&t=455s)** can do like tensor cores that do one part of the matrix multiplication and you can do CUDA cores that kind of run stuff like element-wise operations, reductions, square roots, and so on. So, the idea was to do this in parallel and get the benefit of what I was explaining in the paper to actually test out this concept. So, this is how it was supposed to look like. So, there is if you do things sequentially, there is this idle waiting time when you when the vector unit computes the RMS and scaling, and then there is a matrix multiplication. So, the idea was okay, with flash norm, which is the technique in the paper, you're supposed to do those both in parallel. So, the matrix unit computes the matmul and the vector unit computes the RMS. So, in that way you save uh

**[8:26](https://www.youtube.com/watch?v=c1hGBoWw20A&t=506s)** time. However, you cannot just do this in Python, you have to go a bit lower. And I did that with CUDA code like this. And this looked in general okay at my uh at that time. However, um I realized that I did something slightly wrong. And that thing was that the join in the end, where you're supposed to join the two streams, was implicit in my case. And when I tested this out, the unit tests worked, the quality seemed similar, like perplexity testing, and so on, because it's just like um similar generation, but over long generation, I was able to see this problem. So, I had no idea what this was.

**[9:15](https://www.youtube.com/watch?v=c1hGBoWw20A&t=555s)** And the reason was that when I was doing this uh implicit um join, basically, one of the streams hadn't finished the work, so I got race conditions that kind of read the past from the unfinished matrix multiplication. So, the idea that I had to fix this was um around the fact that I had to be explicit about the join and wait until one of the operations is finished so that I'm certain that when I join I'm not reading from the past. So, that was the realization um in this exploration of CUDA streams. And this is how I had things done. So, the join was implicit. So, the post um scale read like an old uh buffer value.

**[10:06](https://www.youtube.com/watch?v=c1hGBoWw20A&t=606s)** And how this is fixed is with this where basically you need to mark the end of the matrix multiplication, then mark the end of the RMS, and then post scale wait for the first stream and then wait for the second stream. And that fixed the bug and made kind of the paper work and the model speak forwards instead of backwards. And that was the cool maybe academic perspective, but I also wanted to try things, right? Deploy this, test it out, see how I can make it work um in maybe a more production setting. And you can also read the paper and see all the tests. Um some are done most are done around llama models, but like this works for other

**[10:55](https://www.youtube.com/watch?v=c1hGBoWw20A&t=655s)** architectures as well. Um so, what you can do for this specific paper is um for example, the weight folding that I explained the pre-position one, you can just do it with um some code in the repo that's like flash you say flashify and it does that. However, with this second thing that I mentioned, you need to do a bit of kernel work if you want to do that uh like I explained in my example. And these are some results that are based on llama models and there are different kind of details that you can have a look at as well as well. Like what happens if you do only the third normalization, what happens if you do a full fused kernel. Um so there are a lot of experiments of going lower here to test all the propositions, and this have been our results

**[11:43](https://www.youtube.com/watch?v=c1hGBoWw20A&t=703s)** um in different, let's say, levels of um scrutiny and detail. But even the simple one with like weight folding um shows some improvement. And this also works with like the day-to-day tools that you use in the models. It's not like you have to reinvent the wheel or, you know, do things from scratch. So it works with uh torch compile um because the it's kind of like a new checkpoint, and that's it. Flash attention does similar tricks at a different layer, and also it works with quantized models. So it's totally cool to actually apply this, and you can get a model that has this cool new normalization layer. And where you can get this um

**[12:30](https://www.youtube.com/watch?v=c1hGBoWw20A&t=750s)** details and code to actually run this is this transformer tricks repo. So uh it has different algebraic tricks like I explained, as well as this paper that I mentioned. And also there is the GitHub uh not the GitHub, but the Hugging Face uh model repo where I've done this with some models, and you can have a Hugging Face link to that model and test it out. Um and what you also can do with this Hugging Face models is to deploy them in production. And so when I was thinking about doing this, um I realized that, okay, now that, let's say, the science is done and there is a link to a Hugging Face model, um Superlinked's uh inference engine was a cool way to actually deploy any um uh Hugging Face model, and we've done

**[13:20](https://www.youtube.com/watch?v=c1hGBoWw20A&t=800s)** this at hackathons where people would bring like a custom Hugging Face model or checkpoint that they have with their fine-tuned stuff, and you can test out like even if you have some version of this algebraic tricks that you want to improve a model and test on test your own research ideas, you can actually try that out and have a deployed version on a cluster of this model and not have to worry about this glue code around deploying models. So, that's um pretty cool. And the the point is that if you have the full cluster open source and the model inference open source, you can actually test out this kind of maybe more novel research ideas where if you want to do

**[14:08](https://www.youtube.com/watch?v=c1hGBoWw20A&t=848s)** kernel manipulation or flash norm and things like that, it's much more difficult to do that do this at a rented endpoint where you don't own the inference. It's you want something that's portable and flexible to actually allow you to do this stuff, but it's also production ready enough so that you can test things out at scale. And you can, for example, use site to combine this with other models like, as you can see in the top left, there is you can have this flashified models with different other models to do agentic tasks if you want and kind of do that end-to-end bigger use case. And the way site works is this production cluster helps you deploy the models, so you can have a look at site's repo as well for more details on this.

**[14:58](https://www.youtube.com/watch?v=c1hGBoWw20A&t=898s)** Um and also there is a smarter queuing mechanism that helps you, especially if you work with smaller models cuz when doing the flash norm stuff, I worked with like smaller llama models and also with small agents from hugging face. So, having a way to deploy smaller models that can also work on like the same GPU so that you don't have to spend your money on GPU cost, but actually kind of switch models around, especially smaller models. It was quite useful. And you can also control the model configs through an API as well as the cluster, which is also pretty convenient without having like an infra guy supporting you in your open source research. So, that's cool as well. Um, and you own your cloud, which is useful if you want open weights, open

**[15:48](https://www.youtube.com/watch?v=c1hGBoWw20A&t=948s)** models, open source. And there's also like a catalog that Sci has of different models, um, not just the ones I mentioned, but you can have a look. There's also re-ranking embedding models if you're building something along those lines. And with that I'm kind of finishing this story of my research journey where I co-authored this paper, um, around the technique that improves the transformer, but also found a way kind of to bring this to, let's say, production and test it out and find a way to play around with this open source models. And feel free to contact me on LinkedIn, maybe if you have any questions or contributions. A lot of this stuff that I've mentioned, like some of them are PRs on like vLLM or on Hugging Face. You might find them all

**[16:37](https://www.youtube.com/watch?v=c1hGBoWw20A&t=997s)** around. You can also see the check out the paper. That's the archive link that you have there. Um, and you also have the Sci repo and my LinkedIn. Um so thank you very much for attending. >> [applause] [cheering] >> And you can catch me for questions. We'll be here, close by. >> [music]
