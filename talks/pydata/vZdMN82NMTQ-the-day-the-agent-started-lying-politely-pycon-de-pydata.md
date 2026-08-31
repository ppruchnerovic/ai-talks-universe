---
id: vZdMN82NMTQ
title: "The Day the Agent Started Lying (Politely) [PyCon DE & PyData 2026]"
slug: the-day-the-agent-started-lying-politely-pycon-de-pydata
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Asya Melnik"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-04T22:21:25Z
video_id: vZdMN82NMTQ
youtube_url: https://www.youtube.com/watch?v=vZdMN82NMTQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# The Day the Agent Started Lying (Politely) [PyCon DE & PyData 2026]

**Asya Melnik**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=vZdMN82NMTQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Asya Melnik reveal how to detect silent failures and manage data drift to ensure your LLM-based agents remain trustworthy and accurate in production.

Speakers:
Asya Melnik

Description:
LLM agents often suffer from silent degradation, where the model continues to provide confident responses despite a shift in the underlying data distribution. This problem is particularly acute in non-deterministic systems where ground truth labels are unavailable for real-time validation, rendering traditional accuracy metrics useless. In a customer support ticket routing scenario, for example, the launch of a new product can introduce new vocabulary and shift the meaning of existing terms, leading the agent to misclassify ticket priority while reporting zero system errors.

To detect this drift without relying on manual labeling, a multi-signal evaluation framework is used. This approach monitors six distinct metrics: Shannon entropy (calculated using all available class probabilities to measure internal uncertainty), fallback rates (acting as a canary signal), vocabulary drift (measuring the distance of current word vectors from a stable centroid), human disagreement (tracking when users override agent decisions), LLM-as-a-judge (using a model like Claude Haiku to verify if the agent's reasoning is faithful to the input), and trajectory (assessing the logical flow from input to outcome).

The key takeaway is the implementation of a tiered action plan based on the number of triggering signals. A single alert, such as an increased fallback rate, suggests observation. Two or more signals indicate a need for investigation. When multiple signals across different layers—internal confidence, external human feedback, and logical verification—trigger simultaneously, it provides a high-confidence indicator that the agent's prompt or model requires updating. This "nervous system" approach allows operators to identify and fix silent failures before they impact business operations.

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
