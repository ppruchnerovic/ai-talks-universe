---
id: u06ybMn4W1s
title: "Your Browser Lives in VS Code Now | LIVE154"
slug: your-browser-lives-in-vs-code-now-live154
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Justin Chen", "Burke Holland"]
channel: "Visual Studio Code"
duration_min: 10
published_at: 2026-06-05T13:25:22Z
video_id: u06ybMn4W1s
url: https://www.youtube.com/watch?v=u06ybMn4W1s
youtube_url: https://www.youtube.com/watch?v=u06ybMn4W1s
tags: ["Burke Holland", "Justin Chen", "LIVE154", "LIVE154_v1", "Your Browser Lives in VS Code Now | LIVE154", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: []
transcript: true
---

# Your Browser Lives in VS Code Now | LIVE154

**Justin Chen, Burke Holland**

`Microsoft Build` · `Build 2026` · `2026` · `10 min`

`#Burke Holland` `#Justin Chen` `#LIVE154` `#LIVE154_v1` `#Your Browser Lives in VS Code Now | LIVE154` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=u06ybMn4W1s) · [Conference site](https://build.microsoft.com/)

## Description

The integrated browser is not just a preview pane. Agents can share tabs as context, read page content, interact with elements, run Playwright scripts, validate changes in real time, and debug with breakpoints without ever leaving the editor. This session shows what that actually looks like in a real development workflow.

To learn more, please check out these resources:
* https://aka.ms/VSCode/IntBrowser
* https://aka.ms/VSCode/Learn
* https://code.visualstudio.com/docs/copilot/overview

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Justin Chen
* Burke Holland

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE154 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Introduction and Welcome at Build Conference
00:00:13 - Introduction of Justin from VS Code Team
00:00:25 - Overview of the Integrated Browser in VS Code
00:01:09 - Purpose: Simplifying Local Development Within VS Code
00:01:54 - Demonstration: Opening and Using the Integrated Browser
00:02:33 - Pokémon Demo App Example in VS Code
00:03:09 - Using Chat Integration to Inspect Page Elements
00:05:00 - Chrome DevTools and Emulation Toolbar inside VS Code
00:05:51 - Agent Integration and Browser Automation
00:09:00 - Playwright Integration, Automated Testing, and Closing Remarks

## Transcript

*2,063 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=u06ybMn4W1s&t=0s)** Hey, welcome back everybody online, watching online and here at build I love I see some familiar faces sticking around through every session. I love you, you especially. Thank you very much. All right, this fellow in the front. All right, now I'd like to welcome Justin from the VS Code team is here. Here's my talking points. Let's get right to them. Sure. No, so we're going to talk today about the integrated browser, I believe which you work on. Yes right. This is the a feature that you've built inside of Visual Studio Code. And this again, this is a completely different way of working with of building things and programming that is kind of showing up everywhere. It's in the Copilot app. I think the first place I saw it was Visual Studio Code. So tell me more about what this is and how it works.

**[0:46](https://www.youtube.com/watch?v=u06ybMn4W1s&t=46s)** Sure. Yeah. To clarify, I actually don't work on it entirely now anymore. It's passed off to a couple other engineers on the team. But yeah, we started off about a year ago on this. It started in the simple browser and one of the problems that we were trying to solve was being able to kind of have local development and help with the local development all within VS Code without leaving the browser or without leaving the application and going to an external browser. And what that ends up looking like is having this integrated browser which can do everything from launch local agent like local locally hosted websites. It can also do things like log in to any application, any website that you want as well. So to kind of show off what that looks like, I'll go to and share my there's nothing up there, but I'll go to and share my screen here. I'm not sure what the audience will see out there. Yeah. Can we get, can we get Justin's screen up? They're working on it.

**[1:34](https://www.youtube.com/watch?v=u06ybMn4W1s&t=94s)** There's a mad dash back there. It's down here. Cool. So maybe they already see that. Cool. Perfect. Oh. This doesn't change, does it? Wow, I've only been here all day. It's OK. I just got here. But yeah, so to kind of show off what that looks like, so I'm going to go over here and there are a couple different entry points to this actually. So the first one is a little bit more on the nose. You go over here to the command palette and you do open integrated browser. So I'm going to click on this. Can you zoom? In a bit. Maybe yes, let me zoom in a tiny bit here, maybe one more time and you can see I can go over to yelp.com and you can see here, I already logged in myself, so I'm already logged in here, but so. You're just browsing GitHub. Yeah, I'm just browsing GitHub inside VS Code. It's not supposed to replace an external browser, but it's

**[2:23](https://www.youtube.com/watch?v=u06ybMn4W1s&t=143s)** something that you can use in app development, so I'm going to go over here. I already launched this on port number 6967, but here I have a little. Pokémon. Yes, it's a little app that I've been working on just for myself. A lot of my PRS into the public VS Code repo are unfortunately based on Pokémon names and this is just helping me kind of gauge like oh where exactly? When exactly was this issue made? What exactly does it do? It's it's a Bulbasaur. I know that because it says Bulbasaur. I was a little late. I'm a little like that's I'm in the wrong demographic for Pokémon. Yeah, sorry about that. No worries, no worries. I know, I know. Pierce has been really into Pokémon recently. Yes, and I know his kids are too. And big time. Yeah OK. But yeah, something great about this integrated browser is you can do a bunch of stuff with this. So one of the original features that we had is

**[3:12](https://www.youtube.com/watch?v=u06ybMn4W1s&t=192s)** this button up here, which lets you add an element to chat. So I'm going to go ahead and click on this and you can see I can go over and hover on any specific element and it'll add that element directly into chat. So this is kind of like if you had the browser dev tools open and you're doing the pick and then you're going OK. Exactly. And what exactly does that add to the to the chat there? Yeah yeah. So it adds an element screenshot so you can see here there's a queue photo. It also adds a bunch of information about the division, about the URL that it comes from, what the element is called. So wait a minute, hold on, if I could so attached element it says what the element is, the URL, the path? What is a path? Yeah, the path is just the total path, just coming from the very top. Oh OK so. It's like walking. Down the tree. Exactly. And then?

**[3:57](https://www.youtube.com/watch?v=u06ybMn4W1s&t=237s)** The outer HTML interest. Yeah. So that can be particularly helpful if you don't want the agent to, like, spend too long searching for what exactly we want it to work on. So you're basically giving it like the the page and then the the element out of it within the context. Exactly. OK, very interesting. So it's pretty cool because you can also customize this. Let's say we don't actually want to attach all of the CSS. We actually have a setting for this where you can disable the CSS or disable parts and this and pieces of this and. Oh, it includes the CSS too, so it knows about the styling. Exactly. I thought it was just adding just the element. Yeah, yeah, we added it. We changed it so that it adds a little bit more as well. Here there's on this hover, this kind of shows like a more concise and a little bit more of like a, like a, like a quick, what you need to know from that element. So you can just hover over and we'll show this.

**[4:45](https://www.youtube.com/watch?v=u06ybMn4W1s&t=285s)** But yeah, this is a great way for you to pass off to the agent a couple other buttons in the integrated browser. You talked a little bit earlier about the Chrome Dev tools. That's something we have here as well. Sorry if this is not particularly zoomed. In. That's right. You've got a lot going on here. But you can see here we have the Chrome Dev tools. I can load some stuff in the console. The whole dev tools are there. Exactly the entire dev tools isn't here. I can do the same thing, selecting elements and trying to see exactly what it is. The last thing that we have here, which I think is pretty cool, is actually something that some of the engineers on our team recently added. It's called the emulation toolbar. And what this means is now I can click on this button. This is the emulation toolbar. You can set the dimensions, DPR, the scale. The devices. Exactly. So now I can put this into mobile mode. I'm scrolling using my mouse like this. I can also select some presets here and it'll change

**[5:35](https://www.youtube.com/watch?v=u06ybMn4W1s&t=335s)** based on the those dimensions. So this will be really easy for just quick and easy mobile developments. OK, now I have a question for you. Can the agent drive this browser without further integrations required? Like do I need playwright, agent, browser, all that stuff? Exactly. This is actually something that we added and you actually don't need anything else besides everything that we have built in VS Code to have the agent drive this. So I'm going to go ahead and click on this button here it says share with agent and I'm going to remove these for now. Oh and. I see the glowing border. Yeah, so the glowing border means we're now sharing the browser with the agents. Or it means you're talking to Siri. One of the two. For copyright purposes. We'll cut that, cut that from the bottom. As we're showing Pokémon on the. Screen. Jeez.

**[6:22](https://www.youtube.com/watch?v=u06ybMn4W1s&t=382s)** But really quickly here, I'll ask the agent to navigate to the calculator tab and run some tests. I spelled tests wrong, but it. Should do the. Job, so we'll let it work A. Little bit adjusting the warp Dr. I like that. Can you add those too? I did add those too. Fun little. I did add fun little little tidbits. But yeah, you can see here, it took a screenshot first to try to just kind of try to see where exactly it is. It's going to do some searches. Now, while this is running, the other thing that's pretty important about You don't like yellow though. I wanted to keep it off for dramatic purposes. OK. One of the things that's important about being able to pick elements is that that's Friday.

**[7:10](https://www.youtube.com/watch?v=u06ybMn4W1s&t=430s)** Like, I don't know if y'all know, but tokens are expensive now, more expensive than they were three months ago. And so a lot of times you'll say like like if you're messing with the NAV bar. I, I'm guilty of this because we have unlimited tokens and so we don't we don't live in reality, right? It's one of the best perks of the job. But instead of saying like I, I want to XXX with the NAV bar, then the agent has to go grab your files and find out where the NAV bar is. And agents are like post trained on grab and they just go nuts. They will read every single file that may even have remotely to do with the NAV bar, and you know, 2 million input tokens later, you get the result. It's much, much better if you go click and add the element and then the agent doesn't have to go do that.

**[7:55](https://www.youtube.com/watch?v=u06ybMn4W1s&t=475s)** I can't stress this enough. If you want to save tokens, stop giving the agent vague instructions. Tell it exactly which file. Pick the element. Otherwise you're going to burn millions of input tokens with the agent having to find things itself. You do not want that, OK. It's unfortunate that you're talking about that and the agent currently is actually having a hard time finding the calculator tab. It's doing the exact. Same thing that you said. So yeah, to kind of try to debug all of this, I'm actually just going to have it relaunch and launch the app. I like your. You've got some great prompts there, LAKSJDHLAKSD. Very, very generic and on some tests, yeah. So this is kind of the full end to end

**[8:46](https://www.youtube.com/watch?v=u06ybMn4W1s&t=526s)** workflow of it going to the calculator tab, it'll launch. I had a great demo of it going through and like clicking on a bunch of stuff. But unfortunately the gods, the gods said no, the gods said no. One really quick thing is that we actually have playwright integration with this as well. So I mean, it's doing the thing now. We have player integration with this as well. So one of the things I showed off earlier was the emulation toolbar. With the emulation toolbar, it's actually really great because you can go through and through Playwright, it'll run code and it can do things like, oh, I'm going to change the viewport. So I mean, we see this working now. So really quickly, let's just say test in different viewports. And instead of using these browser tools that I just showed off here where it just went and did a bunch of clicking. Now it's going to read the read the page and run some playwright mode which will test and take screenshots

**[9:36](https://www.youtube.com/watch?v=u06ybMn4W1s&t=576s)** of different viewports, different scale, like different sizes and it will do all of that for you directly in player. And this is all in VS Code. There's nothing you need to install, there's nothing else you need to install, and you get it for free. You're giving away the integrated browser. Exactly. Exactly. One time offer, if you don't like the integrated browser, you get your money back. All right, Justin, thank you so much for being here. Randall Cluster. Justin, we'll be right back, folks. Thank you.
