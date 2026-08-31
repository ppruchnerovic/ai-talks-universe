---
id: coeonD6Xwxg
title: "Keeping data private in real-time pipelines by Olena Kutsenko"
slug: keeping-data-private-in-real-time-pipelines-by-olena
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2026
speakers: []
channel: null
duration_min: 33
published_at: 2026-03-30T19:00:00Z
video_id: coeonD6Xwxg
youtube_url: https://www.youtube.com/watch?v=coeonD6Xwxg
tags: []
transcript: false
---

# Keeping data private in real-time pipelines by Olena Kutsenko

**Speaker not identified**

`Devoxx` · `Devoxx` · `2026` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=coeonD6Xwxg) · [Conference site](https://devoxx.com/)

## Description

#VoxxedDaysCERN26

We all love real-time data — clicks, payments, rides, messages — but most of it comes with a catch: it contains personal information we’re not supposed to leak, such as names, emails, locations, or even small clues that can identify someone. The challenge: how do we keep streaming data useful and safe at the same time?

In this talk, we’ll explore practical ways to protect privacy in streaming systems using Apache Kafka, Apache Flink, and Apache Iceberg. We’ll cover:
- simple tricks like masking and tokenizing PII;
- why “anonymous” data often isn’t anonymous (the re-identification problem);
- techniques like bucketing, k-anonymity, and adding noise;
- how to balance privacy with data utility (too much hiding makes data useless).

Along the way, we’ll look at real-world stories: from public data leaks to surprising deanonymization attacks, and show live demos of pipelines that anonymize data before it’s written to storage.
If you’ve ever wondered how to build privacy-aware pipelines, this talk will give you practical patterns you can use right away.
