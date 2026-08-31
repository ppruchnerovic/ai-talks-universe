---
id: FbjpwHLaNb4
title: "Personalized Restaurant Recommendations at Scale combining Transformer with Gradient-Boosted Ranking"
slug: personalized-restaurant-recommendations-at-scale-combining
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Marcel Kurovski", "Steffen Klempau"]
channel: null
duration_min: 49
published_at: 2026-08-04T22:20:36Z
video_id: FbjpwHLaNb4
youtube_url: https://www.youtube.com/watch?v=FbjpwHLaNb4
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Personalized Restaurant Recommendations at Scale combining Transformer with Gradient-Boosted Ranking

**Marcel Kurovski, Steffen Klempau**

`PyData` · `PyData` · `2026` · `49 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=FbjpwHLaNb4) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Marcel Kurovski and Steffen Klempau reveal how Wolt scaled personalized restaurant recommendations across 30 countries by combining Transformers with Gradient-Boosted Ranking for a high-impact, low-latency production system.

Speakers:
Marcel Kurovski, Steffen Klempau

Description:
The Universal Venue Ranker (UVR) addresses the challenge of personalized restaurant and retail recommendations at scale, specifically targeting the balance between recurring user habits and the discovery of new venues. To solve this, a two-stage hybrid architecture combines a Transformer-based predictor with a CatBoost gradient-boosted ranking model.

The first stage utilizes an encoder-only Transformer to process time-sorted sequences of user purchases, incorporating embeddings for venues, timestamps, and location hexagons. This model performs next-purchase prediction via multi-class classification, generating a user-net score for each available venue. In the second stage, this score is fed as a primary feature into a CatBoost ranker, which incorporates additional contextual data—such as venue popularity, cuisine affinity, and delivery time—to perform pairwise ranking using a Bayesian Personalized Ranking (BPR) loss function.

Key takeaways include a significant increase in Mean Reciprocal Rank (MRR) for new venue purchases and a global uplift in conversion rates. The system optimizes for exploration by adjusting sample weights for new purchases and tuning negative sampling ratios to prevent model overconfidence. This approach successfully consolidated four legacy models into a single production pipeline deployed across 30 countries.

⭐️ About PyCon DE:
PyCon DE is the leading conference on open-source Python applications in AI and data science. It brings together industry professionals, researchers, AI and data science practitioners, and software engineering communities, providing a unique platform for collaboration, knowledge sharing, and innovation.

The PyCon DE & PyData 2026 conference delivered an exceptional experience, fostering stronger connections within the Python community while showcasing the latest advancements in artificial intelligence and data science. Attendees enjoyed a diverse and engaging program of talks, workshops, and networking opportunities, further establishing the conference as a premier event for Python, AI, and data science enthusiasts across Germany.

PyCon DE 2027 will take place in Heidelberg from 19 to 23 April 2027.

•  Newsletter: https://2027.pycon.de/newsletter/
•  LinkedIn: https://www.linkedin.com/company/pyconde
•  X: https://www.x.com/pyconde

Links:
• Conference website: http://pycon.de
• Other sessions: https://2026.pycon.de/talks/

The conference was organized by
• Python Softwareverband e.V.: http://pysv.org
• Pioneers Hub gemeinnützige GmbH: http://pioneershub.org
in collaboration with NumFOCUS Inc.: http://numfocus.org

If you enjoyed this session, please like, and subscribe to our channel for more insightful talks and discussions.
Share this video with your network to spread the knowledge!

Hashtags:

Acknowledgements:
Special thanks to all the volunteers and sponsors who made this event possible.

About:
Python Softwareverband e.V.:
PySV is a non-profit that promotes the use and development of Python in Germany through events, education, and advocacy, fostering an open Python community.

Pioneers Hub gemeinnützige GmbH:
is a non-profit fostering innovation in AI and tech by connecting experts and promoting knowledge exchange through events and collaborative initiatives.

NumFOCUS Inc.
supports open-source scientific computing by providing financial and logistical support to key projects like NumPy and Jupyter, promoting sustainable development and collaboration.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.
