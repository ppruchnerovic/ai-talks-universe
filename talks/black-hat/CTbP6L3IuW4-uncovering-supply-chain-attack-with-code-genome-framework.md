---
id: CTbP6L3IuW4
title: "Uncovering Supply Chain Attack with Code Genome Framework"
slug: uncovering-supply-chain-attack-with-code-genome-framework
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 40
published_at: 2025-03-13T17:30:28Z
video_id: CTbP6L3IuW4
url: https://www.youtube.com/watch?v=CTbP6L3IuW4
youtube_url: https://www.youtube.com/watch?v=CTbP6L3IuW4
tags: []
topics: ["RAG, retrieval & knowledge", "Science, healthcare & applied ML", "Security, safety & red teaming"]
transcript: false
---

# Uncovering Supply Chain Attack with Code Genome Framework

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `40 min`

[Watch the recording](https://www.youtube.com/watch?v=CTbP6L3IuW4) · [Conference site](https://www.blackhat.com/)

## Description

Software supply chain security often relies on metadata provided by suppliers. An attacker may compromise somewhere in the supply chain (e.g., source code, build process, or distribution channel) to manipulate the final distributed binary package, embedding the attack logic or payload in the binary. However, it is impractical and challenging for end users to analyze and verify the binary code. We rather resort to trusting the accompanying metadata, such as the supplier's description, cryptographic signature, and software bill of materials (SBOM), if available. Unfortunately, there can be a semantic gap between the code behavior and its metadata, allowing supply chain attacks.

To address this problem, we are open sourcing the Code Genome Framework to generate code fingerprints capturing computation semantics besides metadata, which aims to reduce the said semantic gap. The extracted semantic fingerprints, or "genes", allow us to assess the computational behavior of a binary without relying on metadata. The current release includes core functionalities, such as gene extraction from binaries without source code, gene-level binary diffing (i.e., GeneDiff), and gene searching by constructing a basic knowledge graph. The framework supports common binary formats and architectures, and we have added support for JAR files and enhanced the processing pipeline. The framework is extensible, allowing to add custom gene extraction and embedding methods.

In this talk, we will discuss in-depth technical details and demonstrate how Code Genome can help automatically detect "XZ backdoor" and similar attacks, provide alternatives to validating reproducible build, ensure cross-platform equivalent builds in CI/CD, and examine incremental version differences. Additionally, we will demonstrate building a large knowledge graph of open source software, allowing us to identify software components of an unknown binary to generate and verify SBOM.

By:
Dhilung Kirat  |  Senior Research Scientist, IBM Research
Jiyong Jang  |  Principal Research Scientist, IBM Research

Full Abstract and Presentation Materials:
