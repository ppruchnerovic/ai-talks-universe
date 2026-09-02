---
id: zayHuvKVr34
title: "Simulating the World using SimPy: A practical Example [PyCon DE & PyData 2026]"
slug: simulating-the-world-using-simpy-a-practical-example-pycon
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 23
published_at: 2026-08-04T22:21:55Z
video_id: zayHuvKVr34
url: https://www.youtube.com/watch?v=zayHuvKVr34
youtube_url: https://www.youtube.com/watch?v=zayHuvKVr34
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science"]
transcript: true
---

# Simulating the World using SimPy: A practical Example [PyCon DE & PyData 2026]

**Speaker not identified**

`PyData` · `PyData` · `2026` · `23 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zayHuvKVr34) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Cloud Engineer Niklas demonstrate how to use SimPy to build reproducible, event-based simulations for testing complex systems and optimizing load-balancing algorithms.

Speakers:
Niklas

Description:
Explainable AI (XAI) addresses the "black box" problem in machine learning, where models may rely on spurious correlations—such as identifying a wolf based on snow in the background rather than the animal's features—to make predictions. To mitigate this, a structured framework distinguishes between interpretability (direct reading of model logic) and explainability (approximations of model behavior). The framework further categorizes analysis by model access (white box vs. black box), scope (global vs. local), and data type (tabular, image, and text).

For tabular data, global explainability focuses on feature ranking, effects, and interactions. SHAP (Shapley Additive Explanations) uses game theory to rank feature importance and visualize how specific values push predictions higher or lower via beeswarm plots. Feature effects are analyzed using Partial Dependence Plots (PDP) for average effects or Accumulated Local Effects (ALE) plots to handle correlated features. Local explainability identifies why a specific prediction occurred using SHAP waterfall plots or LIME (Local Interpretable Model-agnostic Explanations), which fits a local meta-model to the input. Counterfactual analysis, implemented via the DiCE package, functions as a "GPS navigator" to determine the minimum input changes required to achieve a different target outcome.

For image data, global analysis employs Testing with Concept Activation Vectors (TCAV) to determine if human-defined concepts, such as stripes, influence predictions using directional derivatives. Additionally, feature visualization reveals what a model learns at different layers, progressing from simple patterns to complex structures and specific objects.

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

*2,981 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=zayHuvKVr34&t=6s)** Thank you for the introduction. Um, you know, I want to present you the topic simulating the world using SimPy and I want to present you a practical example. So, first of all, as said, I'm Niklas, I'm cloud engineer and first time speaker, so please be kind. Um, just some small advertisement. I work at Innoactive. We are IT project center and they sponsored me to talk to you here. So, we are also hiring data engineers and machine learning, also cloud engineers if you want to work with me, maybe. Um, so, first some storytelling how I got to simulating it was, yeah, [snorts] about a year ago. I had to write my final thesis and

**[0:56](https://www.youtube.com/watch?v=zayHuvKVr34&t=56s)** cloud engineering I searched on topic and then we found load balancing. Um, you might think load balancing, that's not that interesting, but um, we have then thought about uh, what is load balancing and how we can improve it. Um, there are some new load balancing algorithm with self-regulating them and smart decision uh, smart decisions and controlling themselves and communication between the back ends and uh, and the load balancer. So, then how hard can it be and are there some implementations and that's why I began the investigation in simulation because there are nearly no implementations of

**[1:44](https://www.youtube.com/watch?v=zayHuvKVr34&t=104s)** this new algorithm or they are so widespreaded across different load balancers like Engine X, Envoy and so on that I have I can't compare them against each other. Um that's why I started simulating them. So, what is a simulation? Um a simulation is mostly a imitation of a real-world process and you cannot quite get it 100 100% quite done right, but you need but you have full control over the environment. And that's what that's what is that is the goal of simulation. You have to control over each component and you have control over each step and so you have also control over time.

**[2:33](https://www.youtube.com/watch?v=zayHuvKVr34&t=153s)** And the most critical thing when you want to evaluate something, it is repeatable. Um so, you have the same input, you have also the same output. And when I was searching for some simulation framework because I don't want to write it myself uh from the ground up, that was also an idea of mine, um but it's very complicated. Um I stumbled upon SimPy and SimPy is a process-based discrete event simulation framework based on standard Python. Has somebody of you used SimPy or heard ever of SimPy? Some of you, okay. That's great. So, you're a little bit familiar and when I make mistakes, please correct me.

**[3:23](https://www.youtube.com/watch?v=zayHuvKVr34&t=203s)** Um Yes. So, as I said, it's this in discrete event-based simulation framework and it uses an event queue under the hood, which is an heap queue implemented and it stores the event there's an checks which event needs to be evaluated at the next time. Um and there there there's a triple of three uh quite uh metrics which are stored there. This it's the time, an event ID which serves as a time breaker, and the event itself. And so, it gets pushed up the queue, and every now and then an event is processed. So, a short introduction to SimPy. SimPy uses an environment, which is in most cases has a clock in it, and you can run

**[4:14](https://www.youtube.com/watch?v=zayHuvKVr34&t=254s)** it until um the clock the inner clock has reached um a limit. So, this is very basic. You create an environment and run it. There's nothing happening here. So, there's no process or anything else. >> [clears throat] >> But, you can create processes like this. You create an environment, you have an run in this case run method, and as you see, it returns in process generator. SimPy relies on the yield keyword, and also on the generators from of Python. So, later you call environment process, and then our run method, and you call the environment.run, and you create your own your first process,

**[5:03](https://www.youtube.com/watch?v=zayHuvKVr34&t=303s)** and every now and then after a time out of five in this case, it do some simulation, and yields an event back. So, this is very basic. So, as I have told you, I've worked on load balancing, and later this was my architecture from the load balancing scenario. So, each box is later an an process for of SimPy. And this architecture was later very flexible, and it creates multiple clients with multiple processes, uh one load balancer, and multiple backends. So, it helped me quite to evaluate these load balancing algorithms. So, but what you don't really see um everything every entity

**[5:54](https://www.youtube.com/watch?v=zayHuvKVr34&t=354s)** till the wire is an entity which I can control and which I can um inject any uh distribution uh disruptions or anything else. >> [clears throat] >> So, you see a lot of communication, but how is this done in SimPy? Um SimPy provides uh provides some shared resources for you which can use out of the box. Um one simple one is just the resource called and it just uh uses uh or shares a resource with multiple users. Then there's a container which stores a numeric value, but the most heavily used by me is a store which is just a queue and you can input elements and you can retrieve

**[6:44](https://www.youtube.com/watch?v=zayHuvKVr34&t=404s)** elements from this store. And the access, like always, is just done via the yield keyword and the get and the set uh put, sorry. So, this was then the whole fundamental in a really short time um to get started with SimPy. So, we want to put it together and I've dumped the code of a wire. It's very simple, but uh I hope you can get the concept of a wire, how it is done. It is using a store. It's then defined as a Sim protocol that some other entity can put a packet uh to the wire and the packet is then distributed to other um things

**[7:32](https://www.youtube.com/watch?v=zayHuvKVr34&t=452s)** um to put it to another entity. And down below is a distribute function with just uh uh The uh Sorry. The put is start self a process to delay the packet depending on the size of the packet. So, it can simulate a larger packet takes longer to distribute over the wire. Yeah. Then what can we do with SimPy and how can we enhance it? So, how can we collect data to evaluate something then? How can we define behavior or configure such a simulation then? Um collecting data is a little is a little bit uh strange. Um

**[8:19](https://www.youtube.com/watch?v=zayHuvKVr34&t=499s)** we can it has no built-in data collection mechanism. You have to do it yourself. Um this is mostly done or you can do it with an event. For me, this worked perfectly fine. So, there was an event triggered every now and then, which is configurable, and just recording the stats of other entities which have been passed to the uh and collector. This is very flexible. Every entity can collec- can determine what it wants to collect. And so, you can define what you want to collect and do not depend on any on any other other things. Then, how can you define behavior?

**[9:07](https://www.youtube.com/watch?v=zayHuvKVr34&t=547s)** Um behavior defines in most cases the outcome of simulation. Um you want to be able to repeat it, but but in most simulations, behavior is defined via some formula and via some logarithmic some logarithms or distributions. And so, you want to interchange them uh you want to change them based on your input or on your needs. So, for me, what worked fine was to define some value generator, which I can then swap out. And then you can define some abstractions around this, some list generators, some tuple generators, to even be more flexible um on to generate these values you want to depend on. Um some small

**[9:57](https://www.youtube.com/watch?v=zayHuvKVr34&t=597s)** mix ins you can put in, some random mix ins, also passing a seed to be uh repeatable. Um do not forget the seed if you want to use some randomness. Um or also some jitter to have a wave formula which is not clearly a wave, but some add some jitter to it. This This are also components to define the behavior and some really simple behavior is some static generators to pass to always uh yield a single value or to yield a list of a single value. But also derive from it some null generator also yields the null uh zero as a value. So, this is how you can easily define

**[10:44](https://www.youtube.com/watch?v=zayHuvKVr34&t=644s)** behavior. But what comes with it is you can then explore on it defining distribution functions from it, uh defining other formulas, uh or just a random number generator. So, this is very flexible this design, and based on the interface, you can then interchange it on your needs. But as a cloud engineer, I like YAML to configure my things. So, I've used Pydantic settings, which is very nice, and you can define your configuration via YAML. And it supports also um uh what is it called? Uh YAML anchors to reduce your config.

**[11:32](https://www.youtube.com/watch?v=zayHuvKVr34&t=692s)** in my uh settings file was later about 300,000 lines of code, and I can dump it down to 10,000 just by using YAML anchors. So, it supports it. It's very flexible, and I really recommend it if you use some YAML configuration, use Pydantic settings to configure them. So, um yes. If you want to use some of the things I've uh shown you, uh there's a package I've created. There's no pip package for it because the name is already taken. Um yeah. Just take the git and use it. It contains all the settings, all the uh generators. Feel free. Um you know, something I want to show

**[12:20](https://www.youtube.com/watch?v=zayHuvKVr34&t=740s)** you uh tell you about some pitfalls you might run into when you simulate something. Um please make the correct abstractions. Um real-world processes are complex, and you need a decision to decide on which complexity is needed. In my case, I had load balancers, and I want to simulate load balancing on the HTTP level. So, if you look at a TCP stack, I want to load balance at the application layer. I first started to simulate uh at the transport layer. Then I found out, "Okay, HTTP 3 uses UDP, so I have to simulate also UDP and TCP, and uh what is really required for this?" So, after some time, I have

**[13:08](https://www.youtube.com/watch?v=zayHuvKVr34&t=788s)** made these mistakes, and so I have chosen the wrong abstraction layer, and decided then to only use the application layer as an abstraction. Um the next thing is time and the clock resolution. Um you have also to choose the right clock resolution if you run your events. So, each event is >> [clears throat] >> uh, through the queue timed. But, what if you want to run your event or your you think one tick is 1 minute, but in really it is 1 milliseconds? Don't underestimate also the time of running such simulation. Um, the worst time I have had for a simulation, I was simulating uh, 10

**[13:57](https://www.youtube.com/watch?v=zayHuvKVr34&t=837s)** minutes with uh, one tick as a as a resolution of 1 nanosecond. It took about 9 hours. So, don't under Don't underestimate the time it takes also to run the simulation. And also think about expected outcome you want to achieve. Um, do your values correspond with what with uh, with what you expected to be? Um, I've chosen the the wrong packet size. I was expected from one request, but as 20 megabytes per request, but uh, you are short as 20 kilobytes per request. So,

**[14:45](https://www.youtube.com/watch?v=zayHuvKVr34&t=885s)** there was a thing that the packets took too long to transmit via uh, over the wire and this was garbage data in such sense. So, also think about expected outcome you want to have or if the simulation makes sense and what it is. So, as an outcome, this was one of the graphs I've shown and I have can I have proven that the newer algorithms uh, better at distributing packets. And they uh, this the they can serve you more value. Um yeah. So, as an alternative to SimPy,

**[15:35](https://www.youtube.com/watch?v=zayHuvKVr34&t=935s)** um [clears throat] you can also use Celebrium. I have not used it, but if you want to use it, it's also an alternative. It does not rely on the yield keyword, but maybe it is more for you because it has a built-in animation system. Maybe that's something you want to use. Um SimPy does not. You have to build your own. Um don't know how your experience with graphics are. Mine's My experience with graphics are not that good. Um components inherit and there's just one process um per component, which was not quite what I wanted because I needed multi-process This is per component, and this was not an option for me, so maybe

**[16:25](https://www.youtube.com/watch?v=zayHuvKVr34&t=985s)** I have done it wrong. Uh you hold it wrong, the typical sentence you have all heard. Um but for me, Celebrium was not an option in this case. So, yeah. Um you can now simply start using SimPy or just wait for an implementation. In my case, I had more or less than to wait for half an year, and there was one load balancing with all implementations I have required, but until this point, I've already written my simulations. Uh they deserved what they uh they showed what I wanted, and this is what I want to tell you. Simulation is not that hard, so yeah.

**[17:11](https://www.youtube.com/watch?v=zayHuvKVr34&t=1031s)** Thank you. Um if you have any questions. >> [applause] >> Thank you so much, Nicholas. We have a few questions here. Um the first one is, "What are the main reasons for using SimPy to simulate load? What does the na- naive approach, for example, okay. Okay, sorry. The questions keeps Okay, mixing up. You mentioned using a resolution of 1 nanosecond. Is this type of resolution needed for the use case? I would have guessed maybe 100 nanoseconds or 100 nanoseconds to 1 nanoseconds. Sorry.

**[17:59](https://www.youtube.com/watch?v=zayHuvKVr34&t=1079s)** >> Um I wanted to simulate a very high demand of requests. So, yes, in this case it was needed. Yeah. If you have a lower resolution, um your data is also um yeah, you uh the resolution you use to uh or you choose is what your events are sent um you can also lower the resolution if you collect not in that um in less interval. Or shorter interval or greater interval. So, you can then decide on your data what you are also collect. Yeah. >> Okay, the next question says, "What are

**[18:46](https://www.youtube.com/watch?v=zayHuvKVr34&t=1126s)** the main reasons for using SimPy to simulate load?" And then it continues saying, "What does the naive approach, for example, a loop over request uh miss?" >> Um so, my approach uh why I choose uh SimPy, um I don't want to write C. Um there was also a network simulator written in C, and I don't want to write C. Um that's the main reason why I have to why I've searched for other frameworks and yeah, the network would have been maybe some better options because there are more abstractions, more predefined components. But for me, SimPy was later better choice to have more control because the C implementation also provided some

**[19:36](https://www.youtube.com/watch?v=zayHuvKVr34&t=1176s)** capabilities um to inject load from real-world applications. So, this was not what I wanted. Yeah. >> What are the main reasons for using SimPy to simulate load? Um >> Um >> Sorry, sorry, sorry. Uh did you answer that? >> No, not not. >> It was part of the >> Yeah, um to simulate load um is not what I wanted to simulate. So, I want to simulate load balancing. So, load balancing between different servers in this case. Um yeah, this was the and I just needed something to simulate the load balancing algorithms. Yeah.

**[20:25](https://www.youtube.com/watch?v=zayHuvKVr34&t=1225s)** >> Okay, maybe good to mention that discrete event simulation is uh partially uh suited for logic logistic uh systems like handling handling imports or warehouse etc. It's I think that's just a statement. >> Yeah. >> [laughter] >> Maybe true. I'm not that an expert of logistics uh it can be used for load balancing or networking if you need that kind of stuff. But logistics, I don't know really know. So, yeah, it can maybe used can maybe be used. >> Okay, if you want to simulate physical systems like electrical system, What does SimPy offer? >> SimPy just offers the discrete event you have to

**[21:15](https://www.youtube.com/watch?v=zayHuvKVr34&t=1275s)** uh more or less do it your own hard way and create your own components. Um if you are lucky, um there are there's maybe a library dependent on SimPy which provides some entities for you or some components to use it, but in most cases you have to do the hard work yourself. >> Okay. On what hardware did you run your simulations? And it continues, did you try to scale your your compute? >> Yes, I have also scaled it. Um it was later a 32 core machine, um but SimPy is uh really single-core performant. So, I have later run uh multiple simulations parallel.

**[22:05](https://www.youtube.com/watch?v=zayHuvKVr34&t=1325s)** Um there's no much need for multiple cores. Um yeah. What was later my shortage was uh RAM um when I evaluated the data. >> Okay, the final question states that what about using Bio3 for Rust uh with uh Python binding for the most demanding parts of the um simulations. Uh and and then it continues, I imagine Python's uh overhead is very time wasting. >> Uh maybe a solution I have not investigated it. >> Okay. That was the final questions. Uh thank you so much uh for the informative

**[22:54](https://www.youtube.com/watch?v=zayHuvKVr34&t=1374s)** uh talk. Can we please give a round of applause to our presenter? >> [applause]
