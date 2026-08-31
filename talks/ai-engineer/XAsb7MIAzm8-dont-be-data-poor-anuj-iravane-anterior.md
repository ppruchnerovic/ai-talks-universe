---
id: XAsb7MIAzm8
title: "Don’t be data poor — Anuj Iravane, Anterior"
slug: dont-be-data-poor-anuj-iravane-anterior
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Anuj Iravane"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-08-19T00:00:00Z
video_id: XAsb7MIAzm8
youtube_url: https://www.youtube.com/watch?v=XAsb7MIAzm8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Don’t be data poor — Anuj Iravane, Anterior

**Anuj Iravane**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=XAsb7MIAzm8) · [Conference site](https://www.ai.engineer/)

## Description

Roughly 70% of medical communication still moves by fax. What reaches Anterior is scanned fax bundles that can run past 300 pages, carrying handwriting, checkboxes, tables and images across one patient's entire clinical trajectory. Anuj Iravane calls it an observation through a fuzzy lens over a lifespan. It is exactly the data his evals need, and the data he is least allowed to keep: their contracts rule out retaining it, deriving from it, or holding redacted or anonymized copies. Nothing survives into a dataset. In a domain where 95% accuracy is not good enough, that is a real problem.

So they generate it, by running the inference workflow backwards. The forward task takes unstructured data plus a policy, follows a reasoning trace and arrives at a label. Reversed, you sample a label, sample a reasoning trace, then build the record that would have produced it. That works because Anterior already models policies explicitly as decision trees, so traces come from a far more uniform distribution than a model asked to invent variety, which tends to collapse onto the same few cases. A coarse to fine pipeline layers patient invariants into a journey of provider encounters, then fans out into documents, with a consistency eval catching contradictions between documents written in parallel. Because generation starts from the label, labels are correct by construction and ground truthing disappears. Clinicians own the pipeline as skills rather than code. Roughly 90% of their datasets are now synthetic, and in a blind review clinicians separated synthetic from real only about 60% of the time.

Speaker info:
- https://x.com/anujiravane
- https://www.linkedin.com/in/anujiravane/
- https://www.anterior.com/

Timestamps:
0:00 - Policy guided decisions over highly unstructured data
1:05 - Most medical communication still arrives by fax
2:11 - Why 95% is not good enough
2:37 - The data you need most is the data you cannot keep
3:05 - Betting on generating it instead
3:55 - Why one shotting a 300 page record fails
5:00 - Reversing the forward task
5:51 - Policies as decision trees you can sample from
7:19 - Testing the edge cases production data never had
8:09 - Building a record coarse to fine
9:54 - The refinement loop and the round trip check
11:09 - Why it never becomes a PDF
11:34 - Giving clinicians the keys through skills
14:12 - Results, and datasets built just in time
