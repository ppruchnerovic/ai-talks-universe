---
id: l8m0YpNf4XI
title: "From Cypher to Conversation: MCP at WestJet - Anton Lysov, WestJet"
slug: from-cypher-to-conversation-mcp-at-westjet-anton-lysov
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: ["Anton Lysov"]
channel: "Agentic AI Foundation"
duration_min: 15
published_at: 2026-04-13T23:18:17Z
video_id: l8m0YpNf4XI
youtube_url: https://www.youtube.com/watch?v=l8m0YpNf4XI
tags: []
transcript: true
---

# From Cypher to Conversation: MCP at WestJet - Anton Lysov, WestJet

**Anton Lysov**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=l8m0YpNf4XI) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

From Cypher to Conversation: MCP at WestJet - Anton Lysov, WestJet

At WestJet, our flight schedule is modeled in a Neo4j graph database - airports, routes, aircrafts, seasonal schedules. The data is rich, but accessing it required Cypher expertise most stakeholders don't have.

I built an MCP server to change that. By creating a proxy layer connecting Claude to our Neo4j database, I enabled non-technical colleagues to query complex flight relationships using natural language. No Cypher. No waiting for developers. Just questions and answers.

This talk covers the journey from idea to working pilot: why I chose MCP, how I architected a proxy server wrapping the Neo4j MCP server, and what I learned deploying it internally. I'll give a live demo showing how analysts can explore our flight network conversationally.

This isn't a top-down initiative. It's about individual ownership - recognizing potential in data your team already maintains and using MCP to unlock value for people who couldn't access it before.
Whether you're exploring MCP for enterprise data or graph databases, this talk offers a practical, beginner-friendly blueprint.

## Transcript

*2,132 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=0s)** If you flew WestJet to get here, there's a non-zero chance a service my team maintains told you which gate to go. So, if you're late, then blame me and me. Have you ever been curious how airlines actually manage their schedule? It's a little bit more complicated than a bus schedule. Like, we have an entire team that manages the schedule in a graph database more. Today, I'll walk you through how we manage our flight network and how we use MCP to open the data up to people who not knowledgeable in the Cypher query language. For people who don't know, Cypher is the query language for the Neo4j graph database. Let me show you how. But, first, let me give you a bit of a context. The airline The airline industry has one of the highest failure

**[0:47](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=47s)** rates of any sector. The US has literally hundreds of defunct airlines. In Canada, over 260 airlines have come and gone. And here's the kicker. Every single discount airline launched in Canada since 2000 has folded. Every single one. WestJet turns 30 this year. Started in 1996 with three used 737s, 225 employees, and five destinations in Western Canada. Today, we have roughly 200 aircrafts, over 15,000 employees, and over 100 destinations across 2,300s. Canada's second largest airline, eighth in North America by frequency. If airlines were startups, and honestly, they kind of are, WestJet is is the one that survived the series Z.

**[1:36](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=96s)** Um, so that's who we are, and let me tell you what I actually do there. All right, digital APIs team. I'm on a digital APIs team. We build, test, and run a fleet of microservices powering westjet.com, our iOS and on Android applications, as well as other various internal systems. Our services cover pricing. So, if you saw WestJet ad online on the internet, the price came from us. We also cover trip information. Questions like, where's my where's my flight? Or, you'll receive a push notification from us on your mobile phone. But today, we'll cover particular area in more detail, which is scheduling. These are two screenshots from our website. The one on the left you see, so

**[2:24](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=144s)** whenever you land on the westjet.com, you'll be presented with the options to choose your origin, destination. And this is one of the use cases this service covers. Another one is whenever you go into detail view about your flight, you can actually see the various amenities that are going to be presented on the flight. And some of the routes are actually not serviceable year-round, so you'll see a little disclaimer that hey, your route is not uh is not available at this time of the year. But here's something that most people don't really think about. When you go to westjet.com and land on this little widget, we'll only show you valid city pairs. You can't even type a route that we don't serve.

**[3:11](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=191s)** And most most airlines in North America don't really bother about this. They'll let you search whatever destination you want to and be like, nah, sorry, nothing. Well, at WestJet, we validate up front. And uh here's a fun fact for you. Only 35% of our theoretical network ends up being routable. That is, 65% is eliminated by business rules. So, let me show you how. Yeah, so why is why is airline scheduling so hard? One example is uh cabotage rules. You want to fly Las Vegas to New York with a stop in Toronto? Sounds fine, right? Nope. That's a domestic US route. We're Canadian carrier can do that. Entire category of OD pairs gone. Minimum connection time. Are you trying

**[3:59](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=239s)** to connect through Toronto? We need to satisfy minimum connection time for a domestic flight and it's even more time for international flight with customs. If the math doesn't work out, that connection doesn't get published. Nobody wants to sprint through the terminal um on a short connection, right? Um another another pain point is the security. If you want to fly from Toronto to Dublin via Vancouver, we technically have this we technically have both flights, but you'd first fly across Canada just to turn around and fly across the Atlantic. We don't show this product because because really why would you do that? And all of these changes by um and all of these changes by day of the week week and the season. Thousands of flights per day, hundreds

**[4:46](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=286s)** of airports. It's a combinatorial explosion of it depends. Here comes the old way. How do you even manage all this? I think you already know it's beautiful, horrifying spreadsheets. Schedule used to be updated only twice a year for summer and winter. It was very laborious and very expensive process. The good news, we've come up with something better. Enter the schedule publication service. Um first we we use the same file, the industry standard format airlines used to exchange schedules. Our schedule team generates this for WestJet and we also receive them for our partner from our partner airlines. If you've never seen a SIM file before, imagine a flat file format from the 70s and then it looks exactly like you would

**[5:33](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=333s)** think a flat file format from the 70s looks. It's got character positioning parsing. It's got fixed with fields. It's beautiful in this in this it predates me by decades kind of way. We We'll receive amenities data that uh we receive every every day. MCT mineral connection time, we receive that information from a vendor. We'll also apply various business rules, security cabotage seasonality and other various business rules that get baked into the into the system. SPS crunches all of this and outputs clean routable OD pairs, routes, and amenities data. That's what powers westjet.com and all our other systems. And just to give you an idea what a single file looks like. Yeah.

**[6:21](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=381s)** All right. But uh what is actually our problem? We end up having a very rich system uh that is stored in Neo4j database. But in order to um besides exposing the information on the external system, it would be great if uh somebody could tap into this data, but in order to access it, they would need to know the domain language, which is Cypher. All of this data lives in a Neo4j graph. Airports as nodes, flights as edges, properties for everything, times distances equipment connection rules. Incredibly powerful for network analysis. But to query it, you need a Cypher, the query language for Neo4j. And the people who would benefit most of it, the scheduling team, network planning optimization team, they might not know Cypher. They're people who

**[7:10](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=430s)** would decide which cities WestJet flies to, which connection at Calgary aren't working. It is is a business question, not a database question. The query The query language shouldn't be a barrier for it. So, the missing The mission was simple. Democratize access to WestJet flight network graph. Let anyone, regardless of their technical background, ask questions in plain English and get real answers uh backed by real data. No Cypher, no begging a developer to run a query for you. MCP made it all possible, not as a proof of concept, not as a hack day project, it's an actual tool that people use. This is a high-level architecture of the solution. So, you have a your cloud desktop as a client where people a person would enter query. It would go through our custom MCP proxy

**[7:59](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=479s)** that sits in front of a Neo4j MCP server that receives expose the tool and it passes it uh it makes a request to Neo4j database. Mhm. And uh everything runs in Kubernetes. That's not surprising. And uh let me do a short demo. So, I'm not taking my chances on the on this Wi-Fi, so I'll show you a history from my cloud instance. All right. So, here I typed in an answer a question a question. How many direct destinations WestJet serves from Victoria, BC? Oh. Oh, my bad. All right. Here we go.

**[8:51](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=531s)** Uh should I make it bigger? So, here's my cloud desktop. I entered a question, how many direct destinations WestJet serves from Victoria BC? And this is how the flow would go. It would interpret the question, refine it, pass it, um and uh in order to optimize the flow a little bit I entered in the context to show the work it's doing. And especially to show what kind of queries uh it was using against database. So, it would load the tools. That's pretty straightforward. It would ask for the Neo4j schema, do the work, and uh this uh I would say the most interesting

**[9:38](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=578s)** piece where it actually generates the query, the cipher query. You could see starts with a match. Oop. That's the query. It gets the response from the database. And uh it puts together in uh in an answer. You'll see that uh WestJet serves eight direct non-stop destinations from Victoria, BC. And then the format you could play with it. You can um type in in the context how you want the data preserved uh shown into you. Um we played around with the displaying this data on the map as well. Yep. Uh And that uh concludes my presentation. Thanks so much. Yes. Can you Can you

**[10:30](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=630s)** Oh yeah. It's good. Uh thank you. That was great. How does the schedule optimization team use it? That's a very good question. Um when you create a schedule, you want to make sure whenever a person makes makes a layover at an airport, you want to increase the number of possible connections could be happening in the cities. So, that's one of the use cases that we found the schedule optimization team would be using this for. Yes. I'm sorry if I missed this, but what does your proxy layer do that's like different from the Neo4j layer

**[11:21](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=681s)** itself? Yes, this is a very good question. I think the idea is to Right now, uh we had the luxury of uh placing this whole system internally, and we don't have to expose it to real actual customers. It's only using being internally. So the idea is to implement the authentication layer in that proxy and potentially expose other tools expose informational services that our team offers potentially using that MCP server. All right. Um this is a very good question. I think we don't have immediate plans to do that. As of right now um for now it's just going to be used

**[12:08](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=728s)** internally. Mhm. I think um we entertain that question and I think we would need definitely a lot of filtering. The in terms of what kind of questions you can ask that uh uh ask the service. So we wouldn't become uh we wouldn't get in the news of people asking um certain questions. We want Yeah, we definitely want to avoid the PR nightmare. Yeah. Yes. Uh have you talked to Neo4j and the

**[12:58](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=778s)** team here and whether they've done anything similar to your purpose and if not I mean what they could learn from Yeah, definitely came right by their booth. Uh they're one of the vendors one of the sponsors of this uh um of this event and uh the question I asked them if uh So in my project I use Claude the state-of-the-art model to that generates those queries, right? My question was if they're thinking about fine-tuning or optimizing LLMs for for Cypher in particular and the answer was no. They also recommended that I just using state-of-the-art models. But under the hood for Neo4j they're using they have a project called text-to-Cypher. That's what that's what LLMs use um

**[13:44](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=824s)** to generate those those Cypher the the Cypher queries. Yes. Did you have any challenges validating the data? So one of the tricky things is you're writing a query back to the graph database. The eight routes that you listed did you know that they're correct? Did you do any evaluations or did you run into any data validation issues? Right. Uh another good question about um and that's something um I came to this conference is uh um definitely wanted to pick up people's brain to on how to eval how to improve the quality of the data. So how we approach this project is we created this tool, spent as minimum resources as possible, and gave it to uh gave it to another team to try out.

**[14:31](https://www.youtube.com/watch?v=l8m0YpNf4XI&t=871s)** And then based on their actual use cases we will we'll see if they find it useful and if they don't then we'll just move on to to something else. Yeah. All right. Thank you guys.
