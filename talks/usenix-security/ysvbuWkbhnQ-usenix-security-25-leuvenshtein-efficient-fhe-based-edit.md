---
id: ysvbuWkbhnQ
title: "USENIX Security '25 - Leuvenshtein: Efficient FHE-based Edit Distance Computation with Single..."
slug: usenix-security-25-leuvenshtein-efficient-fhe-based-edit
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX Security"
year: 2025
speakers: []
channel: null
duration_min: 14
published_at: 2025-10-30T20:03:07Z
video_id: ysvbuWkbhnQ
youtube_url: https://www.youtube.com/watch?v=ysvbuWkbhnQ
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - Leuvenshtein: Efficient FHE-based Edit Distance Computation with Single...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2025` · `14 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=ysvbuWkbhnQ) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '25 - Leuvenshtein: Efficient FHE-based Edit Distance Computation with Single Bootstrap per Cell

Wouter Legiest and Jan-Pieter D'Anvers, COSIC, KU Leuven; Bojan Spasic and Nam-Luc Tran, Society for Worldwide Interbank Financial Telecommunication (Swift); Ingrid Verbauwhede, COSIC, KU Leuven

This paper presents a novel approach to calculating the Levenshtein (edit) distance within the framework of Fully Homomorphic Encryption (FHE), specifically targeting third-generation schemes like TFHE. Edit distance computations are essential in applications across finance and genomics, such as DNA sequence alignment. We introduce an optimised algorithm that significantly reduces the cost of edit distance calculations called Leuvenshtein. This algorithm specifically reduces the number of programmable bootstraps (PBS) needed per cell of the calculation, lowering it from approximately 94 operations—required by the conventional Wagner-Fisher algorithm—to just 1. Additionally, we propose an efficient method for performing equality checks on characters, reducing ASCII character comparisons to only 2 PBS operations. Finally, we explore the potential for further performance improvements by utilising preprocessing when one of the input strings is unencrypted. Our Leuvenshtein achieves up to 278x faster performance compared to the best available TFHE implementation and up to 39x faster than an optimised implementation of the Wagner-Fisher algorithm. Moreover, when offline preprocessing is possible due to the presence of one unencrypted input on the server side, an additional 3x speedup can be achieved.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
