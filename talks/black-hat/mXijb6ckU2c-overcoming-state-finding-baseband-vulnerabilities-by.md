---
id: mXijb6ckU2c
title: "Overcoming State: Finding Baseband Vulnerabilities by Fuzzing Layer-2"
slug: overcoming-state-finding-baseband-vulnerabilities-by
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 36
published_at: 2025-02-24T18:12:36Z
video_id: mXijb6ckU2c
youtube_url: https://www.youtube.com/watch?v=mXijb6ckU2c
tags: []
transcript: false
---

# Overcoming State: Finding Baseband Vulnerabilities by Fuzzing Layer-2

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `36 min`

[Watch the recording](https://www.youtube.com/watch?v=mXijb6ckU2c) · [Conference site](https://www.blackhat.com/)

## Description

Mobile phones are integrated parts of today's society. To connect to cellular networks, they use specialized baseband processors, which expose a large attack surface due to their wireless nature and the many types of supported mobile generations. Over the last decade, security research discovered plenty of flaws in these devices with devastating consequences, such as remote compromise via SMS.

One especially powerful tool for vulnerability discovery proved to be emulation of the baseband's firmware. However, as we will show, most prior efforts focus on emulation of single components and parsers or only focused on network (Layer-3) protocols and messages. In this talk, we will take a different approach and explore the attack surface exposed by Layer-2 with a focus on GSM; Despite the availability of more recent cellular communication technologies, GSM stacks are still present in nowadays' phones and provide a lucrative attack surface.

We will discuss how we got acquainted with Layer-2 data frames and how we used our insights to create fuzzing harnesses within the FirmWire framework. Due to the structure of the cellular network stack, our approach resulted in simultaneous fuzzing of Layer-3 tasks. Our approach led to the discovery of multiple high and critical-severity vulnerabilities in already well-explored parts of the cellular stack in modern Samsung and Google phones.

This talk will highlight our findings, including a deep-dive into two vulnerabilities and modern baseband defenses. We also discuss how we verified the existence of our—at the time—freshly discovered zero days in recent smartphones over-the-air, most notably in a latest-gen flagship phone just one week after its market launch.

By:
Dyon Goos  |  Independent Researcher
Marius Muench  |  Assistant Professor, University of Birmingham

Full Abstract and Presentation Materials:
