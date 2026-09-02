---
id: ND7l5R8evoQ
title: "The PM/dev handoff isn't what it used to be | LIVE167"
slug: the-pm-dev-handoff-isn-t-what-it-used-to-be-live167
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Courtney Webster", "Burke Holland"]
channel: "Visual Studio Code"
duration_min: 13
published_at: 2026-06-05T13:42:09Z
video_id: ND7l5R8evoQ
url: https://www.youtube.com/watch?v=ND7l5R8evoQ
youtube_url: https://www.youtube.com/watch?v=ND7l5R8evoQ
tags: ["Burke Holland", "Courtney Webster", "LIVE167", "LIVE167_v1", "The PM/dev handoff isn't what it used to be | LIVE167", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# The PM/dev handoff isn't what it used to be | LIVE167

**Courtney Webster, Burke Holland**

`Microsoft Build` · `Build 2026` · `2026` · `13 min`

`#Burke Holland` `#Courtney Webster` `#LIVE167` `#LIVE167_v1` `#The PM/dev handoff isn't what it used to be | LIVE167` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=ND7l5R8evoQ) · [Conference site](https://build.microsoft.com/)

## Description

The PM to dev handoff used to mean a document nobody loved reading and a long wait to find out if the idea actually worked. When agents can take a vague idea to a working pull request in a day, the whole loop changes. This session is about what that means for how product and engineering work together now and what a faster, prototype-first culture actually looks like on a team shipping weekly.

To learn more, please check out these resources:
* https://aka.ms/VSCode/AIBlog
* https://aka.ms/VSCode/Learn
* https://aka.ms/VSCode/Build26/BRK204
* https://code.visualstudio.com/blogs/2026/03/13/how-VS-Code-Builds-with-AI

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Courtney Webster
* Burke Holland

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE167 | English (US)

Broadcast Stage

Related Sessions:
BRK204 -- https://build.microsoft.com/sessions/BRK204?wt.mc_id=yt_

#MSBuild

Chapters:
0:00 - Intro and guest introduction – Courtney from the VS Code team joins to discuss changing AI tools
00:00:35 - Adapting to AI in product management workflows
00:01:19 - Traditional PM work vs. AI-enabled faster iteration cycles
00:02:00 - PMs contributing directly in codebases and submitting PRs
00:02:31 - Shift from long documentation loops to real-time feedback and prototyping
00:04:33 - Demo: Improving VS Code settings navigation based on user feedback
00:06:40 - AI-assisted development cycle – from PR creation to merge within a day
00:07:11 - Challenges in PR review volume and managing AI-driven work
00:08:26 - Showcase of another prototype for tool permissions and customization
00:11:17 - Encouragement to experiment with AI-driven workflows and closing remarks

## Transcript

*2,601 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=0s)** Hey, welcome back, everybody. Now listen, folks, I don't know if you've noticed, but things are a little bit different these days. They've changed a little bit in the past, yes. And no one knows that better than our next guest who is having to live this and figure this out every single day. This is Courtney APM on the VS Code team. And yeah, we're going to, yeah, thank you for being here. I'm excited to actually hear about this because I'm curious, like how you're doing. They're like, we're building the tools and in order to understand how they're useful, we have to use them. But there's no instructions on how to do that. So tell me a bit about what what you're doing, how you're using AI to do PM work. Yeah every. Like you said, everything's changing. Everything's different these days, but we're all just, we're, we're

**[0:50](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=50s)** using the tools day in and day out and so constantly experimenting with new ways of working and changing how we're approaching agents and AI in general. And so the PM role, I think how I've seen it change in the last couple years or I guess a year and a half feels a lot longer than that sometimes. Kind of slowed down. Do you see that move where it's like it's from Interstellar, where he's like this little move is gonna cost us five years Like that's how it. Feels. That's how it feels, yeah. But I mean prior to AIA, lot of the PM work was very much like document driven. So it was classic like, OK, let me go surface some user feedback from different channels, different formats, and then kind of aggregate all of those learnings, turn them into a document, make sure the documents formatted well, all of the words fit together perfectly.

**[1:40](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=100s)** And then I'm going to pass it off to engineering to hopefully get a buy in. And now these days that feedback loop and the like iterations of all of this is a lot more condensed to where PMS are able to like go through the cycle multiple times in a day, even in prototype a lot easier. So in the past year I've spent a lot more time with the code base than I ever have before, which has been a great learning experience. Yes, and you push some PRS, I know because I've used some features and you're like, hey, who added this? They're like Courtney added that. Oh sweet. The PM team is surprisingly in the code base and pushing PRS often. They're not always merged, not always even undrafted. But right, you're unceremoniously rejected. Yeah. So what you're saying is you're working much less now. Life is easy. It's a breeze. The agent does everything. I'm chilling. You're like four days a week tops.

**[2:27](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=147s)** Tops. Yeah, the four day work week is happening on the VS Code team actively. Now I have the note here that says there's kind of a new world that we're in where, you know, you get we we we get user feedback on X and Reddit, boy, do we get user feedback. Let me tell you. And then right by the end of the day, that's in APR, sometimes like that's the new flow, whereas before it was kind of like, all right, we'll put that on the backlog. Right. Or it was like, we'll wait for someone to create an issue that has all of the information, all of the repro, anything like that. And now it's like, oh, someone posted on Reddit at 11 AM, let's go explore this, try to dig into it a little bit more. And then if we see it's a real problem or a problem space that we see emerging, we're able to kind of go explore prototypes, iterate on it, and then

**[3:17](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=197s)** bring that to engineering with both like the problem, the user feedback, as well as a not always a working solution, but like a prototype at. Least a prototype which? Is nice because like I said previously, a lot of this work was in documents and so you I as APM, wasn't able to do all of my due diligence. Obviously I wasn't able to and I'm still not able to make all of the right architectural decisions or know the right code quality. That's definitely still the engineering domain for sure. But the agents can do a lot of that initial like code scanning iterations of prototypes to a point where I can have gone through enough like UI, different designs or different edge cases or finding different things. And there before I'm bringing it to the engineering managers and the engineering team.

**[4:04](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=244s)** And then they're able to do kind of that last mile work on the PR potentially, or they're able to take it and be like, OK, I have a much better idea of the user scenarios, the user pane or just like where your head's at rather than having to go read a long doc or try to explain it in series of meetings and right constant. Right, like what you imagine in your head is not with the person reading the issue of just. And there, read your mind. I don't know exactly. That yeah. So do you have like examples or demos here you can. Show us. Yeah. So here's one small, small thing I did. So we were getting a lot of VS Code is super customizable. It's one of the beauties of VS Code, but it also can be hard to navigate at times. So this was back and I think February, we were getting a lot of feedback where people were like if you have the setting, can we do this in VS Code?

**[4:51](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=291s)** Like how do I navigate chat related settings because I don't even know where to begin. What is this 1 specifically? So it was making the settings editor a little bit more navigable. So we were going to bring reorganize some of the chat related settings and then instead of having endless scrolling on the chat panel, we're going to have it paginated so I can kind of. Yes, just show me the example there so I know what you're talking. About setting, oh, that's not the one I wanted. I'm in my VS Code now let's go here. So for example, this, it looks pretty much the same. Like I said, it's more of just like a RE architecture right? But so previously if I scroll to the bottom here, I would have just kept going. Oh, that's right, it just and the left side moves down as. You scroll and so now it's paginated, so it's much more organized and things like that, as well as moving

**[5:40](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=340s)** this chat as a top level setting so it could be a little bit more discoverable. Gotcha. And so, yeah, this is one of the biggest pieces of feedback we get is that this is hard. It's. Hard to find to understand. And so I was like, OK, we've been we've been seeing this on Reddit, we've been seeing this in issues we see this on on X people are constantly like what? How do I even begin here? So I started like maybe iterations with some designers, some quick slack messages back and forth. And then I put put it in APR and I sent it over to the engineering team and I was like, what do you think about this? Like do you have any other ideas in addition to just some of these like low hanging changes that we can make in the UI to just test the experience? So I put it into APR and then had Copilot do a code review for me, which was great.

**[6:28](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=388s)** I got some feedback and was able to keep iterating. And then the engineering team just went ahead and jumped into this PR, did some last mile work, last mile changes, and then we were ultimately able to to merge this into the. Code. What's the timeline there from? Like open to a. Day. 1 to 24 hours. All in a day, which was really nice. And then the engineering team was able to then go figure out how to continue to like iterate on the settings experience to make it more discoverable. Is, is that harder for people like is, you know, like Josh, I think works like way down on the like quality because like the people that are down on the end of this, in other words, like if you're submitting PRS and I started doing that too, like aren't the people way down the line then getting pummeled? Yeah, inundated with PRS, yeah, yeah, I, I that's definitely a problem.

**[7:15](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=435s)** And I think that's what we're seeing on our team as well is like it's not the, the code is not the as much the blocker anymore, but more like being able to review, review the PRS but also understand like the quality gates. And I think that's something as APM too, is I all of my explorations that I'm doing in the code base, not all of them. I'm going to go send to engineering to be like review this PRI need to go make it into the code base. A lot of some of my explorations never make it into APR and I'm able to just like kind of type of my learnings a little bit more in an issue point to specific code, maybe attach a prototype that has is wouldn't go work in production at all. But then engineering is able to kind of go take it when they have a moment to to add it on to their iteration plan. So I think you have to kind of measure what you're sending to engineering as APM, but you're able to,

**[8:05](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=485s)** like I said, iterate on some of these solutions a lot faster and figure out like, oh, in my head that that felt a lot better. But when I actually put it into. The product, yeah, it doesn't make sense. Yeah interesting. And so you kind of have to check yourself on those as well. But one of my one of my Co workers has a really cool Harold. I don't know if he's joining you on on this stage. Lately never heard of him. We don't know Harold, yeah, but he, this is a, a prototype that he did. And this is not like a PR, this isn't in the code base at all, but is just kind of a working prototype that he sent to engineering to expand the customizations UI that we're doing to also include tool permissions. Because we found that tool permissions are scattered through a lot of different settings, and there's not a good central

**[8:54](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=534s)** way to understand which permissions you've set for. Oh yeah. It's impossible. Yeah. And so he mocked up this UI to send to the engineering team for feedback because he was like, we already have this UI. People are giving us good feedback on it. Like what if we extended the site, this concept to permissions as well? And so this was a working prototype that he was able to send to engineering, get some feedback on and but it never made it to APR. It was just kind of a proof of concept. So because this looks like the UI that's in the agents. Yeah, but it's it's not. Is it the same one? And he just added the tool. Yeah OK. So in my VS Code, this is what that UI looks like today. It just covers customizations. OK but he was basically saying like what could it look like if it also covered permissions? Like is that something?

**[9:41](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=581s)** That would fit. Well into this model. Yeah, it's crazy now that we can just sort of build essentially the feature and it's like, OK, here's the feature. Not really, but for all intents and purposes. And then once you see it in action, you can be you do have this I because I've done this where I've you should try this for open APR and issue and mock up the thing that you're trying to open it. And by the time you do it, you'll be like actually don't want to open this issue. Yeah no you. Realize this is like actually not a good idea. Yeah no. And I think that's helpful too. And it, it makes us as PMS kind of evaluate the user experience like from a zoomed out perspective a lot more as well. Because before we would just zoom in on one particular issue and kind of try to move that along in the in the iteration plan. And now we're able be able to kind of see and feel a lot of this stuff in early stages

**[10:29](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=629s)** and be able to evaluate the user experience and the user delight much faster than if we were in without AI in our in our. Yeah, it's phenomenal. I'm curious from the audience here, how many folks are using AI to open issues, not PR is just issues like when you have issues couple just a couple of folks. Interesting. So that's another thing. Go back and try this because we do this as well. It's when you find an issue and you're in VS Code and you have the agent open, don't open an issue. Just go to the agent and tell the agent to open an issue. And if it's writing verbose issues, give it instructions to stop writing verbose issues, right? Explain as quickly as possible, provide reproduction steps and this is how we open issues anymore is just have the AI do it. Yeah. So, yeah, I mean, the, I think everyone's kind of roles are evolving with AI.

**[11:17](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=677s)** They're getting a lot different. But I think my role as APM has, I've learned a lot more about the the product and the code base itself as well. And it's enabled me to spend a lot more time on like synthesizing all of the different user feedback that you get. We talked about Reddit, we talked about X. We also have so many issues, you know, and so we're able to kind of gather those different sources and then prototype in in the code base and then help our engineering partners a lot better. Yeah, in this new way of working. Yeah, it's super interesting. I know we're out of time here, but the, you know, from the, from the diametrically opposed views of like AI is going to replace people to oh, no, actually, you're doing way more and you're way more in the, in the details than you were before. Right.

**[12:03](https://www.youtube.com/watch?v=ND7l5R8evoQ&t=723s)** And like, PMS are doing way more than they were before in terms of the scope of work and what AI enables you. I'm finding the same thing, by the way. Yeah. Same exact thing. Yeah. But it's cool because at the same time we're able to work with a lot more, like different teams as well. So I get to work with with you a lot more, the engineering team a lot more different ways. So definitely encourage people to kind of experiment with different ways of working with AI and with their team as well. Awesome. All right, Courtney, thank you so much. Please give Courtney a round of applause and we will be right back.
