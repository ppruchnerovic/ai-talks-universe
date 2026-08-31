---
id: phchDt63qAA
title: "How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed"
slug: how-we-built-zeta2-training-an-edit-prediction-model-in
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ben Kunkle"]
channel: "AI Engineer"
duration_min: 11
published_at: 2026-05-30T16:00:06Z
video_id: phchDt63qAA
youtube_url: https://www.youtube.com/watch?v=phchDt63qAA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed

**Ben Kunkle**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=phchDt63qAA) · [Conference site](https://www.ai.engineer/)

## Description

To validate settled data, Zed ran 10 frontier model predictions per example and measured Levenshtein distance to the final state. For 100,000 training examples that is a million frontier model requests, which is prohibitively expensive. The fix: Zeta 2's student model now approaches teacher quality, so they run it 50 times instead at negligible cost. Ben Conungle, edit predictions lead at Zed, walks through how this pipeline came together.

The pipeline pulls opt in production edit traces, distills them through a frontier teacher, and routes bad predictions through a repair step before formatting for the student. The ideal training examples sit in the middle of the Levenshtein distance distribution: too close to the settled state is obvious, too far is noise. A metric called reversal ratio, how often the model undoes exactly what the user just typed, was the key diagnostic for catching bad model behavior before shipping.
