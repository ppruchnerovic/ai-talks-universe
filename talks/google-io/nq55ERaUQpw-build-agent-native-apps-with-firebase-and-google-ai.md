---
id: nq55ERaUQpw
title: "Build agent-native apps with Firebase and Google AI"
slug: build-agent-native-apps-with-firebase-and-google-ai
conference: google-io
conference_name: "Google I/O"
category: "Vendor & platform"
edition: "I/O 2026"
year: 2026
speakers: ["Kara Yu", "Sam Phillips"]
channel: "Firebase"
duration_min: 11
published_at: 2026-05-21T19:00:24Z
video_id: nq55ERaUQpw
url: https://www.youtube.com/watch?v=nq55ERaUQpw
youtube_url: https://www.youtube.com/watch?v=nq55ERaUQpw
tags: ["pr_pr: Google I/O;", "ct:Event - Technical Session;", "ct:Stack - Cloud;", "Agent-Native", "Google Antigravity Tutorial", "Firebase for AI Agents", "production-ready AI apps", "Google AI Studio", "App Development 2026"]
transcript: true
---

# Build agent-native apps with Firebase and Google AI

**Kara Yu, Sam Phillips**

`Google I/O` · `I/O 2026` · `2026` · `11 min`

`#pr_pr: Google I/O;` `#ct:Event - Technical Session;` `#ct:Stack - Cloud;` `#Agent-Native` `#Google Antigravity Tutorial` `#Firebase for AI Agents` `#production-ready AI apps` `#Google AI Studio` `#App Development 2026`

[Watch the recording](https://www.youtube.com/watch?v=nq55ERaUQpw) · [Conference site](https://io.google/)

## Description

Transform prototypes into production-ready apps with agent-native development, leveraging deep integrations with Firebase, Google AI Studio, and Google Antigravity. Learn how Firebase empowers coding agents to handle the toughest parts of building a robust backend, including provisioning databases, implementing user authentication, managing security, and deploying apps without manual configuration.

Resources:
AI Studio apps gallery: where you can take a sample app and remix it to make it your own → https://goo.gle/4d8217M

Firebase Agent Skills: where you can install on an IDE of choice → https://goo.gle/42gVK4W

Watch the Firebase sessions from Google I/O 2026 → https://goo.gle/Firebase-at-IO26
Watch the cloud sessions from Google I/O 2026 → https://goo.gle/Cloud-at-IO2026

#GoogleIO

Speakers: Kara Yu, Sam Phillips
Event: Google I/O 2026
Products Mentioned: Firebase, Cloud, AI/Machine Learning

## Transcript

*1,721 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=nq55ERaUQpw&t=0s)** [MUSIC PLAYING] KARA YU: Hi, I'm Kara, and today I'm going to show you how Firebase and Google AI Studio can help you bring any app idea to life. SAM PHILLIPS: And I'm Sam, I'll be helping to drive along too. KARA YU: First, before we jump into the demo, let's recap what Firebase is. Firebase is Google's suite of services for app development. We help mobile and web developers build, launch, and grow their apps. With Firebase, you can accelerate your app development using AI. And once launched, you can improve app quality, with testing and monitoring. And finally, you can drive user engagement, with analytics and messaging tools.

**[0:48](https://www.youtube.com/watch?v=nq55ERaUQpw&t=48s)** Firebase currently has millions of active developers. Firebase makes it easy to build apps. Our secure client SDKs allow you to build your apps on web and mobile platforms, while sharing the same backend in the Cloud. You can build your app logic, just once, from the client. Using Firebase Auth, you can easily implement user sign in and manage user access to your backends and features like real-time and offline come out of a box. That's not all. You don't need to worry about scaling. Firebase is serverless and backed by Google Cloud. The app will scale with your users, without you needing to lift a finger. Finally, with AI capabilities as a core part of our services,

**[1:39](https://www.youtube.com/watch?v=nq55ERaUQpw&t=99s)** Firebase makes it easy to integrate Gemini app API calls in your app, store embeddings in your database, and much more. That's not all. I'm super excited to announce that Firestore now supports full text search. We have a new search API, which allows you to query documents for arbitrary data, including strings. Search queries return documents along with a search score, so you can documents by relevance. We've also added some fancy knobs to the API that lets you control retrieval, depth, sort order, and inclusion of synonyms. [MUSIC PLAYING] SAM PHILLIPS: Those are great improvements to Firestore, and we're making them available in Google AI Studio too. Google AI Studio is Google's fastest path

**[2:27](https://www.youtube.com/watch?v=nq55ERaUQpw&t=147s)** from prompt to production. AI Studio is a vibe coding solution, which helps you build and deploy apps, using Google's latest Gemini models. AI Studio helps prompt Gemini with intelligent context management and coding best practices, so you can use natural language to build apps. [MUSIC PLAYING] KARA YU: Building an app using AI Studio is great, but what happens when you want to store data or let your users log in and have their own accounts? That's why we've integrated Firebase into AI Studio. If needed, AI Studio can set up Firestore and Firebase Authentication to turn your prototype into a real app that's ready for users. Hey, Sam, so I've been kind of stressed, actually. We've been building out this talk,

**[3:14](https://www.youtube.com/watch?v=nq55ERaUQpw&t=194s)** and there's so many things to do. I can't figure out if we're behind. Not to mention, I want to make sure we remember to celebrate our milestones. Could we build something to help? SAM PHILLIPS: Hey, Kara. Yes, let's build an app. What I love about these new AI tools is that they make building apps much more approachable. It opens up possibilities that seem too heavyweight or complex before. Kara and I have worked together on a ton of projects at Firebase, over the years. And we've tracked progress in all sorts of ways-- using plans and documents, plans and spreadsheets, plans and bugs and comments. One time, we tracked a project using a plan that I wrote on a receipt. But my personal favorite is the Kanban board. I love moving cards from idea to in-progress and in-progress to done.

**[4:02](https://www.youtube.com/watch?v=nq55ERaUQpw&t=242s)** What if we made our own tracker just for this talk? Here I am in Google AI Studio. And I've got an input box here, where I can put in my idea and let Gemini do the rest. Let's put it to the test. I've got my prompt pre-written here. I'll put it in and read it out, as the model gets going. "Let's build out a team planning app to plan projects. Make it Kanban style. Let the users create projects, and then, within the projects, let them create tasks and move them from a backlog in progress and done. When all the tasks on a project are done, have a fun celebration. Start simple for now, with no extra integrations." When I click Build, Gemini will get to work. AI Studio brings us into the development environment, where Gemini is interpreting those product requirements

**[4:51](https://www.youtube.com/watch?v=nq55ERaUQpw&t=291s)** and building out an app. In the chat, here, I can see a view of what changes are being made, including a view into its thinking progress and the pre-work it needs to do. Next, it installs the necessary packages and gives the app a name. I love looking at these little drill downs, where I can see how he's thinking through the problem, considering the features that it needs, and building out the core functionality. As it does this, I can see the code starting to appear, like creating task and project types as the core data structures. Once more of the code gets built, I can switch over to Preview mode to see the application live. And just like that, I've got my new team project tracker. Let's try it out and see how it works. I'll create a new project called Test out the new project tracker.

**[5:40](https://www.youtube.com/watch?v=nq55ERaUQpw&t=340s)** Now I can create a task, like Try it out. And there it is in the backlog column. I can move it from the backlog to In Progress. And I'll widen this to see all the rows together. And then move it from In Progress to Done. And cool, I got a fun celebration. The project tracker seems to work pretty well, but right now, it's strictly single player. What if I want to share this with my team? With Firestore and Firebase Authentication, we can add a backing database and authentication flow so that folks on my team can log in with their own accounts and share the exact same view of the project. Let's try that now, by prompting add Firestore to this project and store the progress in a database. AI Studio recognizes this request

**[6:28](https://www.youtube.com/watch?v=nq55ERaUQpw&t=388s)** and presents a special UI dialog for this exact case. It details how it's going to store the data using Firestore, and then starts the Firebase setup process. Under the hood, it's doing a few different things to get this working. It creates a Firebase project, if needed, provisions Firestore, and enables Firebase Authentication with Google sign in. Then it takes all of that configuration and automatically adds it to the applet. As it goes through the process, you can see the new files getting created in the code view. One of the key things it does is generates a Firebase blueprint file. This blueprint records the structure of the application, tracking the schemas and data structures the applet is using. AI Studio also automatically generates security rules and deploys them to the database.

**[7:16](https://www.youtube.com/watch?v=nq55ERaUQpw&t=436s)** Once the database is configured, it wires up the authentication, so that each user can log in and get their own personalized view of the applet. It looks like the generation is done. Let's try it out. I'll create a new project, Try out version2 and then create a task, Send it to Kara. Let's see if this worked. I'm going to press the Share button and share this applet with Kara. KARA YU: Thanks, Sam. Let me try this on my phone. OK, I'm signing in. Let me switch into the project called Try out version2 that Sam was on. Now I see the Send to Kara card. Let's click Start task and move it to In Progress. And now, let's mark it complete.

**[8:07](https://www.youtube.com/watch?v=nq55ERaUQpw&t=487s)** There it is. It's so easy to track how we're progressing on our project. SAM PHILLIPS: And awesome. Your change shows up on my screen too. In just minutes, we've used AI Studio to build an app with a database and login, allowing the whole team to share state. We're so excited about what you're going to build using AI Studio and Firebase together. And we'd love to see what's next. [MUSIC PLAYING] KARA YU: With a single click of a button, our app got supercharged with Firestore, Firebase Auth, and Firebase security rules. These products have been around for almost a decade and are backed by the scale and reliability of Google Cloud. Using this Firebase integration means that your prototype can evolve into a full-fledged app without the need to re-architect anything.

**[8:56](https://www.youtube.com/watch?v=nq55ERaUQpw&t=536s)** Now, did you notice that when I clicked Done, Sam saw it immediately? Real-time sync and offline functionality are included by default. So your vibed app can feel just as snappy and responsive as what you're used to, making it a great experience for your end users. All right, Sam, I think we're ready for prime time. SAM PHILLIPS: I agree. Using AI Studio, you can refine and iterate on your app, by prompting and chatting within AI Studio. But in this case, I think we're feature complete. Let's publish this. You can deploy to Cloud Run from directly within AI Studio. I'm clicking the Publish button. And boom! There you have it. It's been published to the web. AI Studio has a whole gallery of applets like this that you can remix to make your own. Or you can start from just a prompt.

**[9:45](https://www.youtube.com/watch?v=nq55ERaUQpw&t=585s)** Check them out at aistudio.google.com/apps today. The URL is available in the video description below. [MUSIC PLAYING] KARA YU: As Firebase, regardless of where you write or create your code, we want to meet you there. This integration with AI Studio showed how easy it is to create a fully functional, full stack application with a cloud database and authentication system. If you prefer to work in a local environment with an IDE like Google Antigravity, Cursor, or Cloud Code, we also have Firebase skills available for you to achieve everything we just went through as well. Check the description below to learn more about Firebase skills and how to install it in your IDE of choice. Thanks for watching and let us know

**[10:33](https://www.youtube.com/watch?v=nq55ERaUQpw&t=633s)** in the comments what apps you're building with AI Studio and Firebase. [MUSIC PLAYING]
