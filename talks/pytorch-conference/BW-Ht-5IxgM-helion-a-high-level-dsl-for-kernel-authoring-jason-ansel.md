---
id: BW-Ht-5IxgM
title: "Helion: A High-level DSL for Kernel Authoring - Jason Ansel, Meta"
slug: helion-a-high-level-dsl-for-kernel-authoring-jason-ansel
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Jason Ansel"]
channel: "PyTorch"
duration_min: 28
published_at: 2025-11-04T03:45:03Z
video_id: BW-Ht-5IxgM
url: https://www.youtube.com/watch?v=BW-Ht-5IxgM
youtube_url: https://www.youtube.com/watch?v=BW-Ht-5IxgM
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Helion: A High-level DSL for Kernel Authoring - Jason Ansel, Meta

**Jason Ansel**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=BW-Ht-5IxgM) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Helion: A High-level DSL for Kernel Authoring - Jason Ansel, Meta

The Meta PyTorch Team plans to announce a public beta for Helion at PyTorch conference, with the goal of attracting users. Helion is a new kernel authoring DSL tightly integrated with, and using many parts of, PyTorch 2.

Helion is a Python-embedded domain-specific language (DSL) designed for authoring machine learning kernels. It compiles down to Triton, a high-performance backend for programming GPUs and other accelerators. By raising the abstraction level compared to Triton, Helion simplifies kernel development, minimizes boilerplate, and significantly enhances maintainability and portability.

Key features of Helion include extensive automation in autotuning processes, implicit search space definitions, kernel templating via Python closures, and advanced integration with PyTorch 2, including support for tensor subclasses. This talk will introduce Helion, detail its design principles, demonstrate current capabilities, and provide insights into its implementation.
