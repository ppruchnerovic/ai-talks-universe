---
id: cj1YVlJu7C0
title: "Tom Koopen - Finding trash in waste - PyData Eindhoven 2025"
slug: tom-koopen-finding-trash-in-waste-pydata-eindhoven-2025
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2025
speakers: ["Tom Koopen"]
channel: "PyData"
duration_min: 31
published_at: 2025-12-19T12:01:19Z
video_id: cj1YVlJu7C0
url: https://www.youtube.com/watch?v=cj1YVlJu7C0
youtube_url: https://www.youtube.com/watch?v=cj1YVlJu7C0
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science"]
transcript: false
---

# Tom Koopen - Finding trash in waste - PyData Eindhoven 2025

**Tom Koopen**

`PyData` · `PyData` · `2025` · `31 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=cj1YVlJu7C0) · [Conference site](https://pydata.org/)

## Description

Tom Koopen - Finding trash in waste - PyData Eindhoven 2025

At waste transfer stations for source separated packaging waste incoming waste trucks are visually inspected on objects that could disturb the sorting and recycling of the truck load. This is a manual procedure and in case the number of disturbing items is too high, the part of the truck load needs to be removed. Currently, 8.5 % of the truck loads is rejected. This leads to loss of valuable plastics for recycling. We have investigated the automation of this inspection using cameras and vision foundation models. Inhouse, we developed a data pipeline where waste items are first detected, then segmented and eventually classified whether they belong to this waste stream using anomaly detection. The accepted material continues to a plastic recovery facility. This approach has led to a proof-of-principle with the potential to be implemented as a pilot-scale at a waste transfer station. The project is part of the research program ‘MultiPurpose Plastic Sorting’ subsidised by TKI Energy & Industry.

After waste collection of lightweight packaging waste, in the Netherlands known as PMD (plastic-, metaal- en drankkartons), the incoming material is visually inspected by an operator to extract contaminants that disturb the sorting and recycling. Typical contaminants are non-packaging material and large rigids and foils.

At the applied research institute NTCP, we investigated how to automate the detection process in order to have an objective method to inspect a PMD waste stream. This improves consistency and thereby quality and reduces required time needed for a thorough assessment. We decided to use cameras in a top view of the pile of items, as the inspection is performed. For every item, we first need to locate it in the image and segment the pixels of it. We built a data pipeline using vision foundation models.

To determine whether an item is considered a contaminant or PMD packaging, we found that the class of contaminants had a too broad variety to build a classification network. Therefore, we chose to explore the feasibility of anomaly detection models. Several dedicated anomaly detection models were trained. Finally, we learned that using a combination of foundation models for both visual as well textual features, resulted in a suitable distribution to distinguish contaminants from PMD packaging.

With a prototype set-up, we have showcased a proof-of-principle of a well working and promising automatic detection system on actual waste, given the variety in both PMD and contaminants. images, given the variety in both valid waste and unwanted items.
www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
