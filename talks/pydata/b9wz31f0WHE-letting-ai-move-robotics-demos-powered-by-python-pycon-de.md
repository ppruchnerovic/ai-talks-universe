---
id: b9wz31f0WHE
title: "Letting AI Move: Robotics Demos Powered by Python [PyCon DE & PyData 2026]"
slug: letting-ai-move-robotics-demos-powered-by-python-pycon-de
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Larissa Haas", "Annika Herbert"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:21:52Z
video_id: b9wz31f0WHE
url: https://www.youtube.com/watch?v=b9wz31f0WHE
youtube_url: https://www.youtube.com/watch?v=b9wz31f0WHE
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Letting AI Move: Robotics Demos Powered by Python [PyCon DE & PyData 2026]

**Larissa Haas, Annika Herbert**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=b9wz31f0WHE) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Larissa Haas and Annika Herbert demonstrate how to use Python and robotics to transform abstract AI concepts into tangible, interactive experiences.

Speakers:
Larissa Haas, Annika Herbert

Description:
Robotics provides a tangible medium to demystify artificial intelligence, transforming it from an abstract black box into customizable software. By utilizing the Reachy Mini, a collaborative project between Pollen Robotics and Hugging Face, developers can create physical manifestations of AI that encourage curiosity and technical inquiry. The Reachy Mini Lite version operates via a wired connection to a notebook, while the wireless version integrates a Raspberry Pi for local computation. The hardware features a wide-angle camera, a four-microphone array, speakers, and nine servo motors enabling six degrees of freedom for head movement.

The system is powered by a Python SDK, allowing for the development of custom applications and the integration of external APIs. Practical implementations include a conversational interface connected to internal company systems and a mental warm-up tool for workshops that utilizes local file storage. The robot can also execute specific Python scripts for tasks such as taking photographs or running a hand-tracker that recognizes finger points and responds to waving.

Key takeaways emphasize that physical interaction changes how users perceive automation. In tests with children, the robot was treated as a social peer rather than a utility like Alexa, leading to spontaneous multimodal interactions, such as showing Lego figures to the camera. Furthermore, using a physical robot allows developers to treat system failures—such as connection errors or latency—as educational moments to explain the underlying mechanics of AI. While the wireless version offers an accelerometer and better audio hardware, it is limited by battery life and the computational constraints of the onboard Raspberry Pi.

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

*2,673 words · source: supa (sv, exact timings)*

**[0:06](https://www.youtube.com/watch?v=b9wz31f0WHE&t=6s)** Thank you Lara. Thank you for the introduction. Thank you that you all here. I think we very excited about this slot because it's a little bit also out of our comfort zone. You will see in a minute why. So we are here to talk about how AI gets things moving and not in the metaphorical way but in the real actionable thing you can see on the table. exp AI don't maybe do short surve hand AI looks like okay one okay raise your hand AI looks like this

**[0:54](https://www.youtube.com/watch?v=b9wz31f0WHE&t=54s)** for you okay this is clear majority and I think this pretty Ai when you think about daytoday context in business context always like this weird chat window that you have somewhere and you type stuff in and you get response back you don't know where it comes from you don't know what is happening in the background and kind of a black box that lives somewhere and I think like we pretty technical audience but most of the thinking about taking into account

**[1:44](https://www.youtube.com/watch?v=b9wz31f0WHE&t=104s)** AI is not black box AI code AI software customizable code. exp AI show AI can maybe change expectation AI AI do AI also here sparkly star thing you know okay something intelligent happens but I don't know what exactly or sometimes this diamond symbol that you can see on some apps A supported features happening. Ja explanation

**[2:46](https://www.youtube.com/watch?v=b9wz31f0WHE&t=166s)** create more tangible use exp AI and maybe also raise the interest in how AI actually works under the hood and this works really well with cute Larissa Anik not robotic experts like half year ago I had no idea about how to use this thing to let it move or how to move antennas or I don't know. as data scientist as solution architect

**[3:36](https://www.youtube.com/watch?v=b9wz31f0WHE&t=216s)** to explore this kind of context this kind of thing to ja get some ideas how to how to see AI differently and this is exactly how we went so as I said we had no context or no background in robotics we saw reach It was really nice. It comes in a box together like screwdrivers all the cables inside all the electronics when it actually wakes up the first

**[4:23](https://www.youtube.com/watch?v=b9wz31f0WHE&t=263s)** timeol experience. It just looks at you with big eyes and just nice so cool to see it. when we show to others this excitement actually is also happening in others like everyone who sees this waking up the first time [skratt] so yeah we saw hey this is a really cool opportunity to raise interest to get people engaged so we started thinking about how to include it in which situations we can use it will experen and I hand over.

**[5:14](https://www.youtube.com/watch?v=b9wz31f0WHE&t=314s)** Thank you. So first of all as already mentioned this is Rich. Actually it's a Rich mini and it's produced by a collaboration between pollen robotics and hugging face. There are two versions of Rich. One is wireless and one is the light version. What you can see here is the actual light version of Rich and really we ordered both of these versions and we tested out a little bit so you will hear little bit about experiences with the wireless rich later. But yeah, credit credit pollen robotics and collaboration between Polotics and Hugging Face.

**[6:01](https://www.youtube.com/watch?v=b9wz31f0WHE&t=361s)** creating so I don't go to deep into spacks but maybe I talk a little bit about capabilities of R so the Rich wireless has wifi and the Rich light does not the Rich wireless also has a resp inside which is doing all the computation compu running locally connected cable notebook here to try out you don't actually need physical robot you could also use the

**[6:51](https://www.youtube.com/watch?v=b9wz31f0WHE&t=411s)** interface that you can see here and just simulate what you have you want Rich to do or what you have programmed All the microphone inside array of microphones so it can record your voice and then it has also speaker so it can actually respond to you play music actually if you connect it functions like a speaker to your actually actual device and it has a wide angle camera which is curiously sitting between both of those eyes motors antennas antenas and all the motors move in degrees of freedom it can shake head can

**[7:42](https://www.youtube.com/watch?v=b9wz31f0WHE&t=462s)** not head it can roll to the sides and then all angles actually can x y and z axis can be moved Ja, this is to simulate to to sample for you. Okay, [harklar sig] then how does it work? So there is in there is an app you can use and you can search for discover apps from this kind of store looking platform and you can download these apps to for to ja use the features of and it's

**[8:32](https://www.youtube.com/watch?v=b9wz31f0WHE&t=512s)** pollen robotic space on huging phase. So these are you can access all the prebuild apps but then also we have created our own little app. based on a template that we modified and with our own little app we have implemented our innovation factory. So we could ja call our own API and then Rich can use access our innovation factory via the API and answer based on such prompt like this. And then we have also implemented a warm up tool which stores the information locally in a file. So Rich can access the local store and then

**[9:20](https://www.youtube.com/watch?v=b9wz31f0WHE&t=560s)** act upon that. Our warm up tool is actually for mental warm up before some kind of workshop is happening and Rich is then guiding us through the warm of exercise. It's quite fun I can say. Okay. Also Rich comes with the whole library of Python library which you can access. For example, here little short code snipp that would take a photo actually. So you can use this library to code your own little script and create different things and applications. So what you see here today is only a start there are no limits. You can implement your own use cases. You can't you don't need to

**[10:09](https://www.youtube.com/watch?v=b9wz31f0WHE&t=609s)** implement like we did some kind of conversational interface. You can use reach for everything that you can imagine and very very fun. Ja. So you would run your own demon with your own scripts if you want to. Ja. Yes. So what did we experience with using this little robot? And I can tell you maybe a story. So some days ago there was the Eastern weekend and I was visiting my family and I showed Rich to my two little nephews three and seven and they are big Star Wars fans. So I

**[10:59](https://www.youtube.com/watch?v=b9wz31f0WHE&t=659s)** created a persona that is called Pebo. is a Star Wars astrodroid and knows everything about Star Wars. And I was very very curious how my nephews will interact with it actually because they are also very into tag. They have an Alexa in their children's room and they know how to interact with that Alexa. They can play music. They have those Tony boxes. I don't know. So they have a lot of technology to interact with and they just use it in in their daily. Ja everyday basically. So I expected that they will use people just as using

**[11:48](https://www.youtube.com/watch?v=b9wz31f0WHE&t=708s)** Alexa shooting questioning he can turn the light I don't know trying stuff but actually surprised me a lot rich or was not seen as another Alexa they actually behaved as people would be another child and they >> [skratt] >> on uses camera moving reacts head movement antenna movement and then they wanted to know okay how does it feel does it react if I touch it and then they interacted with it just

**[12:38](https://www.youtube.com/watch?v=b9wz31f0WHE&t=758s)** like with another slowly about Star Wars responses back then smaller one ran away went into his room and got small Star Wars Lego figures and brought it and showed it into the camera and said, "Hey, do you know what this is?" I have never thought about doing that and it worked like multi multimodular model running under people saying really nice as droid you have here so very precious toy and was really because I haven never thought about

**[13:27](https://www.youtube.com/watch?v=b9wz31f0WHE&t=807s)** this way of interaction the whole afternoon [skratt] that dinosaurs discussion dinosaurs stars fit together and what kind of what color of light saber would dinosaur stuff like that. really really interesting and also the bigger one then said hey where did you get it and I said yeah build it myself you can see here the cables and he could also see the code running and we immediately had a discussion about okay how does this actually work okay connected cable running on my machin machine

**[14:15](https://www.youtube.com/watch?v=b9wz31f0WHE&t=855s)** telling the robot what say what to do how to react I want to ja to know how works how to get hey can help you the next time I guess really nice really nice way to get the interaction going work >> [skratt] >> couple of examples like experiments with children herecture actually took Lego figure

**[15:07](https://www.youtube.com/watch?v=b9wz31f0WHE&t=907s)** we also had it in work context in customer workshops as Anik just explained we used it as an ice breaker to to introduce ourselves. Python we were able to connect it to different api. Quick way to interact with R actually because it takes some time for R to

**[15:57](https://www.youtube.com/watch?v=b9wz31f0WHE&t=957s)** understand and process into API call everything back use as voice interface for all kinds of automation ag whatever you and exper you see automations because type in into machine screen okay something happens to when an action physical object is reacting to that input and is reacting to you moving around actually answering questions. So before No, we go to the demo now, right? Okay.

**[16:48](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1008s)** So, let's try just some things out and I will quickly change my das one. Okay. Okay. So here you can see the interface. I can make it bigger unfortun quality. here app store preinstall for example maybe start handcker the logs okay

**[17:39](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1059s)** so kind of confused because so many hands >> [skratt] >> Okay. So I maybe go here, maybe show my hand. You can see the points that recognizing. You can wave it. It will wave back. >> [skratt] >> Okay, this small thing alone is so much fun when you just playing around with it. Okay, sometimes I have no idea. [skratt] There are also couple of games like red light, green light. You may know it from

**[18:29](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1109s)** Squid Games. It's not as evil. conversation app undering jaing pattern so let let me stop appion Okay, let me start the local demon. It's now a different one, you know. And maybe we can start people. I don't know. Maybe you w have some interaction

**[19:20](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1160s)** with the Star Wars astroid. Hello people. This is the demo effect. Ja. tools with it prebuil for example the dance module which is not working but normally it maybe let me just start the

**[20:11](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1211s)** started another try hello pibo >> [skratt] >> Maybe he shy. Yeah, I think I think shy. Okay. So, we can do something else. We can actually take a crew picture because

**[20:58](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1258s)** that would be really nice. scripten. So here will make it a little bit bigger. So just what you have seen in the presentation and I can just let run. Nice. [fnyser] Okay. So the demo god is not with us today. But maybe we can do the question round. See if the standard conversation app

**[21:47](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1307s)** will start. Actually, >> we still have a slide. >> Oh, we still Oh, true. We still have a slide. Thank you. >> So, [skratt] over to you for the last slide. No problem. Okay. So, quickly great. So, we treat failure as part of the explanation like you saw now we can see the logs and we can explain to anyone who asking people who thought that AI would be a black box. Can we can show he shivering a little bit might some kind of connection error when he goes offline with wireless rich where we had some connection instability he just shuts down or he stops responding in the midst of sentence we can use this failure to

**[22:37](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1357s)** explain AI to people that are not tag native and people like Lar nephews [fnyser] who might just be curious about it. And then as you can see small actions are actually very impressive already. So you don't need to have a big agent running in a background. big long answer that elaborate even having moving around waving a little bit taking a screenshot taking a photo. It's very very impressive already and it makes people curious about what is happening and curious about what is AI actually doing in the background and it makes the behavior of AI a little bit more elible. So you can

**[23:28](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1408s)** explain yeah it's tracking my fingers there is you can see the points where it's identifying what is a hand and this is very helpful when talking to people that are not very into AI and have not experienced AI as we have and therefore it is designed for curiosity for people to ask questions a little bit more for us as experts in AI finished. >> Yes. Thank you for your attention. Zvanta robotics

**[24:15](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1455s)** software consulting partner sa doing AI interest let us know but of course are any questions so feel free to ask us any questions and meanwhile I will try and set up the conversation first of all thank you so [applåder] Ok, [applåder] we got five minutes and I'm gna go first with the high with the voted questions. So, how did you get your boss to pro the expense to buy it? [skratt] That was actually not that hard. link

**[25:10](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1510s)** expensive [skratt] like every year we have small internal right before Christmas before that we just brainstorming what we can do in heckaton kind of useful but also kind of fun so this wason proesome How can make adult? So it has a children mode actually conversational app that is that has children mode that is also not sending images to another like to external service using the local image processing power

**[25:57](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1557s)** to process the images. So of course when you design your own app you have to be you have to be careful about it but like when when I first got it at home my my mom also was like hey how are you making sure that it doesn't spy on you and I was like yeah so I'm sure that this is not spying on me because this is like python on my local machine. over technology. Let's have a follow up actually on this. How did you audit your project for GDPR and AI compliance? [skratt] >> Sorry. Can I postpone? >> Yes, for sure. [skratt]

**[26:45](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1605s)** >> Ehm, can Rich call your houseverwaltung? Heing Korean right now. >> I don't know why. Sorry. What was the question? >> I'm from the future. I'm talking call my house my houseverwalting maintenance. Ja. >> Ja. >> Cool. >> Ja. >> Ja. >> Ja. Okej oke >> we can try it out. Someone wants to give his phone [skratt] >> and can reach recognized faces. >> We can we can ask the question to Rich.

**[27:33](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1653s)** What was the question? Go ahead and ask your question. Rich can you recogn faces? FA what are the drawbacks wireless in okay so you might recognize a standard way of interacting just like you would expect standard LLM kind of prompting like conversational app doing the drawbacks of the wireless version like it has

**[28:23](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1703s)** its own power source which is limited so like the cable you still need to take with you if the wifi is bad it gets limited computation power computed inside Raspberry so might problem if running very convoluted software on pros so the camera is way better I think the speakers are a little bit of more high quality so yeah pros and cons wireless exclusive expensive version

**[29:17](https://www.youtube.com/watch?v=b9wz31f0WHE&t=1757s)** wonat [skratt] Larissa. >> [applåder]
