---
id: uyrlnwzsW1U
title: "Using Sensor Fusion and ML to Navigate Underground When GPS Fails [PyCon DE & PyData 2026]"
slug: using-sensor-fusion-and-ml-to-navigate-underground-when-gps
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Étienne Tremblay"]
channel: null
duration_min: 28
published_at: 2026-08-04T22:21:11Z
video_id: uyrlnwzsW1U
youtube_url: https://www.youtube.com/watch?v=uyrlnwzsW1U
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Using Sensor Fusion and ML to Navigate Underground When GPS Fails [PyCon DE & PyData 2026]

**Étienne Tremblay**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=uyrlnwzsW1U) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Étienne Tremblay explain how to leverage sensor fusion and ML to maintain precise navigation in GPS-denied underground environments.

Speakers:
Étienne Tremblay

Description:
Underground navigation is challenging because GPS signals cannot penetrate subway tunnels, leaving smartphones to rely on imprecise cell tower mapping or Wi-Fi scanning with accuracy radii often exceeding one kilometer. To solve this, a system was developed that estimates location by fusing motion sensor data, train schedules, and sparse device locations. The core logic treats the problem as a sequence of events: by detecting when a train moves and stops, the system can count stations traveled from a known starting point.

The technical approach utilizes a two-stage machine learning pipeline. First, a Convolutional Neural Network (CNN) is trained on millions of unlabeled user trips using a pretext task to classify general motion modes (stationary, walking, or automotive) based on accelerometer and gyrometer data. Second, transfer learning is applied to a smaller, high-quality dataset of 300 manually annotated trips to refine a binary classifier that specifically identifies "moving metro" states. This model is converted to TensorFlow Lite and deployed on-device via Core ML for iOS and Android to ensure functionality during network outages.

A mixer module integrates the binary motion predictions with offline train schedules and any available high-accuracy device locations to resolve edge cases, such as trains stopping between platforms. The system achieves approximately 90% accuracy, with predictions typically within one station of the true location. To manage uncertainty, the user interface employs warning banners and asymmetric confidence intervals, acknowledging a bias toward late rather than early predictions. The entire training pipeline is managed using Vertex AI to handle complex dependency graphs and parallel testing.

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
