---
id: lbaXnx0KLA8
title: "MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed"
slug: mcp-apps-give-the-model-data-give-the-user-a-ui-dustin
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Dustin Mihalik"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-09-09T15:30:08Z
video_id: lbaXnx0KLA8
url: https://www.youtube.com/watch?v=lbaXnx0KLA8
youtube_url: https://www.youtube.com/watch?v=lbaXnx0KLA8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration"]
transcript: true
---

# MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed

**Dustin Mihalik**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lbaXnx0KLA8) · [Conference site](https://www.ai.engineer/)

## Description

Adding a nice interface made the product worse. With plain text results the model would run ten or fifteen job searches, filter them, and assemble a table. Once a rendering widget was attached, it called the tool once, saw results already on screen, and stopped exploring. Dustin Mihalik is a technical fellow at Indeed working on AI platform and guardrails, and this is a lessons from the trenches account of building MCP apps for Claude, ChatGPT, and Indeed's own job seeker agent. He starts with why a UI is worth having. A text response carries no branding, and getting a host chat app to link out is genuinely hard, since it would rather you stayed; hours of eval work went into that alone. A widget gives you an apply button and a detail view without leaving the conversation.

Then three rules. Anything shown to the user must also reach the model as data, or the widget is a black box and every follow up question fails. The tool description has to say a UI exists, otherwise the model narrates the same results underneath it. And the rule that supersedes the others, separate data processing from UI rendering. At Indeed that meant a plain search tool the model can call freely, plus a render widget taking a list of ids, so it can search a hundred jobs, filter to five, and show only those. Interactions need the same treatment, pushed back through update model context, or the model cannot tell which job was opened. He closes on data first design, small composable tools, and letting the render tool carry the model's own reasoning about why a result fits.

Speaker info:
- https://www.linkedin.com/in/dmihalik/
- https://dmihalik.com

Timestamps:
0:00 - MCP apps at Indeed, and why UI matters
1:22 - Text based results, and the linking problem
3:13 - Rule one, show the model everything you show the user
5:06 - Rule two, tell the description a UI exists
6:16 - Interactions the model cannot see
8:19 - Rule three, split data processing from rendering
10:50 - A search tool and a separate render tool
12:39 - Letting the model add its own reasoning
13:34 - Takeaways, data first and small composable tools

## Transcript

*2,615 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=1s)** [music] >> Uh hey everyone, I'm Dustin Macholic. Uh I work at Indeed. Uh we're the number one job site in the world. And I have to apologize for my voice. I'm recovering from a cold that I had last week. Um Yeah, so at Indeed, we build uh job search. And uh I also work on a team that does AI platform. And I do like AI guardrails and and gateways and compliance stuff. Uh occasionally uh my team gets cool projects to work on because we have relationships with the vendors. Uh MCP apps is one of those.

**[0:49](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=49s)** And um MCP connectors. So, this is a little bit of like practical MCP apps. They gave a great introduction uh to MCP apps. This is a little bit of a lessons from the trenches, uh which is a little bit of like what did we learn in building MCP and MCP apps for Claude chat chat GPT and our own internal uh uh career scout, which is our uh agent that we have for job seekers. So, this is the this is the chat-based interface. So, a lot of my examples are going to be job search. This will I have a lot of screenshots of job searches. Um So, this is this is a job search, which is basically uh you know, I'm looking for barista in Austin. And this is a text-based response. And this works pretty well. Uh as we kind of discussed,

**[1:40](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=100s)** like there's no branding here. There's no Indeed branding. Uh you know, Claude decided to say these are some jobs in Austin. These are some jobs in some suburbs of Austin. That's cool. That's probably good for the user. There may be some limitations uh of like what we can do for branding or how we can uh you know, how we can control things. And you'd be actually be surprised uh unless you've tried to do this yourself that um it's really hard to get Claude or ChatGPT to link to things cuz they don't want you to leave their environment. It makes complete sense, but uh if you get back, here's five jobs that are somewhere on the internet uh without any links, that's a terrible user experience. Uh so it's it took us a ridiculous number of hours and evals to

**[2:29](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=149s)** make sure that like Claude would consistently link to things. So with MCP apps and with uh apps SDK, uh we could kind of control that. Uh we can decide uh you know, that we've got an apply button. We can decide what stuff is important that we want to highlight at the top. We can provide a link to view details um so that when you click it, you get uh a a pop-up, a a modal that has all the job details so you don't have to leave the environment. So it's it's a win-win uh for for both for both uh for both companies. So uh MCP apps is really good, but if you're thinking about hey, I want to build an MCP app or I want to take my

**[3:16](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=196s)** website, I want to put it in ChatGPT or Claude, uh it's not quite just as easy as like dragging and dropping into a chat interface. Uh you really want to think about how you are representing the data, how you're making it available to the user. So if you do a very naive thing, uh which is you still call your existing APIs uh for loading data, um then it basically becomes a black box to the model, right? So you say, "Hey, I want to do something." The model says, "Cool, I'll call a tool." The tool says, "Okay, I'm going to show some stuff, but the model has no idea what what you're displaying." So, there's all these like follow-up questions, like tell me about the first result, or please rank this list of

**[4:03](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=243s)** companies. The model has no idea what data is being displayed. So, the very first rule uh for me uh building MCP apps, anything that you show to the user also needs to be provided as data to the model. I think this makes sense, but uh I've definitely seen some MCP apps where they just, you know, use it to inject some HTML on the page and then call some APIs, uh and that's that just makes a big black box for the model. So, this is really easy to do uh using MCP spec and the MCP app spec. Uh this structured content, this is what you would already be returning if you were doing just text-based MCP. Um and then this resource URI, that's points to where the HTML is. You need to return both of these, and you need to keep them

**[4:51](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=291s)** in sync, right? If you add something new to the API, you make sure you add something add that same data uh back. So, kind of the next step um that uh that once you do that, uh you'll find is that now you've provided data to the model, and you provided this black box that it has no idea about, it's still going to try and describe the it's still going to try and take the output and describe it as it normally would. So, you end up with like, "Here's your display." and then here's the model doing basically the same thing that it would normally do. Um so, what you need to do is you need to update your description in order to tell it that you're going to be displaying stuff in your MCP app. Uh that way you get this like nice, you

**[5:39](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=339s)** know, here's a list of you know, here's a little summary of things, and you know, the results are are are showed above the links, rather than it trying to like do a whole text-based display. Um you'll end up with this a little bit of a battle between like what gets displayed in UI and what gets displayed by the model. You can try and steer that with descriptions. So, even something as simple as results were automatically displayed to the user as UI components at the top of your description, your tool description, uh that covers that covers quite a bit of the cases. Um So, that's one of the next things that you're going to want to do uh once you're providing both data and API access. Uh the next thing is there's these

**[6:26](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=386s)** interactable pieces, right? There's the apply button, there's a view details button, which pops up a big job description. Um this is the same case where, you know, as you interact with those, the model's not going to know necessarily what you're looking at. So, you click view details, you get a big modal that's here's everything about the job. There's once again a whole bunch of questions that the user could ask. Uh write a cover letter for this job, summarize this job description. It has no idea because you've loaded that data in either in via API or you loaded it in dynamically, uh you know, hit you return 10 jobs and user clicks on one, the model has no idea which one you clicked on. Uh so, any information about user interactions, you also need to provide

**[7:17](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=437s)** to the model. And uh once again, MCP abstract has a pretty easy way to handle it. There's this update model context um method, which lets you pass in a string uh that is So, for MCP apps, there's a single string. Uh so, if you like want to track multiple events over time, you kind of have to append uh multiple things to the string, but this is this is this is an example from the MCP apps uh documentation where basically, you know, this is a shopping cart application and they add the total cost and all the items that are on the shopping cart so the user can ask for uh you know, "Tell me information about the items that are in my shopping cart." >> [snorts]

**[8:05](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=485s)** >> So, these two things give you an app that like the model could kind of see what's going on. Um but it doesn't necessarily make a really good MCP app yet uh because it gives you it gives you some UI that looks like what you want, but the thing that I usually do, I don't give I don't give the I don't I don't give Claude uh my easy problems to solve. I give Claude my really hard problems to solve, right? Like if I just wanted to do one search, I would go to the web and do one search. I want to do a whole bunch of searches. Uh this is this is out of date cuz there's no Sonic 5 here yet, but uh this is screenshot from 2 days ago. Uh but yeah, so that So, like this job

**[8:53](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=533s)** search is "Hey, I'm looking for this I'm looking for this title. I'm willing to relocate, so I want to search across a whole bunch of different cities. Um you know, I'm looking for the highest paying option, so I want you to just cherry-pick a few out of there. There's some industries that I absolutely don't want to work in." Text-based MCP does really well. Like we all see this, right? Claude will do 10 different searches, 15 different searches. It'll filter, it'll pull out all the individual pieces, uh and then it gives you a nice table at the bottom, uh which is which is super nice. >> [snorts] >> But with the MCP app that we were just discussing, you know, we we said, "Hey, uh you know, my results are going to be displayed in this UI. Uh

**[9:43](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=583s)** We know Claude Claude will call it once and then it'll be like, "Oh, I guess the results are already displayed. I'm not going to like do a deep dive, right?" Like it doesn't It's you as a user are not going to want 10 different carousels and Claude will also notice that like it's already been displaying some stuff and it won't call to show 10 different carousels. Um and so what you really want to do, and this is rule three, this like supersedes all the other rules, uh which is basically you want to separate your data processing from your UI rendering. And this particular wording I stole uh from OpenAI uh >> [snorts] >> OpenAI uh Apps SDK documentation. There's a couple places where they say this.

**[10:32](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=632s)** Um but basically they want to You want to separate your data processing from your UI rendering. So the job search that we had we're just going to have that be a standard text-based MCP application. Claude can call that as many times as it wants. And then we have a render tool that either you can pass you can have the model basically pass all the data that it wants to render in or you can do a reference uh to it. So in our particular case uh you know, we had search jobs. Now we have a search jobs that doesn't return any UI and we have a render jobs widget that takes a list of IDs. Um and so that list of IDs uh

**[11:18](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=678s)** can be, you know, Claude can do a search. It can get a hundred different jobs that it cares about. It can filter those. It can find five that it cares about and it can show those five to the user. Um now as you make these like render uh as you make these render calls, you need to update the descriptions to say like where did they get the data, what format the data should be. But it's a fairly easy fairly easy mechanism to update your tool description to say you need to always call one of these three tools first in order to get the data that you're going to be using for rendering. So, search jobs, this is a pretty good um It's a pretty good example of of how we where we want to split data

**[12:06](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=726s)** from rendering. I think there's a ton of other like in most industries, you can kind of come up with like, "Hey, where do I want to you know, where do I want to split?" Like I want to be I want the model to be able to explore this data and then I want it to turn around and choose to be able to render it. Right? Like there's there's examples of you know e-commerce, right? Like a bunch of e-commerce options. If you've got a map, you know, maybe you want to come up with like five different addresses and then you pass in addresses. The other thing that you can do is you can let the model be a lot more creative. Like one of the things that we've seen in some of this text-based stuff is that you know, the model will say like, "This

**[12:53](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=773s)** is a >> [clears throat] >> This is a reason why I picked this one." Or "This is a reason why this is really good." And so, you know, potentially we can add something to the render jobs widget where you say give us an ID and a reason why you think that this is a good fit. Or give us an ID and highlight a section of the job description that is really good. Um, so you can get really creative with your render tools to be able to have to be able to give some extra character that the model can inject into those so that so that you've got a much better experience for the user. So [snorts] the key takeaways right when building MCP apps, you want to focus on the data before you focus on

**[13:42](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=822s)** the UI which sounds sounds opposite of you know how we were thinking about it of like hey there's all these there's these MCP apps like it's how I put UI into chat GPT. I think if you want to really have a good MCP apps experience, you need to you need to look at and see what data do I want to what data do I want to give to the model, what data do I want it to be able to do and then rendering is a side effect of of that or it's a result of the the model exploring the data. And then I think small composable tools, right? So uh basically, you know maybe there's like two or three different ways you can search for jobs. We could build two or three different

**[14:28](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=868s)** search tools and then there's one render tool or maybe there's like maybe there's two render tools there's one that's render a list of jobs, one that's, you know, highlight one particular job. So you could build a bunch of much smaller tools. The descriptions can be fairly simple so you don't overload the model, but it gives the model flexibility about how it wants to explore the data and how it wants to render the tools. So that's basically basically my talk. I'm a few minutes few minutes fast. But I don't have a booth that I'm going to hang out in, but I'll I'll hang out in the hall if anyone has any questions. And I am either my last name or my first initial last name on most social media platforms.

**[15:15](https://www.youtube.com/watch?v=lbaXnx0KLA8&t=915s)** Thank you. >> [music] >> Mhm.
