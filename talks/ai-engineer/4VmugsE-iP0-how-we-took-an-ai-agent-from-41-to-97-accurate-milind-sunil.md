---
id: 4VmugsE-iP0
title: "How We Took an AI Agent From 41% to 97% Accurate - Milind Sunil Shah, Brainbase Labs"
slug: how-we-took-an-ai-agent-from-41-to-97-accurate-milind-sunil
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Milind Sunil Shah"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-11-05T09:00:12Z
video_id: 4VmugsE-iP0
url: https://www.youtube.com/watch?v=4VmugsE-iP0
youtube_url: https://www.youtube.com/watch?v=4VmugsE-iP0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Milind Sunil Shah", "Brainbase Labs", "AI agents", "back office automation", "AI evals", "browser agents", "agent reliability", "LLM as judge", "ontology", "Domino's", "cost optimization", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# How We Took an AI Agent From 41% to 97% Accurate - Milind Sunil Shah, Brainbase Labs

**Milind Sunil Shah**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Milind Sunil Shah` `#Brainbase Labs` `#AI agents` `#back office automation` `#AI evals` `#browser agents` `#agent reliability` `#LLM as judge` `#ontology` `#Domino's` `#cost optimization` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=4VmugsE-iP0) · [Conference site](https://www.ai.engineer/)

## Description

Milind Sunil Shah of Brainbase Labs walks through a six-step framework for improving back-office agents, using a Domino's project that tracks competitors' pizza prices across websites and delivery apps. From version 1 to version 11, accuracy went from 41% to 97%, cost per source halved from $2 to $1, and run time fell from 129 to 71 minutes, all through instructions, skills and playbooks rather than a new model. The steps: kickoff, ontology, benchmarks and evals, a narrow first agent, iteration, and handing off the whole loop.

Chapters:
0:00 Intro
0:26 The Domino's pricing problem
1:36 From 41% to 97%
2:02 The six-step framework
2:23 1. Kickoff: agree on the win
3:35 2. Ontology: define every term
5:43 3. Benchmarks and evals
7:42 4. Ship a narrow first agent
8:49 5. Iterate: score, fix, ship
9:44 Fix: the deal below the link
10:28 Fix: stuck zooming into images
11:56 6. Hand off the whole loop

Milind Sunil Shah

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,569 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=4VmugsE-iP0&t=1s)** [music] >> Hey, so I'm Milind, MTS at Brainbase. We help enterprises deploy internal agents at scale and manage them. Today I'm going to be talking about hill climbing back office agents and how we did that successfully with a customer. So yeah, our customer in this case I'm going going to be talking about throughout and like the famous local video we use repeatedly is is is Domino's. As you all know, they have 20 plus thousand stores, 90 plus markets. We started off with a single region with their CMO office. We wanted to answer this question that they kept asking. What does a pizza cost at the competitor down the street? What what does it cost in their delivery app?

**[0:48](https://www.youtube.com/watch?v=4VmugsE-iP0&t=48s)** What does it cost on their actual website with promos, without promos, things like that. They essentially wanted a spreadsheet at the end with the lowest price possible for a bunch of different items. Before we built the agent for them, they had an analyst manually doing these steps. They all look easy in isolation. You open a competitor's website, pick the right store, compare prices with delivery, takeaway, find the right promos, find the cheapest price and write it all down into a spreadsheet. It it all looks easy enough, but if you get one of these steps wrong, you look like you you you get a cell at the end that looks finished, but it's just wrong. We had to build an agent that does the same. Reads a bunch of items, finds the website, interprets prices, fills the spreadsheets, hands it off to an agent, and flags anything that it thinks it's not sure of.

**[1:35](https://www.youtube.com/watch?v=4VmugsE-iP0&t=95s)** When we created version one of this agent for them, we had 41% accuracy. By the end at version 11, we had 97% accuracy. Our cost per source per source means per item per per competitor per website went from $2 per source to $1 per source. And the amount of minutes it took per run went from 129 to 71. All of this went just with just just instructions and and skills and playbooks changing. Here is like the six steps that we use, not just with Domino's, but with other customers as well. We start off with kickoff, followed by anthology, benchmarks, first agent, iterating, and handing off. I'll talk about what these steps mean in detail and what we did for Domino's in each of these and hopefully it's a repeatable framework that y'all can use internally as well. So, step one is kickoff. You should

**[2:24](https://www.youtube.com/watch?v=4VmugsE-iP0&t=144s)** ideally talk to your customer or end user and agree on what the win looks like. As of today, what what is the job? What did the human sign off on at the end of it? How long does it take? How much does it cost? How accurate does your agent need to be? Who judges the output? And what must the agent never do alone? What assumptions should it never make? For Domino's, we ended up creating this brief that worked really well for us. Our outcome at the end had to be a faster, repeatable way to collect local competitor pricing without losing the judgment edge cases need. So, we asked them uh all of these questions. As of today, the analysts create a spreadsheet and the pricing team uh find finally analyzes it. An analyst spent 2 hours daily manually actively working on creating the spreadsheet. Every cell was then checked and and just confirmed and

**[3:14](https://www.youtube.com/watch?v=4VmugsE-iP0&t=194s)** the agent at the end just had to ask for the analyst for sign off and flag anything else it had to. Our win in numbers looked like just having the highest accuracy, the lowest cost of sources possible, run time to be as low as possible, and before we even started, they weren't even sure if we can do this discount search at all. >> [snorts] >> Step two is anthology. What does that exactly mean? We we try to write down all the terms that that the agent needs to know to never make assumptions, which means we need to tell the agent exactly what it's supposed to collect, where each answer comes from, where does it go, what does each term mean to the analysts that actually do the do the work manually, and what should the agent do when it can't figure something out. If if there's one jewel here, it is that every term should ideally have a definition. If you don't

**[4:02](https://www.youtube.com/watch?v=4VmugsE-iP0&t=242s)** write something down, the agent's going to guess and probably get something wrong. For Domino's, here's what it looked like. We at Brainbase have a memory primitive of our own that has memory that looks like a Postgres database that the agent can do whatever it wants with. We gave it a target stable where we gave it up all the items. In this case, let's look at ID number 14. ID 14 is brand B. It's a large pizza. Uh takeaway method is Sorry, it's delivery and on app B. The agent hypothetically does browser use, finds the price on the website, finds that it's 24 and 19. 24 is the striked out price, 19 is the sale price. We also now have a rules file where we actually tell the agent to specifically mark down the price that it that a user pays at checkout, not 24. This came from like a valid failure.

**[4:51](https://www.youtube.com/watch?v=4VmugsE-iP0&t=291s)** What it saves at the end, we created a table again called price observations where it with the corresponding ID stores what price it saw, what the full price was, and the actual source. And at the end, we give it a spreadsheet that has all placeholder item IDs, and all it has to do is look up the ID and replace the price. When a cell is wrong, it points to the exact page and the rule behind why it chose the selected price. Other rules that we mentioned that came through actual life traces were definition of what a large pizza looks like. It's anything that's actually the item itself or a bundle. Delivery is not equal to takeaway. It It got confused with that. It's supposed to do promotion math. If it's 30% off the price, it should do that before entering it in the spreadsheet. And if it can't verify it,

**[5:39](https://www.youtube.com/watch?v=4VmugsE-iP0&t=339s)** write it down as a gap and do not guess. Step three is finding out benchmarks and emails. Now Now, these steps can be interchangeable slightly, but essentially you're trying to figure out what you can run offline emails on and what you can run online emails on. For offline emails, you should ideally start off by asking them if they have past cases that they already have answers for. In this case, we had analysts from Domino's who had spreadsheets that they had worked on. Can we actually rerun those um input cases to get the same final output? And then at the end, how do you figure out how to score each thing that the agent is doing? For evals, you try to figure out what you can check deterministically, what you can check why an LM as a judge, and what you can check as an agent as a judge. That's a concept that we think is slightly more unique, where if there's an output artifact, you probably want an

**[6:27](https://www.youtube.com/watch?v=4VmugsE-iP0&t=387s)** agent to take multiple turns, multiple tool calls to figure out how correct that that artifact is. And at the end, what happens when something goes wrong, and what happens when it's flagged? You should try to score as many things as you can with these three things. So, yeah, at Domino's, our benchmark essentially started off with all the spreadsheets that they had. We tried to create the input environment by going to archive.org and having snapshots of competitor websites at those given dates. What we saw that it was that it didn't work with delivery apps because they didn't serve data the same way. So, we ended up storing browser screenshots for everything the agent was doing starting from version one of the agent, and that's how we create up our environment for for the internal benchmark. For evals, we use code for things like checking if every ID cell was replaced with the price, if the discount map was

**[7:15](https://www.youtube.com/watch?v=4VmugsE-iP0&t=435s)** computed correctly, if the price was 20% plus or minus compared to the previous run, was it flagged or not. LM as a judge just checks the trace to see if the right item was selected, and if the right promo was applied. Agent as a judge actually goes to every flagged price and actually confirms if the flag was valid or not. And the analyst at the end will go look at the final flags and try to figure out what the reason for it was if something went wrong. Step four is actually shipping some version of a first agent. You should ideally ship a narrow first agent in your stack that you can score from from day one. You should probably figure out what the smallest slice worth scoring is. You should figure out how accurate things should be, how long and and you should use this agent to figure out how long does it run take, what what does it cost, what does it get wrong, and things like that.

**[8:05](https://www.youtube.com/watch?v=4VmugsE-iP0&t=485s)** Version one's job is to be measured, it's not to be good. You should widen the scope uh widen the scope after you get some baseline score they're trying to meet. For Domino's, as like I mentioned earlier, version one for us was just 41% correct. It took more than 2 hours. It was $2 per source. And and it just wasn't working well. We found a bunch of changes, made fixes, and then improved and increased the scope. So, we started off with just one app, one item in one city. Moved on to adding burgers and takeaway options. Moved on to adding another app, and finally other websites as well. So, starting off small narrow scope worked out really well for us to figure out how we can fix things. Step five is to just iterate. You should score, fix, and ship. Here is where

**[8:53](https://www.youtube.com/watch?v=4VmugsE-iP0&t=533s)** you'll do steps two, three, and four. Keep iterating, improving your anthology, improving your emails, your benchmarks to get things that work. You should figure out which failures are most expensive, most frequent, fix them, what changes should be used to fix them. If that change results in increased run time or cost, if yes, are you okay with that increased run time and cost? And how can you use those failures to create and add to your benchmark cases or eval criteria? Ideally, change one thing at a time and fix the instructions before you want to change the model entirely. At Domino's, we highlighted two examples. Before I get to that, here is a graph of how our progression went. We one started off at 41%. Um more than $2 a source. We 11 after a bunch of changes, it's $1 a source, and and 97% accurate.

**[9:44](https://www.youtube.com/watch?v=4VmugsE-iP0&t=584s)** So, yeah. Here's an example of a very simple rule change that we made. We gave the agent a link of of a large pizza to find for brand B. Via delivery on its own website. It went to the link which had the section already highlighted. It clicked on it, found the large pizza, found the price, and ended there. The analyst got that somebody manually caught at the end that there was actually a deal below that website below on the same page, that was just $21 instead and and it missed that, right? So, all we had to do there was add a simple rule to not stop at the section that it gets linked to, but actually look at the entire page. And a simple change like that helped us just like catch this and then make sure it doesn't happen again. Another more intricate change that we had to make was actually browser use

**[10:32](https://www.youtube.com/watch?v=4VmugsE-iP0&t=632s)** behavior of set agent. So, in one of the runs, we saw that for brand D this is a this is a brand called brand D promotions page, where all the promotion prices were inside images, so not actually captured in text. What the agent did is it looked at all 26 promo images to find the item it was looking for. It looked them looked at them again by zooming in 4x, 5x, 6x. It found the right card at minute 13, but it still kept zooming to double-check and verify, and it it was just in a loop, and we had to manually stop it at minute 15. We realized after manually looking at the trace and the website, that the HTML DOM is actually super important and could have saved the agent a lot of work here. So, we we tell the agent in in our latest rules to go look at the HTML DOM first, look at things like image titles, all text

**[11:22](https://www.youtube.com/watch?v=4VmugsE-iP0&t=682s)** before looking at the actual image rates, and just stopping past a certain zoom level. What that resulted in is is 1/3 the number of image rates, reducing cost by over 50%, and just us getting an actual answer and a finished report. So, while we have automated checks and eval criteria to help us catch a lot of things, some things require our engineers to actually look at traces and and browser on use tool calls and and just see what went wrong. So, yeah, we made a bunch of these changes, got to V11, got to 97% accuracy, and now it's just figuring out hey like like what next? So, so our our way of this is trying to figure out how best to hand off to the customer at the end. We want to figure out who's running these agents, who's reviewing the outputs, who's trying to correct who's trying to take the corrections into and converting into rules and benchmark

**[12:10](https://www.youtube.com/watch?v=4VmugsE-iP0&t=730s)** cases, and who decides when new version is ready to ship. All these questions are things you should probably have written down. Um you're trying to hand off an entire loop and not just the agent. Ideally the the user should be empowered enough to make these changes if they're small enough themselves. So for for for Domino's, that's exactly what we did. The agent now runs on their schedule either multi um daily or even by email trigger manually. Analysts review only the exceptions at this point. Each correction that they catch, they're automatically able to add as a benchmark case. If they can't, then they obviously they're always available for them. And we are now at a place where we are expanding with them. Um trying to get it into multiple markets and multiple other um areas. So yeah, this is basically how we we used um our framework to work with

**[12:59](https://www.youtube.com/watch?v=4VmugsE-iP0&t=779s)** Domino's to go from an agent that barely works to an agent that works almost perfectly while reducing the cost. We found this framework to be very effective for various other use cases, especially where you have messy sources of data where you're trying to figure out the right answer. And um thanks.
