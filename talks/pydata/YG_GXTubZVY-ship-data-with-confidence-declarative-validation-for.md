---
id: YG_GXTubZVY
title: "Ship Data with Confidence: Declarative Validation for PySpark & Pandas [PyCon DE & PyData 2026]"
slug: ship-data-with-confidence-declarative-validation-for
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Ryan Sequeira"]
channel: "PyData"
duration_min: 28
published_at: 2026-08-04T22:20:14Z
video_id: YG_GXTubZVY
url: https://www.youtube.com/watch?v=YG_GXTubZVY
youtube_url: https://www.youtube.com/watch?v=YG_GXTubZVY
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Data engineering & MLOps", "Evals, observability & reliability"]
transcript: true
---

# Ship Data with Confidence: Declarative Validation for PySpark & Pandas [PyCon DE & PyData 2026]

**Ryan Sequeira**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=YG_GXTubZVY) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Ryan Sequeira demonstrate how to eliminate pipeline failures and ship more reliable data products using declarative validation for PySpark and Pandas.

Speakers:
Ryan Sequeira

Description:
Data validation in PySpark and Pandas pipelines often suffers from silent failures, such as NaN errors, unexpected null values, or duplicate rows resulting from joins. While existing tools like Great Expectations, Pandera, and Soda provide robust validation and observability, they can introduce significant overhead in terms of configuration, build times, and Docker image size, especially when only a fraction of their feature set is required.

DataFrame Expectations is a lightweight Python library designed to provide declarative validation that fails fast when data does not meet predefined criteria. It relies on three primary dependencies—Pandas, Pydantic, and Tabulate—while treating PySpark as an optional dependency to avoid version conflicts in environments like Databricks. The library uses a DataFrameExpectationSuite class to define expectations, which are then compiled into an immutable runner. This runner can validate both Pandas and PySpark data frames using the same set of rules, ensuring consistency across different data processing stages.

The architecture utilizes a registry system and a decorator-based approach to dynamically map expectation functions to their respective implementation classes. To handle different environments, the library supports tag-based filtering, allowing users to apply specific validation subsets for unit tests versus production pipelines. For PySpark, the library implements validations using filter functions to identify violating rows; if the count of these rows exceeds zero, the runner records the violation. Upon completion, the library provides a detailed exception containing a snapshot of the failing rows to facilitate debugging.

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

*4,158 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=YG_GXTubZVY&t=5s)** Thanks a lot for attending this talk. Uh I'm a data scientist at get your guide. Uh and part of my job like is like uh a team and I own and ship a lot of data products. Uh and I'm here to share the library I worked on uh last year to make this process more reliable. Uh so I'll begin uh uh with defining the problem that I'm trying to solve. Uh I'll briefly talk about some of the solutions that exist in this space. Uh I'll give you some context on our use case and why I had to develop this library. Uh give you uh a brief uh description of all the features that this library offers. And finally uh we go through the architecture. uh

**[0:53](https://www.youtube.com/watch?v=YG_GXTubZVY&t=53s)** hopefully I get some useful suggestions after the talk on how to improve it. Uh so let's start with the problem. Uh so in most data processing jobs uh you read the information from one or more sources, you apply some transformations on it and then you send it uh to production. It could be other external tables, dashboards, etc. And on most days uh things go as expected. Uh you uh there are no problems. Uh but then sometimes things go wrong and that's when you realize the impact your work has at your organization and over time like you have interesting anecdotes to share with your grandchildren. So uh yeah why does this happen? like

**[1:43](https://www.youtube.com/watch?v=YG_GXTubZVY&t=103s)** even though your code works uh in terms of uh processing data frames, there can be a lot of errors that go unnoticed. Um some examples are like nan errors like uh when your underlying data changes uh which can lead to like divide by 0 or square root of a negative number and so on or when uh you're trying to cast a non- numeric string to a numeric and so on. Uh and then you may uh have uh null values like uh missing rows or duplicates uh that might happen as a result of joins because of the underlying data. And by the time you uh find out like there's something wrong, it can be often like uh too late uh and the data has already reached production.

**[2:33](https://www.youtube.com/watch?v=YG_GXTubZVY&t=153s)** So recovery can be a nightmare. uh but don't lose hope because uh we can learn a thing or two from how reliable software is shipped in production. Uh so you uh have these common practices like unit tests um that help you validate your core logic uh check if everything works as expected. Uh then you have asserts that help you find if your system reaches an invalid state and uh the the side effect of this is that you also know something more about why your system failed. Uh you also have type hints uh and type checks to help find inconsistencies early on. Uh and these concepts translate well uh into data validation as well. Uh so you

**[3:24](https://www.youtube.com/watch?v=YG_GXTubZVY&t=204s)** could use unit test to test your output data frame. You could use asserts to iterate over all the rows and find if there is something invalid. Also apply asserts on aggregations on the data frames like sum, count uh etc. And then you could apply like schema validation uh to find missing columns or change uh in the data types of the columns and so on. Uh so these are not new problems and there are already like reliable solutions that you could use and depending on uh where uh you want to add tests or validations you have uh solutions with different complexity. So at a very function level like with smaller data frames you have solutions

**[4:11](https://www.youtube.com/watch?v=YG_GXTubZVY&t=251s)** like pandera uh then you as you move further like you have solutions like uh great expectations uh great expectations and soda also offer like observability in terms of errors uh then when you're working on a larger scale like processing billions of rows uh you have uh solutions from uh cloud providers like uh AWS uh data bricks and then uh at a platform level like where data engineers manage the uh warehouse uh you have more complex solutions at a platform level like Monte Carlo like in these solutions you also have automated tests like drift detection anomaly detection also you have uh data lineage freshness etc uh that they offer by

**[5:02](https://www.youtube.com/watch?v=YG_GXTubZVY&t=302s)** default and um most of these uh solutions that uh I'm going or the problem that I'm trying to solve is more in the function and the pipeline level. We'll focus on these uh in the upcoming slides. And uh each uh product or tool solves a different problem. Uh each of them has their own strengths and weaknesses and depending on your use case uh you live with the compromises. Uh so here's a brief comparison. I won't spend much time on it. And as a disclaimer like uh this library uh these libraries are excellent tools. Uh so don't cancel your contracts or cancel your subscriptions. Uh uh but I would like you to try dataf frame expectations

**[5:53](https://www.youtube.com/watch?v=YG_GXTubZVY&t=353s)** and let me know like your experience using it. Uh so what is this library about? Like it's a lightweight library that's uh that uh that's designed for one thing. It lets you easily define expectations on your data frames and it fails fast when the expectations are not met. Uh so I'll explain like our journey at get your guide and why I had to build this solution. Uh we had like very simple requirements. Uh we wanted to validate like pi spark and panda data frames uh both in production and in end to end tests. uh preferably like we wanted minimal configurations required for the tool so that our MLOps team didn't have an additional overhead uh and we didn't

**[6:41](https://www.youtube.com/watch?v=YG_GXTubZVY&t=401s)** want to restructure the code just for the test so that people working don't see it as an afterthought and we wanted the process to be frictionless so uh the solution we had in place was great expectations uh this was incorporated like before I joined get your guide uh the Reason for this was that it offers a large uh gallery of expectations for the most common scenarios and by expectations I mean like data validation tests. Uh it had good documentation like for most uh expectations and what I really liked about it was the reporting. So on failure you knew exactly which validations failed and you know uh it also gave you a snapshot of the rows where the uh valid where the error uh

**[7:31](https://www.youtube.com/watch?v=YG_GXTubZVY&t=451s)** was happening. So debugging became like an easy uh problem to solve. Uh but there were also some limitations with this library. Uh so we were using it mainly for the validation. uh but there was another cloud data observability solution that they offered which meant uh that the configuration uh itself was much more complex. uh so our MLOps team had to do additional configuration for checkpointing reporting etc which was an additional overhead uh because of the transient dependencies the build times were slower uh and also the docker images like the size kept growing uh the learning we got out of it was that we are putting in 100% effort to maintain this tool or to integrate this

**[8:21](https://www.youtube.com/watch?v=YG_GXTubZVY&t=501s)** tool but we were only using it for 20% of what it was designed for. Uh so our needs didn't match the tool. Uh but uh we had a good experience using it. So I took the best parts out of it and implemented a lightweight replacement. Uh it's called dataf frame expectations. Uh clearly I didn't put a lot of thought into naming this library. Yeah. Uh and why build yet another data validation library? So uh it was uh originally planned internally like we had clear requirements in mind that were not uh not met. Uh some of them were easy setup like we preferred to have like a dependency we could just import. Wanted it to be lightweight uh so that the CI

**[9:10](https://www.youtube.com/watch?v=YG_GXTubZVY&t=550s)** is faster. I could use it in unit tests as well. Uh wanted it to be easy to understand and declare the expectations. So the review process is simple. maintenance of this test or updation becomes easier. Uh we wanted it to be versatile so that you could use it in notebooks, unit tests, end to end tests etc. uh even the production pipelines and we wanted it to work well with pandas and pispark data frames. So I'll go through each of these and how I try to solve them. Uh so uh the library is implemented as a python uh library. So installation by default becomes simple just need a single instruction to install and it's also equally easy to uh uninstall it.

**[10:01](https://www.youtube.com/watch?v=YG_GXTubZVY&t=601s)** So there are three code uh dependencies like just pandas uh pyantic and tabulate. So fairly lightweight uh it all runs locally. There's no external uh integration required and pispark is an optional dependencies because if you're working with data fra uh data bricks you already have it installed uh like a custom version that you don't want to override uh in terms of readability like I tried to keep the structure very compact uh it's a declarative style of adding expectations so you import like a single uh uh class which is the data frame expectation suite. Uh and you add uh like simple expectations that are easy

**[10:49](https://www.youtube.com/watch?v=YG_GXTubZVY&t=649s)** to understand one by one. Uh and uh basically once you built a complex suite uh by combining these uh simple uh expectations uh you use the uh suite.build built to get an immutable runner and this runner uh can validate both pandas and pisp uh pispark data frames. So you don't need to define the tests multiple times like for different data frames. Uh the output is also equally readable. So you understand exactly which expectation is not met and you also get a snapshot of the rows where the expectations were violated. It also helps you debugging uh and al so in terms of versatility uh

**[11:40](https://www.youtube.com/watch?v=YG_GXTubZVY&t=700s)** because this is a Python dependency uh you could add it in your notebooks, unit tests etc. uh as a added use case like if you have multiple functions that need the same validations uh I also added like a decorator based validation uh as a benefit what it does is uh you also know exactly which functions are validated when you review them. Uh and one last feature uh uh was like there might be use cases where you don't want to run all the tests uh all the time. So I also added tag based filtering and what this does is essentially when you declare the expectations you also define all the tags uh that might uh that specify the

**[12:31](https://www.youtube.com/watch?v=YG_GXTubZVY&t=751s)** context under which these expectations need to run. Uh and at the runtime like when you build your runner you specify the tags that you want to apply as filters. Uh for example like in your unit test you might be working on a smaller subset of data and you might only want to check if your output has a minimum of 100 rows but when you're actually running it on production you might want to check if it uh has uh 10,000 rows and so on. So you can provide this context and the runner picks up uh the subset of tests and it applies it. Uh yeah. So uh that's uh most of the features. Uh we'll look at how this library works uh under the hood. So the first part like is how the expectations

**[13:20](https://www.youtube.com/watch?v=YG_GXTubZVY&t=800s)** are defined and registered. Most of you who use this library won't have to deal with this. But if you're interested, so it starts with an abstract class called dataf frame expectations. Uh you implement your expectation by extending this and specifically uh implementing the validate pandas and the validate pispark uh class. Uh what you need to do next is add a factory method which returns an instance of this uh expectation. Uh and to keep things decentralized uh you use the register expectation decorator which the register later use to identify all the expectations and add it to its dictionary. Uh so when you're actually authoring your own test suite uh the registry

**[14:10](https://www.youtube.com/watch?v=YG_GXTubZVY&t=850s)** serves as a lookup for it. Uh and the test suite uh basically when you call one of these expectation functions like expect minimum rows uh it actually dynamically calls this function in the sense that uh it calls the get attribute function with this function name. Uh it searches the registry uh if it exists over there. uh the registry returns uh uh of the factory method which uh the suite uses to create an instance of this uh expectation class and then it adds it to its list. The reason for doing this is that when I was authoring expectations uh I had to manually add each class uh each uh function like this and uh at

**[14:59](https://www.youtube.com/watch?v=YG_GXTubZVY&t=899s)** some point the code would be uh difficult to manage. So I switched to this dynamic approach. Uh and for type ahead search like I generate the ST files using a script. Uh so you don't have to know exactly which functions uh exist like the typehead search helps you find them. Uh finally uh once you've defined all your test suites uh you need to uh uh basically build uh the runner by calling the build function. And during this step is when you supply the tags uh and on uh initialization the runner basically uh filters through all the expectations uh and only selects the tag that need to be uh executed during this context.

**[15:51](https://www.youtube.com/watch?v=YG_GXTubZVY&t=951s)** And uh the final step is when you actually run your expectations uh using the runner and you pass the data frame. Uh during this step uh basically you the runner iterates through each of these expectations. It validates them one by one. Uh it checks if there are any violations and it keeps a record of them and at the end like if there are any failures uh you get uh an exception uh with all the details. Uh I know uh it's a lot to take in. Uh so here's a more compressed version of the architecture. Uh so you begin with uh an expectation which is registered in the registry because uh unmelding is important. Uh and then you use your suite which uh refers to the registry

**[16:41](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1001s)** like basically as a lookup and to build the test suite. Uh once this is done uh you generate a runner using the build method. uh and finally uh the runner validates the data frame and then you get uh an exception if there are any failures. So if you think like I piqu your interest uh if you found this talk interesting uh I please give this library a try. Uh I look forward to your experience uh using it and also open to feedback on how I can uh improve it. Uh, so I'll give you a minute to take a photo or scan the QR code. Uh, that's it. Uh, thanks a lot for your

**[17:35](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1055s)** time. [applause] Thanks a lot, Ryan. This was a very interesting and uh useful journey that you shared with us. I think it's one of the struggles we all have when working with large data. I will now check the questions and read out some. If you have more questions, feel free to uh post them in the talks pyonde. One question that we have is the following. Can you define code your own expectations or just choose from predefined ones? Uh so right now uh the way it's designed is uh it uh it's from the predefined ones. Uh but I do want to

**[18:25](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1105s)** make it possible to define your own expectations and add them. Yeah. >> Um we have a second question. Why support pandas and not polars? uh it it was based so the thing is like we worked uh like this was an internal project for our uh team and at the time we were only using these two but it could easily be extended to other data types as well. So uh we have these abstract classes called validate pandas and validate pispark and the way it's designed is like in future you could add support for others as well. >> Very good. Um, let me check if there are new ones.

**[19:15](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1155s)** Can you def Oh no. Uh, sorry. This is red. Actually, it was the same one. Is it also planned to support polar? So, I think definitely you should put as a priority. >> Yeah, sure. >> Can you make more than just simple validations? Is there a possibility to do more complex validations with regular expressions or lambdas after the validation took place? Uh so uh there is uh so there are two kinds of validations that I have right now. One is very simple that go rowby row and then uh basically find any rows where there's uh an invalid uh output. The second is like aggregation based expectations which is a two-step process. So you do some aggregations and

**[20:05](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1205s)** then you uh apply a checks on the aggregations. So I can see like uh adding more complex like depending on the use case it could be uh applied. So the function itself uh like the validate pandas and pispark is pretty generic on in uh intentionally. Uh I would recommend like giving it a try and if there are any problems or hurdles with it uh we could re restructure it. Sounds good. And we have one more question. Have you looked at point blank from positive def? So if so what does dataf frame expectation make it different? >> Uh I haven't unfortunately seen point bl.

**[20:53](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1253s)** Okay, I'll take >> I think you are able to look at the questions yourselves after the talk. So you can check the link. >> Okay, I'll refresh again to see if we have Yeah, we have more questions. I'm going to go into next one. How is logging and error handling implemented? So right now you uh receive an exception which you can also uh toggle like if you only want to u make it optional you receive either a success or a failure message. I plan to add call back so that if you want to integrate it with uh data dog or emails or slack it should be possible. >> Okay. And um how is the performance? Uh so at the end uh it runs uh basically

**[21:44](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1304s)** like pi spark or panda function. So it depends on the environment you're running in. Uh so there's nothing I can comment on the performance itself. It depends on the uh environment. Yeah. >> Okay. And do you want to comment again? There's a two questions about comparing to pandera or comparing to paidantic. uh so pyantic if I'm correct like it validates uh the classes itself. So uh the main goal for us was uh anyone who's not uh familiar with the data frame uh should be able to add validation. So it's like a single line uh check. uh maybe the other tools might be more versatile in that

**[22:32](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1352s)** direction where you uh where it's easier to define complex tests but then maintenance becomes a problem. So this could work alongside these tools. >> Thank you. We have more questions though. Um how do you check Pispark data frames at the moment and is this done with pispark functions? Maybe you can show some code from the library how this is done. >> I I'm afraid we will not have time to show the code because there are many other questions but I think maybe you can just give an answer. >> Sure. Uh so at the end like this is an uh open-source library. Uh you can find it easily. Uh basically what I do is uh pispark functions that find the error. So if you want to find uh if your

**[23:20](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1400s)** expectation is the value is greater than or equal to zero then basically the function I use is uh a filter on the data frame which says find all the negative values. So it's basically a filter on the data frame and if the count is greater than zero you know there are violations over there. >> Okay good. And um another question is about the output. Is the output still readable if many expectations are not met? >> Uh yeah. So uh at the moment uh it's still text based so we don't write it uh somewhere. Uh you could like I want to be able to generate like an HTML or JSON output or or like give people the flexibility uh to define like how they

**[24:09](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1449s)** want to uh generate these reports. Yeah, >> I think this is then related to um another question that is um did I understand correctly that your pipeline fail and data is not pushed to production when some expectation is not met? >> Yeah. Uh exactly. So uh this is basically uh when you expect uh when you're reading or when you're exporting the data the idea is that you fail uh as early as possible. Uh sometimes like compute can also like when you're applying complex uh transformations you might also want to apply these validations early on. Uh but in general the idea is to prevent your uh make sure like you're checking uh the setup before

**[24:59](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1499s)** you export the scores to other uh downstream uh tasks. >> Okay. Thank you. And one question about the maturity. So how mature is your library? Is it actively developed? >> Uh I've only spent the last six to eight months on it. So it's still in early phases. Uh there there is uh a lot uh a longer journey ahead I'd say like for development. >> Okay. Very good. The alarm was just that we still have time for some questions because you finished a bit earlier and it's great because we do have more. So if you're ready. >> No, I don't mind. >> Yeah. I think it's a it's a great sign because people are think have feeling hands on ready to start >> getting a lot of useful feedback. >> And now um one question that I was also

**[25:48](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1548s)** wondering is like where to place this validation where to place in CI or during code execution. >> So uh as I said like this [snorts] uh validation like it's very versatile. So basically uh the way I use it uh we use separate ones in end to end test where we call the scripts and also check the output but I also add it in a lot of functions like the transformation functions in production. Uh so it's up to you like uh you don't need to modify your code significantly for it and even removing or cleaning up these expectations is re uh relatively easy. Very good. Um, how is logging and error handling

**[26:38](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1598s)** implemented? >> Uh, yeah, as I said before like uh uh by default uh so you need to set up your logger like uh all the outputs are in general like written to a logger and you have the flexibility to write it to a file uh etc. In terms of error handling, uh by default, it returns an exception if there's a failure. But if you prefer uh not to have that, uh it also returns either failure or a success message that then you can process and uh decide like how you want to proceed with it. >> Very good. Thank you. And another question related to this is why did you decide to collect all issues over failing fast after the first violation. >> Uh so the way it works it it doesn't

**[27:30](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1650s)** fail after the first validation like it iterates through all of them. Uh can show you this. So it iterates through all of them and it tells you exactly which subset field. uh so it doesn't skip on the checks. >> I guess this is nice if you need to fix more things at once. So then you uh save some time on that. >> Okay, I think we have answered all the questions. I am going to refresh again. There were a lot. So I hope I didn't miss any. Uh if there is, let me know. Otherwise I thank you again. It was very informative, very exciting uh job that

**[28:18](https://www.youtube.com/watch?v=YG_GXTubZVY&t=1698s)** you presented and topic and library and uh yeah hope to see some next versions in the next years coming. >> Thanks for the feedback. Thank you very [applause] much.
