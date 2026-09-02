---
id: 0U0U_qsDnpY
title: "Community | Execution Governance The Layer That Defines What Agents Cannot Do"
slug: community-execution-governance-the-layer-that-defines-what
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: ["Sergey Vlasov"]
channel: "OWASP GenAI Security Project"
duration_min: 14
published_at: 2026-07-20T00:46:36Z
video_id: 0U0U_qsDnpY
url: https://www.youtube.com/watch?v=0U0U_qsDnpY
youtube_url: https://www.youtube.com/watch?v=0U0U_qsDnpY
tags: []
topics: ["Agents & orchestration", "Governance, ethics & regulation", "Science, healthcare & applied ML", "Security, safety & red teaming"]
transcript: true
---

# Community | Execution Governance The Layer That Defines What Agents Cannot Do

**Sergey Vlasov**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=0U0U_qsDnpY) · [Conference site](https://genai.owasp.org/)

## Description

OWASP GenAI Security Project 2026 Virtual Summit
Community Session

In March 2026, a supply chain attack compromised LiteLLM — the universal proxy between AI agents and every major LLM API.
The attack never reached the agent's reasoning layer.
It operated in the dependency beneath it.

Every behavioral defense remained active.
Every defense was irrelevant.
This pattern repeats.

Attacks increasingly operate below the agent — in the execution environment, in trusted dependencies, in the composition of individually safe components.
The same month, Axios (100M weekly downloads) was backdoored via a compromised maintainer account.
Five projects compromised in 12 days. Each component passed individual verification. The chain was the attack.

This talk presents execution governance as the missing architectural layer.
The approach does not detect unsafe behavior. It defines a World Manifest — a compiled specification of what actions and components exist in the agent's executable world. At runtime, enforcement is deterministic: same input, same decision, always. No LLM on the critical enforcement path.
We demonstrate the gap through a controlled scenario: an agent configured with standard best practices executes a supply chain–style attack.
Then, under a governed execution environment — without modifying the agent — the same attack cannot execute. Not because it was blocked.
Because the action does not exist in the agent's world.

The takeaway is architectural: OWASP Agentic Top 10 classifies how agents fail.
Execution governance defines what cannot happen. These are complementary layers.
Currently, only one exists in standard practice.

🔗 Learn more: https://genai.owasp.org

Speakers:
Sergey Vlasov
Senior Software Engineer, Radware

## Transcript

*1,275 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=0s)** Okay. Uh my name is uh Sergey. Uh I'm working in Radar, Israel. But uh uh today's uh speech is uh is a result of my own research, my ideas partially inspired by Radver research. Okay. So let's uh let's start. Uh I want to start with a sentence that sounds contradictory. The agent was safe. The world around it was not. The reason that matters is uh that modern agents don't operate on prompts alone. They operate inside an executable world.

**[0:50](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=50s)** memory tools, connectors, packages, proxies, orchestrators, and external side effects. When the world changes, the model does not become malicious. The system can become inside because uh the things the model can reach have changed. This talk is about the layer that defines the world before the agent runs. Okay, this talk about execution governance. Let's return to the previous uh slide. The layer that defines what agents cannot do. The short version is define the world

**[1:40](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=100s)** before the agent runs and just get lost in in the in the slides. I think an agent does not sit on prompt. It sits on a world. That word includes memory tools descriptors, MCP servers, package dependencies, LLM proxies, orchestration frameworks, and real side effects like email or file access. The attack surface is not just the prompt. It is everything the prompt can reach. Most controls operate at the point of attempt. Prompt filters, output monitors, behavioral guard rails, policy checks,

**[2:31](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=151s)** and human approval are all useful, but these share a premise. The dangerous action already exists in the agent world. The agent can see it, reason about it, and request it. Then we try to catch the attempt. Runtime security asks should this attempted action [snorts] be allowed. Execution governance asks an earlier question. Should this action exist in this agent world at all? That shift matters because some risks should be blocked, other should be made

**[3:21](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=201s)** unrepresentable. Deny versus absent. Deny means the action exists and policy blocks it. The door exists and the guard stops the agent. Absent means the action does not exist in this world. The agent cannot see it. ask for it or formulate it as an available move. A denied action still exists. An absent action doesn't. There are three uh practical pieces uh at least as uh uh as I know them. Okay. First, no tool, no action. If dangerous exit is not projected, the

**[4:14](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=254s)** agent does not have a shell command. Second, capabilities are shaped. Send me email is safer than row send email because the recipient is fixed at design time. Third, taint is computed. Data that came from email or the web remains untrusted when it reached a side effect boundary. Deployment artifact world manifest. World manifest is uh uh basically uh uh policy profile or configuration setting. uh but I choose the term world manifest because I

**[5:07](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=307s)** want to underscore the active uh nature of uh of agents. So world manifest is a document which uh describes uh the reality of of agent. This is a deployment artifact the world manifest. It says what exists in the agent's world become before runtime. It it can be reviewed, def compiled, frozen, audited and replayed. Theo important part is not YAML. The important part is timing. Another term I coined but uh it it not it's not accept uh widely accepted yet.

**[6:00](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=360s)** Okay. But uh it's AI IDO. The idea is to use the power of AI to fight the potential risks and uh and other and other uh nondesirable uh uh results of uh of using of AI. Okay. So yeah, echo is one of the principles uh we need to to apply to to achieve uh agent safety. Use intelligence at design time. Enforce deterministic artifacts at runtime.

**[6:48](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=408s)** An LLM can help draft and review the boundary, but at runtime enforcement should be boring. Same input, same compiled world, same decision. Now I um prepared a demo, a small uh small demo which was pre-recorded. it is it's not a live demo because uh anyway it's deterministic and uh I did it uh also in um in a browser. So let's see uh how it could work how how it looks like when uh when you apply those principles.

**[7:40](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=460s)** Okay, this demo has four bits. Um, this demo has four bits. Uh, an absent shell tool, a shaped email capacity, tainted blocking and external side effect, and descriptor drift rejected by hish. Uh start. Okay. Now it's a just a start of the demo. Uh the model is not becoming safer. The executable world is changing. Beat one absent is stronger than deny. The request asks for dangerous exit.

**[8:37](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=517s)** In a normal policy story, we might say this was denied. But that is not what happens here. The compiled world exposes only read file and send me email. Dangerous exit was never projected. The decision is absent because the tool is not is in this world. B2 capability capability projection removes the dangerous argument. Now look at email row send email is absent because the destination is dangerous as an agent control argument. The projected

**[9:26](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=566s)** capability is send me email. The recipient is fixed to owner at example.com at design time. The attacker has no recipient argument to fight over. B3 taint and provenence. This beat shows why absent is not enough by itself. Some tools must exist. In the baseline world, attacker attacker controlled email content reach send email and the side effect succeeds. In the governed world, the same data still carries provenence from email when it tries to trigger an

**[10:17](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=617s)** an external side effect that the deterministic rule returns deny. bit for descriptor drift and replay. Here the tool exists but the runtime descriptor has changed. A new BCC parameter appears. The manifest recorded the descriptor hash at runtime. At runtime the hash does not match it. The manifest recorded descriptor at the design time at trying time the hash doesn't doesn't match the decision is deny

**[11:04](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=664s)** for descriptor drift then the replace the replace shows the property we want same input same compiled word same decision the idea is uh that we could replay uh later on uh the event uh just by setting up the the stage just by passing the same parameters and uh observing the same uh the same responses deny or proof. The word remembered what it was compiled to be. Replay proves it was not an oneoff runtime judgment. Same input,

**[11:56](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=716s)** same compiled world, same decision. Okay. The model did not become safer during the demo. The executable world changed. That is the point of execution governance. Okay, that's the end of the demo. Let's return to the slides. Let's talk about the OAS mapping. OAS gives us names of failure modes. Execution governance is the layer that make some failure paths unrepresentable and others deterministic to enforce.

**[12:47](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=767s)** For example, the supply chain for the supply chain the mechanism is descriptor drift for plug-in design. The mechanism is capability projection for excessive agency. the mechanism is so-called absent and so on. The honest limit is that a bad manifest produces a a bad world. Someone still uh has to understand uh the workflow and threat model but bounded is better than than unbounded. With the manifest the question questions become engineering questions. Is the

**[13:35](https://www.youtube.com/watch?v=0U0U_qsDnpY&t=815s)** bound boundary complete? Are the projections correct? Can we replace the decision? Can we audit what changed? The industry already has many behavioral controls. The missing artifact is world manifest manifest. So don't only ask whether the agent behaves, ask what reality is allowed to inhabit. Okay. Thank you.
