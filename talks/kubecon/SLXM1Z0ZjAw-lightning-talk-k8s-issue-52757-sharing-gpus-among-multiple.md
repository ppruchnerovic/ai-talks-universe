---
id: SLXM1Z0ZjAw
title: "Lightning Talk: K8s Issue #52757: Sharing GPUs Among Multiple Containers - Xiao Zhang, dynamia.ai"
slug: lightning-talk-k8s-issue-52757-sharing-gpus-among-multiple
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "General software conferences"
edition: "Cloud Native AI + Kubeflow Day 2026"
year: 2026
speakers: ["Xiao Zhang"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 10
published_at: 2026-04-13T23:36:44Z
video_id: SLXM1Z0ZjAw
url: https://www.youtube.com/watch?v=SLXM1Z0ZjAw
youtube_url: https://www.youtube.com/watch?v=SLXM1Z0ZjAw
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Lightning Talk: K8s Issue #52757: Sharing GPUs Among Multiple Containers - Xiao Zhang, dynamia.ai

**Xiao Zhang**

`KubeCon + CloudNativeCon` · `Cloud Native AI + Kubeflow Day 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=SLXM1Z0ZjAw) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Lightning Talk: K8s Issue #52757: Sharing GPUs Among Multiple Containers - Xiao Zhang, dynamia.ai

This issue has plagued Kubernetes for nearly 8 years: K8s issue #52757. The challenge of flexibly sharing GPUs across multiple containers is particularly prominent in AI scenarios, where inference tasks are typically short-lived. As a result, resource utilization becomes a critical concern.

In this talk, we will share solutions and practices for implementing GPU sharing in Kubernetes, focusing on two key projects gaining traction recently: Dynamic Resource Allocation (DRA) and the CNCF sandbox project HAMi. The presentation will cover the following topics:
1. Challenges in GPU sharing.
2. Approaches for sharing AI chips beyond NVIDIA GPUs.
3. How sharing technologies integrate with projects like Volcano, Koordinator, and Kueue.

## Transcript

*1,103 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=0s)** Hi everyone, great hair in Amsterdam. I'm Shaang, the founder of Damia. Today I want to talk about the uh sharing GPUs among uh mutable containers. The issue has started in 2017 and took nine years to get a proper answer and also the maintainer of ham and the commander work on the AI info. Okay, let's uh get the issue. In 2017, someone opened the issue. The issue was very simple. Can we sharing a GPU across containers like we do with CPU and memory? The discussing was unfair and it's a timeline. In 2018 Aen uh the

**[0:51](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=51s)** Kubernetes device plug-in was launched by the one GPU cam uh among the uh pure container no GPU sharing but the 29 the community workounds emerged uh and the 2022 the Nvidia ship the MIG and time sl uh the open source uh project H launched and the 2025 the DR was G and the the native GPU sharing fally the this issue reshaped the whole ecosystem the invidia uh and k and the third parties from device plugin and the dr is very interesting so what's the actual problem um why many

**[1:44](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=104s)** people focus the GPU sharing uh this is one number this the 4,000 times the GPU memory footprint across AI workloads uh various maybe over 4,000 times uh let's look guys the uh OCR mode just need the 300 megaby but the midsized large language model maybe need to 20 item the gigabyte and the deep w3 maybe needs over 1,00 uh 300 the gigabyte but look at the cost uh the average GPU utilization in production maybe uh our end user maybe just needs the 28%

**[2:32](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=152s)** uh but the each H100 will cost uh four maybe five dollars per hour whether you use it or not. Yeah. And the hundreds of influence P people like P need just function of GPU but the Kubalis gives them their own GPU. Uh just like uh I order the egg and get the one chicken. The answer is is not bigger hardware we need fraed scheduling functional allocation and the flexible orchestraction. Yeah. Look at the four GPU uh sharing approach available today. None of them is perfect. First of the time slicing the

**[3:23](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=203s)** uh softwarebased high capability but no isolation unstable performance. And the second one is the MPS the concrete execution but also no memory isolation. Maybe the MIG is the better choice. um but only work on the high-end GPU and the partitional are fixed every approach trade-off isolation flexibility and uh hardware requirements no single merant can covers all the workload patterns yeah uh and the kubernetes uh sh uh the dynamic resource allocation maybe uh it's a big step forward for a

**[4:13](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=253s)** flexible scheduling but but there is a key point the scheduling uh got smarter but the functional GPU remains the hardware hardware bound can tell us which GPU is perfect for us but it can splend the GPU into different pieces we need to use something else this is why hi project created H is a software GPU virtualization layer um as the container runtime. It's integrated the ka cost and enforce pure container memory and compute cost and it supports the 1% GPU core and one megabyte of the GPU memory. For example,

**[5:06](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=306s)** uh the two two task uh will occupy the four GPUs without harming it. it will be um deployed for um GPUs occupied but the real utilization just the five f 50% but with hammy it's just uh two GPU is left for the for two task and the the other two GPU is free for another tasks yeah it's work on the all GPU of Invidia. No MIG required, no special hardware slice of GPU in any fractional. It integrated with uh Kubernetes on

**[5:55](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=355s)** device plugin and mutating web hook. Your workload just lead to tells the the hammy the lead and how many GPU how how many persons the GPU core and the GPU memory the hammy will hand the rest. Yeah, we also support the uh DR. Why? Why is that means? H is no longer bound any specific scheduling such as the WO uh coordinator and the K scheduleuler and the other default scheduling. They all work uh they all work out of the box. As you can see, your scheduleuler has the workload placements on the top with a blow as the virtualization layer. Okay. Uh at the same time, hammy doesn't

**[6:47](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=407s)** work alone. It plug into the uh home sense ecosystem. They were ko as the coordinator and gun scheduling and the QS orchestration and the X inference and where RM management model serving the Q provides the job quing. Yeah. Hamster says the analyst provides the unified GPU um management and the GPU sharing uh can support the 10 chips types such as the Nvidia and the AMD and the other chips such as the ascend and the cam breaking and the other chips they can work together a complete ST from job automation to job slicing and to the

**[7:38](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=458s)** mode serving uh but all the open source is yeah all the software is open source yeah this is the hing production uh truly use case uh there are benchmark this are same use case and the same safe IO uh the first case is uh called holding uh they have 1,000 uh 10,000 ports and GPU utilization trapped from the uh third person to uh third 37% uh user harming and the the SF technology and the prep in vetan they have heterogeneous of invidia GPU in different cluster memory crash gun the

**[8:31](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=511s)** 80% of GPU infer is using ham yeah and the uh NIO is the automatic company. The four uh industry and from two countries uh the same results uh hine west out this is our target. Yeah. Improve the GPU utilization reduce the cost. Yeah. Ham is a ham is a open source uh project under the CNF. Uh it's now have uh 3,000 stars and uh 500 contributors from 17 countries and also have 400 adopters from all

**[9:19](https://www.youtube.com/watch?v=SLXM1Z0ZjAw&t=559s)** all over the world uh such as the LinkedIn and SAP and Huawei and other countries. This is our QR code. Maybe uh scan the QR code, start us on GitHub and join the community. If your GPUs are setting idle uh 73%, maybe the hammy can help you. Um the hammy container team will run the Amsterdam all the way found me the CNF project. Uh or just just look at the hammy strikers. Yeah, found me. Yeah. Uh, thank you
