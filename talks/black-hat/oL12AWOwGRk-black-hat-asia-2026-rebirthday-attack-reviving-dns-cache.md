---
id: oL12AWOwGRk
title: "Black Hat Asia 2026 | RebirthDay Attack: Reviving DNS Cache Poisoning with the Birthday Paradox"
slug: black-hat-asia-2026-rebirthday-attack-reviving-dns-cache
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2026
speakers: []
channel: null
duration_min: 18
published_at: 2026-08-22T00:00:21Z
video_id: oL12AWOwGRk
youtube_url: https://www.youtube.com/watch?v=oL12AWOwGRk
tags: []
transcript: false
---

# Black Hat Asia 2026 | RebirthDay Attack: Reviving DNS Cache Poisoning with the Birthday Paradox

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=oL12AWOwGRk) · [Conference site](https://www.blackhat.com/)

## Description

DNS cache poisoning is a persistent game of attack and defense, posing an enduring challenge for the DNS community. Significant efforts have been made to uncover, detect, and mitigate vulnerabilities that increase the risk of cache poisoning. However, no work has systematically revisited whether the original cache poisoning attack based on the Birthday Paradox remains effective.

In this work, we will introduce RebirthDay, a novel DNS cache poisoning attack targeting recursive resolvers and forwarders, reviving the classic DNS Birthday attack that no longer works since 2002. RebirthDay exploits newly uncovered, protocol-compliant vulnerabilities in DNS extension implementations to bypass the query aggregation mechanism intended to prevent DNS Birthday attacks that have not been well understood. We uncovered that 18 out of 22 mainstream DNS software are vulnerable due to weaknesses in the processing of a DNS extension (i.e., ECS option), specifically lacking or incorrectly implemented ECS coherence checks when handling DNS queries and responses, demonstrating the widespread susceptibility to RebirthDay. These flaws could be exploited to circumvent the query aggregation mechanism and launch RebirthDay attacks. Through comprehensive evaluation, we showed that RebirthDay attacks are highly practical and can have significant real-world impact, affecting 16 router vendors, 14 public DNS services, and 365K (15%) open DNS resolvers.

We have reported the identified vulnerabilities to affected vendors and discussed mitigation solutions with them. To date, we have received acknowledgments from 8 vendors, including BIND, Unbound, PowerDNS, and Quad9, and have been assigned 50 CVE-ids. Our study emphasizes the need for greater attention to the importance of coherent ECS verification and the DNS extension implementation, revealing new security risks introduced by them.

Xiang Li  |  Associate Professor, Nankai University
Yuqi Qiu  |  PhD Student, Nankai University
Mingming Zhang  |  Assistant Researcher, Zhongguancun Laboratory
Zuyao Xu  |  Master Student, Nankai University
Lu Sun  |  Master Student, Nankai University
Fasheng Miao  |  Master Student, Tsinghua University
