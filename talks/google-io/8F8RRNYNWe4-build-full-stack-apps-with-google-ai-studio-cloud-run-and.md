---
id: 8F8RRNYNWe4
title: "Build full-stack apps with Google AI Studio, Cloud Run, and Cloud SQL"
slug: build-full-stack-apps-with-google-ai-studio-cloud-run-and
conference: google-io
conference_name: "Google I/O"
category: "Vendor & platform"
edition: "I/O 2026"
year: 2026
speakers: ["Shambhu Hegde", "Justin Mahood", "Sara Ford"]
channel: "Google Cloud Tech"
duration_min: 9
published_at: 2026-05-21T22:02:10Z
video_id: 8F8RRNYNWe4
url: https://www.youtube.com/watch?v=8F8RRNYNWe4
youtube_url: https://www.youtube.com/watch?v=8F8RRNYNWe4
tags: ["pr_pr: Google I/O;", "ct:Event - Workshop;", "ct:Stack - Cloud;", "Vibe Coding with Google AI Studio", "No-code full stack app development", "Cloud SQL for AI Applications", "database management for no-code apps"]
topics: ["Data engineering & MLOps"]
transcript: true
---

# Build full-stack apps with Google AI Studio, Cloud Run, and Cloud SQL

**Shambhu Hegde, Justin Mahood, Sara Ford**

`Google I/O` · `I/O 2026` · `2026` · `9 min`

`#pr_pr: Google I/O;` `#ct:Event - Workshop;` `#ct:Stack - Cloud;` `#Vibe Coding with Google AI Studio` `#No-code full stack app development` `#Cloud SQL for AI Applications` `#database management for no-code apps`

[Watch the recording](https://www.youtube.com/watch?v=8F8RRNYNWe4) · [Conference site](https://io.google/)

## Description

Turn ideas into live apps in minutes, without the need for coding. Build and launch full-stack apps with Google AI Studio powered by Cloud SQL for storing data and Cloud Run for deploying the app.

Watch the cloud sessions from Google I/O 2026 → https://goo.gle/Cloud-at-IO2026

#GoogleIO

Speakers: Shambhu Hegde, Justin Mahood, Sara Ford
Event: Google I/O 2026
Products Mentioned: AI/Machine Learning, Cloud

## Transcript

*1,449 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=0s)** [MUSIC PLAYING] JUSTIN MAHOOD: Hello, and welcome to this session. build and deploy full-stack apps with Google AI Studio, Cloud Run, and Cloud SQL. I'm Justin Mahood, a Group Product Manager for Cloud Run. And today, I'll be joined by my teammates Sara Ford and Shambhu Hegde. Last year, we enabled the deployment of vibe-coded applications from AI Studio to Google Cloud. But those were AI-powered front-end applications only, with no back-end servers and no databases. Deploying a full-stack application in a traditional fashion may involve some friction. So for example, deploying a full-stack app typically involves setting up a GCP project, installing command line tools, and adding a credit card. But today, we are excited to introduce frictionless, full-stack deployments for non-traditional Google Cloud

**[0:50](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=50s)** customers. That means deploying applications that include a front end, a back end, and a database to Google Cloud. But beyond just adding capabilities, we've decided to offer a bundle of these Cloud Services for customers who are not traditional GCP customers. So today, we're announcing that all you need is a Gmail account to vibe and publish to your own URL a given number of full stack web applications. No Google Cloud experience or Google Cloud project is needed. No G Cloud installation and no credit card or billing account is required to get started. You can use either Firestore or Cloud SQL for your database. And you'll also get end-user authentication. Just publish, and your app is hosted on Cloud Run and ready to scale.

**[1:39](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=99s)** Now, to talk more about the developer experience-- or better yet, the vibe coder experience-- I'm going to turn it over to my teammate Sara. [MUSIC PLAYING] SARA FORD: Hi. I'm Sara Ford, a Developer Relations Engineer on the Cloud Run team. Let's talk about some of the tools and resources you'll need to run your apps. You can build multiple apps and deploy without any time limits for however long these apps are available. You'll have logs and metrics directly from your deployed applications. A Cloud SQL database gets created in seconds to power your application. You'll have access to environment variables to make quick modifications without rebuilding. And lastly, you'll be able to pause, resume, or delete your applications.

**[2:28](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=148s)** Now let's talk about what comes next. For example, you share your website. Now your friends, family, social media followers start using it. You can also publish your apps to make it available broadly. If your app starts doing well, and you want to productionize it, there's a one-click option to onboard to a regular Google Cloud account, where you can add your credit card, provide payment, and then use the full flexibility and power of Google Cloud with full set of features. I'll turn it over to Shambhu, a PM on the Cloud SQL Team, who will show you AI Studio in action by creating an app at no monetary cost and deploying an app to Cloud Run using Cloud SQL as a database.

**[3:17](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=197s)** [MUSIC PLAYING] SHAMBHU HEGDE: Hi, everyone. I'm very excited to show you how to go from a simple idea to a fully published app using Google AI Studio. Today, we are going to build an app powered by a Cloud SQL for PostgreSQL database. This app will be hosted on Cloud Run. Here is the best part. This all happens behind the scenes. We don't need to write a single line of code. Instead, we are going to vibe code it. With just a few conversational prompts and a couple of clicks, you will see an app come to life that you can immediately share and publish. Let's dive in. Welcome to Google AI Studio's build mode. This is our canvas to start building the app. Let's say I want to build a neighborhood tool library to make it easy for my neighbors and me

**[4:05](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=245s)** to share everyday items like ladders, drills, and cameras. I'll start by giving the agent my vision. I just need to enter a prompt, "Build an app for a neighborhood tool library." The app should allow people in the neighborhood to list tools to lend or borrow. Create a basic home page that lists all the available tools. Right away, the AI Studio agent gets to work. It knows that, to build an app, it needs to parse this data, so it selects Google Cloud SQL. We instantly get a Cloud SQL database provisioned and ready to go. The AI Studio agent creates the initial database schema and sets up the tables for us. Using Cloud SQL helps in implementing many useful features such as logins, profiles, smart search, and other helpful things, as we will see later in this demo.

**[4:56](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=296s)** Now you can see that the preview of the app is loaded on the right side of the screen. Now let's add sample data to this app. I'm just entering the prompt, "Generate sample data for this app, and insert it into the database." Just like that, our app is populated. If you have your own data, you can also just upload a file or share a Google Drive link, and the agent handles all the data loading-- NoSQL queries required. Next, let's make it easy for users to securely manage their own tools. I'm entering the prompt, "Set up email-based authentication so users can log in." The agent instantly builds out the login flow and handles all the necessary database filtering to ensure data privacy between users. It also updates the Cloud SQL database schema

**[5:44](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=344s)** to create a users table and make other changes to implement end-user authentication. Now I am logging into this application. Now let's watch how easy it is to iterate. I want to add an actual borrowing mechanism. So I'm going to just add a prompt. "Add a borrow button to each tool card." When clicked, it should link the current user to the tool and update the tool status to borrowed. Then create a My Garage page that shows tools that the user owns and the tools they are currently borrowing. Once I enter this prompt, the agent updates the database schema, updates the app logic, and pushes the UI changes to the app. Now you can see the borrow button in the app preview. Once I click on the borrow, the tool gets linked to my profile in the database.

**[6:33](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=393s)** Now let me go to the My Garage page to confirm it. You can see that all the three tools that I borrowed are linked to my profile because these records are updated in the Cloud SQL database. Now let me try listing a tool that I have. I'm adding a can opener. Once I add it and add all the details, this tool gets stored in the database, and now it is visible in the app. As the tool library grows, users will need to find things quickly. So let's add a smart search feature. I'm entering the prompt, "Update the search bar to make it smart." Users should be able to search even when keywords don't exactly match. To make this work seamlessly, the agent uses database features, including advanced features such as PostgreSQL extensions to power

**[7:22](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=442s)** the search. For example, if a search is implemented to enable the search based on approximate matching of keywords, a semantic search is also implemented to enable natural language searches based on the intent. Let's see it in action. I am now searching by making intentional spelling mistakes in the keyword. You can see that the relevant result "power drill" is shown even if there was a spelling mistake in what I searched for. Now I am adding a natural language question in the search, "Is there a tool to open the can?" You can see that a relevant result, a can opener, is shown in the result. We could easily build these smart search features on the data, as this app is powered by the Cloud SQL database.

**[8:09](https://www.youtube.com/watch?v=8F8RRNYNWe4&t=489s)** And we are done. Our app looks amazing, it's fast, and it works well. Now, with just one click, I can publish this directly to Cloud Run. I can also share this app with my friends, family, neighbors to try it out. And if I want to add new features tomorrow, I can jump right back into AI Studio and keep iterating. That is how quickly you can go from an idea to a live, database-powered app. Now it's your turn to try it out. Thank you. [MUSIC PLAYING] SARA FORD: Thank you, Shambhu, for the demo. We invite you to get started with your coding journey today by visiting AI Studio. Thank you for watching our session. [MUSIC PLAYING]
