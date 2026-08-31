---
id: NxxXpmXa3ws
title: "Hype, Hope, or Headache? Making Sense of GenAI, LLMs, and AI Agents with Anecdotal Evidence"
slug: hype-hope-or-headache-making-sense-of-genai-llms-and-ai
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Sebastian Neubauer"]
channel: "PyData"
duration_min: 27
published_at: 2026-08-04T22:21:58Z
video_id: NxxXpmXa3ws
youtube_url: https://www.youtube.com/watch?v=NxxXpmXa3ws
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Hype, Hope, or Headache? Making Sense of GenAI, LLMs, and AI Agents with Anecdotal Evidence

**Sebastian Neubauer**

`PyData` · `PyData` · `2026` · `27 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=NxxXpmXa3ws) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Sebastian Neubauer deliver a pragmatic, "anti-bullshit" guide to navigating the hype of GenAI, LLMs, and AI agents in industrial settings.

Speakers:
Sebastian Neubauer

Description:
The current trend toward Generative AI and Large Language Models (LLMs) creates a risk of neglecting traditional data science. Over-reliance on LLMs for simple problems violates Occam's Razor, as high-parameter models are often inefficient compared to linear regression or scikit-learn models for specific, low-complexity tasks. There is a concern that the field of mathematical and statistical data science is declining as practitioners shift toward "shiny" GenAI tools, potentially sacrificing the robustness of Bayesian networks and other traditional algorithms.

An AI agent is defined specifically as a system where an LLM acts as a central brain, calling tools in a loop to achieve a goal. This differs from traditional automation, such as a dishwasher or a warehouse management system, which relies on "if-this-then-that" logic. The primary value of AI agents lies in automating low-frequency, high-complexity tasks—such as planning a wedding—that were previously too expensive to automate using traditional software engineering because the development cost outweighed the time saved.

To determine the appropriate automation tool, a cost-benefit analysis based on task frequency and time savings is required. High-frequency tasks should be handled by robust, cheap, and testable traditional automation. Low-frequency tasks are better suited for AI agents. The economic disruption of AI agents is compared to the Toyota Model G loom; the loom did not increase weaving speed but introduced a notification system (a bell) that allowed one operator to manage multiple machines. Similarly, the value of AI agents lies in their ability to handle diverse tasks and signal when human intervention is needed, rather than simply increasing raw processing speed.

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

*4,212 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=5s)** Okay. Yeah. So, uh a quick introduction uh about me. So, I'm I'm a my role title is data scientist at Blue Yonder since 14 years already. So, it's it's quite a bit. Um and now I'm in the GI team. And that's why I I chose this this picture because um uh I'm a little bit the black sheep there, right? So everybody's hyping all those things, right? It's the new shiny stuff and so uh that's why three years ago I started to do an internal talk series and once a year I updated the series, right? So what's the the new development? And so I decided uh in in in December that why not sharing um those things also with a greater

**[0:54](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=54s)** audience and now it's a real great audience. So it's if is there still some seats left then raise your hand. Okay. There's one. Okay. So I I gave uh this talk um yeah three years in a row. So always updated a little bit. Uh but then when I handed in the Pyon talk more or less this happened. So I don't know if you know this homepage. It's uh uh WTF happened 2025. I don't want to go into details right now. Uh but probably many of you in in in the room share this feeling that something strange is happening and yeah it's getting different somehow. So I decided to more or less squeeze the the the rant a bit and and also uh have a look at at the

**[1:42](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=102s)** new things which are happening. And first of all a little disclaimer because I mean if you do a rant it's easy to say ah it's just this guy he doesn't like LLMs that's it right full stop. Uh but that's not the case. I I love it, right? It's uh it's really uh amazing technology. It's uh it's it's disruptive, right? And for me as a very very lazy person, it's it's really incredible. It helps me a lot. So I can do stuff uh which would take me I don't know half an hour to write an email. Now I can do it in two seconds. So I I really love it. So this talk is not about that I don't like uh the technology or whatever. Right? So this is uh this is going in a in a different direction also. I mean um why I u chose this picture here. So um I I really

**[2:36](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=156s)** thought let's say 5 years ago the first industry which gets distribute um disrupted uh is is something like self-driving cars or something like this right but now it it it I mean it it was industries like uh translation industries or uh media art industries and and all these things where I thought oh no that's creative work that's never going uh taken away by uh by computers but now there we are. Um I I try to update the pictures with the same prompts year over year. Uh but if you for example have a look that was one of the newest ones that's matur some some other so I don't like it. It looks so I don't know I couldn't get good pictures so I decided to stick with

**[3:24](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=204s)** the old ones throughout the talk. uh they have some kind of a nice uh yeah it's somehow nice to look at awkward but uh it's it's it's I like it more. So um this this slide is actually 3 years old. So um let's just imagine for a second that we are in a in a in the time where um just uh the wheel was invented. So we open LinkedIn and LinkedIn is full of there is a new technology called the wheel right we see cars we see bicycles we see we see all these uh fancy things and then we are a CEO of a toaster company. So, what's your

**[4:16](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=256s)** what do you have to do, right? So, you add a wheel to your toaster because, of course, everybody puts wheels on toasters. Um, yes. I mean, that's I mean, I don't have to explain it, right? You you know what where I'm going with this. So, of course, we cannot just throw away all the things we already know. We have to make sense of things and ask customers, what do we really want? What's valuable for you? and all these things and then I even figured out this right so I I thought when when I made this this was more or less really a prediction because the in 2023 there wasn't many products with AI attached to it was just everybody was talking about it that we should do it now this is new so who knows this thing it's even a wheel it's even a wheel look at it [laughter]

**[5:05](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=305s)** have you ever tried it I mean I asked it what friends do I frequent frequent frequently chat with on WhatsApp? Oh, I don't have access to your messages. Okay. Why Why is there a Okay, I don't get it. So, yeah, I don't get it. So, um from the Blue Yonder perspective, so Blue Yonder does uh all kind of um what? Yeah. uh does all kind of software around supply chain. So um warehouse management system systems, transportation management systems, all these things. And of course that's a very traditional field of operations research. So algorithms uh the top-notch algorithms in the world,

**[5:54](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=354s)** right? So really doing all these kind of uh fancy uh optimization, linear programming, all these really fancy things. Uh and of course now same things are happening here. So people asked where is geni right so where is it and uh I mean here I mean preaching to the choir right everyone I'm pretty sure everyone in this room knows that language models are not really good at doing math right so but for us we are in the field we know about numbers we we know how a transformer architecture maybe works or something like is so for us maybe it's it's it's more obvious but for somebody who's maybe not that

**[6:41](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=401s)** technical it's not at all obvious why jet GPT gives me an answer to a prediction of how many kilos of bananas do I have to order for tomorrow it gives an answer right it gives 4.5 kilograms but is it so easy to figure out for people who might might not be that technical to really understand that this is a bad idea. So that's more or less that's that's my mission for you, right? So it's your job to tell other people, wait a second, it's not the right tool for the right it's not the right hammer for for this nail that we have here, right? Or it's not a nail or whatever. So um and and also here I mean I'm not saying that there is no use case. Every

**[7:31](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=451s)** company probably has use cases where LLMs actually make sense. I mean, LLMs are good for transforming unstructured data into structured data, for example. I mean, yes, yes, we can have it. Uh, but find the right nail if you have a hammer. That's that's all I want to say here. And this this time it's really not just anecdotal evidence, right? There is even a paper uh I I guess you maybe you you saw it. So they they just used um uh used uh LLMs to to solve the math Olympia um but not the usual ones, the ones which already exist probably also somewhere in the training data but the newest one, right? So it was clear this is the newest Marthol Olympia. It cannot

**[8:19](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=499s)** be in the data set and all of a sudden all of the LLMs got much worse than before. So somehow it was just target information somehow sneaked into the training data set. So I guess uh yeah preaching to the choir you all know this and yet now you you could say is it really that bad? Is is there any problem with it? Um maybe some things are stupid. uh but but it's not because there is this strange this strange feeling that somehow there is this new AI and this old bad AI and many here are data scientists or machine learning experts and so on and I guess I

**[9:09](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=549s)** guess we we all share this. Just just the other day we had a discussion and uh somebody asked do you mean this new AI and no no I mean a traditional machine learning algorithm and okay I I thought the new AI no um so yeah also here it's it's our job to somehow tell people no no no if it's a linear problem a linear regression might be the best fit don't try to do it with an LLM even maybe you can somehow figure it mode uh also Okam's razor right for Okam's razor says the simplest solution is the best solution so always choose the uh the simplest solution for a job so you don't need to have 5 billion parameters for a one parameter problem so I I would say this can be very

**[10:00](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=600s)** harmful if if somehow there is this uh this uh opinion that oh you're working on this old old scikitlearn model Shouldn't you use something more modern? And uh I I think that would be very bad and I guess it will come back and we will use scikitlearn more maybe in the in the coming years. Um and I mean this is really then anecdotal evidence right because I haven't found something to really um uh to to to really uh prove this point. But I mean for us at the Python conference, this is somehow remarkable that now the number one script uh the number one um programming language is not Python anymore. It's gone, right? We were we were top ranking in all of the in all of the indices uh before and

**[10:51](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=651s)** there was one reason it was data science. Everybody who did data science used Python and then you built your applications also using Python. But the core was we want to have the machine learning models. We do it in Python. We do Jupyter notebooks, exploratory data analysis. This is all the Python world. Now, I mean, as I said, it's just anecdotal, right? It's no proof. But maybe seeing that other languages like JavaScript or TypeScript is number one. Maybe it shows not so many people are working on actual data science anymore. And that's really bad right? And then that's that's one of my my points I I I I I don't see enough mentioned um also on LinkedIn and and so on. I mean when when

**[11:40](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=700s)** I started my PhD I was working on machine learning models all these things right and and I thought yes all these things like machine learning AI we called it AI back then as well but more or less this was the future. So um but uh I thought this will make us super human, right? So whatever we do now, it's much better then. And then this happens, right? I [laughter] mean what what we actually did is we made computers as dumb as we humans are. Why? [laughter] I mean uh I mean computers could do things like this before and now they can't. And I don't get it. I mean I I'm just waiting for the I mean also when I made

**[12:28](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=748s)** this slide two years ago I was like yeah I guess in future I will book my flight and instead of going to New York I go to I don't know Amsterdam because just an LM thought it's maybe a nicer uh nicer destination or whatever. Um so I don't know then I I got this uh advertisement on uh on my mobile. So here you can search for flights using LLM. I was like, "Oh, I don't know if that's good. Let's try it." So, I mean, this is this is the end of the first part um of the talk. Um because there is Yeah, I mean summing this all up really there is this uh this problem maybe the world just says, "Oh, okay. There was the year 2010 until

**[13:19](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=799s)** 2020. We did data science. we were at a at a good good trajec trajectory. So we built good models that could solve really really sophisticated problems. Uh and now if really we decide to just move on and do the new stuff and we don't care about Bashan network anymore because ah now I have my uh LLM which does all the stuff. Um I don't think that's that's a good a good thing, right? I mean uh coming back to my original slide, right? I am now in the Chennai team. It's not bad. It's I Yeah, thank you. Uh it's it's not bad at all, right? It's it's fancy. It's shiny. We do cool things. So it's it's not about this, but it's somehow also proves the point. Uh maybe it is the case that somehow this traditional deep

**[14:09](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=849s)** mathematical statistical data science field is somehow drying out and maybe we should fight for it that that it's not happening and this brings me to wow now what happened right um so maybe maybe you're all sleeping right now so maybe please stand all stand up once all standing. And now please sit down if something in your daily work significantly changed over the past six months. And now sit down if you think uh no sit down

**[14:59](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=899s)** if you think something will change in the next two years in your work. I want to talk to you what you are doing because I cannot think of anything but [laughter] no. [snorts] Yeah. So yeah I mean we we just saw it. So everybody has this feeling that something is happening. I mean just I mean I put this here but there are so on this page there are a lot of uh different signals from from everywhere. So why is why are things changed or where are the signals where we see that something is changing? This is just a very simple uh plot. I mean maybe maybe it's complicated but uh just to give you a very quick uh thing. So that's the number of hours a human would have to do the job.

**[15:49](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=949s)** And um and then you see uh so that that's the equivalent what a human would have to do for an LLM to solve it in a 50/50 chance. So and you see yes there is something happening right. So uh around here it was like okay maybe I can do something a human would take one hour but this exploded somehow and I mean this also can be seen just yesterday I I searched Google trends for claw code and open claw. I mean those are the the buzzwords which were popping up around December as well. Uh I was kind of surprised that the open claw is declining so steeply and also plot code. So maybe it is just a hype thing and um maybe it is going away but I doubt it. But um yeah

**[16:41](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1001s)** so but when I started to to have a look at at all these things, right? So my my question was what is an agent? Why is everybody talking about an agent? What what is this? What is this really? Because I mean for example I have a dishwasher at home. I put my dish in, I press start, it does something, and in the end I have a cleaned dish. So that's that's like an agent, right? It it's it it's automating things that I had to do as a human before. So why are now people talking about agents and what's the difference? Um, so first of all, then there is just a very strict definition. AI agent is a very strict definition. Uh I think I have the definition from you. So it's uh it's more or less you just have a brain

**[17:32](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1052s)** which is the LLM. The LLM is calling tools in a loop to achieve a goal. So you tell it okay do this. Then the LLM calls tools in a loop until it finally solves the problem or or reaches the goal. So that's the very definition of an AI agent and that's what we are talking about. If if something else is happening, we probably would just not call it an AI agent, right? So that's that's the because I mean of course if this then that brings you a long way. The dishwasher is just if this then that if uh clean then do something else. Um it it brings you a long way. Only if we have this LLM, this brain in the middle and it calls tools in a loop then we call it an AI agent. And still I I was thinking

**[18:24](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1104s)** so um when do I have to use this AI agent thing and maybe if if there is one thing you should take home from my talk then it's it's this I hope most of you know this because everybody should have this on uh on his and her desk. So for example take so it it shows how often you do a task and uh how much you can save by automating it and this then is the number you are allowed to invest into building the automation for it. So if we take the the dishwasher, it's maybe something like around uh five times a day if you have a big family.

**[19:14](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1154s)** Uh and maybe uh dishwashing takes 30 minutes. So you you in your household, you would have six months to build a dishwasher and you would still then in five years be on on a positive return, right? So you can quickly check okay what's happening yearly 5 seconds uh 1 second okay 5 seconds I mean there there's no there's no uh deeper thing behind it it's it's school math right but but still it's it's good to yeah thank you it's good to just see it once and now let's have a look at this everybody talking about AI agents yes they are awesome this sector over here before we couldn't do because what we were doing as software engineers. We were building these things. We built automating automation

**[20:03](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1203s)** systems which are used heavily. Let's say um warehouse management system thousands of operations per day uh and maybe automating away a second still you can work a long time on it. Right? or here it's absolutely clear these systems we already have because this is the dishwasher and we already have dishwashers at home so this is done already but with the new thing we can explore this field over there which is remarkable because I guess there is a lot of money to be made um and it was just not accessible because you can't just afford to put that tiny number of work into into something to automate it but now you have this brain in the

**[20:50](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1250s)** middle. So you can tell the brain, please solve this for me. Even if it's you're planning your wedding, you will only plan your wedding hopefully once once in your lifetime. Uh but now still you can pass it over to an AI agent to automate something of it because it has a brain, right? So that's the for me that's the clue. And always when people are talking about it uh and and they say, "Oh, we've built this AI agent." I'm like, you're in the wrong corner. You are automating something which is, I don't know, used 50 million times a day. Uh just build a if this then that solution that's probably more robust, more more cheap, uh better testable, all these things, right? So, yeah, uh show this to your uh to your CEO. Uh it might help to

**[21:40](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1300s)** to figure out stuff. Um there is we just saw most of except three people of this conference everybody uh has uh has a feeling something is changing. So there will be a deeper dive. We saw it in the opening session this morning. So there will be a a panel uh I'm the moderator so I have to find some questions. If you if you have some question just send it to me uh over uh over discord. Then there is a open workshop tomorrow. So it's really everybody is uh is welcome to join and we can find ways to to discuss all the things and a final panel on uh on Thursday and I want to send you home with um with this machine. [panting]

**[22:30](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1350s)** No, I don't. Yeah. Is is there I mean maybe some of my colleagues already saw this but is there anyone who knows what this is? You don't know the English word. I didn't know the English word for it either. It's a loom but it's a special one. It's the Toyota model G loom. I think I looked it up and it's really the same Toyota from the cars today. So somehow there is a connection. So question is is this the the first automated loom? So loom is where where you make your clothes with. Um, so you have all those strings, these threads here, and then you you weave some things in between. Was it the first automated loom? No, it wasn't there.

**[23:20](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1400s)** That's a good one. Yeah. Um, no. So a quick explanation. So there were looms before and they were not uh faster not uh so this one is not faster and and not not uh much better in in any in any dimension but it was the first one which was an economic success and it disrupted the whole industry. Now I explain what's happening. So there were automated looms before but if one of those threats breaks everything which is produced afterwards is trash. So what happened next to every loom there has to be one human operator checking if one of the threads is breaking to stop the machine repair it and then go on. So one loom one operator this one

**[24:12](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1452s)** I don't find it somewhere there is a small bell so they have some needles here and they they uh check if the threat is still ongoing. If one of those breaks, there is a bell which makes bing. All of a sudden, one operator can operate a whole a whole um area of looms because he knows, oh, there is something broken over there. I go over there and I fix it. So, this was a factor of x economic improvement. And now you can go home and think about what was the improvement, right? Uh I think there's a talk about evals. Uh so maybe you should check the talk about agent aas and so on. So with this beware of snake oil we see it all day on LinkedIn. Not everything is uh is gold. So thank you very much.

**[25:01](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1501s)** [applause] >> Yeah. Thank thank you Sebastian for this talk and you're sharing your thoughts with us. We have two questions in the talks chat. Um the first one when open data is the major source is the service of this data no longer important after the data was added to a proprietary model. >> Is it the right room? >> Uh it is yeah that's what someone was wondering. >> Can you ask I mean probably I can find an answer but it does not Maybe whoever posted the question might want to rephrase it and post it again in

**[25:49](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1549s)** the talk. >> Is is there is somebody here in the in the audience who posted this question >> or online? Either way, I will refresh and see if um you can clarify. >> Yeah. >> Um we have another question is just more general. Do you think that usage increases exponential? >> Yes. Yeah. Good. Thank you. Well [applause] all right. Yeah, I guess and like um or whoever like post the other question. >> I mean, is there a question here in the audience? We have a microphone. I think >> uh we prefer to have it on the uh talk so that it's recorded. >> I'm the speaker. Is there a question? [laughter] you might want to if if there's no more

**[26:38](https://www.youtube.com/watch?v=NxxXpmXa3ws&t=1598s)** questions I guess you can always just like um in the reach out to Sebastian as well >> and again thank you for your talk sharing your insights and then in 10 minutes we will resume again in this room with another talk um about the next talk wait a second I want to read it out properly um that we have in this one is where's that? Um yeah um well it's in the program it's in the room right thank you just another applause and we'll see it >> thank you [applause]
