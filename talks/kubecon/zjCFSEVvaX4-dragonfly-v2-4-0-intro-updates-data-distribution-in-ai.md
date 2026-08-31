---
id: zjCFSEVvaX4
title: "Dragonfly V2.4.0 - Intro, Updates, Data Distribution in AI Infrastructure - Wenbo Qi & Chenyu Zhang"
slug: dragonfly-v2-4-0-intro-updates-data-distribution-in-ai
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 28
published_at: 2026-04-09T05:17:25Z
video_id: zjCFSEVvaX4
youtube_url: https://www.youtube.com/watch?v=zjCFSEVvaX4
tags: []
transcript: true
---

# Dragonfly V2.4.0 - Intro, Updates, Data Distribution in AI Infrastructure - Wenbo Qi & Chenyu Zhang

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=zjCFSEVvaX4) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Dragonfly V2.4.0 - Intro, Updates, Data Distribution in AI Infrastructure - Wenbo Qi & Chenyu Zhang, Ant Group

Dragonfly provides efficient, stable, and secure file distribution and image acceleration using P2P technology within cloud-native architectures. This talk will briefly introduce Dragonfly and highlight the features of its latest version. Key updates include enhanced security and new functionalities tailored for more efficient and robust model distribution. We will also demonstrate how Dragonfly preheats and distributes AI models (packaged as OCI Artifacts) to read-only volumes in Kubernetes, enabling faster deployments. Additionally, we will introduce P2P-based state snapshot and restore capabilities in AI agent scenarios.

## Transcript

*2,483 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=0s)** Hello everyone. My name is Wenbo. You can call me Guy Us. I'm the maintainer of the Dragonfly. I hope my introduction can let you know about the current status of the Dragonfly. I hope that developers can be interested in the Dragonfly project. Thank you for joining us. Okay. Dragonfly delivers efficient, stable, and secure data distribution and acceleration powered by P2P technology. It aims to be the best practice and the standard solution in the cloud native architectures. It's designed to improve the performance of the large-scale cluster

**[0:47](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=47s)** delivery across the files, container image, OCI artifacts, AI models, cache, logs. You can see that in the container registry the of the CNCF landscape. There are two graduated projects. One is Harbor as an artifact registry and the other is Dragonfly as an image acceleration and file distribution system. Okay, next let me introduce the Nydus, a subproject of the Dragonfly. It provides a file system on the based on the RAFS format. The most important feature is to make the container image uh downloaded

**[1:36](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=96s)** on demand in the chunk and the chunk level deduplication to reduce the storage and the memory cost. It can reduce the end-to-end code launching of the container image from the minutes to the seconds. Okay, next. Now, Dragonfly folks on the three part. Uh image acceleration, file distribution, and AI infra. In the field of the image acceleration, Dragonfly supports container clients such as the containerd, Docker, CRI-O, or us. It provides the three solutions for the image acceleration. The first solution is to use the

**[2:25](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=145s)** Dragonfly to distribute the image based on the P2P, which is suitable for the large-scale cluster. The second solution is to use the Dragonfly and the Nydus to distribute the accelerated image, which is suitable for the large-scale cluster and the faster container launching. The third solution is to use the Nydus uh to distribute the accelerated image, which is suitable for the faster container launching. In the field of the file distribution, Dragonfly supports the large-scale file distribution and use the P2P to eliminate the impact of the origin bandwidth limitations.

**[3:14](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=194s)** It supports protocols including the HTTP HDFS. It also supports different object storage including the S3, AWS OBS. In the field of the AI infrastructure, Dragonfly supports accelerated the data distribution during the AI training and the AI inference. In the AI inference, Dragonfly supports the model pack to distribute the AI model. It also supports downloading models and this side from the Hugging Face by the Dragonfly's command line. Uh In the future, we will pay more attention in the AI infrastructure because we believe that P2P is the best solution to the

**[4:05](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=245s)** celebrated AI decide and AI models. Next, I will introduce why we use the Dragonfly. For example, uh Kubernetes clusters has a thousand nodes and each node needs to download a file or a image at the same time. For the storage, there are three uh there are a thousand concurrent download requests. When downloading files in the large-scale cluster, the storage bandwidth can easily reach the limitation. This will cause the slower uh image launching container launching and slower file downloads in the cluster.

**[4:51](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=291s)** How to resolve the problem? There are three solutions. The first solution is to increase the bandwidth of the storage, but no matter how to increase the bandwidth of storage as a as a back-end storage, it must have a limitations. The second solution is to use the P2P to use the idle bandwidth of the nodes to eliminate the impact of the storage. This also the best best solution in the large large-scale cluster. The third solution is to reduce the download file size. We can remove the duplication during building and download on demand during

**[5:42](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=342s)** the running to reduce the file size. Nydus deduplicates the files and downloads on demand. So, Dragonfly includes the second solution and the third solution. Now, let me walk you through the three core download modes in our content distribution system. First, download from origin. There is no cache in the cluster. One a peer needs to download a file. It first register with the scheduler and then downloads the file directly from the origin. This is the most basic whole download mode.

**[6:29](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=389s)** Second, download from the remote peer. There are some peers in the cluster and have the file cache. One a peer needs to download the file. It first register with the scheduler and then the scheduler will select some candidate parents. Then the peer will download the file from its parent by the piece level. Download from the local peer. The peer has the file in the local disk. One a peer needs to download the file. It will return the file directly from the local disk without registering with the scheduler. Okay, next I will introduce the exciting updates of the Dragonfly in the 2.4

**[7:23](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=443s)** release. First, Dragonfly provided a new attacks transfer protocol based on the TLV, type, length, and value to improve the download performance. Use the TLV format as a lightweight protocol to replace the GRPC for data transfer between peers. We can see that use the TCP based Vortex, the large file download time is reduced by half compared to the GRPC. Using the quick based Vortex, the large file download time is reduced 40% compared to the GRPC.

**[8:13](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=493s)** Okay, next I will introduce the scheduling. There are two stage to select the candidate parents for downloading a file. The scheduler under the peer. In In the scheduler, Dragonfly add a load quality feature to score the parent. Load quality is scored based on the three features. Peak bandwidth usage, bandwidth duration radio, and concurrent efficiency. The peer will connect when the scheduler selected the candidate parents. So, the peer will connect to the multiple parents and sync each parent's bandwidth

**[9:03](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=543s)** usage. When downloading a piece, the peer will select the best parent based on the bandwidth usage. This solution can resolve the problem of multiple peers downloading from a single peer and reduce the risk of the overloading any single peer. Okay. When multiple peers are downloading at the same time, we have optimized the the process to advertise the issue of the root overloading. For example, with a single seed peer, uh the peer A will download the piece

**[9:52](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=592s)** one, piece three, and the piece five from the seed peer. Well, the peer B will downloads the piece two, piece four, and the piece six. So, the peer A and the peer B then exchange the piece they are missing. This prevents uh both of peers down to download all piece from the seed at the same time. In the two download decks, uh this optimization resolved the root peer overloading and reduced the long-tail downloading. By selecting candidate parents in the two stage uh scheduler and the peer, uh we can improve the bandwidth usage

**[10:41](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=641s)** and the download performance. For large files, preheating them into peers is also a solution for reducing the download time. Therefore, we have upgraded the preheating in the Dragonfly. Now, users can preheat the files flexible on the IP, percentage, and the counts, which may which makes preheating more efficient. In addition, we added the rate limit for the preheating task to avoid many peers downloading from the origin at the same time and the causing the overload on the origin.

**[11:30](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=690s)** Okay, client now supports calculating task ID directly based on the hash of the image blobs instead of the using the downloaded URL. This This enhancement prevents multiple downloads when the same blob is used by different repo. Second, Dragonfly downloads by the piece. It will cause multiple the redirect response. So, we support for catching the HTTP redirect response. Finally, please note that the Go Go lang client has been deprecated and

**[12:18](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=738s)** replaced by the Rust client. Okay, next part I will introduce how to manager and distribute the AI model within the Kubernetes. AI models service as the artifact across both training and inference. This part focus on the inference. Addressing how to manager and distribute this model within the Kubernetes. AI models have four key features. Large scale. Model weights has grown from the hundreds of the megabytes to the hundreds of gigabytes, even terabytes. Posing

**[13:06](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=786s)** challenges for the model storage and transfer. Immutability. A base model only base model used for the inference is a read-only versioned artifact. Like a container image, It follows uh, uh, build once and distribute everywhere. Lack of the model management standard. The community is focused on the speed of the distribution while ignoring the critical governance, including the versioning, metadata schema, and life cycle management. And the cloud cloud native gap.

**[13:55](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=835s)** AI infrastructure is based on the cloud native infrastructure. Yet, many companies depend on the custom solution uh, based on the object storage or the Git LFS for the model management. This leads uh, to non-standardized uh, artifact management and uh, lack of the cloud native support. Okay. In the cloud native AI, developers have built it a measure and efficient way for software delivery. First, developers commit the code to a Git repo.

**[14:43](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=883s)** Manage the code changes through the branch and the tags. Second, CI and CD pipeline compare and test packaging the output into an immutable container image. Third, images are stored in the in a container registry. Uh, so uh, supply chain security, access control, and the P2P distribution ensure the safe and uh, fast delivery. Fourth, DevOps engineers use the YAML to define the desired state. The containers life cycle is managed by the Kubernetes. By applying the software delivery and

**[15:37](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=937s)** supply chain to the model life cycle management, we build it a efficient system that resolve the challenge of the managing and distributing AI models in the production. First, developers push the model weights and the model configurations to the Hugging Face Hub, treating it as the Git repo. Second, CI and CD pipeline package the model weights and the model configuration and the model metadata into a immutable model artifact. Third, the model artifact is managed by the by a

**[16:25](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=985s)** artifact registry, reusing the container infrastructure and the tooling. Fourth, engineers use the Kubernetes OCI volumes or a model CSI driver. Models are mounted into the inference container as a volume. In the build stage, we need build the model artifact and the push the model artifact to the registry. Model control is a command tool designed to package the AI models into OCI artifact. In the management stage, Harbor service as the artifact registry for the AI

**[17:15](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1035s)** models, providing a platform for storing, versioning, and distributing models. Harbor manager AI models with the six key feature, versioning. Model are OCI artifact with the immutable tags and the hash digest. Access control. Harbor's RBAC will control who can access and the manager the models. Third, life cycle management. Tag policy will clean the inactive versions and the locking the active versions. Supply chain security, integration with the Cosign notation for

**[18:05](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1085s)** generating the signature. Replication. It will sync AI models between and the central and edge registry. Auditing, logging of all artifact operations, pull, push, and delete for security and traceability. In the delivery stage, we use Dragonfly for the P2P distribution. This solution has been proven in the high-performance AI clusters. It will use the 80% of each node's idle bandwidth and improving the model department efficient.

**[18:54](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1134s)** For latency-sensitive inference service, Harbor will trigger the Dragonfly to preheat the preheat and the cache the model in the node before service scale scaling. When the inference engine starts uh inference inference engine start up, the model loads from the local. The engine runs as a container. Well, the model is mounted as a volume. This native solution enables multiple pods on the same node to share and reuse the model. And it also used the preheating and P2P

**[19:44](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1184s)** to reduce the latency of the pooling large model weights. And native support for the mounting OCI artifact as volume by the CRIO and CRI-O community. This feature was introduced as the alpha in the Kubernetes 1.31. And promote promote to beta in the Kubernetes 1.33. Uh for compatibility with the Kubernetes older version, we offer the model CSI driver to mount and deploy models as a

**[20:35](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1235s)** volumes. In the future, we will continue to optimize management and distribution of the AI models in the Kubernetes include five key points. Uh enhance the preheating. Allow models to be preheated to the specified nodes and the searching cache distribution for the model aware scheduling. And Dragonfly RDMA acceleration enable Dragonfly to use the Rocky or the InfiniBand to improve the speed of the distribution. Lazy loading implement on-demand

**[21:24](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1284s)** downloading of the model weights to reduce startup latency. Connectivity optimization enhance the OCI volumes implementation to reduce the decompression overhead for the large layer. Model security scanning implement deep scanning feature designed for the AI model weights. Okay, next I will show the demo. First we find the model in the Hugging Face. And clone the model.

**[22:27](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1347s)** You can see the model weights and the model configuration is in my disk. Next, I will use the model control to generate the model file. Model file just like the Docker file. You can see the model file's content. This will what I This This will show the models annotation. And use the model control logging the Harbor.

**[23:17](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1397s)** And build the model into the OCI artifact. Okay, next push the uh model to the Harbor. Next, I will log in the Harbor console. I have filed the

**[24:08](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1448s)** model and different version. Uh Harbor will display the models tag, annotations, and summary. Licenses and files. Okay, we can use the members to provide the access control. And created the JumpFlight P2P provider

**[24:58](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1498s)** to preheat the model into the node. You can select the scope. And the policy will remove the deleted old version to save the space. And the audit logging will record the operations. Okay, next I will deploy a VLM inference. You can see the pod YAML.

**[25:47](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1547s)** And the volumes is the model. And the And the container image is the VLM. Okay, apply the YAML. You can see the pod is running. The container runtime will download the image and the model artifact. And this in this demo, we use the CRIO. Wait for the pod already.

**[27:07](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1627s)** >> Okay, the pod is ready. I will enter the inference pod. You can see the model artifact has been mounted into the inference pod. I think this solution separate separate the model from the engine. The model is the volume and the engine is the container image. Okay. Hey, that's all. If you are interested in the Dragonfly or AI model management and distribution,

**[27:57](https://www.youtube.com/watch?v=zjCFSEVvaX4&t=1677s)** please discuss with us in the project community. Okay? Thank you.
