---
id: Zbo4I0IKhTs
title: "LLMbotomy: Shutting the Trojan Backdoors"
slug: llmbotomy-shutting-the-trojan-backdoors
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 39
published_at: 2025-05-08T16:56:23Z
video_id: Zbo4I0IKhTs
url: https://www.youtube.com/watch?v=Zbo4I0IKhTs
youtube_url: https://www.youtube.com/watch?v=Zbo4I0IKhTs
tags: []
topics: ["Security, safety & red teaming"]
transcript: false
---

# LLMbotomy: Shutting the Trojan Backdoors

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `39 min`

[Watch the recording](https://www.youtube.com/watch?v=Zbo4I0IKhTs) · [Conference site](https://www.blackhat.com/)

## Description

Large Language Models (LLMs) are rapidly expanding their functionalities—such as browser-based internet access, interfacing with code interpreters, and connecting to peripheral devices—positioning them as central processing hubs. This transformation heralds LLMs as the new abstraction layer for operating systems, necessitating robust security frameworks to ensure their integrity. As more vendors release foundational LLMs, the urgency for robust security measures grows.

While existing research primarily focuses on external threats like prompt injection and other input-based attacks, our research addresses embedded threats such as Trojan backdoors—malicious modifications inserted during the training lifecycle and triggered by specific inputs to cause harmful behaviors. This orthogonal strategy complements existing security guardrails by adding an additional layer of defense, enhancing the overall protection framework. The rising concern over these embedded threats, deliberately introduced through malicious intent or inadvertently through data poisoning, underscores the necessity for our focused approach on these newly emerging attack surfaces.

In this talk, we introduce a novel approach to mitigate LLM Trojans. We propose targeted noising of neurons, identifying critical ones through their activation patterns in LLMs. Our findings show that noising these important neurons can effectively neutralize most Trojans in a model. We demonstrate that newly inserted Trojans by us tend to share neurons with existing ones, allowing us to locate, then neutralize both new and pre-existing Trojans without prior knowledge of the Trojans' presence. This technique ensures that the model retains almost its full functionality and performance while effectively blocking Trojan activations.

By:
Tamás Vörös  |  Senior Data Scientist, Sophos

Full Abstract and Presentation Materials:
