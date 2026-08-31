---
id: KtbeMz2UHN0
title: "How to Make Hugging Face to Hug Worms: Discovering and Exploiting Unsafe Pickle.loads"
slug: how-to-make-hugging-face-to-hug-worms-discovering-and
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2024
speakers: []
channel: "Black Hat"
duration_min: 41
published_at: 2024-09-03T17:23:12Z
video_id: KtbeMz2UHN0
youtube_url: https://www.youtube.com/watch?v=KtbeMz2UHN0
tags: []
transcript: false
---

# How to Make Hugging Face to Hug Worms: Discovering and Exploiting Unsafe Pickle.loads

**Speaker not identified**

`Black Hat` · `Black Hat` · `2024` · `41 min`

[Watch the recording](https://www.youtube.com/watch?v=KtbeMz2UHN0) · [Conference site](https://www.blackhat.com/)

## Description

How to Make Hugging Face to Hug Worms: Discovering and Exploiting Unsafe Pickle.loads over Pre-Trained Large Model Hubs

Hugging Face (HF) has emerged as a popular open platform for maintaining and sharing pre-trained machine learning (ML) models. It fully understands the pickle model deserialization threats originally introduced by Pytorch and accordingly implements pickle scanning for mitigation. In October 2022, Pytorch patched such a threat by white-listing weights-only modules. But in contrast, the war seems not to have reached its end for Hugging Face, which integrates a family of diverse ML libraries for model training, sharing, and even performance tuning. These libraries accidentally use the raw pickle.loads (rather than the torch.load) to parse the pickle files, hence still vulnerable to deserialization attacks.

In this talk, we present our findings on the unsafe use of pickle.loads across the integrated ML libraries in Hugging Face. We disclose kinds of novel tricks to bypass pickle scanning and enable Hugging Face to host malicious pickle files without triggering visible alerts. To show the further impacts, we demonstrate how easily it is to exploit some of these unsafe loads to execute arbitrary commands remotely in the victim's local machines (reversed RCE) despite such a victim following HF's official guidelines to fetch and load models from remote HF repositories (e.g., calling function from_pretrained for huggingface/transformer or running commands load_from_hub and enjoy for rl_zoo3, etc). In our demos, we also exhibit how to make our RCE wormable when the victim is a logged-in Hugging Face user with a "write" permission, showing the possibility of abusing Hugging Face as an evil weapon for delivering and propagating pickle malware over ML communities.

By:
Peng Zhou  |  Associate Professor, Shanghai University

Full Abstract & Presentation Materials:
