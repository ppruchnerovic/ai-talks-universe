---
id: 8GCnHJDoXRk
title: "What Breaks When Automatic Speech Recognition Systems Go Multilingual [PyCon DE & PyData 2026]"
slug: what-breaks-when-automatic-speech-recognition-systems-go
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Rashmi Nagpal"]
channel: null
duration_min: 44
published_at: 2026-08-04T22:21:13Z
video_id: 8GCnHJDoXRk
youtube_url: https://www.youtube.com/watch?v=8GCnHJDoXRk
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# What Breaks When Automatic Speech Recognition Systems Go Multilingual [PyCon DE & PyData 2026]

**Rashmi Nagpal**

`PyData` · `PyData` · `2026` · `44 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=8GCnHJDoXRk) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Rashmi Nagpal reveal the critical engineering challenges and hidden pitfalls of building scalable, multilingual ASR systems for deepfake detection.

Speakers:
Rashmi Nagpal

Description:
Multilingual Automatic Speech Recognition (ASR) systems face significant challenges regarding linguistic variance, acoustic features, and data integrity. A primary problem is data leakage, where training and testing sets overlap, leading to models that overfit to specific speaker identities rather than learning general language patterns. This is particularly acute in multilingual contexts where a single speaker may appear in multiple language datasets, causing the model to memorize the speaker's unique pitch and cadence rather than the linguistic content.

To address these issues, a robust ASR pipeline must implement speaker-disjoint splits, ensuring no single speaker exists in both the training and validation sets. The technical approach involves a modular architecture using the decorator design pattern, where each language is assigned a specific pre-processor and normalizer. This separation of concerns allows new languages to be added as functions without disrupting validated pipelines. To handle code-mixed audio—where speakers switch languages mid-sentence—the system utilizes Voice Activity Detection (VAD) for silence trimming and a loanword cache to manage context switching.

Key takeaways include the use of specific acoustic metrics to detect deepfake audio; synthetic voices often exhibit lower jitter and shimmer variance, appearing unnaturally smooth compared to human speech. Evaluation relies on Word Error Rate (WER) and Character Error Rate (CER), though the analysis shows that CER can remain high even when semantic meaning is preserved, necessitating loanword normalization to reduce error deviations. Ultimately, a successful multilingual ASR system requires a combination of speaker-disjoint data management, language-specific configurations, and human-in-the-loop validation to prevent hallucination and overfitting.

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
