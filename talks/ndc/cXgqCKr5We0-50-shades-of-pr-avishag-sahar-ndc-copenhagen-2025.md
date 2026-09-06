---
id: cXgqCKr5We0
title: "50 shades of PR - Avishag Sahar - NDC Copenhagen 2025"
slug: 50-shades-of-pr-avishag-sahar-ndc-copenhagen-2025
conference: ndc
conference_name: "NDC Conferences"
category: "General software conferences"
edition: "NDC"
year: 2026
speakers: ["Avishag Sahar"]
channel: "NDC Conferences"
duration_min: 17
published_at: 2026-01-21T11:52:49Z
video_id: cXgqCKr5We0
url: https://www.youtube.com/watch?v=cXgqCKr5We0
youtube_url: https://www.youtube.com/watch?v=cXgqCKr5We0
tags: ["AI", "Cloud", "Languages", "People", "Serverless", "Soft Skills", "Tools", "DevOps", "Lightning Talks", "NDC", "Conferences", "2025", "Live", "Fun", "Copenhagen", "Developers", "Festival", "Denmark", "Avishag Sahar"]
topics: []
transcript: true
---

# 50 shades of PR - Avishag Sahar - NDC Copenhagen 2025

**Avishag Sahar**

`NDC Conferences` · `NDC` · `2026` · `17 min`

`#AI` `#Cloud` `#Languages` `#People` `#Serverless` `#Soft Skills` `#Tools` `#DevOps` `#Lightning Talks` `#NDC` `#Conferences` `#2025` `#Live` `#Fun` `#Copenhagen` `#Developers` `#Festival` `#Denmark` `#Avishag Sahar`

[Watch the recording](https://www.youtube.com/watch?v=cXgqCKr5We0) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Copenhagen in Copenhagen, Denmark. #ndccopenhagen #ndcconferences #developer #softwaredeveloper

Attend the next NDC conference near you:

/        @NDC

Follow our Social Media!

In this short and fun talk (yes it’ll be fun!) - Avishag Sahar laments about the top blockers of PRs, but cheer up - because I’ll also provide insights into how to unblock them.

## Transcript

*2,689 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=cXgqCKr5We0&t=7s)** So almost uh noon but still we are in the morning part. So good morning everyone and thanks for joining us today. Um really uh we appreciate your time uh and just like thanks for being here. Um today in this lightning in this lightning talk that I'm going to present I'm going to talk a little bit about pull request in general many kinds of pull requests and blockers that we are um that we have uh and understanding uh and basically understand them why they are happening and how we can overcome them. So uh shortly introduction I'm from Munich, Germany, Deutseland. Um for the past decade I worked for a few

**[0:56](https://www.youtube.com/watch?v=cXgqCKr5We0&t=56s)** companies uh worked with few source control uh met got introduced to um pull request, merge request any kind of a request like this. Um and yeah uh and this gave me the perspection of uh the common delivery cycle. So what is the common delivery cycle? Basically what I'm talking about it this cycle is the cycle that us as developers we experience when we are working on a task when we are working on something with we want to code and to deliver to production. So the first step most of the time would be actually there is you know there is another step that is not written here the obvious one we are getting a task from Jira trailer whatever and we are working based on

**[1:45](https://www.youtube.com/watch?v=cXgqCKr5We0&t=105s)** task based on story something like this we have our requirements we are doing some grooming we are overviewing everything and once we're done we can start code we can start the best part like I hope like for you it's the best part coding the fun part um this will be the first step in this cycle. Afterwards, we are done coding and we want to start the delivery process. Now, the delivery process is going to uh start with us creating a PR, a pull request or a merge request or anything an entity that allows me to deliver my code to a reviewer in my team. Um, happy pass would be that the PR is immediately approved. Amazing. Awesome. This is really something that happens all the

**[2:34](https://www.youtube.com/watch?v=cXgqCKr5We0&t=154s)** time. No, of course not. But in this PR before we are really allowed to merge, we'll have few cycles something with the review. We can write we can run CI, we can run tests over the CI, anything like that. Uh llinter many many stuff and after a few cycles in this stage we are heading to the merge. Um hopefully for you merge will end up by clicking. Sometimes it's been automatic automatically done by by tools. Uh it starts the integration phase and at the end at the end of the cycle you are finally allowed and you are able to deploy. Sometimes it's manually. Yes. Yes. I know companies today that are still copying DLL files from their local machine to the prod environment. But

**[3:23](https://www.youtube.com/watch?v=cXgqCKr5We0&t=203s)** hopefully for you it will be automatically. So this all consists the cycle. Um and the big question would be how can we speed up the cycle reduce blockers? Well the answer for that would be duh. Like this is obvious. Like of course we want to reduce the blockers but how can we reduce blockers? So one of the managers that I was working with long long time ago, he told me "Vichi anything that I can write a script for, anything that I do manually that I can translate into a script, I would do it right away. If I'm going to repeat on a task more than one time, I'm going just going to write a script and just

**[4:12](https://www.youtube.com/watch?v=cXgqCKr5We0&t=252s)** automated it." And there we are starting to meet the CI/CD approach. So for all of us, I I hope it's kind of obvious. It's kind of given. But again, I still know companies that are copying files from one environment to another in order to proceed deployment. And even me, like I uh on my first company that I was working for, this is what we did. We didn't have any developed CI/CD. We had to copy files from our local machine to production environment. So CI/CD is not that obvious but if you are able to automate your process to automate your development you will actually be able to boost up the cycle. Now again this is obvious and this is really made a huge effect on how how we work these days right so this will be on

**[5:03](https://www.youtube.com/watch?v=cXgqCKr5We0&t=303s)** the end of the cycle super helpful we know tools like GitHub action circle CI drone all of those awesome tools that can help us do it automatically what can help us at the beginning the revolution that we are experiencing right now so a way to automate code would be to use um AI, right? Honestly, it's it's kind of I don't know if I should like even say it, but the past like in the past two, three months, a lot of my work consisted of tabs really tabs, tabs, tabs, tabs, tabs. Sometimes it it hits right, but sometimes it doesn't and I'm just like reviewing it. You still have to you still have to have major and good uh foundations in order to to to understand the code. But really

**[5:53](https://www.youtube.com/watch?v=cXgqCKr5We0&t=353s)** this is like a huge revolution that we are experiencing right now. The the speed that we are coding that we are able to deliver to rep PRs to our teams is just like it's un it's unreal. So yeah if we are able to in our companies in our teams to integrate some automation in the code area and to integrate some automation in the deployment area we're done. So actually now I would say that are we really done and the next question would be can we boost it even even more um in linearb my current company we're specializing in optimizing cycle times for our routines so what we did we did we are doing uh we are doing all the

**[6:44](https://www.youtube.com/watch?v=cXgqCKr5We0&t=404s)** time we are having sorry we are doing researchers over our customers pull request. We have a lot of data. We can analyze. We can understand where are the gaps. And what we came to notice is in most cases your code is actually stuck there. Remember the cycle that I showed you and the steps and the PR. So the PR we talked about the PR having cycles on its own, right? And why and why like why is that? Well, based on on the data that we see, we can see that a lot of code stacks there. Hold on. Yeah. Um because of PRs that looks like this. Now, this is a really bad example of how PR of course all the

**[7:31](https://www.youtube.com/watch?v=cXgqCKr5We0&t=451s)** names are hidden and we don't want to embarrass anyone, but this is an example of a really bad PR that can get uh that can get into a really high risk. And why is that? First, it lacks off context. I don't know what is it feed custom question. What is it? What is the juro ticket? There is a link there that is not associated with any any juro ticket. So, I don't have any description. I don't know what I'm going to review. I don't have any reference of the feature. What's going on here? We see there are like tons of commits. We see a lack of context and of and and we see by the way a huge size of it. So there are tons of additions and let me tell you by the size of the files it's not like a single uh packages lock something or anything like this. This is like a really business logic that try to to get to

**[8:21](https://www.youtube.com/watch?v=cXgqCKr5We0&t=501s)** production and the result would be this change request obviously I don't know what it is like I'm I'm expect what what is what do you expect me to do as a reviewer something happened here and what affects my PR so there are like two actually point of views the one of the developers that created the PR and the other one is for and the other point of view is of the reviewer What can affect this kind of PR and create it and lead to PR that we saw is first of all tech design. You have to start with a really tech design in order to reduce the size of the PR so you it will be more deliverable. Um so you have to to to have a really you know really good investment uh in in your design. The other one is to understand the scope

**[9:09](https://www.youtube.com/watch?v=cXgqCKr5We0&t=549s)** of the task that you are working on. So if it's too big just like break it into small tasks right as a developer. Um and the other one would be the mix between refactors and features. We always tend to do it but this can result exactly what we saw here because you are working on a feature and on the way you found some something that you don't like. You said okay let's do it on the way and from one step to another you have over um one what is it? I don't see 1,300 rows. ridiculous from the reviewer point of view. Your reviewers in the team, you as a reviewer, you were working on your own task. You did your own thing and all of a sudden tech notification, you have to have a review for your teammate and

**[9:56](https://www.youtube.com/watch?v=cXgqCKr5We0&t=596s)** you are a team, you know, team player. So, you are going to grab the review and what you are going to face first is the context switch. You are working on something else and now your focus uh is is on this PR. So it creates a kind of like overwhelming effect if you get to a huge PR like this. Um and what else can affect the the those cycles is actually the the PR context. So if I'm seeing PR that looks like this I don't have even if I click on it for me doesn't tell me anything like you cannot understand anything from from it from the first site. So yeah, so the the the real thing is that on our journey on our career, we will meet tons of and many

**[10:45](https://www.youtube.com/watch?v=cXgqCKr5We0&t=645s)** many kinds of pull requests that we'll need to review that we'll need to create ourselves and there are just like tones. So the question would be if the beginning of the cycle is automated and the end of the cycle is automated can we add some automation in the middle? So I want to introduce you to to secure to kind of a new concept which we call continuous burge. So we have the continuous code with the AI tools, we have CI/CD for continuous integration, continuous uh deployment and then we have something we like to call continuous merge where you kind of add automation so you can get to the merge as fast as you can. And what it actually stands for it send it refers to the pull request and how we can boost the merges

**[11:33](https://www.youtube.com/watch?v=cXgqCKr5We0&t=693s)** in an automated way. So any kind of uh automation like this would be super helpful for you and I always remember this manager told me anything that you are done you are doing manually more than one time you can automate. So if me as a PR creator would have some automated way to add more context to my PR in automated way. If me as a creator can differentiate restrictions um for for for my pull request in automatic way it would be also valuable. We'll see it right away. uh if me as a reviewer if I can get automated notification for for for

**[12:21](https://www.youtube.com/watch?v=cXgqCKr5We0&t=741s)** pull requests that I'm very experienced in their area that also benefit me if I can have maybe auto review this also can help me so this is what we did me specifically I'm using a tool called gstream and with that I'm able to add to my projects um automations. So one example would be this one here. What I did I defined that uh action that approves maintainers documentations. What what we noticed we noticed any PR of uh of documenta of documentation can be approved if a maintainer is creating it. So the rule would be h it will look for regax. So any changes in the file that ends with uh this uh extension h if it has a im an image and if the author

**[13:13](https://www.youtube.com/watch?v=cXgqCKr5We0&t=793s)** is part of the maintainer list we can uh allow this approve to be to be applied and this will have kind of a shortcut for me to get uh to this uh uh to this merge that I'm looking for. Another example is to mark need of a screenshot. For example, if I'm working on a repo on a project of UI and I notice that there are lacking of screenshots and this is like one of my team agreement, we need to have screenshots in this pull request. So this is how I would write this rule when I'm using this uh tool hog stream. Um um save changes if we want to mark safe changes for example it's not something that necessarily will get to production but it's something that I have to do because I need to write tests. So I would mark any changes of formatting any documentation tests or

**[14:04](https://www.youtube.com/watch?v=cXgqCKr5We0&t=844s)** images as safe changes and it will get auto approved. Anything like this. Another way to to to integrate this tool is to have uh to have it uh do reviews in addition to my team. So for instance I created a small PR with only this change one row and I did it just like copy paste from another row. It's something uh that related to configuration with our uh uh ops reposi repository and it find the syntax right away. Why would I waste my time to send this pull request to someone so they might find or not my syntax error. I will just like apply an auto review and a bot will do it for me much better and much quicker. Um another example of uh

**[14:55](https://www.youtube.com/watch?v=cXgqCKr5We0&t=895s)** of this tool uh catching uh catching bugs for me it will be wrong reference. So I would try to write uh this table when I try to query but actually I just pointed to the wrong h to the wrong uh uh variable and this is something that h human eye would rarely see unless I don't know you just wrote their code yesterday and you just created a project but if you have an automated tool that does the review it's just like a lot quicker like for instance what you can do you can just like copy the diff of the branch to some AI I tool ask them uh please review my PR and they might work but if it it's being done by the CI in an automated way it will be just much quicker remember the bad PR we saw that lacks context why not have a tool that

**[15:46](https://www.youtube.com/watch?v=cXgqCKr5We0&t=946s)** write the context it writes for you the context uh in a much easier way probably prettier with h really nice emojis and tabs and everything why not so for me this was a really big change. This is a really game changer because it saves me a lot of time and it allows me to deliver much quicker. Um, and the good thing is that all of you can just like really start today with like small h automations in the PR area for you for all of your uh team members and this is something that can really really affect your cycle. Um, yes and if you have any questions feel free to reach and ask. Thank you very much. [Applause]
