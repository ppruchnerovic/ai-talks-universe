---
id: x4e5O9zN0TE
title: "Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati"
slug: long-horizon-agents-need-experiments-not-just-prompts-erina
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Erina Karati"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-09-26T16:30:29Z
video_id: x4e5O9zN0TE
url: https://www.youtube.com/watch?v=x4e5O9zN0TE
youtube_url: https://www.youtube.com/watch?v=x4e5O9zN0TE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "autoresearch", "multi-agent systems", "long-horizon agents", "AI agents in games", "Project Paradox", "Supercell", "agent memory", "RAG", "agent evals", "AI village", "generative agents", "Erina Karati", "Arunachalam Manikandan", "game AI", "AI Engineer", "AI Engineer World's Fair"]
topics: ["Agents & orchestration", "Evals, observability & reliability", "Prompting & context engineering"]
transcript: true
---

# Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati

**Erina Karati**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#autoresearch` `#multi-agent systems` `#long-horizon agents` `#AI agents in games` `#Project Paradox` `#Supercell` `#agent memory` `#RAG` `#agent evals` `#AI village` `#generative agents` `#Erina Karati` `#Arunachalam Manikandan` `#game AI` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=x4e5O9zN0TE) · [Conference site](https://www.ai.engineer/)

## Description

In a game village full of AI agents, a rumor about a sale on mangoes goes wrong. Pass it along a few times and the agents forget who said it, or start treating "might" as fact. Erina Karati, a former engineer at Microsoft and Supercell, built Project Paradox with Arunachalam Manikandan at Supercell's AI Innovation Lab. It's a framework for game agents with their own memory, emotions and trust scores. It worked well in short scenes but broke down over long ones.

Their fix was to wrap the village in an autoresearch loop. They run controlled scenarios like spreading a public fact, a rumor or a change of plan, collect traces, and score the results on a balanced scorecard: reach, source retention, uncertainty preservation, replanning and privacy. The loop can only change a small, frozen policy surface, and changes are kept only if the scorecard improves. Karati's lessons apply well beyond games: memory alone isn't enough, you need to know where each fact came from, rollback isn't optional, and long-horizon agents need experiments, not just prompts.

Speaker info:
Erina Karati
X/Twitter: @erinakarati (https://x.com/erinakarati)
Arunachalam Manikandan
X/Twitter: @Arunachala64250 (https://x.com/Arunachala64250)

Related links:
Supercell: https://supercell.com

Timestamps:
0:00 Intro
0:43 Project Paradox
1:18 What the agents can do
2:53 A stateful architecture
3:33 Trust scores and memory importance
4:28 Demo: a picnic
5:08 Where long-horizon behavior breaks
6:43 Bringing in autoresearch
8:13 Autoresearch outside the village
9:23 The loop
10:43 Controlled scenarios
12:33 The mango rumor, fixed
13:03 A balanced scorecard
14:33 Keep the editable surface small
15:43 Example policy changes
16:33 Being careful with claims
17:03 Memory is not enough
17:48 Rollback is not optional
18:23 Beyond games
19:33 A recipe for long-horizon agents
20:13 Closing

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*2,724 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=12s)** Hi everyone, I'm Arena, former engineer at Microsoft and Supercell. And today I want to talk about auto research in a multi- aent AI village. I will use a video game like AI Village as a running example here, but the broader question is one I think many AI engineers are starting to run into. How do we evaluate and improve agents that carry state over a long period of time? Before I get into the auto research layer, I want to talk a bit about project paradox. We developed project paradox at supercell's AI innovation lab. Me and my teammate are natural money. We built a modular AI framework that

**[1:02](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=62s)** allows any developer to plug in intelligent autonomous agents within a video game that can interact, compete or cooperate with other players or agents as well and place them uh and make them into dynamic game companions. Now to give examples of what these agents can do, the agents can move with intent. They can go to any location or person and they're guided by their own memories, emotion, or curiosity. These agents can interact with the world. They can pick up objects, drop them anywhere, and they're also aware about the context in their own environment, such as the objects or other characters or agents as well. I would also like to note that game

**[1:51](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=111s)** developers can also add new actions for these agents to accomplish within our framework as well. Instead of just dropping or uh placing objects, agents can also obviously react to what's happening around them. And these events that happen around them affect their own beliefs and emotions on the fly as well. And of course, it wouldn't be complete if agents can't start conversations, right? agents can in this scenario approach other agents or even the player as well and this makes the game feel more alive. And of course these conversations are stored within their memory and is according to their own um and affect their own emotions and

**[2:40](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=160s)** beliefs or goals as well. And al together these agents make our multi- aentic framework. Um yeah yeah one second so the architecture was intentionally stateful behind this. The first important part was per agent memory. Each agent has its own memory namespace backed by rag. So memory did not bleed between agents. Second, we tracked emotion as a small vector. So after an event or conversation, the system could update values like joy, sadness, fear, anger, or disgust.

**[3:29](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=209s)** Third, agents had belief scores towards other agents and the player. You can think of this as a trust matrix. Basically like after the interaction happens, the LM basically decides whether the trust score should go up, down, or whether it shouldn't change at all. And fourth, every memory receives an important score. Um to to explain this better, like let's say you had dinner a few days ago, you probably wouldn't remember what you had for dinner, right? But um if someone was murdered a few days ago, you definitely remember that. So the agent will evaluate or the LM will evaluate uh an important score of an event and if it crosses a threshold, it will store that specific memory uh in a

**[4:20](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=260s)** separate cache so that important context can be retrieved better later on. And here's an example of it just working. Um, we going to ask one of the characters to go on a picnic with us. Here, uh, our character Blossom um, decides to pick up a pastry and go to the picnic area because we asked her to do so. Keep in mind during the conversation in the background, she plans all of these sequence of actions to accomplish. And one when we talk to her afterwards, she will also reply within context as well. Yeah. But this is where an interesting problem

**[5:09](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=309s)** actually started. As you saw in the last example, like for shortterm game play, this our architecture worked pretty well. like a character could make a plan, move around, talk and remember the recent interaction and respond to us or other characters as well. But over longer horizons, this is where we notice the social consistency start to get weaker. So in this example, we have one agent spreading a rumor about a sale on mangoes to another agent and that agent receives that information and goes and tells another agent about it. Later on, after a number of events that occurred in between, when the player asks one of the agents about the mangoes, it doesn't

**[5:58](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=358s)** exactly store that context that we were expecting or it doesn't give us the context that we kind of wanted to. And this is where things are starting to get messy naturally. Like the system may remember the rough topic but lose the source of the topic. A rumor may become certain instead of just a rumor like the agent might state it as a fact or um an agent might know a fact but fail to execute fail to remember it while creating a plan for its actions. So the question here became how do we improve a multi-agentic system over longunning social behavior and not just over one response. And this is where we wanted to bring in

**[6:47](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=407s)** auto research. As you all know, uh few months ago, Karpathi posted out auto research and this this made us immediately very curious. Uh perhaps we can make the system run experiments uh on itself and can we use this for our system as well. So what we understood is instead of manually tuning a prompt or watching one nice demo, we could define sen a scenario suit, run the agents, collect traces, score the behavior and change a small policy surface and only keep the changes that actually improve the score. And this is where we're trying to bridge project paradox with auto research. So at this point basically our multi-agentic framework

**[7:37](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=457s)** project paradox is more like a lab bench and auto research becomes the experimental loop around it. And importantly this is not only about improving rag retrieval. The broader framing is optimizing the agent protocol like how do agents write memories, retrieve them, communicate uncertainty, update trust attribute sources and replan around new facts. basically um yeah in this context uh oh yeah in this context art research is not another agent in the village like I said it's a meta system outside the village the villagers have local

**[8:26](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=506s)** perspectives of course they only know what they saw heard remembered or inferred because there isn't a common memory database in between them. Information only travels once uh other agents communicate them properly. The auto research layer has a different job here. It reads the full traces of a run, compares what happens against the scenario ground truth, uh scores the behavior and proposes a constrained change to the agent protocol or cognitive policy. Then it reruns the scenario and asks society level behavior like did society level behavior get better. This is the key shift we were trying to look for. So we were no longer

**[9:15](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=555s)** evaluating one answer. We were evaluating an entire run. And this is what one of the loops would look like. Like first we define a control scenario which I'll elaborate a bit more about later. For example, one agent learns a public fact or one agent hears a rumor. Uh that could be a controlled scenario. Then we run the simulation. During the run, we collect structured traces, observations, conversations, memory rights, retrievals, belief updates, whatever is relevant to us in that case, we collect. Then we score this behavior. Did the information spread as we expected it to? Did the source attribution survive? Such

**[10:04](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=604s)** as, does the agent remember who started the rumor? Did uncertainty stay uncertain? Did agents act on what they actually knew? And then the auto research layer here proposes a small policy change. And this is important. It should not rewrite the whole application of course. it should only edit a controlled policy surface and then we rerun. If the score improves and the guardrails hold, we we keep the improvement and if not we simply just revert back. And talking about controlled scenarios, the reason why uh scenario design matters is that social behavior is

**[10:52](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=652s)** otherwise a bit fuzzy. uh in general in the sense if you just let the agents in our environment wander around it might look cool and you might get nice interactions but it's actually very hard to evaluate on whether the system actually improved. So this is why we believe you need controlled scenarios. For example, one scenario could test a public fact diffusion. Let's say agent A learns uh the bakery will close tomorrow. Do the right agents learn it? Do they remember who said what? Do they rem do they change their plans based on this fact? Another scenario could test rumor uncertainty. Agent let's say agent A hears that agent

**[11:43](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=703s)** C might leave the village. When this rumor spreads, does might leave suddenly become is leaving or does it stay as might leave? Like does it become a fact or does it still stay as a a rumor? Another scenario could test replanning. The group has a plan, but one agent learns, let's say, the route they wanted to take is blocked. Do agents update this and communicate this uh with each other to avoid uh a improper plan or scale actions? The point is not that these exact scenarios are universal here. The point we're trying to make is that long horizon agent behavior needs scenario suits.

**[12:32](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=752s)** And talking about our Mango example again, after running one of our auto research loops, this time after uh a a long pro period of time, when the player finally asked one of the agents about the sale on mangoes, we did find that u the the agent was able to respond within context this time like compared to last time. Um yeah and for this talk the form the exact formula we believe is less important than the shape of the scorecard. Uh you do not want a single vague met metric like agent quality. This will hide all the interesting failures.

**[13:22](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=802s)** Instead you want a balanced scorecard. For diffusion, you might measure reach like how many agents know the fact after end steps. For provenence, you measure source retention among agents who know it. How many remember it, where it came from, etc. For rumors, you can measure uncerny preservation and false surn rate. For planning, you can measure action consistency and time to replan. And for privacy, you can measure containment. This matters because optimizing only one metric can create bad behavior. Because let's say if you only optimize for diffusion, the agents may learn to overshare everything. And let's say if you only optimize for

**[14:12](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=852s)** memory recall, you might create noisy or steal um like memories. So this scorecard is what keeps the system honest and prevents the auto research agent from gamifying the system to just increase one specific score. The other important engineering lesson that we learned over this project is that um it's important to keep the editable surface really small. The auto research layer should not have permission to randomly rewrite the whole codebase. Instead, it's really important to freeze the harness, the scenarios, and the metrics. So, we're only exposing the

**[15:00](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=900s)** part of the system that we actually want to optimize. Here in project paradox for us that meant things like memory writing policy, retrieval policy, communication prompt, belief, trust rules, source attribution, replanning triggers, etc. This gives the search pro process room to improve behavior, but also prevents it from gaming the evaluation directly as we mentioned before. And this is the difference between the LM writing random patches versus the LM actually searching within a controlled policy space. And here are here are examples of the kind of changes I want this kind of loop to search over. If if source attribution

**[15:50](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=950s)** disappears, the policy change might be preserve source in memory and uh write uh memory rights and summaries. If rumors harden into facts, the policy change might be stored confidence mark firstand versus secondhand and require hedging when retelling uncertain claims. If if facts if public facts stay local, the policy change might be classify useful public facts differently and make agents proactively share important source evidence. The key is that these are small changes to the agent protocol, but they can have larger effects on a society level behavior for multi-agentic systems. This is also where I kind of want to be careful about our claims here

**[16:39](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=999s)** because with we believe without repeated current loop results like I wouldn't say the system just generally improved. We're trying to say this is the right kind of surface to expose to an auto research layer uh loop because it is small enough to control but it's still rich enough to change the social behavior to some extent at least. And the biggest lesson for me perhaps was that memory is not enough here. You can add a rag memory to an agent and still not get the current long-term uh horizon behavior that you were looking for. Um because agents need to sometimes know where that information came for uh

**[17:28](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=1048s)** came from. You need to preserve whether it was firsthand, secondhand, verified or uncertain. Sometimes you need to separate raw episodic memories from what the agent currently believes too. And you need to test behavior through scenarios not not just through vibes. So the other lesson is that uh roll back also is not optional. When you optimize social behavior, a change can improve one thing and damage another. So, a policy that spreads public facts uh faster might also leak private information. A policy that increases recall might increase stale memory usage. So, the loop should basically be like a ratchet. Try a change, score it, keep it only if the scorecard improves and guard rails whole.

**[18:19](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=1099s)** And we we definitely believe this is not only relevant for game agents cuz although I gave you an example using a game village um we believe like let's say for example support agents support agents need to know which policy update comes from where right and whether it supersedes an older answer. Personal assistants for example need to remember commitments that they previously made and h make corrections if uh if the user u wants to change those personal commitments. Research agents need pro uh provenence citations contradiction handling and hypothesis updates. Coding agents need longunning context across issues, files, teammates and changing requirements. Workflow agents need

**[19:09](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=1149s)** access controls, handoffs, and replplanning when the world changes. All of these systems have the same underlying problem. They maintain state over time. And that state affect affects future action. So they need control scenarios and behavioral scorecards is what we are proposing. So again in brief, a recipe for long horizon agents. If there's one practical recipe I want you to take away, freeze the harness, define scenarios, log traces, score behavior, and expose only a small policy surface. Search over these changes, keep only changes that survive your measurement. And this is an

**[19:58](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=1198s)** engineering pattern that we believe would uh make sense for longunning agents. The real question we believe is across controlled runs, does the system behave better? To close, project paradox start as an attempt to make game agents feel alive in a 3D world. But the deeper engineing problem was not animation or dialogue for us. It was the state such as which agent knows what, which agent told whom, what is true, uncertain or outdated, and do agents act on what they remember. Otter research. Otter research gave us a way to approach this a bit more systematically. Not by trusting one demo and not by endlessly handtuning prompts,

**[20:47](https://www.youtube.com/watch?v=x4e5O9zN0TE&t=1247s)** but by running control experiments and keeping only the changes that survived our measurement. Long horizon agents need experiments and not just prompts. And I hope that's the takeaway that you get from this talk. And yes, please do connect with us. We'd love to talk if you have any questions. Thank you so much for listening. Yeah.
