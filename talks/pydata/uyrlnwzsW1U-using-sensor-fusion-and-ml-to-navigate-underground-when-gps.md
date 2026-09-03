---
id: uyrlnwzsW1U
title: "Using Sensor Fusion and ML to Navigate Underground When GPS Fails [PyCon DE & PyData 2026]"
slug: using-sensor-fusion-and-ml-to-navigate-underground-when-gps
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Étienne Tremblay"]
channel: "PyData"
duration_min: 28
published_at: 2026-08-04T22:21:11Z
video_id: uyrlnwzsW1U
url: https://www.youtube.com/watch?v=uyrlnwzsW1U
youtube_url: https://www.youtube.com/watch?v=uyrlnwzsW1U
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science"]
transcript: true
---

# Using Sensor Fusion and ML to Navigate Underground When GPS Fails [PyCon DE & PyData 2026]

**Étienne Tremblay**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=uyrlnwzsW1U) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Étienne Tremblay explain how to leverage sensor fusion and ML to maintain precise navigation in GPS-denied underground environments.

Speakers:
Étienne Tremblay

Description:
Underground navigation is challenging because GPS signals cannot penetrate subway tunnels, leaving smartphones to rely on imprecise cell tower mapping or Wi-Fi scanning with accuracy radii often exceeding one kilometer. To solve this, a system was developed that estimates location by fusing motion sensor data, train schedules, and sparse device locations. The core logic treats the problem as a sequence of events: by detecting when a train moves and stops, the system can count stations traveled from a known starting point.

The technical approach utilizes a two-stage machine learning pipeline. First, a Convolutional Neural Network (CNN) is trained on millions of unlabeled user trips using a pretext task to classify general motion modes (stationary, walking, or automotive) based on accelerometer and gyrometer data. Second, transfer learning is applied to a smaller, high-quality dataset of 300 manually annotated trips to refine a binary classifier that specifically identifies "moving metro" states. This model is converted to TensorFlow Lite and deployed on-device via Core ML for iOS and Android to ensure functionality during network outages.

A mixer module integrates the binary motion predictions with offline train schedules and any available high-accuracy device locations to resolve edge cases, such as trains stopping between platforms. The system achieves approximately 90% accuracy, with predictions typically within one station of the true location. To manage uncertainty, the user interface employs warning banners and asymmetric confidence intervals, acknowledging a bias toward late rather than early predictions. The entire training pipeline is managed using Vertex AI to handle complex dependency graphs and parallel testing.

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

*4,345 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=5s)** Thanks for the introduction. So, I'm Etienne. I work as a data scientist at Transit, and today I'll explain how a smartphone can estimate its location underground when the GPS stops working. So, first of all, what is Transit? It's an app for getting real-time information about public transit systems. For example, you can get real-time schedules, you can get service disruptions, and you can plan a trip. Out of curiosity, raise your hand if you've used Transit before. A few people. We're pretty new in Germany, but we're bigger in other places. We've been developing Transit since 2012. We have now over 100 employees. We have 8 million monthly users, and

**[0:55](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=55s)** we're live in 1,000 cities, 29 countries, and 15 cities in Germany, including Darmstadt. So, I encourage you to try it out. At the heart of Transit is the Go mode. Go is a step-by-step guide through your trip, and it's relying [snorts] on the user location to give you the most relevant information at any given time. So, when you're walking to your stop, you want to know which street to turn. That's the info that's shown. When you get to your stop, you want to know how long you have to wait, so it will give you the schedule for the next buses or trains. And then, once you're on board your vehicle, you want to know when to get out, so it will tell you how many stations or stops are remaining until

**[1:44](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=104s)** you need to get out, and it will give you a push notification in case you fell asleep. Now, this used to all fall apart when you were in a subway, because it relies so much on user location. And if you don't see the skies, the you can see the satellites, and GPS doesn't work in subways. But now it does. How is it possible? That's the subject of today's talk. So, to get an intuition on how it might work, let's do a thought experiment. Let's say you're kidnapped. You're in a subway, you're blindfolded, so you can't see the signs, and you can't hear the announcements. But luckily, you're a subway nerd. You know the stations by heart. You know where you got on, and you know which

**[2:33](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=153s)** direction the train is headed. So, the question is, would you be able to tell where you are? And I think so. You could probably feel when the the train starts to move, and then when it stops. And at that point, you know you've traveled one station. And you just repeat that process, and you count the number of stations, and you could always figure out at which station you're you are, or between which two stations you are. This is the intuition that made us that gave us hope that a problem like this could be solved. And in fact, it's pretty close to the the way that we actually solved the problem. So, which clues do we have in order to infer the location? The first one is locations from the device. So, the the smartphone's OS gives app locations that

**[3:23](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=203s)** are generally based on GPS. But when that's not available, it falls back to other strategies like Wi-Fi scanning, Bluetooth scanning, or based on network infrastructure. And that relies on mapping like cell tower addresses to locations, but this mapping changes over time, and the accuracy is never really good. Often times, we'll have an accuracy radius of over a kilometer, which is not really usable for what we want to do. Here you can see visually what it looks like. It's a trip in Paris where the train starts above ground and we get dense and frequent GPS locations, but eventually it goes underground and then the the locations get super sparse, far away, the updates are less frequent. So, usable, but not enough on its own.

**[4:14](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=254s)** The second clue is the train schedule. Because we're a public transit app, we're already used to ingesting these and they are saved on device in case the network goes down. And those can't really be relied on in absolute terms, but the time delta between the stations is respected. So, if it's supposed to take 3 minutes between stations, that's usually reliable. And the last clue is motion sensors. So, you might know that almost all smartphones now have at least an accelerometer and a gyrometer for angular acceleration. Those are used among other things to infer if the phone is in landscape or portrait orientation, but

**[5:04](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=304s)** there is much more than that that we can do with the accelerometer data. Just looking at it like that, it doesn't look like much, but feed it through an ML network and you can get useful labels out of it. So, like any machine learning project, we need a lot of data and this data set doesn't exist, so we had to collect it. The three inputs that I talked about need to be logged as well as some ground truth about where the user actually is. So, in order to do this, we developed a special screen on the development version of the app where you can enter, as you do your trip, whether you're walking, standing still, on a moving train, on a idle train, an escalator,

**[5:53](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=353s)** everything gets logged. And we want the data set to be diverse cuz we want the feature to work everywhere. So, we made sure that the data collection was done by different people in different cities with different types of devices. Um and an important thing to note about this data is that annotation is impossible after the fact. So, a human labeler couldn't look at the sensor data and say, "Oh, this is an elevator." Which is in contrast with a lot of typical machine learning tasks and it makes a lot of the typical uh data cleaning techniques not apply in this case. So, the data quality is even more important cuz we can't correct the labels. And if you ever find yourself in a situation like this, uh we have a few

**[6:42](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=402s)** takeaways that I hope you can be inspired from. First of all, we relied exclusively on trained employees to collect the data. We invested a lot of effort in the protocol cuz some situations can be a bit ambiguous and we want to make sure that different labelers give the same label for the same situation. Then, even though we can't fully check the labels, we can add some automated coherence checks. For example, it's impossible for someone to go straight from an elevator to a moving train. They probably need to walk a little bit in between, maybe stand still while they wait. So, with automated checks like that, we catch at least some labeling errors. And finally, when in doubt, we discard

**[7:30](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=450s)** the data. Sometimes the labeler will tell us, uh uh I fell asleep at this point. I wasn't paying attention and I was late on the label. And in that case, we prefer to get rid of the trip than to have bad data in the data set, which we couldn't fix later. With these methods, we managed to collect 300 trips, which is respectable, but really not enough to train a deep learning network. So, the other thing we did is leverage our millions of Go users, and those don't put any labels on their trip. So, we needed to rely on some heuristics to kind of have a approximate ground truth. The way that we did that is mostly based on GPS speed. So, this is a an

**[8:19](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=499s)** oversimplification, but basically, if the speed is really low, we assume that they're stationary, they're waiting for their vehicle. If they're walking within a certain range of speeds, well, they're they're probably walking, and if they're going faster than a certain threshold, they're probably automotive. And so, we have these three classes that are not actually what we want to predict, but it's a pretext uh task to get the model to learn useful representations of the sensor data. To get an idea of what the data look like, we passed it through a fast Fourier transform, and you can see it on the the frequency domain. Here at the beginning and the end of the trip, there's a clear peak at about 2 Hz, and you can probably guess what that

**[9:07](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=547s)** is. It's somebody walking making about two steps per second. In the end, using a fast Fourier transform as part of the processing the pre-processing is something we tried, but didn't yield good results. But at least for for a human, visually, it kind of helps to see if somebody might might be walking. Now, as in any machine learning task, one of the most important decisions we needed to take is how do we transform our problem into some kind of classification or regression. And the way that we ended up doing it is by saying uh we have a target variable where a value of one represents a moving train and a value of zero can be anything else. Can be walking, standing

**[9:55](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=595s)** still, an escalator. And if we can get a model to predict that, then all that's left to do is count those kinds of square waves. And we know how many stations have been traveled and we can infer the user location. And at the bottom you have an actual prediction from a train model. And the the waves are very visible. And you can note that at the end there is a smaller wave that's actually uh an escalator. And it turns out the vibrations from escalators are somewhat similar to moving trains, but we're able to tell them apart and let count them as a station. So, the training happens in two stages because as I explained we have two data sets.

**[10:42](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=642s)** The first big data sets from user is used to train a CNN convolutional neural network, which is typical for image classification, but it turns out it also works very well for our sensor data. This allows us to train a pretty deep network cuz we have millions of trips. And uh the we predict the mode as I explained, which is not exactly the label that we want, but it allows us to train this big network that can then be used in transfer learning where we freeze the weights and we keep training a smaller model that's based on intermediate activations from some layer in the middle of the pre-trained model. The the cut point is important. And we treat it as a hyperparameter. So,

**[11:30](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=690s)** we try different values, see what works best. And this has two advantages. First of all, it gives us these two outputs from a model that's not much bigger than the base model, which is good because as I'll explain later, we eventually put this on device. So, we want the model to be small. And the other advantage is we get way better performance than if we tried to get the moving metro prediction from the employee data alone, which is a very small data set. So, this gives us a binary prediction, moving metro or not, but what we actually want is a predicted location. So, how do we go from one to the other? The answer is a module we call the

**[12:19](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=739s)** mixer, and it brings together the motion type, moving train or not, the recent device locations, as well as the train schedule. And generally it just counts the square waves as I explained, but there's also some fancy logic that can happen. For example, in New York City, sometimes the train frequency is so high that a train will leave a station while there's still another train waiting at the next platform. So, they can't go all the way, they stop in between platforms, and that's a tough edge case for us to solve cuz when it stops between platforms, it looks like it stopped at at a station. And so, in order to figure out what happened, we look at the train schedule. If we expect the train to move for 5 minutes between stations and it moved

**[13:08](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=788s)** for 1 minute, we're sometimes able to recover from these situations. We can also recover from mistakes when the we get recent device location that has high accuracy, and it's different from our previous prediction, sometimes we're able to correct. And one thing that's cool to notice is that those three inputs all work offline. The device locations like we can still get them from Wi-Fi scanning or Bluetooth beacons. The subway schedule is already stored for offline use. And the motion detection relies on the model which is only 2 megabytes. So we were able to package it. It's relatively small compared to the rest of the app and all that allows us to keep uh running the model even

**[13:58](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=838s)** when the network fails which happens pretty often in subways depending on the city. Does it work? The The answer is it generally works but not always. As any project like that, there's a certain error rate. It works about 90% of the time where the prediction is less than one station away from the true location. And you can see it on this graph. So the x-axis is the true station index and the y-axis is the predictions. So in a perfect case we would follow the black diagonal line. Uh whenever the like each line here the colored lines are separate trips. So when they're below the diagonal it means the prediction was late. And when they're above it means it was early.

**[14:48](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=888s)** So you can see just from this that we are late more than we are early and also some sometimes the the prediction can recover when it comes back to the diagonal. So it makes mistakes and it doesn't stop us from deploying this for millions of people to use. The important thing is to somehow surface the uncertainty. We don't want people to get off the the subway when we tell them to at the wrong moment. So what the user experience looks like Before, you would have a location that jumps around infrequently. Maybe you'd get an update every few minutes. It's immediately obvious that the location was unreliable. Now, the location moves in real time, which can make it look

**[15:38](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=938s)** more reliable than it really is. So, it's important for us to send a message that it's an approximation. So, we have this big yellow banner at the top, which I personally don't like, but it's important to say don't necessarily get off when we tell you to. We also changed the notification text. It used to say get off in two stations or get off now. Now, it just says to pay attention to your surrounding, your stop is coming up. What's next? Um we we want to have the confidence interval be displayed to the user in a way that's less aggressive than a warning banner. We already have an estimate of it.

**[16:26](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=986s)** It's an asymmetric confidence interval in the sense that we generally think that we may be late more than early. And we want to show it in a way that's intuitive. So, we're thinking about this kind of visualization where you you have a a range displayed on the map, and you know exactly between which stations you may you may be. The other thing we want to add is broadcasting vehicle locations, which is something we already do for buses, and it's one of the most loved features of transit. Where if you're on board a vehicle that doesn't have a GPS transponder, it's not shown on the map for other users. But if you activate go and you ride that bus, you'll be broadcasting your location, and then other users can see it on the map, and

**[17:14](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1034s)** they can literally thank you in the app. Uh it's something that would be especially valuable for subways because in a lot of cities, there is just no real-time locations in subways. It would be something new, and it's difficult because we know that we have a system that's not as reliable as GPS. So, one approach would be to look at when different users' prediction agree and somehow merge those and surface them for other users. We are also thinking about adding other features as input to the to the moving metro model like the OS cuz we know that different phones will record sensor data in slightly different ways, or the city because the rolling stock has a big impact on the vibration

**[18:05](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1085s)** patterns that we're trying to detect. In terms of infrastructure, we've been using a GCP product called Vertex AI. Any Any system would work, but the important thing is that you have some kind of dependency graph encoded to to tell you what task depend on which task's output. And the reason it's important is some of these tasks take really long to run, several days, several weeks. And when you rerun them, you might not want to run the whole pipeline. You only run You only want to run the one that changed, but then all the downstream tasks also need to be updated. So, Vertex AI or Airflow or even just a makefile if it's a smaller project would

**[18:54](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1134s)** work, and it allows us to iterate much more quickly and not have to remember, okay, I updated task X, which ones need to be rerun also. It caches the step outputs, so they can be reused if the task doesn't need to rerun, and it allows us to run different pipelines in parallel, which is super useful to test out ideas. We can just run them both, see how the performance compares at the end. And the cost of a full run is below 50 euros, which is kind of refreshing compared to bigger model training pipelines. Thanks a lot. I hope you try it Transit, and when you see the vehicle location moves, you you'll know a bit what's

**[19:41](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1181s)** under the hood. >> [applause] >> Thank you very much. I for one really enjoyed this session, and I think I can say that, you know, many of us here too also enjoyed the session. Uh we've got a couple of questions here. The first one says, "Would it be possible to incorporate audio data, such as station announcements?" >> Mhm. It's a great question. It's something we've thought about. It would be so easy to just turn on the microphone, listen to the announcement, and uh yeah, but the the reason we don't do it is it takes permissions, which we don't currently ask for. Um like for a public transit app to ask microphone permission can seem weird. But yeah, it's definitely something

**[20:28](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1228s)** we've thought about, and I think it would work great. >> Thank you. And next one says, "Have you considered supplying the motion data to the rail companies to give them hints for their maintenance?" >> Uh interesting. We we haven't considered it. Um it's a good question. Maybe it would help preventive maintenance. What might make this difficult is the We've realized that the sensor data depends a lot on how the people hold their phones. If they're sitting down with it on their lap, or if it's in a bag, or in their backpack, makes a big difference to the vibration patterns. Um like it be used to tell if if some part is vibrating more? I'm really not sure, but it's a good question.

**[21:16](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1276s)** >> Okay. Are you combining the data from different users riding in the same train in order to increase reliability? >> Mhm. Uh good question. We currently don't. We We've done it from manually collected data. So, one subtle thing when collecting the data is that the annotation itself is done in real time and that has an impact on the sensor data because if you're if you're entering annotations, you're you have your phone out, it can't be in your pocket. And also, you might behave a bit differently. So, what we did is have two people ride the subway together, one of which is annotating and the other one is just minding their own business, and we apply the annotations to both of them. So, so that's that's a bit the same

**[22:06](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1326s)** idea, but it's done by employees and not anonymous users. >> Great. Do you have any idea why the model is late more often than early, and can you try to correct for that? >> Yes. Um the reason it's late is usually because it fails to detect departure from a station or arrival at a station, and then once we make a mistake, the mistake can carry over for a while until we get a device location to fix it. For it to be early, the the most typical reason is because we detected a station when when there wasn't one, and it's more rare. Uh but the good thing to note is that this bias is actually on purpose. We prefer to be late than early. Um

**[22:53](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1373s)** but the that's done with the the cost function. We We make a a late prediction cheaper than an early one. >> Okay. And how do you deal with a person jumping on the underground in the wrong direction when they have to change? >> Uh yeah, that's uh that's unhandled. It's a we make a lot of assumptions and one of them is the user will do the trip that they said they would do. If they go in the wrong direction, we're unable to detect it. If we eventually get a location, we we will update the prediction, but uh that that's a hard problem. We can't differentiate different directions yet. >> And what do you do with stops between the stations? >> Stops between stations,

**[23:41](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1421s)** uh I I explained it a bit, but it's it really relies on the the schedule to try and figure out if it might be a stop between stations. So, if if we stopped much uh faster than we were supposed to according to the schedule, we detect it as a stop between stations, and well, the the location just displays it as such. The vehicle location will stop moving between station and then resume once the train starts moving again. >> Okay. Have you noticed differences in the motion data after tracks were replaced? >> After tracks were replaced? >> Tracks. Tracks. >> Tracks were replaced. Uh good question. No, I I haven't, but there's definitely a lot of difference between systems, and

**[24:29](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1469s)** we're biased by the cities that we live in cuz it's cheaper for us to collect data there. So, in Montreal, it's rubber tires, so it works well in in other systems that have rubber tires, but uh yeah, the the biggest difference really comes from the rolling stock rather than the the rails from my experience. >> Okay. And coming from a control theory background, this seems like a good use case for common filters. Did you evaluate them and if yes, what is your experience? >> Mhm. Um yes. So, I I'm not super familiar with Kalman filters, but what I think one approach that we tried at the beginning that was similar is to try to basically take the acceleration and integrate it twice to

**[25:18](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1518s)** get [snorts] the the distance covered. And the issue with that is that we're unable to tell the orientation of the the user inside the terrain. So, to us a turn, like the acceleration from a turn looks the same as the acceleration from braking or accelerating. And we we weren't able to get reliable results from that even though it looks like a a simple and intuitive solution. >> Okay, this one says, I suggest the integral area under the curve over the acceleration graph could be a more precise measure of the distance traveled compared to just taking the time length between of the square. >> Uh yes, so I think that that's the the same suggestion. And I do think it sounds very intuitive. Maybe there's a

**[26:07](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1567s)** way to make it work, but from what we tried, uh it had a lot of issues. And also like a a bad property of this is that the the error is squared and integrated over time, so it can really diverge if there's any miscalibration of the accelerometer. >> Okay, and which library are you using to run the model inference on device? >> On device, so we [snorts] we have um it's separate for iOS and Android. And and we compile the model differently for both so that they can use the the device hardware. On iOS, it's Core ML. On Android, it's something else. I don't remember the name. But we we start from a TensorFlow Lite model that we then specialize for each platform.

**[26:55](https://www.youtube.com/watch?v=uyrlnwzsW1U&t=1615s)** >> Great. I'm going to have a final question that says, "How do you deal with people walking on the train?" >> Mhm. Uh yeah, that's a tough one, but surprisingly enough, we're able to differentiate from someone walking in the train from someone walking on a on a stable ground. And the reason it works is because we have a lot of that in the training data. We have a lot of people walking on moving trains, but it's labeled as a moving train and the model is able to predict moving train even when somebody's walking. We haven't many people that are dancing, though. That might not work. >> [laughter] >> Great. Thank you so much for this really insightful session. Please, could we give him a big round of applause, everyone? >> Thank you. >> Thank you very [applause] much. And enjoy the rest of the conference. >> Thanks.
