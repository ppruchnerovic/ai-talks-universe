---
id: ZvEIqSvvat8
title: "Restaurants around train stations are bad and I can prove it [PyCon DE & PyData 2026]"
slug: restaurants-around-train-stations-are-bad-and-i-can-prove
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Dennis Schulz"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:21:20Z
video_id: ZvEIqSvvat8
url: https://www.youtube.com/watch?v=ZvEIqSvvat8
youtube_url: https://www.youtube.com/watch?v=ZvEIqSvvat8
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science"]
transcript: true
---

# Restaurants around train stations are bad and I can prove it [PyCon DE & PyData 2026]

**Dennis Schulz**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ZvEIqSvvat8) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Dennis Schulz use Google APIs and Polars to analyze 10,000+ restaurants and prove whether proximity to train stations systematically ruins your dining experience.

Speakers:
Dennis Schulz

Description:
This analysis investigates whether restaurants located near train stations in Germany are systematically lower in quality than those in city centers. The study utilizes a dataset of 226 German train stations identified by the presence of a Reisezentrum (travel center), using these locations as GPS anchors. Restaurant data was gathered via the Google Maps Nearby Search API, resulting in a dataset of 10,272 restaurants near stations and 11,331 restaurants in city centers. To ensure data reliability and mitigate the impact of review tampering, the analysis primarily filters for establishments with more than 100 reviews.

The findings indicate a strong correlation between proximity to major train stations and lower ratings. In large cities, restaurants in the city center consistently outperform those at the main station; for example, Berlin city center restaurants average 0.4 stars higher than those at the main station. A linear fit of the data reveals that for every kilometer a diner moves closer to a train station, the average rating decreases by 0.69 stars. In the largest and lowest-rated stations, this decline is more severe, dropping by 1.41 stars per kilometer, which equates to a loss of over 0.1 stars for every 100 meters of approach.

Further analysis of restaurant chains and naming conventions shows that Burger King consistently ranks as the lowest-rated option, while pizzerias, doner shops, and "Asiabock" establishments perform better. Restaurants incorporating "Tokyo" in their name achieved the highest average rating at 4.5 stars. The data suggests that while small-town stations like Backnang and Sinsheim maintain high standards, major urban transit hubs are associated with significantly lower-rated dining options.

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

*4,465 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=5s)** Uh thanks to all of you. I'm super happy that so many people show up at the last slot of a three-day conference. Uh that is very nice. Thank you. Um just as a quick context like I am from a company called uh bless you TNG technology consulting. Um but in our daily work we have nothing to do with restaurants. This has been a hobby project because we have some time off where we can do hobby projects. And this was one and it was created in the moment where I was at Stoutgart main station. And the problem there was like I had about 1 hour of time and I was like there must be some place to get at least slightly decent food

**[0:52](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=52s)** and there wasn't. There was just nothing. And then I was like, but that's often the case at train stations. That happens all the time. Like, can I somehow, you know, look up uh if if there are any, you know, um train station, like if if this is a systematic problem, if there is a conspiracy that bad restaurants are around train stations and they somehow cluster there. And uh this is my attempt. Um I will go through three steps. I will tell you where I got my data from. I will analyze the data and then there will be results. Yay. Um that is the principle. So let's start with where I got the data from. Um can we make that a little bigger? Yeah, that's a little bigger. Um there's a lot of wonderful data sources. There is goth

**[1:42](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=102s)** data.de which has all kinds of data about Germany. Uh there is the mobility that has all kinds of data about mobility in Germany. There's open data upp and fo which is all kinds of data about public transport in Germany and then up around like 3 years ago there was an open data portal of the German train system of Deutschean which is now deprecated but within the last month that they were online uh I found this data set which is um the data set of every single riset centrum which are these places where you can get tickets and sentum that's a great measurement for if you know if a train station is important enough because if they actually pay a person to sit there

**[2:30](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=150s)** like fulltime kind of full-time to help you then probably there's enough people that frequent that train station. So that's great. That's super cool. Um what is in that data set? Well the address that's kind of cool. Um it says that it's a true prizet sentum which just confirms what we already knew. Um there's opening times and uh it's opening times for all of the days. So that's also super helpful. Some of them are open on Sundays. Um and then they have some coordinates which for some reason they give in oh well >> in the end. >> It's in the end. Uh yes, which for some reason they just give at as this full number and then you have just have to trust that they use six digits beyond

**[3:18](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=198s)** the comma and then you have to pass it and then you get these kind of latitudes and longitudes. Well, cool. So we have GPS data of important train stations. That's surely the first step. So let's continue with, you know, just a quick check. And this check is are these reliable? And I will just quickly Oh boy, I didn't think that I have to do this in a mirrored way. Let's see if I manage. If not, just believe me, it's perfect. Like the GPS locations work. They know where the riset central and train stations are. That's super cool. They have fitting GPS data for what they want. So that's cool. Um the GPS locations are reliable. Um okay. So how do we get the restaurant data? For the purpose of this particular

**[4:09](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=249s)** talk, um I will just assume that Google Maps ratings are truth which you know it's okay kind of works. It's some it's often it's okay and there is a nearby search API uh for which you can get a 90 days free limited trial and then you pay per request but there's ample limits within the within where your requests are still free. Uh and that is obviously one of the many ways Google makes money. I found this number that for example Uber used Google Maps and then paid 58 million uh dollars in the years 2016 and 2018. If this is added for both years, I don't know, but you know, like they make some money off

**[4:57](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=297s)** of that. It's one of the many ways in which Google makes money and and that's how Google Maps makes money kind of. And what you then get is a list of restaurants. So, you know, I just went down the list. How many restaurants? It's a little hard to read. So, it's 10,272 restaurants that are in the data set. And uh what you get is well you get the like this is linked up with you know the place uh that this restaurant is around. There is a latitude and longitude. There is a rating uh there's an amount of ratings. Then uh for every restaurant uh Google gives some tags that can be cafe point of interest something like that. We'll take a closer look into that in a second. Uh sometimes there's a price

**[5:45](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=345s)** level if it's expensive, really expensive, kind of cheap, and then of course a unique identifier. All of that kind of expected. So um let's check like how many restaurants do we have per kit sent per train station. We have exactly 60 for every single train station. Why is that? Because uh the places API they say it should not be a search like search engine for restaurants. What they want to do is deliver reasonable results. That makes sense. So they just deliver 60 except if you go back for Munich which has 74 uh which is because they have a risot sentum for the IC and all the big train traffic and then one for the small metro and esban. So I did two requests

**[6:33](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=393s)** and within that range there's basically more restaurants than 60. So that's the idea. Okay, cool. So let's take a look at the labels. Every single one of the 10,272 restaurants got the label food. Makes sense. All of them are an establishment, a point of interest, a restaurant. And then we go into like a lot of them offer meal takeaway. You know, some are a store. Let's go a little bit. Let's let's check the slightly, you know, less common ones. We have uh things that are, you know, a restaurant and a tourist attraction, a restaurant and hair care, which I guess works. Um we have a drugstore, um a furniture store, and a funeral home. Also, [laughter]

**[7:22](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=442s)** there's one space that is rated as a restaurant and a funeral home at the same time, which I'm sure is a great business model. Um okay cool data kind of makes sense. Uh so I would suggest to just take a look you know and maybe sort a little things for the rest of the talk and and this is the only measure that I will do against you know there's a lot of faking of reviews and adding reviews artificially and uh my safety measure is that I only allow places that have more than 100 reviews. Uh if you want to challenge that metric, sure. Uh do that. Cool. Yay. Um we all want to know like so what is the worst

**[8:10](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=490s)** place you could go? Um it is buckfish mic at the rise at centrome visma which I have to say um delivered quite the heartbreak because up until a few days ago this was open but uh unfortunately it is now permanently closed. It has been open for the last 3 years. I check in with my restaurants. I don't know. I checked it from time to time. Um, people uh technically people complain that the uh fish is so solid that it feels like concrete. I guess that's not good. Um, then uh let's uh check the other end of the

**[9:00](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=540s)** scale. Um, I know we have some stuff. The one with the most ratings is the Mamame Mia Pizzeria in F. Um, let's just check. Uh, since I collected the data, it has lost 0.1 stars. Woo. But it is still rated very well. So, if you ever uh happen to find yourself at the main station of F in Bayan, check it out. It's within 500 meters. That's all I can say. Seems good. Seems cool. Um, so, uh, with that, we have a data analysis. you know, we we have a lot of restaurants. We have our data set. Uh kind of makes sense to look into it. Um and uh I will I don't know the thing is that

**[9:49](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=589s)** another thing that we can look into later maybe is that then it's a lot of Burger Kings that follow each other. I don't know what to make of that. Okay. So um what are so so let's you know let's aggregate let's let's like check which place like which train stations are actually the best places you know to to have to grab some food in the entirety of Germany. Um well uh well this is the list by station. We have 226 places that have risen in Germany that are in the list and the best place to eat are Baknang, Image, Aransburg, Likenfeld Tronstein Uber Zinheim Horb, Vinandon and Ravensborg.

**[10:42](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=642s)** I am not sure how many of those you would be able to locate on a map with confidence. I don't know. I don't know. Is this a pattern? Let's I don't know. We can just check the other end of the list, you know? Like let's check what the worst places are. [laughter] Ah, Frankfurt Berlin KW Osnabick. Oh, uh, Stoodgart, Stoodgart, Berlin again, Hamburg, Pman. Those are places that you know and that makes you think right that kind of I don't know it sounds like maybe I don't know bigger cities are maybe bad

**[11:31](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=691s)** like maybe maybe it's just that the size of the place kind of leads to worse restaurants. There's all kinds of hypotheses that you could do with that. Now I I kind of wanted to check if it is just the like in at a train station you have thousands of people that rush by and it's super you know you can just say I mean maybe they are dissatisfied maybe they are stressed maybe you know they just missed their train and then they enact their fury on the local subway I don't know um but I don't know what is what is a data that we could kind of compare this to and if you have any better ideas please let me know but the best idea that I had was to compare it with city centers because those are

**[12:18](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=738s)** typically the other places where a lot of people are. Um, so let's use a data set from goff data.de. Uh, you can download this. It's super cool. It's just every single place that somehow has a name in Germany. Um, uh, it has, you know, places if you sort it by population. Um, it has places like Brun Liberfeld with a population of zero. So I don't know if you want to look for a place in Germany a way you want to move and then increase the inhabitants by infinite percent. This is a list of of places. Uh the other end um again is of course all the big cities Berlin, Hamburg, Munich,

**[13:06](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=786s)** Cologne, Frankfurt and so on. Um, and uh, nicely enough, there is a longitude and a latitude directly inside of that data set. We can just do the same same thing over again. Through this, we get 11,331 restaurants. That's again a lot of restaurants. Cool. Um, so, uh, let's keep the minimum amount of ratings at zero. Um, I don't know, just because it's fun, let's look at the worst restaurants from the data set again. Um the worst restaurant from this entire data set. Let's verify it here in the data is um [laughter] sometimes these break and then I have interesting results. Was this a okay? Yes. Uh for some reason I think I

**[13:56](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=836s)** said 80 here before and was like 80 is a number of reviews that is extremely safe against tampering. Um so uh the worst place with 86 ratings is of course the city Duna in H. Um let's uh check that one. Uh that one is also permanently closed. Um and the second to worst restaurant is still open which is the Hanoi cuisine Vietnamese daily and sushi pizza and da kebab. which they could have just named food. I mean, I don't know. I guess they don't do burger. I don't know. Cool. Um, but that one still shockingly exists. Um,

**[14:46](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=886s)** which I guess is good for them and sad for Chemnets. Uh, okay, cool. Let's do the same exercise as we did just a second ago. And um the best city centers to eat in. You might already recognize the pattern. Those cities are Leonardo, Ibas, Henev, Baknang, Zinsheim. Zinsheim again very strong both in train station and city center which I think is mostly because the train station is the city center [laughter] viping and dead benheim. Um if you map them there's a weird like there's a really weird um weight towards the southern end of Germany. I don't know. Uh, in general, that seems to be a thing. Cool. Um, so I think we've gotten what we wanted out of that plot. Um, and

**[15:37](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=937s)** now let's compare. So we have the average rating at the train station of restaurants at the train station. We have the average rating at of restaurants in the city center. And the assumption is if it's just about a lot of people passing through, then the ratings should be kind of the same. So let's plot it. Um any So this is a lot of dots um and a very raw plot. Down here you have inhabitants. So those are the cities that have more than 1 million people living there. Um this is the zero line. Those are the cities where um well where the restaurants at the train station are better. These are the ones where the restaurants in the city center are better. I think you see that it

**[16:26](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=986s)** strongly, you know, that it strongly skews towards one direction. Uh we can even, you know, uh because let's just say that we need around Yeah, this is okay. This is around 150,000 people to just ensure that we have a town where the city center is at least a little different than the train station. That would be lovely. Uh and then you know we skew strongly towards city centers. City centers usually give you better food. Uh in Berlin the average rating is 04 stars better than at the main station in this particular case. Well that's a that's a pretty cool thing. So seemingly train stations have this thing about them. Um, which of course begs the question, if you

**[17:15](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1035s)** approach a train station, does it get worse the closer you get to the train station? Like, are you on a slope of raiding with every meter that you approach the riser centrum of a train station? Um, basically, how fast does it get worse? And the next plot um I'm happy to say uh is the messiest plot that I have ever seen. Um is um every dot here is one restaurant in the data set and this is the distance from the riset center in kilometers and then what do you what do you get when you have like such a cloud of points? Well, and you do a linear fit and the linear fit

**[18:04](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1084s)** tells you that per kilometer that you get closer to a train station, the rating decreases by 69 stars. Now, this includes a lot of places, you know, where the train station and the city center are kind of the same place. So let's just look at the places at the worst train stations which are which just happen to be also the worst you know the the the biggest train stations and uh there you get a decrease of 1.41 stars per kilo kilometer which means that with every 100 m you approach the train station the average rating drops by more than 0.1 stars. So just keep this in mind next time you know like [snorts]

**[18:53](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1133s)** if you you know if you approach a train station it really it does get worse which can have all kinds of reasons. Honestly one reason that I find kind of convincing [snorts] is that of course you only get 60 restaurants and in big train stations which within a 500 meters radius you have hundreds of restaurants not just 60. So if you do a search, it will give you restaurants that are close to where you searched and then good restaurants that are a little further away. So this might be an effect though I didn't see this effect in the city center data set as strongly but I assume that this is somehow true. For the purpose of this talk again we ignore all of this and um we will just say that rest that just you shouldn't approach

**[19:41](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1181s)** rest like train stations while being hungry. Um and you know uh just as a service portion of the talk you know um let's uh quickly go uh through the few places that are in Damstat. So uh this is the the places that are around Damstat train station you should definitely avoid uh the subway uh at the main station and look and vapo uh just that one is basically I mean yeah do with that what you want. uh and uh those places are the ones where you can easily grab some food before you go to and take your train to home. And then I mean you know we assembled a data set here of about you know 18,000 restaurants I think it is when you

**[20:29](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1229s)** remove all the duplicates. So let's also just quickly check uh which uh chains or you know if you are just in a like random place and you just have the names of restaurants and you have to decide where to go uh then uh let's just see like what is better if uh in the name of the restaurant there's some something like McDonald's is subway better avoc bakvak and then I just included pizzeria for fun um and uh if We rep sort by average rating. Uh Burger King is consistently the worst. Um while Pizzeria, Azia, Azyok and Duna are consistently the best uh choices. And um then you know places are sometimes named

**[21:19](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1279s)** after cities. So I also checked uh some cities that are typically names of restaurants. Eastern Bul Napoli, Paris, Tokyo with ah a place and Italia and uh basically uh places that are named Tokyo ah have an average rating of 4.5 stars which is impressive. So to sum this part up I guess Pizzeria Tokyo is the best place that you can go to. So, what have we learned? I don't know. I mean, [laughter] if a place is called Vietnamese sushi pizza duna kebab uh burger, then maybe don't go there, especially if you're in

**[22:08](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1328s)** cabinets. Um, I also just want to stretch the part that it was so much fun to do this and kind of easy. So, if you have a question like this, I don't know. I mean probably all of you you know know that it's very easy to do this but if you you know just miss this like push to actually like go after your question and try to answer it with data you know like very realistic questions sometimes do have data sets that you can just look up um and just take an attempt at it is really fun and uh I don't know you get weird facts like what the most uh what the eastern most trains station in Germany is Frankfurt order. Um and apart from that I can only repeat

**[22:58](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1378s)** what I have already said. Um you know like if you approach a train station and you're hungry I I mean good luck. Yeah don't unless you're in Baknang or Sinheim or some really small place. Um thanks for staying till the end of the conference. If you want to add me on LinkedIn, I do I am called Dennis Schulz like I am called in real life. Um uh I uh would appreciate that and I really appreciated you all being here. Thanks for listening. [applause] [applause] Thank you once again Dennis for so engaging presentation on the last day on the conference. And the first question we have why this talk was scheduled to

**[23:48](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1428s)** be the last presentation on the last day. This talk would be more useful on the first. [laughter] I understand the issue. Um however I am not obviously not the programming committee. Um and I agree. >> [snorts] >> Okay, we'll take this one into account. [laughter] Uh the next one, uh besides your enthusiasm and humor, I like your presentation, what tool did you use? Is it made with markdown? >> Uh sorry again, which tool? >> Yes, which tool or and is it made with markdown or what? >> So, this is a Marimo notebook uh used like Whoops. Yeah, this is a Marimo

**[24:41](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1481s)** notebook uh that basically uh is uh I use as a presentation in presentation mode uh which works pretty well. It's a it's kind of annoying if you want like a consistent uh top part of your slide or something like that. But it is nice and interactive and uh works pretty well for data. But I mean this is also the reason why I didn't upload any slides yet. um kind of hard to upload this uh because there's just like data behind it and it accesses all the data and it's pretty much a live presentation or live notebook that runs. Okay. Uh you should send the best and worst in DHMA to Discord as a PCA for everyone.

**[25:29](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1529s)** >> Sorry again. Um, you should send basically the list of best and worst in Dharmstat in Discord. So, people are asking for it. >> Yeah. Yeah, it makes a lot of sense. Um, just I mean, uh, I don't know if my screen is still transmitted. I will just scroll to it for the time being. Um, so maybe you can. Also, um, Damstat has a pretty bad city center for eating. I'm very sorry to say. I didn't include this as a I don't >> uh where is it? Uh I I will post it in Discord for sure. Okay. Um but yeah yeah

**[26:19](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1579s)** yeah >> good. Uh the next one is regarding the data set. Uh you collected a lot of data and this is like a huge amount of work. uh is uh are there these data sets uh available on Kaggle? Are you planning to make them? So um so if you read if you are if you read the conditions on how to use the Google maps endpoint that I used okay >> and if you interpret it really strictly I would say that having this data is at least in a gray zone. [laughter] Uh so for the time being, no. Um but uh you know like there's there's

**[27:09](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1629s)** this uh there's this paragraph on how you're not supposed to you know aggregate the data. However um it's a gray zone. I mean who knows? Um but uh um I can only say like apart from that uh it is a very easy to use API. It is super cool. Like it is really a lot of fun to do it. And the thing is that the data collection actually went shockingly fast. I mean it took some time because you have to I don't know I think you have to do a two second delay between requests but it's not like I sat there and hit enter every new request, right? It's just a loop and then it runs for a few hours and then you have uh 20,000 restaurants. >> And the next question is about this one.

**[27:56](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1676s)** Where to download your code? Uh where did I sorry >> to download your code. >> Uh yes I should do that. I'm so sorry. I will yeah yeah yeah I will publish it currently nowhere. Um we'll change that soon. >> Okay. Um another one is yeah people are really crazy about your talk. Everyone is just starting with thanks for the great talk. Uh have you tried Open Street Map as an alternative data source to Google Maps? >> Uh yes, at the time being um I was reading into Open Street Maps API a little bit. Then the Google one was just like very direct and it already delivered the ratings and I was kind of after the ratings and the ratings were kind of the most important thing about

**[28:45](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1725s)** the whole thing. So I just went with Google uh maps. But I have I do enjoy open street map and I would love to to you [snorts] know take a deeper look into it. I haven't yet but yeah good. Um the last one is about the correlation versus causation. So don't we have here an issue that correlation is not really a causation? Yeah likely. [laughter] No, this is, you know, I I mean I do mean this extremely seriously, but I also don't mean it seriously at all. Like this is a fun talk. I kind of try to do a fun talk. Um I have, you know, I have thought about it and there is this

**[29:34](https://www.youtube.com/watch?v=ZvEIqSvvat8&t=1774s)** thing that restaurants do get worse when you get closer to train stations. Um but of course I started with a hypothesis and then looked for data to confirm it which probably is not the cleanest if you do data science. So yes [laughter] it is a scientific method. Okay. So then let's once again thank you Dennis for his [applause] >> [applause]
