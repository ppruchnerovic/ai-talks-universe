---
id: H_1bo-vM1vc
title: "Make Vibe Coding Safe: How to Test with Playwright | Amazon AGI Lab"
slug: make-vibe-coding-safe-how-to-test-with-playwright-amazon
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 13
published_at: 2026-06-18T22:16:13Z
video_id: H_1bo-vM1vc
url: https://www.youtube.com/watch?v=H_1bo-vM1vc
youtube_url: https://www.youtube.com/watch?v=H_1bo-vM1vc
tags: ["AI"]
topics: ["Coding assistants & agents"]
transcript: true
---

# Make Vibe Coding Safe: How to Test with Playwright | Amazon AGI Lab

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `13 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=H_1bo-vM1vc) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 3 - LIGHTNING TALK] Vibe coding is fast, but it often skips the safety rails: features look fine in a demo and then break in real user flows. Especially when you iterate on them. This talk shows how to make vibe-coded web apps reliable by adding end-to-end tests with Playwright that are quick to write, stable in CI, and focused on what actually matters.

A big shift is that modern coding assistants like Cursor and Claude Code can run commands and iterate on real failures. Whats missing is the glue, between e.g. Claude Code to run a test and gets its state. I will show practical workflows for writing tests faster using MCP Skills and Playwright MCP, both in an editor and inside Claude Code environments.

Based on lessons from building multiple websites over the last months, I will share a repeatable approach for growing a small, high-signal test suite that keeps up with rapid development and gives you the confidence to ship more changes without fear.

SPEAKER:
Max Schmitt - Member of Technical Staff, Amazon AGI Lab (and prior core contributor to Microsoft Playwright)

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*2,595 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=0s)** Welcome to my talk make white coding safe and uh how to test with playright. Uh next 15 minutes we will spend about like how you do wipe coding that's what everyone does probably and how to make sure uh that white coding works over time. Uh let me get started short introduction about myself. Uh I was working the last 5 years at Microsoft working on playright. Uh playright is nowadays the leading browser automation end to end testing solution and it works across like chromium browsers, Microsoft Edge, Google Chrome. It works around Firefox and WebKit. You can do it in any any language of your choice. You can do it in JavaScript, TypeScript, uh Java, Python and C#. And uh yeah, across all the platforms and yeah, people use it for end to- end testing, but especially the last one or two years. It's really exciting because we've seen like people

**[0:47](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=47s)** use it for AI and automating uh the web. Uh on the right side, a little bit for to set in perspective, we have like around 90,000 stores on GitHub. And uh yeah, I love open source. the last 10 years I was working heavily on open source and nowadays uh I moved to San Francisco from Berlin to work at Amazon to automate browsers there. Uh yeah, I started in the beginning, but everyone does wipe coding, right? You do it, but at some point you do it again. You start modifying a feature you did last week, but it breaks. And how to prevent that from happening? The clear answer is tests, right? But tests are really hard. Back in the days, you did it with Selenium. Nowadays, you do it with Playright, but do you still write them by hand? Uh, probably no. And today, I will show you how to do it really easily and make it reliable. So, how do you do it? On the left side you see what you can already do with

**[1:36](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=96s)** your coding agents, right? The coding agents like cloud code, codings and cursor they have all access to like the code base, right? They can read the files, write the files uh across different projects and so on. They can run bash commands really awesome to start web servers uh to run the tests as well. And they can use the famous error loop to debug some issue and then uh do like uh the famous loop when an error happens do some modification add console logs and do this over over again until the bug is fixed. Uh they have access to git and that's like what offers uh that's what like codecs and cloud code offers out of the box. But what if you add a browser to the loop right? What capabilities do you get? Then you get access to the browser state. So the agent sees what actually got rendered. In case of react you see like all these

**[2:24](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=144s)** real components which got rendered. In case of Nex.js you see what next.js on the client side and on the server side rendered and you see instant verification as well. Nowadays you just start your vid your next.js with like hot reload. You do a change or your agent does a change and it automatically reloads. The agent can immediately see it and verify does the fix actually work. Uh you can debug browser only bugs very specifics here. Uh and really exciting as well you get access to playright CLI and MCP to interact with your testing suit very efficiently. How did we get here right like pre2024 uh we had all these normal browser automation tools. We had selenium we had playride we had puppeteer. Uh selenium has been around for like 15 years. Uh puppeteer was released 2018 and then playright came around 2020. Uh a little

**[3:13](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=193s)** bit later we uh released agents computer use was announced and uh MCP was announced by entropic and uh there was like a lot of chaos then and everyone started shipping. There was playright MCP, there was openAI operator and test agents. But what tool should you use now when right this is like the main question which I would like to get an answer on everyone has uh at the end of this talk nowadays coding agents can see the browser there are a lot of tools which you can use like playright cli uh there's chrome dev tools mcp and agent browser by versel uh but how does it look like how does it work and uh we will see that in the demo in a bit so let me show you a brief demo so the demo is about like how to write a test right uh on one hand I want to show you a demo without MCP without any fancy

**[4:01](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=241s)** integration of your coding agent and uh the agent then just infers the locator from yeah let me yeah the agent just infers the locator from the source uh let me jump straight into the demo to show you what this means. So um this is like just a normal cloud code session and in this folder I have like a Nex.js JS application which is like very typical if you like ask your agent to create a web page and I want to create like some test coverage around this delete button. Let me show you uh this app. I think I have it running here uh to set in perspective how it looks. So this like AI console task and you can create uh some tasks and mark them as completed and so on. And I would like to cover this delete functionality here which I

**[4:50](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=290s)** need to approve with like a sure button with a test. And I just like before I asked my agent here to cover this with a test and I said yeah please cover it put it in this test file and uh test this and use the existing fixtures which I have and then run the test and make it uh confirm all of this harness like all of these normal scaffolding you can put in your cloud MD as usual right or agents MD. Uh if you run this uh we will skip the execution for now. It will eventually succeed. It will interestingly enough though come up with a test uh which gets inferred from the source but it will fail sometimes for the first time because it doesn't have access to a browser right it tries to find out how react renders these buttons or like your favorite JavaScript framework. React is really deterministic right you can very often look at like these components and predict how they

**[5:38](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=338s)** probably uh look if they get rendered. But like in this case it failed. It then sees the error. It looks at the error and tries to fix. In this case there was like a a rendering issue with like the the name and should be a bit different. It fixed it. It wrote the f file again and then ran it and then it wasn't working still and then it run it again and uh I think here somewhere if I scroll down it was passing. So this is like what works already out of the box right just on the left side what I showed before each coding agent it can write a test. But how to do it efficiently? And this is the interesting part. Let me show you this. So there's like another coding agent, but it uses playright MCP under the hood. And I just set a very similar prompt like before. And this is a live demo. I really hope that this works. Uh it uses like all AWS bad behind the hood. But it uses

**[6:27](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=387s)** playright MCP under the hood which starts like first typical like before exploring the codebase. Just like take a look how the whole app looks like. what existing testing infrastructure do we have? But then it says like let me actually use playright MCP to explore the page right let me actually like see let's first if like the web server is running and it will probably see that the web server is running which I have here and then in a second it will spawn up a browser and uh go through the entire testing workflow and not only like just click through and see if it's feasible it will also collect all these information about like which buttons are there what's the perfect like way to interact act with these buttons and things like this. Um, claude is being slow. Uh, I have a fallback prepared in

**[7:16](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=436s)** the meantime just to show you a little bit how this would look and then uh we will see uh I think around here. Yeah. So, it will explore the page uh around here and it sees I can see the app structure clearly, right? Each to-do has a remove button for example or actually here now it starts exploring the page and uh it sees how it looks like and it's clicking here right we saw it clicked on this and it just changed to sure and it figures out that there is like this two-step verification process to delete uh this to-do item and if we go back now to our demo it seems like oh interesting the to-do is still there after clicking delete the counter still shows five remaining and it gets it this like very like good human way of like how this website looks like. And uh here

**[8:05](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=485s)** it says like the delete doesn't seem to be working. Let me check. And it actually tries to debug not only with code also with like how the real app looks like. And in the end it comes up with a test. Uh it writes this test file hopefully like in a second and then it should all work. Let me go back to the fallback to show you how this uh looks like. Uh this is also very important to outline. when clicking each click basically sends a whole accessibility tree representation back to the model itself and back to your cloud code and it looks like this. What does it mean? It means like which buttons are there, how are they called and then the model uses it in order to figure out the best way how to click in the end in your test. So I think uh here it says like actually it wrote something let me call playright test end to end two times. The

**[8:53](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=533s)** item is still there. it continues debugging. Uh yeah, in the end I think it should come up with a test which we see here and it runs these tests and then uh it will pass. It just takes a little bit more time and model interaction basically. Uh while this is still going, let me jump back to the slides. So what you just saw on the left side was like the agent in a normal scenario just reads the sources, right? and it infers all these locators how you actually target these buttons and these text input boxes and then the test passes. It works really good on small code bases, but as long as soon as it gets like uh a little bit more large code bases with like more node modules, third party modules, monor repos, they get really overwhelmed nowadays. And on the right side with like MCP when you like actually like click through it, uh

**[9:40](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=580s)** it will find out how the website looks like and it will use the correct locators. And this is a reliable work way which works at scale across monor repos across different packages and so on. Uh all right so what tools are there nowadays for coding agents right we just saw like there's playwright CLI uh this is like basically the answer of like uh back in the days there was this debate MCP versus CLI we will get to it in a second as well there's normal playright MCP which gives you like all these browser commands like go to this website click fill reload all of this uh but then there's also this playright test MCP what we just used which is essentially like play MCP with the testr runner capabilities to run a test list. So this is what I recommend if you have playrite. Uh there's agent browser uh by

**[10:30](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=630s)** versel. This was a versatile attempt to make like an AI native uh uh coding CLI harness browser integration basically. And then Google as well tried to answer as well with their chrome dev tools MCP. Uh so there are a lot of tools to solve like browser automation encoding. Just use whatever works for you. If you use playright, I recommend playright test MCP. if you use tests. Um, what I just hinted at, there was this big debate. A lot of people might remember MCP versus skills if you were uh following along back then like uh end of 2025 MCP was very inefficient and uh it was really tokenheavy. So that's why everyone then tried to convert to CLIs instead because it was more efficient. But then Entropic came along and they fixed the spec. they fixed the coding harness and nowadays MCP is actually more coding uh sorry

**[11:19](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=679s)** context efficient. So I wrote actually a small benchmark to compare it and if you like look on the on the left side here MCP in September 2025 there was like around 1.4 4 million context tokens which it consumed and this was very inefficient right this was like when this YouTube video was announced and uh that's why they converted all to skills basically but nowadays if you look at MCP it only consumes around 500k and that's much cheaper even compared to CLI uh so the key takeaway of this slide is basically this big debate about MCP versus skills doesn't really matter anymore just use whatever works for you the best uh if your fancy SAS like Sentry for example has a MCP or CLI. Just use whatever works the best for you. Um, all right, let me wrap this up. So, keep the suit small, keep it green.

**[12:08](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=728s)** Uh, one spec per critical journey. What I recommend for, uh, any like small wipe coded app, uh, to do like a few instead of like a lot because it's very hard to scale and keep them maintained. Uh, run on every commit and playright traces on failure. This will give you the ability to uh, debug them later on on the way. and treat a flake as a bug because like you don't want your CI pipeline to be read like once every 10 commits. Uh investigate into it and for that small shout out to my friend working on flakiness.io which is really nice to debug all these playright tests connected with your GitHub repository. Uh yeah screenshot traces videos are like your reviewable artifacts and the output and the agent doesn't own the test suit you do you commit it into your GitHub repository. Uh yes. Uh so implementation is cheap, confidence isn't. Uh I recommend to like uh write

**[12:56](https://www.youtube.com/watch?v=H_1bo-vM1vc&t=776s)** test for your uh white coded apps. And yeah, slides, demos, and benchmark code is all on my GitHub. And uh thanks for uh listening.
