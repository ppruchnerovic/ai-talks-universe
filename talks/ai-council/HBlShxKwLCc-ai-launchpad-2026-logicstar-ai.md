---
id: HBlShxKwLCc
title: "AI Launchpad 2026: LogicStar AI"
slug: ai-launchpad-2026-logicstar-ai
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 9
published_at: 2026-06-23T22:57:04Z
video_id: HBlShxKwLCc
url: https://www.youtube.com/watch?v=HBlShxKwLCc
youtube_url: https://www.youtube.com/watch?v=HBlShxKwLCc
tags: ["AI"]
transcript: true
---

# AI Launchpad 2026: LogicStar AI

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `9 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=HBlShxKwLCc) · [Conference site](https://www.aicouncil.com/)

## Description

LogicStar finds, investigates, and resolves code issues that matter before they become incidents

SPEAKER:
Mark Niklas Mueller - Co-founder & CTO, LogicStar AI

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*1,620 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=HBlShxKwLCc&t=0s)** Yes, I mark everyone. Let's start with a quick show of hands to get you energized. Who would rather be fixing a PagerDuty right now than sitting here and enjoying some drinks? That's not a lot of hands. That's what I thought. So, to keep it like that, you might want to use predictive maintenance for your software. And that is we find and resolve issues before they turn into incidents. And what we see is that this problem has actually exacerbated a lot with the recent deployment of AI tools for coding. Quick show of hands again, maybe we start with more engagement. Who uses AI tools to ship code? Yeah, that's that's more like it. Almost everyone. And who has actually seen a reduced rate of incidents and other outages since doing that? That's again no hands at all. And this is also what we actually see in the

**[0:46](https://www.youtube.com/watch?v=HBlShxKwLCc&t=46s)** data. We get much faster task completion, twice as many PRs as we used to, but at the same time the incident rate per PR has more than tripled, and there are 50% more bugs per developer. And so, while engineering is definitely getting faster, it's very questionable if it's better. And we call this the maintenance trap. And why do we see this problem? We believe current tools are simply reactive. Code agents implement features when you tell them to, they investigate issues after you assign them to them, and they fix bugs once you point them to them. And even AI SREs only become active after an incident has started and two alerts have triggered. But at this point your customers are already suffering. So, we asked ourselves, can

**[1:35](https://www.youtube.com/watch?v=HBlShxKwLCc&t=95s)** we proactively find the issues that are relevant to address right now at any given time to avoid such incidents from happening? And I wouldn't be standing here if the answer wouldn't be yes. So, what we do is we predict and resolve tomorrow's issues today. And the good news is that the signals that you need to predict what issues will become incidents are actually in your data already. You don't need to gather more data. 92% of all incidents have early warning signs that were simply ignored because they got lost in the noise. And we connect all of these warning signs to your code base and make them work for you. So, let's look at what this might look like for a given incident. >> [cough and clears throat] >> Here we see the number of affected users over time.

**[2:23](https://www.youtube.com/watch?v=HBlShxKwLCc&t=143s)** And after we originally ship a bug, there we detect the we detect the underlying issue if you use Logic Star, but we don't act on it yet because there's lots and lots of issues in your code base and you might not care about introducing change to resolve any and each of them. So, once we see the first signals in your observability data that this is actually hitting users in production, we start the investigation process and propose a fix and let you know the fix is ready and you can just go ahead and merge it right away. At this point, you will not even have reached the alert thresholds and you won't even notice that an incident would have happened otherwise. In the world without Logic Star, if you follow the blue line, you don't know anything about the incident, you don't know anything about the errors until you actually hit the alert thresholds and the errors start piling up and your

**[3:10](https://www.youtube.com/watch?v=HBlShxKwLCc&t=190s)** customers are suffering. Now they breathe down your neck, you might have to worry about your SLAs while you actually go and fix the issue and ultimately you will have a lot more customer pain if you don't use such a proactive solution as Logic Star. So, how does this work in practice? This might sound all sounds a little bit too good to be true, right? So, let me go here over this at a high level. Um we go um and approach your code base using first static analysis combined with LLMs to build a knowledge graph of your application and find types of bugs that might be important for you. Then, repeatedly, whenever your code changes on your deployment branch, we scan your code base and look for defects uh in your codes. And for most companies that we work with, these are hundreds or

**[3:57](https://www.youtube.com/watch?v=HBlShxKwLCc&t=237s)** typically even thousands of defects that we find, but you don't want to absorb so much change to address all of them. So, for most of them, even after deduplication and verification, we just ignore them and wait for signals either from your customers, from your engineers, or from your observability tools to then prioritize them and actually trigger action. So, to see how that works, let's sort of have a look at the little demo to see how quick even the onboarding process is. I'll take you through the whole onboarding. You simply sign up with your preferred single sign up solution, accept our terms and conditions, all standard stuff, and now let's create an organization. We call it AI Launchpad org. And now you have to obviously give us access to your code base. This will only

**[4:46](https://www.youtube.com/watch?v=HBlShxKwLCc&t=286s)** take 10 more seconds. And then, once this is set up, we simply create a project from whatever repositories that you want to include, and we already can get started scanning your code base. You just have to tell us what type of issues you care about. If you don't want to do that, don't worry. We will scan your last year of fixing and determine what you actually care about. Now, you can optionally connect some messaging solution like Slack, or we'll go and start analyze your code base. This is everything it needs at the minimum to get started, but to get most of the value out of Logic Sally, you obviously want to connect your observability system, your ticketing system, and so on. And for this, we already support a broad range of integrations, but more coming every day. So, if yours is not listed

**[5:34](https://www.youtube.com/watch?v=HBlShxKwLCc&t=334s)** here and you want to work with us, just let me know. Now, we're switching to a repo where this is all wired up already, and we look at the bugs that we find. So, here the first one we see is weekly correlated both with some observability data and with some tickets that we have. And in this case we say this one we might actually not work on because we don't want to absorb the change that is necessary to address this. So we simply tell the Logic Star system that we don't care in this case about this retry behavior and we will avoid bringing this up in the future. The next one in contrast however, we have actually seen one of our engineers open a ticket that they're investigating a related issue and Logic Star knows already there's the problem. So here's how you can fix it. Now there's two ways how you can do that. You first can look at our technical

**[6:22](https://www.youtube.com/watch?v=HBlShxKwLCc&t=382s)** analysis and then just fix it yourself from scratch or typically you would say we'll fix, open a ticket in GitHub or whatever other system you're using to track your workload and issues. And then we also request an auto fix from Logic Star. So as soon as you hit this confirmation button, we will start working in the background of providing a fix for you. If you would rather use your Win Surf cursor or Claude code, you can simply copy a prompt which I'm doing here as a a small demo as well. And while Claude is churning along, he's slightly accelerated, we're working in the background. So let's look at what the Logic Star agent here produced as a fix for you. And it turns out it's actually the very same fix that Claude would have provided. However, in addition to the Claude fix, we also have exhaustive test cases for you.

**[7:11](https://www.youtube.com/watch?v=HBlShxKwLCc&t=431s)** And in contrast to most other solutions, we provide for you the pre and the post execution behavior. See that in a second after we check that actually the tests cover what we want them to cover. And now we look at the test outcomes which we have pre-recorded so you can immediately see indeed the tests reproduce the original fading behavior. And after we apply the fixes, the tests indeed resolve the issue. So now we can go ahead with confidence and directly create a pull request, which from this point on is ready to be merged in your system, and the issue is uh caught before it actually turns into a bigger problem. Now, what is the back door What is our

**[7:59](https://www.youtube.com/watch?v=HBlShxKwLCc&t=479s)** background? Why are we suited to do this? In our founding team, we have two PhDs and a professor who have worked extensively on these systems already before they were cool, uh before the time of LLMs. And in the recent years, we've published extensively on benchmarking coding agents. So, we know exactly how these systems fail, how to optimize them, and how to design around these failure cases. So, with all of this in mind, I invite you to try Logic Spark for free. 14-day free trial with this QR code. Um we support a lot of mainstream programming languages. As you saw, the sign-up is super quick and super easy, and you get the first results within less than 1 hour. Now, if I still have a minute for questions, I'm happy to take them now, or you can find me around the

**[8:47](https://www.youtube.com/watch?v=HBlShxKwLCc&t=527s)** conference. >> [music]
