---
id: Jho624IrxpM
title: "From Row-Wise to Columnar: Speeding Up PySpark UDFs with Arrow and Polars [PyCon DE & PyData 2026]"
slug: from-row-wise-to-columnar-speeding-up-pyspark-udfs-with
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Aimilios Tsouvelekakis"]
channel: "PyData"
duration_min: 37
published_at: 2026-08-04T22:20:44Z
video_id: Jho624IrxpM
url: https://www.youtube.com/watch?v=Jho624IrxpM
youtube_url: https://www.youtube.com/watch?v=Jho624IrxpM
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science"]
transcript: true
---

# From Row-Wise to Columnar: Speeding Up PySpark UDFs with Arrow and Polars [PyCon DE & PyData 2026]

**Aimilios Tsouvelekakis**

`PyData` · `PyData` · `2026` · `37 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Jho624IrxpM) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Aimilios Tsouvelekakis demonstrate how to eliminate PySpark UDF bottlenecks by leveraging Arrow and Polars for high-performance, columnar data processing.

Speakers:
Aimilios Tsouvelekakis

Description:
PySpark User Defined Functions (UDFs) often suffer from performance bottlenecks due to row-wise execution and heavy serialization overhead between the Java Virtual Machine (JVM) and Python workers. Traditional Spark UDFs rely on Pickle for serialization, while Pandas UDFs utilize Apache Arrow to move data in batches. However, Pandas UDFs still incur memory overhead during the conversion between Arrow and Pandas formats and are limited by single-threaded execution.

To resolve these issues, Arrow UDFs and the mapInArrow method provide a zero-copy mechanism, allowing Python to read directly from memory buffers. Integrating Polars as a query engine further improves performance because Polars is written in Rust, supports multi-threaded execution, and shares the Arrow memory layout.

Benchmarks demonstrate that when computations are lightweight, such as string normalization, Arrow-based methods significantly outperform row-wise UDFs. For compute-heavy tasks like HTML cleaning or string similarity, the performance gap narrows unless the logic is vectorized. By replacing Python loops with native Rust kernels via Polars, execution speed increased by approximately 2.2 times for complex string similarity tasks. The key takeaway is that maximum efficiency is achieved by avoiding Python loops and utilizing columnar memory formats to minimize cache misses.

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

*5,103 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=Jho624IrxpM&t=5s)** Thank you very much. Uh good morning from my side. Uh my name is Alios. Well, for most of the people it's difficult to pronounce my last name. That's usual. I have a long name. Uh so today here I'm going to present you a problem that I had uh currently in my work and uh I work as a software engineer uh for a company which is an open access publisher which means that uh we publish uh research papers in our journals and I work mainly on the data product. Uh we use spark and um I found some complications. I tried some stuff and I wanted to present them to you. So, uh when we have somebody new into Spark, the idea is that we do big data,

**[0:54](https://www.youtube.com/watch?v=Jho624IrxpM&t=54s)** distributed computing and so on. And the first advice that we give is okay uh whenever you want to do something, try to use native Spark functions. uh if you cannot you can write your own your own functions which which we call them UDFs or userdefined functions uh what they do it's that uh the main principle is that I want to do a task which is not possible natively you can model the data with them perform transformations and usually the tip we give is you should use them with caution why that because they are helpful you're doing your task but in the and they slow you down and uh this is something true uh but uh I will try to change today the

**[1:44](https://www.youtube.com/watch?v=Jho624IrxpM&t=104s)** aspect a bit. So here I I present you the data flow uh over a spark uh UDF and what we have we have a partition with unsafe rows into the Java virtual machine. uh this thing needs to be this thing needs to be serialized. Error error needs to be serialized and converted to bytes. It passes through a socket to move from the JVM to the Python worker. Then the Python worker reads those bytes. It the serializes them. It creates the Python object. You pass this Python object to the function that you have written. you get a result and you do the opposite [snorts] trip to go back to the JVM. What is the problem here? Uh

**[2:34](https://www.youtube.com/watch?v=Jho624IrxpM&t=154s)** actually we have two problems. The first problem is that if you take a look at this graph or if you listen to me describing it, I say serialized the serialized serialized serialized. So we are doing four times this uh this action and this is a CPU bound action and a very heavy one and we don't want it. We are adding serialization overhead to what we are doing. Plus we are executing the computation row by row here. I want to note something important is that many people don't think uh when they do the computation what kind of library they use. What I mean by that using a Python library will be slow. If you can find a library that does the same thing natively, it will be

**[3:23](https://www.youtube.com/watch?v=Jho624IrxpM&t=203s)** much better even if you use a spark udf and we will see it later. H I don't have I don't have included the example but I have examples where I have used a very specific library because the Python version was was much slower. The evolution of UDFs in Spark is that we have the what we call Spark UDF which is the classic one. Everybody starts by this UDF. Uh it was introduced with Spark 0.7. uh as we said the serialization is being done by ple and it's row by row then we move at some point to spark 2.3 which is pandas udf uh here things are changing a bit the serialization becomes arrow we are executing by series the engine is

**[4:11](https://www.youtube.com/watch?v=Jho624IrxpM&t=251s)** mostly numpi or c we continue further with arrow optimized udfs which is something different of a concept it's mostly an improvement over the spark udfs and what improvement the serialization here uses arrow again but the execution is rowby row and we come to today which is uh arrow udfs it's a completely different aspect because you use arrow as the serialization and the execution is vectorized and mostly using C++ kernels Following I will continue with the pandas UDF workflow. Here we have a batch of rows mostly around 10,000.

**[5:01](https://www.youtube.com/watch?v=Jho624IrxpM&t=301s)** 10,000 is uh the the default batch record for for spark and towards the serialization part the JVM what it does uh it changes the rows to columns uh to columns so they can enter the arrow IPC and then this arrow APC converts to bytes they pass through the socket when they pass through the socket they get serialized and they become uh a record batch And this record patch is converted to pandas to pandas series. So you can pass it through the udf you get the result and you have again the round trip back to the JVM. A few uh notes here. Of course we have avoided with arrow the rowby row

**[5:51](https://www.youtube.com/watch?v=Jho624IrxpM&t=351s)** serialization to serialization but it's not enough. Why it's not enough? We have high memory usage. the conversion from arrow to pandas and pandas to arrow uh will give you will you will keep the the objects two times in memory. So this is high memory usage and the pandas data frame from some data frame operations is single threaded which is slowing us down. So I talked about a new concept which I did not introduce so I will do it now and this is Apache arrow it's an in-memory columnar format and what it what it achieves it solves the copy and convert bottleneck and what is a copy and convert bottleneck it's what I previously talked uh in theory

**[6:43](https://www.youtube.com/watch?v=Jho624IrxpM&t=403s)** uh we keep and in practice we keep two uh two times the same data in memory why do that because pi spark is a wrapper over spark. Spark works over the jvm. Pispark works over a python worker python process. So these processes without arrow they need to have a copy of the data. With arrow they don't need that. You don't need to copy the data. You can have the data available to both systems. And why is that? Because you are reading directly from the bytes. you are reading the memory and this is what we call uh zero copy arrow also helps in another aspect which is a bit of lower level and goes to the

**[7:31](https://www.youtube.com/watch?v=Jho624IrxpM&t=451s)** hardware. So uh I said before that we are doing some CPU uh operations all of them actually and the biggest problem is that how we retrieve the data from the from the how we use the data that to uh to execute it on the CPU and the CPU has ces L1, L2, L3 and when you are on the row layout out. So you are not having a column, you are having the whole row being serialized into the C. But what happens if you need only one of the columns of of this row? You are filling the cast with data that you don't need that you are going to request but you that you are not going

**[8:18](https://www.youtube.com/watch?v=Jho624IrxpM&t=498s)** to request. So the next data that you will need it will not be in the cast it won't fit. So you will get always cast misses. This is changing with a columnar format. Why? Because you are just getting the row. You're applying it continuously in the gas and you're not having misses. And the hardware prefacer helps in that in a sense that it predicts always the code that you the data for the code that you will need. Continuing uh on the next UDF is the arrow optimized UDF. As I told you, it's an improvement in one aspect over the over the Spark UDF. The improvement is

**[9:07](https://www.youtube.com/watch?v=Jho624IrxpM&t=547s)** that you see that the first part until the record parts does the same rows to columns, columns to bytes over the socket and you get a record bats. But the biggest pro the biggest issue here is unpack. So because you haven't solved the row by rowby row execution even if you had a if you if you have a batch of columns you need a specific row for to pass inside your function and you do the opposite trick the opposite trick. So the over the Python overhead remains and we go towards RO UDF. ROU UDF follows the same pattern of conversion passing through the socket and so on.

**[9:55](https://www.youtube.com/watch?v=Jho624IrxpM&t=595s)** But we don't have any conversion as you see from the record batch we have a zero copy and we go into inside if it and we go inside the function which is using prow compute and performs and performs computation. So the data stays columner and it's also computed with C++ kernels. A small issue or a bigger one is that it requires pyro compute which is more of a low-level API and if you want to perform multi-step transformations then it's a bit harder let's say to use from what we have been uh you know uh used to with dataf frame APIs and what is the solution to that the solution to that is to use another data frame

**[10:44](https://www.youtube.com/watch?v=Jho624IrxpM&t=644s)** library as your query engine actually uh which is polars polar This is quite a new library. I think it uh started on 2020. It is a very fast library dataf frame library. It's written in Rust. It has multi-threaded query engine. So we bypass the problem that we have uh with pandas and single threaded and it's built on Apachi arrow memory layout. So it means that it already supports uh Apachi and it has a userfriendly and expressive dataf frame API. Now uh besides the evolution of UDFs we have better al better integration with arrow API in spark and what we have uh from spark 3.3 we have mapping arrow

**[11:38](https://www.youtube.com/watch?v=Jho624IrxpM&t=698s)** uh which is the analogous to mapping pandas but we don't have the conversion to pandas from spark 4 we have apply narrow which is the analogous to applying pandas and we don't again have the conversion and we can convert a spark data frame to arrow from arrow and if we want to see how mapping arrow data flow works it's the same idea what we have with uh arrow udf but you have an iterator of uh record batches so the the idea is the same there is no conversion to pandas and you you always stay on the arrow format. Actually the longer you stay on the

**[12:27](https://www.youtube.com/watch?v=Jho624IrxpM&t=747s)** arrow format the better is for your computations. Now uh these are the methods that I have tested. So I started with a spark udf. I picked the pick which is the classic approach and the arrow transport pandas udf arrow udf and mapping arrow. And for arrow, udf and mapping arrow, I chose two query engines by arrow and polars. These are the tests that I'm going to show you. Uh these are tests actually that existed in my in my code and I started fixing them. The history is that I started from HTML cleaning and at some point I got a call from a colleague telling me that this

**[13:16](https://www.youtube.com/watch?v=Jho624IrxpM&t=796s)** was really slow. I took a look in the beginning and it was uh written in beautiful soup. So it was slow without using a lxlm parser. Then what I did to improve it is just I used xlm I didn't even used uh even a better libraries but lxlm is is see it's much f it's much faster. Uh and then I tried to follow the same idea for other transformations. So in theory all of my tests these are five tests broken actually for me it's let's say one transformation one transformation in a data frame uh and I will start with the first one I hope it's readable I think it it is so I am going to show you uh for each of the tests the implementation as you will see we will go through this but for more

**[14:05](https://www.youtube.com/watch?v=Jho624IrxpM&t=845s)** or less the co for more of them the code is uh the same so the structure is the same it's only the execution of the specific uh uh test method that we are using. So in this case we have the classic UDF. I think everybody can recognize uh then we go to uh the classic UDF with the arrow transportation. You just see that the change is only just a flag and we go to pandas udf. We have two options here actually. We have let's say the vectorzed in quotes option which is str nor normalize and using uni code data library which is a python library with the apply and you call it with with column which is the standard way of calling it.

**[14:54](https://www.youtube.com/watch?v=Jho624IrxpM&t=894s)** Moving on, you will see first of all that we can do the same calling with arrow UDF no matter of the implementation. On top you see the pi arrow you see the pi arrow implementation uh we are reading an array a pi array compute array actually batches of this array and we are returning an arrow array. uh on the second implementation same idea we need to do it in polars here uh you see that for this example I can read directly the the column as polar polar service which is arrow interoperability with polars and I do the I do the computation which is the same thing like what I did with arrow

**[15:41](https://www.youtube.com/watch?v=Jho624IrxpM&t=941s)** what I did with with the rest of the uni-ode data or SDR normalize and I save the result to arrow and the difference mapping arrow. Mapping arrow gives you a bit [snorts] of uh more control actually. So if you want to call it you do dataf frame dot mapping arrow the function that you want to call and you need to provide the output schema without it uh it won't run. The idea as a computation is the same. What changes is that you process the you process in batches. Uh a note here that uh when I first tried this way uh I passed the whole data frame which is of course wrong because uh the computation increases

**[16:30](https://www.youtube.com/watch?v=Jho624IrxpM&t=990s)** significantly. So let's see the results on this. The results are this. And now I will try to remember what the next slide writes by heart. The first thing that you that I observe is that uh for the spark udfs uh I gain around 10%. So the arrow transport versus pick gives me around uh 10% 3 seconds. Uh the second thing I see is that pandas udf and pandas [snorts] udf vectorzed are almost equal. And this doesn't make sense. actually it makes that because if you read the code you will see that str nor normalized from pandas is not vectorzed so it's calling the same thing like uni-ode data the uni code data

**[17:18](https://www.youtube.com/watch?v=Jho624IrxpM&t=1038s)** library and then we have uh mapping arrow which has which is faster over polars and this is uh sorry mapping arrow which is faster over arrow UDF and this is due to the fact that uh there is some overhead head udf overhead that you need to do. So you take the column, you pass it to the function and you return it back with mapping arrow, you're providing the the schema. So you're having the schema, you're doing a transformation and as you see the gap is really small. So this is a result on a single column and this is what I told you and also okay for this case pi arrow and polars

**[18:07](https://www.youtube.com/watch?v=Jho624IrxpM&t=1087s)** are within the same uh approach. Now I did the same thing but this time I passed more columns. I passed four I passed four columns. I won't show you the code because it's a for loop and it's the same for this case but I will go straight to the results and the results are this. So here the results become more interesting. Uh what I observe the gap between spark udf and spark udf optimized increased and and that's normal. It's it's something that I expected. Uh vectorzed here wins because we have four columns. So the classic uh approach with apply has more overhead. Uh you can see that for mapping arrow pi

**[18:58](https://www.youtube.com/watch?v=Jho624IrxpM&t=1138s)** arrow and polars have uh have a small gap difference of around 3 seconds and uh this is happening because and this is happening also in arrow UDF and this is happening because we have um the conversion gap although the read is zero copy then we have a conversion gap uh and that the gap between the fastest approach to the slowest approach increased. So uh in this case I will proceed with the next uh test which is a normalization which I remove also a specific uni code group and this is happening like that. So in the

**[19:48](https://www.youtube.com/watch?v=Jho624IrxpM&t=1188s)** beginning uh I keep the same structure. I just added that I don't want this specific category of uni code characters. Uh you will see here that I don't have a vector because uh it uses the ar module and the ar module of python doesn't support this kind of uh operations. Moving to moving to the arrow UDFs you see that uh we added a new line uh that's what I mean by low-level API for [snorts] py arrow I mean it's a bit more difficult and less expressive at least for me from what polars provide for me what polars provide makes more sense to what I have been uh used to in

**[20:39](https://www.youtube.com/watch?v=Jho624IrxpM&t=1239s)** spark And uh of course the same idea comes to mapping arrow that nothing changes. We work in batches and we we perform the the same computation and the results are this. So what we see here is that of course uh native code wins. That's the most uh visible aspect and wins because it's what I told you before that besides thinking uh what transportation you have or what is the python for loop overhead you need to think how you write the actual computation. The gap increases a lot more than the

**[21:27](https://www.youtube.com/watch?v=Jho624IrxpM&t=1287s)** previous case. Still we have the same amount for arrow transport and we expect that the work that needs to be done in the side of Python is more. So this is for uh let's say string normalization and I go back to the problem of HTML cleaning which was the beginning of my my idea here. I used actually the best library that I know. I I changed to Lexore and this is the the method that I use that we use for cleaning. Nothing fancy. I mean it's it's a very easy method to write and we start calling uh this method.

**[22:20](https://www.youtube.com/watch?v=Jho624IrxpM&t=1340s)** Again we do it with uh spark udf spark with udf optimized and pandas udf. We follow the same approach for arrow udfs and the and the thing here to note is that uh in this case there is no native kernel neither in py arrow nor in polars. So what we do is that we call the main function that does the transformation and we convert the column to a list. So inside here, do you believe that uh that this is going to run fast? I mean it's still it's still inside the Python loop. And the same idea for mapping arrow only this time as always with mapping arrow

**[23:10](https://www.youtube.com/watch?v=Jho624IrxpM&t=1390s)** we do it uh with batches. So the benchmarks are this [sighs] uh and the result becomes interesting in a sense that from a first point of view you see an outlier. We'll see why. And all of them are being quite close. So literally you could have used anything you wanted of this. Even a spark udf wouldn't have any let's say disadvantage over the the other UDFs or mapin arrow. Why this is happening? This is happening because here uh the transport part is much lower over the computational part. actually

**[23:59](https://www.youtube.com/watch?v=Jho624IrxpM&t=1439s)** what where we spend the time here is mostly on the computation part. Now why uh spark udfr optimized is that much slow and is an outlier. This is happening because here we have variable length strings. We are making a batch and we are trying to pick from these bots. This is simply not efficient in this case. It is efficient for example for uh small strings like names and so on but for variable length strings that can be very very long it's totally inefficient and you see here and you see also sorry that uh in difference with the previous example the compute part is heavier in the norm in the normalization part the

**[24:46](https://www.youtube.com/watch?v=Jho624IrxpM&t=1486s)** transport part was a big aspect because the computational part was lightweight. And I move also to let's say string similarity also here uh I tried to use the best library actually I use cy deflib and not the deflib from python. Uh actually uh I think that when I tested the deflib it was two times slower. So by changing only the the library I I gained a [snorts] benefit of uh 100%. What I do is that let's say that I want to compare two full names. The idea is that I will compare the f the first with

**[25:35](https://www.youtube.com/watch?v=Jho624IrxpM&t=1535s)** the second and then the second with the first and from their scores I will get the mean of it. H how I do that? I take the the first name or the second I split it and for the parts that I have split I do the I do my computation I sequence matcher works uh with longest uh common substring which is a dynamic programming problem and uh this is the heavy part here that we need somehow to make this part faster. But is it possible to make a dynamic problem programming problem faster? That's a good question and we will see. So again we follow the same approach. Uh

**[26:29](https://www.youtube.com/watch?v=Jho624IrxpM&t=1589s)** in this case we just pass let's say extract or zip zip the names. Nothing really different from the previous case because we have a function and we call we call this function. We do the same uh in pi arrow and polars and in this case uh in polars we pass a strct and we map it with the elements and we do the same also for uh for mapping arrow. going over the the results uh what do we expect? I assume we expect something like that. So we have come towards uh the problem that we have previously and the problem

**[27:19](https://www.youtube.com/watch?v=Jho624IrxpM&t=1639s)** that we have previously is that I have a heavy computational problem. So no matter what I use the result is always going to be the same. But there is a butt here and the butt is what what got me thinking is I want to make this faster. Can I do it? And the answer is yes. So I changed a bit the approach. Uh and by changing the approach I mean the following. Instead of uh doing the stuff with a for loop and passing it to sequence matcher, I said if I want this to be vectorized, I will do the following. I will explode

**[28:10](https://www.youtube.com/watch?v=Jho624IrxpM&t=1690s)** all my columns. I will run them. I will do okay everything that I do in the previous in the main uh method. I will run it for one name and for the other two times. I will join the results and I will run the longest common substring. Uh I will join the results and I will get it back. The good thing of that is that polars has a plugin which is called PDS. It has this functionality and it's actually quite optimized also for for space. uh and now I can even write this natively but okay but I can use arrow UDF and the results become something like that so when I go into the vectorzed space

**[29:02](https://www.youtube.com/watch?v=Jho624IrxpM&t=1742s)** I get around 2.2 to performance increase. Amazing for something that does an explode in the group by I mean explode in spark well it's not happening in spark here it's happening in uh in polars would be quite computationally costly so why this is happening this is happening for two reasons the first reason is that the big the heavy computational part is the part that h it was optimized by running it into native code in this case rust which is using rayon parallel threading and so on and so on. The second part is that how explode by works uh in arrow and in polars and the idea

**[29:55](https://www.youtube.com/watch?v=Jho624IrxpM&t=1795s)** is something like that. Let's say that we have this table and arrow works in buffers. And what I mean by buffers, they have a buffer which is offset and a buffer which is data. For integers, you don't have this problem. You have just the values as a buffer. But for strings, let's say, you have the offset, the buffer offset and the data. What that means is that the offset points to you from where the the string starts and where it ends. And the list of course is a nested structure of the same idea. So what is really happening before the explode is uh the diagram that you see there uh you have the the two the two

**[30:44](https://www.youtube.com/watch?v=Jho624IrxpM&t=1844s)** columns row id and name and then for the rest which is a list you have the offsets which are pointing really the strings which are continuous in memory. So when you explode what you do is in the end you just allocate some new uh some new rows for the other columns but for the nested structure you are using again the child array that you have and it's just a a reference count. It's not a copy. So this gives you the the opportunity not to lose time with an explode, not to be computationally uh big and of course you drop the offset the the offsets buffer because then you don't have a list uh you don't need it

**[31:32](https://www.youtube.com/watch?v=Jho624IrxpM&t=1892s)** you have you don't have something nested you have a flat you have something flat if we check the same for spark h the idea is this the idea of the exploding is the same but here you carry with you it's the same that I was trying to explain you in C uh locality is that you carry the whole row with you. So you cannot say that oh from this row I want this part. So if you want to explode it you will explode everything. You will create many many objects of uh of the originals. Uh so takeaways when your uh function is compute heavy

**[32:21](https://www.youtube.com/watch?v=Jho624IrxpM&t=1941s)** and is a Python call per every UDF type converges and I think that this is clear from my results. Uh the real win is if you can avoid the Python loop. So if you can find a way to do it natively either in C, C++ or Rust that's very good. And you need to match the tool to the problem you are trying to solve. And this was my presentation. Thank you very much for your attention. [applause] Also from my side, thank you for this amazing talk. Like we have questions and people can also use still use talks.bon.d to um ask question. The first question will be like a very long

**[33:10](https://www.youtube.com/watch?v=Jho624IrxpM&t=1990s)** question with two sub questions. Like the first question of the sub question is how much how much this approach bridges the gap between native spark functions and udfs and the second of those did you try to write a native spark function as an udf and compare it with a native spark function. So uh for the second h I have not uh done it to run a spark native function as a spark udf function uh but there are presentations uh from the apache spark uh community that they have done that and they saw uh real improvements and for the first one also I it's something that I have not tested uh I'm not sure if he means actually

**[33:59](https://www.youtube.com/watch?v=Jho624IrxpM&t=2039s)** to write specific natively in Java uh or scala and uh do the comparison but uh I have not done it also. >> Okay. I see. I see it was quite an early question so it might be h would have also been answered by your talk because you really benchmarked it which was really nice. Sorry. Um does it make sense to use parallel polos execution given the fact that spark already execute one execute pro process per physical core? I am not. Should I get it? [laughter] >> Sorry. Should I repeat it? >> Yes. >> Does it make sense to use parallel polos execution? >> Okay. >> Given the fact that Spark already executes one executor process per

**[34:49](https://www.youtube.com/watch?v=Jho624IrxpM&t=2089s)** physical core. >> Okay. Uh it depends. So polars can use is multi-threaded on a single node. Spark uh distributes the workload. So for example in this case uh the benchmarks that I have tested I have done them in a single node of eight cores. Okay I could have done them in almost everything for the stuff that they are for the the the last example which is uh native I if I start adding more nodes of course I will paralyze more the problem. So I expect even more to drop but I wanted to keep it uh uh stable the benchmark to be accurate. But yes uh you you can parallelize but

**[35:39](https://www.youtube.com/watch?v=Jho624IrxpM&t=2139s)** uh the thing is that polars parallelizes only in a single node. It's not distributed for distributed they have polar cloud. So in this case what you do you use either mapping arrow or arrow udf to distribute the the problem to all your worker nodes. For example, I think this um answers the question. So like there's no question left anymore. So I think you will be around here still in the venue the full day. If you have questions arise like later on just approach him also connect with him on LinkedIn and you always open to answer the questions. >> Yes. Super like this was like the last talk before the lunch break and now I want to well give you give you a pause and then have a nice lunch break. Thank you.

**[36:29](https://www.youtube.com/watch?v=Jho624IrxpM&t=2189s)** [applause]
