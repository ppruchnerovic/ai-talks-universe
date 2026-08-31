---
id: lwTfY3Eh1dw
title: "Embedding Data Science in IoT devices with MicroPython and emlearn [PyCon DE & PyData 2026]"
slug: embedding-data-science-in-iot-devices-with-micropython-and
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Jon Nordby"]
channel: "PyData"
duration_min: 27
published_at: 2026-08-04T22:20:06Z
video_id: lwTfY3Eh1dw
youtube_url: https://www.youtube.com/watch?v=lwTfY3Eh1dw
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Embedding Data Science in IoT devices with MicroPython and emlearn [PyCon DE & PyData 2026]

**Jon Nordby**

`PyData` · `PyData` · `2026` · `27 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lwTfY3Eh1dw) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Jon Nordby explain how to leverage MicroPython and emlearn to embed powerful machine learning models directly into low-cost IoT devices for a local-first approach to data science.

Speakers:
Jon Nordby

Description:
Embedding data science into IoT devices is achievable using MicroPython and specialized libraries to overcome the memory and processing constraints of microcontrollers. A primary challenge is implementing machine learning on hardware with limited RAM—often around 1 MB—which precludes the use of standard libraries like scikit-learn or Keras. To solve this, emlearn converts scikit-learn or Keras models into efficient C implementations that can be deployed as .mpy files, allowing for local activity recognition using accelerometer data.

For a standalone smartwatch prototype using an ESP32-based device with 16 MB of flash and 16 MB of RAM, a local-first data architecture is required to store multiple days of sensor data. This is implemented via a time-series data lake using Apache Hive-style partitioning, which organizes data by day, hour, and minute. This structure allows the device to retain high-resolution raw data for short periods while keeping processed machine learning predictions for longer durations. Performance tests show read speeds between 100 KB/s and 250 KB/s, which is sufficient for querying a full day of data in approximately 10 seconds.

The system manages concurrent tasks—sensor readout, ML inference, data storage, and web serving—using the asyncio library. To prevent data loss from sensor buffer overflows, tasks are kept under 100 ms, and the MicroDot web server is used to stream data in chunks. The user interface is served directly from the device using Preact and a minimal version of Plotly (250 KB). While the system supports external integration via HTTP or MQTT, implementing strict timeouts is necessary to prevent network latency from blocking the single-core processor.

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
