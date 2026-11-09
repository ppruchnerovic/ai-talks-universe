---
id: Ecv83JrmuqM
title: "Radiological AGI: How Close Are We? - Hélène Philippe - Raidium - dotAI 2026"
slug: radiological-agi-how-close-are-we-helene-philippe-raidium
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: []
channel: "dotconferences"
duration_min: 10
published_at: 2026-09-28T14:00:24Z
video_id: Ecv83JrmuqM
url: https://www.youtube.com/watch?v=Ecv83JrmuqM
youtube_url: https://www.youtube.com/watch?v=Ecv83JrmuqM
tags: []
topics: ["Multimodal, vision, speech & robotics"]
transcript: true
---

# Radiological AGI: How Close Are We? - Hélène Philippe - Raidium - dotAI 2026

**Speaker not identified**

`dotAI` · `dot conferences` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=Ecv83JrmuqM) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Hélène Philippe, Machine Learning Researcher AT Raidium: https://www.dotai.io/

Hélène is a Machine Learning Engineer and PhD student at Raidium, a startup building foundation models for radiology. Her work is translational: she takes these models out of the lab and into the real world, applying them to clinical questions alongside radiologists.

Lightning talk: "Radiological AGI: How Close Are We?"

AI in radiology has split between specialized point-tools that excel at narrow tasks but don't generalize, and vision-language models (VLMs) whose versatility and zero-shot capacity are undermined by hallucinations, imprecise measurements, and poor reproducibility. Our work examines how agentic systems could bridge this gap, pointing toward a path for building autonomous radiological assistants — and toward what real progress on Radiological AGI actually looks like.

## Transcript

*1,333 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=7s)** [music] [music] [music] [applause] >> Good afternoon. Question for you. Have you ever seen what a radiologist work workflow looks like? Let me show you. So here is a patient. This patient has cancer. They did two CT scan, one before the

**[0:57](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=57s)** chemotherapy and one after. The objective for the radiologist is to assess if the treatment is working. So is the health of the patient getting better? And especially, are the tumors shrinking? So what the radiologist will do is that they will scroll in the image. And when they find a lesion, a tumor, they will make sure that they visualize it correctly. And then they will measure it. To do so, you measure the largest diameter. You do that for all the different lesion that you find in the patient. It's up to five lesions per patient. So here is another one in the pancreas. Once again, you measure the diameter. Once you are done on the baseline exam,

**[1:45](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=105s)** so the one before the chemo, you do the same on the same target lesions, but on the follow-up exam. This way, you will be able to compare the size of the diameters in the two exam. Once you are done, the radiologist will write a radiology report. So, overall, it looks like this. And what we are interested in is the findings section. So, the radiologist will write down the measurements we talked about, but also any important information about the health of the patient. So, for instance, the splenic vein is occluded. Everything a radiologist does to have such an output can actually be subdivided into tasks, okay? Radiologist

**[2:34](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=154s)** detect measure compare and characterize. You may have seen some limitations to such a workflow. First, it can be imprecise. Let's take an example. We said that the radiologist measure the diameter for the lesion. But what if the lesion is growing in height? Then the axial diameter is not a good proxy for the size. Additionally, it's quite time-consuming for the radiologist and very fastidious. The video you saw is edited, but in real-life setting, it takes up to 20 minutes per patient for such analysis. And it is getting only worse because there is an increasing demand, so the radiologist shortage is getting more

**[3:22](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=202s)** important every year. So, what can we do to alleviate the radiologist workflow? Well, there are tools that already exist. They can be AI or non-AI, and they are quite precise. The problem is they are too narrow, meaning that they will work on a CT, but not on an MRI. Or it will work on a specific organ, but not on another. And that is a problem because the radiologist cannot afford to open a specific application to make it run a specific tool, and then another one, but all that for a single patient. So, that is not deployable. There is another option that is quite trendy today. It's using vision language

**[4:11](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=251s)** models, VLMs. So, we would just input the image of the patient, and it would output a written radiology report. So, even though it looks great, it's not ready yet. Especially, it suffers from hallucinations. So, the model will completely invent diseases that are not in the input image. So, what can we do? Well, what about agents? We said that radiologist cannot afford to open and fetch different tools. That's exactly what an agent could do. So, this is what we wanted to check. So, we created an agentic pipeline, and we wanted to see, is it able to reproduce a radiology report? So, we conducted a few experiments. We used a dataset named Parrot. It's

**[5:00](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=300s)** thousands of radiology reports, so just text. And we want to reproduce them. So, we would input the agentic pipeline with patient data. So, clinical data, mainly the age and the sex of the patient. Uh exam indication, so why is this patient undergoing such an exam? And prior exam report. We said that we want to compare. So, to be able to compare, you've got to have the previous time point measurements. You you input that to your agentic pipeline. What is important here is just that agents can call different tools listed in a toolbox. What I want you to understand here is that all the tools in the toolbox are mocked. They are simulated. So, let's that the agent call a tool, so it can be detect

**[5:51](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=351s)** lesion or measure tumor diameter. We will not actually make tool run. We will instead pass the ground truth report to extract the answer such a tool would have given. This way we have perfect tools. Why are we doing that? It's just because we want to evaluate the ability of agents to call correct tools. We do not want to evaluate the tools themselves. Saying it differently, we do not want the identity pipeline to be tainted by tools that are not working properly. All right. So, that being said, the identity pipeline produce an AI-generated report with all the different findings it has been able to collect. And now we want to evaluate it.

**[6:40](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=400s)** Is it faithful to the ground truth one? It is actually a complicated task because this is the radiology domain. So, standard NLP metrics do not apply here. So, we had to use a specific evaluation framework that is called So, Rad Match not only gives you an overall score of how faithful your report is, but will also give you insights finding by finding. We'll come back to that that after. So, this is the evaluation setup. So, now we can conduct a few experiments. The experiments are about the size of the toolbox. In a first experiment, we had 1,000 tools in the toolbox. It's not random tools. It's actually the tools

**[7:32](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=452s)** that nowadays a radiologist is allowed to use in clinical practice. And with such tools, we had a Rad Match actionable recall of 17%. That is quite poor. And you may think that is because the toolbox is not big enough. There are not enough tools. And you would be right to think so. As the tech goes on, more and more tools will get to the market. And so hopefully this identic pipeline will yield better results. So this is what we tested. Because we mock our tools, we can actually mock any tools. So we had an infinite tool pipeline that can go for any tool. It yielded a recall of 67%.

**[8:23](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=503s)** That is quite disappointing. We could have thought that with an infinite tool pipeline, we would reach 100% recall. So where is this gap coming from? We'll see that. This is a typical redmatch output. You've got each row is a finding. On the left, it is the findings as they are in the ground truth. And on the right, the findings collected by the identic pipeline. So when it's correct, perfect, nothing to say. Sometimes the finding is only partially correct. I said redmatch gives insights. Here in this case, it says it is partially correct because the location is not proper, but it is only a minor issue for the health of the patient.

**[9:10](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=550s)** All right. And the last finding here was completely missed by the infinite tool pipeline. So what does it says? It says you read infiltration of the collecting system of the lower pole of the kidney. Okay. I guess you agree with me when I say that this is not a standout classification task. It's not a detection task. That's actually characterization. And characterization can be done only with natural language. So what we would need to catch such a finding would be to have something that is able to see and to output natural language. AKA, we need a VLM. So this is why we keep pushing VLMs in order to make them work all together

**[10:00](https://www.youtube.com/watch?v=Ecv83JrmuqM&t=600s)** with tools and agents to truly achieve radiology AGI. Thank you. >> [applause] [music] >> Hey!
