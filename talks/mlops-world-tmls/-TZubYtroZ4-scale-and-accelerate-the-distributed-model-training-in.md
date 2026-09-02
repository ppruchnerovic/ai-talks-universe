---
id: -TZubYtroZ4
title: "Scale and Accelerate the Distributed Model Training in Kubernetes Cluster"
slug: scale-and-accelerate-the-distributed-model-training-in
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Jack Jin"]
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 49
published_at: 2023-08-18T01:34:36Z
video_id: -TZubYtroZ4
url: https://www.youtube.com/watch?v=-TZubYtroZ4
youtube_url: https://www.youtube.com/watch?v=-TZubYtroZ4
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Scale and Accelerate the Distributed Model Training in Kubernetes Cluster

**Jack Jin**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `49 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=-TZubYtroZ4) · [Conference site](https://mlopsworld.com/)

## Description

Speaker:
Jack Jin, Lead ML Infra Engineer, Zoom
Jack Jin is a lead machine learning infrastructure engineer at Zoom AI/ML, designed and built end to end Kubernetes cluster based ML platform for multiple Zoom ML teams on shared GPU resource pool, to run the distributed model training, like PyTorch DDP with Kubeflow PyTorchJob for accelerating the multi GPU multi nodes training performance with RDMA, RoCE and SRIOV. He also designed and built the data ETL, data exploration, big data processing and ML exploration system and infrastructure. Before joined to Zoom, Jack was MLOps Cloud Lead in Roche Genentech and Cloud consultant in IBM/Taos and was involved in building ML platform serving 500 data scientists of Roche globally

Abstract:
In order to orchestrate Deep Learning workloads that scale across multiple GPUs and nodes, Kubernetes offers a compelling solution. With Kubernetes and Kubeflow PytorchJob, we can easily schedule and track a distributed training job on multi-GPU single-node, and multi-GPU multi-nodes in a shared GPU resource pool. To accelerate deep learning training at Zoom, we enable RDMA, RoCE to bypass the CPU kernel and offload the TCP/IP protocol. We apply this technology in Kubernetes with SRIOV by NVIDIA Network Operator in a heterogenous GPUs cluster with 4 GPU servers and 8 GPU servers, and reach a near linear performance increase as the GPU number and worker node increases
