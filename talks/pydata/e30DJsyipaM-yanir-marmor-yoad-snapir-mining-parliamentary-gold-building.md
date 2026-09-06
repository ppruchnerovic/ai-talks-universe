---
id: e30DJsyipaM
title: "Yanir Marmor, Yoad Snapir:Mining Parliamentary Gold - Building Hebrew ASR (HE)| PyData Tel Aviv 2025"
slug: yanir-marmor-yoad-snapir-mining-parliamentary-gold-building
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2025
speakers: ["Yanir Marmor"]
channel: "PyData"
duration_min: 13
published_at: 2025-12-04T11:14:29Z
video_id: e30DJsyipaM
url: https://www.youtube.com/watch?v=e30DJsyipaM
youtube_url: https://www.youtube.com/watch?v=e30DJsyipaM
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Multimodal, vision, speech & robotics", "Science, healthcare & applied ML", "Training, fine-tuning & model building"]
transcript: false
---

# Yanir Marmor, Yoad Snapir:Mining Parliamentary Gold - Building Hebrew ASR (HE)| PyData Tel Aviv 2025

**Yanir Marmor**

`PyData` · `PyData` · `2025` · `13 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=e30DJsyipaM) · [Conference site](https://pydata.org/)

## Description

Parliamentary recordings are a hidden goldmine for Hebrew ASR, but they're also uniquely challenging. The Knesset's decade-plus of streamed debates contain a variety of technical obstacles, including sessions lasting 50+ hours, protocols that preserve the speaker's "spirit" rather than exact words, timestamp artifacts, and constant background noise from audience interruptions.

We’ll show how a fully reproducible Python pipeline - built with stable_ts + faster-whisper + CTranslate2, with only light ffmpeg remuxing - force-aligns every sentence (despite heckling, in-between shouts, diglossia, and wobbly timestamps), normalizes the text, then packages the whole lot as a license-clean, Hugging Face-ready dataset.

With the dataset in hand, we fine-tune both Whisper-base and Whisper-Turbo, achieving 10% WER reduction compared to former models. The side-by-side error taxonomy shows why smart data engineering can beat brute-force pre-training, especially for low-resource languages.

Attendees walk away with (1) a concrete recipe for turning messy public audio into research-grade training data; (2) Hebrew-specific alignment and text-cleaning tricks that generalise to more languages; and (3) fresh evidence that high-quality local data can outperform generic pre-training, empowering communities to build world-class models on their own terms.

Speaker Bio:
Yanir Marmor - M.Sc. CS & Math student at Weizmann Institute of Science; ivrit.ai co-founder (non-profit)
Yoad Snapir - AI & Tech Consultant, ivrit.ai

Follow PyData Tel Aviv on:

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.
