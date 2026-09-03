---
id: 2xGcqDmkkf8
title: "The Double (AI) Agent: Flipping a GenAI Agent Behavior"
slug: the-double-ai-agent-flipping-a-genai-agent-behavior
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 40
published_at: 2025-05-15T17:00:39Z
video_id: 2xGcqDmkkf8
url: https://www.youtube.com/watch?v=2xGcqDmkkf8
youtube_url: https://www.youtube.com/watch?v=2xGcqDmkkf8
tags: []
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: false
---

# The Double (AI) Agent: Flipping a GenAI Agent Behavior

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `40 min`

[Watch the recording](https://www.youtube.com/watch?v=2xGcqDmkkf8) · [Conference site](https://www.blackhat.com/)

## Description

The Double (AI) Agent: Flipping a GenAI Agent Behavior from Serving an Application to Attacking it using Promptwares

Function calling (a.k.a. Plan & Execute), is a groundbreaking application of generative AI (GenAI). By dynamically planning a solution for a given user input, it offers a powerful alternative to traditional, pre-coded approaches. GenAI engines are used to craft a tailored plan (based on the available functions within an application) which independent agents subsequently execute. Despite its rapid adoption in the industry and integration into countless applications (e.g., chatbots, assistants), the risks associated with function calling (agents-based GenAI applications) remain largely unexplored.
This talk discusses PromptWare, a new emerging risk to agents-based GenAI applications. PromptWare is a family of zero-click input prompts that when given as inputs to GenAI applications, flip the behavior of the GenAI engine from serving the application to attacking it. In the first part of the talk, we discuss the properties and uses of PromptWares. Next, we discuss a naive variant of Propmtware intended to target applications whose interface with the GenAI engine is known to attackers. We show how attackers could exploit such knowledge to trigger a DoS attack against a GenAI-powered assistant by forcing the agents to enter an infinite loop which wastes redundant API calls to the GenAI engine.
Next, we discuss Advanced Promptware Threats (APwT), an advanced variant of Promptware that targets applications with no prior knowledge. We show how attackers could write a prompt that exploits the advanced AI capabilities of GenAI to conduct real-time reconnaissance (by understanding the context of the GenAI-powered application, and identifying the assets in its context), threat reasoning (enumerating the possible malicious activities that could be conducted and deciding on one) and finally use an agent to execute a malicious activity within the context of the application. We show how attackers could write APwT that forces an e-commerce chatbot to provide them discounts.

By:
Ben Nassi  |  Infosec Researcher, Technion
Stav Cohen  |  PhD Student, Technion – Israel Institute of Technology
Ron Bitton  |  Principal AI/ML Security Researcher, Intuit

Full Abstract and Presentation Materials:
