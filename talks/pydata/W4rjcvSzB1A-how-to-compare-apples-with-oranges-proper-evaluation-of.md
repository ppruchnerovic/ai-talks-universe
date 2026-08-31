---
id: W4rjcvSzB1A
title: "How to compare apples with oranges: Proper evaluation of article-level demand forecasts"
slug: how-to-compare-apples-with-oranges-proper-evaluation-of
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Stefan Birr", "Mones Raslan"]
channel: "PyData"
duration_min: 29
published_at: 2026-08-04T22:21:42Z
video_id: W4rjcvSzB1A
youtube_url: https://www.youtube.com/watch?v=W4rjcvSzB1A
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# How to compare apples with oranges: Proper evaluation of article-level demand forecasts

**Stefan Birr, Mones Raslan**

`PyData` · `PyData` · `2026` · `29 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=W4rjcvSzB1A) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Stefan Birr and Mones Raslan from Zalando reveal how to navigate the pitfalls of large-scale demand forecasting and implement robust, aggregated metrics to accurately evaluate millions of time series.

Speakers:
Stefan Birr, Mones Raslan

Description:
Article-level demand forecasting at scale involves predicting sales for hundreds of thousands of items across multiple markets, resulting in approximately 10 billion records daily. The primary challenge is the disparity in sales velocity; absolute metrics like Mean Absolute Error (MAE) or Root Mean Square Error (RMSE) overweight high-selling articles, while naive relative metrics, such as Mean Absolute Percentage Error (MAPE), fall into a scaling trap. In this trap, fluctuations in the aggregate error metric often reflect changes in the assortment mixture—the ratio of high-sellers to low-sellers—rather than actual changes in model performance.

To resolve this, a benchmarking approach using Poisson-based simulations is employed. By generating a perfect probabilistic forecast—where the mean of the Poisson distribution is the actual observed value—a theoretical lower bound for the error is established. This is paired with a naive upper bound, such as repeating the previous day's sales. By anchoring the actual model error between these two bounds, it becomes possible to determine if a model is truly improving or if the error is simply shifting due to seasonal changes in the product mix.

Key takeaways include the danger of overfitting to a single aggregate metric, which can introduce bias toward high-selling items and degrade overall accuracy. To mitigate this, a multi-metric evaluation strategy is used, combining demand error with bias measures and Gross Merchandise Volume (GMV) error. These calibrated metrics are then translated into a traffic-light system for stakeholders, allowing for market-specific diagnostics where a high error in a low-volume market may be acceptable, while a lower error in a high-volume market triggers an investigation.

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
