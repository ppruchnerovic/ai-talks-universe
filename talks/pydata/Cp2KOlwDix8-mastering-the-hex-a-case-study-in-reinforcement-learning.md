---
id: Cp2KOlwDix8
title: "Mastering the Hex: A Case Study in Reinforcement Learning for Strategy Games"
slug: mastering-the-hex-a-case-study-in-reinforcement-learning
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Simon Hedrich"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-25T18:20:17Z
video_id: Cp2KOlwDix8
youtube_url: https://www.youtube.com/watch?v=Cp2KOlwDix8
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# Mastering the Hex: A Case Study in Reinforcement Learning for Strategy Games

**Simon Hedrich**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Cp2KOlwDix8) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Simon Hedrich explore the complexities of reinforcement learning as he breaks down the challenges of building a custom AI agent to master the hexagonal strategy game Antiyoy.

Speakers:
Simon Hedrich

Description:
The project addresses the challenge of developing an autonomous AI agent to play a turn-based strategy game on a hexagonal grid. The game involves capturing territory, managing income, upgrading unit strength levels, and constructing buildings like farms and towers to secure borders. The primary technical difficulty lies in the complexity of the game rules and the vast state-action space associated with hexagonal movement and placement.

The approach involves rebuilding the game logic in Python using offset coordinates to represent the hexagonal map as a 2D array. To facilitate machine learning, a Gymnasium environment was implemented to provide the agent with observations, action masks, and rewards. The observation state consists of multiple Boolean channels representing territories, units, buildings, trees, and gravestones, with normalized values for income and money. The output layer manages approximately 4,000 theoretical actions, though typically only 100 are valid per turn. The architecture utilizes a Convolutional Neural Network (CNN) to process the map channels, paired with an actor-critic model to balance action selection and evaluation. Training was monitored using MLflow.

Key takeaways highlight the difficulty of reward shaping and state complexity. The agent was tested using sparse rewards (final win/loss), dense rewards (intermediate gains), and a hybrid approach. While the model showed some success on smaller maps, it struggled on larger maps, occasionally performing worse than random play. Furthermore, training the agent against itself led to infinite loops of indecision, demonstrating that scaling down the environment and carefully tuning reward functions are critical for convergence in complex strategy games.

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
