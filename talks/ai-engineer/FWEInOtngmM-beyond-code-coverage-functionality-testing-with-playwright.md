---
id: FWEInOtngmM
title: "Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft"
slug: beyond-code-coverage-functionality-testing-with-playwright
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Marlene Mhangami"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-05-16T00:00:00Z
video_id: FWEInOtngmM
url: https://www.youtube.com/watch?v=FWEInOtngmM
youtube_url: https://www.youtube.com/watch?v=FWEInOtngmM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft

**Marlene Mhangami**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=FWEInOtngmM) · [Conference site](https://www.ai.engineer/)

## Description

When an LLM writes your tests, it tends to write tests that confirm what the code does rather than tests that verify what the user experiences. Your test suite goes green. The app still breaks in ways none of those tests would catch.

Marlene Mhangami from Microsoft makes the case for flipping the order: get the agent to write failing Playwright tests against the expected behavior first, then generate code to pass them. The demo runs this live with GitHub Copilot and the Playwright MCP server on a toy store search feature, with the browser open so you can watch the agent click through filters and validate results in real time.

Speaker info:
- https://x.com/marlene_zw
- https://www.linkedin.com/in/marlenemhangami/
- https://github.com/marlenemhangami

Timestamps:
0:00 Introduction to GitHub Octoverse stats and 2025/2026 growth
2:13 Does AI actually increase developer productivity?
3:52 Importance of maintaining a clean codebase
4:36 Test-Driven Development (TDD) and the Red-Green-Refactor cycle
6:07 Common criticisms of TDD and unit testing
7:43 The problem with AI-generated self-affirming tests
8:09 Introduction to Playwright for functional testing
9:18 Integrating AI agents with Playwright for faster TDD
10:54 Live Demo: Adding search and filter features to a toy store app
12:25 Using GitHub Copilot CLI and Work IQ for feature requests
13:50 Generating and running Playwright tests live
16:10 Best practices for using AI with Playwright
17:30 Q&A: Handling state management and testing across different screen sizes

## Transcript

*3,137 words · source: supa (en, exact timings)*

**[0:15](https://www.youtube.com/watch?v=FWEInOtngmM&t=15s)** Okay. Hi everyone. Um, my name is Marlene and I am a senior developer advocate at both Microsoft and GitHub. So I work at I work in a group called core AI which looks at how developers are using AI across our products. Um so this is kind of new. To start off today I wanted to show you some stats about GitHub from GitHub Octoverse uh last year's GitHub Octoverse report in 2025 which shows data about how developers are using GitHub. What we saw from our report was that more code was added to GitHub last year than ever before. So about a billion commits were pushed to the platform in 2025, which is GitHub's most

**[1:06](https://www.youtube.com/watch?v=FWEInOtngmM&t=66s)** active year ever. Okay. What we know now in 2026 is that this growth is accelerating. So, a couple of we haven't actually released any official stats yet, but a couple of days ago, our COO, Kyle Dagel, tweeted that we're seeing about 275 million commits to the platform every week. And if we extrapolate that over time, we're going to see about 14 billion commits by the end of the year. So that's 14 times the amount of growth we saw last year or commits we saw last year, which by the way, last year again was our biggest year ever with a billion commits. One thing that we know is that there's a growing share of these commits that are co-authored by AI agents. We

**[1:56](https://www.youtube.com/watch?v=FWEInOtngmM&t=116s)** haven't released the data yet, but we can actually track and see, you know, some Claude, for example, cosigns commits and so does co-pilot, but Codex doesn't. But we can also kind of track based off of uh some wording in in the code. I had a question when I saw all of this growth in terms of how much code we were seeing. And that question is, does AI actually make developers more productive? We're seeing all of this code. Does it actually correlate with productivity? One of the best resources I've seen that tries to answer this question is actually from AI engineer from a talk last year. And this graph shares findings from that talk that's from a Stanford University study of 120,000

**[2:46](https://www.youtube.com/watch?v=FWEInOtngmM&t=166s)** developers. And in this study, um, it found that while yes, AI can make developers more productive, it's actually how the developers are using AI that matters the most. So this graph from this study actually shows us that clean code bases amplify AI gains and AI productivity while unchecked AI in a codebase is going to amplify entropy. To illustrate this point, the speaker from this talk gave a case study example of a company that used AI in an unchecked way in their database. And what you can see is that the number of PRs that the team was pushing out increased, but at the same time the code quality that this team was was seeing decreased and actually they spent a lot

**[3:35](https://www.youtube.com/watch?v=FWEInOtngmM&t=215s)** more time reworking that code, refactoring that code and so overall though there was effective output increase of like 1% AI didn't really improve the productivity from this team. So what we learned from this study is that a lot of value that we are wanting to see as developers from AI relies or hinges on us having a clean code base. So for developers that are using AI tools, we want to focus on things like good test coverage, type coverage, and things like good documentation, modularity, and so on. So, I'd actually also argue that we need to start standardizing some practices across our teams and across our industry. And this is something that's a bit of a controversial topic because

**[4:21](https://www.youtube.com/watch?v=FWEInOtngmM&t=261s)** some people at this conference believe in just closing their eyes and shipping. And that's also okay. But I think in my ideal world and from this study we've seen, I would recommend standardized practices for keeping a codebase clean. So, how can developers maintain create and maintain clean code? This question is actually not a new question. In our industry over time, we have seen several methods that have tried to make uh maintaining a clean codebase a central part of their philosophy. One of those approaches that I've actually seen a lot of developers that are doing uh agentic coding with coding agents talking about is test-driven development or TDD. Uh Simon Willis who's very popular just recently published a blog post about how he's

**[5:08](https://www.youtube.com/watch?v=FWEInOtngmM&t=308s)** using this specific flavor of TDD called red green TDD. And here what happens is a developer the first thing that happens is the developer gets an incoming feature request. As soon as they get the the request they immediately start by writing a failing test because the feature doesn't exist. After that the developer focuses on getting the test to pass. And in this green phase, when they're trying to get the test to pass, historically, you should not be focusing on the quality of the code. All you're focusing on is speed and getting the test to go green. So, in the past, developers maybe would copy code from uh Stack Overflow and so on and get the test pass. But then after that, the final phase of this is the refactor phase. And in this phase, you're just focusing on code quality. So you're

**[5:58](https://www.youtube.com/watch?v=FWEInOtngmM&t=358s)** taking that code that you made past and refactoring it so that it follows all the best practices. So not everyone is a fan of TDD and like many things in this industry, TDD was pronounced dead in 2014. Um, and one of the most common complaints that I've seen on the internet about TDD is that it focuses too much on code coverage with unit tests and that it doesn't actually test the system. So, DHH who created Rails published this blog post in in 2014 and was kind of talking about this that is an overfocus on unit tests. And we know that when we overindex on code coverage, there's several issues that come up. One of the issues is that

**[6:45](https://www.youtube.com/watch?v=FWEInOtngmM&t=405s)** there's a tendency to test implementation details. So um take an example like we see on the screen where we are having an order calculation with a discount. If the test is tied directly to a method like calculate just simply renaming the name of the test even if the functionality is still fine is going to break those unit tests. So that's not be going to be great. even if we test specifically uh the behavior of the system like the final end result of of the price we're looking for um or we test on something like a stable contract like our API or a module that doesn't change but we export it should survive any refactors of our internal code. I would say that if you're interested in learning more about this and behavior

**[7:34](https://www.youtube.com/watch?v=FWEInOtngmM&t=454s)** driven uh TDD, I would recommend the talk by Ian Cooper called TDD where it all went wrong. It's a very good talk. Another thing that we see is that in the age of AI that uh many developers are using AI to generate tests, what they've noticed is that AI sometimes generates self-affirming tests. So while the code coverage test might pass and you your unit test suite is all green, the behavior of the system is not being validated and that's where the problem lies. So for the rest of this talk, I'm going to be focusing on showing you how you can avoid these problems and start to test for functionality using Playright. Playright is an open- source testing framework that's built by Microsoft and

**[8:22](https://www.youtube.com/watch?v=FWEInOtngmM&t=502s)** it automates end-to-end testing in the browser by simulating user interactions and the link that you see on the screen there is uh is the documentation. So play supports a number of different languages right now Python TypeScript C and the example script that you can see on the screen is what a test would typically look like. So you have that line that says page go to telling the um the script that it starts at the toys pla page is where we want to start and then we're going to look for the placeholder search and then we're going to fill that search bar with that uh letter with the word Furby and that will actually do run the search for us automatically in the browser for example. You can also use headed or headless mode. So you don't necessarily

**[9:10](https://www.youtube.com/watch?v=FWEInOtngmM&t=550s)** have to look at the browser while your tests are running. You can actually just have them running in the background as well. Um why? Okay. So going back to that idea of TDD, when we're using Playright with AI, it actually should speed up the full process of TDD for us. So, a lot of developers in the past have really complained about how TDD is slow and that it it's not effective for teams that want to move fast. But if we have AI, then what happens is that red part and the green part are fast. So, we're focusing on getting our agents to generate these behavioral tests, the playright tests. Then, we're focusing on getting the agent to quickly generate as fast as it can code that's going to make the tests pass. And then I would recommend that developers are going to

**[9:59](https://www.youtube.com/watch?v=FWEInOtngmM&t=599s)** spend the most amount of time so it grows bigger on that refactoring stage. So they're spending time looking at the code the agent has generated and making that code better. There's a number of ways you can connect your coding agents today with Playright. One of those ways is through the Playright MCP server. You can use the CLI tool if you'd like that instead. or you can use something uh called playwright agents. And when you're using playrite agents, you'll run the command that you can see on the screen. And once you run that command, it's going to install for you um three agent MD files. So the first one is going to be a planner. Second is a generator and the third is a healer. So the planner will plan which tests to run. The uh generator is going to actually generate

**[10:48](https://www.youtube.com/watch?v=FWEInOtngmM&t=648s)** the tests and then the healer will fix those tests for you. Okay. So I do want to show you a demo and I am going to hope the demo gods are smiling today. Uh so we will we'll give this a try. Oh. Oh no. Okay. Here we go. So I want to give us a scenario. The scenario is that oh you can't see my you are only looking at my PowerPoint right now and I don't know how to stop that. Uh let me close the PowerPoint maybe and see if that will help. Um >> I don't want to just show this screen.

**[11:36](https://www.youtube.com/watch?v=FWEInOtngmM&t=696s)** Sorry. Hopefully they'll give me more time. Okay, perfect. That that's working as expected. Okay, perfect. So, the scenario that we're going to imagine today is imagine I'm a developer. I'm working at a toy company called Tail Spin Toys. And a few days ago, I got an email from the search product management team and they asked me to add some new search and filter features to the site. They asked me to add in a search bar with tick search for simple searches and Azure AI search for more complex ones. And they've also asked me to add in a sidebar so customers can filter by category and price. So I'd like for copilot to help me with this task and also for us to use this uh TDD first style of development. So this is GitHub

**[12:25](https://www.youtube.com/watch?v=FWEInOtngmM&t=745s)** copilot CLI and the first thing that we can do is we're going to try to get the agent to get the information that we saw in that email and bring in the features here into our terminal. And uh for this we're going to use something called work IQ which is Microsoft it's a skill that Microsoft has developed that lets developers connect to the M365 suite. So Outlook, PowerPoint, whatever it is you would like and to bring that information here into the terminal. So if you're using the M365 suite for work, I can definitely recommend it. And what I will also mention with TDD in the past when we've done things like unit tests, um, typically people what would trigger writing a unit test is adding a new method to a class. But actually in this

**[13:15](https://www.youtube.com/watch?v=FWEInOtngmM&t=795s)** new world, what we want to focus on is the behavior. So we want to focus on a feature. So if a feature request comes that is what the trigger is for the test to be written. So now we have our list of what needs to be actually developed and I'm passing in a second uh I'm tossing in the second prompt and I'm asking copilot to help me develop these features using red green TDD to start by writing the playright tests that fail for each feature and I'm telling it not to commit the changes just for the sake of this example. And I do want to point out that the first thing the agent is going to do is it's going to start to examine my codebase. So it's going to understand what's in my codebase. I have the playright MCP server already installed in my CLI uh into co copilot

**[14:03](https://www.youtube.com/watch?v=FWEInOtngmM&t=843s)** CLI and it knows what it needs to do to create the tests to be able to test for these functions. So the agent is going to understand what the codebase is going to look uh look like and then going to write the tests for it. Uh, this process is actually going to take a while. So, in the meantime, I'm going to switch over to a new tab and I'm going to run the command to get playright the playright test. So, earlier today, I asked uh I got the agent to generate those failing tests and then I got it to do the green phase where the agent just creates the code to get the test to pass. And then now I'm asking my agent to go ahead and run the playright test to actually test for that search bar and filter feature for us. So like I

**[14:53](https://www.youtube.com/watch?v=FWEInOtngmM&t=893s)** mentioned before, I have the Playright MCP server already installed. You can see it installed here. And our agent is just going to look for the test file. And if everything works correctly, it's going to start writing some tests. Running some tests. So we see it's opened the correct page. It's typing in different inputs which is testing for the search bar is working. We saw Furby was correctly found. Simon was correctly found. And now it's clicking buttons. So also testing the category filter is working correctly. Again my hands are not on the keyboard. This is all playright and co-pilot. So super cool. And now it's correctly finding all of the toys in this specific price range. So when I run these functionality tests all I can see actively that okay the agent has written this code the code is

**[15:43](https://www.youtube.com/watch?v=FWEInOtngmM&t=943s)** working as I expected the app is working as I expected. So there's so many different ways that you can test your app by functionality and all of our tests pass. Uh now once our tests have passed that's when I would say we step into the next phase of actually going ahead and um and and running out our writing our refactor. So refactoring the code the agent has created to generate these tests that pass. So a final thing I will do is I will give you some best practices um with pay. The first thing I would say is that when Playright runs those functionality tests, it's going to take screenshots of all the tests that it's run. I've gotten into the practice of

**[16:30](https://www.youtube.com/watch?v=FWEInOtngmM&t=990s)** adding those screen screenshots to a PR. So, if I've made some changes, I'll add them to a PR. The second thing is that you don't have to run it where it launches the browser like you saw in the example. You can run it in headless mode. So, it runs in the background. And then a final thing is I would say commit your code uh before you actually get it to fix the test or you know commit before it starts to make changes to your code because if you don't commit it might not remember what it what happened in the past. So that's something to do and then I would also say to generate one feature one test per feature as well. As a final note these are some resources you could take a look at. Ah, I forgot to add the link to the GitHub GitHub repo. But all of the slides are going to be available at that link there. You can check out the

**[17:17](https://www.youtube.com/watch?v=FWEInOtngmM&t=1037s)** documentation and you can connect with me on social media as well. So yeah, thanks everyone. I think that's all the time I have today. I think we have two minutes for questions. Does anyone have any questions about this? Yes, I see a question there. I use this example. >> Yeah. How would you what are tips for more complex >> where you have a lot of uh >> I mean I think if you have a lot of state management I would focus on maybe

**[18:08](https://www.youtube.com/watch?v=FWEInOtngmM&t=1088s)** I would recommend using playright agents where it downloads the specific agent.mmd file because that's going to have some specialized instructions that are better at handling state and things like that. So, I found that agents um Playright agents specifically has a lot of good instructions already built into it that should help with that. Another thing that you could do is if you didn't want to use Playright for everything, you could also just directly test your APIs. If there's an API available, that's something you could do. Um so, yeah, that's what I would recommend. Another any other questions? Maybe one more question. uh who I'm not sure. Yeah. >> Can play also check like different like sizes like from like desktop like

**[18:58](https://www.youtube.com/watch?v=FWEInOtngmM&t=1138s)** >> Yeah. >> Yes. Yes, it can. It can check your mobile versus on desktop. It should just work. Yeah. One more >> for browser based uh checking for if I'm developing a Mac app or a iPhone. It's browser based for the moment. Yeah, for the moment it's only browser based. Yeah. Okay. I think that is all all the time I have for today. Thanks everyone. Sorry about the no link to the GitHub.
