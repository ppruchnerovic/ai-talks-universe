---
id: 3HrGoSPT8cU
title: "MaLDAPtive: Diving Deep Into LDAP Obfuscation, Deobfuscation & Detection"
slug: maldaptive-diving-deep-into-ldap-obfuscation-deobfuscation
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 40
published_at: 2025-02-20T18:18:28Z
video_id: 3HrGoSPT8cU
url: https://www.youtube.com/watch?v=3HrGoSPT8cU
youtube_url: https://www.youtube.com/watch?v=3HrGoSPT8cU
tags: []
topics: ["Security, safety & red teaming"]
transcript: false
---

# MaLDAPtive: Diving Deep Into LDAP Obfuscation, Deobfuscation & Detection

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `40 min`

[Watch the recording](https://www.youtube.com/watch?v=3HrGoSPT8cU) · [Conference site](https://www.blackhat.com/)

## Description

LDAP is no stranger to the security spotlight. While LDAP is a protocol (Lightweight Directory Access Protocol) and Active Directory is the most popular directory services system that supports a subset of LDAP, the terms "LDAP" and "AD" are tightly coupled when discussing the execution, detection and prevention of attacks targeting directory services data.

In the last decade, the widespread offensive value of querying AD data via LDAP was crystalized in the security community with the release of open-source tools such as BloodHound (SpecterOps, 2016) and PingCastle (Vincent Le Toux, 2017). The defensive community slowly caught up by identifying ways to log and monitor issued LDAP queries on the client device, server and even over the network (with many caveats applied to all three scenarios). However, even today these islands of LDAP visibility are not as ubiquitous as common event logs.

Therefore, proper LDAP visibility mostly remains a privileged asset for those organizations that can afford a slow-growing pool of security agents and services capable of efficiently consolidating issued LDAP queries into a searchable format. Additionally, the security industry's maturity in hunting and detecting malicious LDAP usage is woefully limited to signatures targeting precise search filter substrings found in common open-source attack tools.

MaLDAPtive is the 2,000-hour (and counting) quest of offensive and defensive LDAP exploration and tool-building. This research includes mind-bending depths of obfuscation across all elements of LDAP queries (many undocumented and most never seen in the wild), all baked into an obfuscation/de-obfuscation framework built upon our ground-up custom LDAP search filter tokenizer and syntax tree parser. This foundation also serves as the base for our detection framework, complete detection rule set and feature generator prepped for the data science community.

Come witness the release of our MaLDAPtive research and open-source framework: transforming LDAP from "lightweight" to "heavyweight."

By:
Daniel Bohannon  |  Principal Threat Researcher, Permiso Security
Sabajete Elezaj  |  Senior Cyber Security Engineer, Solaris SE

Full Abstract and Presentation Materials Available:
