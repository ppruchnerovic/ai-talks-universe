---
id: -TpQ3s95O1o
title: "Full-Stack Observability in Ray: Infrastructure Signals in Ray Dashboard | Google | Ray Summit 2026"
slug: full-stack-observability-in-ray-infrastructure-signals-in
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 15
published_at: 2026-09-17T16:06:52Z
video_id: -TpQ3s95O1o
url: https://www.youtube.com/watch?v=-TpQ3s95O1o
youtube_url: https://www.youtube.com/watch?v=-TpQ3s95O1o
tags: []
topics: ["Classic ML & data science", "Evals, observability & reliability"]
transcript: true
---

# Full-Stack Observability in Ray: Infrastructure Signals in Ray Dashboard | Google | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=-TpQ3s95O1o) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Debugging distributed ML jobs on Kubernetes is difficult because of the visibility gap between failures at the infrastructure layer and the framework layer.

At Ray Summit 2026, Richa Banker, Senior Software Engineer at Google, introduces Ray's new platform events integration, which pulls Kubernetes events, for custom resources like RayCluster, RayJob, and RayService and for pod evictions, spot preemptions, and OOM kills, directly into the Ray dashboard by mapping ephemeral pod lifecycles to stable Ray worker identities.

You'll leave knowing how to get instant root-cause analysis without manual kubectl queries.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,314 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=6s)** Hi everyone, I think we will get started. Welcome to Ray Summit 2024. My name is Richa Banker. I am a software engineer at Google, working on GKE and AI infra ecosystem, and I am also a maintainer of the open source Kubernetes project, where I co-chair the SIG Instrumentation. Together with my colleagues at Google and with engineers at Anyscale, we have been focused on solving a major challenge in production AI/ML platforms, specifically bridging the observability gap when running Ray on Kubernetes. While Ray itself supports running in different sets of compute environments, ranging from bare metal clusters to HPC systems, a huge portion of enterprise distributed AI/ML platforms and AI/ML workloads are deployed on Kubernetes

**[0:54](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=54s)** using the KubeRay operator. In these setups, infrastructure failures and hardware failures are often opaque to the ML practitioners. So today, I am thrilled to announce the full-stack observability feature in Ray that we have worked on upstream, which aims to bridge this gap, so let's dive right in . To understand why this work is crucial, let's first understand what happens when Ray runs on Kubernetes. While Ray itself gives a fantastic programming model for distributed AI. Uh, all...Sorry, one second, yeah. While it gives a fantastic programming model for running distributed AI in production. When Ray runs on Kubernetes pods, there are multi-level failures

**[1:43](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=103s)** that can happen, which remain opaque to the Ray runtime itself. So these multi-level failures, number one is application masking. When a node kernel panics or when a GPU drops off the PCIe bus or fails to support because of underlying node memory pressure, all of these errors are not known to Ray, right? They bubble up to the Ray practitioner or the ML practitioner as a generic Python Ray task error, or worse, there could be a silent worker disconnect which is not surfaced anywhere. Number two: Siloed tools. While the Ray dashboard itself is great at tracking task and actor states. And even memory metrics. All the Kubernetes scheduling events and pod lifecycle

**[2:31](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=151s)** events, they live entirely in the Kubernetes API server or in external logging platforms, totally unaware today. Third is context switching. So when things are breaking while running Ray on Kubernetes. ML engineers are forced to switch tools. Forced to go through like kubectl describe pod logs or parse dmesg logs and often raising access tickets to cluster admins because they hardly ever have access to the underlying Kubernetes cluster. And finally, high MTTR. So when hundreds of H100 GPU chips which are super expensive, they sit idle. While engineers are filing all these tickets to get access and then trying to find out why their job failed? Was it because of bad code? Or was it because of some underlying infrastructure failure? You lose time, you lose velocity, and most importantly, you

**[3:21](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=201s)** lose compute budget. So, let's take a look at the debugging journey, what it looked like before versus what it looks like after. So, as I said before, if a Ray worker failed, the Ray dashboard would simply mark that worker and show it as dead in the UI, giving no further details about why and what happened. So the developer was left guessing: was this a CUDA out of memory issue? Was this an underlying infrastructure issue ? I have no idea. Now, an instant platform event is surfaced onto the worker timeline directly within the Ray UI. During investigation, developers would need to go onto the CLI, hunting through kubectl get events. And often, if Kubernetes has deleted a pod or rescheduled a pod. The event history would get lost because of the one-hour TTL on K8s events. Now, a real-time

**[4:10](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=250s)** warning—OOMKilled pod, evicted, or pod rescheduled warning—is streamed directly into the dashboard, and finally, at resolution time, instead of going through multi-day admin escalations to get access to kernel logs, developers now gain self-serve root cause diagnosis within seconds without leaving the Ray dashboard. So how did we achieve this? This is not a proprietary sidecar that we created. This feature is merged upstream in Ray core code and released starting in Ray version 2.5.8. The architecture itself is divided into three clean layers. The first is the Ray head ingestion. So, we provided a Kubernetes events provider, which is a lightweight background pull-based task that runs in the Ray

**[4:57](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=297s)** dashboard head process. Which establishes Kubernetes watches on Ray custom resources, like the Ray cluster, Ray job, Ray service, and the associated Kubernetes pod events, and uses the in-cluster service account for doing that. Second, we have introduced a generic, provider-agnostic platform event Protobuf schema. What this means is that this feature is not just hard-coded to just Kubernetes. In the future, if we want, we could support this for other provider events. Like Slurm events or other cloud provider events if we wanted. Events are themselves stored in an in-memory, bounded ring buffer cache. And exposed via a lightweight REST API. And finally , in the Ray dashboard UI, we have implemented a native surface where we poll these events and then display them

**[5:46](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=346s)** , while also supporting filtering, sorting, and drill-down capabilities. So let's take a closer look at what happens. Uh, during ingestion and filtering of these events in the Ray cluster. So, as stated before, we have implemented Kubernetes watches for the custom uh Ray custom resources. Uh, whenever KubeRay the operator provisions like a new Ray worker pod or it creates the Ray head service or where it just does some updates to the state of the underlying Ray cluster. All of these high-level lifecycle events are now streamed directly into the Ray dashboard. So we are capturing all the Ray uh custom resource lifecycle events directly. And on top of that, we have also implemented granular pod-level ingestion. Which means that in a Kubernetes namespace, there could be hundreds of workflows

**[6:33](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=393s)** running, right, and not all of them belonging to the same Ray cluster. That we are interested in. So we have implemented client-side event filtering using Kubernetes label matching. So that we are only capturing pod events for those pods that actually belong to the active Ray cluster. So, this ends up capturing critical container lifecycle stages. On top of the custom resource stages that we talked about before, which are like image pull latency, pod killed, pod evicted, etc., and crucially, all of this is done in a way that we leave zero footprint on the Ray head performance itself. So the in-memory cache that we have is a bounded configurable LRU ring buffer, which ensures that even in a big, noisy cluster or when the event volume is like super, super high, we are keeping the memory usage capped and predictable

**[7:21](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=441s)** all the time. Another thing: observability should not be confined to a single tab in the UI. Right? Major AI platforms, or all AI platforms, would want to stream all of this information to their own corporate back-end for logging, you know, for logging, alerting, and other SIEM systems. So we have ensured exactly that by integrating the platform events with Ray's canonical event framework and export pipeline. What that means is that whatever the ingested Kubernetes pod events and Ray custom resource events that we ingest, they are converted into Ray's canonical event format. This Ray event format means they will share the same structured schema, the same timestamp fields, and

**[8:08](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=488s)** the same severity levels as the existing Ray events for Ray core tasks, actors, and driver events. All of these events are also streamed to structured JSON line files in the same location where the existing telemetry data exists for the Ray cluster. Uh, this is done using configurable log rotation and asynchronous write buffers to make sure that we are giving zero impact to Ray's core execution. And then finally, because all of this is like uh standard JSON data, uh existing uh observability agents like Fluentbit, Vector, and Promtail can parse all of the structured data and then export that to the bucket of your choice, Google Cloud Logging, AWS CloudWatch, Datadog, or even Kafka. So now, ML engineers can

**[8:59](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=539s)** write unified alerting rules in their corporate Grafana dashboard, correlating Kubernetes spot detections with ML model training metrics. So, what does this look like for an end user in the UI? Right along the top navigation bar, we have added a separate dedicated tab for platform events, where we support filtering these events by three categories: by severity (they could be an info event or a warning event), by platform (right now the only supported platform being Kubernetes but can be expanded in future), and the object kind, like what type of object you are trying to filter : spot, for Kubernetes spot, or for Kubernetes, or for Ray custom resources like Ray cluster, Ray job, or Ray service. The other two red highlighted

**[9:48](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=588s)** boxes are showing the actual event data . The first one is showing a Kubernetes image pull event, showing you that it successfully pulled this particular image in 1 minute 26 seconds. So now, if there is a slow Ray worker startup. The ML engineer knows exactly why, because it was a slow image pull delay. And it was not because of their, you know, slow Python initialization in their code. And then the second one is more interesting. It's a warning-type event which is telling that there is a cited reason of failed scheduling. Zero out of two nodes are available because of insufficient CPU. So now, ML engineers are able to do root cause diagnosis without leaving the Ray dashboard and without requiring any kubectl access. So, all of these events that we talked about, right? The Kubernetes spot events and the custom

**[10:36](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=636s)** resource events. They only solve container-level problems. But there is still one major blind spot that exists in AI infrastructure, which is the node infrastructure layer. Whenever a GPU encounters an ECC memory fault. Or whenever it encounters an XID 79 fatal drop, these hardware failures can be captured by existing uh low-level node telemetry agents. Like a customized Kubernetes node problem detector, which is an existing tool, or a GPU device plugin, like the NVIDIA device plugin or even DCGM. These tools can catch these hardware failures, but they re-emit them as Kubernetes events, but on top of the node object, not on top of the pod object. And Ray user reports , they cannot watch for these

**[11:26](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=686s)** cluster-wide node-level objects, because granting that node-level RBAC to user workloads is like a major security concern, right? So how we are addressing that is through this new proposal in open source KubeRay which we are calling the selective node event forwarder. So instead of forwarding every, you know, blindly forwarding every node event, which could also have periodic health checks which we don't want to include to, you know, increase noise. Uh, periodic health checks like disk health checks or CSI attachments. This forwarder lets admins configure a precise regex and sort of allowlist so that you can filter what events you are interested in. Maybe we are just interested in events that mention a particular XID error. Or some other

**[12:13](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=733s)** hardware error. So we allow for that filtering in the forwarder. So, as shown in the diagram here. This event forwarder is a new controller that will exist in the KubeRay operator. Which will run with cluster-wide RBAC. Watching for Kubernetes events resources. So, it will watch for all the Kubernetes node events. Apply the allowlist on top of that. To filter, you know, the relevant ones that we are interested in. Convert that into—no, before converting, it will map that into active Ray pods that belong to that particular Kubernetes node. So that we make sure that we are only catching events relevant to the Ray pod . Uh, that our cluster has. Right? And then finally re-emits nicely configured and correlated hardware-level warning on top of the owning parent Ray cluster custom resource. What that means is

**[13:04](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=784s)** that in the UI, you will have something like this when a hardware fault strikes . The highlighted box shows you that there was a node infrastructure failure that was detected for this particular Ray cluster object. And the message gives you more details. There was an infrastructure failure detected on this particular node with the reason being XID 31 error caught on this particular GPU UID. And because of the selective event filtering, you see that the noise is kept to a minimum. There is only 13 events reported in the UI. So now ML engineers can point out direct, you know, faults in the hardware silicon layer. From within the Ray dashboard UI without requiring any cluster admin escalations or any cluster-wide access for resources. So, to recap where everything stands today: what we have

**[13:54](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=834s)** merged upstream in Ray 2.5.8 is the core platform event schema, the head injection module, the integration with the event framework as discussed before , and all the UI changes. The feature is gated behind this environment flag: "RAY_DASHBOARD_ENABLE_PLATFORM_EVENTS". So, make sure that you are setting this to 'true' in your Kubernetes pod manifest, especially for the Ray head pod. And we have also published a user guide in the official Ray docs, available at the link mentioned here. And finally, for the roadmap, we will continue to work on the selective node event forwarder in the KubeRay repo upstream, and eventually also look into integrations with the Ray autoscaler, so that we can trigger proactive node drains based on these node preemptions and hardware event warnings. That's all

**[14:45](https://www.youtube.com/watch?v=-TpQ3s95O1o&t=885s)** that I had about this feature. Please do give it a try and then share your feedback with the community. Join the conversation on Slack and GitHub and let me know if there are any questions. Thank you so much.
