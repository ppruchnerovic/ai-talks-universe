---
id: ECx2LhpxaVY
title: "Software ISP FOSS Support for MIPI Cameras - Hans de Goede, Red Hat & Bryan O'Donoghue, Linaro"
slug: software-isp-foss-support-for-mipi-cameras-hans-de-goede
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "Open Source Summit EU 2025"
year: 2025
speakers: ["Hans de Goede"]
channel: "The Linux Foundation"
duration_min: 42
published_at: 2025-09-05T19:39:24Z
video_id: ECx2LhpxaVY
url: https://www.youtube.com/watch?v=ECx2LhpxaVY
youtube_url: https://www.youtube.com/watch?v=ECx2LhpxaVY
tags: []
transcript: false
---

# Software ISP FOSS Support for MIPI Cameras - Hans de Goede, Red Hat & Bryan O'Donoghue, Linaro

**Hans de Goede**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit EU 2025` · `2025` · `42 min`

[Watch the recording](https://www.youtube.com/watch?v=ECx2LhpxaVY) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Don't miss out! Join us at the next Open Source Summit in Seoul, South Korea (November 4-5). Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Software ISP FOSS Support for MIPI Cameras - Hans de Goede, Red Hat & Bryan O'Donoghue, Linaro

Many recent Windows (on ARM and x86) laptops have replaced the standard UVC USB camera module with a raw MIPI camera-sensor using a CSI receiver and ISP in the CPU to process the raw data into an image (and on smartphones this has been the norm for ages).

Supporting these cameras under Linux is an ongoing challenge. At FOSDEM 2024 a solution using a software ISP running on the CPU was presented as a solution to get these cameras to work with a fully opensource stack.

This talk will look at where support for MIPI cameras using the software ISP is at now, 1.5 years later, mainly focusing on the ubiquitous x86 laptops using cameras connected to Intel's IPU6.

Depending on ongoing work this will include a demo of recent developments such as running the software ISP on the GPU and the first FOSS color-corrected images from an IPU6 attached sensor with the color calibration done using all FOSS tools.
