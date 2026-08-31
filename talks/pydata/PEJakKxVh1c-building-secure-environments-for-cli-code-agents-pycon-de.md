---
id: PEJakKxVh1c
title: "Building Secure Environments for CLI Code Agents [PyCon DE & PyData 2026]"
slug: building-secure-environments-for-cli-code-agents-pycon-de
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Harald Nezbeda"]
channel: null
duration_min: 30
published_at: 2026-08-25T18:20:05Z
video_id: PEJakKxVh1c
youtube_url: https://www.youtube.com/watch?v=PEJakKxVh1c
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Building Secure Environments for CLI Code Agents [PyCon DE & PyData 2026]

**Harald Nezbeda**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=PEJakKxVh1c) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Harald Nezbeda demonstrate how to build secure, containerized environments to safely harness the power of CLI code agents without compromising your host system.

Speakers:
Harald Nezbeda

Description:
Running CLI code agents directly on a host machine introduces significant security risks, including accidental data exfiltration, destructive file system operations, and the installation of malicious packages. Because these agents operate with the user's full permissions, a "lethal trifecta" occurs when an agent has access to private data, external network connectivity, and processes untrusted content.

To mitigate these risks, the VibePod framework implements an isolation pattern using Docker containers to sandbox the agent's runtime. This approach restricts the agent's scope by mounting only specific project workspaces and using a deny list to prevent access to root and home directories. VibePod utilizes a Python-based CLI, built with Typer and PlatformDeers, to manage these containers across different operating systems.

Observability is achieved through a man-in-the-middle (MITM) proxy that intercepts all HTTP and WebSocket traffic between the agent and the LLM provider. This traffic is logged into a local SQLite database, which is then visualized via a Dataset dashboard. This system allows users to monitor raw prompts, track response times, and analyze token consumption—including input, output, and cache tokens—by aggregating data directly from the raw HTTP responses.

While containerization reduces the attack surface, it does not eliminate risks such as prompt injection or data exposure via misconfigured mounts. Effective security requires combining these technical isolations with the principle of least privilege and consistent human review of agent actions.

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
