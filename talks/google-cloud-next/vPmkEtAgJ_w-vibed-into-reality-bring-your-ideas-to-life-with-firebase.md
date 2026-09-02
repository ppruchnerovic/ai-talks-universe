---
id: vPmkEtAgJ_w
title: "Vibed into reality: Bring your ideas to life with Firebase and Google AI"
slug: vibed-into-reality-bring-your-ideas-to-life-with-firebase
conference: google-cloud-next
conference_name: "Google Cloud Next"
category: "Vendor & platform"
edition: "Next 2026"
year: 2026
speakers: ["Kara Yu", "Sam Phillips"]
channel: "Google Cloud Tech"
duration_min: 20
published_at: 2026-06-25T16:27:48Z
video_id: vPmkEtAgJ_w
url: https://www.youtube.com/watch?v=vPmkEtAgJ_w
youtube_url: https://www.youtube.com/watch?v=vPmkEtAgJ_w
tags: []
transcript: true
---

# Vibed into reality: Bring your ideas to life with Firebase and Google AI

**Kara Yu, Sam Phillips**

`Google Cloud Next` · `Next 2026` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=vPmkEtAgJ_w) · [Conference site](https://cloud.withgoogle.com/next/)

## Description

As we enter the era of agent-native development, Firebase provides deep integrations with Google AI Studio to transform your vibed prototypes into feature-rich, production-ready apps. Join this session to learn how Firebase empowers coding agents to handle the toughest parts of building a robust backend, including provisioning databases, implementing user authentication, managing security, and even deploying apps – all without the need for manual configuration.

Speakers: Kara Yu, Sam Phillips

BRK2-081
#GoogleCloudNext

## Transcript

*2,608 words · source: supa (en, exact timings)*

**[0:13](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=13s)** Thank you so much, everyone, for making it bright and early on day two of Cloud Next. I'm so impressed you're here, so we have a lot of pressure on us to make this a fun talk and worth getting up this morning. My name is Kara, I'm a group product manager on Firebase. And I'm going to show you how Firebase and AI Studio help brings you bring you yeah help you bring any app idea to life and I'm Sam I'm going to be helping to. First before we jump into the demo, let's recap what Firebase is. Firebase is Google Cloud's suite of services for app development. We help mobile and web developers build, launch and grow their apps.

**[1:02](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=62s)** With Firebase, you can accelerate your app development using AI, allowing you to go from concept to production with fully managed back end infrastructure. Once launch, you can improve app quality with our suite of testing monitoring tools. And finally, you can drive user engagement with analytics and messaging products. Firebase currently has millions of developers. Developers have always loved building with Firebase, and that's for three reasons. First, Firebase makes it easy to build apps. We offer a full backend as a service platform with all the components you need to build an app with database, storage security all integrated together. Our secure client SDKs allow you to build your apps

**[1:53](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=113s)** on web and mobile platforms, while sharing the same backend in the Cloud. You can build your app logic just once from the client using Firebase Auth. You can easily implement user sign in and manage user access to your backends. Want your app to work. When your users step into a Vegas elevator or get the latest scores on the game. Our SDKs include features like offline and real time out of the box. You also don't need to worry about scaling. Firebase is backed by Google Cloud. The app will scale with your users automatically without needing you to worry about infrastructure. Instance sizes or upgrades. And finally, with AI capabilities as a core part of our services, Firebase

**[2:42](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=162s)** makes it easy to integrate Gemini app API calls into your App Store, embeddings in your database, and much more. An AI Studio. I want to talk to you about AI Studio. AI Studio is Google's fastest path from prompt to production. AI Studio helps prompt Gemini with the intelligence, context and instructions for coding to help you build an app idea using natural language. So now. So building an app using AI Studio is great, but what if you want users to be able to log into the app and share data across sessions. That's why we integrated Firebase into AI Studio if needed.

**[3:29](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=209s)** AI Studio can set up Firebase and Firebase Firestore and Firebase authentication to turn your prototype into a real app that you can that's ready for users. Now for the exciting part. Let's try a demo of this live. I'm going to switch to the AI Studio on my computer now. All right. Here I am at AI Studio, where I have this prompt. Prompt box where I can describe my app idea and let Gemini do the rest. So I can type in the idea that I have.

**[4:19](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=259s)** In this case, let's do something a little meta. Let's build a tracker for this talk. So I've pre-written my prompt here. Let me put it in and read it out. Create a simple Kanban board to track a talk with AnchoredDraggable cards let users create projects and have three columns for backlog in progress and done. Start simple. No integrations. This is something that I've been telling Cara. We really need to do track all the things that we need to do for this talk. What I really love about these new AI tools is that they make it so easy to build apps that the barrier from having an idea to having an app is lower. So instead of just saying let's have an idea. Now let's have an app in AI Studio, I could choose other options.

**[5:08](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=308s)** So if I go up to the gear on the side, I could select different models or different frameworks. But these standards seem good for me. Now, when I click build, Gemini app will get to work. So it brings me into this environment where I can see a few different things are happening. So over here, the agent is considering the requirements that I've given it and starting out the process, I can Zoom in and look at its thinking process and see the process, the steps that it's going to. As it thinks about it, as it begins to understand the requirements. If I look in the code panel, it's going to start building out the code that's needed for this application. Here it started with some types and I can see the others flying in as it's working.

**[5:59](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=359s)** In the Preview tab, I see the application as it's coming. A new feature that AI Studio just added are these design previews. So as it's working, I could think about what sort of styling and themes I would like for this app. Now, in this case, I'm probably going to choose a dark theme because developers love dark DevTools. And this is going to take just a moment to build. But I had already built one a little bit earlier, so I'm going to switch to that and show you this dark mode Kanban board for tracking a talk that I made earlier. And you can see what it's done is build out the entire application. And I can look and see now that it's created,

**[6:49](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=409s)** a standard React app with TSX, package.json. If you're familiar with code, these concepts will all be very standard for a normal React app. And I can see the live app here popped up. So let's give it a try. Make sure that it's working. So if I choose a topic, what's the core message of this talk. Well, it's Firebase with AI Studio. So that see if it works. All right. So it moves and drafts the slides. Looks like this is working for me. A feature that AI Studio has is easily being able to share your ideas with others so that they can make them their own and keep adding on.

**[7:38](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=458s)** So I can go up here and share and share this with Kara, and I've already done that. So let me switch to your tab, Kara. And here you go. Oh cool. I got a ping from Sam. Let's see what it is. This is from another developer because he built this. Wow, this is cool. This is exactly what we needed to prep the stock. I'm glad we're doing it. So, ahead of the talk in this agentic era, it sounds like we're. We're making the talk as we give it, but actually. OK, so let's add a thing.

**[8:26](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=506s)** All right. Any ideas from the audience on what we need to do this talk to the data. How many database behind it. Oh store the data. Oh, that's a great question. So the question was, how do you store the data. So far, we just saw React App Store the data store to store the items rooms in the Kanban in a database. All right. So let's put that into drafting and Slides. So actually that was exactly what I was about to demo. This is a multiplayer multi-user thing. We're obviously working together in this.

**[9:14](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=554s)** And I want to make it not just data storage but also have user profiles. So I'm adding certain things. Sam is adding other things. And we want to have this in perpetuity, obviously, because this Kanban is so helpful we're going to use it again. What's really cool about AI Studio is that you have the ability to remix any app that you have access to. What that means is that you can take an app and make it your own, and then add additional features. So let's do exactly that. In order to add data, it tells me what I'll name it and it starts basically creating everything and making it mine. What's cool about this is if I have data or auth set up, it will set it up in my own GCP project so I have access to it.

**[10:06](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=606s)** And if I wait a second. You'll see that it's porting over all the files that Sam just had. And here it is. This is my remix version of his talk. And from here what I can do is simply prompt the agent to add Firebase and auth to make this multiplayer. Now note that you don't actually have to explicitly say Firebase. You can say I want to have a database, or if you say anything where the agent deems it likely that a database would make it better, a GCP project Firestore and auth will be set up for you. You'll notice this lovely card comes up.

**[10:53](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=653s)** It says enable database. Click Enable to continue with Firebase. Data is saved over time. There is a free. There's a very generous free tier for both Firestore and Firebase Auth. And then you can select a location to host your app. US West two looks good to me. And I click Enable. And so behind the scenes, it's actually doing a ton of work. It by clicking enable there I have accepted the terms of service for both GCP and Firebase. So it's marking that as accepted. It's creating the GCP project in under my account. And it's creating a instance of Firestore Enterprise as well as setting up Firebase Auth with Google sign in. Now, this will take a minute.

**[11:41](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=701s)** It's working through defining Firebase structure I'm going to switch over to one that we did just earlier. Cool So immediately you'll notice that you have this sign in with Google. Available here. So if I click Sign In. Wow I did Google sign in with just a click. That's huge. It's so easy to get security implemented here. So let's add some additional ideas. Oops we should write a script probably. Maybe practice our talk.

**[12:34](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=754s)** If I go into the code section. I can go through the Firebase file. And it did all these steps for me. It initialized an app. It set it created an auth. It set up Sybase auth using Google auth provider, hence Google sign in and it created Firestore. So the agent actually didn't just provision all of this, but it actually wrote code against all of this as well. So it ensured that everything I do now gets written against Firestore. You'll see there's configs here. These are API keys that can be in the client. And how we do our client side access.

**[13:24](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=804s)** And the security model for that is via something called Firestore rules. It's basically a language that allows you to say based on your Firebase Auth what access your users have to the database. And then finally, we have this Firebase blueprint which is essentially the structure of the app. So you have card entities with all these different properties that we just updated. And then your Firestore database kind of has this structure of collection card collections with a card. All right. I think this is pretty good. Let's share it back to Sam to show him how cool it is. All right.

**[14:15](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=855s)** Let me switch over here. So Cara went up earlier and shared this version back with me using the Share button. And here it is on my account. And so let's see if this works. Let's see if it's now a multi-user multiplayer Kanban app. So I'm going to sign in here and boom. Now I see the cards that Kara had created earlier. And let's see if I can move them around. So move right to script into drafting practice talk. Oh, let's say that's ready now. And maybe I'll make a new one. That's test out. Test out, shared apps. So if I switch tabs over here to go to the Firebase Console

**[15:07](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=907s)** here I am in the database section of the Firebase Console. Folks might have seen this before. If you've used Firestore, we have a document editor viewer inside of the Console where you can see the contents and change the contents of the database. And I can see here that these cards that I've been creating are getting created and updated as we build out this. So this is a real live database with login tracking the talk. And I think this is working really well. Is there anything else that we need to do. May be that you need your phone for.

**[16:00](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=960s)** Wow, that's a really great call. I just remembered we need to do a thing, but I actually remember literally just now, see. I think. Oh, so you just created a new idea. I did. I wonder what the idea is. Take a selfie with the audience. And so you can see not only is the database set up, but with real time sync, as soon as car is changing it, it's showing up in my instance of the application as well. So this is a sort of a reactive live application

**[16:51](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=1011s)** that really feels like something that we could go do. And should we do it. Kara, do we have everyone's consent to do this. Yes All right. Amazing so we'll go back to the slides now. Funny because I literally did forget. You can see that with just one click of a button. We added Firestore Firebase Auth and security rules. You saw probably that the cards had my name on them when I made them. Sam's name when he made them.

**[17:37](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=1057s)** And you saw me update things in real time. So all of that happened with a single click because with a single click. And you can have all the power of Google Cloud behind you. Now, I think a really cool part was as I updated things on my phone and by the way, I was quite slow in typing it immediately did show up on Sam's app. Real time sync offline are completely included out of the box. Did we write a single line of code just now. No, because all of these things are functionality that Firestore has and that's at all. I'm super excited to announce that Firestore now supports full text search.

**[18:26](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=1106s)** So we have a new Search API that allows you to query documents for arbitrary data, including strings and search queries. Return documents along with a search score. So you can documents by relevance. And query support is also included. As Firebase. We want to be everywhere. You're making applications. So if you prefer a local environment with a fully fledged Ide like Cursor or Cloud Code, we also have Firebase skills available for you to achieve everything we just did. Check out Firebase's GitHub repo to learn more about Firebase skills and how to install it in your Ide of choice. Now I have one more favor to ask,

**[19:15](https://www.youtube.com/watch?v=vPmkEtAgJ_w&t=1155s)** but there's a reward with this favor, which is please help us by giving us feedback around our talk and around our products. Tell us how AI assisted development is changing your work from building to governance. I'm told there is swag involved here if you so choose to help us. I'll leave this up so people can scan it. Yeah thank you.
