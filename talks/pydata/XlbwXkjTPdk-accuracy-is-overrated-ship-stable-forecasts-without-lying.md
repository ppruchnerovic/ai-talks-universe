---
id: XlbwXkjTPdk
title: "Accuracy Is Overrated: Ship Stable Forecasts (Without Lying to Yourself) [PyCon DE & PyData 2026]"
slug: accuracy-is-overrated-ship-stable-forecasts-without-lying
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Illia Babounikau"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:20:30Z
video_id: XlbwXkjTPdk
url: https://www.youtube.com/watch?v=XlbwXkjTPdk
youtube_url: https://www.youtube.com/watch?v=XlbwXkjTPdk
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Accuracy Is Overrated: Ship Stable Forecasts (Without Lying to Yourself) [PyCon DE & PyData 2026]

**Illia Babounikau**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=XlbwXkjTPdk) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Staff Data Scientist Dr. Illia Babounikau explain why accuracy isn't everything and how to implement stability techniques to build forecasting models that business stakeholders actually trust.

Speakers:
Illia Babounikau

Description:
Forecasting instability occurs when retraining a model on new data causes the long-term forecast to shift dramatically, even if the overall accuracy improves. This vertical instability disrupts business planning and erodes trust in the model. To quantify this, the Mean Absolute Relative Difference (MRD) is used to measure the bias between overlapping forecast periods across different revisions.

A stress test of various models on real-world e-commerce sales data reveals a trade-off between accuracy and stability. Simple statistical models and Generalized Additive Models (GAM) tend to be more stable, with MRD often below 0.1, though they may lack precision. In contrast, complex models like XGBoost, LightGBM, N-BEATS, and foundational models such as Chronos and TimeGPT often achieve higher accuracy (lower WMAP) but exhibit significant instability, with MRD frequently ranging between 0.2 and 0.4.

Three post-processing techniques can mitigate this instability. Reconciliation stabilizers use a top-down approach, scaling granular product forecasts to a more stable high-level shop or category forecast. Assembling stabilizers use simple averaging across multiple models; this generally improves stability but can be compromised if a single unstable model is included in the ensemble. Origin assembling, or full interpolation, mixes the current week's forecast with previous revisions using a weighted average (e.g., 80% current, 20% previous). This method frequently provides a win-win result, improving both accuracy and stability.

The findings suggest that simpler models are often preferable for sparse data or when long-term stability is critical. When using ensembles, preselecting stable models is essential to prevent outliers from spoiling the aggregate forecast.

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

*4,072 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=5s)** And let me start. I'm Ilian and it is my already fifth year at Python. So I hope you enjoy Python as much as I enjoy it. And I'm already more than 10 years in data and I think it's all started when I put my head in accelerator at CERN. That's how I started with the data large collider and proceed to e-commerce and supply chain and currently I'm working at voids where we run air power performance software and blah blah blah. So all this marketing stuff but what is important is we do a lot of forecasting a lot of forecasting. We work with a lot of segments from pet food to stylish hoodies and you see quite a lot of revenue we

**[0:54](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=54s)** are forecasting it means we need really stable and accurate forecast. One of them are our prior responsibilities. And imagine we ship some forecast. It [snorts] may be even a bit better. W map was improved, reduced by 4%. Nice. Now you need to put it into production. You put it in production. Uh you but unfortunately you need to sometimes retrain your model and reore forecast. For some reason you cannot just ship the forecast and forget. you need to operate it maybe every week, every month. And that's pretty annoying because your forecast actually can jump up and down significantly. Here's an example. You see this is super nice time series um from one that we work with. First you

**[1:45](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=105s)** deliver some forecast in uh November, this blue line. Okay? Then one month later you retrain your model and that is your new forecast. 30% down. Is somebody happy? No. One more months later even 50% down. Is it acceptable? No. Planning team need to redo decisions. Trust in the forecast is lost. Doesn't matter what was the accuracy number. If somebody see like this, it could be quite unacceptable and it looks like your model is insecure. And with every revision meaning like retraining and reforcasting it changes its long-stand dramatically. And what it means it means focus is unstable. They need to replen decisions

**[2:36](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=156s)** complex. And to be precise when we speak about instabilities there are multiple levels of instabilities. It could be that we take the same origin, the same target and it means our model is just not replicable. Okay, what we are more interested in the top right corner calls vertical stability where we do forecast from different revisions for example retraining last week and this week and forecast let's say for the next month and then we see that okay our model shifted up and down by let's say 10 20%. And that's the one that we are interested in and we would like to uh study in uh this talk. You can define multiple metrics. Here I

**[3:26](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=206s)** selected one of the simplest one mean absolute relative difference that we will be looking at. It is um you sum up the forecast of overlapping period for the future between different revisions for example from previous week and this week and you calculate the difference. So formally it is bias how the new model new forecast this week is biased according to the previous forecast from the previous week and just you take relative and see uh how it looks. Let me explain a little bit what is our experimental setup. We take a real online sales data sets, anomi anonymize them of course uh train model and produce one year forecast ahead of us

**[4:15](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=255s)** and every new week or every new months we create new revision with new retraining and forecast again. And at the end what we would like to measure we measure stability metrics and we measure also accuracy because we would like to see how how they interfere with each other. We measure accuracy over out of sample period and stability for the full one year horizon into the future and we would like to put on our stress test a lot of models to see how this look like. We start with a baseline seasonality classical statistical mo models profit trees xjub boost logbm game model even natural nal and heat also hyping now foundational models let's see how

**[5:04](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=304s)** they perform we're really curious about your expectations and yes we will test kronos and time gpt and autoML and few words about data sets data sets uh that we have are quite interesting because this is not nice clean M5 data set whatever you can find in kegel. No, this is a real data set from real life. We have spikes short data and super big spikes and super sparse products some time series that I don't know what I can forecast here. fine and we put on the stress and let's have

**[5:53](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=353s)** a look how the the end results looks like. So this is types of plot I will be showing a lot what we let me explain a few words what is here on x-axis we have w map one of the most popular not the best metric but one of the most popular metric means lower is better more accurate the forecast is and on y-axis we have MRD this is our stability metrics again lower is better means the forecast is more stable here blue dots you can see simple time series and statistical forecast while it is rather on stable side between stability around 0 and 02.2 two you can see that error vary a lot. It could be quite our lucky shot that

**[6:42](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=402s)** statistical model worked out. It could be quite unlikely that statistical model was not the fit for this particular data set. Then we look at the trees and you can see the trees are mostly grouped in the middle of our accuracy and also kind of rather unstable side. But still you can see that a lot of red dots our tree models jump a lot of uh really high in instability meaning that our forecast with trees can explode from revision to revision sometimes depending on data sets anomalies and etc. Then we try simpler model let's say gam journalize editive model and you can see while we're losing a bit

**[7:32](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=452s)** in accuracy the stability is much better we are below 10% of stability meaning that our new revision is doesn't jump more than 10% from one to another then you can see n hits these triangles while we have some nice accurate forecast stability quite suffering most of the and his stability metric between 0.2 to 0.3 meaning we have from revision revision quite big jumps from training to enter training. Kronos similar story could be stable but uh sorry could be accurate but quite unstable and outlon you can see those here in this corner I don't know maybe we can invest a bit

**[8:22](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=502s)** more time most of the setups are quite vanilla setups models with uh best parameters we can find online and with some optunic but you can see results they speak for themsel. Let's look a bit deeper in another foundational model at Nixlam because we invested some time and talk to them. And here you can see similar experiment we performed with Nixlam. Here I just showing large GBM gum model and time GPT time GPT with the stars. And you can see again you can have quite accurate here with time GPT model and an accuracy level is similar to large GBM a bit better than gum model on average

**[9:11](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=551s)** but again stability here is suffering most of the points between 0.2 and 0.4 meaning that from monthly revisions it could be jump up to 20 40%. Yes, it outperforms in the case of short data. Here you can see time GPT model produce nicer forecast where large GBM model actually failed. But it also could be vice versa where it underperformed for long and sparse data where we have a lot of data and uh with a lot of anomalies and events. So now we learned okay different models can bring different stabilities but what we can do in post-processing maybe we can do after this something

**[9:58](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=598s)** like stabilize the model without losing too much of accuracy and there are different approaches I will mention three the first one will be reconciliation stabilizer the thinking is quite simple we have much simpler model that does some forecast on high level. Let's say on the full shop on the full category level and we use reconciliation to with top down approach where we split high level forecast to the smaller focus on product level based on the product level forecast and the expectation is that model on average become more stable because it always scale up back to the uh simpler uh shop level model.

**[10:48](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=648s)** And here the type of plots that I will be showing in the next few slides on the y-axis. Now we have delta inaccuracy data in the metric and left so means that we improved our accuracy. So here left corner or left side means we improving the accuracy with this uh method and on yaxis we have our stability metrics and lower means that we improve stability of our model and here you can see results. So of course ideal case is left bottom corner where we improved both stability and accuracy and you can see that does it really help? Not always. What we observe that

**[11:37](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=697s)** nervoseness or instability of uh of the model can be learned perfectly learned actually on shop level as well on high level and then you have mixture of two instabilities on shop level on granular level you mix them together quite quite often it's doesn't work um but it helps against really big flotations you see a number of few examples a number of data sets this is really helped and st both stabilize and improve accuracy But this approach is debatable. Then another approach is how to stabilize the model is assembling a stabilizer. You might have seen like M5 competition or other kegle competitions where the winners or top five just drop tons of the models and assemble all of them and

**[12:28](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=748s)** that produce even better results. Let's give it a try. We try the simplest assembling averaging. You just mix a lot of models. All the models give equal weights forecast and surprisingly it it works. Yeah. So you can see that a lot of those here are in the bottom left corner. So it really helped a lot of models at least become st more stable or a bit more accurate especially versus mean within this group of accuracy or stability. But also you can see that there are number of really bad results that we lost actually in both stability and accuracy. And when it happens, it happens when in inside your ensemble there is one two models that are really

**[13:16](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=796s)** unstable, really can escalate especially long-term future up down and it spoils the full assemble. So in my conclusion would be it works but you need to you cannot just blindly drop and assemble tons of model. You need to press select them find really on rather reasonable scales table and then assemble can even make the full collection of the models better. And the last approach that was quite interesting and you can find more details in in this paper. This is origin assembling or full interpolation where we take the model from previous week and mix it with a model from this week retraining and then we can go like n weeks in the past. We mix it with a particular weight. Here you can see the

**[14:05](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=845s)** formula for example 0.2 two meaning we take 20% of previous week model mix it with 80% of this week model and forecast in the future with this approach and here you can see quite interesting results because when we using this origin assembling or full interpolation a lot of our experiments end up in win-win region that we improve both accuracy and stability of our model of course majority this kind a bit expected end up in tradeoff. We we trade off between stability and accuracy. So model become more stable but a little bit less accurate on rather short evolation period. So it's interesting this approach is kind of you almost

**[14:55](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=895s)** cannot lose when using this approach if using this approach in rather smart way and worth experimenting. So this was three types of stabilization one can use and for the conclusion I would say is like if you care about stability means you're building a real product that can deliver value to the users because otherwise they lose trust otherwise they don't know how forecast what you perform because accuracy always is calculated on some short period. You don't know if this period is the same. You can have concept drift. You can have a lot of things and usually much more stable forecast on the long term performs

**[15:45](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=945s)** better in business processes. Unfortunately, I really hoped there will be some more magic peel where you just okay use foundational model it give you super great results or use best pick model and slee give you really great result you are done but unfortunately there's no this kind of magic peel and you need to learn unfortunately learn your data spend time on tuning your model and what I can recommend and try simpler model. Not every use case of forecasting deserves the most complicated model you can find. The more complicated model, the more unstable it is. If you can use simpler

**[16:33](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=993s)** model, linear statistical model and deliver the same accuracy, the end result in most of the cases will be much more stable. If you're using assembling, press select high quality models and then in this case assembling will deliver much better results. So that's it from my side. Thanks a lot for your attention and I think this time for questions. [applause] Thanks a lot I this was very insightful and deep dive into a very important topic for everyone doing forecasting. Let's go now uh through the questions

**[17:21](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1041s)** and I'm going to start with the first one. Why not to consider the forecast uncertainty for the model? This is valuable information that is not used in this experiment. >> Yes, that's right. we were only discussing uh point forecast uh not uh probabilistic forecast in uh all the studies. So I think that's something that we can expand this research and uh see how how to perform with uncertainty and how the uncertainty will be correlated actually with real instability because yeah retrainings yeah I would say it will be interesting it will be interesting to consider this and see if uncertainty of the forecast will be a good primer of potential

**[18:10](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1090s)** instability of the forecast. >> Yeah. Thank you. Uh, another question is on stacking. What is your op opinion on stacking? Feeding the predictions of all models to a final simple model like linear polomial regression or a fully connected neural network with linear activation. >> So stacking is a bit debatable. So we we haven't tested it. This is something that we would like also to test but it is goes a bit into the direction where you learn your stacking in some historic previous like evolation period and you believe that this stacking will

**[18:58](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1138s)** make sense in the future. What we did try we did try like best peak forecast where we assembling and doing the stacking but the winning pro the winning forecast with the winning model for particular product takes all so it fully so formally we like do the stacking with activation zero and one yeah for each focus and we saw that it's very unstable because as soon as you re relearn the stacking your model can fluctate up and down quite significantly. Yes, with linear activation it's something to test it out. I think it will be smoother but I think the general problem is there when you reone the stacking it accidentally can flip some models or give totally different ways to different models uh

**[19:47](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1187s)** than in previous revision that would lead in uh events disappearing some seasonality disappearing and some uh significant issues. >> I see. Thanks a lot. Uh another question is the following. Did you utilize short-term lags and predicted with continuously available coariantss meaning lags from actual or did you utilize lags from the predictions ea iterative approach for longer forecast periods? So we tried both uh we tried both uh I think here in um and uh in trees models we use uh legs from predictions as well for long-term forecast but for example for linear model we use

**[20:35](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1235s)** frozen legs so it means that we uh use for only leg that is frozen after the training period is finished >> I think okay we're good uh then a Question about sparse time series. Do you have any advice on creating robust forecast for sparse time series? I you are missing observations. >> Yes, the advice will be similar. Use simpler models. Simpler models especially for sparse or very sparse time series uh would do the job. And as well uh reconciliation quite helps in learning because the problem with sparse days you cannot learn much on time series level. You need some

**[21:24](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1284s)** reasonable not overtrained model lower level but when you reconcile it on some shop level category level whatever you can extract a lot of good features like events seasonality behavior prices and etc. >> Very good. And I think this is related then to the And uh next question which is exactly on the hierarchical forecasting. Could you elaborate a little bit more on hierarchical forecasts shops category? How do you bring them together? Have models like time GPT automatic handling of hierarchies. >> Okay, let's me start from the end about uh CH GPT. Oh about time GP. You need to ask Nixl. have no idea if they have automatic handling of hierarchy. Uh this

**[22:13](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1333s)** something that I would also be curious to ask them. Um how we handle it at the moment. Uh we do it with reconciliation where you have multiple levels at which you're forecasting and then you can reconcile it either top down or middle out or actually you can also learn the reconciliation metrics on also historical period. Yep. Thank you. Did you utilize a shortterm? Oh, sorry. No, that one is answered. Sorry. Now we have another one. Instead of an assembling, what about making the predictions of model X1, X2, so on XN new features of model Y? Could that could be that model Y learns from

**[23:02](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1382s)** signals and then learns also which signals which model captures the best. This could be the approach. I know a few examples where it worked out when you have really a lot of data with really a lot of clear signals and etc. um on our data sets I would not go so much into into this behavior because you just don't have enough data to to capture this uh signals uh without overtraining I would say because what you're describing because we describe okay you can have best peak then we describe you have linear activation and

**[23:50](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1430s)** this is one more next step where to train model of another model of input of the uh and use a lot of simpler models as input to uh second model. Um it's something to experiment with but I don't see it will perform better than for example similar linear activations and etc. I am quite often quite against uh over complicating the models if simpler models can do the job. >> Yeah, I think that's a good one to have, right? [laughter] It helps. U did you try to combine different methods? Maybe this was partially um answered, but the question is how about an assembling and

**[24:38](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1478s)** convex combinations of models from different weeks? >> No, we didn't try. I mean face space for experimenting is huge. Yes. So we needed to limit uh some face space for experimenting and yeah take more like basic approach in every direction and see where it works. So maybe next year with the next talk we'll find out much much more complex experimental setups that will work. >> Sounds good. Uh another question is um going again to the direction of um ensembling. Do you think that similar stability or accuracy metrics can be achieved by defining one unique right model architecture or feature selection

**[25:28](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1528s)** for your specific use case instead of assembling different models? >> That's a that's a good question. That's something that we are attempting to find this magic pill maybe really good architecture but the big problem is that we have a lot of different use cases and a lot of different clients and some models or that could be quite stable and accurate for one client one data set could be total disaster for another client total data set. Yes. And that's exactly if you look at this plots like okay you have see boosting decision trees are jumping

**[26:16](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1576s)** really quite significantly in accuracy and on this plot maybe it's not too much visible but then uh when we have other tables where the winning model per data set and usually the winning model per data set uh is quite different for different data sets because there are on average winning models that win let's say three data sets out of 10 but not more >> I agree okay good uh we have few more questions [laughter] >> I should have made my talk longer >> yeah but I think it's very valuable for all of us so I am curious about this one might it improve the results when using the median instead of the mean for all

**[27:05](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1625s)** models to improve um stability. I think this refers to like taking the previous predictions and um but instead of the mean take the median >> or on the models. I think we saw two types right we ensemble models or we ensemble previous forecast. So I don't know where there was a mean taking the mean and would taking the median improve. >> I mean for some reason it sounds a bit like uh that we uh from probability forecast trying to make point estimator but if some if somebody from audio from the room asks a question so can they comment >> you mean assembling a stabilizer here?

**[27:54](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1674s)** Okay. So this variance but what do you mean taking median? Yeah. Then we will have >> so if you have outliers they might be more neglected but it's not so important just >> no I mean that's that's good point that's interesting to experiment with the problem is that here we're taking mean of the forecast and one what you call outlier could be a signal like event promotion etc. Yeah. So on average it would of course improve stability because

**[28:44](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1724s)** you're getting rid of stronger signals. But if uh you you want your model forecast some uh some spikes or some big movements at the end then you actually could reduce your accuracy in this way. But uh again this interesting is an interesting idea to experiment. >> Okay. So I'm going to read the last uh question. Um there are a few more but maybe you can uh check them and everyone is welcome to also approach Ilia after the talk to continue the discussion. uh wouldn't be basian methods ship both model uncertainty estimation and stabilization by ensembling or by sampling from the posterior naturally in bias estimation you are using uh the

**[29:39](https://www.youtube.com/watch?v=XlbwXkjTPdk&t=1779s)** same model the same family so they could be biased in the same direction or exploding in the same direction is one good thing about unsembling and why it works because you sample over different models that uh if one exploding or is not robust to anomalous another will be robust anomalous and uh ring beta performance I'm not sure how this would work in uh baian and something >> thanks a lot yeah maybe it can be a topic for the next research so thanks a lot for the very insightful questions thanks a lot IA for your great talk. [applause]
