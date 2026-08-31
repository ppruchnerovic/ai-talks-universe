---
id: K7Hl3vXB5wA
title: "When Space Weather Breaks Your GPS: Building an Explainable Early Warning System"
slug: when-space-weather-breaks-your-gps-building-an-explainable
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Vincenzo Ventriglia"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:20:15Z
video_id: K7Hl3vXB5wA
youtube_url: https://www.youtube.com/watch?v=K7Hl3vXB5wA
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# When Space Weather Breaks Your GPS: Building an Explainable Early Warning System

**Vincenzo Ventriglia**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=K7Hl3vXB5wA) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Vincenzo Ventriglia demonstrate how to build an explainable, real-time early warning system using CatBoost and SHAP to protect critical GPS and communication infrastructure from space weather disruptions.

Speakers:
Vincenzo Ventriglia

Description:
Solar activity, such as coronal mass ejections and solar flares, creates plasma density fluctuations in the ionosphere known as Large-Scale Traveling Atmospheric Disturbances (LSTADs). These disturbances bend and delay radio signals, causing positioning errors in Global Navigation Satellite Systems (GNSS) and disrupting high-frequency communications. To mitigate these risks, a multivariate time series binary classification model was developed to predict the onset of LSTADs over the European sector within a three-hour window.

The system utilizes CatBoost for gradient boosting over symmetric decision trees, with Optuna for hyperparameter optimization and MLflow for experiment tracking. The model is trained on a catalog of 1,600 manually labeled events spanning nine years. To ensure the system is explainable and trustworthy, SHAP (SHapley Additive exPlanations) is used to attribute predictions to specific physical drivers, while conformal prediction transforms point predictions into mathematically guaranteed prediction intervals.

The framework offers three operating modes—high precision, high sensitivity, and balanced—allowing users to prioritize either the reduction of false positives or false negatives based on the socio-economic cost of the error. Feature engineering includes moving averages and lagged features covering up to six hours of historical data. The resulting system provides near real-time forecasts via the ESGUA platform to support safety-critical infrastructure and space weather monitoring.

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

*3,760 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=6s)** Hello everyone. Thank you for being here. I'm very happy to be back at Pyon Germany and today I will tell you about space weather and how we applied AI to build an explainable early warning system. Um before starting a few words about me. Um I have a background in theoretical physics and I work as a machine learning engineer and data scientist in a research institute in Italy which is the national national institute of geohysics and volcanology where we study volcanoes, earthquakes but also the upper atmosphere, the environment in general and space weather. I also um love community and actually that's

**[0:54](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=54s)** why we are here today. Um I'm one of the organizers of the local chapter of Patt in Rome. So if you happen to be in Rome, feel free to uh to join us. We are always very happy to uh meet new friends. And this year I'm I'm going to be on the road to deliver some talks around Python uh conferences around Europe. So that's the agenda for today. We will start with space weather. And I don't know if everyone is familiar with this term. If everyone ever heard about that, possibly not. So auroras are possibly the most striking consequences of space weather. But that's definitely

**[1:44](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=104s)** not all the story and indeed before diving into the machine learning architecture um I would like to set uh the stage. So first space weather just like we have weather on earth we have weather in the space and this is uh the physical state uh of the near earth environment as it is driven by the sun's activity. You know the sun is a variable star. It has a cycle which on average lasts 11 years. So when the sun throws a tantrum like a solar flare or solar wind, this interacts with the planetary magnetosphere and these interactions can have

**[2:31](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=151s)** significant impacts on satellite operations communication power systems, Genesis accuracy and that brings us to Genesis which is a collective name for different constellations like the uh GPS from USA, Galileo for us Europeans, Glonas in Russia, Bedwin, China. There are also some regional navigational systems, but we are focused on the Genesis side. Um, we use Genesis for uh like every day for everything from maps to also timestamping, financial transactions. And it works by calculating incredibly precise travel times uh of radio signals from satellites down to Earth. But those radio signals do not travel

**[3:21](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=201s)** through a vacuum. They have to pass through the ionosphere which is a layer of the upper atmosphere extending roughly from 60 kilometers up to uh 1,000 kilometers and this is filled with partially ionized plasma. This region plays a crucial role in radio wave propagation as it bends and delays the radio signals acting like a giant mirror up in the sky um allowing for uh beyond the horizon communications. So when this density fluctuates you can get positioning errors and that's why we should care about space weather. This infographic actually perfectly maps out the uh domino effect

**[4:10](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=250s)** uh of a solar storm. Um so so this is not just about uh pretty auroras but a direct threat to everything from satellites in orbit down to power grids and navigation systems. And when insurance giants like Lloyds or even the European Commission uh publish risk reports on this matter, you know that this is a systematic vulnerability. Uh a study from ISA, the European Space Agency, estimated that um a single extreme space weather event could uh cause around 15 billion euros in soio economic damages in Europe alone. And that's because our mother infrastructures rely a lot on a space-based systems. And since obviously

**[4:58](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=298s)** we can't turn off the sun, our only defense is anticipation. And a few words about large scale traveling andospheric disturbances which are the u main topic of this talk. Um this is an effect a space weather effect of the upper atmosphere. Those are um plasma density fluctuations that are rippling through the ionosphere and they are usually associated with auroral and geomagnetic activity. Okay. And they have real world consequences since they can disrupt high frequency communications and also genesis positioning and timing. So the physical chain of the mechanisms involved in the formation of LSTs

**[5:47](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=347s)** um it's actually clear from a phenomenological point of view. You have something starting at the sun in the form of coronal mass ejection which propagates through the solar wind. Then you have injection of energy at the higher latitudes which then propagate equa forward as um as waves and then you detect LSTs at ground. [snorts] So how did we build um an explainable machine learning model for that? Um everything as I as I said starts at the sun. So we had to figure out how to um deise this task from a machine learning perspective and despite the clarity of the

**[6:37](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=397s)** mechanisms that I told you which are responsible for the formation and of the real time monitoring and prediction of this kind of phenomena uh remains highly complex. So we frame this uh problem um as a multivaried 10 series binary classification which is taking um different classes of inputs as physical drivers. So we tell the model something about the status of the ionosphere something about the geomagnetic state around the earth. So how currents are flowing uh around the earth. um some uh proxies for the forcing from the sun from above and also we tell the model something about the state of the sun. So

**[7:28](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=448s)** uh where is it um uh as a stage in the in its solar cycle, the number of sunspots and so on and so forth. And we trained this model based on a catalog of um instances which were manually labeled by ionospheric scientists. This catalog consists of roughly 16 events spanning 9 years. So covering almost the entire solar cycle. And the output of the model is trying to predict if uh LSTD is starting or not over the European sector uh in the next 3 hours. [snorts] Let's take a step back now and uh when you deise a machine learning model in

**[8:18](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=498s)** general you have to pick one either a more uh a simpler model or a more complex one. And in general when you choose uh simpler models they tend to be more interpretable but usually they might uh may lack some accuracy. On the other hand if you choose more complex models like complex deep neural networks they can be for sure more accurate but they for sure lose some interpretability. So in order to achieve both we worked like that. Of course we wrote everything in Python. We used cat boost as um a framework for gradient boosting over trees. I don't know if everyone is f someone is familiar with cat boost. I'll

**[9:05](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=545s)** tell you a bit more in a moment. Then we used MLflow for tracking the experiments and Optuna for hyperparameter optimization. And then on top of that we used shop as a layer for explanability in order to peek into the decision making process of the model and also debug it. So few words about cat boost. I'm sorry there are no cats involved [laughter] but it stands for category and boosting. And as I told you, this is a gradient boosting framework on decision trees which handles efficiently and in a very smart way categorical categorical variables missing values as well. And it al also has a peculiar architecture

**[9:56](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=596s)** which is the symmetric trees or balance trees architecture which has some nice pros like um an efficient implementation on CPU reduced inference times but also a natural form of regularization. It also integrates seamlessly uh with sharp as a method for explainable AI and it's also very easy to use with uh with Optuna for automatic optimization of the hyperparameters. In general, the trade-off between precision and recall or sensitivity um is a function of the end user which has to adopt and use the the model. Why so? Because the cost of false positives

**[10:46](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=646s)** is uh generally very different from that of false negatives. So instead of just delivering one model, we um devised what we call three operating modes. So you might go for the I precision mode um when the false positives are more costly. So for example, you don't want to issue frequent um unnecessary alerts uh that could lead to other fatigue or costly counter measures. On the other hand, an I recall or high sensitivity mode might be preferable for you when false negatives are more costly. So for example, you want to detect as many real events as possible even at the cost of some false alarms because missing an events for you could

**[11:35](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=695s)** disrupt some critical communications for example. So for early warning systems or safety critical applications, you will prioritize I recall or eye sensitivity. But for operational purposes, operational systems with also possibly costly counter measures, you might aim for the eye precision mode just to avoid overreacting to benign space weather fluctuations. And when false positives and false negatives matter equally to you, you can just go for the balance mode which is the one that maximizes the F1 score. Few words about uh about sharp. So we have given centrality to trustworthy AI matters and uh this in order to go beyond the blackbox approaches

**[12:26](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=746s)** um placing some emphasis on the interpretability and explanability of the model and this framework comes from the cooperative game theory. Okay, where the inputs of the model are conceived as players taking part into a cooperative game which is the machine learning model and uh the output of the of this model is essentially a price. Okay. So the output of shop is how can we fairly distribute uh the price the model output among the players taking part into the game. And as you can see the finally output uh is decomposed into a reference value

**[13:16](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=796s)** this one um plus a bunch of real numbers which are nothing else than the fe feature contributions for a specific sample. So this is a local explanation. Okay. uh where the sign tells you um uh the uh whether the the a certain driver pushed the prediction up or down and the magnitude of the sharply value tells you how strongly that feature impacted the model output. So sharp turns the prediction into an additive story and essentially that waterfall plot is just the additive path from the baseline to the final prediction. So with this tool in hand, we can peek

**[14:04](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=844s)** into the decision making process of the model and we can see how it uh reasons over time and which drivers are contributing to the decision- making process. And when you aggregate those instances over the entire uh sets, you can also build a global explanation in the form of a feature importance, a ranking of features uh which matter the most on average for your model. And this is very nice because this allows you to make contact with the um domain expertise. In this case, it was physics, but it can be everything that you like. So this is very useful in order to build trust in the model to drive user adoption but also to debug your model

**[14:56](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=896s)** because you can go with this kind of charts to your um fellow colleagues or to domain experts and ask them is the model taking the right path or is it just taking the wrong shortcut and it's not learning the meaningful meaningful things. But before shipping any model to production, you should characterize it a bit more. And we should understand that we have to move beyond point predictions. And to this end, we modeled risk and and uncertainty for this model as well. So we are currently serving near realtime forecasts uh for this model via the ESA platform at the ENTV which stands for

**[15:46](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=946s)** electronic space weather for upper atmosphere but the reasoning uh works like that in the real world acting on forecasts as a price tag. Costsensitive decisions can be more naturally addressed within probabilistic forecasting lens. And just for example, posing an expensive trilling operation because of a force alarm is costly. Sure. But missing a severe ionospheric disturbance could mean losing a drone or compromising a critical communication. And this equation essentially just uh formalizes that business logic. So the expected risk is just the probability of an event times the cost of that event

**[16:36](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=996s)** occurring. So given accurate estimates of the costs that are associated with force positives and force negatives, you can build a system that automatically triggers decisions according to userdefined risk levels. But before uh using this approach um we have to understand that standard machine learning models are poorly calibrated. Why so? Because 90% probability is rarely a true um calibrated probability. And in order to make some safe decisions, point predictions are not enough. And if you look at this chart, we are essentially uh serving not just a single probability line but also

**[17:25](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1045s)** prediction intervals. And so to um to get some robust intervals, we need to look beyond the standard outputs. So it comes uncertainty. Uncertainty quantification can be broadly divided in two classes of approaches. Intrinsic methods or extrinsic or postto approaches based on the fact that you do require some retraining of the underlying model or not. And to give you some examples uh of methods, you can think of vision approach uh and quantile regression as methods for intrinsic uh uncertainty quantification. While on the other hand,

**[18:13](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1093s)** good candidates of uh for extrinsic methods are calibration and conformal prediction. And I will tell you something more about conformal prediction which as you might guess it is a statistical framework for um any machine learning actually AI model to turn point predictions into prediction sets or prediction intervals. This is a nice approach also a quite recent one because um it is almost distribution free in the sense that you in general just require some exchangeability which is a milder IID assumption between test and calibration data. I'll tell you in a moment what

**[19:00](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1140s)** calibration data is. So essentially you ask uh that the uh distribution uh stays the same between test and calibration sets under some permutations of the data points. And that's the recipe for conformal prediction for one experiment. You can use it for classification and regression and it's quite easy to achieve. Those are the ingredients. You need a model that has to be already trained. After all, this is a posttock method. So you do not require um an explicit retraining. You need a neuristic notion of uncertainty which is a metric a distance between the x and y's. Um an error rate or an empirical risk

**[19:50](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1190s)** that you have to set say 5% if you want to aim at the 95% confidence level. And you need a pinch of fresh and seen data for calibration. So you need a separate set uh for your model uh training, testing, validation and calibration data. And those are the instructions. You define the nonconformity score as a disagreement between your inputs and the outputs. You then evaluate those S scores which are numbers on the calibration set. So you learn this quantile Q hat which is related to the error rate that you set at the beginning

**[20:40](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1240s)** of the process and with this Q hat you move from the calibration set to the uh to the prediction phase. So you can form prediction sets and this has the nice um property in the sense that the probability of a new unseen point belonging to the uh conformal set is related to the error level that you set at the beginning and you have mathematical guarantees about that and that's the key difference. I'm I'm sure I confused you a lot because it's a complex topic. So if you want to uh learn more about conformal prediction, you can uh listen to my talk from TW Pyon Germany 2025.

**[21:32](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1292s)** And wrapping up, trustworthiness is not just extra polish for your model. It's very important. And if you want to ship models um in production and have reliable operations, you have to quantify your uncertainty. It's very important and possibly also try to reason in a cost-sensitive perspective. And uh the thing is also that explanable AI and uncertainty quantification answer different questions for your model. So the first one um belongs to the uncertainty side. Conformal prediction for this case gives you intervals or sets and so the model can express the

**[22:20](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1340s)** ambiguity instead of just pretending to be certain and the other question goes in the direction of explanability. So sharp for this case helps you attributing prediction to the relevant physical drivers and also opens the door to the scientific interpretation. So what changes is that the output becomes something that you can inspect that you can challenge and it's also something that you can then adapt to the user context and that is why uncertainty quantification and explainable AI have to be part of the workflow or the workflow and not just a decoration at the end. And that's pretty much what I have for today. So I'm open for

**[23:09](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1389s)** questions. >> [applause] >> Thank you for your talk. Here are some questions. [snorts] You mentioned around 1,600 events over eight years. That seems like too little data to confidently predict an event within the next three hours. How did you solve this issue? >> Okay. Um I mean uh it's not too little. It's how the nature works because uh we have this kind of events with a fixed rate over time. So we can't really tell the sun, oh please try to produce more LSTDs. Um the thing is that uh of course we try to work with colleagues to

**[24:00](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1440s)** enlarge the data sets. Uh, of course it was not possible to go uh backwards in time because there were not enough instruments for ionospheric uh measurements. We had uh we tried to control the uh confidence of the model by looking at the prediction intervals in output. So when the model saw enough instances um as a specific sample it was providing uh estimates which were uh narrow enough. So in this case we were uh okay with the fact that the model was confident enough for sure when you deploy this kind of models to production you have to account for uh concept drift

**[24:50](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1490s)** coar shifts and so in that case you ship your model to production and monitor the um the performances and then take action if you have to take some actions. >> Next question. How do you encode the time series data to predict with the cut boost? How far do you look back also goes in line with the data points across time time questions? >> Yeah. Uh for sure uh uh gradient boosting framework cannot understand what time is. So you have to perform some feature engineering tricks to tell the model something about the time. So this was done in the form of moving averages, exponential moving averages. Uh also uh lagged features which we were

**[25:41](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1541s)** uh design uh deciding how um far back in time to go by looking at um uh correlations between features and the uh target of the model. So if I remember correctly uh we go back in time we take into account like uh no more than the previous six hours of data something like that. >> Next question. If I understood correctly you work on prediction of LSD. What happens next? How the correction of this effect is working? Are you sharing the results with generous companies? >> Uh that's a very nice question. Um I didn't mention that this was part of a European project um Horizon Europe

**[26:31](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1591s)** project and between the stakeholders involved in this project uh there was the um German federal police the Bundes polyai because they have instruments uh like the uh high frequency direction finding systems um which are affected by this kind of of events. So the first phase uh for this project was just building a model which can tell them in advance if something was going is going to happen or not. We are also working towards the integration uh into the European Space Agency uh monitoring room uh for for space weather. >> Next question. Do you know about some

**[27:19](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1639s)** work that is explaining the instability of the given forecast? I I'm not sure that I understood this this question explaining the stability. Um because I can understand what instability is but I'm not sure what do you mean by explaining the stability. know if you are in in this room maybe you can clarify >> maybe next uh the next you can >> next one can you imagine some of these methods to be used in a demand forecasting in explaining the models and their ether casual dependency on the future covers used >> yeah uh for sure you can uh use this

**[28:09](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1689s)** approaches in demand forecasting as well But as you correctly pointed out, it would be much better to also look at the integration of causal inference because the problem with this kind of models is that they are just learning uh correlation and not you are not sure that they are picking um causal um effects. So better to have both. Last one. I graduated in a similar topic and I had no chance but using MATLAB because it provide important functions. How comes you were able to use Python? Uh but it refers to to using M because I'm sorry for that you had to use MATLAB.

**[28:59](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1739s)** [laughter] Um I don't know to what kind of functions are you referring to? Who are you in this room? Possibly. Oh >> yeah. So I think was bit off topic. >> Um yeah um I have to be honest it was quite easy to to work in Python these days. I don't know when you graduated but it was definitely easy and a joy because you have the full ecosystem for for AI models that if you are curious we can discuss it also later. Okay, I think that uh we have already answered

**[29:48](https://www.youtube.com/watch?v=K7Hl3vXB5wA&t=1788s)** all. Okay. Uh thank you very much for the talk very much.
