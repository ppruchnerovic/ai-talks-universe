---
id: DkzXowYO52g
title: "USENIX Security '25- Red Bleed: A Pragmatic Near-Infrared Presentation Attack on Facial Biometric..."
slug: usenix-security-25-red-bleed-a-pragmatic-near-infrared
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX Security"
year: 2025
speakers: []
channel: null
duration_min: 14
published_at: 2025-10-30T20:03:02Z
video_id: DkzXowYO52g
youtube_url: https://www.youtube.com/watch?v=DkzXowYO52g
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25- Red Bleed: A Pragmatic Near-Infrared Presentation Attack on Facial Biometric...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2025` · `14 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=DkzXowYO52g) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '25 - Red Bleed: A Pragmatic Near-Infrared Presentation Attack on Facial Biometric Authentication Systems

Bowen Hu, Kuo Wang, and Chip Hong Chang, Nanyang Technological University

Facial recognition is the most prevalent biometric modality in commercial verification and identification systems (e.g. Windows Hello and Apple FaceID), which typically operate under near-infrared (NIR) illumination. Such systems are generally considered secure on the premise that no commercial screen display can readily enable a NIR-based video presentation attack. However, this work demonstrates a critical vulnerability of NIR biometric authentication systems by a presentation attack, named Red Bleed, mounted on a widely used commercial-off-the-shelf (COTS) enterprise-grade face authentication system through a custom-built liquid crystal display (LCD) that costs less than 400 USD.

Due to the scarcity of NIR video samples, it is more feasible to sneak RGB images in the visible (VIS) spectrum through, for instance, covert secret photography, photos posted on social media or screen captures during video conferencing. Besides using live captured NIR video of the target subject's face, we also propose a novel identity-preserved NIR face generative framework that combines a Variational Autoencoder (VAE) to convert VIS images into the NIR domain for this attack. In conjunction with an advanced face swapping technique, an RGB video can be transformed into a video with NIR face, enabling a more sneaky and pragmatic 2D presentation attack on NIR face biometric authentication demonstrated on a commercially available Windows Hello face authentication module.
The hardware design and source code supporting our findings will be made publicly available at https://github.com following paper acceptance and the corresponding Common Vulnerabilities and Exposures (CVE) release. This vulnerability has been reported to Microsoft and the vendors of the three evaluated COTS Windows Hello face recognition modules. The reported behavior has been confirmed by the Microsoft Security Response Center (MSRC), and a CVE is scheduled for public disclosure in June 2025.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
