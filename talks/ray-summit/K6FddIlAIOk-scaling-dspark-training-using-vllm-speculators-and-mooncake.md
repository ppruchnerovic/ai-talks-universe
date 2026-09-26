---
id: K6FddIlAIOk
title: "Scaling DSpark Training Using vLLM, Speculators and Mooncake | Red Hat | Ray Summit 2026"
slug: scaling-dspark-training-using-vllm-speculators-and-mooncake
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: ["Red Hat"]
channel: "Anyscale"
duration_min: 17
published_at: 2026-09-17T16:06:15Z
video_id: K6FddIlAIOk
url: https://www.youtube.com/watch?v=K6FddIlAIOk
youtube_url: https://www.youtube.com/watch?v=K6FddIlAIOk
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Scaling DSpark Training Using vLLM, Speculators and Mooncake | Red Hat | Ray Summit 2026

**Red Hat**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=K6FddIlAIOk) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

State-of-the-art speculative decoding lives or dies on the drafter, and training drafters well at scale is a production issue.

At Ray Summit 2026, Helen Zhao, Machine Learning Engineer at Red Hat, goes under the hood on building drafters via online hidden-state distillation across a full Verda GB300 rack, using GLM5.2 as the example: how vLLM, Mooncake, and Speculators combine into a reproducible pipeline, and how to keep a rack of GPUs coordinated while distilling in real time.

You'll leave with a reproducible recipe for drafter training at cluster scale.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,370 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=K6FddIlAIOk&t=5s)** Okay. Hi everybody. Um my name is Helen. Um I'm from Red Hat. I'm a machine learning engineer and today I'm presenting on behalf of Vera AI lab. I'm a maintainer of speculators project. Today I'm going to talk about training a Kimik 3D Spark a draft model across a GB300 rack. Uh it's really powerful machine. uh 48GPU Kimk 3DSpark training run combining VLM moon cake and speculators. Uh what this talk covers is I'm going to share our comm3 drafter recipe and what DSpark is and how to scale up training and um why use VM to run our drafters. So training a really good drafter model is a training recipe problem but scaling

**[0:54](https://www.youtube.com/watch?v=K6FddIlAIOk&t=54s)** up is a system issue and uh if you're not familiar specific coding is um uh model optimization technique um that we apply we train a very small drafter model to propose um K tokens in advance and the big model the target model that you were trying to serve originally will verify them all in one forward path. pass. Um why does it work? Because um big models are really big and one for pass is very expensive and very slow. But these drafters uh traditionally for ego 3, it's only one layer. So extremely small. Even some of the later algorithms for Dlash Dspark Dlash 2, we have five layers. But comparing to a giant model like Kimmy K3, it's still like nothing. Um for

**[1:45](https://www.youtube.com/watch?v=K6FddIlAIOk&t=105s)** example in this drafter um we predict four tokens in advance. We predict drums over the lazy and target model runs all these four tokens in one forward pass and create their own log probabilities. And if the log probabilities of the drafter and the target agrees we accept these tokens and we can see for lazy we don't accept it. We reject it because the log probabilities don't agree. And then we just commit three tokens. And because we have run one forward pass in the big model, we get the last token dog for free. And um some important concept to go through these four tokens, we call them acceptance length. Usually the higher the acceptance length um the more

**[2:33](https://www.youtube.com/watch?v=K6FddIlAIOk&t=153s)** of a speed up you're going to see from the drafter model. Um and uh because we have this really great rejection sampling, we can guarantee that these tokens that we are using come from the exact same distribution that target was going to propose themselves. So speculative decoding is completely lossless. It's an optimization technique basically you should always use for free and get uh your speed up. So what is DSpark? Um a lot of tradition um a lot of traditional specular decoding techniques um when we propose tokens the small model still runs auto reggressively like eagle and eagle 3 but for D flash model uh for the first time

**[3:24](https://www.youtube.com/watch?v=K6FddIlAIOk&t=204s)** we're using sort of a diffusion uh technique to make sure we only run one forward pass and because eagle and ego 3 runs auto reggressively we only we only produce three to five tokens each step but for D flash we can produce eight to 16 in one step um comparing to ego 3 that's a huge bump and because it's only one forward pass it's a lot faster and why is DSpark even better because these tokens um U1 U2 U3 U4 these tokens are predicted in one forward pass at the same time so they don't have a causal relationship between them. Uh for example, I can both say no problem or of course. These are two both valid uh

**[4:15](https://www.youtube.com/watch?v=K6FddIlAIOk&t=255s)** short sentences. But for token one, I can predict of but for token two I can predict problem because they are produced by the same time I can end up with a phrase like off problem which does not make any sense. So to recover this um causal relationship between these tokens um DeepSk lab was very smart. They introduced this um very lightweighted mark head um that from left to right kind of add this low rank bias BK to recover this cost relationship a little bit. There's also a confidence head and a prefixuler trim. Um so verifier does not waste any time on tokens that drafters are not even that confident about to further speed up

**[5:04](https://www.youtube.com/watch?v=K6FddIlAIOk&t=304s)** the processes. Um and what is speculators? Speculators is uh under the VM project in the same ecosystem and it's a production training library. We've published 33 drafters in the Red Hat AI collections and we cover six different algorithms. Ego 3, Dlash, DSpark, PGO, MTP and we are very proud we were able to um support Dlash 2 the first week it came out. Um why is this library great is we have distributed training through DDP and we support BF-16 FP32 mixed precisions. We now support motto hidden states extraction which is um which is how we train this

**[5:53](https://www.youtube.com/watch?v=K6FddIlAIOk&t=353s)** giant Kimmy K3 model with and um we add a lot of data and tooling features as well. Uh for example we have uh weights and biases and tensorboard. If you figured that your trainings are already overfitting there's no need to train more. And the most exciting part is our G team Kim K3 training recipe. So we use a 12 node online hidden states extraction job. I I guess it's worth noting why we are extracting hidden states from the verifier. Um initially initially the idea of specular decoding is we use a small model in the same family like we use when 34B to speed of a 70dB model or something like that and then the small model will also take in tokens as input. But as eagle team found out um getting

**[6:46](https://www.youtube.com/watch?v=K6FddIlAIOk&t=406s)** tokens is not as good as just get the hidden states from the verifier model. So it's kind of like your drafter is learning the inner thoughts of the bigger model and try to think like it and this way it spits out tokens that are more similar to the verifier model and hence the speed up and we used a 48 GB300 GPUs across 12 nodes and four TP8 uh independent Kimik3 extractors using VLM and we use DP16 replicated DSpark trainer on 16 GPUs and completed two epochs with a 4.15 final validation acceptance length. We are very proud of this model and um I'm I'm just going to say it. It's the best on

**[7:35](https://www.youtube.com/watch?v=K6FddIlAIOk&t=455s)** the market. Please try it out. Um uh this is a really cool graph. Um you can see you can see the output throughput is a very significant uh specifically in really low throughput regime which is where um speculative decoding shines. And how we actually appro how we actually got here there are three steps. Usually when you train a draft model uh first you got to prepare the data to help the draft model learn how the big model talks. You have to regenerate response by the big model to help the drafter model learn exactly which tokens to use. And that usually takes a really long time. And um during training we extract hint states from a

**[8:24](https://www.youtube.com/watch?v=K6FddIlAIOk&t=504s)** target model in this case Kimik K3 using VLM. We captured uh five hidden layers and uh they are all stream batched through moon cake connector and on the trainer speculator side we have a 4GPU DDP five layer drafter uh block size eight and mark of rank 256 like the model uh uh deepseek release used and uh we train everything um open perfect blend like deepseek um released in their model and we found this data that is pretty great in training your model. Um, and during training, we can see most of the heavy heavy lifting was done in epoch one and training through epoch 2 kind of gives a little bit of a bump.

**[9:13](https://www.youtube.com/watch?v=K6FddIlAIOk&t=553s)** So where do these hidden states actually come from? As I explained, these hidden states are like really key to our training. There are most there are two ways on getting these hidden states. offline dumping to disk um is really really expensive because these hint states are huge especially for um a giant model like Kim K3 it's like uh trillions of data like you shouldn't really be saving these so we have to move to online streaming while training uh to make sure that we have enough memory um to get through this training run and uh which is why having a hint states extractor is very important. This is um this is supported natively in VLM the

**[10:02](https://www.youtube.com/watch?v=K6FddIlAIOk&t=602s)** hidden states extractor. Um this is hacky but I also personally think this is very smart. We are smuggling them out and we are dressing them up as KV cache and the shape kind of matches. Not exactly, but um we are uh we're using the layer as num heads and we're using the head head size as hidden uh hidden sides and we kind of just pipe them out using KV cache. So we don't have to allocate um separate space for hidden states extraction. And this is our original connector. It lives in VLM. It's correct. It's debugable. It's zero and fra but single node because we have to use shared storage. Um how does this extractor work? We create log files um to help

**[10:53](https://www.youtube.com/watch?v=K6FddIlAIOk&t=653s)** with async uh reading and uh consuming. And these files are stored um in dev shin ran or disk. And on the trainer speculator size it checks the lock and the lock will block until the writing is done. And then uh the on the trainer side it wakes and load file file and trains. um because the limitation was very obvious. You can only train smaller models that fits on one node. So we switch to moon connector. Um the trainer will send a request to the extractor and the extractor will gives give back a data handle the key along with some metadata and everything is handled by moon cake master. uh we're we're sending

**[11:41](https://www.youtube.com/watch?v=K6FddIlAIOk&t=701s)** these uh key uh hidden states tens tensor p uh uh pairs and moon kick master will fetch that for us kind of acting like a proxy uh proxy um uh conveniently and now let's go through the exciting part the machine this beast the Vera GV300 uh NV uh L72 uh it contains 72 Blackwell GPUs in 18 trays weld all to all by um multi-node Nvidia NVLink. So everybody talks to everybody very easy to set up very great um what we did is that we used two uh we had four of these units uh like training units. We have two trace of extractors

**[12:33](https://www.youtube.com/watch?v=K6FddIlAIOk&t=753s)** extracting hidden states by uh setting up a VLM instance that basically just does prefill and uses MoonK connector to transfer that to the training side. And the trainer um each trainer tray only connects to um one um Henates extractor pair and we have four of these units um to help us scale out. Um, one thing I'd like to point out is that um, uh, the target and drafter are completely disagregated. Um, the only things that moves across the node boundaries are the hidden states flowing from extractor to trainer and a very tiny gradient are reduced across the um, four nodes 16 GPUs on the trainer side. everything nvlink heavy um

**[13:25](https://www.youtube.com/watch?v=K6FddIlAIOk&t=805s)** hungry stays inside the node. So to scale to scale out like I just said that um we have four four different copies of uh those um little three uh not little three trace um units and uh on the trainer on the trainer side each training node initialize with a separate VLM endpoint to shard requests across replica replicas um and each uh serving instance is a TP equals to eight VLM M Kimmy K3 instance and on the trainer side we have replicated DDP the drafter and optimizer all fit in one GPU to avoid parameter all gathers um we did some experiment of switching

**[14:13](https://www.youtube.com/watch?v=K6FddIlAIOk&t=853s)** from TCP to RDMA and found like little bit of a speed bump of 2% and obviously there are still a lot of future improvements we would like to do we did a little bit of profiling and found out um majority of time We're still waiting for the hint states to be extracted and training comparing to hinstates extraction is still basically nothing and we would like um to in the future speculators is shifting focus from algorithms and correctness to um throughput and efficiency. We're adding lots of um performance benchmarking on our training to figure out what exactly the bottleneck is and how to make training as efficient and as as as fast as possible. There are a lot of things

**[15:00](https://www.youtube.com/watch?v=K6FddIlAIOk&t=900s)** we can do. There are more replicas of VLM and having more KV headroom and uh tune a number of data loader workers and optimize compute. If you have any ideas, feel free to share it with us. create issues, get engaged and finally why using VLM on draft on on serving a draft model um we have great feature async scheduling that's been introduced so as little downtime as possible while the GPU is running step n theuler already prepares for uh step n plus one and the copy of m n m minus one drains so the drafter runs inside the same execute model and the full CUDA graph um draft step is in one full graph. So there's no

**[15:50](https://www.youtube.com/watch?v=K6FddIlAIOk&t=950s)** perlaunch overhead for a tiny drafter. And finally, I'd like to thank Vera um to generously let us borrow their amazing machine. They are a full stack AI cloud company that has data centers, networking, and platform software. And they have a great ML system engineering team that ties it together. uh please scan it for our repositories if you're interested in training your own speculators or fine-tuning your own speculators and please uh via serve our uh redhead AI comm3 speculator dspark model we have more interesting and exciting checkpoint come out uh please reach out and um create issues contribute we're on V on Slack we're

**[16:40](https://www.youtube.com/watch?v=K6FddIlAIOk&t=1000s)** easily reachable And thank you for thank you for your time.
