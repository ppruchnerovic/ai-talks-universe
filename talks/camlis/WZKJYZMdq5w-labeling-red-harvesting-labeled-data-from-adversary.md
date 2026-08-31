---
id: WZKJYZMdq5w
title: "Labeling Red: Harvesting Labeled Data from Adversary Simulations"
slug: labeling-red-harvesting-labeled-data-from-adversary
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: null
duration_min: 33
published_at: 2018-11-16T17:30:00Z
video_id: WZKJYZMdq5w
youtube_url: https://www.youtube.com/watch?v=WZKJYZMdq5w
tags: ["camlis", "camlis2018"]
transcript: false
---

# Labeling Red: Harvesting Labeled Data from Adversary Simulations

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `33 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=WZKJYZMdq5w) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Brian Genz, Northwestern Mutual
Labeling Red: Harvesting Labeled Data from Adversary Simulations (slides: https://www.camlis.org/brian-genz/)

Attackers have a seemingly endless arsenal of tools and techniques at their disposal, while defenders must continuously strive to improve detection capabilities across the full spectrum of possible attack vectors. The MITRE ATT&CK Framework provides a useful collection of attacker tactics and techniques that enables a threat-focused approach to detection.

This talk will highlight methodologies and key lessons learned from an internal adversary simulation at a Fortune 100 company that evolved into a series of data science experiments designed to improve threat detection.

In 2017, we performed basic Exploratory Data Analysis (EDA) while working to improve detection engineering activities around post-exploitation attack techniques during adversary simulation exercises. We paused to ask the question, “Isn’t this labeled data we’re generating? The red team just performed this attack, and we can positively identify the observations that resulted from that attack technique.”

Could we move beyond clustering, we wondered, and into the realm of supervised learning? We had to consider whether we were introducing any biases based on the methodology used in selecting and executing the attack techniques. We were also curious as to whether the inherent attacker tradecraft principle of stealth might translate into imbalanced classes in the data, and to what extent.

We defined what we wanted to model: “Post-compromise attacker activity.” We focused on an initial technique: “DNS Exfiltration.” We defined the goal as, “Incorporate labeled attack data in training a model to classify DNS requests as ‘malicious’ or ‘benign.’

What started as a few questions and resulting brainstorming sessions eventually grew into a security data science practice supporting detection engineering, Digital Forensics and Incident Response (DFIR), Threat Hunting, and Threat Intelligence at the Fortune 100 company. This talk will step through the key aspects of the problem-solving approach used, with an emphasis on model selection and feature engineering.
