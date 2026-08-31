---
id: zlGkhvhE-KQ
title: "OpenTelemetry At Scale 101: Intro to OpAMP - Aakansha Priya &Adriana Villela"
slug: opentelemetry-at-scale-101-intro-to-opamp-aakansha-priya
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: []
channel: null
duration_min: 52
published_at: 2026-03-04T16:44:30Z
video_id: zlGkhvhE-KQ
youtube_url: https://www.youtube.com/watch?v=zlGkhvhE-KQ
tags: ["OpAMP", "DevOps", "Architecture", "NDC", "Conferences", "2026", "Live", "Fun", "London", "England", "United Kingdom", "UK", "Great Britain"]
transcript: false
---

# OpenTelemetry At Scale 101: Intro to OpAMP - Aakansha Priya &Adriana Villela

**Speaker not identified**

`NDC Conferences` · `NDC` · `2026` · `52 min`

`#OpAMP` `#DevOps` `#Architecture` `#NDC` `#Conferences` `#2026` `#Live` `#Fun` `#London` `#England` `#United Kingdom` `#UK` `#Great Britain`

[Watch the recording](https://www.youtube.com/watch?v=zlGkhvhE-KQ) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC London in London, England. #ndclondon  #ndcconferences #developer #softwaredeveloper

Attend the next NDC conference near you:

/        @NDC

Follow our Social Media!

Managing telemetry at scale is hard. In large distributed systems, teams often deploy hundreds of OpenTelemetry Collector agents across clouds, edges, & on premise.

Keeping them properly configured, updated and healthy involves manual steps per host. Without a central control plane, it becomes error-prone and hard to scale, leading to config drift across fleets.

Enter OpAMP (Open Agent Management Protocol), which enables each agent to connect to a central server so it can “phone home” and receive instructions with capabilities like remote configs, health monitoring, agent telemetry and credential management, drastically simplifying Agent lifecycle. OpAMP is also vendor-agnostic, meaning the Server can remotely monitor & manage a fleet of different vendor Agents as long as they implement the OpAMP specification. In this talk, we’ll discuss the motivation behind OpAMP, the communication model, and how to enable it in the Otel Collector using the OpAMP Extension & Supervisor components.
