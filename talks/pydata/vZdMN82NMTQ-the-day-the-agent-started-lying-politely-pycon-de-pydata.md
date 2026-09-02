---
id: vZdMN82NMTQ
title: "The Day the Agent Started Lying (Politely) [PyCon DE & PyData 2026]"
slug: the-day-the-agent-started-lying-politely-pycon-de-pydata
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Asya Melnik"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-04T22:21:25Z
video_id: vZdMN82NMTQ
url: https://www.youtube.com/watch?v=vZdMN82NMTQ
youtube_url: https://www.youtube.com/watch?v=vZdMN82NMTQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Agents & orchestration", "Classic ML & data science", "Evals, observability & reliability"]
transcript: true
---

# The Day the Agent Started Lying (Politely) [PyCon DE & PyData 2026]

**Asya Melnik**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=vZdMN82NMTQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Asya Melnik reveal how to detect silent failures and manage data drift to ensure your LLM-based agents remain trustworthy and accurate in production.

Speakers:
Asya Melnik

Description:
LLM agents often suffer from silent degradation, where the model continues to provide confident responses despite a shift in the underlying data distribution. This problem is particularly acute in non-deterministic systems where ground truth labels are unavailable for real-time validation, rendering traditional accuracy metrics useless. In a customer support ticket routing scenario, for example, the launch of a new product can introduce new vocabulary and shift the meaning of existing terms, leading the agent to misclassify ticket priority while reporting zero system errors.

To detect this drift without relying on manual labeling, a multi-signal evaluation framework is used. This approach monitors six distinct metrics: Shannon entropy (calculated using all available class probabilities to measure internal uncertainty), fallback rates (acting as a canary signal), vocabulary drift (measuring the distance of current word vectors from a stable centroid), human disagreement (tracking when users override agent decisions), LLM-as-a-judge (using a model like Claude Haiku to verify if the agent's reasoning is faithful to the input), and trajectory (assessing the logical flow from input to outcome).

The key takeaway is the implementation of a tiered action plan based on the number of triggering signals. A single alert, such as an increased fallback rate, suggests observation. Two or more signals indicate a need for investigation. When multiple signals across different layers—internal confidence, external human feedback, and logical verification—trigger simultaneously, it provides a high-confidence indicator that the agent's prompt or model requires updating. This "nervous system" approach allows operators to identify and fix silent failures before they impact business operations.

⭐️ About PyCon DE:
PyCon DE is the leading conference on open-source Python applications in AI and data science. It brings together industry professionals, researchers, AI and data science practitioners, and software engineering communities, providing a unique platform for collaboration, knowledge sharing, and innovation.

The PyCon DE & PyData 2026 conference delivered an exceptional experience, fostering stronger connections within the Python community while showcasing the latest advancements in artificial intelligence and data science. Attendees enjoyed a diverse and engaging program of talks, workshops, and networking opportunities, further establishing the conference as a premier event for Python, AI, and data science enthusiasts across Germany.

PyCon DE 2027 will take place in Heidelberg from 19 to 23 April 2027.

•  Newsletter: https://2027.pycon.de/newsletter/
•  LinkedIn: https://www.linkedin.com/company/pyconde
•  X: https://www.x.com/pyconde

Links:
• Conference website: http://pycon.de
• Other sessions: https://2026.pycon.de/talks/

The conference was organized by
• Python Softwareverband e.V.: http://pysv.org
• Pioneers Hub gemeinnützige GmbH: http://pioneershub.org
in collaboration with NumFOCUS Inc.: http://numfocus.org

If you enjoyed this session, please like, and subscribe to our channel for more insightful talks and discussions.
Share this video with your network to spread the knowledge!

Hashtags:

Acknowledgements:
Special thanks to all the volunteers and sponsors who made this event possible.

About:
Python Softwareverband e.V.:
PySV is a non-profit that promotes the use and development of Python in Germany through events, education, and advocacy, fostering an open Python community.

Pioneers Hub gemeinnützige GmbH:
is a non-profit fostering innovation in AI and tech by connecting experts and promoting knowledge exchange through events and collaborative initiatives.

NumFOCUS Inc.
supports open-source scientific computing by providing financial and logistical support to key projects like NumPy and Jupyter, promoting sustainable development and collaboration.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

## Transcript

*4,590 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=6s)** Well, yeah. So, uh let me start with a quick question. So, how many of you um recently or not very recently uh just uh deployed an LLM agent? Could you just raise your hands, please? Uh-huh. Uh-huh. Uh-huh. Uh-huh. Okay. Okay. Okay. So, and now could you please raise your hand if you still completely sure what your agent is doing and it's doing completely what it's intended to do. No one ah one oh okay one two okay there's three okay I want to talk with you later [gasps] but this is significant difference [laughter]

**[0:53](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=53s)** so this is actually this gap between first group of people and second group of people is actually what I'm going to talk today so how to actually catch when your LLM agent is degrading and starting to lying to you but still it will sound very confident so if you want to stay in touch with me just this is my uh LinkedIn. So in short I work for uh Blue Yandere. I'm not going to uh tell the story how I end up there but uh in blue yonder currently what I'm doing I'm doing AI agent development. I work in an AI agent uh evaluation and I should written here also AI mentor and um uh educating uh teams but it would be too uh much AI agent words for one slide. So yeah. So let's uh just look uh before

**[1:43](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=103s)** starting with the solution we need to first understand what actually is wrong what's going on. So let's say you have some traditional uh solution uh agent whatever you call it um it could be ML it could be whatever it's just uh some sort of um uh algorithm model that just does something uh it runs a predict uh prediction so and uh you know uh the ground truth in the end so you actually can label it um and if you know a ground truth uh you can label it. So that means that you can actually calculate some metrics and if they look wrong or something is going bad you can just improve your model and just repeat the cycle. So this is just a cycle it's a loop works fine

**[2:32](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=152s)** great. Um unfortunately it works only for deterministic systems. So if we talk about LLM agents so what's happening? So you have your agent same like as before right it does something right? I'd give you response, but I mean what's what's what's right? I mean what's actually the ground truth? I mean there is no ground truth unless you actually really sit down and define it somehow. Um but it might be too strict or something or you just see the person that actually clicks right wrong right wrong wrong right right wrong wrong um which actually might be uh for our uh case uh happening like in two uh three times percent but if you do it like for 100% it's not automation anymore. So if we don't have actually grand truth so how can we

**[3:20](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=200s)** calculate matrix so this loop is broken and you have no idea that your agent is doing what it's supposed to do. Um yeah but um yeah this is one of the most important things lines that I want you to take from this talk. So if you you can't improve what you cannot measure and you cannot measure uh if something has no label. So if you don't know what to measure. So uh here is uh the concept of my talk. So we have an uh LLA agent that read uh customer support tickets uh assigning priority like it's uh um high priority, super high priority, medium or low and assign this wrote all tickets to some uh team uh that should solve them. So everything should happen

**[4:08](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=248s)** automatically on scale and human shouldn't actually be involved but could be. Um two things two disclaimers uh not disclaimers uh two things I want to say before we actually proceed uh later on. So uh first all tickets that you will see here actually synthetic so those are generated I couldn't bring real customer support tickets here obvious reasons so but failure patterns actually real so I just synthesized the uh data uh so that they will uh copy the pattern that I observed in reality so and the second one uh I will show mainly explain what's going on uh just uh show you some plots and explain what they mean and so on so so on so on. Uh but all the code and if

**[4:57](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=297s)** you want just to look at this uh demo toy uh setup will be available in the GitHub and the link will will be in the very very last uh page of this um please don't go there right now and otherwise I will lose you completely. So what's going on here? Um you have your agent it's deployed uh here you have um your timeline let's say in our setup right uh we deployed in January okay so uh you see this uh nice number like 100% accuracy which actually means that just only you managed to I mean your agent not you managed to actually to um give a priority to the ticket and send it somewhere yeah and uh zero errors in

**[5:45](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=345s)** your locks Yeah, because you actually not really know what's track. So everything looks actually really cool and this like numbers what you probably want to show to your manager. Um yeah but there is something happening in the June month six. So what's happening actually company launch new product um in this terms like for example purpose we will talk about authentification. So new authentification method so is launched. Okay. So actually some new words are coming. Some might be changes uh are coming and uh your AI agent doesn't actually not aware what's going on. So some strange thing uh uh signals come from outside but your agent u

**[6:35](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=395s)** doesn't know what to do with this. So it's continue doing what it's used to do like just giving priorities roing and actually showing the same numbers to you until the one moment uh when you just see that your engineers actually coming to you like ops engineers and say like okay something is wrong like um for the first uh last five months we got 113 uh wrong tickets to us like they were marked as urgent while were not. What's going on? So nothing crashed. Platency was stable. So everything was green for 5 months. No alerts. Yeah, you just missed it. Here is example of the ticket. So you can understand what's going on and how it's working. So um ticket this is still

**[7:26](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=446s)** unresolved login with Microsoft broke after our Azure AD tenant was renamed. Do we update something here? Our SLA requests resolution within four hours. Wow, that's really strong. So what your agent will think actually it says like okay okay okay I see login I see Microsoft this is what I was trained on this is what in my prompt uh I see like SLA maybe urgency okay fine fine fine so this is like actually emergency so wrote it to authentification team as emergency but truth actually this is not it truth that this is actually medium is this is not how uh this is related actually to the change that company um did. So this is a new authentification method that

**[8:16](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=496s)** launch and just configuration uh question which just requires uh 15 minutes picks. So here might be some numbers what you might see or would see. So confidence is actually below uh this uh threshold. So actually it will not trigger anything. So fall uh back trig will be not triggered for this case. So and this is your agent reasoning. So um it's treating as a high priority of emergency why this happening why this actually treat while if you would measure entropy you already could spot that something is completely wrong going on your agent have no has no idea what it's actually doing and what is uh reasoning about. So uh let's see what's

**[9:04](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=544s)** going on here. First thing, so this is again our timeline here. So this is a stable phase here. This new authentification method came new uh product, right? So this is a transition state and this is our drift where where we see everything significant. But let's just dive in a little bit and understand from the agent perspective how it looks like what's changed. Actually four things changed. First is um new product launch. So um new vocabulary is coming to your agent and your agent is not aware uh about this vocabulary. So it's actually doesn't know where to wrote it, what to do with this. There is no actually

**[9:54](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=594s)** description. Uh yeah, it never saw it. So uh second it's like new failure models. So um now difference between urgency like act with urgency and something like normal is different. So before this launch let's say let's let's go back to our case example case. So uh before if something really bad happened uh it would be say saying something like okay we um have like we cannot login for example our password is failing whatever uh for now it's completely different uh model how it failure will look like for the model. So uh third one is terminology shift by itself before um our change login just

**[10:47](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=647s)** word itself it actually means something different before thisification change login meant that something is broken user cannot actually use our solution. User actually cannot reach our solution. So something is completely bad and we need to fix it right now. Um after this uh launch actually login changed completely different the meaning. So now login it's just it's just completely different word. It doesn't mean that uh customer cannot log to our system that it cannot reach it because other words they're using. So it's not anymore uh the right priority and uh meanings of the words is different. So now the first

**[11:39](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=699s)** the last thing is uh priority label shift. So we remember that we have new wording that some of the words actually uh changed the um uh the meaning and we uh have different uh uh filler models. Right? So and we see that from our prompts actually like how we prompted this agent. So if we see login so usually it should be high but login and authentification it should be medium but it will be labeled as high because we didn't change anything in our prompting. So um yeah it was uh coming for quite a long time um completely slipped no logs nothing. So just silently coming and model is completely confused. So your

**[12:27](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=747s)** agent is confused but on the surface on a cursy everything looks perfect as it does what it's supposed to do. So here is a little bit of the architecture that we're going to take like uh all about. So we have some tickets uh tickets um uh going to some LLM classifier. LLM classifier defines like um uh what the urgency and which team it belongs to. Then it rots um it might fall back um occasionally and then we just goes to support Q and here this page at some point occasionally human can override it whether it's like completely wrong or not completely wrong and so on. So at every step in this architecture we going to uh log um what's what's agent is

**[13:21](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=801s)** doing uh so and um that will actually evaluation process uh possible for us. So if you look at the code later on um so this is a decisions DB this is where you can find actually uh everything uh we write. So uh predicted uh uh priority class probabilities confidence entropy and so uh and so on. Not going to uh read it all through. So now about signals what we actually measuring our uh matrixes and uh signals. Um yeah might be look scary because a lot of text a lot of something um yeah uh but we will go a little bit deeper into all of this. So this is in principle six

**[14:09](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=849s)** matrices that we are taking in uh six evaluation signals. So uh like um shenanropy fallback rate vocabular drift um uh disagreement disagreement is the only one where a human is actually involved um like judge score and trajectory if you want to review this later on. So this is actually what takes its in as input uh and uh like formulas uh below how it's calculated so that you can easier understand the code um that you might want to see and here is actually how to interpret it. So like for example for um entropy this is like higher is entropy obviously so it's um more confused um just important to note here for entropy and this is probably

**[14:58](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=898s)** the most important thing in this talk so please if you just forget everything if you're already sleep or whatever please hear me out only for this one thing please um for Shannon entropy just use all available probabilities that you have. Let's say for our case we have like four different classes uh of tickets like um extreme urgency, high uh mid and low right so this is like four if we just look at this formula. So then it will be just uh we have like the highest entropy will be like uh two but actually it returns not one number it returns um probability per each of these categories. So please rather use this

**[15:46](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=946s)** one because if you uh can look only on the lowest number for one of the uh categories uh it might might actually fail you and you might skip a drift. So okay uh later on we will talk about those um like in pairs. So but this is pretty practical um uh plot what it shows you in our timeline. So when we go from the stable uh running zone um running time and actually introducing our new authentification method as for per our example when uh our uh matrixes that I just showed you roughly uh will actually be triggered when they will detect that something is

**[16:34](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=994s)** wrong something is wrong something is going on um yeah here you can see that actually uh fallback rate uh it's like um it's soal like canary signal. So it shouts first when something is wrong. So that means uh uh that means that um but from specific of this uh metrics it's actually kind of shows points that something is wrong but it cannot say what exactly is wrong. So um okay might be I go really roughly through this ones because of the time. Sorry. Uh so uh s_ub_1 and s_ub_2 like entropy and fall back uh those um uh uncertainty signals uh both measure just internal confidence and uh neither of them uh needs ground

**[17:22](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1042s)** truth. So this is the point of all of this talk. So uh here you can see like how it's actually changes with a drift how it detects it uh how slowly it's going. So you see that in a stable um when we in a stable uh time it's actually pretty I mean it's pretty good there is no shift um so you remember lower is better uh and uh at um the era when actually all customer are talking in the terms of a new uh product uh it's like has no clue I mean agent doesn't have like has no clue what's what's going on so it's actually kind of not even guessing Uh yeah. So uh for this uh two like vocabular drift this is a cassand distance from a

**[18:10](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1090s)** stable uh centroidid. So it's actually calculated like um window uh usually a week and batches of all tickets that are actually uh building a vector of words uh that are used within this uh week and then it's shifting and shifting and just uh measuring like which of these uh words are shifted comparing with some stable error that that we defied as a stable error. So disagreement as I already mentioned is the only one um um human uh written. So external signal um might be one uh thing to say here is actually for stakeholders might be one of the most important. Why? Uh because it doesn't require knowledge of any statistics. So what it actually does uh if uh person uh is uh looking at the

**[19:01](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1141s)** ticket uh decision let's say yeah uh it's overrides it but for disagreement um it's actually allows you to uh for the person who's uh overriding this ticket to specify is it like completely wrong or it's just adjustment and if it's completely wrong well I mean this is pretty strong signal that your person saying that something is completely Yeah. And you can see that for our case at the end we had like uh one half of the people one two people said that this um agent was wrong. Yeah. Uh this is raising signals. Um first one like S5 is LLM as a judge. I uh used Claude Haiku for this. Um yeah it's just looks on the cached um uh

**[19:53](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1193s)** reasons uh that reasoning that we're recording and verifies it with the actual tickets to see was it actually uh faith faithful or not and trajectory is actually kind of um comes together with less judge because it shows how logical is uh our outcome. So uh this is again um again it's you you can stop me here and say like okay I talking about all of these numbers why you talking about all of these metrics and blah blah blah. So what should we do? So here's the your action points uh plot. So uh you can see how uh all of these signals are alerted like signals means matrixes. So if you have like only one signal that is uh saying that okay

**[20:42](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1242s)** something wrong it's probably will be a fallback uh because it's um shouts the first um you can just watch might be observe what's going on so if two okay investigate what's going on very likely something is broken something is wrong maybe you need to uh yeah uh s3 s4 whatever uh yeah just maybe you need to roll back or completely fix your prompt or um yeah something is going on completely wrong. So uh this is live demo and I really really hope that it's going to work. This is the dashboard. I mean if you copy the code you will get it as well. Um yeah so uh let me go like very roughly. I'm skipping this part. So this is actually a example. I'm not sure how

**[21:32](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1292s)** visible it is. I'll try to make it might be a little bit um bigger. So this is how uh our uh model uh not model like AI agent is actually processing the tickets. So here we can see like all of these matrices uh and tickets and reasoning in the same page. So uh this is table error and we have the first uh ticket that coming to us. So ticket states our service account password was rotated by it and now all automated processes are locked out. Wow, that sounds serious. What agent says? Well, it understand it. Yes, it's definitely it's blocking. So, it's uh uh wrote it as high and uh to the right people.

**[22:21](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1341s)** Okay, this is good. Uh truth. So, truth is actually high and so this is actually correct. Uh our confidence as you can see it's actually also really good. Entropy is fine. Perfect. Um what will judge said? So let's look at our reasoning. So in here, so account assess problem affecting user uh productivity needs immediate resolution. So judge looks at this reasoning looks at the ticket. Okay, sounds good. Yeah. um trajectory uh if this uh measuring if this uh um reasoning was actually pretty logical to the ticket itself and yeah looked fine. So everything is good. Now

**[23:08](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1388s)** we're going to the error unstable error where we already have the drift in uh all our wording and so on. So another ticket which is actually indicating something. Yeah. Can't login in since migration. So getting invalid grant uh after entering credentials. It says it worked last week. Okay. So if not tuned. So we have the same uh agent, right? It says wow it high. Yeah. because um I mean person cannot log in something is really wrong going on but truth it's actually um not it's medium so because it's just like change uh in um uh setup

**[23:58](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1438s)** so confidence confidence dropped significantly but still there is something but if you look at entropy it's just like a nothing yeah uh judge you can also see it's almost zero so it just immediately catches and see that actually your agent does something completely wrong. So um yeah like all of this matters. Let me go back to the presentation. So blueprint uh if you go to the code uh this is the everything you need to know again this is what we um this is what we lock like uh text um class probabilities confidence reasoning human override. So this is what we lock from all of these logs. So this is what we uh can uh what metrices we can apply, what signals we

**[24:46](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1486s)** can uh track and uh here you can see your action plans. So if one signal just triggers and just uh might be don't start to panic and uh this is actually by GPT [laughter] [gasps] but I really like this phrase. So you don't need a single accuracy number, you need a nervous system. I really like this. Um yeah, so just um accuracy doesn't really uh shows that your agent does what it's supposed to do, I guess. So just use more matrixes even if you don't have ground truth and you cannot define it by design. And this is the link to the um to the code that I just mentioned

**[25:34](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1534s)** multiple times. It has really nice vibecoded uh comments. So, it's self-explanable. [gasps and laughter] Yeah. Um yeah, here just description might be where you can find what. Um yeah, I guess that's that's it. Thank you. [applause] >> Yes, thank you very much. And I'm very sorry for the bump at the beginning but you did it very very well. >> We have a lots of questions so I hope I fear we cannot answer every question. The first question is how do you establish relative thresholds for alerting coming from a stable word pre-eployment. >> Uh this is actually all coming from uh

**[26:24](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1584s)** these numbers and so you can get it like from this formulas. uh and we know for example for this case uh we know what is stable error so we see the drift actually after new um new wording are coming let's say to us right so we can just divide it and u yeah after that uh just simply uh I mean there actually uh thresholds that uh suggested to do like for example like for entropy P this is uh like around uh 0.67. So this is like a stable uh if it's uh like higher number again again number it depends on how many um classes you have. So I mean there are actually suggested

**[27:14](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1634s)** versions what like thresholds which to use but you have to apply looking at your data at your tickets so or not tickets whatever you use. Yeah. So just uh yeah try to identify which is stable error which is transition and which is complete der. >> Okay thank you. The next question will this evaluation signal work for a multi- aent workflow rather than one agent or classifier? >> Ah that's actually a tricky one. So um the main thing is maybe I'll go here uh lock whatever you have at any stage otherwise yes you can I mean you can do it you I mean straight away but if something is actually triggering and saying like okay there is something wrong um how would you I mean if you

**[28:03](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1683s)** build it on top how would you actually understand where exactly it broke so you need to look at every step. >> Okay, thank you. And then one question. Um, is it really so different than ML? Data drift exist there as well? >> Sorry. Sorry. >> Is this really so different than machine language? Uh, machine learning. Sorry. Uh, data drifts exist there as well. What's the question? >> Okay. >> Um, sorry, I'm a little bit confused about >> read like it like it was written. So, the next Just a moment, please. Next question is is a judge classifying every ticket. This makes your cost double or only for testing evaluation set. >> No, actually every ticket. Yeah. So if you log I mean for this case actually

**[28:51](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1731s)** for this demo uh I mean we don't have like a big agent that does something like properly. So we use like uh just cached uh uh this um like reasoning. So yeah for each ticket >> maybe the last question uh how do you get the model confidence of model or judge here getting a good confidence value from LMMS is usually difficult. >> Well it is difficult. Yes. I mean what can I say? [laughter] >> Maybe then one one more question. I have an alert problem. I have an alert equals problem. What do I do now? How can I use a six matrix for derive actions to get the LMMS to stop lying again? >> Well, this is exactly the recipe that I already gave you. So, you have like uh

**[29:42](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1782s)** multiple uh metrics. I mean don't act when uh something like here for example uh this is this recipe. So, uh how many signals you have like how many metrics is alerting that something is going on. So, then just act with urgency. If it's only one or two might be just check which of those might be just something uh miscalculating something. Yeah. So uh there is no you don't need to jump immediately and shout fire. Nothing is working. Yeah. But if several because you measure it from different point of views. You measure it from external point of view. You measure it's also from internal point of view. and uh a little bit deep dive into what's going on underneath this agent. So I guess if

**[30:32](https://www.youtube.com/watch?v=vZdMN82NMTQ&t=1832s)** you have like uh different agents uh different metrics from these different layers actually saying that something is wrong. So I mean this is a very solid sign that you need to change your agent. Does it answering? I don't know. >> Oh yeah. I mean you can do I mean this is this is the purpose of all of this right because it's actually can indicate where to search what is failing at which stage yeah >> okay I think we have to stop here because the lighting talks already have started thank you very very much was very great presentation and please big applause for her thank
