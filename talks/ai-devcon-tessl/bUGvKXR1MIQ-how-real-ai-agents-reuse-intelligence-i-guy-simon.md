---
id: bUGvKXR1MIQ
title: "How Real AI Agents Reuse Intelligence I Guy & Simon"
slug: how-real-ai-agents-reuse-intelligence-i-guy-simon
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 6
published_at: 2026-02-15T15:01:04Z
video_id: bUGvKXR1MIQ
url: https://www.youtube.com/watch?v=bUGvKXR1MIQ
youtube_url: https://www.youtube.com/watch?v=bUGvKXR1MIQ
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# How Real AI Agents Reuse Intelligence I Guy & Simon

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=bUGvKXR1MIQ) · [Conference site](https://tessl.io/devcon/)

## Description

Your skills work in testing but break in production. Or they work with Sonnet but fail with Haiku.

Guy and Simon explain why: different models interpret the same skill completely differently. Opus refuses instructions; Haiku needs more hand-holding. Getting this right matters.

There are three types of context for agents:
1. Skills: Go in the context window. Load 1000 of them, and your agent dies.
2. Docs: Loaded only when needed. Zero performance cost. Scale infinitely.
3. Rules: breadcrumbs that tell your agent when to invoke a skill or consult a directory.

Most teams copy-paste skills everywhere. Guy breaks down why that's technical debt and what production skills are actually needed.

Full episode: https://youtu.be/ntkM-hRblfo

## Transcript

*1,293 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=bUGvKXR1MIQ&t=0s)** We need to remember that agents eventually still remain just interfaces to the LLMs. So every time there's a request to the LLM and the question is what is the data right? Though all of these different means of context engineering they're just about giving the right path to choosing the right words to include in the message. Uh and you can easily put too many things into the context window that the actual instruction gets lost. There are rules which you kind of shove it into the context window whether you like it or not. Right? uh you would put it into that claude MD or a must use rule in cursor. Those are mandated but they take up context window space. Then you've got skills. [music] Skills include like cursor rules uh basically a tiny rule like a little bit

**[0:48](https://www.youtube.com/watch?v=bUGvKXR1MIQ&t=48s)** of data that goes into the context window for the agent to choose to invoke a skill implicitly. can choose to call a skill actively like a command uh in which case you don't need those things there but you can also uh uh uh you expect the agent to invoke the skill at the relevant time. So you have to put a little bit of that breadcrumb in the window. There's some development right now but maybe separating that out with in the agents. Does it go and consult some directory for now that's the reality and then you've got docs. Docs are uh just available information for the agent to find uh but they're not naturally findable for the agent and so you need to either leave a breadcrumb somewhere like with a rule uh or you just need to name them in a way that allows for uh you know gps and sort of other agentic search to find them. Uh but they purely loaded on demand and

**[1:36](https://www.youtube.com/watch?v=bUGvKXR1MIQ&t=96s)** they don't have any price to pay. So you can have as many docs as you want. If you have a thousand skills loaded you might really your agent today. Uh but if you have a thousand docs, they're just available. It's more about which docs that is load at the right time and can it actually find them. And it's a good time to remember as well that while it's a standard format, they are not standard models. Uh and so the same instruction in the skill text right now would be loaded by different agents by different models. Uh although we know in like for a fact we have like repeating data to show that the same wards would not trigger you know haiku and set and opus to the same action. You know opus is much more of a kind of smartass, right? and sort of can can choose to say no I know better and won't do it you know how might I sort of need more sort of detailed instructions and so at the moment skills don't really solve for that they are one standard unit of context but it's not sure that

**[2:26](https://www.youtube.com/watch?v=bUGvKXR1MIQ&t=146s)** the same words will affect uh will be the optimal ones for different agents so so I'd sort of say you know think of skills as an amazing new capability it is absolutely worth leaning into we're doing that in Tesla we think they're amazing they are maybe the most sort of standard way right now to reuse use context, but like MCP, I think they're also a piece of the puzzle and there will be all sorts of of sort of tools or just sort of helpers that we would want to reuse for making agents successful. >> That's really interesting. So, so essentially the standard allows it provides a kind of standard bolt fitting in the sense that you can integrate it with the agents but your mileage may vary depending on which agent you use because it will use it'll it'll assess the wording and it'll it'll use them uh differently depending on how of course they are implemented in the background.

**[3:13](https://www.youtube.com/watch?v=bUGvKXR1MIQ&t=193s)** So that's that's a that's a good insight as well. >> Okay. So skills uh we can use them as indie developers, as hobbyists, as open source developers. Uh we can also use it as in an organization uh to describe how we want to do certain things in in our certain methodologies and our certain processes that are key to our organizational uh requirements. Now when we think about adding skills as a first class citizen into our into our organizational process, our development process, um what do we need to consider when building owning those skills and actually distributing it and expecting other you know professional developers in our organization to to to make the best use of that? What do we need to consider? >> Yeah. So I think it's a good question and I think kind of allure of uh of skills is that they they have this

**[4:00](https://www.youtube.com/watch?v=bUGvKXR1MIQ&t=240s)** immediate impact on it. you create some static markdown file, you do it with a create skill, very very low lift. Uh, and it helps like right now you immediately can anecdotally see that it works. But I think just like with software, there are differences between kind of a one-time it worked and therefore it's awesome uh and something that is a sort of longived uh assets that you now need to live with. These are competencies that you want to reuse across the team. So I think to to kind of take skills to a professional level, to a team level, to an organization level, uh you're you're better served by thinking of skills not as a markdown file, but as a unit of software. This is a a competency, a reusable competency that you want the agent to have. Um so this this sort of puts a a different lens on on what are the tools that you need to be able to own skills, right?

**[4:48](https://www.youtube.com/watch?v=bUGvKXR1MIQ&t=288s)** And to to be able to operate them and collaborate them on them over time. Um there are probably many things to handle but I'd say the three to focus on is one you need to be able to test skills just like software you know you if you want it to remain working or even just sort of assess whether it works today you have to think about what's correct and then test or in the world of AI evaluate uh against those two is uh really thinking about how do you distribute that software we can talk about this more but at the moment there's a >> uh kind of easy but you know sad reality that people are copying skills all over. They're designed to be reusable and yet we kind of copy and duplicate and copy everywhere. We've seen that movie. We know where that ends. So that's not awesome. Uh and then the third is you have to think about how do you own them long term. You know they will fall out of date just like any docs or anything

**[5:36](https://www.youtube.com/watch?v=bUGvKXR1MIQ&t=336s)** like that. They uh the models will change and so you know a new model will come along it will think it's very smart right or you would want to use it with some sort of cheap model or open model. Um and so uh we have to we have to think about how do we how do we maintain those skills? How do we keep them up to date? How do we uh allow a team to collaborate when the person that wrote them leaves the organization? And so the kind of the whole life cycle management of it. I think those are the core ones to think of.
