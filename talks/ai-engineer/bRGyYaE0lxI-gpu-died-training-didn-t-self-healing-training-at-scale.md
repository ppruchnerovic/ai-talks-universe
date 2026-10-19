---
id: bRGyYaE0lxI
title: "GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe"
slug: gpu-died-training-didn-t-self-healing-training-at-scale
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-03T21:00:39Z
video_id: bRGyYaE0lxI
url: https://www.youtube.com/watch?v=bRGyYaE0lxI
youtube_url: https://www.youtube.com/watch?v=bRGyYaE0lxI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "fault tolerant training", "GPU failures", "distributed training", "Slurm", "Kubernetes", "Slurm on Kubernetes", "Slinky", "PyTorch", "checkpointing", "GPU cluster", "AI infrastructure", "MLOps", "Crusoe", "Crusoe Cloud", "AI Engineer"]
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: true
---

# GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#fault tolerant training` `#GPU failures` `#distributed training` `#Slurm` `#Kubernetes` `#Slurm on Kubernetes` `#Slinky` `#PyTorch` `#checkpointing` `#GPU cluster` `#AI infrastructure` `#MLOps` `#Crusoe` `#Crusoe Cloud` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=bRGyYaE0lxI) · [Conference site](https://www.ai.engineer/)

## Description

Across thousands of GPUs, hardware failures are guaranteed. Fixing them by hand at 3 a.m. doesn't scale.

Connor Guerrero, Young Jeong and Nikhil Gupta from Crusoe explain why they built Managed Slurm on top of Kubernetes. Slurm gives researchers gang scheduling, topology awareness and familiar sbatch workflows, but falls short on dynamic resources, node health and observability. Kubernetes fills those gaps without either team changing how it works. They walk through AutoClusters' fully automatic remediation of an XID 79 GPU failure, then demo killing a GPU mid-training and resuming from checkpoint in under 15 minutes with no human action.

In this talk:
• Where traditional Slurm excels for training and where it falls short
• Why one stack beats separate Slurm and Kubernetes infrastructure
• The automatic remediation flow: notify, drain, replace, requeue, resume
• Sharing GPUs between training and inference as demand shifts

SPEAKERS
Connor Guerrero, Sr. Developer Relations Manager, Crusoe

Young Jeong, Staff Solutions Engineer, Crusoe

Nikhil Gupta, Senior Software Engineer, Managed Orchestration, Crusoe

LINKS
Crusoe: https://www.crusoe.ai/
Managed Slurm docs: https://docs.crusoecloud.com/orchestration/slurm/overview/index.html
AutoClusters docs: https://docs.crusoecloud.com/orchestration/cmk/autoclusters
Self-healing PyTorch training (blog): https://www.crusoe.ai/resources/blog/self-healing-distributed-pytorch-training-with-slurm-on-crusoe-managed-kubernetes
Slinky (Slurm on Kubernetes): https://github.com/SlinkyProject/slurm-operator

CHAPTERS
0:00 Intro
0:12 GPU failures are inevitable
0:56 What Crusoe Cloud is
1:56 Why this architecture
2:13 Where Slurm excels
3:31 Where Slurm falls short
4:21 Node health checks
5:04 Observability gaps
5:51 Why Kubernetes
6:45 Two stacks, double the burden
7:35 Managed Slurm on Kubernetes
8:09 What researchers and platform teams see
8:58 Sharing GPUs between training and inference
9:43 AutoClusters: automatic remediation
10:03 What happens on an XID 79 error
11:27 Demo: a GPU fails mid-training
12:56 Back to training in under 15 minutes
13:16 One-click Slurm
14:01 Recap
15:55 Design for failure

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,509 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=1s)** [music] All right. Hello everyone. Uh, my name is Connor. I'm a developer advocate at Crusoe and I'm joined by my colleagues Nikil and Young. And we're going to be talking today about the infrastructure we've built at Crusoe and how it handles critical hardware errors. And so our customers when they're running extremely largecale training workloads across thousands of GPUs, GPU failures are inevitable. And so at scale, manual remediation is completely unsustainable. And so what we'll cover today is how by using both Slurm and Kubernetes, we can provide a robust platform with automated remediation that maintains ease of use

**[0:50](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=50s)** for both machine learning engineers running jobs and the platform teams managing the underlying clusters. So to provide a little bit more context on what Cruso cloud is for those of you who haven't heard of us um we provide infrastructure as a service consisting of compute storage networking and the latest gen GPUs from Nvidia and AMD but the focus of this talk will be on the tooling that we've built on top of that to orchestrate these large fleets of GPUs including our managed Kubernetes service called CMK and our manage slurm service which is built on top of CMK and built off of Slinky which is SCADMD's official open source project for running slurm on top of Kubernetes and this allows us to get the high performance

**[1:39](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=99s)** job scheduling of slurm with the infrastructure resilience features and observability of Kubernetes including one of the systems we've developed called autoclusters which is our system for automatically detecting and replacing failed GPU nodes when a GPU failure has been detected. And so to explain how and why we landed on this architecture, it's helpful to understand where traditional slurm both excels and falls short, which Young will get into now. >> Thanks, Connor. Um, traditionally, I mean, looking at it from the tra traditional perspective, >> sorry, can can you hear me now? Okay, cool. I I'll just do it like this. But basically, traditionally, slurm was

**[2:27](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=147s)** built slurm was built by the researchers for the researchers, universities, labs over 20 years ago. Uh built for high performance computing uh which as we've observed with our customers and others that are using slurm today translates very well to modern AI specifically around training workloads. this idea that when you're running a multi-node training job, you need this idea of tight collective communication across the ranks that that you're using. Uh including, you know, specific network built for training workloads today. Um concepts like gang scheduling, topology awareness, uh prologue and epilog for cluster validations. These are all the features that are readily available with

**[3:15](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=195s)** slurm today that helps researchers run their jobs. Uh essentially running their jobs with tools that are already familiar to them. Scripts, especi cluster today. Now, where we feel like this is a bit of a shortcoming or short falls a little bit short around the modern training is the things that you see on the screen right now. Um AI training workloads today are very dynamic and it doesn't just include training. Uh there's a lot of other aspects that your AI labs and other companies are running as part of your your AI workloads including training post-training eval inferences some of which may or may not even land on your slurm cluster today. But because of of what we've observed as as a GPU

**[4:06](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=246s)** capacity constraints and other things kind of limits you to how you need to be able to be more dynamic around the resources that you have. Uh slurm traditionally is pretty static and it's partitioning and other other uh functionalities. The other thing I want to mention is this idea of health checks and maintaining your nodes. Uh you know you can make sure your nodes are healthy or not healthy. GPUs do fail, how do you manage that? Uh, SlurpM obviously has features around it to be able to, you know, reue the jobs, uh, detect bad nodes, uh, using things like prologue and other open source tools that are now available to be able to do this. It just adds an operational burden, uh, that we've seen from customers today. you know, this idea that you have to

**[4:55](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=295s)** detect if nodes are bad, you have to drain the nodes when they're bad, you have to kind of work around that. That could either be manual or you need some sort of an automation or scripting to be able to do all of this. And the last thing is observability. Um, you know, jobs can fail. Jobs could also come with degraded performances for any number of reasons. I mean, GPU failure is just one of them. there's other things like network flaps and other things within your your switches that may be causing degraded or failed performance. Uh slurm knows when a job fails. It doesn't necessarily be able to tell you everything about why it failed. And that's where the observability comes into key uh key play. So all of this kind of encompasses the reason why we we built this product that Nikil is going to go over and sort of describe some of the specifics around manage slur.

**[5:49](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=349s)** Um all right uh thanks young. So yeah, I'm going to be talking about our Cruso manage slurm product and uh like like we've mentioned before um there's a lot of benefits uh that slurm can bring to the uh training teams and uh researchers that are building the next best models but there are some issues with you know setting up slurm managing it keeping it reliable uh and on the other hand you have kubernetes which is the OS of the cloud It's widespread use and familiarity. It's a very mature ecosystem with lots of tools, extensions, and plugins for whatever you need to add, whether it be observability networking security. It helps uh maintain services with

**[6:39](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=399s)** there, you know, built-in safe healing, uh load balancing and autoscaling that keeps everything running smoothly. And so we often see that uh customers will uh come with us starting with say inference running on Kubernetes and then they want to expand to training uh or vice versa. And so maybe a Kubernetes familiar team struggles with deploying and managing a slurm cluster. Um or uh the incoming slurm native training team is unfamiliar with the existing Kubernetes frameworks uh and adds you know additional friction that just slows down your team and with you know how fast everyone's trying to get to uh the next best model and next best product. um teams get set up with the tools they're familiar with and you end up

**[7:26](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=446s)** with two separate infrastructure stacks which has its own host of extra operational burdens uh and extra costs. So we decided to build out our Cruso managed slurm uh on top of Kubernetes. So we have our Cruso slurm operator uh which coordinates with our Cruso managed Kubernetes platform and the broader Cruso cloud. So including storage, networking etc. And uh cso manages uh slurm users, slurm partitions, configurations and storage. So you don't have to do it peacemeal. You just you know one one command you create your slurm cluster and there it is existing in your kubernetes cluster. So the benefit is for the slurm users um it's just another slurm cluster. They just need uh an IP address they can SSH with

**[8:14](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=494s)** their uh user and now to them it's a slurm cluster with all the bells and whistles that they need. They don't even need to know that Kubernetes is running underneath. For your platform team and your uh infrastructure team, uh the benefit is slurm is now just another service that plugs into your existing infrastructure. You don't need to set up an entirely new infrastructure stack, new observability tools, new you know on call teams, new runbooks, nothing like that. It's all built into the same thing. It runs alongside all your other services and um resources in slurps. any jobs make use of the uh built-in topology aware scheduling um and the platform team just sees it as another service um and now since all your GPUs and hardware are in one cluster they can move around seamlessly uh it enables uh

**[9:03](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=543s)** more interesting uh tooling and dynamic availability like when you need to burst your uh inference service when you're reaching uh high uh users high number of users you can take away some some of your or even reallocate some of your hardware from your training cluster to your inference service or vice versa. You know, when your user uh load goes down, you have all these GPUs sitting idle. That's the perfect time to up your training job or do a a larger hero run across more GPUs. Um this is something that's only possible when you have everything in a single uh infrastructure stack like uh cru managed slurm. Um an additional benefit is uh now crucial managetorm can make use of our autoclusters product which is our auto remediation for additional hardware

**[9:51](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=591s)** errors. So Connor is uh going to walk through that and show a demo of uh of how that works. So this is an overview of what exactly happens when autoclusters detects a critical hardware error. in this case an XID79 error where one of the GPUs is completely unusable. And so the first thing that happens is that the user is notified although there's no action required from them. Then the slurm operator sets that that specific node to down and cancels any running jobs. There's then a uh the process re receives a sig term signal before being terminated and you have up to two minutes to handle that sig term to either save your checkpoints or flush

**[10:38](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=638s)** your logs before that node is eventually replaced. The cancel job is automatically reued and then autoclusters start. So first it verifies that no pods on the node have a label that disables automatic replacement. Assuming that node can be replaced, the Kubernetes node is then cordoned and drained. And then the unhealthy node is removed from the node pool and replaced with a new healthy node from spare capacity. And then a record of the alert and the remediation is logged for the user's reference. Uh but there's still no action required from them. And then once that healthy node comes back online, then the slurm job starts. Your application code runs to load your model and load your checkpoint and resume

**[11:27](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=687s)** training. And so here's what that looks like um in a demo. And so here on the left, I'm just using sbatch to launch a PyTorch training script. On the right is the Cruso cloud console where I have a GPU node pool of two A100 nodes. And I'm going to launch this as normal. Um, and then what I'm going to do is run a script in to tell our backend internal monitoring system that there's been an XID79 error on one of the GPUs. And this will trigger autoclusters. And so we can see immediately the GPU utilization drops. And so we know that that that GPU has gone offline and autocluster's node

**[12:16](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=736s)** replacement starts immediately. And the full process from detecting a critical hardware error to getting a healthy node back into the node pool takes roughly five minutes with autoclusters. The rest of the time is mainly application level code. And so in this example, it's a little under 15 minutes um from end to end. And here I'm just showing some of the alerts that uh the user receives when there's a critical hardware error like this. So as you'll see um there's no action required from the user. The slurm job will restart. It'll load the checkpoint and continue training where it left off. And we can see the GPU utilization returns back to normal. And the total downtime is less than 15 minutes. And this is um much better than having an

**[13:06](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=786s)** engineer have to log on in the middle of the night and spend hours debugging something. All of this is handled automatically on our platform. Now, historically, creating this type of environment has been challenging to merge both Slurm and Kubernetes. And so we're really excited to announce what we call one-click slurm where everything that we've talked about in this presentation, this entire environment can be provisioned with with just a single command. And so this one command includes provisioning the underlying Kubernetes cluster, the slurm controller, login nodes and storage. And then adding a GPU node pool is only one command beyond that. And so this means that engineers can simply SSH in and start running jobs

**[13:55](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=835s)** immediately and autoclusters is enabled by default. So wrapping up what we covered um starting with the limitations of traditional slurm it gives you the high performance job scheduling but not the automated the automated healing that modern AI infrastructure requires. And so by building slurm on top of Kubernetes, we can enable these advanced advanced features without having either team change uh their workflows. Then we covered the full node remediation flow from an error being detected to the slurm job resuming and the checkpoint and the training resuming. And so the key takeaways here first is that traditionally slurm and the infrastructure that it runs on are two separate systems.

**[14:43](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=883s)** But together with Kubernetes, both systems stay in sync and so a failed GPU node can get cord in automatically and that signal will propagate directly to the slurm operator. Also, like I mentioned earlier, neither the platform teams nor the machine learning teams have to change their workloads. Researchers can still use the same commands to launch slurm. And although Kubernetes is running underneath, researchers never have to SSH into a pod or worry about containers, but the Kubernetes team still get access to the same level of telemetry and observability that they're used to. And then lastly, like Nicole mentioned, the GPU nodes are Kubernetes nodes

**[15:32](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=932s)** first. And that means that slurm is just a workload running on top. And when a slurm job finishes, those GPU nodes don't have to sit idle waiting for another job. You can schedule inference pods on those immediately through Kubernetes because from the platform's perspective, they're still just nodes in a pool. And so the core idea here is that failures are inevitable. Um and so in today's AI landscape, the architecture of infrastructure should be designed in a way so that when there is a critical error, all the right actions are handled autonomously and engineers can focus on building their application and not worrying about their infrastructure. So hopefully this was an informative

**[16:22](https://www.youtube.com/watch?v=bRGyYaE0lxI&t=982s)** talk. Um, if you have any questions, feel free to um, connect with us at booth ug12 or on social at crusadev. And uh, thank you for listening and feel free to ask any questions. Thanks.
