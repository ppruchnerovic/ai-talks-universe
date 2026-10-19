---
id: cQCzlHnNZzQ
title: "Nick Smith: Fast Track to Production: The New Stack for Today's Founders"
slug: nick-smith-fast-track-to-production-the-new-stack-for-today
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 10
published_at: 2026-10-07T22:53:35Z
video_id: cQCzlHnNZzQ
url: https://www.youtube.com/watch?v=cQCzlHnNZzQ
youtube_url: https://www.youtube.com/watch?v=cQCzlHnNZzQ
tags: []
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# Nick Smith: Fast Track to Production: The New Stack for Today's Founders

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=cQCzlHnNZzQ) · [Conference site](https://aiconference.com/)

## Description

Watch a complete software delivery pipeline go from zero to running in minutes, then spend the rest of the session on the more interesting question: what do you do with all the time you just got back? CircleCI's Nick Smith will demo the new CircleCI CLI live, and and lead a discussion on how tools with robust terminal-based access reduce the burden of setup so you can get to building software. Whether you're a technical founder, a domain expert eyeing your first product, or an executive wondering why your team still struggles with deployments, this session shows how much simpler getting code into production can be today, and opens the floor to what that possibility actually unlocks.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,708 words · source: supa (en, exact timings)*

**[0:19](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=19s)** Hi everybody. I'm Nick Smith, uh, staff field engineer at CircleCI. I've been there for a number of years that I have stopped counting. Um, today I'm going to show a little bit of an odd demo because hopefully uh if Opus 5.5 behaves, I'm just going to hit enter here and we're going to see CircleCI onboarding its own project. So, a big problem with CI, especially trying out new CI vendors, has been that migration process. Going from one CI to another, you have to figure out configs, settings, all sorts of stuff. And CircleCI recently has updated our CLI to make it so that an agent can do all of that for you. So all we're going to do here is have Claude look at a prompt that simply says fork the express project and onboard it

**[1:10](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=70s)** within CircleCI. And we'll see that happening here. Uh with the new CLI, you can do anything that you could do had to go to the UI for you can now do in the terminal. So, not only does the agent have access to the entire surface of CircleCI and can crawl over it, you as the user no longer have to go to the UI and see all of that information. So, with the CLI, uh, it's going to first thing going to check to make sure that we are authenticated. Nice thing about our CLI is we have an OOTH authentication method where you can set read only, write or admin access. And we are on the cusp of allowing you to set a custom expiration timer for that as well. So if you want an agent to just look at the data in CircleCI for an hour, that will be possible without the

**[1:57](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=117s)** agent being able to affect anything else. So you can see right here it's confirmed I have logged in and it's going to start forking that project right there. Uh and pretty soon we'll see that starting to appear on the pipelines page. Uh the nice thing about uh the CLI is as it sets up this, it's not just going to throw some settings at CircleCI, throw a pipeline config at CircleCI. It will be able to see the full output of the job. It's not just getting a status check. It's able to see exactly what is run inside the job, which is very, very handy. So, it's going to go ahead and it's asking me to fork it. This is a new thing with the auto mode which is fun to deal with.

**[2:47](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=167s)** Um so as it's going through and doing that uh the other really handy features of the cir of the CLI to help with onboarding is we do have a way to validate your config against uh a really nice schema. So it lets the agent know that it's pushing up actual config rather than uh trying to guess at what it sees. So here it goes. It's going to go ahead and create that project. And you can see right here, uh, it is creating the project. It's already getting a slug for it and everything there. So we'll start to see that pipeline coming in in a moment. There it goes. The pipeline is going to start being created. And the nice thing about CircleCI pipelines is we've actually split the pipeline up into three different areas. Uh traditionally a trigger comes in, a

**[3:36](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=216s)** pipeline runs and it has a set config for that pipeline. With CircleCI we've divided that up into three different uh spots. The first thing you can do is you can select where the trigger is coming from. So repo A can trigger from repo B. The second thing we allow you to do is set where the code is being checked out from. So repo A can even check out repo B if it needs to. And then my favorite part because I'm very uh a very big proponent of centralizing everything is you can select where the configuration is coming from. So you're able to set up a fully centralized configuration model with CircleCI uh where you're not having to update 500 configs every time you need to change just a little version. So it's gone ahead and done that first push

**[4:25](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=265s)** and we can see right there we have a CircleCI pipeline running. uh instead of polling the API consistently to see what the status is. You can see right here we have a watch command. It's not highlighting but it's right there. That watch command gives you a active status live status of what the job is doing and tells the agent what is happening inside of it. So you can see as soon as the build job actually finishes, which is going to take a little longer because we aren't caching just yet, uh it will be able to see that green. So as soon as we saw in the UI that green happen, the agent saw the success happen as well. Um so we have our first green pipeline, but that's not typically the best pipeline that we can do. So uh

**[5:16](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=316s)** agents typically nowadays are pretty good at optimizing at least the first layer of it. Uh we do provide skills along with our CLI to help your agent optimize for CircleCI specifically. Uh first thing it typically does is go in and put in some caching, but there's a lot of other features that on CircleCI that you can use to optimize. Uh caching is obviously a very easy one across the board. A newer feature of ours that can very much help with optimization is something called smarter testing. So what smarter testing does is uh it analyzes the metadata of the test suite and will only run the tests required for that change. So obviously if you're dealing with a node project, some of us

**[6:04](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=364s)** have 15,000 tests that we have to run in our unit test suite. It'd be really nice if we only had to run 10. And that system can make things go much much faster whether it's for a human or an agent. So you can see here we are getting the caching. It's checking on the step timing. So we can see all the way down to the step level exactly what's happening in the system. There's no guessing happening here. Um and it's able to iterate on itself which is very very handy. The other nice thing about smarter testing, uh, just to go back to that for a second, is there's a couple other features inside of that, I'm sure we all have to deal with flaky tests every now and again. And while we would all like to fix them, we often have to do a

**[6:52](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=412s)** little bit of a band-aid. Smarter testing allows you to rerun your tests up to five times, so your developers don't have to go in and manually rerun uh, those things um, over and over and over again. So that can definitely help speed up uh the timeline. There you can see we are still going in and uh making sure that everything is installed there. Uh we have the caching all set up which is great. And the CLI is letting the agent just go back and forth setting up all the settings that it would need to do. Um, security-wise, if you wanted to make sure that an agent was only setting up the configuration that you wanted it to set up, we have a feature called config policies, which can be used to only allow the configuration uh

**[7:41](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=461s)** to be run that you allow. It's a reggo policy. You can write it against the YAML, and that makes it so that uh it will stop a pipeline from even triggering if there's something in the configuration that you wouldn't allow. and an agent can see that output with the CLI uh and make sure to iterate around that issue which can be very helpful. You it's still running here. Uh it will go ahead and make sure that everything is good with the lint job and it's just iterating through. So what we did here was take a raw project from GitHub that had never seen CircleCI before and we're about seven minutes in. I probably hit it about six minutes ago and we already have a project that's onboarded to CircleCI. Agent can go ahead and iterate

**[8:31](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=511s)** as it goes. Uh but the actual migration process from GitHub actions in this case to CircleCI took about 2 minutes. So as you're looking at CI providers and thinking is this the best one for my agents? Is this the best one for my team? it is much easier to migrate do a proof of concept and see that information uh very quickly. The other side just because we have a few minutes here that I want to show off um is we do have open telemetry and open telemetry if you all are familiar with it provides you a lot of information about the system with CircleCI our open telemetry lets you see down to the step level. So if you have an agent that's

**[9:21](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=561s)** adds 20 extra dependencies and your dependency install step starts bloating on CircleCI, you would know exactly which step uh was contributing to that increased duration and you'd be able to action on it. Uh this is very very handy. My entire job is helping customers optimize. And because we can see down to the step level, we know if the spin-up's taking too long, we know if dependencies installs are taking too long. we know if the if a bunch of erroneous tests were added. All of that information is very very easy to see and this is a free feature on CircleCI. Uh we do not charge for this whatsoever. So end to end your agent if it was hooked up to an open telemetry system would be able to not only set up CircleCI projects would also be able to optimize

**[10:09](https://www.youtube.com/watch?v=cQCzlHnNZzQ&t=609s)** those projects based on the open telemetry data. And I'll leave it at that.
