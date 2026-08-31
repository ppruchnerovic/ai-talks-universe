---
id: vRFqbEzzDsI
title: "Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza"
slug: building-agentic-applications-w-heroku-managed-inference
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: []
channel: "AI Engineer"
duration_min: 53
published_at: 2025-06-27T00:00:00Z
video_id: vRFqbEzzDsI
youtube_url: https://www.youtube.com/watch?v=vRFqbEzzDsI
tags: []
transcript: false
---

# Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2025` · `53 min`

[Watch the recording](https://www.youtube.com/watch?v=vRFqbEzzDsI) · [Conference site](https://www.ai.engineer/)

## Description

In this workshop, you’ll learn how to use Heroku Managed Inference and Agents to build agentic applications. We’ll cover how to provision and deploy LLM models to your app, run untrusted code securely in Python, Node.js, Go, and Ruby using built-in tools, and use the Model Context Protocol (MCP) to connect tools and actions that extend your agents' capabilities.
---
Agentic applications are reshaping how developers approach automation and AI integration. In this workshop, you’ll learn how to use Heroku’s new Managed Inference and Agents platform to create applications that can reason, make decisions, and trigger actions, all while staying fully integrated with your app logic and infrastructure.

We’ll walk through how to provision and deploy LLMs, run untrusted code securely in multiple languages, and extend your agents with the Model Context Protocol (MCP). Whether you're building internal tools, developer assistants, or customer-facing AI features, this workshop will give you the technical foundation to get started.

You’ll learn how to:

- Deploy and manage LLMs using Heroku Managed Inference and Agents
- Safely run untrusted code in Python, Node.js, Go, and Ruby using Heroku’s built-in tools
- Use the Model Context Protocol (MCP) to extend your agent capabilities

By the end of this session, you’ll know how to build and deploy agentic applications on Heroku using production-ready infrastructure.

---related links---

## timestamps

Introduction to Heroku AI [00:00]
Core Mission: The product's goal is to make every software engineer an AI engineer. Anush Dsouza, the Product Manager, states Heroku wants to make it “simple to attach agents and AI to your application.” [04:24]

Agentic Control Loop: Heroku provides an "agentic control loop" running on its platform. This loop gives AI models access to tools like code execution and data access, all secured under Heroku's trust layer. [05:01]

AI Primitives: Heroku AI is built on key primitives. These include inference for accessing curated models, the Model Context Protocol (MCP) for extending app functionality, and PG Vector for handling embeddings. [06:25]

Trusted Compute: Heroku's trusted compute layer, Dynos, runs first-party tools. They plan to expand this with tools for web search and memory, and users can bring their own tools via MCP. [07:08]

Provisioning and Usage
Managed Inference: This service allows you to run AI models directly within your Heroku infrastructure. This keeps your data within your application's network for enhanced security. [13:23]

Supported Models: The platform supports text-to-text models from Anthropic (Claude 3.5, 3.7, and 4), embeddings from Cohere Embed, and image generation with Stable Image Ultra. [14:38]

Chat Completions API: The basic chat completions endpoint is designed to be highly compatible with the OpenAI and Anthropic APIs. The presenter notes it's “95% compatible with the OpenAI API,” allowing the use of the OpenAI SDK. [50:51] It supports standard parameters like temperature and max_tokens, as well as streaming responses. [21:29]

Heroku Tools and Agents
Serverless Execution: Tools run on one-off Dynos, which scale to zero after execution. This means you “only pay for the compute that you use.” [17:57]

Dyno Run Command: This powerful tool allows the LLM to execute Unix commands or pre-deployed scripts on a Heroku Dyno. This gives the agent access to real-time information and the ability to interact with the file system. [25:08]

Database Querying: The agent can interact with your PostgreSQL database through two tools:

postgres-get-schema: This retrieves the database schema, which helps prevent the LLM from hallucinating incorrect table or column names. [25:45]

postgres-run-query: This tool generates and executes SQL queries based on the provided schema and the user's natural language request. [25:52]

Code Execution: The agent can generate and run code in Python, Node, Ruby, and Go on a one-off Dyno. It even supports installing dependencies on the fly. [27:02]

Extending with Model Context Protocol (MCP)
Bring Your Own Tools: You can extend the agent's capabilities by deploying your own tools as MCPs to Heroku. [37:38]

Deployment: MCPs are deployed by configuring a Procfile with an mcp process type. This makes your custom tool discoverable by the Heroku agent. [46:19]

Example MCP: The workshop demonstrates a "Brave Search MCP" that allows the agent to perform web searches, showcasing how to add external knowledge to the agent. [43:42]
