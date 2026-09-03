---
id: 9lExGn-JLFg
title: "Hierarchical Models in MMM: Can Structure beat data size? [PyCon DE & PyData 2026]"
slug: hierarchical-models-in-mmm-can-structure-beat-data-size
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Mohamed Amine Jebari"]
channel: "PyData"
duration_min: 25
published_at: 2026-08-04T22:20:38Z
video_id: 9lExGn-JLFg
url: https://www.youtube.com/watch?v=9lExGn-JLFg
youtube_url: https://www.youtube.com/watch?v=9lExGn-JLFg
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Enterprise adoption & strategy"]
transcript: true
---

# Hierarchical Models in MMM: Can Structure beat data size? [PyCon DE & PyData 2026]

**Mohamed Amine Jebari**

`PyData` · `PyData` · `2026` · `25 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=9lExGn-JLFg) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Mohamed Amine Jebari demonstrate how hierarchical modeling and partial pooling in PyMC can stabilize ROAS estimates and outperform raw data volume in Marketing Mix Modeling.

Speakers:
Mohamed Amine Jebari

Description:
Marketing Mix Modeling (MMM) often faces the challenge of insufficient data for specific regions, where the number of available data points is equal to or less than the number of coefficients required for prediction. This data scarcity leads to high uncertainty and unreliable coefficients, particularly in smaller markets. To address this, hierarchical Bayesian modeling is used to implement partial pooling, which allows models for data-poor regions to borrow statistical strength from data-rich regions.

The approach utilizes PyMC for probabilistic programming and the Hypothesis library for property-based testing of transformation functions. To reflect real-world consumer behavior, the model incorporates ad stock functions to account for the delayed effect of advertising and saturation functions (such as the Hill function) to model the plateauing of returns as spend increases. Testing ensures these functions remain bounded between zero and one to prevent unrealistic simulations.

Three modeling strategies are compared: pooled (all regions combined), unpooled (separate models per region), and hierarchical (partial pooling). While pooled models ignore regional variance and unpooled models fail in data-sparse regions, the hierarchical model uses a group mean and a deviation parameter to balance these extremes. To improve sampler efficiency and avoid restrictive distributions, a non-centered parameterization is applied.

Key takeaways include the importance of calibration and uncertainty intervals over simple metrics like RMSE or R-squared. Hierarchical models are most effective when regions share domain similarities, such as shared culture or audience demographics. However, they fail if regional behaviors are too divergent or if data is uniformly sparse across all groups.

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

*4,363 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=9lExGn-JLFg&t=6s)** Um, so yeah, today we're going to talk about the eternal struggle between data and uh models. Which one would win? Before we go deep into the topic, small introduction, that's me in the picture. I'm [snorts] from Tunisia and I've been in Germany for nine years. And yeah, I'm a data science lead at TD Reply. TD Reply is a consultancy firm. We worked for a lot of clients which takes me to my segue that these clients expect a lot. Um they might give you they might tell you that your data is good. They might tell you that they have everything ready but most of the time it is not. So that's why I tend to to say that data is expensive. Of course, you can put all

**[0:55](https://www.youtube.com/watch?v=9lExGn-JLFg&t=55s)** your data in S3 for almost no money, but the processes to get that data and to ask them to go get the data usually take weeks and um in tight time frames of consulting, it is usually not possible. So, what can we do about it? I'm going to talk about something called partial pooling. Maybe it's um known for some of you. I'll go into it a little bit. I'll talk about when it works, but also when it doesn't work. um a bit of basian modeling just to set the scene and uh I'm going to talk about testing in basian modeling and markix models because my boss told me to and uh yeah the two packages we use is going to be pime which is a package for probabilistic programming if you were at

**[1:42](https://www.youtube.com/watch?v=9lExGn-JLFg&t=102s)** 11 today in the talk with Juan he talked about it extensively and that little animal there is a library that's called hypothesis it's a Python library that allows you to test. Actually, it's called propertybased testing. When you have a property of a curve that you expect and make sure that that test will kind of challenge that property to make sure that your your function doesn't explode. Meet Volulta. Volta is a music distribution company. I chose music because I like music and I dream that one day I can like make music to distribute it to the world. Volulta is specialized in putting music on Spotify for different um musicians. In this case, we're going to take one musician. We call him Amin. And uh we're going to try to analyze

**[2:31](https://www.youtube.com/watch?v=9lExGn-JLFg&t=151s)** things like Meta, Spotify, Tik Tok, YouTube, radio, and playlist pitching. For this one, it's when you are a musician, you want your playlist to go into discover weekly for Spotify or in chill focus playlist when you want to work, and that song would appear there. So, these what we call marketing channels. This is how you would get exposure so that people will listen to you. What we're trying to explain is the revenue you get from the streams. So a lot of charts. Let's go slowly. So this is our time series of the revenue that that artist so far has made. As you see Germany and UK, we have quite some data. It's quite complete. You could make quite a good model out of it. But if you look at Sweden or Poland, you have only six data points and that is horrible. But the client or the musician or the distribution company they still

**[3:20](https://www.youtube.com/watch?v=9lExGn-JLFg&t=200s)** want to know how can they create an uplift in these specific countries. That is the first problem. Second point is that somehow the data collection of Tik Tok in Poland did not work. So we have no data there. Second problem. Third one is the data to parameter ratio problem. So when I started studying data science, they told me for each 10 rows you can pred get get one coefficient to predict. I don't know if it's a myth or true. I think there was some something related to like a normal distribution about it. But nevertheless, now we are in a worse position when we have six data points and we have six coefficients we need to predict which is also or sounds kind of unfeasible for Poland and Sweden. Last point is our spends are quite volatile. So there's a lot of outliers. You have

**[4:10](https://www.youtube.com/watch?v=9lExGn-JLFg&t=250s)** eight countries you not predict and you have one month to do it. So how to as I showed all these countries are quite different but they're also a little bit similar and this is when we start thinking a bit more about the problem. First all the eight countries I showed you they're all in Europe. That is great because Europe has quite at least the countries that I chose have a quite a similar weather has similar like um holidays to some extent has similar culture. We are also also in this case trying to explain the the streams of the same artist I mean and the audience usually people who like rock are quite a clear audience or like metal

**[4:58](https://www.youtube.com/watch?v=9lExGn-JLFg&t=298s)** in this case. So there's a lot of similarities and the most important assumption if you spend money you're going to get revenue to some extent. We'll see why later. So three models we want to try. First one is what probably the most pragmatic person will tell you. Sum everything together. Consider them as one data point. Run the model. Whatever you're going to get, it's good enough. Second one, eight countries make one model per country. That will probably work for Germany and UK because we have 100 data point 104 data points. But for Poland, making a model with six data points, not sure if it would work. Third one is what I'm going to show you, which is kind of a middle ground solution. Use

**[5:48](https://www.youtube.com/watch?v=9lExGn-JLFg&t=348s)** the knowledge that you have from Germany and these countries. try to give parts of it to Poland and Sweden and all the missing countries and try to end up with a nice middle ground. So this is the equation for um just a regression model. So what we're trying to predict Y which is the revenue per country at a certain time. You have alpha which is how much revenue the streams would have made if we don't advertise at all. And then the sum of the different coefficients in this case we have six. We say this meta, Tik Tok, Spotify, etc. how much we spend on them and some error rate. And this is the where the caveat starts. Yes, if you spend you get revenue, but at some point it's going to plateau at some point. Think about it. I want to be famous in

**[6:37](https://www.youtube.com/watch?v=9lExGn-JLFg&t=397s)** Sweden. There's 50 other people who want to be famous in Sweden. How do we share that piece of cake? Am I going to be extreme? I'm going to reach everyone. But at some point I would have reached all my audience and that would have stopped. Second point is that the ads in themselves they don't impact you directly. And to be honest this is my favorite part of my job and what we do it feels like a bit of sociology psychology. If I listen to a radio today I might hum the song one week later I will know the lyrics. By a month it will probably be my favorite song. And that's what this function kind of shows you. I'll go in it very deep, but if you want more very fast, but if you want to go deeper, talk to me later because I have only 20 minutes left. So ad stocks, as I said, 100% of your spends will not

**[7:27](https://www.youtube.com/watch?v=9lExGn-JLFg&t=447s)** affect me 100% today. They will affect me over time. I buy radio for three months. So once that spot of, hey, listen to on the radio for the next three months, it's going to be spent once. But the effect is going to go slowly slowly until it sticks in people's mind. This is what we define as adstock in this case and we need to include it in our model if we need to really explain reality not explain like a a point in time. Second thing are the saturations. So saturations are like I said doubling your spend doesn't mean you're going to get double the streams just because you would have reached already everyone at some point and any money you're going to spend more if someone doesn't like metal today they're not going to like it tomorrow even if you spend money about that song and the testing part I'm trying to

**[8:17](https://www.youtube.com/watch?v=9lExGn-JLFg&t=497s)** finish it fast so that I can tell my boss I did it testing so actually I'm it's not true I love software engineering and testing okay So testing this is exactly what I showed you here but 50 times. So hypothesis is kind of a library where you give it the state giving that amount K. So K in this case is when the spends would reach 50% of their effect. Giving that K is between 0.05 and five. S is the steepness of the curve. How fast do you want it to go up or to um flatten at the end? Giving K and S. Now do N examples. In this case is I chose I think 50 examples and the deadline is none. Deadline is none means if you fail or if you find an error when you go past the boundaries of zero and one I will explain why it's

**[9:06](https://www.youtube.com/watch?v=9lExGn-JLFg&t=546s)** dangerous then stop. But in our case we said deadline is none. So even if you find errors you have to keep going and then we call our hill saturation function. So why do we need to test saturations basically? Because most of the time at the end of the projects clients come and tell us it's a good model. Now can you simulate what would happen if I change my spends to some extent? If at some point my the total spends or their effect go past one, it's quite unrealistic because the whole effect and information should always stay between zero and one because this is the maximum spends that the person did. So if it goes past one, it's kind of like unrealistic. So this is the function we're going to use when we're going to simulate. So when we do a simulation and that function is wrong, we're going to tell to the client, yes,

**[9:53](https://www.youtube.com/watch?v=9lExGn-JLFg&t=593s)** you're going to increase your streams by 50%. While in reality, they could have only increased their streams by 20%. They would have lost quite some money for no reason. We do this usually for a lot of the other transformation functions like adstock and other functions. Now back to the modeling. So we saw the transformations, we saw the different channels we want to predict or understand and we do our first model. So basian modeling is I don't know if I would call it counterintuitive but we're not used to it because we're used to the usual frequentist approach. You can think about it as instead of letting it find the betas we can we tell to the model the betas are most likely in a normal distribution between zero and one and this is my data. Now

**[10:41](https://www.youtube.com/watch?v=9lExGn-JLFg&t=641s)** 4,000 times choose one point in that distribution compare it and see if it works with the data. If it's good, then stay in that area and keep discovering. If it's not good, go to another area and try to discover. But you have to stay into that zero and one. This is basically what Beijian or what we're going to see here in a nutshell is the first model. If you look at it like this, it's not too bad. Green is the real coefficients because this is synthetic data. So I know what the beta is supposed to be. So we actually caught five out of the six. This one was a complete fail. Uh but personally this one and this one and this one are also fail because what you see the two blue bars are what we call like the

**[11:28](https://www.youtube.com/watch?v=9lExGn-JLFg&t=688s)** uncertainty. The longer these bars, the worse it is. The shorter the bars, the better it is. The worst thing that you can have is something like this. The playlist effect is most likely at 0.2, two but it can be minus one or it can be one. If you go and tell someone this they will tell you I can do nothing about this. Is it negative negatively impacting me or positively impacting me? And that's quite a problem for us. So we can do nothing basically with this model. The main reason is that that coefficient worked well because all these values here are quite close to each other. So even when you summed everything together, we didn't really lose so much information. it was quite okay. Nevertheless, something like this one, the space between all the countries

**[12:17](https://www.youtube.com/watch?v=9lExGn-JLFg&t=737s)** is quite different or the real value of all the countries is really different and that's why the model doesn't know what to do. So we go to the next model. Next model we try to predict to explain every country by itself. Germany was I think okay for example if we take Spotify what is the effect of Spotify? It's between 0.5 and three still too wide for me if you want to be show my opinion. But Sweden and Poland and Italy and all these that have so less weeks of data. It was again a complete failure. And if you look at Poland who has six data points, I would not expect anything to be honest. The width of the certainty is very large. That mean that the model doesn't know So

**[13:10](https://www.youtube.com/watch?v=9lExGn-JLFg&t=790s)** what we want to do now all the points that I showed you they exist in the space of okay how effective is the channel these are the countries we're going to try to pull pull and pull all the countries partially together and get them closer to the average. Why? Because like I said in the start they're all European countries. There's a lot of similarities. So we assume that the effect might be similar. Whatever you're going to do on Spotify in Germany, yes, it probably might work in Poland to a certain difference. So, we cannot take what Germany did. So, let's try to assume that and try to include it in our calculation. So, what we're going to end up extracting at the end is the mu of K which is a group mean. So, the group itself has an average. We want to find that. That would be interesting to know

**[13:58](https://www.youtube.com/watch?v=9lExGn-JLFg&t=838s)** what is the average of all these countries together. then how much each how much the countries deviate from themselves. The bigger this, the worse your model is going to be. And this will prove to you that you shouldn't use this method. So this should be usually quite low. Zed is for each country how much it deviates for the the center of the channels and beta is the coefficient of that specific country that you want to get. It's kind of a compromise to some extent. So we started like this. the width. I want to focus on the numbers up there. They're quite interesting. So, Poland, we start with a width of 1.8. It was not bad, but we were failing to catch meta here. Some of them were negative. Then we did the next model when the width increased a lot. So, a lot of uncertainties now in the model, unusable. And then we end up with a

**[14:46](https://www.youtube.com/watch?v=9lExGn-JLFg&t=886s)** third model. Still some problems, but we, as you see, we're getting very close to that green dot. Optimally, this should be next to the green dot. Now, some of them are still the negative. the width has decreased on average. So, we're back to 1.8. And this is due to the fact that I created a terrible data set where there's like a lot of multiolinearity. I want really to keep it as close to reality as possible. Usually, you cannot do a good model with only six features. You usually need more. You need the competitor. You need seasonality. I didn't include any of these things. So, that's why we are not optimal and it will not be optimal, but it's a showcase. So to give you more detail here as you see Germany we're very close to reality uh France not so much sorry [clears throat] um SW Poland we are actually quite close

**[15:35](https://www.youtube.com/watch?v=9lExGn-JLFg&t=935s)** to reality so I think the models improved a lot compared to unpoolled so unpulled as a reminder is each model is per country one model per country versus this one is the blue is like this what we the concession we did I had to put code because it's pyon So this is a pulled model summarizing everything together in one equation. So like I told you we are assuming that we want to find beta whatever coefficient it is and we assume that it should be in a normal distribution between zero and one and try to find it for all the channels. This is what this syntax is. Usually the models are way bigger but I wanted to just focus on what I change. unpooled here. Beta should be in a normal distribution should might have an average should be centered in zero and

**[16:24](https://www.youtube.com/watch?v=9lExGn-JLFg&t=984s)** can deviate up to one time and please do it per channel and per country. So they're completely independent. Then the partial pooling when we say we have a beta of everyone this time we start with a beta for all the countries together and it should be in this zone. We try to keep it small because we want to actually find the different. We would we put it also in 0.5 to let it deviate and stay quite positive. That's also another discussion that there's an assumption of positivity about the spends. Sigma is how much the the countries can deviate from each other. And then the last beta which is of the specific country should be in a normal distribution but it should be close to the center or close to the average of all the countries and should deviate this much.

**[17:13](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1033s)** This works but creates huge problems for our sample which is what is going to go find and find the solutions because it's very restricted. Let's say the model decided that beta is 0.5 and that beta sigma is 0.03. The freedom of beta to try and explore of the sampler to try and and explore the coefficients of the account will be very small because I have to stay in 0.5 and move very little this 0.03. So we come there is a solution for that. It's called a non-entered parameterization. We start the same. This doesn't change. Yeah, still the two things. So we have normal half normal but we add this offset. So the offset is another feature we add that gives more space for the sampler to go discover further. Small

**[18:03](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1083s)** tweak but fixes your model. Now this chart is actually pretty cool because it tells you how much each each country took from the average. And I think I'm not going to lie to you. I didn't do this at work before, but I think I'm going to start using it every time because it shows you that Germany or the countries that have a lot of data points, they did not really take a lot from the average because they're confident about their numbers. I know what I am. I am 100 for points. You don't need to help me. I mean, in some case, I needed help. Again, some of these numbers are messed up because of the multicolinearity. But if you go to Poland or Sweden, on average, these two rows are like 50% because they actually don't have so much information. They have just six points and they need help from everyone else.

**[18:53](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1133s)** How did we improve these models? So pulled reminder everyone together one model it had a high RMSSE but it was quite calibrated and this is due to the fact that Germany did the most of the lifting and do the work like the country the the countries that had a lot of data unpooled we improved again because the big countries did most of the work so if you average the model of all the countries it's going to be fine but the uncertainty gets very high and our solution solution is kind of a nice middle ground. We're still very close to the ampulled model and the certainty improved a lot that is the actical modeling. When does it doesn't work. So first imagine we have eight countries eight

**[19:42](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1182s)** data point per country for all the countries then there is nothing you can do. the the prior that you chose that normal distribution we talked about going to take over the model and it's not really going to be a representative model for reality. Second thing I mean wants to go on tour in Poland as soon as possible. So it will there will be a weird peak in that country or maybe it did already a big tour in Germany. So that's going to create a very different effects regarding the time and the models will be worse. So you have to add what we call time varing coefficients. So every country will have its specificity in the events in time that happen and probably the worst one is choosing the pooling in a wrong way. Um an example here is like I assumed I

**[20:30](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1230s)** recreated my data but I assumed that Tik Tok is uh Tik Tok is very used in Sweden, Italy and Spain and not used at all in Germany, France and UK. In this case it's Europe you assume. So we put them together but there is a very big difference because Tik Tok has almost zero effect here and here it's almost one. You cannot put them together in one model. The model is not going to be able to reconcile this. So instead you will then create one model for these three countries because they're similar in their behavior and a model for the three countries. For me that just says that a lot of what we do especially in basian modeling really has to do with like understanding a lot the domain what is happening in that country spending a lot of time doing analysis before modeling learnings test your transforms very important because if you simulate wrong

**[21:19](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1279s)** data it's going to cost you a lot of money second calibration is calibration and certainty matter not only RMSSE because as you saw my RMSSE was not great but my calibration is improving over time. If you add four other features for seasonality, for competitor price of Spotify, maybe some kind of things, then your MSE will probably improve a lot. But always look at the calibration at the certainty and synthetic data helps. It helped me really tweak change. I discovered the shrinkage chart by creating the synthetic data and seeing how good my model was improving. And uh that's it. Thank you very much. [applause] Yeah, thank you uh Mohammad for your

**[22:09](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1329s)** talk. Um yeah um one question is how did you perform validation using hierarchal modeling >> uh test train split the same? Is this the question like how do we validate >> like the validation set? >> Yeah the validation set. So yeah, you have to take if you have in this case probably Poland and Sweden, you probably cannot validate it. That is a good point. But for things like you can at least validate Germany and validate the countries where you have more data and that could probably allow you for to get a signal if your model is doing great or not. >> Uh what all metrics you use for your evaluation? >> So in this case I showed RMSSE. To be honest, this is a very interesting topic because we internally try to avoid to use R square. It's quite good to know

**[22:59](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1379s)** about it, but it's just too good to be true most of the time. And uh clients love it. So we tell them that, but but we also try to tell them, but we also try to include your domain knowledge and the model is well calibrated. end. So um at least when in my experience when I use Bayian I usually tend to have three or four different ways to validate what uh what we are shown to the client instead of just R square is great good luck. >> Uh will this approach also work for data outside of Europe like can this be extended to all the countries? >> Yeah the example of Europe was just because I thought of where which place has some similarity. Uh yesterday we were talking about the topic. I was talking about we could do it also for

**[23:46](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1426s)** North Africa. You could also do it for like people who like pizza. You can put them together and make something. It just you just need to before writing your model. Can I have enough similarities? And that's why I spend so much time showing you all the charts and slides because you have to really see the similarities and do extensive data analysis and what we call artisal code and the old data science work to really make sure that what you're doing is actually good or not before doing the model. Probably the model for us it's 20% of the project and 40 to 50% is a back and forth data analysis, assumption collection, talking to the client. So yeah. All right, that's it. So, thank you speaker for a wonderful talk and let's end this with a big round of applause. Thank you very much.

**[24:35](https://www.youtube.com/watch?v=9lExGn-JLFg&t=1475s)** >> [applause]
