---
id: Jj8DNLA5hYc
title: "Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simula... Weizhou Lan"
slug: making-topology-aware-scheduling-practical-for-ai-workloads
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 24
published_at: 2026-04-09T05:19:53Z
video_id: Jj8DNLA5hYc
youtube_url: https://www.youtube.com/watch?v=Jj8DNLA5hYc
tags: []
transcript: true
---

# Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simula... Weizhou Lan

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `24 min`

[Watch the recording](https://www.youtube.com/watch?v=Jj8DNLA5hYc) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simulation at Scale - Weizhou Lan, Daocloud

In large-scale AI inference clusters, multi-tenant workloads require both efficient GPU utilization and dynamic RDMA networking. However, heterogeneous GPU interconnect technologies inevitably lead to multi-level network topologies, such as scale-up networks and RDMA spine–leaf structures.
These diverse topologies introduce several challenges: Dynamic topology discovery and health detection across multiple layers, including scale-up, RDMA spine, and RDMA leaf. Second, Topology-aware scheduling that supports priority-based placement and ensures GPUs leverage optimal communication paths.Third, Validation at scale, requiring cost-effective simulation of large, multi-level topologies instead of relying on expensive hardware.
In this talk, it will share practical approach of topology discovery to help Kueue to achieve topology-aware scheduling, and showcase how Kwok simulates thousands of virtual nodes with multi-level topologies, enabling large-scale validation at zero hardware cost.

## Transcript

*2,429 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=0s)** Thank you for joining my session and today I would like to give a talk, give a session about making topology aware scheduling practical for AI workloads from discovery to simulation at scale. Uh, I'm Weijie Lan and senior tech lead at discuss the goes beyond the the scheduler. It includes uh, network topology discovery and cost effective approach for function validations. So, let's get started. As we know in model training scenarios,

**[0:48](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=48s)** uh, networking communication volume is enormous uh, for conventional dense models such as Llama or reduce communication uh, uh, dominate in this pattern. Uh, data exchange uh, typically occurs among the GPUs within each single network area. As a result, most uh, traffic can be handled locally by leaf switches. In contrast, MoE models like Deep Seek routes data to different uh, experts and generates intensive all-to-all communication. This traffic frequently traverses the upper tier switches to reach destination across different areas. Uh, consequently, uh, in a large-scale

**[1:39](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=99s)** cluster, uh, workloads must be placed in an orderly manner according to the topology to avoid network congestion. In inference scenarios, uh, complex RDMA traffic uh, patterns are also unavoidable. Uh typical example is PD disaggregation, a prefilled and the decoder workloads um needed to synchronize KV cache data. Uh so, they must uh be placed uh on topologically close nodes. Uh this shortens the switch uh forwarding path and it helps avoid uh traffic conflicts uh with other jobs. In addition, MOE model uh inference also

**[2:28](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=148s)** involves all-to-all communication, often requiring traffic to traverse multiple layers of network topology. So, related tasks should be placed uh close together uh within the same network domain, and unrelated workloads should be uh spread out to uh minimize path level traffic contention. Network traffic is further challenged by multi-tenant workloads. In a multi-tenant environment, uh nothing is static. Uh we are constantly driven by requirements like canary releases and SLA. To maximize GPU utilization, we cannot

**[3:18](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=198s)** afford to isolate resources for each tenant. Instead, um the cluster is treated as a single fluid pool. Uh workloads from different tenants uh must be free to dynamically uh scale across all nodes. Uh therefore, the flexibility comes with a challenge. If workloads scale without topology awareness, uh network contention becomes inevitable. Uh or it can lead to unfair allocation of network resources uh, within certain parts of the topology among tenants. To adjust this uh, challenges we've discussed the in in the past the slides,

**[4:07](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=247s)** we need the intelligence topologies scheduling. It's no longer enough to uh, just to find the free slots. We must find the right slots. We rely on three core strategies. I think first pass isolation. We ensure that uh, unrelated AI workloads do not uh, contend with each other. If a job A and a job B are independent, their traffic should never collide on the same network path as much as possible. Second affinity. For affinity sensitive workloads uh, like the prefilled and the decode pods, uh, distance is the enemy. We make sure communication paths are as short as possible.

**[4:57](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=297s)** Third, health health uh, awareness. Uh, network can fail and links can degrade. Our system should constantly monitor network health and triggers uh, disaster recovery rescheduling when necessary. Um, um, ultimately we should like to uh, achieve several objectives um, to guarantee job SLAs by minimizing communication latency and to minimize uh, ROI ensuring that our uh, expensive network infrastructure is fully utilized and to ensure network resource uh, fairness among the tenants and the applications.

**[5:48](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=348s)** Uh, but it's the only native Cuba scheduler. Uh in some scenario simple scenarios, someone might consider using node label combined with pulse node affinity to control scheduling. Uh I think unfortunately, um this approach is fundamentally uh is unsuitable for AI workloads. Uh first the reason, manual orchestration overhead. Uh node affinity requires uh us to manually map a physical topology uh to logical labels. This depends heavily on human planning. As the cluster grows, static partitions can cause conflicts between applications and operational costs quickly um um

**[6:37](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=397s)** escalates. So, second reason, topology drift. Labels are static metadata. They have no awareness of dynamic physical infrastructure. If a network cable is removed or a switch is under maintenance, but the label isn't updated in real time, uh the scheduler is operating on a updated map. Third reason, lack of hierarchical global view. Node affinity is essentially set-based matching. It only knows whether a pod belongs to or does not belong to a node. This flat view cannot represent a global network topology or quantify complex architecture. As a result, users often

**[7:27](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=447s)** cannot uh define node affinity rules that truly reflect the physical network. Final reason, gang scheduling. It is a uh all or nothing game. Without the scheduling the entire group simultaneously, we may end up with the with partial allocation. Some resources are locked while others are missing. It leads to resource deadlocks across the cluster. On this slide, we outline the core requirements for topology-aware scheduling. First, hierarchical topology view. The physical network is modeled as hierarchical key tree covering both

**[8:17](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=497s)** scale-up and the scale-out architecture from smallest to largest. The typical hierarchy is node and a super pod and a rack and a spine. Second, hard and soft topology constraints. First, hard constraints are strict. All pods of a job must stay must stay within a specific domain. If there's no sufficient nodes, the scheduling stays pending. Soft constraints are flexible. The scheduler tries to pack pods tightly in a domain like rack and only spills over to adjacent domains if necessary. Third, optimize the switch path for communication. For workloads like

**[9:08](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=548s)** ML inference or PD aggregated tasks, we should place pods close close together within the same domain. In the open source community, Volcano, Kai scheduler, and the queue already support the topology-aware scheduling. On this slide, we have queue and enhancement over the native Kube scheduler. Queue acts as a a gatekeeper for job scheduling. We could use node labels to define a topologies that are deeply replicated lines to the a hierarchical network topology. Each cluster each cluster node is labeled accordingly. So Q can understand the logical topology.

**[9:58](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=598s)** We can specify hard hard or or soft topology constraints using annotation labels in the workload YAML. When a job is submitted, Q first calculates the remaining capacity within the relevant topology domains. If sufficient resources are available, Q injects node selectors or pod affinity to pod templates. This guides the native kube scheduler to make placement with decisions that respect the topology constraints. Now, we are uh let's look at the Volcano. Volcano serves as a replacement for the default

**[10:49](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=649s)** kube scheduler. It builds a logical topology tree using hypernodes CRD. We can manually assign labels to nodes for each switch tier of the topology and uh Volcano will automatically sync these updates to the hypernode instances at periodical intervals. When uh submitting a Volcano job, uh we use the network topology field to specify a topology constraints. I think a key advantage of Volcano is the integration of InfiniBand InfiniBand topology discovery. Uh Volcano can interface directly with

**[11:39](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=699s)** the InfiniBand UFM to automatically pull the network topology. This eliminate This elim- elim- um eliminates the manual effort of maintaining node labels. On this slide, we introduce CAR scheduler developed by NVIDIA. Uh it's a a replacement for the default Kube scheduler. CAR scheduler use a topology CRD to understand how a network is uh structured. Applications can define topology constraints either in pod group CRD or directly through pod annotations. These constraints can be specified as

**[12:30](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=750s)** required replacement or preferred replacement. A key feature of CAR scheduler is subgroups. Within a pod group, subgroup allow multiple sets of pods to have their own the independent topology constraints while also enabling a group-wide constraints across all pods. This ensures that affinity-sensitive workloads are placed uh uh close together. Uh it is especially suitable for a pre-fuel and the decoder workloads in PD um disaggregation. So, let's look uh let's look at the list uh typical topology example that

**[13:18](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=798s)** combines with scale-up and scale-out networks. As shown in the diagram, within each GB200, every 72 GPUs are interconnected via NV switch to form a super pod. Nvidia refers to this as multi-node NVLink domain or NVL domain. These super pods are also interconnected through rack and a spine switch, forming a scale-out fabric. So, the topology hierarchy from smallest to largest is node, super pod, rack, and spine. Now, suppose we are deploying a group of

**[14:07](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=847s)** vRAM inference instances. As shown in the YAML on the right of the slide, we can apply a hard topology constraints to ensure that the entire workload stays within a single rack domain regardless of how it scales. And we adopt a bin pack strategy and apply soft topology constraints to keep instances tightly grouped within a few adjacent super pods. This allows communication to fully leverage the performance advantages of of NV switch within the super pod. As a result, all pods are deployed in a structured manner.

**[14:57](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=897s)** So far, we would discuss the advanced schedulers. They are powerful, but they are also one critical dependency is node label for each topology layer. These node labels represent the logical mapping of underlying network topology hierarchy. If the labels are wrong, the scheduling decision will be wrong. Humans cannot reliably integrate complex the network topologies. It is not a reliable to manually label node at scale. That's why we need a topology detector or builder. Think of it as the bridge between your physical network

**[15:45](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=945s)** infrastructure and the Kubernetes. It runs inside the cluster and solves two key problems. First, network auto discovery. It connects directly to external systems such as InfiniBand fabric manager or NVLink manager tools and uh automatically discovers how the network is wired uh from scale-out switches down to scale-up GPU internet connects. It builds an accurate topology view and it tells us uh the position of each node within the uh different network hierarchy levels. Second,

**[16:32](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=992s)** uh network health awareness. It is not enough to know a link exists. We need to know it works. If a cable is uh degraded or a switch port fails, the detector should identify it immediately and update node status accordingly so the scheduler can make the right decision. Now, let's look at the uh topology detector solution from NVIDIA network environments. NVIDIA topograph it it automates the entire workflow uh workflow. It supports the full NVIDIA networking stack.

**[17:20](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1040s)** When you're running uh RoCE on Spectrum switches or InfiniBand on Quantum switches or leveraging NVLink switch for scale-up connectivity, it has visibility across all fabrics. It continuously talks to network infrastructure. It builds an accurate topology map and the light it automatically applies multiple topology labels to each node. Each label represents the node's position at each level of the network uh hierarchy like super pod, uh rack, and the spine. Uh because this process is automated and uh synchronized with uh the with the fabric, the labels stay

**[18:12](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1092s)** accurate. So, scheduler like a cast scheduler can immediately uh make right decision of topology aware scheduling. So, what if your network hardware comes comes with vendors other than NVIDIA? In a non-NVIDIA network environments, uh we may need to develop a custom a custom topology builder. For the scale-out network, many problems many modern switches uh run Sonic OS. Uh topology builder can query the switches via GNMI protocol to collect all the network neighbor information. For the scale-up fabric, each GPU vendor

**[19:00](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1140s)** repre- uh provides CLI tools or API to expose domain IDs. By collecting these uh IDs, we can uh determine which GPU are physically interconnected by scale-up network. Therefore, they can build an accurate topology map and apply multiple topology labels to each node for the scheduler. Now, we are facing validation challenge across multiple scenarios. First, scenario for scheduling decision. For instance, after deploying and configuring the scheduler, we need clearly we need a clear visibility into

**[19:51](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1191s)** its scheduling behavior. And second, uh like scenarios for network topology construction. For instance, if we want to develop a custom topology builder, we need an environment for developing and testing. So, we need a a network environment environment with rich and realistic topology layers covering both scale-up and scale-out architectures. However, it may require a dozens of switches or GPU servers. The cost is uh prohibitive prohibitive. So, when it comes to validating the

**[20:41](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1241s)** schedulers like Kai scheduler, we can how we can access a GPU cluster with a multi multi-layer network topology. My answer is It is It mean means Kubernetes without the Kubelet. Uh functionally, simulates the behavior of the Kubelet. It allows developers to generate thousands of virtual nodes inside a kind cluster within seconds. These virtual nodes can be configured with arbitrary resource specifications such as GPUs or memory regardless of the actual actual host

**[21:30](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1290s)** hardware. When a pod is scheduled to a node immediately updates the pod status to running. But no actual containers are started. The mechanism operates entirely at the control plane level. Uh with cap at least with this cap capability, we can label the virtual nodes with topology tire attributes such as spine or rack. So, we we learn deploy kind scheduler in the kind cluster and submit simulated inference workloads to these virtual nodes. Well, at least allows us to accurately verify validate the

**[22:21](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1341s)** scheduling results. When we are developing and testing a custom topology builder for non-Nvidia network environments, the the builder needs to actually communicate with switches at different network layer and construct a network topology. This means we must have real switch available. So, how do we obtain such a Kubernetes cluster? My My practical solution is Nvidia Air. Nvidia Air is a free SaaS platform to simulating network infrastructure of a data center. It allows It allows us to deploy Linux VM and the virtual Ethernet

**[23:10](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1390s)** switches with Sonic OS or Cumulus OS. So, we can build a multi-layer network topology exactly as we desire and deploy Kubernetes directly on top of it. We can deploy our custom topology builder on a cluster. It can communicate with the switch to collect topology information and the generate a hierarchical node labels. In addition, NVIDIA provides APIs to automatically create infrastructure based on user-defined topology configurations. This makes it easy to

**[23:58](https://www.youtube.com/watch?v=Jj8DNLA5hYc&t=1438s)** to build a CI pipelines for automatically testing. Okay. Uh Uh that's all of my presentation and thank you. Any questions?
