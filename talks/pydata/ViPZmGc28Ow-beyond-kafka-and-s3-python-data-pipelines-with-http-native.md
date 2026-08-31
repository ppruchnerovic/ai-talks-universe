---
id: ViPZmGc28Ow
title: "Beyond Kafka and S3: Python Data Pipelines with HTTP-Native Bytestreams [PyCon DE & PyData 2026]"
slug: beyond-kafka-and-s3-python-data-pipelines-with-http-native
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Johannes Dröge"]
channel: "PyData"
duration_min: 45
published_at: 2026-08-04T22:20:58Z
video_id: ViPZmGc28Ow
youtube_url: https://www.youtube.com/watch?v=ViPZmGc28Ow
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Beyond Kafka and S3: Python Data Pipelines with HTTP-Native Bytestreams [PyCon DE & PyData 2026]

**Johannes Dröge**

`PyData` · `PyData` · `2026` · `45 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ViPZmGc28Ow) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Johannes Dröge explain how the ZebraStream Protocol simplifies cross-organizational data sharing by enabling HTTP-native bytestreams that integrate seamlessly with Python’s file-like interface.

Speakers:
Johannes Dröge

Description:
Cross-organizational data sharing often incurs high alignment costs due to differing infrastructure, technology stacks, and compliance regimes. Traditional solutions like message brokers (e.g., Kafka) require significant infrastructure coupling and specific protocols, while S3-based transfers often rely on one-way push/pull models. REST APIs frequently blend transport layers with data models, creating rigid dependencies. To address these challenges, the ZebraStream protocol adapts the Unix named pipe model to HTTP, treating data as opaque byte streams rather than discrete, size-restricted messages.

The approach utilizes a stateless relay that connects HTTP PUT (upload) and GET (download) requests in real time. To solve the timing and synchronization issues inherent in HTTP, the protocol employs a rendezvous system via a Connect API. A long-poll mechanism ensures both the producer and consumer are present before dispatching them to the data API for streaming. This architecture shifts the coordination model from a static architectural decision to a runtime decision, allowing the system to function as either a push or pull pipeline depending on which party connects first.

In Python, the implementation provides a file-like interface inheriting from the IO base class. This allows the stream to be passed directly into standard functions, such as Pandas read_csv or LogGuru sinks, without modifying the underlying business logic. The protocol supports end-to-end encryption using an adapted AGE-H algorithm, ensuring that the relay provider cannot access sensitive data. Key technical benefits include the elimination of VPNs or open ports, the ability to handle arbitrary data sizes, and the propagation of exceptions between peers to ensure data integrity.

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
