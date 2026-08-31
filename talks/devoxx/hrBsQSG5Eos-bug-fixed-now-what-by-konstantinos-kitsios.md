---
id: hrBsQSG5Eos
title: "Bug fixed, now what? by Konstantinos Kitsios"
slug: bug-fixed-now-what-by-konstantinos-kitsios
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2026
speakers: []
channel: null
duration_min: 20
published_at: 2026-02-27T13:52:49Z
video_id: hrBsQSG5Eos
youtube_url: https://www.youtube.com/watch?v=hrBsQSG5Eos
tags: []
transcript: false
---

# Bug fixed, now what? by Konstantinos Kitsios

**Speaker not identified**

`Devoxx` · `Devoxx` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=hrBsQSG5Eos) · [Conference site](https://devoxx.com/)

## Description

When a bug is fixed, how can we make sure it will not be re-introduced in the future?

Of course, through a proper regression test, i.e., a test that fails in the presence of the bug and passes in its absence.

However, regression tests are frequently ommited by the developers, who tend to submit the patch alone.

How can AI automation help developers it this scenario?

We explore this question in depth by introducing our open-source GitHub bot that is triggered when a pull request is opened, and proposes a test that is guaranteed to fail in the presence of the bug and pass in its absence.

We use a combination of LLMs and traditional, search-based testing techniques to achieve this goal.

The bot is currently deployed in three Python repositories (Javascript and Rust will be soon also supported) of the Mozilla corporation, where it has already helped developers with their regression tests. We share interesting early insights and feedback from this deployment and invite more open-source developers to adopt the bot and provide constructive feedback!
