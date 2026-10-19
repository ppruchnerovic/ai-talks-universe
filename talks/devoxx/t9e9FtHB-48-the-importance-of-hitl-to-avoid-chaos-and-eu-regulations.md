---
id: t9e9FtHB-48
title: "The Importance of HITL to Avoid Chaos and EU Regulations for AI by Juan Antonio Breña 🇪🇸🇪🇺"
slug: the-importance-of-hitl-to-avoid-chaos-and-eu-regulations
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2026
speakers: []
channel: "Devoxx"
duration_min: 20
published_at: 2026-10-07T05:59:16Z
video_id: t9e9FtHB-48
url: https://www.youtube.com/watch?v=t9e9FtHB-48
youtube_url: https://www.youtube.com/watch?v=t9e9FtHB-48
tags: []
topics: ["Governance, ethics & regulation"]
transcript: true
---

# The Importance of HITL to Avoid Chaos and EU Regulations for AI by Juan Antonio Breña 🇪🇸🇪🇺

**Speaker not identified**

`Devoxx` · `Devoxx` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=t9e9FtHB-48) · [Conference site](https://devoxx.com/)

## Description

*No description published on YouTube.*

## Transcript

*2,070 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=t9e9FtHB-48&t=1s)** [music] [music] [music] [music] >> Welcome everyone. So, this is Juan Antonio Breña and today we are going to talk about two interesting aspects in the age of AI agents. In this case, we're going to talk about the importance of reinforce the human in the loop in the pull request and also

**[0:50](https://www.youtube.com/watch?v=t9e9FtHB-48&t=50s)** now in the market appear a specific regulation about AI agents and how we can automate or increase the awareness in our deep things. Okay. So, this is Juan Antonio Breña. I work in IG, a trading company firm located in London. This particular talk we're going to talk about technology, but also about processes. The focus will be in how the senior software engineers interact with AI agents, okay? So, we will not talk about the models. And also how to apply in our daily work for brownfield projects. So, the agenda

**[1:37](https://www.youtube.com/watch?v=t9e9FtHB-48&t=97s)** will be focused on try to introduce the problem statement. Later, I will try to explain how we can improve the pull request and what is important to add and maintain the human in the loop in the processes. And finally, we will enter in some aspects about governance and regulations. So, if you serve in when you are working for large companies, people change, jump to one company to another. Existing internal rotation and now we are introducing AI agents tools. What happened with these kind of changes? Um sometimes some knowledge are in the mind of the engineers and it's possible to impact

**[2:25](https://www.youtube.com/watch?v=t9e9FtHB-48&t=145s)** the software development. So, what happened when someone pick up a an issue, make a small change in the repository, everything goes fine, but you deploy it to production and fails. I had the impression that I am not inventing this particular case, but it's important to remind us when you are using AI agents, it's important to to review the contest. Okay? So, when it fails, what happened? Maybe it's because your change impacts other subsystems. It's possible that your small change changes something in the in one Pascal contract or maybe you change it something in the

**[3:12](https://www.youtube.com/watch?v=t9e9FtHB-48&t=192s)** database. So, you need to review the consequence. And when you are thinking in this problem, it's pretty interesting to watch in the in this contest Conway's Law because with a fragmented context, it's possible that software engineers using AI tools, it's possible to accelerate potential changes. And maybe one team change something in one part of the system, another team change something in another part. So, we don't have control for that part. Okay? And this kind of new velocity in the software development is possible to accelerate potential issues in our systems. So, at the end uh also the new hype

**[4:01](https://www.youtube.com/watch?v=t9e9FtHB-48&t=241s)** put emphasis in this kind of new tooling is important to reinforce processes and and reinforce people, okay? So, maintain the ownership and communication improve the processes about specification and validation and obviously to use AI and tools in a good way. So at the end you could see that one small change doesn't generate an issue. But if you don't take care about the consequence maybe a small pull request review only will be considered as a cosmetic review.

**[4:49](https://www.youtube.com/watch?v=t9e9FtHB-48&t=289s)** And this is this is the starting point. So, how we can improve the pull request? So, at the end not it's not only like your pull pull request is in green, okay? And you review that you review the test and you review that everything is fine. It's necessary to to review the evidence. The evidence about the consequence. And also it's important that not everyone review your change. It's necessary that the people who review that change has the capacity to accept the change. So it's important that that pull request has notes about the consequence has the capacity >> [clears throat]

**[5:37](https://www.youtube.com/watch?v=t9e9FtHB-48&t=337s)** >> that doesn't break um that doesn't break the consumers and also matches with the regulation. The pull request needs to have that evidence described it. Okay. And also in that pull request you need to have the evidence about if something goes wrong you can roll back. That not always is possible. So So when you are sending that pull request depending on the change you need to select the right pull reviewer okay? And also when you are running that pull

**[6:27](https://www.youtube.com/watch?v=t9e9FtHB-48&t=387s)** request the reviewer needs to have the capacity to a stop and roll back because not all changes are acceptable. Also when you are >> [clears throat] >> affecting that pull request needs to be taken that the deployment needs to if something goes wrong is necessary to have the capacity to roll back and not always you have that capacity. So depending on the change you need to have that measure designed it and tested, okay? Well

**[7:18](https://www.youtube.com/watch?v=t9e9FtHB-48&t=438s)** we talked it about human in the loop in the process, okay? But when you are adding AI agents, okay? You need to think about the laws the frameworks and some of the >> [clears throat] >> Something pretty interesting that's introduced uh the new AI European AI Act is about the the neces- the need to have oversight. So, so this new regulation about AI Act try to protect ourself

**[8:06](https://www.youtube.com/watch?v=t9e9FtHB-48&t=486s)** because at the end with as a regulation like a depending on the classification of your system is mandatory to have a a a human reviewing that change. So, depending but not in all cases it required depending of the change. Okay? This is important. So, you could use a generative AI tools like for example close or others, okay? But depending on the nature of that change is the point that you require a mandatory review. What are the regulation you could have in mind? We talk about a AI tool a European AI Act, okay? As something new

**[8:57](https://www.youtube.com/watch?v=t9e9FtHB-48&t=537s)** that it will be adopted gradually by the companies but you have from the past GDPR and others about fiber security like crap, niche tool or Dora, okay? So, it's important to classify the change in the case of European AI Act, okay? And do um and store the evidence in the case of European AI Act. >> [clears throat] >> For the case of the GDPR for the case of the GDPR, you need to take care about what information you are returning in the channel, okay? And try to minimize the

**[9:47](https://www.youtube.com/watch?v=t9e9FtHB-48&t=587s)** number of data that you expose. This is something that is present from 2018. Okay? So, as you saw examples that I have added about login, about as I commented exposing data, okay? And something pretty interesting is when you make a change and for example, you are removing data, you need to take care about that change to remove data are propagated. So, it's not only that you change something in your repository that affect the data. It's like that later that consequence are propagated in the next services. Another important stuff

**[10:41](https://www.youtube.com/watch?v=t9e9FtHB-48&t=641s)** Yes. So, another regulation is about security, fibers resilience act okay? That is happening from this year, okay? So, in this particular case, we put focus on the security. And some examples that we can we can review in our repository is about the we need to review about if we have secrets, if we have insecure defaults, if we have a about bomb, okay? If we have about unsafe this serialization. Hey. Okay.

**[11:35](https://www.youtube.com/watch?v=t9e9FtHB-48&t=695s)** Another regulation about fever security is about NIST 2. That if it was a publicized in 2024, okay? So, it's something that you should apply. And some examples are about the login, reporting about when it happened that issue, >> [cough] >> an aspect about the uses of third-party SDKs. Something that we need to take care about is about the access of about permission over privileged access. We need to review if we have untested recovery

**[12:26](https://www.youtube.com/watch?v=t9e9FtHB-48&t=746s)** and bad configuration. This is some few examples that we can find from the regulation. Finally, this is something that maybe you know because maybe you apply it about DORA, is about the capacity that you have to to retry, okay? Your your capacity about resilience in your services, okay? And this is something that is applied from 2025. This is important that you review in your system that you have capacity to resilience. If you have a capacity to classify,

**[13:14](https://www.youtube.com/watch?v=t9e9FtHB-48&t=794s)** and finally, >> [clears throat] >> if you have the risk that few providers are part of your system. Also, it's important from Dora that you need to have plans to recover your system. And also about your inventory. So, here you can see that the calendar about that regulation. So, in your service we have introduced in European Union one regulation about AI AI AI Act, okay? That is improving. It's It's evolving. So,

**[14:02](https://www.youtube.com/watch?v=t9e9FtHB-48&t=842s)** it's not necessary to be applied, but others like NIS 2, GDPR, or Dora or CRA, you you need to apply, okay? So, what is possible to to to review? What is possible to to break? How was produced? And finally, what is the system? Well, as a technical way I would like to see that when you have um a pull request you need to label that pipeline, okay? In order that that code was generated by

**[14:52](https://www.youtube.com/watch?v=t9e9FtHB-48&t=892s)** by AI agents. Something that is pretty interesting is if you are serving in the in the slides maybe some regulation it could be possible to add new gates in your pipeline in order to create some evidence to help engineers because maybe using the combination from the regulation plus the pipelines, you can identify issues from GDPR, CRA, NIS chew, and aura. Also, it's important, as we mentioned in the second part of the talk, that not everyone is possible to validate and affect that pull request, depending of the of the change.

**[15:40](https://www.youtube.com/watch?v=t9e9FtHB-48&t=940s)** Also, something that you could review next week is about your capacity to roll back. Are you sure that your pipelines have the capacity to do roll back? Yes or not, and what is the evidence? Something that you could you could review is about where is your incidence. Review if your services has migration scripts because when you are using AI agents, okay, something that is not fully fixed is about the capacity to recover bad changes from databases. So, you could have contract testing, okay, for protect yourself and others

**[16:31](https://www.youtube.com/watch?v=t9e9FtHB-48&t=991s)** with rest contracts, and also for messaging contracts. But, what happened with your local service? Take care about the changes because if you are using AI agents, okay, it's possible that you will have issues in that way, okay? Also, it's it's important that teams are able to manage in a fluent way the pattern parallel change, that is super interesting. And why is interesting? Because parallel change is a good pattern, like when you do a change in your database, it's possible that to maintain the same service before and prepare the change for the future. In that case, you will not have a breaking change, basically. And this is important when you are maintaining a a large database in production.

**[17:24](https://www.youtube.com/watch?v=t9e9FtHB-48&t=1044s)** Also, when you are reviewing changes to improve your development, mono repos is a good practice. Why? Because if you have normally during the last 10 year more or less applying microservice architecture, okay? One service is like one repo. But now that we are using AI tools, the issue is like the context of the or your agent is only one service, one repository. So, using mono repos at least for the for the context of the whole subsystem is something useful. And that idea

**[18:13](https://www.youtube.com/watch?v=t9e9FtHB-48&t=1093s)** is interesting when we are talking about a good pull request because if you are using AI agents tools, it's possible it's possible to increase and enhance the context that the model are using. Something pretty interesting is about if your company, your team or area, okay, has common skills for particular service or at least for the most common stack. And finally, in order to mitigate potential issues when you are sending pull request and maybe that pull request doesn't match with the regulation, maybe it's interesting to use aspect

**[19:03](https://www.youtube.com/watch?v=t9e9FtHB-48&t=1143s)** driven development because it is a good vehicle to define your specification. I share the links for this regulation. And thank you so much. Well, maybe later we can we can talk about it in the in the corridor, okay? Thank you so much.

**[19:50](https://www.youtube.com/watch?v=t9e9FtHB-48&t=1190s)** Bye.
