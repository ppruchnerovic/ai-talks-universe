---
id: HWMjP7uFA1s
title: "JDD: In-depth Mining of Java Deserialization Gadget Chains"
slug: jdd-in-depth-mining-of-java-deserialization-gadget-chains
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 37
published_at: 2025-09-23T16:33:06Z
video_id: HWMjP7uFA1s
url: https://www.youtube.com/watch?v=HWMjP7uFA1s
youtube_url: https://www.youtube.com/watch?v=HWMjP7uFA1s
tags: []
topics: ["Security, safety & red teaming"]
transcript: false
---

# JDD: In-depth Mining of Java Deserialization Gadget Chains

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `37 min`

[Watch the recording](https://www.youtube.com/watch?v=HWMjP7uFA1s) · [Conference site](https://www.blackhat.com/)

## Description

JDD: In-depth Mining of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction

Java serialization and deserialization facilitate cooperation between different Java systems, enabling convenient data and code exchange. However, a significant vulnerability known as Java Object Injection (JOI) allows remote attackers to inject crafted serialized objects, triggering internal Java methods (gadgets) and resulting in severe consequences such as remote code execution (RCE). Previous works have attempted to detect and chain gadgets for JOI vulnerabilities using static searches and dynamic payload construction via fuzzing. However, these methods face two key challenges: (i) path explosion in static gadget searches and (ii) a lack of fine-grained object relations connected via object fields in dynamic payload construction.
- First, we will introduce a gadget fragment-based summary and bottom-up search approach to address the path explosion challenge.
- Second, we will then demonstrate how to infer the dataflow dependencies between injection objects' fields and use them to guide dynamic fuzzing to generate exploitable objects.

We evaluate JDD upon six popular Java applications (e.g., Apache Dubbo, Sofa-RPC, Solon, etc) in their latest version, which finds 127 zero-day exploitable gadget chains with six Common Vulnerabilities and Exposures (CVE) identifiers assigned (i.e., CVE-2023-35839, CVE-2023-29234, CVE-2023-39131, CVE-2023-48967, CVE-2024-23636, and CVE-2023-41331). Each of these CVEs has a CVSS score of 9.8, indicating an extremely high risk of exploitation and the potential to cause significant security damage. Given the wide range of impacts and potential consequences of these vulnerabilities, the related developers patched all these gadget chains in a prompt and timely manner after we reported our findings.

By:
Bofei Chen  |  Ph.D Candidate, Fudan University
Yinzhi Cao  |  Associate Professor, Johns Hopkins University
Lei Zhang  |  Assistant Professor, Fudan University
Xinyou Huang  |  Master's Student, Fudan University
Yuan Zhang  |  Professor, Fudan University
Min Yang  |  Professor, Fudan University

Full Abstract and Presentation Materials Available:
