---
id: 23egdat_wfU
title: "Jongryool Kim - Disaggregated LLM Serving with Shared Memory KV Cache at Rack Scale"
slug: jongryool-kim-disaggregated-llm-serving-with-shared-memory
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Jongryool Kim"]
channel: "Berkeley RDI"
duration_min: 5
published_at: 2026-08-12T07:49:56Z
video_id: 23egdat_wfU
url: https://www.youtube.com/watch?v=23egdat_wfU
youtube_url: https://www.youtube.com/watch?v=23egdat_wfU
tags: []
transcript: true
---

# Jongryool Kim - Disaggregated LLM Serving with Shared Memory KV Cache at Rack Scale

**Jongryool Kim**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=23egdat_wfU) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*650 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=23egdat_wfU&t=2s)** SPEAKER: Hello, everyone. My name is [? Junior ?] [? Kim ?] from SK Hynix. I'm senior director, and I'm also working for the SRC as a sub. So today, I want to talk about the new memory as a physically disaggregated pooled memory. So this is a memory pool disaggregated from the servers. So in this diagram, so no domain server. And this is a memory pool box is really a disaggregated memory pool. So multiple server can use this memory pool at the same time with the two modes. The first one is a memory pooling. So each node can dynamically allocate the additional memory, but that memory region is isolated between node. But as a sharing mode, sharing mode is a multiple node.

**[0:50](https://www.youtube.com/watch?v=23egdat_wfU&t=50s)** Can see the same memory address space. So each node can access the same data. So we are very interested in this sharing feature, so we quickly integrated this memory pool with the real LLM serving system. So we successfully deployed this system, and we demonstrated at the last year so many events. So in this diagram, so there are four servers, and four servers can work with so many random serving component. And the middle of the rack, that is a [? Niagara. ?] That is a real physical as a pooled memory. In this demo scenario, so we use that memory pool for transferring the key value cache.

**[1:43](https://www.youtube.com/watch?v=23egdat_wfU&t=103s)** At first, prepare. After prepare, we need to deliver the key value cache to the decoding side. So by using the two memory copy, store and load, we can deliver the KV cache to the decoding node. But we can [? find ?] that. In this system, all KV cache can be stored in the memory pool. So we can reuse it for the next request without some additional storing of operation for reusing. So as a result, we can improve the system performance compared with the overall competition. This is an [? XL. ?] And LM-Cache [INAUDIBLE] server is a DRAM-based KV cache storing. But the important part is why we can have this kind of benefit. The first one is fast interserver data movement by using the pooled memory.

**[2:34](https://www.youtube.com/watch?v=23egdat_wfU&t=154s)** Yeah. Instead of using the TCP/IP, we generally use RDMA. This is fast. But this pooled memory-based data sharing is faster than RDMA so we can have a performance improvement for the LLM serving system. Second one is by using the pooled memory-based data sharing, so we can have another benefit. We can release the GPU HBM immediately by operating the KV cache to the pooled memory. So if there is out of memory at the decoding side and prepare side, but we can continuously do the prepare because we already uploaded that KV cache to the pooled memory side. And so to store the KV cache and for reuse the KV cache, there are many contention can be happened in the GPU side, GPU side PCI bandwidth, and network side PCI

**[3:25](https://www.youtube.com/watch?v=23egdat_wfU&t=205s)** bandwidth. There are many contention. But by using our pooled memory-based data sharing and transfers, we can remove this kind of additional contention. So we deployed an agent AI service system, so we should reuse the large amount of KV cache. So we applied this system. We applied the agent AI serving system to the pooled memory environment. And we can find this kind of performance improvement compared with the Mooncake and LM-cache. That is a very initial performance number, but by end of this year, I'm working with many collaboration parties. Around the 25 parties, we are preparing the five more system POC, such as multimodal serving and long-term memory management. And we are trying to build the real system

**[4:16](https://www.youtube.com/watch?v=23egdat_wfU&t=256s)** with the pooled memory for the HPC, a US-based national lab system. So yeah. That's it, how the pooled memory can change the AI system. That's it. Thank you. [APPLAUSE]
