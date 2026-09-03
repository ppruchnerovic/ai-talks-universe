---
id: RFfInBj-lUI
title: "AI Evals Done Right: From Vibes to Confident Decisions [PyCon DE & PyData 2026]"
slug: ai-evals-done-right-from-vibes-to-confident-decisions-pycon
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Martin Seeler"]
channel: null
duration_min: 31
published_at: 2026-08-04T22:21:18Z
video_id: RFfInBj-lUI
url: https://www.youtube.com/watch?v=RFfInBj-lUI
youtube_url: https://www.youtube.com/watch?v=RFfInBj-lUI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Evals, observability & reliability"]
transcript: true
---

# AI Evals Done Right: From Vibes to Confident Decisions [PyCon DE & PyData 2026]

**Martin Seeler**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=RFfInBj-lUI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Martin Seeler, Sr Staff AI Engineer at Blue Yonder, reveal how to move beyond "vibes" and implement a rigorous error analysis methodology to make data-driven decisions for your AI products.

Speakers:
Martin Seeler

Description:
The provided transcript contains no technical content, data, or descriptions of methodologies regarding AI evaluations. It consists entirely of repeated expressions of gratitude and does not address a specific problem, approach, or set of key takeaways. Consequently, there is no subject matter available to summarize.

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

*4,792 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=RFfInBj-lUI&t=5s)** called Blue Yonder. I am senior staff engineer in the Geni area there. And Blue Yonder, for those of you who don't know, we are doing supply chain management. So everything related to goods and warehouse management and transportation management. And one of the projects I'm responsible there is a root cause analysis report. So what we are doing there we are doing some data science and in the end we uh transform everything into a nice report with the help of an LLM. So we are not throwing all the data in it and let the LLM analyze it. We have data science processes at hand but the uh report generation and the uh text generation is has been done with the LLM. So uh we are dealing with probabilistic outputs here

**[0:54](https://www.youtube.com/watch?v=RFfInBj-lUI&t=54s)** and with systems which are non-deterministic. So as you might know this is actually quite hard. Even the best companies in the world like Google and Amazon are very uh bad at it. If you look at the longtail for example you can still ask uh the Amazon recommendation to create a react component. Google is recommending to eat a stone once a day. So the traditional software engineering is quite simple, right? You have an input like 2 plus two and you have write a test to uh expect four. But geni genai is exciting because uh if you have two plus two, you might receive four. Next run you receive a five. Next time you

**[1:43](https://www.youtube.com/watch?v=RFfInBj-lUI&t=103s)** receive a poem about the number four. Uh you you never know. So it's much harder to test large language models and probabilistic systems. And that brings us to EVAs. You might have heard about EVA. Evas are the one and only solution to test large language models. And there are lots of off-the-shelf solutions out there like uh there are some dashboards and you have numbers like helpfulness and truthfulness. But my manager when I show him our report uh and I tell him hey our report has a score of helpfulness for the two um yeah he is probably looking at me and doesn't know what that actually means and if I continue with but we have a truthfulness of 4.5 he is

**[2:31](https://www.youtube.com/watch?v=RFfInBj-lUI&t=151s)** even more confused. So uh I think we can all agree that those generic evils are creating this false sense of measurements. Those are not really good evils in place. So um to sum up all the questions we have in mind uh we need to find a good way to write better evas in the first place. Okay. And if everything goes as planned, we might also use those tests to quantify our quality over time. and track the improvements when we're working on it. That would also be very great. And we need to know what to work on next. That's also something lots of companies and teams don't know actually. They are uh they have lots of ideas like oh let's try out this new rack

**[3:19](https://www.youtube.com/watch?v=RFfInBj-lUI&t=199s)** technology or this new uh framework what not and but but why and what problem you're exactly trying to solve with this is not quite clear. And last one um we also want to be sure when we are releasing a new model that uh everything is working quite fine. For example Sarah Sex, she is lead uh of the geni team at notion and she wrote that they released the newest entropic model back then within 24 hours after release. So I don't know but please raise your hand if you're working with large language models in production. Okay. And please keep your hand up if you think you can answer all those questions. None. Okay. Oh, one. Okay, great. For

**[4:11](https://www.youtube.com/watch?v=RFfInBj-lUI&t=251s)** the rest of you, I hope that after this talk, you feel much more confident and you drive back home and you start implementing much better ES. Let's see. So, uh, spoiler, I already I will already tell you how to do it. And uh there's something called error analysis. This is nothing new. It's actually more than 50 years old already. And it was invented to test stoastical systems like OCR for example. And it's quite an easy process. You create a a data set then you annotate those traces and then you group those errors together. And in the end you iterate and refine more and more. That's the whole idea of error analysis. And to show you how easy it is and how much value it provides, we will

**[4:59](https://www.youtube.com/watch?v=RFfInBj-lUI&t=299s)** do it with one of our examples of the report I showed you earlier. Okay. But before we can start, we need of course a mechanism to start collecting traces in the first place because if you are not able to monitor what your agent is doing, you have a problem. So there are lots of different solutions out there. A trace is uh the full end to end uh action your agent took or your LM from input how long it took uh which model it used how many tokens it consumed so it tracks uh all the actions and for a chatbot might be easier for an uh agent performing more steps you have longer traces but there are lots of solutions I try to keep it as agnostic as possible uh length use brain trust you can choose

**[5:47](https://www.youtube.com/watch?v=RFfInBj-lUI&t=347s)** whatever you want but uh you need to start to collect traces in the first place. So now that you have some traces you can look at um you need to decide which traces you are annotating and there might be many many traces and you need a mechanism to find out which one to start with and with how many and I can tell you we need to keep our costs low. Uh we cannot put someone at the desk and tell them hey please look at 1,000 traces. So uh you can start with 20 or even less and you do this process until you reach a point of um theoretical set saturation that means you don't find anything new. Uh so it's quite easy and which ones to choose? Well, you can use random

**[6:36](https://www.youtube.com/watch?v=RFfInBj-lUI&t=396s)** sampling or you use those generic evas like uh helpfulness as a base line and you select the first traces. Okay, here's an example from our reports. So as you can see in the top um we are talking about 100% of shipments are late but the number of shipments is actually zero. So uh we need to put our product head on and we simply annotate this trace from a customer perspective and we would write down uh this is a contradicting statement for example. The next one we are talking about severe inefficiencies and significant delays but remember we are we don't have any late shipments. So uh we would also write this down. Okay. Um and the important thing is we are doing uh

**[7:25](https://www.youtube.com/watch?v=RFfInBj-lUI&t=445s)** outcome based evaluation. So we are looking at it from a customer perspective. So don't comment stuff like oh the model did not call the right tool at the right place here. So instead from a customer what would the customer have to say when he's reading the report. Okay. So uh another example uh average worker productivity stands at 14.52. Well uh my teacher would have said 14 what apples. Um so there's probably a unit missing. Uh that would be nice to have. Also we are talking about 25% of our workforce is uh low performers. Um if we would release this I might receive a notification from HR. they want to discuss something with me. Um, so better annotate this as well. And

**[8:16](https://www.youtube.com/watch?v=RFfInBj-lUI&t=496s)** then there are more trickier ones like low performers take 70% longer uh blah blah blah due to pecking congestions. This one is much trickier to spot and that's that's why it's important to have some subject matter expert at hand to uh make those comments because actually uh since we have a congestion the people take longer and it's not the other way around. So this is a um yeah a problem of inverse causality here right so if I would have shown this to an LLM the LLM would have said wow it's a great report I like it um that's important uh to know so don't let an LLM write the comments for you let anme comment on your traces okay now the next thing is that we group

**[9:06](https://www.youtube.com/watch?v=RFfInBj-lUI&t=546s)** all those comments together and for example we had several comments about the low performers so we can group everything into judgmental language. And how you can group it? Well, you can here you can use an LLM again. Throw everything into CHGBT. Hey CHBT, please group all those comments for me. Uh or you're using embeddings. And now I grouped this into judgmental language. Now judgmental language that is a very good evil, right? Much better than helpfulness. And we had 168 comments and we grouped them to down into 19 different failure modes. Okay. Okay. Now that we are now that we know what we are going to uh test in in our case let's test judgmental language. We can um decide how we are going to test this. There are two different ways. One

**[9:56](https://www.youtube.com/watch?v=RFfInBj-lUI&t=596s)** is verifiables. So for example you have a regax for units for example or you want to test how long the report is. You can do this via code and you have non-verifiables like subjective things. And here you need LLM as a judge. You want to have as much as possible of verifiables. Why? Because they are repeatable, cheap, fast, much better. LLM as a judge, a little bit more expensive, slow. So try to keep as much as possible in this area. Okay. But let's say you need to write an LLM as a judge. And um the good thing is now that you've written down all those comments, you can use those examples from your comments by uh putting them into the prompt. So you

**[10:43](https://www.youtube.com/watch?v=RFfInBj-lUI&t=643s)** give some context, you're evaluating a root cause analysis report and then you give some positive and negative examples. Okay? And in the in the end you have a placeholder where you throw in the the report and then you have an LLM evaluating your report. Now the thing is um if you then let the LLM decide how how much judgmental language it has uh it gets a little bit tricky. So for example, if we have a so-called Lyot scale, there a scale from 1 to 5 or 1 to 7, uh it's very difficult to make a difference between 3.9 or 4.1. What's the difference anyway? So uh the better option is to make it binary. Let the LLM as a judge return one in case of

**[11:33](https://www.youtube.com/watch?v=RFfInBj-lUI&t=693s)** a failure mode and zero in case there is no error. So you have a clear distinction between failure or not. And uh if you think about it, you have to make it a binary decision anyway because even if you have a Lykot scale, you need to decide what the cut off rate is for you to say, okay, at this point it's too bad to put it into production. So you're making it a binary decision in the end anyway. So uh you can start it from scratch with binary returns right away. Okay, now that we know how we can s how we can write such an LLM as a judge, we need to make sure how we can trust him. That's uh also possible by bringing your theme back into play. So let's say we

**[12:23](https://www.youtube.com/watch?v=RFfInBj-lUI&t=743s)** have decided okay judgmental language is an evil we we want to have. We can give our theme 20 reports. let him label those 20 reports where he thinks that this contains judgmental language and then we run our LLM as a judge and we create something uh like a confusion matrix and the important thing here is that we will focus on the true positives and the true negatives because uh let's assume that the error is in the long tail that we only have very rare errors. uh if we simply return every time zero for we don't have an error uh we might even get 99% accuracy uh but in the end it's not really that good. So um yeah you can label those and compare it with

**[13:12](https://www.youtube.com/watch?v=RFfInBj-lUI&t=792s)** a confusion confusion matrix until you are satisfied. And the other question I get quite often is can I use the same model for the evaluation uh as I'm using in my product? And the answer is yes because usually the task is quite different than what you are actually doing on the other side. So if I let the LLM generate a report that's quite a diff different task than uh grading it for judgmental language right but there are actually some models who identify oh this text might looks like I have written this I I think I like it. So there are some uh there might be some bias. There are some papers about this if you want to read more. Uh but you can start with the most capable model first and then optimize for costs later. And uh another thing there's uh when you

**[14:04](https://www.youtube.com/watch?v=RFfInBj-lUI&t=844s)** reach 100% accuracy or pass rate as you want um that means you don't really know anymore what to work on next. So if you have a stoastic system like an LLM, you should never reach 100%. That simply means that your tests are not challenging enough. So if you really reach 100%, start your whole process from from the beginning again. Create new annotations, create new failure modes and so and so on. Now coming back to our report, uh I said we had 19 different failure modes. We also group them into four different main uh categories. For example, the judgmental language you can find in the bottom right here as well as some uh generic titles for example. And we could

**[14:52](https://www.youtube.com/watch?v=RFfInBj-lUI&t=892s)** say both are related to presentation quality. Right? So we can create this taxonomy and this is quite cool because uh if we set up the LLM as a judge as a continuous evaluation and we grade every new report, we can simply create new data sets. We can every time the LLM as a judge uh marked a report as judgmental language, put it in a custom data set only containing judgmental language or for the full presentation quality even that might also be really nice. And there is a powerful technique in data science which is called counting. And if we if we apply this um we get this beautiful chart. So each color here is one top category. Blue for example is context clarity. Purple is presentation

**[15:41](https://www.youtube.com/watch?v=RFfInBj-lUI&t=941s)** quality. And now we can see how often each error actually occurs. And if we then say how meaningful each error is for our product, we can actually decide what to work on next, what's most important for us to work on. And for example, when we are doing this for one model, we can repeat the whole process for multiple models. So this is an older chart. Therefore, the models are a bit older as well. Each color is a different model. Green, for example, is GPT41 nano. uh the red one is GPT40 and now we are running the same experiment for different models and we can now compare okay GPD4.1 nano has only 96% error rate and GP40 75 and now

**[16:31](https://www.youtube.com/watch?v=RFfInBj-lUI&t=991s)** we have concrete numbers at hand to uh compare those things and let's look at this chart those are the different uh top categories And again, each color is a different model. And what can you see by looking at this chart? Well, the first thing you can see is that the errors are actually quite evenly distributed across the different models. And that's that tells you something. And it's that it's not a model problem we are having. It's a prompting problem. because if it would be a model problem, one model would have more errors than the other. But it's actually quite evenly distributed. And now together with the stats from our

**[17:20](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1040s)** monitoring where we track how long each request takes and how many token it consumes and therefore how costly it is, we can actually create a report per model compared to our base model. And I c can give this report to our manager and say hey for example GPT4.1 nano uh reduce the context clarity by 6.2% and uh it's running se uh 37% faster even and it's costing 96% less. That that's something my manager can work with, right? Much better than hey we have helpfulness of 4.2. Um and and based on those numbers, you can actually make decisions. And how you make those decisions is up

**[18:08](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1088s)** to you. For example, uh let's compare it with a sink. If you are washing dishes, you can start from the top and simply uh start with the most convenient one or you take out the huge pot first and uh start with the with the biggest impact at first. That's totally up to you. And what you are ending up with is this beautiful data flywheel, right? So let's assume that uh you have a product in production and you're constantly monitoring this product and also you have set up all the LLM as a judge. So you have constant evaluations of your reports per each category from our 19 different failure modes.

**[18:55](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1135s)** the product manager or whoever is responsible for your uh decisions here can now based on those statistics make decisions like hey we need to work on judgmental language or the next release is focused on context clarity for example and is working on five different failure modes at once. Now he can take this task, plan it and tell the engineer, the developer, hey in our next release we need to tackle judgmental language. Now the engineer has a concrete goal to work at and how he's achieving this that's completely up to the engineer in the end. He can try out a new rack system, change the prompt, uh whatever that's completely freedom how he's tackling this uh

**[19:46](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1186s)** problem. And he also has metrics to test his own progress. And when he's satisfied, he can report back the new numbers to the product manager. And in the end uh they can decide if it's good enough to release the new model or not. And you uh repeat this process over and over again and by doing that you can actually improve over time much better. So coming back to our initial questions um how can we find good evas that's the process I just described you are doing error analysis by annotating your traces then collecting those traces grouping them together and from those groups by using those examples from your annotations creating very good uh LLM as

**[20:33](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1233s)** a judge prompts and then by comparing it with the confusion matrix you may get very good aligned withmemes and then you have complete uh confidence that the LLM as a judge is exactly doing what you are trying to achieve. Now how can we quantify the product quality uh that we have seen in the bar chart we can quantify and see the progress over time and what's the most critical task to tackle on? Well, if you combine the actual um bar charts and the errors with an impact level or you give it a score, you can decide what's the most critical task to work on next. And the last one, how can we be sure to release a new model? Well, with this approach, whenever a new model comes

**[21:21](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1281s)** out, you simply rerun it with uh all your LLM as a judge in place. you would get immediately this nice chart how how it compares to your current baseline and you can give it to your manager I don't know 10 minutes after release and uh 24 hours later you can already run it in production so there is actually um some guy uh Hame Husin he is very famous for this whole process and if you want to learn more about this I highly recommend his course for this as well it's quite costly but uh it's worth it. Yeah. And uh from my side that's actually it was useful feel free to get in touch with me and also we are hiring. So if you're interested in working some um LLM

**[22:12](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1332s)** and GI areas then feel free to reach out and happy to answer your questions. [applause] Thank you Martin. It was quite an interesting talk and uh we have a dozen of questions at least. >> Okay. I don't know if this if that's good. >> Let's start with the first uh how do you avoid the manual labeling hell when you iterate? So for example, you change the prompt or the model or etc. uh how I avoid what the >> the labeling the labeling manual labeling hell. So >> you can't uh avoid this. So the manual labeling the annotating that's something someone has to do as I said you can't

**[23:01](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1381s)** use an LLM for that. someone with domain knowledge needs to do this and uh yeah the labeling I mean you can start by writing the LLM as a judge and if you think it's good enough and you don't need to align it with anme that's also fine but I would highly suggest that you uh align it by comparing the labels from your LLM as a judge with the labels from anme >> okay uh the second one is do you keep the LLM judge uh constant when evaluating different models or do you change this too? Seems likely that evaluating a model with itself even with a different context can just reproduce failure models. >> No, you keep the uh prompt the same. That's crucial to make it a fair comparison. And if you would not do

**[23:50](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1430s)** this, you would actually uh write a custom prompt just for the model. But the idea is that models come and go and the uh prompts or the evas are here to stay. that's that's your ground truth and what you're trying to achieve. So um don't customize prompts for different models just for testing. So for the testing it has to be the same. When you have it in production and uh you see that the numbers are much better with a different prompt that's of course totally fine. Um if that improves your overall quality then >> okay uh the second one is how do we evaluate tech generation of a model quantitively without LLM judges? >> Yeah that's the verifiable approach. So if you find things like uh I don't know

**[24:40](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1480s)** units for example you can write a regax for that. You can have code to check how long the report is and there are lots of different ideas and I yeah I don't have more examples now but uh that's the preferred way actually as I said llm judge is much uh more costly and takes much longer okay the next one would be a tricky one uh how do we evaluate the benefit of a gen AI generates >> that I can't uh answer that has to uh be answered by product managers. How much that improves your numbers like uh revenue from customers etc. PP so those are actually numbers your company needs to have in place to evaluate how uh much

**[25:32](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1532s)** an or a new version of the product improves on business numbers. >> Okay. Uh just a moment. Uh oh my uh you said the engineer focused on fixing one thing on each release. How do we ensure that doesn't make other factors worse? >> Yeah, you run of course every evil you have in place. So uh what I meant was um your engineer gets a specific task like I don't know I could tell my colleague hey please work on uh judgmental language and he can then go ahead try different techniques to improve this but

**[26:23](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1583s)** before we we release it we will of course run all the evas again and see okay uh well yeah we fixed judgmental language but all the other metrics are much worse now then of course we would not release it. So uh that's why you have so many failure modes and EVAs in place. So every failure mode in the end becomes an LM an EVA and it's either evaluated through code if it's a verifiable or through an LLM as a judge. >> Okay. Uh the next one when do you run these tests if they are rather expensive? depends on how much uh you want to spend and how many you can afford. I mean you need to definitely run this before you release something to be sure that uh you

**[27:12](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1632s)** don't mess up. Uh preferably you would also run this on a sampled set in production to measure online how you perform over time and also to discover user drift. Um that's a little bit tricky but uh remember in good old days maybe some of you can remember when chbt came out what was the first thing everyone did uh hey chgt please write me a poem about I don't know uh please write me a poem about my job and nowadays nobody is actually writing poems with chgbt anymore so there was a drift in user behavior and if you have online evaluations also in hand um then you might see this in your EVAs and how the errors uh come back um as well and

**[28:01](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1681s)** that's also then a good time to redo the whole process but otherwise it's a one-time process and you don't have to do it that often um yes it's uh you need anme in the beginning and it might take some time but it's totally worth it. >> Good. Uh the next one is an advanced one. uh what is the framework you are using to do the LLM as a judge? >> In our case, we are simply using um Lenfuse that uh is also our monitoring and you can set up LLM as a judge in there as well. But as I said the the whole idea of error analysis is framework agnostic. You can also write everything from scratch uh in your own infrastructure. Um that's totally up to you.

**[28:51](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1731s)** >> Okay. Yeah. Uh when you use LM as a judge, your return is binary as you told. >> Um do you have a threshold underneath or zero is really no error? I think like >> we have a gray area somewhere in between zero and one. >> So what can we probably do with it? >> No. Uh the prompt actually mentions that the judge uh is only allowed to create either zero or one and we are using examples from our comments uh and tell the LM as a judge hey if those things are included in a report like low performers that's definitely a judgmental language and can include other examples and we

**[29:39](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1779s)** can also use positive examples what we would expect instead but in the end we want either zero for everything is fine or on if there was judgmental language in it. And of course, you can then uh average this score about uh your your traces like uh the last 100 reports and have a continuous number what the percentage is and there you can have a threshold again. But it's easier to say that it's not allowed to uh that we are having more than 10% of judgmental language in our reports than if you have a like scale that you define okay 2.3 is our cutoff rate for example that's much harder to do because uh again uh people default to the safe middle values anyway

**[30:28](https://www.youtube.com/watch?v=RFfInBj-lUI&t=1828s)** it's like a gas uh curve and um if I asked someone here they would the average would be in the middle anyway. So uh it's much better to have binary decisions. >> Okay. So I think we have a couple of more questions though the time is over for this talk though I think uh if you have these questions probably you can reach out to Martin directly. Yeah. >> So and let's once again thanks Martin for this great talk. [applause] >> Thank you.
