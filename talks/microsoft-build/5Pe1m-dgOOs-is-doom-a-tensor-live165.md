---
id: 5Pe1m-dgOOs
title: "Is DOOM a Tensor? | LIVE165"
slug: is-doom-a-tensor-live165
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Anthony Shaw", "Burke Holland"]
channel: "Visual Studio Code"
duration_min: 17
published_at: 2026-06-05T13:39:16Z
video_id: 5Pe1m-dgOOs
url: https://www.youtube.com/watch?v=5Pe1m-dgOOs
youtube_url: https://www.youtube.com/watch?v=5Pe1m-dgOOs
tags: ["Anthony Shaw", "Burke Holland", "Is DOOM a Tensor? | LIVE165", "LIVE165", "LIVE165_v1", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: []
transcript: true
---

# Is DOOM a Tensor? | LIVE165

**Anthony Shaw, Burke Holland**

`Microsoft Build` · `Build 2026` · `2026` · `17 min`

`#Anthony Shaw` `#Burke Holland` `#Is DOOM a Tensor? | LIVE165` `#LIVE165` `#LIVE165_v1` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=5Pe1m-dgOOs) · [Conference site](https://build.microsoft.com/)

## Description

Every model you use runs on tensors. But what actually is a tensor, where does DOOM fit in, and why does it matter when you are trying to get Copilot to optimize your code? Anthony Shaw breaks down how machine learning models work under the hood and what knowing that changes about how you write prompts that actually get results.

To learn more, please check out these resources:
* https://aka.ms/VSCode/Learn
* https://code.visualstudio.com/learn

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Anthony Shaw
* Burke Holland

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE165 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Exploring Model Example – Harrier Text Embedding Model
00:03:59 - Discussion on Onyx being Turing complete and capable of running complex logic
00:04:31 - Reference to Doom running on Windows since 1995
00:06:26 - Audience poll concludes option 2 (CPU emulator) is correct
00:08:43 - Discussion on Excel interpreting machine code
00:10:37 - Explanation of Nectron representing a RISC CPU and RAM as tensor
00:13:56 - Scaling out challenges due to Doom being single‑threaded
00:14:00 - Best practices for coaching AI agents – importance of benchmarking
00:16:44 - Session conclusion and closing remarks praising the learning experience

## Transcript

*3,062 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=4s)** All right. Hey, folks, we're back. We're back. We're back. I'm joined by Anthony Shaw, Tony Baloney, Tony. Baloney's mistake. Yes good. I'm doing well. You are a technical advisor. I am, yeah, yes. And previously Python advocate at Microsoft. I've been working on Python for five years at Microsoft. Yeah, there's like, am I supposed to read this entire bio? There's. Like, no, it's fine, don't worry. You won a Nobel Peace Prize. There's only a couple of them, yeah. Amazing. Unbelievable. All right, now literally the title of this session is. The next 16 minutes is I don't under this sentence makes no sense. Is Doom a tenser? Yes and why? Yes, here and yes, and here's why. What does this even mean? OK, we're going to do it and.

**[0:52](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=52s)** By the way, this is not what we agreed to talk about. What did I agree to talk? About no, you sent me a message. You're like, we are accused. I'm so sorry you're going to hate me, but we're doing this instead. Yeah, I thought we'd just got a bit of an adventure in this session over the next like 20 minutes and we're going to talk about tensors. I'm going to explain how CPUs work, machine learning models, inference. We're just going to go fast and go quick in. 15 minutes in. 15 minutes. Best of luck. OK so is Doom a tensor? First of all, like what is a tensor? So if you look at something like an Onyx model, a tensor is some data which has a size and a shape. So normally we represent these as like a matrix. So for example, if it was an array, there's one dimension and it has four items, and then we had

**[1:42](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=102s)** a model that outputs 1. Then it could be the numbers 1234 and you could run the operation sum and it would give you back one number, which would be the number 10. That is the simplest machine learning model I could come up with. All it does is add the numbers together. It takes a sequence of numbers and returns you back the total. So we're going to we're going to go deeper and deeper and deeper until I make Burke prior. OK I'm. Are you there? It did only took one slide. OK, so that is the simplest one I could think of. Here is a tool that I love to play with called Netron. Netron allows you to actually inspect AI models and explore what's inside them. So yesterday we announced a whole bunch of new Mii models, image models.

**[2:29](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=149s)** There's like reasoning models, there's all sorts of stuff. I love to actually just explore what's inside them, how do they work? And the way that we can do that is a Neutron, and we can actually open up one of those models. The model that I've got on screen is a text embedding model called Harrier. And inside there you can see this is basically the graph that explains how to actually execute this model. So the input to the model is your tokens, so like the text and then also something called the attention mask which we definitely don't have time to explain so. I do know a thing about attention. We should have a whole session on attention because that's the most interesting. Part. Sorry. Go ahead. So you might think that a model is basically just some weights. That's not entirely true. It actually has instructions to explain how you take the weights, the user input, and you process that through the

**[3:19](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=199s)** different layers to get the output tokens. So that's what it kind of looks like inside. I was looking around at this and I've been focused on thinking about how some of these nodes can be optimized for some new hardware that we've got coming out. I don't know if you heard that announcement. I did. I was coveting it, but I don't think they're going to give it. To me, OK, yeah, we have. So we're working on a project with NVIDIA. We've got this new Windows Surface device, the Surface Ultra. I believe so. The Ultra with. What 128? Up to 128 gig Ram also has a on the sock. It has a GPU. So I'm really excited about how we can make that work. Yeah, but I noticed that Onyx itself is Turing complete. Some of those instructions include like and IFS, loops, stuff

**[4:10](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=250s)** like that. So I thought, if an Onyx motto is Turing complete, can it run Doom? OK, can you see where this is going? No, you're still. Yeah. OK. Kind, I'm 50% with you. OK, so to answer the original question, is Doom a Tensa? We're going to get there and we've got 12 minutes. OK, Now hopefully you're familiar, but we announced this a few builds ago. This was in 1995. Geez, Bill Gates looks younger than I am right now. Doom runs on Windows, so we've gone got that one nailed. There's absolutely no reason to run it in a Tensor, but it's fun because we get to explore how they work and how Onyx models are put together so. So Onyx ISM is the model. Onyx is the model and it includes instructions to how

**[4:59](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=299s)** to take the user, input the tokens, process it with the weights and compute the out. So would it be accurate to say the question is can an LLM run Doom? Yes. OK, it's a bizarre. I don't believe you. I know. That doesn't even make sense. It can't. They can't spell strawberry. So I thought what is the what is the lowest level of compute that somebody has run on run doom on and is this project called Potato Doom? No. Potato Doom. Essentially they created a string of potatoes and used that string to power a small device which ran doom. OK, so the potatoes aren't running Doom, they're just powering the device. They're running Doom. That's a little bit of misinformation. Fake news. Fake news.

**[5:47](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=347s)** So I thought, if we're going to figure out in our Hobbit land, how are we going to get this running in the model, I think we have three options. Is this an AI image? Maybe. OK, right step. What? Option one is write AC compiler, so we compiles it doom from source into Onyx. That's option one. OK, option 2 is create ACPU emulator and option 3 is go for a war. Who's in favour of option one in the audience? Nobody. And option two, option two. Yeah, that's good. OK, option three. OK, a few of you. OK, option 2 is the correct choice. If this was an adventure game from the 90s and you pick option one, option three, you've lost the game. It's game over, I'm afraid.

**[6:36](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=396s)** So I thought, OK, what would be a simple CPU that we could emulate purely in Onyx nodes? And the answer would be the RISC 5 architecture, because it's fairly straightforward. We can actually add doesn't have that many types of instructions. I can compile doom from source into machine code, and then I can interpret that machine code purely in Onyx. Do you believe me, Burke? I mean. Or am I losing you? I just I'm just a JavaScript developer. OK, so with this I had a little bit of a trick up my sleeve which was that I described this problem to Copilot and said copilot this is my idea I need to get this working for tomorrow. Are you on board? You. Said yesterday no.

**[7:22](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=442s)** No, no, this is a week ago, OK, And I started off with Opus 4.7 and it wasn't convinced. It said this would take several weeks and I rolled back to my old friend Opus 4.6 because it is a bit more gung ho. Yeah, it is getting a little bit more like, Nah, I'm not doing that. He tries to talk you out of things I've found with some of the newer versions, and I'm like, I need you on board for this project. Yeah, because we need to make this work. So I didn't have a disassembler to hand. So I actually compiled Doom into machine code and I wanted to show you what that would look like. So I've put together a disassembler in a different tool that we can use, which is. Are you familiar with this one? Excel. OK, yeah, that's it.

**[8:09](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=489s)** This is Excel. We can actually just read Doom in Excel and we can disassemble it in Excel because there are not many instructions in the RISC 5 instruction set. We can just do this entirely in Excel formulas. This is so cursed. Everything about this is cursed. It just gets worse. OK, we're nearly there. So if we can understand and read just using excel formulas machine code, I had a question. This is going to get worse, but OK. Please. If Excel can read the machine code, can it just interpret the machine code for me? And then you get a red doom in Excel. Yeah. So I thought I had, I had another spreadsheet. Wait. Is it sound turning complete? It turns out yes is the answer.

**[8:58](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=538s)** No way. So I put. I added a sheet which is the program and then I added a sheet which is the memory or the RAM. So the RAM would get stored there. And then I basically just added the registers as columns in the spreadsheet and you can just do flash fill in Excel. The problem with this implementation is that you have to keep dragging down otherwise you run out of instructions and Excel unfortunately only has up to about a million rows. So oh. Really, there's an upper limit. There is an upper limit, and you've discovered that by doing experiments like this. You found it. We found the. Upper at which point what happens? Like the whole thing just freezes it. Just I think it just runs out of letters on the left hand side. Like, literally, there's just no more yeah. There's nowhere for it to.

**[9:44](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=584s)** Go. It's like, it's like going to the end of the Internet. Like can you see? You want me in that commercial where it's like you have you have reached the end of the Internet and the guy's like, there's nothing I have to do. You reached the end of the Internet. We've reached the end of Excel. OK, so that's .2 Doom runs in Excel. I think we've ticked that box. We already do. We already knew. Know. This. No no no. This is new. This is live and announced at Build 2026. I've created the. Promotion. Yeah, here it. Is we've added this promotion to our build announcements that should be. In the Why is it all from 1985? This is AI. This is AI generated. Yeah, I asked AI to make me a 90s looking advert showing how Doom looks runs in Excel. OK, so can we run Doom in an Onyx graph? So that's my next demo.

**[10:34](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=634s)** So I'm going to show you Nectron. And what I did with Nectron is I basically built a graph that represents ACPU, and the inputs to our model are the game, which is 8 megabytes of RAM, and also the compiled game and the CPU itself. So I have to zoom out because it's a bit big. So this basically represents a RISC CPU and it's got all the instructions in the RISC CPU and it can process those nodes, calculate it, and basically treat the RAM as a tensor. OK, OK, Now would you like to know how fast this is? How long do you think it took for it to

**[11:26](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=686s)** output this frame? One single frame. Yeah. Yeah. How long did it that's got. It's got to be something like 30 minutes. So I I set this running and I was going to one of my kids soccer games. It was a long drive to get there and I said to copilot when you get the 1st frame that is not just black, I want you to go and drop it in my OneDrive and then send me a ping on Teams so that I can just have a look at it and see what it did. And I'm jumping around like a silly person on the soccer pitch because I saw this flash up and I'm like, I can't believe it worked, but it was 6 hours. What's? The frame rate on that. So I it's like I don't know how many decimal places it was, but I worked out if this was ACPU it would be 2000 Hertz or two kHz.

**[12:18](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=738s)** It would be a 2 kHz CPU. So I had AI, had a bit of a conversation with Copilot. I was like your graph implementation of this Onyx model. This is not performing like what? What can we do about this? Very well it there's room for improvements. So that's why I want to kind of change the tangent of this talk from something entirely pointless and exploratory into actually what can we do in synal areas like this where Copilot or something like it has put together something and you're not happy with the performance. Now, my tips with performance generally are like, work with the cheapest and easiest thing first, which is caching. It's always caching. You just cache the output. I think like computer systems these days are just caches and caches and caches. So for Copilot, I'm like, OK, how can we cache

**[13:07](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=787s)** the output? OK, it couldn't do that. It couldn't cache the output, no OK. The other option is you reduce work, so you just reduce the amount of compute that you have to do. So after a couple of iterations it compacted that graph and actually thought about it and tried to reduce the number of nodes. And the next option is how? Much did you get out of that number 2? It was. I got to about 4-4 kHz. OK, it's just one. One image every five hours. Yeah. I think it's 33 frames, 1 frame per three hours. There we go. So not quite playable. And then the other option is scale up where you just make the computer bigger. This is currently the biggest computer we sell. It has a ridiculous amount of processing power. Is this the Ultra? It is not, no. Oh, it looks like I would be in trouble for bringing that on stage.

**[13:55](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=835s)** Oh OK. Yeah. And the other option is scale out. But unfortunately, Doom is single threaded. So my tips for coaching AI agents on speed is that when you start them off, you need to give them a benchmark at the beginning because otherwise they're going to make a bunch of assumptions about how to make things faster. And they're not going to base that on facts. They're not going to base that on reality. They're just going to jump in and be like, oh, we could just paralyze things, or we can introduce threads or they're going to try all these new approaches. But if you don't start with a benchmark, it's kind of guessing whether or not it's going to be faster or slower. OK, The other thing you can do is you can use the contrasting hypothesis or the rubber duck if you use the rubber duck feature. Yeah OK. You can use the rubber duck, which is a really cool feature in Copilot CLI where it can kind of

**[14:43](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=883s)** review things for you and challenge it. And you as a human or the kind of one who actually has to look and see like did the thing that it do to optimize that make it faster? Yeah. So here is the working demo of the final result. I've speed it up by about 1,000,000 times. Otherwise we would use up the remaining 2 minutes. This is the Onyx model, unfortunately. Onyx. How are you clicking? How are you? Onyx doesn't have a screen, yeah, it just outputs numbers. So you have to take the frame buffer and then convert it to a GIF. But yeah, that's the only downside of that implementation. There's no keyboard controls, there's no sound. Well, how did it? Who's firing the gun? It's the demo reel for Doom, yeah. So it's. Running the demo program. It's running the demo program.

**[15:31](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=931s)** Wow. How many? How many tokens? We're burned on this. I think it's best I don't answer that question with Martin within a shot of me. Hey Martin. Is Anthony above me on the leaderboard? There is no such board. So to bring this back to something concrete, yes, Doom is a tensor. That's brilliant. This is not efficient. It's not a good idea. I don't recommend doing this. The thing I do want to talk about though is that these nodes in your model, they are specific to the computer that you're running on. So like some of these, for example, in the Harrier model matrix multiplication is specific, like the implementation is specific to the CPUGPU hardware that you run on. So I think what's really important is that if you

**[16:21](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=981s)** download a model from Hugging Face or something like that, you need to understand is actually optimized for the hardware that you're running on. Just because you've just bought a new GPU or you've just plugged in something that has a Tensor core or an MPU doesn't mean it's necessarily going to be faster. In most cases, it doesn't actually know how to use it. So you definitely all need to learn a bit more about these models. That's my summary. Thank you for coming to my Ted Talk that. Was amazing, man, That was amazing. I love that. I'm going to be honest, I learned, I think I've learned more in the last 15 minutes than in the previous like 6 months. So I appreciate that. And most importantly, we learned what we already knew, which is that you are a million times smarter than I am. All right, get out of here. All right, we'll be right back.

**[17:08](https://www.youtube.com/watch?v=5Pe1m-dgOOs&t=1028s)** Thank you.
