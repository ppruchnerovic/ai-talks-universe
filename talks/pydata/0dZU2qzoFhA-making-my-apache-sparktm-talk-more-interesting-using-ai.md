---
id: 0dZU2qzoFhA
title: "Making my Apache Spark™ talk more interesting using AI [PyCon DE & PyData 2026]"
slug: making-my-apache-sparktm-talk-more-interesting-using-ai
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Celeste Horgan"]
channel: null
duration_min: 24
published_at: 2026-08-04T22:21:06Z
video_id: 0dZU2qzoFhA
url: https://www.youtube.com/watch?v=0dZU2qzoFhA
youtube_url: https://www.youtube.com/watch?v=0dZU2qzoFhA
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Data engineering & MLOps"]
transcript: true
---

# Making my Apache Spark™ talk more interesting using AI [PyCon DE & PyData 2026]

**Celeste Horgan**

`PyData` · `PyData` · `2026` · `24 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0dZU2qzoFhA) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Celeste Horgan transform a technical Apache Spark presentation in real-time using AI to demonstrate the power of dynamic data pipelines and the Cortex Code CLI.

Speakers:
Celeste Horgan

Description:
Apache Spark serves as a versatile transform layer for large-scale extract, load, and transform (ETL) pipelines. It is particularly effective for processing massive datasets, performing in-stream joins, and managing data through a stable deployment platform. While it utilizes a Java Virtual Machine (JVM) and can be resource-intensive, its ubiquity makes it a standard tool in data engineering. Key components include PySpark, which utilizes data frames to organize data into named columns, and Apache Parquet, a columnar file store that enables high-speed bulk lookups by accessing specific columns rather than scanning entire rows.

A practical application of these tools involves building a visual inference pipeline to detect patterns in image data. In one implementation, a pipeline processed 62,000 images stored as Parquet files sourced from Hugging Face. By training a visual inference model and using pandas for parallel processing, the system identified specific animals and output the results as a JSON file intended for a Kafka topic.

To enhance data accessibility for non-developers, the Snowflake CortexCodeCLI coding agent allows users to interact with Snowflake environments using natural language. This tool integrates with specific warehouse roles and permissions to assemble data views without requiring SQL knowledge. By analyzing datasets—such as view counts and transcripts from EuroPython, PyCon DE, and PyCon US—users can identify content trends and generate data-driven insights. This approach addresses the gap between data availability and the ability of business users to perform independent analysis.

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

*4,238 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=5s)** Uh so my name is Celeste Han but we're going to forgive we're going to forgive the misprononunciation. I think Seline is a beautiful name. It means moon. My name means sky. We're going to survive. Uh this is making my Apache Spark talk more interesting using AI. Uh there's a lot of talk to get through in half an hour. So I'm actually going to make this a little bit interactive and choose your own adventure. I'm going to ask you to vote on which direction you would like this talk to go. We can spend more time in some places, we can spend more time in others. Um, with that said, uh, let's rock and roll. Uh, this is a weird slide that my legal team tells me to display. Look at all these words that I'm sure you're going to read. Um, so a little bit about the agenda. I'm going to give a brief introduction to myself. Uh, we're going to talk a little bit more about what's going on here and why I'm

**[0:52](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=52s)** giving this very weird talk. Um, we're going to do a bit of a talk within a talk. We're going to inception the talks and how much time we spend on that is going to be up to you guys. Uh, and then we're going to talk about our Snowflakes coding agent which is called Cortex Code CLI. It's in like super duper early preview. Um, and we can mess around with that and spend more time less doing that if that is what you guys desire. So, my name is Celeste. Uh, I was born and raised in Canada. My mom is Filipino. My dad is British. I've lived in various parts of Europe since about 2018. I've spent the most time in Berlin and more recently I moved to London to take the job at Snowflake. Um I've been described as an open source true believer which I will take as a compliment. Um I started doing open source in 2020 uh where I was actually

**[1:41](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=101s)** working with the Linux Foundation as a technical writer working on the Kubernetes project. Um and I just sort of fell in love with the ethos. I fell in love with the people. I fell in love with conferences and giving talks. Uh, and all of that spun into being a developer advocate for a company called Ivan, which if you are in Berlin, you've maybe heard of. Uh, I did started doing that in 2022. Um, and I've been with Snowflake since, uh, September of 2025. Um, I could be represented by this raccoon in the lower corner with a martini glass if you so chose. Um, so what is happening here? Why are there raccoons everywhere? Why was the talk description so uh scattered? Um, first things first, you're actually in a sponsored talk and Pyon is like a little bit weird in that they don't really indicate which talks are sponsored or not. Um, but I personally don't go to

**[2:29](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=149s)** sponsored talks unless I can help it and I kind of think they're boring. So, when I was asked to do this, I was in a bit of a conundrum because I was like, uh, but I wouldn't. Um, and so I really wanted to look at like why is that the case though? And I think there's three main reasons. one, it's a lack of alignment with the audience's interests. So, you don't have control over the content that you're seeing. And I think that's a huge problem. Um, it ends up being nothing but a sales pitch. And I also think that's a huge problem. I think especially at an open source conference from somebody who is an open source true believer to people who are spending their free time talking about open source things, like it's a bit of a problem. Um, and there's always a feeling of being talked at rather than talked to. So sort of the way that I'm hoping to structure this talk is that we can kind of like create what we're interested in together. Um so with that said, the next portion of this talk is

**[3:20](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=200s)** the talk within a talk. Um this is a talk that I gave at PI data London. No, not PI data London, one of Confluence meetups um in London probably about a month ago. It's as you can tell about Apache Spark pipelines. uh it is about adventures in raccoon detection and we'll talk about raccoons later on. So this probably can comprise half to maybe a little more than half of this talk if you so please. The other half of this talk um what I've done is I've pulled data on the top talks from the Euro Python YouTube channel, the PyonDe YouTube channel, and the Pyon US YouTube channel. I've pulled those basically by view count. Um, I've also pulled the transcripts of the top 50 talks. So, we can use um a little bit of data analysis

**[4:10](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=250s)** interactively together for better or for worse um to kind of look through that data and see if there's anything interesting in the trends that we can use to make this I think it's fine talk um a little bit more interesting. So, there's two ways we can go here. One, we spend a little bit more time on this Apache Sparks pipeline talk and we spend a little bit less time doing AI stuff. Or two, we do spend a little bit more time doing AI stuff. You can potentially embarrass me. Um, but I'm going to have you vote who wants to talk a little bit more in depth about Apache Spark today. Okay. Okay, that's like a third of you who wants to potentially embarrass me with AI. Hey, there's my people. Cool. So I'm going to try I've got a timer. I'm going

**[4:59](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=299s)** to try and hit like the 15 minute mark. It is important that you understand the talk so that we can understand how to improve it. Okay. Uh what I'm going to cut out is actually going through like the code sample. I'll just sort of show you what the end of this pipeline is and we'll focus on the content of the talk. Capich? Good. Cool. Uh so talk within a talk agenda. What is Spark anyways? What is Spark good at? Let's build a data pipeline. Question mark question mark. Profit. Um, so this talk was really geared at people who didn't really know what Apache Spark was but were maybe data engineers. Anyways, I think Apache Spark is a really really useful tool to know because even if it isn't the right the tool you would choose now in 2026, it is such a ubiquitous tool and it is such a sort of like Swiss Army knife of data tools that you will find it out in

**[5:46](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=346s)** the wild like two out of three workplaces. So what is Apache Spark? Um, I think it's really easy to misunderstand Apache Spark because it depends on what part of Apache Spark you're using. Um, I like to describe it as three raccoons in a trans coat or a Swiss Army knife because it's a lot of different tools that are kind of loosely tied together that help you do data things. Um, a lot of people use it for large scale ETL, extract, load, transform sort of pipelines. um it has a sort of offshoot called MLIB which is a very like classical machine learning inference situation so it's non-generative you can do a little bit of near time near real-time stream processing it pairs very nicely with CFKA for that um you can do sort of SQL based data analysis graph processing a whole bunch more there's like a really

**[6:34](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=394s)** really big offshoot of like pandas on Spark that you can do stuff with [snorts] um but and they're all kind of like loosely connected by like the Spark engine. Um, if you're coming new to Spark in 2026, the thing to know is that Spark is basically a sort of transform layer of superhero. Um, it's really really good at processing really large amounts of data and sort of doing instream processing like joins on large amounts of data. Um, I would say that it's biggest good quality is that it's also a relatively stable platform both in terms of like release cadence, maintenance, but also deployment. Um, and that's why it tends to stick around and why even if you would maybe not choose it in 2026, the f the chances that you'll encounter

**[7:22](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=442s)** it in 2026 are still pretty high. [snorts] Um, that said, it's probably about 15 years old now and we need to sort of, especially in 2026 and especially in the world of postgenerative AI, have a little think about where Spark kind of sort of sucks. Um, it's pretty resource intensive to run. It uses a JVM. So, it's, I would argue, maybe a bit more antiquated in its architecture at this point in time. MLIB, especially in the age of generative AI, is not the most useful library. these days. Um, and it really spark really kind of grew out of slashadjacent to Hadoop and the map produce projects and those are borderline irrelevant in modern data engineering. But I think the key thing to understand

**[8:10](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=490s)** Spark is an intermediary step. You never just deploy Spark. You're taking data from somewhere. You're doing something with it in Spark. You're probably joining it from data from somewhere else and then you're sending it somewhere else. It is a step in the pipeline and a lot of businesses find that it's a step that's very very hard to replace with anything else. That said, for almost everything that Spark does, there is a more lightweight alternative available. So, think about that. Um, very briefly, this is what the pipeline that we would be doing should do. Um, we are taking a very very large set of images. Uh, they're stored as paret files. These were found on Hugging Face. Uh, and we are looking for raccoons. So this is just like a very classic like look for a known pattern. So we need to train a visual um inference model. We're also

**[8:58](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=538s)** using a hugging face model in that regards. Um like I said, we're cutting through code time, but I will very briefly kind of show you what's going on if I can tame the browser windows. Wish me luck. [laughter] Come on now. This is what I get for not mirroring my display the way that the lovely guys in a do uh suggested that I do. [snorts] So, this is on me, everybody. Cool. Um, that's not working. So, I'm just going to read what's happening on this screen uh while I mirror my display because evidently the way that I wanted to do this did not work and you were right, guys in the back. Uh, thank you

**[9:46](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=586s)** and I'm sorry that I'm stubborn. Um so [laughter] so the way that um rude. Um [snorts] anyways the way that this works it is a very classic sort of spark pipeline. Uh we do a bunch of configuration. We prep the data. Uh we then take a subset of data of images that are just raccoons which all the images of raccoons on this presentation are. Uh we train the model saying this is the thing you're looking for. Um, and at the very end it processes through about 62,000 images uh using pandas to actually process in parallel. Um, and then it uh spits out a file. And let me see if I can get this to behave better. Escape now. Will you let me drag and drop?

**[10:36](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=636s)** No. Well, that's going to be a problem. Um, and it is in fact a problem that I am going to need to burn a little bit of time to solve. Sorry everybody. Mirror. Yeah, there we go. Okay, so this is the model. Like I said, we're going to zip and zoom through the model because we've got we got time to spare. Uh, we've got like 16 gigabytes of images of random animals. And I'll show you what the output ends up looking like. Um, so it's really just a JSON file. Uh all of these are designed to be written to a CFKA topic. Um and as you can tell tell by the fact that it's uh detecting Pomeranians, cats, the occasional chicken, it's a reasonably accurate

**[11:24](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=684s)** pipeline, but it could use some work. Um okay, carrying on with that because we cared more about AI. Um very briefly, uh again, bear in mind this presentation was made for sort of people who are new. Uh what is Pispark? Pispark is of course um one of the many language specific libraries um and I would say the key point that we care about is that Pispark functions a little bit differently than some of the other libraries and that's if you were to implement Spark um now the thing that I would really caution you is that the different language implementations of Spark do behave a little bit differently. The biggest one that I can think of, the biggest sort of discrepancy is that the Scallow library doesn't implement dataf frames. Uh but

**[12:11](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=731s)** Pispark does. Um so what is a dataf frame? Um anytime we load data into Spark and if we had gone through the code, we would have gone through this like a little bit more um bit by bit. A dataf frame is a blob of data organized into names columns. Um, if you've ever worked with Flink before, it's a similar idea of like whenever you sort of move data into a Flink pipeline and it asks you to kind of orchestrate them as a table, do a thing and then it sort of spits out like a temporary table. Those aren't real tables, but it's a table kind of for your benefit as much as anything else. Dataf frames are very very similar. It's really just a way of organizing data in such a way that we can perform actions against it in a sort of organized fashion. Uh so with very very few exceptions um we load data into Spark using dataf frames. Um

**[13:03](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=783s)** and again some of the other language implementations don't actually use dataf frames. They use sort of older constructs that spark was using before dataf frames. Um and that is something to keep in mind if you were to do a vanilla implementation of spark today. Um what is an Apache parquet file? Um it's an open source kilometer file store for big data processing. If you don't know what any of that means, that's totally legitimate. Uh, the key word to keep in mind is the word columar. Um, so typically when we work with database structures, we go row by row by row. And a row might have five or six different columns. So like name, age, address, whatever. So if we wanted to look up the addresses of say 100 people, we'd have to go row one, give me the address in position three, row two, position three, row three, position three. What a column data store does and why it is so so

**[13:52](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=832s)** useful uh for any kind of big data or any kind of analytics data is it lets us go please go to the address column and give me rows one to 100. So it lets us look up things in bulk very very quickly. Um Apache Parkhead is just a way of sort of storing unstructured data in a sort of kind of columar way. Um Spark works really really well with it. Um, pandas is a Python data analysis library. Again, we sort of use it to parallel process things. Um, as a part of this pipeline that we did not go through because we're more interested in playing with AI. Um, [snorts] TLDDR parallel processing. It helps us be speedy fast. Um, when doing the initial sort of run through this, it did take about 10 minutes, which is another

**[14:40](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=880s)** reason that we're not really going to run through the code right now. Um 14 minutes into a halfhour talk, we're right at the AI part. Um so let's talk about AI. Um Snowflake has introduced uh Cortex code CLI. Um it's a coding agent. Uh it actually lets you use whichever model you like. So if you have a particular model that you prefer, you can actually specify uh that Cortex use a specific model. Uh what Cortex really does for you is it knows inherently about your Thank you. um about your Snowflake environment. So if you are a Snowflake customer and if you have a Snowflake warehouse um it knows your roles within the ware within that environment. It knows what data you can and can't access. It knows what data you can't access and what roles you

**[15:29](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=929s)** might need to access it. Um and it knows and it can kind of assemble views of data for you. Um this is super useful. Um, so let's play with some data because I think that's easier to understand. Um, and again, go easy on me because this could go in many different directions. [laughter] So, um, I'm already connected. Um, we're connected to the Devril account because I work in the Devril or um, we're also connected to this Pyon Pan the analysis public schema. And I think first things first because none of you know what's in the schema. Can you tell me? Oh, I already asked. It's already here. Sweet. Um, so we have a title called Pyon videos. Uh, again, so I pulled basically

**[16:19](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=979s)** the name and the view count of Python videos on Euroython, Pyon D, and Python US. We have the tags for each of those videos. We have the transcripts for the top 60 by view count across all of those channels. Um, and we have a row of summaries. Um, also I lied to you. This transcript, it's the top 50 videos by view count and the top 10 that mention Spark. Um so by way of starting a thing to probably know about me is I

**[17:09](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1029s)** think I mentioned this a bit in my intro. Um I started my life as a technical writer. So I wouldn't call myself a developer necessarily and I learned a lot about data and a lot about cloud computing along the way. Um what I think is really really interesting about this that is maybe hard to access especially if you're a developer is that you don't actually need to know SQL. Um you can describe what you're looking for [snorts] and you can get a result without necessarily needing to know um the details. Um, so with that said, you have a sense of the data that is kicking around in this database. Who has a fun question they'd like to ask to help me improve this talk? Hands

**[17:58](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1078s)** up. Wow. Okay. This is not how it was supposed to go, guys. Okay. So apparently my talk should talk more about scalability and performance uh about integrating with other tools which it does thank you very much. Um and apparently this is my recommended talk title is Pispark versus X scaling Python and data pipelines for the real world. I'm going to put it out again. Does anybody have a question that they think would be interesting to ask? Yeah. >> [laughter] >> So within the scope of the data that we have, like ultimately any AI tool is

**[18:45](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1125s)** only as useful as the question that you ask. And in regards to this AI tool in specific, it's only going to be as useful as the question you ask can be referenced in the data that you have. So the question as you phrase it, how can I get a better audience? Is probably not going to be a useful question to ask this particular AI or really any AI because it doesn't know who the audience is. What we do know like I said is we understand the transcripts and we have view cones. Um so I think a better question that we can ask is have the most views and what do they talk about? And can you give me the top

**[19:32](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1172s)** three? And again, ultimately that's only going to be as useful. Okay, so Vim is a Python IDE developing Android apps productivity. Um, and interestingly, all three of these are tooling environment talks and no data are ML talks. So that's actually my data sourc's problem. Um, I apparently only have five minutes left. So, unfortunately, I can't take more of your questions, but if you come to me with the snowflake booth after, you can play around with this a bit more. Um, and I do want to cap this off with a note on AI skepticism. Uh, because who would describe themselves as

**[20:20](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1220s)** somewhat skeptical of AI? And I think this is important because I think I would describe myself as the same. I don't sit quietly with this and I don't look at this and go like, "Wow, amazing. How amazing is this?" I don't think we've accurately assessed our impact on society as a whole. I think that the environmental impact is really, really large. Um, I think that we're putting a lot of trust in these tools. However, um I was having a conversation with a good friend of mine uh who is a rather well-known SE s sur um probably about a month ago and we were discussing AI in specific and the thing that we both agree on is that the environmental impact is large but realistically it's on a downward curve. And I would also be remiss not to point out that it's on a

**[21:08](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1268s)** downward curve because the data supports that. Um the cost of training models is getting lower and lower. Um, so that's thing number one. I think you have to assume that that problem is going to get solved because that is in these companies best interest to do. Um, the other thing that I would say and I would say that I'm still probably quite critical of of this technology to be quite honest with you. Um, the thing that I noticed when we deployed these things at Snowflake that was really, really interesting to me is that it wasn't the developers who were doing the most work with these tools. Um, it was people in our sales organization, it was our solutions engineers who are talking to customers, um, it was our support teams, it was our IT teams, um, it was our marketing teams. Um, and I think you

**[21:59](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1319s)** sort of have to ask yourself why is that? Why aren't the developers interested in it? And I think it's not a lack of interest from the developers. I think it's that in departments where there aren't developers, there are so many problems that can be solved that no developer will ever want to look at because they think it's not interesting. Um, an example that I have is one of the things that I do at Snowflake is I run the open source programs office. Uh, and we have a pipeline that people have to get a certain set of approvals before we publish something as open source. And it's very very basic. It's security. It's security. It's IT. It's basic basic checks. And it's absolutely the kind of thing that can be automated. But nobody's interested in doing that. There's developer productivity teams in large companies all over the place, but

**[22:48](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1368s)** they're not interested in automating a pipeline for legal. But legal can do it themselves with this kind of tool. And I think that's why you're seeing so much adoption outside of developer tools. And I think if you're a data engineer and you're sitting here thinking, I'm collecting all this data for you. I'm storing all this data for you. I'm moving all this data for you. I'm processing all this data for you. Why aren't you making datadriven decisions? I think you need to maybe understand that it's because people can't. These tools are still too hard. And tools like natural language processing can help make that easier. To note, Snowflake is actually working on a tool spec like Cortex code, but specifically for business users that's still under total lock and key, but like watch this space and look up project

**[23:36](https://www.youtube.com/watch?v=0dZU2qzoFhA&t=1416s)** snowwork if you're interested or if you work with a large set of business users who are not developers and who have who want to explore the data that you have. Um, that's the talk. I think I'm on time. [laughter] >> [applause] >> Well, thank you very much, Celeste. Um, well, there are no questions. >> No questions. >> No questions. Uh, >> I'm chill with that. >> So, anyone maybe wants to pose a question or a remark? >> You don't have to. >> Okay. Well, in that case, thank you very much. >> No problem. >> Bye-bye. >> [applause]
