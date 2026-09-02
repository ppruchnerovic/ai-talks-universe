---
id: SslOMR_YnVw
title: "Krishnaram Kenthapadi - Trustworthy Multi Agent AI Systems for Healthcare: Challenges & Lessons"
slug: krishnaram-kenthapadi-trustworthy-multi-agent-ai-systems
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Krishnaram Kenthapadi"]
channel: "Berkeley RDI"
duration_min: 13
published_at: 2026-08-12T07:13:44Z
video_id: SslOMR_YnVw
url: https://www.youtube.com/watch?v=SslOMR_YnVw
youtube_url: https://www.youtube.com/watch?v=SslOMR_YnVw
tags: []
topics: ["Agents & orchestration", "Governance, ethics & regulation", "Science, healthcare & applied ML"]
transcript: true
---

# Krishnaram Kenthapadi - Trustworthy Multi Agent AI Systems for Healthcare: Challenges & Lessons

**Krishnaram Kenthapadi**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=SslOMR_YnVw) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*2,001 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=SslOMR_YnVw&t=2s)** Uh hi everyone. Uh while we're waiting for the slides to load up, uh just a raise of hands. How many of you are from academia? Okay. Uh and how many from industry? Anybody from government or NOS's? All right. I see uh at least I could kind of see maybe a a larger proportion from industry and a sizable number of folks from academia. Um so while while we're waiting uh for these slides to load uh let let me just um give some feel for what we are doing um as uh I was introduced I'm the chief scientist for the healthcare AI efforts at Oracle. So we have been looking at some of the uh challenges in healthcare. The

**[0:53](https://www.youtube.com/watch?v=SslOMR_YnVw&t=53s)** challenges that clinicians face every day on a day-to-day basis. So these uh these range from spending a lot of time on say the electronic health record systems or spending a lot of time going through the patient records and so forth and not being able to spend as much time facetoface interacting with the patients. Uh so that's a that's a kind of broad problem we are we are kind of looking at solving. Um so while we we we are still waiting on the slides um so let me just give give some context on where I'm coming from. So I I have been at Oracle for almost two years uh helping grow these efforts and launch uh our flagship product clinical agent and uh its varants. So before this I I have been over the last two decades or so

**[1:43](https://www.youtube.com/watch?v=SslOMR_YnVw&t=103s)** working on uh problems related to trustworthiness starting with data privacy, bias, fairness, explanability uh a observability and so forth. All right. So here we we have um okay so let me start with some of the where the state of healthcare today. Uh today we have a number of different challenges. So we have the challenge of shortage of physicians or more broadly clinicians. We have the problem of burnout and administrative overhead experienced by clinicians. There are surveys showing even before COVID pandemic that about 80%age of clinicians were experiencing burnout causing them to quit the profession or

**[2:32](https://www.youtube.com/watch?v=SslOMR_YnVw&t=152s)** planning to quit uh the healthcare industry as as a whole. Then we also have on the other other hand uh the amount of time that a patient gets to spend with the physician is reducing because the physicians are asked to see more and more patients and even in this small amount of say 15 minutes typically the the provider or the physician will be spending a good chunk of time looking at the computer and maybe not as much looking at the patient. And all of these factors along with maybe several other systemic factors result in a number of errors in uh health care for example resulting in as much as 400,000 preventable deaths in the US alone. And of course these are not limited to US.

**[3:20](https://www.youtube.com/watch?v=SslOMR_YnVw&t=200s)** These are problems in many countries across the world. At the same time we are seeing that the health care costs have been going up. For example, in the US, it is estimated that around $1 trillion is is uh associated with the administrative overhead or administrative burden in healthcare. So the natural question is this is not sustainable. What can we do about this? How can we bring down the cost and also improve the quality of uh the the the care that the patients receive today? uh this is where I think that AI has a huge role and in fact this is not just thinking it's AI is already being used across healthcare and being adopted rapidly the challenge

**[4:10](https://www.youtube.com/watch?v=SslOMR_YnVw&t=250s)** that we are looking at is how can AI help reduce ad administrative overhead clinician burnout and so forth so that hopefully it results in better patient outcomes and and since this is the domain of healthcare. How do we do this in a trustworthy manner? How do we ensure patient safety? How do we ensure that all the regulations are followed and so forth? So with this context, um let me let me kind of um go into more into what we are doing. As I mentioned earlier, our goal is to reduce the time doctors spend entering data or searching patient records or typing nodes and so on and instead spend more time interacting with

**[4:58](https://www.youtube.com/watch?v=SslOMR_YnVw&t=298s)** the patient which is the thing that they or they the reason they came to the profession in the first place. Um towards this we have built and uh deployed uh a product called clinical AI agent where we first focused on the task of automatically capturing the medical nodes by listening to the doctor patient conversation of course with the consent of the patient and the doctor and then building on top of this automatically capturing uh various orders placed by the doctor like X-rays, labs, medications and so forth and going beyond that helping the doctor when before they go and see a patient in terms of

**[5:46](https://www.youtube.com/watch?v=SslOMR_YnVw&t=346s)** what what is the summary or what is the gist of why the patient is there and what what are the relevant parts from the patient record for that u to to go into more uh specifics like we have been building this to be voice first and multimodel um something that works across devices ranging from mobile or web interface, desktop and so forth and also in a way where it takes the provider context into account. It knows the preferences of the physicians as well as the patient context, the re the reason the patient is here, the history of the patient and so on and do this in a way which is as proactive as possible. uh for example if a new lab report has arrived we want to

**[6:35](https://www.youtube.com/watch?v=SslOMR_YnVw&t=395s)** suggest what might be the next best course of action in terms of the care pathway for the patient for example uh there are a number of uh technical nuances behind this today let me just give uh one example of this just as a flavor of this so by the way uh here is a a link to a live demo of the system. Uh so one of the key components of our system is what we called the multi- aent orchestrator. Suppose that the doctor is looking at uh Samantha's uh record and wants to know how how her her vitals trending. The doctor might ask show me the recent labs.

**[7:22](https://www.youtube.com/watch?v=SslOMR_YnVw&t=442s)** So given this query we need to figure out whether we need to uh search in structured records containing the labs. Do we need to search over unstructured data like the medical nodes? We need to take into account the UI context uh the context of the the patient and so forth and do the do this in a way which supports multi-turn conversations. And to do this um even though this query might be simple you can imagine a number of other uh settings like are there side effects of the medications that Samantha is taking now or what might be the best course of action for Samantha given her past records and the new uh lab lab results that have

**[8:11](https://www.youtube.com/watch?v=SslOMR_YnVw&t=491s)** arrived. Um to do this the orchestrator has a library of tools and skills. It needs to decide which is the right one to invoke. Um then it it invokes those tools and it also has uh different types of guardrails. guardrails on at the input side especially if this is not doctor phasing but say patient phasing making sure that uh any queries which are sensitive or which require appropriate uh escalation due to medical emergencies are handled appropriately. Likewise god rails once we get the response from the agent on the output side then of course we also want the latency and costs to be contained. So we do a number of optimizations such as uh caching or parallel computations or

**[9:02](https://www.youtube.com/watch?v=SslOMR_YnVw&t=542s)** deciding when the query needs to be routed to a reasoning model a complex reasoning model and when it simpler uh language model or even a deterministic Python code would suffice to get the response. So making those decisions at runtime so that we save both the latency and the cost. Of course, there are a number of other optimizations that I won't be going into today. Um as we move towards not just a multi-agent architecture for a specific application but a multi- aent health care system as a whole uh there are of course a number of different stakeholders involved ranging from patients, doctors on the administrative side, the folks involved on the payer side and so on. And of course a number of systems including the

**[9:50](https://www.youtube.com/watch?v=SslOMR_YnVw&t=590s)** electronic health records and different tasks ranging from search uh document document summarization or uh understanding the u medical coding and so forth. How do we do this in a manner which is which where all these agents interact with each other. Um at the same time there are aspects like a number of things that can go wrong. uh if you're interested please take a look at uh the tutorial that we presented at the ACM conference on agentic systems and AI recently um just to give an example there are challenges around evaluation the evaluation that works offline may not translate to online either because the assumptions are no longer true or

**[10:38](https://www.youtube.com/watch?v=SslOMR_YnVw&t=638s)** the distribution of the patients may have changed. We also need to make sure that we take the business metrics and map them to appropriate applied science metrics which we can measure and iterate on. Then there are problems like omissions. Uh if you are presenting a summary of the patient to the doctor unlike say web search or other systems here recall is extremely important. If you miss something which is medically uh pertinent in the summary that can lead to patient safety. So, so while we are doing this, let me just illustrate this with another setting in the medical imaging scenario. So, here the task is how do we encode clinical workflows uh when it comes to something like chest X-ray

**[11:25](https://www.youtube.com/watch?v=SslOMR_YnVw&t=685s)** interpretation? How do we leverage tools that clinicians use today uh and so forth? Um and again like even in this work we have an orchestrated agent then we have a number of sub agents inspired by clinical workflows. There is something called ABCDE system in um medical imaging stands for airway breathing and so on. And we have the sub aents which are invoked um in parallel and then there is a synthesizer which combines potentially conflicting uh results from these sub agents and then decides what's the best course of action. Um again like as you all know healthcare is heavily regulated. Uh so this motivates uh some of the other work we do whether

**[12:13](https://www.youtube.com/watch?v=SslOMR_YnVw&t=733s)** it's in the data privacy space or bias and fairness space. uh in the interest of time let me skip this and let me conclude with the following uh takeaway. uh in a setting like healthcare it's very important to understand the domain uh not just focus on model development but also on the data validation on the evaluation methodology and so forth and it's important to iterate with the clinicians uh understanding their needs having some early version out and iterating based on that and of course we we use frontier models but those may not have all the healthcare specific nuances so building domain and task specific knowledge and encoding these in uh in the form of a semantic knowledge graph and uh semantic data layer is very important and as I alluded to uh trust safety are extremely

**[13:02](https://www.youtube.com/watch?v=SslOMR_YnVw&t=782s)** important and uh here is just an an example of a process we follow uh in the form of AI review for health uh and let me conclude with this and uh happy to talk to you offline if there are questions thank
