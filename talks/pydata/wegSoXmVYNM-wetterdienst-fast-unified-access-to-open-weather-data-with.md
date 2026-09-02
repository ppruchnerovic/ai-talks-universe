---
id: wegSoXmVYNM
title: "Wetterdienst: Fast, Unified Access to Open Weather Data with Polars [PyCon DE & PyData 2026]"
slug: wetterdienst-fast-unified-access-to-open-weather-data-with
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:21:50Z
video_id: wegSoXmVYNM
url: https://www.youtube.com/watch?v=wegSoXmVYNM
youtube_url: https://www.youtube.com/watch?v=wegSoXmVYNM
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Wetterdienst: Fast, Unified Access to Open Weather Data with Polars [PyCon DE & PyData 2026]

**Speaker not identified**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=wegSoXmVYNM) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Benjamin Gutzmann demonstrate how to eliminate API complexity and accelerate weather data pipelines using Wetterdienst, a powerful Polars-first library for unified open weather access.

Speakers:
Benjamin

Description:
In this presentation, Benjamin Gutzmann, a Data Engineer at Otto Group data.works, introduces Wetterdienst, a Python library designed to simplify the complex process of accessing open weather data. Because weather and environmental APIs vary wildly in format and structure, data engineers often spend more time on "plumbing" than on actual analysis. Benjamin explains how Wetterdienst solves this by providing a unified, Polars-first interface that standardizes request patterns across multiple global services, including the DWD, NOAA/NWS, and ECCC.

Viewers will learn how the library normalizes inconsistent data into tidy, long-format DataFrames using SI units and UTC timestamps, while implementing robust caching and retry mechanisms to ensure pipeline reliability. Benjamin walks through the provider architecture and demonstrates practical workflows for station discovery, timeseries retrieval, and exporting data to databases. Whether you are building ETL pipelines or training ML models, this talk provides a blueprint for integrating weather data via Python, CLI, or REST API to accelerate your analytics and operations.

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

*4,568 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=wegSoXmVYNM&t=6s)** So uh yeah, hello, welcome everybody. Actually, I just added the title itself uh this morning because I forgot about it. Um and also there's um another slogan we use usually which is open earth data for humans. So Vetadines these days also covers not only weather data but also some hydraological data. And maybe the slogan resonates with some of you from another library. No. Uh we actually took it from requests which uses HTTP for humans. So the idea is just to make it as simple as possible to yeah retrieve weather and also earth data uh in a few lines of code. Um and yeah [clears throat] weatherines also stands for weather service. Uh, and also

**[0:55](https://www.youtube.com/watch?v=wegSoXmVYNM&t=55s)** a little warning, I will use the word DVD which stands for German weather service and I think the English pronunciation of DVD is just it's not good. So, um, I will skip that. Here's a little introduction. So, I'm first I'm going to introduce myself again a little bit. Uh, I'm talking about the journey of betadines or to better then about vetines and its futures itself. uh then the value that it uh gives to you, me and to everyone hopefully. Then we have a little demo and afterwards the questions. So I'm 32 years old. I'm a happy resident of Hamburg. Um I have several hobbies. So I usually play football but but I also like to go to Hamburg's biggest uh

**[1:42](https://www.youtube.com/watch?v=wegSoXmVYNM&t=102s)** football stadium. Um I play also volleyball and also by day I like to walk auto on the right side. Um, and by night I like to go to cinema and concerts, for example, in the famous Mojo Club and on the Rapan, but obviously I also do coding by night when there's some time left. Um, yeah, I studied hydrarology at Todd Dristen, so I'm from the environmental sector. So from 2013 until 2020. Um, when people ask me what is hydrarology, I first tell them water. And the second thing I'm telling them is it's basically the entire water cycle. So from the clouds in the sky up to the bottom to the groundwater. Uh yeah. And why Dston? D has a long history with

**[2:33](https://www.youtube.com/watch?v=wegSoXmVYNM&t=153s)** severe floodings. You see in the middle a picture of Dston in 2002 the entire city center was flooded and on the right you you see from the same year a picture of the main station. Imagine uh how what conditions you had during this period. Um so I think that's that's a big relation between the city and hydraology. Uh and in this in this case of of flooding. Yeah. Um since 2022 I'm at Autogroup Data Works which is also part of 10. Uh we are also here with I just put up the picture on the right. We are here with a big group of people. Um there are many young people also there. It when I when I joined them it felt a bit like just being at university again. So not a real

**[3:21](https://www.youtube.com/watch?v=wegSoXmVYNM&t=201s)** change. Um yeah and at at um the other group I'm working usually on rankings for shops but also these days we are working on generative AI based bots um which I'm feeling feeling really lucky about because we can use all the nice technology and uh we al we also on the Google cloud so we have access to all the features um of of Google of the Google cloud and yeah it's a real pleasure to work there and you get to learn lots of stuff. Um so then about the journey to vetin um I'm starting at how you can work as a hydraologist. So there are many different possibilities. For example, on the top left, some people like to go in the field do some measurements on rivers like velocity and chemicals and other

**[4:12](https://www.youtube.com/watch?v=wegSoXmVYNM&t=252s)** people also go into simulation. For example, on the on the bottom left, the groundwater simulation is an important part. Others may may may go to um some companies that manage reservoirs and do some predictions and forecasting for the capacity. And uh on the bottom right uh some people tend to stick to university or to some research and actually this is the institute of materology and this is also where I um started with my bachelor thesis uh which was about homogeneity. So homogenity in terms of um precipitation time series. So I had to I was tasked to research the homogeneity of eastern saxony eastern sonian precipitation time series and homogenity in this case means um so usually you have your

**[5:02](https://www.youtube.com/watch?v=wegSoXmVYNM&t=302s)** precipitation station and you do the measurements all the time but um and then then maybe over over decades over hundreds of years climate may change um and this this could cause a disruption in the time series. So may it may jump or it may um yeah there may be a trend upwards. Um but there could also be external cases or like external changes in the surroundings like for example a house is being built the station could be moved 100 mters further and then suddenly you have other conditions there and precipitation may be also different because of those different conditions and you don't uh you want to make sure that when you say um precipitation changes in this area it's not because of the surroundings

**[5:51](https://www.youtube.com/watch?v=wegSoXmVYNM&t=351s)** changes but because of actual climate changes. So um and this was this had to be done for um like I said eastern sex saxony with roughly I think 95 stations it was and you could imagine this is not being done by excel but instead and this is a I think the typical entry to scripting and coding in the university it's not python but I think it's R rather because it's really simple you have your script you can run line by line you can I think it's easier to understand for the beginners. So this is how I started. So I was not into Python back then. But uh my interest was sparked and I continued working in the university and then I thought hm I have the opportunity as a student to join

**[6:39](https://www.youtube.com/watch?v=wegSoXmVYNM&t=399s)** some conference for cheap money. So I went to Brussels in 2017 which was really nice. And there was also a talk about air DVD or RDWD by a colleague who I think worked in pot climate research institute back then. uh and it's yet it felt really nice like you have really only a few lines of code to achieve some data which I think basically back when I worked in the institute they did still some um transfer of like from um I think they I don't know if they sent them hard drives from the DVD uh to the institute and this this uh library would just make it so much easier to retrieve the data and in the same time I thought um R is not enough for me I think um you can do

**[7:29](https://www.youtube.com/watch?v=wegSoXmVYNM&t=449s)** some stuff with it, but Python has so much more capabilities. Uh so I want to learn Python and I have already a library that I I like. Um and I need a project which uh I can use to learn Python. So I'm just going to port it over to Python. Um yeah, and that's that's how it actually went. Um along the way, I want to mention uh two important things. One is my mentor I call him. I don't know if he I don't think maybe he doesn't understand it like that but it's Andreas Mupt. He's like a legend in OSS development. Check him out on GitHub. He has many projects is in uh software development for already decades I guess and he was or is active in beehive community and they

**[8:18](https://www.youtube.com/watch?v=wegSoXmVYNM&t=498s)** have relations to weather data because they like to measure temperature because bees tend to leave the hive when it gets cooler and they come back when it's warmer. Um so there was his interest for weather data and also for the library. Yeah. and he joined me and helped me set up a clean structure for vetadines in the beginning and also some state-of-the-art CI/CD pipelines and he also comes back every now and then and then also honestly it pushes me also just to uh put again some more time into which is not always the case in the last month and uh yeah and then also which is really important is open data because Vadins could not afford providing data when like for example I would have to pay for the data I would be bankrupt uh

**[9:08](https://www.youtube.com/watch?v=wegSoXmVYNM&t=548s)** but luckily there's open data these days and I think it's great because it's uh enables research privately as well as institutionally so um and this is great because in times of climate insecurity we it's good to have a single source of truth so we can just look into the data and prove um the climate change we see outside maybe or in the models which is also important but also in terms of global insecurity. So it's good to have multiple institutions because you know these days some institutions may um yeah quit or not provide data anymore and run models. So it's really important to have I think multiple institutions like DVD and yeah um also yeah like I said many national

**[9:58](https://www.youtube.com/watch?v=wegSoXmVYNM&t=598s)** weather services published their data already like vet like do vetadin since 2017 and they do it really accurately so basically I think everything they measure there's a data set for um it's it's a real um it's a real lot of lot of data they provide um but there's also other services for example in Europe the geosphere the it's basically the environmental agency of Austria. They also have um an API these days and Noah the the US version of the environmental in agency also publishes the data in 2018. Um and they they have the benefit like in terms of the delta data wealthy that they also um ingest some of the data of um the German weather service

**[10:47](https://www.youtube.com/watch?v=wegSoXmVYNM&t=647s)** but not all of it because they have ti they are tied to fixed resolutions. They have data in daily resolution and also in hourly but uh nothing more than that. And also I forgot uh open source software is obviously also really important because relies on polars uh fast API uh click and many more and um those are obviously also really important for vetadines to work. Um yeah now let's look at vetadines itself. So the statement is retrieve the entire climatological history of a place or a location like for example say damstat and this in 10 less than 10 lines of code and this is actually um uh what's the case these days. So you just

**[11:34](https://www.youtube.com/watch?v=wegSoXmVYNM&t=694s)** need to import um like um combination of provider and network. So provide pro provider would be DVD in this case and the network um I call it observation. So it's observational historical data. It's not forecast data but it's historical. Uh and then you just define the parameters you want for for example in this case it's uh in daily resolution the climate summary data set and from that the parameter temperature I mean 2 m. So this is a regular measurement in 2 m height in this I think it's called English hut or something they measure it in plus maybe some start and end date plus maybe some settings for the unit you want to have the temperature values in. Uh yeah and then as you see also you need some kind of station. Uh ah no

**[12:25](https://www.youtube.com/watch?v=wegSoXmVYNM&t=745s)** first first the results and the yeah like I said the results the core results are polar data frames. I think everyone can work with it with it. Even like in the university everybody knows data frames. Everybody loves them. Um on the on the top you see first um the station list. So basically you see on on top we filter for station clutcher and then you you get one row with all the information for that station. So it's basically again the the parameter is is listed there like daily and climate summary. then the ID then um start and end date and some geographical um information which is important to filter it out in a way. Um and then the actual values. So there

**[13:13](https://www.youtube.com/watch?v=wegSoXmVYNM&t=793s)** you get uh the list of values. Um you also have a quality column in the in the back but we won't talk about that today. Um yeah and here you also see the the the details about the request. So it's daily climate summary and then the parameter. So the the response is full of the details we we have or we need from the request. Um then there's also a metadata model um which is important to define all kinds of no code stuff to um that that basically describes the data set in its hierarchy. So there's some information about the provider and the network some kind of metadata. Then there's a resolution which like shows how the values the resolution of the values that

**[14:01](https://www.youtube.com/watch?v=wegSoXmVYNM&t=841s)** you retrieve basically so daily or hourly or whatever the data set uh so it's it's data the data set's name and um uh yeah some other definitions and then maybe most importantly the parameter model where you also have this definition of unit sorry and uh the benefit benefit of it is also that you can rewrite your request using this model with a dot annotation. Yeah. A and it's it's based on pedentic I forgot to mention. So um and the other thing you need is the simplest form. You would just have to define two um or to do some implementations for two abstract methods which one is one is

**[14:52](https://www.youtube.com/watch?v=wegSoXmVYNM&t=892s)** all method for the station list and the other one is the collect station parameter data set and this second method does all the collection for the data itself. So it fetches some data from the API. Um there's different methods for the selection of the station. So typically in the beginning you don't know which station you actually are looking for. So who knows the ID for the dumpshot station? I don't know. Uh so in the beginning you could just uh request all the stations and then from this list on um yeah look look up the ID of the Damshot station and once you have that you could just go with filter by station ID or um alternatively you could do a fuzzy search for Damshot as a city name or you do some bounding box search um if you're

**[15:43](https://www.youtube.com/watch?v=wegSoXmVYNM&t=943s)** interested in stations in a certain bounding box you could also do a ranked search for um x number of stations closest to latitude longitude pair um or just retrieve all the stations in certain distance but there's also um SQL filtering for the stations you want to retrieve data for um yeah and if [snorts] no station is found there's also interpolation and summary methods these days and they try to automatically fetch as many stations as reasonable So um you don't typically want to fetch all like 100 stations that would be able to use for interpolation because that takes ages. So instead we do like a I think I try um we try to fetch as many

**[16:33](https://www.youtube.com/watch?v=wegSoXmVYNM&t=993s)** stations as feasible to interpolate uh as much data as possible in a certain date range. And this is important to notice. This works best for homogeneous data like temperature. Temperature is really equal over the area. But precipitation is really inhomogenous over the area. So it's really different of if you're looking at precipitation in Damtra or in Frankfurt for example. Um there's also many different exports. So from the data frame you can go on to some databases. Uh you have file exports. Uh and you have also many different uh formats also in Python objects. Uh so you can just continue with um yeah your your your whatever whatever setup of database you have

**[17:23](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1043s)** locally. Um there's also a CLI. I think everybody has a CLI today and also Vadin. So this thing also replicates a request you've seen before. Um yeah and um you could just write rewrite then the request in with the CLI but also there's if you install fast API optionally you can do the same with an HTTP request and the same I I show you the same for one for stations and the other thing for the for the values. Um yeah and there's also an app these days. Um, shame on me. I vipcoded it because I'm not a front- end developer. Um, and the idea here is just to simplify the access

**[18:11](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1091s)** for people who cannot code or set up a VN for whatever like my I think my mother for example. And the idea is J. Yeah, you have different um applications. One is the explorer where you can just also um replicate the requests I've just I've just shown you just in a UI way. There's also climate stripes. Stripes I you may have seen them already some on some events. It's a nice way to express climate change for your city. Um yeah, maybe I can also show it later to you if you want. um station history is um showing the metadata of some stations but this metadata is for many services not available I think at this time only for DVD and there's also the rest API itself

**[19:00](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1140s)** so basically the HTTP request I've just shown you can just also send it to this to this app which is running on better eops.org talk. Uh yeah, one more thing. This is a vet in uh this is a DVD API. So it's a plain file server. Uh there's no actual API. And this is also the the the best reason why vetines actually started because you would just have to go all through all the files manually and look it up yourself. You see even here the station list is not a real CSV. So you have to do some manual pausing there or like fuzzy pausing. uh yeah but I think we are still lucky because they provide just so much data uh DVD for example this extensive data set description where you find all the information about

**[19:46](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1186s)** the parameter and there are also some quirks but I think we don't have too much time for this so I will just skip that yeah and then the what value did it give us so I think for me it's fun and also obviously the result belongs to me and you and everyone and it's not hidden behind in the business case um it's a good place to try out new stuff um and then usually um if it works like new tooling I also tend to take it to my workplace and implement it there um but there's also many impact on many businesses and processes for example agriculture construction industry for example where they rely on temperature forecasts for concrete drying um insuranceances for example where they want to show that a hazardous event was

**[20:37](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1237s)** caused by this historical rainfall for example. Uh autonomous driving I've also seen so people use high resolution precipitation data for training on the rain sensors. Um and then obviously also the research on climate change itself. But my hope um I think yeah people who who are into this already know how to get the data or they are in reach with with me um but my hope is also for you to inform yourself. So but I'm still figuring out how to how to improve Vetadin or the Vetadin app for this case. Yeah. Now the demo and VIP code alert again. Uh what I did is because I I think I what I wouldn't I wouldn't want

**[21:24](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1284s)** to rely on the internet here. So I just dumped the daily climate summary data set into a duct DB file. Um and I created a Marimo notebook around it. The ductb file I put also online. So if you want you can just do your own SQL on it. So I'll jump over to PyCharm. started and I did some an analysis of uh some analysis of this data. So first thing um we see is um yeah here's here's uh by the way the code snippet how I created the ductb file. So I just used some to target function here to pump the data into

**[22:11](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1331s)** ductb file. Yeah. And the first thing first interesting thing we see is the station network of this climate data climate summary data set. We see there are a total of 1,200 stations but currently there's only 566. So so there's been obviously lots of changes going on in the past. We see also the historical development. Yeah. First station was um opened in 1759. Um yeah and then we see by 1900 it was still quite scattered 1950 it looks already better. Um yeah and today we have a really dense dense network of stations here. Um what I asked um

**[23:01](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1381s)** or like what question I asked myself is the impact of war. And you could see here that in the first world war there was no real impact but I think it was also not so many stations maybe but then in World War II you could definitely see definitely see a decline in stations during the end. So I think um you always also see this kind of historic events and sadly in this case um also in the data. So there's also some gaps in the data usually you see during the World War II period for Germany. uh yeah and there's another interesting effect I think we talked also during my uh work at the institute at the at the university and you see here in the in the end you usually you would expect well we have developed a good network now maybe let's continue or even or just

**[23:50](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1430s)** maintain the same number of stations but there's actually a decline here and I think there were two reasons one is that usually the network is um there's volunteers working on it usually retired uh teachers I uh I heard and they have to go to the station every day and check if everything is okay. And actually I think this is hard to um yeah acquire those people those volunteers these days. Uh and it comes also with a side effect. So David Day is at least when we when I was in the institute we were we were discussing this. So DVD I think tended to um replace u people by um like automated technique like cameras and this kind of stuff and they were actually not really happy with it because it would or they they would

**[24:38](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1478s)** implicate that the quality of the measurements would go down with this um yeah with this change. >> All right. Well, I guess we're short on time. Uh we have five minutes for the Q&A session. If that's okay, I will uh read out the questions one by one. Okay. The first question u is uh interpolation between multiple stations purely mathematical or does use some kind of meteorological model in the background? Um yeah good good question because um also you have some um sometimes difference in the height of the station and this kind of stuff. So yeah,

**[25:26](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1526s)** geometry also I think should play a role but honestly at the moment and I can say no except we do some uh additional technique for precipitation interpolation um which is because there are days um where where there's zero precipitation but usually when you interpolate you always get not zero but really close to it. So in for the case of interpolation of precipitation we do another interpolation of has it rained or has it not rained. So zero um 01 and then we do the cut off there to say the interpolated value is either zero or above zero. >> Yeah makes sense. Uh the next question is as polars is relatively new did you

**[26:15](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1575s)** start with pandas? Did you have any conversion problems or do you miss any features in polars still? >> Um yes, we started with pandas. Um and but like I said, we like to play with the new stuff and we were um yeah happy to see this advertisement by Polas. It's really fast. It has lots of optimization. Honestly, I don't know what it means in reality, but we uh switched directly to Polas um when we thought it would have the most necessary features and I think in the beginning we had also some workarounds. I think these days it's quite complete for what we need. So we do just some clean up mostly on the data and then uh yeah for that case it it is already state

**[27:05](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1625s)** >> state. Yeah. Uh next question. And the logic is set up so that if a good weather station isn't found, it pulls data from several nearby ones. But does it take elevation into account uh with just a straight line distance whether you actually get similar data? Seems like it would depend on the station. >> Um can you repeat? >> Yes. Uh the logic is set up uh so that if a good weather station isn't found, it pulls data from several nearby ones. But does it take elevation into account? >> No. For the elevation, no. At the moment no. >> All right. Uh what amounts of data do we

**[27:55](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1675s)** talk about when working with weather data? Um so I've shown you like on the um daily um so this daily values obviously I think are the ones that reach most back in time because it is just one time per day measurement. One person could go to the station check the value and like return home. Um and those values reach into um 18th century. So it's a really long time series. I think you find maybe only older ones in England. Um and for the higher resolutions they don't reach back that long. So for example we have this one minute precipitation data and this is starts I think at uh in the '9s 1990s. Um yeah and I think also

**[28:43](https://www.youtube.com/watch?v=wegSoXmVYNM&t=1723s)** yeah that's that's the answer 1 minute and 10 minutes don't reach back that long maybe in the ' 90s >> I guess uh we have time for one more question. Which kind of distance are you using when searching for stations? >> Um like the >> the units maybe they mean. >> Yeah. Right. Um I don't I don't find the name right now in my brain but obviously we cannot just um we have to do some like uh projection distance calculation. I don't know if that answers your question correctly but I don't have the name my in my brain right now. >> Thank you. you can ask him after the session. Well, thank you so much. Uh, okay. Let's thank our speaker once again.
