---
id: utjtAxagbr8
title: "One Flip is All It Takes: Identifying Syscall-Guard Variables for Data-Only Attacks"
slug: one-flip-is-all-it-takes-identifying-syscall-guard
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2024
speakers: []
channel: "Black Hat"
duration_min: 29
published_at: 2024-09-13T16:48:36Z
video_id: utjtAxagbr8
url: https://www.youtube.com/watch?v=utjtAxagbr8
youtube_url: https://www.youtube.com/watch?v=utjtAxagbr8
tags: []
transcript: false
---

# One Flip is All It Takes: Identifying Syscall-Guard Variables for Data-Only Attacks

**Speaker not identified**

`Black Hat` · `Black Hat` · `2024` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=utjtAxagbr8) · [Conference site](https://www.blackhat.com/)

## Description

As control-flow protection techniques are widely deployed, it is difficult for attackers to modify control data, like function pointers, to hijack program control flow. Instead, data-only attacks corrupt security-related non-control data (critical data), and can bypass all control-flow protections to revive severe attacks. Previous works have explored various methods to help construct or prevent data-only attacks. However, no solution can automatically detect program-specific critical data.

In this presentation, we identify an important category of critical data, syscall-guard variables, and propose a set of solutions to automatically detect such variables in a scalable manner. Our insight is that most data-only attacks rely on security-related syscalls (e.g., execve, unlink, chmod) to achieve ultimate goals and these syscalls are often guarded by security checks in the form of conditional branches. We refer to variables in such security checks as syscall-guard variables. We propose "branch force", which intentionally flips every conditional branch during the execution and checks whether new security-related syscalls are invoked. If so, we conduct data-flow analysis to estimate the feasibility to flip such branches through common memory errors. We build a tool, VIPER, to implement our ideas. VIPER successfully detects 34 previously unknown syscall-guard variables from 13 programs. We also build four new data-only attacks on sqlite and v8, which execute arbitrary commands or delete arbitrary files. VIPER completes its analysis within five minutes for most programs, showing its practicality for spotting syscall-guard variables.

By:
Zhechang Zhang  |  Ph.D. Student, Pennsylvania state university
Hengkai Ye  |  Ph.D. Student, Pennsylvania state university
Hong Hu  |  Assistant Professor, Pennsylvania state university

Full Abstract & Presentation Materials:
