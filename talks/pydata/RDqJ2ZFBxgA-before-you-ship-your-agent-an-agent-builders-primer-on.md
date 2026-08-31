---
id: RDqJ2ZFBxgA
title: "Before You Ship Your Agent: An Agent Builder’s Primer on Jailbreaking Attacks"
slug: before-you-ship-your-agent-an-agent-builders-primer-on
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 32
published_at: 2026-08-04T22:22:00Z
video_id: RDqJ2ZFBxgA
youtube_url: https://www.youtube.com/watch?v=RDqJ2ZFBxgA
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Before You Ship Your Agent: An Agent Builder’s Primer on Jailbreaking Attacks

**Speaker not identified**

`PyData` · `PyData` · `2026` · `32 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=RDqJ2ZFBxgA) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Simonas Černiauskas, CTO of tisix.io, reveal why traditional AI guardrails fail and how to secure your AI agents against jailbreaking and prompt injection attacks before they hit production.

Speakers:
Simonas Černiauskas

Description:
Large Language Model (LLM) agents introduce significant security risks because they combine three dangerous capabilities: the processing of untrusted external input, access to sensitive private data, and the ability to execute external actions via APIs. The fundamental vulnerability lies in the transformer architecture, which fails to distinguish between system instructions and data tokens, allowing attackers to override intended behavior.

Attack vectors range from direct prompt injection to indirect attacks, where malicious instructions are hidden within retrieved web content or Model Context Protocol (MCP) tools. Advanced techniques include tool-chaining, where a sequence of seemingly benign calls results in a destructive outcome, and memory poisoning, which embeds long-term vulnerabilities in a RAG or graph system. Research indicates that dynamic, adaptive attacks can bypass standard guardrails with success rates as high as 90%, rendering static keyword blockers and basic content filters insufficient.

To secure agentic systems, developers should implement the principle of least privilege by scoping tool access to specific tasks and using short-lived API keys. Infrastructure should utilize sandboxing via Docker or micro-VMs to isolate execution. A critical defense strategy is to avoid the lethal trifecta by ensuring an agent never simultaneously possesses all three dangerous capabilities without a human in the loop. When high-risk actions—such as financial transactions or data deletion—are required, explicit human approval is mandatory. Finally, security monitoring must establish a baseline of normal data flow to detect anomalies in tool combinations or data volume, treating all external input as untrusted through rigorous sanitization.

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
