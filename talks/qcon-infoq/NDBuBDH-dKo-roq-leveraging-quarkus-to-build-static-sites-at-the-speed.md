---
id: NDBuBDH-dKo
title: "Roq: Leveraging Quarkus to Build Static Sites at the Speed of Go"
slug: roq-leveraging-quarkus-to-build-static-sites-at-the-speed
conference: qcon-infoq
conference_name: "QCon / InfoQ Dev Summit"
category: "Software dev with AI tracks"
edition: "InfoQ"
year: 2026
speakers: []
channel: "InfoQ"
duration_min: 21
published_at: 2026-05-04T10:15:22Z
video_id: NDBuBDH-dKo
url: https://www.youtube.com/watch?v=NDBuBDH-dKo
youtube_url: https://www.youtube.com/watch?v=NDBuBDH-dKo
tags: []
transcript: true
---

# Roq: Leveraging Quarkus to Build Static Sites at the Speed of Go

**Speaker not identified**

`QCon / InfoQ Dev Summit` · `InfoQ` · `2026` · `21 min`

[Watch the recording](https://www.youtube.com/watch?v=NDBuBDH-dKo) · [Conference site](https://qconferences.com/)

## Description

Andy Damevin, a developer who worked on Quarkus for almost a decade, talks about Roq. A project that started as an experiment to try to see if it’s possible to build a static web site generator on top of quarkus. He touches on the rationale for choosing Java and Quarkus, how to migrate to Roq, and the platform's future.

Read a transcript of this interview: https://bit.ly/48Q5SoJ

Newsletter:
Subscribe to the Software Architects’ Newsletter for your monthly guide to the essential news and experience from industry peers on emerging patterns and technologies:

InfoQ online certification cohorts:
Online cohorts for senior engineers and architects, built around QCon talks. Join a 5-week confidential peer group to validate your approach and apply practitioner frameworks to the technical challenges you face at work. Learn more: https://certification.qconferences.com/

Upcoming Events:

QCon AI Boston 2026 (June 1-2, 2026)
Learn how real teams are accelerating the entire software lifecycle with AI.

QCon San Francisco 2026 (November 16-20, 2026)

The InfoQ Podcasts:
Weekly inspiration to drive innovation and build great teams from senior software leaders. Listen to all our podcasts and read interview transcripts:

- The InfoQ Podcast https://www.infoq.com/podcasts/
- Engineering Culture Podcast by InfoQ https://www.infoq.com/podcasts/#engineering_culture
- Generally AI: https://www.infoq.com/generally-ai-podcast/

Follow InfoQ:
- Mastodon: https://techhub.social/@infoq
- X: https://x.com/InfoQ?from=@
- LinkedIn: https://www.linkedin.com/company/infoq/
- Facebook: https://www.facebook.com/InfoQdotcom#
- Instagram: https://www.instagram.com/infoqdotcom/?hl=en
- Youtube: https://www.youtube.com/infoq
- Bluesky: https://bsky.app/profile/infoq.com

Write for InfoQ:
Learn and share the changes and innovations in professional software development.
- Join a community of practitioners.
- Increase your visibility.
- Grow your career.

## Transcript

*3,595 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=0s)** If your team has AI running in a proof of concept, but you're still figuring out how to run it reliably in production, you're not alone. That's the gap most engineering teams are navigating right now. QCon AI Boston this June 1st and 2nd brings together senior engineers, software architects, and technical leaders who've already made that shift. They'll share the patterns that scaled, the mistakes that didn't make the blog post, and what they'd actually do differently. No hidden product pitches, just senior practitioners helping senior practitioners. Learn more at boston.qcon.ai. Hello everybody. I'm Olimpio Pop, the InfoQ [music] editor. And I have in front of me Andy, who is the builder, the fire starter of Rook, which is more or less a new way of putting markdown languages

**[0:52](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=52s)** online, right? But before, Andy, can you please introduce yourself and then tell us what actually Rook is. Of course. So, I'm Andy Damevin. I'm a full-stack developer. I love Java. I love UIs. And above all, I love making it all streamlined. I love when things are easy to use. I've been in the Quarkus team for 9 years. If you don't know Quarkus, Quarkus is a Java framework. It's getting pretty famous. And I made a lot of tools for Quarkus already. So, what's the connection between Quarkus and Rook? Because in the end, we're here to speak about Rook. Right? Yeah, we're here to speak about Rook. Rook is a static site generator, and it allow to create static sites using Quarkus behind the scene. But you

**[1:39](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=99s)** don't need to know about Quarkus or Java. It's just that it's using its power to do it. That's nicely said. But before we delve into why would you like to build another static website generator? Because usually that's a piece of technology for other areas, not for Java. I have to take note about the fact that you said I like Java. For those people that don't know Andy, he's very young, and he still likes Java. And that's why I wanted to see how did Java change in the 9 years since you joined the Quarkus team in terms of language and how easy it is to get started with it. Mainly the language level that you use like a developer.

**[2:26](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=146s)** So, I see two questions. The first is about Java and and why it's cool again, let's say that this way. And the other is about why using Java for Rook, and that I think a totally different question. And you also ask why another static site generator. Well, we'll just take them one by one. But now I'm just curious because, you know, for a long period of time, people were saying whenever they would say Java, they said slow. Java slow. This this was like a contest. And then everybody was explaining how fabulous different type of ecosystems are. And now these voices start to get smaller and smaller. And I think in the last couple of weeks, I organized at least two meetups. And there are a lot of young people, meaning fresh graduates that are working and looking into Java.

**[3:14](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=194s)** And that was like, "Wow, finally it's getting out of those weeds, and it's nice." So, Java is in a good place. Then going back to what you mentioned, yes, why another static sites generator? So, why Java again? To be fully honest, at some point I started working a bit on Go. And I thought Java was not going to be something in the future. And Quarkus really changed the game. It's not really Quarkus. It's the fact that it brings that native speed that was missing in Java. I always loved Java. I always preferred coding in Java rather than in Go because it give a really nice format to things. Everything is clean. You have tests. It's well organized. And that's what I love about Java. And I

**[4:03](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=243s)** think to make really nice infrastructures, to really powerful application, Java is the perfect solution. But the thing is, people were moving away from it and starting using Go and stuff like that, mostly because it can compile to binaries. And if you take Java, you were not about to do that. And the JVM was a problem. And now it's starting to be a good thing again because when you see that you can do binary again, then you start to switch back to the JVM again because you say, "Okay, I can do binary. I can be quick, but I can also do like optimization at runtime and things like that that you can do with the JVM and that you can't do with plain native. I think that makes Java cool again. And that's not taking everything that Java

**[4:53](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=293s)** has really evolved with the new JDKs that are arriving. If you take everything together, I think yeah, it would be something in the future. Yeah, well, we are promising or the community is promising that Java is dying for at least 15 years. And for me, it seems that the ecosystem is growing and growing. And looking aside, it's like somehow very much differentiator in terms of the different generation of technologies. Like if you just think initially you had the EJBs a long time ago. You had enterprise Java beans, and that was like awful. And then we had the new wave of stuff, and it was Spring that was trying to do something different. And then there we had the POJOs, regardless of where they are

**[5:40](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=340s)** enterprise or Spring. And then we have now this, you call it renaissance if you want. We had a third generation of way of writing applications, and that's Quarkus. And probably you can put Micronaut in the same category, but that's a whole different perspective of looking at it. Fast. And what I particularly liked a lot about what Quarkus did even since it began, and I had at least one conversation with Max Anderson about it, you thought about the developer's joy. And that was a new metric that appeared for the developer because up to then you spoke about performance, you spoke about patterns, and then out of the sudden you had all different mechanism. That was good. Did any of this play any role into writing Rook around Quarkus? So, the thing with Rook is it's

**[6:33](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=393s)** just luck. Let's say it that way. Because I don't think that Quarkus initially was the best place and the best system to make a static site generator. It wasn't obvious. And when I built it, I thought, "Okay, maybe it's more than what I initially thought when I started it." I started it because it was easy to make. It was just a a small piece on top of Quarkus. So, I I thought, "Okay, why not?" And then I thought, "Oh, but we have everything in Quarkus that you need. But just out of Quarkus, the static site generator is just a small part. It's nearly nothing compared to everything that Quarkus brings. And I don't think there any other static site generator that have everything ready beforehand. And

**[7:23](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=443s)** the static site generator is just a small part of it. So, Rook is actually an extension on Quarkus. Actually, what you have is a Quarkus engine that is enabled to generate static sites, right? Yep. Okay, that might make sense in some situations. But isn't it too heavyweight? If I need a plain website, I don't know. I have a bunch of MD files. I want to create something like a blog, a release site, or whatever. Do I really need something as powerful as Quarkus behind it? If you take that question, you need to consider the alternatives, obviously. And if you compare it to the alternative, I think it makes Rook a really good candidate in your choice. Because in the end, Quarkus is not making it heavier at all. And it brings an awesome developer experience. And we

**[8:13](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=493s)** will see later a lighter experience. If you want to write content, it also really good. So, if you put everything together, yeah, I think it's a good candidate. Okay. What actually is behind this thing? So, how should I I look at it? Okay, we have Quarkus, and we know that it starts fast, and it has a bunch of things internally that allows it to process things faster due to the way how the team built it around the reactive streams and everything inside. And then, obviously, the way how it handles and loads the data allows it to be very fast. So, it's clear that this is a very powerful tool. What's needed more to be able to build static websites? Okay, please describe how, I don't know,

**[9:01](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=541s)** basically the architecture looks like. Okay, we have Quarkus that provides with the context. And then what else does Rook bring to the table? Or what do you have to put together? That's a good question. So, how is Rook working? If you look closely, in Quarkus you have two distinct parts. You have the build time and the run time. That's a big particularity about Quarkus. But just to say, everything I'm saying now is not making Rook more complicated. It's just that it's how it's made. But you don't need to know all that to actually use it. But it's always nice to know how it's working behind the scene. What changed in my mind is when I thought, "Okay, when you're building a static website, you want to build your website." And building means generating all those pages statically. When you think about Quarkus, you have

**[9:49](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=589s)** the build time. So, you want to build things at build time. But I thought, "Okay, why do we need to build things at build time? We could actually work like on any normal Quarkus application that is served at runtime and generate it like a snapshot. You just dump everything as files from the Quarkus application and that's actually how Rock works. It's just starting a Quarkus application, but it's so light that it's really fast and it's dumping everything from your Quarkus application to static files. This is what makes it pretty unique because you're actually using Quarkus like the Quarkus runtime. You're starting it to generate your things. And that's also what's cool for development because when you're developing compared to other

**[10:37](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=637s)** static site generator, we don't actually generate anything. We just use Quarkus server. It will just render on demand. So, you have live reload by default. And when you actually need to build, then we are going to dump everything as files. So, let's take an example and we we discussed about this previously. Let's say the Java Advent calendar that is published each year in December. We have the articles and so on and so forth. Probably now we have 13 to 15 years of articles there. They are part of a database probably in WordPress. I don't know. I I never understood how WordPress works. Well, it's PHP. Who actually knows what's in there? But if we're looking into migrating it to

**[11:24](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=684s)** Rock to just say that, okay, we are bootstrapping and we are pushed into Java ecosystem. What actually should we do? What are the steps that we should take to go get on the other side? Something special about WordPress is the fact that I don't think it's a static site generator. It's more a content management system and I don't think it's generating things statically. Maybe you can, but I'm not sure it is using PHP and it it's rendering at runtime as far as I know. Yeah, that's a whole different conversation, but let's think about it making it simple. So, we generate the articles and obviously you want a static site generator because it's more secure on one hand side and then it's easier to index. So, basically these would be the things that I would think of to need a static site generator. What should I do? Because in the end

**[12:13](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=733s)** if I understand correctly, Rock is using MD files. So, it's using Markdown, Yeah. Markdown. There are a bunch of them, right? >> can use Markdown or AsciiDoc. Okay. So, any of the more programmatic way of writing things. Markdown is a lot more simple. AsciiDoctor is more complex. If you have more complicated stuff and you want to put more stuff in there, it's very powerful. But it's moving away from the what you see it's what you get to a more programmatic way of looking at things and the probably GitHub made MD very very powerful. So, if I understand correctly, we need to have these things in place, right? So, we have the markdowns with the content that you want on our website, right? >> Yes.

**[12:59](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=779s)** Then if we look about the website, the other thing that we need is about styling. How does it look in terms of templating and stuff like that? How is that done in Rock? So, if you want to convert from WordPress to Rock, considering that you can easily convert from HTML to Markdown or to AsciiDoc, I suppose you would have to take your DB as HTML and convert it to Markdown. It doesn't mean that you need to write article in Markdown because you have a lot of editors that allows you to just use it like you would do on Word on any other writing tool and then it will just convert it to Markdown. When you have all your Markdown, there is a structure that you you put your files in and instead of having a DB, you will put

**[13:48](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=828s)** them on the file system. And when you have all your file, you will need templates that direct how you page look like. And that's pretty much it. For styling, you use a Quarkus extension which is named the web bundler. It will take all your JavaScript, all your styles, bundle them to make them production ready and make them available to your application and without any configuration. So, that's out of the box. Okay. So, if I get it correctly, you'll use a folder structure for your hierarchy where you're just putting the things one after the other and then you use MD files or AsciiDoctor two types of are done. And in terms of templating, you need another Quarkus extension that will take care of the web stuff and just bundle it and that's it. Yes.

**[14:36](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=876s)** How about the footprint? If I'm looking at the normal application, so just out of the box without any kind of tinkering around, what should I expect in terms of amount of resources that I need? Is it huge? It's decent. Can I run it on, I don't know, Raspberry Pi? Can take a very small space in the cloud and just run it. What should I think in terms of running it? When you you're a developer, you will use Quarkus to develop the base of the website. If you're a writer, you can use Quarkus and the file system to edit content. You can just do it on the file system. We are building a CMS as part of the UI. So, as a writer, you will be able to just create, edit like you would do on WordPress with what you see and what you get and everything. So, for writer, it's pretty cool. And then you have the

**[15:25](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=925s)** generating part where you generate all the pages and out of that, you get all the pages that you can run on any static server. So, you could start it on Nginx or Apache or whatever. It's just static files. So, it will work on a Raspberry I suppose. Okay, great. So, there are two different things to that. It's up to me what I get. So, in the end I'll just get the content. It depends on me where I put it. And then behind it, it's the engine that actually does the transformation, right? Did I understand correctly? Yeah. And the engine is pretty light. So, you you could also say that both parts are quite light. How friendly would it be for non-programmers? Is it enough to just tell them, okay, write an MD file and just drop it there? So, we actually have already the case where users are not

**[16:13](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=973s)** Java friendly. Writers are not Java friendly and they've been using it on different site and feedback were good compared to the other like Jekyll or Hugo. So, yeah, it's pretty easy to use and it will be even more easy very soon because for now you need the JDK installed on your machine, which can be a burden for people. If it's already installed on most machine without you knowing, but if you don't have it, that can be a problem. And we are building a small wrapper so that anyone can start developing or writing without having anything on his machine, which I think it's pretty cool. I don't think there are any other SSG in which you can do that. Okay. So, let me see if I get it correctly. Is it way to bootstrap yourself like, I don't know, it as it was the Gradle

**[17:01](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=1021s)** wrapper in the lack of a better example where I just got everything. I just started it and that's it. That's what you have in mind? >> Yeah. And how I would I get my hand on that? It's just downloading it or it's installed through Brew or what do you have in mind, guys? So, that's still to figure out. We're really working on making the story as streamlined as possible and there are still pieces missing, but we want them to be there. Even starting a binary can be hard for writers, I think. Some are not using the terminal and I'm not sure how we could do that, but in the end, when you start Quarkus, it could be a really small app that just spin up the local server and then you do everything on your browser, which is local. This is something we want for Rock. It's not there yet because it's pretty fresh,

**[17:49](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=1069s)** but that would be cool. Well, good luck with that. Let's see how cool it is. And then, what else should we know about Rock that I didn't ask? I've been working on the web bundler extension for Quarkus. This is the one that lets you add JavaScript, styles and libraries without you configuring anything. It will just make them prod ready. It can be served on your static server. And I'm working on the V2 and the V2 has out of the box support for Tailwind. I know a lot of people want Tailwind or such UI frameworks to style their website. It's really important for static site generators. So, it's coming and it's it will be soon there. We already have the web bundler, but the V2 will come.

**[18:37](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=1117s)** We also thinking about AI in two places actually. One will be the CMS that will be in the UI where you will be able to write article. It will automatically add tags or guess the title or write part of the article or tell you suggestions about your article, stuff like that. So, you can have AI help you edit content. And the other part where we are considering AI is because everyone is talking about AI now and it's important that we will always need to have content on the web. If you don't have the content, the AI will not be able to build its data and without its data, it won't be able to work. So, for this, you will need to write the content and those generators will need to know how

**[19:27](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=1167s)** to make it friendly for AIs to consume. And we're actually working also on that so that when you use Rock, it will automatically generate all the metadata that is necessary for AI to consume, semantic graph. Yeah, it will be AI friendly for AIs to consume. One last question from me to wrap up and that's more probably for managers than for developers. There are a lot of changes in the IBM/Red Hat ecosystem. A lot of things move from one side to another. Where does Quarkus remain? Is it with IBM? Is it with with Red Hat? Any concerns about the changing license because that was a a topic not long ago. Can you share anything on that point? So, first thing I'm maybe not the best person to answer

**[20:17](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=1217s)** that question, but something I can say is that the fact that Quarkus has moved to Common Cause, which is the most important part, it means that it's fully open source and led by an open source organization. Yeah, okay. So, Quarkus' destiny is tied to Open House Foundation. And that allows it to still remain in the open source ecosystem and that's governed by that organization, right? Exactly. And it doesn't mean that Red Hat and IBM will stop helping it, but I I have not much information on that part, but they're also still building projects on top of it. So, it means that they will rely on it in the future. Okay. Great. Thank you for your time and for sharing all the information. Thanks to you, Olimpio. >> [music] [music]

**[21:12](https://www.youtube.com/watch?v=NDBuBDH-dKo&t=1272s)** [music]
