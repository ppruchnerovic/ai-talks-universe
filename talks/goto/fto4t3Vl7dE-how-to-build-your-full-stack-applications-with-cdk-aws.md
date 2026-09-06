---
id: fto4t3Vl7dE
title: "How to Build Your Full-Stack Applications With CDK & AWS Amplify • Erik Hanchett • GOTO 2025"
slug: how-to-build-your-full-stack-applications-with-cdk-aws
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Erik Hanchett"]
channel: "GOTO Conferences"
duration_min: 26
published_at: 2026-05-19T12:00:54Z
video_id: fto4t3Vl7dE
url: https://www.youtube.com/watch?v=fto4t3Vl7dE
youtube_url: https://www.youtube.com/watch?v=fto4t3Vl7dE
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "Erik Hanchett", "KIRO", "AWS Amplify", "AWS CDK", "GOTO Serverless Day", "AWS", "Serverless", "EDA", "GenAI", "Event-Driven Architecture", "Serverless Compute"]
topics: []
transcript: true
---

# How to Build Your Full-Stack Applications With CDK & AWS Amplify • Erik Hanchett • GOTO 2025

**Erik Hanchett**

`GOTO Conferences` · `GOTO` · `2026` · `26 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#Erik Hanchett` `#KIRO` `#AWS Amplify` `#AWS CDK` `#GOTO Serverless Day` `#AWS` `#Serverless` `#EDA` `#GenAI` `#Event-Driven Architecture` `#Serverless Compute`

[Watch the recording](https://www.youtube.com/watch?v=fto4t3Vl7dE) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Serverless 2025. #GOTOcon #GOTOserverless

Erik Hanchett - Senior Developer Advocate at AWS @ProgramWithErik

RESOURCES

ABSTRACT
Building full-stack applications comes with a host of complexities. However, did you know with AWS Amplify you can now enjoy the benefits of authoring your frontend and backend completely with TypeScript and still leverage the underlying CDK and its ecosystem?

In this talk, we'll look at some new design patterns that you can leverage when building full-stack applications from start to finish. We’ll also look at how you can leverage AI to make this task even more straight forward. [...]

TIMECODES
00:00 Intro
01:45 How can we make app development faster?
03:01 Let's create a story teller app
03:47 Demo
07:33 Story teller app
10:22 Infrastructure as code
11:44 What tools do we need?
14:48 AWS Amplify Gen 2
21:21 Demo
25:17 Outro

Read the full abstract here:

RECOMMENDED BOOKS
Sheen Brisals & Luke Hedger • Serverless Development on AWS • https://amzn.to/3W3Sw2f
Adam Bellemare • Building Event-Driven Microservices • https://amzn.to/3WfNKfM
Peter Sbarski • Serverless Architectures on AWS • https://amzn.to/3hJzEUM
Michael Stack • Event-Driven Architecture in Golang • https://amzn.to/3G5e8ST
Ford, Richards, Sadalage & Dehghani • Software Architecture: The Hard Parts • https://amzn.to/3v4pKQS
James Urquhart • Flow Architectures • https://amzn.to/3Tyz8cY

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*4,327 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=0s)** [Music] So, I'm Eric. I'm a senior developer advocate for AWS. Uh, as the introduction said, I'm a huge Vue.js fan. I'm a big fan of frontend and full stack apps. And you can find me on all the socials, E R I K C. I spell my name the right way, other unlike the previous speaker Eric Johnson. So just keep that in mind. You can see here uh I also have a YouTube channel at Eric. Video. So feel free to watch some of my videos. I do videos on AWS frontend development and all those other things. I also today for you in this audience, I have some

**[0:48](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=48s)** stickers in my pocket. Not a lot, but if you come up to me afterwards, show me that you have uh show me that you're interested. Uh follow me on LinkedIn. I will give you a sticker until I run out. That is. So, who here I'm going to ask a few questions. Who here has heard of Curo? Okay, I see quite a few hands. That's good. Who here has heard of Amplify? Okay, many more. Good. Well, you're in the right place for both of these. So, we're going to go into them, talk about how you can use it today. And I really want to kind of show all the little features that we have and how you can build apps cuz AWS has like 200 different services. And I don't know about you, I don't know all of them, but I really want to focus

**[1:37](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=97s)** on ones that are going to be in this talk today. Focus on ones that can get you up and running quickly. All right? And get your app running fast because I really like this idea. How can we make app development faster? So that is everything from how do we quickly deploy our applications? How do we code faster? And so we've seen a lot of amazing talks today, especially from Nick and Eric today about like orchestration and building agents, but not all of us are doing that and we can do that, but how do we get up and running quickly? So we don't for those of you who aren't going to be using a Kubernetes cluster um we may have a website we need to host it we need to be able to talk to Lambda functions we may need to talk to cloud or large language model so let's take a look at how we can do this quickly

**[2:27](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=147s)** so Kira is the AI ID this is our brand new agentic IDE that we released just recently in the last few weeks we have been so happy with the reception We had to put up a wait list after 24 hours because we got so many people signing up and trying it out. People are really uh vibing with with it. So, we are so happy to have it. Uh there is a wait list right now. So, if you're interested, definitely check it out. And I want to show you a few few features of it and how you can code faster with it as well. So, we're going to create a storybuilding app. So, I have a couple of kids. So, let's imagine we want to create an app that generates a fantastic story, a mythical story, and create some pictures that are talking to some of these AWS services. And we want to build

**[3:16](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=196s)** this fast, efficient, and and something that makes sense. It's going to look like this at the end. I'll do a quick demo, but you're going to be able to put a prompt in and use that as a prompt to create this story. And it's going to use a lot of different backend AWS services like S3, uh, Amazon Bedrock. It's going to use our Amplify hosting service to host the website. This is an Nex.js application. So, I kind of want to show that. Now, we do have Curo here and I kind of want to show you the IDE. I have a video, but I thought this would be more interesting. So, this is what the IDE looks like. And you can see here we have two options on the right hand side, vibe and spec mode. So I think this is what really differentiates differentiates us from

**[4:04](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=244s)** some of uh the other agentic tools out there. I mean everybody does Vive but definitely spec. So this is a way to create uh when you're adding a new feature you want to create some in-depth uh you have some like you want to really create a feature you want it to be planned out correctly. So this creates a spec document it creates a design document some implementation details as well. uh we also have ways to we can generate documentation. So right here we have our agent steering. So this is in this case these aren't here but uh you can create basically uh steering documents that tell the application what um what it's what's in there. So uh it can more intelligently look at your code and be able to answer

**[4:53](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=293s)** questions and use it together. We also have agent hooks which are kind of analogous to events that are listening in the background. So basically this is a VS code fork. Any VS code fans out there? Yes, I'm a big huge VS Code. So it uses VS Code. So all your extensions work as long as they work with the uh with the open source marketplace that we use. And the hooks themselves, you can put them in the background and they'll listen to certain events. So, one common example is maybe every time you save a component, it'll create a test for you. Now, for the sake of time, I'm not going to go code this for you or do some live coding, but I just want to get you an idea. We also have an ad uh MCP server.

**[5:41](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=341s)** It uses standard IO, so you can connect to a bunch of different MCP servers. For example, Eric was mentioning in the last session that he wanted to create these step functions and then he connected to the AWS MCP server that we have. So, one thing that I've heard before is that our docs aren't always the best. So, using an MCP server to help search the documentation actually makes a lot of sense. Uh, you can also set up with a bunch of the o open source MCP servers out there. I I use context 7 which is really nice one to use. Let's continue on. I'm going to go back to the presentation. Here's what it looks like in practice. Just want to show you real quick. Here's

**[6:29](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=389s)** that agent steering. You click the generate steering docs. It would create those documents. It analyzes your app. It creates this for you. You can add your own steering documents. Like maybe you have a certain way you do TypeScript and things like that. It creates a curo folder and then oops then I click through quickly it creates those steering files as well and then it create you can go through the spec driven development mode which I'll show right here can't really fast forward but it's at the end it'll go through the steering documents that here we'll go I'll show you. So right here on this screen we'll show uh it creates three tabs

**[7:19](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=439s)** there requirements design and task list and so it'll basically go through the feature that you want to create and create all this documentation for you and then it'll help you walk you through implementing the feature. So in the storyteller app I did that beforehand. So we have uh I'll show you kind of what it looks like at the end. Also, I just want to give a shout out to Amazon Cube. That's another Agentic tool that we have. Uh, it doesn't have a wait list. You can download it now. So, it's a command line tool to really quickly get up and running. Uh, get your app up and running. You can ask questions. You it connects to MCP servers. You can have profiles for different people in your organization. Let's say you have a back-end developer. You can set up a profile for them and it'll have the right context so that when you ask it questions, it knows what to do.

**[8:09](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=489s)** And of course uh quick shout out to just using AI responsibly always a great idea because uh you as you are coding you want to make sure that what it's coding is correct. uh you obviously don't want to use low quality images and and as you're learning I use it mostly uh to create tests to create features but I also always double check what it what it outputs and then for this oops cancel that and then for this application that we're going to create today I'm going to deploy it to AWS if you don't know we have a free V2 tier. We just updated it. You can get up to $200 in credits. So, if you are wanting

**[8:57](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=537s)** to to check this out beyond what your company has, maybe your personal accounts, this is a great way to get started. And it one thing nice about this is once you hit that $200 in credits, it stops. It's not going to charge you over that amount. So, we we're creating this storyteller app. Where do we start? We we saw a little demo of Curo. So first we need to kind of understand what I tools we're going to use. So I is infrastructure is code and we want to build this app quickly and we don't want we don't have to we don't want to be like CDK or Terraform experts to do this. So we have a few options. First I really like this idea of just learning is just do click ops. Go through the console click around try to understand

**[9:46](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=586s)** what's everything's in there. This is the AWS console of course. Has anybody used this click ops way of learning in the past? Kind of just clicked around the console and try to generate things. Not a bad way to do it. You can always delete the resources that you create. Another is of course using the AWS CLI. You can uh generate all your resources. You can script this if you need it. I like this to play around with as well. I a lot of container fans I know with ECS EKS uh that's a great way to to orchestrate and and create your applications. One thing I really want to talk about though is infrastructure as code and I really like this with cloud the cloud development kit. So uh this is a you can it's supports a lot of different

**[10:35](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=635s)** languages that TypeScript is typically the one that most is commonly used with CDK. Uh, and you can just write code here and it will generate your backend. So for this storyteller app, uh, I looked at this option. I think it's a great way to do it. But there's one more that I want to talk about and that's amplify gen 2. This is a layer on top of CDK. So you can drop down to your CDK layer if you want, but we added a level uh, several levels of abstraction. So you don't have to necessarily be a CDK expert. Of course, you can use Curo with both of these to help you generate these applications, but I feel like when I want to really quickly get a website up, I want to get a database, I want to have some authorization, Gen 2 is a great way to go. And if I need to extend it and be

**[11:23](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=683s)** more extensible, I can drop down to CDK. So, what should you use who are watching? I'm going to use AWS amplify in this. I think CDK or Amplify are great options. I know there's probably some Terraform fans and SST and others, but I think this is a great way to start. So, what tools do I need for this storyteller app that I'm creating today? Well, there's a JavaScript library, and the one you probably want to use is AWS Amplify. And so, this is a front-end library. We have it working with all your favorite, well, basically works with TypeScript, JavaScript. We also have uh libraries for iOS, Android, net, but this is the one that we um that I recommend for the front end. And that

**[12:10](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=730s)** way you can connect to some of these AWS services like your S3 bucket and and other and your like Cognto things like that. We also have AWS SDK. That's what I use in the back end whenever I need to I'm like on a Lambda function or I'm somewhere in the back end I need to connect to AWS services, I use AWS SDK. And then for UI libraries, I don't know I don't think many people know this. AWS has a set of UI libraries make it easier for front-end developers to get up and running quickly. We have a whole AWS amplify UI react library. Uh but we also have a a Vue Angular as well. And so these have like a set of preset components that you can just with a few lines of code drop into your codebase and start using and they'll connect to services and I'll show you an example of

**[12:59](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=779s)** that. So we call them connected components. So they are components that connect to AWS services. So kind of our most popular one is this authenticator. And so it adds as you can see here like an email password. You can create account sign in. You just with a few lines of code you can drop this in. You can configure this and and you can customize it to make it look like your branding. But it's a great way to just get if you want to get an authentication system up and running quickly, you can use this. It also supports some uh social login federated. It supports uh multiffactor authentication as well. Here is what it would look like in your

**[13:47](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=827s)** React codebase. You would just have this authenticator. You just have this authenticator component that you drop in and then you would just do some configuration on it. Anything between the opening and closing brackets would show when a user is signed in. And you can also customize this. Maybe have a login route and you want to use this would be perfectly uh fine to do. And and this is for view and angular too. We have a storage image component. Uh this is my PM's cat. And so with just a few lines, if you want to have an S3 bucket who has an image in it or another file, you can just use this component into your React codebase and the image will appear and you don't have to worry about coding it all yourself.

**[14:34](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=874s)** And you can also do public private and it it's smart enough to know like obviously if it's a protected bucket or private bucket, it won't let you access it. So how do I build the storytelling app? I'm gonna use Amplify Gen 2 as I was saying and like I said it's really great. It's on top of CDK. It has this new kind of philosophy is that we really went deep into Typescript. We thought let's do when when you're creating an application, let's have TypeScript in the back end. Let's have TypeScript in the front end. Let's make it easy for you to create apps uh to create your your database to connect your authorization to connect to lambda functions. So we have this what

**[15:22](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=922s)** we call like end to end type safety and I'll show you what that looks like and if you're used to something like zod you might be familiar with that. So we have faster once again this theme of like how do we get up and running quickly we have local development. So these we have per sandbox instances uh environments that you can run. So in this example we have NIL, Renee, Joseph and Danny and they all are on a project and they want to test it out. So now they can run a command on their command line and it'll spin up an instance that's ephemeral that they can stop or delete at any time. they can share with other co-workers and it will basically have their whole backend ready to go. And this is all built into this

**[16:12](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=972s)** amplified Gen 2 system. So here uh in my storyteller app I'm going to use AWS AppSync which is our managed GraphQL service. We're going to use Dynamob and Cognto as our off provider. And for those of you are keen those icons are a little bit old. They're newer ones. I didn't get a chance to change it. So the this is what we're going to look at. So I want to create a schema for and this will be how I'm defining my data s my database my my models. And so I'm going to have a customer model. It's going to have a full name and email and I'm going to type type it string. Um I can also put as many models as I want. You can think of this as like fields in your database. And we're going to use apps sync to talk to it. And our library by the way handles all this. And I'll show you how

**[17:00](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1020s)** it works. We can also add authorization groups and maybe only we we only want certain c people to access this customer database. So maybe only people who are logged in or who are public and we only obviously want read access. So we we can do fine grain control of our resources with gen two and that is a little loud but we'll close that door. uh we h the way this works is it would export a schema and the schema then would be available from the front end. So imagine you have an application you have a a folder called amplify and you define your backend resources using infrastructures code as gen two then you can expose this schema to the front end so it understands your backend so you can talk to the data models. So in this case uh we'll come back to that that

**[17:50](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1070s)** schema in a second. This is how you define your O. So this is what your O looks like. This is still defining our backend resources. So we're using Cognto. We're going to have a profile picture is a an actual attribute when a user logs in that they can set. And then we're going to use my favorite one of my favorite my I like Nex.js and Nux.js. We're going to use Next in this instance. And so we're going to use Gen 2 to talk to the table that we just created. We're going to import that schema in from that back end. Then we're going to use our U state. Now we'll have IntelliSense. So, we're going to have autocomp completion now, and we can easily talk to any of the models that we created. Do all those create, read, update, delete that we all

**[18:38](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1118s)** know and love. It's just really quick to get up and running. Here's a quick video of how this is in practice. On the on your guys' right hand side is the back end. So, we're defining on our back end uh a schema for a to-do. And then on the on your left hand side we are in real time as we are creating the schema the VS code on the lefth hand side already knows or in this case hero would already know the attributes that you added. So I'm adding a priority and now I have that nice auto completion high low medium. So you can see imagine you can be creating your backend front end basically virtually at the same time and you know that they're going to be type- safe because of the way the schema is going

**[19:26](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1166s)** to be talking to both of them. Uh your your schema is always going to be updated and the front end will never get out of sync from the back end. So of course you've heard a lot about agents and bedrock today already but how how do we do this? Well CDK is great. We can code our infrastructure, create our lambdas. Gen 2 does have something called amplify AI kit. So we released this as a a lightweight option on top of amplify to talk to foundational models and use something like tool use and converse APIs. So it kind of looks like this. We have a couple of them. We can do like adding a chat window. This would be adding this conversation. This is uh this would be a file inside your front end that would define this interface. It

**[20:15](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1215s)** says use cloud 3.5 sonnet your helpful assistant and then you can have different tools and the tools can either access your app sync like tables or they can actually access their own custom lambda functions and then that data would be turn returned back to the model so it can more intelligently answer whatever question or whatever thing you're trying to do. In our case, we are trying to do a storytelling app. So, I'll show you what that looks like. And of course, if you use anything, you don't have to use anything I'm showing you today. You can use this by itself. It's called Amplify Hosting. Uh, a lot of people don't even know that AWS has its own managed hosting service for your websites. But we do, uh, it's called Amplify Hosting. It supports all the major frameworks and, uh, SSR, SSG, uh, static sites, anything you really want.

**[21:05](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1265s)** It does really well and we're constantly updating that. Kind of looks like this. You can connect it to your version control system. So, I have a few minutes left. So, I thought I would show what it looks like. My storytelling app. Well, first this is what the app looks like. Okay. And so I have this app here. It's uh Curo is running it. And if I look at I have this amplify folder. It might be kind of small. Can you see it? I have this amplify folder on the lefth hand side. And I have this data. And this is where I defined by the way I just can

**[21:54](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1314s)** close this window. This is where I'm defining the schema for my my conversation API which I'm going to talk to Amazon Bedrock. I'm using clot 3 sonnet. I have a system prompt the storytelling finder and then I set a bunch of tools. So list stories get news. I use a knowledge uh a knowledge base too to kind of show you you can use a whole bunch of AWS services with this. You can change it up. So I can try it out. All right. So, here's my app. So, now I can give it I can give it a prompt and then it should uh generate a story for me. So, let's try it out. Anybody have like a favorite animal? And

**[22:45](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1365s)** don't say duck bill platypus cuz everybody says that. What's a like an an animal that like a cow? And what else? What? Tell Give me an animal. >> Okay. Penguin. How about a blue pen? [Music] Okay. So now what it's doing, it's using this tool. I have right down here. I have a generate story. It generates a story and title that's funny and exciting. This obviously this prompt is very simple. You can have it much more advanced. And then it's using a generate image which is using a lambda function that I called generate image.

**[23:34](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1414s)** And it's using stable diffusion. And so this is just some very basic code to create stable diffusion. It just passes that prompt in there. Hey, there he is. So the penguin enchanted crystal. So then it goes through it generates this story. It actually saves it into the Dynamo DB database. So I can retrieve it uh with it. So after this looks good, I can switch to chat mode. And then I can just this is also a part of the AI kit that I was showing you. This is a component that I just dragged and dropped onto my React application and it creates this chat window and then I can put whatever I want here and it's connected. So, so now I'm just asking it to find and I

**[24:25](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1465s)** also have a a knowledge base here. So, I could have loaded like a bunch of customer like a bunch of thousands of stories and had to look through that as well. So, now it's looking through the story helper. So, I did find the penguin's enchanted crystal and then it gives me more information about it. And I could probably even, if I'm more specific, I can have it retrieve it. Now, I'm sure some of you are getting hungry because we have lunch coming up next. [Music] What's that? Oh, one more session. Well, you you'll have to wait one more session. Uh, one last thing. So then you can have cards inside here

**[25:14](https://www.youtube.com/watch?v=fto4t3Vl7dE&t=1514s)** too is what I'm showing. All right, I think my time is up. I'll be here. Thank you so much.
