---
id: LdrqX5Nhe94
title: "Immoral Fiber: Unlocking & Discovering New Offensive Capabilities of Fibers"
slug: immoral-fiber-unlocking-discovering-new-offensive
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2024
speakers: []
channel: "Black Hat"
duration_min: 29
published_at: 2024-09-03T17:23:21Z
video_id: LdrqX5Nhe94
youtube_url: https://www.youtube.com/watch?v=LdrqX5Nhe94
tags: []
transcript: false
---

# Immoral Fiber: Unlocking & Discovering New Offensive Capabilities of Fibers

**Speaker not identified**

`Black Hat` · `Black Hat` · `2024` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=LdrqX5Nhe94) · [Conference site](https://www.blackhat.com/)

## Description

Fibers are an optional component of the Windows Operating system, largely undocumented and existing exclusively in Usermode. Compared with Threads they have been given a limited spotlight from a security perspective. They are non-trivial to extract from memory and the current API doesn't offer remote enumeration capabilities. From a defender's perspective this could sound like a nightmare, however red teams and malware developers may feel the opposite.

This talk details the offensive capabilities of Windows fibers and how to apply them. It discusses current open-source techniques such as shellcode injection through current fibers, inserting malicious callbacks, callstack spoofing and misdirection via dummy Fibers.

It also provides an overview of the main components of a Fiber. How each component can be leveraged from an attacker's perspective, their representation in memory and how to use them to evade EDRs and AVs when executing malicious code.

This talk also debuts the release of a new novel form of remote process injection using Fibers. This is demonstrated in the POC tool 'PoisonFiber'. At the time of writing this is the only implementation that unlocks the ability to inject malicious code into dormant Fibers inside remote processes. Either by injecting directly into the context structure, replacing Fiber objects entirely, or overwriting existing Fiber local storage callbacks with malicious code.

Finally, this talk will reveal another new POC technique 'PhantomThread'. This is a more OpSec aware method of leveraging the stack switching effect of Windows Fibers to achieve callstack spoofing. It evades existing forms of detection telemetry collected by EDR agents and AV products by masquerading as a regular Thread. In addition, it temporarily patches indicators which can be used as forensic artifacts inside the TEB, TIB and the Fiber object itself, reverting these changes when necessary.

By:
Daniel Jary  |  Security Researcher

Full Abstract:
