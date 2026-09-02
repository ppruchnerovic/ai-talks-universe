---
id: NXodiipqNco
title: "Build agentic testing systems to validate AI generated code | ODSP912"
slug: build-agentic-testing-systems-to-validate-ai-generated-code
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 13
published_at: 2026-06-04T11:24:17Z
video_id: NXodiipqNco
url: https://www.youtube.com/watch?v=NXodiipqNco
youtube_url: https://www.youtube.com/watch?v=NXodiipqNco
tags: ["AI", "Agent Observability", "Agentic Security", "Agents", "Automation", "Build agentic testing systems to validate AI generated code | ODSP912", "Deployment Pipelines", "DevTools", "Developer", "Developer Technologies", "Monitor", "ODSP912", "ODSP912_v1", "Reliability", "Resiliency", "Scaling", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Build agentic testing systems to validate AI generated code | ODSP912

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `13 min`

`#AI` `#Agent Observability` `#Agentic Security` `#Agents` `#Automation` `#Build agentic testing systems to validate AI generated code | ODSP912` `#Deployment Pipelines` `#DevTools` `#Developer` `#Developer Technologies` `#Monitor` `#ODSP912` `#ODSP912_v1` `#Reliability` `#Resiliency` `#Scaling` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=NXodiipqNco) · [Conference site](https://build.microsoft.com/)

## Description

AI is driving rapid expansion of software, but vibe coding lacks the rigor needed for reliability. Traditional tests can’t keep pace with agent-generated logic. To scale, we must move beyond manual checks to Agentic Testing: using autonomous agents to validate autonomous systems. Explore patterns for creating autonomous test agents, detecting failures across workflows, and continuously verifying behavior. Take away practical approaches to make AI-driven software reliable and production ready.

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

ODSP912 | English (US) | Agents & apps

Pre-recorded | (300) Advanced

#MSBuild

Chapters:
0:00 - Exploring the challenge of validating autonomous agent-built applications
00:03:41 - Markdown-based TestMD framework integration for CI/CD
00:04:08 - Shareable evidence through video logs and trace runs
00:05:28 - Starting test case execution and opening KNCLI in interactive mode
00:07:21 - Initializing KNCLI session within agent environment
00:08:35 - Demonstration of KNCLI aiding AI agents in building and testing end-to-end workflows
00:09:23 - Order placement and test data generation for checkout
00:10:02 - First workflow completed and preparing for second step
00:10:45 - Workflow successfully completed and test passed

## Transcript

*1,665 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=NXodiipqNco&t=0s)** Hi everyone, welcome to Microsoft Build 2D6. I'm Spurs KC Developer Relations Manager at Test Me AI and we are very much excited to be back here today. I'm going to talk about a very interesting topic, agent testing, because here we are. Agents can write code now. They can also run it, break it and patch it. What they haven't been really able to do is test it not in the way that you would trust before shipping an application to production. And that's the gap. An agent can generate hundreds of codes in seconds, but the speed is in the hard part. The hard part is trust. Did it test the right thing? Can you actually rely on what it tells you when it says everything passed?

**[0:47](https://www.youtube.com/watch?v=NXodiipqNco&t=47s)** And that's what I want to talk. About today and specifically I want to show you around Keynes CLI, the newest product launched by Tesma AI to help ship end to end product in an agent take era. It is an command line tool built so that agents can test the code in the careful engineer, Not just running checks, but giving you something that you can actually rely on. Everyone is focused on how fast we are building, but very few of our are asking the real question, How fast we are validating. How we are able to trust an application that was built by set of autonomous agents and deployed by another set of agents. How we are able to trust and feature or an page that was developed by an agent is doing what

**[1:36](https://www.youtube.com/watch?v=NXodiipqNco&t=96s)** it is supposed to be doing without any human intuition. This is the exact blind spot that we are targeting today. The fix is adding more intelligent smarter system, but is to add a deterministic validation layer between shipping and development. To solve this we at Tesma AI released Keynes CLI. Keynes CLI is a command line validation layer that helps you. Test any. Feature application on a local browser. Keynes CLI can be used by humans and directly by agents. It is. It natively integrates with all of your agents. Could be. Cloud Codex. Gemni, Copilot etc. You can describe KSLI what you want in a natural

**[2:24](https://www.youtube.com/watch?v=NXodiipqNco&t=144s)** language. Prompts and KSLI will open a local browser, test it, test your feature out and you also have the option to validate that on cloud, on different cross browser, cross device, cross environment setup. This helps you release your features and products with confidence. So what do you get out-of-the-box with kcli? First is intent based control. You just. Need to describe kcli, the natural language objectives. There is no betel test scripts, no locators, no selectors, no X paths. Kcli also helps with resilient runs. It stays on the task even when there is a complex journey involved. KSLI also automatically discover bugs while it is executing and

**[3:15](https://www.youtube.com/watch?v=NXodiipqNco&t=195s)** if there is any failure it has vision based waiting. It actually waits on the required rendered page or feature then adding arbitrary time waits. KSLI by default generates the playwright code of the test that is created. So you can put in the natural language prompts and playwright test case comes out back. It also has a test MD framework which has all the test cases that we have written in a markdown value. You can autoplay it anytime and you can also trigger it by your CICD pipeline. All the test cases generated by Knci also has auto heals so if there is any UI change on your page, Knci will automatically heal the test cases and give

**[4:05](https://www.youtube.com/watch?v=NXodiipqNco&t=245s)** you the new test code in return. Also have a shareable evidence so you have video logs as well as trace runs for each run. Kncli also gives out agent native ND Jason format so it's a structured output which is understandable by all the agents. To use kncli, we have three options you can directly use in your command line CLI by running this command and Justice add your prompts in natural language prompts and KNCLI will start automating that. We also have an SDK where you can just import KN from our SDK and which can be used in your CI pipeline or any custom agent or any of your test suite.

**[4:53](https://www.youtube.com/watch?v=NXodiipqNco&t=293s)** KNCLI can also automatically talk to your agent tool, so just point your agent to our agent MD file and your agent will understand how to use KNCLI effectively while building your applications. So let's see this in action. To start using KSLI, you just need to download the NPM module in your system so you can directly copy this command and paste in the terminal and let your KSLI get downloaded. Once downloaded, you can open any terminal and call KSLI to start running your test cases. For now, I will open KSLI in an interactive mode, the session get initialized and we get an option to paste our objective.

**[5:42](https://www.youtube.com/watch?v=NXodiipqNco&t=342s)** So I can write any kind of objective here and KNCLI will start completing that workflow. For now I have a sample website where we are trying to complete the checkout flow and pasting the order ID from our first session into Google. In our another session, KNCLI will start understanding the objective and as you can see it has beautificated into two workflows. The first task is to complete the checkout flow and the second task is to copy the order ID and paste it in another session. And to complete this, KNCLI will open a local browser and start completing and thinking about the next steps. As you can see, it has automatically opened the sample website that we have added and it is thinking how

**[6:32](https://www.youtube.com/watch?v=NXodiipqNco&t=392s)** how it can navigate to the next step. You can also see all of the steps that it has identified in the terminal itself. And it will take some time to complete this. So let's also check out another method where you can use KNC Alide directly with your agents. To do this, you just need to paste this agent MD file to your agent and your agent will understand how to use knci while it is building out a new feature.

**[7:21](https://www.youtube.com/watch?v=NXodiipqNco&t=441s)** For this, let's open another browser and call out plot to call knci. Within your agent browser you can just used by directly adding slash and typing key NCLI and key NCLI. Session will be initialized within your agent environment. It is identifying my user ID and key NCLI is ready to use As you can see. You will also see what are the different types of actions key NCLI can perform. It can perform any type of actions, assertions, It can extract any type of top results and also run any test suite that we already have within our project.

**[8:14](https://www.youtube.com/watch?v=NXodiipqNco&t=494s)** File. For this, let's let's try something simple. Go to testmuai.com and validate if the page opens. KNCLI directly interacts with your AI agent and think about the next steps. So while you are building with any of your AI agent, let's say it is cloud codecs or Copilot, your agent can directly define what kind of end to end test cases it want to write according to the feature or product that you are developing. And KNCLI will provide them hands and eyes to perform those end to end workflows.

**[9:06](https://www.youtube.com/watch?v=NXodiipqNco&t=546s)** By default for any agent, it runs in a headless mode and you will see all the results popping up here once this step is completed. Meanwhile, let's go back and check out what is happening in our TUI mode. As you can see it is placing an order and also thinking about adding. As you can see, it can also automatically generate some test data to complete the card. Checkout process. It has completed the order and it has completed almost completed the first flow that it has identified. Now it is extracting the order ID from the first flow confirmation.

**[10:02](https://www.youtube.com/watch?v=NXodiipqNco&t=602s)** Now it has completed the first flow. It has extracted and saved the order ID from our first flow and now it will try to complete a second step that is opening a google.com and pasting the order ID from our first Test case. Now it is opened google.com and it will now paste our order ID. It has successfully pasted the order ID from our first flow into the second flow and it has passed all

**[10:55](https://www.youtube.com/watch?v=NXodiipqNco&t=655s)** the. It has completed the workflow and it has passed the test case. Now once my test case is completed, I can click on exit and it will save the session into the particular file folder that we have wanted. And it will also download the create a playwright script of the test case that we have completed. And it will also show us a shareable link. So I can just directly copy this and open it in my browser. Here we get all the logs of the steps that we have completed.

**[11:42](https://www.youtube.com/watch?v=NXodiipqNco&t=702s)** I can automatically autoplay this and it will play how Cane CLI basically completed this workflow. You can also see the cursor, what kind of decisions it is making and how it is completing the user's objective. And this becomes a shareable proof of any any step, any test cases that we are running. So you can validate it before completing before merging this feature or product into your. And if there are any bugs that are identified within this step, you will also see KNCLI automatically marking that

**[12:34](https://www.youtube.com/watch?v=NXodiipqNco&t=754s)** bug to the user as well. Now let's also see what happened while using KNCLI with our AI agent. I, our AI agent run the objective in an headless mode and it gave us lot many starts. The test case was passed, the objective was completed, and it also gave us an agent rating. You can also see the shareable proof by copying this and pasting and viewing it in your own browser.
