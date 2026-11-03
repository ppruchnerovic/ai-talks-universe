---
id: 3osCbSufv8g
title: "Voice AI Where One Wrong Question Breaks the Rules - Shiv Indap, Upstart & Brooke Hopkins, Coval"
slug: voice-ai-where-one-wrong-question-breaks-the-rules-shiv
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Shiv Indap"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-31T07:00:11Z
video_id: 3osCbSufv8g
url: https://www.youtube.com/watch?v=3osCbSufv8g
youtube_url: https://www.youtube.com/watch?v=3osCbSufv8g
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Shiv Indap", "Brooke Hopkins", "Upstart", "Coval", "voice AI", "voice agents", "AI evals", "LLM as judge", "human review", "fintech", "lending", "compliance", "AI Engineer", "AIE NYC"]
topics: ["Evals, observability & reliability", "Governance, ethics & regulation", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Voice AI Where One Wrong Question Breaks the Rules - Shiv Indap, Upstart & Brooke Hopkins, Coval

**Shiv Indap**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Shiv Indap` `#Brooke Hopkins` `#Upstart` `#Coval` `#voice AI` `#voice agents` `#AI evals` `#LLM as judge` `#human review` `#fintech` `#lending` `#compliance` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=3osCbSufv8g) · [Conference site](https://www.ai.engineer/)

## Description

Upstart handles thousands of lending calls a day, where one wrong question can become a regulatory problem. Shiv Indap, who leads voice AI at Upstart, and Brooke Hopkins, founder of Coval and former head of evaluation infrastructure at Waymo, walk through automating loan verification calls: the compliance traps, outgrowing a Google Sheet for human review, and raising agreement between the LLM judge and human reviewers from 33% to 92%. Then they lay out the full loop from live monitoring and human review queues to re-simulating fixes and self-healing agents, with every change still signed off by a human.

Chapters:
0:00 Intro
1:02 Voice AI at Upstart
2:11 Automating verification calls
3:04 Where compliance gets tricky
4:14 Outgrowing the Google Sheet
5:28 Metrics and LLM judges
7:03 From 33% to 92% judge agreement
8:52 The continuous improvement loop
10:04 Defining metrics
10:51 Monitoring live calls
12:31 Re-simulating fixes before production
14:04 Self-healing agents
15:11 Wrap-up: humans stay in the loop

Shiv Indap

Brooke Hopkins

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,903 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=3osCbSufv8g&t=1s)** [music] >> Um so I'm Brooke. I'm the founder of Koval and we build evaluations for voice agents. My background's from Waymo, so I led our evaluation infrastructure team at Waymo and my team was responsible for all of our developer tools for launching and running simulations. You might be like, what does that have to do with with voice agents? Well, autonomous vehicles are actually very similar to autonomous voice agents. How do you make sure that something reliably gets from point A to point B, all the possible paths in between, and also how do you architect lots of models working together in order to build an autonomous system that reacts and responds to the

**[0:48](https://www.youtube.com/watch?v=3osCbSufv8g&t=48s)** world reliably? Um so we work with enterprises, everyone from really fast-growing AI companies like Perplexity to Fortune 500s across the board, um to make sure that their voice agents are working well for customer support, logistics, etc. >> Cool, and I'm Shiv. Uh I lead our voice AI at Upstart. Uh for those not familiar with Upstart, we are a fintech company and we primarily do lending. Okay, cool. So, let me talk about voice a little bit. So, Upstart in general does uh thousands of calls, well, every day. Um I think um we talked about domain, which is lending. So, what is unique about lending is obviously it's a highly regulated space, um you know. And when when we have voice agents doing

**[1:38](https://www.youtube.com/watch?v=3osCbSufv8g&t=98s)** these calls with with applicants or borrowers um if things go wrong, it's not just a uh you know, customer experience issue. It is It could be a potential regulatory issue, which is worse. Right? So, um whenever we we launch these agents, we want to make sure that uh you know, we are we are first and foremost compliant with all the rules and regulations. So for this one, I'm going to talk about a use case that you know, we we launched. The process the the agent that we launched was automating verification calls. So what happens is about 90% of people who apply to Upstart are instantly decisioned. The 10% that are not, they have to call in and they

**[2:26](https://www.youtube.com/watch?v=3osCbSufv8g&t=146s)** have to verify some information. So use case is fairly simple. We ask three questions. Will your income sources continue for the next three months? How do you plan to use the funds? And do you have any outstanding obligations such as you know, alimony, wage garnishments etc. Okay, so those three questions aside, you know, we we first need to verify that the person calling in is actually the person. So they don't ask like, "Hey, can you tell me about some random application that they don't own?" Um then sort of you may think that this is a very simple use case, but this is where sort of regulatory things come into the picture. So I'll give a couple of examples. If someone says that I plan to use the funds for medical purposes, we can't ask the amount. We just prevented from doing

**[3:14](https://www.youtube.com/watch?v=3osCbSufv8g&t=194s)** that. If we do ask it, it creates a big issue for us. Um on the other hand, if someone says, "I plan to use the funds to travel to graduation." Right? Well, whose graduation is it? Your graduation? Your kids' graduation? Someone else's? That really determines the use of funds, right? So depending on on sort of what the applicant or the human at the other end says, we have to do specific things. We can ask or cannot ask things. And lastly, I think the it was very important for my compliance team that when we handle this use case, we just handle this use case, right? A lot of applicants are very eager to know what their status is or when they'll get the money because we can't just say like it'll be up to three business days. We just sort of sidestep the question in

**[4:02](https://www.youtube.com/watch?v=3osCbSufv8g&t=242s)** a nice and polite way. Um so that's that's sort of the use case that we launched. Cool. So um So that's the call. Now obviously when we launched this we want to make sure that the agent was doing well what it set out to do. Uh you know, so when we start audit auditing was very important. So every call had to be reviewed by a human. Um now obviously when this started out well how do you review all these calls? So we started with the humble Google sheet. You know, we start maintaining it. Our operations team that were reviewing these calls started putting in data there. In a few weeks five columns went to 10 then like 15 people started adding

**[4:52](https://www.youtube.com/watch?v=3osCbSufv8g&t=292s)** columns randomly putting stuff in columns creating things that you know, just just sort of messed up the whole process, right? So ultimately like what we need is data to improve both our agent as well as you know, the uh the things that we look in terms of performance right? So that's where we sort of uh needed to have a better and more structured process for human review, right? And that's where Kowal came in and helped us build this human review process. Um but before I go there let me just talk a little bit about metrics, right? So when I talk about metrics here think about LM as a judge running once a call is complete. Right? So one important like criteria is

**[5:42](https://www.youtube.com/watch?v=3osCbSufv8g&t=342s)** were the compliance requirements met? So I it's a simple like yes no question with an explanation, right? So, uh one of the things we did is post post run, we run this judge and it produces an output with an explanation. Now, we want to make sure that the judge is working. So, we we put it and and we get a human to review the output of the LLM judge. Yeah, so when we started off, you know, we had metrics and we were tracking like a whole bunch of things like call time, you know, obviously accuracy, clarity, etc. I think over time we sort of whittled down the list to the metrics that were sort of the most important, right? And you can see some of the ones here like accuracy clarity completeness policy alignment, whether it was escalated

**[6:32](https://www.youtube.com/watch?v=3osCbSufv8g&t=392s)** correctly, and ultimately CSAT score. One important thing I'd say is don't be too attached to your metrics. Start off with the ones that seem logical. If things change over time, you know, discard those metrics and track the other ones that really like impact your use case. Um Cool. So, we talked about LLM as judge and metrics a little bit. So, again, all these are run automatically once a call is complete. Now, I'll talk about one specific one here which was, you know, adherence to compliance, right? Or compliance violation. So, basically we we score the call. It goes into a queue. A human reviews the output of the of the metric.

**[7:21](https://www.youtube.com/watch?v=3osCbSufv8g&t=441s)** And then puts in their feedback, right? Why this is important is because we want to make sure that whatever the judge is outputting aligns with humans or experts in that particular area, right? And as you can see here like when we launched a while back, the compliance sort of agreement metric was 33%. That means a human reviewer and a LLM agent or a LLM judge agreed only 33% of the time. Now, well, we don't we we can't get to 100% but we can get like very close, right? So, we really start looking into like what is the gap there and that's where this process of providing feedback by experts sort of really helped, right? And ultimately it came down to a couple of things, right? There was a lot of tribal knowledge when we launched the agent that was not coded

**[8:08](https://www.youtube.com/watch?v=3osCbSufv8g&t=488s)** as part of the agent. So, we changed that and over time the the metric seems number went up. Then we realized that amongst humans in who are reviewing this call there was disagreement as well, right? Because there was a lot of stuff that was not written or or like tribal knowledge. So, we tried to like encode that. And then like sort of the next big bump came as we started to like look at more use cases. We started to see that well, the judge itself needed to be improved, right? So, ultimately we went up from like a 33% agreement rate to now today it's at 92%. >> [clears throat] >> Um we'll talk a little bit about how this process works in detail. So, I'll hand it over to Brooke. >> Amazing. So, from there what we really implemented was this continuous this

**[8:58](https://www.youtube.com/watch?v=3osCbSufv8g&t=538s)** complete loop of how you continuously improve the agents. So, I think this is something that Upstart has done really well is actually setting up a process that doesn't allow you to just launch once but allows you Um amazing. I'm super happy this is useful. Um so, everyone taking pictures. Um but it really allows you to like continuously improve your agent. I think this is something that enterprises get wrong is that they set up how whether the release gate so that we can launch one time but then it makes it very hard to change a model or change a prompt or anything underneath. And so, we go from like um I'll step through all of these processes of how you go from monitoring conversations, defining what your metrics look like, flagging calls, and then using that to constantly improve your agent. Um and so we also use this human review that Shiv just talked about and really

**[9:47](https://www.youtube.com/watch?v=3osCbSufv8g&t=587s)** believe that human review is a super important part of the evaluation process and where you should be spending most of your time is thinking about the product like evals are really the product definition. So where should you be spending your time um is what should my product be doing? Um so the first step is defining your metrics. So there are different types of evaluations. Like I think about it in three categories of did it get to the end? Did it adhere to the steps in order to get there? And then what was the conversation quality or the experience? Um and so in Cobal, and I'll be showing you how this actually works in Cobal. So you can build out these LLM judge or metrics that align with this original criteria that human reviewers were going through and labeling. That's also a really important step though is to have these human reviewers labeling what do they care about and then you can take

**[10:36](https://www.youtube.com/watch?v=3osCbSufv8g&t=636s)** that and turn it into automated evals versus the reverse is starting with like we care about word error rate but that's not actually what we're actioning on. Um and then the types of metrics are you know LLM as a judge, heuristics, audio processing. Um and so what we do is we monitor then take these metrics to monitor live calls. And so we can detect known failure patterns at scale. So being able to show exactly where for example we didn't verify um the correct pieces for the loan um or maybe where it didn't have the wording correct. Um and this is really important because no system works uh 100% of the time at scale. Uh even Google you know six nines of reliability there will will be failures. Um and then we also detect unknown unknowns. So things that we didn't know were going to

**[11:23](https://www.youtube.com/watch?v=3osCbSufv8g&t=683s)** happen doing by doing like clustering analysis and anomaly detection. Um and then we can route each one of these failures for human review. So you can configure review queues where they're actioning on any one of these metrics that we defined and then having these amazing human reviewers look through those failures. So now instead of looking at every call, they're only looking at the calls that matter most. And so from there we route all of these different failures to the right teams. This is a really critical step because you want to set up an operational practice so that every failure that's coming in you're doing something with that. So either you're routing it to you're routing for human review to detect real failures. So let's say like

**[12:10](https://www.youtube.com/watch?v=3osCbSufv8g&t=730s)** you know off script or wrong answer is 34% of the time. These are just made up numbers. Um then like maybe we send those to the agent team versus compliance violations we send that to a compliance team so that they can file a process or you know take some like tactical action on it versus sending to an engineering team etc. Um and so now once we have a set of real failures, we can then re-simulate or we then for example Steven who's here can figure out what is the right fix to the agent. Um and then we can re-simulate that that fix to see what exactly the result is. Like did it actually fix this issue? Um and so our simulations do voice to voice evaluation. We will call your agent and actually run a simulation to

**[13:00](https://www.youtube.com/watch?v=3osCbSufv8g&t=780s)** um you know test different background noises, different accents, um the actual voice quality, interruptions etc. And then we can verify that that improvement actually fixed things before it's impacting your users. So once you know that there's an issue like a compliance violation or maybe like a poor user experience, you don't want to launch that again to production to see if it fixed it because you're now risking impact to your users. So we want to shift left to use a devops term. Um we want to detect as many failures as we can in simulation instead of doing that in production. So, here you can see that, you know, we improved um those cases in the report. And so, this finally completes the loop of um we monitor we define what our metrics are based on our product definition. This is

**[13:47](https://www.youtube.com/watch?v=3osCbSufv8g&t=827s)** honestly where you should spend the most of your time is what does my agent do and what should it not do. Um and then we can monitor and score every live call, um detect those failures, send them for human review, find failure patterns across all of these to prioritize engineering work. And one of the most exciting things is now you can enable the self-healing loop where we can actually have agents that look at all of these evaluations and identify fixes, but we can also use RL pipelines or fine-tuned LLMs in order to make our system even better over time automatically. Um and then actually I have to go back. Okay. Um and then from there we can automate fixes and then prove that this actually is improving things in production through

**[14:35](https://www.youtube.com/watch?v=3osCbSufv8g&t=875s)** simulation. And all of these things obviously are gated by human review and integrating human review in the loop. Um and so, these defined setups can uh both make sure our metrics are really accurate. So, as I should have talked through, every time you label a feedback every time you label a metric as it was being as it was incorrect, now you can align your metrics to human judgment or it it actually is a true failure, in which case you can use that to automatically improve your agents. Um >> Cool. Um so, yeah, in conclusion, right? Evals are important. Don't don't skip them. Uh evals uh sort of help us uh sort of monitor and score the calls, but also determine which calls need attention or which

**[15:23](https://www.youtube.com/watch?v=3osCbSufv8g&t=923s)** calls need to be like reviewed by a human because humans can't review like thousands of calls a day. Um, the human reviewer annotations are important because they help improve the LM judge. Um, all this data that we collect ultimately helps improve the agent as well. Um, changes are always gated behind a feature flag, right? So, we when we say self-healing or self-improving, it doesn't mean like humans are completely out of the loop. Uh, with uh, fintech, uh, we we need these, uh, changes to be sort of monitored and and signed on by like someone, right? So, judges usually the engineers do. Uh, but if uh, there was a compliance change, then compliance is involved in approving like, uh, the behavior of the agent. Um, and lastly, like this has served like as a blueprint

**[16:10](https://www.youtube.com/watch?v=3osCbSufv8g&t=970s)** for us to launch agents safely meeting regulatory requirements and also improving their performance at the same time. >> And I think that's why like actually being able to set up really robust evals defines a really high-quality product. Um, in all cases, but I think especially in regulated industries, you just can't, um, deploy the applications that you want to without having really robust evals that give you confidence that you're doing it like deploying these autonomous systems with precision and robust reliable um, you know, great products that can actually scale. >> Cool. Uh, we are almost at time. So, yeah, feel free to like, uh, you know, connect with us on LinkedIn or you know, just reach out if you, uh, see us, uh, anywhere, uh, today. So, but that's, uh, that's our presentation.
