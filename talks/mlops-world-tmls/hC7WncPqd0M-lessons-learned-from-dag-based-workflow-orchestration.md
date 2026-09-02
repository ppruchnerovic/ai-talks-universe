---
id: hC7WncPqd0M
title: "Lessons Learned from DAG based Workflow Orchestration"
slug: lessons-learned-from-dag-based-workflow-orchestration
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Kevin Gregory Kho"]
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 39
published_at: 2023-08-18T01:34:36Z
video_id: hC7WncPqd0M
url: https://www.youtube.com/watch?v=hC7WncPqd0M
youtube_url: https://www.youtube.com/watch?v=hC7WncPqd0M
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Agents & orchestration", "Classic ML & data science", "Data engineering & MLOps"]
transcript: false
---

# Lessons Learned from DAG based Workflow Orchestration

**Kevin Gregory Kho**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `39 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=hC7WncPqd0M) · [Conference site](https://mlopsworld.com/)

## Description

Speaker:
Kevin Gregory Kho, Senior Open Source Community Engineer, Prefect
Kevin Kho is an Open Source Community Engineer at Prefect, an open-source workflow orchestration management system. Previously, he was a data scientist at Paylocity, where he worked on adding machine learning features to their Human Capital Management (HCM) Suite. Outside of work, he is a contributor for Fugue, an abstraction layer for Pandas, Spark, and Dask. He also organizes the Orlando Machine Learning and Data Science Meetup.

Abstract:
Workflow orchestration has traditionally been closely coupled to the concept of Directed Acyclic Graphs (DAGs). Building data pipelines involved registering a static graph containing all the tasks and their respective dependencies. During workflow execution, this graph would be traversed and executed. The orchestration engine would then be responsible for determining which tasks to trigger based on the success and failure of upstream tasks.

This system was sufficient for standard batch processing-oriented data engineering pipelines but proved to be constraining for some emerging common use cases. Data professionals would have to compromise their vision to get their workflow to fit in a DAG. For example,
1. How do I re-run a part of my workflow based on a downstream condition?
2. How do I execute a long-running workflow?
3. How do I dynamically add tasks to the DAG during runtime?

This has led to the development of Prefect Orion (Prefect 2.0), a DAG-less workflow orchestration system that emphasizes runtime flexbility and an enhanced developer experience. By removing the DAG constraint, Orion offers an interface to workflow orchestration that feels more Pythonic than ever. Developers only need to wrap as little code as they want to get observability into a specific task of the workflows.
