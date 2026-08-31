---
id: 9gWjqjHEM8g
title: "To nest, or not to nest? Nested data types in Polars with big data [PyCon DE & PyData 2026]"
slug: to-nest-or-not-to-nest-nested-data-types-in-polars-with-big
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Daniel Finnan"]
channel: "PyData"
duration_min: 26
published_at: 2026-08-04T22:20:10Z
video_id: 9gWjqjHEM8g
youtube_url: https://www.youtube.com/watch?v=9gWjqjHEM8g
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: false
---

# To nest, or not to nest? Nested data types in Polars with big data [PyCon DE & PyData 2026]

**Daniel Finnan**

`PyData` · `PyData` · `2026` · `26 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=9gWjqjHEM8g) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Daniel Finnan explore the critical trade-offs between nested and flat data structures in Polars to optimize your big data pipeline's performance and readability.

Speakers:
Daniel Finnan

Description:
Polars provides nested data types, specifically lists and arrays, to store multiple values per row. While lists allow variable lengths, arrays require fixed lengths. These types are often used to express cardinality explicitly or to maintain a relational structure that avoids repeating observation data across multiple rows.

To evaluate the efficiency of these structures, a benchmark was conducted using simulated limit order book data consisting of 9,000 observations with 5,000 levels of bids and asks. Five different schemas were compared: no nesting (flat), flat arrays, nested arrays, flat lists, and nested lists. The dataset, totaling approximately 43 million rows in the flat format, was stored using the Z-standard compression algorithm.

The results indicate that no nesting is the most efficient approach for both storage and query performance. Flat formats resulted in the lowest storage overhead, whereas nested types increased file sizes and created more pronounced peaks in storage usage. In terms of execution speed, the no-nesting schema performed approximately twice as fast as the nested alternatives. Nested lists showed the worst performance, particularly during sophisticated queries involving filtering and aggregation.

The analysis concludes that while nested types offer a more intuitive relational structure, they introduce significant storage overhead and result in more complex, less readable query syntax. Despite the need for more frequent group-by operations and joins, flat data structures provide superior performance in Polars. For high-performance requirements with large datasets, avoiding nesting is recommended.

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
