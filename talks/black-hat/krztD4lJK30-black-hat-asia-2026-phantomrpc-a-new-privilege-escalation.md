---
id: krztD4lJK30
title: "Black Hat Asia 2026 | PhantomRPC: A New Privilege Escalation Flaw in Windows RPC"
slug: black-hat-asia-2026-phantomrpc-a-new-privilege-escalation
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2026
speakers: []
channel: null
duration_min: 34
published_at: 2026-08-22T19:30:01Z
video_id: krztD4lJK30
youtube_url: https://www.youtube.com/watch?v=krztD4lJK30
tags: []
transcript: false
---

# Black Hat Asia 2026 | PhantomRPC: A New Privilege Escalation Flaw in Windows RPC

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `34 min`

[Watch the recording](https://www.youtube.com/watch?v=krztD4lJK30) · [Conference site](https://www.blackhat.com/)

## Description

Windows Inter-process Communication (IPC) is one of the most complex technologies within the Windows operating system. At the core of this ecosystem lies the Remote Procedure Call (RPC) mechanism, which can function as a standalone communication channel or as the underlying transport layer for more advanced inter-process communication technologies. Due to its complexity and broad usage, RPC has historically been a rich source of security issues. Over the years, researchers have identified numerous vulnerabilities in services that rely on RPC, ranging from local privilege escalations to full remote code execution.

In this Briefing, I will present a new vulnerability within the RPC architecture that enables a new local privilege escalation technique in all windows versions. This technique allows processes with impersonation privileges to elevate their permissions to SYSTEM level. Although this vulnerability is different from the known "Potato" exploit family, Microsoft has not issued a patch despite proper disclosure.

I will introduce five distinct exploitation paths that demonstrate how privileges can be escalated from various local or network service contexts to SYSTEM. Some approaches involve coercion, others require user interaction, and some leverage background services. Because this is an architectural flaw, the number of possible attack vectors is unlimited, any new process or service that depends on RPC may introduce an additional escalation path. For this reason, we will also describe a methodology for identifying such opportunities and constructing custom exploits.

This research is intended for vulnerability researchers, exploit developers, red team operators, and defenders seeking to understand, detect, and mitigate these classes of attacks.

Haidar Kabibo  |  Application Security Specialist, Kaspersky
