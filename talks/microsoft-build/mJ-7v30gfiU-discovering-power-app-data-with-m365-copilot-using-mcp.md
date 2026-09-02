---
id: mJ-7v30gfiU
title: "Discovering Power App Data with M365 Copilot using MCP | DEM360"
slug: discovering-power-app-data-with-m365-copilot-using-mcp
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Christine Flora"]
channel: "Microsoft Developer"
duration_min: 20
published_at: 2026-07-02T18:22:57Z
video_id: mJ-7v30gfiU
url: https://www.youtube.com/watch?v=mJ-7v30gfiU
youtube_url: https://www.youtube.com/watch?v=mJ-7v30gfiU
tags: ["Azure", "Microsoft", "Tech", "Technology", "Dev", "Development", "Cloud Computing"]
topics: ["Agents & orchestration"]
transcript: true
---

# Discovering Power App Data with M365 Copilot using MCP | DEM360

**Christine Flora**

`Microsoft Build` · `Build 2026` · `2026` · `20 min`

`#Azure` `#Microsoft` `#Tech` `#Technology` `#Dev` `#Development` `#Cloud Computing`

[Watch the recording](https://www.youtube.com/watch?v=mJ-7v30gfiU) · [Conference site](https://build.microsoft.com/)

## Description

With millions of users world-wide, Power Apps and Dataverse now sit atop critical business data, but developers face challenges with discoverability and schema understanding. This session introduces Power Apps Model Context Protocol (MCP), which empowers M365 Copilot to access app metadata, Dataverse schemas, relationships, and permissions. Learn how MCP enables Copilot to answer natural-language queries, aggregate data, and deliver real-time insights, plus best practices for Copilot-ready apps.

Seating for this session is first-come, first-served. Add it to your schedule to plan your day and arrive early to secure a spot.

To learn more, please check out these resources:
* https://aka.ms/build26-next-steps

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Christine Flora

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

DEM360 | English (US) | Agents & apps

Demo | (200) Intermediate

#MSBuild

## Transcript

*3,251 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=0s)** Yeah, hi. Good afternoon. Thanks for coming to this session. This is DEM 360. I'm Christine Fora. I've been working in Power Platform and Power Apps for over 15 years now. I'm a Microsoft MVP in Power Apps, as well as an MCP. Uh today we're going to be talking about um uh Power Apps and the new uh Power Apps MCP tool, why it's important. We're going to do a little bit of grounding on why it's important and how it can open up the ability to securely expose your data with the context of M365 including Outlook, Excel, Word, uh Teams, and of course Copilot and Copilot Studio. Then we're going to talk about uh we're going to actually uh

**[0:48](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=48s)** look at how to enable your uh Power Apps um for the MCP, as well as create a custom tool associated with it that you can then upload for richer experiences with your data in M365, just like somebody's in your app. Uh then we're going to cover and finish it off with uh how some of the prerequisites that you need to do this so that you can go and play and um work and create your own custom tools, and then we're going to um finish up uh with some links. So let's get started. Um So why Power Apps MCP? Uh MCPs are the kind of like the universal translator for agentic experiences these days. They uh

**[1:35](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=95s)** work and give you basic capabilities into uh writing and uh basic credit information. And Power Apps is basically in Power Platform is a suite of tools that enables business subject matter experts and professional developers to create mission-critical solutions uh automate processes, uh analyze data, and even create AI solution AI-driven solutions using connected data. Uh all without needing deep technical skills. It enables and empowers business users to rapidly solve business uh solutions with their own expertise cuz they know their data and their problems better than almost anybody using uh wizzy wig layout tools and

**[2:24](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=144s)** natural language prompts to build data uh structures and even whole solutions. It also enables traditional developers to build and extend using advanced capabilities like VS Code, Claude, GitHub Copilot, DevOps Git, and even Copilot Studio. And especially Copilot Studio. As I said, MCPs are like a universal translator for today's today's Agionic including the just announced Autopilots and Work IQ. Um I've some additional uh slides within this uh presentation for you to go in and look. I'm not going to read these cuz I think that our time you guys really want to see this in action. So, let's take a look at that. And uh I'm going to be hopping around a

**[3:12](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=192s)** bit uh between a a bunch of different tools. I'm going to be in Power Apps and the Maker portal. I'm going to be in VS Code with Claude. And also, of course, I'm going to be in M365 to demo this functionality. So, as I jump between the different tools, I'll uh tell you what I'm jumping to so you know where I'm at and uh you can follow along when you do your own uh testing and playing around with this uh awesome capability. For this um demo, I actually created a equipment maintenance application. It allows me to uh see uh upcoming work orders, everything about my equipment, it when they were purchased, any inspections that were made,

**[4:00](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=240s)** work order information so that we can keep up on keeping them in work order and available to do work on the shop floor. This is a power app and as you can see it's a very rich and visual, but I want to be able to expose that data for users of this application no matter where they're at including M365. So, if I go over to Copilot, so I was in Power Apps over here. Now I'm going over to Copilot. I have this new chat. If I just do this show work orders, it's not going to see anything beyond the context of M365. It'll look in my SharePoint drive, it'll on my OneDrive, on my works and what you're going to see

**[4:47](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=287s)** is it's going to see some sample data that I did in preparing for this demo, but it's really limited and it's not showing any of the data within the Power App that I just showed you for equipment maintenance. But, with the MCP and the Power Apps, I can actually create a declarative agent that will let people see my data within the context of M365. Just by at mentioning this declarative agent that I've already uploaded into my M365. If I do that same that same prompt, now what it's going to do because I have declared on this agent, I it'll go out to my application and

**[5:36](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=336s)** bring back the information that I requested in this format as a list. Now this is a live look at my data, there's nothing static about it. I can change the sorting and select it just like I am in my application. I can even drill down and look into the record that I want to see without having to go into my app outside. And I can do this in Word, Outlook, Excel, as well as here within Copilot. Uh, this is a very rich uh UI as you can see as it is. Um, and if I were to say open right now, it would open my app straight from this record. So, that's a really great shortcut into

**[6:24](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=384s)** getting into the app. So, I'd have to go in my app, then I'd sort and select, and I don't want to do that, right? But, with MCP now and the release of being able to create our own custom tools, I can offer my users even more rich interaction and insights into my data. So, for example, if I say show my equipment work order status, this is a custom tool that I've created that allows me to show different aspects of it as well as cards and my equipment. So, as you can see, it came up and I have these KPIs and cards at the top as well as some pretty good graphics associated with it. And then I was able

**[7:12](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=432s)** to create a card for each type of machine or equipment that I have in my shop floor. It's coming straight from my application and I've styled it in a a really nice way and it's completely interactive so I can say show me open issues, show me work orders, and drill straight down into that piece of equipment. Now, another custom tool that I've done is let's say that I wanted to be able to do I want to see all my upcoming work orders and see if we have any kind of resource restrictions, am I missing anything? Um what does my schedule look like for uh work orders coming up in the next week, in the next 2 weeks, in the next 3 weeks. And I could probably do that over in my application,

**[8:02](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=482s)** but I wanted to provide this really rich UI associated. And as you can see, I've created this timeline and it shows um it's very it's a very live data. Look at my application, right? I can go I can hover over these things. I can change my uh granularity of when it looks like and even look at uh for example, I have this emergency work order that's in the past. I will want to follow up with that and the team that's associated with that by equipment and you can uh sort and select and make this UI as uh robust and as visual as you want. And it's so let's go take a look at how I would do this. So, I'm going to switch over. So, I'm leaving Copilot. I'm going to switch

**[8:51](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=531s)** over to the maker portal. Uh I've got my solution up and I'm going to go into my app and I'm going to look at settings. Now, in my settings, I want to go to upcoming cuz we're still in preview and I want to set this Copilot control to on and I want to enable this app for Copilot, which is uh creating this MCP. And you're going to click save. Now, what that does is it brings up this little squiggly. It'll be a new icon on your navigation board. And what you'll be able to see now is that I have not only the built-in tools that I was talking about. So, I have basic CRUD, create, edit records, see the view data, that kind of thing, but I also have the three custom tools that I did and you

**[9:38](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=578s)** saw two of these. You saw the status and then you saw the status line. And I can download this agent and upload it and I would be done. But let's create our custom tool. So I'm going to click create. Uh you need to name it. Right? And then I'm going to be able to see uh I need to provide the instructions for it Now I can choose whatever model that I want and whatever you're uh cleared for. And then I can do two things. I can start um putting my prompt in here or I can use this prompt assistant and if you've ever done any kind of prompting in AI Builder, you're going to get this right

**[10:26](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=626s)** away, right? So I can type something in, but what I'm going to do is I have this prompt already set. I'm going to pull this in. And we're going to take a look at it. So I have the idea of I want it to do uh week, month, quarter. I want it to show it as a timeline visual. I want to display my work orders. I want it to provide a data and here's really the secret sauce of this is that I want to add those fields, remember in the pop-up of the timeline? I want to add those fields that I want to show. Now I can add text, I can add Power FX, but I'm going to go over here to Dataverse. And I'm going to say look at my maintenance work orders. And now you can see that I have all of

**[11:15](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=675s)** the fields from that maintenance work order table that I can choose from. So I'm going to start uh clicking on the things I want. I want who requested it, uh priority. I think that's enough. Uh they're upcoming work orders so there's no start and end date, and I'm going to click add. Now, if my custom tool requires the information that comes back to be filtered in a certain way, I can certainly add that filter attribute here, but I'm not going to I'm not going to add a filter currently. And, um, then I'm going to choose test. Now, what this is going to do is it's going to take the information including the dataverse content that I added and create a JSON file that I'm going to use

**[12:05](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=725s)** in Visual Studio and the, um, MCP tool and skill over in Claude to create the UI that I need. I'm going to cut and paste this. I'm going to click next. And now I'm going to switch tools and I'm going to go to VS Code. >> [snorts] >> Now, over here I've set it up with all my prerequisites. We'll talk about that the the Power Platform skills, the plugin for Power Platform. I've signed into my Power Platform as a, um, user over there in a maker, and I've got my Claude code connected with Claude Code Pro. You can use, uh, GitHub Copilot Pro to do this. And then I'm going to initiate the skill. And so, as you could see Claude knows the skills that I have loaded, and I'm going to choose this

**[12:53](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=773s)** MCP. And what this is going to do is it's going to go out and, uh, look at what this is, and it says, "I need two things, right? I need, uh, description and the tool." So, I'm going to add that into I'm going to add that into Claude. And then, I'm going to add that, uh, JSON from Power Platform. And that is here. And this is just that Jason that uh JSON that I had, right? And then I'm going to tell it, go. Go. Go do your thing. Go Claude. Go sponking. Whatever, right? And it's going to use the skill that's

**[13:41](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=821s)** in this and create that UI. Now, this is going to take about This particular one took about 5 minutes. Um I'm not going to make us uh work around and try to do that. I already have that. So, I'm going to stop this and save my tokens. >> [laughter] >> And I'm going to go down here to this timeline. What it generated and I'm going to put this out like this. What it created was this Fluent UI uh code that I'm going to paste back in my MCP. Now, uh I can if I know Fluent UI, I can go ahead and manually change this or I can use Claude to reiterate and change the things that are until I get it just right. I have visual person, I don't know about you guys, but uh I'm going to

**[14:30](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=870s)** go ahead and say show preview. And what you'll see is that now I can actually see and when I reiterate, I can actually look at that kind of thing and make my adjustments. So, it's got all this stuff that I have in here. It's looking at my live data. It used my JSON that I have. So, everything looks great. And I'm just going to cut and paste that. And now I'm going to switch over back to the Power Apps. And this uh when I said next, it went to the UI code. So, this is where you paste that UI code in here. So, I'm just going to cut and paste that straight in. And say save. Now, you'll see that I have that that uh

**[15:24](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=924s)** new custom uh tool. And don't forget, as with every power uh platform, you're going to need to publish that. And now the question is, how do we get that new tool and all that declarative stuff over in the M365? And this really great download, so you click on the download app. It's going to package that uh MCP up for you to be able to upload into M365. Now to upload into M365, you're going to need um either Teams upload permissions and publish permissions, or you're going to need to be a global admin, or work with your global admins to make that publish available. Notice this over here. And I have my Teams open uh here. And I'm going to go over into um

**[16:15](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=975s)** my Teams site and do the manage apps. And I'm going to They've changed just recently, so this might look a little different to you. And I'm going to say upload this app. Upload to my app catalog. And I'm going to choose that declarative agent. Tell I've been testing this for a bit and during the the build. And so here's my agent. I'm just going to select that. And I'm going to say upload. Now if you don't have publish permissions and things like that, then it needs to go through approval. You're going to have to do that. And then what will happen is then it will appear on your sidebar for you to use. And so what are the prerequisites for that? So a Power Apps license for both you as a developer and your users. So they need a Power Apps license to

**[17:03](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=1023s)** access your data. They also need permissions to use your data. So this is very securely um time boxed around that you need uh permissions to do what you say that you need to do and um M365 and they also need a Copilot license. So, as a user and a dev, you need that. Um you need on the Power Up side of things, you need to be a customizer or an admin role. And currently um the MCP is only supported in the in a model-driven app. They're working to um expose it and be able to create that for canvas apps and all the other like code apps and my code apps and things like that. And because it is in uh preview, you're going to need to be in the preview maker portal. So, if you can uh see here, uh let me um

**[17:52](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=1072s)** I'm in the preview maker portal. And then um on the widget side of things, I it took me about probably a half a day or so to set up my VS code for this. So, I have VS code, I have Node.js, I have Power Platform uh tools and skills. I also, as I mentioned at the top of this, is that you need GitHub uh Copilot Pro or Claude Code Pro in order to generate that skill. And then to finish it off, um I have some links in the deck. I'm going to be putting this uh it'll be in the session notes as well as in the GitHub repository that you'll be able to see. But these are uh links to the uh general information around uh how do you get the tools, how do you look at the skills

**[18:40](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=1120s)** repository, and some of the web uh components of Flow AI. And that's it. That is how you create skills. A kind of a whirlwind uh way to go. Um I really appreciate you attending my session. If you again, if you want to reach out and have any questions, uh some of the questions that came up during the session at Build were um is it currently in the uh G um the government cloud yet? And it's not. Uh it will follow that normal cadence around that Uh um as far as being able to I think there was a question around um being able to pass parameters and things like that to a cloud flow. Um it it would be um the same way as if you

**[19:31](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=1171s)** were doing any kind of data if your cloud flow is triggered off of a like a record out or something like that it would automatically cuz I'm just um when I'm adding a record or I'm adding in a record within M365 it's like I'm doing it right in the in the app itself. So any of those triggers would happen and um if you have external data sources depending on how you brought them in if there's a if it's a power apps data connector that you're using or uh you've created a virtual entity or table around that then you know those will work just like they work in um your power app. So just on questions feel free to reach out to me on LinkedIn or at my email I'm happy to record or respond to that. So appreciate you taking the time and uh I hope you found this session useful.

**[20:21](https://www.youtube.com/watch?v=mJ-7v30gfiU&t=1221s)** >> [music]
