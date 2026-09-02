---
id: m0WGHOnAxmA
title: "Python Takes Root in Robotics: ROS 2, Simulation, and Reinforcement Learning"
slug: python-takes-root-in-robotics-ros-2-simulation-and
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 49
published_at: 2026-08-23T07:00:36Z
video_id: m0WGHOnAxmA
url: https://www.youtube.com/watch?v=m0WGHOnAxmA
youtube_url: https://www.youtube.com/watch?v=m0WGHOnAxmA
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science", "Multimodal, vision, speech & robotics", "Training, fine-tuning & model building"]
transcript: true
---

# Python Takes Root in Robotics: ROS 2, Simulation, and Reinforcement Learning

**Speaker not identified**

`PyData` · `PyData` · `2026` · `49 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=m0WGHOnAxmA) · [Conference site](https://pydata.org/)

## Description

Welcome to the PyData & PyCon Yerevan 2026 video collection - our biggest edition yet, held on 24-25 July in Yerevan, Armenia.

From data science and machine learning to Python tooling, production systems, research, and open-source technologies, these recordings capture the ideas, experiences, and practical knowledge shared on stage.

🌐 Website: https://pydata.am

📅 24-25 July 2026 · Yerevan, Armenia

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*5,557 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=5s)** Yeah. Hello everyone. I'm um Vasov and uh I will speak about robotics today. Uh if you if you was on the last session uh last uh question was about what we will we will build after we built all our harnesses and so on. uh and I think uh I have somehow answer uh about that. Um so uh first of all we have uh not perfect environment and uh uh not perfect uh uh uh solution for my slides. I have uh QR code with PDF. uh you can open this presentation on your phone or or your laptop and uh it might be better

**[0:57](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=57s)** to see slides. So uh little about me I am Vim Batov. I am team lead at Yandex. Uh now I'm working on deep research solution for internal internal Yandex data. It's about uh uh uh AI agents harnesses and so on. Everyone works on harnesses. I'm too uh before that I worked on Yandex mail and Yandex disc uh here in Armenia and worked on delivery solution for uh Yandex delivery and outside Yandex uh interesting uh uh projects like afternoons racing and uh blood analysis automated blood an blood analysis

**[1:44](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=104s)** uh so I work on uh some harness harnesses and some automation but my hobby connected with robotics uh and uh today uh I will uh speak about some basic things uh uh you can uh it's about robotics and uh how you can start to work with robots today uh but uh tomorrow uh will be more uh hardcore uh speak about speech about uh delivery robots and some um uh on age computation and today some basics how you can start with robotics. Uh my agenda today is uh the first part it's about uh how you can use Python and

**[2:34](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=154s)** how to you can communicate with robots. Uh second part it's about how we can control and uh what uh uh simple instruments do we have in nowadays. Uh third part about it's about simulation. What if you do not have uh uh robot and hardware? Uh what you can do. Uh fourth part is about u reinforcement learning. Uh it's uh some common way how to robots uh learn how to do things. And uh uh last part it's about what you can start doing right now. Uh as you noticed I have some setup on the stage. Uh little bit about that. I have my laptop uh my it's a basic

**[3:24](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=204s)** MacBook. Uh I have Raspberry Pi sitting here. Uh and uh uh it's connected uh through Wi-Fi. Uh and uh uh on USB I have uh some uh hardware. It's Richie Mini Robot. Uh so no cloud no master uh no master nodes uh everything connected through basic Wi-Fi uh and u um and that's it uh no complex solution uh how you can uh communicate things right now under the hood we have a DDS uh it's a data distribution uh uh oh I forget the >> [laughter] >> uh data distribution system I don't

**[4:14](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=254s)** remember last s uh so it's uh protocol uh above uh UDP uh and uh uh very reliable uh revival um so reliable uh uh standard uh in uh industry and internet of things. Uh so about my hardware, it's Richie Mini from Poland and Hugging Face. Uh it's uh six six uh degree of freedom uh steward platform for the help for the head. Uh rotational body with two antennas. Uh so motor for every antenna and for body uh nine motors uh total. Uh it has camera uh for mics and the speaker and it's uh

**[5:07](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=307s)** absolutely open source. You have a specification for body. You can 3D print it. Uh and all SDK and all software connected with the robot is also open source. Uh price uh um $300 for light version. uh light version uh because we have only uh simple controller for the motors inside the body and we need some brains outside robot uh for my case it's Raspberry Raspberry Pi 5 uh connected with the robot so uh what we can do uh robot uh with our basic Python okay uh robot it's a massively

**[5:56](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=356s)** distributed system every robot has some uh server uh serve motors uh have some sensors uh uh have control if you have number of robots uh uh number of things do we have to control to communicate and so on uh different rates different SDKs different languages and uh we need something to uh uh some system to communicate and to connect all all of that Uh so we need some hard of middleware uh to have communication and some and uh we have one with uh uh convenient uh Python app uh it's called ROSS uh we have second uh version of it robotic operated system uh it looks like uh some uh uh uh micros

**[6:46](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=406s)** service architecture so we have not uh as a micros service some um thing uh which uh work with one uh one business uh uh business item uh and uh we have a topic it's pops up uh publication subscriber uh pattern uh with messages uh uh some message broker or or event bus uh we have a server service it's about uh synchronize u uh remote procedure calling and action It's longterm uh actions are synchronous with process and which can be cancelled uh parameter it's not about the parameter it's some runtime config which

**[7:35](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=455s)** we can uh uh which we can uh edit on the right time uh but it's not very important so yes and we have uh DDS under the hood uh uh that as a transport uh uh that uh connect everything uh together. So uh Ross uh have a C core C writing on core. It's a robotic control library and the thin language libraries uh for right now it's two languages. It's C++ and the Python. So uh two official clients and the Python and one of them. So everything uh which uh you can use in C++ you also can use in Python uh uh not

**[8:27](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=507s)** exec executors QNS uh quality of service and life cycle uh and uh you know if you know Python you can uh uh communicate with robots on stage. So uh test demo um it's about topic uh topic it's some event bus uh with stream of messages uh and uh uh everyone can publish anyone can subscribe and uh uh you can uh read something about state of the robot uh our robot con uh constantly push some uh state of the motors and uh uh head position and so on. So um some basic idea how to write Python code on ROSS. Uh we have a note

**[9:18](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=558s)** uh we make class listener we in it something something uh in terms of of ros we uh create subscription uh interesting things about interesting thing about um joint state it's object uh typed object about uh uh state of the robot or joints of robot um and uh uh we and create subscription and in my demo I uh simply log uh something uh uh on the console so some initialization and uh spin it's uh some loop for uh for that listener so let's try to do something.

**[10:17](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=617s)** Yeah. And uh we have a lot of messages. Our robot push uh messages uh to a network. Uh and I have a two nodes, one on on my laptop and one in Raspberry Pi. uh robot push uh pushed some uh uh state of the robot and uh I subscribed in on my laptop uh so I can uh u know something about this robot. So yeah um oh what's going on? Yeah. Okay. So, and right now I would like to do

**[11:08](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=668s)** actually something to control the robot. Um, first of all, we have a service uh uh predefined services uh in robot. It's some kind it's uh uh syn uh remote procedure call uh one short comment uh with some answer. In this robot, we have some useful wake up, sleep, and another motor uh enable motors. Uh and I would like to wake up uh this uh reach mini. Uh also uh some basic idea how to do that. Uh we create note uh we create uh client we call trigger uh and we uh uh print some response uh of this action or the service.

**[12:09](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=729s)** Oh, lost connects to the server. Oh, what's going on? Sorry, >> I lost connection. Okay, not stable Wi-Fi here. Uh I think uh

**[13:05](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=785s)** >> I have a case [snorts] Oh my god. >> Is it friendly?

**[13:57](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=837s)** >> I guess so. >> Yeah. Okay. Uh we have success. Uh we have message. Uh I don't know. Yeah. >> Yeah. Uh we have success. Uh true. And uh message that uh robot waked up. Okay. Uh uh yeah. Uh and uh the next one I want uh some some moves. So I want more control. Okay. Um yeah and uh topics works in both way. Uh you we can read messages

**[14:48](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=888s)** and we can send messages. Uh so we can stream uh some uh message to uh make some movements of the robot. Uh basic idea we have a head pose uh and uh we make some uh post stamped uh some position of the head uh some properties of this position and we push it uh to the robot. Uh yeah. Uh we may we make some uh one pose to rotate 60° or we can push uh every move every degree to the robot to have a more more control and uh uh make some changes in runtime. So we can start to uh rotate clockwise and uh make

**[15:39](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=939s)** another decision and go back and and so on. So it's to approach to make some things. Uh so let's try to do that. Oh, wake up. Um yeah. Uh, so we can push some messages uh to to the robot and make some movements of uh of head. Um, okay. So we have some sensors inside

**[16:30](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=990s)** this robot camera and it's also uh the uh message message type. So it's uh uh objects and we have uh we saw John state post uh uh post temp and right now we can work with compress uh compressed image. Um yeah and you can subscribe for this message uh from laptop or some another device to make some decisions about what what we can see on the images. So make some uh computer vision and so on with something with GPU maybe in cloud and so on. So uh how uh in my setup uh uh camera works uh we have I camera in the

**[17:21](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1041s)** robot uh connected through USB to Raspberry Pi. So we have some stream video uh to the uh which we pre-process uh on the on the pi. Uh I have some pre-processing uh to make uh compressed video from from the stream. I have a topic with compressed images uh image uh uh with uh 10 frames per second and I have I have subscriber on the laptop with some open CV uh wrapper to show the the image show the picture uh it's it's just a message so pops up also works and uh you can make some pre-processing and whatever you want uh compressed uh images for this Wi-Fi

**[18:12](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1092s)** because we have some problems with that. [snorts] So yeah, basic idea of subscription uh we have a ROS note uh we create subscription for compressed images and some uh uh some method for uh for processing of the result of the message from the topic. Let's try to do. Okay. >> Say hi. [laughter] So, we worked uh we worked with camera on my laptop. uh my laptop

**[19:02](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1142s)** doesn't know uh don't know anything about what's going on with camera inside the hardware and I work only with messages of compre um yeah I will close it um yeah and uh what cool uh what about some complex movement We have a a body which can be which can rotate uh which can be rotated. We have a connected head also can rotate uh and uh what if I need some uh complex move when I want to uh have camera uh steady and rotate body

**[19:52](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1192s)** and uh and head sim simultaneously. Um we have some uh additional li uh libri for that because uh body and head have have frame of the coordinates and we need to uh sync them uh uh angles and speed and we need something uh which can be useful for that kind of calculation. So we have a TF2 it's a basic idea uh and uh code some some more complex uh but uh we can uh we have some library which can be useful for that kind of uh calculation. Uh the uh yes we have a basic link it's

**[20:44](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1244s)** um stand of the robot uh body can rotate it and uh uh um head rotated and we need uh keep angle of the camera relatively to base link and we need some calculation in between. So let's try to do that. we have a camera uh angle of the camera in uh in a frame of the world. So or base of the robot and we have uh coordinates of the uh

**[21:34](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1294s)** body and the head in the in the messages. So it's not perfect in terms of uh value of the angles but uh you will see that uh you you can see that uh we have a 30 uh degrees of the body and the all and the and of the head. Okay. So some complex movement and uh we can control it uh uh with some basic programming skills with the Python uh and uh we have a action action it's the last part of the uh of the instruments uh that we have to communicate with the in in the robot world. Uh it's long running job uh uh with a goal and feedback stream. Uh how

**[22:25](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1345s)** we proceed to the goal and we can cancel cancel it uh in uh uh we can cancel cancel it. Um so yeah uh how we can work with the actions uh uh we can we create uh client we uh set a goal something some name and we send uh this goal to the uh topics uh to run some some longterm action uh uh on the hardware. Let's do some dance. [laughter]

**[23:22](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1402s)** We have a progress here. Um yeah and uh action it's a good uh way how we can control where we we do calculation because uh one way we uh push some uh lowlevel messages just about every move of the robot of the every motor of and uh every joint of the uh robot and another approach when we uh make decision on some brain of the robot

**[24:12](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1452s)** in Raspberry Pi and uh make some goal which we can call from some uh master node or some something. So it's balance between where we do calculation on the row on the hardware or maybe in the cloud or where we have more resources. Uh yes and in in this stuff I move all everything to the pi because we have we do not have stable connection for that. uh another building blocks uh which we have in uh ro in the robotic operating system uh um it's nap to move it uh at the gaze s bridge and tf2 which I uh talk about uh navu it's uh about navigation uh so

**[25:04](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1504s)** drive uh from point A to point B and the interesting thing that uh in terms of uh uh the main it uh uh makes in uh terms of pose. So uh in this robot we have pose of the head and uh in robot with uh some wheels we can make the pose uh of point B. So it's some kind of same domain with same uh actions and we uh can uh do programs with with the same ideas. uh move it. It's about uh how we uh it's about kinematic uh direct and uh inverse kinematic when we have connected joints and we need uh uh and some actuator like

**[25:53](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1553s)** uh uh grab in robot arm and we need to move uh this actuator to some point in in space and we need to calculate which uh angles do we need in every joint. Uh so it's about make this calculation how to uh make this kinematic. Um and uh also uh it uh library has a collision uh collision theme. So we uh on a scene we have can have some uh what's going on? Okay. [laughter] uh so and uh we can we can work with collisions.

**[26:42](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1602s)** CV bridge it's a library for uh for working with images and I have some basic demo but CV bridge can be connected to open CV and make some uh more complex stuff uh and uh interesting things it's universal robot definition format it's some XML format uh which define uh physics and uh some shape of the robot uh and uh if uh uh if manufacturer of the of the robot provides this kind of thing uh and uh some some popular platforms do it. uh we can use this format uh for uh um

**[27:35](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1655s)** um some visualization and more interesting we have we can use it in simulation. So we have format uh uh and we can put our robot in simulation with help with one one file and one format. Uh what do we have for simulation? uh Gazea it's Ross native uh uh simulator with uh physics and with uh uh good support of the Ross uh Mujo it's more about um reinforcement learning and uh more uh fast and uh but we without uh uh complex physics and uh the most powerful uh invidious club uh thousands

**[28:28](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1708s)** of robots very complex scenes and uh with uh with purpose of automation of huge warehouses with the thousands of robots but you need to uh you need to have a lot of GPUs for that. Uh so at least uh uh six at least 24 or 32 GB of video memory. uh in in in one GPU and uh for for one robot and uh you need a lot of uh computational power to work with that but very powerful and very um uh complex physics because of uh Nvidia and uh gaming experience uh but uh need a lot of resources um gazea it's most

**[29:23](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1763s)** ros native way to work with simulator, you run world, you uh allow your robot uh with RDF format and uh you have a gross uh JZ uh bridge uh to have some topics about what's going on in your world and with your robot and uh you work with the topics and not uh uh in the same way uh as you work with your hardware robot. But uh in the purpose of this demo, I chose Magiko because uh I do not have a lot of resources here and I need some basic uh visualization. So let's make dance in simulator

**[30:14](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1814s)** [snorts] and we do not have nothing. Maybe by >> maybe It can be because of the Okay. I don't know. Um okay

**[31:07](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1867s)** uh you can try it after my speech with my code. Um yeah. So uh and how robots can learn something uh in in real world. Uh I think I guess everyone knows uh something about reinforcement learning. uh but uh in a basic we have some uh observation of the of some environment in in this uh in my in my case it's joints and pixels from the camera we have a policy some uh uh some network which can make some decisions we have action uh rotate the motors of or uh or makes something in in this environment

**[31:58](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1918s)** and and we change environment And uh we have uh we make some observation and we have reward how we uh how we close to our aim. Uh we have no label data only uh some function of the reward and observation of the environment. So we uh and we may may have may have some millions of simulation of this policy and neon and our network learns how to do things more efficient in terms of uh reward. So basic stuff uh and uh uh we have a lot experience with the reinforcements learning

**[32:46](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=1966s)** and now in uh in the real world uh robots with the help of reference learning uh have may do some uh complex stuff like uh parcel sourcing, picking up and storing. Uh we can we have a human that's who can run and makes acrobatic things and uh we have some sidewall delivery with our cute brothers. uh so everything of that uh um uh making with the reform learning and uh it's uh now it's basic way how to robots uh can learn new things uh reference learning have a good uh instruments in Python and uh I guess we

**[33:36](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2016s)** know something about gymnasium it's basic things uh how to do environment and some uh some lefence learning uh basic idea very few strings of the code in Python and huge world how you can implement something interesting in a simulation uh with with this approach and uh interesting thing that with uh uh URDF uh simulation and uh that's uh and uh approach approach when you can use raw specific topics and nodes in the simulation. It's uh uh way then you can uh do your policy uh in the simulation

**[34:24](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2064s)** and deploy it uh in uh in hardware and use the same code with the same nodes and same topics in the in a real uh robot. Yes, you you have to do some domain randomization in environment uh because uh real world more complex than simulation but it's uh working way how you do basic stuff uh with some basic uh uh moves and decisions uh in the simulator and uh uh take this code deploy to the uh to the hardware and make some tuning uh only tuning uh uh do on the expensive and uh uh slow hardware on the real in the real world.

**[35:15](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2115s)** Um so what you can do right away um Python is enough to working with with robots. You have robotic operation system uh uh as a playground with a lot of libraries which which can use right now and uh robots it's not so expensive uh rich mini uh open sourced and uh $300 and uh it can be shipped in Armenia uh free country I love it um and yeah you can install uh Ross uh through cond uh if you work with uh some data stuff uh cond I I think you uh uh know how to do that. Uh in my repository you can find

**[36:05](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2165s)** some examples how to work with uh vi and um I also have a simulator and uh uh um file for riches. So you can uh do some things in simulation uh uh with this code without the hardware. Um so your Python uh today have uh you you can talk with the robot today and uh yes last things but my robot already sleeps. Uh yeah uh >> maybe can wake up and then sleep. >> Uh okay. don't have a connection. >> No,

**[36:52](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2212s)** >> maybe let's try it. >> Yeah. >> So, thank you. [applause] >> Amazing. Thank you. Do we have any questions? Lots of questions. You open the microphone. >> Yes, of course. >> Thanks for presentation. Actually, it's truly amazing especially work with robots. It's always exciting. Uh I'm not sure about the role of the Raspberry Pi. Uh am I right in thinking that all these

**[37:41](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2261s)** mean sensors connect to to the Raspberry Pi, right? and then sharing uh data using I mean Google message broker here. >> Yeah. Uh we we have not uh uh expensive controller inside the robot and uh there are streams of the sensors uh from the robot to the Raspberry Pi through USB. >> Mhm. and uh yeah has some pre-processing of the processing of the streams for sensors you have to do in the brain in the Raspberry Pi >> and commands you you push directly to uh message broker into Raspberry Pi and some of some of >> I have two nodes one one ROS node in the Raspberry Pi and ROS and the node in my laptop and I communicate only between

**[38:30](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2310s)** the ROS nodes in in my demo. >> Mhm. So I have communication uh within the ROS and some uh SDK and preprocessing of streams in the Raspberry Pi which can which have uh bridge from SDK to ROSS in the Raspberry Pi. So my laptop does not anything about rich mini hardware and streams uh within the robot but only knows about Ross nodes topics and the messages from from the ROS. >> Mhm. And Raspberry Pi here connected with your laptop using Wi-Fi, right? >> Yes. Yes. >> Okay, cool. And um about the message broker, right? Is it kind of I mean Kafka or >> it's DDS it's uh protocol within the

**[39:21](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2361s)** ROSS and you do not have uh to think about which uh message broker do we have DDS handle it in the ROS >> in this case I I just need special specific library to to to process it okay cool and is it compatible only only with Raspberry Pi right I mean >> no Raspberry Pi it's basic Ubuntu you can you can use uh uh everything which can run some Linux stuff and uh uh when you can uh set up the ROS it's Ubuntu Linux Linux and >> okay cool thank you thank you question >> oh thank you for the presentation u I had a quick question about the >> I I didn't see you

**[40:08](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2408s)** >> I have a quick question about the communication between the Ross nodes so is there any authentication mechanism or if I connect to the same Wi-Fi and run a ROS node, I can technically send the commands or read the sensor data from the RPI too. >> Uh basically out of the box you can you need to u set up the same domain of the ROS node to uh to handle the visibility of the ROS in in in your in your network. And that's it. If you uh see the another ROS note, you can you can uh communicate with with it. uh also uh DDS has a very complex system of uh quality of uh service and it's a lot of uh

**[40:59](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2459s)** variability how you can uh uh handle the messages uh do do you need acknowledgement and how you prove the uh receiving of the message and so on. uh very complex and uh reliable standard which which used in uh heavy production and uh DDS have have a lot instruments uh for message bro uh for messages and how to handle them. >> Um thank you very much for interesting presentation. Um robots are evolving. Some people are afraid of it. I'm not. Anyway, uh so the question is uh does

**[41:48](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2508s)** Ross 2 follows three laws of robotics by Isaac Azimov. [laughter] >> Um [laughter] I don't know how to answer. It's not connected things. Uh okay. Uh let me put this way. uh uh does uh our AI harnesses uh follow the free free laws I I guess not and it's comparable things uh Ross it's harness for robotics and how we communicate and control things in robotic robotic world and it's uh somehow can somehow like harnesses in AI Uh thank you. First of all, I'm going to

**[42:41](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2561s)** go a little bit deep near the hardware. Uh so the messages, if I'm not mistaken, the messages are being interpreted to drivers by ra by the Raspberry Pi. Am I right? messages um from my laptop uh uh some control messages uh yes interpreted in in uh being interpretated by Raspberry Pi and uh uh through the bridge uh make some signals to SDK of the uh rich rich mini in Raspberry Pi. >> Okay. And do you have any idea about the software inside the robot or is there any simul is there any opensource package that I can use to build my own hardware with for the robot?

**[43:31](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2611s)** >> Yeah. uh uh reach mini it's open sourced every uh uh software which used in in this robot uh you can uh take and make your own robot also they have a sch sch schematic for uh physical body so you can print out uh on the print on uh 3D some new kind of body or or head for for this and specification the motors uh also available So you can buy some hardware, some motors, some some antennas and uh controller and make your own uh reach with uh your custom body with some additional maybe hands and so on. So uh this project it's open sourced but uh in

**[44:23](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2663s)** uh in the real world uh robots are proprietary expensive and uh open source it's not it's more for fun and for education for some research but uh for m for production for business it's uh like proprietary platform which you have to buy and uh have to spend some money for that. >> Thank you. >> Thank you for your talk. It was amazing. Uh I have a question about the SDK and capabilities. So you told that you like know for dance or

**[45:12](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2712s)** some something else you pre-created sequence to prevent the Wi-Fi jeter and and something else. So my question is do this actions have some condition or business logic? For example, I have a camera. If on the right I see green, go forward. If I see red, don't go. And if not, do this like if I want to make some conditional logic, do I need to do the round trip and resolve this on my note or robot can do it by itself? uh it depends uh what uh resources do you have uh in your brain of the robot or some another source of calculation. So it's a question about where I can make decisions uh about uh hardware and what I do next. Uh it's two uh two

**[46:02](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2762s)** policies of that uh you can uh do everything inside the robot and uh tomorrow uh speech will be about that how you how you how you can make uh navigation robot uh uh with every decision uh inside it. And another approach uh you can you have a very thin uh uh hardware and very thin uh brain in your robot Raspberry Pi 5 and all computation uh you do in your laptop or in the cloud with some GPUs and so on. So, uh you can make actions and uh make some uh small signals from the outside world or uh you can push a lot of messages with uh

**[46:54](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2814s)** moving of every motor in your hardware to make control signals to the hardware. >> Okay. I just I think you mentioned this uh our dance for the service it's a action right so action is a rose term >> yeah yeah >> so the question is in this ro term >> do you have place where you can do actually decisions uh >> you can uh do both way >> yeah so it works so the functionality is supported >> you you you can you can push a lot of messages to the topic to make every move of the robot or can or you can push one action with one goal and uh >> take new action.

**[47:40](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2860s)** >> Yes, of course. >> My own with some business conditional logic. Yes, >> you you may have a action uh with some business logic inside your robot and push this action from outside world to start them and >> yeah um yeah I guess if I understand you can just push a logic to server client side depending on the resource availability yeah so my question is like related but it's about you mentioned there's like two SDKs one is C++ and Python Right. >> Uh two clients for the Ross. >> Yes. For the for the Ross one. >> Yeah. Um is there any other languages and is it the parity the same between C++ and Python? >> Uh there is parity between plus uh C++ and Python and uh I I guess uh right now

**[48:32](https://www.youtube.com/watch?v=m0WGHOnAxmA&t=2912s)** we don't have another implementation of the ro library official one. I think I saw something uh with go uh but it's not official. >> I think I think Russ and uh go it's obvious uh nonofficial clients for the ROS but with with uh agents it's uh doesn't really matter which language do you use. So I think my next project will be in C++ because uh you do not have to read the code anymore. So >> thank you very much. [applause]
