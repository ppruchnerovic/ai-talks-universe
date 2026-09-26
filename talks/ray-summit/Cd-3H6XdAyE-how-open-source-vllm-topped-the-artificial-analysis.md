---
id: Cd-3H6XdAyE
title: "How Open-Source vLLM Topped the Artificial Analysis Leaderboard | DigitalOcean | Ray Summit 2026"
slug: how-open-source-vllm-topped-the-artificial-analysis
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 13
published_at: 2026-09-17T16:06:56Z
video_id: Cd-3H6XdAyE
url: https://www.youtube.com/watch?v=Cd-3H6XdAyE
youtube_url: https://www.youtube.com/watch?v=Cd-3H6XdAyE
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# How Open-Source vLLM Topped the Artificial Analysis Leaderboard | DigitalOcean | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=Cd-3H6XdAyE) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

DigitalOcean's vLLM deployments reached leading Artificial Analysis results across frontier open-weight models, including 230 tokens per second per user on DeepSeek V3.2 and sub-second time to first token for 10,000-token Qwen 3.5 prompts.

At Ray Summit 2026, Debarshi Raha, VP and Fellow Engineer at DigitalOcean, breaks down the open-source optimization work behind those results, from low-batch kernel fusion and EAGLE3 speculative decoding to linear-attention fusions and dual-stream execution.

You'll leave seeing how profiling model-specific bottlenecks and upstreaming the fixes into vLLM delivers production inference performance that rivals proprietary stacks.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,267 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=6s)** So, we have something very interesting for you today. We will talk about how Digital Ocean and vLLM got to the top of artificial analysis leaderboard for the inference. So, just for intro, I am the fellow engineer at Digital Ocean, and I have Balaji with me who is staff engineer working on inference. So, little bit context on Digital Ocean, we are a full stack AI native cloud. So, we have everything from at the bottom infrastructure, our own GPUs to inference, to manage agents. Now, for the inference to be useful, it needs to be fast. For example, think one agent running on the managed agent on the top, and they are performing one task. So, they will have to plan, they will have

**[0:55](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=55s)** to reason, they will have to do tool call, and then finally stitch everything together to get back the result that you want. Now, every one of them is one model call. And if you introduce latency at every token, that finally it blows up and finally it shows up to the end-to-end, to humans or to the agents. So, that's why we need the inference to be super fast. Now, we'll take you to through the journey how we did that and got to the top of the leaderboard. Now, this is the outline. You can see that we have selected the right hardware. And based on the hardware, you select the right version of the model, the quantized version of the model. And after that, there is a serving engine. So, we had vLLM, and yeah, the infra team and vLLM did awesome job of

**[1:45](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=105s)** tuning it end end-to-end, from top to bottom. So, we'll describe some of those, and of course, you take the advantage take advantage of the other techniques like speculative decoding. So, with all of this together, you can make the time per output token super fast as you run and deploy your inference. So, to start with the GPU, as I mentioned, we have the full stack inference in our own data center with GPUs. We had AMD and Nvidia GPUs. So, we had the flexibility of selecting the right GPU best for the task. So, for these models, we selected B100. Now, that is not the only option. You of course have the other options, but this is what we chose based on the availability at that time, and that was perfect. And it had two main advantages

**[2:35](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=155s)** that it gave us. So, one was the memory. It had 50% more memory than the previous generation B200. And how that helps you? That means that you can load more of the model weights on single GPU. And so, that way you can reduce the cost of your deployment. You can host the whole model on less number of GPUs to reduce your cost. Now, for speed, there is the 1.5x more in VFP specific compute that we had. So, this is Now, 1.5x more in VFP for compute does not mean that you will have 1.5x the throughput or 1.5x the latency reduction. Why? Because the token generation has two phases. One is prefill, and one is decode. So, prefill is compute hungry.

**[3:24](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=204s)** They are you can going through churning through all the previous context. And that needs lot of compute. So, sure, your prefill will get fast, and that will show up in your TTFT latency, time to first token latency, but it also has a decode step, which is lot of memory bandwidth constraint. So, not the whole thing will get 1.5x better, but yeah, the TTFT will get better. Now, we'll also show you how we uh what impacted the T time per output token or T pot. So, that will come next. So, after the GPU selection, you have to exploit those benefits that I mentioned that 1.5x more the more of the NVB4 compute. So, that's why we chose the NVB4 version of the model. So, this was

**[4:12](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=252s)** for DeepSeek and MiniMax and uh Gwen. So, we chose the NVB4 quantized version of the model so that you can exploit that 1.5x more NVB throughput. And another for the fast token, how it helps is that when you quantize use a quantized version of the model, it drastically reduces the memory footprint. So, in this case, you can see that the model now needs 1.8x less memory. Now, when you have 1.8x less memory, you move around less data. When you move around less data, that shows up in your part token output generation. So, that's how it contributes to your fastness of the model. Uh but by selecting NVB4, you are not losing much accuracy. So, this is from

**[5:00](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=300s)** the model page of DeepSeek uh 3.2. You can see GPQ and diamond, it is not dragging much. So, this was fine for us. So, now going to the interesting part, which is the VLLM end-to-end optimizations. Now, this is the overview of all the different techniques, all the different mechanisms we applied. So, first one is tensor parallelism. That is no brainer, you have to do it anyways because you cannot fit the whole model on one chip. Uh then this is very interesting kernel fusion. So, this will be very interesting for you guys to know. Then there is programmatic dependent launch. So, how much you can parallelize a kernel launch although they are dependent on each other. So, that one and then finally, you have to take advantage of the other techniques like

**[5:47](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=347s)** speculative decoding. And uh whatever else you can to speed up the generation. Now starting with the TP tensor parallel as I mentioned this is no brainer again because the Deep Seek V 3.2 had 600 gigs plus memory and the right current one the V4 is like 1.6 terabyte or plus. So that is that is not going to fit you on your one chip as I mentioned it has only 288 GB. So you have to shard it across the chips to get to to even load the whole model. So this is no brainer this is straightforward it's just one parameter on VLM you just set it and you are done. Uh but not this one. Now this one is very hard work thanks to the InfiniBand VLM team.

**[6:36](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=396s)** So they found lot of opportunity in fusing kernels. So let me start by telling what is a kernel right? Um so kernel is something that you launch from CPU to GPU to do the computation on GPU. Now as you know GPU is has tens of thousands of cores and do things very fast and parallel. But if you launch just a fraction of the compute with lot of overhead from CPU to GPU then that CPU to GPU launch dominates your whole timeline. And imagine you are launching multiple of those kernels. When you launch multiple of those kernels but do just small amount of work tiny amount of work then you are paying lot of cost only to launch kernels from CPU to GPU but not getting that benefit of taking all the

**[7:25](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=445s)** SMs in GPU and working in parallel. So that's why you can't fuse some of those small operations to make it bigger and run in parallel in the GPU with one launch. So that is the main theory of kernel fusion. Uh now let's see how we did it for DeepSpeech v3.2. Now, these are the steps that you see, these are very small steps and mainly uh they are for most of the models in the attention layer. So, in attention layer, you have uh RMS norm to stabilize the attention input that you are getting. Then, there is uh a rope. So, that is to embed the positional embedding of uh of the attention. And then, the Q FP8 quantization to quantize and reduce

**[8:13](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=493s)** the memory footprint of the model. So, all these small attention layer uh components are where they are in the kernel for DeepSpeech v3.2. Now, instead of doing those launches one by one, you can think that you can fuse them together to get a bigger launch. And when you are doing a bigger launch, you can actually exercise the all the SMs in the GPU to launch and do more task or launch. So, that's how it helps you. And there are of course the other benefits. For example, when you are launching just one kernel instead of multiple, then you are not storing the result of one kernel in main memory and then again going back and fetching from there. So, you're not doing slow memory access. So, rather you are on registered and shared memory and doing things faster. So, that is one.

**[9:01](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=541s)** And also the other benefits that I told from using the more SMs. So, all those together, that helps you in the kernel fusion. Now, similarly, the So, that was the main attention path. Now, there is the So, DeepSpeech also had DSA, DeepSpeech sparse attention, which means in a light So, in normal attention, you go back to each of the token that comes previous to this token in the sequence and try to attend to them. But, all of those tokens are not going to be meaningful in your final calculation because only few are relevant to this token. So, that's why DeepSpeech introduced this one. And even the sparse attention path also has those same requirements. Like it does the same RMS norm, it does the rope, and those all the lightweight. So, you can fuse those as well.

**[9:48](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=588s)** So, now the team fused the RM fused the attention path as well as the DSA path, and you can see this is what I I don't have time to go through each one of them, but this is what finally happened. So, instead of doing so many kernel launches on the left, you launch only 10 kernels. Instead of 33 kernels, you launch only 10 kernels, and finally you got 1.2x the speed up by doing this. So, that was the main benefit of kernel fusion. And with that, so I'm not going through the rest of the details. Um So, this is the final screen that you guys all are waiting for to see how what is the result. So, this is the result. So, you can see that Digital Ocean came on the top of the artificial analysis leaderboard. Now, this graph is telling what is the output speed output tokens

**[10:35](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=635s)** per second speed. Uh now, this is not telling the rest of the story like TTFT or other thing, but this is mainly output per token how much time you are taking. And to increase this one, what you need to do is you reduce the time per output token or TPT latency. So, in this case we reduce the TPT token latency from I think from 7 to 8 ms to around 4 ms. So, that gives you that number around 230 plus uh tokens per second. Now, this is just the another chart. This shows the time the latency for the first token, and you can see on the first token also you are pretty less here, and the output speed also super high. So, this is what for DeepSpeech 3.2. Now, I'll invite Balaji to quickly cover the rest of the models.

**[11:24](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=684s)** >> Um For the rest of the models, we did spec decoding. Spec decoding is how you use the raft model to basically predict the tokens faster, and then the master model will will either accept or reject it. In this case, we trained our own Eagle model with hidden states of the Minimax. So, that gave a better acceptance rate. So, that is what gave the better throughput. And the PDL, which is nothing but overlapping kernel launches, which will reduce the corner kernel launch time improving the decode time improving the decode performance. So, that got us the top two or top three of the leaderboard for Minimax as well as the Quen models. And what we are building right now is an input optimization agent that can learn and from these signals and work through the models ourselves. So, that is a work in

**[12:12](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=732s)** progress that we are having. And I'll let Devarshi wrap it up. >> Okay, so what all of this means to you, right? Of course, you can come to DigitalOcean to experience this fast inference. So, our promise is to give you the best inference on the planet. Best and fastest. But, all of this is open source. All of this that I explained are open source. So, you can host it yourself as well. So, if you just go to vllm and you just get that recipe for DeepSeek v3.2 or Minimax or Quen, you will get the same performance with the fastest latency. So, thanks to the DeepSeek I mean thanks to the Inforrect and vllm team who helped us achieve many of this. So, thanks to Simon,

**[12:59](https://www.youtube.com/watch?v=Cd-3H6XdAyE&t=779s)** Uh Usuk, Roger, and others in the team. So, try try all of those, try these models, try these recipes. So, all of these are open source. These are not in any of the closed fork that you have. So, you can try yourself. Or, you can simply come to DigitalOcean for the inference and inference routing. So, with that, I will end. Thank you so much and I'll be happy to talk if you have any question at hand. Thank you so much.
