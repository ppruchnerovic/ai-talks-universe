---
id: 95f19uLpEFo
title: "Encrypted inferences over decision trees"
slug: encrypted-inferences-over-decision-trees
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: null
duration_min: 22
published_at: 2026-08-11T13:10:10Z
video_id: 95f19uLpEFo
youtube_url: https://www.youtube.com/watch?v=95f19uLpEFo
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Encrypted inferences over decision trees

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `22 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=95f19uLpEFo) · [Conference site](https://mlopsworld.com/)

## Description

Alex Shpurov, CTO, 01 Quantum
Daniel Johnson, Software Engineer, 01 Quantum

About the Speaker:
Alex is a hands-on Software, AI, and Cloud Engineer with 30+ years of experience building and scaling fintech systems for some of North America's top tier-1 financial institutions, including Capital One, RBC, TD, and Bank of America. His work spans cloud-native architecture, production AI and agentic systems, and cutting-edge cryptography — including blockchain, Zero-Knowledge Proofs, and Post-Quantum Security. He's the founder of FHE-Studio, an open-source IDE for privacy-first AI built on fully homomorphic encryption, and holds 14 granted US patents across AI, cryptography, cloud, and blockchain. An AWS Certified Solutions Architect and TMLS Agentic AI Committee member, Alex brings rare depth at the intersection of finance, AI, and security — with a track record of not just designing systems, but actually shipping them.

Daniel holds a PhD in Applied Mathematics from Carleton University (2025) and is a post-quantum cryptography researcher currently working with 01 Quantum and the NC-CIPSeR lab at Carleton. His doctoral work produced some of the field's most notable recent results- including the discovery of the Lattice Reconstitution Attack (LRA), which broke the HPPK KEM in under one second with 100% success, and a variant that matches the world record for cracking the 1978 Merkle-Hellman scheme. Daniel has also developed novel attacks on NTRU and NTRU Prime, implemented at scale on national supercomputing infrastructure. Since completing his doctorate, he has turned his focus to Fully Homomorphic Encryption applied to AI decision tree models, exploring the unsolved challenge of achieving simultaneous client and model privacy. A University Medal recipient in Mathematics from his undergraduate years at Carleton, Daniel brings equal passion for solving hard problems and making complex ideas accessible to others.

Abstract:
This virtual talk will introduce the 01 Quantum AI Marketplace concept and demonstrate an example of an FHE-encrypted decision tree. The demo will show a client logging in with private data, encrypting that data using fully homomorphic encryption, sending it to a model owner, and receiving encrypted inference results.
Decision trees are a useful starting point for encrypted inference because they are deterministic and interpretable: for a given input, the model follows a clear path to a prediction. In an FHE setting, however, that path cannot be followed with normal plaintext branching. Instead, the tree logic is transformed into encrypted comparisons, path scoring, and leaf selection, allowing the model owner to evaluate the decision tree without accessing the client’s raw data.
The client then decrypts the result and obtains the final prediction.
The second part of the talk will explain why FHE development is fundamentally different from regular AI software development. Unlike traditional applications, FHE systems cannot rely on normal branching over private data. Comparisons are difficult and often approximate, algorithms must be redesigned as mathematical circuits, and performance depends heavily on packing, rotations, multiplicative depth, and parameter selection.
Attendees will leave with a practical understanding of how encrypted inference works, why it matters for sensitive-data AI use cases, and what engineering challenges must be solved to make FHE-based AI systems production-ready. This session is intended for AI leaders, applied ML engineers, privacy engineers, and technical decision-makers exploring secure AI deployment models.
