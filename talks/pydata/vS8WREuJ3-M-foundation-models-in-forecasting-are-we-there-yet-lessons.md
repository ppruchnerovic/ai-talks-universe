---
id: vS8WREuJ3-M
title: "Foundation Models in Forecasting: Are We There Yet? Lessons from the Trenches"
slug: foundation-models-in-forecasting-are-we-there-yet-lessons
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Dr. Irena Bojarovska"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-04T22:21:10Z
video_id: vS8WREuJ3-M
url: https://www.youtube.com/watch?v=vS8WREuJ3-M
youtube_url: https://www.youtube.com/watch?v=vS8WREuJ3-M
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Training, fine-tuning & model building"]
transcript: true
---

# Foundation Models in Forecasting: Are We There Yet? Lessons from the Trenches

**Dr. Irena Bojarovska**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=vS8WREuJ3-M) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Dr. Irena Bojarovska share a hype-free, production-tested look at whether time-series foundation models can truly replace specialized local models in forecasting.

Speakers:
Dr. Irena Bojarovska

Description:
Zero-shot forecasting aims to predict time-series data without model training, utilizing foundation models to handle multivariate settings and global forecasting across multiple markets and KPIs. Traditional statistical models and tree-based methods often struggle with consistency across related variables, such as the relationship between gross merchandise volume, item count, and average price.

Testing with Chronos 2 demonstrated a 4.6 percentage point improvement in weighted average percentage error for GMV compared to baselines. The model's success stems from time and group attention layers and training on synthetic data that captures causal relationships. This allows the model to maintain consistency across different KPIs and markets without the need for fine-tuning, provided that past and future covariates are integrated.

Production readiness requires evaluating five pillars: accuracy, stability, consistency, exogenous sensitivity, and scalability. While zero-shot capabilities are effective for aggregate-level forecasting and cold-start scenarios, the models currently lack scalability for article-level forecasting and do not provide native explainability or feature importance. Effective implementation remains dependent on high-quality data preparation and the careful selection of covariates.

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

*4,502 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=6s)** I'm going to start with a question. How to [clears throat] cook without cooking? Do you have some tip for me? I think any working parent can probably relate and would dream of having a solution to this problem. And um we are here in Germany and I was thinking that probably one answer I will get is uh buy a thermomix. So what I want to speak today about is something about cooking without a cooking when trying to forecast time series. Is it possible that we are able to predict some data without actually training? This is the so-called zeroshot forecasting problem.

**[0:55](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=55s)** At the same time, we still have to use the coariates. Ideally, we have to be I not have to, but we could be in a multivariate setting and a global fashion. Which means that if a normal thermom mixture just cook one meal at a time, are we able to deliver a five course menu with just one go and even without pre-program such a menu. So it sounds like the dream and this is what I want to take you through today. a journey on foundational models for time series forecasting and what we have tried about at Salando. So this is the title the content of my talk. I'm going to uh go with you a

**[1:46](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=106s)** little bit about the short but very deep history of foundation models. So think about LLMs but specialized for time series data. Then we're going to check what is the interesting thing about having a zero shot forecast. Is it really working and what it can bring us when we think about forecasting at the scale of Zelando or any other big e-commerce or other um type of company that works at scale. Finally, what should we look at? should be happy looking at the accuracy only and close the project so to say and go rest or is there something more that we should care about.

**[2:35](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=155s)** So first of all I want to share with you why is it important for us to look beyond the classical time series forecasting. Zelando is a leading multibrand fashion and lifestyle destination in Europe. It's a very um big um assortment first of all then very big sa um um scale in terms of we are operating in 25 plus markets and we are generating more than 17 billion GMV in one year and we need to know when is this GMV coming and where is it coming from. Moreover, we are not only interested in forecasting um GMV but a set of other variables or KPIs like for

**[3:26](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=206s)** example the number of items that we are going to get for example the cancellation rate our partner program share and so on. So we have in total nine KPIs and then we have a horizon up to 112 days and we need both daily and weekly granularity. So as you can imagine we really love to forecast but we also really struggle keeping this whole layer of forecast alive accurate and usable. So is foundation model any foundation model able to help us in this task? How it all started? So here this timeline is probably not so correct in the years because you see we have um few years in a row. We all know how time

**[4:15](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=255s)** series um forecasting was solved in the past with statistical models. Then transformers were very popular at some point trees and so on. And then in 2023 a series of time series um uh foundation models appeared uh like time GPT and Lama then 24 more of them appeared and we were reading the news reading the papers uh and thinking okay we really have to try this out and we had the chance to have a three-day hackathon in May last year where we explored everything that we could find and Um um I will share the results with you in a moment. Afterwards in October a new version of Kronos foundation model appeared that was very promising and

**[5:05](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=305s)** then again we had the mindset okay we have to try it out and uh we tried it out. We had a 10 days research sprint where we uh focused particularly on this model investigated a lot researched got some results got excited and finally this quarter we had a end to end initiative to see how much of this we can actually even put to production. So it was quite a journey and um let us now see how it worked in the two hackathons that I mentioned in May 2025. If we were following our mindset, think big, act fast. That means what is everything that we can find uh what are the usual baselines that we use in forecasting and how can we compare those uh different

**[5:55](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=355s)** models if we focus on market level GMV and just forecasting the next seven days. Mostly we did zero shot but then we also tried fine-tuning and um we tried coariate integration but this was a problem to most extent because it was just not possible with the given models. Then in the other hackathon in December our focus was on finding a solution. So we gathered the forces and we decided to go all in uh trying out Kronos 2 because it was promising in terms of being able to take future coariantss and also being able to even forecast globally let's say more markets at once and even more KPIs

**[6:46](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=406s)** at once. Now I think I'm sure you are curious to see the results. So in the first hackathon we play to win but we also dare to fail and we kind of also failed because our models were matching to some extent the baseline but this was not enough to go live into a business context. Being able to have a model which is sensitive to the coariantss is very important and this was just not given and the accuracy was also not um mind-blowing and we were thinking okay it probably just means that we need to fine-tune more and we didn't do it and we kind of blame it on that. Then we had the next hackathon in December and there funnily enough just taking the model as

**[7:37](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=457s)** it is trying zero shot was already showing great results with the right context like with used um past and known future coariantss and it just worked pretty well. So on some um KPI like for example GMV which is our most important one the weighted average percentage error was on average improve by 4.6 six percentage points and we were like okay in May we were thinking we have to fine-tune and now we were like wait we don't have to fine-tune and this was really cool and now I want to try to help you understand how come so uh Kronos is a very cool model with a lot of great ideas which I think are

**[8:26](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=506s)** value val valuable on their own not even in this particular setup. So the architecture is very interesting and I think probably would take another talk like this or even longer to go through this. But I would like to pay your attention to the things that are different from the previous foundation models in forecasting and which make it more successful to my opinion. That is these two layers here that is time attention and group attention. While we all know about time attention and how usual the model is learning from the time series itself and the things were happening throughout the history. Group attention is focusing on a given time point but then checking what was going

**[9:16](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=556s)** on not at one time series but at a series of time series. So you can think okay how is Germany acting upon let's say a black Friday and how is Austria or Poland or another market performing at that same period. Moreover, not only markets per market but even if I think okay if my GMV is changing how is the number of items changing or the average price. So all of these things are captured in the uh group attention and another I also think secret powered which is not secret the source is open source and there are very nice introductory uh videos that you can watch. Uh the model was trained on synthetic data. Um and the way this synthetic data was built is very elegant

**[10:05](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=605s)** and very powerful because it tries to capture a relationship between time series that we can find in reality and not only normal and usual correlation but even causal effects. So this is really excited and this is I think what um changed our perspective but also gave us a different win which we did not expect but we were happy to get. So yeah fine-tuning didn't was a hope for us. I was thinking about building a foundation model for fashion data or something like this. We have seen it for other types of data but it turned out that if we have the right context then actually we don't need it and I think here the hypothesis is that

**[10:57](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=657s)** this synthetic retraining is already capturing um the relationships and this is then much more effective than retraining the model. So the analogy is here if your teopix doesn't know how to make a tiramisu maybe you don't even need to teach it but it's very important that you write buy the right ingredient right and um now I'm going to go back to this original big problem that we are facing right so having an accurate and good and stable forecast without training I mean it's great it's nice to have but we were also kind of thinking Okay, wait a second. Here we are getting something even more. And that more comes from the fact that the Kronos model that we um were trying out is able to forecast all

**[11:49](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=709s)** markets at once, all KPIs at once and all u time horizon at once. The only thing is that daily or weekly one has to decide on the frequency. So you can have both and um this is something that you still have to take care either afterwards or decide only for the lower granality for example and then do um some kind of reconciliation afterwards. And um this is really amazing right because our models that we have in the past and also very recently we had great uh success with for example global light GBM when we were forecasting all markets at once. We still had the task on figuring out this relationship between

**[12:38](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=758s)** the variables that I mentioned like number of items times the price is equal to my GMV. If I forecast this in the three different forecasts, the numbers will not match. So we had to reconcile and the relationship is more complex than what I just said. And Kronos thanks to this in context learning is managing to capture this relationship and to give us consistent data and this is really amazing. So what do we do? Um the thing is that I don't want to stop here and there is one thing that was in my mind already before let's say playing and actually using foundation models that is we have to listen to the people who are using our forecast. Our forecast is not just there

**[13:28](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=808s)** because it's cool and because we are wizard who can predict the future but the forecast is there because some decisions need to be made upon that forecast. And if the forecast is not for example stable enough, if the forecast for the future is changing a lot as we come closer to this date then our planners cannot rely on it. If the forecast is not sensitive to the coariantss that are we are giving to it then again this is not that useful because we want to know how our actions impact our um GMV that we are expecting in the future and um here there was actually I'm very happy there was a talk on forecastability just um I think

**[14:18](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=858s)** yesterday or before yesterday by Ilia you should check it out It's very nice that there are ways to measure this and there are ways to measure this and there are ways to even figure out how to adapt if this stability for example is not given. So that's why I want to say that we have to look at the big picture when we are choosing what should we go with at the end and um I have something here that I call the production readiness score card and it has five pillars each of them I think is um very important. Of course the accuracy is very important and here again um a connection to another talk from my colleagues at the Zalando that was just before the break

**[15:06](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=906s)** on the accuracy. I say here it is very important to have an accurate forecast but do we even know how to properly measure this accuracy and when we are comparing do we know how to properly compare? It's very easy to go into this trap of comparing apples with oranges and then it's a problem. So carefully choosing the accuracy metrics, comparing and then um being able to and also the period right. See here I wrote on the hold out set we had this negative experience in the past when we were training a certain amount on certain amount of data and doing an optimization on it and then testing in a test period but not leaving a hold out period on which we did not perform the HPO. And

**[15:55](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=955s)** this is very um difficult in a way that it can really lead to overfitting and it can lead to promising a number that you are not able to deliver when it will come to putting this forecast live and use it. Then the second measure that I already mentioned this is stability and here there are two types of stability vertical and horizontal stability and both of them I think equally important uh one is measuring okay if I'm going to forecast some uh number in the future as I'm coming closer to it if my forecast isn't jumping around I cannot really use it because I need to plan how many

**[16:44](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1004s)** people are going to work in the logistic ICS warehouse one month in advance and if you're going to change that number two days before they are about to come I can't so fast or it's going to cost me much more to now all of a sudden hire 100 more people but here there is again an issue that is sometimes these numbers change not because the forecast was wrong but because the reality changed because what if the marketing department decided all of a sudden to play a big um voucher campaign in some country and then that is what is raising the forecast and it's right to be different from the original one. It's a very difficult topic. Then we come to the consistency when we are producing different KPIs we need to make sure that

**[17:35](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1055s)** they are consistent with each other because our forecast is used by different pillars in the company and different decisions are made. If you think again about the warehouse probably you can imagine that they are not that much interested in how much GMV do we expect because if we tell them okay expect 100,000 but this is maybe 10 super expensive jackets. Okay number don't make sense right but you can make like 10 expensive jackets versus packing 300 socks. you need quite a different amount of people in the warehouse to pack this or the other although the GMV number was the same. So that's why for example number of items is another very

**[18:24](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1104s)** important KPI that we forecast but it has to match to the average price that we are expecting. And finally coming to the exogenous sensitivity here all the future coariantss are super important and I think this is what made Kronos 2 being so good is because we could include this coariates. So a model that doesn't know about our plan per default somehow cannot be that good. And I'm really curious to see because since October I'm starting to get a bit worried have to say because since October I have not seen any big um let's say new models coming out there that will capture this idea and try to implement it and integrate it and that we can test it out. And finally scalability. This is for me a little bit

**[19:14](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1154s)** the sad point. I just moved to uh article level forecasting team at Salando and uh I cannot bring this with me because the uh research sprint that we did at least the first iteration showed that at this scale at the moment the model is not ready to give us the solution that we are looking at. And I think this is not only related to the scalability and to the performance but also to the uh architecture. And here if someone has some successful stories I would be very happy to um listen to them. So now we come to the final question. Are we there yet? And um my answer is zero shot is real but zero effort is not. And the future

**[20:03](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1203s)** is hybrid. So it is true we can forecast without pre-training. We can cook without having a recipe and without needing to sit in front of a stove. But we still need to have some effort made. And this effort is going to the right shop, buying organic ingredients. I mean to be honest one of the biggest problems that we have during the years in working in forecasting when we try to figure out what was wrong with the model most of the time that was something wrong with the data. If we give wrong data, inaccurate data, wrongly prepared data, anything of this can lead to some

**[20:56](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1256s)** results that were not as expected. So this is one thing that we have to continue do and um the other thing that we need to take care is then again how is this forecast used right so the five pillars that I mentioned can we tick all those boxes and this requires quite some amount of work that goes beyond that zeros forecasting so with this I still hope that you uh get some glimpse about um how we try the foundation models at Alando and um I am now happy to answer any open questions and uh get your feedback. Thank you. [applause] [cheering] [applause]

**[21:43](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1303s)** >> Thank you Arena for a wonderful talk. Uh we have couple of questions from the app. So I'll just take one by one. Uh first question, how different are different foundational models in performance? Who is systematically winning the race? Kronos. >> Mhm. Good. Thanks a lot. So here I would um first ask sadly I don't know if it can be follow up. When we think about performance, do we think about the more accurate or in terms of speed? Because if it's in terms of speed then here when we are working on aggregate level as you can imagine we don't have any issues because the data is relatively and absolutely in general very small right

**[22:32](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1352s)** when it comes to performance at the moment um Kronos 2 on a um on a set of KPIs and markets Kronos 2 was for us the winning model but also on par with global light TBM So but when we compare to other foundation models then uh definitely that one we had a long collaboration and it's still active with NIXLA and time GPT but unfortunately the topic that I mentioned on the future coariates looks like has not been completely solved yet so that's why there is still an open question about the performance >> okay thanks u we have yeah questions of similar flavor related to Kronos 2. So I'll just club them together. So is

**[23:21](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1401s)** group um in Kronos 2 the same as hierarchies? Does Kronos forecast market and detail articles at the same time? >> No. So this model is not hierarchical in the structure. So there is a group attention. So there is a knowledge about the different things that we put in the model. But it's not per se hierarchical. It's not something that will take care of predicting both article level and category level let's say together and make sure that they are reconciled. I would be happy if some extended version comes out that can do this. It would be super nice. >> Okay. Thank you. One more question on

**[24:09](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1449s)** Kronos 2. In your experience, what number of co-variants can Kronos 2 handle reasonably while still improving the metric? >> Super good question. I kind of hide that part in the presentation, but choosing the right coariantss I think is one of the most important and crucial aspects and it's not so easy to decide. And here I think the size of the set like how much I guess it also depends how much you have. So as compared to let's say light TBM here we did not use coariates like taking legs of some KPIs and so on. We just use actual coariates about things that we know related to Zando

**[24:58](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1498s)** like the commercial calendar average coupon rate discount rate maybe the weather personalized marketing cost and so on. But even here even if I take just the commercial calendar it's so complex that there there are some hierarchies and there I have a a variety of choices how to go from this commercial calendar to some informative data that I put in my model. So I think I don't think that there is a limit on the model itself and also it's very cool that the model can forecast a lot in the future and it forecast it all at once. So there is uh no um yeah so it makes it also super fast but at the same time yeah the coariat question is still left to the experts and there I have one idea

**[25:47](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1547s)** that I um still didn't manage to try it out maybe many of you have heard about auto search so this is like if you give some OPUS or some other LLM the task to iterate um over different configurations and try to come up to an optimal configuration kind of like an HBO but done by a LLM instead of Ray or Optuna and so on which is difficult to do if you just have a set of coariantss where the number of subsets that you can take is um arbitrarily um so I was thinking that maybe another LLM can decide which are my optimal coariantss but I haven't tried it yet >> okay thank you uh we have next [snorts] bunch of questions related to explanability. So I'll group all of them

**[26:36](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1596s)** together. So what is the state of explanability in time series foundation models and do you use explanability methods to guard against forecasting mistakes? >> Yes. Uh it's a good question and I think it's another difficult one. um I don't think at the moment the architectures as they are um are giving the opportunity to explain we used to use transformers uh temporal fusion transformers for example in the past and they offer as per the paper let's say that these models are explainable we never managed to make this work other simpler methods like profit maybe there we did some um demand drivers sensitivity where we try

**[27:24](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1644s)** to show which are the coarias which are more important but um I find this topic super hard and most importantly even if I know and I'm able to say that there is a correlation it doesn't mean that there is causality so we try to convince our stakeholders that they should better focus that it's um um accurate uh because explanability is hard >> uh yeah a follow-up question is there a way to plot got some kind of feature importance then >> um not that I know about. Yeah, good question but I don't think so. >> Cool. Uh next question. So did you try to do top-down reconciliation of more aggregated predictions based on the foundation models?

**[28:12](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1692s)** >> Um good question. uh we have not um we have tried forecasting categorical level so something in between top down so not a market and not an article but like category like male jeans or female shoes and something like this and actually this turned out to be pretty good and also good for um cold start like a start of the season where our current um uh trees are struggling but [clears throat] otherwise not um we have tried different type of reconciliation and here I really um recommend for example an XLA library and other libraries have is so-called mint reconciliation so optimal reconciliation where you don't go bottom or top down but just find the the the optimal by

**[29:02](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1742s)** taking both um um outputs but we were using this for the task that I mentioned about forecasting different KPIs so if I have my GMV, my items and average item price, how do I reconcile them without throwing away any of these forecasts? Because in top down, you end up throwing up if if you had it in the first place and like this you can remain everything and still have optimally reconciled KPIs. >> All right, final question of the session. Uh where did foundational models succeed and where did they fail? Are there some phase space where they outperformed tree significantly for example new product introduction? >> Yeah, very good question. So I think

**[29:51](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1791s)** interestingly they do perform well both on established. So we I did not focus that much on articles but more on the markets but markets themselves they have the same property right you have mature markets like Germany and Switzerland and then you have uh lower performing markets or new markets uh and here we do see a better accuracy in the um compared to what we have at the moment in the newer markets but then it's a question is it because the model is so good or is it because our baseline is so bad. So it's hard to say but u yeah I think reasonably well in both scenarios. All right that's it from this session then thank you all for all your

**[30:39](https://www.youtube.com/watch?v=vS8WREuJ3-M&t=1839s)** questions and being a wonderful audience and let's end the session by giving Adina a big round of applause for a great talk. >> Yeah thank you. Thank you.
