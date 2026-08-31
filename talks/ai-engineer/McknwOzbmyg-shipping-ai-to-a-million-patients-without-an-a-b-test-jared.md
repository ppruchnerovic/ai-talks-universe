---
id: McknwOzbmyg
title: "Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia"
slug: shipping-ai-to-a-million-patients-without-an-a-b-test-jared
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Jared Joselowitz"]
channel: null
duration_min: 19
published_at: 2026-08-19T15:00:31Z
video_id: McknwOzbmyg
youtube_url: https://www.youtube.com/watch?v=McknwOzbmyg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia

**Jared Joselowitz**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=McknwOzbmyg) · [Conference site](https://www.ai.engineer/)

## Description

You cannot A/B test on patients, because randomizing someone into the worse variant is unethical and often illegal. You cannot undo a call once spoken. And a vendor's benchmark number is not a defense at a post incident review. Jared Joselowitz builds the safety and evaluation stack behind Dora, a Ufonia voice agent that phones patients for post op follow ups and pre op checks. It has made roughly 200,000 real clinical calls across 20 UK hospitals and is contracted to reach a million patients within two years. Because it asks about symptoms and gives advice, it is a regulated medical device.

Ship to 5% and watch the dashboard does not survive that. 5% is thousands of patients, and a dashboard turning red means someone was already harmed. So the reactive loop moves into simulation, as self driving did with millions of simulated miles. Their framework has one model play the patient against hazards written with clinicians, and a second model judge every dialogue. Both were validated rather than assumed. In a patient and public involvement study, real patients shown a genuine consultation beside a simulated one picked the simulated patient as more realistic in three of four sets. The judge, checked against 10 clinicians from 10 specialties on 240 cases, matched or beat them at near perfect sensitivity, the metric that counts when a missed red flag is catastrophic and a false alarm is merely annoying. Prompts are then optimized against a cost matrix instead of hand tuned. You do not ship the model, you ship the evidence.

Speaker info:
- https://x.com/JaredJoselowitz
- https://www.linkedin.com/in/jaredjoselowitz/
- https://jossy.co.za/

Timestamps:
0:00 - Proving a product is safe before a patient hears it
1:28 - What Dora is, and the scale it runs at
2:18 - A call with a patient after cataract surgery
3:22 - Giving advice makes it a regulated medical device
3:59 - Starting from what could actually harm someone
4:35 - Why ship to 5% and roll back breaks here
5:53 - Borrowing the simulation playbook from self driving
6:32 - Matrix, and a model that plays the patient
8:24 - Can real patients tell which one is simulated
9:43 - An automated judge, and validating it against clinicians
11:35 - How brittle prompts really are
12:50 - Optimizing prompts instead of hand tuning them
13:30 - Making the metric a real cost function
14:42 - The flywheel that replaces the reactive loop
15:20 - Simulation is necessary, not sufficient
16:38 - Shipping the evidence, not the model
17:14 - New modalities bring new hazards, same framework
