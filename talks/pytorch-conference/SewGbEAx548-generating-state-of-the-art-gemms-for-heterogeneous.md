---
id: SewGbEAx548
title: "Generating State-of-the-Art GEMMs for Heterogeneous Hardware with... - Michael Lazos & Henry Tsang"
slug: generating-state-of-the-art-gemms-for-heterogeneous
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Michael Lazos", "Henry Tsang"]
channel: "PyTorch"
duration_min: 28
published_at: 2025-11-04T03:47:26Z
video_id: SewGbEAx548
url: https://www.youtube.com/watch?v=SewGbEAx548
youtube_url: https://www.youtube.com/watch?v=SewGbEAx548
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# Generating State-of-the-Art GEMMs for Heterogeneous Hardware with... - Michael Lazos & Henry Tsang

**Michael Lazos, Henry Tsang**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=SewGbEAx548) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

Generating State-of-the-Art GEMMs for Heterogeneous Hardware with TorchInductor - Michael Lazos and Henry Tsang, Meta

CUTLASS (Nvidia) and Composable Kernel (AMD) are header-only libraries generating high-performance GEMMs with flexible fusion capabilities. They provide GEMM templates that instantiate thousands of kernels with varying performance across different shapes, requiring runtime autotuning for optimal performance.

Our work integrates CUTLASS and CK into TorchInductor as GEMM backends. TorchInductor automates autotuning by precompiling kernels, caching locally/globally, and benchmarking to select optimal kernels during PT2 compilation. Generated kernels achieve state-of-the-art performance - up to 10% improvement over triton/cublas for some shapes in production workloads.

The backends support torch.compile, AOTInductor, and GEMMs like mm, addmm, bmm. FP8 GEMM and Grouped GEMM support is in progress.

We also support epilogue fusion for CUTLASS through epilogue visitor trees, which generate flexible C++ epilogues. Our custom tracer converts Python epilogue code into CUTLASS snippets representing operation trees following the GEMM. These snippets integrate into GEMM templates creating fused kernels. This fusion enhances performance and achieves feature parity with other backends like Triton.
