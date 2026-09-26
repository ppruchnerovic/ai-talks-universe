---
id: bDG8f5KGetw
title: "Where’s My Training Job? Ray & GPU Observability at Datadog | Datadog | Ray Summit 2026"
slug: wheres-my-training-job-ray-gpu-observability-at-datadog
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 12
published_at: 2026-09-17T16:01:51Z
video_id: bDG8f5KGetw
url: https://www.youtube.com/watch?v=bDG8f5KGetw
youtube_url: https://www.youtube.com/watch?v=bDG8f5KGetw
tags: []
topics: ["Evals, observability & reliability", "Inference, serving & GPU infra"]
transcript: true
---

# Where’s My Training Job? Ray & GPU Observability at Datadog | Datadog | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=bDG8f5KGetw) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Ray enables large distributed training workloads across GPU fleets, but understanding what happens inside each job remains difficult.

At Ray Summit 2026, Marina Petzel and Ashley Chu from Datadog share how they built a unified job-level view that preserves history beyond cluster lifetimes, traces work across Ray processes, and connects failures with GPU health, utilization, and cost.

You'll leave seeing why distributed AI observability should center the job, not just the infrastructure.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*1,865 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=bDG8f5KGetw&t=6s)** Hi everyone. My name's Ashley and I'm an engineer at Datadog building out GPU monitoring. We help teams power more AI work from every GPU by connecting capacity, AI workload performance, hardware health, and cost in one place. That mission begins with a familiar and slightly stressful moment when you launch your job, watch the terminal, and wonder is anything actually working or am I just burning compute while I refresh logs? Now multiply that uncertainty across thousands of GPUs and Ray makes it possible to scale training from one machine to an elastic cluster, but that that scale also makes it much harder to understand what the job is doing and why it might be slowing down. I'll show you how connecting tracing, training, and infrastructure context can

**[0:56](https://www.youtube.com/watch?v=bDG8f5KGetw&t=56s)** turn a stalled Ray job into a system we can actually diagnose. So a model that starts in local development quickly outgrows one machine. Ray gives teams a straightforward path from local code to a distributed job and Ray distributes that job across GPU workers while the cluster can add GPU capacity as a resource as demand grows is grows. Ray solves a very real capacity and orchestration problem, but it also changes the visibility problem. The work is no longer happening in one process or even on one host. It is spread across workers, GPUs, networks, and cluster infrastructure that may come and go during the run. So the question changes here from is my GPU healthy to is my training job actually making useful progress?

**[1:46](https://www.youtube.com/watch?v=bDG8f5KGetw&t=106s)** At cluster scale, the unit we need to observe is the training job itself. Each training worker has a rank, is scheduled onto a host, and is commonly assigned one GPU. A GPU can look healthy or even busy when the overall job is still making poor progress progress. So, the job includes many ranks, each tied to a worker and host communicating over the network through collective operations. That means device level metrics are necessary, but they aren't sufficient. We need to connect each device back to the synchronized workload it supports. And a healthy GPU doesn't necessarily mean a healthy training job. The reason is synchronization. Distributed job training is not merely work spread across machines, but in synchronous distributed training, the

**[2:34](https://www.youtube.com/watch?v=bDG8f5KGetw&t=154s)** job advances at the pace of its slowest rank and behaves more like a hive-mind mindset. During a collective operation such as all reduce, every rank in the process must participate. The operation may overlap with other work, but completion of dependent work is still gated by the slowest participant. So, if a delayed rank gates a synchronous process group, that delay can propagate across thousands of otherwise healthy GPUs, and that gives us our first diagnostic task to find the straggler. The slow rank tells us where the delay surfaced and not necessarily where it began. The root cause could be anywhere in the application or the runtime layer like garbage collection or from a data loader or in the network fabric such as NVLink

**[3:22](https://www.youtube.com/watch?v=bDG8f5KGetw&t=202s)** or InfiniBand. And it might come from the node level CPU, memory, or storage issues down to the hardware level thermal thermals of ECC errors or the GPU itself. A wrong root cause diagnosis is costly causing disruption from unexpected investigation time, wasteful restarts, and lost progress in the last checkpoint. So, finding the straggler is not the same as finding the cause. That's why finding the straggler is only the first step. We need to connect the slow down to evidence across the application, host, network, and hardware layers. We need job aware root cause analysis that connects the MFU or step time change to a suspected cause, an evidence path, and a level of confidence that we can have. This matters because failures are

**[4:09](https://www.youtube.com/watch?v=bDG8f5KGetw&t=249s)** increasingly common as the study state. During several month-long pre-training runs for Llama 3 on tens of thousands of GPUs, about one failure occurred every 3 hours. More than half were GPU related, and even though the run maintained over 90% um effective training time. Economics amplified every gap. So, this is this fleet is roughly 36 million dollars per month, and a 1% efficiency loss equates to 4.3 million dollars a year. At that scale, observability is not just about responding to incidents, but it's about protecting training progress, engineering time, and fleet efficiency continuously. We learned this firsthand at Datadog when a customer reported an unexplained drop in their model flops utilization or MFU on their large pre-training run.

**[4:59](https://www.youtube.com/watch?v=bDG8f5KGetw&t=299s)** At first, several signals looked correlated. Agent restarts and memory errors were plausible suspects, but they turned out to be red herrings. And by relying on workload and hardware context from Datadog's GPU monitoring product, we were able to localize the cause to the NVLink fabric. XID events along with the physical layer retransmission became leading indicators for us. And this single investigation highlighted a common pain point. Teams need a way to easily connect hardware, topology, tracing, and workload aware diagnosis to remediate in days rather than months. And that's exactly what we're building as part of the Datadog's GPU monitoring product. Datadog's GPU monitoring already connects workload performance with GPU utilization, health, and cost, but now we're extending that foundation with job

**[5:48](https://www.youtube.com/watch?v=bDG8f5KGetw&t=348s)** level workloads designed to help your SREs, ML engineers, and data scientists answer end-to-end observability questions for your AI infrastructure to the workloads running on them. These are questions like, which rank slowed down, where did the time go, and where did the problem originate? So, let's answer how we're showing those capabilities in the product. So, we start at the level that the users care about, the training run, and we preserve the ray job and the training run identity, then connect each worker's world rank to its process, host, assigned GPUs, traces, and physical topology, even as the underlying cluster changes. In this example, our training view flags step 24 is unusually slow, and it takes almost 11 seconds while other steps are faster. Users are no longer forced to manually inspect

**[6:36](https://www.youtube.com/watch?v=bDG8f5KGetw&t=396s)** dashboards with hundreds of graphs per worker, and GPU monitoring immediately identifies rank 14 as the primary straggler and shows how far it deviated from its peers. That scopes the system, and we know which step changed, by how much, and which rank fell behind. But, let's see why it slowed down. So, we have an intelligently powered root cause analysis that's connected to all relevant layers of your AI stack through our MCP and Bits AI. The goal is to assemble a casual narrative from the the signals that we have. The triggering fault, the mechanisms that slowed down the rank, the cascade across its peers, and its actions an operator should take. In this example, the investigation links a hardware fault on one node to ECC and XID signals, the NVLink recovery events,

**[7:25](https://www.youtube.com/watch?v=bDG8f5KGetw&t=445s)** a sharp increase in step time, and an MFU drop. It also distinguishes affected synchronization peers from nodes that were largely affected and affected. And beyond just metrics that reveal a slowdown has happened, GPU monitoring also provides lightweight continuous tracing, which reveals what the rank was doing or waiting for during that week missing time. Here we can see a detailed execution trace that correlates what goes on in the CPU directly to the actual GPU execution of these calls. So, instead of a single duration number, we can see the sequence of work and identify a long synchronization call consuming most of the step. For example, here you can see a CUDA synchronization call consuming 166 milliseconds, more than 80% of this trace. And the best part is that all of

**[8:14](https://www.youtube.com/watch?v=bDG8f5KGetw&t=494s)** this can be continuously run with less than 2% overhead, so you no longer have a trade-off between observability and your training job performance. This trace becomes even more actionable when it leads back to the code a machine learning engineer recognizes. Although much of the underlying execution happens through native libraries and GPU kernels, the tracing view can connect those spans back to their relevant Python call site. Here, an optimizer steps with collective operations leading directly to the relevant lines in the training loop. That removes another layer of archaeology and saves debugging time. An engineer doesn't have to translate low-level GPU events into a guess about the application, and instead the trace preserves the path from system behavior

**[9:03](https://www.youtube.com/watch?v=bDG8f5KGetw&t=543s)** back to our source source code. So, tracing explains what happened, and then our topology visualization helps identify where it happened. We group affected workers by physical infrastructure that they share between the host, rack, GPU, or the link. In this instance, errors that looked like separate device events actually concentrated within within a single rack of GPUs. That pattern changes the diagnosis that we have. Instead of treating each red square as an independent GPU failure, we can investigate a shared rack level dependency. This is especially value valuable when the visibly slow worker is only on the endpoint where broader infrastructure issues surfaced. Now users can connect a job impacting symptom to the relevant physical pattern

**[9:52](https://www.youtube.com/watch?v=bDG8f5KGetw&t=592s)** in the AI infrastructure. Together, these views created one connected investigation. You no longer need the manual, cumbersome, custom investigative notebooks, data sources, and dashboards, and our training view identifies the slow step and the rank. Tracing shows whether time was spent computing or waiting and connecting um code that belong back to the behavior that we found. And topology reveals whether affected workers have shared infrastructure, narrowing the failure domain that we have. That connected context is the foundation for the job level diagnosis we're building into GPU monitoring now. We continue to work closely with our customers running training runs to improve these capabilities I've shown today, and are looking to apply the same

**[10:40](https://www.youtube.com/watch?v=bDG8f5KGetw&t=640s)** foundations beyond explaining failures to our providing remediation across any training or inference workload. So once So when someone asks, "Where's my training job?" the answer shouldn't require four dashboards, six bookmarks, and terminal archaeology. The job should remain understandable as works restart, clusters change, and symptoms cross layers of the system. The most useful observability starts from the user's unit of work that then connects downward into the code, devices, networks, hosts, and our topology. So Ray helps us scale the work, and Datadog allows us to understand the system that the work becomes. Created context here turns a stalled job from a black box into a diagnosable system.

**[11:28](https://www.youtube.com/watch?v=bDG8f5KGetw&t=688s)** So if you're running GPU workloads, you can scan the first QR code to try GPU monitoring free for 14 days. And if you're an eligible startup new to Datadog, the second has information about up to 100K in credits that you can use. So, please come find us after the talk, and we'd love to hear more about your training workloads and what's been hard to debug. Thank you. And if you want to continue the conversation, you can reach out to us at GPU monitoring product@datadoghq.com. Or we have a booth in the back that you can come visit and talk to us in person, and we have lots of free t-shirts as well. But, thank you so much.
