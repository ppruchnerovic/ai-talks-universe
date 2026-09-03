---
id: yJz2-LqO9qo
title: "Reproducible Machine Learning Using DVC"
slug: reproducible-machine-learning-using-dvc
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: null
duration_min: 24
published_at: 2026-08-23T07:00:31Z
video_id: yJz2-LqO9qo
url: https://www.youtube.com/watch?v=yJz2-LqO9qo
youtube_url: https://www.youtube.com/watch?v=yJz2-LqO9qo
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science"]
transcript: true
---

# Reproducible Machine Learning Using DVC

**Speaker not identified**

`PyData` · `PyData` · `2026` · `24 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=yJz2-LqO9qo) · [Conference site](https://pydata.org/)

## Description

Welcome to the PyData & PyCon Yerevan 2026 video collection - our biggest edition yet, held on 24-25 July in Yerevan, Armenia.

From data science and machine learning to Python tooling, production systems, research, and open-source technologies, these recordings capture the ideas, experiences, and practical knowledge shared on stage.

🌐 Website: https://pydata.am

📅 24-25 July 2026 · Yerevan, Armenia

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*3,253 words · source: supa (en, exact timings)*

**[0:10](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=10s)** So I'm K. I'm going to talk to uh talk to you about reproducible machine learning today. Uh the problem is of course uh we want to reproduce our results uh 6 months from now or by somebody else. That is the uh basically that's the problem we're trying to tackle and uh that isn't that that easy that it seems. So uh let's uh go to that. Uh so there is a actually big literature about reproducibility. There is a reproducibility cris crisis in machine learning. A lot of people are failing to reproduce results from papers

**[0:58](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=58s)** from uh research or reported numbers in industry. Uh se has provided kind of taxonomy of reproducibility. Uh so he basically showed uh that is not interesting just describing your solution. The second one is code. Your code should be uh you should be able to run your code and get the same results. For data reproducibility, we need uh uh uh more tools actually. But what we are looking at what we're looking after is uh basically experiment reproducibility. We want to be able to run from start from the data to the code from the parameters and then uh to the

**[1:48](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=108s)** metrics we are uh producing. Uh so that's what we are after for that we need both the code to be reproducible and the data to be reproducible and some extra steps I'm going to walk you along the way. So we first start uh to uh basically explore how software engineers handle uh their problems. That is like 80% of the way. There is a lot uh more to it. So uh but 80% of their way is just to write the code in gendencies to the code in a file. Of course, Unix philosophy, everything is a file and version control. In each comet, they have uh basically

**[2:38](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=158s)** the environment, the dependencies their code depends on and their code. And in each comet, both of them work together perfectly. So, and they strive to go from commit to another commit without breaking that that invariant. But data science is different. it requires much more than that. So, uh I'm going to talk about the methodology here for data science. In data science, we have code, we have data, we have hyperparameters. They go into a machine uh an algorithm and the algorithm produces another algorithm. For example, uh a training algorithm produces uh a classification algorithm and then we evaluate it using some metrics. So

**[3:28](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=208s)** uh in order to be able to reproduce our models the outputs are models and metrics inputs are these three to be able to reproduce it we need some tools also the research there is great body of research about that it also asserts that tools are really useful without tools you have a hard time uh tracking your experiments uh let's see uh how it's handled uh traditionally. Well, it's basically a spreadsheet all the way. A spreadsheet likes that uh uh tracks or experiments, the accuracy, the feature transformation and of course it results final version to final that that

**[4:17](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=257s)** final is really painful to say. Uh but it's not enough. we have these inputs in one run of a uh example uh one uh experiment it's quite uh how can I say it doesn't fit in a spreadsheet easily and then we have uh metadata models and different metrics what I want to get to uh is that it's not ergonomic to track experiments in a spreadsheets you know in order to be able to reproduce the results you have to have uh quite significant uh resources dedicated to it to basically enter like 50 columns in a spreadsheet every time you run some code.

**[5:06](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=306s)** Then we'll move to uh my advices about code reproducibility. the first stage of uh uh our path. We want to go from this to this. Uh Sugimaru actually paved the way for us. He argues that every machine learning project has these stages. It starts from raw data data layer features. It extracts some features. There is some scoring delay layer and some evaluation layer h my argument and that is how I started. This is my first layer. I ran it twice and run into a bug some notebooks some training scripts. This is the first

**[5:54](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=354s)** version of the results final v2 something and yeah this is not what we strive to get to. You can't after 6 months you cannot uh basically reconstruct your results from this kind of code. After what we seek to get to is to use the insight we have to impose some abstractions. When we want to manage software complexity we impose abstractions to make it easier to follow. Uh we start by uh organizing our code this way. We start a preparation stage. uh that basically outputs some uh in get as input some data and outputs some uh transformed uh data that we want to feed

**[6:45](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=405s)** to our algorithm some features. Uh, I argue a good interface for this is just a script that creates your features and in a file and then uh we want to feed it to our model reads the file and some hyperparameters and produces a file that contains uh a model. Then we read the model file feed it to evaluation algorithm and we will have our metrics. So uh if you are going to use agents for writing code when agents get frustrated they kind of break boundaries and are not quite uh how can I say they can't keep their focus on keeping your code clean. Imposing restrictions like that so your repository would look like these

**[7:35](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=455s)** different stages is quite uh a good practice to instruct your agents to follow. So the environment is quite easy. You have to track your environment. But I'll skip it. For data reproducibility, we have actually we need some more complicated uh complicated procedures. We want to fit this this is our data into this a git commit. we can't do it that easily. So regularly we face 10 GB file, 100 GB file and uh basically we up until now we shoved the code and uh

**[8:26](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=506s)** organized our code and the dependencies and put it in a single bit commit but we can't do it like that with data. We need some tools. Uh a quite useful tool for that is data version control. It's basically aspires to be g for data science. Uh and this tackles the problem of fitting the squaring this circle by basically uh defining a remote data repository putting the data into that. For example, S3 is great for storing blobs, gfs, whatever you have and just calculate the hash of it and put it in the g commit. So in the single g commit you can add your data instead of doing g add you would do g uh dvc add it adds the data to its repository that is

**[9:17](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=557s)** optimized for uh basically keeping large blobs of data and it adds the hash to a g commit. Now in a single g commit you have the stages of your code you have your environment and the exact hash of the data it uh basically produces your results with. So we expanded it. The data wasn't in it. We can add the data. And if you do for example uh for pulling code you do get pull. For pulling data you have to do DVC pull. For pushing it DVC push checkout just take care of uh the data for you. You do a G check out then DVC checkout. It pulls the data related to your commit on your machine. This is what I call data ergonomic for data science. It doesn't adds too much

**[10:06](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=606s)** hassle. It's relatively simple and it's quite useful. Uh so up until now do we have experiment reproducibility or not? Ponder a little bit. Ponder harder. Okay, we have it. But it's not again it's not ergonomic. It's not easy to uh we have the data, we have the uh we can put hyperparameters uh and we can uh basically track our results. For tracking model files, we can use DVC again. We just define it in

**[10:55](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=655s)** somewhere. It's it's good as storing blobs. So model is just a blob. It can take care of that. We have our models also version controls and tracked. Easy peasy. Then uh we have two other parts. We want to uh be able to track our metrics. We want to be able to track our hyperparameters. And these two uh we can't just put them in the file. So and DVC just does it. It puts them in the file. But they do carry some special meaning. We want to compare each commit with this metric. Uh for example, if you branch off your code, you want to uh change uh your code, change your model, whatever you want to do, and then produce your metric and then be able to compare two branches with each other. Compare the metrics. If it's good, you

**[11:44](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=704s)** merge it into the master or main. And if it's not good, you just leave it be there. And this is our pipeline right now. If you write uh metrics in metric JSON and just read parameters from parameters.yaml the tool just take care of the rest for you. It understand parameters. You can run experiment by modifying the parameters without modifying your code and it it basically stores all its data inside your g repository. So a g push would send it to all your colleagues and the results. So up until now there is another uh useful thing we can do is that basically defining the stages

**[12:35](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=755s)** of our code and wiring them together. Instead of for example running uh one file three times or whatever is necessary and then uh going to the next stage uh we can write that as a script as or some kind of directed as cyclic graph of dependencies and let the tool whatever tool we want take care of executing each step of our uh pipeline. Uh also we uh there is another useful feature DVC offers is that it creates a DVC lock file in your repository. So if you in a single commit you again it's extended a little bit. You have the relation of your different stages uh and scripts wired together.

**[13:25](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=805s)** So you can define it easily. I'll show you. Uh and it automatically creates a lock file. The lock file actually gets all the dependencies and all the outputs, hashes them and keep the hashes together. So you have a uh you can have a binary perfect uh view of your run. Everything is hashed inputs at every stage and the outputs are also hashed and kept in a file. So a single commit contains everything you need to uh verify uh your results. Parameters and metrics are small g files there are no problem and blobs are cached locally and they are pushed to a remote and there is a lot of things

**[14:13](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=853s)** going on making it uh efficient. For example, it only stores a single copy of your data. If you check it out several times, it just creates a hyperlink to it. So it's again ergonomic we just derived the tool that data version control is actually uh oh before that so if you install PP install DVC it automatically collects uh telemetry. So we don't want that. Be careful disable it before you move on. Uh the commands I told you if you do a dvc init in a repo it creates some files in g if you do dvc add it adds the file to its repository and uh syncs it with g.

**[15:04](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=904s)** Uh now for defining the stages of your code you just do a stage add give it a name give it some dependencies for example a train stage would depend on results of uh preparation stage and outputs a model and then runs some command the command it needs to run to train the model uh with that you can define your direct cyclic graph it fills in the dvc.ml in your repository you can view it. You can edit it directly or use command line to generate it. Then you can do a DVC repro. DBC repro actually is much more interesting. It looks at the log file. If the dependencies hasn't changed, it doesn't run the code. It just use its results. So instead of running from the scratch

**[15:54](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=954s)** every time you change evaluation, it checks uh basically other stages. If the input hasn't changed, the output wouldn't have changed. So or is it if you write your code such a way that it's only dependent on the inputs we call it a pure function you have to write it in such a way and if you do it it only depends on in its inputs and if the hash of the inputs reads for example your preparation message didn't change it's quite easy the tool can change check that automatically and skip that and just use the file of its results so Uh yeah and it has uh metrics and it has diff here you can put a commit hash and it show you the difference between the

**[16:46](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1006s)** your current commit and the commit you are trying to compare with and there is also experiment run the parameter basically your pipeline uh is parameterized you should have your pipelines parameter ize you extract the parameters from the code and uh just store it in the parameters. The benefit you get from it is you don't have to change your parameters by uh basically every time you want to uh you don't have to change code every time you change your parameters. For example, whenever you change your learning rate, you don't want to change your whole code and create a new commit for that. You can just set a parameter and run an experiment and it again stores the result as a full pipeline in git. So takeaways

**[17:36](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1056s)** uh try to build pipelines not only notebooks it's not notebook not only notebooks use the tools uh use hashes for uh provenence of your data making sure your data is in sync use files to communicate your results different the stages and use metrics to compare your whole pipelines use the lock file It's quite nice idea and reproducibility is actually a workflow. You don't uh you have to take it into account at every step you do using DVC. You can have an extension of git flow uh which you basically branch off and change your code if it's good enough. Merge it. If it's not keep it and you can now delete the spirit and

**[18:24](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1104s)** don't have pain every time it happens. So when DVC is actually a good fit for you. If you are a team it's quite good. If you have multiple stages it's good. If your data is above 100 GB it starts flickering. You you don't want to use that. You want use something else. And if you want to compare your code uh and results 6 months from now, it would be useful too. Uh this is the bookkeeping you're trying to do. You're defining your different stages. You uh you add different commits. You do bookkeeping, but the time you save actually worth it. It's

**[19:13](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1153s)** quite that's what what I call ergonomic. If you track all your experiments like 50 variables in a spreadsheet, the time you do book you are doing bookkeeping doesn't worth the time you're saving. Uh but if you let a tool do that for you, that's great. And uh this is uh this is a repo that I will push today because of the conference. uh you can uh clone it and run a DVC repro. Instead the dependencies, run DVC repro. It's actually a five commit repo that uses DVC to classify some text data. So you can see it in action. And if you want to uh know about reproducibility fer you can look at

**[20:01](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1201s)** Gunderson sources of irreproducibility ML and sera reproducibility and ML research. So that's it. I see questions. Thank you. uh for managing the experiment results and the code we can use g and also g has g lfs plugin live file system and system like hugging face already use that to upload data sets and

**[20:51](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1251s)** manage data sets. So uh what is the benefit of using dvc over uh g lfs or what is the process of cons of the using g over the dvc? >> Yes. So you in DVC you can use G LFS as a back end. Uh G LFS has its own shortcoming. It's not quite uh easy to use for files like 2 GB, 3 GB. Uh the other problem with that is that it has no notion of version or pipeline or how the file is produced and it also doesn't have garbage collection. Uh so uh you cannot clean the results of a failed experiment easily. You have to go through your g history and delete it by hand. It has uh size caps. Uh for example, GitHub free account offers 2 GB only file size cap and you are at the

**[21:42](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1302s)** mercy of your provider. If the provider supports it, it's good. You can use it as a back end to DVC to for connecting it to your whole pipeline. Yeah. >> What is the problem to use uh any seed in process and uh in toppel and uh reuse in next stage? >> Uh any what >> any seed? >> Oh, >> you maybe write a little program that save seeds in uh reuse. What is the problem? uh saving C data for example storing your base parameter or locations config and

**[22:31](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1351s)** >> yeah that that is actually you have to do it in some other file but again it doesn't have a notion of a pipeline you see it doesn't connect to your whole experiment you can do it by hand uh DVC strives to uh do the same thing but easier Uh thank you for the most interesting presentation. Uh this approach strikes me as very elegant and uh reusing a great deal of tools we already are familiar with. At some point as you said uh the data can become so large that this approach will probably no longer work. Could you

**[23:21](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1401s)** please elaborate when and in what case a team using DVC and running their pipelines in the console on files will be forced to migrate to a data warehouse or something else equally untoward. >> Yeah, thank you. You're too kind. Uh so basically uh it has it has some uh idiosyncrasies and uh that can cause uh problems with large files. For example, if we have 300 GB of data set and pulling it on every laptop, uh it's hard. DBC pulls that caches it locally. So you want to be able to for example in that case use some server to use. You can't have it as easy as it is for example a 50 GB

**[24:12](https://www.youtube.com/watch?v=yJz2-LqO9qo&t=1452s)** file and it check sums it all. For example, if you want to check some a two file that could be a problem. uh that is the limitations that comes to my
