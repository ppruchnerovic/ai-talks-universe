---
id: _cVfz88_j7A
title: "Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs"
slug: can-oncology-workflows-run-without-human-touch-anant
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Anant Shankhdhar"]
channel: null
duration_min: 17
published_at: 2026-07-20T00:00:00Z
video_id: _cVfz88_j7A
youtube_url: https://www.youtube.com/watch?v=_cVfz88_j7A
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs

**Anant Shankhdhar**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=_cVfz88_j7A) · [Conference site](https://www.ai.engineer/)

## Description

Can Oncology Workflows Run Without Human Touch?
At Risa, we automate healthcare workflows in oncology end-to-end using AI agents. We built four agents that work together  , each one handles a different step, then passes its output to the next. No human needed in between. The agents when combined are able to do the work of hundreds of medical workers a day. These agents are deployed across 20+ hospitals and supporting care for more than 100,000 patients.

Here is the overview of our agents:-
Ingestion Agent

Takes messy, unstructured medical documents, faxes, scanned PDFs, clinical notes and turns them into clean, structured data. AI models read each document, extract the key information (patient details, medications, diagnoses), and check against historical records to avoid duplicate work. If a patient has been seen before, the system already knows their history and skips redundant lookups.

EV Agent
Checks whether a patient's insurance is active and what their plan covers. Some insurers offer APIs; others only have web portals. The agent uses whichever method works calling APIs where available, and driving a browser through the portal where not. The result is always the same standardized output: what's covered, what the patient owes, and whether the plan is active.

Medical Reasoning Agent

The clinical brain of the system. It evaluates whether a proposed treatment is appropriate for a specific patient by checking their medical records against clinical guidelines and insurance coverage rules. It breaks complex guidelines into simple yes/no criteria, evaluates each one against the patient's data in parallel, and aggregates the results. A confidence score determines whether the case can proceed automatically or needs a human clinician to review it.

Submission Browser Agent

100+ browsers running in parallel on Kubernetes, each one filling out forms and submitting requests on insurance portals. Each insurer has a different website with different forms — the agent knows how to navigate all of them. For portals that ask clinical questions during submission, the agent calls the Medical Reasoning Agent in real-time to generate answers. At full capacity, the system handles thousands of submissions per hour

At Risa, we automate healthcare workflows in oncology end-to-end using AI agents. We built four agents that work together as a DAG , each one handles a different step, then passes its output to the next. No human needed in between. The agents when combined are able to do the work of hundreds of medical workers a day. These agents are deployed across 20+ hospitals and supporting care for more than 100,000 patients.

Here is the overview of our agents:-
Ingestion Agent

Takes messy, unstructured medical documents, faxes, scanned PDFs, clinical notes and turns them into clean, structured data. AI models read each document, extract the key information (patient details, medications, diagnoses), and check against historical records to avoid duplicate work. If a patient has been seen before, the system already knows their history and skips redundant lookups.

EV Agent
Checks whether a patient's insurance is active and what their plan covers. Some insurers offer APIs; others only have web portals. The agent uses whichever method works calling APIs where available, and driving a browser through the portal where not. The result is always the same standardized output: what's covered, what the patient owes, and whether the plan is active.

Medical Reasoning Agent

The clinical brain of the system. It evaluates whether a proposed treatment is appropriate for a specific patient by checking their medical records against clinical guidelines and insurance coverage rules. It breaks complex guidelines into simple yes/no criteria, evaluates each one against the patient's data in parallel, and aggregates the results. A confidence score determines whether the case can proceed automatically or needs a human clinician to review it.

Submission Browser Agent

100+ browsers running in parallel on Kubernetes, each one filling out forms and submitting requests on insurance portals. Each insurer has a different website with different forms — the agent knows how to navigate all of them. For portals that ask clinical questions during submission, the agent calls the Medical Reasoning Agent in real-time to generate answers. At full capacity, the system handles thousands of submissions per hour

Speakers:
- Anant Shankhdhar (Risa Labs): Anant Shankhdhar is an AI researcher and Machine Learning Engineer at Risa Labs whose work focuses on large language models, agentic AI, retrieval-augmented generation (RAG), multimodal AI, and document intelligence, combining research and industry experience from IIT Guwahati, Adobe Research, Walmart Global Tech, and healthcare AI to build production-scale intelligent systems.
