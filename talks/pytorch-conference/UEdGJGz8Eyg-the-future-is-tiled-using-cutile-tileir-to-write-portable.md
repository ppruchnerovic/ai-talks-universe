---
id: UEdGJGz8Eyg
title: "The Future Is Tiled: Using CuTile & TileIR To Write Portable, High-performance GPU...- Jared Roesch"
slug: the-future-is-tiled-using-cutile-tileir-to-write-portable
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: []
channel: "PyTorch"
duration_min: 28
published_at: 2025-11-04T03:46:55Z
video_id: UEdGJGz8Eyg
url: https://www.youtube.com/watch?v=UEdGJGz8Eyg
youtube_url: https://www.youtube.com/watch?v=UEdGJGz8Eyg
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# The Future Is Tiled: Using CuTile & TileIR To Write Portable, High-performance GPU...- Jared Roesch

**Speaker not identified**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=UEdGJGz8Eyg) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

The Future Is Tiled: Using CuTile and TileIR To Write Portable, High-performance GPU Kernels - Jared Roesch, NVIDIA

While tools like OpenAI Triton and PyTorch Inductor now enable Python programmers to write high-performance kernels with ease, the challenge remains in balancing algorithmic abstraction with evolving HW and performance optimization.

In this talk we’ll describe cuTile, a Python DSL that lets you author fast, portable CUDA kernels and TileIR, a new virtual ISA for NVIDIA GPUs that cuTile targets via a TileIR MLIR dialect.

cuTile extends CUDA kernel programming in Python to be closer to PyTorch or NumPy building on TileIR to make it easier to innovate on new high-performance programing abstractions.

TileIR is an array-based sibling abstraction to PTX that enables both forward compatibility and performance for GPU architecture-specific features such as tensor cores, across hardware generations, without time consuming rewrites.

We’ll show you how to write and use cuTile kernels, target TileIR, present performance results and present contributions such as our TileIR backend for Torch Inductor.

cuTile and TileIR were introduced at GTC 2025. cuTile will be open-sourced and open to community contributions and Tile IR will be released as part of the CUDA toolkit.
