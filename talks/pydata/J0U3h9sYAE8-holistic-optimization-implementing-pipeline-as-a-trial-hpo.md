---
id: J0U3h9sYAE8
title: "Holistic Optimization: Implementing \"Pipeline-as-a-Trial\" HPO with Ray and Cloud Infra"
slug: holistic-optimization-implementing-pipeline-as-a-trial-hpo
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Abdullah Taha"]
channel: "PyData"
duration_min: 22
published_at: 2026-08-04T22:20:53Z
video_id: J0U3h9sYAE8
url: https://www.youtube.com/watch?v=J0U3h9sYAE8
youtube_url: https://www.youtube.com/watch?v=J0U3h9sYAE8
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science"]
transcript: true
---

# Holistic Optimization: Implementing "Pipeline-as-a-Trial" HPO with Ray and Cloud Infra

**Abdullah Taha**

`PyData` · `PyData` · `2026` · `22 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=J0U3h9sYAE8) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Abdullah Taha explain how to escape the "local optimization trap" by implementing a scalable "Pipeline-as-a-Trial" HPO architecture using Ray and cloud infrastructure.

Speakers:
Abdullah Taha

Description:
Local optimization in machine learning occurs when a specific model is tuned for its own output rather than the performance of the entire downstream system. This often leads to failures during A/B testing because improvements in one component can negatively impact subsequent steps in the pipeline. To solve this, a "Pipeline-as-a-Trial" approach for hyperparameter optimization (HPO) was implemented, treating the entire end-to-end pipeline as the objective function for tuning.

The technical implementation utilizes Ray, specifically the Ray Tune library and its HyperOpt search model, to manage the search space and trigger trials. Instead of tuning a single model, the trainable component is a customizable function that builds and executes a full pipeline. This pipeline consists of multiple steps, such as short-horizon and long-horizon forecasting models, an assembler, and a post-processor. The system uses a config-based approach where data scientists define the model classes and parameters in a configuration file, which is then translated into a directed acyclic graph (DAG) for execution.

Three proof-of-concept (POC) infrastructures were evaluated for scalability: AWS SageMaker, Databricks, and a custom Ray cluster on EC2 instances. SageMaker utilized SageMaker Pipelines to orchestrate training jobs, while Databricks employed Workflows for similar DAG management. The EC2 approach used Metaflow to define the pipeline structure within a Ray cluster. While Databricks provided superior UI and traceability and EC2 offered maximum configurability, SageMaker was selected for production due to existing data scientist familiarity and integration with the AWS ecosystem.

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

*3,862 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=5s)** I want to start this talk with this scene from Rick and Morty. But just before starting, can I see a show of fans who are familiar with the show or not? Okay. Yeah. So just for you who doesn't know, it's not mandatory to know the this show. So on the left here we have Morty. Morty is in love with Jessica. Jessica doesn't care about Morty. So Morty goes to his uncle Rick whom is this genius scientist who can solve everything with science. And so Rick comes up with this love potion. He give it to Morty. Morty goes to a party, makes Jessica drink it and it works. Jessica is in love with Morty. But the fallback here is that Jessica had the flu and then it spread across the party and now all the party and the whole city is just crazy about Morty. Morty goes back to his uncle and then Rick come up with a new solution and they spread

**[0:54](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=54s)** across the city. It doesn't work and now all the humans just turns into monsters and the whole city is just chaotic and and chaos and they cannot reverse the changes and so they just have to ditch the universe they're living in and go to another parallel universe and start living there. And so Morty is is traumatized. Yeah, it reminds me of our last Friday production hot fix. Um, so I want you to take a couple of seconds just to look at to look at Mort's face and see if it's familiar to you. Like, have you seen it anywhere? So, basically, it's it's it's um it's this look. I mean, I saw this look many many times working in tech. It's it's look of a data scientist when they're working on their model for weeks. they

**[1:43](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=103s)** put it into an AB test, it fails the AB test. It's the the look of a like product manager when their feature of or improvement just causes the the revenue to fall. And and and it's the same problem that Rick and Morty have fallen into. It's this problem of when you're trying to solve something but without considering the whole system, right? So, let's take a step back here and see what happened. So Rick did come up with a solution which is this clove potion but he only considered the input at hand. He could have didn't consider the city the flu the the whole system and normally in real life like you would have let's consider this this diagram on the left. Let's say this is a working system. It can be anything we want to we would notice that C is not is not doing very well. So we want to optimize C. And

**[2:33](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=153s)** let's consider that C is a machine learning model just for the sake of talk. And so we got a data scientist. Data scientist take the C do some machine learning magic. Come up with with CV2. It's might be improved C like an improved model or another model. We take C, we put it in the system. Now E is green. So everything is good. But we broke D. Why? Because D also take input from F which we didn't know about. And and and now G is also broken. So, so and this problem once you start see it, you see it everywhere. Like the problem when you're trying to optimize is the problem of local optimization. You optimize something when you put it in a bigger system, it fails. It's everywhere. It's in back end, it's in product, it's in machine learning and and it's even in your real

**[3:22](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=202s)** life like you're doing some recipe, you're following some recipe, you taste the stock, it needs some salt, you add salt, it's good. Later in the recipe, you need to add soy sauce. And now everything is just too salty. Uh sorry for the long introduction. Uh my name is Abdul Lataha. I work as an MLOps engineer at Salando. And today I'm going to talk to you about this exact problem of of how to optimize holistically how to optimize a pipeline. And we're going to focus today on this on the problem of HBO of hyperparameter optimization and how we at Zelando implemented a solution um a scalable solution with Ray and and cloud infrastructure. So just to give you a little bit of content uh I'm going to start with some context and what we do at my team as Alando and how are we dealing with

**[4:11](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=251s)** hundreds of machine learning models in production just to give you a background of where are we starting from. Then we're going to narrow down a little bit on on the problem of of um of how to optimize a pipeline. Then I'm going to present you with the solution design that we did. How do you implement like we tried couple of PC's, couple of implementations using Ray and cloud infrastructure. And then I'm going to show you some comparisons and some insights that you can take home. Okay, let's start. So I work at a forecasting team at Zelando and our team is responsible for predicting couple of business KPIs like number of sold items, cancellation rate etc etc. Predicting those targets helped Zelando to plan some logistics to to to plan budget etc etc and we do this for 24 countries

**[5:01](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=301s)** roughly and like each of those boxes is not a single machine learning model but it looks something like this. So we might have like model one is a short horizon model to predict like five weeks of data. We have like model two that would predict like 15 weeks of data long horizon model. Then we might have like an ensembler that take the input from the models and do some ensembling techniques or so. Then we would have like a post processor and the KPI consolidator that take the input from another KPI and try to to make result consistent. So yeah, it's kind of pipeline and then we get the final target. So if you try to visualize this for each of those KPIs multiply by 24, you would understand that we're dealing with kind of hundreds of models. So how are we doing this in in uh in

**[5:48](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=348s)** production? Uh we are following a config based approach kind of. So you see here this blue library is like we have a library that holds every machine learning codes. So it's training, evaluation, splitting, post-processing, whatever. Uh and and this library is is is used by configs. So normally a data scientist just try different configs to experiment with different machine learning models and then whenever he get the best model or the best config, he would just give the config to the MLOps which is me. I put it into production and I take my salary. Um even that like I put I give it to cloud now. But yeah uh so [laughter] um and and and for the dependency here you see that we have some kind of DAG like here we have dependencies like it's a it's a kind of direct a cyclic graph

**[6:38](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=398s)** for the dependency management of the DAG building we use airflow we also follow a config based approach there um if you if you watch the the talk by Akif it's he talked that this is a good design um So, so we also have like we define a dependency there in kind of config and then we have a dynamically generated dag in airflow. Um so, so he this part on the right is our production but we're going to focus today about experimentation part. So normally when a data scientist want to experiment with machine learning model he would use this part uh this process called hyperparameter tuning or hyperparameter optimization. I'm sure most of you are familiar with the topic. Uh but just an overview. Wow, this resolution is bad. Okay. Uh so you start with ML model. You

**[7:28](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=448s)** start in a machine learning model. Uh you define a set of parameters that you want to optimize and then a search space is created. So this search space is basically like combination of different parameters that you want to optimize against and then the hyperparameter tuning happens. I will talk a little bit more on that. and then you get the best config of your model. And the hyperparameter tuning looks something like this. So there's a couple of approaches to this but yeah just just an example. We're talking here about the baian optimization. So you would have an optimizer. The optimizer creates a search space and then the optimizer decides on an initial set of hyperparameters and then you would trigger like couple of trials. On each trial, you would train the model, evaluate the model, and then the result

**[8:16](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=496s)** would be reported back to the optimizer. After a couple of iterations, you get your best results. So, looping back on our PL problem, if you recall this picture from before, so basically in the normal normal uh circumstances, you would optimize, you know, model one for the output of model one, which we don't want. What we really want is that we want to optimize model one for the output of the pipeline and not only that we want to optimize each step of the pipeline like we want to optimize the the parameters at the assembler the parameters at postprocessor etc etc and so if you if you like th this diagram that I showed before about the hyperparameter optimization what we really want here for each trial that we try we don't want

**[9:05](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=545s)** to try training only the machine learning model what we want to do is this. Basically, this is the core of this presentation. This is what we want to implement. We want for each trial to evaluate the whole pipeline. Okay. So, how did we do this? Like a good a very good like every good engineering team, we go and consult our senior principal data engineer. Um [laughter] no, just joking. So, how did we do this? Well, we used Ray. Uh and for those of you who doesn't know uh Ray is a is a very cool library a machine learning library that allows you to run machine learning in a distributed way. So you would write the same code it would run on your either machine or run on on on like 10 machine cluster and

**[9:54](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=594s)** it's the same code. So we used ray as the main implementation library and for the infrastructure for where the code would be executed in a scalable way uh we tried couple of PC's uh one when uh on sage maker one on data bricks and we also tried our own custom solution running array cluster on EC2s um so from ray we used um the hyper opt search model which is a component under the ray tune so ray have couple of libraries one for training, one for data processing, etc., etc. So, this one is under the rain tune library and um um this diagram is from the documentation of ray and as we talked before as like a hyperparameter uh tuner, you have a search space and here you trigger the

**[10:42](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=642s)** trainable. So, the trainable here is the objective function that we want to tune against. So normally this is a machine learning model but what we will do is that we will use this customizable component to feed a pipeline into this and so uh so this is just an example from our codebase. So here when we define the trainables we take like we tried a couple of PCs so this is just a dictionary of those. Uh as you see here when we define tuner we pass the trainable. So here like each of those functions are responsible of building a pipeline and I will talk a little bit more on that. So uh just to give you a rough idea uh this is the config that a data scientist might write. So without going lot into details you can see that

**[11:30](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=690s)** we have steps and in under steps we have three steps basically here the naive seasonal which is a model. We define the name of the model the class that it will bind to and then we would define the parameters that we will optimize and uh and like here we have another model which is autoats and uh here we have an assembler that would take as input the two models. So here we have the structure of how the pipeline which is a very simple pipeline here but just uh to give you an idea. Now in term of solution design here we need two components both clearly in the solution one which is the entry point. So here where the data scientist would interact with this whole system. So the data scientist would would write those configs and then what he need to put them somewhere and so this entry point

**[12:19](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=739s)** is where data scientist would just define the configs define the class that we wrote and then trigger whatever method it's it's working and the what is triggered basically so the infrastructure should be able to build this concept of a DAG or this concept of pipeline. it should run multiple trials in a scalable way and it should report back to the entry point. So this is just an overview of the of the solution. Uh so we tried couple of PC's um as I mentioned before I will talk a little bit on details on those. We tried on SageMaker on data bricks and on EC2 machines. There are two couple of two worth mentioning um uh things that we didn't try but if I have time I will talk a bit more. So what are the consideration when we will build such

**[13:07](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=787s)** PC's? There are a couple. So there are performance. So each each uh each infrastructure here has its own boot time you know running performance, maintainability. Uh how hard does it do you need engineers to maintain your environment or is it self-maintainable? Like you can imagine that building custom thing would require more maintainability. Usability does the data scientists are able to use this easily. [snorts] traceability where can you see logs where can you see failed failed step failed pipeline cost limits of the infra etc okay let's start so uh we start with the SageMaker um P so in SageMaker we use this concept of SageMaker pipelines if you're not familiar with it you so you can define

**[13:54](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=834s)** multiple training jobs and you combine them to together and it's called SageMaker pipeline um so as our entry point we used SageMaker Studio notebook. So the data scientist would log in SageMaker Studio, open a Jupyter notebook, define the configs, trigger the system like define the class and and run the the cell and then in the background it would use the config use SageMaker pipelines to build a DAG and run it run each trial on a single SageMaker pipeline basically. So you would run this in a scalable way and this is some code. So here as you see four step instep configs we're iterating over each step and in each step we're doing define job training. So we're defining a SageMaker training job. So

**[14:41](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=881s)** this is one step of it. So we're defining multiple jobs and then in the second for loop we're looping over the over the dependencies between the steps. So we combine them uh together. So we can so when you use this basically you you you create this DAG and then so uh yeah and then you return the pipeline and this ray would use to to to evaluate against and this is a screenshot from SageMaker. Uh as you can see there are two steps and they are bounds into this inse step. It has nice UI. You can see the running steps. You can see the cued steps. And and if uh here in SageMaker um if you want to see logs, they are all go to Cloudatch if you are familiar with the AWS ecosystem uh tech system. Um and if you want to also look for each

**[15:31](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=931s)** instance CPU and memory usage, you would also go to Cloudatch. Uh so another similar one which is data bricks. Data bricks also have this concept of pipeline which called workflows. Um again same system here for the for the entry point. I'm going to skip that part because not very important. It has a similar just to keep the timekeeping. Um it has a similar concepts and it has like this nice visual UI. Um and in in in data bricks I think it's very nice that they have this airflow kind of look. So you can see a couple of like running uh pipelines. You can you can see the logs directly from there. You can restart each step like if you have vest step you could look log

**[16:18](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=978s)** you could try a retry which isn't there in SageMaker. And so yeah now the third PC that we tried. One thing to note about the first PC is that here we didn't use ray cluster we basically used rail library and we did the scalability on ourself like we tricked Ray to triggering each um SageMaker pipeline or each datab bricks workflow. So we provide scalability in this way but in this one we use basically ray cluster. So as an entry point we use again SageMaker notebook but it can be your local it can be anywhere. Here we spin up array cluster. So we said okay I want a five machine EC2 cluster on on spin it up for me and after that we're reading the configs and submitting the job to the ray and then

**[17:06](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=1026s)** ray would use those machines to run this in parallel. And if you recall, we needed something to define this DAG. And here we used metaflow because we need, if you're familiar with metalflow, uh you can build Python classes and you can build a DAG from the classes basically. Uh so yeah, this is a little bit more complex, but it's yeah, it's without using a platform. We needed something to measure against two just worth mentioning things. I'm not going to spend a lot of time. So data bricks also have this concept of ray cluster inside data bricks. So you can run one notebook run array cluster behind those notebook. Um it's it's we didn't try this but basically like one downside here is that you cannot see the pipelines running be behind the notebook

**[17:56](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=1076s)** because you have one notebook and a lot of things running in the beh in the background. Another thing is this platform which called any scale. So this is a platform that's built by the people who built Trey. First they built the library. They said okay we we we built the Ry now we built the infra. So they basically request to connect to your AWS system and they would handle like spinning up the machine terminating the machine etc etc. Um yeah uh and they have they pre um give you this nice notebook kind of thing and you can run things and it will just scale by itself. So uh some comparisons um so in term of spin time and warm pool let's start with that. So each of SageMaker and data bricks have this concept of warm pools that you can um

**[18:45](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=1125s)** you know uh not don't need to wait for machines to boot up um on ray on EC2 this can be configured we can just tra spin up ray cluster beforehand and and and so we would kind of configure that in term of traceability monitoring debugging so where to see the logs how to trace the the the the pipelines I think data bricks have the nicer UI in term of this uh on ray on is two it's none it's basically a terminal but it can be configured again um so yeah let me just so just a a quick insight like here ray on EC2 is the most configurable one but it requires more maintainability you need an engineering team to maintain this the other one is a little bit okay you pay more for a for a platform but

**[19:34](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=1174s)** you get better you know less maintainability Okay, final thoughts. So, what's the winner P between those? None, obviously. I mean, we ended up using Sage Maker just because our data scientists were just using SageMaker from day to day. And it really depends on your requirement. If you require to to more configurable thing you want to to to publish logs to some other platform or so, you can build your own stuff. If you don't have engineers and like one engineer and like 50 data scientists, you probably don't want to build something custom. Um, and again like the second insight is your MLM infra only as good as the ability of data science to navigate it. You can build the most amazing system engineered system. If the data scientist cannot use it, it's useless. The third one is go look

**[20:24](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=1224s)** around. I mean detect the local optimization problem in your system. Try to figure out the solution. Don't be a Rick. I mean the insight here is that we talked about this concept in the context of hyperparameter optimization but this problem is everywhere it's it's it's it's in on old products back in engineering you're trying yeah just go around try looking for it the fourth insight well yeah I needed to fill out the template and I didn't have the time so okay [laughter] [snorts] I'm wanted to finish with um this quote uh from a great author in system design uh the performance of a system is not the sum of performance of its part. It is the product of their interactions. Thank you very much. And uh if you're interested in the talk, if you like the

**[21:12](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=1272s)** talk, if you want to work on this similar problems, please uh join us at Gelando, you can look out our open jobs at uh jobs.zon.com. If you want to reach out to me through LinkedIn, you can use the link on the right. Thank you very much. [applause] Okay, thank you so much. Uh, first question is when testing the PC's, did you use enterprise level or were the test using the open-source levels of different PC's? >> Um, I mean in in in Zalando we all have both data bricks and SageMaker are used in enterprise level. So, it's not open- source free stuff. No.

**[22:05](https://www.youtube.com/watch?v=J0U3h9sYAE8&t=1325s)** Any more questions? Anyone? You have anything? Okay. [laughter] Uh, >> thank you so much. We can give him a big round of applause. [applause]
