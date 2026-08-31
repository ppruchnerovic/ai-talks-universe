---
id: 4Ol-_G_y2vQ
title: "Katrina Riehl - GPU Algorithm Authoring with CUDA Tile | Pydata London 26"
slug: katrina-riehl-gpu-algorithm-authoring-with-cuda-tile-pydata
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Katrina Riehl"]
channel: null
duration_min: 86
published_at: 2026-06-15T15:50:28Z
video_id: 4Ol-_G_y2vQ
youtube_url: https://www.youtube.com/watch?v=4Ol-_G_y2vQ
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Katrina Riehl - GPU Algorithm Authoring with CUDA Tile | Pydata London 26

**Katrina Riehl**

`PyData` · `PyData` · `2026` · `86 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=4Ol-_G_y2vQ) · [Conference site](https://pydata.org/)

## Description

Katrina Riehl - GPU Algorithm Authoring with CUDA Tile

Want to write your own GPU algorithms, but not sure how to get started or keep them portable? Come to this hands-on session to learn tile programming with CUDA Tile and cuTile Python: you will build an accurate mental model of tiles and thread groups, write and debug real GPU kernels in a browser-based JupyterLab (no installation), profile and tune performance with NVIDIA Nsight, and see how the same tile code applies across DL and HPC examples like LLM inference and conjugate gradient, including when to use tiles vs SIMT and how to mix both.

CUDA Tile is NVIDIA's new programming model for writing GPU kernels in an array-centric style that is portable across NVIDIA GPU architectures. Instead of orchestrating thousands of threads directly, you express computation over small local arrays (tiles) and let the system manage the parallel execution details: synchronization, data movement, and coordination across the GPU.

This interactive session introduces the core mental model behind tile programming and how it is realized in cuTile Python on top of the Tile IR compiler stack. You will write tile code, see how it maps onto real GPU execution, and learn how to evaluate and tune performance with NVIDIA's Nsight profilers. We'll explore examples from both DL and HPC, such as large language model inference and conjugate gradient solvers.

This session is hands-on with no installation required, just a web browser. We'll use Brev, NVIDIA's developer cloud, to get access to GPUs, and all work will be done in a JupyterLab environment.

By the end of this session, you will:
- Build an accurate mental model of tiles, thread groups, and how tile code executes on GPUs.
- Write and debug tile-based GPU kernels in Python for real workloads.
- Use profiling traces to identify bottlenecks and guide optimizations inside a notebook workflow.
- Decide when tile programming is the right tool versus SIMT, and how to mix the two when needed.

Links:
- Accelerated Computing Hub: https://github.com/NVIDIA/accelerated-computing-hub
- cuTile Python: https://github.com/NVIDIA/cutile-python
- Tile IR: https://github.com/NVIDIA/cuda-tile
- TileGym examples: https://github.com/NVIDIA/TileGym

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
