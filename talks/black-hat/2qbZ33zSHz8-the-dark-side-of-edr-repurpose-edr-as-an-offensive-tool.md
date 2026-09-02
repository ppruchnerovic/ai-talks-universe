---
id: 2qbZ33zSHz8
title: "The Dark Side of EDR: Repurpose EDR as an Offensive Tool"
slug: the-dark-side-of-edr-repurpose-edr-as-an-offensive-tool
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2024
speakers: []
channel: "Black Hat"
duration_min: 43
published_at: 2024-09-09T16:49:19Z
video_id: 2qbZ33zSHz8
url: https://www.youtube.com/watch?v=2qbZ33zSHz8
youtube_url: https://www.youtube.com/watch?v=2qbZ33zSHz8
tags: []
transcript: false
---

# The Dark Side of EDR: Repurpose EDR as an Offensive Tool

**Speaker not identified**

`Black Hat` · `Black Hat` · `2024` · `43 min`

[Watch the recording](https://www.youtube.com/watch?v=2qbZ33zSHz8) · [Conference site](https://www.blackhat.com/)

## Description

As EDR solutions have become an integral part of the cybersecurity landscape, operating on millions of endpoints and servers, their role in advanced threat detection is undisputed. However, with great power comes great responsibility, an incorrect deployment can lead to critical vulnerabilities, potentially exploited by malicious actors.

This research explores a distinctive approach, differentiating itself from prior studies and real-world attacks that aimed at bypassing, disabling, or removing EDR systems, all of which tend to be conspicuous and impractical for Advanced Persistent Threat (APT) campaigns.

Our methodology involves control over the EDR, enabling the execution of code within its context. This capability allows us to operate secretly and persistently, significantly enhancing organizational security postures.

Focusing on Palo Alto Networks Cortex XDR, we demonstrate not only the manipulation of the system to bypass security measures but also the transformation of the EDR into a stealthy and uniquely persistent form of malware. Our research goes beyond the limitations of existing attacks, which are often too conspicuous for APT campaigns.

We successfully bypassed significant security features implemented by the Cortex XDR, including machine learning detection modules, evasion of behavioral modules, real-time prevention rules, and overcoming filter-driver protection against file modification.

The depth of our exploration encompasses exfiltration of sensitive user credentials, establishment of persistence on the targeted system, encryption of the entire machine (FUD), complete LSASS memory dumping, concealing malicious activity notifications, bypassing the XDR administrator password, and exploiting XDR comprehensively for malicious endeavors.
Notably, our persistence is so robust that it necessitates physical access to infected machines, as the XDR cannot be removed remotely from the management interface.

Join us as we delve into the implications of this novel attack vector, shedding light on the intricate relationship between attackers and XDR, and addressing a significant aspect of EDR security that has hitherto remained unexplored.

By:
Shmuel Cohen  |  Security Researcher, SafeBreach

Full Abstract:
