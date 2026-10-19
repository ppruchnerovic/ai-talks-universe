---
id: pyvRID_CZZU
title: "We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI"
slug: we-built-an-ai-support-agent-that-resolves-80-of-tickets
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 16
published_at: 2026-10-04T15:00:15Z
video_id: pyvRID_CZZU
url: https://www.youtube.com/watch?v=pyvRID_CZZU
youtube_url: https://www.youtube.com/watch?v=pyvRID_CZZU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "AI support agent", "customer support AI", "forward deployed engineer", "FDE", "Claude Agent SDK", "voice agent", "voice AI", "Voice Agent API", "speech to text", "AssemblyAI", "Railway", "RAG", "agentic search", "Matt Lawler", "AI Engineer"]
topics: ["Agents & orchestration", "Multimodal, vision, speech & robotics", "RAG, retrieval & knowledge"]
transcript: true
---

# We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#AI support agent` `#customer support AI` `#forward deployed engineer` `#FDE` `#Claude Agent SDK` `#voice agent` `#voice AI` `#Voice Agent API` `#speech to text` `#AssemblyAI` `#Railway` `#RAG` `#agentic search` `#Matt Lawler` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=pyvRID_CZZU) · [Conference site](https://www.ai.engineer/)

## Description

1,000 API signups a day and one onboarding engineer. So AssemblyAI built Joey.

Matt Lawler, forward deployed engineer lead at AssemblyAI, shares how his team replaced an off-the-shelf support bot that resolved 10% of conversations with their own agent, Joey, which resolves 80% end to end for about $700 a month. Joey is built on the Claude Agent SDK with docs checked out as local markdown, embeddings for retrieval, agentic file search and a large CLAUDE.md. It's deployed on Railway so fixes ship in about 30 seconds. Then Matt gives Joey a voice with AssemblyAI's Voice Agent API and demos it live, making the case that FDEs should automate themselves out of a job and dogfood the product their customers build.

In this talk:
• Why the FDE model doesn't scale to 1,000 signups a day
• Joey's architecture: local markdown docs, embeddings, agentic search and a single CLAUDE.md
• Turning every escalation into a roadmap item for the agent
• Adding real-time voice with one websocket: speech-to-text, LLM and text-to-speech

SPEAKER
Matt Lawler, Forward Deployed Engineer Lead, AssemblyAI

LINKS
AssemblyAI: https://www.assemblyai.com
Voice Agent API docs: https://www.assemblyai.com/docs/voice-agents/voice-agent-api
Introducing the Voice Agent API: https://www.assemblyai.com/blog/introducing-our-voice-agent-api
AssemblyAI on X: https://x.com/assemblyai

CHAPTERS
0:00 Intro
0:33 Meet Matt
1:13 What AssemblyAI does
2:08 1,000 API signups a day
2:38 What a forward deployed engineer does
3:28 Why the FDE model doesn't scale
3:57 Automate yourself out of a job
4:12 The off-the-shelf bot: 10% resolution
5:17 Building Joey
6:12 Architecture: docs, embeddings, agentic search
7:22 Deploying on Railway
8:02 Results: 10% → 80% for $700 a month
9:01 Escalations become the roadmap
9:31 Giving Joey a voice
10:56 Code walkthrough
12:11 Live demo: talking to Joey
14:24 Dogfood your own product
15:08 Go build

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,712 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=pyvRID_CZZU&t=0s)** Cool. [music] All righty. Can everyone hear me? Okay. All All levels coming through good. All right. Sweet. Well, uh, how's everyone doing? How's everyone doing? Better. Okay, there we go. Cool. Well, I hope uh the conference has been good for everybody. Appreciate you all being here to to listen to a chat from uh from me. Um for anyone who hasn't met me at the at the booth yet, uh my name is Matt Lawler. I'm a forward deployed engineer at Assembly AI. Uh mostly focused on bringing in inbound customers, um helping win their business, u making sure that they have a good time building

**[0:46](https://www.youtube.com/watch?v=pyvRID_CZZU&t=46s)** with our API. Um so, how how many other like forward deployed engineers are out in the audience right now? Any of us? Okay, a couple. Cool. Well, um, still coming through. Okay. All right. Um, yeah. So, I wanted to make sure I I gave you guys an overview of kind of some of the go to market engineering stuff that we've been doing at Assembly AI that maybe you can apply to your own FTE team or maybe you can apply to your company um, as something that you can do as an easy win for your customers. Um, so for a little bit of overview of like assembly AI in case you haven't heard of us, um, we provide voice AI infrastructure. Um, so we train our own foundation models for speech to text primarily. Um, but we're starting to branch into other parts of the voice agent space. Um, so if anyone's ever had like a Fireflies note-taker join your meeting or something like that, you've also you've already seen a transcript from Assembly AI. Um, so we train our

**[1:35](https://www.youtube.com/watch?v=pyvRID_CZZU&t=95s)** own foundational models not only for like async use cases like meeting recordings and things like that, but also for real time uh real-time like voice agents. Um, so if you've ever used like a a phone customer support agent when you called in somewhere and it wasn't a human or like drive-through ordering, they're more than likely building with Assembly AI's models. Um, and for anyone who's building a voice agent now, you can use us for the entire stack, not just speech to text. Um, so you can use our voice agent API and we'll string together the speech to text, the LLM, and the text to speech as well. Um, as our competitors know, as we know, as anyone in the voice AI space knows, demand is absolutely insane um, for voice AI right now. Um, so assembly at our current moment, we see around a thousand API signups every single day. Um, which is somewhat of the theme of why we were focusing on automation and wanting to build kind of a new support

**[2:22](https://www.youtube.com/watch?v=pyvRID_CZZU&t=142s)** bot for our team because at least until like two days ago, I was the only uh onboarding engineer at Assembly AI. And so you can imagine, as much as I'd want to talk to a thousand new signups every single day, that's just not feasible. Um, so we had to build something to to solve that problem. And then for anyone here who doesn't know like what a forward deployed engineer is, it's a very catch-all title. It varies a lot at every different company, but effectively we want to get deployed with our end customers. We want to understand their use case. We want to make sure that we are building exactly what they need. Um, so we frequently commit code directly to their repositories. We usually meet with them several times a month, if not a week. Um, and we really try to understand their use case and get to know them very personally. Um so like at least on the inbound side for anyone who comes into assembly who wants to build with us we are the people um that are their main point of contact for anything

**[3:10](https://www.youtube.com/watch?v=pyvRID_CZZU&t=190s)** they need on the technical commercial side anything that they might need they get from us their FTE um and we're responsible for winning their business um and building that trust with them. So it's a great services model. It's great uh if we can actually get that kind of relationship with every customer, but again with like a thousand API signups every day, I I can't be one to many serving that many customers and getting on that many calls. Um and so ultimately this doesn't really scale super well. Uh we want to make sure that we're freeing ourselves up to be leading uh humanled deals as much as possible, but we can't do that with every deal. Not every customer win can be like handbuilt by us. Um and we can't just continue to hire more and more FTEEs if we're going to try and serve more and more customers. Um, so ultimately like for anyone who's an FTE in here, if you're looking to become an FTE, if you already have an FTE team at your company, I would encourage you to take

**[3:58](https://www.youtube.com/watch?v=pyvRID_CZZU&t=238s)** that knowledge that you have as an FTE and try to automate yourself out of a job. I think that should be your role every single day. If you want to serve your customers better, if you want to work with them more, um, and if you want to deliver a better customer experience at scale, you can't be the bottleneck to having a good customer experience. And we learned that firsthand. So again, we were drowning in like inbound um, volume. Um, you can see like we basically had a thousand API signups up there earlier. Um, and we had the natural instinct that a lot of teams do where we were like, we just need to deflect more conversations. I just want to talk to fewer people. I want to make sure I'm freeing myself up to work on more important stuff. Um, so we basically bought this off-the-shelf support bot and we're like, let's point it at the docs. It'll answer all the docs questions for us. It's going to be great. We'll never have to answer a simple question from customers again. And it only resolved about 10% of the conversations. Um, so it helped. Um, you can imagine if we had like a thousand

**[4:47](https://www.youtube.com/watch?v=pyvRID_CZZU&t=287s)** conversations a day, a hundred of those were now entered by a bot. But then our team still had to field 900 tickets a day. So it wasn't exactly very scalable. Um, so 10 10% uh end to end resolution rate wasn't good enough. And ultimately we couldn't iterate fast enough to be able to fix this. We didn't have access to the system prompt. We didn't have access to the tools. We didn't have access to the rag infrastructure. So anytime we needed to change something, we'd go to this vendor and they'd say, "Well, it's on the road map." and that didn't quite work for us. So, we wanted to build our own. So, we built uh another member of our team rather than hiring one and we named him Joey. Um so, anyone now who reaches out to us, whether it's on our chat widget on our site, whether you reach out to contact sales, whether you reach out to our support alias, you're going to meet Joey instead of a human. Um he's the first line of defense now for every

**[5:35](https://www.youtube.com/watch?v=pyvRID_CZZU&t=335s)** single conversation that happens in bounded assembly. And he's built to be the most infinitely scalable FTE on our team. Um, so he remembers past conversations with you. Um, we track all of his metrics via Pylon because he's still a member of our support team and so he has access to Pylon to manage conversations and remember who you are. Um, and he's built on top of the cloud agent SDK. And so the cool things that he's able to do is he can manage his own infrastructure. He has a file system. He can write and debug code for you. He can call tools. He can give himself new abilities. Um, and so he's actually able to operate more like an FTE and less like just a standard chatbot that you'd be talking with, you know, on on most major sites nowadays. So, um, if you want to know a little bit of like how to build your own Joey, um, the architecture kind of has like four major parts. Um, so as everyone might know from working with Claude, Markdown

**[6:24](https://www.youtube.com/watch?v=pyvRID_CZZU&t=384s)** is your friend. You should be giving Markdown files to Claude so that he understands everything about your business. And so we wanted him to have access to all of our documentation and be trained up on it all the time. So, we checked all of our docs out as local markdown and gave it to Joey. Um, and so anytime that we push an update to our documentation system, he's able to get all of those files and he has them locally in his file system. So, actually what's really cool is if our entire doc site was down right now, you could go to Joey and still get live answers on all the newest stuff that we've shipped without our team having to actually get involved. um for retrieval so we can give you a good answer. We partner with Voyage so we use their embeddings um so that he gets the most relevant documents up front so he doesn't have to spend a lot of time searching and he can get you a faster answer. And then since he has all these docs as local files if he gets confused or he needs to string together multiple resources to create a response

**[7:11](https://www.youtube.com/watch?v=pyvRID_CZZU&t=431s)** he can agentically search the file system that he lives on so that he can go and find those resources for you. Um so he can kind of go into this like deep thinking mode where he's able to search across all these resources and then we shipped it on railway. We didn't want to deal with infrastructure. We didn't want to spin up an EC2. We didn't want to have to change instance types. So, we deployed it all on Railway. Their service is pretty incredible. Basically, we can just go ahead and see if he has a bad conversation with someone in Slack. We can write a PR real quick and we can deploy it and within 30 seconds there's a new live version of Joey. So, we're able to iterate really, really quickly. Uh we've actually had times where we've actually monitored a live conversation, caught a bug, deployed a fix, and then it's been proof for the rest of the session, and that customer doesn't even have to know that we we shipped that fix behind the scenes. Um so Joey is able to to basically get updated whenever we want. Um so we actually have full control over everything that that he

**[7:59](https://www.youtube.com/watch?v=pyvRID_CZZU&t=479s)** does. Um and so the results were pretty remarkable from us building this. And it's another reason why and wanted to encourage everyone who's here to try and build your own Joey. So, we went from 10% to 80% endto-end resolution rate in just the first week of deploying this this build with a pretty naive implementation. And we did that all for around $700 a month in both token and inference uh or infrastructure costs. So, we resolved 80 80% of our our tickets end to end with no human in the loop. And some people like to game these metrics. They'll say like, oh, we resolved 80% but only on like a subset of types of tickets. Not the case here. you cannot reach a human directly unless you go through Joey and you tell him to escalate. So he actually does handle 100% of these inbound tickets for us now. Um and he only escalates 20% of them to a human for the right reasons. Maybe it's a rate change. Maybe it's a

**[8:47](https://www.youtube.com/watch?v=pyvRID_CZZU&t=527s)** data opt out. Maybe you need to sign an agreement with us or you have needs that only an FTE or someone from legal needs to be involved in. These are things that actually still need a human but eventually we can automate. Um and so the best part is whatever Joey can't do yet gives us a very clear list of what we need to do to continue to scale our team. Um, if he's not able to send them a BAA, well, okay, maybe we should give him a link that he can reference as a resource. Um, if he's not able to talk to customers about pricing, well, you can negotiate with Joey. Um, if you go on the site and you test him out afterwards, you can tell him exactly how many hours you have. Um, and he'll actually quote you a rate and then you can negotiate with him. Um, so we tried to automate a lot of these other things that he was still escalating and there's still there's still plenty more to come. But the real thing that, you know, we wanted to test out by building Joey was we wanted to dog food our own product,

**[9:34](https://www.youtube.com/watch?v=pyvRID_CZZU&t=574s)** too. We didn't want to just like build something that deflects more stuff from our customers. We didn't want to build something that just um is kind of this general support bot that anyone can build. We work in voice and our customers build voice agents. So, I wanted to build a voice agent and so I wanted to give a voice to Joey. So, now rather than just chatting with him via text, you can actually chat with him using your voice as well. Um, so we have a voice agent API as I mentioned earlier. Um, and we integrated this into Joey this week. So now if you go onto our site, you can switch to voice mode and you can talk to Joey using just your voice. Um, because I ultimately think for any FTE here, no matter how much you've been deployed with your customers, no matter how embedded you are with them, the best way to understand what your customers are building is to actually build their same product yourself. And that's exactly what we wanted to do with this. So we put our voice agent API into Joey. Um, it's all speech in, speech out, one

**[10:24](https://www.youtube.com/watch?v=pyvRID_CZZU&t=624s)** websocket connection where we string together our speechto text model, an LLM and text to speech, all optimized for voice. It's real-time and low latency. It handles all the pauses, interruption handling, barge, all of that kind of stuff for you. U, we bring our own voices, so you don't have to find another provider. And it's all the same tools that he already had if you were communicating with him via text. It's just now you can actually talk to him like you were a human. Um, and hopefully later this week we can hook them up to a phone number. So now we'll have an Assembly AI phone number so you can get real-time support from Joey whenever you need it. So let's go ahead and talk to Joey a little bit and we can walk through some of the architecture live. Um so for anyone who wants to know a little bit more about how this was actually built um we basically have all of the the docs checked out locally in Markdown. Um so every single time someone puts an update

**[11:10](https://www.youtube.com/watch?v=pyvRID_CZZU&t=670s)** out to our docs, these files also get locally checked out into this repo. So they stay perfectly in sync with any new features that we're shipping, our change log, our pricing, all of these major uh pages from our website get converted to markdown and get given to Joey. Um so he sees all of these in markdown format and he's able to see what the URL is so he can site his sources to the customer in case they want to double check his work or if they just want more information. Um at the same time, um all of it is provided as like Claude MD instructions. I think it's like a 30,000 line Claude MD of all these guard rails and and advice on how he should be operating with customers. Um, and this is what we majorly update whenever we see that he had a bad experience with a customer or gave a wrong answer, we ship an update to this cloud MD and now for every conversation that he has going forward, he's able to be better. Um, and it's all contained as a Docker file. Um, and so it's really easy to go and just

**[11:58](https://www.youtube.com/watch?v=pyvRID_CZZU&t=718s)** containerize and deploy him on Railway. Um, and so again, every time we ship an update to this repo, a new version's already live on Railway and no one had to manually monitor the deployment. Um, so let's go ahead and uh I'll fire up Joey here. we can ask him a pretty typical question so you can see what our voice agent API is like. So I'm going to simulate this locally because I I know probably many of you are going to test Joey after this and I don't want to add to the queue for our actual support team. Um so I'll I'll go ahead and just do a local simulation of it. But typically, yeah, you would go into here, you'd meet Joey, you'd want to have a typical question. You might talk to him via text, but let's go ahead and talk to him with voice. Hi, this is Joey at Assembly AI. How can I help you today? >> Hey Joey, I'm looking to build an ambient medical scribe with Assembly AI, but before I can test, I need to assign

**[12:46](https://www.youtube.com/watch?v=pyvRID_CZZU&t=766s)** a BAA. Is that something that you can do? >> One sec. Let me check that for you. Yes, you can execute the BAA yourself right away. Just complete our standard HIPPA business associate agreement, but note that you'll need a paid account with a card on file first. And signing the BAA automatically opts you out of model training. The relevant docs are linked in the chat. >> Cool. Thanks, Joey. Well, I got to I got to get back to my demo. I'd love to chat more, but uh thanks for all the help. You are very welcome. Good luck with

**[13:34](https://www.youtube.com/watch?v=pyvRID_CZZU&t=814s)** your demo and feel free to reach out if you need anything else later. Have a great day. >> Isn't he so nice? [laughter] I enjoy talking to Joey. I think our customers will enjoy talking to Joey. But this is a great example of like two years ago when I first joined assembly on our support team. This is a conversation that would have to be handled by a human. This is something that if you roached out in in chat and a customer uh or a support engineer wasn't able to uh answer you immediately. They'd have to wait. They'd have to get a response from us. It was a canned response. Um it was just not a great customer experience. And now you have an FTE that you can talk to 24/7 for these basic questions. Um and you can do it through voice. So you can actually test our product at the same time. Um so there's there's kind of a meta layer there of where if you're talking to Joy about how to build a voice agent API, you're already using it. Um, and you're already seeing exactly what your product experience could look like.

**[14:25](https://www.youtube.com/watch?v=pyvRID_CZZU&t=865s)** So, if there's anything that you should get out of this talk, it's not just that you should build your own Joey. Um, but I think that it's like if you're if you're an FTE at your company, you need to be dog fooding your own product all the time. It's not enough to just be teaching your customers how to get started with it. any new feature that you launch, any new product that you offer, you need to be teaching your customers, um, with all the knowledge that you've built from actually using and building and trying to ship the same product. Um, so I had to run through all the same walls. I had to figure out how to deal with latency. I had to figure out how to deal with turn taking or bargain or interruption handling. Um, and I think I have a lot better empathy of how to like work with customers that you want to use our voice agent API. Um, because now I've actually used it. I've used the same API. It's the exact one that my customers build on and I can give them better advice because I've actually shipped something with it. So go build go build something. Go build whether it's a your own Joey, go build

**[15:15](https://www.youtube.com/watch?v=pyvRID_CZZU&t=915s)** whether it's a voice agent, especially if it's a voice agent, build it on Assembly AI. Um, but if you're if you're actually working in an FTE capacity, try to build the exact product that your customers are building and do it on your own. Don't just wait for them to ask you for help. Don't just wait to remove all their blockers. You should be going out and building the exact same thing. And at the same time, you might actually be able to make your customer experience better simultaneously. So, um, if anyone has like questions on how to build Joey, if you want to check them out at the booth afterwards, our booth is just right over here. Um, if anyone has feedback on Joey since this just shipped this week, if you have a weird conversation with him, I'd love to know about it so we can keep making fixes and I can show you how we deploy that live. U, but overall, really excited to uh, be here at the conference and talk to more people about voice agents. So, thanks for uh, coming and listen to this talk. >> [applause]

**[16:16](https://www.youtube.com/watch?v=pyvRID_CZZU&t=976s)** [music]
