---
id: 5fs9ntKOYW0
title: "Bytecode Jiu-Jitsu: Choking Interpreters to Force Execution of Malicious Bytecode"
slug: bytecode-jiu-jitsu-choking-interpreters-to-force-execution
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 39
published_at: 2025-01-28T18:32:40Z
video_id: 5fs9ntKOYW0
youtube_url: https://www.youtube.com/watch?v=5fs9ntKOYW0
tags: []
transcript: false
---

# Bytecode Jiu-Jitsu: Choking Interpreters to Force Execution of Malicious Bytecode

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `39 min`

[Watch the recording](https://www.youtube.com/watch?v=5fs9ntKOYW0) · [Conference site](https://www.blackhat.com/)

## Description

Code injection is a category of techniques that hides the behavior of malware by injecting malicious code into the memory of a legitimate process. However, most existing techniques rely on specific system APIs that are considered suspicious and often monitored by security products, which makes them easy to detect.

We introduce a novel code injection attack, Bytecode Jiu-Jitsu, that injects malicious bytecode into an interpreter. It works by dynamically replacing existing benign bytecode in the memory of an interpreter process and forcing the process to execute the new bytecode. This attack is covert because it does not need to call suspicious APIs for thread creation, executable memory allocation, or instruction pointer modification. The main challenges lie in reverse-engineering the locations and structures of bytecode and symbol tables (data structures that manage data referenced by bytecode) in memory, which depends on the specific implementation of the interpreter. This reverse engineering requires a prohibitive human effort, especially if the source code is unavailable.

Therefore, we propose an almost fully automatic technique for analyzing an interpreter binary to reveal the locations and structures and injecting arbitrary bytecode based on the analysis. The analysis allows our injection attack to be applied to even proprietary interpreters with minimal human effort.

In this talk, we first revisit different types of code injection techniques. Next, we explain the interpreter analysis technique and the Bytecode Jiu-Jitsu technique while showing its advantages so that the audience can obtain a blue belt. We then demonstrate that our attack can:
(1) apply to diverse real-world interpreters,
(2) evade detection by more than 80% of antivirus products on VirusTotal and state-of-the-art memory forensics tools,
(3) disturb behavioral analysis with sandboxes and EDRs as well as manual analysis by experienced malware analysts.

Finally, we will release our tool that Red Teamers and security researchers can use for research and evaluation.

By:
Toshinori Usui  |  Research Scientist, NTT Security Holdings Corporation
Yuto Otsuki  |  Senior Researcher, NTT Security Holdings Corporation
Ryo Kubota  |  Researcher, NTT Security Holdings Corporation
Yuhei Kawakoya  |  Distinguished Researcher, NTT Security Holdings Corporation
Makoto Iwamura  |  Distinguished Researcher, NTT Security Holdings Corporation
Kanta Matsuura  |  Professor, Institute of Industrial Science, The University of Tokyo

Full Abstract and Presentation Materials:
