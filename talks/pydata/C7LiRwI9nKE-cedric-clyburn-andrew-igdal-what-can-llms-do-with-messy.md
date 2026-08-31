---
id: C7LiRwI9nKE
title: "Cedric Clyburn, Andrew Igdal - What Can LLMs Do with Messy Data? | Pydata London 26"
slug: cedric-clyburn-andrew-igdal-what-can-llms-do-with-messy
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Cedric Clyburn"]
channel: null
duration_min: 30
published_at: 2026-06-15T15:50:55Z
video_id: C7LiRwI9nKE
youtube_url: https://www.youtube.com/watch?v=C7LiRwI9nKE
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Cedric Clyburn, Andrew Igdal - What Can LLMs Do with Messy Data? | Pydata London 26

**Cedric Clyburn**

`PyData` · `PyData` · `2026` · `30 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=C7LiRwI9nKE) · [Conference site](https://pydata.org/)

## Description

Cedric Clyburn, Andrew Igdal - What Can LLMs Do with Messy Residential Electrification Data?

Residential energy models like NREL’s ResStock generate the kind of data most humans run from: thousands of buildings, dozens of columns, and at least 8,760 rows per column. Great for research, but difficult for anyone who just wants to ask, “What happens to electricity demand in Texas if homes used solar water heating?” or “How do HVAC upgrades change my annual cooling costs in North Carolina?”

Join us for this session as a University of Texas energy researcher and a Red Hat engineer team up to see what large language models can realistically do with this kind of messy, domain-heavy data using Python. We’ll show how we sample, reshape, and describe large datasets so LLMs can help generate and refine pandas/DuckDB queries, explain upgrade scenarios in plain English, and guide non-experts through “what if” electrification questions. This and more, all while being honest about where the models break down and why humans still need to do the science.

ResStock is an incredible tool for residential energy research, but quite tricky for anyone who isn’t deep in the weeds. It produces huge, domain-heavy datasets: thousands of simulated homes, dozens of variables, and hourly time series for a full year. Great if you’re writing a paper, overwhelming if you want to understand how electrification upgrades change bills or demand.

This talk asks a practical question: What can large language models actually do with ResStock-style data, using a Python workflow? Can LLMs help normal people make sense of the benefits of electrification upgrades without pretending the model is “doing the science” for us?

We ground everything in two real ResStock runs: (1) solar thermal water heater upgrades in Texas, and (2) HVAC upgrades across the Southeastern U.S. Both are large and messy, so we can’t just upload the parquet files. Instead, we:

Use Python (pandas/DuckDB) to sample and aggregate the data into representative slices that fit within context limits.
Build a clear schema description (“data card”) so the LLM understands variables, units, and constraints.
Ask the LLM to help where it shines: generating and refining pandas/DuckDB queries from natural-language questions, and explaining upgrade impacts in plain English.
Andrew (UT Austin) brings the ResStock data, research questions, and domain constraints; Cedric (Red Hat) brings the open source + LLM integration side. Attendees will leave with a realistic pattern for using LLMs as helpers, not replacements, when working with large, messy scientific or policy datasets in Python.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
