---
id: lwTfY3Eh1dw
title: "Embedding Data Science in IoT devices with MicroPython and emlearn [PyCon DE & PyData 2026]"
slug: embedding-data-science-in-iot-devices-with-micropython-and
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Jon Nordby"]
channel: "PyData"
duration_min: 27
published_at: 2026-08-04T22:20:06Z
video_id: lwTfY3Eh1dw
url: https://www.youtube.com/watch?v=lwTfY3Eh1dw
youtube_url: https://www.youtube.com/watch?v=lwTfY3Eh1dw
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Inference, serving & GPU infra", "RAG, retrieval & knowledge"]
transcript: true
---

# Embedding Data Science in IoT devices with MicroPython and emlearn [PyCon DE & PyData 2026]

**Jon Nordby**

`PyData` · `PyData` · `2026` · `27 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lwTfY3Eh1dw) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Jon Nordby explain how to leverage MicroPython and emlearn to embed powerful machine learning models directly into low-cost IoT devices for a local-first approach to data science.

Speakers:
Jon Nordby

Description:
Embedding data science into IoT devices is achievable using MicroPython and specialized libraries to overcome the memory and processing constraints of microcontrollers. A primary challenge is implementing machine learning on hardware with limited RAM—often around 1 MB—which precludes the use of standard libraries like scikit-learn or Keras. To solve this, emlearn converts scikit-learn or Keras models into efficient C implementations that can be deployed as .mpy files, allowing for local activity recognition using accelerometer data.

For a standalone smartwatch prototype using an ESP32-based device with 16 MB of flash and 16 MB of RAM, a local-first data architecture is required to store multiple days of sensor data. This is implemented via a time-series data lake using Apache Hive-style partitioning, which organizes data by day, hour, and minute. This structure allows the device to retain high-resolution raw data for short periods while keeping processed machine learning predictions for longer durations. Performance tests show read speeds between 100 KB/s and 250 KB/s, which is sufficient for querying a full day of data in approximately 10 seconds.

The system manages concurrent tasks—sensor readout, ML inference, data storage, and web serving—using the asyncio library. To prevent data loss from sensor buffer overflows, tasks are kept under 100 ms, and the MicroDot web server is used to stream data in chunks. The user interface is served directly from the device using Preact and a minimal version of Plotly (250 KB). While the system supports external integration via HTTP or MQTT, implementing strict timeouts is necessary to prevent network latency from blocking the single-core processor.

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

*4,570 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=6s)** Yeah. So we will be talking about very small devices. I think it's one of the few talks about hardware related uh at this uh event. Um so uh if you didn't know um Python will actually run on a small device like this. You get smartphone watches or any other form factors devices you can uh put on battery or have around. So we'll see a little bit about this today. Uh so just as a question has anyone here uh played with microython before? Yeah there is like maybe a a fourth so you will hopefully learn something and uh you that haven't played with it will definitely learn something. So I work for a company called sound sensing. We provide um sensors for monitoring ventilation units. So our customers are operators of buildings like this. So we

**[0:55](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=55s)** notify the operations team when there's something weird and we use microython for prototyping new sensors there and also of course we use python for all the machine learning analysis anomaly detection and back end but today I'll be talking about a side project of mine I have had now for seven years already about uh doing machine learning on microcontrollers and for two years we've had microython support in this open source project. So the in this talk we'll talk about uh making a smartwatch as a standalone IoT device. Like if you have a smartwatch today uh they are mostly they're very dependent uh on their on the phone and on cloud services basically like very very small part of the system is actually on the watch. So it's interesting to see like

**[1:44](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=104s)** okay with Python with MicroPython uh and this taking a local first approach how far can we go and what are the bottlenecks currently in the ecosystem because I'm trying to expand the ecosystem for data science on physical hardware with microython um so we want to make some hackable device we're not making a product we're not making like something super polished and we want to understand possibilities and constraints and we want it to run Python we want to be able to do some machine learning with activity recognition. So we can tell you what have you been doing in the last hours and days. You can do some statistics on that. Um and it should have a few some days of data otherwise it's it's not that interesting and that causes some challenges. Um for a small device and it should be able to serve the um user

**[2:33](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=153s)** interface as well from itself so that you don't have to have an app or a server that you install at home or a cloud service etc. But ideally should all be uh from the device and but optionally you should be able to integrate it of course if you want to you should so it's local first but not uh not necessarily you can choose if it's only local. So uh hardware there's lots of possibilities these days if you get started with microython I would recommend going with some ESP32 based device. Um they're cheap, affordable from like €3 uh to uh this device is like maybe around uh 50 uh in total but has a lot of sensors and devices and things like that included touchscreen etc. So this is on kind of like a higher end of a microcontroller. Um so it has 16 megabytes of flash for

**[3:22](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=202s)** our program data etc and uh 16 megabytes of RAM which for microcontroller is a lot. um but it uh we'll see how far we get with that and for lockometer which will be our primary sensor and Wi-Fi which will be our connectivity. So microython is a independent implementation of Python 3. It doesn't share any code with CPython. Um it has uh quite surprisingly good compatibility. Um it support devices that have at least 128 kilobyt of RAM. It's mostly fun if you have like one megabyte or above. It's a bit um tedious below that in my opinion. Supports a lot of different devices. Um ESP32 is a great start. The Raspberry Pi Pico etc. is also a great

**[4:12](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=252s)** start. Um I'm not going to talk that much about Micyon. I give a talk at FOSM which you can u if you're interested in that. Um but the basic uh premise is it's uh you install a pre-built firmware for most devices. you will find that um plug it uh in your device. Uh the tools for ESP32 is in it's in pipi. So it's very easy to get if you're a Python developer and also a tool for uh like talking to your device called MP remote. Um and then you you flash it and you have a prompt you have a ripple on your physical hardware and it runs completely standalone on that device. Uh which is quite amazing. Uh and you can of course use an IDE if you want but this will get you started and there's some interesting uh lots of functionality. It's like

**[5:00](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=300s)** comes with you could say batteries included from the Python perspective. Um interesting here is we want a file system so we can store data and um this MP remote is useful for transferring for example our configuration our machine learning model etc. we can transfer via uh MP remote and also has a package manager. Uh they tried to use Pippi for a while but now it's a dedicated uh tool and repository which is very uh tailored to these small devices. So you can install packages uh like this uh either from like a common repository or from a specific GitHub or a specific file just on HTTP and you can also install native C modules at runtime. This is a very unique functionality. So you can actually extend your not just with Python code but with the C module that

**[5:48](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=348s)** expan exposes um a Python interface and this is very powerful uh and I haven't seen it on other uh embedded devices. Uh there is a little uh data science ecosystem because of the uh the CPI is different from CPython but also like we have ex we have typically 1 megaby of of RAM. Uh none of these libraries will run with 1 megabyte of RAM for sure. They barely run with 100 megabytes of RAM. Um so uh there are alternative implementations. I maintain em microython which basically scikitlearn for microython. There's something called open mv which is very similar to open cv. Um and there is u which is a very compatible implementation of numpy. Um and there's like a lot of tools around that we're um

**[6:39](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=399s)** building and I'll show you a bit more today that we needed to build for this project. So emarn microython uh has two components you there's a library that you install in python so that you can convert your scikitlearn or kas models onto an efficient um implementation which you can deploy on device and we support both C deployment and microython deployment and it's a single MPY file so it's just you can actually install that at runtime you don't need to rebuild your firmware etc even though it's uh mostly implemented in C for the efficiency Um today we'll show just a little bit about this uh activity tracking. I've given uh two talks about that before. So I'm also going to uh kind of skip through it quickly. But typically this

**[7:29](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=449s)** is classical pipeline. You separate some sort of the uh the orientation. So how are we how are we uh standing or down uh from the extometer data and then the residual of that is basically an estimate for the motion. Uh without our gyro you can't do like very good um positioning but it's good enough for activity detection. So then the output will be uh this typically these kind of classes and there's uh examples um in the repository for coupled common data sets. So you can use that pre-trained classifier although make sure that uh sometimes you need to uh reconfigure like the scale of your data and also um uh axis orientation might be different in different devices. So that

**[8:16](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=496s)** that can be critical. Uh there's many other examples for memor of course and these two talks go in detail about activity tracking with micro. Um so uh on our wish list how are we doing so far? Um, so yes, it's possible to um, uh, run Python on these kind of devices, which is already super cool and like that opens a lot of possibilities if you already know Python. And you can get off-the-shelf hardware as well, so you don't have to be an electronics engineer. You don't have to do a lot of soldering to get started. You can just plug it in via USB and and you're up and running. Um, it's possible to do activity recognition uh, with the EMR microython. There's examples for that. But then how about the the the next pieces?

**[9:06](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=546s)** So uh that's where for this project there's a repository that's linked in the in the conference talk page there's a link to a repository where I've been experimenting and I found very quickly that you know in order to have multiple days of data and then be able to query it and so on we need some sort of representation which is not just like one flat buffer. we need to be able to continuously append uh to the end like the current data um but be able to when you open the UI uh query back in time or select time. So uh created a small um time series uh database or time series u data lake um using like a parti hive style partitioning. So you partition based on the the day, hour and potentially down to minute if you have

**[9:54](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=594s)** very high resolution data. And then you can have different resources like this. So that um you can do uh you might keep your raw data just for you know some hours but then u the outputs of your machine learning model you'll keep for uh several many days maybe even a month or maybe even longer. so that you have this um uh granularity and you can in the small space that we have fit both a long context but also a rich uh raw data. Um so this is uh in process of being moved to this repository uh so that we can have it as a general um tool in the microython data science land. I tried row based and columner chunks and um columner chunks [snorts] is nice for trying to compression etc but it didn't work so well. So I'll talk about that.

**[10:44](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=644s)** Um so this is just like typical API. So you you're we append all the raw data and then when we have when we have enough uh data for a whole window typically like 4 seconds that we're going to classify the activity we will um process the window which just a classification uh sorry it's just pre-processing of data we store those uh features that we have extracted and uh we also do a prediction and we store the classes that we get and um uh yeah this is the main part like we're pushing pushing pushing And then we have an API which we can get long periods of data which will be for our UI. Um so the key is performance right we don't have a lot of uh a big device. Um so uh I tested and we were able to read around u u 100 uh kilobytes to 250

**[11:37](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=697s)** kilobytes per second which is not that much if you think about in in the normal scale of things but it actually it's 100 data points 100,000 data points per second which means you can do two hours of one resolution data per second if you're willing to wait uh 10 secondsish then you will get a whole day um or you can get one year of one hour resolution data Yeah. So that's with 10 columns. So this is already quite okay. I was hoping to maybe get 10x of this but it's it's already at a useful level but and it's really IO bound. So I found that reading these chunks even though I tried to size them well according to the flash precision and so on it's uh it's really the the reading uh that takes time. Uh and that also influenced compression and uh I didn't raw accelerometer data which is the highest resolution takes the most

**[12:25](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=745s)** space. I only got 5% net savings with the compression. So it was not that great. We'll see if we can do better. But it's possible to do 24 hours with the raw data without compression and still have space for our other data and our front end and our part of firmware etc. So I find found that very um successful. Um then we need to serve our web interface. So there's a project called micro dot uh which is basically a flask style web server implementation for microython. It's super well documented, uh, very robust, has really good features that you need for these kind of devices, like being able to do streaming, uh, so you can chunk up your, uh, response and being able to serve pre-ompressed files, so you can serve the gzip, uh, pre gzipped static assets,

**[13:16](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=796s)** for example, for your, uh, JavaScript, which tends to be quite big. Um, yeah, not going to go too much, but uh, here's how to do a streaming with that. It's it doesn't support asynchronous generators which is would be of course even nicer but that's not supported in micropython I think. Um so then you can plug that together um and you have an API and that you can uh query to get this kind of graphana like view. So we're still very much hacker mode. It's not a very pretty uh interface but this exposes the features that have been um um computed as well as the predictions. So you can choose which uh what you're looking at and I'm testing it on the device and in a few seconds you can load uh 24 uh four hours or a few days of data. Um I use

**[14:05](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=845s)** plotly uh which I I like it a lot. It's very powerful and nice for interactive. The default one is like over 1 megabyte. So it's it really hurts on this device. But there is a minimal um JavaScript as well which has most of the things you you want and that's just uh 350 kilobytes of fitness and we use pact for the UI which it's like react but you don't have to do a build step. Um important here is like how we're doing multiple things at the same time. where we are uh collecting data, analyzing data with machine learning, uh pushing that into a data store and then uh we might be someone might connect to the web interface and uh want to look at the data. So how is this done in practice and super nice in microython is that it supports async.io. So you can do

**[14:53](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=893s)** this at least conceptually in the same way that you would do with Python but we do have typically more um stringent um uh timelines. So so uh async io is cooperative scheduling which means that it's important that the individual tasks are rather well behaved that they yield at some point so that other um tasks can come in and do some work. uh otherwise they will starve each other and this is especially critical for the sensor data readout because if you uh fill there's a buffer in the sensor itself and if that is filled up you're going to lose samples you're that data is forever gone right there's no way of catching up at that point uh thankfully in this device there's a

**[15:41](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=941s)** rather large uh buffer can take around 100 samples so that's around 4 seconds at 25 Hz sample rate so that's like quite comfortable but you probably want um I haven't added the user interface yet but when I have on that I I want to have responsivity better than 4 seconds right so um it's a general recommendation good practice to keep all kind of chunks of work under 100 milliseconds or so or even a bit lower if you if you can um but that means that if you have longer tasks like for example when we are responding to like oh give me all the data for the last weeks from the web user interface that needs to be chunked up so that's why the streaming is critical when you are fetching from the uh data store. So then yeah the whole process takes maybe 4 seconds or maybe more. Um but it's done

**[16:30](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=990s)** in a way that um the micro dot will actually yield to the async.io runtime uh in between uh chunks. So then the um task that does the sensor readout get it just a chance to read. uh but it is critical here to use the buffer in the uh sensor. If you didn't do that, you would basically have to your deadline would be now uh 25 hertz. You could you couldn't miss and even if you would get a little bit of delay, you would actually get jitter on your data. So this is a really key techn um key part of this kind of system to make it feasible. Um there are ways to do with interrupts etc. But uh I would always recommend going with um FIFO based approach for this kind of advice even if

**[17:18](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1038s)** you would do this in in C. Um yeah so async.io but um the very [clears throat] familiar but keep deadlines in in mind and you actually want to guarantee the worst case and that if you have multiple tasks that can be multiple things before your critical task comes in. Uh that's general and bettered uh practice. Uh but do this and you will kind of be uh in okay spot. Um so that's a little bit further. So yeah it is possible to store um enough days of data uh when we do this hive style data lake uh type thing and we can serve it without compromising the ability to read and analyze data. Um and it's possible to serve some browser UI.

**[18:08](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1088s)** You basically need to dedicate like a 1 megabyte to your front end. Uh which is a lot in firmware uh terms, but it it does it is there is enough on this kind of device. So uh then we had okay what if we don't want just local what we would we do then? Oop. That's missing stuff. [laughter] Okay, I'll have to just explain it. So the UI that you saw that gives you this Graphana style is of course backed by a HTTP API. So you can just uh basically from your device copy that URL and uh as long as you're on the same network which you need to see the web interface anyway uh you can just curl that part and it will stream down a numpy array for you. So then you can do plug that straight

**[18:55](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1135s)** into your ordinarily data pipeline if you want to do some more analysis than you could do in this very basic um web interface. Um so that already that's kind of your escape hatch right as as a data scientist and that's very important to have this yeah you provide some standard functionality but we want a hackable device to just have a open hatch where you can u uh get the raw data. Um, so that's uh important and you can use that of course for backups or for syncing. So you can keep around one day of data on this device which means that maybe you want to have a script that uh when you're at home it will transfer it to a longer so if you want the raw data um but you might want to integrate it like into some more of a of a system and then uh you could push data via HTTP or MQTT. I mean you have a full

**[19:44](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1184s)** Wi-Fi capable device. Um, but here it's a little bit tricky if you want to uh make sure that you don't risk losing data. For example, if you have an external server, that could very well um spend more than 4 seconds um responding, especially in a in a downtime scenario. Or Wi-Fi can be unreliable, so you might fall on and off and so on. So it's always good to to if you have data that you want want to have guaranteed delivery, keep them in a in-memory queue or even in a disk based queue and then only remove it from the queue if you when you've gotten confirmation that you it's been sent and acknowledged by the server. And you really want to implement timeouts to that so that you're not you have a bound for how bad this influences the rest of your system because there is

**[20:31](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1231s)** just like one core. There is no there's no way for it to do anything else. um as I mentioned with um async.io So you need to kind of kill it if it uh takes more than a second for example. And unfortunately there there's a very nice um async io http package in microython a aio http um styled uh but there is no timeout support. There's a nice to-do implement timeout in there. [laughter] So that's a possible contribution if someone wants to you know do that. Uh so I unfortunately cannot recommend that but that's like a Python wrapper on top of a socket implementation in microython and that has timeout support. So right now you would actually have to uh probably manually do your uh HTTP uh request with the socket if you want the

**[21:20](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1280s)** timeout help. Uh in MQTT it's a little bit better. The simple MQTT server has uh timeouts uh built in that would be typical for ingest or sending data to some IoT cloud platform. there are many nice ones that you can get like free plan and integrate if you want. Um so yeah little bit stuff that we should improve in the microython um community for these use cases and that's the purpose of these kind of uh things to find what we need to to fix to to make it really uh good. So yeah it's possible to of course do get or um push with uh this with some caveats if you want to do it properly with timeouts. Um yeah that's I think um all I had. So to to summarize on this like experiment

**[22:10](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1330s)** uh we are don't call me now. Um we are it's possible to build uh feasible to build a standalone device with microython. We have the hardware easily accessible uh affordable. Um there is a lot of uh open source libraries available that you would need for this. You have machine learning models implement um implemented. Uh you have web servers, you have uh UI elements uh that you can use and with this grade of like device which is not like crazy expensive. Uh you can kind of use quite standard things like plotly for example. I was surprised that I that actually um worked out that I could fit that and you can use your existing again your existing skills as a data scientist. Um

**[23:00](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1380s)** and yeah so I think it's was very very good and then one new thing we needed was this hive style data lake and that's now uh going up on GitHub so that we can have uh more nice things in the future. So thank you very much. [applause] [applause] >> Yeah, thank you Yan for your great talk. Um uh we have some question from the audience and so the first question can I extend microython with rust as easily as with C? >> Uh yes but you do need that C kind of wrapper. So um uh all all yeah that's generally the case. Uh so you just need a little skeleton around with the with C

**[23:48](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1428s)** around your uh Rust code. There is also a project that actually does Rust to Wasam and has a generic uh binding layer uh that you will find that could be another way that's a little bit more experimental but could be interesting also. >> Okay. So next question. Which data set did you use for training? uh I used the PA map 2 data set. Uh there's also in the examples I think for UCR UCI H which is uh also very popular old and not so big data sets but they have like typical like like everyday activities at least little selection. >> All right. Um not really a question but like two people are like asking like

**[24:36](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1476s)** will you publish your slides on GitHub please? [laughter] >> Yes they will be there uh for sure right after the talk. >> All right. Yeah. And then it goes into that is your code snippets published for that prototype I guess. Yeah. >> Yes. That that's I think is already linked from the link in the uh GitHub u repo. >> And another question what is the battery life with this setup? >> Oh yeah. So that depends a lot. We didn't go into power management which is like big uh topic but uh Wi-Fi will kill you. Uh that will basically if you keep it running all the time probably will be like two hours. Uh so it's very bad. So you what needs to be done is you need to have a mode. So like it doesn't need Wi-Fi when you're just running around tracking, right? So you just want to

**[25:24](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1524s)** have a mode that is like oh I'm I want to connect to it now. Um so yeah and with that but there is that's one thing that is um I didn't have it in my slides in async.io So there is no integration with the sleep functionality out of the box in microython. It would be nice to have. But there is an alternative implementation uh called async.io alt from Peter um hinch. He writes is has super good tutorial about async.io and microython. And that one has power um power saving support. So you can like swap it out. And that's uh I haven't tested it for um full day or full 24 hours, but I think we'll need that in order to reach uh 24 hours uh or like 24 hours to 48 hours um uh with Wi-Fi off

**[26:17](https://www.youtube.com/watch?v=lwTfY3Eh1dw&t=1577s)** or at least off most of the time. You can do for example wake up 5 minutes uh dump your data and then uh uh go back or disable Wi-Fi again. >> All right, I think that's it. Thank you so much John for your talk and good [applause]
