---
id: EcgYMY4eUTo
title: "Rules Are Not Suggestions: A History of MCP Non-Compliance - Sterling Dreyer, Arcade.dev"
slug: rules-are-not-suggestions-a-history-of-mcp-non-compliance
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: ["Sterling Dreyer"]
channel: "Agentic AI Foundation"
duration_min: 19
published_at: 2026-04-13T23:19:11Z
video_id: EcgYMY4eUTo
url: https://www.youtube.com/watch?v=EcgYMY4eUTo
youtube_url: https://www.youtube.com/watch?v=EcgYMY4eUTo
tags: []
transcript: true
---

# Rules Are Not Suggestions: A History of MCP Non-Compliance - Sterling Dreyer, Arcade.dev

**Sterling Dreyer**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=EcgYMY4eUTo) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Rules Are Not Suggestions: A History of MCP Non-Compliance - Sterling Dreyer, Arcade.dev

Less than 20% of remote MCP servers fully comply with the MCP Specification.

MCP adoption took off quickly, but full compliance didn't follow at the same pace. Today, partial implementations are common across both clients and servers, and the reasons go beyond just a fast-moving spec.
In this session, we'll walk you through:

-The first version of the MCP Specification and what it was designed for
-How MCP evolved to keep up with the quickly evolving AI ecosystem
-How clients and servers deviate from the spec and why developers choose not to comply
-What we can do to shrink the gap between design and implementation
This isn't a story about bad developers or tight deadlines. It's about how bending the rules has become part of how agents get built.

## Transcript

*2,775 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=0s)** Uh, my name is Sterling. I'm a founding engineer at Arcade. I work on our core products and I do some work on our infrastructure. And part of what I have done in the last year is our work on our MCP integration. Uh, Arcade's an MCP runtime. We manage auth and governance for agentic tools. Um, and we also provide a evaluation suite and hosting for MCP servers. Uh, so I'm going to talk about my experience adding MCP to our products. Um, it was something that I thought would be a simple task for us to do and it ended up becoming a drawn-out process that wasn't as straightforward as I had imagined it would be. Um, so integrating with MCP was hard.

**[0:48](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=48s)** I initially started doing it when streamable HTTP was added. Um, and along with the OAuth, so version two. Um, so initially, like, I wanted to try it out. I made a standalone script. I just got an open-source SDK and tried to test against a remote server. Uh, first server I used worked. Second one didn't work. The next one also didn't work. So, why wasn't it working? I wasn't sure. Was it the server that wasn't implementing something properly? Was it the client that wasn't implementing something properly? Um, I saw people at our company having issues with this, too. If it was, uh, you know, a client like Cursor or Claude that they wanted to add an MCP server to

**[1:38](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=98s)** or just like an SDK, um, they would also run into issues with some servers every now and then as well. Um, AI has helped to open up uh, development and these tools to people that aren't developers. Um, so if I'm having a problem figuring this out, what are these people experiencing? So, we analyze the entire ecosystem of MCP tools. Um, we took some of these servers from registries. There's I'm sure you've seen there's tons of lists of servers that uh you can use. People compile them all the time. Um, we also found smaller projects that people were building um on public repos in GitHub. Um,

**[2:27](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=147s)** and why we included non-production servers into this is think about when you make a project and you use an HTTP client. Um, we assume there's guardrails to make it hard for you to mess up and you expect them to just work. So, um we should assume that MCP itself, if we pick up some client that's provided to us, will also be 100% compliant. Um, to get this data, we built two tools internally. One is called MCP Debugger. Uh, it does live tests against servers, gives you information about parts of the spec that fail. Uh, it shows you the risk of not implementing that or that it just may

**[3:15](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=195s)** not work. Um, and it gives you a link to remediate it. So, it helps us internally understand is it us making a mistake in our clients or is it the server we're connecting to that's not working properly. Um, so most of the data I'll be talking about is from this tool. Uh, we have a couple hundred servers that we use this on. Um, but it's a bit smaller than the overall uh scale that we have because we have to actually run the servers ourselves or have it already hosted in order to test against them. Um, the second tool that we use is called Tool Bench. Um it's our static server analyzer. So, we can give it the code. It will one, tell us the quality of the server in terms of

**[4:03](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=243s)** does the code itself comply with the spec? Needs to be things that we can actually look through and check in the code itself. Um how much functionality does it support? Is it just tools? Um what are the resources can you use on that server? And then we have other metadata like the framework and owner of the server. Um Um and we found that 94% of servers we tested failed some kind of test. So, only 6% fully complied. One or 9% failed one check. And 85% failed two or more checks. Um for context, this doesn't mean that they don't work. Uh you may be able to use it and you may not even notice that there's something wrong with it. It may work perfectly fine. Um but you can introduce security issues

**[4:53](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=293s)** or um the client may have to rely on fallbacks instead of being able to use uh the uh initial path it was supposed to take. So, for examples, a lot of servers don't validate the origin header when they get requests. And a lot of them also don't return a www-authenticate header. Um so, very minor if you're using a pre-built client, you probably haven't even noticed it. Um but it does have uh implications. Um these were also we compared them against the version of the spec that uh the server advertised because in some versions, it may be suggested that you do something and then in a later

**[5:40](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=340s)** version, then that is required. So, we made sure to not count things that are currently required against servers that were previously built. So, uh let's dig in. Let's figure out what's happening and what we can do to fix it. Um so, first, the spec is moving really fast. We've only had four releases, but every release is really big. It's They're not little patches. They're new functionality, changes in functionality, um changes in the transport itself sometimes. Um so, like I said, in the latest release, we changed some suggested things into hard requirements. Uh so, as a developer, if you're building a client or you're building a server, you know now have to support that new functionality. You have

**[6:29](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=389s)** to support the changes in functionality. You have to test all of that. If you're uh trying to run multiple versions, maybe your client supports multiple versions, then you need to make sure that you can support those changes in the schema between versions. Um when I started trying to build our own client, I was like, how do I test my client? And for reference, this was about a year ago. So, there's a lot less tooling then but it still hasn't come up to where uh I would expect it to be. Um so, I wish that we had a conformance suite back then. And something that I could run in CICD and make sure we don't have any

**[7:16](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=436s)** regressions, make sure all the differences in versions work, um you know, like normal software engineering. Um so, this is actually new to me. I didn't realize that there's a conformance test. Um I have been looking for this. I could not get it to come up in search results. I figured out this week that it exists. Um there I was surprised because it has 50 stars on GitHub, whereas most of the clients have tens of thousands of stars. I thought this would be something that um would, you know, show up and be well used. But the MCP debugger that we built before, we started building that before this came out. So, that's why we currently have that.

**[8:04](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=484s)** Um, and in the time that I had to test it out for this talk, uh it seems to be pretty narrow in the scope it does, and there's some tests that only work for the client and don't check the other side on the server. So, what should we do about that? Um, we want to get the spec into a place where people can just pull a client off, know it works. We can see conformance tests. There's no thinking about does this server SDK work? Does this client SDK work? Um so something is I feel like we need to heavily promote this uh conformance repo more. It should be something that everybody should be running in CICD.

**[8:52](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=532s)** Uh, it also needs to be extended more. I would like to see I could see them putting things in from the new specs, but it feels like it's fairly lacking in what it currently supports in scenarios that the people could run into that we need to make clear when they test uh if it's acceptable if it passes. So, another stat. Uh, 19% of all tools that we scanned uh had some issue with the input schema. So, why why does this happen? A lot of people use the provided frameworks or or use a third-party framework. Um and I learned that a lot of this was due

**[9:41](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=581s)** to bugs or just not enforcement in the uh SDK itself. People can give null values when they shouldn't. And or uh ambiguous parameters. And that's something that we need to work with the um third-party libraries on on making sure that they are doing everything properly to help their users. Um I'm sure some of you have seen this. I'm sure all of you have seen this. API key usage in the spec. So, API keys are not in the spec at all. It's not It wasn't in the first spec.

**[10:30](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=630s)** It I mean, the first spec didn't have auth in it. But, how are you going to connect to GitHub or linear or some other service that you want to make an MCP server for if there's no if you can't use an API key or there's no auth. So, you know, the easy solution is allow your server to take a API key and a header or throw it in the environment throw it in the environment. Um problem with API keys is it takes work on the user side. So, if someone else builds a server, I can't just use it. I have to go get that API key and it maybe I'm at a company and I don't have access to go make my own API key. Um a lot of API keys also give full access. There's some apps that you can make them more granular, but

**[11:19](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=679s)** they often just give you full permissions. Um and it's less secure. So, in V2, we introduced uh not we, but uh MCP introduced OAuth to GCR. A lot better usage. Users can just log in if they already have an account. It's more secure, but people still use API keys. So, why are we still using API keys if we have a better alternative that's safer, that's easier for the user? And I I've been thinking of it as a scale problem. So, if I'm a company and I have my product, the lift to add a uh add OAuth to my app is pretty low

**[12:06](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=726s)** comparatively to the effort that I'm using to build that app or product itself. But, if I'm a developer and I'm making MCP servers for my personal projects or for some friends or for some coworkers to use, not an official um company product, then this is a little overly complicated for what I want to do. If I just want somebody to read my emails, I don't really want to implement that. So, if everyone has to implement OAuth, we're going to have issues with compliance. The thing is though, very few people build servers and clients from scratch.

**[12:55](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=775s)** Most people use a provided SDK. Um so, why are we still failing so much? A lot of frameworks still make you do a lot of the work. So, like I mentioned before the uh origin header verification or the WW-Authenticate, some frameworks don't handle that for you. You have to do that yourself even though it's very minimal uh code from your side and their side, but people forget. So, the framework should take ownership of making sure that it's very difficult for the user to forget something like returning a header. Um

**[13:42](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=822s)** this could be guided setups where it's a requirement when you make your server or templates or just a a easier flow or uh interface where you're it's required. You need a host name or something. The user doesn't have to think about that. They just have to give it to you and they can't forget it. So, other solutions. What else can we do? These are a bit more aggressive. Uh registry gatekeeping. So, I believe MCP is already starting to do something like this. They have their um tiers. So, making it so that you if you're

**[14:31](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=871s)** failing as badly as some of the servers that we've seen are failing, that shouldn't be something that is offered or allowed for uh users to use through like a official list. Um and client-side rejection. So, thinking about clients as more of a browser, the way browser we treat browsers rather than a standalone piece of code. So, if I don't have a certificate on my server, my browser lets me know that very clearly and puts roadblocks in the way for me until that client exists or I have to forcefully get through that.

**[15:19](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=919s)** Um now, this is easier for MCP to support with things that it provides, but let's say we need cursor to support that for this to work, um, it needs to be part of the spec. It can't just be, uh, maybe you can do this. If we really want to push everyone to be compliant, we need to enforce that. Um, so, overall, the goal is to lower barriers for users, non-coders, make developers' lives easier, and produce a standard that we know will work. And we don't have to guess. And this has just been servers. I could make a whole 'nother presentation

**[16:07](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=967s)** on clients, but just as a scope, that's what I have so far. Uh, thank you for coming. Uh, I still have some time to answer questions. Uh, you can also come to our booth, or grab me after this. And feel free to check us out. Um, and you can check out MCP Debugger and Toolbench. They, they're free. You don't No account required. You can just go look at them and use them. Any questions? Yeah. Yeah. So, I saw the talk by, uh, your colleague this morning. Demoed a lot more of Arcade. Mhm. Did you just know, like, the problems you were talking about here, did they Did you learn a lot of them, or did you find them through the process of building

**[16:54](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=1014s)** Arcade, or were these sort of foundational problems that led to your team building Arcade? Uh, these were not issues that led to us building Arcade. These were issues that we found while we were building Arcade. So, earlier on, we had our own protocol that we were using, and then MCP got really popular, and seem, you know, became the way to go to support. Um, and then a lot of this was finding those problems while getting that MCP implementation in. Cool. Besides the two tools that you mentioned and obviously using the inspector Mhm. What other tools do you recommend to say I checked the boxes? So far, um

**[17:45](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=1065s)** I would say that's that's a hard question because we built the debugger because we needed more Inspector works fine, but I couldn't find any other tools that were widely used that I felt gave me the clarity that I needed. So, that's why we built MCP debugger. Um going forward I would like to see the conformance test provided by uh MCP to be built out further or someone else to build a like client test. But, the the client test was definitely the hardest thing to find. I I wasn't sure like how do I confirm that my client works? I just couldn't find anything that would help

**[18:33](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=1113s)** me with that when I was building this out. The way you showed it, it showed it's like synonymous to how back in the day you would grade your your website you know eight blocks on it. You still have I'm sorry, right? So Is there a rubric out there that can say, "Okay, here are the things that need to be graded on?" Oh, yeah. If you So, for MCP debugger, that is a very I'm not sure what like the lettering grade as much uh follows, but it'll give you an exact number of you fulfilled 50 out of 50 requirements. Um, for Tool Bench, we do have a rubric on there that shows you how we wait things, what kind of information we're using,

**[19:19](https://www.youtube.com/watch?v=EcgYMY4eUTo&t=1159s)** how we collected that, so.
