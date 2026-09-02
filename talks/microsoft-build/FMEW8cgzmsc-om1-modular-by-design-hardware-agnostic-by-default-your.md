---
id: FMEW8cgzmsc
title: "OM1: Modular by Design, Hardware-Agnostic by Default. Your gateway to next-gen robotics | DEM306"
slug: om1-modular-by-design-hardware-agnostic-by-default-your
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor events"
edition: "Build 2026"
year: 2026
speakers: ["Prachi Sethi"]
channel: "Microsoft Developer"
duration_min: 21
published_at: 2026-06-04T13:46:57Z
video_id: FMEW8cgzmsc
url: https://www.youtube.com/watch?v=FMEW8cgzmsc
youtube_url: https://www.youtube.com/watch?v=FMEW8cgzmsc
tags: ["AI", "Agents", "DEM306", "GitHub", "OM1: Modular by Design Hardware-Agnostic by Default. Your gateway to next-gen robotics | DEM306", "OSS", "Prachi Sethi", "build", "build 2026", "f9818341-9d02-497c-9b46-cb5f25533179_M9Z7-DEM306-1", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: ["Inference, serving & GPU infra", "Multimodal, vision, speech & robotics"]
transcript: true
---

# OM1: Modular by Design, Hardware-Agnostic by Default. Your gateway to next-gen robotics | DEM306

**Prachi Sethi**

`Microsoft Build` · `Build 2026` · `2026` · `21 min`

`#AI` `#Agents` `#DEM306` `#GitHub` `#OM1: Modular by Design Hardware-Agnostic by Default. Your gateway to next-gen robotics | DEM306` `#OSS` `#Prachi Sethi` `#build` `#build 2026` `#f9818341-9d02-497c-9b46-cb5f25533179_M9Z7-DEM306-1` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=FMEW8cgzmsc) · [Conference site](https://build.microsoft.com/)

## Description

Robots today are powerful but siloed. Each one is locked to its own stack, hardware, and interfaces. OM1 is a modular, hardware-agnostic orchestration layer that bridges any robot with the cognitive infrastructure needed to make it actually useful. In this session, we'll walk through OM1's architecture, show how its modular design allows you to swap or add capabilities, and get started on your laptops. We'll also demo it live on the Unitree Go2 and in a cloud simulator. Bring a laptop if you'd like to follow along!

To learn more, please check out these resources:
* https://aka.ms/build26-next-steps

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Prachi Sethi

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

DEM306 | English (US) | Developer tools & frameworks

Demo

#MSBuild

Chapters:
0:00 - Architecture overview and robot sensor inputs
00:02:12 - Explaining LLM-based robot cognition and decision making
00:03:31 - Live demo with robot Bytes
00:07:40 - Robot Restart and Transition to Simulator Configuration Setup
00:10:02 - Explaining Configuration Structure and Personality Customization through Prompts
00:12:22 - Migration from Python to Go for lower latency and better performance
00:14:37 - Robot begins autonomous SLAM mapping and location tagging
00:16:10 - Discussion on initiating multiple conversations and group interaction
00:16:29 - Introduction to App Store concept for robot applications

## Transcript

*2,612 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=2s)** Hi everyone, how are you all doing today? Have you heard about Open Mind before? OK, so today I'm here to demo our software stack which is OM1. OM 1 is a hardware agnostic layer which connects to different kinds of robots. So I'll quickly start with the intro. OK, so this is the agenda for today. I'll start with the introduction. Then I'll go towards the architecture quickly and then how to get started with this and then how you can contribute. Then we have a quick demo with the dog over here and I'll quickly demo our Cloud Axiom as well. So for introduction, we are building software. That brings cognition. To the robots, Omo M1 is open source and it's modular, hardware agnostic at the same time, which acts as

**[0:53](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=53s)** a orchestration layer. That bridges any. Robots. To the cognitive. Infrastructure which is also provided as API infrastructure through. Open mind too. It brings social intelligence capabilities to the robots. You can write it on Mac. Ubuntu machines and. We currently support unitary goto Jiwan Limuxtron. Booster then you be tech and it's a small. Humanoid and also. The turtle bot OK, this is a quick architecture overview for you. Each robot comes. With a different stack for their sensors, they have different. Microphones. Speakers. They have lidars, then they have location, GPS, battery and everything. Else so we take all these inputs then. We also take inputs from the user, so if the

**[1:41](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=101s)** user wants person of the robot to. Look around and. Say something or do. Certain other things. You can give us a user prompt, so for example as a robot can you move forward? Something like that. And then there's system prompt which tells the. Robot, what kind of personality it has, and then you can also name the robot. For say this robot is named bytes. And it knows what its. Name is then all of these. Inputs along with the. System prompt goes to the LLMS and the. LLMS go think and take. Different actions based on that. So all these. Inputs are taken the. LLM does the thinking and performs certain actions. Now actions could be either. Movements or the robot will talk to you, or ideally if if it wants to tell what's a battery or something like that. And these are the full autonomy features which.

**[2:32](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=152s)** We have so there's face detection and anonymization, SLAM map generation. Autonomous. Navigation. Then there's obstacle avoidance, the. Robot will. Navigate by itself. And it will avoid any obstacles. Which comes on its way. Then we also support auto charging for units to go to which is not. Supported for. Other robots but unit to go to when it drops after certain battery level it goes. And charges itself and we have simulation support as well. Then robot also does person following so I'll quickly demo that too. So for there's another thing if you OM1 is open source, so I've put our QR code here for our GitHub repository if you want to take a look. And we're open to contributions. From people if you want to integrate your. Own robot, so for example.

**[3:21](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=201s)** If you have. Another robot Which? We don't support yet you. Can raise a PR and. Try to contribute here. Or you can. Add support for different kind of sensors as well. So I'll quickly start with a demo now. Hi bytes, hey bytes, hey bytes, How are you doing? Can you switch to conversation mode? Hey Bites.

**[4:28](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=268s)** Sorry, meanwhile I'll try to. Show you the cloud simulator as well. Along with that, if you see there's a portal. Here you can. Choose which robot you are connected to one second. OK. Because. Hardware. Into the same intelligent software across different types of robots like me, a quad or even a humanoid or a drone. It really simplifies how we manage and coordinate multi robot

**[5:17](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=317s)** systems. Have you had a chance to test out that portal interface? Hey bites, can you? Switch to greeting mode. I think the Wi-Fi is a little. Can you try that robot? Can you switch to greeting? Mode. I think the Wi-Fi is a little slow as well. Let me switch. I'll switch to the other Wi-Fi. One SEC. OK, so this is the cloud simulator.

**[6:16](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=376s)** I'll switch the Wi-Fi on the. Dog and I'll demo that meanwhile. You can take a look here. So there's a simulator here. We have a simulator for go to. Linux Tron and also unitary G1 which you can choose from the portal. Let me restart it.

**[7:40](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=460s)** OK, while the robot restarts, I'll. Showcase how you can try out different configurations in the simulator and also how to get. Started on your laptops? So first thing you do. Is you clone the repository and once you clone the repository. You have to. You'll have to ideally. Install a bunch. Of dependencies. So if you go here and go to our repository here, once you clone it, you'll find certain steps to get started. And the. Very first step is to grab the API key from the portal. So you go to the portal, go to the dashboard and create the API. Key. Once you do that, you can define the robot type.

**[8:29](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=509s)** And also give it a label. So ideally this is the portal and once you get the API key you just grab. That and declare it as a. Environment variable. And I've already cloned the. Repository here. So the step is to export. It is export OEM API key equals to and give your API key here. Since I've already exported it, I will try. To run. By default there's. There are certain. Configuration files so. You run it by UV run. Search run by and its conversation. OK, so if you see that error, you just need

**[9:33](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=573s)** to do some troubleshooting. Wait, OK, I'll also show you. How the configuration? File actually looks like, so it looks something like this. You need to define the version. Then you define the. Name of the agent. And then there's the API key. You can even do it here, or put it as part of your environment variables or export it over there. And then?

**[10:20](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=620s)** If you see here there's a prompt example and also system prompt base which is like it says you're a smart, curious and friendly dog. If you want. The robot to have personality of a robot or a monkey or a teacher or maybe a psychologist or whatever you want or somebody who roast everybody else. Whoever it sees, you can just. Tell the robot to have that personality and the robot will act in that certain way. So. That's basic. Prompt Engineering and. You can also. Give certain example or context. So for example, if you're going. Somewhere and you want the robot to. Have some information? About certain things, you just feed it as the. Prompt and. You go to agent inputs. Inside the agent inputs you have. Different. Kinds of inputs like if you have the speaker, the microphone and the camera, so we have Google ASR as input and then you have probably if you want the

**[11:09](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=669s)** camera to be there as well, so you give. BLM villa there. That's what we support. And then there's. Cortex. LLM. So we support multiple. You can plug in whatever you want. You can have. Gemini Open AI. And we support open router as well. So through open router you can. Plug in Anthropics or any other LLMS you want, we also support. Olama so it. It's up to. You if you want. To host your local models so you can switch to Olama plug in. And then make the robot respond through that LLM. OK, so here if you see I think you can't. Hear from the laptop but. It's running over here and if I say hi bytes or something like hot spot or whatever it is.

**[11:59](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=719s)** It would listen to what I'm saying and then respond. Accordingly, I see it over there. It's making funny noises, isn't it? So ideally the robot. Tells this and so this is like a virtual agent which runs on your laptop. And what is running on the robot? Is on the Thor. We have everything dockerized, so this was a. Python version we. Also have a. Go version and we are migrating everything to Go as the latency is pretty much pretty less as compared I'm. Listening closely to your computer, OK. OK, so here this is the go version and it is pretty.

**[12:46](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=766s)** More. Faster as compared to the Python version and once you can just run it on your systems as well. And Go is also compatible with the Windows. So you can try. Out on that. System as well if you want it creates a binary. File and you can just run it on Windows Ubuntu machines. Or if you have a Raspberry Pi or other supported hardwares as well. Then apart from. That if we. Want to I'll? Show you a. Quick demonstration with the. OK, so here. Is our. Simulator I'll start. There's a file called cloud SIM and if we just start this. And put in. Cloud SIM.

**[13:43](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=823s)** So ideally you will go to machine. Tele OPS and you can see simulation robot here. So once you click on this OK, so you'll see the stream which. Robot is able to see. On the simulator. And ideally when you. Have a actual robot. You can also see the stream in the other. Portal. So the other portal which I have here is so you choose. Your micro robot. I think there's network latency here, so you're not able to see the. Streams here but. Ideally. That's how you look at the stuff. So this is the. Simulator and the. Robot is. Here in the you can see it on the portal what the robot can actually see and you can start

**[14:31](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=871s)** the SLAM mode. So what happens now? Is the robot. Will start moving around the place autonomously and start generating a 3D SLAM map. And while it's generating the map, you can save certain locations. As kitchen. Or living room or front door. Or something else? And the robot would ideally know. Which places what after the whole. Map is generated, you can make the see the robot is now navigating by. Itself over there. And ideally it's trying to map the whole area and the map is getting generated which you can take a look. At the portal. So that's how the map is generating now. And once the map is done. You can click here and save the. Map and after saving the map when the robot is

**[15:20](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=920s)** moving around, you can just. There's an option which comes. Up save location. And once you save it and the slam map is done, you can do the navigation. Mode. You can switch the mode from. Here to NAV mode NAV to mode or you can also verbally tell the robot to switch the mode so ideally when it is in navigation mode you can tell the robot hey, can you go to the kitchen for me and the robot will ideally go and go to the kitchen and do certain things whatever you. Prefer it to. Do so that is one thing, and then apart from. That there's person. Following and the greeting mode, I'll try to. Switch the Wi-Fi again if. We can do it and so ideally in greeting mode, robot would track a person and walk. Towards the person. And greets the.

**[16:08](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=968s)** Person have a. Certain amount of conversion like 3. To five conversations. And try to find another person and go there and. Greet the other. Person and have the conversation. Do you? Guys have any questions or suggestions or like what do you feel about this? So App Store is like if you want to build so it's. It's like different. Conversation or different Jason files or the configs which we have. You can ideally go to the App Store and either deploy your own applications and so ideally. How it works is if. You have a robot connected. Through the API key, so whatever. API key you configure on any robot audio machines. It identifies as a machine on the portal and you

**[16:59](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=1019s)** can create an app and deploy it on the app on the robot. Based on the API key OK I think. The map. Generation is complete. Now so we. Can go ahead. And save the map. I'm just going to say map. 2 and let's. Stop the slam. Mode and. Start the navigation mode. Now there's. One more feature for telepresence. So you can ideally, so if for example, if you have your robot at home and you're not at home, plus your parents who are old are home and you

**[17:47](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=1067s)** want to see if everything is OK or not, and you can also quickly hop on a video call with them. Through this. So you just do this here and it starts telepresence. OK so. The other person on the other side. Would be able to see. So for example, my parents are not responding and I want to check if they are in the living room or the bedroom or wherever, but I'm not able to track them or they're not picking calls. So I can make the robot navigate through the portal and go to the living room or the kitchen or wherever, and then if I want to see what's happening, I can hop onto. A call there and. Ideally we can see what's going on on the other side and they can also see us and have a.

**[18:34](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=1114s)** Conversation. And see like if they're doing OK or everything's fine or not. Something of that sort. OK, so now. It's in navigation. Mode and ideally you can. If if you want to. Have the robot. In particular position and you want to tell the robot OK, remember this. Place as kitchen. You just put in here and say this location and this location is now saved as kitchen. It saves the coordinates here and. That's how the robot would ideally. Know and if. Now robot navigates. To a. Different place, we can just tell the robot, hey, can you go to the? Kitchen I can. Ideally. Ask it here. I'm not sure if you will be able to hear that, but hey Whites, can you move? To the kitchen.

**[19:51](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=1191s)** So you. Can even save. Multiple. Locations here and. You can also make the robot move through. These there's a. Tele operator and you can make the robot go to different. Places through this and it. Moves on the simulator there and you can. See the view. Then I can also. Show you other options we have for this. On the cloud simulator you have different options you can. Deploy whichever robot you feel like you can try. It with Tron G1 or the go to and. Then you can choose different. Environments either apartment or the warehouse. The current one is the warehouse. Setting so ideally. It depends on if you want to deploy the robot in the apartment setting or. Warehouse. And then you can play around with that.

**[20:40](https://www.youtube.com/watch?v=FMEW8cgzmsc&t=1240s)** I think that's pretty much for the demo for now. I'll try once again if I am able to switch the Wi-Fi there, but. Meanwhile, if you guys have any? Questions. I'm up for the questions. We have like few minutes remaining.
