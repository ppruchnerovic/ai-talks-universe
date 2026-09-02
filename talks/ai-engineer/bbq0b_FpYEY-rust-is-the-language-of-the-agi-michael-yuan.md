---
id: bbq0b_FpYEY
title: "Rust is the language of the AGI - Michael Yuan"
slug: rust-is-the-language-of-the-agi-michael-yuan
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["Michael Yuan"]
channel: "AI Engineer"
duration_min: 29
published_at: 2025-06-03T22:22:27Z
video_id: bbq0b_FpYEY
url: https://www.youtube.com/watch?v=bbq0b_FpYEY
youtube_url: https://www.youtube.com/watch?v=bbq0b_FpYEY
tags: []
topics: ["Agents & orchestration"]
transcript: false
---

# Rust is the language of the AGI - Michael Yuan

**Michael Yuan**

`AI Engineer` · `AI Engineer` · `2025` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=bbq0b_FpYEY) · [Conference site](https://www.ai.engineer/)

## Description

In the Latent Space podcast, Bret Taylor argued that strongly and statically-typed programming languages, such as Rust, could be especially well suited for AI coding, since the generated code can be validated by compilers for real-time feedback and reinforcement learning. However, unlike weakly or dynamically typed JavaScript or Python, there are few examples of Rust code in LLMs’ training corpora, and hence limiting the LLM's capability in generating Rust code.

In this talk, we will discuss the open-source Rust Coder project, which provides an integrated agentic framework based on the MCP protocol for generating complete and valid Rust projects. The Rust Coder framework enables the following functionalities for coding LLMs (e.g., Qwen Coder or Codestral).

* Provides Rust example code, explanations, and tutorials relevant to the user’s request within the LLM query context.
* Generates and parses generated code artifacts into Rust Cargo projects.
* Compiles and executes generated Rust Cargo projects.
* Executes the compiled project against test cases.
* Provides coding LLM feedback based on compiler and testing outputs.
* Runs continuously until all issues are fixed.

We will demonstrate how the Rust Coder project works, how to integrate it into your agents, and ways to contribute to the open-source effort. We will also discuss pilot results from a large Rust coding camp (1000+ college students) using the Rust Coder tool.

The Rust Coder is supported by two Linux Foundation Mentorship grants, as well as content provided by the Rust Foundation.
