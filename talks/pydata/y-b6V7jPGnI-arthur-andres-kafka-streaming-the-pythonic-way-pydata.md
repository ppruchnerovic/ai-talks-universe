---
id: y-b6V7jPGnI
title: "Arthur Andres- Kafka Streaming, the Pythonic Way | Pydata London 26"
slug: arthur-andres-kafka-streaming-the-pythonic-way-pydata
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Arthur Andres- Kafka Streaming"]
channel: null
duration_min: 36
published_at: 2026-06-15T15:55:11Z
video_id: y-b6V7jPGnI
youtube_url: https://www.youtube.com/watch?v=y-b6V7jPGnI
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Arthur Andres- Kafka Streaming, the Pythonic Way | Pydata London 26

**Arthur Andres- Kafka Streaming**

`PyData` · `PyData` · `2026` · `36 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=y-b6V7jPGnI) · [Conference site](https://pydata.org/)

## Description

Kafka Streaming, the Pythonic Way

Adopting a streaming architecture as a Python developer often means abandoning the tools and abstractions you know: DataFrames, batch processing, familiar data workflows, in favour of an entirely different mental model. After ten years of tackling this problem across multiple companies, I've learned it doesn't have to be that way.

In this talk, I'll show how to treat Kafka not as a stream of individual messages but as a source of micro-batches, and how to deserialize those messages, whether JSON or Protobuf, into Arrow-backed DataFrames. The result: your processing code looks the same whether the data comes from a Parquet file or a Kafka topic.

No heavy framework required. Using confluent-kafka and Apache Arrow, I'll walk through how to build this from the ground up, so you understand every layer of the stack.

The talk opens with a concrete example of stream processing. We have data flowing in, and a clear task to perform on it. No theory, no definitions, just a practical scenario the audience can immediately relate to.

From there, we step back and look at how Kafka works. Topics, consumers, partitions, message formats. Just enough to understand the architecture behind the example, and to appreciate why Kafka has become the standard backbone for streaming systems.

Then comes the friction. When you consume from Kafka, you get one message at a time. Each message is serialized as JSON or Protobuf. If you're a Python developer used to working with DataFrames, this feels like going back to writing for loops over rows. We'll look at what the naive approach looks like in code, and why it quickly becomes painful as processing logic gets more complex.

With the problem clearly felt, we introduce the solution: treating Kafka not as a stream of individual messages but as a source of micro-batches, and deserializing those batches directly into Arrow-backed DataFrames using confluent-kafka and Apache Arrow. The processing code that follows looks identical to what you'd write against a Parquet file. We'll see both versions side by side to make this concrete.

We close with lessons learned from applying this pattern in production over ten years. What breaks, what surprises you, and what trade-offs you should be aware of before adopting this approach in your own systems.

The talk assumes familiarity with Python and basic data processing with DataFrames. No prior knowledge of Kafka or streaming is required.
www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
