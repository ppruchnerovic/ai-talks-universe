---
id: 0Mh271tYYmQ
title: "It Works on My Machine: Why LLM Apps Fail Users (Not Tests) [PyCon DE & PyData 2026]"
slug: it-works-on-my-machine-why-llm-apps-fail-users-not-tests
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Thomas Prexl", "Frank Rust"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:20:07Z
video_id: 0Mh271tYYmQ
youtube_url: https://www.youtube.com/watch?v=0Mh271tYYmQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# It Works on My Machine: Why LLM Apps Fail Users (Not Tests) [PyCon DE & PyData 2026]

**Thomas Prexl, Frank Rust**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0Mh271tYYmQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Thomas Prexl and Frank Rust reveal why LLM applications often pass every test yet still fail in production, and learn how to bridge the gap between evaluation metrics and actual user experience.

Speakers:
Thomas Prexl, Frank Rust

Description:
Large Language Model (LLM) applications often fail in production despite passing automated tests because of a gap between technical performance and user expectations. This failure typically manifests in three dimensions: expectations, where users compare specialized business tools to the versatile, conversational nature of consumer-grade APIs like ChatGPT; functional scope, where users attempt tasks outside the intended design; and operational stability, where latency and timeouts in the customer's specific tenant create unacceptable delays.

To address these issues, a user-centric development approach replaces traditional waterfall or agile models with a process focused on transparency and real-world data. The methodology begins by collecting a baseline of 100 or more real-world questions, including the expected answers and the specific source documents required for the response. To manage performance, Arize Phoenix (OPIC) is used to trace the LLM pipeline, allowing developers to pinpoint bottlenecks—such as distinguishing between slow data retrieval and slow model generation—and communicate these constraints to the customer.

Trust is established by explicitly defining the system's limitations and providing sample questions to guide user interaction. For Retrieval-Augmented Generation (RAG) systems, transparency is increased by providing direct links to source chunks and utilizing metadata filters to ensure the model retrieves information from the correct product version. Finally, adoption is driven by implementing "quick win" features that solve immediate pain points, such as voice-to-text maintenance reports or automated email translation, which integrate the LLM into the user's existing daily workflow.

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
