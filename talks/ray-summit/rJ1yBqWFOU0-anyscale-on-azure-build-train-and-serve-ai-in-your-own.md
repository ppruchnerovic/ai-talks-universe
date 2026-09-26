---
id: rJ1yBqWFOU0
title: "Anyscale on Azure: Build, Train, and Serve AI in Your Own Tenant | Microsoft | Ray Summit 2026"
slug: anyscale-on-azure-build-train-and-serve-ai-in-your-own
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 14
published_at: 2026-09-17T16:06:21Z
video_id: rJ1yBqWFOU0
url: https://www.youtube.com/watch?v=rJ1yBqWFOU0
youtube_url: https://www.youtube.com/watch?v=rJ1yBqWFOU0
tags: []
topics: []
transcript: true
---

# Anyscale on Azure: Build, Train, and Serve AI in Your Own Tenant | Microsoft | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=rJ1yBqWFOU0) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Anyscale on Azure is an Azure-native integration co-engineered with Microsoft. Built on Ray and AKS, it helps teams run Python AI workloads on Azure with more speed, flexibility, and control.

At Ray Summit 2026, Daniel Arrizza, Field Engineer at Anyscale, and Bob Mital, Product Manager at Microsoft, show how it removes the familiar AI platform tradeoff between developer agility and platform governance, giving ML teams a faster way to build and run AI while helping platform teams keep operations under control.

You'll leave knowing how to build, train, and serve AI in your own Azure tenant.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,343 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=6s)** Okay. All right. Well, hey everybody. My name is Danny Laritz. I am a partner field engineer at Anyscale. I'm here today with with Bob who's from Microsoft. We're going to talk about this exciting partnership that we have between Anyscale and Microsoft, what we've built, and yeah, we'll get into all of it. Well, Bob, do you want to get us started in all of it? Yeah. >> Sure. Thanks. Um well, here you go. So, let me start off by talking about with a story. And so, uh I was just recently chatting with a friend named Priya, and she's an AI engineer one of the leading AI startups. And um her leadership just told us that she needs to build a custom model, which is

**[0:54](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=54s)** using the company's proprietary data, fine-tuned on custom use cases, and fine-tuned for the company's data and use case. And so, now Priya's main job is to build this this custom model. However, her biggest challenge seems to be the infra because there's a massive amount of GPUs and CPUs. The GPUs are idle because the CPUs are processing. The cost is going up, and the CFO is having a challenge with that. And now, what is Priya doing instead of building AI models? She's babysitting the infra. And that's where the biggest challenge comes because Priya's main problem is she wants to be able to take these models, deploy them at massive scale on a

**[1:42](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=102s)** trusted platform, fine-tuned with her own data, managed for her, and be able to scale massively with privacy, security, and low latency. And so, with that, introducing Anyscale on Azure, which is a managed Ray platform that allows you to build this Azure native integration together. Firstly, with the open source Ray as a managed distributed engine. And then the Anyscale managed life cycle, which allows developers to use observability, the familiar tools with support, and finally something that's running in the customer subscription in their tenant through an Azure map agreement. So, how does this all come together? And

**[2:32](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=152s)** what are the different components of the two pieces of in this architecture? So, first is the control plane, which is running on Azure. And this is the familiar Anyscale control plane with all the dev tools, observability, APIs, cluster controller, orchestration, and so on. And then is the critical data plane. Cuz remember, Priya's job is to fine-tune the model on her company's custom data and not leak the data to a Frontier AI model. And so this Anyscale runtime is powered by Ray running in a customer's AKS subscription in in the AKS tenant with the data across a fleet of GPUs and CPUs. And all of this running on a trusted

**[3:22](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=202s)** platform with Azure infra across 80 plus regions with security and governance, with billing and cost management, and with private networking. So, what is the key takeaway? Your data and your models do not leave your Azure environment, and that is super critical because a lot of companies are worried about their data getting leaked to a Frontier model and then getting beaten down by them in terms of their IP getting leaked. >> And so finally, let's talk about the build, train, serve loop, which we heard a lot about in the keynote. And why this is a massive inference scale problem, because every time you're building, you're serving, you're fine-tuning, and then training again, this loop is what happens repeatedly,

**[4:11](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=251s)** which is a complex orchestration and infrastructure problem uh that an AI engineer does not want to spend time debugging and troubleshooting, rather focusing on building and scaling the AI workloads. And so here are some six use cases that we've seen our customers in Azure use. And first is like multi-model data pre-processing, which is curating and preparing image, video, audio, and text data sets for training. Distributed training, where you have you can reliability reliably scale them from 1 to 1,000 GPUs. And then finally, reinforcement learning. And again, with reinforcement learning, it's a complex challenge of orchestration and infra, because you're

**[4:58](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=298s)** running three jobs. One is you're taking your models, you're doing inferencing on them, you're getting the traces, then you're scoring them with reward models using CPUs for that, and once again, using training to update the weights. Once again, a complex infra and scaling challenge with CPUs and GPUs across different clusters, different regions, all coming together at massive scale. And across these six workloads, what you see is one platform with one runtime across the life cycle on a trusted infra like Azure. And some of the industries where we're seeing adoption is in autonomous, uh in in the physical AI, robotics,

**[5:47](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=347s)** where you have we are running thousands of simulations and then fintech and banking with low latency and risk modeling. I don't know Daniel if you want to speak to any of the use cases as well that you're seeing. >> Yeah, I mean all of them we're seeing. I would say a few that are pretty hot right now are the physical AI side of it the biosciences where we've got genomics and drug discovery been I've been pretty big. Some of these that are inherently multimodal where you've got video decoding that has to be done on CPU and then the actual LLMs that are on the GPU. So when you have both of those together that's the type of challenges that we help out with. >> Awesome. And then finally like talk about two large customers which are using any scale on Azure in production.

**[6:35](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=395s)** One is Wave which is an autonomous driving company based out of UK and they're using this petabytes of data video audio all taken together doing multimodal data processing and then training their own models for autonomous driving and so they're seeing a lot of success with any scale on Azure across the fleet. Another company is Zūprl which is a Spanish based startup which is using satellite imagery to train their models for intelligence. And so think about millions of kilometers of data uh trained within with their GPUs within seconds. And they are successfully deployed on any scale on Azure. So I think we're seeing a lot of success with enterprises use this.

**[7:23](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=443s)** And um I'm going to now talk about a little bit about the partnership we have with any scale and how we've come together. >> Yeah, awesome. Well, thank you Bob. Yeah, and those last two companies I'll tell you the scaling that is required in order to be able to process the amount of data they have is insane. Just a little bit about the kind of the story about why this all came together. Um, there were kind of two directions. Right? So, Kubernetes, amazing at scaling containers, and like from a lot of like traditional transactional applications. And that's what it was originally designed and isn't like the industry standard for. And then on the other side, we saw um, the uh, machine learning libraries like the PyTorches and things like that. And what was kind of missing was this middle ground where between the containers and the

**[8:12](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=492s)** libraries, where we have visibility and orchestration at the Python layer. And that allows, let's say, okay, I'm I'm running this pipeline, and we're backed up on this stage. Now we can go down to Kubernetes and say, "Hey, here's now the resources that we need to be able to to serve that." So, we put those two things together, and Brendan Burns, the one of the the fathers of Kubernetes, uh, saw that AI workloads are going to need this type of architecture, and this is the whole partnership came together, which is amazing to see. Um, and then I'll show a little demo of what it looks like on Azure today. This is something that you can pick up right now. All right? So, uh, you have a an Azure account, you go to portal.azure.com, you search any scale services, and you'll be able to to go off and do this, all right? We're currently in public

**[8:59](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=539s)** preview. GA is, uh, just around the corner. So, I just want to show you what it looks like in my account. And I wasn't brave enough to do this live, so I'm just going to like show you, uh, a little bit what's going on here. So, it really starts with Kubernetes, right? So, I've got a Kubernetes uh, cluster where maybe I have some applications running, uh, or I have some, uh, AI workloads in there already, perhaps. And so, I'm looking for my my my uh, my Kubernetes cluster here, and I've got some node pools. So, some that are CPU, some that are GPU. And I'm going to need to use both of them depending on the workload that I need. So, the next thing is is I wanted to deploy my Anyscale operator inside of my Kubernetes cluster. And so, now I'm going to say,

**[9:47](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=587s)** "Okay, create an Anyscale cloud." And I pick the subscription that my Kubernetes is in and I say, "Create. Okay." So, the next thing I do is I pick, "Okay, the what resource group is this going to be in?" So, I can kind of manage all the things around this. Uh and then I'm also going to pick the the region that this cluster is inside of. And then give my cloud a name. And finally pick the cluster that I want to to to add Anyscale inside of, all right? So, I just pick my cluster. Okay, I hit next. And the next part is I'm going to configure a storage account to be able to store some logs and things like that. And what's good is that all those logs and metrics, they get to stay here, right?

**[10:35](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=635s)** So, your data, your models, they don't leave your your subscription. We don't want them. And so, this really helps with the security approval and things like that. And now I'm I'm ready to go, right? So, I created an identity. So, we're using Entra ID for the identity portion of it. And yeah, I hit create and then I'm I'm ready to go. So, now I've got Anyscale on Azure set up in here. So, I'm going to look for my cloud in here. I got I pick my cloud and what I can do is now add the permission model around it. So, who should be able to have access to this cloud? And so, we're using Entra identity and permissions natively for who can be in there. So, then I can go check out some docs if I want. I'll hit launch Anyscale. I'm now

**[11:24](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=684s)** inside of the Anyscale console. And in here I can launch up my my workspaces to do interactive of the I can be doing jobs. Yeah, or I can be running services as well, too. >> Just want to add here, I think the the benefit of an Azure native integration is you use your same identity, your Azure AD, to then just log in seamlessly from within portal to the Anyscale portal. So, you don't have to like re-sign it, add another email address, or whatever. It's fully baked in. And so, the native service allows you that flexibility of deploying it right from your Azure portal. >> Yeah, that's definitely one of the like one of the main key benefits of it is that um we can actually get this deployed in your environment. Like, you it'll go through an enterprise governance and security review successfully, right?

**[12:11](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=731s)** Because there's been so much vetting of the Azure cloud that um you know, we we can make if we're integrated in that, then we're we're usually pretty good. Um I do want to even mess um talk about here very quickly that um I was going through um a full enterprise review with a customer, uh and they had some very serious requirements in regulated industries around being able to deploy in that environment with no questions asked from the their security team. And so, I've got a a Terraform of a private cluster where we're using every possible private Azure service to be able to fully uh pass that sort of kind of security review. Uh I won't go through all of it, but there's just like a lot that Azure uh uh uh offers in this area. And so, you'll

**[13:02](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=782s)** actually be able to get this rolled out in there. Um so, that's kind of the the the main thing that I wanted to show in terms of um you know, what the the capabilities are in terms of what the flow is to get installed. Um just want to thank Bob so so much for this partnership, and uh the entire Azure team for making this thing happen. I I want to encourage everybody to uh go to your Azure portal and check out Anyscale inside of there. There's a few of us here that work specifically on this partnership. So like a few people like Lou, if you want to raise your hand. So the folks that like you come to, some folks in the front here uh from from from from the Azure team and more. But anyways, thank you for for checking us out and any final words, Bob? >> Yeah, I think I just want to leave with one thought, right?

**[13:49](https://www.youtube.com/watch?v=rJ1yBqWFOU0&t=829s)** The AI scientist or the AI engineer should focus on building AI workloads and leave the infra and the scale and the trust to like experts like us where we manage infra at massive scale for enterprises. So that way you just focus on what you're good at and leave the rest to us and not worry about the infra kings with scaling and so on. >> All right. It's true. It's awesome. All right, well thank you everybody. Appreciate attending. Thank you. >> [cheering]
