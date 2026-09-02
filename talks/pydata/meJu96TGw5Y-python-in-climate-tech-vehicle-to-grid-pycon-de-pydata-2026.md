---
id: meJu96TGw5Y
title: "Python in Climate Tech: Vehicle-to-Grid [PyCon DE & PyData 2026]"
slug: python-in-climate-tech-vehicle-to-grid-pycon-de-pydata-2026
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:21:32Z
video_id: meJu96TGw5Y
url: https://www.youtube.com/watch?v=meJu96TGw5Y
youtube_url: https://www.youtube.com/watch?v=meJu96TGw5Y
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Science, healthcare & applied ML"]
transcript: true
---

# Python in Climate Tech: Vehicle-to-Grid [PyCon DE & PyData 2026]

**Speaker not identified**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=meJu96TGw5Y) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Christopher Sedlaczek-Bock explore how Python is bridging the gap between automotive and energy industries to scale Vehicle-to-Grid solutions for a zero-emission future.

Speakers:
Christopher Sedlaczek-Bock

Description:
Vehicle-to-Grid (V2G) technology addresses the volatility of renewable energy by utilizing electric vehicle (EV) batteries as distributed energy storage. In Germany, the EV fleet provides approximately 150 gigawatt-hours of capacity, which is two orders of magnitude larger than existing stationary storage. This capacity allows the grid to store overproduction from solar and wind sources and discharge energy during peak demand, reducing the need for power grid expansions and preventing the waste of renewable energy.

The approach distinguishes between V1G (unidirectional smart charging) and V2G (bidirectional charging and discharging). To commercialize this flexibility, individual vehicle assets are aggregated into larger blocks to meet the minimum capacity requirements of energy markets. Users define boundary conditions—including minimum and maximum state of charge and departure times—which create a "polygon of charging flexibility." Within these constraints, optimization algorithms determine the most profitable times to buy or sell energy based on spot market prices and weather forecasts.

The technical architecture employs a hybrid language approach. Python handles the majority of the backend and optimization logic. However, because the Open Charge Point Protocol (OCPP) requires stateful WebSocket connections, Rust is used for the charger control layer to provide the multithreading and performance necessary to maintain thousands of concurrent connections. Hardware integration involves industrial Raspberry Pi-based controllers for dynamic load management. Measured data suggests that V2G cycling results in less than 1% additional battery degradation per year, making the service viable for users who receive financial bonuses for providing grid flexibility.

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

*4,116 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=meJu96TGw5Y&t=5s)** Well, thank you very much. Um, nice to be here again. Uh, we've been here two years ago. Well, not here here, but back in the time in Berlin and, um, back then we were talking a little bit more broadly about what we do. Today I'm just specifically focusing on uh vehicle to grid and uh first of all also who we are um because it's not 100% right I'm from the mobility house energy actually um so since back then um we split into the subdivisions um so that's what I'm going to talk about first then I want to tell you about our vision our mission why actually do we do that um even

**[0:54](https://www.youtube.com/watch?v=meJu96TGw5Y&t=54s)** though it's kind of omnipresent the topic currently in the news and the media and then want to dive deeper into what is VGI, what is V1G, what is V2G because those are terms usually people deal with them if they dive into this topic of bringing batteries onto the power grid and then also give you a little bit of a glimpse because it's just roughly 20 minutes um of what our tech is and what we use. So who are we? We are the mobility house. It's a group um of divisions of companies. Um we are in the middle charging. It was basically how we started reselling wall boxes because 15 years in the past the market

**[1:42](https://www.youtube.com/watch?v=meJu96TGw5Y&t=102s)** was quite different. We basically resell hardware to home customers but also to businesses. We also provide installation services and help with that. Um we also since um I think it was last year have the charge line um in our portfolio our own um wall box but um that's charging. That's how we started. Then usually customers get bigger. The market got bigger. Um fleets came up um and as such also solutions our solutions business where we also developed the charge pilot which is also heavily Python based um even runs um if you look closely um probably you cannot see it well from the back it's an

**[2:29](https://www.youtube.com/watch?v=meJu96TGw5Y&t=149s)** industrial Raspberry Pi so probably familiar to a lot of you here. Um and the charge pilot is basically dynamic load management. So on side if you have a lot of cars charging in parallel usually you blow the fuse. Um and charge pilot is here to prevent that. Has a lot more features than that but that was basically the basic need with which it started. We in the energy we provide electricity as an electricity supplier at least in certain markets but also we commercialize flexibility on the markets. Flexibility means that something on the market somewhere on the power grid attached to the power grid can either consume or actually give power back to the um power grid. And we

**[3:21](https://www.youtube.com/watch?v=meJu96TGw5Y&t=201s)** focus on stationary as well as on mobile assets. So basically as I always uh say it we focus on batteries with and without wheels. So um without wheels those are stationary storageages. I will not talk about them much today just here mentioning them because we have quite a lot of capacity there also under management in operation in the real field um several hundred megawatts. Um I today want to focus on vehicle um to grid in our domain in the energy our vision and mission why actually do we do that um it's a statement um which is quite old 00 what does it actually mean we want to enable people we want to

**[4:10](https://www.youtube.com/watch?v=meJu96TGw5Y&t=250s)** enable everyone to charge their electric vehicles at zero cost and thereby causing still zero carbon emissions. So we want to work towards an emissionfree future and one of the cornerstones for that of course are uh renewables. Um and we are currently in a transition phase towards it. And here a study from 2022 um where um they um analyzed the growth and predicted the growth um probably already outdated and probably um in recent studio studies you would see a little bit of a bigger growth. Um, and the remarkable thing I want to point out here, it's comparing 2022 to 2030, it's

**[5:02](https://www.youtube.com/watch?v=meJu96TGw5Y&t=302s)** roughly tripling um the um power we have available through renewables. However, every one of you knows how renewables work. You need sun, you need wind. And then if you look at how the um public net electricity generation Germany is, here a picture from back in 2024. Um well um they cause problems. Um they are flexible kind of. If there's a cloud over a solar plant, well, it's not producing that much anymore. That's something we have to cope with on the energy markets and thus this increase in volatility needs to also an increased

**[5:53](https://www.youtube.com/watch?v=meJu96TGw5Y&t=353s)** need in flexibility inside the system. So we need to be able to somehow store the over production but also give it back to the grid. So there is already technologies for that but try to build a lot more um hydropower plants um that's not going to work. They are huge. They take a lot of space. They Well, you can debate over whether they destroy nature or not. Um, but you need a lot of rivers for that. Batteries, they're a lot easier to use. And well um I'm not sure how many EV drivers we have here but in Germany end of 2025 we already had around about 3 million uh

**[6:41](https://www.youtube.com/watch?v=meJu96TGw5Y&t=401s)** cars here out on the streets. If you do the rough math actually assume a capacity of run about 50 kilowatt hours you end up at 150 gawatt hours. And well that's also what studies show. Um, we have a capacity with EVs alone of 150 gawatt hours. That's a huge lot. That's a huge battery. Um, and um, here as a comparison, the stationary storageages, which are usually a lot of batteries packed together on just one place, they don't have wheels anymore. um it's two orders of magnitude less than actually for cars. That's two orders of

**[7:30](https://www.youtube.com/watch?v=meJu96TGw5Y&t=450s)** magnitude. So we don't have that much capacity available in form of stationary storageages in Germany currently. That's a problem because we still need to store that energy. Currently the solution often is well turn it off. Um if we have an over production um that's not good. we shouldn't waste that energy. And if we look at the predictions for 2030, well, it's going to double. Um, that's that's quite a number going from 150 gawatt hours to 300. Um, so that's a capacity we should use. we should put to action and not just leave it standing there 90% of the day being wasted

**[8:19](https://www.youtube.com/watch?v=meJu96TGw5Y&t=499s)** because that's actually what cars usually do most of the time. They don't drive around. They stay. However, um there's one complaint or one fear which often comes up. Cars come back home and then they get plugged and then they start charging. Yes, and that usually could become a problem. However, that's also then where the true vehicle grid integration comes into play. Instead of just having them blindly charge, you shift the charging. You manage it towards times which uh suit it better. And that's also what I wanted to show you now a little bit more into detail what is in the year for the individual parties. So

**[9:08](https://www.youtube.com/watch?v=meJu96TGw5Y&t=548s)** most of the cars as you know probably they currently just can't charge. Um they are from the hardware side not capable of discharging the battery other than by driving. Um that's what we call V1G. Um so basically the only service to the grid you can you are providing is you can consume over production but that's already very very helpful because then your car doesn't charge in times where there's a huge stress and strain already on the grid. If now however your car can also discharge that's what we call then V2G. Um so then we can actually also in times where there's a huge stress on the grid discharge the

**[9:57](https://www.youtube.com/watch?v=meJu96TGw5Y&t=597s)** car to support it. Thus also reducing the need for extensions of the um power grid because you have it local you have it there. Um it's not like you need to deliver it still from yet another coal power plant or so to your home. instead it is the most local and easy thing to do. Um and the value chain basically is that the users provide the power grid with flexibility flexibility for storing or giving back energy to the power grid. this flexibility in the first step on our side is aggregated because one car alone um I'm not sure how many people out of the energy business are there but

**[10:46](https://www.youtube.com/watch?v=meJu96TGw5Y&t=646s)** usually trades on the energy market start at at far more than just the few kilowatt hours um you can do with your car. Um so you need to build aggregates which are also useful to the um energy grid and then of course we trade it. Um it's a quite active market. Um if you go to the short-term market which is actually where the flexibility lives um and um then of course the users also get paid back. Um that's the value they get for providing flexibility which is an asset for the market. they get value back in the form of money. How does it look like? Um if you then

**[11:34](https://www.youtube.com/watch?v=meJu96TGw5Y&t=694s)** are a customer, how does the customer journey look like? So here um for the example of um Renault, we partnered up with Renault and together launched um more than a year ago uh the first full V2G offering in Europe. It's working and it's in production. So V2G is not a dream anymore. Um first of all the person goes to a car dealer makes the decision to buy a car which also is capable of doing V2G. So charging and discharging. Then of course you also need to have the appropriate wall box which currently luckily is also um in the package um available. And then of course you also need the correct tariff. Yes, we could

**[12:25](https://www.youtube.com/watch?v=meJu96TGw5Y&t=745s)** also do smart charging for the customer with other terrorists just optimizing the charging of the car, but the users wouldn't get anything back from that. And that's usually well, you don't want to provide just an asset just for providing it and not getting anything back because still it's work on the battery. Um, it consumes a little bit of the lifetime of the battery and not getting anything in return for that. I guess that's also a little bit of unfair you could even say. And then the customer of course needs to activate V2G in the app. There are some settings. Then you need to set what is the minimum state of charge because it might be that there's an emergency at the school. You need to pick up your kid. The battery

**[13:13](https://www.youtube.com/watch?v=meJu96TGw5Y&t=793s)** would be drained empty. The car is of no use to you. um which would leave us with a lot of unhappy customers which would never again use V2G or something similar and therefore there's uh the minimum state of charge the maximum state of charge and also your departure time when you least expect to leave next and that's parameters we then operate the battery in and generate value both for the grid as well as also for you um with the asset [snorts] you're providing to the grid and then of course the customer even might charge for free in the future hopefully. We also have solutions for V1G where the then um here in Germany for example with

**[14:03](https://www.youtube.com/watch?v=meJu96TGw5Y&t=843s)** the Eon tariff um provide also options for people who just have VI 1G available and we all know Germany um we don't also have that many smart meters available which are also for V2G very very important you basically also have an app uh which then the back end our back end is the OP optimization of your charging sessions uh which also takes into account the prices at the spot markets and um all your mobility needs. So that's always the most important point for us if the customer becomes unhappy V2G vehicle grid integration VGI um V1G however you want to call it is of no

**[14:52](https://www.youtube.com/watch?v=meJu96TGw5Y&t=892s)** use. Um then we have the electricity tariff. Um because if we don't have a contractual relation, no one gets anything in return. And of course as a component also the flexibility or the bonus payout then. Um maybe a little bit on the um tariff. Um you know there are the usual German flat terrace but also dynamic terrorists. Um on the flat tariff you usually don't take the risk. Um you have something you can calculate with that's fixed for um until whenever usually for a year or so. On the dynamic terrace side you take the full risk. If the market goes crazy you can either earn a

**[15:40](https://www.youtube.com/watch?v=meJu96TGw5Y&t=940s)** lot or you can lose a lot. And our solution is well not kind of in the middle. It's still a flat tariff, but you get additional money paid back. So that's how we try to provide users with a risk-free approach to V1G and uh V2G. However, all in all, V1G vehicle grid integration V2G they pose a lot of challenges. Of course, the fear of battery degradation is real. Um however if you operate them within the boundaries um it is usually fine um the degradation is found to be not much more than they either way would be because you either way you would charge your car wouldn't you um I at

**[16:29](https://www.youtube.com/watch?v=meJu96TGw5Y&t=989s)** least would because I want to go um someday um so um there um the effect on the batteries are less than also anticipated and expected And uh on the other hand, however, hardware is currently still a problem. We have just a limited selection of E2G cars and car makers available. Also, the charger compatibility, well, it's not yet all plug and play. So, offerings like with Renault are still needed. It will still stay take some time even though there are standards like the OCP standard which usually should provide us with a little bit of safety. But as it is with standards, usually everyone interprets them differently. Then there's of course

**[17:18](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1038s)** the cost factor. EVs are still at least the European ones quite expensive. And regulatory, we still have a little bit of uncertainty. Luckily, at least in Germany, double taxation has been abandoned finally. Um, but the other downside in Germany still is smart meters. We're missing them. Um there are two ways basically to control the cars usually via the charger or via a mobile network. That of course also opposes challenges in data quality and frequency. You have to do a lot of data cleaning. Um we observed cars driving around in the uh streets um having a bug where it none said the car was charging which just wasn't true. It wasn't at

**[18:07](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1087s)** home. it was driving on the streets and the position data supported that and the driver as well. Um forecasting of course for us is very crucial and important weather forecasts how sunny is it going to be. Um that also has an impact on the energy prices and of course then the user behavior because the users well they are the most unpredictable thing to us um whether they unplug early or leave the car plugged for another 20 hours. That's not under our control. And then of course you need to um orchestrate the whole system all these distributed assets aggregate them and disagregate them again because also you have to fulfill what you promise on the market and then of course testing on energy

**[18:54](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1134s)** markets that's not very easy um because they are energy markets a lot of people take place you don't have a controlled setups and especially talking about a controlled setup you als also have home energy management systems which might intervene the decisions you took on the other end. So it's better to integrate them. Then lastly a little bit about our tech. Um how did we approach those problems? How did we solve them? And there's a plethora of technologies involved and yes it involves grasp python as well as also others um flutter mainly then also for the app. Um but for you probably more interesting is how did we tackle the optimization

**[19:45](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1185s)** problem actually how how do we think about charging? Well, we usually think in terms of boundary conditions um what we call the um polygon of charging flexibility. We take as inputs what the user gives us basically the minimum state of charge, the maximum or target state of charge and then we also need to think about charging and discharging. they might have different efficiencies and that's also what we need to model and this basically gives us boundary conditions in which we can operate. First of all uh it would be that the user discharges or the car discharges as soon as possible then waits and then as late as possible charges to the desired state. Now on the other hand side the

**[20:35](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1235s)** other boundary would be to charge as soon as possible to actually 100% then leave the car there and then go down via discharging to the target state and within that boundary we have a lot of flexibility where we then interact with the market and then try to optimize what is the best buy or sell decision to take and to make our hardware and not hardware, our architecture. Um we try to keep it tidy by splitting it into domains um which are quite um well um domains also in a business sense um to keep our services cleaned up. Um but also within the domains then choose the

**[21:24](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1284s)** technologies um which are appropriate for the task at hand. And um who of you knows OCP? Um anyone who knows the details about the protocol or at least roughly what it does? What? Well um the thing is OCP is a stateful uh connection opposed to what we usually deal with in the cloud systems um with stateless um connections. we have to keep the websockets open all the time. Um which of course well um Python is not the most suitable tool always for that. There nowadays um a lot of improvements in the most recent versions but that's the part where we said we

**[22:13](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1333s)** need Rust. We need something more performant which can keep a lot of connections open in parallel and process the data um in a speedy manner. um uh whereas all the rest um for us most of it is Python. So um here when we tried to control the chargers we ended up in a dead end kind of with Python we were quite well at least in terms of resource usage um meaning computing resources it was intense um and that's where we said we switch we switch to something which is truly multi-threaded um and that's where rust helped Um apart from well there were

**[23:04](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1384s)** some other things which also helped um the one lesson we learned there is um have a lot of tests that usually helps on such a migration project quite a lot. Um so if you ever transfer something to just build your safety net um having a huge test coverage makes that usually quite easy. Um it was a huge project but um with the safety net um we had nearly no regressions at all. Um so if ever you're in the same position think about first invest that time into your tests and then do the migration. Don't do the tests while migrating. That will just screw you up. Right. With that, um, thank you for your

**[23:55](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1435s)** patience. Thanks for listening. And any questions? [applause] Um, thank you Christopher for the nice presentation. Um, you mentioned you have also some optimization problems and I went I went to Gorobi before and I think they all in on optimization. So maybe there could be a collaboration between you guys. We actually um have also people who worked a lot with Groi in the company. So they are known to us. [snorts] Um okay. Um so let's proceed with the questions. Um so you mentioned um people are certainly an uncertainty factor in the whole system. So the first question is how to prevent that early in the night my car

**[24:44](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1484s)** charges my neighbor's car and later in the same night my neighbor's car charges my car back. Well um I'm not sure whether that's a nightmare. That's how markets work. Um but indeed uh considering it from an energy uh well from the degradation perspective um it's not nice. Um what we do there we have certain cycling limits to prevent this uh feedback loop from appearing. Um so we try to just have one I think it was one cycle a day or so at most. Um so we reduce the cycling time and thereby these feedback loops um between neighbors. >> Okay. Um, second question. If everyone in Germany is having a V2G car with the

**[25:36](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1536s)** same similar algorithm to determine when to charge and to discharge, how does the algorithm determine which cars to charge discharge? We currently prioritize them actually by the departure date um plus then also the boundary conditions which uh were shown right here because you know where you are in the time frame. So from uh from left to right you have the time and if you then are at this dead end where you just have to charge then it's for us something we have to fulfill kind of now. So >> okay. Um are there any studies on the impact of vehicle to grid on the battery lifetime and what hidden costs

**[26:26](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1586s)** um this is equal to? Yes. Um they are uh and if I remember correctly um the um degradation um per year is actually less than a percent um from the additional V2G cycling. Okay, thank you. Um are there any other questions in the audience? connection between what? >> Mhm. So basically uh the question was um

**[27:20](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1640s)** what's the connection here between the chargers and um our um cloud applications rest applications and the charging stations are connected usually via LAN or wireless LAN um to the internet and um then it's a websocket connection to us and the protocol they are speaking is um OCP uh usually >> the other thing about business site how can your company make profits from VGG offer >> yeah so uh we profit a lot from them selling and buying energy at the right time so currently that's a time where you should buy energy it's sunny outside we have a lot of production and then usually manage the charging such that we

**[28:09](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1689s)** would discharge charge when people get home. Um, and their energy prices are usually higher because people turn on the TVs, washing machines, everything and consumption usually then rises up. Okay, thank you for the talk. Um, those V2G cars such as the Renault one, can they also be used to directly power stuff in my house? >> Yes and no. Um, so that's then what's called vehicle tone. Um, the thing is if you discharge your car, usually you don't have so much control over where does the power exactly go in the system. Um, that's just physics. Um so that's

**[29:00](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1740s)** hard. Um however with a home manage energy management system um you have better control and knowledge about what is going on in your home because for us currently in the state we are in um that's the missing piece of information. Um we have um we just have the final output of the smart meter. Um and that's usually it's just a guess what is going on in the house and um to um make better predictions you would need to disentangle PV from the car uh and the other stuff to then say okay wait he's going to come back at 8 then we discharge the car so you have an at zero consumption but it's in the works. Okay, thanks.

**[29:51](https://www.youtube.com/watch?v=meJu96TGw5Y&t=1791s)** >> I think our time is up now. Um, but I guess because House Energy is also sponsored, you also have a booth. >> We are there. Yes. >> So, please go ahead and meet them in person and ask your questions if there are any more. So, thank you very much and yeah, see you around. >> Also, thanks for my help. [applause]
