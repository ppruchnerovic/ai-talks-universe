---
id: 0Mh271tYYmQ
title: "It Works on My Machine: Why LLM Apps Fail Users (Not Tests) [PyCon DE & PyData 2026]"
slug: it-works-on-my-machine-why-llm-apps-fail-users-not-tests
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Thomas Prexl", "Frank Rust"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:20:07Z
video_id: 0Mh271tYYmQ
youtube_url: https://www.youtube.com/watch?v=0Mh271tYYmQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# It Works on My Machine: Why LLM Apps Fail Users (Not Tests) [PyCon DE & PyData 2026]

**Thomas Prexl, Frank Rust**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0Mh271tYYmQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Thomas Prexl and Frank Rust reveal why LLM applications often pass every test yet still fail in production, and learn how to bridge the gap between evaluation metrics and actual user experience.

Speakers:
Thomas Prexl, Frank Rust

Description:
Large Language Model (LLM) applications often fail in production despite passing automated tests because of a gap between technical performance and user expectations. This failure typically manifests in three dimensions: expectations, where users compare specialized business tools to the versatile, conversational nature of consumer-grade APIs like ChatGPT; functional scope, where users attempt tasks outside the intended design; and operational stability, where latency and timeouts in the customer's specific tenant create unacceptable delays.

To address these issues, a user-centric development approach replaces traditional waterfall or agile models with a process focused on transparency and real-world data. The methodology begins by collecting a baseline of 100 or more real-world questions, including the expected answers and the specific source documents required for the response. To manage performance, Arize Phoenix (OPIC) is used to trace the LLM pipeline, allowing developers to pinpoint bottlenecks—such as distinguishing between slow data retrieval and slow model generation—and communicate these constraints to the customer.

Trust is established by explicitly defining the system's limitations and providing sample questions to guide user interaction. For Retrieval-Augmented Generation (RAG) systems, transparency is increased by providing direct links to source chunks and utilizing metadata filters to ensure the model retrieves information from the correct product version. Finally, adoption is driven by implementing "quick win" features that solve immediate pain points, such as voice-to-text maintenance reports or automated email translation, which integrate the LLM into the user's existing daily workflow.

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

*4,470 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=6s)** Well, when some of you are delivering or developing um LLM based applications, you probably know the drill. You develop, you test, you deploy. 10 minutes, 10 minutes later, customer calls. Ah, it's broken. Now before I get into that, let me give you some context and I don't want to give you any advertisement or something just for you to understand what we are doing. Um, this is what we have in mind. Our day job is to free companies from what we call digital business work. Right? If you're producing in Germany, your shop floor is basically full of

**[0:57](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=57s)** robots, but your administrative floor is typically full of humans doing robots work. And this is uh what we do just very briefly. Uh we do have a platform which is basically an fast API application. We basically treat everything as if we are a model ourself. We use some hugen, some Postgress, some S3 storage and we get kind of everything from customers, right? Dumps, databases, um, MCPS nowadays, the first agent to agent stuff. And we literally talk to any model as long as it exposes some sort of API and we talk to any front end um as long as it can talk to an API and

**[1:45](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=105s)** we can run on any infrastructure as long as it runs containers. Right? So our day-to-day job is understanding processes, understanding data and then most importantly understanding user experience. Our customers typically come to us when they think generative AI will be a long game. So they want to you know invest quite heavily into bringing their whole organization into that or if they have been disappointed by tools um because you know in a world where most people try to deliver off the shelf we basically do tailormade applications for companies. But enough about us. Let's get back to the problem. Working like this means we have our our users as part

**[2:36](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=156s)** of our testing process from the very beginning. Ideally, users look like that and are part of the software development process themselves. And of course, we have tests, various automated tests. But still back to topic, there's a call and people tell us the AI doesn't work. In the last two and a half years since we've been working on this topic, we have found three major dimensions of these problems that we want to talk to about. The first one is expectations. >> Sorry. Okay.

**[3:26](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=206s)** The second one is functional and the third one is operational. Now, now let me give you some examples of that. You know, John J just some real life experiences that we had in the past. The first one and also the oldest one is expectations and that we are working in a world where you know the whole hype was created by jet GPT. So we are com we are competing at least expectctions regarding with consumer level API. It's shiny. It does everything. It works for everyone and it always has an answer. Our reality though is

**[4:16](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=256s)** we do work on a specific set of use cases not on everything. We are optimized for a specific target group. And the reason why both these are true is we not only have to give an answer but we have to give an answer that's kind of always correct. Right? Otherwise it's not very useful for business applications. So still you know of course we need to manage expectations about what users can really get from a solution that is tailored to their data. Talking about data second part is functional.

**[5:05](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=305s)** Right? The problem with functional is we design for a specific reason. We have access to a specific set of data wherever it is and then the user tells us well you know you built this service agent for us that our service technicians are using. It's really great and now I ask it to do an email for marketing and it doesn't work. So either data was never available right because it was not in scope for what we did or and that's of course also true regardless if you have some connection to some you know in company data lake storage whatever um or some access to their CRM system or their ERP system

**[5:55](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=355s)** maybe it's temporarily not available so that's the functional that and the third part is operational. Even if everything else kind of works, we need to make sure that it works all of the time when the customer is using it. One example here is time, right? when you are using your coding uh system today, maybe you're used to sometimes minutes if not hours of letting you know your coding agent do stuff. But for example, if you're working in a hotline and you have customers calling,

**[6:43](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=403s)** so our customers have their customers calling them and they want to give an answer. That is not an answer. And people tell us, yeah, well, it takes one to two minutes, so I can't do that that that much small talk anymore on the phone. I need the answer quicker. And we tell them, well, we don't understand on my computer in our development setup, it is less than 10 seconds, right? In this very specific case, one of the reasons was that you know when it was running in the customer's tenant, their LLM provider suddenly had timeouts, right? 1 minute, 2 minutes, and then we were out of the game. So three major problems

**[7:36](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=456s)** with you know the tests are working but the customer says it's wrong. The one being that we have to manage expectations. The second one that we need to make sure that functionally everything is as expected. The third one is that we need to make sure that operationally it stays working. And how we do that that is what Frank will tell you now. So uh as Thomas uh mentioned um our goal when we started project is to somehow make the users happy using AI. Um when I started or when I studied informatics uh 25 years ago um our life as developers was quite easy. So maybe not easy but it was predictable. So we had waterfall

**[8:27](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=507s)** models and we had something like a complete complete plan what to do. We somehow knew our obstacles. Uh so it was like hiking with a map. We we knew what we what we uh what we are focusing on. Um but the problem with that uh is that waterfall models sounds great for developers uh but not so much for users. So typically we had uh our formal uh our formal specifications but they didn't meet the uh expectations of our users. This is why uh also some years ago agile development uh roles. So we we we had something which helped us to better connect to the users and to also make sure that we always can adapt to to changing uh user demands. So it was more

**[9:16](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=556s)** like hiking with a compass. you know your goal. You don't have a predefined plan, but at least it worked. Now we have AI and developing with AI and it feels more like you're now hiking in a fog without a compass and without a map. So what do I mean by that? We have instead of predictable software, we have nondeterministic LLMs. So instead of a predefined user interface where you know what your users are clicking or doing, you have something like a chatbot where people just type in whatever they like. And uh most uh uh importantly also for us uh you don't even know what kind of data requirements you have because you don't know what your users are

**[10:04](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=604s)** requesting. So your goal is that you are somehow a guide which leads through this process with the users and you do this um by giving them focus create trust and transparency and also ensure that the user experience is always great. So how do we do this? Sharpen your focus before we start coding. So before we start single line or before we start writing a single line of code uh we start collecting real world questions. So we talk to the users and tell them okay what kind of question do you are you looking uh to get answered what kind of answer are you looking for? So how we do this now hopefully this works uh I thought it's maybe more interesting to

**[10:52](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=652s)** do this in live setup. Uh so this is just a demo case uh or a demo data set but what we collect is really like what is the question for example what are the mandatory break times during your workday according to the aside gazette so it's a German law um then you note down what's the expected answer and this is also very important but this is where what we collect here you also tell the system okay this information needs to come uh from this specific uh um PDF about our site gazettes. So this is an example but this is what we do whenever we start a project. We collect 100 or more questions with the correct answers and also uh with the um sources where this information is coming from. So this

**[11:43](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=703s)** is the the first step you have. Then the second part is you need to focus on the most valuable feedback. So early on you identify your core group of users, your project team who is really willing to support you, who is maybe a power user later on and you work with them very closely and you tell them okay this is a joint cooperation between um us and whenever you use our uh our for example chatbot uh we collect uh the data. So what we do is we tell them okay um you know what um we have for example like this dashboard which we also share with the users all of the time. This is why we incorporate this into the front end. Uh you can see okay there are a lot

**[12:32](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=752s)** of you um messages we have the ratings and then you go with them through their feedback and you tell them okay you ask for the specific capacity of an iPhone 17. um you didn't get the answer you were looking for and you noted it also down here and then we try to explain okay why is this information not available or what might be done uh to improve the quality of the answers that's very important and that's why we do this uh several weeks uh in the first phase of the projects then and I think that's the next slide um for us. It's also very important to not only get the qualitative feedback from the users but also to understand

**[13:20](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=800s)** your bottlenecks as Thomas explained uh it is very crucial that the response time meets the user expectations and for that you need to understand what's really happening behind the scenes and I'm not sure who of you is let me jump here uh using OPIC opic uh is a nice frame uh software which we are ing where we trace uh all our projects or several projects where you can see okay there are a lot of uh questions uh and answers where we uh enabled the tracing. You can see the response times is also for uh the average uh response time is for the chats and what's more important for us and this also helps us a lot with uh or uh when we are talking to to to

**[14:10](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=850s)** customers about the performance. It also gives us an overview okay what process in this chain takes up how much time and as you can see okay detecting the language based on what the user typed in it's important for us to to answer in the correct language it's it's a it's not an LLM so it's very fast but we have the classification agent it's a small model uh you have your rack uh workflow and you can see okay the retrieval of the data is very fast but the generation I need to scroll is uh taking up more time. So now you have the basis to talk to uh to your customers and tell them okay yeah I mean we optimized our uh our pipelines but the problem is your LLM

**[14:58](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=898s)** provider is not fast enough for uh generating the response. So this is on OPIC and uh as mentioned this helps us uh really to to um also understand where our bottlenecks are. So what we typically then do is uh beside the profiling we select different models maybe running on a specific GPU server which is uh at your customer site or finding other models and uh if needed also optimize um the retrieval process. So um the next thing is um that we uh need to build trust and create transparency. What do we mean by that? Um and I think this is maybe obvious but it's very important. Tell upfront what

**[15:47](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=947s)** you can't do. So tell them what kind of data is not available. Tell them what kind of questions you will not be able to answer because it's very important that you reduce the frustration in the beginning because everyone will be frustrated because the expectation for AI can do everything is really in everyone's head. tell them what you can't do and then tell them also what you can do and this is I think uh most of you who work with chat GPT interfaces uh or with chatbot interfaces know there's some kind of sample questions so that people get an understanding what kind of questions they can ask and also how to ask them because especially the rack process needs some kind of structure to to to get better results and then uh and that's also something

**[16:37](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=997s)** especially for the initial phase of the project working with the core team power to the people. What do we mean by that? Uh we mean uh that uh I mean let's uh let's start differently. Um if you're working for example on something like a rack based chatbot uh you start um uh putting a lot of data into your systems and the problem with company data is that it's a lot that it's unstructured that there's no metadata. So it's really a mess and it's like if you want to find data in there it's like finding a needle in a jar of needles. So it's very similar because maybe it's the specification of a product and this is the specification of a product B and the specification of a

**[17:24](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1044s)** product C. So it's very hard to find the right information and what we do is um and uh want to also highlight that is we provide whenever we have uh uh let's take a predefined uh question whenever there is a question for example is the iPhone water resistant we provide an answer and then uh and I think this all of you might know we also provide them links okay where is this information coming from what you see here are the different the specific chunks I mean this can be uh done better but this is how we currently do it and they can immediately see ah okay this is the information is coming from this document that's the right document but as mentioned before the problem is if you have a lot of documents for example um

**[18:13](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1093s)** and you can see it here you have iPhone 13 14 15 16 17 all the technical information it's very similar and if now someone is asking for specific information maybe you have hundreds of products, it's very hard to find the right information. But what we do and what you also need to show to the users because they really start to understanding the value of that. You show them, okay, we have specific metadata which we assign to your data. In this case, it's a product name and it is iPhone 15. So whenever they have a chat and they tell you okay um I I don't have the right information you tell them okay then please look the the filters we applied automatically are they fitting

**[19:01](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1141s)** this is to the specific product you were looking for or for the specific uh part you were looking uh or searching for information and this I mean even if it's very technical but it helps to discuss with the people okay what can we to improve this. And what maybe should be done more explicitly by allowing users to set a specific filter up front because this is done automatically but maybe they want this filter up front and u this helped us a lot especially because uh and we didn't expected that that people ask us I know my documents uh why can't I just put in the right metadata myself so this is also what we uh then provide to the power users okay if you have specific meta metadata you can assign it and then it's also

**[19:50](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1190s)** available for the automatic furthers later on. So very powerful also uh for you to learn um also important uh and this is uh also about trust and transparency. Um uh in I mentioned in the beginning we are collecting a lot of questions and uh we have a baseline when we start the project and whenever we do a sprint review we also share with the whole team okay this is where we now stand we improved some things and so on. So it's basic uh but it helps again based on the questions you defined earlier to also uh manage expectations. So last but not least and I think this is for us at least uh the most uh interesting learning we had um we were

**[20:40](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1240s)** focusing on our main task. So something like okay we have questions we need to provide the correct answers we need to improve the uh Rex system or the the connection to specific EIP systems to find the right information. But while talking to the users uh we also learned uh quite some some interesting things which also helps us to uh to uh yeah convince more users of this solution and important is that you also uh strive for quick ones. For example, people told us, "Okay, you know what? It's nice uh that you have this specific chatbot, but what I need to do is I need to email translate." So, it's I mean, we're all experts. I mean, it's the

**[21:28](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1288s)** pyon. Everyone of know of of us knows how to use and maybe write some scripts for that. But for them it's really like wait I can copy and paste my email somewhere and it formulates an answer in the language of the people who are uh requesting this information for me. It's like eyeopening. I mean they are doing this but it was very uh cumbersome and I mean it's trivial but uh we it is something we just provided and there are similar examples like document summaries, text reformatting or FAQ based answers. If you can do it and you can do things like this very easily with LLMs, just do it because they love you for it and uh they also uh then ensure that people are using the software.

**[22:18](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1338s)** Another example because it's also very nice. uh um we talked to to to to the uh company and they were telling us it's nice that you want to do this this knowledge chatbot for our service and support but you know what we don't have the data and we were asking okay why don't you have the data yeah because our maintenance guys when they do a fix they fix it and they typically I mean well hopefully they then go back to the PC or laptops and then create a maintenance report, write down what was the problem, how did you fix it, and what are the ferups. The reality is no one is doing that. So for them, it was really hard to use AI for for maintenance uh reports. Uh and we told them, okay, you know what, we just

**[23:06](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1386s)** create something very simple when your maintenance guys are driving back from um their their uh company. Um you just have a record button in this application where you just via voice recording you you just tell them okay yeah I was uh create a maintenance report I was visiting a client blah blah blah there was something broken this is the serial number and then we have a pre-formatted uh report which is uh filled out and then automatically sent to the backend system and it helped them a lot for us it was not so much work but uh this was one of the the killer features And uh this is a more advanced one. Uh and this is also what you can do because the customer helps you to build up this metadata information. Uh there they had

**[23:55](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1435s)** the problem that they had hundreds of products and uh the problem they are facing is okay we have uh also hundreds of characteristic. So when I am looking for a specific product we don't have a product information system. And we told them you know what we have the data. If you are looking for something like this, we can build this quite easily. So now if uh if you're typing in something like I'm looking for a product with a mechanical sensor and silver context which can be used in hazardous and atmospheres, the system applies those filters automatically and then tell you okay now we only have those products left. Do you want to filter it? And then you can see it down here uh based on other criteria. So it's a product finder which can easily be done based on the data we have.

**[24:42](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1482s)** So I think key takeaways uh at least from our side is um the chat GPT expectation is real plan for it. So as Thomas mentioned this is what you are facing every time you tell people you are implementing AI in a business environment. analyze what uh users actually ask. And um we mean not only by looking at some log files, but by talking to them and then build on that and try to figure out what to optimize and really focus on this one. If there are quick wins you can do, just chip it uh because this will drive the daily usage of the systems. All right, thank you very much so far. COME OUTSIDE.

**[25:29](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1529s)** >> [applause] >> THANK YOU. Now we go with the Q&A. Uh just from the how do you use the user feedback to improve the model? we we the model um if you mean uh if or if the question is if we retrain or fine-tune the models, we don't do that. What we do is we improve the whole chain, the whole pipeline. So maybe there are some prompts we can optimize or there are some filters we can apply which helps us to even uh to to better improve the the rack process. Next one.

**[26:19](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1579s)** What is the platform you are using to see the evaluation question and expected comments? Do you build it yourself? >> Ah yeah. Yeah. Sorry I didn't mention that. Um the platform is um is still OPIC or OPIC and they have a very good restp you can use. Uh so we really love this but the problem we are facing uh is that opic you cannot provide the nav interface to the users. This is why we use the restp to uh implement it here and then just get their results uh in our front end. So and this is just another example I didn't show before. We have also some different metrics. For example, if we test automatically, this is also coming from epic uh from OPIC. Um we have something like okay, we

**[27:08](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1628s)** measure the source accuracy um based on uh some rack questions or we have an LLM which judges the quality of the answers for specific questions. This is all done through opic but we integrate it in our interface so that we can show this um to the users. How do you test for conversations and the corresponding outcome? Do you have an LM mimic the user side with a system prompt? Uh yes. Um this is also coming back here. Uh this is exactly what we're doing here. So uh this L&M judge is really doing this. Okay. Is this the right answer? Maybe phrased differently. Is there some kind of hallucination in there? It's also based on this specific

**[27:57](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1677s)** Dutch which we use to analyze the the results from uh the models. >> And last one, I don't know if you want to reply. What is your go to platform to deploy production ready application? Uh what we use uh um is we use um containers uh for sure and uh we now have uh Kubernetes infrastructure for companies who are not willing to deploy to deploy their own solutions. Um so um if you like you can use the same containers in your Azure infrastructure or even on your local PC it's not a problem but for us it's Kubernetes uh based and we're running this by ourselves and provide the uh the interfaces then uh to the customers.

**[28:47](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1727s)** Another one analyze what the user ask and build on that. Isn't it dangerous giving how quick the market and the user experience and expectations changes? And there's a famous quote from uh Henry Ford. Uh if I would have asked the users what they want, they would have told me faster horses. And I mean somehow it also applies here when they tell you what they are looking or what kind of answers they are looking for. You need to be a bit a little bit careful. But at the same time you learn so much more by talking to them. So because sometimes they are asking some things and if you dig deeper and ask them why are they asking for the specific uh information you maybe find okay they are not looking

**[29:36](https://www.youtube.com/watch?v=0Mh271tYYmQ&t=1776s)** this information but maybe they want to solve another problem and we can solve this problem with LLMs which was not able uh or which were not able to be done before. >> Okay that's enough. So [laughter] >> thank you. Thank you.
