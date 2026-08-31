---
id: Doi4WCb0C9I
title: "Lightning Talk: Roche's Kubeflow Story: Large Models in Seconds, Costs Cut, Securit... Oswaldo Gomez"
slug: lightning-talk-roche-s-kubeflow-story-large-models-in
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 11
published_at: 2026-04-13T23:36:03Z
video_id: Doi4WCb0C9I
youtube_url: https://www.youtube.com/watch?v=Doi4WCb0C9I
tags: []
transcript: true
---

# Lightning Talk: Roche's Kubeflow Story: Large Models in Seconds, Costs Cut, Securit... Oswaldo Gomez

**Speaker not identified**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=Doi4WCb0C9I) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Lightning Talk: Roche's Kubeflow Story: Large Models in Seconds, Costs Cut, Security up With Bottlerocket - Oswaldo Gomez, Roche

At Roche pRED, our MLOps platform runs hundreds of ML endpoints for scientific discovery. Spikes in traffic were causing timeouts, as our large (13.4GB+) GPU models took ~10 minutes for a cold-start pull. To ensure quick responses, we were forced to set min=1 replicas, resulting in over $100K in annual waste for idle nodes. This was unsustainable, especially as we retrain and deploy new models daily.

This is our end-user story of how we solved this by adopting Karpenter for rapid node autoscaling and Bottlerocket on EKS. We will detail the specific technique of using Bottlerocket's mutable data volume to prefetch large container images before pods are scheduled.

We will show load-test data (20K API calls) that proves how we cut pull times from minutes to seconds, achieving a 58% faster cold-start. Learn how this combination enabled true scale-to-zero (even for GPUs), slashed costs, and enhanced security with an immutable OS

## Transcript

*1,750 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=0s)** Hello everyone. So, my name is Osvaldo Gomez. Um I'm I'm here to talk about our Roche Kubeflow story. Um we are I want to share with you how we managed to call to reduce the cold start by using open source technology and I think it's something that it's resonating with a lot of colleagues that I've talked to today. I'm originally from Mexico, so a little bit far away from from here, but I've been living for 5 years in Poland. And for the last approximately 7 years I've been doing stuff around AI on Kubernetes. And this is my second KubeCon in in Europe and yeah, the first one was in the other side of the of the ocean. >> [snorts] >> Okay, so I want to share with you some of our some of the work that we do. So,

**[0:48](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=48s)** we cover a wide span from target assessment. I work for a pharma company, so we do things like target assessment and identification, lead identification, early development. And all of that because we're not, you know, here for a biology talk, we do we have 140 case of predictions predictors. And we generate each month 150 million predictions. And when I'm talking about predictions, it means a lot of different things. So, we do things like embedding for example. We have an embedding model. We have two different embedding models. Each one can scale from 0 to 80 GPUs. So, we have it's very very fast scaling out behavior. However, I noticed that the cold start was about

**[1:36](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=96s)** like 10 minutes for embedding model, but we also are now doing protein folding. And this was this is a very gigantic for our purposes. It's very cool science, but for our purposes, it's like a 26 GB Docker image, right? So, how do we go from like 15 minutes of cold start into six about 6 minutes? This is what I will share today. So, cold starts are not great because our scientists are expecting results immediately. And we cannot we cannot wait for like telling tell them to wait 15 minutes to get the results. Also, the scientists are using these predictions in user interfaces and I've seen them live and it's very nice because you can they can interact with a molecule and real time they can get

**[2:26](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=146s)** for example prediction about the solubility of the protein, no? So, they need to do this in a in the in the UI in a in a manner that's real time. So, if if we have a model because we want to save some money for example, that's using GPU that scales out in 10 minutes, then it's impossible to do that. So, at the very heart of our infrastructure we have Kubeflow. This in in yellow here. So, we have we have multiple different types of input data from pathology, genomics, and chemistry. And what we are after is of course some output, some insights, some safety assessment, lead optimization. And there's a lot of things happening in this like very long cold starts. First of all, you have to first provision the

**[3:14](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=194s)** EC2 instance. And for those of I mean we already tried our best by using Carpenter to reduce the the time it takes for the machine to be assigned to the Kubernetes cluster. And there's a lot of benefits. I'm sure you are aware with Carpenter. So, if you have no idea where to start, first check out Carpenter. But if you already have Carpenter like we do, there's other things happening. So, traditional Linux systems have are very heavy. They have about 500 packages. And what we experimented with and the solution that I'm presenting today is using Bottlerocket, which is a operating system that was created by AWS. And yeah, so a lot of the so

**[4:01](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=241s)** provisioning is one part, but also we are, you know, the image has to be pulled. If it's 26 GB, pulling takes a long time. Decompression takes a long time. So, it's not an easy task to to to fix. So, we have a a lot of money that's going out the drain because we have to keep the minimum of one replica always on. And this is what we are uh having forced to do. And even if we have this one replica, if you want to have two or three or replicas, the cold start is always present when there is a new node. So, there is this is not this is not a long-term solution even if we have, you know, infinite money. Like it's still you still need to provision new new machines. And this is this is something that combined into what we are

**[4:50](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=290s)** presenting today. So, the solution like I said is Bottlerocket. This open source like I want to like bold it, it's open source. It's built by AWS and it's optimized for EKS. And there is also one variant for VMware. And this open source it's it's like a purpose-built open source model. And then the sorry, the operating system. And this purpose-built is only having about 50 packages instead of 500 like for example Ubuntu, no? To give you some comparison. And we have what we are doing is we are the the operating system has an immutable file system and a data volume. And the data volume is where you can

**[5:39](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=339s)** prefetch all the data that you have. And what we are doing is we are prefetching all of the inference services Docker images and we are putting it inside of a data volume. Then we take a snap we stop the EC2 instance. We take a snapshot. We enable fast storage restore. And then we configured Carpenter to be aware of this snapshot. This process is is is basically something we can reuse. So, like I said we have we first discover these images. We build a Python We have a like a Python package that we created that it's a scanning the Kubernetes cluster. It's looking for all the inference services, looking for all the images, and it's basically grabbing

**[6:27](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=387s)** compiling a list. We also have like another YAML file that you can add additional Docker images if you are interested in pulling those as well. Then we launch the EC2. We pull from private registries or public registries. And then we create the EBS snapshot. Once we have the snapshot, we put we can reuse it many many times across multiple multiple Carpenter nodes. And this is where the magic links happen. There is a a custom resource definition called EC2 node class that's from Carpenter. And here if you you can actually add the snapshot ID from the the one that contains all of your Docker images so that you don't have to wait to pull this image.

**[7:17](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=437s)** And one thing that I I I I almost forgot to say, >> [gasps] >> the throughput is actually the most important thing here. I was experimenting first with IO2, but it's very expensive and I got a finance alert about my my decision there. So, I I started looking if I could use GP3, which is much much cheaper, and the cold start came back. But when I put the throughput at 1 GB per second or 1,000 here, so this line is super important, then I was getting exactly the same cold start as with IO2, which is two times more expensive. >> [snorts] >> We were actually looking to reduce the cold start by accident. We made much secure environment. Why why is this? Because this this Bottlerocket operating

**[8:05](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=485s)** system is used is immutable. It has the the the volume A is immutable. And we this immutability is means that there is no configuration drift. So, you choose an AMI. Amazon publishes the AMIs every couple of days even. And you can just automatically opt in to one of these snapshots. They have a Bottlerocket operator that automatically pulls the latest security patches for you, so you don't have to do that. So, you can increase, you know, security by just basically using this new operating system with with the operator. They have SELinux, which is security-enhanced Linux. So, this is like strict isolation and some CIS benchmarks. And now we have infrastructure as code, but enforced as immutable artifacts. And

**[8:54](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=534s)** that was kind of like on accident. But very nice and welcome. And this is the the result these are the results. So, here is an experiment that I that I I did a scaling from 0 to 10 replicas. Like I said, the cold start is reduced about 50 to 60%, but also scaling out to 10 replicas it's 246 seconds faster. So, we are basically able to serve our scientists our internal customers much faster. So, some of the takeaways. >> [gasps and sighs] >> We have a performance improvement. So, we have interactive AI. We are not waiting 15 minutes just to be able to deploy a new replica. And the cold start went down to 60% in

**[9:42](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=582s)** the most extreme and most difficult case with this 26 GB image. We have some cost savings that can can be up to 68%. And second stronger guardrails like with basically immutability, SELinux, and CIS alignment. So, let's connect. I I just published right now a demo of this because I only have 10 minutes. So, if you have some questions or if you're trying to implement this for the first time, just you know, send me a message and we can this I can help you you know, make sure that you are also able to reduce your cold start. And I And if you add me, then you will see the demo because I just published it. Finally uh I want to you know, make sure that you if you're interested in ways to uh lower your your cloud costs, uh

**[10:31](https://www.youtube.com/watch?v=Doi4WCb0C9I&t=631s)** please come tomorrow to Sorry, day after tomorrow on Wednesday, Małgorzata Wilczyńska and Łukasz Agrodowczyk will come and give you a very nice talk. They're also here, so you can talk to them and if you have any questions. And of course, a special thanks to my period and my old team who's here in the crowd. I really appreciate your support. And of course, all of you who are listening, uh very very nice uh thank you so much for listening. And that's it.
