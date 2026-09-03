---
id: _NprbCLgs3A
title: "Insecure Agentic Code Examples"
slug: insecure-agentic-code-examples
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "Security conferences"
edition: "OWASP GenAI Security"
year: 2026
speakers: []
channel: null
duration_min: 10
published_at: 2026-01-21T03:16:26Z
video_id: _NprbCLgs3A
url: https://www.youtube.com/watch?v=_NprbCLgs3A
youtube_url: https://www.youtube.com/watch?v=_NprbCLgs3A
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Insecure Agentic Code Examples

**Speaker not identified**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=_NprbCLgs3A) · [Conference site](https://genai.owasp.org/)

## Description

*No description published on YouTube.*

## Transcript

*1,809 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=_NprbCLgs3A&t=2s)** [music] [music] My name is Ally. How I am the insecure code um examples co-lead. So I'd like to also thank my other co-lead that cannot be here with us today, Peter Stephenson. Thank you so much, Peter, if you're with us virtually. Um, like John mentioned, there's a big initiative within OAS of not only to put out ter terrific guidance, but to make sure it's practical and useful, um, and really get our hands dirty and make sure this stuff works. So, one of the ways that we were looking to accomplish this was to lead this initiative around this insecure

**[0:51](https://www.youtube.com/watch?v=_NprbCLgs3A&t=51s)** code example. So, go out and with ourselves, try these agentic frameworks, build examples of agents ourselves. um and see, you know, how easy is it really to create an insecure agent. We also opened this up to the larger community for them to be able to send us and produce insecure code examples. Um we did a hackathon in New York City as part of that initiative, which I'll touch on more later. Um but basically, you can go to this link and see some of the insecure code samples that are up on GitHub to date. Um we're constantly adding more, so always come back and look back for more. Um, as of right now, some of the frameworks covered that are in there, um, are Langraph, Autogen, Crew AI, um, AWS Bedrock, and the the agents SDK from OpenAI. Um, also been working to add Pyantic AI and MRA to the

**[1:41](https://www.youtube.com/watch?v=_NprbCLgs3A&t=101s)** list as well. Um, but basically there's a bunch of different great examples in there. I'll go over some of the things we've um, covered in there. So, a lot of what we have done to date is built on the work that has come before us. So um we mentioned earlier that we have an agentic threats and mitigation guide that um Helen led and um produced for us which has all these amazing threats and vulnerabilities that are specific specific to AI agents um for example like tool misuse excessive agency um even going so far as like human manipulation and that guide explains what those are um and we have mapped our insecure code examples to either those threats and vulnerabilities or the um top 10 for the um LLMs and some of the agenda.

**[2:31](https://www.youtube.com/watch?v=_NprbCLgs3A&t=151s)** Are you saying that that clever keyboard that Helen was presenting someone could go and see the Python code for those? >> Yeah. No, Finnbot is real. Okay. So, if you want to go see Finnbot, go to our repo and actually check it out. You can, you know, clone fork it. Um try it out yourself. You want to add more to it, add more, make it even more insecure, ship it again, like bring it back to us. I'd love that. So, please. Yeah, that'd be great. Um, and so there's more patterns that were covered like single agent, multi- aent. I mean, we've got rag examples in there. We've got a hierarchal agent, um, conversational agents. We've got examples of like customer chat bots gone arai. Um, you name it, it's in there. I hope it's really helpful. I hope it's useful. If you've got any sort of like feedback on it, or if you'd like to add more to it and participate, I'd love that. Um, it'd be really helpful to get more people involved in this.

**[3:20](https://www.youtube.com/watch?v=_NprbCLgs3A&t=200s)** So, one of the things we did to expand our outreach because OAS is fantastic and there's so many people here, but that we just we just need more we need more people to create um examples of insecure agents so we know kind of like what not to do or really um put ourselves in a position to provide actionable guidance. And one of the ways we did that is we hosted a hackathon in New York City um at Pensar HQ. So, thank you so much Pensar for host helping us host that. Um it was on April 1st which is like kind of fun, right? It's like April Fool's Day. Like let's actually get together with the idea of building something that's insecure like by design like on purpose. Um which was kind of fun. Um we did that in support from a few companies. Mostra, Pyantic, um Pensar and Splai. Um Pensar and Splai were really helpful um at this hackathon because they helped us find some of the vulnerabilities that were in our agentic code. Um, so both of those companies

**[4:09](https://www.youtube.com/watch?v=_NprbCLgs3A&t=249s)** were able to map the findings back to our threats and mitigations guide as well as the um top 10 for LLMs. And some of these um examples um made it into our repository um that has the insecure code examples. Um some of these submissions were um fantastic and we'd like to recognize um some of them. But before we do, I think one of the big takeaways that I'd like to share from this event is it's really easy to build an insecure agent. Um we had people there at that event. There were students all the way up to senior architects at well-known companies that you would recognize. Um all of them easily built insecure agents within matters of minutes um without really trying too hard to do so. Um so there's a lot of work to be done in terms of like recognizing that there's lots of like

**[4:58](https://www.youtube.com/watch?v=_NprbCLgs3A&t=298s)** different threads there and how can we you know do our best to make sure that we don't Yeah. Oh yeah. And vibe coding for sure. Right. I mean, that's that's a whole whole another thing for sure. Um, yeah, that's that's that's something to get into as well. Um, so to recognize the um some of the people that did amazing work at this hackathon, um, I'd like to recognize um Harrison Machnik, um, Arjun Remach Rishnan, and Ply Dan. Um, thank you so much for your amazing work and your insecur. And I hope you're watching, guys. Oh, thank you. >> Yeah, I hope you're watching because we're going to send you one of these amazing um plaques in the mail. Um you deserve it. Thank you so much.

**[5:48](https://www.youtube.com/watch?v=_NprbCLgs3A&t=348s)** >> Super fun, super nice. Um we'd also like to recognize some special >> Oh, yeah. He's not gonna want to miss this. I know it. Um yeah, we had some really good contributions um outside of the hackathon as well. Um these were kind of like internal, these are folks from OAS that did some really great work for this. Um Vulcan cuddle, he made a conversational agent that has that handles customer um refunds. Um and you can like notice in the system prompt here, he says like always follow the policy, never overwrite it. Um spoiler alert, it's going to override it. Um and it's also not going to follow the policy. And you can check out that example um on the repo. Um and then I like to also recognize um Ken, our >> well I I know a lot of people are

**[6:41](https://www.youtube.com/watch?v=_NprbCLgs3A&t=401s)** wondering right now, how do I build an MCP server securely? Like I'm personally fielding questions from companies of like how do I build an MCP server and can I rely on these PRs about authentication that are up right now? When are they going to go through? Like what are the threats um related there? And so Ken's made an awesome example there to check out um uh if you're looking at using MCP servers or building your own. Um and then also one of the fun interesting takeaways like for me personally after working um with all of these different frameworks is um it's really easy yes to create an insecure agent, but that's not to like bash the frameworks, right? We're not saying like you know if you're going to use a framework then it's going to like make your code like insecure. Um, some of these frameworks do offer some like advantages for security. Um, so I think

**[7:30](https://www.youtube.com/watch?v=_NprbCLgs3A&t=450s)** it'd be fun to, you know, continue this research and to look into ways and like best practices for these common frameworks that people use like what are the security advantages that they offer um that we can distill and bring to the community. So it's like, hey, if you're going to use like MRA, if you're going to use Pyanic, if you're going to use Crew, like here's the things that um, you want to make sure you're, you know, taking advantage of that this framework provides that could be helpful for security. Um, for example, like for MSRA, like they shipped um agent runtime contexts, which is like pretty cool because you can set um certain contexts per agent run like not everything needs to be persistent in memory. Um, so that's a good use case um for just like scoping down um and preventing um excessive agency. Um and also like the tools list on MCP servers can be beautiful. So like say like for one example I did I was building something with um the GitHub MCP server and I

**[8:18](https://www.youtube.com/watch?v=_NprbCLgs3A&t=498s)** wanted to like create PRs but I also didn't want to be able to delete things in GitHub. So I didn't need the delete um MCP tool that came with it but you can you know it's a mutable tools list so you can get rid of the tools that you don't need um which is helpful for security as well because we know we want to prevent we want to prevent like excessive agency and tool misuse. um from Pyantic they've got like data validation which can be helpful for security and also um they have a a built to run Python MCP server so you can like run arbitrary code um in a sandbox which is you know helpful for security and I'd like to continue this research and go into like other frameworks as well that um I'm sure they have amazing things as well to offer for us um that are helpful for security um any questions on any of the insecure code samples that we built Yeah, exactly. Totally. Yeah, super

**[9:12](https://www.youtube.com/watch?v=_NprbCLgs3A&t=552s)** exciting and it's ever evolving and excited to continue researching this. >> Planning to do more hackathons. >> Yes. Oh my gosh, we are. >> So, um that's okay. So, you know, don't don't think you miss your opportunity. We we think that's kind of vital. If you're watching from uh kind of the the live stream, we're going to be one in Europe possibly with a nice city in London. But yeah, you know just a event, you know, you can go to the report and you can see the you can your own.
