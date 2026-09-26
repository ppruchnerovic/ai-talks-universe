---
id: MFyBXjacCXQ
title: "One Cluster, End-to-End | AWS | Ray Summit 2026"
slug: one-cluster-end-to-end-aws-ray-summit-2026
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: ["One Cluster"]
channel: "Anyscale"
duration_min: 13
published_at: 2026-09-17T16:06:55Z
video_id: MFyBXjacCXQ
url: https://www.youtube.com/watch?v=MFyBXjacCXQ
youtube_url: https://www.youtube.com/watch?v=MFyBXjacCXQ
tags: []
topics: ["Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: true
---

# One Cluster, End-to-End | AWS | Ray Summit 2026

**One Cluster**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=MFyBXjacCXQ) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Teams training large models on Ray often run three separate footprints: one for data processing, one for distributed training, one for serving. Each brings its own scheduler, its own scaling behavior, and its own idle GPUs.

At Ray Summit 2026, Shreyas Adiyodi and Anoop Saha from AWS walk through collapsing that into a single Amazon EKS cluster with SageMaker HyperPod: scheduling heterogeneous CPU and GPU Ray clusters against shared capacity with queue-based admission, where checkpointing belongs when a run spans days, recovering from node-level hardware failure without restarting the pipeline, tightening the experimentation loop, and deploying models for accelerated inference.

You'll leave with a reference architecture for end-to-end Ray pipelines on Kubernetes that maximizes GPU utilization across every stage of model development.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,177 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=6s)** Hi everyone, I'm Treas and I'm a product manager in the SageMaker Hyperod team. >> Hello. >> Hello. Uh my name is Nesh. I'm a senior SD in AWS. Today we are going to talk about how you could deploy data prep, training and inference array workloads on a single Kubernetes cluster, especially when you're operating a multi-team organization. So this is where most teams typically start with. They're going to have a GPU pool which is shared across different teams and they're going to deploy maybe a ray job for data and training, data prep and training. You would have a ray service deployment for inference or a ray cluster deployment for interactive

**[0:53](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=53s)** development and experimentation. So ray is really good at optimizing tasks and actor scheduuling within a ray cluster. But as soon as you have a multiple deployment of ray cluster across your teams, Kubernetes takes over and the way it works is it would prioritize whichever workload was submitted first. As you can imagine, this leads to inefficient GPU utilization. So in order to solve this, there are four building blocks that you need to keep in mind. Number one, you need a queue in front of Ry that allows for efficient resource sharing. Number two, you want to provide managed developer environments for your data scientists and out of the box observability so that they could iterate

**[1:41](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=101s)** faster and free up your resources faster. And all of this needs to be brought together on a multi-tenant interface that allows for resource isolation. And finally, you want a resilient and performant infrastructure that allows you to finish your training runs faster uh and provide you accelerated inference performance. So we'll deep dive into each of these blocks in this talk, >> right? Um so queuing. So if you ever had to share a Kubernetes cluster with multiple teams or between data scientists from the same team, um you probably already have faced this problem before. What normally happens is someone would submit a workload that would consume entire clusters capacity leaving everyone else's workload to star forever or stuck in a state where they aren't

**[2:28](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=148s)** making any progress. So when faced with this problems administrator typically try to solve this in the simplest way possible which is by doing static allocation. You slice your compute capacity into n pieces and um you assign one slice to team A and another slice to team B. Well let's take an example. We have two teams here. Uh team A has been given two comput capacity units. Could be nodes, GPUs, doesn't matter. And the second team has three. Uh team A wants to run three jobs and two of them are running just fine. But the third job is stuck because there is no free node available within team A's COD. Team B, however, tells a different story. They have two nodes sitting idle, uh but they aren't using it. So we're in a state where your cluster is overprovisioned and underutilized at the same time. And this obviously is not the

**[3:16](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=196s)** most efficient place to be. So how do we solve this? Well um demand exceeding supply or capacity is a problem that we've solved countless times in computer science and uh the solutions almost always take the take a same shape and form. Uh you need priority. What do you do when you have infinite number of workloads and limited capacity? You have to prioritize. Uh so we start by assigning workloads priority. Uh some workloads are more important than other. um a an inference deployment that's serving live production traffic is uh you know way more important than a weekend experiment. And what do you do if your workloads have same priority? You cue them. Um and when it comes to capacity allocation, you you you can go beyond static allocation. Um you can define a floor for each team saying that my team needs

**[4:03](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=243s)** x amount of capacity at all times. But if there are more capacity in the cluster that's sitting idle, let me use that too. uh so that way a team can lend their idle capacity to other teams knowing that they will get it back when and if they need it. So this kind of capacity transfer between teams uh increases your resource utilization uh significantly when you use a shared cluster. There are some nuances to be aware of too. Uh one of them is uh partial admission uh training jobs typically require all workloads to be running uh for them to make any progress. If you have, you know, 12 parts out of 16 running, it it's pretty much stalled, not making the right progress as it should. Um, not only that, it it's going to keep 12 GPUs you uh, you know, locked in, and it prevents someone else from using it. So, you need

**[4:50](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=290s)** gang admission. You can probably guess where I'm going with this. One of the best solution in the market to this is Q, but it's it isn't the only solution as we'll see. [snorts] Um, the second thing is uh, resizing. Typically when you resize something in uh KQ uh the workload is suspended and it's resumed at a later point in time. Um when you suspend a ray cluster you're using the you're losing the entire state that held in its head pod. Um everything that you collected so far just kind of goes away because the ray cluster that's created when you resume the workload is an entirely new rate cluster. Uh the solution to that is elastic admission. This is a recent feature enabled in KQ. uh if when you have the fish flag enabled you can scale up your rate cluster without losing any state and the failure can sometimes be silent. You can say that my you can go into your

**[5:39](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=339s)** reg cluster and say I need x amount of capacity to run my uh ray workload but your kod could be preventing you from accomplishing that capacity or reaching that capacity. So you need visibility into your uh queuing system uh so that you can know when your job is going to actually run. Um so we'll go into that solution a little bit at the end. Uh so once you have this kind of compute component system set up what would a data scientist need next. It's it's for to be really productive with this you really need a a functioning developer environment and developer environments for ML applications are not well they're they're quite different from the ones that we're used to. um gone of the days when you could just write and build application and run it in your laptop or local workstation but for ML workloads you need GPUs the is not going to load in your memory so you need an

**[6:29](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=389s)** environment that's colloccated within a standard GPU cluster so you can quickly iterate see the results and then launch your job um so you also need an interface that you're familiar with could be Jupyter lab notebooks or VS code environment u but whatever this environment is uh you have to be able to interact with ray as if you're it's running right bes right right beside you. You also need uh sorry come back to yeah uh you also need visibility into ray dashboard um and the once again the queueing system so you know how far along you are from uh your job actually getting scheduled [snorts] right so right so these problems can be solved by a manage ray developer environment it gives you a VS code or a code editor instance that feels like it's running

**[7:18](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=438s)** inside ray um so you can just do raot in it and then just start working. You can work with all ray primitives. It could be ray data, ray serve, ray uh train, uh ray tune. They're all available right at your fingertips. And to make things easier, you have out of the box observability. Setting up observability in ray involves steps. Um you got to set up your own Prometheia, scrape targets, uh create graphana uh environment, set up access dashboards and maintain them. Um all this could be simplified if you have it uh out of the box in a managed environment. Yeah. So, as Nish mentioned, you need a queueing system. You need managed developer environments and out of the box observability. And on on top of that, especially if you're operating a multi-team organization, you want a multi-tenant interface that's easy to

**[8:06](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=486s)** use. And with Kubernetes, what you would typically end up doing is you would have a namespace based resource shar resource isolation environment. So every team is mapped to a namespace and you uh you allow them to manage resources and deploy resources and access resources in that particular namespace, >> right? Yeah. So the fourth pillar is basically the theme of the fourth pillar is everything fails all the time. Um so you need a performant and resilient infrastructure. So let's look into what happens when you run into failure during a training job. Um so naturally all your training jobs hopefully checkpoint and they checkpoint frequently. Uh but when when you're when one of the nodes run into a failure all

**[8:53](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=533s)** the progress that you've made since the last checkpoint is gone. And depending on how frequently your checkpoint could be a few minutes or it could be hours and if you multiply by the total number of GPUs you have in your cluster the cost is significant. Now most obvious one of the most obvious ways to solve this is to checkpoint frequently. But checkpointing is also an uh expensive operation. So the more frequently you checkpoint uh you're going to lose your your training throughput is going to reduce too. So how do you solve this? Well first of all failures are inevitable. We can't prevent GPUs from failing. Uh but what we can do is make sure that infrastructure layer you have an ability to automatically recover failed instances. Um so that your jobs can run uninterrupted for as long as possible. Um you can listen to GPU signals and take recovery actions.

**[9:43](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=583s)** actions like rebooting the node or sometimes even replacing your hardware. In terms of checkpoints, we talked about how um increasing the checkpointing frequency can uh minimize the lost work. Um you can improve the checkpointing performance by having some kind of tier checkpointing where you don't write to some durable object store directly but you save checkpoints within your cluster in memory and you do that frequently and then you periodically sync that to durable storage for you know persistence. So that way you can checkpoint at a much rapid rate than you normally would uh without compromising your jobs throughput. Now taking a step back we talked about training u the similar principles apply to raise serve as well. For example if you're using ray serve to deploy your production endpoint you could take care of uh KV caching. Normally what happens

**[10:32](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=632s)** is production deployments see when they see a spike in traffic um they launch a new replica and the replica takes time to come up because the additional capacity has been provisioned and uh the first few records are going to be slow because they start with a cold KV cache. So if you had the KV cache maintained outside the replicas in a separate environment um these requests could uh technically be served quicker with a warm KV cache from the get-go. So yeah. >> Yes. So you all might be wondering how you can implement this on your own. So we are happy to announce that Ray on SageMaker Hyperod now brings all these building blocks all together from the infrastructure layer which is exc uh performant and resilient all the way up to the purpose-built multi-tenant

**[11:21](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=681s)** interface on SageMaker Studio. Now your data scientists can easily manage your ray clusters, spin up develop manage developer environments all in one purpose-built solution. And one thing to stress is this is not just a one one sizefits-all solution. A lot of you might be operating your own internal ML platforms. So we have a layered stack solution here. So if you want to just integrate a manage developer environment or you just want to plug and play observ internal platform, you could opt into individual features and integrate easily. So Hyperod is a highly customizable environment that meets you where you are. So yeah, just the four main takeaways. You need a queue to have efficient

**[12:11](https://www.youtube.com/watch?v=MFyBXjacCXQ&t=731s)** resource sharing. You want managed developer environments and observability for faster iterations for your data scientists. You want to give them an easy to use interface which multi-tenant which supports multi-tenency. And finally assume failure. So you need resilient and performant infrastructure that powers this all. Thank you. And you can scan this QR code if you are interested to learn more.
