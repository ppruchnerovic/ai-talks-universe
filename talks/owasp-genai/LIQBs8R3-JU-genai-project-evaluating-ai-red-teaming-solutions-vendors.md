---
id: LIQBs8R3-JU
title: "GenAI Project | Evaluating AI Red Teaming Solutions/Vendors: New OWASP Criteria Guide"
slug: genai-project-evaluating-ai-red-teaming-solutions-vendors
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: ["Jason Ross"]
channel: "OWASP GenAI Security Project"
duration_min: 14
published_at: 2026-07-20T00:08:33Z
video_id: LIQBs8R3-JU
youtube_url: https://www.youtube.com/watch?v=LIQBs8R3-JU
tags: []
transcript: true
---

# GenAI Project | Evaluating AI Red Teaming Solutions/Vendors: New OWASP Criteria Guide

**Jason Ross**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=LIQBs8R3-JU) · [Conference site](https://genai.owasp.org/)

## Description

As demand for AI red teaming accelerates, organizations face a growing challenge: how to meaningfully evaluate the tools and vendors claiming to secure their generative and agentic AI systems. The OWASP GenAI Security Project addresses this gap with its newly published Evaluating AI Red Teaming Solutions/Vendors: Criteria Guide—a practical framework for assessing capability, coverage, and credibility in an increasingly crowded market.

This session introduces the guide and walks through its core evaluation dimensions, including depth of attack simulation, alignment with real-world threat models (such as the Agentic Top 10), transparency of methodologies, and support for continuous testing across the AI lifecycle. We’ll examine how to distinguish surface-level testing from rigorous adversarial assessment, and how to validate whether a solution can effectively uncover risks like prompt injection, tool abuse, and unsafe autonomy.

🔗 Learn more: https://genai.owasp.org

Speakers:
Jason Ross
Co-lead, AI Red Teaming Initiative, Product Security Principal, Salesforce

## Transcript

*2,228 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=4s)** Hello. Uh, welcome to the OOSPAI security project red team update. Uh, I'm Jason. I'm one of the co-leads for the red teaming project uh, within the security project. Um, myself and Sonu kind of lead that project. Uh, and Felipe helps us out with the code stuff. Uh, unfortunately neither of the my my co-leads and uh companions were able to make it here today. So, just got me today unfortunately uh for you all. But, uh we'll have a good time. Uh any questions that you might have as we go along, definitely feel free to put them in the chat and uh I will happily answer them as we go through the process. So, uh, what have we been doing in the

**[0:55](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=55s)** last year with the red team project? Uh, we've been working on a red team manual. We'll talk more about that in just a minute. But what I really kind of want to focus on with this today is a couple months ago, we released an AI red teaming vendor evaluation guide. Uh, that came out of basically a bunch of internal questions that we had amongst ourselves within the security project. And essentially we were looking at the landscape. We saw a whole bunch of people saying they had cool AI red teaming stuff and no really good rubric or metric for people to kind of measure the BS against what was reality and see what is vendor hype versus what is actually useful to me in an AI red

**[1:44](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=104s)** teaming scenario. So we started in October just having some conversations amongst ourselves as the core team about this discussion and the point that we kept coming back to with this was all of the tooling seems to be primarily focused on chat bots and we really are well past the chatbot phase in enterprise AI systems. So a guide to test this stuff is really kind of needed. And then as we were talking through which of the various sub projects made sense to provide that uh we sort of settled on probably it made sense for the AI red teaming group to to do that. Fortunately I had a request at work to come up with a similar task of creating something that we could use to

**[2:33](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=153s)** kind of gauge vendors as we do proof of concepts with them. So, I was able to kind of kill two birds with one stone. Uh, we spun up a really fast project within the team to create this guide and then I was able to go back to my leadership and say, "Hey, look, OASP has this cool thing." Uh, and we can use that now. So, let's talk about why we needed this thing at all. Um, like I said, the market's flooded with vendors and they're all saying essentially the same thing, it's really hard to tell what's important, what is useful, and what's just hype and spin. Um, and since they're all kind of saying the same thing, it makes it really hard to tell like what's the distinguishing

**[3:20](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=200s)** feature, what makes you different from everybody else, why would I pick you over somebody else? Um, so if you look at the landscape for AI right now, jailbreak engines aren't enough. And if you look at what the red team tooling generally is doing right now, it's jailbreak engines. They're doing things like, can I tell you to ignore all previous instructions? And that's like three plus years old attacks, right? No model that's modern is going to still fall for that reliably. It's all old school stuff and they're just outdated. Um, so we needed something that could help us cut through the security theater. Um,

**[4:07](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=247s)** basically behavioral risk is important. Jailbreak engines is not. So, how do we evaluate which of these tools that are claiming to be awesome gets us what we need to be? The way that we approached this for this document, um, we recognized that there's there's kind of two buckets that people fall into. So, if you've been doing stuff with AI over the last year plus two years, you're probably further along in this than other people. So we we see kind of a pattern in the industry right now where people fall into one of two categories. Either you're building up some kind of simple Gen AI chatbot, maybe you're doing some simple rag. Um so things like customer service uh bots that are looking up articles or

**[4:59](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=299s)** documentation and providing answers to people. That's a fairly simple use case. The red teaming needs for that is very different from a fully agentic stack where you're doing things like tool calling, you have multiple agents, you've got orchestrators in the process, maybe you even have multiple party agents, right, coming at you. Um, so as we as we kind of thought about what's the approach for this document look like, we realized we needed to kind of provide context for both of those use cases. So we split the document up into both of those use cases. Um, and what we did is for each of those use cases, we provided a really simple evaluating rubric. Our intent here was for this to be given to executives and

**[5:49](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=349s)** management making strategic decisions for like what should we buy? Um, so we've got a really high level executive green flag red flag checklist and then we broke things down categorically and provided a little bit more technical detail there. So if you're a practitioner whose management is coming to you and saying, "Hey, help me evaluate this thing that is bugging me to look at their product." You've got technical details that go into the weeds. Um, still doing it though through a green flag, red flag. So, if you go look at the document, you'll see it'll talk about if the vendor says this, that's a red flag. And so, things like jailbreak type system prompts, uh, that that is a red flag. If that's all

**[6:37](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=397s)** they're talking about and they're not going to more in-depth testing or rigorous threat modeling, especially as part of what they're talking about, big red flags. So, we made it pretty simple, pretty straightforward to go through and evaluate. You can almost literally pull this thing out while the vendor is pitching you and just be like, "Yep, they said this. Yep, they said this. Bye." Uh, or, "Yep, they said this. Yep, they said this." You can ask pointed questions. We have a Q&A section at the end for you to ask pointed questions to your vendors to get good answers. Um, so it's really just kind of a as the vendor's pitching you, look for these things, ask them these questions, see how they answer, and then you can decide, does this fit your needs or not. Pausing for a second,

**[7:28](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=448s)** obviously there's a whole lot of vendor hype out there in the market. And if you look at the OAF project right now, if you join the Slack channel, which you should have joined the Slack channel, um, if you're interested in this, there's a lot of practitioners and a lot of vendors that are sitting in the Slack channel. So, one obvious question becomes, how much did you sell out to the vendors that are helping you do these types of things as you created this document? And the answer to that is, we sold out zero. Um, my goal for this was specifically to cut through the BS. Um, I'm very frustrated with the current state of AI red team tooling and vendors, there's a whole lot of hype and a lot of it is garbage. So, not only am I tired of leadership coming

**[8:19](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=499s)** to me and asking me about terrible products and saying, "We should hire these guys." And then I have to explain to them all the reasons why they we should not hire those guys. Um, I also just want to uplift the security community, right? Like that's that's the whole point of what OASP is doing. We want to give people tools to be able to do that. We didn't sell out at all for this. It's completely vendor agnostic. We don't talk about vendors. We don't recommend tooling as part of this guide. It's literally just questions to ask and key phrases and things to look for as you're talking to them. You can decide for yourself from there. Um, everybody that contributed to this guide is doing AI red teaming. So, we all have experience and we know what we want to see in tools and what we don't want to see in tools. And that's where this all

**[9:06](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=546s)** was driven by. All of that said, you should please add your voice. So, go download the evaluation guide. We have a QR code here you can scan. Um, as you're talking to vendors, actually demand rigor. Demand adversarial rigor from your vendors. Don't just look for prompt jailbreak escapes. That's not good enough, and you're going to be doing a disservice to yourself if you if you do that. So, download the guide, demand rigger, and finally, if you're a practitioner, like I said, join our Slack. Come talk to us. We would love to get help. Uh we need more practitioners uh helping us figure out how to build tools, how to guide the community. Uh we're always open and looking for help with that.

**[9:58](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=598s)** That is it for the vendor evaluation guide. Now the next question is what else are we doing? Um I don't have slides for this part of it so I'll stop sharing this right now. Um, but what we're doing in addition to the vendor guide, we are currently working on a red teaming manual. This is designed to be a practitioners hands-on guide. So, about a year and a half ago, we put out a red teaming um, guide book. I forget what we called it. um that was intended to be what are the things that I need to think about as I'm approaching red teaming AI based stuff. It was very high level and it was geared

**[10:47](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=647s)** towards how how to think about the approach. This manual is hands-on what you should do, how you should do it, actually talking about ways to run um attacks against the AI. There's a huge section on threat modeling because threat modeling is critical for red teaming AI. Um it's not optional. You have to threat model because the use case specifically matters. And if you are not already doing threat modeling of the use case in your red teaming, you are doing it wrong. So we have a huge section just around that. We're about ready to release that for public uh comment. It's not finished. There's a lot of work still that needs to go into

**[11:34](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=694s)** it, but we feel that we've got it in a good enough place right now that we want to make sure that it aligns with what the community is thinking about this. And we want to make sure that we're including um everybody's feedback as we put this out there so that it becomes a useful resource for the community and not just something that we're doing in isolation. Uh so expect to see some forms and LinkedIn posts and things like that posted pretty soon for that. Um, and when we do that, please go download it, read it, tear it apart, send us all the terrible things that are wrong with it, send us all the good things that are good with it, too. Um, so that we can make sure that when this is finally released, it's it's what the community needs and wants. That's coming soon. Right now, we also

**[12:25](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=745s)** have a um red team GitHub project. So, if you join our Slack, you'll see links to that. And if you want to help build tooling or demos, uh we've got a great project that we're building up right now. Felipe, uh like I said, is is kind of leading that within the Red Team project. Um come join us. It's it's a pretty cool lab. It's got a nice uh vulnerable agent. Does a whole lot of stuff. Um it's one of many vulnerable agents that the project has. Um, but this one specifically aligns to the red team manual that we're putting out. So, as you're reading the manual, the agent in our repo will be able to be used as a teach myself how to do this. Walk me through how to do this. Here's vulnerabilities that directly map to

**[13:13](https://www.youtube.com/watch?v=LIQBs8R3-JU&t=793s)** what we're talking about in the manual. That's the intent there. Um, we're also releasing tools slowly. Um, so if you've got an idea for a cool tool that's useful for AI red teaming, like I said, join the Slack, come come see us. We're happy to talk. That is kind of all I have. So, I think in any remaining time that we have, we can just kind of open it up to questions sort of I'm a red teamer AMA style. If you want, uh, dump questions in there and, uh, I'll see if we can answer them all.
