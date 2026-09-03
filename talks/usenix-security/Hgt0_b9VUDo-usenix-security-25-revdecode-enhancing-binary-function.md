---
id: Hgt0_b9VUDo
title: "USENIX Security '25 - REVDECODE: Enhancing Binary Function Matching with Context-Aware Graph..."
slug: usenix-security-25-revdecode-enhancing-binary-function
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 14
published_at: 2025-10-30T20:03:05Z
video_id: Hgt0_b9VUDo
url: https://www.youtube.com/watch?v=Hgt0_b9VUDo
youtube_url: https://www.youtube.com/watch?v=Hgt0_b9VUDo
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Security, safety & red teaming"]
transcript: false
---

# USENIX Security '25 - REVDECODE: Enhancing Binary Function Matching with Context-Aware Graph...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `14 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=Hgt0_b9VUDo) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

REVDECODE: Enhancing Binary Function Matching with Context-Aware Graph Representations and Relevance Decoding

Tongwei Ren, Ronghan Che, and Guin R. Gilman, Worcester Polytechnic Institute; Lorenzo De Carli, University of Calgary; Robert J. Walls, Worcester Polytechnic Institute

Binary reverse engineering is important for security tasks, including vulnerability discovery, malware analysis, and code reuse detection. These tasks often involve analyzing binaries without source code or debug symbols. A common yet challenging step in this process is function matching, i.e., comparing functions in unknown binaries to known reference corpora. Function matching becomes complicated due to variations introduced by differences in compilers, optimization levels, and versions. Existing matching techniques primarily focus on similarity but reverse engineers prioritize relevance—whether a match provides meaningful insights.

We present REVDECODE, a context-aware framework designed to improve function matching by leveraging interdependencies within binaries through relevance decoding, a technique that identifies meaningful matches based on contextual information. REVDECODE represents binaries as directed layered graphs and employs a Viterbi-inspired algorithm to determine the most relevant matches. Additionally, we propose GPU-optimized variants of REVDECODE which partition the graph traversal workload into independent subsets, maximizing GPU resource utilization and enabling greater parallelization. Experimental results demonstrate that REVDECODE significantly enhances the performance of existing function matchers, improving rankings for 56.3% to 98.8% of the evaluated functions across multiple datasets and matchers.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
