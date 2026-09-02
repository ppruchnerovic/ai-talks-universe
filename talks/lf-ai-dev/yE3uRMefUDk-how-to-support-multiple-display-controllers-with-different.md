---
id: yE3uRMefUDk
title: "How To Support Multiple Display Controllers With Different Inter... Devarsh Thakkar & Aradhya Bhatia"
slug: how-to-support-multiple-display-controllers-with-different
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "General software conferences"
edition: "Open Source Summit EU 2025"
year: 2025
speakers: []
channel: "The Linux Foundation"
duration_min: 32
published_at: 2025-09-05T19:40:15Z
video_id: yE3uRMefUDk
url: https://www.youtube.com/watch?v=yE3uRMefUDk
youtube_url: https://www.youtube.com/watch?v=yE3uRMefUDk
tags: []
topics: []
transcript: false
---

# How To Support Multiple Display Controllers With Different Inter... Devarsh Thakkar & Aradhya Bhatia

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit EU 2025` · `2025` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=yE3uRMefUDk) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

How To Support Multiple Display Controllers With Different Interfaces on One SoC - Devarsh Thakkar, Texas Instruments & Aradhya Bhatia, ARM Limited

Modern SoCs often integrate multiple display controllers to support advanced use-cases such as multi-display setups, content mirroring, or screen extension. These controllers typically support heterogeneous interfaces like DSI, HDMI, OLDI, or (e)DP to accommodate a wide range of panels and bridge devices. Taking TI’s AM62P SoC as an example-which includes two display controllers, a GPU, and multiple interfaces such as DSI, DPI/HDMI, and OLDI-this talk will cover the design considerations involved in enabling Linux DRM driver support for such systems. It will explore two key approaches for supporting multiple controllers: integrating both under a single DRM card versus exposing them as 2x separate DRM cards, along with their pros and cons. The talk will also highlight the architectural changes made to support dual OLDI bridges multiplexed between controllers, allowing either configurations–dual-link (from a single controller) or 2x single-link (from separate controllers). Finally, it will discuss the challenges with DSI bridge integration, particularly around crtc-encoder-bridge operation sequences, and how bridge APIs can be used to support custom sequences for bridge operations.
