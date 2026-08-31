---
id: p-znSwtxito
title: "Can GenAI predict code’s energy use and why should we care? by Wilco Burggraaf"
slug: can-genai-predict-codes-energy-use-and-why-should-we-care
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2026
speakers: []
channel: "Devoxx"
duration_min: 16
published_at: 2026-04-09T21:33:21Z
video_id: p-znSwtxito
youtube_url: https://www.youtube.com/watch?v=p-znSwtxito
tags: []
transcript: false
---

# Can GenAI predict code’s energy use and why should we care? by Wilco Burggraaf

**Speaker not identified**

`Devoxx` · `Devoxx` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=p-znSwtxito) · [Conference site](https://devoxx.com/)

## Description

Please subscribe to our YouTube channel @ https://www.youtube.com/@DevoxxForever

This 15-minute demo shows how AI helps you spot and shrink the hidden energy and CO₂ footprint in “mature” Java code.

We use a simple, transparent theoretical model for sustainable decision making.

Micro-ops map to CPU work at one to five gigahertz, which we convert to milliwatt-hours bandwidth. Multiply that by your grid’s carbon intensity to estimate CO2. This matters because much of the marginal electricity on the grid still comes from gas turbines, so every milliwatt-hour you avoid cuts indirect emissions.

The AI annotates code line-by-line with uOps and mWh, flags smells/SOLID issues, predicts boost/threads risks, etc.

You’ll see how this works on small, widely used open-source Java libraries (think helpers, IO, logging, JSON).

We apply a lightweight playbook focused on under-utilization, waiting patterns, and bottlenecks. Using our ten DevOps++ open-source principles, like eliminate idle compute, right-size memory, prioritize I/O before scaling, prune work at the source, etc.

Key takeaways
A practical AI-assisted method to estimate a theoretical energy from code.
A repeatable playbook for low-risk patches that save watts without sacrificing speed.
A governance hook to make “less energy” a default quality bar in your CI/CD pipelines.

Target audience
Java engineers, tech leads, SRE/DevEx, FinOps/Sustainability owners, or anyone who wants measurable, low-effort energy wins in code and CI.
