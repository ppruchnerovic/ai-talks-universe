---
id: 7ajiXYpnOLI
title: "Nandini V.: No Agentic Sovereignty, No Agentic Security"
slug: nandini-v-no-agentic-sovereignty-no-agentic-security
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 11
published_at: 2026-10-07T15:40:10Z
video_id: 7ajiXYpnOLI
url: https://www.youtube.com/watch?v=7ajiXYpnOLI
youtube_url: https://www.youtube.com/watch?v=7ajiXYpnOLI
tags: []
topics: ["Agents & orchestration", "Enterprise adoption & strategy", "Governance, ethics & regulation", "Science, healthcare & applied ML", "Security, safety & red teaming"]
transcript: true
---

# Nandini V.: No Agentic Sovereignty, No Agentic Security

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=7ajiXYpnOLI) · [Conference site](https://aiconference.com/)

## Description

For high-security organizations like government, finance, defense, and regulated industries, failing to secure agents isn’t just inconvenient. It’s catastrophic: stalled payments, delayed medical treatments, and dead power grids. More than 70% of regulated-industry leaders name security and privacy as their top barrier to adoption. Agents break the assumptions these industries were built on. Unlike deterministic software, they take actions on their own, reach into live systems, and act with privilege no one formally provisioned. The autonomy is the value. Where it acts, and on whose authority, is the exposure. The instinct is to bolt on data residency and call it solved. It isn't. Data sitting in a database is one thing; data an agent picks up, reasons over, and acts on is another—and that motion is where sovereignty actually breaks. In this session, we’ll detail why regulated industries need truly sovereign solutions to support agents in the environments where they run. We'll examine why data residency alone isn't enough, and unpack the risks across every sovereignty control point an agent touches—data, infrastructure, decision, and ecosystem Attendees will leave understanding the high-risk actions agents can take on their behalf, why probabilistic guardrails satisfy none of these dimensions, and what high-assurance controls — spanning identity, infrastructure, and decision authority—regulated industries actually need before they let agents act. Organizations that treat this as a continuous, auditable posture will be the ones who move fast in AI adoption and still pass the audit.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,292 words · source: supa (en, exact timings)*

**[0:13](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=13s)** Hello everyone and welcome you all. Hope you all are doing well and enjoying your lunch and thank you so much for being here. And behind these three things that I just mentioned for all of us to be here in this fantastic theater and having food on our table. There are industries that make this happen. The most regulated, the most secure industries of the world, the banks, hospitals, the utilities. And these industries like any other industries are also in the race of adopting agentic AI but with one condition to have utmost control over it

**[1:04](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=64s)** and that is sovereignity. I lead agentic AI security product at RSA and this is the topic I would like to share about in the next few minutes. When it comes to agentic security, if there is no sovereignity, then there is no agentic security. Take a look at this number. So this shows 70% of the regulated industries such as the government, the plants and the healthare and the infrastructure think that security and the privacy is their number one concern. And that's the reason for them to slow down and that's the key reason for them to go put the brakes and their concern

**[1:56](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=116s)** is right because for them the failure is not just a friction or it is lack of boosting their productivity failure means payments delayed healthare treatment or a dead power as much as they are concerned They're also under the pressure of adopting this agent like you know all the sessions that we have been hearing how to build the agents how to deploy the agents how to take the agents from your sandbox to production right so that leads us to think okay when we think about sovereignity when we think about security and the privacy the first instinct is that okay put the data in the region where the company is

**[2:43](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=163s)** located and call it But that's data residency protects the data at rest. But the agents change this equation completely. They never leave the data at rest. They pick it up. They reason with it. They act on it and they retain it. And every such that they make they widen their reach. And the data reset systems that we have built for the software that we have programmed to act exactly the way we have written the instructions. But the agents on the other hand they are autonomous. They can act independently. They reach into life

**[3:32](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=212s)** systems and they operate under the privileges which no one would have for that is where the sovereignity breaks and exact a human over the core value that they bring in. But at the same time the actous is the real exposure. The thing that is making them extremely useful is also making them extremely dangerous. And that leads us to think okay so when it comes to agentic security and

**[4:20](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=260s)** sovereignity what are the different control points these agents out. So the first and foremost is the data itself. What can agents see reach and carry with them? the infrastructure. Where are these agents running in whose environment right now and decision who is approving their actions and the last one ecosystem? What are the downstream systems they reaching? So these are the four different control points. They're not these are built around the way these agents act and behave and are built to act. So let's put these four points in

**[5:08](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=308s)** perspective with a very simple example. Take for example there is a hospital who have ruled out this agent that takes up the last minute request from patients looks up the free slots and reschedules the appointment and sends the confirmation simple workflow right but behind this simple workflow so the four control points that we just talked about we'll see how these agents out so the first one when the cancellation request comes in It picks up the patient's record and there goes your PHI and the agent itself may or may not be running within your hospital environment. It may be hosted in someone else's cloud or server. And then when it decided to swap that

**[5:55](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=355s)** appointment, there was no front desk involved. There was no nurse practitioner who approved that. And finally to close the loop to send the confirmation, it reached into third party messaging tool and set the appointment. So behind the simple workflow, it's an agentic workflow. We are no longer deploying a tool. We are delegating authority. And in this simple workflow and there are many complex workflows which we have seen and which you want to achieve and which you want to automate. We are delegating authority and that leads us to think okay what do we do about

**[6:44](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=404s)** high assurance? Okay first of all what is high assurance right? Because when we talk about high assurance, it's a key distinction to think about like okay are they guardrails but there is a key distinction between the high assurance and the guardrails. So guards are good because they reduce the likelihood but high pros that you have the right controls and those controls are effective and that is high assurance. And when we start applying okay there are four different control planes that these agents out okay how do we apply this high concept to those control right data for example it starts with the data the agents need the data

**[7:34](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=454s)** it can reach infrastructure make sure that agents are hosted within the trust boundary decision for human approval Not every single human approval. We don't want to create that fatigue that we think that we have solved right but for high transaction that has consequences. And finally the ecosystem that's a real trap you can think that okay I have included the human in the loop but human in the loop only stamps the entry not the onward journey. Every time the agent calls another agent, delegates it action, it makes a hop and nobody has verified that hop.

**[8:24](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=504s)** So it is not just enough that okay we have human in the loop and we have the data security and the sensitivity guards but we also make sure that the access to the downstream systems is controlled. So basically the point I'm trying to make here is that when it comes to sovereignity and the high assurance it's no longer that okay the data residency is enough right we have to think beyond the data residency and before we let any agent act in such regulated and secure environment we got to ask four questions what can agent reach where is it running who authorized it and can we

**[9:14](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=554s)** can we prove it is the most critical one and if we don't get that right the other three do not matter and the organizations who take that seriously and have the answers from their records are the ones can actually accelerate but still pass their audit because sovereignty is no longer you know ticking the check box or a one time certification okay we got it can forget about it. It's something auditable because every time the agent makes the call, every time the agent delegates, we should be able to prove it, build that evidence layer and have the ability to reconstruct it every single time because agents do not

**[10:03](https://www.youtube.com/watch?v=7ajiXYpnOLI&t=603s)** stop acting. And more for sovereignity and for the secure industries high assurance is not a preference. It is a requirement. Thank you. So this is a QR code behind which the complete white paper on sovereignity and agentic security is drafted and for those who are interested to know more about agentic AI security and what is working at RSA I'm here around thank
