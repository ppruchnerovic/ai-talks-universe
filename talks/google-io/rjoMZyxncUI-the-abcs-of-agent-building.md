---
id: rjoMZyxncUI
title: "The ABCs of agent building"
slug: the-abcs-of-agent-building
conference: google-io
conference_name: "Google I/O"
category: "Vendor & platform"
edition: "I/O 2026"
year: 2026
speakers: ["Kristopher Overholt"]
channel: "Google Cloud Tech"
duration_min: 14
published_at: 2026-05-22T19:37:48Z
video_id: rjoMZyxncUI
url: https://www.youtube.com/watch?v=rjoMZyxncUI
youtube_url: https://www.youtube.com/watch?v=rjoMZyxncUI
tags: ["pr_pr: Google I/O;", "ct:Event - Technical Session;", "ct:Stack - Cloud;", "Google AI Agent stack", "agentic architecture 2026", "Gemini Enterprise Agent platform", "Agent gateway", "A2A Protocol", "Agent-to-Agent", "Model Context Protocol", "MCP", "Google Agent Development Kit", "Agent Studio", "Scaling AI agents to production", "multi-agent orchestration", "AI infrastructure"]
transcript: true
---

# The ABCs of agent building

**Kristopher Overholt**

`Google I/O` · `I/O 2026` · `2026` · `14 min`

`#pr_pr: Google I/O;` `#ct:Event - Technical Session;` `#ct:Stack - Cloud;` `#Google AI Agent stack` `#agentic architecture 2026` `#Gemini Enterprise Agent platform` `#Agent gateway` `#A2A Protocol` `#Agent-to-Agent` `#Model Context Protocol` `#MCP` `#Google Agent Development Kit` `#Agent Studio` `#Scaling AI agents to production` `#multi-agent orchestration` `#AI infrastructure`

[Watch the recording](https://www.youtube.com/watch?v=rjoMZyxncUI) · [Conference site](https://io.google/)

## Description

Explore each framework and protocol in the AI agent stack and learn how they fit together within the Google ecosystem. Whether you are building your first agent, or scaling an existing one to production, gain a clear architectural map to navigate the expanding agent ecosystem.

Resources:
Developer's Guide to AI Agent Protocols → https://goo.gle/4dnLm09
ADK Tools and Integrations → https://goo.gle/4dgac3u
Generative AI Samples and Notebooks → https://goo.gle/4dnN5m9

Watch the cloud sessions from Google I/O 2026 → https://goo.gle/Cloud-at-IO2026

#GoogleIO

Event: Google I/O 2026
Speakers: Kristopher Overholt
Products Mentioned: AI/Machine Learning, Cloud

## Transcript

*2,091 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=rjoMZyxncUI&t=0s)** [MUSIC PLAYING] KRISTOPHER OVERHOLT: Hello, and welcome. I'm Kris Overholt, a Developer Relations Engineer in Google Cloud. I work a lot with Agent Development Kit and its growing ecosystems of tools and integrations. Today, I want to walk through six protocols that can help make your AI agents more capable, in terms of working with external systems, remote agents, payment processing, and real-time interactive frontends. AI agents by themselves are surprisingly limited in terms of what they can do. With just a simple set of instructions and a few tools, they can answer questions and maybe call a tool or two. But the moment you need them to collaborate, or pay for something, or stream results, they hit a wall.

**[0:50](https://www.youtube.com/watch?v=rjoMZyxncUI&t=50s)** And if you're like me, you've seen the growing list of agent protocol acronyms. And you've wondered, why are there so many and what do they actually do. Traditional APIs assume a person is on the other end. A person clicks by, but an agent doesn't know how to check out. A person can browse a storefront, but an AI agent doesn't have a catalog. A person can read a form, but an AI agent produces text. Each protocol that we'll cover today addresses one of these specific problems. Now, to make this more concrete, we'll build a kitchen manager agent that orders food for a restaurant from wholesale suppliers. And we'll use Agent Developer Kit, or ADK, which is Google's open source framework for building and deploying AI agents.

**[1:38](https://www.youtube.com/watch?v=rjoMZyxncUI&t=98s)** Now, here's what happens when you give your agent no protocols and no tools. You ask it to check inventory and place an order. And it confidently fills in the blanks with made-up inventory data, prices, and order confirmations. To understand these protocols at a deeper level, I spent the last few months building agents with them, asking really hard questions and figuring out how they solve real problems. We'll start with a plain agent and add one protocol at a time, until it can check real inventory, place orders, authorize payments, and stream interactive dashboards. By the end, you'll know what each protocol does, what the real code looks like, and when you'd actually reach for it. First, let's start with something probably familiar to you, MCP, or Model Context Protocol.

**[2:28](https://www.youtube.com/watch?v=rjoMZyxncUI&t=148s)** This helps us connect our agent to tools and data. So the first problem is my agent needs to use external tools. Without MCP, every API endpoint needs its own custom tool. And a few services in, and you're already managing dozens of tools. That really doesn't scale well for you or the agent. MCP solves this by letting your agent connect an MCP server that dynamically exposes its available tools. Now, instead of hard coding dozens of tool definitions, you just point at a few MCP servers and the agent discovers what's available at runtime. For our kitchen manager agent, that means connecting to three MCP servers-- one for inventory databases, one for recipes and procedures, and one for supplier emails.

**[3:18](https://www.youtube.com/watch?v=rjoMZyxncUI&t=198s)** In ADK, this is just three lines of code per server using MCP toolset. You don't have to write a single API call. So the agent has real data access now, and adding a new data source is just adding another MCP server URL. And where MCP really shines is prototyping. When you're still figuring out what your agent is capable of doing, MCP lets you quickly plug in new data sources and see what the agent decides to do with them, before you actually start optimizing with individual tools. Next up is A2A, the agent-to-agent protocol. MCP gave our agent data. The next problem is expertise. Our kitchen manager can check inventory, but it doesn't really know today's wholesale prices,

**[4:06](https://www.youtube.com/watch?v=rjoMZyxncUI&t=246s)** supplier quality grades, or delivery windows. That knowledge actually lives with different agents, potentially built by different teams, in different frameworks. A2A solves this through standardized agent discovery. Each agent serves an agent card at a well-known URL that describes its capabilities. Your agent then fetches these cards, discovers what each specialist can do, and talks to them, via send message. In ADK, you can expose any agent as an A2A service with one line using the two A2A method. On the discovery side, you point to a remote agent's URL, fetch its card, and send messages. The agent doesn't need to know how the remote agent is built or even what framework it runs on. In our example, the kitchen manager

**[4:55](https://www.youtube.com/watch?v=rjoMZyxncUI&t=295s)** discovers three remote agents-- one for pricing, one for food quality, and one for logistics. So when you ask it, what's the price of salmon, what's the quality grade, and can I get it delivered by 5:00 PM today-- the agent actually routes each question to the right specialist, without knowing anything about how they're implemented. And the real value of A2A shows up at the organizational level. When every team in your company is building their own agent, A2A gives you a standard way to discover and delegate tasks to them. Adding a new remote agent capability just means adding a new URL. Now our agent needs to order supplies. This is where UCP, or Universal Commerce Protocol, comes in. And it standardizes how it discovers merchants, how to place orders, and how to track order status.

**[5:47](https://www.youtube.com/watch?v=rjoMZyxncUI&t=347s)** A person can browse a storefront, but an agent really needs machine readable information about a merchant and product discovery. UCP provides this through a well known endpoint at well-known/ucp. So now the agent can discover suppliers catalog and send a structured checkout request with line items, quantities, and payment details. The agent doesn't have to browse a website. No parsing HTML and it doesn't have to guess at the checkout flows. Here's what that looks like in code. It's all just standard HTTP requests following the UCP specification. But now, the typed request format means the agent doesn't have to guess at what a checkout request actually looks like. For our kitchen manager agent, this means discovering the suppliers catalog,

**[6:36](https://www.youtube.com/watch?v=rjoMZyxncUI&t=396s)** placing a typed order for 10 pounds of salmon, and then getting back a confirmed order number. The agent goes from supplier discovery to a completed checkout, through a structured set of steps. UCP lets your agent place orders, but who authorized the spending? There's no audit trail, no spending limit, no list of approved merchants. That's where AP2, the agent payments protocol, comes in. AP2 introduces typed mandates. A checkout mandate defines the guardrails, like which merchants are approved and what can be purchased. A payment mandate enforces spending limits, specifies approved payment methods, and it records the actual user authorization. And finally, signed receipts create the audit trail. Here's what that looks like in code.

**[7:25](https://www.youtube.com/watch?v=rjoMZyxncUI&t=445s)** The restaurant owner can configure guardrails, like only buy from these approved vendors, auto approve orders under $500 on the company card, and require manager's sign-off above that. When the agent tries to buy from an unauthorized supplier, the mandate rejects it. When it places a legitimate order, it gets a signed receipt, with the full authorization chain. Instead of telling your agent, "Don't spend more than $500 in the instructions" and hoping for the best, you're actually specifying conditions in a typed protocol with enforceable guardrails. UCP and AP2, together, give you the full commerce lifecycle-- discovery checkout, authorization and a complete audit trail. Now, at this point, our agent can check inventory, consult specialists, place orders, and authorize payments.

**[8:17](https://www.youtube.com/watch?v=rjoMZyxncUI&t=497s)** But every response comes back as a huge wall of text. A2UI or the Agent-to-User interface protocol helps our agent generate the right user interface at the right time, all on the fly. Now, when you need a reorder checklist, or an order form, or a supplier comparison, you'd normally build a separate front end component for each one. Instead, a A2UI defines 18 primitives, like cards and buttons, text fields, date pickers, and sliders. Now the agent can actually compose these primitives into whatever UI fits the user requests. And then a client renderer, like Lit, or Angular, or Flutter turns them into real native components. So the code is a JSON payload with three parts. We have a rendering surface, a component tree built

**[9:08](https://www.youtube.com/watch?v=rjoMZyxncUI&t=548s)** with primitives, and a data model that fills these components with values. So now, the agent doesn't generate HTML or front end code, it simply generates a declarative JSON payload that any renderer can interpret safely. Back to our kitchen agent. We'll try this with three different prompts. So now, if we send, show me what to reorder, we get back a checklist dashboard. If we send, set up an order form, this produces a form with a date picker and an urgency slider. Or if we send, compare two suppliers, side-by-side, it actually gives us comparison cards. So we get three different UIs, zero changes to the agent, and they're all composed from the same 18 primitives. So a A2UI kept the layout and the data separate. The agent sends the component structure once.

**[9:58](https://www.youtube.com/watch?v=rjoMZyxncUI&t=598s)** And then you can update the data whenever you need to. So that's why the same payload works across different renderers, like Lit, or Flutter, or Angular. Last up is AG-UI. So we covered what the agent can do. Now the question is, how does the user actually see it happen? Think of a scenario where the agent finished thinking, 30 seconds ago, but the user still staring at a spinner. AG-UI standardizes what those streaming events look like. No matter which agent framework you're using, your front end gets the same typed events-- what tool was called, what it returned, and what the agent is saying. Under the hood, it's sending typed streaming events, like text message content, tool call result, and run finished. And if you're using ADK, this is just three lines of code.

**[10:47](https://www.youtube.com/watch?v=rjoMZyxncUI&t=647s)** So you wrap the agent that we've been building with ADK agent, you mount it on an API endpoint, and now everything the agent does streams to your front end, in real time. For our kitchen manager agent, the user can actually watch every protocol fire, in sequence. First, MCP checks the database and finds three pounds of salmon in stock. Next, A2A queries the pricing and quality agents to get the latest information. And now that we have pricing and quality confirmed, UCP discovers the supplier and actually places the order, while AP2 authorizes the payment and returns a signed receipt. So the user sees all of this streaming, in real-time-- not after the agent finishes, but actually as each step happens.

**[11:34](https://www.youtube.com/watch?v=rjoMZyxncUI&t=694s)** Here's what's happening in this diagram. Our kitchen manager pushes events through AG-UI, and the frontend receives them as a standard typed stream. The agent does the work while AG-UI handles the delivery. That's all six protocols in a very short time. Let's take a step back now and look at the big picture. Each protocol that we covered today was created because traditional APIs assume a human is on the other end. In our agent, real data and real expertise came from MCP and A2A. Structured commerce with signed payment authorization came from UCP and AP2. And interactive dashboard streaming in real-time came from A2UI and AG-UI. We started with a plain agent that made up inventory data.

**[12:23](https://www.youtube.com/watch?v=rjoMZyxncUI&t=743s)** And by the end, the same agent can fetch real inventory levels, discover specialist agents, place typed orders, get payment authorization with signed mandates, render dashboards from 18 primitives, and stream it all back to the front end. Keep in mind, these protocols don't actually depend on each other. You don't need all six to get started. So if your agent needs real data, start with MCP. If it needs to talk to other agents, add in A2A. Pick the one that solves the problem you have right now. If You're looking for ADK tools and integrations, you don't have to start from scratch. You can check out the Tools and Integrations page in the ADK documentation, where we have a growing library of tools, integrations, connectors. Many of them with ready-to-go code snippets.

**[13:13](https://www.youtube.com/watch?v=rjoMZyxncUI&t=793s)** For MCP and A2A, specifically, the Generative AI Repo on GitHub has notebooks that you can run today. For the other protocols, you can go to the official repositories-- A2A Python, UCP samples, AP2, A2UI, and AG-UI. They all have built-in examples and many of them use ADK. Now you know what problem each protocol solves, what the code looks like, and exactly when to reach for it. Thanks for watching. [MUSIC PLAYING]
