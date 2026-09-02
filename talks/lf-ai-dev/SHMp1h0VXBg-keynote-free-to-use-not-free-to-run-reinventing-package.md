---
id: SHMp1h0VXBg
title: "Keynote: Free to Use, Not Free to Run: Reinventing Package Registries - Robin Bender Ginn"
slug: keynote-free-to-use-not-free-to-run-reinventing-package
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "Open Source Summit + ELC NA 2026"
year: 2026
speakers: ["Robin Bender Ginn"]
channel: "The Linux Foundation"
duration_min: 12
published_at: 2026-06-03T18:16:02Z
video_id: SHMp1h0VXBg
url: https://www.youtube.com/watch?v=SHMp1h0VXBg
youtube_url: https://www.youtube.com/watch?v=SHMp1h0VXBg
tags: []
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# Keynote: Free to Use, Not Free to Run: Reinventing Package Registries - Robin Bender Ginn

**Robin Bender Ginn**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit + ELC NA 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=SHMp1h0VXBg) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Keynote: Free to Use, Not Free to Run: Reinventing Package Registries - Robin Bender Ginn, Executive Director, OpenJS Foundation

The package registries that distribute software across every major open source language ecosystem, from Python and Rust to JavaScript, Java, PHP, and beyond, will collectively serve over 10 trillion downloads in 2026, all of them free. But the infrastructure behind those downloads has never been free, and the small number of donors and volunteers quietly absorbing those costs can no longer keep pace with AI-driven demand and machine-scale supply chain attacks. In response, registry leaders have formally convened under the Linux Foundation to reinvent the model through the newly formed Sustaining Package Registries Working Group. This keynote explains what's breaking, what's changing, and what it means for every organization that builds on open source.

## Transcript

*1,732 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=0s)** Good morning. Let's just start with something simple. You all paid to be here, right? Flights, hotel, tickets, time. Because you know this experience, this infrastructure of people and ideas, has values. Now, imagine walking in here and saying, "Hey, you know, I'd like all this for free. You're all open source, right? Open the Linux Foundation?" Well, of course that sounds ridiculous. And yet, that is exactly how most of the world treats open source infrastructure. Not the code, but the infrastructure behind it. So, you know, we've built an industry on a powerful idea, something I'm very passionate about. Open source is free. It's we free to use, free to download, and of course the wonderful community

**[0:47](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=47s)** that freely builds upon it. And that part isn't changing. But here's what we've overlooked. Free to use has never meant free to run. Open source being free is not the problem. It's the promise. The problem is assuming that infrastructure, the infrastructure behind that promise, has no cost. So, you know, if you think about it, we've quietly turned open source into something else. We've kind of turned it into the equivalent of free overnight shipping of software. You know, click a button, dependencies show up instantly around the world, just like magic. No friction, no second thought. But you know, anyone who's ever run a

**[1:33](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=93s)** logistics system knows that overnight shipping isn't free. It's one of the most expensive systems you can operate. You have warehouses, routing, people solving problems, abuse prevention, and that's exactly what package registries have become. They become a global, a real-time distribution network for software. And we've been treating it like it runs on goodwill. So, think about the scale of registries. It's just staggering. 10 10 trillion downloads in 2026. That's across ecosystems. So, JavaScript Python Java Rust PHP Ruby. That's over a billion per hour. And so, that's what we're kind of calling industrial infrastructure.

**[2:23](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=143s)** And for years, you know, it's kind of worked. But, in reality, a small number of people have been carrying this enormous burden. You know, registries today, they often survive on infrastructure credits from some wonderful partners. A lot of small teams, often volunteers. Many registries, and I know there's some registry owners here, are just run by one person. So, you know, people again, they're doing the hard work and critical work because they care. But, goodwill is not an operating model. And for years, again, that was just barely manageable. But, you know, today, of course, the baseline changed. And as we know, modern apps aren't built on 10 dependencies. They're built on hundreds, and gosh, I know with JavaScript, often thousands. And so, AI often didn't

**[3:12](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=192s)** create the problem. It just accelerated an existing curve. So, you know, this week I pulled some just some data points from a few of my projects at OpenJS. And if you look at NPM, and downloads are just exploding. Many 50% in the last quarter. I even looked at Lodash this morning. Now, two months ago, when John David Dalton calls me, he goes, "Hey, Robin, we're like, we just passed 100 million downloads a day." Well, yesterday it was 155 million a day. That's just barely 2 months. So, if you think about, you know, just a few of these projects, Express powers apps, Lodash is just buried deep in the dependency tree. Almost in almost everywhere. Undici powers modern Node

**[4:00](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=240s)** networking. So, you know, different layers, same trend. And again, these are not trendy AI frameworks, not that they're trendy, they're foundational JavaScript infrastructure. Um and all of this is changing um because the consumer changed. So, if you think about NPM, NPM is no longer just serving human developers. Um it's serving automation, CI, cloud environments, build system, and of course AI agents. So, we've essentially moved from human-triggered installs to machine scale consumption. But here's the deal, and you already know how this ends. When infrastructure gets stretched, the impact doesn't stay hidden. Many of you you probably all

**[4:47](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=287s)** feel it, right? Slower incident response, more supply more supply chain risk, and the trust starts to erode. So, what essentially looks like an infrastructure quickly becomes your business problem. Uh Brian Fox, who I think is out here somewhere at Maven Central with Sonatype, he said it well, "Open infrastructure became the free extension of private optimization." Uh he described one default enterprise workload can trigger 80,000 downloads of the of the same artifact a week. That's in 40 terabytes in 24 hours. Uh another common problem he's experienced, uh React Native build scripts pulling debug and release binaries via curl. It adds 27 terabytes

**[5:37](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=337s)** a day. So, you know, really no one is really behaving irrationally. They're just, you know, companies are optimizing for speed right? But unfortunately, the shared infrastructure absorbs the costs. And that's the shift. Package registries are no longer just dependency servers. They've quietly become uh runtime infrastructure for global systems. So, you know, from the outside, registries can look deceptively simple. Upload a package, download a package. But what's really being managed today is trust. Because when trust breaks, the consequences scale just tremendously. Um if you think it Take a look at Axios that happened about a month ago as an NPM um issue. Um Axios is one of the most widely used JavaScript AT-HTTP

**[6:28](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=388s)** libraries in the world. And that one compromised maintainer account briefly turned one of JavaScript's most trusted packages into like a a malware delivery path. And the malicious versions were only live for a short time, but when you look at Axios and how deeply embedded it was in everybody's dependencies, the supply chain risk and attack did not take long. And that's why this just isn't package hosting, it's critical infrastructure. Um but good news, here's the important point. This isn't quite theoretical. Um and the market is already adapting. Um the Eclipse Foundation saw the same pressure with Open VSX, which sees 300 million downloads a month. Uh again, they saw the same sort of behavioral shift. AI agents, cloud IED,

**[7:16](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=436s)** CI, again turning human scale usage into machine scale consumption. So, Eclipse adapt adapted and recently, they announced a managed service where the common stays open, developers stay free, commercial platforms at scale pay, and rate limits protect the shared infrastructure. Uh it the the shared service. So, that distinction really matters. So Eclipse is not abandoning openness. It's just updating the economics. Because again, you're not paying for open source, you're paying for industrial scale usage. Um again, Sonatype for Maven, the message was direct. Public infrastructure has been treated like a free extension of private platforms. Um and that model doesn't hold. And we're

**[8:05](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=485s)** seeing it happen beyond package registries. If you look at the Linux vendor firmware service, they have more than 145 million updates delivered. Same pattern. Critical infrastructure scaled way beyond the model, the funding model. And the cool thing is Dell and Lenovo stepped up. So different infrastructure, same economics. So today I'm here not just representing JavaScript, but my friends uh across the open source language ecosystems working on this together. Um and the conversation didn't start today. Um registry leaders have already been sounding the alarm. I don't know if you saw some of the open letters that we've uh released in the last few months. Our first one kind of made the point that open infrastructure is not free. Um and

**[8:55](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=535s)** then we recently released a second open letter uh really focused on the really operational burdens and what it takes to run a registry at scale. Um and really the message is uh free to use does not mean free to operate. Um again, AI is only adding to the pressure. Um and so if you think about the folks running these registries, we've been meeting weekly 7:00 a.m. Um great friends from uh PyPI, RubyGems, crates.io, Packagist, Open BSX, and other friends uh from Open SSF to the CD Foundation, Pearl, and what have you. Um so again, this is not about any one registry. Um and so many again of these registries are running at nonprofit foundations who are really committed to keeping the open

**[9:44](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=584s)** infrastructure open and trusted. But again, an open mission does not solve structural economics. So that's why we just recently launched the sustaining package registries working group at the Linux Foundation, which I'm proud to be a part of. Um but the one important thing to note, uh this is not about charging developers or restricting access. It's about aligning cost with value for industrial scale commercial consumption. Because these systems are really just too interconnected for anyone registry to solve alone. So let's uh think about what are we actually doing in this working group? And again, we've just started, but we're really excited. We have a charter um on GitHub, and first we're tackling economics. Again, the hard question, how

**[10:33](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=633s)** do we fund the infrastructure, the operations, the governance, and the people who are working to to keep these systems running? Um second, governance. Where can we collaborate on on common areas? Because no registry wants to reinvent legal terms, terms of use, policy frameworks, or commercial models alone. Um and third, communication is the really an important part of this um and setting expectations uh with those who are using our registries. Um and again, the industry is treating this like infrastructure, like it's costless, but we really are getting more clear and more aligned about what sustainability actually requires. So you know, our message again is open structure, open infrastructure has become essential infrastructure. And as we know, it powers every app, every

**[11:22](https://www.youtube.com/watch?v=SHMp1h0VXBg&t=682s)** company, every AI system. Um and here we share the same value. And our responsibility is to is to sustain it collectively too. So, I just want you all to be on the lookout for your favorite package registry. You may see some of them changing their business models um because we recognize that if the sustainable models don't emerge, some of this infrastructure won't survive in its current form. And as one registry owner said in our working group, "Gosh, you know, we just might simply go out of business if things don't change." So, with that, I'll leave you all. Thank you. >> [applause]
