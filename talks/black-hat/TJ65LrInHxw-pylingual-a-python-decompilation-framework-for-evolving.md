---
id: TJ65LrInHxw
title: "PyLingual: A Python Decompilation Framework for Evolving Python Versions"
slug: pylingual-a-python-decompilation-framework-for-evolving
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 25
published_at: 2025-02-26T18:33:22Z
video_id: TJ65LrInHxw
url: https://www.youtube.com/watch?v=TJ65LrInHxw
youtube_url: https://www.youtube.com/watch?v=TJ65LrInHxw
tags: []
topics: ["Security, safety & red teaming"]
transcript: false
---

# PyLingual: A Python Decompilation Framework for Evolving Python Versions

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=TJ65LrInHxw) · [Conference site](https://www.blackhat.com/)

## Description

Python has become a popular choice for creating malware due to its ease of development, wide user base, pre-built modules, and multi-platform compatibility. Python's popularity has induced demand for Python decompilers, but community efforts to maintain automatic Python decompilation tools have been hindered by Python's unstable bytecode specification. Every year, language features are added, code generation undergoes significant changes, and opcodes are added, deleted, and modified.

Our research aims to integrate Natural Language Processing (NLP) techniques with classical Programming Language (PL) theory to create a Python decompiler that adapts to new language features and changes to the bytecode specification with minimal human maintenance effort. PyLingual uses data-driven NLP components to automatically absorb superficial bytecode and compiler changes, while leveraging engineered programmatic components for abstract control flow reconstruction.

We demonstrate the efficacy of our approach with extensive real-world datasets of benign and malicious Python sources and their corresponding compiled PYC binaries. Our research makes three major contributions: (1) we present PyLingual, a scalable, data-driven decompilation framework with state-of-the-art support for Python versions 3.6 — 3.12; (2) we provide a Python decompiler evaluation framework that verifies decompilation results with "perfect decompilation"; and (3) we launch PyLingual as a free online service at https://pylingual.io, which has helped reverse engineer over 5,000 PYC binaries over the past three months.

By:
Josh Wiedemeier  |  Research Assistant, The University of Texas at Dallas
Elliot Tarbet  |  Student at The University of Texas at Dallas
Max Zheng  |  Student at The University of Texas at Dallas
Jerry Teng  |  Security Engineer, Flatiron Health
Ximeng Liu  |  Research Assistant, The University of Texas at Dallas
Muhyun Kim  |  Principal Data Scientist, AWS
Sang Kil Cha  |  Associate Professor, KAIST
Jessica Ouyang  |  Assistant Professor, The University of Texas at Dallas
Kangkook Jee  |  Assistant Professor, The University of Texas at Dallas

Full Abstract and Presentation Materials:
