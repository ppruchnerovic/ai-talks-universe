---
id: jfTltMo0TMg
title: "Meta, Stanford & Odevo on Agentic Coding at Scale"
slug: meta-stanford-odevo-on-agentic-coding-at-scale
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-09-09T16:00:37Z
video_id: jfTltMo0TMg
url: https://www.youtube.com/watch?v=jfTltMo0TMg
youtube_url: https://www.youtube.com/watch?v=jfTltMo0TMg
tags: []
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration"]
transcript: true
---

# Meta, Stanford & Odevo on Agentic Coding at Scale

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=jfTltMo0TMg) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Rolling out agentic coding to one team is a tooling problem. Rolling it out to five hundred engineers is a completely different problem, with a completely different set of ways to get it wrong. Four speakers at AI DevCon London whose job is getting other engineers using these tools on what actually moved the numbers.

Ian Thomas (Meta) grew an organic community 40 times over and took weekly usage from under half to above 80%, with no mandate involved. Rob Willoughby (Tessl) and Simon Obstbaum (Stanford) have been measuring across 150,000 engineers and are seeing the widest performance spread they have ever recorded — Simon set out to disprove the 10x engineer and now thinks he's watching one appear. Daniel Jones (Resync) and Tomasz Maj (Odevo) open with a warning from the 2025 DORA report: point agents at an organization that already ships badly and things get worse, not faster. And Hannah Foxwell on the part that gets the least airtime — on-call rotas, error budgets, and career planning for the skills teams need today rather than yesterday.

What we cover:
– How Meta moved from ad hoc AI use to 80%+ weekly adoption without mandating it
– What 150,000 engineers show about the performance spread agentic coding creates
– Why the 2025 DORA finding says agents make weak delivery worse, not better
– The fundamentals to fix first: CI/CD, a platform, tests, coding standards
– Career planning and sustainable on-call for the skills teams actually need now

Chapters:
00:00:00 - Introduction
00:00:26 - Ian Thomas, Meta: operational load and slow adoption
00:01:39 - 40x community growth and 80%+ weekly usage
00:02:30 - Rob Willoughby and Simon Obstbaum: 150,000 engineers measured
00:02:47 - The 10x engineer he set out to disprove
00:03:34 - How the performance spread is shifting
00:05:00 - Daniel Jones and Tomasz Maj: starting with discovery
00:05:16 - The 2025 DORA warning about agentic coding
00:06:26 - CI/CD, platforms, tests and coding standards first
00:07:24 - Hannah Foxwell: careers, on-call and the broken comb

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

What actually shifted adoption on your team — tooling, training, or someone senior going first? Tell us in the comments.

## Transcript

*1,663 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=jfTltMo0TMg&t=0s)** Back in June at AI DevCon in London, we heard from several people whose job is not to use these tools, but to get other engineers using them, which turns out to be a completely different problem with a completely different set of ways to get it wrong. Let's first hear from Ian Thomas at Meta, who took a community from heel dragging and ad hoc usage to 40 times the size, with weekly usage above 80%. Yes. Hi. I'm Ian. I am a software engineer based in the UK. I work remotely from Yorkshire, which is a wonderful juxtaposition to working on VR and and metaverse products. Lots of people were working on operational work. They had lots of on-call overhead, bugs coming in, front and center, things that everyone has to deal with in their day to day work, and it takes up a significant amount of your capacity.

**[0:53](https://www.youtube.com/watch?v=jfTltMo0TMg&t=53s)** We're also trying to build this culture of AI adoption, and we knew that AI tooling was going to be important, and it was going to be the way that engineering evolved. But what we were finding was there was a bit of heel-dragging going on, and the adoption wasn't uniform. It was, it was ad hoc at best. People were finding low quality outcomes. They were dragging. They were trying to use the wrong tools for the wrong problem. They didn't always have the same processes. And where there was success, it was kind of kept in a fairly small area of knowledge, siloed information within their teams, and there wasn't a great deal of value being perceived. People weren't seeing the return on their investment in time. So we were seeing this was going to be quite a difficult problem for us to bridge. And to fast forward you to the end.

**[1:41](https://www.youtube.com/watch?v=jfTltMo0TMg&t=101s)** What we did achieve in the end with this, with this work that I was part of, we grew an organic community that was over 40 times bigger than when we started. I think at the time when I stopped working on this, we were well over 500 people and that was at the start of this year in January, well over 80% of people were using these tools weekly, which was up from under half. And I would say consistently now, I think I see this in the mid to high 90s. So we're really high up in the adoption curve now. And for certain workflows we're seeing significant time gains. We built a maturity model that I'm going to share with you later today. And there were patterns that we invested in. And we found through experiments that we then started to spread throughout the company. And it became a pattern that was used widely, not just in these small, siloed groups of success.

**[2:30](https://www.youtube.com/watch?v=jfTltMo0TMg&t=150s)** We also heard from Rob Willoughby and Simon of the Stanford QA lab, who have been studying this across 150,000 engineers. They're seeing the widest performance spread they've ever measured. Simon set out to disprove the 10x engineer. He now thinks he's watching one appear. It's a significant difference. It's the biggest difference that we've ever seen to be honest I started this study in 2020. That's going to be, you know, thought about how do we measure productivity. For me, I had worked in Silicon Valley, and the 10x engineer was something that I really liked, to a certain extent, and I wanted to show that it doesn't exist and it didn't exist.

**[3:19](https://www.youtube.com/watch?v=jfTltMo0TMg&t=199s)** But over time, we're starting to see it now. So people that know how to create agents, people that know how to work, they they achieve significantly better outcomes. Now. On top of that, and I think this is a really interesting slide in terms of how performance is shifting. So once here is the top and the bottom again. And we saw a pretty high rank ability direct. The pivoted was 0.70. Yeah. And policy it dropped to 0.45. So we believe also like that the tactics that anybody looking to get to perform

**[4:13](https://www.youtube.com/watch?v=jfTltMo0TMg&t=253s)** no longer enabling you to get top performer today. So what we believe is what happens to be honest, a lot of other people from the the top performers, they moved to the top performance. One hypothesis is that like these were people that were coding would be using the teams. And now in terms of how maybe some of that automated, some that have got 15 way, and now they became the top performers. So arguably that's the hypothesis is right. I don't understand why, but we observed that it happens. They were busy helping others deliver something delivered good outcomes. But now they have time and they're killing it. Daniel Jones and Tomasz Maj ran an AI training program across

**[5:04](https://www.youtube.com/watch?v=jfTltMo0TMg&t=304s)** an entire enterprise. And their starting point is a warning. If you are not already good at shipping software, pointing agents at the problem doesn't help. It makes it worse. The first thing that we did is a process called discovery. thing that we did is a process called discovery. So for folks who aren't consultants, this is where you go into an organization and you figure out what's the current lay of the land. And this is a really important thing to do because of this very authentic DORA report quote, might be. But in the 2025 DORA report, there were a couple. There was one that was, I think, August-ish. It made the point, after looking at a couple of thousand companies that if you are not doing software development well at the moment and you throw agentic coding at the problem, things are going to get worse.

**[5:55](https://www.youtube.com/watch?v=jfTltMo0TMg&t=355s)** You're optimizing a system, you're making one part of an interconnected system go really fast. You will expose bottlenecks elsewhere. If you're doing software delivery well and you start adopting agentic coding, then things will go much faster and you'll be on a hockey stick of like exponential performance. The tricky part is that nobody knows where this balance point is. Like how crap do you have to be? Is it, how bad at software development do you have to be to go slower? Like, are you in a good place or not? And as an industry, we haven't quite figured that out, but the kind of things that we needed to look at across the various different teams and cultures at Odevo were things like CI/CD. Do you have a platform? This is a current bugbear of mine with I shouldn't tell too many tangents about other customers,

**[6:44](https://www.youtube.com/watch?v=jfTltMo0TMg&t=404s)** but if you don't have a platform like you can't ship code reliably and quickly, and then you're just going to generate all this code and have no where to go with it. Do you have tests? If agents can't run tests to find out they've broken your software, don't be surprised when they break your software. If you don't have coding standards. If the humans in your organization don't agree what good looks like, then there's a very low chance that an agent is going to be able to produce code that your team is going to approve of. So there are lots of things that are worth looking at. And the optimist in me likes to think that maybe this is another opportunity as an industry, that we get to look at those fundamentals and go, look, we really need to improve these. And to close, Hannah Foxwell on the part that gets the least airtime. Careers that make sense for the skills we actually need. Now, her three anchors are: build something worth building,

**[7:36](https://www.youtube.com/watch?v=jfTltMo0TMg&t=456s)** Speed requires safety and people matter. People matter. Like, I want to make sure that every engineer has a sustainable on-call rota. I want to make sure that we have a language to discuss, like our error budgets and our availability targets, and invest appropriately. And I want to do realistic career planning for the skills that we need today, not the skills that we needed yesterday. I am trashing heavy planning processes. Two-week sprints are absolutely too long right now, and mandatory code reviews feels like an unsustainable practice that's going to need to be replaced with some other ways of assuring quality. I'm definitely shifting left on peer review using spec-driven development, and I'm going to encourage all of you in this room, and especially the managers,

**[8:25](https://www.youtube.com/watch?v=jfTltMo0TMg&t=505s)** to think about how we create people who are less T-shaped and more of a broken comb, people with diverse areas of depth, because those are the sort of people who are going to thrive in this new age. We are all on a journey and we do not know where we're heading, and I find it exciting, but it can also be daunting. And so as you leave here, hopefully I've given you some ideas to experiment with or to help you address some of the new challenges. I would just urge all of you to experiment with empathy because it is not an easy thing to change, to change your discipline so fundamentally and at such speed. So yes, we do need to try new things. We need to share our learning, but do it with people.

**[9:16](https://www.youtube.com/watch?v=jfTltMo0TMg&t=556s)** Don't do it to them. And so here are the things that I'm keeping. No matter what, no matter how good agents become, I'm always going to build an organization that focuses on the user. Build something worth building. Solve a real problem. I'm going to be investing in ways that we can move safely with speed. And I'm going to always, always focus on the people because people matter and we need to create teams that are joyful to work in and careers that are worth pursuing. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit AI DevCon to learn more and book your ticket.
