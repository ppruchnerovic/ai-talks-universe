---
id: eyEsg7SGEKY
title: "Viktor Kessler - Zero Trust with Iceberg REST Catalog and Policy Engines | Pydata London 26"
slug: viktor-kessler-zero-trust-with-iceberg-rest-catalog-and
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Viktor Kessler"]
channel: null
duration_min: 33
published_at: 2026-06-15T15:55:08Z
video_id: eyEsg7SGEKY
youtube_url: https://www.youtube.com/watch?v=eyEsg7SGEKY
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Viktor Kessler - Zero Trust with Iceberg REST Catalog and Policy Engines | Pydata London 26

**Viktor Kessler**

`PyData` · `PyData` · `2026` · `33 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=eyEsg7SGEKY) · [Conference site](https://pydata.org/)

## Description

Viktor Kessler - Governance-as-Code for the Lakehouse: Zero Trust with Iceberg REST Catalog and Policy Engines

Modern lakehouse architectures promise flexibility and scale — but governance is often an afterthought. While we version data and evolve schemas, we rarely version or test access policies.

This talk explores how to implement governance-as-code in a lakehouse using the REST Catalog from Apache Iceberg, applying Zero Trust principles and enforcing fine-grained policies with Open Policy Agent (OPA) and Cedar.

Attendees will learn how to move from static IAM and implicit trust to centralized, engine-agnostic, policy-driven governance.

Lakehouse architectures unify data lakes and warehouses, but governance models often lag behind the architectural innovation. Access control is frequently engine-specific, policies are fragmented, and trust is implicit.

This talk argues that the missing layer in many lakehouse implementations is governance-as-code enforced at the catalog boundary.

We explore:
- How the Iceberg REST Catalog introduces a centralized enforcement point decoupled from compute engines
- Why Zero Trust principles apply to data platforms (no implicit trust between engines, users, or services)
- How policy-as-code systems such as OPA and Cedar enable versioned, testable, auditable access control
- Patterns for implementing fine-grained authorization (row/column-level policies, environment isolation, service-to-service trust)
- How governance becomes reproducible and portable across Spark, Flink, Trino, and other engines

The session focuses on architectural patterns rather than vendor-specific tooling and highlights practical trade-offs when implementing policy enforcement in production lakehouses.

Key Takeaways
1. Understand why traditional RBAC is insufficient for modern lakehouses
3. Learn how REST-based catalog architectures enable centralized governance
5. See how Zero Trust can be applied to data access workflows
7. Discover how to implement policy-as-code using OPA or Cedar
9. Gain a reference architecture for governance-first lakehouse design

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
