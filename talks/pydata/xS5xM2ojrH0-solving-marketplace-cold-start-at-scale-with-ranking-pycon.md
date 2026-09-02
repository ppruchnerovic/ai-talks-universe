---
id: xS5xM2ojrH0
title: "Solving Marketplace Cold Start at Scale with Ranking [PyCon DE & PyData 2026]"
slug: solving-marketplace-cold-start-at-scale-with-ranking-pycon
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Theodore Meynard"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:20:55Z
video_id: xS5xM2ojrH0
url: https://www.youtube.com/watch?v=xS5xM2ojrH0
youtube_url: https://www.youtube.com/watch?v=xS5xM2ojrH0
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science"]
transcript: true
---

# Solving Marketplace Cold Start at Scale with Ranking [PyCon DE & PyData 2026]

**Theodore Meynard**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=xS5xM2ojrH0) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Theodore Meynard share a pragmatic blueprint for solving the marketplace cold start problem through scalable ranking strategies and experiment-driven iteration.

Speakers:
Theodore Meynard

Description:
Marketplace cold start occurs when new activities lack the historical data—clicks, bookings, and reviews—required by ranking models to achieve visibility, creating a self-reinforcing loop of low exposure. To break this trap and activate the growth flywheel for new supply, a system was developed to transition from rigid, manual constraints to flexible, ML-driven exploration.

Initial attempts focused on prioritizing a queue of new activities using supplier-level features or filtering out low-scoring candidates, both of which yielded marginal results. A breakthrough occurred when the system replaced random selection with the existing ranking model to pick the best candidates for reserved exposure slots. This increased conversion rates and the total number of activated activities. Subsequent iterations removed the queue and prioritization models entirely, allowing all new and unactivated activities to compete in real-time.

The final architecture replaced fixed exposure slots with a blended score, combining the standard ranking score with a boost factor for unactivated items. This flexible boosting approach increased bookings per visitor for unactivated activities. Key findings indicate that removing hand-crafted constraints increases ML optimization and that framing cold start as a supplier activation problem rather than a customer ranking problem provides clearer business metrics for success.

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

*4,733 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=6s)** Um yeah so welcome so sorry please come in I think uh there was a bit of delay for the start but uh welcome everyone uh for this first session after the keynote uh so today yeah we'll talk about uh solving marketplace cold start problem at scale uh with ranking but let's start by uh introducing myself so my name is Theo I'm a data science manager at Get Your Guide, a marketplace for travel experiences and there I'm leading the team that is responsible for the ranking of the activities on the website and the app. Um so today I'll be talking about how we solve this uh cold start problems in our marketplace and especially as part of my team. So with that let's dive into the agenda. So we'll start with the problem itself.

**[0:58](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=58s)** what cold start means in the context of a market place marketplace like ours. Then we'll look at the legacy system that we had in place. The third and probably the and the most important part is the uh of the talk will be around our experiment the third part. So the uh three years of iteration including the one that didn't work and I will close with some key takeaways from this journey and things that I think can be useful uh to you too. So the talk uh should be around 20 minutes. That should give us uh 10 minutes for questions. So looking forward to this. Great. With that, let's get started. So cold start at get your guide. First let me give you a bit more intro of get your guide. So get your guide is a two-sided

**[1:46](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=106s)** marketplace. We have suppliers that list activities and then we have traveler that book them. And so we are connecting more than 50,000 suppliers on one side with the millions of travelers across more than 200,000 activities. So at this scale ranking become critical a travelers for searching for things to do in Rome for example we only see a tiny fraction of what we have available in such a big city and touristic city like Rome. And the ranking model then decides what's get to get seen and what does not. And the last point is exactly where the cold start problem begins. So indeed our ranking model is using past behavior clicks, bookings, review etc to rank activities. So a new

**[2:35](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=155s)** activities are joining the platform today. We'll have none of that. So by default it will get ranked low then it will get no exposure, gets no booking and then stay at the bottom. And this is a self-reinforcing loop. Indeed, the situation is structurally unfair for these new items. Reviews make things even worse. Traveler are even less likely to click or book an activities with no reviews. So, the first bookings are actually the hardest to get and the system works against it. This is what we mean by the cold start uh trap or cold start problem. But we can break it. Once an activity gets its first booking, then the model can

**[3:24](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=204s)** pick the signal and then it can show it a bit higher. Then it can get even more bookings and starting this kind of reinforcing loop or flywheel is what we call on dragon uh in in the company and our team is activating the activities. Once it's activated, then basically it's able to sustain organic growth in our platform. But maybe to make you a bit more um make it a bit more practical, let's imagine you go to Berlin and you have two working s to decide. So which one you choose? Please let's vote. Who wants to be the one on the left? Raise your hand. Some courageous. Yeah. Who will be the one on the right? bit more expensive but pretty sure about you guys. So in

**[4:14](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=254s)** practice that's what we mean like this is a thing. This is very hard for the new activity to to get this first booking and maybe it's even better than the first one like in term of reviews but and it's cheaper but who will be the first one to try. So with that let's uh start with uh let's go to our second part of status quo. So what did we have? And in here our uh previous proc process was starting from a very simple ideas. New activities just need exposure to get signals. So we give them a guaranteed slot. So they get enough visibility to start collecting clicks, bookings until the ranking model is then able to take over and rank them uh naturally. Pretty

**[5:02](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=302s)** simple. So like in other words basically a new activities gets into assessment and as long as we don't have enough signal it's stay in the assessment and then we can use our normal ranking but what's happened is we see that our supply grew faster um faster than anticipated especially in some destinations and impression per location is limited. So we could not access everything at once. So for that we introduce a queue to uh limit the throughput uh to control the throughput that we put into the assess assessment pipeline here. But then we saw that the queue was getting longer and longer. So we then needed to have a model to prioritize which activities from this big queue should need to go

**[5:50](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=350s)** enter this assessment thing. And that's started like this was our process but that's uh come with some challenges especially specifically supplier will sign a deal with get your guides on board their activities pretty excited uh together and then they had to wait a long time even sometime weeks before seeing their first bookings. And second point, even if we were assessing as many as we could, we still have a significant share of them that did not activated. I.e. what I mean is like starting this virtual flywheels. Um, and so this sign like we had at the end a significant share of inventory that never received enough traction to be able to sustain their organic growth. So the process was designed this process

**[6:38](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=398s)** was designed to uh gather signal not really to activate activities and we have been solving with this um for throughput where actually our real problem we should be focusing on is trying to activate let's try to start this flywheel of these new activities. This is a reframing that change how we approach and how we approach especially how we thought about the uh the experiment that we run. With that let's go to our experiments and yeah now that you have a good idea of our setup then uh and the problem let's uh go through our multiple iteration. So the first one it was a bit hard so crawling basically in a way our first instinct was to try to uh work with the

**[7:28](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=448s)** existing system and try to make it smarter. Indeed, most activities come from supplier that are already on the platform. So, we have a track records about uh about their activities. We know their star rating, their reviews uh on their previous activities. So, hypothesis were pretty simple. If we have a strong supplier, it's more likely to have strong new activities. So, we can just use a signal to prioritize it. So, we just added supplier feature to the prioritization model. So in other word basically we try to improve this prioritization model with supplier feature but the result were kind of marginally better but not significant. The main learning that we got here was that uh by improving this prioritization model we were not really it was not a

**[8:19](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=499s)** strong lever uh towards uh improving activation. So not the thing. So with that we move to our next experiment. Uh we still try a second time to optimize the system and here our hypothesis what that we should focus on the most promising activities we could and for that what we could do is try to uh filter out the one that has the least promising based on our prioritization model so that we could spend more time on the most promising one. So in a more flowchart ways here what we say is like we introduce this shortcut to enable to directly not uh spend time on this activity with the low scoring but then we can spend more time on this uh other ones and push them harder basically and it it worked in a narrow sense. uh the activities that we

**[9:11](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=551s)** did assess were indeed more likely to be uh booked um uh but the total number of uh bookings did not really increase. We are just concentrating on fewer bets and with that we start thinking and both this experiment taught us kind of the same thing like if we are trying to be uh trying to be smarter with our current framework has limited upside. So if we want to optimize a system for activation, we needed to rethink the system itself. >> Okay. Um

**[10:03](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=603s)** sorry. Uh is it Okay, you were ask or is it I didn't get the question but if it's something that is unclear for everyone I prefer to to answer now but I'm not yeah okay let's continue then um so let's go to uh our next experiment so here up to this point basically we were randomly selecting which activity uh to boost from the uh from our assessment pool But here what we thought about is um pretty simple idea. The ranking model model uh already knows which activities are more likely to convert. So why not try to use it to pick the best candidate for the the slots the reserve slots that we have. So

**[10:51](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=651s)** there was actually an obvious tension here. We were not very convinced of this because we said that we need assessment because we don't have enough signal to rank new activities. That's the whole point of this process. So but now we are using ranking to select the activity to to show in assessment in a way. So that was a bit uh contradicting to uh the purpose of this whole thing. But like maybe on the more things like here we we improve the placement logic that we have here by now leveraging ranking to do that instead of doing uh pure randomization. And what uh turned out is that it was very positive. was uh like to our to our surprise itself, ranking was still very good at um figure out what has the best activity even if we

**[11:38](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=698s)** they were have very limited signal on those and so what we saw was a significant uplift on the conversion rate on this uh activity in assessment and we also saw an increase in the total number of activities that got a booking. So that was our first big win uh on this and with that we started uh rethink a bit more the architecture. So the success of this uh make us rethink the the whole flow and do we even need a queue and a prioritization model. Indeed, what we see is that the queue and priorization model exist to manage the limited exposure slots. But if ranking can select the best candidate in real time, the queue is just adding friction. We are reducing the set of candidate that it can uh it can select. So why not

**[12:28](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=748s)** trying to uh remove it, right? So we just take out the queue, take out the presation and directly all your activity directly go into this assessment and we let ranking do its job. basically um and what we got at the end was we saw that new activity conversion went up but the overall conversion rate dipped a bit. We were giving slots to new activities that we were not that were not yet competit competitive with the established one. This is a very classic uh exploitation explo uh exploitation sorry exploration exploitation uh tradeoff. And here what we did is actually we partner with our finance team um and we uh and we saw together we we modeled that the long-term value of

**[13:17](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=797s)** starting more flywheels cancel the short-term revenue loss uh that we saw but it simplified quite a lot of process and also improved the new supply experiences because now the new activity directly gets uh eligible for uh for for for more exposure basically. So that gave us the confidence to roll it out and we move to the next step. So removing the queue uh now and with this ranking uh selection we mainly had a ranking driven system but that raised new concerns. When ranking selects every single candidate you only ever boost the model the one that the model thinks are good candidates but maybe we stop learning about activities the model is

**[14:05](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=845s)** unsure about. So here the hypothesis that what that what we should try to reintroduce randomness in the selection that will be actually uh valuable. So what we did is we tested some kind of hybrid approach. We still use our ranking model to score the activities. Um but uh then we use the score as a probability to select which activity to be on the reserves of. So higher the score more likely this activity will be to be selected. But there is still some randomness involved. So in other words uh we kind of reintroduced some randomization in this placement logic but uh when running our test we saw that actually our result were clear. Conversion rate uh trended

**[14:53](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=893s)** negatively. We had fewer activity receiving booking overall. So what we learned is ranking model actually didn't really need need our help to diversify. So we closed this experimentally and moved on. Getting to uh first running experiment at this point we had a quite good system. We had a working system for new activity. Uh but then we start stepping back and ask us bigger ask ourel bigger question. New activities are not the only one that are stuck in this cold start trap. As I said at the at the start at the beginning, we also have a significant share of existing enferey that had go through the assessment but they did not start their flywheel. They were not activated yet. So here what we thought about is why not to try to make all unactivated activities eligible for

**[15:43](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=943s)** the boosting slots. So same mechanism ranking select the best candidates for the slots. Um so here basically to make it uh more visual we instead of just considering new activities we also will look at new activities to go through this uh feedback loop and here the result was pretty strong. So we saw a small drop in the overall customer um conversion metrics um but uh we also saw a big big uplift in the booking per visitors on this unactivated activities. So again we did a trade-off uh between the short-term performance and the long-term uh benefits for the marketplace the platform that we saw and we did the same trade-off uh and we saw

**[16:31](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=991s)** that the incremental value of starting this new flywheel largely outweight the short-term cost. So the experiment was actually the proof that the same solution could be scaled beyond new activities but also to improve the overall platform and with that we have to our last experiment that we that we run. So up to this point this um the entire system was built around fixed slots but that was actually a deliberate uh design choice. We want to have guaranteed expion which guaranteed position that mean a guaranteed exposure but fixed slots have uh flexible like but fix lots have a cost right we're always giving up the same position regardless of the context. The hypothesis here was that by having flexible boosting we'll be more

**[17:21](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1041s)** efficient by letting the system decide where the activity fit best. So for that we use some kind of blended score. We use a weighted average between the activity ranking score that we that we ranked and now we give them like some kind of uh boost factor for being unactivated. So this unactivated activity have some help but they are they they do not get like a guaranteed exposure. Uh so we let them more naturally compete uh with the rest of the activities. So more visually basically here again we're trying to optimize this optimize this uh placement uh logic that we have here and there we run two successful experiment one after the as well and both of them were positive uh and generating like a commulative strong increase in the booking per visitors on

**[18:09](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1089s)** this unactivated activities and this is now what what we have still have things uh planned for the future but I think we are now have a more much more mature version of the system we have no fixed slots no Q, no handcrafted rule and ranking now is doing most of the work with kind of lightweight intervention to give an activity a fair chance to compete and in a nutshell um that's where we were uh around uh 3 years ago and how we moved uh to this new system which is now significantly more efficient but also much simpler. With that, let's move to our uh key takeaway. So the first one uh or my first key takeaway on this is our new problem explore fast explore

**[18:59](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1139s)** fast sorry. So co starts was an underexplored problem for us uh three years ago. So for well-known problem where we have a clear northstar it makes sense I think to try multiple times uh in the same direction. For example, when we try new idea on our ranking model, things that we have been iterating for a long time and we we have a lot uh uh experience in this and we have a clear idea where we want to go. Um we try one, two, three, four, five times before we uh we really rethink if this whole approach makes sense. Here I think um for the cold start we didn't have such north star. every experiment was a completely different uh direction and every time we touch some different part of the system. So the supplier feature experiment and the low scoring removal

**[19:47](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1187s)** both failed relatively quickly. But what matter is actually that for each of us it gave us a bigger p a clearer picture of what the real problem was and especially what could be a good lever moving forward. Our second takeaway was around constraints and this pattern really um uh across like that's a pattern that we saw across our experiment and really became obvious in hindsight. So every time we try to add a constraint to add constraint like when remove low scoring activities or when we enforce randomness the result were flat or negative. that every time we try to remove a handcrafted constraint or try to increase the scope of freedom of our ML model uh like for example when we increase the uh when we have more

**[20:36](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1236s)** activity made more activity eligible removing the fixed loss we got a positive result. So I think handcrafted restriction reduce the freedom of the system and the ML model have then uh and limits the ML model this ability to optimize. So the lesson here is not to never add constraint but actually you should treat them as hypothesis and that mean you should test them. And last one probably the most important one. For a long time we frame this cold start as a ranking problem. We have a new activities. We have no data for this activity. How can we rank it? Well, we could never prove that knowing the true ranking of a new the true rank of a new activity has a measurable long-term

**[21:24](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1284s)** value. But the the framing then make us impossible to show progress on this. But the breakthrough came when we stopped thinking about it as a customer problem but more as a supplier problem. So how many activity already started a flywheel? What's the incremental value of their first bookings? And these question are much more easily answerable. And then when you get an answer, you quickly get a business case than a clear metric you can optimize and then team alignment follow. And that's changed how we uh what we build. Uh and so we start building for uh optimizing for activation instead of just throughput. And sometimes that's basically probably the best things one can do is to start by uh reframing the question.

**[22:15](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1335s)** And with that that's it. Thanks everyone. Uh I just want to give a big thanks also for the the team behind especially Shining Adus that uh who did uh the lion's chair of this work. So thanks and happy to take any question now. >> [applause] >> with your question at talks.pyon.a and I write the question to the speaker. So the fifth is I could imagine that companies listing activities might be too bother bothered by being ranked low. How do you communicate your approach in such a case? Is the ranking system interpretable enough to provide

**[23:04](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1384s)** recommendations on how to design a more appealing listing? >> Sorry. Yeah, I could imagine. >> Um, so I the accompany listing activity might be brought up by being ranked low. Yes, that's a a general thing that we have with ranking and we provide some self-s serving tools for our internal uh sales teams that is then able to explain and basically we're explain we're able to show some insights internally to show why is ranking low or not and that's how we uh handle this uh situation uh is the ranking system to provide recommendation and how to design more appealing listing. Um so the second one is this is a bit of a black box in a way like any complex machine learning

**[23:53](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1433s)** system and uh so what what we what we say and what is true is the best way to make your activity uh higher in the ranking is just uh make your activity more appealing which there are kind of normal uh things like you need to have a good title and we have guidelines for that. You need to have good picture and we have guidelines for that. You need to have right availability. I mean if you are just a guided tour but it's only at 8 a.m. you will not have a lot of people doing that. So we there is a lot of rules like that that we care about like what is a good activity and our ranking is then optimized to make the good activities go to the top basically because that's the one that sells and that's how we answer these questions.

**[24:41](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1481s)** >> Okay, next one. Are you optimizing on booking numbers or general engagement and our finance on ranking? >> So um our our ranking metric so what we're optimizing for is um at this point now is a kind of a composite metric. So we are not just optimizing purely for booking or purely for revenue. um I cannot go there but in term of fairness we don't have any kind of fairness in term of um activities I mean we we could introduce fairness but like if we have more guided tour than entry tickets like it's it's not the kind of things that we we optimize by by default like where where in some other areas it makes a lot of I mean you should be uh introducing fairness if you

**[25:29](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1529s)** are doing dealing with credit score thing but that's for This fairness is not an aspect that we treat uh given the entities that we rank basically. >> Okay, next one. How was the decision regarding guaranteed exposure made? In other words, what percentage of results were explorative and what percentage were explorative? >> Okay. Uh good question. So this decision that was made around this uh exposure sort was made years before I uh I was there and that's like basically grew against with this queue and things like that. So that's where we we were three years ago. Um in term of percentage I mean we still reserve a pretty limited

**[26:18](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1578s)** slot. So the the number of exposed slot slot that we have is relatively small compared to uh how much is reserved for exploit exploitation basically for the bestselling things because it it wouldn't it would not make sense uh to have just new activities on the page like that's no one would like this. Yeah. So yeah, we always uh push more toward exploitation and have a share not null but uh small compared to the exploitation thing. >> Yeah. >> Okay. Next one. Your model helps bringing up a new activities to customers but the problem on one of your first slides is still not solved. For example, it still has no recommendations likes and might not appear as serious solid as the other offers. Is that

**[27:08](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1628s)** problem? And if so, how do those deal with it? >> Yeah. So, yeah, that's that's exactly the I mean that's still a problem, but that's that's how we solve this problem in a way is like if if you don't show it or to nearly no one uh then it's sure that no one will book it. If you uh help it show to the by pushing it higher, you still have some people that are ready to uh to to take the uh the chance with is your product because the the other one is not exactly passing by the same touch point. I mean all your activities should have something differentiable. They should be uh cheaper or should propose something that is unique. uh if it's exactly a copycat from an existing product that's something that we uh uh that have very low chance to compete

**[27:57](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1677s)** against an existing product that is already have review and things like that. So they all have something slightly different and if we give some uh visibility to those we still have a few percentage of people that will take the chance and those people basically is the one that will be able to uh start this flywheel. basically we get the first booking we see that this activity get it first reviews and then that's how this activity gets there and that's exactly the the hardest thing we there is no other way I mean we cannot fake review like we cannot start to show reviews uh just to make people book this activity like that's that's completely against the whole marketplace idea but we still want to show this so that we have the first people to uh be able to uh to try and and then we we we see that

**[28:49](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1729s)** also they are also great and now you have more and more people that start booking it. >> Just last one, >> how do you test the results of your experiments? How did you measure the performance of the new ranking strategy with the performance of the old one? >> Yeah. Uh we run AB test. So we uh split our traffic uh or usually so or by visitors. Some of the earlier experiment were also split by uh two ideas. So half of the tour ID got a special treatment. The other half got another treatment. And at the end we can compare the score. We see how many how many of this uh tours get more booking, how many of those tour get more booking and how we statistically significance based on the total number and is do we expect that with randomness and same thing on the visitor things is we can see how uh this behavior change depending on the logic

**[29:40](https://www.youtube.com/watch?v=xS5xM2ojrH0&t=1780s)** that we put in place is do we have more people who booked less people etc. And that's the classic AB test that we have for uh for this. Yeah. Sorry, I could have been more clear on this. >> Okay, thank you again. >> Thank you.
