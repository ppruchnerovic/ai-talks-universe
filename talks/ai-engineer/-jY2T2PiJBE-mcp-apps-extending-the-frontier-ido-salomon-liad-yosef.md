---
id: -jY2T2PiJBE
title: "MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef"
slug: mcp-apps-extending-the-frontier-ido-salomon-liad-yosef
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Ido Salomon", "Liad Yosef"]
channel: null
duration_min: 19
published_at: 2026-08-02T23:30:06Z
video_id: -jY2T2PiJBE
url: https://www.youtube.com/watch?v=-jY2T2PiJBE
youtube_url: https://www.youtube.com/watch?v=-jY2T2PiJBE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration"]
transcript: true
---

# MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef

**Ido Salomon, Liad Yosef**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=-jY2T2PiJBE) · [Conference site](https://www.ai.engineer/)

## Description

Chat and coding assistants still hand you walls of text when a button, a chart, or a small interactive view would say it faster. Liad Yosef, who co created MCP UI, walks through MCP Apps: a way for an MCP server to return a real interactive interface instead of a block of text, built on the MCP UI project he started and now shaped through an open working group in the MCP committee. A tool call links to a registered resource, the host renders it as a web component, and clicks flow back into the agentic loop, so the same funnel that would take a paragraph to explain becomes something you can see and act on at a glance.

The payoff is write once, run anywhere. Because it is a standard rather than a bespoke integration, a UI a server ships shows up across every host that supports it, and Yosef points to adoption by hosts and tools already in the ecosystem. He is candid that the spec is still evolving, with live work on how the app and the chat talk to each other and how apps interoperate, and an open invitation to contribute. The bigger bet is distribution: when a host reaches hundreds of millions of weekly users, a server that speaks MCP Apps reaches all of them at once.

Speaker info:
Liad Yosef
- https://x.com/liadyosef
- https://linkedin.com/in/liadyosef
- https://ora.ai

Ido Salomon
- https://x.com/idosal1
- https://www.linkedin.com/in/ido-salomon/

Timestamps:
0:00 - Why we need MCP Apps
1:52 - From walls of text to interactive views
2:29 - MCP UI, created and adopted
4:26 - An open working group in the MCP committee
5:04 - How a tool call becomes an interface
6:31 - Standardizing the flow
8:52 - The architecture: resources and web components
10:10 - Consuming apps through the browser
14:29 - What's still evolving in the spec
16:07 - Interoperability across hosts
17:14 - Write once, reach hundreds of millions

## Transcript

*3,260 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1s)** [music] >> Hi. So, hi everyone. We built this talk yesterday, so it might be out of date. I'm Ido Sadan, I am the creator of MCPY and co-creator and maintainer of MCP apps in the MCP steering committee. I also created Adam Craft if you were in the talk yesterday. >> I'm the Adi. I work with Ido on MCPY. I'm also the co-creator and maintainer of the MCP apps spec and recently co-founded Aura, which is a research lab for the agentic web. And we're going to talk a little bit more about it later. >> So, MCP apps are all around us. You might not even realize it, but all the

**[0:50](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=50s)** fancy apps you have today in ChatGPT and VS Code and Slack are actually all based on MCP and the MCP app spec. >> And if we take a step back and we ask, why do we need MCP apps? What's the idea behind MCPY or MCP apps? So, when we work with chats, when we chat client clients, we used to text because that's the natural interface, but text is really the worst way to convey a lot of information, right? Because we don't want walls of text. And actually, this is the main blocker from companies to build an MCP server. They don't want to be reduced to a textual database. They don't want to lose their brand identity in the process. They don't want their data that they work so hard on um building the UX for to look something like this.

**[1:37](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=97s)** So, instead of this, what if the apps could just send their UI to the chat, right? What if every service and every brand could just send their user interface to the chat? So, instead of us looking at something like this, we could just have the apps send their own identity, their own UI chunks into the chat, and then we take a look and we see, "Okay, yeah, I know this is Shopify in the middle. I know this is Hugging Face. I know this is Monday." And what if we don't want to do it only as a visualization? We also want to do it interactive. So, we want the users to be able to actually interact with Hugging Face, for example. And for Hugging Face to actually do something with it. >> So, we don't have to imagine the future as we said

**[2:26](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=146s)** with MCPUI, which I created in May last year, and took that, which is essentially like an open protocol for interactive applications over MCP. So, it's not only how you transmit UI, but also how that UI, that application connect connect communicates with the host. And just a few months ago, we partnered with Anthropic and OpenAI to create the official extension to MCP, which we call MCP apps based on MCPUI, MCP SDK, and other solutions in the field. Their launch was pretty cool with Claude and VS Code supporting it to begin with, but now obviously also OpenAI and others have adopted it. >> Yeah, and there are a lot of early

**[3:14](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=194s)** adopters to MCPUI. 11 Labs, Shopify, Postman. Those were one of the first first companies to support it back like a year ago. They were the one believing in this spec, in this vision. And Goose also supported it. And it's a it's a funny anecdote because today Block released their agentic commerce solution that is based on MCP apps. So, a year ago Goose was the first client to support MCPUI, and now it is part of Block's product uh product. And today we have a lot more clients that are supporting MCPUI. We We Cursor, and we have co-pilot and GitHub ChatGPT support MCP apps. ChatGPT apps that you know are actually based on MCP apps and open eye actually recommend

**[4:03](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=243s)** using MCP apps as the protocol to build ChatGPT apps. Postman and a lot more and obviously Cloud supports MCP apps. But we also have a lot large community around it, right? So people start to to build plugins to MCP apps and um integrations to different agents and also courses on how to build MCP apps. This is by integration for MCP apps. So we have a lot community around it. Um There's a repo X app which is the repo for MCP apps where everyone can just come and propose PRs and ideas of how to how to extend this spec and we have a work group in the MCP committee and we're convening every 3 weeks. We have a tri-weekly meeting on the future of the protocol and how to make the spec not just serve the bigger apps but also the community. So it's an open working group

**[4:52](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=292s)** with Anthropic, Open AI and all the partners in in the MCP apps protocol. >> Okay, so let's look at a few of the core concepts of MCP apps. The first and most obvious one is how do we even transmit UI over MCP? So if we look at this example of Cloud like you know agent times like a few months ago and I would ask something best case scenario it would reach out to my MCP server and it would get back a textual response which is obviously suboptimal. So let's say I do want to get some something better. So now I can use existing MCP primitives like a resource and now return HTML. And I can take that HTML and since Cloud

**[5:41](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=341s)** supports MCP apps it can turn it into an interactive application of the best soundtrack in the world. And what if you wanted to be really interactive, right? This is nice because it shows the best soundtrack in the world. What if I want to favorite one of the songs there? I want interaction. I want communication between the app and the host. So, when the user clicks on the favorite button, MCP apps actually standardizes this flow. So, instead of the app sending a message to to the backend, to Spotify's backend, it's actually sending a message to the host saying, "Hey, user clicked a button. Do something with it. I recommend you to call a tool in Spotify's MCP server." And the host decides what to do. The host keeps this control of the flow. In this case, the

**[6:27](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=387s)** host can decide to actually call the favorite favorite tool. And MCP apps standardizes this flow. >> Okay, so seeing is believing. So, let's see an example from Claude. Yeah. Uh so, let's say that I'm a product manager to understand the status of my funnel. So, I would go to Claude and I would ask what's the status? In the again, old world of a few months ago, uh I would get back the textual response. Let's say that it's PostHog. So, it reached out to the PostHog server, got back the textual response. It's factually correct, but it's useless. I mean, how do I even take that and understand quickly what's going on? I would have to read, which I don't want to do. Uh and it's pretty challenging. Uh but luckily, because both PostHog server and Claude

**[7:17](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=437s)** as a host support MCP apps, I can just say, "Show me." And now, instead of getting that block of text, I can actually get something useful, uh which is this interactive um widget that you would get, you know, on the PostHog uh uh server. And when you have that, you can at a glance see what's going on. And as you can see, it's branded PostHog. So, you're actually getting the PostHog experience within ChatGPT or Claude, etc. Uh but it doesn't really end there. As we said, MCP apps is also like an interactive photo call. So, not only can I see and and interact with it, I can also do stuff like ask him to explain what a funnel is. I might not even know that. So, again, instead of getting that huge wall of text explaining what a funnel is, I can just get this generative UI answer from

**[8:07](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=487s)** Claude, which uses MCP apps. It streams like the HTML inside, and now I can get this nice interactive experience of learning. And not only is it visually nice and helps me understand, but it's also fully interactive. And when we say interactive, it actually means that clicking it would help me communicate with the host. So, let's say that I want to understand like a particular step in the funnel. Uh I just go and I click on it, and since it's an MCP app, it can send a prompt back to the uh model and say, "Okay, explain this specific step to me." And I can advance the flow. Uh so, this is a like an example of of how that uh looks. So, how does it actually work? If you look at the architecture of it,

**[8:54](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=534s)** uh so, we started by prompting. So, we type something in. Uh we asked for the funnel information. A tool call went out. Since our server supports MCP apps, that tool call is actually linked to a resource. And if you look at the uh code here, then, you know, it's it's a it's just a resource with a uh some prefix. Uh we take that. It's pretty simple code. I could just add the but it's still the the resource with the HTML, and you're done. Uh that resource is then um consumed by the host. In practice, it's usually consumed beforehand, like it's preloaded. Uh but imagine that it's just consumed in real time. That same HTML then passed to the host that also supports MCP apps. MCP apps basically if you look at the MCP UI SDK, just a React component or a web

**[9:43](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=583s)** component that just accepts that resource plus a callback which is how we implement that communication protocol as I said earlier. And renders it in a sandbox. So, like we said, not only is it presentational, I can click. So, what happens when I click? So, we click on it, it sends back through that callback the event all the way up. The model takes that event and then it can send out a tool call or call a resource or anything else that's completing the agentic flow. >> And this architecture actually brings a new philosophy or a new vision to the web. So, instead of us thinking of the web as tabs or services that we need to consume using a browser, we're now consuming it using our own personal assistants, right? What

**[10:30](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=630s)** does it mean? It means that if I want to accomplish a task, for example, plan a um anniversary. So, up until now I had to open 20 tabs in the browser and I had to try to convey my intent to each of those services. And by saying conveying my intent, it means that I have to interact with the dashboards or the UIs of those companies. So, just to plan an anniversary, I need to convey my intent to Google Calendar and Amazon and Booking and Booking again and Amazon again and all and I don't need 99% of the UI that is shown there because this UI doesn't know me. It doesn't have the context on me. What if we could just take these UIs and just break them into atoms? And those atoms can be composed by my own personal assistant, right? Because I don't need the the UI. I need those atoms. So, if we can take these atoms and have my

**[11:21](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=681s)** cloud or ChatGPT or OpenCloud just use them using MCP UI, we can have this flow. So, my proactive assistant can say, "Yeah, I know. I see that you have an anniversary coming and instead of just showing me data from Google Calendar, it can display a Google Calendar chunk. Now, for me it's good because I know Google Calendar, I trust Google. For Google it's good because it maintains their brand and identity and for the host it's good because they don't need to develop these capability themselves. And it goes even deeper because if I'm interacting with Amazon, instead of Amazon being reduced to just a list of items or or text, I can see Amazon. I can I can know that this is this is Amazon and I can complete my entire flow without even leaving my assistant. And this is the agentic web. This is how we're going to consume the web because my assistant

**[12:11](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=731s)** will have the context on me. It It will know to pull the the map from booking.com. I don't need to know that, right? So, this is going to be the shift that we're going to see very soon where websites are going to shift into small chunks of UIs inside inside personal assistants. Um [snorts] and with that come new interaction mindset because um if I click on something in the Shopify's MCP app, then Shopify doesn't control my journey anymore. The host does. Um and no application will control the user journey anymore. So, Amazon won't be able to know to see my flow. It everything will go through the chat for auditability. Um and MCP apps actually standardizes it by defining this three level of control over the user journey. So, an app can notify the chat that something happened or an app can actually ask the chat to

**[12:58](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=778s)** run a prompt and and releasing all responsibility to the chat. So, MCP apps actually standardizes it and this is the new software flow, the new flow of interaction that we're going to see between applications, the chats, and the users. Um in 2026, we had we had an amazing year of standardizing MCP UI and 2026 is going to be the year where it's going to be a global standard for UI. >> Yeah. >> But, it's still evolving. There's a lot of stuff going on. Even in these past few months, these are some of the things that are already in or already contributed or proposed uh, by the community. Uh, so you still have a lot of time and a lot of room to influence how this future will look like. Uh, so you can go to X apps. Uh, that's the official SDK and spec is also hosted there. It's under the official model

**[13:46](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=826s)** context protocol uh, repository. There will be a QR code later. Uh, so you don't have to uh, to uh, photograph it. Uh, and also um, the the cool thing about using X apps in particular is that because it's maintained by us directly, uh, all changes to the spec are immediately uh, reflected in the SDK. So, if you use that SDK, then you automatically get all the new stuff out of the back. Uh, these are some of the issues that we have. So, please feel free to come and uh, contribute. So, what's next? Um, there's a bunch of stuff coming up. Uh, the first thing uh, that we get a lot of uh, uh, of asked for is kind of reusable views. So, if you have uh, um, companies like Autodesk that have really heavy apps like they have

**[14:33](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=873s)** in, you know, the entire 3D render there. They don't want to keep re-rendering that over and over again because it just it takes time, it's inefficient. Uh, that is the way that we had to do it uh, for the MVP. But we are working on thinking of maybe we can pass some identifier from the server uh, in a way that would help the model actually keep updating the same view. Uh, the other way to do this is >> Um, app tools, which is something uh, if you've heard of web MCP, which is Google standard of how agents will interact in with web views. So, in MCP us, we actually standardize it into app tools. So, up until now we saw the flow where users does something in the app and the app talks to the host. But what if the host or the chat wants to speak to the app? If the user writes something, uh, fill

**[15:22](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=922s)** out this form for me and the chat will fill out the form for the user. So, MCP apps actually standardizes this this flow which we call view tools. That's actually that's in the spec right now. It's also it's going to be released very soon. And we're working on this generative UI spectrum where you have predefined UI. That's MCP apps. That's like the black box iframe that renders all trace UI in that example. But you also have other things on this spectrum like declarative UI like JSON render or A2UI. These specs that say yeah, the the app just returns an instructions on how to build the UI, but the chat will actually build the UI. And you have fully generative UI on the other end of the spectrum. And if you know cloud apps, yeah, MCP apps is agnostic to the way the UI is generated. And if you know cloud apps imagine feature where you can just ask cloud to generate a UI for you.

**[16:12](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=972s)** That's actually based on MCP apps. So, this is an MCP app behind the scenes, but it supports generative UI. So, we're working on interoperability with those other standards. And actually just a few days ago we released a guide on how to do A2UI versus a generative UI standard and MCP apps which is the standard. How to do interoperability. How can a server can write A2UI and ship it to Gemini, but also wrap it as an MCP app to ship to ChatGPT and vice versa. An MCP app is supported everywhere. So, it can run everywhere. If you build it once, it runs in Libra Chat which is an open source MCP app supported in ChatGPT. That's the same app that you're seeing the same code base that runs in in both which is pretty cool. Yeah.

**[17:00](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1020s)** Yeah. >> So, this isn't just a technology or a cool feature. This is an entirely new way to distribute applications. So, if you look just a few months back then someone said that ChatGPT in particular has 800 million weekly users which is 10% of the entire world population. That's insane. So, if you think about the web in general, it took around 13 years to get to that number of users. So, if you look at that and you think that in the last few months we actually had a growth of over 1 billion. Just that we have like 170 times the total addressable market of the Apple App Store when it launched. So, MCP apps are everywhere. So, actually to list them, it is called cloud, open AI, etc. It's already there.

**[17:49](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1069s)** So, how do you get started? You can clone those you can go to the X apps. As a host also go to X apps or the MCP website. >> Please visit the official repo. >> [laughter] >> The X apps repo to get involved. And yeah. >> So, embrace the new web. It's awesome. With MCP apps you can write once and run it everywhere. And the future is looking bright. Not quite Travis, but with MCP and MCP apps we're close. >> And come talk to us afterwards. >> Yeah, thank you. >> [music]
