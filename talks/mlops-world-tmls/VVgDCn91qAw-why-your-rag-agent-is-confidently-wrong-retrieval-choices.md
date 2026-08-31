---
id: VVgDCn91qAw
title: "Why Your RAG Agent Is Confidently Wrong: Retrieval Choices That Actually Matter"
slug: why-your-rag-agent-is-confidently-wrong-retrieval-choices
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: null
duration_min: 35
published_at: 2026-08-11T13:10:10Z
video_id: VVgDCn91qAw
youtube_url: https://www.youtube.com/watch?v=VVgDCn91qAw
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Why Your RAG Agent Is Confidently Wrong: Retrieval Choices That Actually Matter

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `35 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=VVgDCn91qAw) · [Conference site](https://mlopsworld.com/)

## Description

David vonThenen, Sr Ai/ML Engineer, Office of the CTO, NetApp

About the Speaker:
David is a Senior AI/ML Engineer within the Office of the CTO at NetApp, where he’s dedicated to empowering developers to build, scale, and deploy AI/ML solutions in production environments. He brings deep expertise in building and training models for applications such as NLP, vision, real-time analytics, and even classifying debilitating diseases. His mission is to help users build, train, and deploy AI models efficiently, making advanced machine learning accessible to users of all levels.

Before NetApp, he was heavily involved in the AI/ML community, specifically in conversational AI solutions and driving AI platform growth in a DevRel and pre-sales role. David frequently shares his insights at industry conferences and events, offering hands-on guidance for implementing AI/ML in cloud environments. David's prior experience includes contributing to the Kubernetes and CNCF ecosystems, working hands-on with VMware virtualization, implementing backup/recovery solutions, and developing hardware storage adapter firmware and drivers.

Abstract:
Most RAG discussions start and end with vector embeddings. That makes sense because vector search is approachable, fast to prototype, and widely supported. But semantic similarity is not the same thing as answer retrieval. When teams rely on embeddings as the default for every use case, they often end up with systems that sound convincing while returning weak, incomplete, or confidently incorrect answers. This talk reframes retrieval as the real design decision in RAG, not a backend detail.

We will walk through the major retrieval options at a high level, including vector, graph, and BM25 approaches, and explain where each one fits. Then we will show why hybrid designs, such as Vector + Graph and Vector + BM25, often produce stronger results by combining semantic context with stronger grounding and greater precision. The goal is to give AI engineers a practical mental model for choosing a retrieval approach based on the shape of their data and the kinds of answers they need, rather than defaulting to embeddings because everyone else did.
