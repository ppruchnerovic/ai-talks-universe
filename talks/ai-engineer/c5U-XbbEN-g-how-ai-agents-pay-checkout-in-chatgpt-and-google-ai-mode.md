---
id: c5U-XbbEN-g
title: "How AI Agents Pay: Checkout in ChatGPT and Google AI Mode — Sam Parsons, PayPal"
slug: how-ai-agents-pay-checkout-in-chatgpt-and-google-ai-mode
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Sam Parsons"]
channel: "AI Engineer"
duration_min: 15
published_at: 2026-10-06T01:30:12Z
video_id: c5U-XbbEN-g
url: https://www.youtube.com/watch?v=c5U-XbbEN-g
youtube_url: https://www.youtube.com/watch?v=c5U-XbbEN-g
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "agentic commerce", "AI payments", "PayPal", "Braintree", "Agentic Commerce Protocol", "ACP", "Universal Commerce Protocol", "UCP", "ChatGPT Instant Checkout", "Google AI Mode", "Google Pay", "MCP apps", "payment tokenization", "Sam Parsons", "AI Engineer"]
topics: ["Agents & orchestration"]
transcript: true
---

# How AI Agents Pay: Checkout in ChatGPT and Google AI Mode — Sam Parsons, PayPal

**Sam Parsons**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#agentic commerce` `#AI payments` `#PayPal` `#Braintree` `#Agentic Commerce Protocol` `#ACP` `#Universal Commerce Protocol` `#UCP` `#ChatGPT Instant Checkout` `#Google AI Mode` `#Google Pay` `#MCP apps` `#payment tokenization` `#Sam Parsons` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=c5U-XbbEN-g) · [Conference site](https://www.ai.engineer/)

## Description

Your next customer might check out without ever visiting your site. Here's how the payment actually works.

Sam Parsons, senior staff engineer at PayPal working on PayPal Enterprise Payments (formerly Braintree), walks through three ways merchants can accept payments initiated by AI agents. First, Instant Checkout in ChatGPT with the Agentic Commerce Protocol and a merchant-built MCP app. Second, Google AI Mode with the Universal Commerce Protocol and Google Pay, where merchants only stand up endpoints. Third, an MCP app with an external checkout page that gives full control. He demos each flow, explains how tokenization keeps card details out of the agent and the merchant's PCI scope, shows the integration points, and covers how tokens are limited by merchant, amount, currency and expiry.

In this talk:
• How the Agentic Commerce Protocol (ChatGPT) and Universal Commerce Protocol (Google) compare
• What MCP apps are, and how merchants control the UI inside agents
• How tokenization and constrained tokens keep agent payments safe
• Trade-offs between in-agent checkout and an external checkout handoff

SPEAKER
Sam Parsons, Senior Staff Software Engineer, PayPal Enterprise Payments (Braintree)

LINKS
PayPal Agent Ready overview: https://docs.paypal.ai/growth/agentic-commerce/agent-ready/overview
Agentic Commerce Protocol integration: https://docs.paypal.ai/growth/agentic-commerce/agent-ready/agentic-commerce-protocol-integration
Universal Commerce Protocol integration: https://docs.paypal.ai/growth/agentic-commerce/agent-ready/universal-commerce-protocol-integration
Braintree docs: https://developer.paypal.com/braintree/docs

CHAPTERS
0:00 Intro
0:37 PayPal Enterprise Payments (formerly Braintree)
1:07 Three paths to agentic payments
2:07 Instant Checkout in ChatGPT (ACP)
3:06 The checkout flow
4:51 Demo: booking a hotel in ChatGPT
6:00 What tokenization does
7:00 Integration points
8:00 How the tokens are constrained
8:30 Google AI Mode (UCP)
9:54 No UI to build, just endpoints
11:14 Path three: MCP app with external checkout
12:09 Demo: checkout from Claude
13:23 Coming soon: elicitation
13:38 Choosing a path

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,563 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=1s)** [music] Okay. So, I'm going to talk to you about aentic commerce um with PayPal enterprise payments. So, this is about how do we accept payments from agents kind of maybe a human in the loop, maybe not um for merchants. So, I'm from PayPal. Um, and I work on our Aente Commerce area. Um, my name is Sam Parsons, senior staff engineer here. Um, so first of all, you may have heard of Brainree before and Brainree is PayPal's large enterprise payments. Was that Brainree Heart? Brainree. Yes. Uh, so

**[0:49](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=49s)** but now it's PayPal enterprise payments. So I'm going to say PayPal enterprise payments, but if you know it as Brainree, uh, it's the same thing. So, we handle payments for really large corporations. You know, think of the biggest ones that you can think of. Huge volume, huge scale. So, what we're going to talk about here is a couple of things, three different paths. And really, the the key takeaway that I want you to have is that PayPal Enterprise Payments is building the bridges for merchants to be able to accept payments from many different places. And so, I'm going to give you a flavor of some of them, but really this this is in a fast evolving area. that you're going to see way more um over the coming months and and year. So, first of all, we're going to talk about a genic commerce protocol. So, this is uh OpenAI has created that and that'll be in chat GPT. You can use

**[1:39](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=99s)** this universal commerce protocol. Google partnered with some others and created that protocol and these are very similar. So, if you go look at the specs, you're going to find out, oh, they are almost identical. Um, and again, you know, we're we're kind of early days here, but also we're going to demo for you another path towards accepting agentic payments, human in the loop using just MCP apps and and external checkout. Okay, so let's dive in. Um, so first of all, this is instant checkout and chat GPT using aentic commerce protocol. So, PayPal Enterprise Payments built an integration to a Gentic commerce protocol that allows you to start taking payments in this manner. So, there's a couple different flavors. The one I'm going to walk through uses an MCP app. So, an MCP app is like an MCP server, but you embed inside of that

**[2:30](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=150s)** app. You embed UI. So, it has HTML, JavaScript, and things like that. And those then can get rendered inside of different agents. So, Jat GPT can render those. You can add an app. You can render them in Claude. You call that a connector. Same thing. It's an MCP app. And this extension many different agents out there, you know, Goose or other ones also support. So, this is kind of a a general standard. Instant checkout allows us within chat GPT to trigger like an in chat purchase of something. Okay. So let me kind of walk through what that flow looks like. So first of all, the user will have their intent. So they're searching in chat GPT. They'd like to buy something and move to the next part. There's discovery

**[3:20](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=200s)** there. So the merchant using an MCP app can show to the user, here's things that you may want to purchase. They get to control that experience. So it's inside of say chat GPT, but the merchant gets to control it. They get to control the look, the feel. they get to control what's showing up and interact there. Then when the user decides, I'd like to go to the next step and buy this. They can trigger this checkout. So that's where the MCP app talks to its kind of host chat GPT and says, I'd like to purchase something that uses a gentic commerce protocol. behind the scenes, the user would enter in maybe a credit card or maybe they had that stored and move to the next part that will get tokenized against PayPal systems, PayPal enterprise payments. And finally, when we get to the end of that, they'll

**[4:09](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=249s)** complete that and send that across to the merchant who then charges that. So, we kind of look at this big life cycle. At the end of it, from the merchants's perspective, they do a couple of things as far as bridging that gap. They're pro providing these MCP app experience to the user, but they're also providing [clears throat] they're receiving these tokens that come from ultimately PayPal enterprise payments. And that looks like every token they normally process. So this is a really seamless integration for them at the end of it. And on the back of it, settlements, refunds, chargebacks, compliance, all of that remains the same and is supported through PayPal enterprise payments in general. So right now we're just going to do a a walkthrough of searching here in chat GBT. This will give you that instant

**[4:57](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=297s)** checkout experience. So this one here is like a travel app. So I'd like to buy some um looking for some hotels. Um here's some different options. And I'll just pause here. So you can see this UI here is not a chat GPT UI. This is controlled by the merchant. merchant gets to specify that they can have their interface for what makes sense depending on what they're selling. Um, sorry that fast forward through there. Hit play. And so then we continue here. When they're ready, they go to proceed to checkout. This now is pulling up the chat GBT instant checkout experience inside of there. So the the merchant isn't actually generating this. This is provided from the instant checkout

**[5:44](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=344s)** experience. Apologies about that. And from there, they start entering in their credentials. So, they're going to enter in some credit card details. It's just a test credit card number that they're going to enter. And behind the scenes, that'll be tokenized with PayPal. So if you're kind of not familiar with payments, tokenization means where the user exchanges a real payment credential that's transactable, say your credit card number and instead they exchange that for a token that can then be passed around without increasing PCI scope and you know dangerous things happening. So that's what's going to happen right here behind the scenes is a tokenization will occur and that's the merchant doesn't have to do that. This is like within the host the host app is going to do that tokenization send it to PayPal enterprise payments and then we

**[6:34](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=394s)** give back the token to chat GPT and that's safe to pass around. So this is what's happening right now. Tokenization is occurring and then it's going to be sent to the merchant. The merchant receives that and says okay now I transact with that token securely. And now you see they've come back to the MCP app. This has been updated. Their booking's been confirmed. And so you can see from a merchants's perspective, they have all control of what that UI looks like and it's pretty seamless for the the user. What are the integration points here? So the first integration point is inside of that MCP app widget. So this I'm showing you the real code for um for do this instant checkout with open AAI. You need to have this JavaScript code that triggers that checkout experience. So that's provided within the context of your MCP app. And then the next place where the merchant

**[7:23](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=443s)** picks this up is they receive a call to their MCP server with this complete checkout tool and they get that token and then they can proceed as usual with their processing of you know a typical PayPal enterprise payments token. So it's really pretty straightforward as far as that goes. Now there's still obviously the work of creating an MCP app within that experience. Also, there's um links here to the QR code if you want to like follow and look at the docs for how you would set this up. And what's kind of happening behind the scenes here is these tokens are constrained in a number of ways. One of them is with the merchant so that this is can only be processed on a given merchant. It has a max amount of dollars that are applied. It has a currency. It

**[8:11](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=491s)** also has an expiration. So, you can't just use this forever. And all of those transactions when processed they get attributed to the source where they came from. So this would show up within PayPal enterprise payments as a chat GPT um transaction that occurred. Um so next I'm going to walk through what Google AI mode and how we're meeting merchants there. So the flow looks a little bit different when you're processing transactions on Google AI mode. So first of all the user might be shopping in AI mode that you know want to buy you know say a pair of running shoes or something like that behind the scenes using the universal commerce protocol the agent will create a session against that merchant for the

**[8:59](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=539s)** user. So that kind of exists as an entity belonging to the merchant and and it uses that. Then when the user says I now want to check out with this the tokenization happens but here this is using Google pay. So Google pay would tokenize with PayPal enterprise payments. And so that's step three and then give that token back to the merchant. And you kind of see this is actually a very similar model. Then at the completion step they provide that to the merchant. And at step five we do the charge. So the merchant comes along and says here's my token. I would like to process this transaction. here's all the information about it and the same sorts of things like this again settlement refunds chargeback risk compliance this all is just standard operating procedure as far as the

**[9:47](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=587s)** merchants perspective but they receive this token from a different path this came in through Google AI mode one of the things to note here is in Google AI mode the merchant doesn't create an MCP app they don't create an experience their integration with Google AI mode is more providing here are my products, here is my endpoints for receiving the payments, the complete checkout payment um and so forth. There is no like UI that you have to build. You have to stand up endpoints essentially to to integrate with this. Um so you can see here one of them is specific specifying in your um well-known JSON file for universal commerce protocol and you specify some

**[10:35](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=635s)** things that tell us or tell Google pay this is needs to be processed on brainree or PayPal and price payments and here's your merchant ID and here's your client key and that's safe to pass through in the public. Then Google will take that and when the final end of it is you'll get a call to this endpoint from UCP checkout session with that session ID and a complete and you then get to process that and what you'll receive in there is this um token representing the credit card behind that Google Pay payment. So again two main key integration points um as far as receiving those payments. The next one I'm going to show you here is about MCP apps and just kind of opening up your mind about what are the other things that you could do with MCP apps. This

**[11:23](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=683s)** one gives the merchant really full control over the whole experience and we're going to work in things that are not necessarily Google or ChatGpt, but there's a lot of different um agents that already support MCP apps. So, a couple of key pieces here. One is that there's the MCP app widget. So this will in our example here will show like a product card and you'll get a checkout button. Then there'll be a handoff um that will open up the checkout into an external page. So then you can complete that there and then come back and get it automatically updated within your MCP app. So that gives you a lot more control, but there is a little bit more friction that's in introduced in this mode because you're not you're not doing like the actual checkout inside of your agent. So let's um walk through this

**[12:13](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=733s)** one. So here we're going to search for some things uh that we'd like to buy. And this loads up an MCP app. And you see this is using cloud and this is a connector. So MCP apps show up as connectors or apps depending on you know the container. So here's this is the MCP app. The merchant would design this. They add the things that the user now is picking what they want and when they click checkout this is now going to pop up an external link and you can tie these together with a session as a merchant. So that's what's happening here. This opens up that session. They can then can complete things with any payment method that they want. You have complete control as a merchant over everything. But when you complete that, notice how this MCP app updates

**[13:02](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=782s)** automatically. So, we're using communication behind the scenes to allow us to know exactly that it was completed and the status of that order and everything. So, that again just kind of demos for you what you can do with an MCP app and kind of what's on the table. And there's a lot of new things um coming along here. MCP apps has a new feature. It's not supported in most of the major ones yet that is called elicitation and so you can do that maybe a little bit more seamlessly as far as requesting that external validation in an iframe or something. So that's coming soon. Um I wanted to show you what you could really do today which is you know like this. This kind of gives you a little bit of an over overview of like what are the different options um that we offer merchants today and kind of what are some of the trade-offs. So like if you

**[13:49](https://www.youtube.com/watch?v=c5U-XbbEN-g&t=829s)** want to be in chat GPT or you want to be on Google um there's options for you or if you want more control as a merchant over the whole experience you also have um some options there too. And um yeah so that's um that's the main thing that I wanted to share with you. Uh there's a link here on this QR code if you want to look at our docs find out more about how to sign up and how to use that. And if you have any questions, um, I'd love to hear that. I don't know if we can maybe do questions here. Maybe just come talk to me afterwards. We also have a booth over there in the back of the room. So, I'm going to be there for the next hour or so and would love to talk to any of you who have any questions about uh what we offer. Thank you. >> [music]
