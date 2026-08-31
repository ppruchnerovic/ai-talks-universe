---
id: eP4gXyekgt0
title: "Protocol-Hopping C2: Transport-Agnostic Command & Control That Won't Die - Francine Solheim"
slug: protocol-hopping-c2-transport-agnostic-command-control-that
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: ["Francine Solheim"]
channel: null
duration_min: 19
published_at: 2026-03-27T12:39:26Z
video_id: eP4gXyekgt0
youtube_url: https://www.youtube.com/watch?v=eP4gXyekgt0
tags: ["Hacking", "Fun", "Security Tooling", "NDC", "Conferences", "2026", "Live", "Oslo", "Norway", "Francine Solheim"]
transcript: false
---

# Protocol-Hopping C2: Transport-Agnostic Command & Control That Won't Die - Francine Solheim

**Francine Solheim**

`NDC Conferences` · `NDC` · `2026` · `19 min`

`#Hacking` `#Fun` `#Security Tooling` `#NDC` `#Conferences` `#2026` `#Live` `#Oslo` `#Norway` `#Francine Solheim`

[Watch the recording](https://www.youtube.com/watch?v=eP4gXyekgt0) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Security in Oslo, Norway. #ndcsecurity  #ndcconferences  #security  #developer   #softwaredeveloper

Attend the next NDC conference near you:

Follow our Social Media!

Modern command-and-control (C2) frameworks don't just fall over when you block one protocol - they pivot, quietly but surely. The C2 brain, the intent and the goal stay the same, but the wire changes. If your detection strategy is married to ports or protocol signatures, then you're already behind - and at risk.

This talk will explore a small Python-based C2 lab with pluggable transports: the same controller/agent pair that can talk over ICMP payloads, DNS TXT records and HTTP headers, and automatically fails over to another protocol without changing its core logic when detection occurs.

The goal is not to show off yet another tunnel or a 'hey look, an ICMP data exfiltrator!', but to make the architectural pattern behind advanced tools like Cobalt Strike as painfully obvious as possible: C2 logic is transport-agnostic, indifferent, and ruthless, and protocol-centric defences are outdated.
