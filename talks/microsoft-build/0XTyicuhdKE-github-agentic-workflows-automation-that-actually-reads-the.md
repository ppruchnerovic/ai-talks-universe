---
id: 0XTyicuhdKE
title: "GitHub Agentic Workflows: Automation That Actually Reads the Room | DEM350"
slug: github-agentic-workflows-automation-that-actually-reads-the
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 17
published_at: 2026-06-04T14:50:51Z
video_id: 0XTyicuhdKE
url: https://www.youtube.com/watch?v=0XTyicuhdKE
youtube_url: https://www.youtube.com/watch?v=0XTyicuhdKE
tags: ["AI", "Agentic SDLC", "Agents", "Alejandro Menocal", "Ari LiVigni", "Automation", "DEM350", "DEM350_v1", "DevTools", "Developer", "GitHub", "GitHub Actions", "GitHub Agentic Workflows: Automation That Actually Reads the Room | DEM350", "GitHub Copilot", "GitHub Copilot CLI", "GitHub Enterprise", "Skills", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration"]
transcript: true
---

# GitHub Agentic Workflows: Automation That Actually Reads the Room | DEM350

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `17 min`

`#AI` `#Agentic SDLC` `#Agents` `#Alejandro Menocal` `#Ari LiVigni` `#Automation` `#DEM350` `#DEM350_v1` `#DevTools` `#Developer` `#GitHub` `#GitHub Actions` `#GitHub Agentic Workflows: Automation That Actually Reads the Room | DEM350` `#GitHub Copilot` `#GitHub Copilot CLI` `#GitHub Enterprise` `#Skills` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=0XTyicuhdKE) · [Conference site](https://build.microsoft.com/)

## Description

GitHub Agentic Workflows let your repo improve itself. With a simple markdown file and one command, GitHub Actions launches an AI agent to triage issues, fix CI failures, update docs, and improve tests, with no complex YAML required. See a live demo from minimal workflow file to a safe, sandboxed pipeline that delivers a ready‑to‑review PR. Your repo on autopilot, with you in control.

Seating for this session is first-come, first-served. Add it to your schedule to plan your day and arrive early to secure a spot.

To learn more, please check out these resources:
* https://aka.ms/build26/DEM350

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Ari LiVigni
* Alejandro Menocal

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

DEM350 | English (US) | Developer tools & frameworks

Demo | (200) Intermediate

#MSBuild

Chapters:
0:00 - Overview of GitHub Agentic Workflows and goal of demo
00:01:00 - Benefits of Agentic Workflows for automation and CI/CD
00:02:16 - Demo of fictitious Mona website and automated PR generation
00:04:51 - Explanation of the setup and Copilot scaffolding process for workflows
00:06:01 - Choosing agentic workflow agent to create website update process
00:07:22 - Modifier example: customizing an agent to always perform specific actions in workflow creation
00:15:05 - Addressing security restrictions and sandboxing during compilation
00:16:36 - Encouragement to experiment with agentic workflow exercise
00:17:00 - Providing GitHub Skills link and closing remarks on workflows

## Transcript

*2,552 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=0XTyicuhdKE&t=2s)** Thank you, hope everyone is enjoying Microsoft build day one in the afternoon guys made it. My name is Ari Livigni. I'm a senior learning advocate with GitHub. And my name is Alejandro Menocal and I'm a senior service delivery engineer at GitHub. And we're going to talk about GitHub ejectic workflows and how auto this automation actually reads the room and we'll get it to the first slide. We want to get into more of the demo. The idea here is that instead of having to know YAML for actions, you can define your workflows in Markdown. You can even use Copilot to create those Markdown files that then can be compiled into an agentic workflow. So a lot of folks automation or CI is very much centred around, you know, very being very rigid and,

**[0:53](https://www.youtube.com/watch?v=0XTyicuhdKE&t=53s)** and, and it has to do syntax errors. It's hard to identify with agenda workflows. You can really automate your, your CICD easily. You can triage test failures. It can identify. It can create issues for you on a daily basis or a daily report of your of your repo or open up pull request. And the idea is that it takes a lot of the toil and the mundane things we have to do as developers on our repos and automating that process for you. I don't know if you want to add anything. And the idea too is right. We have our agents and our models behind this. So whether it's Copilot, clawed codecs or Gemini, any of the models, it can dynamically diagnose, test failures, open up pull request to make changes or maybe update your stack

**[1:45](https://www.youtube.com/watch?v=0XTyicuhdKE&t=105s)** and give you recommendations. And there's already a deep ecosystem available on different types of identic workflows. There's a website that's part of this that you can also go. Look, we're actually releasing this in public preview next week. So you'll get an idea that you can use it yourself. Also, we're going to walk through a skills exercise that you could take and use your own GitHub handle to learn how to do this and see how it works first hand. I guess we can go to the next slide. So we're going to do with this exercise is we're going to take a fictitious Mona website that is tasked with looking at different updates on GitHub through its blogs, it's change logs, maybe notes that we've written ourselves that are in the repository. And with that, we're going to constantly get updates on

**[2:35](https://www.youtube.com/watch?v=0XTyicuhdKE&t=155s)** all of that on some amount of frequency that we want to then give us APR that shows us what we can then either merge directly or obviously we probably want to peer review that and look at what's been created, have our teammates peer review that, and then we can merge that pull request. I guess with that, I think we can get into the, let's get right into it since we have like 20 minutes. Cool. So in this GitHub skills exercise, what Alejandro is going to show you is we've already kind of started the process because it takes longer than the 25 minutes we have here. But from start to finish, this GitHub skills exercise is going to show you in an issue the different steps you can take of how this works. And with GitHub Agentic Workflows, we can automatically install it and create a it'll create a PR for us of

**[3:28](https://www.youtube.com/watch?v=0XTyicuhdKE&t=208s)** how to install that in our repository. And what Alejandro is showing you here is those files that have been created. So besides the markdown file, we have an agent file which you can see it says Agentic Workflows. And this is describes what the agent installed. Just like if you have a custom agent, your repo or the the coded the cloud agent that you have normally in your repository. This sits there in in your repository under the dock GitHub directory. We also have a skill that gets installed as part of agentic workflows also. So all of this once we create the PR and I don't know if you want to show the command line of what that looks like on the exercise. So some of the set up here we installed here and we just ran this command to create the pull

**[4:16](https://www.youtube.com/watch?v=0XTyicuhdKE&t=256s)** request and initialize our repo and have the completions already set to go. And that's what created the PR that Alejandro is showing you. So I'm going to go ahead and merge this in so that you can see in action how this works. Yeah, it has some good attributes to other files. If you do this yourself, you'll see all the files that get created. Again, you can take this GitHub skills exercise and walk through it to show exactly how it works yourself. And you can take that and modify it and, you know, maybe make some changes or make it work for yourself. And what this does is really doing the setup right, of setting up that identic workflow. And what we have here is really those, you know, like for example the Copilot setup steps, it kind of goes automatically scaffolds this for you, right?

**[5:07](https://www.youtube.com/watch?v=0XTyicuhdKE&t=307s)** So you don't have to start from scratch and instead you can then have this framework and then build upon it depending on what you want to do, whether it is auto fix, CICD or automatically updating your website, right? This is the. This is where you add basically the business value of what you want to build. And it even installs an MCP server as well as part of it so that. So again, this is like a self-contained early ready to go. Like Alejandra said, it's early scaffolding, maybe some of the checks we have in there for the exercise too. We'll take a look at fixing that. But now we're going to do is we're going to go on to, we're going to prompt and we're going to use that agent. Yeah, and we're going to do that.

**[5:58](https://www.youtube.com/watch?v=0XTyicuhdKE&t=358s)** Let's choose the agent in the maybe make that a little bit bigger. So now we're picking the agentic workflow agent and we're going to give it directions to create this workflow for us that's going to update the website for us. So we want to make sure we're on the latest main branch. We're going to create a new branch and we're going to update our info file that's used for our website. So we get the latest GitHub updates from the blog, changelog and so on. And what this should do is create, yeah, when this should create our workflow file for us. And then we're going to have to compile that. So part of this project, project or process with the

**[6:47](https://www.youtube.com/watch?v=0XTyicuhdKE&t=407s)** agentic workflows is that we have to compile. Since it's just a markdown file, we have to do that so that it actually generates a YAML file that it it's called a lock file that it knows what to do to run those workflows. And we're, we added a little bit something extra here that the agent sometimes will automatically compile it for you. But we wanted to show that step. So that's why we had that in there as in the directions. And now Alejandro's adding this one extra section to the to the actual agent so that it goes through that. So you can also modify that agent. If there's something specific you want to do with your agentic workflow for that agent to do all the time,

**[7:37](https://www.youtube.com/watch?v=0XTyicuhdKE&t=457s)** you can add that to the agent. It's so one of the differences here, in case you know it was sorry about the demo, but we hear this agent is really helping us to create agentic workflows, right. So we are using this agent to help us create those agentic workflow. So it currently what we're doing is basically this agent gives us the scaffold to create more agentic workflows, right? And so the next step that I'm going to do here, it's basically add the instructions to create the agentic workflow that's actually going to update our our website, right? And in here I have for example, when is it

**[8:30](https://www.youtube.com/watch?v=0XTyicuhdKE&t=510s)** going to run? What access am I given to? And then disigentic workflows in order for them to be secure, we are not actually giving the agent any permissions besides read access to the repository, but instead we use something called safe output, which is something that happens after the agent runs. So that the, so that basically that workflow, that step in the workflow is the one that has the access to perform the actions, whether it is to create an issue, to create a pull request. And that's how we segregate those responsibilities from the agent, just having all types of access. Yeah. So we can't hallucinate or delete your code base or, you know, remove files from your repository. It's always going to be where you're in control. It's going to do that automation for you, but you're going to be the one that ultimately decides, is this

**[9:19](https://www.youtube.com/watch?v=0XTyicuhdKE&t=559s)** something that's useful from what's generated or do you want to throw it away? So currently with that prompt, right, what I'm just using is I'm using that agent agent to create the agentic workflow. And currently it's, you know, going to be thinking about that it's using that skill that we show that came with the scaffold in order to create that this new agentic workflow. So now and as you can see the steps, it's creating that workflow for us. It's preparing it. And you can see as if you've used copilot chat and the ID. This should look familiar to you to see all the steps that it's doing. Should be generating a file soon and the website we're doing this is just a basic Astro website and that's

**[10:11](https://www.youtube.com/watch?v=0XTyicuhdKE&t=611s)** actually running right now too. This is the. Website. Go ahead. No go. Ahead, this is a website that has the information and I think if you see at the top, it should say the date on it goes a little bit lower, right? Yeah, March 17th. So that's when I initially started creating this exercise. So it has that static information and the identic workflow is what's going to allow us to keep that up to date with new. You know, as you've seen announcements today about GitHub Copilot features or agents, that would be something that would be pulled from the blog or the change log as an example. This maybe could be something in your repository of a stack that you have that has versions that may be out of date. And that's another example that it would look at that

**[10:59](https://www.youtube.com/watch?v=0XTyicuhdKE&t=659s)** and then automatically give you APR to give you those updates. Here we go, and now. So it's adding the, yeah, the latest GitHub updates. Yeah. Whoops, I didn't mean to do that. Did you just delete their word? Yeah. There you go. Oh, you just closed it. OK. So that's that markdown file that update GitHub info dot MD that you can see created. That's our agentic workflow.

**[11:48](https://www.youtube.com/watch?v=0XTyicuhdKE&t=708s)** And then the next step that Alejandro is going to do is what's going to compile that markdown file. That then is our workflow that we can run at a certain frequency. And I believe there is a frequency in there, but you can also, we asked it to also do it on demand that if we wanted to do this whenever we want, we can do that as well. Just like any GitHub Actions workflow that you're used to running, it's the same applies. So that if you're familiar with GitHub Actions, this is just GitHub Actions kind of on steroids with the identity agentic workflows. Still thinking? Still still creating. Yeah. And obviously, like with any of, of anything you do with Copilot or the agents, you can iterate with that

**[12:39](https://www.youtube.com/watch?v=0XTyicuhdKE&t=759s)** agentic workflow. You can add like we added a complete comment in there that we did not want it to compile. Maybe there's other things that we want to add to the agent to make it work better for us. Maybe there's other pieces of the agentic workflow that we've created that we also want to modify as well. There we go. What's reading it? It's reading it, yeah. So it's checking the schedule. Can we open that file? Should be under workflows. Yeah yeah. So here is the the markdown file, right? It's very basic.

**[13:25](https://www.youtube.com/watch?v=0XTyicuhdKE&t=805s)** There's also a front matter that's at the top, I believe. Yep. This is all the front matter that basically instructs the general directions that we told it in natural language of what we wanted, and now it's generated this file for us and our next step is now to compile that file. Tools allowed. It's calling out. Site Contents. Let's try compiling 1 again.

**[14:21](https://www.youtube.com/watch?v=0XTyicuhdKE&t=861s)** Saying filter name. Safe output assigned to user. I am compiling the right one right workflows of the GitHub info workflows Yeah web fetch edit it's. Doesn't like the word. Allowed oh here. There's another one too, but I don't know if that's. There we. Go no. It says write for contents. Write is not allowed for security. Use safe outputs.

**[15:07](https://www.youtube.com/watch?v=0XTyicuhdKE&t=907s)** Create issue to perform. Write. It's part of the writing and sandboxing stuff too that doesn't allow you to the contents write. Oh, here should. Be read, write. Read Yeah. Write. I think write for the pull request is correct. No, I think it's. Didn't create our let's see there we go OK so now we had to make some tweaks to the front matter but now we can submit that we can add that file got about a minute left so we're going

**[15:58](https://www.youtube.com/watch?v=0XTyicuhdKE&t=958s)** to kind of breeze through this but this should have. The lock file if you want to talk about that. Yeah. So the lock file is what gets generated and that's the actual workflow. And I don't know if we can bring that up, show that too real quick. But the the lock file is the actual actions workflow that's going to run. The the MD file that we just showed you is the natural language markdown that you can do that, that you can control and check in the lock file something that gets generated as part of the compilation. We got about 30 seconds left. Again, you can take this exercise afterwards and play around with yourself. We'll make some tweaks to it, make sure it runs seamlessly.

**[16:45](https://www.youtube.com/watch?v=0XTyicuhdKE&t=1005s)** And also there's probably been updates to agentic workflows too that we have to account for. But this is the workflow file here. And then maybe just show the this, yeah, the, yeah, the slide. If you want to try this GitHub skills exercise, you can go here. And if you yeah, so if you have that link, you can go to that link via the QR code and try to get up skills exercise out for yourself. We'll we'll be iterating on it, making improvements as we go. But thank you for the time and I hope you enjoyed the session on Eugenic Workflows. Thank you.
