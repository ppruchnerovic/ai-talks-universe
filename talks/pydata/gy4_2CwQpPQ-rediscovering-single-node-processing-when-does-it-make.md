---
id: gy4_2CwQpPQ
title: "Rediscovering single-node processing: When does it make sense to move from Spark to Polars?"
slug: rediscovering-single-node-processing-when-does-it-make
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Jonas Böer"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-04T22:21:00Z
video_id: gy4_2CwQpPQ
youtube_url: https://www.youtube.com/watch?v=gy4_2CwQpPQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Rediscovering single-node processing: When does it make sense to move from Spark to Polars?

**Jonas Böer**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=gy4_2CwQpPQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Jonas Böer challenge the Spark status quo as he explores when switching to Polars for single-node processing can streamline your data pipeline and reduce costs.

Speakers:
Jonas Böer

Description:
Apache Spark and Polars represent two different philosophies of data processing: horizontal scaling via distributed clusters and vertical scaling via single-node optimization. Spark, written in Scala and running on the JVM, is designed for terabyte-scale datasets across multiple nodes. It utilizes a lazy execution model and a client-server architecture, making it ideal for massive parallelization but introducing overhead through cluster startup times and complex JVM stack traces during debugging.

Polars, written in Rust, optimizes for single-node performance by utilizing all available CPU cores and memory on a single machine. It supports both eager and lazy APIs and employs a columnar memory layout. While Spark remains faster for simple row-wise parallel processing, Polars often outperforms Spark in complex operations like joins. Polars also offers a more modern, hierarchical API and faster development cycles because it eliminates the need for cluster management and simplifies unit testing.

The decision to migrate from Spark to Polars depends on data volume and infrastructure. Polars is most effective when the data per processing step fits within a single machine's memory (typically in the gigabyte range) and when there are high interdependencies between rows that would otherwise cause expensive shuffles in a distributed Spark environment. While Spark provides superior integration with data warehouses and comprehensive monitoring via the Spark UI, Polars reduces operational complexity by running within a simple container. For users currently employing Pandas, Polars serves as a high-performance replacement with a more consistent API.

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

*4,676 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=5s)** So uh let's imagine a situation. You just wrote some amazing Spark code. It will be really cool. You want to run it, test it out, but the cluster is down because yeah, of course it's uh it's not running. Uh so you click on start, you go make yourself a coffee, uh chat with your colleagues, maybe with your cat if you're in home office, come back to your computer and completely forgot what you were doing. So u maybe you know this situation I do. Uh and one of these days I thought yeah maybe there's a way not to wait that I don't have to wait for the spark cluster. Maybe uh there's something new something different. And uh I discovered polars and the idea that uh yeah that everything runs on one machine not on a cluster. Um and yeah does not need to run all the

**[0:56](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=56s)** time. Quick aside, quick uh advertising block blog. Uh why can I do this uh talk? Because I'm at InovX. Uh we had like six talks at this conference and we are hiring. So if you also want to make conference talks here uh and meet amazing colleagues, uh talk to us. But now back to topic. Uh let's talk a bit about an introduction about uh Spark and Polas. A quick comparison of the two. So uh dry facts uh spark has been released in 2012. It's maintained by the Apache software foundation. It is a distributed query engine written in Scala. So it has the JVM behind it. It is ideal for horizontal scaling. So uh if your job

**[1:45](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=105s)** does not run just add more nodes to the cluster. It runs uh in a lazy execution model. So uh it collects all the instructions and only in the end when you give it a command to write it out uh it optimizes the collected instructions and then runs them and uh yeah it is a server client model so it has a server that's always running or not uh and a client that connects to it and submits jobs. Polas is rather new. It's been released in 2020. It's maintained by Polas BV which is a company. Uh it is single node. It's written in Rust and yeah, it's ideal for vertical scaling. So, it's designed to make use of all the memory and all the CPU cost that your machine has, but no other machines. Uh, it supports both an eager and a lazy

**[2:34](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=154s)** API. So, you can choose if you want your commands to be run immediately or again only at the end. And yeah, it is part of your code. It starts and ends with your script. A few notes that about both both are uh released under a free license. So spark under the Apache license polit they both provide a data frame interface and they both have a column memory layout to enable yeah aggregations on big data. So uh let's compare them. uh as uh for this talk I used the NY NYC taxi data set which is just a good way to get a few hundred million rows. Um I want to make a few comparisons execution speed

**[3:24](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=204s)** runtime cost development and experience analysis debugging deployment integration and finally the big question. Yeah when and how would you switch from spark to pol. So let's start with the execution speed. I would like to note I will not do any benchmarks. I will [snorts] not show any numbers because uh I was not sure if I would write both perfect spark and polar code to make a comparison uh sensible and even then if I did then uh why would I expect uh that everybody who uses them writes perfect code in both. So uh I think those numbers are nice for websites but I want to bit I want to go over my subjective experience and that was particularly in parallel processing. Spark is still much faster. So if you

**[4:12](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=252s)** just have uh a job that make does maybe row wise processing spark just could distribute the work across its nodes and uh yeah have an advantage there. For everything else, uh, Polas is faster. So, especially if you have joins, join your data within itself. Um, it felt a lot faster or it was a lot faster. But I have to say the performance was sometimes a bit inconsistent. It is rather young. I want to highlight one bit of code, the sync delta function, which is the lazy evaluated uh function. So, which yeah writes your data frame into delta. And uh in my experience this was significantly slower than using a

**[5:00](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=300s)** collect so execute the lazy uh the lazy data frame and then write with the eager method. This was slower. I think it's mostly because the sync delta was newer. It was introduced to the code or it was released somewhere between when I wrote the proposal and when I started working on the talk. So uh at least we have it now. It's it's cool. Uh spark on the other hand uh you probably have seen code something like this. Uh you do some kind of repartition uh and your code is faster but you don't know why it is faster with this exact number. So uh spark is a bit difficult here. Then of course uh about the costs, yeah the cluster startup uh costs especially for small small tasks when the cluster

**[5:50](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=350s)** startup is a significant part of the runtime that uh makes some of the costs and uh at least in my experience the compute size in total is not much [snorts] smaller uh for polar. So I found uh at least for my task so I did some feature engineering on the NYC data set um the compute size in the end was roughly the same. So I just used uh one machine with let's say 64 GB of memory instead of eight worker nodes with 8 GB each. Let's move over to the development experience. So very sub subjective uh polars is fun. So it feels very modern. It it has an hierarchical API. So many

**[6:41](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=401s)** similar commands like string commands or datetime commands are grouped into more or less modules that makes it really easy to read especially and uh I don't know there's a law law of computing code is read 10 times as much as it is written or so. So yeah reading experience is important. On the other hand, I have to say, oh yeah, uh and as the polas community says, come for the speed, stay for the API. I tend to agree. So the speed is really nice, but uh when being faster at writing code is also uh a significant factor. On the other hand, Spark, I mean, it's established. Everybody knows Spark. No matter what problem you have, somebody has had it before and written a blog

**[7:28](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=448s)** post about it. So you can really well uh find solutions for almost all of your problems and especially in this year uh this also means a lot of LLM training data. So uh wipe coding with spark is easier because there's so much more training data that the LLMs can use. Let's compare two bits of code. So this is a feature processing written in Spark. uh I wanted to get the taxi trips uh aggregated by the hour. So I did a window function uh by one hour. Then I added some aggregations like the trip count, the trip distance, the amount of passengers, the mean trip duration. Uh in the end I needed to tidy up a bit.

**[8:17](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=497s)** So uh remove the uh or reintroduce the pickup date time and finally drop an intermediate variable in Polas. The code would look like this. So Polas has this group by dynamic for I think mostly for time uh time based aggregations. So I say group this by every hour and uh yeah don't mix up data from different vendors or different pickup or drop off locations and then there's the aggregations like I used the length of the group uh give it an alias I sum up the trip distance as well as the total amount this is particular for polars so I give multiple column names into the sum function and it just sums

**[9:05](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=545s)** up the columns each separately and just keeps their name. So you see in the spark example after the sum I needed to print an alias so that the column name stays the same. And finally I uh subtract the date times uh yeah calculate the mean cast it to an integer uh in microsconds and convert it to seconds. So now the code has run or is running. Uh you want to know uh how fast is is it uh and if it did not work what went wrong. I found the error messages not unsurprisingly less noisy in polars mostly because Spark often has this long stack of JVM communication in its error uh in its uh stack trace. So this uh so

**[9:58](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=598s)** it's sometimes hard to find the actual error. Both offer a data frame explained. So for the uh lazy uh lazy evaluation in polars and this I don't have to say much about it. If you've seen one and understand spark data frame explained you can read the polars explain and understand it just as well. They are nice. But now let's go to something that big advantage of spark in my opinion. In the Spark UI, I would say yeah, it's as complex and great as Spark itself. So you have the uh your worker nodes, you have the submitted jobs, you have your stages, those three are not relevant for polars of course uh but it has this post hawk performance analysis. So afterwards, especially if you persist your Spark logs, you can see how long

**[10:47](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=647s)** your jobs took, how long uh what what was slow and polos just feels quite limited in comparison. So uh Spark uh SQL query views might look like this. Every blue box corresponds to one Spark operation and or every light blue okay the contrast is a bit bad. Every small box uh is a one spark uh command and every big blue box is one stage. And now you can go into this. You see for every command how long it took, how much data it read, how much data was shuffled across the executor nodes, how uh how much c the cache was used and so on. And you can go really deep into this and uh optimize your code really in a very detailed way.

**[11:35](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=695s)** Let's contrast this with polars. So again a bit of polars code as an example. I wanted to introduce lag features. So by 1 hour, one day, one week and one year. So I wrote a for loop uh joined uh the data to itself just with uh with an offset. There you can see the dt offset by as a uh as a hint when reading. Yeah, this is a datetime function. I want to have an offset on a datetime column and um add a suffix to the uh to the data and then I run the show graph command. So you don't need to remember this code particularly um just that I had this loop and in the graph it looks like this. So maybe okay uh there's a bit of preparation and

**[12:26](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=746s)** then there are those four joins up above. You don't need to read this. Uh the basic thing is uh yeah it joins by itself and yeah you can see uh the operations but not how long they took. For this, Spark has a profile function which evaluates the lazy data frame, returns the result and the runtime. And then you get something like this. So there's an optimization step, there's a width column for the L column, then there's the join and then uh there's returning the data frame or writing the data frame. The problem is now there's one join, but I had a for loop with four joins. So which one of these four joins was the slow one? I don't know. And unfortunately, I cannot read it from

**[13:14](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=794s)** this graph. So, uh this is still something to be improved. Until then, I'm a bit confused by this. It's not that as helpful as it could be. But now, let's say the code is fast. You're happy with how it runs. So, let's look at the integration. Spark. Yeah. I mean, again, Spark has been used by everyone. It has integrations for pretty much everything. There are multiple data warehousing platforms that uh that have their own implementation of Spark or they use Spark. So basically with Spark you can easily connect pretty much everything. So catalog servers, other databases um various file formats and of course yeah Snowark or datab brick spark as propri proprietary implementations of the API.

**[14:06](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=846s)** Polas on the other hand feels a bit limited. So uh it can read from the unity catalog. It cannot yet write into a table registered in a unity catalog. It can read and write delta. I think I heard this morning or yesterday in a talk that uh uh iceberg support is uh yeah ongoing. it's uh not not yet finished but yeah it's uh just a bit less and then yeah of course for spark you need to have your compute cluster you need to run uh you need to run the cluster all the time polas you just probably have it in a container as part of your code so you have your container image that just uh has polars installed and your code just uses it and

**[14:55](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=895s)** afterwards it's uh yeah afterwards it's it shut down again then yeah spark in if you have a data warehouse solution then probably you use the fully integrated uh scheduleuler in there but if not maybe airflow or some other kind ofuler polas does not yet have uh data warehouse integration so yeah you just need to use your own scheduleuler bring your own scheduleuler which is not bad it's just how it is and With this uh comparison of the two, let's go into the big question. Why, when, and how should I know use polar over spark. Let's start with the when and why. So, uh I think if you have worked with

**[15:47](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=947s)** polars before, you probably heard it. Yeah. If the if your me if your data per processing step roughly fits into the memory of your machine. So if it's in the range of gigabytes not terabytes for most applications then uh polars can be faster then uh in my experience at least if the processing takes place in a uh yeah in a serialized or random way. So there's interdependence between the rows in your data. then you don't need to shuffle between the executor nodes which is which makes spark slow. Uh so if your data looks if your data interdependencies look like the one on the left then probably you are better off with polars. If there are no interdependencies you can just run all

**[16:36](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=996s)** the rows in parallel through your processor then spark uh might still be faster and uh as we just had with the integration if a strong integration is not your priority right now. So if you for example need uh need uh your uh the data catalog updated all the time with the current result of your uh of your jobs. Then uh with polars it is a lot more work. With spark you just load the corresponding plugin for uh data hub or whatever and spark and it takes care of for of it for you. Then uh yeah consider the switching cost. So uh in the age of LLMs it's not that bad but uh still consider your

**[17:25](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1045s)** development time and the cost of running two resources in parallel. So I think that's XKCD1205. Uh read it later on. uh how much time you shave off, how often do you run the task, how much time do you want to spend on it? Multiply those numbers with your hourly wage and uh the cost of running them and you get an estimation of whether it's worth it to switch. And at least in my experience, yeah, the cost savings with polars rather come from uh a faster execution time and not that much from cheaper instances. So uh now if you want to start with polars after all this what should you do? First of all uh I would say quick

**[18:14](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1094s)** and dirty projects work really well with polars. So uh especially if you use pandas try tryas instead. I heard from Inovax colleagues that they just have uh stopped using pandas entirely. They have switched completely to polas. Uh, and if you have spark code that uses UDFs, uh, like this one, so the old style, uh, that uses pandas, uh, just switch it over. This polar bear tells you, yeah, use an arrow UDF. There you have an an, uh, pi arrow array array and this and polars can just load this with with a zero copy load. So you don't need to pass anything. and you just put in the uh the pi error pi arrow uh object. And uh if you just want to try

**[19:08](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1148s)** something, if you want to uh to try out polars, maybe even with a production size job, uh why not run it on a single node cluster? So if you have your spark cluster for example in data bricks then uh create a single node uh cluster uh give it a lot of memory give it many processing cores uh add a uh pip install or whatever install polars to the init script and use polars there why not I mean there you still have the uh the cluster start time but uh at least you can run polar us afterwards and uh yeah why not try an LLM of your choice uh to translate the code between

**[19:57](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1197s)** the two. So uh I would say Polas to Spark might work better again because there's so much more training data for Spark available in the internet than compared to Polas. But uh I also tried uh some larger feature engineering or data transformation jobs put it into an LLM. tell me, hey, this is Pispar code translated to call us for me. And uh the code worked mostly. So of course sometimes there are bugs still, but all in all uh it worked quite well. So uh I come to my conclusion. Spark is still yeah the major framework. It is well established. It has a lot of documentation and supporting material. If you have your uh your data warehouse

**[20:47](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1247s)** platform then uh yeah spark is there spark works and [snorts] uh you can just use it. Polas on the other hand, yeah, it's new, it's fun, it's really fast, but uh in my experience or what I found is the integration in business environments is unfortunately still lacking. But uh yeah, both are in active development. I mean, Spark has been in development for much longer. It uh brings cool updates, performance upgrades, new features. uh in Polas there are still a lot of new things coming for example as I said uh the iceberg support that might come soon so uh yeah continue watching them

**[21:38](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1298s)** should you change yeah it depends I hope that I have given you a bit of uh my opinion and from there you can form your own opinion whether you should change it at least uh no matter if to switch production. If you decide to switch production right now, try it out and form your own opinion, replace Spark, replace, not maybe replace Spark, definitely replace Pandas in my opinion. Uh, Polas, yeah, it's fun. Try it out. And with that, thank you. [applause] Thank you. Thank you for your great talk, Eonas. So we have lots of questions. Please upload um the audience please upload them so that we can focus

**[22:25](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1345s)** on the better questions. So the first questions is has two sub questions. The first sub question is from small data volumes is polus better than panders question mark or will there or will it makes no difference? I think you answered it now with the closing remarks. >> Yes. So uh I think uh I mean polas is definitely faster than pandas. If your data is small enough that it makes no difference then in my opinion at least polas has a nicer API. So uh it I mean uh everybody who's worked with uh pandas knows this setting with copy warning I think uh which shows you some important information that you don't

**[23:14](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1394s)** understand and still continue to use it as before. uh with polars you don't need to use lock or eyelock and know the difference between the two. So it's just easier to write, it's easier to to work with. And uh both for exploratory work, you can just use the eager API in Polas and uh yeah, run your commands on your data frame and see the result immediately. And if you decide, yeah, okay, this entire process looks good. I can go towards production, you can very easily just switch over from the eager API to the lazy API and just have it execute at the end. uh have the optimizer optimize your execution graph and um I I think pretty much all the commands that work

**[24:01](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1441s)** on the eager API also exist in the lazy API. Sometimes they are a bit different. For example, you would run scan CSV instead of okay I don't know load CSV or read CSV. Uh so you would use different methods for reading and writing but all the processing commands are pretty much the same and they work the same. So uh I think they there's ongoing effort to really just get rid of the eager API and just replace every eager command with a collect uh with a yeah lazy API command and then a collect so that you they of course they don't want to maintain two code bases uh in parallel so they would just uh yeah >> I I think you also great answer thanks so the next question is for Matias and

**[24:50](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1490s)** this really a great question do you consider it an antiattern to run polos in data bricks do you consider >> maybe antiattern >> I mean uh if it works it works so uh it's uh of course it could be better but if you I don't know if your organization is completely in data bricks you have all your tables you have all your data in there uh then of course you don't go and spin up and Kubernetes cluster somewhere else uh set up the integration there and all this just so that you can run polars outside of data bricks. So depending on the situation it makes it might make sense but uh of course if you can avoid the cluster startup then uh it's

**[25:40](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1540s)** probably better >> makes sense completely. So the next question is like small question with a little bit more context then. So did you try testing this with polus or pike spark? Um like the context found that unit testing conversions was much easier with polus versus spark and deciding to use db dbx spark versus normal spark. Um so currently I don't know for the second part I don't know uh particular differences between the spark the datab bricks implementation of spark and uh the open source but there are differences uh for my tests I use the datab bricks implementation um for the first part of the question yeah running unit tests with polars is

**[26:28](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1588s)** much easier because you don't have to either set up a spark cluster or mock it you just run polars with maybe separate test data. Uh so yeah it is much easier to to develop unit testable code with polars. >> I see the next question um is about what about ray or dask for hor horizontal scaling? So what's about these tools? >> I have no experience with them. Sorry. I think they are probably also good but uh yeah I wanted to talk about single node processing not horizontal scaling >> there's so many libraries and tools to use like always you can only have like a limited view sorry on the next question did you have a chance to try polos cloud

**[27:19](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1639s)** distributed polars question mark >> uh I have not and okay I wanted to say it during the talk but I uh decided to leave it out of here. So for those who don't know, Polas cloud is an effort by Polas to uh provide this really nice Polus API but uh also with cluster compute. So it I think their expectation is to develop this as an a paid offer. So they want to host the polar cloud yourself evolve into a data warehouse similar to data bricks uh snowflake or so and uh finance the development of open source polars single node polars with it. Uh but yeah this would have been too much for this talk so I left it out.

**[28:07](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1687s)** >> Super. Next question. Does all of this also applies to pipeline and snowflakes? Should I use polars instead of snowflakes? >> This was and should I use polars? >> Yeah, >> I mean uh snowflake is a bit different because uh it's uh that the data is not saved in a location that you can access from outside the environment. So I think it's harder to use polars in there. And as far as I know, but I might might be wrong, there's not yet a method to directly convert a snowpark data frame into uh polar data frame. So uh as long as this is not available and you might

**[28:55](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1735s)** still need to convert a polar data frame to pandas and from pandas to p no snowflake data frame to pandas and from pandas to polars I think uh this will probably uh negate any speed advantage that you might get. >> Okay super I I think we have time for one maybe two question. Do you need to write your own polus plugin context? I think it's important to mention that you would need to need rust to write us to do that. So writing your own polar plugins. So >> yeah, that's right. So yeah, Polas is very is also extensible. You can write plugins, but yeah, you need rust. So uh there are no, as far as I know, there are no bindings for Python to write plugins.

**[29:43](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1783s)** Um I I think they just expect that yeah you that that you want your plugins to be as fast as possible and use Rust for this >> experience in writing them. >> No. >> Okay. So then the last question would you agree if this with the statement statement of starting out with data engineering start with polos and delta and then see if you need spark. >> Yes. So especially if you start yeah if you if you start out start with this it's a nice API uh and you don't need to think about stages and shuffling and all these things that you have with spark just start with polars understand the concepts and when you got them then you can decide if your data is big enough and fulfills the requirements for spark.

**[30:34](https://www.youtube.com/watch?v=gy4_2CwQpPQ&t=1834s)** Thank you, Yianas. We are on time. Um, so I will see you all later in the closing sessions. Um, and I want to have a big applause for Yonas, one of our last speakers. [applause]
