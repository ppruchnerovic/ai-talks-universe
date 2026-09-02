---
id: AHePPIVx31s
title: "Don’t call your LLM too often! How to build your dialog graph with confidence and sleep at night."
slug: dont-call-your-llm-too-often-how-to-build-your-dialog-graph
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Evgeniya Ovchinnikova"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-04T22:20:41Z
video_id: AHePPIVx31s
url: https://www.youtube.com/watch?v=AHePPIVx31s
youtube_url: https://www.youtube.com/watch?v=AHePPIVx31s
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Don’t call your LLM too often! How to build your dialog graph with confidence and sleep at night.

**Evgeniya Ovchinnikova**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=AHePPIVx31s) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Evgeniya Ovchinnikova and Andrei Beliankou reveal how to replace unpredictable LLM prompt chains with explicit dialog graphs and rigorous tracing to reduce costs and increase system reliability.

Speakers:
Evgeniya Ovchinnikova, Andrei Beliankou

Description:
Large Language Model (LLM) integration in corporate environments often leads to excessive operational costs and system inefficiencies due to redundant API calls and complex, looping dialogue graphs. These issues frequently emerge when systems evolve from simple prototypes into production environments without rigorous observability, resulting in "death paths" or infinite loops where competing evaluation checks—such as faithfulness versus hallucination rates—force the model into repetitive regeneration cycles.

To mitigate these inefficiencies, a structured approach to dialogue graph optimization is employed. This involves implementing observability tools like Langfuse, Arize Phoenix, or MLflow to trace individual spans, track request inputs and outputs, and analyze cost breakdowns. By analyzing these traces, developers can identify redundant paths and restructure the dialogue graph. Optimization techniques include implementing a routing layer to bypass the retrieval process for simple queries (e.g., greetings or out-of-scope questions), disambiguating queries before retrieval to avoid irrelevant document searches, and summarizing conversational history to reduce token consumption.

The effectiveness of these optimizations is measured by comparing a "redundant graph" against a "clean graph" using a golden dataset. Success is evaluated through a trade-off between routing quality—measured by the number of LLM and database calls and the depth of the graph—and outcome quality, which includes metrics for groundedness, usefulness, and correctness. This methodology allows for the reduction of latency and cost while maintaining the integrity of the final response, ensuring that LLM calls are only executed when necessary for the specific intent of the user query.

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

*4,623 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=AHePPIVx31s&t=5s)** Good morning everyone. Welcome here for the first talk of this day. Third day still fresh and energized. And you may know Eon in this red colors as a company first uh selling electricity across Europe. It is the probably first idea you have in your mind or an old hardware company managing a lot of energy networks replacing fuses uh climbing pylons and doing a lot of uh hardware stuff. But actually nowadays AON is more represented in the cyber space uh because we have to manage somehow this infrastructure and the infrastructure got smarter with every day. We get smart meters. We can offer a lot of um plans for our customers. Cheaper, more expensive, but more stable. Uh

**[0:55](https://www.youtube.com/watch?v=AHePPIVx31s&t=55s)** reliability is a very interesting topic because we have multiple suppliers on the market and everybody can sell the electricity to the grid. You need to think about the congestion problems when uh at some point you have uh our producted state and you need more consumption somewhere else uh hundreds kilometers uh away and all these problems match actually um very well on the uh topics we would like to present uh you today. Uh the topics uh for today are uh how we can manage the load uh in this world uh information load for the customers and for the uh employees of uh eons and one of the very important topics here how to do it efficiently.

**[1:42](https://www.youtube.com/watch?v=AHePPIVx31s&t=102s)** The efficiency means you don't have to waste your resources. Eon is very cautious about not producing more and selling more but uh doing it um environmentally friendly. uh that's why we don't want to call our LLMs too often and sleep well at night uh for these reasons. If we look at the um last years uh meanwhile uh four years back um LMS pioneered a very interesting class of applications. We do not [snorts] take uh seriously the necessity of training a new classification model for uh customer feedback text for example or we do not provide our custom models for um extraction of personal information uh

**[2:32](https://www.youtube.com/watch?v=AHePPIVx31s&t=152s)** from uh texts we get every day in the emails or um in the transcribed voice messages. We uh do not try to uh write uh emails uh blocks for the customer support. Uh we uh all delegated it to some cryptical model which lives somewhere in the cloud and we aim for the newest one always through the information there hope for the best and get some result. But the reality is uh in this shiny world uh very simple uh this gets very expensive and uh after four years we have a very clear statement the eye cannot burn more money in the real uh sense of this world than it saves uh in the end.

**[3:21](https://www.youtube.com/watch?v=AHePPIVx31s&t=201s)** Um in the last four years uh we went uh through a very uh clear evolution uh starting in the uh 2023 with a very simple rack applications uh we took uh models at that time it was um opent 3.5 family we took a lot of code from Microsoft Eon is a Microsoft shop to biggest extent and our 90% all of of all our code is running in the Microsoft code. We [snorts] used a lot of uh predefined path u on the Asia cloud using for example document intelligence and AI search and not bothering with other uh vector databases and we had a lot of uh chaptt like um

**[4:12](https://www.youtube.com/watch?v=AHePPIVx31s&t=252s)** functionality for um internal users of us um not for the customers. Yon does not offer any digital solutions of this kind to the outside market but we automate our internal uh work a lot. And then we went uh next year to uh the point where we battled a lot with uh external sources not only using the sources provided in the PDF documents uh with very simple injection pipelines or uh the model knowledge. uh we tried to give uh the chance to the model to learn from our shareepoints for example and in a big big corporation it is not easy to get all the permissions and combine all the uh sides of shareepoint to one u big mash another pain was uh definitely

**[5:01](https://www.youtube.com/watch?v=AHePPIVx31s&t=301s)** handling non-English input uh we have Hungarian c uh customers we have Romanian customers we have uh definitely uh people from Sweden and Italy and it uh made our life uh much more complicated and uh having learned that uh Jenny is laughing much more complicated was her work working with Hungarian customers. [snorts] Um um the next year was actually uh the idea of uh doing uh not only uh single application but combining it all into uh backends which can be called from anywhere and custom front ends uh were a very important step where we uh offered centralized um

**[5:51](https://www.youtube.com/watch?v=AHePPIVx31s&t=351s)** services across um even for uh people who would like to build their own uh information retrieval solution and for that we had our EI hub hosting uh very different LLMs uh behind it. Uh the gen architecture from that uh made us uh cautious that we do not need um to only give access to the models but uh give all this stack and make uh some elements of this stack inevitable if you build new application. And I would like to uh point your attention to uh observability today because it is a point which is uh mostly neglected. If you build a fresh PC, you look at your logs, you try to understand what is happening. But in the

**[6:40](https://www.youtube.com/watch?v=AHePPIVx31s&t=400s)** end uh the system evolves and today I and my colleague Jenny will show you mostly how this evolved system can look like. uh how bad things happened to us. Um these systems were built overnight and then evolved over month and then landed in a situation where they were not efficient anymore and uh how we circumvented a couple of problems. Uh talking about the architecture retrieval and evaluation we can look at the generalized architecture of an retrieval system at um Eon. It is not one specific project. It is part of the architectural board. All of you where uh we can see that we uh tackle multiple

**[7:29](https://www.youtube.com/watch?v=AHePPIVx31s&t=449s)** sources uh uh in two phases. Uh the runtime where we get uh answers generated um on the bottom of the slide. And actually the whole magic happens uh previously when you extract uh data from different sources running it in batches for example on um data bricks or in uh custom pipelines in our kubernetes clusters. Uh and as usual uh looking uh at the bottom and the green bar uh you see the magic word langfuse the uh mostly used solution for observability uh in our uh in-house u solutions. It came up not um from a certain year it was a learning that without a system for um this functionality you cannot

**[8:19](https://www.youtube.com/watch?v=AHePPIVx31s&t=499s)** understand what happens uh to your system. Lenfuse is not necessarily one solution. And something bad happened to our video signal. I can entertain you in these two minutes telling you jokes about how the cockpits are but the signal is back. Um and uh Lenfus is not only the one solution I can show you very quick uh commercial overview uh for that starting starting with um OPIC uh which is a very

**[9:11](https://www.youtube.com/watch?v=AHePPIVx31s&t=551s)** widespread solution in our on the UK market. Um Eon next um and Eon UK use this uh cloud provider for observability a lot. We'll be talking about the functionality um on the next slide. Uh a very reliable partner for us if you are not concerned with storing your data uh definitely in the European region and you can outsource to uh the U which is possible for our UK um departments. The next very uh widespread solution is definitely um langu uh open source solution with a big um office in Berlin. You can talk to these people directly. They are approachable and um they went actually did the exit a

**[10:03](https://www.youtube.com/watch?v=AHePPIVx31s&t=603s)** couple of month ago very successfully and were bought by uh Click House um after they reviewed all the architecture to um the Click House u back end. And the next one is uh the solution which is probably known to everybody in this room is um MLflow. If you have a datab bricks account or you have ML studio running somewhere and do not want to have a third dependency again go for extended functionality of MLflow. But those were commercials um of the systems. Let's look at what is important actually for us as uh people who operate these systems. First of all, we do want to understand how the input and output

**[10:51](https://www.youtube.com/watch?v=AHePPIVx31s&t=651s)** of the LLM looks like tracing and tracking of single uh spans and um requests. We do want to annotate every span uh if we would like if they are problematic to custom data sets and run experiments on them. Calculate scores. One of the examples for this course is on the left and definitely you would like to compare after a deployment the performance of your system based off the predefined golden data set uploaded to this uh tool. You can manage your prompts. Mostly we do it on the code side and synchronize it to the um UI of u length views uh to enable our nonat uh coding uh affiliated people uh to do the experimentation on the length use UI and

**[11:41](https://www.youtube.com/watch?v=AHePPIVx31s&t=701s)** a very important thing for the management is actually the cost breakdown uh because you don't understand your costs for the LLM or specific path uh for optimization if you look only on the Asia uh coast panel But uh let's look now at the things which can definitely go bad uh in the system. These two examples I will be showing you um now are not created from scratch. I mean nobody would uh go into uh this situation willingly. But if you do it in a team which evolves and new people come in and you don't look at the behavior in the production, sometimes you can get a situation when uh you try to generate an answer and then you run um obvious checks in parallel. In this

**[12:30](https://www.youtube.com/watch?v=AHePPIVx31s&t=750s)** um depicted case, you have the uh check for faithfulness, how uh trustworthy your answer is, the correctness if you can actually compare it to the golden uh truth in this case, and the hallucination rate. And understandably, if you would like to force your generation into state to give you more details, uh the hallucination rate um rise up because the model gets creative. And if you force it to write more text, it writes it. but uh not necessarily based on the text. In this case uh you may uh end up with the endless loop. The loop is definitely not endless because you have u some retry count and you exit after five um uh times calling your model but you end up with a um situation where one check

**[13:20](https://www.youtube.com/watch?v=AHePPIVx31s&t=800s)** with one prompt forces to do the opposite as uh the other check. In this case, we have the trade-off between the hallucinations and faithfulness. Another example could be uh if you do not differentiate the error mitigation uh techniques here and uh in uh all the uh consequent checks um after the generation you always exit if your check fails after some time of um retries and your user and badly your logging system does not understand what the point where you um exited. Um how to fix this state? Fixing this state means that uh we definitely need to observe the system and see what

**[14:10](https://www.youtube.com/watch?v=AHePPIVx31s&t=850s)** happens on the trace level and then handle it. How we can handle Jenny will explain you in two minutes. >> Is it working? >> Somehow not. >> Yeah. So as Andre has already mentioned, we have various uh project related to different drug systems. Uh so in this graph I show more or less the possible issues that Andre has already discussed in details and basically to tackle it practically we need to first formulate the issue. So basically that the long dialogue graphs might accumulate various pathologists such as death path or uh infinite loops all that Andre has already discussed and what we want is actually to reduce those graphs by adjusting maybe some thresholds for

**[14:57](https://www.youtube.com/watch?v=AHePPIVx31s&t=897s)** evaluation or restructuring the node system but before this we need to ask us several questions. So first of all if this graph should happen at all if uh in this way. So if you need the retrieval at all because for example there are often some questions not a questions but queries from the users like for example hello or some uh polite form or some mal for questions like what is and this can actually be a problem because in our early systems when we always did a retrieval because well it's right we need to retrieve the documents. Exactly. this what is was uh working very badly because we had did retrieve some documents and there was just some very weird answers. Uh it can also be a question that more complex case for example uh we need to disambigue the question because for example if in a system we have uh information about

**[15:44](https://www.youtube.com/watch?v=AHePPIVx31s&t=944s)** several departments and the question about please tell us about the traveling guidelines. Uh the question is okay generally but uh exactly this system should first understand about which department it goes in. So it should also ask the question so please make it uh more precise or there can be also some questions that are certainly not about our documents and they those would require for example web search. Uh it can be a question like what is the weather today and it's obvious that we also don't need to do the retrieval and we have different systems. uh some would contain web search, some would not. Uh if it does contain it, we can go in that direction. If it doesn't, then we should uh just finish the graph and say, well, sorry, I don't uh have this information. Another question is how much history or

**[16:36](https://www.youtube.com/watch?v=AHePPIVx31s&t=996s)** conversational conversational context we should use if uh because it is very token consuming. If you have a long history, maybe we should use only last several sentences. Maybe we should summarize it. Maybe we can also check the query and then we would know that it doesn't have to consider the history at all. For example, if it is again just thank you. Okay, thank you. we don't need a history for this or we know that the new question doesn't have anything to do with the previous one because some users are uh working just in one chat and is actually very confusing for them uh when the history is too much present in the chat because we often had also questions for example if I start a new chat I have this answer but if I somehow uh do it in the old chat it's completely different answer and of course yeah there is a question

**[17:23](https://www.youtube.com/watch?v=AHePPIVx31s&t=1043s)** of how we do the quality check for the answers. Uh how uh how high is the threshold for the evaluation? Uh how good basically the answer should be and it can also be considered differently because for example correctness we have a example answer but it actually can also be correct when the answer is quite different because the user who created this data set uh didn't think of a different answer based on the on the document base. And when we consider considered all of this um we can start creating a new cleaner graph uh by tweaking all those thresholds as well as restructuring the nodes. Here for example we see that for certain questions we would just go directly to the answer using LLM and without executing all of the uh graph with the database calls that are also

**[18:13](https://www.youtube.com/watch?v=AHePPIVx31s&t=1093s)** actually very time consuming and expensive. And so our method would be keeping the redundant graph and compares certain metrics for the redundant graph and for different uh options for the clean graph. Uh so basically we did it automatically partially uh using something like uh auto research uh uh we had some skill files that would adjust some parameters of the graph and uh so when we have the answer first we need to evaluate like in any ra system because evaluation basically uh defines the success of our project uh how good the answer is if it is correct if it is well grounded if there are hallucinations and uh if it is actually useful because it can be perfectly based on the documents but uh not really on the point

**[19:01](https://www.youtube.com/watch?v=AHePPIVx31s&t=1141s)** to the question. Uh then of course there is a question of latency efficiency depending of the use case the answer should be it is crucial that the answer is fast and our users not getting annoyed for our system it's very important that the answer is really thorough and thoughtful and then they can also wait for five minutes because the before the answer is there but exactly for our use case it is also important to have a good routing quality basically that is something that we are going to evaluate here so how many uh data path are there, how how deep the graph is, how many LLM or database calls uh we had and basically so here we evalate at each experiment step our outcome quality versus the rooting quality. if uh some reductions in the

**[19:51](https://www.youtube.com/watch?v=AHePPIVx31s&t=1191s)** graphs are affecting our results in a better or worse way because we can uh reduce the graph completely. It will be very fast and nice but the answer quality will be horrible. And then would like to show just a very small demo. Basically it is exactly where we compare. Sorry I don't see my mouse. Uh yeah. Oh sorry it's now it's here. I'm sorry. Yeah. So uh right now here we just use use just more or less uh generic uh Jupyter notebooks because for different projects we use different obser observability systems like lenfuse opic and ML um flow as Andre said and here basically we can see that uh when we run

**[20:41](https://www.youtube.com/watch?v=AHePPIVx31s&t=1241s)** it we uh execute our graphs uh and we wait a second uh we execute it and I think my token has expired, but we'll still be able to see something. Wait a second. Deos as usual. Sorry. Yeah, I can show it. And here before the token has expired, it was working. Um, yeah, I can show you the result then. Uh so basically it uh builds our graphs and we get uh such tables. Uh here we see the query uh how uh and the comparison of the clean and redundant graph. So

**[21:30](https://www.youtube.com/watch?v=AHePPIVx31s&t=1290s)** basically we can see how many retrials there were how many generations there were and um uh their LLM calls. uh for example in many cases it's going to be the same uh because uh maybe the questions are straightforward or too complex that is why here for example we have the same LLM calls and but in this case we see that we have one uh three LLM calls which can also already be um a lot of time saved then we can also build the graphs that was actually doing the note that didn't work because my token has expired and uh yeah so here we see for example that for clean and for redundant graph it was the same because the question was very ambiguous. But in this case for example, we can see that actually the cleaning graph didn't do too many checks and

**[22:18](https://www.youtube.com/watch?v=AHePPIVx31s&t=1338s)** didn't go into the loops because the question was answer was good enough and the redundant graph had built already a lot of uh looping uh trying to improve the answer that was already good enough. And basically in this way uh we can continue and see with different parameters um how it works. And yes, so in this case we continue developing our graphs and uh uh we actually so it sounds a bit theoretical but it is actually the approach uh that we use in various uh project related to our customer emails or some chatbots that we use for our customers with the internal systems or some internal documents that they have.

**[23:07](https://www.youtube.com/watch?v=AHePPIVx31s&t=1387s)** So yeah, thank you very much. [applause] >> So super nicely done. Now thank you for the nice talk. I think there's your LinkedIn. So [snorts] >> feel free to connect with the speakers or also feel free to pick up the speakers after that for like um like simply asking a question personal. So we have some question already there at talks.pyon.de. So I will start now with the first question and this is a side question. Which lang use version do you use the self-hosted one? If yes, what is your experience regarding the cost of it? I can't answer this question because I

**[23:56](https://www.youtube.com/watch?v=AHePPIVx31s&t=1436s)** was a lot concerned with different um installations exactly of length views. Currently we are in the middle of a migration between the second and third generation. It is not very straightforward because of this big architectural change. Um I would say that it is affordable both in uh cloud and uh self-hosted uh scenario. Uh we are happy with that. Uh the only problem is that you need a dedicated team who would look after uh this installation. And that's why we uh definitely would like to centralize that. Uh not every team needs its own installation of landfuse. Um we have uh now uh three bigger uh of them uh like the for example

**[24:46](https://www.youtube.com/watch?v=AHePPIVx31s&t=1486s)** installation of EDG uh EON um in Dutch langa and the centralized EDT installation for Eon um digital technology which is the hub of um technology for the whole uh EON and definitely a couple of widespread uh installation. The centralization here is um in my opinion the key. >> Super. Thank you for the answer. The next quite upvoted question would be do you try agentic architecture which overcomes the DHE approach completely? Type X >> the Atlantic architecture which all comes DHD

**[25:33](https://www.youtube.com/watch?v=AHePPIVx31s&t=1533s)** >> D H D A >> D okay directly craft okay >> um I mean we have u a lot of agentic components in the racks uh themselves um they decide uh on theirelves which part of the system needs to be called especially if you have um tasks uh in this case uh conversational task, retrieval task or actionable uh task as well. Yes. uh for information retrieval purely where you have especially different types of documents you can do it uh deterministically better in our opinion >> not led to the services >> it depend it's a little bit on the project because we also did some demo

**[26:21](https://www.youtube.com/watch?v=AHePPIVx31s&t=1581s)** it's not in a real project but uh where we didn't use only this vector search but also built um graph based on the uh on the data so we com combine the vector search and this graph uh since uh the document base had a lot of uh somehow interconnected documents and for build this graph we actually also used some agentic approach but usually it is u yeah the agentic part is mostly uh in the part uh after the documents are already there and processed >> super thank you for your answer the next question will be will you share your slides >> we will >> yes sorry Sorry. And um like pretext or >> Yeah, we've forgotten to upload them to

**[27:10](https://www.youtube.com/watch?v=AHePPIVx31s&t=1630s)** pretext. They will be available shortly after the talk. >> So I think you can also upload them to the discord channel and the slide channel. So maybe it's also easy to spot them. Thanks for uploading the slides. So the next question would be how do you tell what is a redundant graph? Did I understand it correctly that you look at the intermediary generations to figure out when a response would have been good enough without any additional LL large language models calls. >> What about the redundant graph? Uh so usually uh we just uh observe it for example in certain project we observed it in length views and we saw that there were a lot of calls uh before we set a good threshold for the number of attempts. Uh so uh for example we saw this uh infinite

**[27:58](https://www.youtube.com/watch?v=AHePPIVx31s&t=1678s)** uh in the graph uh or we saw that uh for example we go through the whole graph and still the answers to general uh that is why it means that probably it was some generic question and we didn't have to go through it completely but yes so I think the easiest way is to observe it and see if there were some loops that were taken too long or some executions that don't lead to anything. >> I see. Thank you. So, um, another question from your session name you call it as don't call your LL too often. Could you explain what it means? Are you referring to building a simple graph versus an redundant graph like simple versus redundant graph? >> Uh, yeah, it is the reference exactly to

**[28:45](https://www.youtube.com/watch?v=AHePPIVx31s&t=1725s)** this case that we try to make the amount of counts calls as less as possible. trying to build the optimal shorter graph uh in this uh specific case. Yes, >> another question. How did you measure correctness of the answer in the chat? Maybe longer graph graphs have better answers in the end was an assumption from the question Oscar. >> It is exactly our problem with the correction. As I said, exactly this step is uh the trickiest one because the groundedness for example is clear if it is based on the documents or not. uh or usefulness is also more or less clear but for the correctness we have some data sets where our users uh say what they expect but yeah as I said often it is not correct actually what they expect because they don't know all hundreds of

**[29:33](https://www.youtube.com/watch?v=AHePPIVx31s&t=1773s)** documents in the database and um yeah probably there are some documents that actually answer the questions better than they expect on the documents they think of uh that is exactly these parameters what we use evalation but uh cautiously. >> The last question will be do you run any component level evolation of a graph or are you evol or are your evalations mostly targeting end to end quality? It is a very tricky question because we are currently trying to modularize these um approaches and we have tests for uh rack um components specifically

**[30:24](https://www.youtube.com/watch?v=AHePPIVx31s&t=1824s)** uh if additional dialog component is employed uh then it will be an end to end test. on the architectural diagram we showed you um in the middle slide. Uh you probably saw the rack as an extendable component and we try to pre-est them uh let's say on the unit level but generally the acceptance test uh will be end to end uh having the friendly user group and then testing um from the front end uh to the retrieval uh back end um the 100% of the pipeline. So in the most cases we are talking about the end to end testing. >> Thank you for your answers. This was Jenny and Andre with their talk and I hope you as nasties can now sleep better at night. Thank you. >> Thank you. Thank you.
