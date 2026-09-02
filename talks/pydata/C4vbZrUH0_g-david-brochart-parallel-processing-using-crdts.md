---
id: C4vbZrUH0_g
title: "David Brochart - Parallel processing using CRDTs"
slug: david-brochart-parallel-processing-using-crdts
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2025
speakers: ["David Brochart"]
channel: "PyData"
duration_min: 28
published_at: 2025-11-21T16:25:19Z
video_id: C4vbZrUH0_g
url: https://www.youtube.com/watch?v=C4vbZrUH0_g
youtube_url: https://www.youtube.com/watch?v=C4vbZrUH0_g
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: []
transcript: false
---

# David Brochart - Parallel processing using CRDTs

**David Brochart**

`PyData` · `PyData` · `2025` · `28 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=C4vbZrUH0_g) · [Conference site](https://pydata.org/)

## Description

Beyond embarrassingly parallel processing problems, data must be shared between workers for them to do something useful. This can be done by:
- sharing memory between threads, with the issue of preventing access to shared data to avoid race conditions.
- copying memory to subprocesses, with the challenge of synchronizing data whenever it is mutated.

In Python, using threads is not an option because of the GIL (global interpreter lock), which prevents true parallelism. This might change in the future with the removal of the GIL, but usual problems with multithreading will appear, such as using locks and managing their complexity. Subprocesses don't suffer from the GIL, but usually need to access a database for sharing data, which is often too slow. Algorithms such as HAMT (hash array mapped trie) have been used to efficiently and safely share data stored in immutable data structures, removing the need for locks. In this talk we will show how CRDTs (conflict-free replicated data type) can be used for the same purpose.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
