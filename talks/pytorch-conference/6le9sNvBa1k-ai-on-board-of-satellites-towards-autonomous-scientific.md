---
id: 6le9sNvBa1k
title: "AI On-board of Satellites, Towards Autonomous Scientific Instruments - Vit Ruzicka, NASA"
slug: ai-on-board-of-satellites-towards-autonomous-scientific
conference: pytorch-conference
conference_name: "PyTorch Conference"
category: "Practitioner AI conferences"
edition: "PyTorch Conference 2025"
year: 2025
speakers: ["Vit Ruzicka"]
channel: "PyTorch"
duration_min: 30
published_at: 2025-11-04T03:43:36Z
video_id: 6le9sNvBa1k
url: https://www.youtube.com/watch?v=6le9sNvBa1k
youtube_url: https://www.youtube.com/watch?v=6le9sNvBa1k
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: false
---

# AI On-board of Satellites, Towards Autonomous Scientific Instruments - Vit Ruzicka, NASA

**Vit Ruzicka**

`PyTorch Conference` · `PyTorch Conference 2025` · `2025` · `30 min`

[Watch the recording](https://www.youtube.com/watch?v=6le9sNvBa1k) · [Conference site](https://events.linuxfoundation.org/pytorch-conference-north-america/)

## Description

AI On-board of Satellites, Towards Autonomous Scientific Instruments - Vit Ruzicka, NASA - Jet Propulsion Laboratory

I recently finished my PhD at the University of Oxford focusing on deployment of ML models on-board of satellites. I would like to share my research and outline several future points that I am currently exploring as a Postdoc at NASA JPL.

In 2023, our ML model was deployed on-board of a satellite by D-Orbit. We successfully tested our efficient and tiny foundational model RaVAEn and also achieved the world's first training of a ML model using PyTorch on-board of a satellite. We used few-shot learning with a small annotated dataset of cloudy tiles. While on-board inference often uses frozen model inference and libraries such as ONNX or TensorRT, for training we interestingly needed PyTorch to keep the model weight changing during training.

Since then I focused on designing ML models for imaging spectroscopy (hyperspectral) data. This data is a key enabler for a number of detection tasks, such as the detections of faint traces of methane in the atmosphere, or the identification of minerals present at the surface of the Earth. NASA’s recent mission EMIT uniquely provides global coverage. I am currently researching the deployment of efficient ML models to enable instrument autonomy.
