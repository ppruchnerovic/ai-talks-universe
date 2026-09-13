---
id: z4-_eCPNGlI
title: "Using Agents to Curate the Content You See Online - Dan Gish"
slug: using-agents-to-curate-the-content-you-see-online-dan-gish
conference: wearedevelopers
conference_name: "WeAreDevelopers World Congress"
category: "General software conferences"
edition: "WeAreDevelopers"
year: 2026
speakers: ["Dan Gish"]
channel: "WeAreDevelopers"
duration_min: 13
published_at: 2026-09-09T10:01:38Z
video_id: z4-_eCPNGlI
url: https://www.youtube.com/watch?v=z4-_eCPNGlI
youtube_url: https://www.youtube.com/watch?v=z4-_eCPNGlI
tags: ["conference", "congress", "Europe", "tech", "technology", "IT", "people", "code", "future", "coding", "programming", "programmer", "software", "engineer", "developer", "developing", "WeAreDevs", "WeAreDevelopers", "wearedevelopers", "wearedevs", "wearedeveloperslive", "tech talks"]
topics: ["Agents & orchestration"]
transcript: true
---

# Using Agents to Curate the Content You See Online - Dan Gish

**Dan Gish**

`WeAreDevelopers World Congress` · `WeAreDevelopers` · `2026` · `13 min`

`#conference` `#congress` `#Europe` `#tech` `#technology` `#IT` `#people` `#code` `#future` `#coding` `#programming` `#programmer` `#software` `#engineer` `#developer` `#developing` `#WeAreDevs` `#WeAreDevelopers` `#wearedevelopers` `#wearedevs` `#wearedeveloperslive` `#tech talks`

[Watch the recording](https://www.youtube.com/watch?v=z4-_eCPNGlI) · [Conference site](https://www.wearedevelopers.com/en)

## Description

Join us for a coffee chat with Dan Gish at AgentCon! Discover how EvoGENT lets you control your social media experience. Share your thoughts in the comments!

00:00 Introduction
00:49 EvoGENT Explained
01:38 Personalization Features
02:33 Platform Compatibility
04:17 Project Inspiration
06:38 Tech Architecture
08:36 Open Source Concerns
11:01 Deployment Options
12:17 Event Impressions
12:32 Conclusion
-----------------
WeAreDevelopers is the global platform for developers and AI professionals to grow, connect, and lead in the age of AI. Millions of professionals use our year-round platform to build skills, explore thousands of hours of expert content, find career opportunities, and engage with a community that shares knowledge at scale. Companies partner with us to reach developers authentically, strengthening their employer brand, engaging top talent, and showcasing their products to a global network. Our flagship events in Europe, North America, and India bring together the world’s leading engineers, tech leaders, and companies. Together, we are driving the innovations that define the next era of technology.
Head to worldcongress.dev and wearedevelopers.us to secure 10% with the code "wearedevs_yt"
-----------------

## Transcript

*2,284 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=2s)** Hello and welcome to another coffee with developers. We're live at Asian Con in in the Silicon Valley. And we just had a chat and this person came up to us and he had some really interesting ideas. So Dan Gish, what is Evogen and who are you? >> Evogen is a personal agent that browses your social media for you and puts you back in the control over what you're looking at. So instead of looking at what Elon wants you to see or Mark Zuckerberg wants you to see or whatever makes these companies the most money um it allows you to run your own algorithm on this um curate it how how you want to see. Um so it still allows you to stay connected with these social media services like Twitter is something that I find really

**[0:51](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=51s)** valuable. Um I there's interactions and information that I find on Twitter that it's just you you can't replace it, but you got to filter through like 98% of propaganda and AI slop and all that kind of stuff to get there. It's so this is this is having your own personal AI agents run by Claude code or Codex or whatever you want to do all that filtering for you and just giving you exactly what you want to see. >> So it's kind of missing it's the missing filter feature of these tools and instead of just having to filter each tool you can just connect to any any of them and basically say like here's the things I really don't want to have. So how do you do it? Do you do like a blacklist or a whitelist? Like what

**[1:39](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=99s)** what's the what's the idea of it? >> It it it it's super flexible and it it'll do it however you want and in fact it'll evolve with you. So you can just set it up where you can just import say your um your Twitter preferences um and it'll just figure everything out from from that. It can see what your likes are and who you've interacted with and kind of set up your curation like that. Or it could be um just something that you explicitly say that I don't want propaganda. I I want to look at healthy content or I do want propaganda, but I want it to be like my kind of propaganda. Um

**[2:25](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=145s)** >> So the the Which services I guess it's completely open. I mean you can you could connect to X, you could connect to Facebook, you can connect to Instagram. It's kind of the same. And Blue Sky and like Doesn't that Is that a bit playing catch-up for you to actually Cuz all of these systems don't want agents to do that exactly because they want to give you the curated timelines. >> Absolutely. >> Like is that playing whack-a-mole with those services or is it something that that is not as bad as I as I consider it to be? >> Huh. It it it it could turn into a game of whack-a-mole. Um These These agents are smart and they can figure things out and they're browsing these websites basically as a normal user. Um and so

**[3:13](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=193s)** they they it'll adapt over time. Um they had the the the framework is set up so that if it detects that Twitter has changed around how its feed is structured or whatever, it'll it'll adapt over time. Um and that's the whole idea behind it is that um uh you can point it at whatever source that you want and it'll over time figure out the the the best fastest way to to to to browse that and get it into your own So how do you control >> How do you consume it? Like what's So, uh I mean the front end you showed me is a React app, but also is there other ways to integrate it into the desktop? It's like if I want to style it for myself, if I want to find a way of doing it.

**[4:00](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=240s)** >> Sure. >> So, how do I do that? >> Yeah, I mean, it's an open-source app, so you can you can point your own coding agent at the React app, and you can style it however you want. Um we encourage that. Um you're you're in complete control over it. >> So, what's your what's your your push for it? Like, why did why did you do it? I mean, this is something that's a lot of effort. Uh and you're not making any money with it, obviously. Uh and you've said you worked on it for like 2 to 3 months right now. Like, where do you see this going? Like, is it just something that was a your own itch that you had to scratch, or >> Yeah, I mean, I I I think it just started out of boredom. I was just bored of looking at AI slop and the whatever propaganda was getting pushed to me in in my social media, and I just started

**[4:50](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=290s)** messing around with having my own personal agent kind of find the most interesting content on there, and it started to work well, so I started to think about like how could this be made in a more generalized kind of way where other people could could use it. Um >> It could be a It could be a list of presets where I say like, "Hey, this worked for another person to filter out that kind of content." I can see in the future like a a dashboard of like filter options. I used to work on Yahoo Pipes, and that was just great cuz you had these connections, and then you got the final data out. And I think something like that would be interesting in the near future to make it less make it a personal thing, but also say like, "Hey, I curated or helped actually make this thing less annoying for everybody else out there, counteracting the traffic that is generated by AI slop

**[5:38](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=338s)** that we have at the moment." >> 100% like that's one of my first kind of inspirations behind this is that there there's there could and should be a way for you to share these curation algorithms. So, like these should be able to evolve both with you and and I should be able to share kind of the best curation practices that I have with you. The There should like if there was a community that arose around this where everyone can kind of share the best ways that work for them. Um and maybe the best ways even to get around like if if these companies do try to um play Whac-A-Mole. Um the the the the best practices to keep us all in full control over over

**[6:26](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=386s)** what we're looking at. >> I mean, it feels like RSS collections like OPML files that you sent to each other in the past or things like what was the Mastodon like follow group kind of things. So, this feels like a really interesting idea. In terms of In terms of like having written it, you do you What what is the architecture of the thing itself? Like I mean And as it's open source, where do you want contributors to? >> Yeah. Um Well, the the design philosophy behind this is that I I try to put as much of it into the agents as possible so that it stays flexible and evolving. I I try to evolve I try to avoid um

**[7:13](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=433s)** a huge amount of like deterministic kind of slop. So, on the on the back end there's kind of a pipeline of agents that uh will will browse your various sources. So, that that's kind of one step in the pipeline. And then you have And and we'll use kind of uh cheaper, faster agents to do that. And then you have a a curation agent kind of a middle step in the pipeline, where maybe you want to use a uh a smarter like the the the latest cutting-edge Opus 4.7 agent to do the actual curation, and then we have like a enrichment agent kind of further down the pipeline that will curate the the comments and

**[8:02](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=482s)** replies to the to the to the content that that's in your feed, so that instead of like I I see this on Twitter all the time, where I see like a really interesting post, and then I click on it, and I'm like, "Woah, like the the replies are just horrendous. It's AI slop, and it's the the worst possible thing." And so, I I I really enjoy having this kind of final stage of the pipeline, where it's curating the replies and comments as well, so the the entire thing is everything that you want to see. >> One thing that always annoys me about like being in that open-source and in that that that technology space is like the adoption is harder for people, because I mean, we we chatted about earlier. I

**[8:49](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=529s)** talked about how I like Mastodon, and I was how I realized Mastodon will never be for the mainstream, because it's it's too vague to be defined. It's really hard to use. And I I had people on the podcast with that work for Mastodon, and like they're like, "Yeah, we understand. We're trying to make it that way." This feels also a lot of effort to actually start using it. Is it just that you install the app, and you start doing it, or cost the the cost of the effort to start filtering things? A lot of people shy away from that. So, is it is there like a gamification moment, where you get the agent to actually reward you for doing it? >> Well, I I I think that the magic of this moment in time with technology is that like

**[9:35](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=575s)** like I I I I just literally went public with the Git GitHub repo today. And in instead of having like complicated instructions of what to follow, I I'm literally just giving you a a a blob of um instructions for your coding agent on how to install this app. So, you literally just copy and paste the instructions from the GitHub repo into your favorite coding agent, and it's going to walk through everything for you. It It's going to It is a complicated setup process, but your agent can do it all for you. >> Mhm. >> Um >> And what are the dependencies on you? Like, is it Is it something that can run completely locally on my machine, or are there any cloud dependencies, any

**[10:24](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=624s)** licensing dependencies? >> No. Uh you you can run it however you want. Um you can run it on your local machine if you have um if you have a Mac at home that's always online, that could be a good way to go. Um I personally install it on a a cheap VM on a Hetzner VM in the cloud, and that allows me to just install a progressive web app on my phone. Um so, it it seems just like a normal app on my phone. Um it's it's running off of my own VM in the cloud, so you can set it up however you want, really. >> Cool. Yeah, that I mean, seeing that you can run on a VM in the cloud would be interesting to offer it as a Docker image so people can just use it themselves. >> 100%. Yeah. Um again, I have instructions for your coding agent on

**[11:14](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=674s)** the GitHub that'll set up a Hetzner VM in the cloud, do all this stuff for you. So, it's literally just like a one-click kind of thing, but yeah, we we could also we could also have a an image or whatever that you can install, as well. >> I I love uh hearing Hetzner. I mean, first of all, they're one of our They're one of our our partners for our event as well. But, growing up in Germany and being on the forefront at the very early beginnings of the internet, I had a server on Hetzner, and that was basically when something was broken, I picked up the phone and called Mr. Hetzner. That was like one of like 60 people on that server back then. >> [laughter] >> I don't know. It's like I haven't followed that up since, but I found a server that I had in 1996 that is still running, and I've really forgot about

**[12:00](https://www.youtube.com/watch?v=z4-_eCPNGlI&t=720s)** it. Like, sometimes it's amazing how much detritus you left you leave on the internet without knowing, but So, yeah, it's it's an interesting thing to get to meet you. I mean, how was your impression so far of the event? Like, did you get to know a few people? Have you seen a few talks that inspired you? >> Uh I I kind of showed up late here. Um was in a talk or two and decided to come out for coffee and met you fine folks. So, I guess it's off to a good start here. >> Excellent. >> [laughter] >> Well, thanks very much. This was uh Dan Gish. This was Coffee with Developers Live here. People are queuing up for food, so it's getting noisy, so we might as well pack it in and release this soon. Thanks very much for this. >> Yeah, nice to meet you, Chris. Nice to meet you, too.
