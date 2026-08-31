---
id: 5eIrd7bHy9I
title: "USENIX Security '24 - Inference of Error Specifications and Bug Detection Using Structural..."
slug: usenix-security-24-inference-of-error-specifications-and
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX Security"
year: 2026
speakers: []
channel: null
duration_min: 11
published_at: 2026-06-02T20:54:10Z
video_id: 5eIrd7bHy9I
youtube_url: https://www.youtube.com/watch?v=5eIrd7bHy9I
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '24 - Inference of Error Specifications and Bug Detection Using Structural...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `11 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=5eIrd7bHy9I) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

Inference of Error Specifications and Bug Detection Using Structural Similarities

Nora Dossche and Bart Coppens, Ghent University

Error-handling code is a crucial part of software to ensure stability and security. Failing to handle errors correctly can lead to security vulnerabilities such as DoS, privilege escalation, and data corruption. We propose a novel approach to automatically infer error specifications for system software without a priori domain knowledge, while still achieving a high recall and precision. The key insight behind our approach is that we can identify error-handling paths automatically based on structural similarities between error-handling code. We use the inferred error specification to detect three kinds of bugs: missing error checks, incorrect error checks, and error propagation bugs. Our technique uses a combination of path-sensitive, flow-sensitive and both intra-procedural and inter-procedural data-flow analysis to achieve high accuracy and great scalability. We implemented our technique in a tool called ESSS to demonstrate the effectiveness and efficiency of our approach on 7 well-tested, widely-used open-source software projects: OpenSSL, OpenSSH, PHP, zlib, libpng, freetype2, and libwebp. Our tool reported 827 potential bugs in total for all 7 projects combined. We manually categorised these 827 issues into 279 false positives and 541 true positives. Out of these 541 true positives, we sent bug reports and corresponding patches for 46 of them. All the patches were accepted and applied.

View the full USENIX Security '24 program at https://www.usenix.org/conference/usenixsecurity24/program
