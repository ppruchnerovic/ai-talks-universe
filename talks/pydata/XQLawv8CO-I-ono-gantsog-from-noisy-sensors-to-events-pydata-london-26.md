---
id: XQLawv8CO-I
title: "Ono Gantsog - From Noisy Sensors to Events | Pydata London 26"
slug: ono-gantsog-from-noisy-sensors-to-events-pydata-london-26
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Ono Gantsog"]
channel: "PyData"
duration_min: 29
published_at: 2026-06-15T15:54:08Z
video_id: XQLawv8CO-I
url: https://www.youtube.com/watch?v=XQLawv8CO-I
youtube_url: https://www.youtube.com/watch?v=XQLawv8CO-I
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Evals, observability & reliability"]
transcript: true
---

# Ono Gantsog - From Noisy Sensors to Events | Pydata London 26

**Ono Gantsog**

`PyData` · `PyData` · `2026` · `29 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=XQLawv8CO-I) · [Conference site](https://pydata.org/)

## Description

Ono Gantsog- From Noisy Sensors to Events: Event Detection in Sensor data with Kalman Filters and Hidden Markov Models

Sensors operating in complex environments produce noisy data. Determining exactly when a system transitions between states — and what values it is recording — is surprisingly hard: vibrations, environmental changes, and gradual shifts all conspire against simple threshold approaches. This talk walks through a real-world Python pipeline that solves this problem, starting with classical signal processing, exposing its failure modes, and then building a principled solution using a Kalman filter for noise reduction coupled with a Hidden Markov Model (HMM) for state inference. Attendees will leave understanding how to frame sensor problems as state estimation tasks and how to apply these techniques in Python using necessary libraries.

Objective
Many operations depend on accurate data from continuous sensor streams. Knowing when a system transitions between states, when a process cycle completes, and how much change occurred per cycle drives scheduling, monitoring, and operational reporting. This talk presents a complete data science pipeline — built entirely in Python — that automates event detection and value estimation from noisy sensor streams. The goal is to give attendees both a worked real-world case study and a transferable toolkit for tackling noisy, event-driven sensor data in any domain.

The Problem
Sensors record measurements continuously, but the raw signal is far from clean. Vibrations, speed changes, and environmental shifts all create noise that masks the true underlying state of the system (for example: wake, light sleep, deep sleep, REM sleep). A naive threshold-based approach — the initial "traditional method" — is brittle: it misfires on transient spikes, misses gradual transitions, and cannot estimate values reliably. This section sets up the problem visually with annotated sensor traces and shows concretely where simple methods break down.

Why Kalman Filter + Hidden Markov Model?
The key insight is that the system operates as a latent state machine: at any moment it is in one of a small number of discrete states (idle, transitioning, active, completing), and what we observe is a noisy function of that state. This framing motivates a two-stage approach: Kalman Filter — smooths the raw signal, handles sensor noise, and provides a principled estimate of the true instantaneous value with an associated uncertainty. Hidden Markov Model — takes the smoothed signal and infers the sequence of hidden states, including the timing of transitions and the most probable value estimate at peak. The talk explains the intuition behind both models without heavy mathematics, and then shows how to implement them in Python with filterpy (Kalman) and hmmlearn (HMM).

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*3,405 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=XQLawv8CO-I&t=5s)** Thank you. Um last uh February when I was sending my submission of the talk, it was easy just some abstract and then hit submit. I never thought the possibility of accept the talk would be accepted and then I was like okay I need to get the visa now and then I need to travel to London etc. It was all exciting and the visa was declined once. So I was like, okay, should I reapply again or should I just leave it, not come here at all? But here I am. And signal processing is something I'm I got very excited after coming back to Mongolia from US. And then my full-time job is a data

**[0:54](https://www.youtube.com/watch?v=XQLawv8CO-I&t=54s)** scientist at a international mining company. It's a subsidiary of Riotinto and since joining Riotinto subsidiary in Mongolia um I start started working on sensor data and then I started getting excited about it. So that's how I uh submitted my talk from noisy sensor data to detecting events and uh without deep learning models or neural networks I tried I tried to get a robust event detection with common filters and hidden marker models. So let's start with uh

**[1:43](https://www.youtube.com/watch?v=XQLawv8CO-I&t=103s)** so first of all when I was doing uh masters in the US uh mostly they teach about this uh table data and uh data analysts they mostly work on table data like future engineering etc but sensor data is something very different like you have to rely on timestamps and you have to format them a lot and sometimes you make some mistakes uh on the timestamps that mess up whole values in there. So this is one of the very simple time series data as you see like uh at the bottom part uh when it's stable kind of exh stable sensor is sending all those noisy

**[2:34](https://www.youtube.com/watch?v=XQLawv8CO-I&t=154s)** data and then when it's going up or when it's going down it's very quick in a matter of a few seconds but it's happening like so if you look at the nature of the data like when it's oscillating or fluctuation fluctuating like that, how would you uh detect an event? Like when you see it with your eyes, it's easy to see it's going up or it's easy to see when it's going down. So when you uh visualize the raw data, it's very easy. But the solution we are trying to uh the solution we are trying to get is without looking at the data uh we have to come up with an algorithm that

**[3:23](https://www.youtube.com/watch?v=XQLawv8CO-I&t=203s)** detects the event so that some kind of uh very easy to understand um fact table is going into the database. So why time series data is very difficult? Although this previous one was one of the very simple sensor data like usually they are very messy like always fluctuating sometimes they are just out of range uh below than zero or uh uh out of normal range of values. So in real life especially sensors they throw you off a lot like there is a data shift sometimes there is no signal at all although the event is happening

**[4:13](https://www.youtube.com/watch?v=XQLawv8CO-I&t=253s)** meanwhile sensor is off and then you have to think all those things and also sensors goes off the calibration so you have to see detect those uh out of calibration events too. So this is also one of the messy uh noisy data which is EEG electrons in a hologram. Um this is where I got very interested in this data and then trying to figure out how to process this one also which uh is actually I got to uh interested in neuroch startup with because of the signal processing. So going back to this very simple

**[5:02](https://www.youtube.com/watch?v=XQLawv8CO-I&t=302s)** uh sensor data. So this is actually a uh sample um data from weightter sensor. So uh when it's around 75k uh the truck has no load. It's just traveling from point A to point B. And then when it's loading it's getting payload. And then with the payload it's going from point B to point A back and then it's uh fluctuating again and then it's unloading the payload. You see uh unloading happening in the second part in here. Um so going back uh when I got the the task that I need to process this data at

**[5:56](https://www.youtube.com/watch?v=XQLawv8CO-I&t=356s)** I started with the data distribution and if you look at the data distribution it's very easy that around uh 80k the truck is empty around 150k it's uh in the middle of loading uh phase and around 225k it's fully loaded but you don't know exactly which one is the accurate or correct actual payload of the sensor. So uh um the other business end units are just assuming that 220k is the final uh payload of the uh final tonnage of the payload. That's what we have to assume actual load. But if you look at the uh real

**[6:46](https://www.youtube.com/watch?v=XQLawv8CO-I&t=406s)** payload it could be different. So at first I started with manual processing and from this uh data distribution well you are already guessed it I guess the first part around 800k is empty state and middle part is about loading uh or half loaded state and then the final part around 220k is fully loaded part. So that's uh in the manual processing that's where I defined the states empty half and loaded and uh also I defined the cycle from point A to point B loading activity and then from point A back to point from

**[7:38](https://www.youtube.com/watch?v=XQLawv8CO-I&t=458s)** point B to uh back to point A it's one cycle going fully uh one full cycle. So it's from empty half loaded or from half uh from loaded to empty. So we have to count each cycle and with each cycle we have to determine the actual tonnage of the truck. So this was my manual uh proc uh manual uh processing part sorting by the date time and like I said before uh removing duplicate uh rows because sensors give you the same time stamps two different values. So you have to determine which one is

**[8:28](https://www.youtube.com/watch?v=XQLawv8CO-I&t=508s)** the correct value or which one uh you need to remove automatically from the data. So removing duplicate row was also uh also a challenge like do you want to remove the first row or do you want to remove the last row. So that's uh that's kind of like you have to discuss it with the business end users like which one do you accept if the the time stamps are uh same and also you we need to remove those uh unlikely outlier values like if the sensor is detecting less than zero value which is which shouldn't happen because it's weightter data and uh when the maximum payload is 250 50k. If

**[9:17](https://www.youtube.com/watch?v=XQLawv8CO-I&t=557s)** sensor is detecting more than 250k sometimes around 500k then do would you accepted or not? Um so uh coming back to the algorithm at first I assigned uh ids to the day times and then I assigned states to the rows and then I try to remove weight uh weight noise and then uh the cycle determining part is coming up. So if the rows have same state um at first um I flagged rows that have changed the state. So one row is empty. It's going on with empty empty. And then

**[10:06](https://www.youtube.com/watch?v=XQLawv8CO-I&t=606s)** when the payload is coming up uh when it reach to the thresh of half loaded it's ch uh state is changing to uh half loaded. So that's where you flag the state changing is happening. Then find average weight for that state because for empty you have many rows. You just average it out and then add uh those uh use those columns to define uh the cycle. But oh and also with this algorithm we got uh this kind of flow from sensor system. At first you uh log all the data raw data into a database and then uh with my

**[10:57](https://www.youtube.com/watch?v=XQLawv8CO-I&t=657s)** algorithm first step is removing noise and then second step is state definition uh also cycle definition put it uh uh store it back into the database and then dashboard like how many cycles the truck did uh for the day or how many payloads was carried. for the day. So the that kind of dashboard was built from this automated processing. But you see here um all this uh processing was actually only just two big steps. One is noise removal and then the other one is state definition. And also with the dashboards actually business users complain that my numbers

**[11:48](https://www.youtube.com/watch?v=XQLawv8CO-I&t=708s)** are not my algorithm numbers are different than the actual numbers like they said roughly 10% change is detected so I have to change it or they have to accept that it's weightter actual uh tonnage so I started I started digging That's where I figured out common filter is uh something used for noise removal. So there are uh at least there were I found four different noise removal techniques. The very easy one we were taught at school is moving average. like consecutive 10 numbers are averaged to

**[12:37](https://www.youtube.com/watch?v=XQLawv8CO-I&t=757s)** find the total tonage or like you can play with that numbers number when you're calculating moving average like five consecutive numbers or 10 consecutive it doesn't matter it's just moving average and there were two other methods like seitki or something like that but uh with uh sensor data common filter worked best. The very simple idea about the common filter is at first it's just predicting one number and then when the next number comes up common filter is actually uh fixing its own common gain parameter and then applying it uh to the next estimate.

**[13:26](https://www.youtube.com/watch?v=XQLawv8CO-I&t=806s)** So if you look at the predict and update part, you will see that it's always um it's always predicting next state, updating its parameters and then predicting the next state. So uh this one works very well with the continuous data. So continuous data means it perfectly works well with that weightter sensor data. Um uh so it's about that common filter thing. First of all um prediction filter predicts next state of the system based on the previous state and then the updating part is uh actual uh sensor uh measurement is used uh for me changing

**[14:20](https://www.youtube.com/watch?v=XQLawv8CO-I&t=860s)** the parameter and then it corrects its filter. So if you refer back to the image you see that it's almost like linear regression correction is happening there. So uh I visualized how common filter is working with the moving average. If you look at the moving average the average of the that fluctuation part even though it's a little bit less than the actual fluctuation there is still some fluctuation going on with the moving average like it did not matter how much I move uh increase the number 10 20 or something it there was always some kind of fluctuation what but with the common filter it was much more smoother than

**[15:11](https://www.youtube.com/watch?v=XQLawv8CO-I&t=911s)** the actual um numbers. So, and also if you uh notice the yellow lines here, it's actually predict uh estimating very well when the sensor is not available, sensor data is not available. So when sensor is out so like with the next uh value from the uh sensor it's actually predicting very well the values should have been when if the sensor was on. So there this is comparison with between common filter and moving average. Um so uh I think you have seen from here uh the benefits of the common filter.

**[16:04](https://www.youtube.com/watch?v=XQLawv8CO-I&t=964s)** First of all it's accuracy because it's always um updating the parameters. uh accuracy is very good and adaptability as you uh as we have shown in the in this image uh when there is no sensor value it's uh trying to predict the uh value when it's off and then efficiency or efficiency is very nice thing because when you have real data and then uh when the sensor is logging like every uh every second then it should calculate the next one quickly and then have to log into or use the value for the next

**[16:52](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1012s)** um for the next estimation. So this is part of the code just uh to show it here. The first part is common filter class. It's just the initiation in the in instance creation. You see that process variance, measurement variance, estimate and error covariance. Four parameters are initiated and then predict is just uh returning estimate but it's also updating error covariance common gain and then estimating uh updating its estimate again. So the real

**[17:41](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1061s)** job is happening in that update part common gain common gain parameter is getting updated with each error co-variance uh is updated. So common gain is where um common filter is saying that okay we are accepting this estimate or we are not accepting this estimate or how how what percentage of the actual value or what percentage of the estimate we are using it. So this is what I uh used for the common um this is what uh I used for the weight uh here weight uh that the real actual weight of the sensor.

**[18:34](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1114s)** So if we refer back to this law the second step was state definition. So state definition is trying to figure out if the paid loss. It's uh if the step is loading or unloading that's where hidden marco model is coming up. Hidden marker model I think you have all heard of markoff chain. It's like states you transition from one state to the next state. it's derived from that hidden marco model is actually a model that represents hidden states. So um in the hidden marker model we have

**[19:25](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1165s)** states obviously and observations on those states and then transition probabilities and emission probabilities. But if you look at this picture it will make more sense. Um so uh by hidden state what do we mean is we can't uh always see the state of the system but we see the observations for example in this case uh the example is we can't see the weather because we are at home maybe we can't see outside but we see uh people are carrying umbrellas that's the observation so if someone is carrying umbrella umbrella we assume that it's raining. So we also take our umbrella. That's the

**[20:14](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1214s)** very um uh very natural intuition of this hidden marker model. But also states should uh should be transitioning from one to another with certain probabilities like if it's raining today what's the probability of raining tomorrow or if it's uh sunny today what's the probability of raining uh tomorrow. So what's the advantages of hidden marker model for event detection in sensor data? It's it works very well with the sequential data handling and then state estimation hidden marker model uh estim uh estimates hidden state of the system

**[21:03](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1263s)** based on the observed data and then probabilistic nature of the model and then uh flexibility it's like uh it can work on different v u different types of sensor data. But let me quickly uh move forward and then show this visualization. This is a slip stage uh slip stage visualization. Like if you uh see the image uh when we are sleeping at first en RAM stage is happening and then REM stage is happening. when we are sleeping of course we don't know which stage our uh

**[21:52](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1312s)** brain is so that's where hidden state is really mentioning but observation in this cases for example those EEG sensors when it's put on our head it measures all those electric activities in our head so that's uh our observation is happening so each time some kind of wave is uh measured by the EEG G we can say that okay N RAM is happening now or REM is happening now. So this uh two images actually very um real data of the uh sleep stages. So you see from wake to n1 n2 n3 and then rem stages. So this is uh one of the case where hidden marker

**[22:46](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1366s)** model works very well too. So let me go back. So uh these are the advantages of hidden marker model. It works very well with the sequential data handling uh which is sensor data is all about transitioning from one system to another uh one state to another state. So uh with our simple uh example it's just loaded or unloaded state it's happening from one of the state to next state do which is uh which works well with the hidden marker model and also uh unlike the common filter you have to train first the model.

**[23:36](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1416s)** uh training is easy. It's just using a class and then using your original data and then using uh predicting the next one is just using that model which is the easy part. So with uh our simple example uh this is what um state uh the state prediction is visualized like this. So zero uh with the blue it's actually loaded state and then one is actually unloaded state. And if you see the image uh the fir up im um top images with the very cleaned smoothed out data sensor data. The

**[24:27](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1467s)** bottom uh image is raw data and uh actually you can see that when it's going very high like much about the 100k the loading uh state is triggered and then when it's going down uh actually unloading is happening it's uh detecting unloading event very earlier early than around like 160k. So this is how it's visualized when the code um algorithm was working. And uh before I said event detection or activity recognition works very well with the hidden uh marker model and also

**[25:16](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1516s)** I saw that failure prediction and situational awareness those cases are also very good at uh good with hidden marker models. So it seems like common filter and hidden marker models are very similar um algorithms or models like both of them is working the next state or next value of the uh sensor data. So what's the different uh what's the difference between them? difference is uh common filter works uh on continuous value but hidden marker model works on discrete value and examples I have already uh mentioned like common filter is

**[26:05](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1565s)** weightter position or velocity those types of uh value works what with the common filter on the other side hidden marker model works with the discrete stages like the uh like that sleep stage and then uh with the common filter uh the noise is almost uh defined by Gaussian noise um and uh in the hidden marker models residue is just the observation and uh for the common filter we don't need pre-training but uh hidden marker model we need a small training on the historical data.

**[26:54](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1614s)** So this is the result comparing to the manual processing of the sensor data and then comparing it uh with new algorithm I mean uh what I mean is common filter with the hidden marker model. So uh the tonnage difference with the new model uh new algorithm is around zero median is the zero and then uh the old algorithm uh if you see the box plot uh median is higher than zero and then uh it's going way up to 4k and in terms of percentage wise like how closely uh the new algorithm is detecting the actual value. It's

**[27:44](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1664s)** actually uh new one is 100% around 100% it's detecting the actual value but the old manual processing is like median is something around 20% different. So actually when business users told me that there is 10% difference they were not telling me the truth. It was actually 20% difference. So that's uh what I saw when I compared two algorithms and I have showed this earlier. Um this uh both of them common filter and hidden marker model is very general uh general algorithms to be can that can be used

**[28:36](https://www.youtube.com/watch?v=XQLawv8CO-I&t=1716s)** specifically for the sensor data and actually when I used it on the sleep stage uh stage data it smooth it out and then predicted very well but unfortunately I did not have the good visual visualization of it here. Um, I guess I'm done with the talk. if you have any questions. And I hope I didn't bore you much.
