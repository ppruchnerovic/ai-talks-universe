---
id: 3u3cECUbPu4
title: "Lightning Talk: AI as the Attack: Weaponizing APIs"
slug: lightning-talk-ai-as-the-attack-weaponizing-apis
conference: sans-ai-summit
conference_name: "SANS AI Cybersecurity Summit"
category: "AI security"
edition: "AI Cybersecurity Summit 2026"
year: 2026
speakers: []
channel: "SANS Institute"
duration_min: 6
published_at: 2026-05-04T18:54:39Z
video_id: 3u3cECUbPu4
url: https://www.youtube.com/watch?v=3u3cECUbPu4
youtube_url: https://www.youtube.com/watch?v=3u3cECUbPu4
tags: ["sans institute", "information security", "cyber security", "cybersecurity", "information security training", "cybersecurity training", "cyber security training"]
transcript: true
---

# Lightning Talk: AI as the Attack: Weaponizing APIs

**Speaker not identified**

`SANS AI Cybersecurity Summit` · `AI Cybersecurity Summit 2026` · `2026` · `6 min`

`#sans institute` `#information security` `#cyber security` `#cybersecurity` `#information security training` `#cybersecurity training` `#cyber security training`

[Watch the recording](https://www.youtube.com/watch?v=3u3cECUbPu4) · [Conference site](https://www.sans.org/cyber-security-summit/)

## Description

When AI Becomes the Attack: How Threat Actors Weaponize AI APIs to Hide Their Tracks

🎙️ Bryant Pickford, Security Specialist Solutions Architect, AWS
📍 Presented at SANS AI Cybersecurity Summit 2026

Problem → risk → action structure:

Problem: Threat actors exploit AI APIs to generate overwhelming traffic that appears legitimate

Risk: Traditional defenses can't distinguish between legitimate AI crawlers and weaponized ones

Action: A 3-step detection framework attendees can implement immediately

Explore upcoming SANS Summits to continue learning from leading voices in cybersecurity: https://go.sans.org/summits

## Transcript

*1,110 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=3u3cECUbPu4&t=0s)** Hello, my name is Bryant Pickford. I'm a security specialist solutions architect at Amazon Web Services and we're here to talk about how threat actors are weaponizing AI APIs to basically hide their tracks, right? Now, I kind of want to start with just an image, right? There's an inherent trust that we have when it comes to infrastructure. Now, this can be infrastructure that we have on the cloud, on prem, hybrid, you know, the tools we use, the software we use, right? Anything really, we have an inherent level of trust with it. And this is actually being used against us at this exact moment. Now, in the last year of my own research, I've noticed that there's been an alarming increase in DDoS attacks that are heading not only my customers, but the infrastructures of companies I use every day, you know, across the board. And

**[0:49](https://www.youtube.com/watch?v=3u3cECUbPu4&t=49s)** what that really is coming from and stemming from is this sort of weaponization of AI against us. Now, there has been some level of research on this already. You can kind of see here on the slides, but the one thing I do want to sort of state for the matter is that this is something that is kind of being thrown under the rug, right? Now, from a standpoint of, well, why should I care? You know, what does this matter to me, right? Well, for one, AI is being utilized in such a way that it's kind of being used to hurt us when we're not really looking, right? We can talk about usage, visibility into who's using AI APIs, stuff like that, but the real reality of it is that it's actually being used to basically crawl into greater number of websites, right? Now, we can definitely bring that into an infrastructure problem, a conversation, right? But the scale is actually pretty

**[1:37](https://www.youtube.com/watch?v=3u3cECUbPu4&t=97s)** staggering. Now, going into, well, isn't this just another botnet, Bryant? Like, isn't this just the same as everything before? Isn't this the same thing as like, you know, Kim Wolf, right? Or RSU, any other botnets that are kind of just destroying our web applications? Well, in reality, this is actually an inherently trusted IP space, right? We inherently trust Anthropic, OpenAI. We trust all these AI companies to be able to self-regulate themselves and rate limit themselves, right? Without understanding that if I go tell my AI right now to go scrape some site to understand some more, I can create a thousand, 10,000, million processes to go do that and inadvertently destroy that website's website's performance. Now, going a little bit more into what that attack looks like from a

**[2:25](https://www.youtube.com/watch?v=3u3cECUbPu4&t=145s)** perspective, right? Well, hackers traditionally speaking could use botnets. Back when I was younger, I would always hear about like low orbit ion cannon being utilized to like destroy websites for schools. But the attack chain has kind of been simplified here nowadays, right? We can talk about what's been happening over the news with supply chain attacks, right? APIs just being sort of exposed, but this isn't a type of attack chain that can really only be utilized in a very small manner by little to no nothing of of sort of resources, right? So, one API can actually increase and create a massive DDoS event not only to our own infrastructure, but to the actual resources that we're actually using there. And lastly, right? One of the things I do want to sort of pitch of what's the

**[3:12](https://www.youtube.com/watch?v=3u3cECUbPu4&t=192s)** takeaway for this, how do we sort of understand this a little bit better is we need to understand our own patterns, right? When I talk to customers, when I talk to teams, we traditionally start with, well, what's your baseline? What is it that you normally see day-to-day, right? If there is no monitoring, how do we sort of detect this, right? What is the sort of guardrails we can put into place not only to protect ourselves, the APIs we use, but also from the external threat, right? If this is used against us, we need to be able to understand exactly what that's looking like from a layer three, four, or even seven. Now, when we're talking about this, right? You might also ask, well, Bryant, you know, what exactly is this? I I still can't understand, you know, why can't we just block all of this, right? If this is coming from an AI of some sort, you know, do we have crawlers? And the real answer is a lot of businesses

**[4:00](https://www.youtube.com/watch?v=3u3cECUbPu4&t=240s)** do not have actual visibility into what crawlers are actually accessing, connecting, communicating, and scraping their sites, right? Now, going into the actual solution, right, is more looking into it from an adaptive throttling perspective, right? We have already the tools, we have the mechanisms to have visibility across every single layer. The only thing we have to do is understand from a corporate perspective, from a team perspective, from a top-down or up-down, is do we want to allow this, right? Do we actually need AI to actually scrape our websites? Do we actually need AI to be able to communicate, interact in a way that is, you know, without any restrictions? And how do we sort of throttle it, rate limit to a way that we're still able to continue doing our business, we're still able to provide access to our legitimate users, um and

**[4:49](https://www.youtube.com/watch?v=3u3cECUbPu4&t=289s)** we're still able to still have visibility in whether we want to make revisit this conversation communication later down the road, right? And just to kind of leave you with a bit of an image, right, this would be like if you walk into your apartment and there's a random person in there making pancakes, and you're just like, "Who are you and where did you even get this pancake batter from?" And they're just like, "Oh yeah, I took it from your neighbor." Oh yeah, by the way, I also trashed this place. Right? So, it's one of those things of like, how [snorts] do we look into what our APIs are utilizing, but also on the other side, the other customer, the other company that's also on the far side of it, that's also being impacted by this, how do we also help them? And I kind of leave you with this. If anyone wants to communicate and connect, um there's a lot of research I've been doing in the last year around this. If you want to connect and communicate on that, I would love to hear you. Um

**[5:38](https://www.youtube.com/watch?v=3u3cECUbPu4&t=338s)** thanks again. Hope to hear you soon.
