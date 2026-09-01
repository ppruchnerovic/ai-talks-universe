---
id: TXe9hkWgxOI
title: "The New Web: How MCP Apps Put Live UI Inside ChatGPT & Claude"
slug: the-new-web-how-mcp-apps-put-live-ui-inside-chatgpt-claude
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 20
published_at: 2026-05-29T14:00:06Z
video_id: TXe9hkWgxOI
url: https://www.youtube.com/watch?v=TXe9hkWgxOI
youtube_url: https://www.youtube.com/watch?v=TXe9hkWgxOI
tags: []
transcript: true
---

# The New Web: How MCP Apps Put Live UI Inside ChatGPT & Claude

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=TXe9hkWgxOI) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Ido Salomon is the creator of MCP-UI and a co-creator and maintainer of MCP Apps. Liad Yosef works on MCP-UI and co-leads the MCP Apps working group inside the MCP committee.

In this keynote they tell the story of how a six-month-old idea that no one believed in became the first official MCP extension, live in Claude, ChatGPT, VS Code, Cursor, Copilot, Postman, and Goose, and make the case that 2026 is the year MCP Apps becomes the global UI standard for agents.

In this Keynote: MCP Apps: Extending the Frontier - Ido Salomon, Creator MCP-UI & Liad Yosef, Co-creator, MCP Apps

- The six-month origin story
- Why text is a terrible interface: Why companies refused to be reduced to a database, and how MCP Apps lets apps like Canva, PostHog, and Airbnb keep their brand and identity inside any host.
- The core architecture, end to end: Tool call points to a ui:// resource, host renders in a sandboxed iframe, UI sends postMessage events back to the host (tool calls, notifications, prompt requests) to close the loop through the model.
- Live PostHog demo: The same funnel question answered as a wall of text, then as an interactive PostHog component rendered inside Claude, without ever leaving the chat.
- Generative UI in Claude: Why Claude's new generative UI feature is actually MCP Apps under the hood, and why the spec is agnostic to how the UI gets generated (predefined, declarative, or fully generative).
- The "new web" philosophy: Stop tabbing between Google Calendar, Amazon, and a dozen other apps, and let an assistant compose atoms from each into a single planned experience.
- The official @mcp-ui SDK (X Apps): Write once, render everywhere across every compliant host, with spec changes reflected immediately.
- Working group additions: Theming so a server's UI can match Claude or ChatGPT's look, sampling from the app's own front-end code, and ongoing community input on naming (they landed on "view").
- What is next: Reusable views for heavy apps like Autodesk that cannot re-render every turn, the app-tools proposal that lets the model drive an app's UI like a human filling out a form, and the open question of whether HTML is enough for mobile-native experiences.

Links and Resources:
- MCP Apps overview: https://modelcontextprotocol.io/extensions/apps/overview
- MCP Apps official spec and SDK repo: https://github.com/modelcontextprotocol/ext-apps
- MCP Apps launch post (Model Context Protocol blog): https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/
- MCP-UI project site: https://mcpui.dev/
- MCP-UI on GitHub: https://github.com/MCP-UI-Org/mcp-ui
- @mcp-ui/client on npm: https://www.npmjs.com/package/@mcp-ui/client
- @mcp-ui/server on npm: https://www.npmjs.com/package/@mcp-ui/server
- VS Code MCP Apps announcement: https://code.visualstudio.com/blogs/2026/01/26/mcp-apps-support
- OpenAI Apps SDK examples: https://github.com/openai/openai-apps-sdk-examples
- Agentic AI Foundation: https://agenticaifoundation.org/

Timestamps (approximate, please adjust after upload):
00:00 - Intro: Talk built yesterday, already out of date
00:20 - Meet Ido Salomon and Liad Yosef
00:30 - MCP Apps is already everywhere: Claude, ChatGPT, VS Code
01:00 - The chicken-and-egg problem six months ago
01:10 - OpenAI Apps SDK and the Anthropic, OpenAI, MCP-UI collaboration
01:50 - Official launch with Claude and VS Code, plus Canva
02:30 - Multi-host adoption in under four months
03:10 - Community adoption: Pi, OpenClaw, advocates, PRs
03:35 - MCP Apps is an open standard: How to join the working group
04:10 - Stepping back: Why text is not an ideal interface
04:30 - Brand and identity: Why companies refused to be a database
05:00 - MCP-UI's original concepts a year ago
05:30 - Core concept one: Passing UI over MCP via an HTML resource
06:20 - Core concept two: Standardized postMessage back to the host
07:00 - Demo: Asking about a PostHog funnel, getting an interactive component
08:00 - Augmenting the agent: Generative "what is a funnel" UI
09:00 - Architecture recap: Sandbox, events, model loop
09:55 - A new philosophy: The "new web" of composed atoms
11:30 - Making 2026 the year MCP Apps becomes the global UI standard
12:00 - Spec evolution: Theming, sampling, and more
12:20 - Official SDK: X Apps, spec changes reflected everywhere
13:00 - What is next: Reusable views and the Autodesk use case
13:50 - App tools proposal: Letting the model drive the UI like a human
14:30 - Do we need native mobile, or is HTML enough
14:55 - MCP Apps vs other generative UI methods
15:45 - Claude's generative UI is MCP Apps under the hood
16:15 - Interoperability with AG-UI and other protocols
16:25 - Distribution: ChatGPT users as a 160x Apple App Store moment
17:00 - How to ship: MCP Apps skills and MCPUI client SDK
18:00 - Call to action: Repo, issues, PRs, working group, Discord
19:15 - Write once, render everywhere, even this early
19:45 - Not quite Jarvis, but close enough

## Transcript

*3,529 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=0s)** Okay, hello everyone. So, we built this talk yesterday, literally, but it might already be out of date. Hi, I'm Adi Solomon. I'm the creator of MCPUI and the co-creator and maintainer of MCP apps. I'm Adi Yosef. I work with Adi on MCPUI and together we also lead the work group on MCP apps in the MCP committee. So, MCP apps are already everywhere. Cloud, ChatGPT, VS Code, all of these already replaced walls of text with rich interactive user experiences. The really cool thing here is that it revolutionizes the way that we interact not only with agents but the entire web. And it feels like it's been here forever, but in reality it's only been 4 months.

**[0:47](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=47s)** In those 4 months, like yeah, I don't know how many of you have been in the previous Dev Summit in London, but just 6 months ago we really had to sell this idea. Everyone thought no one needed this, but you know, and we had this really huge chicken and egg problem. Luckily, just 4 days later we got our chicken. OpenAI released apps SDK and suddenly the most widely used host in the world had interactive applications. We took advantage of this momentum. The community joined together and Anthropic, OpenAI, and MCPUI joined forces to create a new spec to finally bring this into the official MCP specification. A draft was born just a month later. And as you can see, MCP apps extending MCP with interactive UI.

**[1:38](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=98s)** It was very popular very quickly. People were very emotional about it. And with really hard work from the community over the past 2 months, we improved it. We really brought it to a to a place where it's ready to get dozens of new applications like Canva and be officially launched both in Cloud and VS Code. And that was the starting point because in the past 3 months there was a rapid adoption across the ecosystem. And not just the community, but multi-host support. In just 3 months, we saw these are these are the early adopters of MCPUI. So, shout out for these companies. These are These companies adopted MCPUI when no one knew

**[2:26](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=146s)** what MCPUI was. But now, we have VS Code and we have Cursor and we have Copilot and we have GitHub and we have ChatGPT which adopted MCP apps as the recommended way of building ChatGPT apps. We have obviously Postman and Goose and Claude was with Claude apps adopted MCP apps. And all those hosts adopted MCP apps in less than 4 months, which is amazing. This is exactly what we tried to do with this spec, with this standard, to have a unified spec across the industry. But not just those, not just big companies, we had huge community adoption. We had um a lot of extensions and additions to MCP apps. We had Pi, the engine behind Open Claw,

**[3:14](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=194s)** that recently announced support in in MCP apps, which is amazing. And we have a lot of advocates and champions across the community talking, speaking building things with MCP apps. In the official MCP apps repo, we have a lot of PRs opened by the community and there's a lot of discussion going on there. And that's a good time to remind that MCP apps is an open standard. It's for for us, for everyone. We're looking at it as the foundation of the new web. So, everyone is welcome to to join the to join the discourse, to to join the conversation. We have a public work group meetings once every 3 weeks where we discuss uh additions to the spec, where we discuss changes to the spec, where we discuss discuss input from the community, from host builders, from server builders, and

**[4:02](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=242s)** we advance MCP apps to be uh this unified standard. But let's take a step back. MCP apps, like we said, um started with the concepts of MCP UI, and the idea of MCP UI is that text is not an ideal interface, right? I mean everyone here uh tried to ask the chat um a question definitely a year ago and got a wall of text, right? But what if the apps, the connectors that are uh being connected to this chat could actually send their own UI to the chat instead of just text? Because that that was a big blocker for companies to adopt MCP. They didn't want to to lose their brand, they didn't want to lose their identity, they didn't want to be reduced to a database, right? But what if they can just send their identity? What if instead of this we could have just have this. I mean, this looks might much

**[4:52](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=292s)** nicer. This looks more natural to us, and this actually keeps the identity of each of those companies, of each of those tools that are being connected to this chat. And these are not just presentational, they can also be interactive. So uh a year ago, uh when I first released uh MCP UI, the concept was fairly simple. How do we create an open protocol to send UI over MCP and also standardize the way that this UI interacts with the host? Obviously, we also had to uh encourage adoption, so we needed to uh put out community SDKs uh for easy adoption. So, let's look at the core concepts behind MCP apps. Uh the first one is an obvious one is how do we even take UI and pass it over MCP?

**[5:39](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=339s)** Uh so, if we take this example, let's say that we want to uh get the best playlist in the world. So, uh the agent would usually just uh put a tool tool call out to the MCP server and in the old world we'd get back a textual response. This is obviously sub-optimal, but with MCP with existing primitives we didn't have to invent anything new. You could instead of return text point to a different resource, an HTML resource and once the host already supports these resources it can take the HTML and turn it into an interactive component. And like we said, this component needs to be interactive and for it to be interactive it needs to communicate the view, the UI needs to communicate with its back end somehow. But we don't want the UI to communicate directly to its

**[6:26](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=386s)** back end. Why? Because then the model would know what happened. So if a user clicks something in the UI MCP apps actually standardizes the way this UI makes the change, takes the action. Instead of communicating to the back end it just sends a message back to the host, for example a tool call, a request for a tool call. The host gets this message and decides what to do with it. In this case it decides to actually call the tool of uh favoring the song and thus closing the loop between the UI and its back end through the model. And the interaction doesn't stop only on tool calls. The UI can also send notifications or prompt requests to the host. Okay, so seeing is believing. Let's see an example. Uh so let's say that I'm developing an app and I want to understand how the funnel works. So I send a message and it

**[7:15](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=435s)** send out uh recall to let's say PostHog and I get this textual response. It's factually correct, it's very informative, but it doesn't really help me to understand what's going on in a glance. But because you know Cloud supports MCP apps and PostHog supports MCP apps, I can just say show me. And now instead of this wall of text I get this interactive component that was actually created by PostHog. So it maintains the branding, it maintains their identity and user experience, and I can see what happens with my funnel in a glance. It doesn't just stop there. MCP apps doesn't only allow you to get pre-made UI from afar. You can also augment the agentic experience. So, for example, let's say that I don't know what a funnel is. So, I can just ask, "Tell me

**[8:04](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=484s)** what a funnel is visually." And now again, instead of a long wall of text, I can get this generated UI, generated on the fly by the cloud team, where I can actually understand visually what's going on. The really cool thing is that, like we said earlier, it's not just presentational, it's also interactive. So, not only can I see what's going on, I can also click on it. And what what happens now is that we didn't have to type something up and hope that the prompt does what we want. The the agent, or it can also be the app, created this curated an experience for us where I can just click on something, it would auto prompt, send a a prompt to the host and to the model to continue the flow and explain to us.

**[8:55](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=535s)** So, how does it work in really 2 seconds? So, the architecture is really simple. What happened here is that we prompted, that sent out a tool call. As we said, the tool actually points to a resource that might have already been pre-fetched and kept in the host. So, the rendering is instant. We instantly see that there's an app there. That app is then rendered inside a sandbox. And because it's not only presentational, we can click on it, as we saw earlier. And what happens there is that an event is being sent out from the sandbox through post messages all the way back to the model, and we can continue the interaction without prompting. So, in those examples, I could say show me visual I could I could

**[9:43](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=583s)** click and get the the next step of the funnel. It would just send a tool call. It would prompt the model, call a new resource, etc. And the amazing thing is that it's not just technical. It's not just the architecture change or the technical change that MCP apps bring. It's a new philosophy. It's something that ushers what we call what we think of as the new web. So, for example, imagine that you want to do something. You want to plan an event. Today you you have to open bunch of tabs in your browser and you have to browse between them and you have to adapt yourself to a lot of a lot different a lot of different UI and UX and learn those interfaces just to convey your intent to plan an event to plan an anniversary or something like that. We don't need all of this, right? If we

**[10:30](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=630s)** have agents, if we have AI, we can just take those interfaces and we can just break them into atoms and have our agent our assistant compose these atoms for us, right? So, instead of having this multi-tab experience like we saw before, I can just ask my assistant to do something. It can then query Google Google Calendar and get the UI chunk the the small view of Google Calendar that I know that I recognize as Google Calendar and Google maintains their identity. And then I can continue and ask something from Amazon. Instead of just getting the data from Amazon, it can actually get the small UI chunk from Amazon. And this streamlines my experience. This keeps the brand's identity and this that's also good for the assistant because they don't need to generate all of this from scratch and my experience instead of being multi-tabbed can be something like that. So, with the

**[11:19](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=679s)** agent with my assistant, I can plan my event using all those tools with the interfaces that I already know and have it all in one in in one context. And this this is the the real philosophy of MCP apps. This is what we're trying to bring. And we plan on continuing pushing this back and we want to turn 2026 to to the year of MC apps is the global standard for UI, not just something that's adopted by some hosts or some parts of the community. Um the spec is evolving rapidly. In only 3 months, we managed to add all of these additions and more to the spec. We got input from hosts that said, "Hey, we want to be able to theme the small UI in in Cloud's theme or in ChatGPT theme." And then you we added added this to the

**[12:06](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=726s)** spec. Um we added a sampling. We added We added a lot a lot of cool things and I really encourage everyone to be to to come to the public meetings. But the spec is evolving. We have an official SDK for developing MC apps. It's called Axed apps. And the nice thing about having an official SDK is that you build it once and it runs everywhere. Like you saw, all the hosts support it. And also, all the spec changes are immediately reflected in the SDK. So, the community and the hosts immediately adopting them. For example, here, Goose adopted the the theming that we discussed earlier. Um like we said, the repo has a place for the community to actually open issues and discuss issues, not just PRs. And let's talk about what's next. Yeah, so what's next?

**[12:54](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=774s)** MC apps already supports a bunch of use cases. There are already hundreds of different apps and probably dozens of different hosts that support it. Uh there are a few stuff that we are working on in the work group. So, you are very much encouraged to join the work group meetings and use GitHub. First one is reusable views. We get that quite a lot. In the MVP, we decided consciously to simplify things. And whenever we render we we set up a new tool call to render a new UI, it replaces the old one. Uh that works fairly well for most use cases. But if you look at this example from Autodesk, they have a really heavy application. Re-rendering it all the time doesn't make sense for the user experience. So, we are looking at ways to update or bring new information into existing UIs. Uh now, one way one of the ways to do it

**[13:43](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=823s)** is let's say that each one of these has its own session ID, and we can just reference to it and push information in. But, the second way to do it is to flip the script. If we look at this new proposal, which is App Tools, the idea there is that instead of the tool injecting like the the tool injecting references to update a specific widget, why not let the model or the agent use that application as if it was a human. So, the idea there is that every app would have their tools, and instead of us interacting with the app, it would do stuff like fill out forms in our behalf. So, the UI would be updated in place instead of updating in the server and then somehow making its way to the UI. Uh the another thing that we are looking

**[14:34](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=874s)** at, but it's not yet uh I think in consensus, is the idea that maybe HTML isn't enough. Maybe we need something like a native experience for mobile. Currently, we don't have real use case for it yet. HTML seems to do a pretty good job with iframes, but if you do have a use case, then we'd be happy to hear about it. Yeah, and the big elephant in the room, the question that we keep getting asked is how MCP apps relates to other generative UI methods. Because if you have this spectrum of how UI how chunks how the views can be generated, then we have predefined UIs, right? Which is the the UI that the app decided to render. For example, the Airbnb UI or the Canva UI. And then you have things that are a little bit more flexible like The UIs like JSON render, where the app doesn't

**[15:22](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=922s)** really render the UI, but just defines a structure. And then on the other hand of the spectrum, you have like the fully generative UI, where the model just decides to generate from thin air the UI. And the nice thing about MCP apps is that it supports all of them because MCP apps are actually agnostic to the way the UI is being generated. It only standardizes how this UI gets to the model and how this model interacts with this UI. And a good example for that is a feature that Cloud released only a few weeks ago, which is generative UI in Cloud, right? Probably saw that. And that is using MCP apps under the hood. So, this is generated on the fly, but it's wrapped in an MCP app, and that shows you the power because MCP app can handle third-party UI or first-party UI at the same time. We're also working on interoperability

**[16:10](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=970s)** with other UI protocols because like we said, we want to have a a complete stack of how to do a gigantic UI, whether it's MCP apps, AGI, web MCP, we're working on connecting with all of them. So, MCP apps isn't just a technology. It's really a new way to distribute your apps. If we look even just a few months back in October, ChatGPT had 800 million users, which is 10% of the entire world population using it weekly. That, you know, the internet took 13 years to get to that. And that's, you know, what now it's actually a billion or something. That's over 160 times the market that the Apple App Store had when it launched. So, you might ask yourself, how do you tap into that? Like, how do you get to

**[16:57](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=1017s)** all of these people? How do you get to all of these devices? So, if you are developing an MCP server, if you have an app, all you need to do is visit the official MCP app site. There's this QR code if you want to use it. And you can use the official MCP app skills to have your favorite engine just code it for you. Uh and if you are a host developer and you want to open your platform to this new technology and give this new experience to your users instead of walls of text, interactive UI, uh you can uh go to XApps to get like the granular capabilities or you can visit MCPUI, which is the recommended client SDK used by Postman and Goose and others and simply hook it up

**[17:44](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=1064s)** [clears throat] and get started. And if you want to be a part of this new new future, if you want to help us build that and plan for that, and if you're sitting here, you're probably you're already at one step ahead, but this is going to be the future of the web. So, if everyone here wants to get involved, visit the MCP Apps repo, leave an issue, take an issue, open a PR, help us build MCP Apps the from the spec side and from the SDK side. And I think more importantly, use the join the conversation, join the working group Discord where we actually we have good conversations there with the community, with the host builders. For example, here there's a survey that we posted on how to call these small UI chunks. Everybody had different ideas.

**[18:32](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=1112s)** Eventually, we landed on view. We thought about applets, but Java stole that from us. So, join join the working group Discord where a lot of good conversations are happening and also join the community Discord where people from across the community ask questions, give tips, and helping together to build this future of the new web. So, I hope when you heard this, you actually got a little bit excited. We have this unique opportunity to kind of take our apps, take the very way that our users interact with it, break it apart, and try and build it not as just one single app, not just one monolith, but actually just a part of a huge web of a lot of different apps, all connected through a model. Uh and not only use it, but also shape

**[19:21](https://www.youtube.com/watch?v=TXe9hkWgxOI&t=1161s)** it. Uh you can actually be a part of how this happens, how this protocol is actually coming to life. And with MCPI apps, you can really write once, write the application once, and even this early, run it everywhere. Run it in cloud, in VS code, in cursor, in ChatGPT anywhere. So, what does the future look like? Uh we're not quite a Jarvis yet, uh but with MCPI in general and MCPI apps in particular, we can bring new rich experiences that would have seemed impossible just a few months ago uh to every host in the world. You can do whatever you want. So, thank you. Thank you very much. Yeah. >> [applause]
