---
id: H6E46K0WPWg
title: "Daniel Homola - From Multi Agent Patterns to Reliable Orchestration"
slug: daniel-homola-from-multi-agent-patterns-to-reliable
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Daniel Homola"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T07:51:13Z
video_id: H6E46K0WPWg
url: https://www.youtube.com/watch?v=H6E46K0WPWg
youtube_url: https://www.youtube.com/watch?v=H6E46K0WPWg
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Daniel Homola - From Multi Agent Patterns to Reliable Orchestration

**Daniel Homola**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=H6E46K0WPWg) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*939 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=H6E46K0WPWg&t=2s)** Hi everybody, I'm Daniel Homola from BMW Research. The title sounds like a patterns talk, but the core question is simple. In an agentic system or a multi-agent system, the core question is who should handle this piece of work? Reliable orchestration depends on making that choice well repeatedly at runtime. This is my background. Recently, I'm working on agentic architecture, basically system-level architecture for agentic AI customer products, and a graphical user interface agents, basically computer use agents that operate screens like users do. And for the motivation behind the GUI agent paradigm, you can have a look on this talk that I held last year at AI Engineer conference if you're interested why an enterprise would consider this technology as a one of the agents.

**[0:52](https://www.youtube.com/watch?v=H6E46K0WPWg&t=52s)** Let me ground my talk in a multi-agent in-car voice assistant, where we could have free agents. You might have navigation agents for finding your route, car control agents for manipulating your windows, seats, climate, and also this for example GUI agent, computer use agent that can operate for example applications through the screen. Above them, then you have the orchestrator who acts, coordinates the execution, and sometimes combines the results. And after all, the hard part in the orchestration is not the patterns and how do we put stuff between the agents. It's about the delegation choices and the coordination, making it reliably under constantly changing context. And there are many coordination patterns, but they

**[1:40](https://www.youtube.com/watch?v=H6E46K0WPWg&t=100s)** all come down to the delegation decision, to the runtime decision. In a handoff, the control transfers to another agent. In agents as tools, the orchestrator delegates work to the specialized agents and waits for the result. In a Uh, the classifier or the router dispatches the each turn to the specialist, but there are other patterns. Every enterprise defines their patterns in a different naming, but essentially it's the same. It's about the choice. It's about the delegation that we need to do, and it's about the which agent or tool should we, uh, delegate this piece of work to. And it can all sound like ordinary tool selection, but it isn't. Tool selection is often evaluated in, uh, against one ground truth label, but for agent delegation, who should handle this work in this context, it's different. The

**[2:28](https://www.youtube.com/watch?v=H6E46K0WPWg&t=148s)** overlap is normal there because we have multiple agents that can solve the tasks as well, considering, for example, the GUI agent. And the choice includes also cost, latency, all the or the user experience that we want to provide to the user, uh, in this case, in the driver's seat, for example, or the passenger. And here's an example that where, for example, the ambiguity comes. Like, if the user says, "Play some jazz." The media API may be the best if we have an empty screen, but if there's already a song or a playlist on the screen, then we can also tapping it. And that could be also valid choice. So, the ground truth doesn't have to be just one label. We can have multiple acceptable valid choices. And basically, uh, the point is also that the overlap is real, but this is not the only problem that we have in agent delegation. Even when it's implemented as a tool call,

**[3:15](https://www.youtube.com/watch?v=H6E46K0WPWg&t=195s)** agents are not tools. A tool call is bounded, and the agent delegation is unbounded. So, basically, delegating to an agent can start an autonomous a loop. It may reason, uh, sorry. Uh, it may reason, ask for clarification, get stuck, resume later, uh, or never return cleanly. So, the orchestration is not just selecting capability, it's also deciding deciding when it's safe and useful to let another loop take over, effectively unbounded control. So, we have to, this uh, see the distinguish distinguish between this, and then also with the overlap, there's the ambiguity. So, here are some examples where for example, it's clear if I say navigate me to Munich, this is navigation agent. But, for example, the play some jazz, there are multiple valid trajectories, multiple valid agents that

**[4:02](https://www.youtube.com/watch?v=H6E46K0WPWg&t=242s)** could solve the problem. So, reliable systems should not basically force it into one canonical label, and it should use the runtime context and adapt accordingly. So basically uh it's about uh the overlapping agents becoming multiple valid choices. And then it also leads to uh consequences in the evaluation. How do we want to do evaluation? And the benchmark basically should only ask whether the final task succeeded. No, it's also about the reasonable path, the cost, the latency, the user experience that we want to provide. And then we can accordingly create the data set that then have also the full runtime context. And then uh we have the metric. For example, sometimes we can optimize for latency, sometimes we can optimize for the human-machine collaboration.

**[4:49](https://www.youtube.com/watch?v=H6E46K0WPWg&t=289s)** And after all, it's about also how do we want to build this multi-agent system in an enterprise. So, how I would say like in an enterprise, every team who owns an agent could build their own benchmark. And then after all, multiple teams can put the benchmarks together, and then we can build a shared benchmark where we also consider the core core collaboration, coordination patterns, and uh basically how everything works together in the orchestration and delegation benchmark. So, the patterns are just the means uh to connect the pieces of the multi-agent system. What matters is making orchestration paths and delegation decisions measurable, context-aware, and reliable. So, keep asking, "Who handles this work? What path should they take together? And how do we know it was good?" Thank you.
