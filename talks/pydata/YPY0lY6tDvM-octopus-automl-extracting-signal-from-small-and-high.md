---
id: YPY0lY6tDvM
title: "Octopus AutoML: Extracting Signal from Small and High-Dimensional Data [PyCon DE & PyData 2026]"
slug: octopus-automl-extracting-signal-from-small-and-high
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Nils Haase", "Andreas Wurl"]
channel: "PyData"
duration_min: 29
published_at: 2026-08-25T18:20:11Z
video_id: YPY0lY6tDvM
url: https://www.youtube.com/watch?v=YPY0lY6tDvM
youtube_url: https://www.youtube.com/watch?v=YPY0lY6tDvM
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Octopus AutoML: Extracting Signal from Small and High-Dimensional Data [PyCon DE & PyData 2026]

**Nils Haase, Andreas Wurl**

`PyData` · `PyData` · `2026` · `29 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=YPY0lY6tDvM) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Nils Haase and Andreas Wurl demonstrate how the Octopus AutoML library ensures statistically honest results and prevents data leakage when working with small, high-dimensional datasets.

Speakers:
Nils Haase, Andreas Wurl

Description:
Octopus AutoML is an open-source supervised machine learning library designed specifically for small, high-dimensional tabular datasets, such as those found in clinical trials or material science. In these environments, the number of features often equals or exceeds the number of samples—for example, datasets with only 50 to 100 data points but hundreds of features. This imbalance typically leads to the lottery problem, where model performance varies wildly depending on the random seed of the data split, resulting in unreliable estimates of generalization performance.

To mitigate this, Octopus AutoML implements nested cross-validation. Unlike standard k-fold cross-validation, this approach uses an inner loop for hyperparameter optimization and an outer loop for testing, ensuring that every data point is used for testing exactly once across multiple models. This process reduces the impact of split seeds and allows for model ensembling to improve overall performance. To address high dimensionality, the tool integrates various feature reduction methods directly into the nested cross-validation pipeline to prevent information leakage, ensuring that dimensionality reduction is performed only on training splits.

The framework includes a comprehensive data health check to identify input issues early and a modular benchmarking system to compare different tools, such as the native TACO tool and AutoGluon, under identical conditions. It supports regression, classification, and time-to-event problems. By automating the pipeline from data preparation to evaluation, the tool enables a high-throughput screening approach where numerous use cases are ranked, allowing researchers to prioritize deep-dive investments only on the most promising signals.

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

*4,613 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=6s)** Um yeah, our talk is about um another outl tool, but we think it's still worth in doing it because uh we didn't find anything that has or working with small data and high dimensionality, a problem that occurs often u in our company. So my name is Neil Hardzer. I'm a data scientist at the EMD digital group at Merc. Um I'm more coming from so I'm a physicist by training. I'm coming from the material development. uh I first start in the lab and then more and more over take uh coming to this data science approach and yeah in the end we figured out that um there's some lag uh for daily work that we went work on and so this is like an open-source project so you can also use it um if you want to so

**[0:57](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=57s)** >> yeah my name is Andreas and um I'm a data scientist in Mer healthcare and in me healthcare we do a lot of machine learning But we live in a small data world. So so like a typical clinical trial has 300 patients and what we are really interested is in in is uh that does machine learning work on 50 patients. >> Yeah. That said um whenever people talk about machine learning it's all about dictata it feels like. So for example I mean autonomous car driving is a hot topic right now. And so I looked at Intel and they say like you create like 4 terabytes of data each day with each car uh which is a lot and we could only dream about. So what you end up uh with

**[1:46](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=106s)** that you have millions or trillions of data points and you generate way more samples than you have features. I don't know how many sensors you have in a car, maybe 100, 150s. And compared to this million or trillions of data points, you really get this like vertical flow when you um yeah have your samples against your features. So here, for example, overfitting is maybe not a problem because um you have so many samples, maybe you can remove outliers quite easily and so on. So the real problem is scalability. when you now join a company like Merc uh things look a little bit different so um it's even hard to find public data set that really showcase uh our problem so I

**[2:34](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=154s)** found one interesting that is already from the early '90s last century but I think it gives a nice idea uh what problems we are dealing with so it's about arisma so um if you have an abnormal heart rhythm um this can be detected via machine learning um and back then to create these data was a lot of effort because you need like experts they have to look at the graph and so on so each data point you generate was really costly so in terms of or nowadays you have all your smart watches maybe this is not the case anymore but I think it's a really easy transition to our current plat problems like um when we look at cancer uh we want to create a new medicine you for

**[3:22](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=202s)** sure don't want to test it on like 10,000 people maybe if you have a new drug. Um the same is true if we go to um creating new um materials for the semiconductor industry or the display industry what we do at Merc um then so normally it takes like I don't know 3 to 6 months to synthesize a new molecule um and you still want to learn from it. So I normally end up with data sets that have like 50 data points. If I'm lucky, I get like 100 data points. But you still want to do machine learning to extract valuable insights out of this. So this example shows quite good um what we can do with that. So we have like 150 patients and comparably uh around 280 features. So you get from this vertical

**[4:13](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=253s)** stack to like a horizontal stack. So you have way more features than patient or at least uh the same number. Um so it's really like a small data set with high dimensionality. So when we talk about high dimensionality it just means we have a lot of features compared to the number of patients. So the question is then does like normal standard machine learning you can do with autolan whatever you name it is this still valid or do we run into problems because we have like some changes in it. Um so what I have done is now for this example data set I created like different splits that means it's always the same data set the only difference is that some points are in training and some points are

**[5:02](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=302s)** interesting and I just change it um and then you get results like this so we have five different data splits and we get like for split one split four and split five we get more or less the same results. So we get a score of 0.9 but then we have split two which outperforms quite a lot. So we end up with a score of 0.94 and then we also have like split two where the score is very bad and we go with 0.77. So if I go to my scientist um and I talk them so what is the best option to create um the model. So if I do just like one split and end up at split two I

**[5:50](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=350s)** will tell them we have a super good model we can use it no worries and then we will figure out over time that it may not be as good as we expected because it was just a lottery. It took a nice split for me and we have a very good model. Um the other part would be we end up in split three the model is not very good and I would tell them yeah I don't think we can really do something in machine learning the model is not good enough that we get any insights out of it and then we just leave it both cases would be false in this case um and both would be cost us a lot of money so it's really about knowing um can I trust this model or not um if I end up in like split one split for split five you maybe have like the real insights um or you can have a

**[6:41](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=401s)** yeah you can trust these more or less. So you can already see um that you maybe need to treat your data a little bit different if you want to do machine learning and you also get an idea what you can do. So everything that we implemented is nothing new. For example, this is called like nested cross validation. You do normally if you have very low data. Um but there's nothing out there that does this more or less automatically. So um you have to do it all by yourself and then you end up with different problems. Um we come to this later. um because like implementing a nested cross validation is maybe easy but it gets you down the road into some troubles. So that's why we thought there's really a need to have this

**[7:29](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=449s)** autoML tool even so there are a lot out there already but nothing that really fits our problem. So yeah, we can just recommend if you have small data um also that's maybe like the key takeaway already from my side. If you're going to have little data, you can remember this plot before um and see okay maybe I run into a problem or you can just use octopus autoML. So it's a supervised machine learning. Um we have like regression problems, classification and also time to event. uh it works for small data set as I already said and what you can also say this is all driven by real industry problems. So um we figured out that we have some problems that we want to solve

**[8:18](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=498s)** and we already uh looked at these things and then we developed this tool and at some point we finalized okay we want to make this public then poor people can use it also at our company and this is not just used by I don't know Andreas and me so that you can all have the advantage about that. Yeah. So it's like an open source uh under Apache 2 license. So you can go to the GitHub link and just work with it or you can also just pip install auto octopus auto glue I guess. Yeah. And with that okay now we um Neil's mentioned the so what he mentioned was one of the problems that we face when we do machine learning on small data sets. So this this lottery problem. So how do we

**[9:06](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=546s)** tackle that? Before I explain that I just a short execution into the classical approach. The classical approach is we have a data set we split away a test data set here shown in red and then we do a cross validation to train and tune a model and then once we have that model we test it on the test data set and and get a generalization performance. So and and that exposes us to this lottery uh problem. And what we do is we um we take a data set. We do this nested cross validation. We split the data set into five equal parts and each of those parts becomes exactly once a test set. And that mi that means um in in the end we don't not only train one model, we train five models in the end. So what are the benefits? First uh we

**[9:55](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=595s)** reduce this the impact of this data split seat dramatically. The second one we test on every single data point and also get for every data point a test prediction and then in the end as we have five models we can also investigate those models for example look at um what features do those models use and that tells us um a little bit about the robustness of the solution. So if all models use the same set of features that would tell us oh there is a converging solution and that builds trust in our solution. Nested cross validation comes at a cost and that is compute and also complexity and octopus is designed just to take care of that complexity. Once we have trained a model, we always

**[10:44](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=644s)** um uh in the end we want to predict on new data and then there comes another benefit. Uh as we have five models, we can ensure the second issue as needs mentioned is the dimensionality and coming back to the example he showed. So um in for this arith arythmia data set we had roughly 450 patients 280 features that that means uh two patients per feature um two times as much patients as features and that is a situation where machine learning algorithms start to struggle. So the the message is clear. We need to reduce that dimension and there are a lot of um um

**[11:34](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=694s)** dimension reduction methods outside. We have checked or investigated them all and selected some that we find very beneficial and have implemented or imported that in into this octopus autom. The main point here is um that we have embedded that in the in the nested cross validation and that prevents information leakage. For example, feature reduction should never be done on the full data set. It should be always done after the data split. And we take care of that. Then um like the first step to great results is a very simple one and it's simply is avoiding mistakes and that's why we um with octopus we cover the full process machine learning process. We

**[12:23](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=743s)** start at the data preparation. We cover data split. We cover model training and also um provide tools for model evaluation. So this process is um I mean full of pitfalls that need to be avoided and one of the biggest topics is already starts with the input data and that's why we developed a comprehensive data health check that catches those problems very early on. The ne next big topic is the data split and uh in contrast to other packages we completely take care of the data split. So we take care of the splitting of the test data set and of course of the inner splits to avoid all the all the typical mistakes. And the biggest point or the biggest issue of them all is information

**[13:11](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=791s)** leakage. I already mentioned that. So never apply um a processing or feature reduction method on the full data set. But it can be also like um very subtle on an organizational level. To give you an example of a topic that we cannot cover is if you have two teams working on the same data set and one the first team uh tells the second team about let's say three or four features that don't have an impact that is already data leakage and it's something that needs to be avoided. So um we cannot control every aspect of information leakage but um whatever is possible in in our means we have done in octopus. Octopus is not only a machine learning

**[14:00](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=840s)** tool, it's also we have extended it to become a benchmarking tool because we have faced the situation that um the machine learning world is a fastm moving world and um there are many claims in this and the claims are done on maybe benchmark data set sets which may be different to our data sets. So what we really needed or what we need is a way to compare um tools against each other and this is what octopus also provides. So we have imple we have designed octopus in a very modular way. So our own native machine learning tool is called teco but we also provide other machine learning tools from external libraries like autoclone. So we import them and uh to make uh to be able to

**[14:50](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=890s)** compare and what we want is we want to compare tools on ident identical conditions like identical data splits. Um but yeah and and yeah on identical conditions and on our own data sets. So if you use octopus you can basically you can benchmark on your data sets. We also included feature selection methods, packaged them in modules and the benchmarking framework allows to uh design complex let's say machine learning workflows um where you can explore the different methods. The important point is that all that all this benchmarking is done within this nested cross validation. So we take care of that. Now some comments on on how we started

**[15:41](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=941s)** to use octopus. So having octopus h available and over time we have built trust in its capabilities. So we now um have let's say good trust that if there is a signal in a data set there is a high chance that octopus finds it. And the third point of course it is an autoML tool. So there is a high degree of automation. So the full process is much shorter. So all this all those three points together changed our approach to how we deal with machine learning use cases. And our typical setting is that we have many use cases. We have many ideas but limited resources and then when we invest in a machine learning use case then we have one attempt. So um if that fails we if a data set or use case fails we don't look

**[16:30](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=990s)** at it again. So what we now do is because of this automation we uh let it run let octopus run on as many as possible use cases then rank the use cases and come up with a short list and then we only do deep dives on that short list. So in this sense octopus is not only a machine learning tool but it also uh helps you to make decisions where to invest your time. So in order to to wrap up um Octopus is a machine learning uh AutoML library optimized for small data sets. Its development is driven by our industry use cases and we now have made it open source so that everyone can use it and and explored and test it. So

**[17:22](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1042s)** um Octopus has been a teamwork. So many thanks to the contributors. So they made this possible and also many thanks to the uh people who gave us advice and to help us to uh to get in into the um to shape our direction. So Octopus is available on GitHub. Have a look. You can easily install it via pip and we would be very interested in your feedback and ideas. With that, thank you very much and happy to take questions. Thank you uh Na and Andreas for this wonderful talk. Um I remind you really quick uh that you can ask your questions on talks.pyon.de

**[18:11](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1091s)** as well as upvote questions. And the first question and the first question is uh what's the difference between nested CV and standard K fall CV? I mean the nested is that you do it twice. Yeah. And with a standard cross validation uh you cover only the let's say inner loop. With a nested one you you you do two on top of each other. >> Yeah. We have to do this because we're doing hyperparameter optimization and so we have a force and back between we call it like development data set and you should never do any assumption on your test data set right. So which model

**[18:59](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1139s)** performs best. So that's why we use this nested cross validation. So we do everything on all the development data set um which model works best and so on. Otherwise you introduce like data leakage. So you need to do it twice just to avoid data leakage would be the short answer. >> Okay. Um the next question is what exactly is the optimization for small data sets? How are you have you adjusted the modeling part or do you use vanilla ML algorithms? >> Do you want to answer? >> Yeah. In principle we just use when you call it vanilla so we use like standard libraries right. So we do hyper optimization uh hyperparameter optimization and so on but there's like

**[19:47](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1187s)** cat boost um random forest what you name it um but we also use like auto glow so whatever autoglone uses you you can also do it so as I said before there's nothing like super special we introduced but it's more like putting them all together in one tool so you don't have to select I just want to test like random forest and that's it. No, we just want to put all the things together. So like in this modular approach that we don't have to test all these things by ourself. Um maybe I add something to here. So there are multiple approaches to that to to deal with the small data sets. I mean and and what is beneficial is to combine different approaches like um feature reduction methods and um what we also

**[20:37](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1237s)** have implemented is um a tool to constrain the hyperparameter optimization. So so that in this hyper parameter optimization that um models are um rewarded that are leaner from this by by from the beginning. Yeah. And um but there is there are many ways of doing it and that's why we uh provide this modular platform so that uh you can test on your individual data set what works best for you. >> The next question is a an interesting one. How easy was it uh to obtain the company's permission to release the package as open source? Yeah. So, we were pretty lucky because I don't know who attended last year and

**[21:27](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1287s)** but they're also the developers of the baby package which is also done by Merc. So, they yeah get the way um that it's a little bit more easy. So, we can just use uh their um yeah their work. Um and it was not that easy. Uh it was not it was easier than we thought, right? Um because I think like Merc is also very open um to topics like this and it's just like uh we think there's a value gain to have this whole community because we thought that um having like one single bug in your code is uh worth a lot of money, right? So if somebody outside of our company finds that, it's still worth to get like open source it just because we can maybe rescue two or

**[22:16](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1336s)** three uh projects. Um and yeah we also so we are just using open source tools in there right so there's nothing like fundamentally we doing different you can just go on sklearn and find everything more or less what we are doing here right it's just like really the combination and the speed up and yeah what what we also found internally so I mean our team uh is a very diverse team coming from different business units and what we found is that Because of this diversity, we get a lot of different information how to shape this uh the software and this is this is also the the question to the audience. Um please give us some ideas what you find useful and and what you don't find useful and we of course uh would like to

**[23:05](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1385s)** consider that in in in the upcoming developments. >> I think the only constraints we got is that we were asked to have a talk at the Pyon if we want to go public. So >> excellent. Uh the next question is what is the smallest data set size the auto your autoML framework needs to work well. That is a hard question depends on how good your features are I would say. So I think the smallest data set where we really got um good results were 50 data points. Um so it depends a little bit on what is a good model. I would also say um do you want to have best performance but like from the material development background I would say you can still

**[23:53](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1433s)** have a rather good model but if it helps you to filter out the ones that really would not work and you limit your option so I mean the chemists they have like lots of ideas right and if you have like a solid model where you can get off like 30% of the models mod you want to synthesize that is always a huge gain and then you maybe just need like a good model but not the best model at all. So um it depends a little bit on your use case. I think in healthcare it's a little bit different. Um >> yeah I I just thinking about one use case or one project I worked on and we had uh we started with 67 patients and I was very pessimistic about it and finally um or we were super surprised it worked. So we got a very very strong

**[24:43](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1483s)** model but um let's say that only I mean in this regime it only works if um the signal must be super strong with a weak signal it doesn't work so in this case we were lucky we had a strong signal and it was a classification so in in this data set also the classification was balanced very balanced and that was those two things were the precondition of of it um in order to make it work if we had um let's say an unbalanced data set with big signal no chance. >> Okay. The next question is uh is octopus also able to cover imbalanced data sets when you have a small data set as entry point? >> We try to cover that. Yeah. >> Can you also use your framework for

**[25:34](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1534s)** large data sets? If not, why not? um there should not be a problem in uh using large data set but what we didn't didn't um do was like to optimize it or to um yeah technically optimize it for let's say 1 million samples or 2 million samples. We we didn't um yeah the opt let's say all our optimization efforts went into how to make it work well on small data sets but there's nothing that in principle would stop it from working on large data data set. >> Yeah I think the question can I do it or should I do it? >> Yeah so the compute is increasing quite a lot if you have like I don't know 20 data splits um and if if you have 1 million rows then I don't know if you really want to do that. So I think

**[26:22](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1582s)** that's why we also I think there are other open ML tools out there that already fit the purpose but um that's why we are only focus on the things um that matter for us. >> Uh can one use Octopus AutoML for tabular data? >> It is primarily tabular data. Yeah. And so is um we we should have mentioned it. It's a tool for tabular data but um of course we are exposed to multimodalities in in our real work life but there there is one um trend that is is helping us a lot so they are this there's this emergent of of all those um foundation models for example I'm now thinking of image foundation models and what those models do is basically they

**[27:11](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1631s)** take an image and and create an embedding and then uh the the problem comes it goes from and is converted from an image problem into a tapular problem where basically now um we are playing. So I I am trying to understand the question. I don't understand the question. Um um can octopus handle sparse data or nuns or corrupt data? um to some degree of course we we we do uh support uh imputations but um I mean I mean this would could be a direction to develop it further. Yeah. So I guess

**[27:59](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1679s)** if it's too sparse one one hits some limits. Yeah. >> Yeah. Also we don't allow any nons in the target uh currently. >> I'm going to read the question and maybe you understand it better. Um, have you tried quantifying the confidence that the results of two models trained on very small data sets are different significantly and not just due to noise? >> Yes. Yes, we do that. So that is one of the main directions to as quantify this this noise. Yeah. >> Could you explain a bit? >> Yeah. I mean it's it's like um the so this is one of like like we get we we get performance means and we also look at at the standard deviations and um uh

**[28:49](https://www.youtube.com/watch?v=YPY0lY6tDvM&t=1729s)** because if you have two solutions then of course um one should also do a significance test to to find out is are those two solutions really different. Yeah. >> Awesome. That was the last question. Thank you very much. Uh, a round of applause to our speakers.
