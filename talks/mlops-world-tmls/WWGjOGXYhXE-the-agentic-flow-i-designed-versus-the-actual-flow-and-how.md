---
id: WWGjOGXYhXE
title: "The Agentic Flow I Designed Versus the Actual Flow: And How I Discovered It Using OpenTelemetry"
slug: the-agentic-flow-i-designed-versus-the-actual-flow-and-how
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 28
published_at: 2026-08-11T13:10:06Z
video_id: WWGjOGXYhXE
youtube_url: https://www.youtube.com/watch?v=WWGjOGXYhXE
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# The Agentic Flow I Designed Versus the Actual Flow: And How I Discovered It Using OpenTelemetry

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `28 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=WWGjOGXYhXE) · [Conference site](https://mlopsworld.com/)

## Description

Michael Havey, Principal Data Architect, OpsGuru

About the Speaker:
Michael Havey is a data architect with thirty years of experience in graph databases, generative AI, data integration, application integration, and business process management. Michael is the author of two books and numerous articles on software design topics.

Abstract:
An agent has a flow, and getting the flow right is critical. We can trust the agent's result only if the path the agent took to get there aligns with our architectural intent. For years, BPM practitioners have faced this exact challenge with production workflows.

Most agent tools provide observability traces of the agent's execution. This flow log gives useful raw data, but it would be advantageous to bring that data together to give us a picture of the path the agent usually takes. We borrow from BPM an algorithm called Process Mining, which uses the log to reconstruct the actual process flow. We can then compare that to the process flow we intended. Is the actual flow close enough or is it way off? Are there inefficiencies, such as superfluous tool executions, that we can try to reduce? Can we trim the flow to save cost and reduce latency?

I present results from an agent I built on AWS's AgentCore service.
