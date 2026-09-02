---
id: qQvXgfGMlJg
title: "Startup Spotlight - AgntID"
slug: startup-spotlight-agntid
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Startup Spotlight"]
channel: "Berkeley RDI"
duration_min: 5
published_at: 2026-08-10T05:21:52Z
video_id: qQvXgfGMlJg
url: https://www.youtube.com/watch?v=qQvXgfGMlJg
youtube_url: https://www.youtube.com/watch?v=qQvXgfGMlJg
tags: []
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# Startup Spotlight - AgntID

**Startup Spotlight**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=qQvXgfGMlJg) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*788 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=qQvXgfGMlJg&t=2s)** SUNDAR KRISH: So I'm here to talk about AgntID.ai. We provide runtime access control for AI agents-- sorry, runtime access control for AI agents. A bit about me. My name is Sundar Krish. I'm a third time founder. I have had two successful exits so far. My last cybersecurity startup was acquired by Fortinet. I was a distinguished engineer before that. We are backed by several cybersecurity founders, some of them with billion dollar exits. Traction-wise, we have large enterprise customers. Our product has been available since March 2026. We are at the preseed stage. So let's get into the fun part about the product. So this is a very simple example of what AgntID does.

**[0:51](https://www.youtube.com/watch?v=qQvXgfGMlJg&t=51s)** So let's say, your prompt to the agent to summarize Google Doc A. Now, what that means is that the agent should only look at Doc A. Sometimes, it gets overeager and starts looking at other docs, Doc B or something. If it does that, we block it. And also, you said summarize, that means the intent is to read it. And sometimes, agent ends up updating it or deleting it. We block that too. And then you said Google Docs. It might go look into Dropbox or something else, making a tool call there, so we block it. So the whole point is we basically make sure the agent is kept in line with what the original intention is. And obviously, this is an oversimplistic example. Modern agents are much more sophisticated. But I'm pretty sure, most of you have heard about the OpenAI Hugging Face incident.

**[1:41](https://www.youtube.com/watch?v=qQvXgfGMlJg&t=101s)** Show of hands if you can. So that's obviously much more complicated example with multiple points of failure, but unauthorized tool call is one of them. An AgntID could have stopped at least that part of it. So that's what we're talking about here. So let's back up. Why does this problem even exist? before agents, we had traditional applications. The workflows were fixed, 1, 2, 3. And then the tools were known, like call Google Docs right into Salesforce. So all the access was predefined at design stage. The whole point of using agents is that so they can reason and decide the next action dynamically. And so they discover the tools at runtime, using MCP and other protocols. So all the access has to be evaluated during execution. And that's where we come in. So what we provide is what we call just-for-task runtime

**[2:31](https://www.youtube.com/watch?v=qQvXgfGMlJg&t=151s)** access. So only the access needed for this task is given, and only while it's needed, and only at runtime. So agents never receive any blanket permissions. So there are two parts to how we do it-- first, we look at the intent of the agent, what the agent is trying to do. If it tries to do something outside of it, we block it. Customers can also write policies. Same thing, if it goes outside the policy, we block it. And so this is a high-level summary. So think of the agent having a broad access, almost having a wide pipeline in the beginning. First, our internal evaluation comes in, narrows it down. The policy evaluation narrows it even further. And if the agent makes out of it, we can also do a scoped credential derivation, which means basically, we do a token exchange

**[3:20](https://www.youtube.com/watch?v=qQvXgfGMlJg&t=200s)** and get a smaller token for the agent. Now, the agent makes a tool call, either through MCP or CLI, using that. So one advantage with us is that the execution stays inside your environment. So basically, the customer data stays private, and also, it helps in low latency. Our runtime is basically something that you deploy in your environment. And it's sandwiched between agents, and MCP, and tools. So why AgntID wins? So we are very focused on this runtime access control. To us, intent plus policy equal to access. That's our mantra. And we let you bring your own MCP, own CLI, own skills. We don't come up with an MCP catalog or anything like that. We are extremely focused on the infrastructure buyer, identity people, security people, DevOps, and so on, and with very little

**[4:13](https://www.youtube.com/watch?v=qQvXgfGMlJg&t=253s)** dependency on developers. That's a huge win. And we also complement existing enterprise systems. So it works with your existing IAM systems, IGA systems, or agent orchestration systems, line graph, Vertex AI, what have you. So just to finish it off, I mean, we all know that the future of software is agentic. I mean, that's why we're all here. And because it's agentic, the future of access control is runtime. Learn more about us at AgntID.ai. You can email me at sundar@agntid.ai, that's S-U-N- D-A-R at AgntID.ai. Thank you. Have a nice day. [APPLAUSE]
