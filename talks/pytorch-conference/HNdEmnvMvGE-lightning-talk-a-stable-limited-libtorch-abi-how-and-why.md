---
id: HNdEmnvMvGE
title: "Lightning Talk: A Stable Limited LibTorch ABI? How?! (and Why?) - Jane Xu, Meta"
slug: lightning-talk-a-stable-limited-libtorch-abi-how-and-why
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Jane Xu"]
channel: "PyTorch"
duration_min: 12
published_at: 2025-11-04T03:43:38Z
video_id: HNdEmnvMvGE
url: https://www.youtube.com/watch?v=HNdEmnvMvGE
youtube_url: https://www.youtube.com/watch?v=HNdEmnvMvGE
tags: []
topics: []
transcript: false
---

# Lightning Talk: A Stable Limited LibTorch ABI? How?! (and Why?) - Jane Xu, Meta

**Jane Xu**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=HNdEmnvMvGE) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Lightning Talk: A Stable Limited LibTorch ABI? How?! (and Why?) - Jane Xu, Meta

Do you use or maintain third-party C++/CUDA extensions with torch? (Think flash attention :)) Would you like to build that extension with one torch version and run with another torch version WITHOUT rebuilding the extension? Do you ever wish you didn’t have to rebuild all your wheels when a new PyTorch nightly or release came out? If so, then this talk is for you! Come explore our plans for a new limited stable libtorch ABI that you can build against to simplify your binary packaging situation. Trek with us through the cobwebs of detangling and rearranging C++ libtorch into header-only APIs and ABI-stable APIs powered through a C shim. Dream with us as we envision the possible futures we can build on top of a sturdier, stable, ABI compatible interface for fundamental concepts like Tensor. Before we get too ahead of ourselves though, sit tight and inquire of us about the new APIs we’re landing (like STABLE_TORCH_LIBRARY) so you can start building ABI stable PyTorch extensions ASAP!
