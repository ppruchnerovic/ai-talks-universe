---
id: N5T7l_TX2TI
title: "From Reservation to 1,600 GPUs: A Petabyte-Scale Ray Data Pipeline | CoreWeave | Ray Summit 2026"
slug: from-reservation-to-1-600-gpus-a-petabyte-scale-ray-data
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 14
published_at: 2026-09-17T16:06:55Z
video_id: N5T7l_TX2TI
url: https://www.youtube.com/watch?v=N5T7l_TX2TI
youtube_url: https://www.youtube.com/watch?v=N5T7l_TX2TI
tags: []
topics: ["Data engineering & MLOps", "Inference, serving & GPU infra"]
transcript: true
---

# From Reservation to 1,600 GPUs: A Petabyte-Scale Ray Data Pipeline | CoreWeave | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=N5T7l_TX2TI) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

What does it take to go from a fresh GPU reservation to a production-scale multimodal data pipeline in less than a day? Scaled to 1,600 GPUs and a 0.6 PB dataset, this pipeline generated 70 million captions in 1 hour and 35 minutes, with storage never becoming the bottleneck.

At Ray Summit 2026, Xinyu Zhang, Software Engineer at Anyscale, and Jeff Braunstein, Senior Director of Product at CoreWeave, walk through standing up and optimizing a large-scale video captioning workflow on Anyscale on CoreWeave in under 24 hours: the shift from a Ray Core implementation to Ray Data, why streaming execution and autoscaling mattered, and how that change delivered 3.7x more captions per GPU-hour on the initial 600 GB workload.

You'll leave with concrete lessons for building GPU-efficient, storage-aware data pipelines for large-scale AI workloads on Ray.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,079 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=6s)** Hey everybody, I'm uh Jeff Bronstein from Cororeweave. I'm here with Ginyu Jiang uh from Any Scale and today we're going to talk to you about u the project we did to bring a workload on Coreeave using uh Ray data from a brand new account on Coreeave to running 1600 GPUs in production in under 24 hours. really excited about it. Uh for those of you who don't know Coreweave, um we are the oops um we're the AI cloud built for production. We provide an integrated multimodal uh focused foundation platform spanning high performance compute networking storage orchestration training experiment tracking, evaluation, and more. And we help we we help people move AI workloads from experimentation to a reliable efficient scale. And if you're curious

**[0:53](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=53s)** about us, we've got a booth right over there. Um so the challenge began with uh an account that we gave to any scale with a workload that we wanted to try to test out. Um what we wanted to do is both see how fast we could get the production workload going and started and then once it started how fast could we make it run. Uh and so what we did is we tried to um bring up 600 terabytes of video and get them ready for use in training. Uh so what we did the goal was to basically um uh caption videos for use in training. So what we needed to do is uh look at a large set of of video data 600 terabytes in total uh scan it find all the unique sections of it create

**[1:43](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=103s)** images and then point those images to uh in an inference stack to a GPU so that we could add a caption to them. And here's an example of what that looks like. I'm sure you're all familiar. uh and then that that allows this data to be used for training. So this was a uh train a pre-training workload but we were using inference we were using GPUs in order to prepare the data and we were doing this at very large scale. So we wanted to see how fast we could do this. So here was the timeline we gave we gave uh uh the Anscale team our account brand new account never been used but with the GPUs and CPUs ready to go at hour zero. It had uh 200 uh RTX Pro uh 6000 Nvidia GPUs, the B40s they sometimes call them.

**[2:32](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=152s)** Um and a couple hundred uh CPU nodes as well. Uh the thing about Coreweave is that we provide a stack that is ready to run at scale from second one that you get on the stack. That includes our core kubernetes service uh which allows you to manage all your GPU and CPU nodes at scale immediately as well as our core AI object storage which we call chaos CIOS we pronounce it chaos. So the chaos storage is tightly integrated with the compute stack to provide high throughput so that the data can flow in and out of those uh compute nodes as quickly as possible. This is optimized storage for compute in the cloud that that nobody else really has. And so uh within an hour the Anycale

**[3:20](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=200s)** team had ray core and ray data running on the stack uh and started running test runs. Uh they started with going up to 600 gigabytes of videos. Once they were confident then they ran that went from ray core to ray data. Uh and then they brought that up to 600 terabytes of data. And at that scale, they were able to do 70 million uh captions using 1,600 GPUs in 90 minutes. Uh I was just talking to a customer after my presentation yesterday. It was taking him a day to do 100,000 and we did 70 million in 90 minutes. So this is a a scale that's unbelievable. Um, so it's it's both the rate at which you can get up to use and using the stack quickly, but then also the rate at which the stack actually works in production.

**[4:11](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=251s)** So the the way the flow worked was that um the any scale the ray data stack read. So we first had the videos on our object storage. We call it again coreweave AI object storage or chaos. That's where the video files were. um uh and then we read those into the CPUs to process them to prepare them uh for this process so that we could give these uh uh images to the GPUs. Um and then in step three we fed using uh VLM we uh set up uh an inference on each of those GPU nodes and those were able to look at the pictures and create the captions and then the data was written back by rated data back into the object storage. That's a simplified view of the process. I'm now going to talk hand it over to Ginu who's going to talk about uh uh the

**[4:59](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=299s)** uh Ray data side of the stack. >> Yeah, I'm very happy to like unwrap how like RA data works under the hood to process like 6 terabyte of data. So 6 terabyte of data is a huge uh amount of data and so like query we've provided like the out of the box uh storage solution um chaos and on top of that they have provided like a caching layer they allow like in the query cluster like there are like many GPUs and CPUs with used NVMe like local storage and in each node they cache like the terabytes of data inside of the like local cluster storage like a disk. So we can fetch um the like storage where it's actually

**[5:51](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=351s)** used. Um so the first stage of this video pipeline is like decoding. We have to like extract the videos from the disk storage and then using like the CPU like video decoders like fmp to extract the key frames from those videos. So in the second stage we get like the key frames from the videos and we load the VRM engines into the GPUs to process the images into like the captions that is going to be used for pre-training. So at this stage um it's going to be like a autoscaling pipeline because there are a ton of like videos in a

**[6:40](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=400s)** storage and we have to um we have two stages of processing which is CPU for decoding and uh the VRM engine in a GPUs for inference. So like Corey give us like two 200 nodes of like B200s and that's in total like 1,600 GPUs in total. And how do we scale that from like eight GPUs in a single node to 1,500 GPUs in total is where the magic happens with RE data. So like one obvious thing you could have when you have like a s such a large amount of nodes is you're going to have like failures. So raid data handles those failures by replacing the inference engines um and kick out the

**[7:29](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=449s)** failed nodes and like uh replace it with a brand new node. So in this case, we only use 1,500 out of them because we like um keep their enough like redundancy so like the failed nodes can always find the replacements to keep the pipeline running. So let's see how um the bottlenecks are occurring in this workload. So first of all in a rate data pipeline since you have like large u a large um like chunk of data in a storage however like a rate data doesn't really know like how it's um how much like data or how many videos you actually have to process. So in this case when um we impact the data rate

**[8:19](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=499s)** data naively thinks there are like only 150 blocks um of data um that like can be processed in parallel. But in the reality we have such a large amount of data with like 70 million videos in total 150 blocks are not enough to be processed in parallel. So we have to first of all repartition in a way that we have like enough number of parallel blocks to be fed into the CPU stage so we can like utilize the CPUs um at a full utilization. So the second block is actually um so after like removing the like part repartition u bottleneck we uh get this GPU flit saturated from 10% to 25%.

**[9:12](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=552s)** And the second bottleneck comes when um the GPUs are not saturated because like after like the CPUs decodes the videos, we don't actually know like how many videos should we uh process at the same time um to saturate the compute. So we need to tell like the rate data pipeline, hey we have like 16 1,500 GPUs to be utilized in total. Please go ahead and make full use of that um those GPUs. So in this case we like saturate the number of GPUs we are using. We use total like uh like the total like 1,500 GPUs and the utilization comes jumps from uh 25% to 54%. And why it is still

**[10:02](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=602s)** not saturated to 100% is because like the decoding is lagging behind at this stage. So when like the GPUs are like doing inference at maximum speed, we don't have enough number of CPUs to do the decoding and how do we like uh solve that problem is we kind of infer like the number of CPUs and GPUs that is um the ratio of number of CPUs and GPUs and the speed speed we should have for uh the number of CPUs inferred by like the total number of uh GPUs. In this case, we can have like the CPUs decoding at the pace and the velocity of GPUs are doing inference. So after we have like enough um and

**[10:51](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=651s)** saturating um decoded like frames to fed into GPUs and we have like a 100% utilized GPUs in a cluster which is amazing. So another takeaway for this is starvation could look like um satisfaction because when you have like a large um data site to process and if you don't specify how much hardware you're going to utilize for this workload your software is not going to be able to infer out of the box because it saturate it goes well like the the throughput looks fine and the rate data pipeline stops to um like spin off more nodes and and resources to um like accelerate the pipeline. So you need to

**[11:40](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=700s)** specifically tell like how much GPU resources you're going to use in this pipeline and how much CPUs are going to be used accordingly uh to the number of GPUs you have in mind. So another takeaway is like um fault is inevitable when you have like over a,500 GPUs for example if you have a very low probability for failure uh in each GPU and when you like go to exponential rate to a,500 that low probability could always translate to a must happen failure in your cluster and rate data helps you recover that fault um like using the na native like fault tolerance feature.

**[12:29](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=749s)** So the takeaway is like we processed like point6 terabyte of data with zero boat failures with zero stalls and we like complete the entire pipeline within one hour and a half which is um how we are able to achieve great um data processing speed um at um terabyte scale paby scale. So you can see in the diagram um we're able to keep the same throughput across different scales in a data site and different scales of like the clusters. So um like 256 GPUs performed almost the same for single GPU performance and throughput when we scaled up to 1,500 GPUs and like the um even and we iterated like the same data

**[13:20](https://www.youtube.com/watch?v=N5T7l_TX2TI&t=800s)** set for three times and the throughput stayed almost the same as well. So um yeah consider using like a ray and ray data for your um image or data processing pipeline. We are able to u manifest this success with 1,600 GPUs with core roof cluster. Um yeah and um looking forward to how you're going to be able to um fully release the potential of free data. >> Thanks a lot. Yeah. We'll be around for questions.
