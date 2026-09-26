---
id: Xh04f8eAPNc
title: "Accelerating Large Language Models: vLLM on TPUs | Google | Ray Summit 2026"
slug: accelerating-large-language-models-vllm-on-tpus-google-ray
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 18
published_at: 2026-09-17T16:06:58Z
video_id: Xh04f8eAPNc
url: https://www.youtube.com/watch?v=Xh04f8eAPNc
youtube_url: https://www.youtube.com/watch?v=Xh04f8eAPNc
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Accelerating Large Language Models: vLLM on TPUs | Google | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=Xh04f8eAPNc) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Large language models demand significant computational power for inference, and TPUs are becoming a first-class target for serving them.

At Ray Summit 2026, Qi Zhou, Senior Staff Software Engineer at Google, explores the work to leverage Google TPUs with vLLM, orchestrated by Ray. He covers the performance and cost-efficiency benefits of TPU-based LLM serving, key enablers like the TorchTPU backend that brings a native PyTorch experience to TPUs, and insights from optimizing and scaling vLLM deployments.

You'll leave with the architectural approaches, the challenges overcome, and the outlook for high-performance, TPU-accelerated LLM inference with vLLM and Ray.

This session was part of the first vLLM Conference at Ray Summit, hosted by Inferact.

Liked this video? Check out other Ray Summit vLLM session recordings: https://www.youtube.com/playlist?list=PLXMguE8Nc9o4

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,416 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=5s)** Uh hello everyone. This is T from Google and today I'm going to talk about the VLM on TPU. Um and first of all, how many of you have used TPU? Please raise your hand. My my colleagues put please put your hands down please. [laughter] And how many of you found the TPUs easy to use? Good, good, good, good answer. Good answer. Um, I'm hoping the updates I'm bringing today going to make you feel more excited about TPUs. So, I'll talk about the basic TPU architectures and then the history of VM on TPU and then latest technology called torpu and how we use torture to power VM.

**[0:54](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=54s)** So within Google, TPU has a relatively long history and we've been using TPUs for to drive many AI innovations including Gemini, the model development, training and serving and image and video generations and also scientific exploration and discoveries. For example, alpha fold which predicts proteins 3D structures, alpha go zero which rivals the best human players and alpha chip which is used can be used for designing advanced hardwares and in recent years Google has started offering TPUs to external customers on Google cloud platform such that the customers can use TPUs for their own model deployment and development and get efficiency and performance. And many of you probably already

**[1:43](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=103s)** familiar with GPUs and CPUs which are general purpose processors. And TPU is a different type of hardware that is highly optimized for large scale machine learning workloads. And this is a diagram of the V7 TPU architecture. A TPU host connects to TPU chips via PCIe. And the TPU chip consists of one more tensor cores, one more sparse cores and memory units. Each tensor core consists of one or more matrix multiplying units what we called MXUS, a vector unit and a scalar unit. And sparse cores are data data flow processors that accelerate models using sparse operations for example embedding lookups or collective offloading. And TPUs features a multi-ter memory

**[2:33](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=153s)** system including high bandwidth memory HBM for example for um model parameters KV cache activations and also vector memory VM which is a smaller onchip SRAMM with higher bandwidth than HBM. Optimizing the use of VM is crucial to the performance of TPU custom kernels. TPU chips are connected to each other via what we call the interchip interconnect SEI and TPUs V7 chips have a 3D Taurus interconnect topology. This topology allows TPU slices to scale up to 9,216 chips per pod which makes it superior for very large scale machine learning workloads. And here is an example of 64 TPUs arranged as a 4x4x4 Taurus network.

**[3:25](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=205s)** And each TPU addressed by XYZ coordinates and connected to six neighbors along X plus XUS, Y + Y minus, Z plus and Z minus. And because of this topology, users need to sh their workload properly to minimize the communication cost between chips and choose collective properly. The majority of the compute provided by TPU is via the matrix multiply units MXU. And this is probably the most important component that a user new to TPU needs to pay attention to. An MXU is composed of either 256x 256 or 128x 128 multiply accumulators in a systolic array. And data flow is

**[4:14](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=254s)** pipeline in both dimensions. In order to utilize the MXU efficiently, normally we need to make sure that the model dimensions line up with the array or you are paying for the silicon that you aren't using at all. For example, a high dimension of 256 is much more TPU friendly than a high dimension of 64 for the V7 chips. And similarly, model sparity needs to be designed carefully to best leverage the SAI connections. So that is the hardware a compiler scheduled a systolic array that one static align shapes with every decision made before the chip ever sees the program. And next we'll talk about what an inferenc does and the challenges it brings to the TPUs.

**[5:04](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=304s)** On the high level we mainly focus on two frameworks J and PyTorch. And in this talk we'll mostly be focusing on PyTorch. In 2024, we built the first version of VLM TPU using Torch XLA. Um, you may or may not have heard of the name and Torch XLA is being deprecated soon. And in 2025, we introduced another technology called Torch X and also added Jack's native serving to VRM TPU. Same year, a new effort kicked off which is called Torch TPU to provide a native PyTorch experience. Torch XLA, Torch X and Torpio all try to answer the same question. Where does PyTorch stop and where does the compiler XLA begin? So here's the comparison between them

**[5:56](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=356s)** all. Torch XLA uses lazy tensor tracing. It accumulates operations into a graph and users need to define the boundaries explicitly. Nothing runs until you flash it. Similar to all other firsttime attempts, we hit many usability and performance issue with Torch XLA. In order to address these problems and to leverage a mature and powerful Jax ecosystem, later we introduced Torch X which is a PyTorch front end for Jax that translates PyTorch models into Jax. Both Torch X and Jax native serving require users to be familiar with the Jax parameters. for example, Jack Smash, partition spec, Jax array, etc. Everything from the PyTorch ecosystem

**[6:45](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=405s)** that you're already familiar with like Dynamo, torch distributed, torch profiler, etc. has to be reprovided rather than inherited. And if you pay closer attention to the TPO inference repo, you will notice that a lot of the functionalities are rewritten in Jax. So we didn't forget our commitment to make PyTorch native serving a reality. And in December 2025, we started a new effort building VRM on top of torch TPU, the new compiler. And I'll go through the technical details in next slides. Um torch TPU tries to minimize the friction of migrating from PyTor CUDA to TPU. And here's an example, a simple training script. On the left side is

**[7:34](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=454s)** PyTorch CUDA. On the right side is PyTorch with TPU backend. A user only needs to touch three lines. The first change to change the back end from Nikico to TPU for the distributed process group initialization. And the second change to change the device type from CUDA to TPU. And the one last change to change the API from torch.cudaside device to torch.tpuite device. and the rest of the code including the model definition optimizer data loading and distribution and the main training loop remain the same and that is how easy it is to start with torch TPU and here's the table comparing PyTorch to TPU jacks and torch

**[8:23](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=503s)** as you can see to TPPU preserves majority of the PyTorch features and semantics it supports one process per lines both MPMD and SPMD and use of DTensor and FSDP for sharding and remon for orchestration and the main difference between them is custom kernels which inherently tied to the hardware. On TPU we use palace a TPU kernel authoring language and the support for helium is developing in progress. Meanwhile, as you can see, Jags and torch are quite different and the people who are familiar with PyTorch need to ramp up separately. Torpus supports both eager and compound modes and eager mode is something new

**[9:11](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=551s)** because TPU is famous for full graph compilation. Torp eager has multiple modes including strict, debug, defer and fuse. The strict mode dispatches one op at a time plus asynchronous execution. It is similar to the default pietorch on t on on GPU and debug dispatch. Debug mode dispatches one op at a time but with synchronous execution. So is easier for debugging but slower and is similar to CUDA launch blocking plus bump checks. The defer and fuse mode defers and fuses multiple ops into a larger chunk through automated heruristics. So we have the opportunity to run local and global optimizations and as a result this it performance is better than strict eager

**[10:02](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=602s)** for torch TPU's compile mode. We start with dynamo but the back end is XLA not inductor. This is a deliberate reuse decision because XLA is the compiler that every TPU workload at Google already goes through is battle tested and robust. So when you when your torch compile a model, the model is traced by torch dynamo autograd into a FS graph. Tor DPU replaced the graph through its eager aton kernels in defer mode to capture the stable HO graph and the stable HO is passed to XLA for compilation. So there's no separate compile mode lowering is the same 800 kernels that the eager path already uses. while lowering implementation to entry points

**[10:51](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=651s)** so they can drift and all artifacts can be cached to avoid need for recompilation if shapes and keys remain the same. If you are serving with VLM you eventually want the last bit of performance out of the hardware and that usually means custom kernels. On GPU we use CUDA, Cutless, QDSL, Triton and on TPUs we use Palace, Jackson, Native and Helium and Palace is the main one to TPU supports all of them. You will find rack page attention fuse, GDN, MLA and other custom kernels in both TPU inference and VRM tortu repos. The palace kernel is just exported to stable stable ho and registered as a

**[11:40](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=700s)** real torch custom operators. So they are dynamo traceable and compatible with torch.compile and at call time the kernel's mlir is inlined into the surrounding module. So there's one executable and no host roundtrip. From a user's perspective once a kernel is registered you you can just call it like other pytorch operator. nothing special at the call site and that works that's what make kernel easy to adopt. So torch TPU makes TPU TPU a PyTorch device and with those building blocks in place. Now let's talk about VLM torch TPU at a very high level VM torch TPU is a platform plugin of VLM for TPU. The design goal is to reuse as much VLM as

**[12:30](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=750s)** possible and that's how you get the benefit of being pyro native and write TPU specific code only where the hardware actually forces you to for example custom kernels. The first piece is the TPU platform which answers VRM's question about hardware. It registers our palace attention back end. So if you specify attention backend flash attention on TPU, it resolved to the rack page attention kernel. The TPU platform also sets the compilation mode and token buckets because static shapes mean every shape has to be compiled ahead of time. And it picks the executor and configure the KV cache as well. For example, block size, cache DT type, which transfer connectors are allowed, etc. The second piece is the model worker.

**[13:21](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=801s)** Below the platform is the TPU worker. One worker per device and one process each. The worker owns the process. It binds to its device joins torch distributed world on the TPU distributed back end profiles memory to figure out how many KV cache blocks actually fit and then hands off to the model runner. If you ever read VM's GPU worker, this one will look similar. And that's a point. The model runner is where it gets interesting. And the first thing we're saying is that our TPU model runner is a subclass of VLM's GPU model runner. We override about 15 method, the hot path and the inherited rest. The most important job of the TPU model

**[14:08](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=848s)** runner is to guarantee the model only ever sees a shape that the compiler has already seen during the warm up. For example, it prepares inputs on CPU using padding to align batches to pre-ompile predefined bucket sizes and copy them to device and it split the forward path into compile subgraphs. So the warm up path and the real path trees identically. Before the server takes a single request, it runs dummy batches through every bucket. So every shape is already compiled. And there's one thing that isn't about shapes, but probably worth mentioning is that the TPU runner also enables async scheduling to overlap CPU processing with TPU processing to hide the CPU latency.

**[14:58](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=898s)** So, so far you've heard PyTorch native a lot and you may be wondering what it actually buys us and here are the numbers in the VLM tortu codebase about half of the repo is palace kernels because that's a part the hardware genuinely requires and there's no way around it and then about 20% is for K transfer and PD sack which requires a lot of handling of device memory for example H2D D2 and H2H and the VRM integration surface like platform worker executor compilation etc is about 4%. The model definition layer is only around 1% because we inherit majority of the model architectures from VRM's reg registry instead of redefining them.

**[15:49](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=949s)** So we didn't port a model to we inherited one and spend effort where the hardware actually demands it. And this project started around December 2025 and over the past eight months our team has enabled majority of the main features in BLM. For example for ter for parallelism we have tensor data aspert and contest parallelism. For KV cache management we have uh prefix caching KV offloading import including the support for hybrid models like quens.5 and we support PD disagregate serving using the TPU sync library which Google recently open source and it supports different topologies between preview and decode for the best efficiency.

**[16:37](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=997s)** We also support other important optimizations like quantization, specular decoding async scheduling for performance and nowadays majority of the popular open source models are already available in VRM tourpu including quen 3.5 K3 GM 5.2 2, Deepseek, W4, Gemma 4, and more. And we are also expanding to full stack serving to cover complex serving needs, including integration with Google's LMD for large scale production serving. We have several customers already in private data with us using VR Inventor TPU for offline and online inference. And we've also been collaborating with Infact to accelerate the development and get ready to embrace the OSS community.

**[17:26](https://www.youtube.com/watch?v=Xh04f8eAPNc&t=1046s)** If you still remembered optimizations from Wuk's talk earlier, we already covered many of them. So this journey has just started. Uh we'll be open sourcing to GPU, VM to TPPU and other libraries soon. And please stay tuned and let's build the future together. Thank you. [applause]
