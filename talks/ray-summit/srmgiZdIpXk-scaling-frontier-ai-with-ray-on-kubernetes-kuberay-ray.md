---
id: srmgiZdIpXk
title: "Scaling Frontier AI with Ray on Kubernetes | KubeRay | Ray Summit 2026"
slug: scaling-frontier-ai-with-ray-on-kubernetes-kuberay-ray
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 19
published_at: 2026-09-17T16:06:21Z
video_id: srmgiZdIpXk
url: https://www.youtube.com/watch?v=srmgiZdIpXk
youtube_url: https://www.youtube.com/watch?v=srmgiZdIpXk
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Scaling Frontier AI with Ray on Kubernetes | KubeRay | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=srmgiZdIpXk) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Ray on Kubernetes has emerged as the go-to orchestration platform for large-scale compute, and through the KubeRay project the community is co-engineering Ray and Kubernetes to meet the reliability and scaling demands of frontier models.

At Ray Summit 2026, KubeRay maintainers Andrew Sy Kim (Google), Jui An Huang (Anyscale), and Hanju Chen (Texas A&M) share how the ecosystem is evolving to support emerging AI workloads, including post-training pipelines and agentic workflows, key community-driven initiatives addressing critical scaling gaps, and real-world lessons from frontier deployments.

You'll leave with the KubeRay roadmap and lessons from frontier deployments.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,724 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=srmgiZdIpXk&t=6s)** All right. Um, hey folks. Um, this, uh, welcome to the, um, Cubray session at Ray Summit. Uh, I know this is the last talk of the conference. So, appreciate folks, uh, making it out. Um, so my name is Andrew. I'm one of the maintainers of Cubray. And joining me are Rion and Hanu who also maintain the project. Uh so in our session we're going to share um progress update on how Ray on cube has matured and and grown over the past uh few years. Uh and then Hanju will cover some examples of uh how ray on kubernetes is powering uh frontier AI research and and next generation um a IML platforms and then uh Rion will share some of the recent developments in Ray and Kubernetes and what's on our roadmap. Yeah. So quick intros before we dive in. I'm Andrew. I'm a staff software engineer at Google leading the

**[0:53](https://www.youtube.com/watch?v=srmgiZdIpXk&t=53s)** ray team. I'm Haru. I previously work at Enskill. I'm now a master student at TexasM University. >> Uh hi everyone. I'm Rayan. Um I'm work on ray core and cube and any scale. Thanks. >> All right. Yeah. So to get started um I want to spend um couple minutes just uh providing a high level introduction to Cubray for anyone in the audience who who might be uh new to to Ray or Cubray. So, Cubray is the uh open- source Kubernetes operator for Ray. Uh it's uh written in Go and provides a collection of Kubernetes custom resources which you can use to manage uh and scale uh your Ray clusters on top of Kubernetes. Um so, as seen in the keynote and throughout the throughout Ray Summit, we

**[1:40](https://www.youtube.com/watch?v=srmgiZdIpXk&t=100s)** see Cubray being the most um productionready and and battle tested uh open source deployment option for Ray today. Uh and in addition to a Kubernetes operator um Cubray also provides uh complimentary components for platform builder such as extension API servers, cube control plugin, helm charts uh and more. So yeah, I wanted to reflect on kind of the past few years of progress um on the whole you know ray on Kubernetes journey which began somewhere between 2022 and 2023. Um so at the time you know generative AI was rapidly taking off and creating massive demand for um scaling distributed AI workloads and many companies were uh exploring Ry for their scaling needs and uh around that time um there was like an engineer at by

**[2:27](https://www.youtube.com/watch?v=srmgiZdIpXk&t=147s)** danceance developing a Kubernetes operator for Ray which was eventually donated and and became uh Cubray. Uh so and then in 2024 um our primary focus was uh hardening Cubray. So we focused on um core scalability and stability. Uh we matured the the CRDs um and eventually um we released 1.0 um which was the GA release. Um by 2025 Cubray started to emerge as the open source standard for Ray in production. Um last year and then this year at Ray Summit we saw many sessions from leading AI companies that shared how they're um building their uh production machine learning platforms using Cubray. And then in addition, we started to focus on more like deeper integrations and bridging Ray and Kubernetes primitives

**[3:14](https://www.youtube.com/watch?v=srmgiZdIpXk&t=194s)** closer together um for uh for especially for like platform ML platform builders. Uh and then um today in in 2026 we're uh entering this new era where between Ray and Kubernetes projects we are uh co-engineering new capabilities together. Uh and beyond just running Ray in production for machine learning platforms, we're also seeing Cubray being used uh for frontier AI research um at larger scale. Yeah. So going forward, we want to make uh Ray and Kubernetes kind of synergize even better together. Um we we see Kubernetes bringing the most battle tested and uh productionready infrastructure platform adopted by basically almost every company at this point and it has a really um thriving cloudnative ecosystem that surrounds it.

**[4:02](https://www.youtube.com/watch?v=srmgiZdIpXk&t=242s)** Um Ray brings the distributed computing for AI widely adopted loved by researchers and and machine learning engineers. Uh and so we see Ray and Kubernetes um continuing to be two leading open source standards that together are powering um AI at scale and uh yeah and Hanu will cover some of the some of these examples in more details. >> Um now I'm going to talk about real kernetes for frontier AI research example. First um let's look at a real world example from XAI. They use rayon kubernetes to prepare multimodel image and video training data. Ray here handles the multimodel data processing and video creation pipeline and

**[4:52](https://www.youtube.com/watch?v=srmgiZdIpXk&t=292s)** kubernetes provides the underlying infrastructure for running and scaling ray clusters. So we can clearly see the division here. Ray handles the distributed workload while kubernetes provides the underlying compute infrastructure. Now let's look at another example from Nvidia. Here is Nvidia's robotics foundation model growth and one which scale training to 1,024 GPUs. Nvidia use Osmo uh which is their kubernetes workflow orchestration pro project to manage the training workflow and Osmo can use uh different kinds of kubernetes cluster as compute backends inside the

**[5:40](https://www.youtube.com/watch?v=srmgiZdIpXk&t=340s)** group workload use ray for distributed multi-node training and data injection so again kernetes provides the compute while ray handles distributed execution inside the workload. Next, let's look at Microsoft's uh recent frontier model use case. So, they recently released a new model called MAI syncing and MAI's pin model. Mi based one is a model with close to one trillion total parameters. Microsoft use renet across end to end frontier air workloads including pre-training reinforcement learning uh inference and evaluation and CPU heavy data pipelines. So again Kubernetes

**[6:31](https://www.youtube.com/watch?v=srmgiZdIpXk&t=391s)** provides the underlying compute infrastructure while ray provides the distributed runtime inside the jobs. Beyond frontier workloads, rayon kubernetes has also been integrated into internal aim platforms and many companies. Here we can see production examples from Uber, Spotify, Apple, Bidance, Reddit, Pinterest, Shopify and others. These platforms cover trending inference data processing and other distributed ML workloads. Uh because space is limit on this slide. So the citation number will point to the four reference at the uh the next slide. These are just reference and you can

**[7:18](https://www.youtube.com/watch?v=srmgiZdIpXk&t=438s)** come back to them when you replay the YouTube video. Okay. Next, let's look at the progress in the kubric community over the past year. We've seen a lot of new contributions and they can roughly be grouped into three areas. The first is ephemeral clusters focusing on debugging postmodern analysis and recovery for show leave and failed jobs. The second is cluster management including authentication, narrow policies and end to end MTOS encryption. The third is runtime interro uh interoperability improving how ray and kubernetes work together around autoscaling asability and multi no gain scheduling

**[8:08](https://www.youtube.com/watch?v=srmgiZdIpXk&t=488s)** now I'm going to hand off to ran and ran will talk about how great community solve this challenge this year >> yeah um thank you Haru and um yeah let's talk about the progress address in the past year. Um there there are many contributions over the past year covering the three areas Henry just mentioned. Uh I will go through the key items on this slide briefly so that um you can have an idea what happened since the last year and some new features may be useful for your needs. Uh starting from the left column, we have introduced a new type of custom resources uh ray chron job which allows you to uh schedule repetitive rate job directory with cube ray and then we have promoted

**[8:57](https://www.youtube.com/watch?v=srmgiZdIpXk&t=537s)** race uh ray service incremental upgrade to beta after uh fixing a couple of H cases by the Google GK team and uh we have the history server beta which is one of the biggest joint works since the past year in the community joined by Google, Aniscale and Alibaba um to improve the debugability for infirmal rate clusters for the center column. Uh thanks to Microsoft, we finally have a better uh Kubernetes ingress API integration. This is a long requested feature that allows you to um customize more on the default behavior of the ingress object for a rate cluster. And then thanks to linkin we have the new uh embedded rox db back end for gcs for torance. Uh it is also well integrated with cube brain so that

**[9:46](https://www.youtube.com/watch?v=srmgiZdIpXk&t=586s)** you don't need to like bother with preparing not and and also babysitting u an additional radius server deployment. Um and thanks to Google uh we have native ray authentication with kubernetes rback integrated and thanks to redhead we have mtos and network policy integration for your security compliance. Lastly the right column we now support the um the new in place resizing as well as the new um kubernetes workload API for native GA scheduling. As you can see, um, many of these contributions are from Google, Microsoft, LinkedIn, Red Hat, and Alibaba. Um, it's great to see that companies coming to the Cubray community working together to address shared challenges and continue uh,

**[10:35](https://www.youtube.com/watch?v=srmgiZdIpXk&t=635s)** improving Cubray and Ray. I'm also extremely thankful to have this opportunity to stand here at Ray Summit to um, introduce all these contributions to you. Um next I think um this is the last session today. So um we want to keep the talk short. Um for the next few slides uh I will only talk a little bit more about history server and ray token um ray token authentication with cubernetes arpback and um in place power resizing integration. So um history server is one of the biggest works in cub community since the last year. A lot of work has been done to make the history server stable and production ready. We are now confident to graduate to beta in cube 1.7. We actually had a dedicated talk for

**[11:24](https://www.youtube.com/watch?v=srmgiZdIpXk&t=684s)** history server yesterday but yeah I will introduce it again at a high level in case you missed the talk yesterday. So the goal of history server is to improve the debugability of infirmal ray clusters. It helps you persist all ray logs and ray events to an external object storage and then allow you to like restore the ray dashboard after your clusters are terminated. Regarding the architecture of the uh history server, the history server is broken into two main components. the collector and the server. Regard um the collector is a sidecar running alongside your ray container which is responsible for uploading all the ray logs and events to your object storage. The server will replay those events from the storage and then serve them in the format that array dashboard understands.

**[12:14](https://www.youtube.com/watch?v=srmgiZdIpXk&t=734s)** So um you can connect your array dashboard back to the history server to inspect u the state the last state of the terminated cluster. The server itself is say this and um you can scale out the server horizontally. But to balance the latency and the cost, each each of the server instance will do its own lady zoding and in memory caching when replaying the events. Again, history server is a huge collaboration among Google, any scale and Alibaba. Thanks to them for their contribution and welcome like welcome you to try it out and please give your feedback to the back to the community and make we can make the history server bit better and the next feature is the token authentication with

**[13:02](https://www.youtube.com/watch?v=srmgiZdIpXk&t=782s)** Kubernetes and you know like uh Andrew Henry mentioned earlier we have seen more and more rate clusters running on Kubernetes and in production and more companies use cube rate to build their internal merchanding platform and usually to comply with their security needs they would need to build additional like their seven authentication around their platform to make sure there are no um unauthorized assets to to to their ray clusters but now with uh cube 1.6 6 and RAID 2.55 you don't need to you don't need that additional layer anymore you can uh authenticate RA cluster with Kubernetes arback directly uh which also means if you uh your Kubernetes cluster is configured with like OIDC or external IM uh you can use u those external

**[13:54](https://www.youtube.com/watch?v=srmgiZdIpXk&t=834s)** credentials to access the uh your rate clusters for example you can use a GCP access token to submit a rate to to a ray cluster running on GKE. The SS token will be uh checked by the will be checked with the Kubernetes token review API and then will also be checked with the sub subject assess review API to see if you have been like granted granted the assets. The next one in place pod resizing or IPR um which is a new Kubernetes feature like Cam G in the last December. Before that, pod resources are known to be immutable. But um with IPR, you can patch a running pod with a new resource requirement and limits to resize the

**[14:43](https://www.youtube.com/watch?v=srmgiZdIpXk&t=883s)** running pod while um instead of killing killing it with ray 2.56 and cube ray 1.6, the in place part resizing integration um in array autoscaler is not alpha. You can specify additional max CPU and max memory on each worker groups and then the rails scaler will try to resize those parts up to the maximum you specified before like trying to add more parts with your for your uh pending pending rate tasks. Uh this can be particularly useful because you can start with a smaller part size if not enough of resources currently available on a node but later resize up when those resource become available. Again we uh

**[15:34](https://www.youtube.com/watch?v=srmgiZdIpXk&t=934s)** to try this new integration and please give us feedback to keep improving the new feature. Um now in terms of the feature road maps there are uh many things are still in the discussion but again today we are going to share uh with you three key ongoing works that are more uh concrete and planned. First we will continue the work on the Kubernetes workload API integration. We actually um already have the first integration now with Kubernetes 1.3 36. It is a huge contribu uh contribution from Microsoft where we utilize the new uh part group object for doing native G scheduling for Ray cluster without the

**[16:21](https://www.youtube.com/watch?v=srmgiZdIpXk&t=981s)** help of uh third party Kubernetes schedulers. But um we will continue to co-work with the Kubernetes community especially to explore the new idea of composite part groups in Kubernetes 1.37 and also to co-engineering together with the with them to find a way to allow you to have more flexibility on uh customizing how pods get scheduled for red cluster including how like topology constraint are applied to pods. And next um concurrent to the integration of the native workload API like to improve to to to further improve the interoperability between Kubernetes and Ray uh we will introduce a new admission web hook in Cubray to forward

**[17:10](https://www.youtube.com/watch?v=srmgiZdIpXk&t=1030s)** node labels from Kubernetes nodes to pods and then to the ray processes so that ray applications on cube can leverage the new ray uh topology strategy API to place bundles of uh ray placement group according to node labels. Finally, we will keep improving uh obserability end to end from kubernetes to ray. One example is that we will have a new event forwarder in cube to forward node events from kubernetes to cube and then leather rate dashboard to place those u events so that you can like observe node anomalies writing your rate dashboards. So um that's all for today. I didn't

**[18:00](https://www.youtube.com/watch?v=srmgiZdIpXk&t=1080s)** cover all the works in deep details but yeah you can find all the details in our cube release notes and we'd like to thanks again to all the contributors from Google Microsoft linking redhead and Alibaba and also thanks to the other like individual contributors as well uh we welcome everyone to join our um weekly community syncs to shape the future of cube the schedule of of our weekly community sync is posted on our um Linux Foundation calendar. You can scan the QR code to subscribe to the calendar and learn more about uh our road map. Thank you all for participating to this talk. [applause]

**[18:49](https://www.youtube.com/watch?v=srmgiZdIpXk&t=1129s)** >> Yeah. Any any questions? Yeah. If you have any questions, you can come to find us at at the stage. Yeah. Thank Thank you again.
