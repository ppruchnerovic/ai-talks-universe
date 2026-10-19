---
id: XczFLWEntiE
title: "AI Apps in a Flash: Ship to GPUs Without Docker — Dean Quiñanola, Runpod"
slug: ai-apps-in-a-flash-ship-to-gpus-without-docker-dean
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Dean Quiñanola"]
channel: "AI Engineer"
duration_min: 14
published_at: 2026-10-11T18:00:22Z
video_id: XczFLWEntiE
url: https://www.youtube.com/watch?v=XczFLWEntiE
youtube_url: https://www.youtube.com/watch?v=XczFLWEntiE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Runpod", "Runpod Flash", "serverless GPU", "GPU cloud", "AI deployment", "Docker", "DevOps", "Python", "MLOps", "AI infrastructure", "image generation", "text generation", "developer experience", "Dean Quiñanola", "AI Engineer"]
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# AI Apps in a Flash: Ship to GPUs Without Docker — Dean Quiñanola, Runpod

**Dean Quiñanola**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Runpod` `#Runpod Flash` `#serverless GPU` `#GPU cloud` `#AI deployment` `#Docker` `#DevOps` `#Python` `#MLOps` `#AI infrastructure` `#image generation` `#text generation` `#developer experience` `#Dean Quiñanola` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=XczFLWEntiE) · [Conference site](https://www.ai.engineer/)

## Description

Write code, build the image, push it, run it, find a bug, repeat. One loop can take 15 minutes. Runpod Flash cuts it out.

Dean Quiñanola, staff engineer at Runpod, introduces Runpod Flash, which lets you run Python on cloud GPUs as if the GPU were local, with no Dockerfiles, image builds or registry pushes. He covers serverless queue and load-balanced endpoints, endpoints that call each other like local functions, network volumes with warm caching, and live serverless for instant iteration. In a live demo he checks which GPU he's on (an RTX 4090), evolves the same function into text generation and then image generation, installing dependencies on the fly, and deploys it to production with one command that packages and serves the app without Docker. He also shows off a hackathon project that fans experiments out across endpoints, and how to get started.

In this talk:
• Why the Docker build-push-run loop slows AI development
• Live serverless: iterate on cloud GPUs like they're local
• Endpoint-to-endpoint calls, network volumes and warm caching
• Deploying to production with one command, no Docker

SPEAKER
Dean Quiñanola, Staff Software Engineer, Runpod

LINKS
Runpod Flash: https://runpod.io/flash
Flash docs: https://docs.runpod.io/flash
Flash (GitHub): https://github.com/runpod/flash
Flash examples (GitHub): https://github.com/runpod/flash-examples

CHAPTERS
0:00 Intro
0:27 The Docker loop
1:12 Why we built Flash
2:21 What Flash can do
2:41 Endpoint-to-endpoint calls
3:16 Live serverless
4:06 Demo: flash dev
5:40 Iterating: text generation
7:10 Fixing it live
7:59 Image generation
10:09 Deploying with flash deploy
11:13 Calling the deployed endpoint
12:18 A hackathon win
13:13 Getting started

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*1,747 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=XczFLWEntiE&t=12s)** Hello, good afternoon everyone. I'm uh Dean Kinyanola from Runpod Flash and um I want to talk to you about how you might be able to deploy AI applications without Docker. So currently this is how you deploy a serverless application. Well, especially AI applications. You write code, you build your docker file, you run a bunch of commands, docker build, all that. And then you push the image to docker hub. Then you execute it. Then maybe you'll get what you want. If not, you have to change your code again, rebuild it, repush it, execute. Um, in my experience, sometimes this one loop takes about 15 minutes depending on

**[1:01](https://www.youtube.com/watch?v=XczFLWEntiE&t=61s)** the changes you're doing. So, my name is Dean Kinyanola. I am a staff engineer at RunPod and I have an entire team that's working on making that easy. So, why did we build flash? development iteration loop requires a makeover. It's really a hassle. A lot of you guys are software engineers or ML engineers who really don't want to deal with all the DevOps. So, as you're working on your ideas or as you're working on your experiments, you want the results. So, no more need for Docker. Run code like it's local, as if you have the GPU. Uh test your changes instantly and debug quickly if you need to. So this is how we're thinking about keeping it simple. You write your code,

**[1:50](https://www.youtube.com/watch?v=XczFLWEntiE&t=110s)** you execute, you get the results. Rewrite your code, execute, you get the results. Right? Of course, there's the deployment part. I'll talk about that later. So it's so simple it feels like it's running locally. So what are the features that we have? So we are able to build and deploy faster. We optimize the resource utilization. There's a lot of tricks happening under the hood and it's intuitive. It's just Python code. It's really whatever you can run locally with a GPU, just do it on the cloud. So, what can you do with Flash today? We have serverless endpoints. It's mostly locked on serverless right now, but we're working towards doing it for pods. Uh we have Q endpoints for it and load balance endpoints that you can use it for. Here's the uh really cool feature

**[2:40](https://www.youtube.com/watch?v=XczFLWEntiE&t=160s)** that I put in an endpoint to endpoint communication. Sometimes you're building all these servers, but then you still have to know how to contact each server, right? You don't have to do that with this because it's just a code talking to another code. You execute a function and it looks like it's just local, but once you deploy it in different endpoints, it's all talking to each other. It's all happening under the hood. We also have network volume attachments. Um we have warm caching in network volume attachments so that if you ever have to scale up with your serverless endpoints then it has those cache carried over through the network volumes. And then the most important part is the live serless. Uh you are coding and testing as if it's all happening in your local system. And then you know this would

**[3:29](https://www.youtube.com/watch?v=XczFLWEntiE&t=209s)** just be a toy project if you can't deploy to production, right? So you want to deploy to production. So serve the inference, serve all the uh stuff that you're building. And we're making that possible all through the CLI. So let's get a demo. Hopefully I can do this with one hand. Okay. All right. So my demo here shows the the rapid iteration and evolution of a function. So the first function is just talking to torch getting what kind of GPU you have. So I'll do this live. I'll do flash dev. And what this does is it launches a fast API local host. So you can actually toy around with it. So now you want to

**[4:18](https://www.youtube.com/watch?v=XczFLWEntiE&t=258s)** try it out. Let's try it out. Execute. So it's provisioning this serverless endpoint. And if we go to runpod console, refresh this, you'll see this. This is running now. And as it's loading, let's let's show the logs. So you can actually see it. All right. Workers ready. Yep. Oh John. Cold start. This is common with all

**[5:08](https://www.youtube.com/watch?v=XczFLWEntiE&t=308s)** serverless platforms. Oh, there it is. So, it's running. We got logs, container logs. So, it's testing all these things, making sure it's all healthy, and it ran the job. So, now if we go back here, you'll see the result. It ran on an Nvidia GeForce RTX 4090. You see all the RAM, GPU count. Now, here's the kicker. What if I want to change this function and just want to test it? So, here's a different iteration of this function. What we do is we add more code. And this code really just does generation of text. And I've added some dependencies, the Python dependencies

**[5:56](https://www.youtube.com/watch?v=XczFLWEntiE&t=356s)** here. Oh, actually, let's do this without the hugging face token first. Let's see what's happening. See, it refreshed everything. I refreshed this. Test it again. What prompt do we need? Uh, let's do string cheese. Is it real? Run it. You see it again here. Container. Okay. It's coming up. You'll see all the the logs are simpler here because you're not supposed to be inundated with so much stuff. But what it's doing is in on the fly installing the dependencies and it

**[6:47](https://www.youtube.com/watch?v=XczFLWEntiE&t=407s)** even gave me a warning about communicating with the hugging face server without the token and it should be finished. Okay, now it's finished. Let's see the result. I ask is string cheese real? I'm sorry but I cannot provide answers. All right, that's that's spicy. All right, let's let's change that up. Let's enable my HF token. That's just changing the code right now. We release this again. Let's change the uh prompt. Let's see who is Batman. Let's execute that. Ready? And let's see how's this working

**[7:38](https://www.youtube.com/watch?v=XczFLWEntiE&t=458s)** here. It's cool. I'm doing this with one hand. >> All right, let's finish. Now we see the result. Oh, there. There you go. Batman's a fictional character. All right, we knew that. Let's go for something that's more intensive than just generating text. Now, we'll do an image generation. All right, it refreshed. Let's refresh this local host. Now you see generate image and then we'll test this out with a prompt. Let's create an image of a string cheese Batman.

**[8:29](https://www.youtube.com/watch?v=XczFLWEntiE&t=509s)** All right, this is how creative AI could be. Let's look at what's happening here. Running logs. Oh, look at that. Roll out in progress. Okay. I got plenty of time. That's not it. All right. I just had to terminate that because it was running the the older version. All right. Now it's new. I didn't want to wait for that roll out.

**[9:20](https://www.youtube.com/watch?v=XczFLWEntiE&t=560s)** I just want to see string cheese Batman. All right. So, it's it responded with a base 64. Okay. Let me clean that up before I show that. So how you can render this is through the browser. All right, let's see what string cheese Batman looks like. That's not string cheese, but that proves it right. It did it. Now, what if you want to deploy this? So, check this out. When I cancel it, it actually deprovisioned that endpoint. So, you don't have to have that lying around.

**[10:09](https://www.youtube.com/watch?v=XczFLWEntiE&t=609s)** See, it's gone now. Now, what if we want to deploy this? So, let's deploy that. Flash deploy. That packages up the whole thing, builds it up, sends it to our servers. Again, no Docker. You're not dealing with Docker here. This is instantaneous packaging of your application, sending it out to our servers, and serving it. Now, here's the cool part. Once it's out there, I have prepared this prompt, but I just need to change this ID later because this is going to matter. All right. So, it's created the archive built flash. All right. Sending it out. Uploaded. Deploying. Now it's up. All

**[11:01](https://www.youtube.com/watch?v=XczFLWEntiE&t=661s)** right. Let's see the ID here. Okay. Now, let's get this going. So, my prompt is a cute baby sea otter with a bow tie. Generate that image. Oh, yeah. I want to show you where this is. Now this is fully servable, right? Like you can have your customers, you know, use your application that uses this back end. It no longer lives in my local host. This is being hosted. All right, let's see workers log. Okay, when it's done, it should print the output here.

**[11:51](https://www.youtube.com/watch?v=XczFLWEntiE&t=711s)** There we go. All right, let me wrap this so I could pull this up. This is crazy doing it in one hand. All right, let's load up the picture of a sea otter with a bow tie. There's no bow tie. But that's not the point. We All right. So, you get that. That's the demo. We had a hackathon yesterday and I just wanted to be to present this to I'm very proud of this guy uh Funka. He created a wrapper around our flash that enables you to upload a data sheet of all your experiments of some specifications of some models and run it instantly and it

**[12:40](https://www.youtube.com/watch?v=XczFLWEntiE&t=760s)** just fans out builds out all these endpoints runs your training and then reports back to you. And he did this within three to four hours. And he had no idea how to do runpod flash. He had to ask me questions if this was even possible. I'm like, let's see. And he was very surprised when he won yesterday because his his project was not even his best one apparently and he keeps losing to other hackathons. So just really proud of this guy. How do you get started with runpad flash? So, well, you sign up for an account on RunPod, scan that QR code, get some $10 uh credit now, and all you really have to do is just install it, write your code, log in to have your uh API key in there, initialize, it'll have

**[13:31](https://www.youtube.com/watch?v=XczFLWEntiE&t=811s)** some skeleton application if you want, flash, the local dev that you have, or flash deploy to production. And we have all these URLs. The best advice I have is visit the runbot flash examples on GitHub because we have all these cases and examples that you could kind of refer or if you like AI coding just run cloud code into that repository and it will learn everything. We also have skills if you're into that. And that is my presentation.
