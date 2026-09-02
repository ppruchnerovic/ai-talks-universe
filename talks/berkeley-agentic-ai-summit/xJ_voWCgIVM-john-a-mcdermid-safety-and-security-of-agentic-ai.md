---
id: xJ_voWCgIVM
title: "John A McDermid - Safety and Security of Agentic AI"
slug: john-a-mcdermid-safety-and-security-of-agentic-ai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: []
channel: "Berkeley RDI"
duration_min: 12
published_at: 2026-08-12T07:30:21Z
video_id: xJ_voWCgIVM
url: https://www.youtube.com/watch?v=xJ_voWCgIVM
youtube_url: https://www.youtube.com/watch?v=xJ_voWCgIVM
tags: []
transcript: true
---

# John A McDermid - Safety and Security of Agentic AI

**Speaker not identified**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=xJ_voWCgIVM) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,718 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=2s)** JOHN A. MCDERMID: Thank you very much. Good afternoon, everybody. And I hope you're still doing well. It's been a long day already. So I've worked on safety of software-intensive systems for around 40 years. By safety, I'm really meaning physical harm to people, the environment, and so on. Over the last 10 years-- or nine years, I've run a program on the assurance of autonomous systems, including AI, which these days is progressively moving to including agentic AI, although they're not deployed that much in safety critical systems these days. Session's about security. Some of the things I'm going to do when the slides appear is to say a little bit about the interaction of security

**[0:50](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=50s)** and safety, and some of the analysis that we're doing there. I'm going to do it around a maritime example, something that we've been working on with some people deploying some autonomous vessels in a different part of the world to hear. But we also do work in other domains on autonomous driving. Colleague here, Yan Jia, has been working on applications of AI in health care and looking at the safety issues there as well, so a wide variety of interests and applications. These days, the center's quite big between faculty, science researchers, and PhD students. We're approaching 100 people. So it's a pretty major research center. And fortunately, we've actually got some slides.

**[1:39](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=99s)** So I'm going to talk a say about safety and security of agentic AI, but doing so trying to illustrate some of these ideas in the context of maritime operations because that, gives an idea of the nature of the problem. So interestingly, of course, my slide buildup hasn't worked. But I'll talk around that. So really, the motivation here is to understand, as we progressively introduce agentic AI into cyber physical systems, how we manage that. And traditionally, safety and security have been assessed independently, done in isolation. With the sort of systems we're talking about, cyber attacks can cascade through the technical system, through perception systems, and so on,

**[2:30](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=150s)** to lead to unsafe effects. We use the term "hazards" as something that threatens physical or equipment or personnel safety. Introducing AI changes both the security and the safety issues quite substantially. We have a much bigger attack surface. We have training pipelines as well as the operating system. But actually, we have a physical system. Then the physical environment is part of our threat surface as well. And this little example-- not ours, one we borrowed from somebody else, but they took an AI algorithm and trained it to detect weaknesses in a perception system. And what it did is then it printed out stickers to stick on a stop sign so that the perception logic decided

**[3:22](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=202s)** it was a 45 mile an hour speed limit. 93% accuracy in the lab. 83% in the real world. So these sorts of physical attacks are real. Safety is based around models of cause and effect. So in essence, what we've been doing is building world models that represent those causal structures we call SCWM, Structural Causal World Models. There's a lot of interest in AI about automatically learning world models. These are things we describe explicitly ourselves and actually bind security into those structures. To give you an example, this is not the real system we've been working on, but is very representative of it. It's an unmanned surface vessel. IMO, International Maritime Organization,

**[4:13](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=253s)** to them, degree 3 autonomy means it's largely remotely operated but can operate autonomously without remote interaction if necessary. So we've built a simulation of this with a YOLO object detector. But there's then what we call a dropout protection module. It falls back onto completely autonomous function on the vessel, if it loses its communication, back to the remote operating center. That can happen for all sorts of reasons, such as jamming and so on. There's other things we have to worry about. AIS is something that tells other vessels where you are. You can spoof that. Lots of other things we can worry about. So what we're doing here is talking about a compound attack.

**[5:03](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=303s)** I said we can do physical attacks. So this example is using a classical digital attack, network intrusion, but also physical attack at the same time. So I've outlined some details here of an exploit in the simulated system we've built. The details aren't particularly important. But what the nature of the attack is, it's a denial of service attack on the remote operating center, so it can no longer control the vessel. So the immediate effect of this is this protection module on the vessel kicks in. It operates autonomously, continuing to follow the agreed path to transition through the piece of the ocean it's actually on. But separately, I showed you this example of a physical attack.

**[5:54](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=354s)** This is an unmanned surface vessel out in the water. So you fly a UAV and actually put in front of the cameras an image, which means it either doesn't detect the vessel at all, or it detects it as being something completely different, for which it needs a different evasive maneuver. So this means that this approaching tanker is either not seen or is completely misclassified. To either of these, independently-- and actually the result is safe. I fall back onto this DPM. The vessel operates safely. I spoofed the cameras. But actually, the remote operators will realize that, because they get a data feed and they will take appropriate action. If I do the two together, then I end up creating an unsafe state. And the idea of this little graph

**[6:44](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=404s)** is to show how those failures, in fact, the two initial attacks, propagate through the system to end up with a vessel that's maneuvering, but not knowing this tanker is in front of it. So it's not going to take evading action. So we've got something on a collision course. And I've said we would model this. So this idea of these structural causal world models is they have four layers. The top layer is an ontology. It's describing those things in the world in which I'm working that matter. So an example here is wave height. That matters because the force of waves on a vessel alters its maneuverability. We then, below this, actually try to model uncertainty. Actually, it matters in lots of ways.

**[7:33](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=453s)** But in this particular context, you won't be able to work out exactly what the wave patterns interacting with the vessel are. So it's an uncertainty about how the sea state will affect the motion of the vessel. And this gets mapped down into some bounds on uncertainty. So what we can then do at the bottom level, for those of you who like formal methods, you can actually verify the behavior of algorithms at this level. You can say, I can actually set some bounds on the uncertainty, and I will operate safely within those known bounds. This is how our model works. And so when we talk about security issues, what we can do is we can view the attacks as interventions on this causal graph of dependencies. I should actually have said, I'm only highlighting four nodes.

**[8:24](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=504s)** You'd build a causal dependency graph of all the things that matter in the particular situation. And the security events perturb those relationships. And we actually propagate through the effect from the attack to some ultimate deviation in a safety metric. In this particular case, the metrics we're interested in are the closest point of approach to the other vessel. The smaller that is, the more dangerous it is, the more likely we are to have a collision. And then the time to closest approach-- time really matters, particularly depending on how big the vessel is and how maneuverable it is. You need to be able to predict the closest approach much further out to give enough time for the vessel to maneuver. But the attack then can propagate

**[9:14](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=554s)** through these causal structures, degrading the estimation of the position of the vessel, actually changing its beliefs, in the case of the image attack, about what's actually in front of it, so leading to the degradation in this safety metric, the closest point of approach or the time to that. So what we are able to do is to find ways of actually integrating analysis of physical safety. And both classical security approaches are more on conventional approaches made by spoofing cameras, physical attacks. But in the real world, we have to carry on worrying about all those classical security concerns. But as a summary, so the use of AI

**[10:07](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=607s)** and these cyber physical systems introduces new challenges. We have a much expanded attack service, training data, prompts, context, if we're using large language models, and so on. There's a physical attack surface as well. Spoofing images is the obvious one. But you can actually do that in other electromagnetic domains, for example. But actually, one of the things that we tend not to worry about in safety, or to an extent in security, is time ordering of events. And one of the reasons we wanted to analyze this is that it actually shows that the temporal order of events can actually overcome-- defenses might have made one agent secure. But actually, by changing the time ordering of events, I can actually undermine the safety and security

**[10:56](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=656s)** of the agentic ecosystem. So conclusions are that we actually need to work on new analysis approaches that integrate safety and security. What we've done based on these structural causal world models is one possible approach to doing this, which actually we're currently extending to include ideas in the world model of the shared understanding between the agents and humans, where we have dialogue interfaces. Really, the main thing I wanted you to take away from this is, if you work on security, please come and talk to we guys who do safety. There's new challenges that arise at the interaction of those two issues. If we don't look at them together, we're going to deploy systems that have very undesirable effects when they get into the physical domain. Ladies and gentlemen, thank you very much for your attention.

**[11:45](https://www.youtube.com/watch?v=xJ_voWCgIVM&t=705s)** Cheers. Bye.
