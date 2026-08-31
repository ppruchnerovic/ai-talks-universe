---
id: GcaQy9K9FDc
title: "Black Hole Stars: An Astronomical Mystery (Mostly) Solved with NumPyro and JAX"
slug: black-hole-stars-an-astronomical-mystery-mostly-solved-with
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Raphael Hviding"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-04T22:20:43Z
video_id: GcaQy9K9FDc
youtube_url: https://www.youtube.com/watch?v=GcaQy9K9FDc
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Black Hole Stars: An Astronomical Mystery (Mostly) Solved with NumPyro and JAX

**Raphael Hviding**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=GcaQy9K9FDc) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Dr. Raphael Hviding demonstrate how JAX and NumPyro are being used to solve one of the universe's greatest mysteries: the nature of "Black Hole Stars."

Speakers:
Raphael Hviding

Description:
The James Webb Space Telescope (JWST) has revealed a population of compact, high-redshift objects known as little red dots. These objects appear in the early universe, approximately 13 billion years ago, and exhibit spectral characteristics that defy standard astronomical models. Specifically, their spectra show extreme broad emission lines and absorption lines, as well as spectral breaks that are inconsistent with galaxies dominated by stars or typical quasars. Because these objects are too small to be standard galaxies and do not match the red-end profiles of quasars, they are hypothesized to be black hole stars. These are massive systems where a central black hole undergoes rapid accretion, providing the outward pressure to support a massive envelope of gas, rather than relying on nuclear fusion. This mechanism may explain the existence of supermassive black holes in the early universe by allowing for super-Eddington accretion rates that exceed standard growth limits.

Analyzing these objects requires precise spectroscopy, but researchers face the problem of undersampling, where pixel sizes are larger than the scale of the spectral functions. Traditional supersampling via Riemann integration increases compute time and memory usage, which hinders the use of Monte Carlo methods for error distribution. To solve this, the Unified Line Integration Turbo Engine (Unite) was developed. Unite uses JAX and NumPyro to replace numerical supersampling with analytic integrals of the spectral profiles. This approach provides exact solutions and enables efficient Bayesian inference using MCMC and NUTS. By combining low-resolution and high-resolution spectra within a single inference model, researchers can increase detection confidence for broad lines from 95% to nearly 100%, allowing for the precise distance measurement of the most distant known galaxies.

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
