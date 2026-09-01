---
id: K8-vXq49Kuc
title: "AI Launchpad 2026: Mixtrain"
slug: ai-launchpad-2026-mixtrain
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 12
published_at: 2026-06-23T22:57:04Z
video_id: K8-vXq49Kuc
youtube_url: https://www.youtube.com/watch?v=K8-vXq49Kuc
tags: ["AI"]
transcript: true
---

# AI Launchpad 2026: Mixtrain

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `12 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=K8-vXq49Kuc) · [Conference site](https://www.aicouncil.com/)

## Description

Mixtrain provides infrastructure for the full post-training lifecycle, spanning data curation, training, evaluation, and deployment

SPEAKER:
Dharmesh Kakadia - Founder & CEO, Mixtrain

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*2,028 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=0s)** I'm going to try to convince you in the next 10 minutes not only why you should build the specialized model but it is easy, fast, and cheaper than than the general model that you are used to running. The fundamental argument about why build a specialized model is because your task are specialized. What I mean by task being specialized is if you work in a domain that is not the focus of the main frontier labs that is hill climbing then you absolutely are not getting the best model for your job. If you're doing coding as a task obviously you should rely on the frontier models as the hill climbing there is is really steep by the frontier models. The moment you step out of that whether you are doing it robotics whether you are doing object detection whether you are doing

**[0:47](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=47s)** the other vision based task and so on any one of these task is not a focus of the frontier model and all of these LLMs are not going to be giving you the best performance for your task. Um So let's get into the why why we are in the first place in this business. When you ask somebody like do you want the best model? Of course everyone wants the best model. Show of hands if anybody in the audience thinks that they don't want the best model. Right? At the end of the day the best is although very difficult to define. So best in terms of what accuracy for your task best in terms of latency for your task best in terms of cost and the answer to that obviously also is all of the above and some combination of the all of the above. It's not that if if you have to pay for

**[1:35](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=95s)** million dollar for each inference endpoint for each inference you are not going to get the the most out of the model not because the model is not the best but because it's not cost efficient for your business to integrate that into your stack. Similarly for what job like if you are in a domain which is not the focus you are not going to get the best performance. So ultimately what it ends up looking like is So, here is a radar chart which is essentially showing different capabilities that you might care about, right? So, you might care about the deployment efficiency, you might care about the accuracy for your task, you might care about the cost, you might care about the privacy. And and you are also might lately given the the stability of the infants APIs from the from the providers, you might also care about the longevity of the the APIs themselves.

**[2:22](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=142s)** You are going to have to sacrifice that by doing some taking a model in this case let's say it's on 10 on 10 on a task and then so-so on the other tasks. You can otherwise take a different model which is say an open source model in this case highlighted by a red line that gives you a lot of deployment flexibility. You can deploy it anywhere because it's an open source model but you're not going to get the best performance because it's not a domain fit for your model. You can go a step further and domain adapt your model for that particular task for that particular cost efficiency that you care about for your particular hardware. The specialization does not stop at any particular point in in the specialization journey. It is about what makes sense for you as a business, what makes sense for you as a task. And notice how we only have three choices.

**[3:10](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=190s)** Like that's the world that I don't think we should live in. We should live in the world where we have so many choices that you can't really see each line on that radar graph because each task and each domain has enough specialty that you can actually get a lot more out of it if you focus on that. So, what I'm and you might have seen similar graph like the moment you have a task in a domain data, the specialized model is going to outperform a generalized model. Doing that today remains very very hard and one of the reason why it remains hard is the infrastructure. And MixTrain is trying to solve that problem by giving you the frontier grade infrastructure for your task for your domain so that you can build a specialized model. It gives you data infrastructure, training infrastructure and the eval deployment. Now, you might think all of this is like very theoretical and and so on. What I'm going to try to do

**[3:59](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=239s)** in next 5 to 10 minutes is going to show you that not only you can build a specialized model that is better at a vision task than a frontier grade LLM. And I'll show you the demo for that. For demo, we are going to basically build a GeoGuessr game. I don't know if you have ever played the GeoGuessr game, but the task here is to show take take an image and guess which part of the world the image is in. So, we are going to build a model that is using our algorithm, in this case a PPO algorithm, that is going to give a certain amount of reward if you get the country right, if you get the region within the country right, and within the at the city level, and at the distance from the actual target. So, let's see what what we are going to do here. The first thing is We are launching Claude because I'm not

**[4:49](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=289s)** going to write all the training code myself. I am going to try and show you that I have installed a mix train as a skill. So, skill is in this case a markdown document because of which Claude knows how to talk to mix train the platform. Since this is a I have a prompt that basically summarizes the same thing that I said on the slide. Let's build a GeoGuessr model and we are going to try and do that. Given the the time it is going to take, I have taken the liberty to show you the previous version of the same output of the prompt. And we are going to try and run it. So, here is the the workflow that it will produce. Notice that the the Claude will actually produce the exact same workflow. It's not going to just produce

**[5:36](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=336s)** a script that is sitting on your local machine. It's going to produce the exact same workflow that you can run directly by the same command. Here I'm using the two data sets, GeoGuessr train and eval, and I'm running it for just four steps. Um Let's see what this looks like. So, while the model is running and I'll keep coming back to this while it's running. Let me show you what the data set looks like. So, in this case the data set is OpenStreet data set where I have taken the image from the OpenStreet and the ground truth for each of this there's the country code as well as the region and the city. Some of you might realize like this is a New Mexico for example and so on. When you are doing a training you are

**[6:25](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=385s)** not just after any random data set. What you are after is data set that is good enough for training. So, in this case let's first see the data that we just saw but let's also see I want to do analyze what the distribution of the the images are. So, what you're going to see is group by country in this case. And then order by country descending. Actually, let me do the the ordering by count so that it makes life easier to see. So here

**[7:13](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=433s)** it is actually going to show you that you in this case the US has the highest number of images and followed by Russia and Australia. This is a very good start but when you're talking about a multimedia models this is not good enough. Right? So, what you don't know is if there is some bias in the images themselves. So, what I'm going to also try to show you is the distribution of the images themselves. So, here I'm going to use an actual embedding model. So, we are going to take each image, run a vector model on it to produce an embedding that is 512 by 512, and it should show you us a distribution of country. So, in this case, the the distribution looks all over the place, which is actually the right distribution for this task.

**[8:00](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=480s)** What we're essentially showing is if you just want to see US examples, it is not clustered together, which means just by looking at image, the model cannot cheat and and decide that I can I can quickly figure out particular image. Um this is very similar than the eval set is very similar. It does not have the eval set is very similar holdout data set that we're going to use. Um so, as you can see here, the run that I just started at it started running within like seconds. It is now actually still running. So, let me actually show you what the output of that run will look like. In that case, this is the the example output of this. Notice that it did not just produce the

**[8:47](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=527s)** training script. It didn't just not not produce the model weights themselves, but it also produced the the Sorry. The zooming in is not working for the the image themselves. So, it is actually going to also produce the output that is showing where is the ground truth and where is the prediction for the entire data set. This is in addition to other summary metrics that it is producing, which is Okay. There's some issue on the zooming in. Cool. So, in this case, it's not only producing that, but also producing the the amount of the loss per step and so on. Since the the image is not

**[9:35](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=575s)** clicking properly, I'm I'm going to skip that part. The other thing that you can try and show in this case is the model themselves. So, I here notice that the model that we just produced is directly available for inference the very second. It's not just producing the weight, it is producing a model that you can directly call today. Um and so which we are going to try and run by uploading an image. Let's say this image. And while it's doing that, let me also show you why you need to specialize. So, let's pick this image from URL. Ask ChatGPT um the same question. Um to guess our game. Where is this from?

**[10:27](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=627s)** Um and you can see like the the model uh here the output should be um producing the result. Um that is showing somewhere in Southeast Asia, Thailand, where the image is actually from India. Um and as you as you saw here and All right. So, once that is there, we can also see the final URLs that it produced. Let's see how our run doing. So, our run finished

**[11:13](https://www.youtube.com/watch?v=K8-vXq49Kuc&t=673s)** right on time, I would say and uh Yeah, I think since since I'm running out of time I'm going to skip showing you the the exact URL, but it is going to actually There it is. The The URL is actually going to look like um a particular um ground truth and and prediction on the world map. So, thank you guys. Um I'm going to uh skip the the details of our infra and just sign up for the the on the website you are going to get a $100 free credit for creating your first specialized model. Uh if you're ever thinking about creating your own model, uh come talk to me. Thank you. >> [music]
