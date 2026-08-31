---
id: Z8VVDCei91w
title: "Ophelie Bleu - When Your Dataset Has Blind Spots LLM-Based Data Augmentation | Pydata London 26"
slug: ophelie-bleu-when-your-dataset-has-blind-spots-llm-based
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Ophelie Bleu"]
channel: "PyData"
duration_min: 25
published_at: 2026-06-15T15:54:08Z
video_id: Z8VVDCei91w
youtube_url: https://www.youtube.com/watch?v=Z8VVDCei91w
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Ophelie Bleu - When Your Dataset Has Blind Spots LLM-Based Data Augmentation | Pydata London 26

**Ophelie Bleu**

`PyData` · `PyData` · `2026` · `25 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=Z8VVDCei91w) · [Conference site](https://pydata.org/)

## Description

Learn practical techniques for using LLMs to solve the data scarcity problem that plagues real-world ML projects. This talk demonstrates three production-ready approaches: synthetic generation, LoRA fine-tuning, and LLM-powered annotation to augment training datasets when you have abundant data for common cases but almost nothing for edge cases or emerging categories. Using a food review classification scenario, you'll see how to generate high-quality training data, when each technique works best, and critically, how to validate synthetic data to avoid amplifying errors. Perfect for practitioners facing the "we have 10k examples of X but zero for Y" problem.

Target Audience: Data scientists and ML engineers working on classification, NLP, or content moderation tasks who struggle with imbalanced or incomplete training datasets.

Takeaway: A decision framework for choosing between synthetic generation, fine-tuning, and LLM annotation, plus validation strategies to ensure data quality before retraining models.

Objective
Many machine learning teams struggle not because of model limitations, but because their datasets fail to cover rare classes, niche domains, or emerging user behavior. Traditional data augmentation techniques offer limited help for text, often producing surface-level variations without meaningful semantic diversity. This talk presents a practical framework for using large language models to augment NLP datasets.

Outline
The Data Bottleneck: Why models trained on "standard" food language fail to generalize to "Molecular Gastronomy" or niche culinary terms.
Three Complementary Techniques:
Synthetic Generation: Creating fully labeled examples for missing classes.
LoRA Adapters: Fine-tuning LLMs to control style and label consistency (e.g., matching a "Professional Critic" tone).
LLM Annotation: Labeling large volumes of messy, real-world text from social media or external scrapes.
Validation Strategies: Addressing error amplification and bias through human agreement checks, self-consistency, and "LLM-as-a-judge" approaches.
Measuring Impact: Evaluating downstream model performance via rare-class recall, calibration, and error distribution.
Central Thesis and Takeaways
The session provides a decision framework for choosing between generation, fine-tuning, and annotation based on data availability and the need for style or tone. Attendees will walk away with strategies to ensure synthetic data quality before retraining their models.

Background Knowledge Expected
Basic knowledge of Python and familiarity with machine learning workflows (training, labelling, and evaluation) is recommended.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
