---
id: MZFcNuYOch0
title: "Scaling Massive Transformer Training with KubeRay | Capital One | Ray Summit 2026"
slug: scaling-massive-transformer-training-with-kuberay-capital
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: ["Capital One"]
channel: "Anyscale"
duration_min: 16
published_at: 2026-09-17T16:06:15Z
video_id: MZFcNuYOch0
url: https://www.youtube.com/watch?v=MZFcNuYOch0
youtube_url: https://www.youtube.com/watch?v=MZFcNuYOch0
tags: []
topics: []
transcript: true
---

# Scaling Massive Transformer Training with KubeRay | Capital One | Ray Summit 2026

**Capital One**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=MZFcNuYOch0) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

When infrastructure is siloed, I/O overhead can stretch development cycles into days. Capital One processed 3.5TB of data and cut hyperparameter optimization from days to hours, a 16x acceleration in model tuning.

At Ray Summit 2026, Mauilin Patel, Raja Chawat, and Yifei Wang from Capital One showcase how KubeRay on their compute platform bridges the gap between raw data and optimized models with a unified ecosystem of Ray Data, Ray Train, and Ray Tune, enabling users to distribute PyTorch training while eliminating costly I/O bottlenecks. They share platform-level lessons on Kubernetes autoscaling, resource isolation, and memory optimization for large-scale transformer workloads, grounded in real Capital One use cases.

You'll leave with patterns for consolidating fragmented training stacks.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*1,949 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=MZFcNuYOch0&t=6s)** Good afternoon everyone. I hope you all are enjoying the race summit so far. My name is Marin. I'm the managing vice president of product at Capital One and I'm responsible for building their a IML platform product. And together with my colleagues and my team here, we are really thrilled to share with you how we are scaling massive transformer training with the ray platform and specifically the coupube platform. So joining me today on the stage we have the key leaders who actually build the ray platform in capital one Raja Shawat and UI Wing.

**[0:54](https://www.youtube.com/watch?v=MZFcNuYOch0&t=54s)** Together with my colleagues and our team, we are building the most scalable, performant, enterprisegrade a IML platform that powers majority of machine learning and AI models and applications at Capital One driving enormous business impact. So just to give you an outline in next 15 minutes what we are going to cover. So first I'm going to explain to you our AI first approach at Capital One. Then we'll take a deep dive into challenges we faced to in building the a IML platform especially the scalability and performance challenges and then we'll

**[1:43](https://www.youtube.com/watch?v=MZFcNuYOch0&t=103s)** explain why we picked the ray and how it helps us address those scalability challenges. Then we'll take a deep dive into our ray platform focusing on ray data ray tuning and also we'll share with you the astonishing performance results we have seen by adopting ray for many of our training and distributed compute platform and we'll conclude by sharing some of the best some of the best practices in running the ray workload on a scalable platform. So just to give you an a glimpse of Capital One's approach of AI. So Capital One sees itself as an AI first

**[2:34](https://www.youtube.com/watch?v=MZFcNuYOch0&t=154s)** organization and we have invested enormous amount of capital to bring in the top talent and be at the frontier of AI revolution. We have been using machine learning and AI models to power our core business functions ranging from risk mitigation to all the way providing the best possible customer experiences. We have partnered with the leading research universities and top tier universities and programs throughout the United States to lead the frontier of AI. And because of all the investments that capital run has made in AI

**[3:22](https://www.youtube.com/watch?v=MZFcNuYOch0&t=202s)** technology, we are recognized at the forefront of AI revolution within the banking and fintech industry and the best manifestation of that is capital one is ranked number seven in AI patterns within the US and it is astonishing to see a bank leading the chart in terms of AI patterns. And to sustain the momentum behind this innovative platform, we are investing in Ry. And now to walk you through our ray journey, I'll invite Raja Shawat to take us. Thanks Molen.

**[4:13](https://www.youtube.com/watch?v=MZFcNuYOch0&t=253s)** So, as uh Molin walked you through our AI IML vision, u as our a IML teams started building our incredibly complex models, specifically massive sequence models, processing terabytes of data. Our legacy system started to crack under their weight. The scale of our ambitions outpaced the tools that we had. And let's look at like uh what bottlenecks uh we uh faced. Historically our machine learning life cycle, development life cycle was highly fragmented. We had siloed tools for data processing, model training, wall tuning as well as uh model serving. And our users had to manage the this

**[5:02](https://www.youtube.com/watch?v=MZFcNuYOch0&t=302s)** disjointed ecosystem code bases and dependencies at every single step of their machine learning life cycle. And this fragmentation didn't just add any complexity. Uh it also heavily inflated our cost and severely impeded our velocity. We knew we had to consolidate this entire life cycle onto a single unified containerized platform. So when we started uh evaluating our target architecture, we didn't just want a faster engine, we also wanted a better developer experience. And that led us to rail. So first and foremost, Rail provided us a Python native ecosystem that acts as a seamless bridge allowing our data science teams

**[5:50](https://www.youtube.com/watch?v=MZFcNuYOch0&t=350s)** to scale their code from local prototyping to building massive uh transform based models and taking it to a scalable cluster and it completely eliminated the paradigm switches between different model ecosystems. Secondly, it provided us the massive compute and scale that we need at Capital One. Uh we are streaming multi- terabyte data sets directly to hundreds of GPUs and Ray handles that orchestration effortlessly via this unified cube rate system. Most importantly, it gives us like full MLDDLC support and instead of stringing multiple tools, open source tools together ray access as single engine supporting our data injection

**[6:40](https://www.youtube.com/watch?v=MZFcNuYOch0&t=400s)** processing, model training, hyperameter tuning as well as batch or realtime inference. So what brings us uh that brings us to our architectural vision uh our unified cube ecosystem. Now we have a unified programming model that scales our application seamlessly from a prototype on a single node to multi-node GPU cluster running our full scale inference uh as well as training. Uh but the most critical win for our team has been zero infrastructure switching. We don't have to tear down and reprovision our infrastructure when we are shifting through different phases of our life cycle. And because this is fully Kubernetes native uh the Cubray platform

**[7:29](https://www.youtube.com/watch?v=MZFcNuYOch0&t=449s)** handles automated pod scaling management and resource isolation provides native GPU pooling and we achieved this architectural vision. Uh but our real test uh for this platform was our most demanding sequence models. uh that we are building and I'll hand it over to Epha who's going to walk you through the bottlenecks that we faced and what we achieved uh and how we accelerated our ML journey. >> Yeah, thanks Ara. So um to ground our infra infrastructure setup in a real world application at Capital One. So let's look at how we apply like a secret modeling to financial events streams like a risk modeling u powered by the re

**[8:18](https://www.youtube.com/watch?v=MZFcNuYOch0&t=498s)** ecosystem. So with a tabular financial data uh we face three main challenges. So rapidly uh changing uh risk patterns heavily um maintenance for uh handcrafted uh features and irregular timing between events. So traditional methods rely on uh complex uh rolling window aggregations which take a long time to build uh test and deploy. So by adopting transformer encoder um for tabular sequences. So we treat our uh history events as sequence tokens. So instead of manual features so the transformer inest the raw uh attributes directly and learn dynamic events uh trajectories. So also added like a time interval features to capture um the

**[9:07](https://www.youtube.com/watch?v=MZFcNuYOch0&t=547s)** event spacing and also use fusion techniques to blend a customer contest uh uh within uh with uh history uh event histories. So this automated feature uh engineering um speed up iterations and also capture complex temporal signals that traditional method may easily miss. So however uh scaling uh uh sequence transformer models to production uh requires uh processing massive data sets. So in our uh in our case we have to uh stream uh about 3.5 terabytes uh training data side with nearly two billion uh records. So when we tried conventional data loaders we hit a major bottl neck. So um standard like

**[9:56](https://www.youtube.com/watch?v=MZFcNuYOch0&t=596s)** injection cause severe IO delays and also push um huge uh serialized files into node RAM that are repeatedly cause uh automemory crashes. So uh read data really help us to solve this issues. Uh so using uh lazy loaded streaming read data stream micro batches from S3 through uh the real object objective store. um straight uh straight into GPU memory on demand. So because uh training deep sequences model is uh more like a computer bound rather than IO bound. So streaming on demand uh keeps our uh GPU running at full capacity without overloading the host RAM. So this eliminate um uh host memory crashes and also give us uh

**[10:48](https://www.youtube.com/watch?v=MZFcNuYOch0&t=648s)** incredible uh 20 time speed up compared to our old pipelines. So once injection was unblouted um so we needed a distributed training layer uh to seamlessly scale our pytorch across multi-GPU nodes uh cluster. So standard distributed uh data parallel setup often struggles with worker um synchronization and also rigid uh failure recovery. So retraining really help us to solve this uh issues with two uh key features. So first it provides nearly uh zero copy uh sharding directly from R data to uh pettor workers in memory. So removing a civilization overhead and second uh retrain provides manage uh uh worker

**[11:36](https://www.youtube.com/watch?v=MZFcNuYOch0&t=696s)** life cycles. So if a worker power file uh during like a multi-node training run um the ray handles workers rescheduling and also isolated uh retries automatically. So there's no need to tear down the uh and restart the entire um cluster. So together uh these efficiencies uh we gained from infra infrastructure side uh delivered us a uh 1.6 time uh training speed up over uh the venina pettor DDP. So finding the best uh transformer architecture requires uh searching a huge par hyperparameter space including uh uh sequence length uh model dimension attention has uh batch sizes and also uh

**[12:25](https://www.youtube.com/watch?v=MZFcNuYOch0&t=745s)** the weight decay drop off and learning rates. So running manual and sequential trials are used to take us uh days or even weeks. So we integrated a return tone with up to TP sampling and Asia um u early stopping to run up to 200 concurrently. Uh so critical platform feature here is pre-trial pre-trial a pro uh resources isolation. So in large um hyperparameter such a bad configuration can easily spike TPU memory. So by enforcing a hard uh pro uh memory limit on cuber uh so a automemory issues uh in one batch is isolated and also pruned immediately without crashing

**[13:14](https://www.youtube.com/watch?v=MZFcNuYOch0&t=794s)** uh adjacent uh workers. So by piring um asham early pruning with zero uh cluster reprovisioning between training and tuning. So rone gave us a a three time um uh speed up in our toning velocity. So looking at our overall imping so previously our uh model uh suffered u like from fragmented tools. So second data processing run on separate clusters uh requiring four data DOM to S3 before handling off to training. So state boundaries added a heavy uh IO uh overhead also toning was slow and manual and we are constantly facing automemory issues. So with our unified Kubri

**[14:03](https://www.youtube.com/watch?v=MZFcNuYOch0&t=843s)** ecosystem read data retrain and return run all in the uh same exact uh Kubernetes cluster we eliminate uh intermediate data dump and also move smoothly from uh inestion to multiGPU training and distributed toning um without uh tearing down the uh the infrastructure. So operationally um ingesting raw uh event stream directly allow us to replace uh dozens of menu uh feature pipelines and most important most importantly uh unify our stack on the reacelerated our overall model development by four times. So to summarize here are some key lessons uh we learned. So first Kubernetes code start takes three to five minutes per GPU. Uh keep warming

**[14:52](https://www.youtube.com/watch?v=MZFcNuYOch0&t=892s)** start uh so keep warming standby post eliminate a de developer time waiting time and let autoscaling uh schedule instantly. Second always set um uh pre GPU memory uh uh limits uh during hyper searches. So isolation keeps a bad config from crashing uh the shared uh worker pods. And lastly, never try to load a multi terabyte data sets uh into the host RAM. So cap you can cap re objective store memory uh use lazy streaming uh and let the GPU compute uh put the data on demand. Um with that um um uh thanks for um uh joining us today and we can follow uh uh offline if you have any questions. Thank

**[15:40](https://www.youtube.com/watch?v=MZFcNuYOch0&t=940s)** you.
