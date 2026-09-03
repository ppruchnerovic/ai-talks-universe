---
id: 7zkQtw951U4
title: "Dhruv Batra - Computer Use Models Will Agentify the Web, Not APIs"
slug: dhruv-batra-computer-use-models-will-agentify-the-web-not
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Dhruv Batra"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-12T07:10:23Z
video_id: 7zkQtw951U4
url: https://www.youtube.com/watch?v=7zkQtw951U4
youtube_url: https://www.youtube.com/watch?v=7zkQtw951U4
tags: []
topics: []
transcript: true
---

# Dhruv Batra - Computer Use Models Will Agentify the Web, Not APIs

**Dhruv Batra**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=7zkQtw951U4) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,742 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=7zkQtw951U4&t=2s)** Okay. Um, thank you for having me. Um, I'm Dror, I'm the chief scientist of Utori and one of the co-founders. Um, unlike a regular talk where I just give you a spiel about our company, I want to talk about something, you know, fairly different. Um, I want to talk to you about a specific argument and a counter argument. And the specific argument is that there's a popular narrative online that you hear, which is that uh AI agents will be the primary drivers of action on the web, not humans. Um, that they will be booking meetings for us, booking appointments for us, buying things for us, securing information for us, and so on. Okay, that's the claim. Step number two, when you ask people who make that claim how, the answer usually is, well, the web will be agentified. It will be made agent-friendly.

**[0:51](https://www.youtube.com/watch?v=7zkQtw951U4&t=51s)** Okay. Uh, when you ask how, uh the response to that is that with APIs that my agents and your agents and our enterprise agents will call through 14 different standards. Um, MCP, web MCP, you know, payment protocols, and so on. And today, I just want to make a very specific argument that the first two steps are right, the third step is wrong. This argument does not work, and I will give you a counter uh argument for that. Um, so, let's My claim for this talk is that computer use agents, which are agents that operate computers and browsers like a human by looking at the screen and pressing buttons, will agentify the the web, and more specifically the long tail of the web, and not APIs. Your websites, the long tail of websites will not have APIs available.

**[1:38](https://www.youtube.com/watch?v=7zkQtw951U4&t=98s)** Um, and in order to uh demonstrate that viscerally, let's begin with the example that most people commonly show um in in this literature, which is a consumer or a developer is sitting there at their iPhone asking, you know, find me this flight, and you imagine a a behind the scenes a browser use agent or a computer use agent operating a browser, going to flights.google.com, clicking those buttons like a human does. This is an extremely common demo in this literature, and it is ludicrously funny because why would you possibly do this? There are API services that are aggregators. It's a database. You can send in a structured query, get a structured query back. Why would you possibly kick click buttons to do this? Um my claim is that let's generalize this. Um let's say instead of that question, I

**[2:28](https://www.youtube.com/watch?v=7zkQtw951U4&t=148s)** ask you I'm planning an evening uh gathering with my friends, and what I want to know is I will point you to a restaurant and ask you, are there any gluten-free items on this restaurant's menu? And what people imagine is that at some point uh there will be myfavoriterestaurant.com/menu as a endpoint that you can just curl and ask a natural language query or filter it by saying, give me the gluten-free um uh menu items on your menu. Um and for people who think that either this is reality or this is what's coming, I would like to show to you what actual restaurant websites look like. Um uh I'll have my slides later online. Today, I'll just show you a couple of easy, medium, hard mode of what these things look like. When you go to the easy mode,

**[3:15](https://www.youtube.com/watch?v=7zkQtw951U4&t=195s)** people imagine restaurants like this where there is some text you can read. In medium mode, you get PDFs, which are menu items. In hard mode, you get a gallery of individual scans of pages of menus. And that's just stuck together, pixelated, not even OCR'd. And so, these are the people they are small business owners. They exist somewhere. There's about 200,000 small business owners in a single, let's say, country in in Europe that maintain their own websites. And what you are imagining is that tomorrow or in the next 5 years, they will all be revolutionized so that there are gateways for your agents to to poll. Um my claim here is this is not coming.

**[4:04](https://www.youtube.com/watch?v=7zkQtw951U4&t=244s)** Like the the cavalry that we're waiting for is not coming. The web is extremely long-tailed. Uh those individual websites may be of limited value, but the tail cumulatively has a lot lot of value, and infrastructure changes slowly. Um And at this point, usually the response is okay, fine. Uh let's just read the code. We have coding agents. Uh let's read the HTML. Uh we can do this. Um and I'd like to walk you through another example why that's a bad argument, why that cannot be done. Um let's say you want to know on a e-commerce website, is this 24 mm osmium cube in stock or out of stock? It's a It's a really simple query. The There's a product page, and you just have to answer is this in stock or out of stock? You scroll down, and you know, there's a

**[4:53](https://www.youtube.com/watch?v=7zkQtw951U4&t=293s)** quantity button that you that you drop down. That selector tells you and me with eyeballs who can see pixels uh that three of those items are sold out. They're not available. One of those items is available. However, when you send your agents to read the HTML for this for this page, what you see is that the selector says nothing about the quantities. The HTML actually has selectors that have descriptors for the items, but nothing about the quantity. Why? Well, so everybody who understands JavaScript and web technology at this point is shaking their head. You idiots, you thought this would happen. Um behind the scenes, there is a a query that is made that when the page loads, gets a JSON object or a dictionary that is filled with with at that moment, what

**[5:42](https://www.youtube.com/watch?v=7zkQtw951U4&t=342s)** does that store have? And it has quantities and stock uh listed there. And then when you click the drop down, there is a different part of code that renders whether it should show up as grayed out or it should show up as as color. Um and this is because, you know, we see this, but behind the scenes a browser is a rendering engine. For people who have worked in video game technology, the analogy made that you should be making is a browser really is a renderer. Like there's a there's, you know, assets underneath, there's code, ultimately pixels are produced. And so the claim is that the web was built for human eyeballs. That is the source of the truth. And so machines will need to operate with vision. Um we at Edditory wrote a blog about this called the bitter lesson for web agents

**[6:31](https://www.youtube.com/watch?v=7zkQtw951U4&t=391s)** that if you do not look at the pixels, you get stuck feature engineering to read. So this is what we built at Edditory. It's a model called navigator. Takes as input a screenshot of the browser, produces as output a human-like action, like clicking, typing, scrolling on a browser. Uh the kind of thing that was just happening here with a human telling a another human what to do and the other human producing button clicks. Imagine if the other human was a machine in this case. Um and so, you know, you could do things like I tell you about a website. Uh it's it's a e-commerce website and I just ask you, I have a promo code, does it work or not? There's no API for that. The the the store account will never give you that API. And so this machine will go open that browser, you know, go through a mock checkout flow, apply the promo code, look at the price, did it go

**[7:20](https://www.youtube.com/watch?v=7zkQtw951U4&t=440s)** down or not, and will send you a structured object saying, yes, this promo code works and actually, you know, the price went down by 22% or whatever. Um and there is your API-fication of the web. Um while I do claim that machines will need to operate with vision, um they will not be limited to human ways. Um so you do have to be superhuman and on on this screen what I'm showing is a form filling task where what the what the model does on the right is directly read the and write JavaScript. So, the model has an action called execute JavaScript. It writes custom code and it fills out a bunch of fields uh simultaneously. So, it does not have to be limited to button clicks. At this point of time, you might ask, well, are computer use models good enough? Um, and there is a narrative

**[8:08](https://www.youtube.com/watch?v=7zkQtw951U4&t=488s)** online that computer use amongst all capabilities is stuck. Somehow coding agents are making a bunch of progress and computer use agents have not. And it's not true. That's not what the the reality is telling us. Benchmarks after benchmarks are falling. This is a benchmark that is run by an academic group um at Ohio State. Over the last couple of years, the benchmark has essentially gotten saturated uh most recently um as of like a month ago where the accuracies are now sitting at 97%. So, the benchmark is essentially done and we'll have to create new ones. At this point, the last argument that stands is people ask, well, are computer aren't computer use models slow and expensive? And there as well, my answer would be no, specialized models are getting quite good. If you are using a frontier model, so on this slide I'm comparing to Opus 4.7 and GPT 5.5. Yes,

**[8:58](https://www.youtube.com/watch?v=7zkQtw951U4&t=538s)** those are often slow. Every action takes you about, you know, 10 seconds in GPT uh 5.5's case and you know, the whole task is takes you to $2.30 on some on some data set. Uh the model we trained is significantly smaller, therefore just as accurate but slightly faster. So, um that was the entire argument. I think the web is uh you know, machines are going to be the drivers of action on the web. Uh we've had 30 years of web for human consumption. That is changing, but the how matters. I think the way we will have this API where you could poll any website and describe any task in natural language is by having a sea of agents that are operating browsers in the background. And that's that's it. Thank you.
