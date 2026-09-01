---
id: 2WZsT-znFTQ
title: "Guardians of the State: An Air-Gapped AI Fortress for Consumer Data — Rachna Srivastava, DFPI"
slug: guardians-of-the-state-an-air-gapped-ai-fortress-for
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rachna Srivastava"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-08-29T00:00:00Z
video_id: 2WZsT-znFTQ
url: https://www.youtube.com/watch?v=2WZsT-znFTQ
youtube_url: https://www.youtube.com/watch?v=2WZsT-znFTQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Guardians of the State: An Air-Gapped AI Fortress for Consumer Data — Rachna Srivastava, DFPI

**Rachna Srivastava**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=2WZsT-znFTQ) · [Conference site](https://www.ai.engineer/)

## Description

The fiber optic cable carrying data into California's financial fraud system has been cut in half. One end sits on the internet with a laser transmitter. The other end, inside the building, has only a receiver. There is no transmitter pointing outward, so data physically cannot leave. Rachna Srivastava's team chose that over a software firewall for a blunt reason: any configuration can be misconfigured, and a misconfigured secure system is an exploited one. Everything her group builds has to survive a defense attorney whose entire job is attacking it, which means every step must be explainable, reproducible and auditable years later.

They did not get there gracefully. The first build was the obvious one, an open model in an isolated environment with guardrails, and it collapsed within two hours. The diagnosis was not a weak model. They had treated it as a magic box rather than a data pipeline, so Kafka took ingestion and replay, Spark took cleaning, and the model was left to reason over data that had already been made sane. Her framing is that most AI data problems are data engineering problems wearing an AI mask. Running one frontier model for every task was making a neurosurgeon take everyone's blood pressure, so a router now sends over 80% of work to the smallest model that can do it, tripling throughput on the same GPUs.

Speaker info:
- https://www.linkedin.com/in/rachana-srivastava-ms-mba-78bab86
- https://dfpi.ca.gov/

Timestamps:
0:00 - When seeing and hearing stopped being proof
2:32 - Building for the courtroom, not the demo
3:44 - Why encryption and private endpoints were not enough
6:08 - Certifications as paper
7:22 - The first build, and two hours to collapse
8:29 - Kafka for spikes, ordering and replay
10:56 - Data engineering problems wearing an AI mask
12:01 - A key bolted to the server rack
13:13 - One frontier model doing every job
14:23 - Routing 80% of work to smaller models
15:38 - Learning without opening a hole
16:53 - A cable cut in half
18:05 - Time travelling to the moment of a decision
20:27 - Trust as a physical property

## Transcript

*2,226 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=1s)** [music] >> By the time this presentation ends, someone, somewhere will make life-altering decisions based on something generated entirely by AI. Last 30 years, digital infrastructure is based on these unwritten rules. If you see a face or you hear a voice, you trust someone behind it. If you see a signature,

**[0:49](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=49s)** you trust someone has approved it. Every business transaction, every government workflow is based on this foundation of trust. So, trust is a invisible layer on top of it all this digital infrastructure based on. But, generative AI trashed it completely. AI agent can clone a voice. Synthetic face can bypass identity check. AI can impersonate people at a speed no criminal organization have been able to do that before. So, in the era of generative AI,

**[1:39](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=99s)** seeing is no longer believing, neither is hearing. The cost of deception is collapsed and the speed of deception is exploded. Hi, my My is Rachna Srivastava. I work for California Department of Financial Protection and Innovation. Our mission is to protect 39 million Californian and their financial identities. Let me tell you what we do. When a massive fraud attack in in the state of California, we identify the fraud, we examine the fraud, and we run enforcement. Let me take you behind the scene what we

**[2:28](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=148s)** actually do. Fraud comes, we investigate the fraud. When the investigation happen, we collect all the evidences for the fraud. When we have all the evidence, we take that evidence to the court. And in the court, the defense attorney has only one job, to attack the system that we have built. So, the question arises, how should we build a system which is credible? What are the attributes we need to have in a system which can appear in the court? And appear in the court means system should be defendable.

**[3:16](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=196s)** Defendable means it should be we should be able to explain the system at every step of the process. We should be able to reproduce the issue at every step of the process. We should be able to audit the issue at every step of the process because everything, every data that we produce, it's going to appear in the court. So, how do you build that kind of system? You Since we deal with financial data, we have to ensure that the data is secure for sure. We have to ensure that the data is evolving and learning. Why? Because the fraud space is changing every day. We have to ensure that the data is

**[4:05](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=245s)** available to be appear in the court and reproducible. So, what I'm going to show you now, the system that we built, and the lessons we have learned the hard way. So, the first and foremost decision that we have taken was to build our solution offline. So, you might be wondering like it's it's extreme. Like, why are you Okay, why do you want to create a solution offline when we have a secure cloud? So, before we show you what we build, let's talk about what do industry do in the normal way.

**[4:54](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=294s)** So, the gold standard of security is encryption. Encryption means you encrypt the data at rest or encrypt the data on the transit. That means the thing is but for machine learning model to work, the data has to be decrypted and available in the plain text in the model memory. And if the data is already decrypted and present in the plain text, it is prone to prompt injection attack. Secondly, let's talk about private endpoint. Private endpoints are actually a isolated environment given to you from your cloud provider.

**[5:43](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=343s)** But cloud providers actually own the on the on the disk. So, the question the thing is that according to the Cloud Act federal government can access your data which is in the cloud and they don't even have to tell you that your data have been accessed. Let's talk about certification. FedRAMP compliant, I also certified SOC 2 compliant. All these compliance are just paper. And we have seen these highly compliant organization

**[6:31](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=391s)** fail over and over again. So, only way you can make your data secure to be available in the court to present as a as a evidence is to build the solution offline. So, like everyone else we thought like what a big deal, let's just download a open-source model, create an isolated environment, spin up some GPU, add some system prompt, and add some guardrails, and done we are running. Push the live data into it. We did the same like everyone else. And the model the system collapsed in 2 hours.

**[7:22](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=442s)** And our first instinct was you know, we took the model free model from online. Model is not good for our use case. But the issue was we were we were treating machine learning model as a magic box instead of as a data pipeline. So, anything that garbage comes into the system, we were expecting the model to clean up and do all the processing. So, to solve this problem, we introduce Kafka for data ingestion, a Spark for data processing, and large language model for reasoning.

**[8:10](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=490s)** Three different tools to solve three different problems. We use Kafka for these three things. First, the data that enter into our system does not come at a consistent speed. When a fraud attack happen, it attack all over the state. So, we get a high spike of traffic into our system. So, we needed a tool that can buffer that traffic so that the downstream component can access the data at a consistent speed. And Kafka did that. Secondly, we wanted all the events that occur in the system to

**[9:00](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=540s)** come and store in a sequential order. When did you open the account? When did the transaction happen? The order of events in the fraud is extremely important. Kafka helped us solve that problem. But the main problem that Kafka helped us solve is reproducibility. In Kafka, it let you move the checkpoint to the point at which the decision was made, and it helped you replay the event. And this replayability of the event is the proof that we present in the courtroom. So, now Kafka did solve our data storage problem.

**[9:49](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=589s)** But, the data that enter into the system is really messy. We get 10 different format of bank statement. We get audio file. We get screenshot, facts statement. And, if you dump all this data to model memory, then no wonder model hallucinate. So, we introduced a Spark because a Spark let us process this data behind the scene in the clusters of CPU instead of working on GPU. And, Spark let it let us clean the data. And, then when we process send the clean data through the model memory,

**[10:37](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=637s)** to our utter surprise, the same model started giving us so good results. It found the connection between the points which we never thought expected. So, we learn our first lesson. The lesson is most of the data problem in AI are data engineering problem wearing AI mask. So, I recommend you to consider using data engineering tool to solve those problems. Now, our model memory is filled with a very condensed clean data. But, then we found our next issue. The issue was

**[11:26](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=686s)** the memory was filled with lot of sensitive information. Your credit card number, your bank account number, your social security number. So, we introduce something called cryptographic vault. Which is basically a SHA-256 cryptographic algorithm with hardware security module. So, in the simple sense, it means that as we get the data into the system, cryptographic vault which convert the data into cryptographic hash. But, the key that is used to do the conversion is physically attached to our server rack. So, if tomorrow somebody is able to get

**[12:17](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=737s)** our data, they have to walk into our office physically, break the server rack, get the key to actually make sense of the data. Then, we learn our second lesson. If the stakes are really high, trust hardware over software. Now, we have a model which is working really well. All the PII is redacted. We thought, let's just run a quick round of load testing and release this product. The problem is in the cloud, the scaling is unlimited. You get a high spike of traffic, it is spins off more server, it's it's

**[13:06](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=786s)** distribute the load to those server, and you are done. But, when you are creating an isolated environment, you have limited GPU, limited compute, limited VRAM. So, we have to step back and figure out what is the actual problem here. The problem was we were using one state of the art machine learning model to do every single processing. The same model was doing the summarization, entity extraction, fraud ring detection. So, we were actually making a neurosurgeon take the blood pressure of every single patient.

**[13:55](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=835s)** To solve this, we introduced triage nurse or semantic router. And the goal of semantic router is as we get the data, it analyzes the data and forward the request to the smallest possible model which is capable of processing that request. And by making this simple architecture change, we found that more than 80% of of our task could be easily done by the smallest, fastest, cheapest model. By not adding any new GPU, we could process three times more

**[14:42](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=882s)** traffic and cost of processing each request reduced to nearly 70%. Now, we have done the unit testing, we have done the load testing, and then we found the hardest problem of all. The problem was we built this highly secure system, but the system was not learning. System did not know what is happening in the threat space. So, the question arises, how do we make our system learn without creating a security hole?

**[15:36](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=936s)** Usually in industry, people solve this problem by configuring software firewall. But any configuration can be misconfigured. And once you have misconfigured, your highly secure system will be highly exploited one. We decided to not trust the configuration, and we took help from physics. We introduce one-way data diode, which is basically a fiber optics cable physically cut into half. The first half of the cable is connected to the internet to receive the data. Second half of the cable is connected to

**[16:24](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=984s)** our solution. First of the half of the cable has laser transmitter, which receives the data from the internet and transmit the data to the second half. >> [snorts] >> Second half has a laser receiver to receive the data from the first half. But there is no laser transmitter from our end to the outside world. So, it is physically im- possible for data to leak from the system. And this is how we ensure 100% guarantee of the security of the system. Data diode solves the problem of

**[17:12](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=1032s)** directionality of the data. But anything enter into the data is is considered to be unsafe till proven. So anything from outside first first lands into quarantine zone. Where we run a spark job that runs a validation on each input data. And when all the validation is successful, then the data goes to the production layer. In the production layer, we also save the data into Apache Iceberg. Apache Iceberg is a time traveled queryable immutable data store.

**[18:02](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=1082s)** We enter the data in this data store because 2 years from now one of our results from our system goes to the court. We cannot present We cannot go to the court and tell them, "You know what? This system is result is produced by AI and we don't know anything about it." At that moment, we travel the Apache Iceberg, go to the point at which the decision was made and get the state of the system at that moment from the database. And that is state of the system appear as a proof in the court. And that is how we build a solution

**[18:53](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=1133s)** which is secure, which is evolving, and which is defensible in the court. This is the whole architecture end to end. If you see this only at the very end of the system, we are when a user logs into the system, they we authorize the user into multi-factor factor authorize authentication and only then the data is reverted. Data is not opened till the very end at the browser where the user is actually evaluating the threat case.

**[19:45](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=1185s)** So, don't look at the solution as a fraud detection solution. This is the architecture of the future. Soon the same architecture will be used to predict the health care, banking e-statements, legal and other domains. In the end, I just want to say one thing. Build solution that can be trusted. And remember, trust is not a policy. Trust is a physical property of the system. You have to build the trust from day one into your hardware, into your physics, into your architecture or it's not there.

**[20:33](https://www.youtube.com/watch?v=2WZsT-znFTQ&t=1233s)** It's that simple. So, years from now nobody will remember the models you trained. Nobody will remember the benchmark you received. People will only remember the solution that you have built can be trusted when it needed the most. Thank you so much. >> [music] >> Mhm.
