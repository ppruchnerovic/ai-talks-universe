---
id: 41NimccrfP8
title: "Keynote - Samuel Colvin - Pydantic Monty & Logfire | Pydata London 26"
slug: keynote-samuel-colvin-pydantic-monty-logfire-pydata-london
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Samuel Colvin"]
channel: null
duration_min: 42
published_at: 2026-06-06T08:48:56Z
video_id: 41NimccrfP8
youtube_url: https://www.youtube.com/watch?v=41NimccrfP8
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Keynote - Samuel Colvin - Pydantic Monty & Logfire | Pydata London 26

**Samuel Colvin**

`PyData` · `PyData` · `2026` · `42 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=41NimccrfP8) · [Conference site](https://pydata.org/)

## Description

Pydantic Monty & Logfire: Wild LLMs, from tool calling to computer use

LLMs are increasingly being used to take actions, call APIs, and write code. But giving AI agents the ability to run code opens up a surprisingly tricky question: how much control do you actually hand over?

There's a full continuum here, from structured tool calling at one end to full computer use at the other, but most developers don't realise how many interesting options live in between. That gap matters, because the extremes both have serious trade-offs: pure tool calling is safe but sequential and limiting, while full sandboxes or computer use are powerful but complex, slow, and often a hard sell to enterprise security teams.

This talk introduces Monty, a minimal Python interpreter written in Rust, purpose-built for running AI-generated code safely. Unlike traditional sandboxing approaches that start with full access and try to lock things down, Monty starts from zero and requires you to explicitly grant each capability — meaning the LLM can only interact with the outside world through functions you wrote, control, and can audit. It's a new paradigm: not AI using your tools, but AI writing its own programs to coordinate your tools.

In this talk, you will learn how to think about the control-capability trade-off when building AI agents, where Monty sits on that spectrum and why, and how to use it with Pydantic AI to replace sequential tool calls with expressive Python — complete with a live demo traced through Logfire.

Basic familiarity with Python and LLM tool use is helpful but not required. No prior knowledge of Rust or sandboxing concepts needed.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
