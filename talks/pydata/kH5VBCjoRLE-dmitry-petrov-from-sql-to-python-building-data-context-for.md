---
id: kH5VBCjoRLE
title: "Dmitry Petrov - From SQL to Python: Building Data Context for Agents and people | Pydata London 26"
slug: dmitry-petrov-from-sql-to-python-building-data-context-for
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Dmitry Petrov"]
channel: null
duration_min: 25
published_at: 2026-06-15T15:55:08Z
video_id: kH5VBCjoRLE
youtube_url: https://www.youtube.com/watch?v=kH5VBCjoRLE
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Dmitry Petrov - From SQL to Python: Building Data Context for Agents and people | Pydata London 26

**Dmitry Petrov**

`PyData` · `PyData` · `2026` · `25 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=kH5VBCjoRLE) · [Conference site](https://pydata.org/)

## Description

Text-to-SQL makes great demos, but in real systems generating queries is rarely the hard part - understanding data is. Modern data is increasingly S3-first and multimodal, where meaning is defined by Python workflows, not table schemas.

To work reliably, both agents and people need data context across multiple layers: storage context (what exists and where), metadata context (what’s inside files), dataset context (how files are grouped and versioned), and code context (the transformations that define semantics).

In this talk, I’ll share a practical framework for building these context layers in Python-first systems, and show how DataChain makes multimodal workflows agent-ready in domains like Physical AI and biotech.

Text-to-SQL is often presented as the future interface for AI-driven analytics: connect an LLM to your warehouse, ask questions, get answers. The demo works. But production systems reveal a deeper issue: SQL can query structure, but it cannot provide the context required to understand what data actually means.

After years of building data infrastructure, I’ve learned that context is the real bottleneck - for both people and agents. This becomes unavoidable in S3-first, multimodal environments: video, audio, medical scans, sensor streams, and model outputs. In these projects, the source of truth is object storage, and meaning is defined by Python pipelines.

To reason correctly, you need data context across multiple layers:
- Storage context - what exists, where it lives, and how it changes
- Metadata context - what’s inside files, extracted signals, and hierarchical structure
- Dataset context - how files are grouped, reused across datasets, and versioned
- Code context - the Python transformations that define semantics and intent

In this talk, I’ll present a practical framework for collecting and using these layers systematically. Using DataChain as a concrete example, I’ll show how typed schemas (e.g., Pydantic), vectorized metadata operations, and scalable Python execution make multimodal workflows understandable, reusable, and agent-ready - especially in Physical AI and biotech.

Attendees will leave with a clear mental model for building data platforms where meaning lives in code, and agents can operate with real context rather than isolated queries.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
