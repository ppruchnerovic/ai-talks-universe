---
id: t6oX0fbQHAY
title: "From Prompt to Production: How to use AI Code Assistants for Python Data Systems"
slug: from-prompt-to-production-how-to-use-ai-code-assistants-for
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Serhii Sokolenko"]
channel: "PyData"
duration_min: 49
published_at: 2026-08-04T22:21:39Z
video_id: t6oX0fbQHAY
url: https://www.youtube.com/watch?v=t6oX0fbQHAY
youtube_url: https://www.youtube.com/watch?v=t6oX0fbQHAY
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Agents & orchestration", "Classic ML & data science", "Coding assistants & agents", "Data engineering & MLOps", "Prompting & context engineering"]
transcript: true
---

# From Prompt to Production: How to use AI Code Assistants for Python Data Systems

**Serhii Sokolenko**

`PyData` · `PyData` · `2026` · `49 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=t6oX0fbQHAY) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Serhii Sokolenko demonstrate how to move beyond "vibe coding" to build production-ready Python data systems using a disciplined, engineering-first approach to AI code assistants.

Speakers:
Serhii Sokolenko

Description:
Building production-ready Python data systems with AI coding agents requires moving beyond linear prompting toward a structured framework of skills, personas, and state management. While LLMs can rapidly generate initial code, they often struggle with existing codebases, environment configurations, and the non-linear nature of debugging and deployment. To solve this, a system can be implemented using a combination of persona-based skills, a fuzzy state machine for workflow orchestration, and a specialized runtime environment.

The approach utilizes markdown-based skill files to define specific roles, such as a business analyst for requirement reviews or a data architect for structural validation. Instead of a simple chain of commands, a fuzzy state machine identifies the user's intent—such as deploying a hotfix versus building a new feature—and assesses the current state of the repository to determine the necessary path. This is complemented by hooks that monitor tool calls and suggest debugging utilities, such as increasing logging verbosity or limiting data samples, when a pipeline fails during its first execution.

In a practical application, this framework was used to build a data pipeline that fetches issues from a public GitHub repository using DLT and loads them into DuckDB. The process involved using the Tower platform to manage secrets via a built-in vault and deploying the application through a unified CLI. The final system expanded the pipeline to write data to Apache Iceberg and integrated a Discord webhook for real-time bug notifications. This methodology transforms AI agents from simple code generators into expert collaborators capable of maintaining architectural standards and operational reliability.

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

*5,745 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=6s)** Hello everyone. Uh I'm one of the co-founders of tower. Uh this is not a session about tower. This is a session about what happened after November 2025. Uh uh show of hands who knows what happened in 20 November 2025 like remember that day. Okay, I see a few hands raising. Uh, of course, Oppus 4.5 came out and since that day the life of uh, data engineers have changed dramatically because before November LLMs were crap and after November suddenly we were able to build pretty sophisticated data pipelines. So today's session is about not about how awesome cloud code is. It's pretty awesome and

**[0:57](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=57s)** we have concerns but it's still pretty awesome. Uh this session is about what else do we need as as a profession as data engineers people who need to process data who need to provide good quality data to their end users. What else do we need in addition to cloud code to um write good software? Uh I'm going to do a little bit of a switcheroo. Uh I'll apologize for this. Uh the majority of the content of this session was developed by Simon Rosenberger who I at this point would like to invite to the stage. Simon is uh one of my my friends and uh early employees of Tower. Uh actually if you look at some of our product requirements

**[1:45](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=105s)** documents in uh in Tower, you'll see Simon's name mentioned because he was the original user of Tower. He basically was the reason why we uh started the the startup. Uh by the way, for those of you who don't know what Tower is, uh we are a startup in the Berlin area um hiring building a platform as a service for Pythonic uh data apps. So I would like at this point maybe start transitioning the mic um to Simon. He is going to lead you through uh three parts. Um he's going to explain what these three parts are. Uh it's going to be a demo version uh portion of the uh of the session and a hands-on version of uh this tutorial. Uh my co-founder Brad is uh in the back

**[2:34](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=154s)** of the of the room. Uh I am also going to stay in the room and help all of you. So the three of us, Simon on stage, me uh in the room, Brad in the room will all be helping you with the hands-on portion of this tutorial. Uh at this point, Simon, why don't you take away and uh and tell us more how to get from prom to production? >> Yeah, Siri, thank you for the kind introduction. Um as people are still coming in, uh yeah, I think there's still plenty of space over there. Um yeah, we're going to talk about code agents um in data engineering today. And really my goal for this session for the next 99 minutes uh 90

**[3:23](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=203s)** minutes is for all of you to walk out here and have the feeling you got some more tools at your fingertips to be more effective using AI coding agents. Um we're going to divide the section into three parts. Um for one, this is going to be very short. We're going to dive into some like of the underlying concepts that we'll be working with today. Then I'll spend some time uh walking through a like specific example of how to apply these. And then the third part of the session which is like the last 45 minutes uh is actually meant for you to apply these skills and uh the techniques

**[4:13](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=253s)** um to a specific problem. So I hope you brought your laptop. Um we do have all the tools uh ready for you. Uh so don't worry and let's dive straight in. Um before we get going with the content, I want to get like a quick show of hands. Uh who of you is in the data engineering space or considers themselves a data engineer? Yeah, it's about half of it. A bit more probably. Okay. And who of you sympathizes very well with this image and the experience that's depicted in this image? Yeah, that's definitely even more than

**[5:01](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=301s)** the the data engineers in the room. So, this is a clear problem, right? Uh AI coding agents are super powerful. They allow us to get from zero to one in no time. Uh, it all looks fancy and bright, but at the end of the day, we still find ourselves spending almost as much time as we've as we've always did until we arrive here at the right at something that really works. And today, um, we'll hopefully learn how to change that. um how can we move from prompt to something that is actually resilient, reliable and production ready um with a few tweaks. Um Sahi already covered this part. Uh

**[5:50](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=350s)** I'm a forward deployed engineer at tower. Uh I used to be a data engineer before that and um tower itself uh is something that we quickly going to look into now. Um, I'm briefly going to give you a demo of the platform, not to advertise it, but to give you a sense of why uh it makes sense to use tower in conjunction with [snorts] coding agents. So, let's jump over here. Um [snorts] this is the platform. Um you will create an account uh a free account uh later to participate in the in the actual coding part. Um what do we have here? Tower is a platform to run Pythonic data apps. Um so we have apps in here. Um they run some of them

**[6:41](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=401s)** errored some of them were successful. Looks a bit like GitHub actions if you've used that. Uh but it is much more than that. Um, we have builtin storage so you can run your Python data pipelines, data transformations, dashboards, um, and query data from a storage repository directly adjacent to your runtime. Um, we have different environments. We have secrets built in. And the beauty of that is, um, we'll see that later. All of these apps um run locally just as if they run on tower in the cloud because it's all bundled into

**[7:31](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=451s)** the same runtime like the secrets vault um the lock streaming um observability it's all bundled together. So it's literally a oneline CLI command to deploy what's just been running on your machine into the cloud. Um obviously it comes with a CLI that agents understand really well. Um so that works uh that works. Um that was the platform intro. Um before we get into uh how we actually work with it um some conceptual background. So coding agents make us faster but how can they make us better right? How can we transform Claude and all the work trees from a team of workh horses to a team of

**[8:19](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=499s)** experts that doesn't make us faster but does that gets us to the to the moon literally. Um so the cool thing is we do have the like the plumbing that we need already in place. We have um code generation from the LLM. We have memory and context from the agent memory. Um, the agent can take actions on our operating system using tools and we can even give specific instructions to the agent using skills. Um, so what's missing on this is like this is this is all very linear, right? we can like chain those tools and those skills together to get like from A to B,

**[9:09](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=549s)** but the reality isn't as linear. We run into issues that we didn't expect. We have to take different turns in our development workflow and all of this is not really built for that. Um, and it's also kind of like very it captures our own perspectives on how we going to solve things. So there's two tweaks to look at the problem from a slightly different angle. So what if we were to give our agents different personalities? Um, for example, if we're in um in data engineering, um, I mean, in reality, you would involve an opinion from a data architect, a business analyst to make

**[9:59](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=599s)** sure that whatever pipelines, dashboards, etc. you're building uh, are actually meeting requirements, security requirements, business requirements, etc. Um, so that's something that we going to weave into our agent setup. And the second piece is what people usually experience is if you work with coding agents on a blank slate, it works incredibly well. If you onboard a coding agent onto an existing codebase, um, problems start occur because your coding agent usually doesn't have the notion of a state like which state is your codebase currently in. And also it doesn't really question

**[10:48](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=648s)** your intention like are you here to just like write a hot fix? Are you here to add a new feature? Are you here to refactor stuff? Um, but all of this should factor in how the ensuing development workflow evolves, right? If you just want to build a hot fix, there's no need to do like extensive planning, like chances are that you exactly know what you want to do. Um, but if you want to build a new feature, you probably want to like involve more of those like additional perspectives from a platform engineer, from an architect etc. Um there's a lot of talking uh on those like abstract concepts. Uh so I would say without further ado um let's actually dive in. Um there is this

**[11:39](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=699s)** website. So if you go to tower.dev/blog dev/blog which all of you should do now. Um there is uh a blog post that is not a blog post but that just shows these two links to the repo that we're going to be using and to the discord channel. Um so the discord channel is over here. Um so join that. Um there you will find all the links that you will need later. Um, and while you do that, um, I will get like going with the actual demonstration. Um, and for that jump over to this repo.

**[12:30](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=750s)** So, what are we going to do together? Um, this is a repo. There is a very simple data pipeline in there already. And what it does is it fetches all issues from enthropics cla public repo. Um so we want to do two things with that. First we want to get this existing pipeline running and then we want to build like a small data application on top that notifies us uh whenever a new buck ticket is filed. It's like a it's it's a toy example of what could work really well inside an organization where you say, "Okay, like I always want to stay on top of of buck tickets um to keep my customers happy. Um we're going to use this public repo because it's uh

**[13:18](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=798s)** easier to to access for everyone. Um um exactly. So what I'm going to do now is I'm going to clone this repo and then run the pipeline without giving all these skills, tools, and hooks to my coding agent. We'll see how that evolves and then we'll switch gears uh with all the additional tooling. Okay. Um, and by the way, um, after this like demo session right now, we'll also have like

**[14:05](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=845s)** a quick Q&A where you can ask like questions about what we're doing here. Um, also about tower in general. Um, we just wanted to make it more like condensed for people to ask questions. All right, there we go. I'm going to zoom in a little bit. Okay. Um. Whoops. Open a new terminal. Oops.

**[15:00](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=900s)** Cool. Um, so as I said, um, what we have in here is I hope you can all see that. Um, we have a single data pipeline. In this case, it's a DT pipeline that loads issues from cloud code repo into ductb. So, I'm going to launch cloud and oops, there we go. and tell it to run the pipeline and see uh how it behaves. So this is now like a plane like if you

**[15:50](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=950s)** would have just like signed up for cloud launch this on your IDE no skills no MCP servers whatsoever um and um yeah essentially start with a plain stupid agent. Um what you see is what happens. So it had no idea what's actually in this repo. So it started exploring. It found a pipeline. It wants to run it. It fails. Why does it fail? Because it has no clue how this entire environment is actually managed. In this case, we're using UV for dependency management. So there is no uh global Python to run it with. Um, and now it's like starting to think how can I fix this? Um, and so on. The next problem that we're probably

**[16:39](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=999s)** going to run into is that there are no secrets configured. Um, there is no safe way for the agent to configure secrets. Um, and then once we finally got the pipeline to run, um, we're going to struggle to actually get it deployed somewhere where we can run it on a schedule. [snorts] Um, luckily there is a solution to all of these problems. Um, so let's switch gears. Um, I'm going to go to the main branch and Oops. And the main branch comes with um, and that's what I want to spend a little bit of time on. Um, quite a bunch of skills um, and other markdown files. Well,

**[17:28](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1048s)** quick show of hands. Who knows what skills are in the context of coding agents and uh LMS in general? Okay, so yeah, we we're all talking the same language here. This is good. Um, so when I first started using skills, I treated them as recipes uh for completing workflows. Um, and there are still some of those recipe like skills in here. For example, a recipe to debug a data pipeline, a recipe to initialize a tower app. Um, but there's also other skills in here that are less recipe- like. They are more personaike. um for example like a business analyst that does a review of my uh plan of

**[18:18](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1098s)** building the pipeline or uh a data engineer review that has a much more thorough understanding of data engineering best practices. Um so we'll see how those going to be useful. Um the second piece that we talked about earlier and this is the this is the really interesting one is this um workflow skill which is no longer this linear workflow but it's a what I call like a fuzzy state machine. So it tries or like it identifies your intent like what do you want to do if you prompt this? Do you want to build a feature? Do you want to deploy a hot fix? Do you want to just investigate some data? Do you want to refactor? Um, and it combines that with the state in which

**[19:08](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1148s)** your repository is at the moment. Uh, so does it already have an app? Uh, does it have nothing at all? Does it have some code, but it's not um it's not bundled yet as in this case a tower app. So and depending on on where you are at the moment, it sends you down uh a uh yeah calibrated workflow. So without further ado, uh let's see how running the pipeline behaves [snorts] with this uh more tailored tooling. Oops. Make this a little bit smaller. run the pipeline. All right. Um,

**[20:01](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1201s)** okay. Um, it's checking the project state to understand where we're at. Um and uh as per this fuzzy state machine, it's seen okay there is some pipeline code in there but it's not readily bundled into a tower app. So I'm going to do that first. Um it's using the skill like in initialize a tower app. Uh while that's going uh it will realize that the tower MCP server is not running yet in the background. So we have to start it. There you go.

**[21:22](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1282s)** Yeah. So, Tower MCP server was not running. Um, it uses the tower MCP server to for example validate the configuration. Um, interestingly, it saw that uh there was a little bug in our config file. Um, we'll take a look at that in a second. Uh, so now it's running and this is now an interesting step because what what did it do? So, it tried to run the app which is the pipeline locally. Um, and there was a what looks like a failure. And we are using hooks in here uh that essentially hook into those individual tool and skill calls and um compare it

**[22:11](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1331s)** with the local state. In this case, it saw there hadn't been a historic run of the pipeline before. Um, so it notified the agent that hey we we might want to like add some debugging utilities if we run this for the first time. Um, and how is this useful? And I don't know how about you, but when I get to these like existing pipelines that I'm supposed to extend or fix, um I usually start by just looking at a sample of the data without running the whole thing because it's going to take forever and chances are that uh things are going to break anyways. So adding a bit of like limits and more verbose logging is always a good idea and that's exactly what uh what happens here. So yeah, let's uh go

**[23:01](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1381s)** ahead. Oops. [sighs] So it's using another skill here uh the debug pipeline skill uh which is essentially just telling it to hey make the logging more verbose and pull less data so that it gets faster. Let's see what happens. All right, we've gotten a little further. Um, still not looking great. Uh, but uh we're getting there. Uh, there was uh a rate limit [snorts] error, which is an interesting one. So, let's see what Claude's going to do with it.

**[23:50](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1430s)** Yeah. So it has correctly identified what the issue is. Uh because GitHub API is rate limited unless you use a token. Um any token would suffice here because it's a public repo at the end of the day. Um and this is uh yeah one of the advantages of tower is um we have a secrets vault built into the runtime. Uh so that means in the UI is this here we can create secrets like Claude has already created one for us uh with a placeholder value. Um so we can now go here um

**[24:38](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1478s)** pick our secret from one password put it in here [sighs] update and those secrets will be available both on the local runtime on our machine um and also later when we deploy this uh to the to the cloud. So it's telling us hey go to tower replace the token with the actual token value which we did. So ready to go. Running again. This time we shouldn't run into timeouts anymore. Um,

**[25:30](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1530s)** looks like we still did. Uh okay. Let's run again. Yeah. Okay. Um app completed successfully. That's good. Uh so we were actually able to complete the first part of uh our mission here which is to uh run the pipeline. But that was not the eventual goal, right? We wanted to get alerted when new pe when people file new bug tickets. Um so that's the next step. Uh it's suggesting to remove the debug

**[26:20](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1580s)** utilities again. So, let's wrap that up. Yes. Okay, it's all clean. Done. And so now it's asking us what we actually want to do. And what we want to do is uh next I would like to build an alerting system that writes issues to iceberg and tells me whenever a new bug ticket

**[27:14](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1634s)** was filed via Discord. Let's use Discord because it's super easy to integrate with uh web hooks. Let's see what it does. Um like last time when we prompted it, it was just like okay like we don't need to do extensive planning. We just want to run the pipeline was a very different intent from what we're doing right now. Um let's see. Yeah, so this is a feature request. So we are on our fuzzy state transition matrix uh at a very different place. Um so what it's going to do now it's going to make a plan like a mini plan. Um and then it's going to use those two persona skills like the business analyst and the data architect to make sure what we're planning here is

**[28:05](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1685s)** actually sane. And I found this to be quite helpful because I used to invest a lot of time in like refining product requirements documents and then throwing them over to the agent. Uh until I tried using those like very specific personas to give feedback on very specific sub aspects of these plans. uh makes them a lot more robust and also um yeah makes me think about things that I wouldn't have otherwise considered. Okay. Um it's come up with a plan. Uh we're going to use iceberg as a destination. Um and we're going to uh add an alert hook from Discord. So uh we're still waiting for the second agent

**[28:56](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1736s)** to complete. Okay, while it's doing that, we can already head over to Discord and create uh a web hook integrations. Um, web hooks, new web hook, copy web hook URL. There we go. Okay. Um, so based on the feedback, we've slightly revamped the plan. Uh it's found that there are

**[29:45](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1785s)** some additional dependencies that we need to add um and some cleanups that we need to do. Uh but overall uh this looks good. Um so let's build it. This time obviously takes a bit longer because uh there's more stuff to build. Um, what you can already do in the

**[30:36](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1836s)** meantime is you can go to app.ttowwer.dev and create an account for yourselves if you want to participate like in the second part of this tutorial session. Um, it's completely free to use like we give you free compute uh for today. Um and uh yeah then we're going to be faster later. Okay. Um the agent has advanced. Uh it has all the details and starts implementing Uh yes. Hello. All edits.

**[31:53](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=1913s)** Yeah, >> remain seated please. Um yes uh you can leave in case of emergency but otherwise please remain seated. There should be no walking during the talk. We can al I mean if if people if like we we could also say like we do a quick break like if people do want to leave like we don't want to force anyone to uh like sit here and do things you don't uh you're not interested Okay, looks like we've weeded out um the

**[33:22](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2002s)** crowd. out. Uh so excited to continue uh in a more intimate uh and more interactive setting. Um so what we're doing right now is um this is actually running. So I guess for the sake of this um we've gotten all the like underlying concepts in place. Um I would open this up now for like general questions on how these skills are composed, how the platform works. Um, and then I would say we transition into like getting everything up and running uh for you guys to try this out by yourselves.

**[34:09](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2049s)** Um, sounds good. Then I would say we're open for questions. Yeah. >> Um, so you can ask the questions through the talks punctu.pyon.da. the year. Um, there are no questions for now, but maybe someone has questions. Uh, yeah, and I will just hand the mic. Yeah, thanks so much for the um presentation and the demo. I just have a question. So from everything you have done the only thing that is different was the API key stored in toa right because I've not seen anything

**[35:00](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2100s)** different from what I do usually compared to what you have done >> and are you presenting to as a secret manager for for the project or what exactly because I I've not really gotten >> Yeah. No, that's a that's a that's a really good question. Um, and it's a very fair question because we haven't seen much than tower as a secrets manager at the moment. Um, but it is actually uh much more. So, let's like say we've like we're done with developing and this actually works. Um, then I can just like tell Claude uh deploy this. Um hopefully it's going to do this because and it's not going to object because we haven't finished the

**[35:47](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2147s)** development yet. But this is like a tower is like this endto-end platform. It's a runtime that runs on your machine but it the same thing runs also in the cloud. Um and in a normal setting uh you would like I don't know have to provision a lambda function, a Google cloud function um like EKS cluster maybe even uh if it's a heavier workload. Um and all of that is going to be abstracted away for you. So like the secrets management is only one part of it. Um does that answer your question? Um quick reminder please ask your question on talks pyon pd. >> Okay. So um for the deployment sometimes

**[36:39](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2199s)** I need to specify what I want to deploy. So normally I use like terraform or whatever to create my infrastructure. I manage my secret on terraform um vault can you connect to that because I don't want to move away from that I need to keep that because I can manage those things I have been managing them >> I can easily provision because I don't know what kind of infrastructure I going to use sometimes I just want to use kubernetes clusters eks sometimes I want to use nanda functions depending on the future of what I'm building so how do I >> sync that with tour. >> Um, so I think like what what are the people that you usually work with? Like um you have like an internal data team

**[37:27](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2247s)** that works on the infrastructure you provision or you are the data team. Okay. Yeah. So what what we usually try to do is to like simplify live for teams so that you like you now you already have like a terraform setup but uh most of the like other and smaller data teams out there uh they are not that advanced and this like this is where we come in and and help them. Yeah, I would say like why why don't like these are very very great questions and specific ones. Um like we can like

**[38:16](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2296s)** have a discussion down at the booth uh and go like in depth in in all of those like we're right next to the uh main auditorium. >> All right, there is the next question. Um have you tried other code harnesses like codeex or GitHub copilot? what were your experiences? >> Yes. Uh very good question. Uh comes very often. Um we've tried it and up until recently uh they were pretty I would say compatible with each other. Uh specifically uh hooks are at least as of last week things are moving fast. Uh only supported by cloud code. And I I actually found them to be

**[39:05](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2345s)** quite useful. Um in terms of yeah whether Opus is better than codeex um there was no not really a difference but like the way in which you can integrate all this like tooling around them is slightly better for claude at least in my experience. >> Uh thank you for the answer. Um how is the approach can be extended for machine learning use cases like for feature stores creating a features? >> Um yeah that that that's a very uh interesting question. So I would say like two things that you would need to have is like your feature store needs to have uh a CLI or

**[39:56](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2396s)** some way that an agent can interact with it and then um yeah go through your own workflow like what kind of perspectives do you usually take probably like a machine learning engineer or a statistician and then uh write like these persona skills and uh write some recipe skills uh so that the agent knows how to interact with your feature store and the underlying training process. Then I guess [snorts] yeah >> and there is another question uh how the standardization can be provided to have the same pattern across a company. >> Yeah. Um also very good question. So probably this will be answered in the ensuing like work that we're going to do

**[40:44](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2444s)** is this is literally just a bunch of markdown files in a GitHub repo. Uh so that can be shared across the entire company. >> Right. Thank you. Um yes there are no questions more. Do we have some questions? Um not. Yeah, >> cool. Um, if not, I would say >> no, we have one question. >> We have one more. Cool. >> Um, I just wanted to ask uh how was the procedure in order to create all these markdown files or the workflows? Do did you use cloud code as well to create them? >> Yeah. Um, so it was like uh I would say a very iterative development uh process. Um, of course the like the idea is um is

**[41:37](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2497s)** not new. Uh, there's like lots of uh repos out there who adopt a similar approach for front-end development, backend development. Um, and so this was the the brainchild came from somewhere else and then I just spent a day or two with claw together saying, "Hey, this is how my usual workflows look like. These are the perspectives I take. These are the um like steps I follow and like cast this into a harness of of skills. Cool. Yeah, perfect. Uh we're at 45 minutes. So we have 45 minutes left, I would say. Let's uh so we going to go uh around.

**[42:28](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2548s)** Um, there is also the Discord channel where you can ask questions. I'll be Whoops. I'll be monitoring it and there you go. Yeah, there you go. Um yeah, this is our Discord. Okay, lots of people uh on here already. Um special perk for those who stuck around. Uh for the part of this session, we will provide free cloud API tokens. Yay. Um,

**[43:21](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2601s)** [laughter] so, um, the links are all in here. Uh, we're going to walk around. Um, with 15 minutes to go, uh, we'll like do a cut, um, do a little final Q&A, um, slashdebrief. And if people feel really brave, uh, we can also do like a quick showand tell of what you've built. I'm pretty excited. I would say let's get cracking. minutes left. Um but more than 10 people

**[44:21](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2661s)** left uh which is great. Um and it was quite exciting to to walk around and see um what things are working for people and what things are not working. Um obviously we made a bit of a bold claim uh from prompt to production. Uh like um we're obviously not at production. It is still a rocky road. But uh yeah, the goal was to to give you guys um some tools to be more effective working with agents. Uh hopefully you can take the repo away and like build your own set of skills um out of it. Um I'm incredibly curious for feedback. So I mean if some of you like want to share the experience like how did you find it? Was it um did

**[45:11](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2711s)** it feel differently for you working with uh AI code agents that way? Did you think you you learned something new? Was it all um known to you before? Any any thoughts? No. Okay. Um that's fine, too. Um, we are I mean you're already part of our Discord server. Um, feel free to Yeah. Thank you. Um so uh let me repeat um I

**[46:00](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2760s)** hadn't been here from the very beginning so I don't know which instruction uh which introduction you gave but at the time being I'm not 100% sure what tower actually is. So I had seen the repo I had seen the skills but I mean this is not tower so >> um what does tower actually know do? What does it do from the data side does it do from the infrastructure side? Yeah. Um, a good question, especially since you haven't been here from the beginning. So, in in very simple terms, tower is a data platform behind an API. Uh, so both you and your agents and your our SDK can interact with tower as a data platform. That means it can run Python code for you. Um, it has also storage built in. So we have like part of tower is uh a

**[46:50](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2810s)** set of like or like iceberg storage where you can create your own tables. Um you can also run interactive apps on it meaning notebooks, dashboards etc. Um and you can do all of that with zero knowledge about the underlying infrastructure. Um the runtimes are serverless. The storage just looks like any other iceberg rest catalog if you want to use that. Um and you get all the observability in a single dashboard. Yeah, exactly. Yeah. >> Yeah. Uh so it it runs on AWS. Um, but

**[47:40](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2860s)** if you want to like run it in your AWS, uh, that also works. Yeah, we have self-hosted runners. Cool. Um, if there is are no further question. Yeah, there's one more question up there. You mean the the logs? >> Yeah. Um, so under the hood, um, we run like a Kubernetes cluster. That's where like the jobs that you run, uh, are getting executed and we, our control

**[48:29](https://www.youtube.com/watch?v=t6oX0fbQHAY&t=2909s)** plane listens to the logs of those pots and then streams it, uh, back to you. Cool. Um, for the next two days, we have a booth downstairs, uh, right next to the auditorium. Uh, there's coffee, uh, there's swag. Uh so uh yeah feel free to come by have a chat um give us feedback and yeah thanks a lot for being part of this session.
