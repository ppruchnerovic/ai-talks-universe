---
id: g3Gv0mjlQEU
title: "Detecting hand-crafted social engineering emails with a bleeding-edge neural language model"
slug: detecting-hand-crafted-social-engineering-emails-with-a
conference: defcon-ai-village
conference_name: "DEF CON AI Village"
category: "AI security"
edition: "AI Village"
year: 2020
speakers: []
channel: null
duration_min: 49
published_at: 2020-08-09T21:07:19Z
video_id: g3Gv0mjlQEU
youtube_url: https://www.youtube.com/watch?v=g3Gv0mjlQEU
tags: []
transcript: false
---

# Detecting hand-crafted social engineering emails with a bleeding-edge neural language model

**Speaker not identified**

`DEF CON AI Village` · `AI Village` · `2020` · `49 min`

[Watch the recording](https://www.youtube.com/watch?v=g3Gv0mjlQEU) · [Conference site](https://aivillage.org/)

## Description

Authors: Younghoo Lee and Joshua Saxe

Social engineering attacks leveraging hand-crafted emails are on the rise, and are causing at least $12.5 billion dollars in damage per year. Custom authored and often incorporating background research on their targets, they pose a significant challenge for traditional signature and ML detection technologies, as an individual targeted email may not share word sequences or word choices with previously seen attacks, and may appear different in only subtle ways from benign messages.
To attack this problem, we've built a neural network model that's been trained on billions of words of benign text so as to "learn" a sophisticated representation of the syntax and semantics of natural language.  This allows the network to pick up on the subtleties of email topic, tone, and style.  We then compress and fine-tune the network to detect phishing attacks in a "generic" way, based on these abstract semantics, such that our detector accurately detects new, targeted phishing attacks, achieving an 85% detection rate on custom-authored attacks at a 0.1% false positive rate.
In our presentation, we'll walk through the research path we followed to create our detection system, including the baseline methods we tried, the procedure by which we collect millions of training examples, and the architectural decisions we made in creating our system. Then we'll walk through actual emails we detected.  Finally, we'll demonstrate that our detector is resilient to randomly introduced changes in word choice, word ordering, message length, and other permutations.  We believe our work demonstrates that recent breakthroughs in neural language modeling will have a dramatic effect on our community's ability to protect users from natural-language based social engineering attacks.
