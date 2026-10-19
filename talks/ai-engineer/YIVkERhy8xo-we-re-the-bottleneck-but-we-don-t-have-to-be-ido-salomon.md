---
id: YIVkERhy8xo
title: "We're the bottleneck, but we don't have to be — Ido Salomon, AgentCraft"
slug: we-re-the-bottleneck-but-we-don-t-have-to-be-ido-salomon
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Ido Salomon"]
channel: "AI Engineer"
duration_min: 15
published_at: 2026-09-27T14:30:07Z
video_id: YIVkERhy8xo
url: https://www.youtube.com/watch?v=YIVkERhy8xo
youtube_url: https://www.youtube.com/watch?v=YIVkERhy8xo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "AgentCraft", "Ido Salomon", "MCP Apps", "MCP-UI", "agent orchestration", "coding agents", "Claude Code", "developer tools", "AI UX", "gamification", "multi-agent", "human-agent collaboration", "software factories", "AI Engineer", "AI Engineer World's Fair"]
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# We're the bottleneck, but we don't have to be — Ido Salomon, AgentCraft

**Ido Salomon**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#AgentCraft` `#Ido Salomon` `#MCP Apps` `#MCP-UI` `#agent orchestration` `#coding agents` `#Claude Code` `#developer tools` `#AI UX` `#gamification` `#multi-agent` `#human-agent collaboration` `#software factories` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=YIVkERhy8xo) · [Conference site](https://www.ai.engineer/)

## Description

If agents are so capable, why doesn't everyone have an army of them? Ido Salomon, creator of AgentCraft and MCP-UI and co-creator of MCP Apps, argues the bottleneck is us: steering, directing and reviewing agents at scale is exhausting. The skills we need already exist, though. We learned them from games like Warcraft and StarCraft.

Salomon demos AgentCraft, an orchestrator styled like a strategy game. Agents appear as units on a map, your file system becomes the terrain, heat maps show where work is happening, and the space bar jumps you to whatever needs attention. He shows how it adds visibility, autonomy (with orchestrators, loops and a review kit with visual evidence) and collaboration, through shared rooms where people and agents work side by side. Then he turns to lowering the floor: an early, simpler mobile-game-style mode aimed at the 90% of people who aren't power users yet.

Speaker info:
X/Twitter: @idosal1 (https://x.com/idosal1)

Related links:
MCP-UI: https://mcp-ui.dev

Timestamps:
0:00 Intro
0:35 If agents are amazing, why aren't we unstoppable?
1:10 We are the bottleneck
1:50 Lessons from video games
2:20 Meet AgentCraft
2:50 Agents on the map
3:40 Buildings: plugins, skills, terminal and git
3:55 Raising the ceiling: visibility
4:25 Your file system as a map
5:00 Jump to what needs attention
5:40 Too much to hold in your head
6:15 Quests
6:40 Autonomy: orchestrators and loops
7:35 The review kit
8:25 Collaboration: shared rooms
10:45 Lowering the floor
11:50 Loopers: a simpler mode
13:28 Wrap-up
13:50 Try AgentCraft

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*2,550 words · source: supa (en, exact timings)*

**[0:21](https://www.youtube.com/watch?v=YIVkERhy8xo&t=21s)** Okay. Hi everyone. Uh I'm Solomon. I am the creator of ATMCraft and I also created MCPUI which became MCP apps and MCP steering committee. I've done a bunch of other stuff. Uh but we're here to talk about why we're the bottleneck and why we don't have to be. So, uh as you all know and use every day, agents are amazing. There's so much they can do uh from generating cat memes to B2B SAS apps. So if they are so amazing, we have to ask why aren't we all unstoppable? Why doesn't everyone have an army of agents that just does whatever they want? So it should be relatively easy. I mean you just have a bunch of monitors and you spin up 25 cloud code agents and you're done. So

**[1:09](https://www.youtube.com/watch?v=YIVkERhy8xo&t=69s)** the reality is that it's just not that simple to do something like that. you need to a really want to use agents and secondly once you actually spin them up each one of these agents requires you to steer them direct them review them and when it's at scale especially it's just exhausting we need to find the skills to allow us to do it without burning out so in reality we are the bottleneck and the the cool thing here is that while we are the bottleneck The skills that we need to do these things to uh find ourselves not burning out every time we use an agent are with us all along. Uh if you try to compare it to other stuff that you've been doing

**[1:57](https://www.youtube.com/watch?v=YIVkERhy8xo&t=117s)** outside of programming, for example, playing video games, it's not really that different. Like if if you're playing Warcraft, for example, or Sims, and you have a bunch of different uh units running around, you need to understand what they're doing and supervise all of it. How different is that from from actually inspecting agents? So I took this concept uh too far and I created agent uh which is a game inspired orchestrator uh that tries to bring all that good stuff together into work. So let's take uh a quick look of what that actually looks like and try and understand the journey that we can go through to really raise the ceiling of how humans and agents can collaborate. So, uh, this is AgentCraft. Uh, there's really a lot to unpack here. Uh, so

**[2:46](https://www.youtube.com/watch?v=YIVkERhy8xo&t=166s)** we'll just go through the basics really quick. Um, what you see here is an agent. Uh, it's an actual representation of a cloud code or openclaw, whatever agent that you can imagine. Uh, it can be detected on your device or you can actually spawn new ones directly from a craft. Uh, so like I said, you have like codecs and uh, open code etc. at your command. >> Uh, and these agents can do everything. They're just normal agents. Uh, so I can just prompt them in this nice side panel that also has voice. So there's multimodality here. Uh, and just do something for me. >> Prompt. Prompt. >> And now these agents can do whatever. Uh, and if you look around you would see

**[3:35](https://www.youtube.com/watch?v=YIVkERhy8xo&t=215s)** that the map has a a bunch of different elements. So you have buildings. These buildings represent functionalities. So for example, if you can manage your plugins or skills, uh you have like integrated terminal, integrated git, uh you can do in your all of your work from within this space. So now that we have this and we understand the basics, let's look at what we can do uh to raise the ceiling. So the first step is obviously visibility. I need to understand what's going on. What are my agents doing? So, I have this nice side panel and it shows me the different agents and what their task is and what the last thing they did is and what they're currently doing. Everything I need to quickly understand who needs my attention and who doesn't. The second part of it is we're not just limited to this. We have a map. So, I can take let's say my file system,

**[4:25](https://www.youtube.com/watch?v=YIVkERhy8xo&t=265s)** project it onto the map, and now I can see exactly what my agents are doing. Not just by looking at a list of stuff. I can actually see okay this agent is now working on this directory or this file and these files are represented as runes on the map. So I can really look at each one and see exactly what each agent did and when. And now I can take this nice information because we are the orchestrator uh and use that to create linkages and now I can create cool stuff like heat maps. So I can really easily see what's going on. And the the other aspect is that now that we have this visibility, that's not really enough. We need to be able to react to what's going on. If someone needs my attention, I need to be able to quickly jump to it.

**[5:12](https://www.youtube.com/watch?v=YIVkERhy8xo&t=312s)** So much like video games or RTS games or Civilization, whatever, you would click uh spacebar and it would just take you to the nearest thing that actually needed your attention. So you can really easily understand what's going on. and jump from one thing to the other and answer questions or approve plans, etc. That was nice. I mean, it's a nice step just to have that visibility, but it's not really enough. It's pretty exhausting to keep looking at what the agents are doing in the granularity of what files are they using and what tools are they using at the moment. So, we need something else. Uh and the reason is that we have like two two main problems here. Uh one is that there's just too much to hold in our heads. Even if I can understand what's going on and

**[6:00](https://www.youtube.com/watch?v=YIVkERhy8xo&t=360s)** I can see everything, I can't really do like 20 things at the same time. I can't even think of the next thing I want to do if I have this, you know, huge coding project or whatever. So I need to find some way to fix that. Uh so we can I mean we can tell the agents uh you know go through my codebase, find out what the next things I need to do are, create these tasks for me and I just click a button, I accept the quest and there's some agent that does it for me which is fun. Uh it's cool. Uh but the next problem here is that okay now I have 20 stuff going at the same time and I have to babysit each and every one and that is completely exhausting. So you could ask okay we have agents agents are amazing as we've established so I can just go ahead and tell the agent to do it for me now it's called software

**[6:49](https://www.youtube.com/watch?v=YIVkERhy8xo&t=409s)** factories but at the time it was just doing stuff autonomously uh so you can give it like a general sense of what you want it would spawn an orchestrator and break it down for you and run it all in well in this case it's a local uh container so everything is just done in isolation and I don't need to do any babysitting the agent does it for me. On top of that, you have loops, which everyone really likes right now. So, you can do cool things like just tell it to, I don't know, scan Twitter for cool stuff you want to build or scan your GitHub, and it will just create these nice uh features for you in the background without you needing to do too much up front. The bad thing is that I mean this is nice uh but what do I do when I have again I don't know I would say 20 but

**[7:37](https://www.youtube.com/watch?v=YIVkERhy8xo&t=457s)** even five things to review at the same time. Uh it's very very hard to get that out of the way. So what I did is create uh this like review kit. So I get the entire changes I need and I get uh what files changed if you want to go like file by file or you can get just get visual evidence. So you can actually see videos of what changed or photos of what changed so you can really quickly understand what you want or even run a few uh instances in parallel and just pick the best implementation out of these. So now that we have this we have uh visibility and we have autonomy uh it's pretty cool like we reached a pretty good place in raising the ceiling of what we can do with agents but it's still pretty exhausting. I mean it's it

**[8:25](https://www.youtube.com/watch?v=YIVkERhy8xo&t=505s)** was fun. Uh, but now I have to ask myself, do I really need to be the only one doing this? It's pretty lonely to just talk to agents all day and trying to and you know, if you look at uh what a team does, for example, if it's just me, that's fine. But if I have a team, I might not even be the right person to review what's going on. So, I need something else. Uh, and that something is collaboration. We can just have other people join us. So the way that looks in agent craft is that I can create these uh you can call it you know war halls war room whatever uh host them it's like completely local but you can do like tunnels and people can join you h so I can create a room and let's say I have a product designer in my team in this case

**[9:13](https://www.youtube.com/watch?v=YIVkERhy8xo&t=553s)** uh it's my wife and I can approve uh her otherwise she'll be mad uh so I can approve her and she does her thing she designs whatever and I as an engineer can not only see that that's that's her um I can not only see that on my map uh I can actually take that and follow off off of it >> prompt prompt >> yeah that's just like her um so I can take that design follow up on it implement it while she keeps working uh and the cool thing here is that not only can I hand off or fork and kind of have this shared workspace so I'm not really bound anymore or to Git. I can use Git, but I'm not really bound to something. Everyone is working together. Uh you can see that there's also some kind of chat between not only between the people

**[10:03](https://www.youtube.com/watch?v=YIVkERhy8xo&t=603s)** within the room, but also between agents. So we can have this really nice notice board of exactly what each person is doing, what each agent doing. They're all aware of each other and they can collaborate much more closely uh than you normally would be able to do. Uh so for example, here I can say, okay, I took off this design task. Uh so now we have oh by the way this is also from devices you can have like mobile and and if you like telegram you can use telegram whatever floats your boat. So we have visibility and we have autonomy and we have collaboration so we managed to raise the ceiling. Uh it's now possible especially if you're power users to do really cool stuff and use more agents and do more things. But the interesting thing here was, you know, if

**[10:50](https://www.youtube.com/watch?v=YIVkERhy8xo&t=650s)** I looked at the feedback I got, it's not just that power users were able to do more. The cooler thing for me was that people that had even nothing to do with agents or nothing to do with productivity, uh, come and say, uh, okay, my kids really loved it and they use it all the time to to orchestrate agents, which they didn't do until now. uh or you know someone that flunked out of college because he played Starcraft and now you can suddenly do really productive stuff with it. Uh and a bunch of other examples of kind of bringing communities that so far were kind of behind into this new world of productivity. So we need to raise the ceiling but we also need to uh lower the floor. We need to have some kind of way to take no probably around 90% of the people in the

**[11:39](https://www.youtube.com/watch?v=YIVkERhy8xo&t=699s)** world and bring them into this hygienic future without having them burn out. So again, I took it too far. Um, and there's this uh currently named TBD um potentially loopers. Uh the idea here is okay why don't why do we need something like you know Warcraft which is potentially very complicated uh especially or might be even daunting if you're not into the granularity of what files are there are or how uh complex the UI is and kind of try to find a lower denominator of what makes stuff accessible especially now that agents are much more capable so instead of granularity or having like exactly what files they're working on maybe I can have it more of a mobile game level uh have projects that they keep returning

**[12:27](https://www.youtube.com/watch?v=YIVkERhy8xo&t=747s)** to and use loops and other stuff that rely on agents being more autonomous to have like a very basic level of I prompt I get the result I don't really care perhaps about the way I can see it if I want to and I have this really nice interactive and cool experience that makes me want to come back to this and obviously I mean this is one visualization uh it can really resonate with some people but might not might not present to others because we're not all the same and what may appear like amazing and easy to one person can appear very difficult to another. Uh but here uh I'm trying to look at a way to make this more customizable. Try and understand what it is that you as a person need in order to understand and

**[13:15](https://www.youtube.com/watch?v=YIVkERhy8xo&t=795s)** want to use these tools. So this is a very very early draft. Um but if you want to use it, please let me know. So we're the bottleneck. I think we've established that uh pretty well until now. But the skills that we need to stop being the bottleneck and enable this new future are already with us. So we are the bottleneck, but we don't have to be. And I hope that you all can take what's relevant to you and your life and apply it forward. So I would ask you for two things. One, agent is already out there. Like you can just npx install agent as a website uh and do your thing. Uh this new thing that I just showed you uh potentially loopers uh is still experimental. I'm still trying to understand the interest

**[14:05](https://www.youtube.com/watch?v=YIVkERhy8xo&t=845s)** and what people are actually looking for to uh get the floor that they want or the ceiling that they want. So, please uh go here and express your interest and tell me what you're looking for so I can know what to do with this. And thank you. I got it.
