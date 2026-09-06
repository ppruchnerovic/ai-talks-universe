---
id: u5074_0k0UU
title: "From Model To Trust: Building Upon Tamper-proof ML Metadata Records - Mihai Maruseac, Google"
slug: from-model-to-trust-building-upon-tamper-proof-ml-metadata
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Mihai Maruseac"]
channel: "PyTorch"
duration_min: 25
published_at: 2025-11-04T03:45:47Z
video_id: u5074_0k0UU
url: https://www.youtube.com/watch?v=u5074_0k0UU
youtube_url: https://www.youtube.com/watch?v=u5074_0k0UU
tags: []
topics: []
transcript: false
---

# From Model To Trust: Building Upon Tamper-proof ML Metadata Records - Mihai Maruseac, Google

**Mihai Maruseac**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=u5074_0k0UU) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

From Model To Trust: Building Upon Tamper-proof ML Metadata Records - Mihai Maruseac, Google

The integrity and provenance of machine learning models are critical for building trustworthy AI systems. While cryptographic signing protects many digital assets, a standardized approach for verifying model origins and ensuring they haven't been tampered with is still missing. We are addressing this gap by building upon the OpenSSF Model Signing project – a PKI-agnostic method for creating verifiable claims on bundles of ML artifacts. We show how this project can expand beyond just model signing to also cover datasets, and other associated files, recording all integrity information in a single manifest.

In fact, this can be used as a foundation layer upon which we can build useful AI supply-chain solutions, both in terms of security and in terms of reducing development costs. Imagine querying "What datasets were used to train this model?" or determining which models and agents have been trained on a poisoned dataset, even before these get deploy in production systems. This is all possible by merging model signing, model cards, SLSA and AI-BOM information and analyzing all this metadata using tools such as GUAC. Our talk lays the groundwork for such capabilities.
