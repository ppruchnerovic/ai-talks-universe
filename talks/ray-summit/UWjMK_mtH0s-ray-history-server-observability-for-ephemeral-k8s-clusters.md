---
id: UWjMK_mtH0s
title: "Ray History Server: Observability for Ephemeral K8s Clusters | KubeRay | Ray Summit 2026"
slug: ray-history-server-observability-for-ephemeral-k8s-clusters
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 17
published_at: 2026-09-17T16:06:18Z
video_id: UWjMK_mtH0s
url: https://www.youtube.com/watch?v=UWjMK_mtH0s
youtube_url: https://www.youtube.com/watch?v=UWjMK_mtH0s
tags: []
topics: ["Evals, observability & reliability", "Inference, serving & GPU infra"]
transcript: true
---

# Ray History Server: Observability for Ephemeral K8s Clusters | KubeRay | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=UWjMK_mtH0s) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Ephemeral Ray clusters on Kubernetes improve cost efficiency and resource sharing, but once a cluster is deleted, the Ray dashboard, jobs, tasks, actors, logs, events, and node state disappear, making post-mortem debugging difficult.

At Ray Summit 2026, JiaWei Jiang (University of Washington), Aaron Liang (Google), and Hanju Chen (Texas A&M) introduce the Ray History Server, a new KubeRay project with two components: lightweight sidecars that persist the necessary data, and a stateless server that reconstructs the telemetry so users can view historical jobs, tasks, logs, and statuses.

You'll leave knowing how to keep observability after your clusters are gone.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,406 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=6s)** Uh hi everyone. Uh today I'm excited to share with you the latest addition to KubeRay, uh the history server, and how it solves the post-mortem uh observability challenge for ephemeral clusters. So, the agenda for today is we'll do a quick introduction, and then we'll talk about the observability problem and the solution we have for it. And then a quick demo. And then we'll talk about the different components and what makes up the history server. And we'll end by discussing what's next, and hopefully some time for Q&A. Um I'm Aaron, and I'm a software engineer at Google. >> I'm Hanru Chen. Uh I'm also a software engineer from Nyscale, now a master student at Texas A&M University. >> Hello, I'm Jiawei Jiang, and I'm a master student from the University of

**[0:54](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=54s)** Washington. >> So, this is what we're seeing across the industry. So, across the industry, we're seeing like a huge increase in the KubeRay adoption, and KubeRay becoming more of a standard to run your distributed AI workloads in production. And these AI workloads are typically running in expensive resources like GPUs or TPUs. And during the workload's life cycle, the user team has to choose. On one side, users can keep the workloads running to inspect task timelines and execution. And but on the other side, users can choose to shut down the cluster right after it completes. And as more team uses KubeRay, we're seeing a shift towards ephemeral clusters, so more towards shutting down the cluster right after completion. But

**[1:44](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=104s)** at the same time, we're also seeing a preference to use Ray dashboard as like the method to access those these Ray clusters. And essentially, these platforms teams have two options. In one option, you keep the cluster alive. The positive side of this is that you keep all access to the Ray dashboard, but the downside is the cost. The keeping these clusters alive I and I don't using these GPU and TPU quotas is extremely expensive. And exhausting these quotas just to have the dashboard running is very inefficient. On the other side, you have the other option if you want to save cost, you can immediately tear down the Ray clusters um the moment they finish, but you lose all the observability. And then all the in-memory dashboard is destroyed, no visual way to debug these

**[2:32](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=152s)** runs. >> [snorts] >> So, where do we debug and view the Ray dashboard without spending more money on the idle resource costs? So, that's why we built the history server to completely decouple the observability run the observability from the existing computer life cycle. And at the same time still providing a familiar dashboard UI and zero idle compute cost. So, what exactly is the history server? At its core, it's a postmortem replay engine. Observability that outlives the Ray clusters. Uh so, at the high level, it's broken down into two paths. Each reflecting the different stages that is required to reanimate the Ray clusters. Recording and replaying. So, representing the recording path is what

**[3:21](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=201s)** we call the collectors component and representing the replay path is the history server component. And the result of this combination is the reconstruction of historical telemetry that can be used to provide almost a near identical Ray dashboard experience. And still, at the same time zero idle cost. >> [snorts] >> So, with history server, you can shut down these expensive Ray clusters immediately after the execution, but still have researchers and data scientists access them the way they love. Through the Ray dashboard. So, before we go even deeper, let's take a look at history server in action. So oh thank you. >> [laughter] >> So, I currently have I currently already have a Ray cluster

**[4:11](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=251s)** running on Google Cloud with all the history server installed as well as the Kube operator. And what we're going to go through is just applying a Ray job, accessing it live, and then accessing it through a history server. Try to keep it short. >> [snorts] >> So, wait a few seconds for the Ray job to start. Great. Yeah. So, I'm sure many of you are already familiar with this dashboard. You can view the logs, uh the actors, uh cluster information, uh job information, and like of course

**[4:59](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=299s)** the overview that way. Oh, it looks like we have a failed Ray job here. >> [snorts] >> And just to clarify, I am using Ray data so the Ray data overview page should also be populated. And so, I would like to imagine like this is one of the Ray job that you're running, and it's you're just leaving it and like letting it die out. Uh so, in a few moments, we'll let the Ray class Ray job die on its own, and then we'll access it through the Ray history server so that we can debug it. All right. So, the history server Oops. Did I spell that right?

**[6:00](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=360s)** Yeah, okay. Sorry. So, the history server has a a UI page for you that lists all the terminated clusters that you can have access to. So, what we want to do is take a look at the latest run for the Ray job that just fell, which is this one right here, the second one. And I just go into it. And so, as you can see, pretty much everything's the same. Uh but just to also make sure we can show it later, but the Ray job isn't running anymore, and there's no pod or anything on the the Kubernetes cluster as well. And yeah, so let's for demo's sake, let's take a look at the Ray data, make sure that's populated, and let's take a look at the logs.

**[6:51](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=411s)** All right. So, the reason why the Ray job fell was because there was a corrupted data on batch 19. Yeah, so as you can see, you can access the terminated Ray jobs even after termination. And so, now I hand it off to uh Hanru to talk about the collector. >> Okay. Thanks, Aaron. Now, let's look at the history server's collector computer configuration. So, most of the configuration is shared by the head and worker collectors. On the left, we configure where we to store data, and which Ray cluster the data belongs to, and how to access Ray's local data.

**[7:39](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=459s)** These includes the storage back end and buckets, the cluster name and namespace, and the shared temporary volume. On the right, the main per pod difference is the field called ray role. Uh this is for a collector to know which node it is at, either the ray head node or the ray worker node for the head collector and the worker collectors. So, the configuration is mostly shared with only the collector's role changing between the head and worker pods. Now, let's look at the collector architecture at a high level. So, the collector receives two types of data from ray. Uh the first is ray logs. Uh ray logs are read from the shared temp directory

**[8:26](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=506s)** volume. While the second is ray events, and ray events are pushed to the collector through the events HTTP endpoint. And both are collected by the sidecar and uploaded to object storage. So, the history server can access them later. In the next few slides, we'll look at these two collection paths in more detail. So, once the workload starts running, one of the collector's responsibilities is to persist ray logs to object storage. The ray container and the collector sidecar share the same ray temporary directory volume. So, the collector can directly access ray's log files. There are three main cases that we handle. The first is normal pod termination. During a graceful shutdown, the

**[9:15](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=555s)** collector performs a final scan of ray's temporary directory and uploads the remaining logs. The second is a ray session transition. The collector detects the old session and moves its log into the previously logged direction directory for later upload. Uh the third case, and this one I want to emphasize is collector crash and restart because this is important for reliability. After the collector restarts, the logs are still preserved on the shared volume. So, even if the collector itself restarts, we can still recover and upload the logs left from the previous session. And next, let's look at the event collection path.

**[10:03](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=603s)** So, to understand the event collection path, you need to understand some part of Ray's knowledge first. So, Ray core components will generate different types of events, including task, actor, job, node, and worker events. Each producer sends these events over no local GRPC to the local aggregated agent. The aggregated agent first buffers and batch these events in memory and then sends them through HTTP post to the collector sidecar in the same pod. To enable this pipeline, we need to configure these four environment variables in the Ray container. But you you don't have to remember them. Uh those examples are in um Ray documentation and the cool Ray repo

**[10:52](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=652s)** repository examples. So, you can find all these settings. Next, let's look at the what happens inside the collector after it receives the events. The collector use a this-first pipeline, which means that each event batch it receive, it will immediately append it to a local JSON line file. And when the file reaches its time or size threshold, it is rotated and uploaded asynchronously in the background. And if local disk usage reach the back pressure threshold, the collector temporarily stops stops accepting new event batches. This design keeps memory usage bounded and preserves a subset of events on disk

**[11:41](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=701s)** if the collector restarts. And all of these um features can all be configured. But it's too deep, so uh I'm not going to deep dive this, but you can see those examples on Cooper repository and read documentation example. Now I'll hand it over to Zhaowei to walk through the history server architecture. >> Okay, thanks, Hanru. And Hanru has covered the write path, so from this point forward, I will focus only on the replay path. So here is the basic configuration for the history server. And for history server deployment on the left-hand side, we just run it as a Kubernetes deployment and under the history server service accounts. And the main configuration is on the

**[12:30](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=750s)** right. In this example, GCS means Google Cloud Storage, and GCS bucket identifies the object storage bucket name. The cache byte budget and pod memory limit can prevent the pod from like crashing due to out of memory errors. So the basic configuration contains only one history server uh deployment, one object storage to reform, and a few cache and resource settings. Now let's look at the replay architecture. Once the rate cluster finishes, its history remains in the object storage. We run the history server completely decoupled from your active workloads. When someone opens a past rate cluster session, the server reads the logs and

**[13:18](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=798s)** event files to rebuild an image snapshot. And then serves the standard rate dashboard APIs. That means users get the exact same UI experience they are used to even though the original cluster no longer exist. In short, object storage keeps the durable history and the history server turns it back to the dashboard view. So, this works great for a single cluster session, but when scale up to like uh hundreds of thousands of sessions, the efficiency becomes the real challenges. So, how do we avoid loading sessions nobody opens? And how do we stop like rebuilding the same popular session over and over? That brings us to our solution on the next slide, on-demand loading,

**[14:08](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=848s)** and combine with a by bounded error cache. So, now we can see both optimizations in one request flow. When a user selects a historical session, the history server first checks whether it uh its snapshot is already cached or not. If it is a cache hit, uh the server skips the entire loading process and serves it directly. The cache keeps recently used snapshot and removes the least recently used ones when it reaches the memory limit. On the other hand, if it is a cache miss, the server uses on-demand loading. It reads and rebuilds only the selected session, so sessions nobody opens are never loaded. The rebuilt snapshot is then cached and served to the raid dashboard.

**[14:57](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=897s)** So, the real scaling benefit comes from combining the two. On-demand loading means thousands of historical session can remain in object storage without consuming like uh CPU and memory until someone opens them. Once the session is loaded, the error cache that later dashboard requests reuse a snapshot instead of like downloading and rebuilding it again. Also the IO cache is by default this, so memory is well under control. As a result, resource usage follows the sessions user are actively viewing rather than like every historical session stored in the object storage. This allows the history server to support a growing number of historical session without its compute and memory

**[15:46](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=946s)** growing at the same rate. Okay, so to close, let me briefly walk through our road map. We started with an alpha proof of concept to answer how we could collect, store, and replay the Ray cluster's his uh history after the cluster shuts down. Now in beta, our focus is scaling up, supporting heavier production workloads, and hardening performance and storage. Looking toward GA, our focus shifts to operability, observability metrics, simpler configurations through the Ray cluster API, and managing dashboard life cycle. So, if uh if you are running Ray uh Ray on Kubernetes, try the beta and tell us what breaks. And so, this has been a true community

**[16:34](https://www.youtube.com/watch?v=UWjMK_mtH0s&t=994s)** effort, over 100 PRs from contributors, reviewers, and maintainers. A special thank you to our co-maintainers, Andrew, Ryan, and Kou, whose guidance and reviews helped us bring the history server from proof of concept to beta. And so, for those who would like to join the Ray history server Slack channel, the QR code is on the left, and for more information about the history server details, we also have a blog post, the QR code is on the right. Okay, so for those who have questions, we can discuss more down here. Okay, thank you so much. >> [applause]
