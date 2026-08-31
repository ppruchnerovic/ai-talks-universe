---
id: klFR-KFR_EY
title: "Beyond “System Complete”: Shipping Globally with Agentic Commerce Orchestration"
slug: beyond-system-complete-shipping-globally-with-agentic
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: null
duration_min: 11
published_at: 2026-08-11T13:10:10Z
video_id: klFR-KFR_EY
youtube_url: https://www.youtube.com/watch?v=klFR-KFR_EY
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Beyond “System Complete”: Shipping Globally with Agentic Commerce Orchestration

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `11 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=klFR-KFR_EY) · [Conference site](https://mlopsworld.com/)

## Description

Amit Kumar Padhy, Senior Computer Scientist II, Adobe Inc.

About the Speaker:
Amit Kumar Padhy is a Senior Computer Scientist II and Lead Architect at Adobe. Based in Sunnyvale in the San Francisco Bay Area, he works out of Adobe’s San Jose, California headquarters. He specializes in cloud-native platforms, distributed systems, and AI-enabled digital commerce, and architects and modernizes mission-critical, event-driven microservices at global scale, emphasizing reliability, performance, cost optimization, and platform governance. Amit is an invited keynote speaker at international IEEE conferences and has delivered PRO-level talks at leading industry events, including DeveloperWeek, ProductWorld, and major IEEE, AI, and Data Summits. He also serves on advisory boards for IEEE and ACM conferences.

Abstract:
Distributed commerce platforms don't fail because features are missing, they fail at the seams. A product is created in Catalog, but pricing is incomplete. Promotions don't qualify. A compliance rule blocks three regions. The system says ""launched."" The business knows it isn't.

This talk replaces traditional workflow orchestration with a production-tested, multi-agent swarm model that coordinates Pricing, Catalog, Promotions, Tax, and Compliance in real time, driving products to a verified sellable state, not just workflow completion.

We'll walk through a concrete architecture: Planner Agents using ReAct-style reasoning to decompose onboarding goals into dynamic execution graphs; Domain Agents that invoke live APIs (Pricing Runtime, Billing Preview, Tax engines) as tools; Validator Agents enforcing regulatory and pricing integrity at every step; and a Coordinator Agent maintaining shared state via a blackboard-pattern memory layer over Kafka-backed events.

The hard lessons are where this talk earns its value. We over-used LLMs and paid for it in latency and cost, until we scoped them strictly to planning and exception handling. Centralized orchestration became a bottleneck, until we shifted to loosely coupled, domain-specific agents. Compliance flows exposed the limits of probabilistic reasoning, until we layered in deterministic, rule-based validators as a fallback.

Attendees will leave with a working blueprint for LLM-agent swarms that handle uncertainty across distributed systems, recover through intelligent compensation (not blind retries), and produce auditable decision traces, so when something fails, you know why, not just where.

Key takeaways: event-driven agent coordination patterns, selective LLM invocation strategies, saga/compensation design for agent failures, and a practical observability model built around decision reasoning."
