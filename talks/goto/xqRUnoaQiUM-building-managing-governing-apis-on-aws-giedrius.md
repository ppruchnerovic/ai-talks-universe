---
id: xqRUnoaQiUM
title: "Building, Managing & Governing APIs on AWS • Giedrius Praspaliauskas • GOTO 2025"
slug: building-managing-governing-apis-on-aws-giedrius
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Giedrius Praspaliauskas"]
channel: "GOTO Conferences"
duration_min: 26
published_at: 2026-04-21T12:01:50Z
video_id: xqRUnoaQiUM
url: https://www.youtube.com/watch?v=xqRUnoaQiUM
youtube_url: https://www.youtube.com/watch?v=xqRUnoaQiUM
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "Giedrius Praspaliauskas", "Janak Agarwal", "Software Architecture", "AWS", "EventBridge", "Serverless Platform", "Infrastructure", "GOTO Serverless Day", "Serverless", "Event-Driven Architecture", "Serverless Compute", "Lambda", "AWS Serverless", "Serverless at Scale"]
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# Building, Managing & Governing APIs on AWS • Giedrius Praspaliauskas • GOTO 2025

**Giedrius Praspaliauskas**

`GOTO Conferences` · `GOTO` · `2026` · `26 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#Giedrius Praspaliauskas` `#Janak Agarwal` `#Software Architecture` `#AWS` `#EventBridge` `#Serverless Platform` `#Infrastructure` `#GOTO Serverless Day` `#Serverless` `#Event-Driven Architecture` `#Serverless Compute` `#Lambda` `#AWS Serverless` `#Serverless at Scale`

[Watch the recording](https://www.youtube.com/watch?v=xqRUnoaQiUM) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Serverless 2025. #GOTOcon #GOTOserverless

Giedrius Praspaliauskas - Senior Solutions Architect, Serverless at AWS

RESOURCES

Links

ABSTRACT
As organizations integrate AI agents with existing systems through APIs and new protocols, they revisit strategies of building, management, and governance of the APIs.

This session explores how AWS services and features help customers implement effective API strategies. We'll walk you through the complete API lifecycle, highlighting key considerations at each stage and showing the tools available to ensure successful implementation. [...]

TIMECODES
00:00 Intro
02:12 API lifecycle
03:08 Plan & design
04:40 Develop & test
10:12 Secure
12:55 Deploy & publish
14:10 Scale
18:14 Monitor
21:12 Insights & analytics
23:03 API discoverability & adoption
24:47 Monetize
26:01 Outro

Download slides and read the full abstract here:

RECOMMENDED BOOKS
Peter Sbarski • Serverless Architectures on AWS • https://amzn.to/3hJzEUM
Michael Stack • Event-Driven Architecture in Golang • https://amzn.to/3G5e8ST
Ashley Peacock • Serverless Apps on Cloudflare • https://amzn.to/3EU7P85
Jeroen Mulder • Multi-Cloud Strategy for Cloud Architects • https://amzn.to/3FdNDOA

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*3,763 words · source: supa (en, exact timings)*

**[0:13](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=13s)** I'm going to do this today. I will talk about building, managing, governing APIs on AWS. And also, regardless of what he said, we are not going to escape AI agentic in this talk, either. For simple reason that it's everywhere. It's AI age, so we will throughout this entire presentation, as long as we as we talk about API management, API governance, I also will talk about tools, about tooling that is using agents, AI, gen AI, LLMs, and so on. And it's very broad topic, so I will

**[1:02](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=62s)** touch surface and check resources that are linked throughout this presentation, and you'll see QR codes there for more details, and we'll start with listing just two services. Usually, when customers are going for implementation of APIs on AWS, these are two services to use, Amazon API Gateway and AppSync, because they are managed, they are scalable, you don't have to care about much while using them. So, that's one reason. Another reason also is that they are pay-per-use and have built-in security. Again, I will not go into feature-by-feature explanation, what they do, how they work, and so on. If you look up, for example, Eric Johnson, who opened this day, on YouTube, you'll see his presentations at re:Invent. Notably, I

**[1:53](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=113s)** didn't know API Gateway did that, and so on, where he goes in-depth. Some other presentations, if you go to serverlessland.com, there are plenty of resources, so you can find deep dives, workshops, and so on, and uh look into the services. Uh what we'll talk about mostly API life cycle. And those 10 different life cycle stages and high-level activities. And this QR code points to our opinionated way of doing things throughout this life cycle documented on serverlessland.com. For each of the stages, you'll see links into workshops, deep dives, videos from re:Invent that we think you should know, and it's constantly being

**[2:43](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=163s)** updated so bookmark that, and take a look. And throughout this presentation, I'll go into every single of these stages, and we'll talk about from different persona perspective. You see API developer, operators, business owners, API users, and so on. What tooling is available there? What kind of activities they performing there? And how it works for them. So, with that said, plan and design, first part. Uh this involves working backwards from business needs in identifying API contract that you will need, and typically, we use API driven development, ideally, and it's not new. We've been talking about this for years and years, and this is not specific to API Gateway or AWS. It's simply practice of the designing, building APIs before

**[3:32](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=212s)** building any other parts of the system, uh ideally, again, that user user support APIs. And this API first design establishes your contract with the rest of the world that you shouldn't change, but stuff happens. You change, you think about versioning, which is very important when you when we start thinking about how AI systems, agents outside of your world, interact with you. So, everyone now talks and then tries MCP, model context protocol. Okay, how do you implement versioning there? It's supposed to be there, because it changes over time, and you don't want to break customers who implemented it. It's still early early days, so you still need to think about it, and as it is new layer of APIs, and it

**[4:22](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=262s)** operates in parallel of APIs, or let's say old school APIs, REST APIs, SOAP, and so on. It's still API, it's still your contract, even if it's a bit more loose to outside world. So, think about those needs while you're designing and next, when design is done, results of those planning and design stages serve as a basis to develop, document, and test APIs. And there's usually two ways how we implement them on on AWS. One is you just go to API Gateway console, go to API uh start new API, start putting resources, methods associating with back-end integration targets, and so on, and so on. That's one visual way. Another way is infrastructure as a code, uh using CloudFormation, Terraform, CDK,

**[5:12](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=312s)** similar tools, and so on. So, and to simplify that infrastructure as a code, we really often switch to open API specification, which is industry standard, define API there, and then refer to open API specification from infrastructure as a code. So, that's typical way of doing things. Import-export allows external partners to integrate with API Gateway, and most of the external integrations, let's say from SmartBear, SwaggerHub, as it used to be known, now API Hub, or Postman Enterprise. All them use the same integration approach. They import open API into API Gateway, open API specification with resources specified using Amazon API Gateway extensions to open API. Now, when you use infrastructure as a

**[5:59](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=359s)** code, all AI-assisted API development tools understand it and can work just fine with your APIs the same way as they work with code. Any agentic development tools, Hero, QCLI, QDeveloper, any non-AWS tools, any open-source tools, they have enough knowledge or enough or they've seen enough information in their training sets of their LLMs that are used behind the scenes to build open API specifications if you ask them in a proper way. So, it's mostly at that point about spec-driven development, specification-driven development, where you specify in the most detailed way you can what you want out of that API, and what you want of that API code

**[6:47](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=407s)** behind, and then you can use, like in this particular case on the screenshot, Amazon Q, just start telling that build me e-commerce API for pet store that should have uh car checkout, you should have user you should user management, and so on, and so on. So, more detailed definitions you give, it's going to be easier to use it, and then refactoring migrations testing it's just just a code. And next step is centralizing guidance, where you can take your organizational knowledge, your organizational best practices, style guides, use knowledge base, but in this case, Amazon Bedrock knowledge base, uh and then the link points to the repository that has all that code. And you can expose to your development

**[7:39](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=459s)** tools, development processes, that knowledge base through agents, through MCP, model context protocol, extending that knowledge and centralizing, so you don't have do not have to write those rule files for every single project, and so on. You can just simply ask questions. And next step is specialized AI agents for API Gateway. Couple examples on that diagram, where for every time an API Gateway gets deployed to production, it will kick off, it will pull configuration of that API Gateway, configuration of the of the account itself, and generate recommendations based on your organizational best practices, what should be improved, and then send that message to Slack, to email, that maybe owners identified as in as a as email address in in in tags of the resource.

**[8:30](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=510s)** Testing. For testing, most simplistic way, you just go to API Gateway console, you provide payload, or provide query string, path parameters, and so on, try few of those requests, done. Next, much better way, you just use testing frameworks. You just go with the API testing frameworks from third parties, API clients, automation, Postman automation, and for example, for enterprise, it's quite popular, and so on. And then, security partners, AWS doesn't have out-of-the-box, doesn't provide out-of-the-box, at least yet, security and penetration testing solutions for API Gateway, but there are plenty of partners in security space that would have those tools. And that's where AI again comes into the picture in

**[9:18](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=558s)** slightly different way. One thing, it helps you to uh generate synthetic data for testing. It helps you to generate test cases, look, perform coverage analysis, response validation, threat modeling, uh even penetration testing. There is uh there is hacking APIs GPT. I haven't tried it, cannot recommend, cannot not recommend. You look at it, maybe it's tool for you to use. And as uh MCPs become part of APIs, now question, how do we test them? Because in many cases, they have APIs behind. You you do not build entirely new system just to put MCP in front of it. You have existing APIs and most likely that's going to be your protocol with MCPs when you go down the road. So that's one more

**[10:09](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=609s)** one more service that you will need to test and see that it's working. Next securing. Even though it's supposed to be every it's it's even though it's singled out as a separate life cycle stage, it should be part of your every single step along the way and there are so many ways and options to secure APIs on AWS starting from control plane access control where you specify who can do what with APIs, data plane access control where you can specify who can access who can have access to what kind of data, network level controls, governance where you can also implement detective preventive uh rules directly appointing to API gateway and so on. And all the specific specific security features, it's area that is still

**[10:58](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=658s)** maturing for AI space especially when you look at MCP. In last two or three months it evolved security from local to remote to auth and so on. All those things are still happening but you have to start thinking thinking about it right now. Another part to security and how you can use those new toolings that came into the market or or into the picture recently is use those AI agents to assess your security posture, configurations, troubleshoot your issues and incidents, use AI most to be exact it would be more machine learning for anomaly detection, for prevention, for detection anomalies

**[11:46](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=706s)** while they're happening and stopping traffic on that particular resource and so on and so on. And then again, penetration testing from using tools from partners uh one more area. And just as a reminder, it's not specific to this talk in any way. Security should be applied at all layers. It's not specific to any of API services. This is small example of small microservice that has only one lambda function and one DynamoDB or Aurora serverless instance behind. So it's small microservice, nothing special. And you see how many auxiliary or additional services and features of those services can be employed to make sure that your API is secure as secure as possible. And frankly, if you use infrastructure

**[12:32](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=752s)** as a code, you simply point that agentic IDE or CLI that you're using to your code and simply ask, "Okay, where are potential security gaps? What I am missing? What features of services that I'm using are not enabled, not used in my stack?" You may be surprised how much information you can get from a simple question. Deploying as the next step. So it's deployment operating, it's pretty straightforward. It's maintaining after deployment. But as you use infrastructure as a code, it's just a code. You do not have anything special to APIs there. It's entire stack and API is just part of that stack most likely. Uh if you use CICD pipelines based on AWS services on well-known industries leaders services

**[13:24](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=804s)** most likely LLM in your environment where in your development environment, in your operational environment that you are using as a tool will have enough information in the training set to be able to generate configurations for those services, to be able to inspect those services. If you have tools enabled, for example, if you have I don't know uh Terraform MCP, take a look at that Terraform deployment or Argo CD, can you inspect that implementation for me? Can you inspect the configuration for me and so on. Just think about what you want to do and ask tool if it can do. In most cases it will and again, it's not specific to API in any way.

**[14:11](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=851s)** Scaling. So Amazon API managed services unless you run APIs on your own infrastructure that you manage by themselves, this is also an option to serve APIs on AWS. But managed services scale automatically and they scale to massive levels. Think about all those prime days, Super Bowls that we are serving. And service team shared last number that I know it in 2023, API gateway processed over 100 trillion with a T process requests per per per 2023 year. So most likely API gateway will not be bottleneck in your system. Most likely it's going to be your stack behind. Only thing that comes to API gateway that you need to check when you scale is

**[15:00](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=900s)** your account region request per second quota. It's 10,000 by default default in most of the regions in the larger regions. Take a look, make sure you have enough. It's self-service increase to some level or you submit support ticket above that. But you need to track resource utilization for entire stack. You have to know if it's scaling behind the scenes as fast as you need. If you use lambda authorizer, do you have enough lambda concurrency high enough lambda concurrency quota in your account to be able to accommodate that spike in the request if it happens and so on. And at some point we start talking about scaling in and then going into multi-account architectures for blast control, for quota management,

**[15:49](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=949s)** making sure that that you do not build too big thing to fail because it will affect your business not just user experience. And here >> [sighs] >> AI comes from two sides. >> [snorts] >> One is again, building operational side, uh predictive predictive scaling of your back end based on your on your traffic patterns in the past and so on. All that is nice and and square. But that's maybe first place along the along that life cycle where you start thinking about how usage of your services by AI outside of your stack will affect it. Think about let's say

**[16:39](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=999s)** last month I believe Claude published in on their blog article about multi-agent architectures and how for some of the tasks multiple agents when they are split start brute forcing through some of the tasks and repeat the same task again and again multiple agents as they getting errors until they get right right response or right result. Now think if that agent has as part of their logic has step or tool to connect to your API and ask for data. And now that brute force ends up as a huge spike in consumption on your API end. Now do you have anything to prevent it to make sure that rest of the users still can use your API especially if you have resources in the back that may not scale fast enough. Do you have

**[17:30](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1050s)** throttling enabled? Do you have throttling per resource, per individual user of that API and so on and so on. So all those things when it comes to consumption by highly unpredictable source of the requests and also long running requests uh because if again, if you are handling that on infrastructure that you manage by yourself that is not elastic uh scaled automatically or if it's not serverless that would scale almost immediately or immediately, you have to think about those long running sessions. Do I have enough capacity in the back pre-provisioned for to to handle that load? And that's where we come to monitoring uh activity of of the life cycle as part

**[18:20](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1100s)** of operations where we use those traditional observability tools for any AWS service most likely you used CloudWatch logs, CloudWatch metrics, X-Ray. Those are kind of three main or three factor of tools for observability in in AWS. One thing though, there are plenty of observability partners. And most likely if you're a larger organization, enterprise and so on, take a look at what your partners observability partners that you have in house, all those DataDogs and and Sumo and and Splunk and whatnot, Honeycomb. They most likely have API gateway specific features already available out of the box, dashboards, reports, analysis and so on. Use it.

**[19:08](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1148s)** If that's your in-house standard, there is no need to use just AWS services. Though as I will show on the few next slides uh it has its own advantage. For example, AI operations in CloudWatch Insights you can select some subset of logs. Something happened. I see that something happened at that time. I have maybe metrics increase for my errors. Maybe I start seeing more log error logs in my logs and so on. I just select some period of time and tell, "Go investigate." And it will go and then for a few minutes just will keep adding some information on that right-hand side column, "Okay, I found this. I found that. I correlated with this event. I correlated with that change, and then we'll come up with hypotheses and proposal for how to fix

**[19:58](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1198s)** it. So, that's one of the tools. Another under quite often underestimated old-fashioned command line tool and with new with new generation of those tools like QCLI, where you as a developer work in in command line. Operators do the same. Operators can use that tool just fine. And it's even more powerful for operators than for developers because it can it is capable using tools and MCP and agents exposed to MCP to troubleshoot, to pull logs, to correlate the same way as that as that CloudWatch Insights agentic investigation. You can do that from command line. You simply ask,

**[20:47](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1247s)** "Okay, what kind of errors do I have in the in that lambda?" And or take a look at API Gateway increased increased latency. Can you see something wrong in rest of the logs and so on. So, it will go, it will collect logs, it will do analysis for you. If ask for next step recommendation, "How to fix this issue?" It will provide recommendation and if you allow it will even implement it. Now, next insights and analytics. Once it's in use, monitoring is just part of operational part. A part of operational picture. Now, insights understanding what is going on in a deeper level. Do I have some areas of for improvement? Do I have some business concerns? That's where insights come into the picture and in CloudWatch Log Insights you can use, for example,

**[21:36](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1296s)** natural language to SQL or to CloudWatch Logs query language translation. And once you have those logs selected that you are interested in, you want to analyze, you can ask for summary and you see in the middle that I know on the middle it provides summary of the logs that are selected at the bottom. Uh and you can analyze you can also visualize. That's typically on the left at the top. That's from API Gateway management console. Bottom right it's custom custom dashboard with business metrics that are emitted from lambda function in the back using embedded metrics format EMF. That's cheaper way to embed metrics that are business specific from your lambda functions instead of custom metrics in CloudWatch. And build those dashboards. And next

**[22:24](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1344s)** step, even better, if you stream logs, for example, this one, this repo is analysis of access logs where access logs from API Gateway can be streamed into S3 where it can be picked up by Athena, enriched along the way if you want using Kinesis, and then using QuickSight analyze it. And QuickSight can can analyze, can provide narrative of your data. You can ask questions in natural language to analyze, to build your dashboards and so on and so on. QuickSight has really really rich analytics engine based on AI. So, try it. And not last, but close to that, discoverability and adoption. So, as a customer scale their numbers of API products and then

**[23:12](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1392s)** number of consumers, it becomes complicated to manage that entire thing and provide information they are looking at onboard them when they ask for API access and so on and so on. And that's where those common challenges start surfacing. Discoverability, duplication of effort across multiple teams internally as they start building APIs that overlap, outdated API documentation, and so on and so on. And AI's they have their own take onto it. If it is hard to understand your documentation for human, how to use it, how do you expect that machine, that robot to understand it better than human what you meant where so much is cultural and then maybe between the lines. So, that's one aspect. How to build documentation that is clear enough for

**[24:00](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1440s)** both humans and machines. And answer is samples, details, and so on and so on. And another part is how I can use AI and agentic tooling for developers to improve it where you can simply go and ask, "Rewrite it in a more concise way." Or "Generate documentation gaps based on on my code." And so on and so on. And then publish to either open source portal or there are partner solutions for developer portal. You can pick either. And also there is still available API Gateway uh developer portal serverless version that you can self-manage and and host by yourself. And last part, monetization. So, that's

**[24:48](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1488s)** last slide that I want you to uh to to take away with you. How do we monetize? Because more and more of those APIs are packaged as products and sold to consumers because you want to make sure you have money to pay for that infrastructure that those APIs are running on. So, there are few ways. One is uh take it, package as usage plan, sell it on the marketplace. Or sell data APIs through data exchange. And two other approaches would be build by request. If you need to build per consumption, in that case you go back to that analytics solution that I showed you uh based on access logs, it's just one more report. Give me breakdown of requests by API key. An API key is

**[25:39](https://www.youtube.com/watch?v=xqRUnoaQiUM&t=1539s)** issued to particular tenant of yours. Or create packages of APIs as products and sell them to your customers as SKUs as particular product. Those three APIs are my pro plan. If I add those two APIs to the pro plan, I get enterprise plan and you consume as much as you want. We just make sure that price is right. And with that, thank you. >> [applause]
