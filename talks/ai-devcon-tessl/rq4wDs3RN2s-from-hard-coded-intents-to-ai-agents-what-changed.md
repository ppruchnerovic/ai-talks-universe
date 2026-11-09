---
id: rq4wDs3RN2s
title: "From Hard-Coded Intents to AI Agents: What Changed"
slug: from-hard-coded-intents-to-ai-agents-what-changed
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "AI DevCon NYC 2026"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 21
published_at: 2026-11-08T10:49:21Z
video_id: rq4wDs3RN2s
url: https://www.youtube.com/watch?v=rq4wDs3RN2s
youtube_url: https://www.youtube.com/watch?v=rq4wDs3RN2s
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# From Hard-Coded Intents to AI Agents: What Changed

**Speaker not identified**

`AI DevCon (Tessl)` · `AI DevCon NYC 2026` · `2026` · `21 min`

[Watch the recording](https://www.youtube.com/watch?v=rq4wDs3RN2s) · [Conference site](https://tessl.io/devcon/)

## Description

Voice assistants used to need months of work to add a single new intent: strict grammars, hard-coded mappings and fulfillment built by every app. Akhil Sharma, software engineer at Meta and formerly of the Google Assistant org, and Sudipta S. Mohapatra of ChartHop trace the evolution from hard-coded intents to AI agents. Using a ride-booking example, they show what reasoning loops, tool calls and human-in-the-loop gates change, and what we give up in determinism. Recorded at AI DevCon New York 2026.

What we cover:
– What an intent is, and how assistants used to handle them
– Why adding one new intent took months of work
– Replacing hard-coded grammars with a reasoning loop
– A ride-booking example, from request to confirmed booking
– Human-in-the-loop gates when money is being spent
– What we give up in determinism, and where this is heading

Chapters:
00:00:00 - Introduction: from intents to agents
00:00:55 - What is an intent?
00:03:53 - How intents used to work
00:06:24 - Why one new intent took months
00:07:50 - The limits of hard-coded grammars
00:11:52 - The reasoning loop
00:12:35 - Example: booking a ride to the airport
00:16:01 - Human-in-the-loop gates
00:17:43 - What we give up: determinism
00:19:14 - Where this is heading

Register now for AI DevCon London 2027, June 7–8 at The Brewery, Moorgate:

Try Tessl today and build a software factory you can trust:

🔔 Subscribe for weekly videos on AI-native development

What changed for your team when hard-coded flows became tool calls? Tell us in the comments.

## Transcript

*3,157 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=0s)** Hi, everyone. My name is Akhil. I'm a software engineer at Meta. I'll be talking about me and Sudipta. We'll be talking about this from intents to agent evolution. A little bit about me. Before Meta, I used to work at Google and in Google. I used to work in the Google Assistant org. So a lot of my knowledge about how intents used to work and how they are being migrated to agent comes from that, experience and. Yeah. Hello. My name is. I'm currently a senior software engineer at ChartHop, which is a which is a up and coming startup here in New York City scene. We have been AI native for a while now. So yeah, just kind of focusing on what he brings to the table from his experience at Google and then how we sort of thought about migrating it out to agents with that.

**[0:55](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=55s)** Okay. So I'll start with this. I'll start with, before I start just quick introduction on what intents actually are. So intent basically is if a user talks to an assistant, then what the assistant agent understands out of it is basically an intent. For example, I need to book a cab that's basically the CreateTaxiReservation intent. I get me a taxi home again, CreateTaxiReservation. Now, what used to happen in the previous world when we were still in before the agentic world? A lot of these intents were more hard coded and less on the go. And that created, a limitation that for each user query, only a specific action could be performed.

**[1:51](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=111s)** I need to book a cab. That means one intent, CreateTaxiReservation. That action will be performed so that basically what intent is like just yeah. Today we'll be talking about these three things. Basically the legacy bottleneck about how intents in the previous world were very limited. They worked well, but still the implementation was limited. The effort required to implement a new feature was months versus now, which is like days or maybe weeks. Then Sudipta is going to talk about the rebuild. And then in the end we will also go over like how this even though we're just talking about like intents and assistance, how this is actually being expanded throughout this agent world where, we are moving on from the previously defined

**[2:47](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=167s)** APIs, handshakes to a new, more flexible world. Do you want to add anything to that? No. I mean, it's basically what he said, right? Previously, these intents were hard coded map and on the client side. Whereas now, based on the intent of the user, based on. So think about like the the cab right thing. Right. So you had these phrases that will get mapped and based on those mappings existence, they get mapped onto the actual function that needs to run to execute those actions. Whereas now, because AI is good at knowing what the natural language means, you don't need to have that mapping structure entirely in XML. We'll go through that in detail as we go through the slides.

**[3:35](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=215s)** But then using that understanding by AI, it now itself autonomously picks the tool that it needs to call where you don't need a mapping structure to maintain anymore in the long run, which is very cumbersome. Okay. Yeah. So, I will take the CreateTaxiReservation example to go over the previous world, but basically there were three structure, three parts to it, which were also now kind of the limitations is one, there's a very strict grammar. The user has to say something out of which n you could extract the intent. The user could not just say, oh, can you book me? Actually. You know what? Don't do it.

**[4:23](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=263s)** Oh, but yeah, let's book an Uber to airport. No. Book a lift to the airport. Like something like that. Which is, like, super vague in the previous world. And then you would not be able to take out, they intend out of it. Just adding the grammar for a specific intent. Used to be months of work involving multiple teams. It was start by like getting user queries, examples on what a grammar looks like, then training models, running evals, then using those for the actual code to see how the code is working with that grammar. So it used to be months of work just to introduce the grammar for a single intent. The other thing was there was the the schema of the entities was fixed. So as an example. Like this is where if, if, if an assistant wants to book an Uber, you book a taxi using Uber.

**[5:17](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=317s)** Then first of all, Uber has to tell assistant that, hey, this is something that we can perform. Uber can be used to book a taxi for that. Uber will have to give some inputs to the assistant for Google Assistant or Alexa or Siri. Here's an example of what it used to look like. Uber would give us like this is the intent that they can fulfill, CreateTaxiReservation. It'll give us like if you want to fulfill it, this is the action that needs to be performed. Like basically the URL that needs to be opened. It will also give us the parameters, for example, the drop-off location. Pickup location. It'll also give us other details, like if this, for example, this parameter, drop-off location, is required or not.

**[6:06](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=366s)** So it was a cumbersome long. XML that needed to be provided to the assistance so that a simple action can be performed, which again took a lot of effort from the app's point of view. Basically, these are all the work that need needed to be done. The app had to pick a BII, declare capabilities, built fulfillment on that app. Google in this case will have to create the grammar handle ambiguity. Make sure that the difficult complex parts are gated properly. For example, you don't want to end up spending the user's money before without authentication. So all kinds of things needed to be handled. A lot of it, it was just static routing user at her, something intent is matched. A deep link is triggered. App opens all of the the the

**[7:01](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=421s)** the the execution happens. That's it. One. It used to be a lot of single, single flow without a scope of a like for example, a user, if a user says, do you know the flight that I have tomorrow? Can you, can you book me an Uber for that flight? Those kinds of complex queries could not be fulfilled. Yeah. This is an example of this equation. Like if there's an immigration, Google will not be able to do it. Mostly it will just fall back onto the Google search page. We can go to the next one. Yeah. And then Sudipta will now talk about the next steps of how we are handling that. So this is the part I was talking about, right.

**[7:52](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=472s)** So in the XML that you saw, all of these are hard coded. Now imagine all the different phrases that you have to keep that XML maintained for and all the different things that that assistant might do. Like most of us have Alexa or Google Home at our home. Have you ever wondered how it works behind the scenes? So behind the scenes, there's this huge XML that needed to be maintained in order to map things out, and all the things that you saw subsequently with. If the request doesn't match, it will by itself do a Google search and give you results. Whereas now, you don't have to have that mapping structure in place because you can describe what, the function is doing in English itself, that the agent can understand and then decide when to call it by itself autonomously.

**[8:42](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=522s)** So yeah, in the legacy, it's what I talked about. Right. So we have the XML file that you needed to have, you know, context that needed to be saved on on state. Whereas now it's just one file that needs to define what the tool is. So we hear a defining book_ride as a tool. You give the description as just an English statement. So like book a ride it commits money. It's a destructive action. So the agent knows that this is a dangerous action to to do. But this is how the mapping would work. AI DevCon is coming back to London. Our first London event sold out in June. After our second New York event this November, we're heading back to The Brewery, Moorgate, in 2027, with a bigger lineup and two full days of talks from the people

**[9:34](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=574s)** actually building with agents. You'll hear honest takes on where the industry's at, real stories from teams adopting AI, the wins as well as the messy bits, and where they think things are heading next. It's on June 7th and 8th, and don't tell anyone, but we've got a really great deal for you. Scan this QR code to grab an early bird ticket for just £100. See you in London. Yeah. So. Basically earlier we used to have like this whole XML, but now we are just adding more structures where we had like pickup. There's a string that represents this as a pickup, drop-off, vehicle type, schedule time. And we are adding these over the methods. That methods acts as a tool that can be read by a new by

**[10:32](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=632s)** an agent, and then it knows what action to perform. So now Uber doesn't have to tell Google that, hey, I can book a taxi for you. What Uber does is that over every method that they have for, for example, booking a ride, they just implement a tool that says this method is for booking a taxi. This is what it does right now. Here's how you can call it. And then assistants now. For example, Gemini will now talk to this tool and try to figure out that, okay, this app has this capability instead of it going through a predefined, XML. Yeah. So previously we used to have an intent and a webhook pair where every time you call it, it will use the webhook to kind of call and do that action. Whereas now you just have one defined tool that lives.

**[11:25](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=685s)** Like this. There's you basically define the structure and the description of the tool itself. And then you execute it. If it's resumed, there is something called interrupt with which I will highlight in a little time. It basically allows the user to cancel if it changes in mind midway, which is something you could not do in the past. We'll come back to that point. Now the reasoning loop. So let's say you have a changed location midway. It's what he was giving an example for, right? Like, if I'm confused about where I'm going. Book me a cab to Brooklyn, but. Oh, wait, let's go to Bronx. That needed to. That was very difficult to handle in the past.

**[12:14](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=734s)** Whereas now, because of agents in in-built reasoning, it can understand that the actual cab ride is supposed to go to Bronx, and we don't have to maintain that behind the scenes on the code. This is just an example that we ran through. Yeah. So I can go over there. So basically let's say that the user says book me an Uber to the airport for the flight tomorrow. Now. Google, in the previous time Google would have just like booked an Uber and then looked at the destination and tried to figure out the destination and then maybe it would have failed. Maybe it would not have. But now the way the new AI agents would work is look at this. They will try to figure out what all is going on.

**[13:01](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=781s)** They will say, okay, I need to book an Uber. I need to figure out this time. So the first thing I'll do is I'll run parallel agents. One of them will be, for example, looking at Google Calendar, and then it'll be search in the calendar will say, this is the query, this is the time. And then hand it over to the Google Calendar agent. Now the Google Calendar agent will go over this. Look for the calendar for tomorrow. Try to figure out what all events are there in the calendar, corresponding to the airport. It will return those both of those back to, Gemini. Gemini, for example, let's say let's say Google. Google calendar had two events for the next day. One was a flight from JFK. The other one was for a flight in Newark. So now the agent, instead of just executing whatever it, understood or failing agent

**[13:55](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=835s)** can now question the user again to see. Okay, I found two trips. One is at this time, the other one is this time. Which one do you want? And now the agent. Now. Now the human can decide. Like the morning flight. Now it's way more conversational. We didn't have to define the grammar here, because the grammar is just being handled by the agent itself. The. We didn't have to define the all of that API handshake XML models. We just defined tools over each method which where the tool could, just like in simple language, explain what this method does or what. An API or an app can do, and then agents can just use that tool to figure out what all can be executed. There's also this option of mid flow correction where someone says that,

**[14:47](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=887s)** leave at this time Uber XL list as much. It's a sorry agent says that and then you understand. Oh sorry. No this is not the correct flight. I need to move. It got moved to the other airport. We need to book it to a different airport. So now you don't have to say the full query of, like, hey, do this and do this and book this. You can just say, oh, wait, the other flight or the other airport. And then agent will now start again running parallel about like getting traffic estimation, getting right estimates, running those in parallel, talking to different Google, Google Maps for the time it takes or calendar for some other events, and then get back with like, okay, this is the time we need to leave. Here's what the Uber Uber XL will cost. This is your ride is booked. Yeah.

**[15:37](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=937s)** I mean, basically to add to that is like your your chain of conversation doesn't break. Whereas previously, because it was so hard coded and rigid, if at some point it didn't understand where it needs to go or the user didn't give correct information, the flow will need to start all over again from the beginning. So that's pretty much what's getting highlighted here. And then the last part is just like when the actual booking is being made. Or like money is being spent, for example. Then there's also gates that can that are being added where, for example, human will do human-in-the-loop pause where it looks at book_ride as destructive, which means that it can cost money.

**[16:26](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=986s)** So confirm again. Yeah. This is the interrupt with that I was highlighting earlier for a tool call where we are marking it as destructive. You can give it something called interrupt width where it knows that if it's trying to do a destructive action, it interrupts its own flow and responds back to the user asking, hey, do you want to confirm if this is what you actually want? Again, this is something we were not able to do previously. I can talk about this a little bit. So in the previous case, we didn't have the ability to store history of these conversations. It was just a bunch of API logs. But now the entire conversation itself is the state. So you don't have to separately maintain a history somewhere else.

**[17:21](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=1041s)** The AI pretty much takes care of it. And this is the one I was talking about with tool interrupts where if you call something interrupt with allows you to pause the loop as it's working and ask the user to whether to confirm or deny the request, and then continues on in the same path without breaking the conversation chain. Now, where if if everything is so good. What are some of the things we're giving up? So the main thing of giving up is determinism, right? Previously, because it was so hard coded and because it was the mapping was so rigid, you knew exactly which phrase calls which tool. Whereas now it's it's completely left on the agent's interpretation of the English language itself. Now you can do certain things to improve that on your

**[18:14](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=1094s)** side, which we have seen increased efficiency for like having better guardrails or eval checks. You can have it make sure that it doesn't end up in a constant loop of guessing itself with max turns. Understanding when to insert the interrupt with a tool to make sure that it's not able to do something that it's not supposed to do. There is also latency. Like, it depends on how well the agent can understand, like the from the point of you asking the agent a request to the point of delivering on your request. That is entirely dependent on how well it understands the context in the first place, and how well your guardrail and evals are designed. Whereas previously it was very deterministic, you could you could measure it out and

**[19:06](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=1146s)** improve the performance of it pretty deterministically. Okay. So essentially where this is going is. We have been migrating a lot of things, even in in the work that I'm doing at my company, where we are using now instead of hard-coded API calls in terms of user requests, we are making tool calls for most of those. So my company is currently doing HR tech platform stuff. So let's say I want to hire somebody or I want to send somebody an offer letter. I can ask my agent in Bill to like, hey, send this person an offer letter. It knows which calls to make to grab that data and then what tools to

**[19:58](https://www.youtube.com/watch?v=rq4wDs3RN2s&t=1198s)** execute to actually send that information out. Do you want to add anything to it? I mean, that's basically the the MCP route. So previously columns are tools, but now we basically have some sort of an MCP layer that allows agents to understand which tools are available to them. Yeah. Yeah, that's all we had. But we have time for questions. We're happy to answer a question on, like, this new agent world, how different agents are talking with each other. MCP etc..
