---
id: tCeWbdekqJE
title: "Breaking the Monolith: Decomposing and Governing Giant LLM Jobs Across Clusters - Kevin Wang, Huawei"
slug: breaking-the-monolith-decomposing-and-governing-giant-llm
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "General software conferences"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Kevin Wang"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 24
published_at: 2026-04-09T05:29:40Z
video_id: tCeWbdekqJE
url: https://www.youtube.com/watch?v=tCeWbdekqJE
youtube_url: https://www.youtube.com/watch?v=tCeWbdekqJE
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Breaking the Monolith: Decomposing and Governing Giant LLM Jobs Across Clusters - Kevin Wang, Huawei

**Kevin Wang**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `24 min`

[Watch the recording](https://www.youtube.com/watch?v=tCeWbdekqJE) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Breaking the Monolith: Decomposing and Governing Giant LLM Jobs Across Clusters - Kevin Wang, Huawei

Multi-cluster architecture is now a common choice for enterprise AI infrastructure, enabling unified resource management, flexible integration of multi-cloud and data center GPUs, and abstraction of hardware differences for simplified scheduling.

Traditionally, AI jobs were scheduled as a whole to a member cluster to ensure performance consistency, but this limited flexibility and resource utilization. In practice, splitting jobs across clusters becomes necessary for large-scale LLM training exceeding single-cluster capacity or aggregating idle resources from multiple clusters.

This session introduces how Volcano Global and Karmada enable adaptive cross-cluster scheduling for LLM jobs:
1. a universal global scheduling control plane
2. a higher-level job abstraction for intelligent decomposition of large AI jobs across clusters
3. a centralized global queue and priority mechanism to ensure fair and orderly resource allocation, preventing large tasks from overwhelming the shared pool

## Transcript

*3,109 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=tCeWbdekqJE&t=0s)** Hello everyone. Uh thank you for attending the uh the talk. Uh I'm Kevin Juan. I have been working in the community for a very long time and uh I'm serving on the technical oversight committee as well as multiple uh projects. Uh today my talk is uh uh today my talk is more about uh my maintainer role uh working on uh some of the project. Yeah. So um okay let's just uh uh dive right in. So um we already know that kind of the multicluster has been default by a lot of enterprise AI. Um the benefits are kind of very clear, very straightforward. We can get uh

**[0:51](https://www.youtube.com/watch?v=tCeWbdekqJE&t=51s)** unified management crosscloud GPU resource pooling as well as general resource abstraction to simplify the underlying uh underlying hardware details, right? But um how do we draw the cluster boundaries? Uh typically we define cluster by geography, by capacity or by uh hardware specifications. But uh then comes pro the problem because the AI cluster underlying design involves very fast, right? We have a kind of multiple setup of different AI cluster network with for example in link and also like uh roi thing and it turned out to be um uh independent clusters for different uh AI cluster that is uh set

**[1:41](https://www.youtube.com/watch?v=tCeWbdekqJE&t=101s)** up right but uh that's also kind of uh exposes one of the challenges that the um resource utilization versus the performance or versus the efficiency. Uh traditionally uh we have seen a lot of people they just schedule their uh AI workloads, AI jobs as uh uh monolith, right? Uh one job entirely into a certain cluster to uh get an guarantee uh network uh performance uh with the you know the the location, right? uh but uh it's kind of challenging because you know uh all the AI workloads run dayto day and the resource fragmentation is kind of unavoidable

**[2:30](https://www.youtube.com/watch?v=tCeWbdekqJE&t=150s)** makes the um uh job scheduling and the collocation is kind of uh still very challenging uh uh we have adopted like uh being packing or also like priority preemption uh method trying to improve that But they are not silver bullets, right? So the true cost of running monolithic jobs uh would result in uh massive resource bubbles. So uh we leave the highly expensive uh and you know standard uh capac capacity are sitting in idle because it cannot fit a whole job. That's the the challenge. So uh it's kind of a funny fact that we you know spend massive engineering effort to

**[3:21](https://www.youtube.com/watch?v=tCeWbdekqJE&t=201s)** to build our cluster with some of the boundaries we mentioned above but uh then we spend even more effort trying to you know cross this boundary. So uh uh it's kind of funny uh looking back to uh what we have built in uh and shared with our community previously. Uh this is the um architecture we have shared multiple times uh starting from uh 2019. uh uh the volcano project has continuously u making good progress on uh you know um scheduling managing the uh AI ML workloads in a single cluster scope and it's uh doing better and better and the kamada started uh in 2021 uh to trying to resolve the multicluster

**[4:11](https://www.youtube.com/watch?v=tCeWbdekqJE&t=251s)** resource management uh resource scheduling issue and also provide a a lot of uh good support but there are still uh a lot of more gaps we need to fill. So including like the um global queue management over multicluster architecture and also like the uh fair sharing uh capacity consideration from a a universal uh view right that's why we started the the uh volcano global sub project so during the year of 2024 uh we built the uh the initial versions of uh volcano global on top of kamada to deal with uh the especially the uh pri Q priority uh capacity considerations and also like the fair sharing between uh

**[5:01](https://www.youtube.com/watch?v=tCeWbdekqJE&t=301s)** multi-tenant uh uh use cases and during the year of uh 2025 we improved the commod with a lot of uh advanced uh scheduling feature and also like the fe failover mechanism trying to make the whole stack more mature more stable um I would say that the kind foundation is uh uh ready. Uh the basic resource management is all is uh uh resolved and the the like the task scheduling is working. Uh but there are still are some mi missing pieces like we uh we need a need a kind of uh you know federation native a a api abstraction to bring more flexibility for uh kind of

**[5:50](https://www.youtube.com/watch?v=tCeWbdekqJE&t=350s)** customizing the splitting partition policy of the joint LM workloads especially the training workload right and we also need to uh introduce or or we we need to provide the extensible architecture for uh job uh splitting policy because it's uh very related to the AI researchers work and the different model architecture and also like the different uh data setup uh they uh tend out to be different uh splitting uh strategy also um for the workload scheduling we also need to be more precise on uh evaluating the resource request as well as the the real um cluster status.

**[6:40](https://www.youtube.com/watch?v=tCeWbdekqJE&t=400s)** So this is the question uh how shall we uh really split a giant uh training uh job across different clusters. uh it's it's it's a bit related to more about the AI researches but I will try to uh uh explain it a simple so uh we know that uh like the for the uh the the job uh the AI training parallelism there are typically uh three patterns first is the uh tensor parallelism uh the it splits single layer uh matrix to uh different uh computations and uh uh it demands uh um extreme network bandwidth, right? Because of the law of uh uh physics, the

**[7:32](https://www.youtube.com/watch?v=tCeWbdekqJE&t=452s)** the tensor parallelism must be uh strictly um uh scheduled into a single node or tightly coupled inside a kind of uh super pod or super node with a very uh guaranteed high uh perform and to end hardware high performance. And the second one is the data parallelism right it replicates the uh full model across different data batches. So what the uh problem here um the massive uh gradient uh synchronization is the uh the the key challenge if you try to run like data parallelism across cluster a multicluster network it's it's just too challenging. you need to kind of uh uh

**[8:24](https://www.youtube.com/watch?v=tCeWbdekqJE&t=504s)** improve your underlying network to make it very uh uh good at you know low uh latency and high bandwidth. So uh then it leaves us with our pipeline parallelism. cases. Uh I think currently the the best and the easiest way to start with most of the cases you uh you don't have a very uh fancy multicluster network, right? Uh the the the pipeline uh parallelism splits the model vertically, right? uh layer by layer uh into different uh stages. And the the the brilliant brilliant part is is the boundary because only it only passes a relatively lightweight activations uh and gradients across the network instead

**[9:14](https://www.youtube.com/watch?v=tCeWbdekqJE&t=554s)** of instead of syncing the entire model, right? And what can we even do better? So uh in a lot of uh uh end users use case we have seen that people have different uh AI cluster set work uh setup that means that the the underlying uh performance is different. Um so uh when we trying to uh deal with the uh pipeline parallelism uh one of the uh issue become is that like in this example we uh if we use a traditional approach uh like a symmetric 50/50 split between a B200 cluster in Beijing and an H00 H100 cluster in

**[10:03](https://www.youtube.com/watch?v=tCeWbdekqJE&t=603s)** Shanghai. We hit a massive uh bottleneck, right? We we give them like four uh layers for each uh the B200 tier uh through their um computation uh instantly and then they just sit there. Look at the you know the um red idle bubble. you your you your kind of running faster cluster are uh you know uh literally uh literally uh stalling waiting for the slow cluster to finish their forward and then you know back backward passes you are kind of you know uh burning incredibly incredibly uh expensive uh B200 compute cycles on absolut absolutely nothing right so these are the um resource bubbles we we

**[10:54](https://www.youtube.com/watch?v=tCeWbdekqJE&t=654s)** we we we have to kill we have to optimize. Now uh if we look at the uh uh the the other side the option uh the uh uh semantic uh semantic trick layout uh instead of forcing the equal uh split we can align the uh throughput or or t step uh we can assign like um six layers to the faster uh cluster in Beijing and only two layers to the slower cluster in Shanghai and and then it resulting kind of uh similar um you know uh timeline for each uh step of the micro batch and then you can adopt like the other uh zero bubble approach for

**[11:42](https://www.youtube.com/watch?v=tCeWbdekqJE&t=702s)** the uh optimization. Yeah. So uh this is kind of very uh simplified example how we map this into our uh hyper job uh API. So basically uh uh uh we already have the volcano job which is kind of multi- template job definition for uh training or uh even other type of workloads. Uh but to make our life easier uh so the hyper job design is simply just consists of uh different um uh volcano jobs and we can uh you know with this uh replicated jobs uh failed we can just different uh uh declare two types of uh the expected uh

**[12:34](https://www.youtube.com/watch?v=tCeWbdekqJE&t=754s)** book job you are going to uh ask the system to help you create And the uh volcanic global will also automatically create the propagation policy uh from the commada API to uh help you customize the uh the scheduling uh preference. All right. So um yeah looking into the uh hyper job uh concept we are we are really trying to make a uh federated native uh primitive. So uh it focuses on the uh kind of uh meta level. Like I said uh we uh uh you can define multiple uh type of the expected v volcano job uh with the failed uh

**[13:25](https://www.youtube.com/watch?v=tCeWbdekqJE&t=805s)** replicated jobs and also it allows you to customize uh the the exact underlying uh what kind of jobs you want to uh replicate. And also uh it it has the um splitting uh policy uh failed. Currently we the our implementation is only about the uh predeclared uh static uh supplementing uh uh splitting but uh we are thinking about uh to make it more automated. Yeah. and also uh from the uh from the uh the other side the status aggregation is also uh very important. All right. Um let's move to the the kind of API uh workflow and maybe I try to

**[14:14](https://www.youtube.com/watch?v=tCeWbdekqJE&t=854s)** Oh sorry. Okay. So as you can see that uh for user they just uh uh create the uh hyper job basically with all the uh basic information like what the model and also like the where are the data and uh uh you kind of what image you're using and the uh hyper job controller will uh analysis and uh uh split it into multiple uh volcano jobs and also with the um dedicated uh propagation policy for each volcano job and also uh with the check of underlying uh cluster status they will try to uh add more uh scheduling constraint like that hey make

**[15:04](https://www.youtube.com/watch?v=tCeWbdekqJE&t=904s)** sure this set of volcano jobs uh scheduled to a certain set of clusters. So uh because sometime you your cluster may have different uh network setup uh you have certain set of cluster stay closer with each other that's quite kind of quite easy with uh this uh API and the uh the controller design and also the volcano global actually the controller also uh deal with the uh the global queue management to uh figure out kind of which set of what kind of jobs coming from the uh higher priority user and they will try to schedule them first. Uh this is also very important to you know uh prioritize between different

**[15:52](https://www.youtube.com/watch?v=tCeWbdekqJE&t=952s)** uh workloads and also uh later on we will also introduce the uh gang scheduling between volcano jobs. uh basically it's a to provide a uh uh hyper job level uh GAN scheduling which is very important but also uh a bit challenging for with uh uh existing implementation if we're uh without volcano global project and then the uh command uh will focus on the actual uh resource uh scheduling as well as the uh the the usage estimation. and the monitoring thing. So, uh this is a little bit more details about how we uh make the volcano global collaborate with

**[16:41](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1001s)** uh Kamada pro project. So um this is uh the the idea is kind of uh you you might have seen in the in the uh KQ project which I think it's um it's actually very helpful with this uh multicluster architecture because you know uh the multicluster the crosscluster scheduling is kind of very uh I would say expensive period of uh the whole system. We try to uh we will try to make sure uh it always uh uh you know uh run out uh give the uh exact uh scheduling result in a certain period of time. So any with that any functionality we want to add we need to think about how uh we don't break the

**[17:30](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1050s)** that. So uh what uh volcano global project they do is that with the uh web hook we will basically suspend anything any uh resource bindings created by default and then uh uh with the actual uh uh step of checking uh the uh mapping them into different Q to uh with different priority and also taking the Q capacity into consideration. And then we can just you know uh DQ them right. And the uh uh the commada uhuler will just uh start to schedule every uh resource binding that their uh suspension failed was uh set turned to from true to false.

**[18:24](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1104s)** Okay. Um if you have been you are if you have been uh using uh commada you probably know that actually uh commada is scheduling the workload as a uh as a as a whole thing it's not just uh uh scheduling the pod it's it's a just a different idea different concept compared to the uh kubernetes default scheduler so um one of the challenge is that as workload So especially the like the training job we typically have a different um components right different template with different uh resource requests. So in this example as you can see we have a a pietorch uh with the the master and the worker node with

**[19:13](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1153s)** different uh resource requirement. Uh in the previous uh releases we simply took the larger resource requires the template and it multiplies it with the the total replicas and you can see it's kind of very uh unaccurate. So um so in uh in recent releases we improved that to to uh look into more details and with the commander scheduler actually um collaborating with the uh resource estimator we can um uh find out very detailed result which uh the underlying member cluster can actually run this uh job and how like

**[20:04](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1204s)** how much uh available resources left there. So we with that we can enable like uh even more advanced um scheduling policy like bingpack or we try always try to uh pick the the uh the most idle uh cluster right so um but that's still uh uh that's just the the what we have done uh looking into the future I uh we are we are uh especially for uh like the following uh uh months we will uh prioritize working on the smarter uh splitting policy and uh uh with that we will uh introduce the more underlying uh resource awareness

**[20:54](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1254s)** and the more dynamic waiting for uh for splitting the the uh the workload and also uh uh that's more uh about the uh pipeline parallelism but uh It's also um uh it's also very important to explore even more uh different pattern of uh uh the the uh job job uh basically the job job level topology right so we are uh we have already working on some um the data parallelism optimization to make it able to work over uh crosscluster uh architecture it definitely has a higher requirement on the uh underlying uh network cluster network.

**[21:42](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1302s)** But we can try to optimize the uh the the the uh the the all reduce uh uh operation you know to make it uh do it uh hierarchical or reduce. So we can reduce the uh crosscluster uh data exchange and hopefully uh get a a good uh end to end performance when we are working when we are doing the multicluster training over uh the the the whole architecture and also uh actually uh with kamada we already provided the uh the feature for um scheduling groups. So basically it uh allows you to kind of uh identify

**[22:32](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1352s)** multiple uh set of pre preferences of the uh scheduling. So with this we can uh also integrate with that to provide uh so let the users indicate or let the uh O2 job partitioner to uh provide multiple uh fallback scheduling uh preference combination. So uh with that the system will easier to get just get everything scheduled. Okay. So uh time is short. So uh that's all uh we have today. So we have discussed about the uh the background uh paradigm shift and uh the hybrid job is more uh itself from the API concept uh plan. We we are adding a a higher layer

**[23:24](https://www.youtube.com/watch?v=tCeWbdekqJE&t=1404s)** on top of volcano jobs to reduce the complexity of splitting volcano job. Yeah. With that we we we can easily uh let users identify how you want to split or uh we can uh develop the job auto partitioner to do that. Yeah. And also um uh it's already uh uh released in the community. So you can definitely just check out the uh our GitHub to uh uh to figure out more details and also we we uh uh give some uh practical example to uh how we can uh you know uh use the uh pipeline parallelism to do that. Yeah. And also uh we just covered the uh future
