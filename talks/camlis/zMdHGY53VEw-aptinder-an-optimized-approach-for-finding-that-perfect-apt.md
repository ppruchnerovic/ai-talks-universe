---
id: zMdHGY53VEw
title: "APTinder: An optimized approach for finding that perfect APT match"
slug: aptinder-an-optimized-approach-for-finding-that-perfect-apt
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: null
duration_min: 29
published_at: 2018-11-16T17:11:34Z
video_id: zMdHGY53VEw
youtube_url: https://www.youtube.com/watch?v=zMdHGY53VEw
tags: ["camlis", "camlis2018"]
transcript: false
---

# APTinder: An optimized approach for finding that perfect APT match

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `29 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=zMdHGY53VEw) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Matthew Berninger, FireEye
APTinder: An optimized approach for finding that perfect APT match (slides: https://www.camlis.org/matthew-berninger/)

APTinder: An optimized approach for finding that perfect APT match

It is the job of the SOC and IR team to collect, classify, and report malicious cyber activity. Knowing "who" is behind an attack can help an Incident Response team anticipate the adversary’s next move, or understand what the attackers' end goal may be. In order to be useful, this attribution need not always be tied to geography. Simply knowing "this backdoor is used by group X, who also tends to use Y method of lateral movement" can be enough context to help an IR team optimize their investigation. Knowing where group X lives, or what language they speak, may not always be knowable, or necessary.

But how are these groups of activity built over time? How do we "know" that certain activities are related or similar? How confident do we need to be to “merge” highly similar groups? There is no universal answer key in the industry for these questions, so we are left with the experience and reasoning of intel analysts. A quick survey around the cyber intelligence industry reveals a tangled web of associations, multiple naming conventions, and overlaps between established “groups”. Rather than depending on instinct and intuition, we sought to find a way to provide intel analysts with simple, objective information to assist in making these grouping decisions.

Viewed from a pure data science perspective, this cyber intelligence problem begins to look very similar to a clustering and topic modeling problem. By creating 'documents' from a corpus of intelligence knowledge, we vectorized each body of activity, and then explored different similarity metrics to build a distance matrix. From there, we performed clustering and topic modeling to show interesting dynamics in the global cyber threat intelligence space.

We built the initial proof of concept with data collected from over a decade of incident response and intelligence activities. Using features such as tools, infrastructure, timing, and targeting, we were able to calculate objective similarity between hundreds of adversary groups. We directly expose this distance metric, along with context, to intel analysts as they make intelligence assessments. Comparing our model’s output with their intuition has helped to challenge assumptions, expose data modeling gaps, and highlight associations between previously unknown groups.

Further challenges to this approach include the proper modeling of cyber threat information, normalization, and variations in confidence. Additionally, correctly adjusting for time is a key area of improvement, given the rapid changes to the cyber threat environment. Even if these are solved, there will always be information in the cyber intelligence space which eludes a formal data model. However, exposing the objective similarities - or dissimilarities - of groups of activity can help illuminate gaps, provide leads, and challenge biases. We have found this approach to be a useful tool in our quest to map and model the many (and multiplying) cyber adversaries around the globe.
