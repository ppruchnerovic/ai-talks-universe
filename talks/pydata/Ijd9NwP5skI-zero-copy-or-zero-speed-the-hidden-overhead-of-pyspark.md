---
id: Ijd9NwP5skI
title: "Zero-Copy or Zero-Speed? The hidden overhead of PySpark, Arrow & SynapseML for inference"
slug: zero-copy-or-zero-speed-the-hidden-overhead-of-pyspark
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Petar Ilijevski"]
channel: "PyData"
duration_min: 28
published_at: 2026-08-04T22:21:44Z
video_id: Ijd9NwP5skI
url: https://www.youtube.com/watch?v=Ijd9NwP5skI
youtube_url: https://www.youtube.com/watch?v=Ijd9NwP5skI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Data engineering & MLOps", "Evals, observability & reliability", "Inference, serving & GPU infra"]
transcript: true
---

# Zero-Copy or Zero-Speed? The hidden overhead of PySpark, Arrow & SynapseML for inference

**Petar Ilijevski**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Ijd9NwP5skI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Petar Ilijevski dismantle the "zero-copy" myth to reveal how to eliminate serialization bottlenecks and optimize distributed inference performance in PySpark.

Speakers:
Petar Ilijevski

Description:
Scaling machine learning inference to 6 billion daily predictions using an Ensemble LightGBM model requires overcoming the performance bottleneck created by the Python-JVM boundary in PySpark. In standard PySpark User Defined Functions (UDFs), data is serialized via pickle and sent row-by-row through sockets, resulting in hundreds of millions of boundary crossings and underutilizing the C++ engine of LightGBM. While Apache Arrow aims to provide zero-copy data sharing, in PySpark it still involves CPU-intensive format conversion from Tungsten rows and socket-based data movement.

To optimize throughput, four execution methods were evaluated. Standard UDFs served as the baseline. Pandas UDFs improved performance by vectorizing batches, reducing boundary crossings from 400 million to approximately 4,000. Mapping Pandas further increased speed by introducing a stateful iterator, allowing the model to load once per partition rather than once per batch. SynapseML provided the highest throughput by executing the model natively on the JVM, eliminating the Python boundary, the Global Interpreter Lock (GIL), and serialization overhead entirely.

Benchmarks on a 20-node cluster demonstrated a 9x total performance improvement moving from standard UDFs to SynapseML, reducing total runtime from seven hours to four minutes. For maximum throughput, SynapseML is the most efficient choice, though it lacks the flexibility for complex custom Python transformations. Mapping Pandas is recommended for workloads requiring custom logic, as it offers a 4x speedup over the baseline. Additionally, tuning the spark.sql.execution.arrow.maxRecordsPerBatch parameter to a "Goldilocks zone" of 50,000 to 200,000 records prevents both networking overhead and out-of-memory errors.

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

*4,067 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=5s)** Uh I'm Petar. I'm a senior software engineer at Zalando. I've been working there for the last uh 3 years. Uh if you already don't know Zalando, Zalando is like the largest fashion uh online fashion store in Europe. We sell over 2 million articles to over 61 million active customers over 25 countries across Europe. So, some numbers, our GMV or global uh gross merchandise value is around 17 billion. So, we are a pretty large-scale company. But today we are not here to talk about fashion. We are here to talk about what happens behind the scenes or what is how our computational infrastructure looks like and that's providing our one of our most critical systems.

**[0:52](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=52s)** So, in our department, we embarked on a quest and our quest is to optimize the discount across all of those 200 million uh articles. So, our scope is actually to to optimize the discounts for each article for uh multiple markets. So, we start this quest by uh forecasting demand and if you have I have attended any of the previous talks, so we uh forecast around 6 billion predictions uh for every single article every single day. So, today we are going to cover the quest of uh how we have a achieved this massive scale and where in which places we have found uh performance boost um so we can we can run at this scale.

**[1:43](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=103s)** But first, uh a bit of introduction about the core program uh problem. So, um we uh forecasting demand as I said. So, in order to better understand what that means is that if we see this article, uh we basically want to answer the following question. Is So, what would the demand be if we discount, for example, this shoe in by 20% in Germany? And in the end, we would produce a graph like this where we have various discount levels from 0 to 70%. With, of course, we would expect that as as we have higher discounts, the demand would increase. So, when you take this into consideration, we have a lot of uh 5% increments.

**[2:31](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=151s)** Uh we have a lot of articles across 25 markets. It amounts around 6 billion predictions per day. Don't do the math. It's not correct because there are a lot of things underneath the hood. But the question here we're trying to answer is uh how do we scale this to run every day cost effectively? So, we decided to find our weapon of choice. And our weapon of choice is our ensemble light GPM model where we have hundreds of input features and we output around 6 billion predictions. So, because in Zalando, most of our data processing happens uh in Spark on Databricks, we wanted to explore the idea. So, since we use Spark for data processing, let's try to figure out if

**[3:19](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=199s)** we can use the same framework to run our ML inference models. So, the question that we were trying to answer is how can we use Spark to scale our model inference efficiently? But before we try to answer this question, I would like to cover some basics. There was also another interesting talk that covered Pandas series uh earlier in this uh in this sessions. So, but now I'm going to uh cover it more of a high-level. So, first, let's explain the Python JVM boundary. So, basically, whenever uh what is the problem that we're trying to face? So, uh we have Spark on one hand, which is a JVM base, so it runs on Java or Scala, but our applied scientists built our models in Python.

**[4:08](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=248s)** So, we have a bottleneck, right? So, uh in order to use Python on Spark, we need to cross this boundary. So, what happens is basically every single time we need to make a prediction, uh the data needs to go from the Spark worker, it needs to be serialized, sent to the Python processed, make the inference, serialize it back, and send it back to uh to to to the Spark worker. Of course, this is done through the socket uh through sockets, and the serialization is usually done through pickle. Of course, this is a very slow and uh slow uh process, and when you scale it to 6 billion predictions, it really doesn't scale very well. So, what we want to uh solve is

**[4:57](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=297s)** basically how can we eliminate this boundary of Python {slash} uh Java communication? So, we enter Apache Arrow. So, Arrow has been around for almost 10 years, and if you haven't been using it, you should please have a look and uh start using it. So, basically, what Arrow does is it's it's a new uh tool that standardizes the uh format between which uh different languages can uh communicate in. So, it can create this uh standard uh standard data format, so we can create the data in Java, and we can just pass the same pointers to the Python consumer, and the Python

**[5:45](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=345s)** can just read the uh the raw data without needing to serialize, without needing to deserialize, or to move the bytes between the two processes. Uh some pro tip for you. So, PyArrow is enabled by default on Spark cluster since uh Spark 3.5. So, if you're using maybe an older uh Spark version, you should uh maybe enable this configuration. But, the promise of Arrow is that it allows zero copy, which is true, but that's not really the case in the Spark use case. So, what really happens in PySpark with the zero copy? So, we have three phases. The first phase is the format conversion. So, uh the JVM needs to uh translate that Spark uh Tungsten rows

**[6:36](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=396s)** into Arrow format. So, this might cause us a lot of CPU cycles, memory allocation. Then, Spark actually still communicates to its Python's uh workers through sockets. So, the data still needs to move from JVM to Python through sockets. It This means that you still need to uh the you need still need to invoke the kernel to copy the data, pass it through the socket, and write it to another process. So, it's not really zero copy as as as it says. And finally, if you're using Pandas, then the uh the data still needs to be uh translated into into Pandas, into a new memory space. So, basically, there is still a lot of overhead. Of course, um it's not all bad. It's

**[7:25](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=445s)** still a huge improvement because uh you get a lot of uh these Arrow batches that we call that you can optimize the the serialization. But, the reality is that calling zero copy it's not really not really true. So, let's see how we can actually cross the this boundary. Uh so, our journey actually consists of four methods that we're going to explore. So, first we start with the standard Python UDF, which is actually executing Python functions row by row. Then, we will move on to the Pandas UDFs, which is an improvement. It vectorizes the Panda and Pandas batches. Then, we move on to the map in Pandas, which

**[8:11](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=491s)** uh is again a vectorized batches, but it also allows us to have a stateful iterator. And finally, we look at San X ML, which is a JVM native framework, which complete uh completely removes this uh Python JVM boundary altogether. So, when I go through this journey, we are trying to answer, "Okay, so uh where can we gain this performance?" Like can we remove the function call overhead? Can we maybe uh play around with the batching? Or maybe we can reuse the state of the workers? Or maybe we can even eliminate Python altogether? So, let's try to find out. So, standard UDF is normally the first start for everybody who would like to run their Python code on Spark. So, it's

**[9:00](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=540s)** comfortable, it's familiar, and it's very slow. So, this is where most people start. Of course, the code looks very clean. Like all you need to do to run a Pandas UDF is just to uh add the wrapper on top of your Python function, call it, and that's it. Like it looks like a production code, but in reality, it's very slow. So, uh what actually happens underneath the hood? So, whenever uh arrow batches arrive uh to the Python worker, Python still needs to process these batches row by row. So, the cost, even when we talk about the boundary crossings for our use case, it's still like over 400 million boundary crossings that need to happen between Java and Python. And that's not one problem. So, the other problem is as I

**[9:49](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=589s)** said before, we are using LightGBM models and LightGBM is basically a C++ engine that's built for large matrices and by sending it row by row data, we are just using 15 rows at a time and basically it's like having a Formula 1 and it's stuck in first gear. You you you're not utilizing the full potential of the library. So, while it's most convenient, it also provides you with the most overhead. And this is basically our baseline. From here, we can see how we can improve further. Next, we have the Pandas UDF, which is like our first real upgrade. So, with the Pandas UDF, we can start batching our rows into Spark batches and Arrow can here can kick in and it can uh pack these batches into Pandas data

**[10:39](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=639s)** frames. So, our function here when we see predict batch, it will actually receive the whole batch and then we can utilize the C++ engine of uh of the LightGBM to to do the vectorized um matrix uh multiplications. And this is exactly what it was designed for, so we already can have some performance boost. Uh so, because now we have batches, it means that we reduce the number of boundary crossings by a lot. So, from 400 millions, here we can have about 4,000 uh 4,000 uh crossings, which is the number of batches that would be sent from the JVM to the Python workers. And the data path here looks something

**[11:29](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=689s)** like this. So, the JVM will write the Pandas arrow, uh then it will be sent to the Python worker. Python worker will wrap the pointer, and then C++ will read it. So, it's much more faster. But, there is one more problem with this approach, and because we are using machine learning models, it means that you need to have your machine learning model loaded onto the worker itself. So, uh on the other hand, Pandas UDFs are inherently stateless, so you need to somehow figure out a way to manage the state. Uh one native way how you can do this is, of course, like if you use this this uh has attribute method, you can basically have some custom logic to cache the model on your worker, and that way you can load the model.

**[12:17](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=737s)** Um it's it's a hacky way, but it can work. It's like applying a little bit of a duct tape to to the problem. Um the problem for us is that we still have 4,000 uh batch groups. It means that we have to reload the model even if it's cached sometimes uh up to 4,000 times. And this is seconds of just loading the model, which are very very important to us. So, we wanted to go a bit further, and we explored the mapping Pandas. Mapping Pandas is a Spark operation that solves our statelessness problem by introducing a stateful iterator. So basically uh we can have a stateful iterator once per uh partition, and then uh the model is

**[13:07](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=787s)** loaded only once per partition, and once we load the model, then all of the other batches that come into that partition will reuse the same model. So, because we can now repartition the data to uh right now, we have chosen 200 partitions, but you can choose whatever you need for your workloads. Basically, this means that we would have at most 200 model loads for our our Spark job. Of course, it's important to mention here that even though we have this improvement, like this is still Python. So, we still have the cross boundary communication. We still need to cross the data through the socket. We need to interact with a global interpreter lock, and we have a lot of waste level

**[13:54](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=834s)** switches. So, while we reduce this realization tax, we still don't eliminate it entirely. So, this is where our Synapse ML comes into play. So, Synapse ML is an open Previously, it was Spark ML. Now, it since then it has been taken by Microsoft. So, Microsoft is currently the operators of this library. And basically, it is a wrapper around many machine learning models, and it allows you to run your machine learning models natively on Spark. So, now instead of optimizing our boundary crossing, we can skip it entirely. So, no more pickling, no more arrow, or global interpreter locks. So, because

**[14:41](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=881s)** because we are using Java, we can still use the Java native internal format. It means that whenever we load a model, we load it once per worker or once per executor, and then the JVM will just pass the worker to the C++. And then we can run the inference. So, there are no more no more communication. We have completely removed the context switching and we basically drop the the communication to nanoseconds because everything is done natively in Java. So, Python here still plays a role, but Python just becomes an architect. So, Python still builds the execution plan of your Spark query and on the driver and then sends it to the worker to execute it. But the heavy lifting now

**[15:30](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=930s)** everything is done purely on JVM. Of course, uh you cannot have your cake and eat it. This also comes with um problems. The biggest The biggest problem is flexibility. So, if your custom Python logic like if your model has some complex transformations, let's say like meet inference, you need to transform the data or something, then then using SynapseML becomes a problem because you you still need to figure out the way how you can uh translate your uh custom Python logic into Java. So, you cannot just uh reuse the same model, you know, because you still have custom logic. And if and basically here we we have a problem. So, it's not very flexible. But if you just have raw inference, then uh SynapseML might be the job for you.

**[16:21](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=981s)** Now, let's try to look at some benchmark results. So, we have used for our benchmark uh 20-node cluster that uh predicts around 1.3 billion predictions per second uh per run, sorry. And let's see how we can and do uh how did we make the speed up. So, the first between standard and Pandas UDFs, we can see that we drop with drop from uh 200 to almost uh 50 uh 500,000 uh predictions per second. So, we have around double the increase. Why Why? Just because we introduced the vectorization with Arrow. So, we eliminate this row by row. Then from Pandas UDF to map in Pandas, again we see another almost two times

**[17:10](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1030s)** the the speed up. And this is mainly due to the stateful iterators. So, we removed the serialization and the deserialization task of the models. So, we get a nice increase here as well. And finally, from Mappin Pandas, when we move to the Synapse ML, of course, we eliminate Python entirely, so it is expected that we see around 2.5 increase better. So, if you compare it from the beginning all the way to the end, we end up with around nine times the improvement of just using a different setup over the baseline. So, when we ex- ex- explode these production to or when we explode these predictions to our production workload, basically, for standard UDF, we would have around 7,000

**[17:58](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1078s)** 7 hours of run time, while for the Synapse ML, we bring it down to 4 minutes. So, we use the same cluster, the same model, same everything, the same data, we only change how we execute the model on Spark. So, it's a massive increase. So, maybe which path should you take? Like, because we explore different option. So, if you uh for maximum throughput, if you if you need, you can all of course use Synapse ML. It's natively supported uh I It has natively supported models like XGBoost, some deep learning models. You can also, if your uh model can support an ONNX runtime, it can also run ONNX models. And of course, for our use case, it also supports

**[18:46](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1126s)** LightGBM. It's definitely the fastest route if you want to have production performance, but if you have some extra logic, as I said, it may it not be the right path for you. That's why we have Mappin Pandas, which is my recommendation for ultimate flexibility, because it will deliver you deliver you four times the speed for custom Python logic, and it is very suitable if you have complex model during inference. Right now, this is the approach that we are currently using in the London. Uh, then we have of course Pandas UDFs. Pandas UDFs are still very useful for quick prototyping and then we have standard UDFs which of course you cannot see it here because I

**[19:33](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1173s)** don't really recommend them. They're very good for notebooks, but please don't bring them to production. Um, before we wrap this up, I would also like to talk to you about the Goldilocks zone. So, basically uh in Spark we have this maximum record per batch parameter and I think this is a very important lever for tuning your Spark performance. So, it directly affects our um, Pandas UDFs and map in Pandas operations because there we utilize the arrow underneath the hood. So, by by playing around with the batch size, you can you can basically gain a lot of performance. So, if you choose this value as too small, you might get something like this on the first picture where there is a lot of

**[20:21](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1221s)** communication overhead between the JVM and Python and you lose a lot of performance just on networking. On the other hand, if you set this to too large, then you might run into out of memory problems because you you might get massive memory spikes and if you don't have enough RAM, you might start using the swap memory and then basically your your your workload be just stuck into communi- shuffling data between memory and shuffle instead of actually doing the processing. So, uh, the sweet spot is base for our use case was around 200 to 100 to 200,000 batches and it's like the Goldilocks zone. It's not too hot, not too cold, it's just just right.

**[21:11](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1271s)** So, there are four key takeaways that I would like you to take home from this presentation. So, the first one is please always use Arrow for your Spark workloads, even if you if you don't if you haven't done so long already. If you want to gain four times the improvement, please switch to map in Pandas. And you should tune this uh maximum records batch parameter. Like for us, as I said, the sweet spot is between 50 uh thousand to 200,000, but depending on your cluster size and workload, this uh this optimization parameter can vary. And finally, like the last thing is technique always beats hardware. Like we saw that we can achieve around nine times the improvement using the same hardware just by switching uh how we

**[22:01](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1321s)** process the data. This is equivalent like going from 20 nodes to 180 nodes, but we get this for free. So, if you manage to make these optimizations, your finance team will be very happy because you have saved them a lot of money. So, thank you, everybody, and now we can open the session to the questions. >> [applause] >> Uh thank you so much. Uh yes, we have some questions here. Uh first, uh you mentioned mapping Pandas. Have you tried mapping Arrow method as well? If so, was there an improvement over mapping Pandas? >> We did not try mapping Arrow, uh to be

**[22:49](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1369s)** honest and yes, so mainly why we focused on mapping Pandas was uh because um our our current models work with pandas matrices, so we were only trying to explore the execution methods over an already existing model framework or already existing production models. So we were trying to optimize for this. Of course there are many different rounds you can take like like this but we unfortunately have not explored this. I expect from a previous discussion that we would gain around similar performances because if you map it in arrow or in pandas, it more or less should result to the same performance. Depends on what your underlying data processing would

**[23:39](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1419s)** look like on your python function. So it really depends on that. >> Thank you. Do you use synapse ml for both training and inference? What if inference data is not as big as training data? Would you recommend for doing two different approaches for training versus inference? >> Yes, I would recommend and this is exactly what we are doing. We are still evaluating and exploring synapse ml while it brings this performance boost as I said like for us it's not a very good use case because we have a complex inference model based on the light GBM trees. So we don't really we cannot really port this functionality easily to

**[24:30](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1470s)** uh to to synapse ml without needing to rewrite the code of course and we we are trying to avoid this. So basically if you can export your model to run in any different platform natively then you can do the inference in python or in one worker node and then you can run the inference in synapse ml on multiple nodes which is the case that we have actually covered here. >> Thank you. Um pa rum pum pum. Oh, wait a minute. Um okay. How are data scientists Mm again. How data scientists are dealing with this amount of data for experimenting? It seems like an engineering problem. So, I'm curious. How are you handling this in experimentation phase?

**[25:22](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1522s)** >> This is This is a very interesting engineering problem to solve, but in the end uh our infrastructure and our setup allows us to uh for our applied scientists to run experiments on the full set of data. So, because uh the run time of our end-to-end processes take around 30 minutes, this is still very um very efficient for us, and we can allow to run multiple experiments. Of course, we are always looking for ways to improve and reduce this run time as we see as we saw here, but in the end we use the same infrastructure for experiments as we use it in a production setting. >> Thank you.

**[26:11](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1571s)** Um have you Have you considered use Scala or Java to implement Spark job to get optimal performance? >> Yes, but our applied scientists are not happy about it. >> Okay. Uh did you also try mapping pandas for training? >> Mapping pandas for training? No, but that's more due to the nature of the problem of tree models. Like the tree models still require uh the full data to be available uh at a single time. Uh of course, there are new algorithms that can improve the that can distribute this workflow during the training process, but we analysis needs to be done and we need to explore whether using this new

**[27:00](https://www.youtube.com/watch?v=Ijd9NwP5skI&t=1620s)** distributed approach will be more performant for us over the current approach. So for us the safe choice right now is to train the the data on a single node where we have all the data available. >> Thank you. So it seems there are no more questions here. Uh somebody? No? Okay, then we thank you for the speak and you all for coming. >> Thank [applause] you.
