---
id: tPm2LdF3ARE
title: "Paddy Mullen - The Future of Notebooks in a Claude Code World | Pydata London 26"
slug: paddy-mullen-the-future-of-notebooks-in-a-claude-code-world
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Paddy Mullen"]
channel: "PyData"
duration_min: 27
published_at: 2026-06-15T15:55:08Z
video_id: tPm2LdF3ARE
youtube_url: https://www.youtube.com/watch?v=tPm2LdF3ARE
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Paddy Mullen - The Future of Notebooks in a Claude Code World | Pydata London 26

**Paddy Mullen**

`PyData` · `PyData` · `2026` · `27 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=tPm2LdF3ARE) · [Conference site](https://pydata.org/)

## Description

AI coding agents are changing how data professionals work. But an AI agent chat session is a stream, a long conversation that scrolls on and on. A good notebook is something different: a sequence of distinct, well-structured transformations, each with an explanation and a visible result. How do you get from the chat stream to that? And how do you see the visualizations, the tables, charts, and diffs that make data work legible?

We'll trace the historical reasons why the programming notebook style developed, what problems it solves, and what problems it creates. Notebooks intermingle three valuable concepts: a live execution environment, a long-running process that caches state in memory, and a narrative log of exploration steps. The long-running process is the key. It's why data scientists use notebooks instead of Python scripts. But this coupling is also why notebooks are fragile, unreproducible, and impossible to productionize. And the kernel's implicit mutable state is a poor fit for AI agents. Unlike databases (explicit state, declarative interface, introspectable), a notebook kernel degrades as implicit state accumulates across cells.

This talk introduces the Deconstructed Notebook: a system that gives AI-agent-driven data work the structure and visualization of a notebook without the notebook's baggage. Claude writes the instructions in the terminal. The PyData Arrow stack, driven by Ibis and xorq, handles the compute. A browser companion renders tables, charts, diffs, and lineage live as the work iterates, organized into distinct steps, not a scrolling chat log. The key architectural insight is that automatic caching of expression results to disk replaces the notebook kernel's in-memory state, letting each step execute as a self-contained script while preserving the interactive, incremental workflow data scientists depend on. The system is built on xorq, an open-source library built on Ibis and Apache Arrow, but the design principles generalize. We'll demo the full workflow live and share what we learned about building post-notebook tooling for the age of AI agents.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
