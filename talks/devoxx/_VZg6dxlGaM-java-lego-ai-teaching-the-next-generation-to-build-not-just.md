---
id: _VZg6dxlGaM
title: "Java, LEGO & AI: Teaching the Next Generation to Build, Not Just Prompt by Eddy Vos"
slug: java-lego-ai-teaching-the-next-generation-to-build-not-just
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2026
speakers: ["Eddy Vos"]
channel: "Devoxx"
duration_min: 24
published_at: 2026-10-06T05:32:28Z
video_id: _VZg6dxlGaM
url: https://www.youtube.com/watch?v=_VZg6dxlGaM
youtube_url: https://www.youtube.com/watch?v=_VZg6dxlGaM
tags: []
topics: ["Prompting & context engineering"]
transcript: true
---

# Java, LEGO & AI: Teaching the Next Generation to Build, Not Just Prompt by Eddy Vos

**Eddy Vos**

`Devoxx` · `Devoxx` · `2026` · `24 min`

[Watch the recording](https://www.youtube.com/watch?v=_VZg6dxlGaM) · [Conference site](https://devoxx.com/)

## Description

*No description published on YouTube.*

## Transcript

*2,211 words · source: supa (en, exact timings)*

**[0:09](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=9s)** go Good afternoon everybody. Enjoying lunch? >> Okay, welcome to my talk. all about Java of course but also about Lego and AI because when we start coding what happens when robots don't understand the programming language I try to do

**[1:01](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=61s)** live demos moving robots that we are building Devoxx4Kids. I always get questions. Why do we teach kids to code ? Because we have AI. Yes. Parents are asking me this. Teachers are asking me because we also give workshops at schools. But also my colleagues at the coffee machine. Why do we need to learn coding? Fair question, ChatGPT. Everything can be generated with one sentence in English. We think differently because you can use AI, but

**[1:52](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=112s)** you need to know how. Great example: the calculator, a nice invention, but we still teach mathematics. If it's 7*8 , we know it's 56. What if the machine says 5600? We know that's an error. With that mindset, we are talking and thinking about: how can we still teach children the basics of Java coding and still use AI. So, AI changes how we write code but not why we learn to code

**[2:51](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=171s)** , so asking the right question to AI is very important. Yeah, I want to move a robot. I have a robot here. Yes. I want to run it around the room. Don't hit a wall. Spin around. Hey, it can just deliver me the code. Yes, that's true. But judging the answer of the code... Yes, that is something different. Because if you see a loop, you really need to know if the robot turns four times instead of three, where is the error? So someone has to face reality, because coding is great, especially

**[3:38](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=218s)** physical computing like with robots. Yes, to be honest, you face a lot of different things. The motor can stall, or your battery is empty. The floor is slippery or something. You need to expect all those kinds of things. So for me, prompting is asking, but building is understanding. And yes, I used AI a lot while creating this workshop for kids, using Claude, getting great errors when generating the code. The funniest thing is that in the delivered code nothing happened and then it says to me, "Ah, congratulations, I baked a deadlock into your code." I am Eddie Fos, I'm currently the chairman of the

**[4:32](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=272s)** Devoxx4Kids Foundation in the Netherlands. I'm also an engineering manager at Ahold Delhaize. People in the Netherlands know that from Albert Heijn, and Delhaize as well. And specifically I'm working at the Ahold Delhaize tech division. I started coding when I was, yeah, 10 years old. Everybody knows, maybe the older people here, the Commodore 64. Such great old times. First coding, uh, in BASIC, uh, started at 12, uh, on computers. In 2016, I went to my first Devoxx4Kids event as a volunteer helping kids, and

**[5:22](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=322s)** since 2022, I'm on the board. And I like it. But back to where we are, why are we teaching children, especially, uh, physical stuff? Because yeah, we say if you have a robot they can code, you have their attention. Just coding behind a screen, yeah, kids check out, they don't like it. And what is the nice thing is, if you have a robot running around the room coding it, you can see the bugs directly. 90. Is it? Is the speed of the motor, who knows?

**[6:16](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=376s)** We also do it first in Scratch, kids who are young, 8 years, 9 years old, and we can also give it in Java and that feels like a real promotion for them. And then we also use prompting to explain what the code is doing. And for this, we use the Lego Spike. Lego Spike is an educational kit, uh, built by Lego. It is the successor to Mindstorms . Uh yeah, the application that comes with it gives you blocks like Scratch and also gives you some icons to throw around, uh. I meant it, but okay, using

**[7:11](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=431s)** Python unfortunately, so now no Java support, and that's because, uh, the Mindstorms set with this suit supported 20 till 2022, uh, the JVM was stopped. But what we wanted is, yeah, we wanted to have it running on Java because our volunteers at Devoxx Netherlands are mostly Java developers and we want to show the kids our IDE that we use, IntelliJ, Visual Studio. Yeah. But we were using Legos and Spike doesn't have a JVM. Why not? Well, let's look under

**[8:01](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=481s)** the hood. This is the controller, the motor. The engine is a, uh, little computer in it, uh, it's, you can move it and it detects it. The only problem: it has tiny resources, a small, uh, processor in it with 320 KB of RAM. And yeah, that's the exact problem because a standard JVM doesn't fit in there. So what do we do? Lego published the complete documentation on GitHub, thankfully. So, uh, uh, telling you how it translates the building blocks into

**[8:48](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=528s)** specific bytecode, going to the robot using Bluetooth. And that was my way in . How can we hack this using it to write our own custom overhead by stuffing code, exclusive OR validator? One disclaimer, no Lego part was harmed during this journey. Everything is still working. There are three roads that we explored. First, yeah, let's try to get a JVM on the robot. The problem is putting a JVM on the hub.

**[9:36](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=576s)** Yes. That's a deadlock because it will crash, since you need to install custom firmware on the robot. If you do that on a robot bought by a school, they can't use it anymore with the Lego software because you could break it completely. So there was no way. Second part, let's make Java code and have the Java code generate Python, MicroPython. Put it there. We did that. Wrote all the code. The nice thing is it uploaded to one of the slots on the robot. The robot has 20 slots. You can send the program, the program that executes it.

**[10:27](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=627s)** And we started running it, and the robot did not move again. Failure. But it partly worked, because we had still sent the code to the robot and it worked. Let Java have the brain, Lego have the body, so let's use the laptop and just use Bluetooth, sending it to the robot. Java can talk Bluetooth directly using libraries. That was the call. The strange thing is, we used Windows laptops and the libraries we got were only for MacBooks or Linux. So

**[11:18](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=678s)** we hit a dead end. Then we came up with an idea. Ah, we still had some Raspberry Pis left. We are also teaching how to code on the Raspberry Pi online. So that is why it we are building a bridge sending the code to that new hardware, same work. It uploaded to move and then we found it out. Yeah, let's do it step by step. Okay, let's just use Python first. We finally found a library that worked. Okay, it moved. Switch back to Java.

**[12:08](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=728s)** Wire Java to the bridge that we coded and it failed again. The strange thing is we didn't get any errors back. We were sending everything out. We caught all the errors, but nothing was sent back by the robot. That end. Then we started to reroute our architecture create a simple API in Java, sending it to a little program on that code robot sending it it finally worked. So, hopefully this works. And I will show

**[13:00](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=780s)** you something about how we did it. First, we built a bridge. And yes, the bridge is in Python. So, we installed Python on a Raspberry Pi. Let's run it. Let's switch on the robot. It's pairing too late again. Connected, waiting for Java. Fun stuff. What we coded here is

**[13:58](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=838s)** just a simple API for the kids to learn . We have a loop, drive forward, turn, do everything, we created a lot of things. What we noticed while creating this workshop is that the Lego robot, well, you can send a drive command, but the drive command requires more; you have to specify the speed and duration, so how many seconds at what speed, or it won't work. It was a challenge to set this up and also make it easy for the children. So if I, for instance, take here, drive for a second speed

**[14:49](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=889s)** adding it after the last one, and I say speed is 100 and we do this for another 3 seconds just adding it. And now hopefully it get it working with the camera. Because so cold doesn't show because there was text in it. We

**[16:10](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=970s)** finally got it moving but we have to say we are still working on it, building a lot more commands because, for instance, there is also a distance sensor and we are still figuring out how to code it in Java because it was still blocking. And that's why we also need some help from you people. Let's switch back. So how we put this together is that we still use Windows

**[17:06](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=1026s)** laptops because we have a lot of Windows laptops available for workshops . It's based on Windows because all the schools are still using Windows books. We put a Pi in between because a server runs there that translates the Java code into bytecode, sending it to the Lego robot and then sending the response back. And we are still working on this because what we really want to do is combine this, as there is finally a Java library for Bluetooth. So we still need to do some work on it to,

**[17:54](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=1074s)** well, get the Raspberry Pi out of the architecture, but also for the kids coding it in Java. And why Java? Well, real Java. Something that most parents are also coding in Java, and they see that they really want to learn that. Since it's much easier for the kids to start with now, if you look at the main , there are no arguments, nothing is needed anymore, the public static voids are all gone in Java 25, you can quite easily write clean code, and that makes it very easy for them to jump in, and

**[18:46](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=1126s)** also they can learn the real stuff like IntelliJ, Visual Studio Code, the same as what the parents are using, what you guys are using. So could AI have built this? Of course. I also used it mostly to look at all the documentation published on Git, generating the boilerplate hard to beat what AI spit out. Humans are still in the loop, still figuring it out. And if that API

**[19:37](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=1177s)** is designed well, an AI can teach a 10- year-old kid how to use an API, making it easy like making a robot drive. It's much easier than writing a whole method . So, that brings us back. Yes, why do kids still need to learn the code? Yes, AI is a powerful tool. But yes, you still need to think about how to use it and how to build it. I also think it’s a very good medium. So. Uh, And why are we working so hard on this? Yes

**[20:28](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=1228s)** , because we think the developers of tomorrow are 10 years old right now. Yeah, kids already meet Java using Minecraft built in Java, and yes, they play a lot of Minecraft during the Devoxx4Kids days. We have a great Minecraft session. Also, the first experience of making a robot move is fun, too. And if you look at the modern Java nowadays. Yes, it's fun for them to play with it. Much, much easier. And if you think of Java as just for the server. Uh yes, behind the server. Okay . Normally, everybody says Java is

**[21:16](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=1276s)** backend. Uh the web services, enterprise systems, it's all server-based. And nobody thinks about robots. Normally it’s Python or Arduino, true, but you can still combine it. So in our communities, we are using a lot of Java to teach at the Devoxx4Kids days. And every Java developer here in this room can give that training. It's all on remote. Because the Java developers of 2040, yes, they are in primary school now, but they will follow you quickly. Make sure they learn Java. And in the right

**[22:09](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=1329s)** way, too. So my feedback and thoughts for you to take home. Help the next generation build Java. Volunteer for a workshop. In the Netherlands we have the website, and in Belgium too. Daniel is also creating a lot of Devoxx joints , or think about your company hosting a Devoxx4Kids day, and teach them Java at your office. Invite kids, we can help. Go to the Devoxx4Kids website, ask for help, and we will help you. And if you’d like to experiment with LEGO

**[22:59](https://www.youtube.com/watch?v=_VZg6dxlGaM&t=1379s)** Spike or something, all our code is in the repo. In the Netherlands, once a quarter, we also have a hackathon. Also with a lot of LEGO, and we are playing with it and creating workshops in Java for it. So I would say, go to the website and join us. I thank you all.
