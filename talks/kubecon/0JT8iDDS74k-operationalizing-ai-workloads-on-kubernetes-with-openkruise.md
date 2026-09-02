---
id: 0JT8iDDS74k
title: "Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen & Vec Sun"
slug: operationalizing-ai-workloads-on-kubernetes-with-openkruise
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Zhang Zhen", "Vec Sun"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 20
published_at: 2026-04-09T05:24:09Z
video_id: 0JT8iDDS74k
url: https://www.youtube.com/watch?v=0JT8iDDS74k
youtube_url: https://www.youtube.com/watch?v=0JT8iDDS74k
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen & Vec Sun

**Zhang Zhen, Vec Sun**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=0JT8iDDS74k) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Operationalizing AI Workloads on Kubernetes With OpenKruise - Zhang Zhen, Alibaba Cloud & Vec Sun, Xiaohongshu(RedNote)

AI workloads on Kubernetes face unique operational challenges: container images packed with large models and libraries require pre-warming for fast startup, and distributed training jobs often run as PodGroups that must be scheduled and disrupted together. However, native Kubernetes lacks group-aware disruption handling—PodDisruptionBudget treats pods individually, risking partial job failures during node maintenance or hardware issues.

In this talk, we showcase OpenKruise’s solutions: (1) cron-based image pre-warming to proactively cache AI images on target nodes; (2) an advanced disruption policy that enforces availability constraints at the PodGroup level; and (3) upcoming enhancements to ContainerRestartRequest to support planned, in-place restarts of entire PodGroups—rebuilding only necessary pods while restarting others inplace. These features enable reliable, efficient AI workload operations on Kubernetes at scale.

## Transcript

*2,622 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=0JT8iDDS74k&t=0s)** Uh okay let's start. Hello uh hello everyone. Uh I'm John from open cruise from open cruise community. Uh yeah I'm the maintainer and today I will share with you uh how some some experience and features we provide in open cruise and its sub projects to operate to operate the AI workload. Uh we uh we have some outlines here. First I will introduce some the challenge of the AI work clothes including the uh training inference and agents and then I will go to the the different the operations for different kind of of applications. Yeah. Uh actually there are two kinds of

**[0:49](https://www.youtube.com/watch?v=0JT8iDDS74k&t=49s)** application from my point of view. First is that the training and inference. Yeah. They just contains a lot of datas. Yeah. Mostly in most uh uh practice some of will put data or in in the image and use the image as a as a as a source of data and then the horse will just some of the training or inference will just run and die in groups because they rely on some some uh some communication library uh such as nickel sometime such some something like that also the this application may rely on some devis that that is slow to allocate uh for example they need to allocate the GPU or some uh

**[1:40](https://www.youtube.com/watch?v=0JT8iDDS74k&t=100s)** high performance uh comm communication devis the second type of agent uh application is agents or it's related sandboxes uh for agents uh or especially agent sandboxes they need a very fast creation uh demands. Yeah, they mostly need they need to get the sandbox under one second. And then another thing is that the the command and file system operation is a must for this uh for for the agents because the agents may need some do some uh op do some uh token injection or some file system operation uh preparation uh before do some code uh code generation or code code running.

**[2:30](https://www.youtube.com/watch?v=0JT8iDDS74k&t=150s)** And third is that uh now with agent sandbox uh many many operation previous happens in the virtual machine now becomes a master for for the containers things like hibernate and resume become a must. So we have to deal with that. Uh the first operations I'd like to introduce is impl update. uh it is actually can be used for faster inference uh inference service update. Uh I'd like to introduce some the concept of in place update. Uh in previously if you want to update a a port in Kubernetes you just uh delete the port and just recreate the port. Uh in in such cases you get a new port uh you get

**[3:19](https://www.youtube.com/watch?v=0JT8iDDS74k&t=199s)** a you get the new IP and then he he may schedule to a different node. Uh yeah with imp place update you just it doesn't delete the port at all. It just delete one of its containers. So K will just recreate the container uh so that actually we can just reuse many of the resources already prepared uh in the in the pre in the node. For example uh additional cost of scheduling IP allocation and volume mounting is just saved. Uh another thing is that we can get much faster image pooling because when we do some upgrades because the nature of kubern uh do uh docker images most of most most of the time we can

**[4:06](https://www.youtube.com/watch?v=0JT8iDDS74k&t=246s)** just re reuse the the the button layer of the image so that we can only pull several new layers. Yeah. The third is that when a container is in place update other containers for example side cars can kept running so they don't need additional initialization. The in place update uh operation is actually integrated by uh several several inference engine. Uh one example is that uh in SE lands community uh recently they have as a role-based group project uh which introduced the idea of the implicit update. Yeah, they just take the same uh idea from open cruise. Yeah, just implement them in the in the

**[4:56](https://www.youtube.com/watch?v=0JT8iDDS74k&t=296s)** RBG. Another another operation is image prewarming. uh just remember that because the now now the now now the image contains not not only the the application binaries but it also contains data contains modules models. Yeah. So it can be quite large to speed up the the inference or training drops you have to get prepare get a note to prepare the some some of the image. uh one can just use some fancy uh image speed up technology for example peer-to-peer downloading or just on demand uh image downloading. Those technology just works but uh maybe not

**[5:46](https://www.youtube.com/watch?v=0JT8iDDS74k&t=346s)** very useful for some some case because uh because of the environment or or the ability of your uh your vendor or because you're just in the on pre on premier premier environment. Yeah. So here the image pre prewforming is one of the most basic and most generic way of to uh to image speed up. Uh yeah, open cruise project uh pro provide API in the form of custom resource customized resource. It called image pool drop. In the in the this CR we can provide the desired image uh some of the image downloading parallelism and the related node or port labels to to pull. Yeah, with image pool drop uh the

**[6:37](https://www.youtube.com/watch?v=0JT8iDDS74k&t=397s)** open cruise demon run in every node we'll just pull the related image beforehand so that when the ports get uh the real port get scheduled they can get every image is already already there almost no image downloading uh required uh with image prewarming and because the image can get a garbage collection marketed by by Kublet. Uh especially in a very high professor uh high loading environment. Yeah. Like some training uh training environment uh the image can get garbage collected. So sometimes we want we have some scheduled uh job run once in a while but we know in advance

**[7:27](https://www.youtube.com/watch?v=0JT8iDDS74k&t=447s)** that this job requires some very large images and so we can just just before run those uh schedule drops we can firstly do a schedule the image prewarming. Yeah we also provide uh a chrome droprop which in our case called advanced chromedrop. It has a template uh called image list pulldrop template. Yeah, it it contains a list of images to be uh pre uh pulled and as a schedule field which can just uh one can just use the chrome tab chrome tab syntax to specify when uh when to download these images. uh use using this using these features

**[8:16](https://www.youtube.com/watch?v=0JT8iDDS74k&t=496s)** uh one can just uh can works with those uh maybe chrome large chrome drops to ensure these drops can just run very efficiently. Uh another another operations that we want we are just working on is that some of the the job maybe uh not only job also for the some inference service uh some of the inference may need multiple uh TPU from multiple nodes. Yeah. So so usually the this kind of inference service and they need multiple groups of ports. each group of ports just will just uh just runs and dies in the same times. Yeah, they form a port group. But

**[9:06](https://www.youtube.com/watch?v=0JT8iDDS74k&t=546s)** in sometimes when one port in a port group just uh has go goes wrong for some some anomaly happens in the nodes. Yeah, in in such cases the port uh actually this this whole port whole port group actually is inavvailable uh in the sense of these applications. uh if in the meanwhile another port uh in the another port in another port group for example here in the group one uh if there is a non non-critical uh anomaly happens in the nodes and the and some controller will try to evict these ports from from the nodes and then the whole inference service in the sense of maybe like a

**[9:54](https://www.youtube.com/watch?v=0JT8iDDS74k&t=594s)** little work set it will just not have enough enough uh inference service running to uh to to respond to the user user prompts. So in such kind of things uh actually it needs some kind of port uh disruption budget but in the not to the single single port but to the port of group. So uh we actually we are having uh a proposal and a working uh a working patch that are working on this problem. Uh we have introduced a pause group policy. We have a label to to just describes all these all this what is what is a related pause group. So we have a just a label for the group. So,

**[10:45](https://www.youtube.com/watch?v=0JT8iDDS74k&t=645s)** so that in this case if one if group zero is down and one uh and one group one and group two any port in group one group two uh receive a voluntary disruption uh request it will be just uh rejected by the port unvailable budget. So protect the inference service from uh from un from those to unavailable. Uh the third operation actually we are just discuss uh with the community also uh with the the sig batch community. Uh the problem is that uh let's focus on a a group of ports. Yeah. If the single port single port in the port group get

**[11:34](https://www.youtube.com/watch?v=0JT8iDDS74k&t=694s)** fails because some anomaly actually uh they will just caused that the whole port group got recre recreated in such kind of things maybe that all these port pods recreation were just cause of the cost of all these port group recreation is very high. they get they need to get uh get a scheduleuler uh to get GPU and um highspeed network get allocated and so it will just take a lot of time. So uh so this community have come up with some solution. He will just uh recreate the the the ports that that is that is fail because like worker one which maybe notice uh node goes wrong. So we can just recreate them. But if

**[12:25](https://www.youtube.com/watch?v=0JT8iDDS74k&t=745s)** worker two and worker three, it's actually healthy. But we have to recreate them. Instead of recreing them, we just in place restart these containers. So that the for in a in a cluster point of view only one port is get rescheduled. Uh so that everyone is much uh much easier to to face this condition. uh actually this solutions rely on on one features which in recent kubernetes recent kubernetes it's called restart all containers it's a feature uh that can enabled in pre restart uh the but the problem is that in such uh in existing solution which is proposed by the Google it need a sidecar called a water side car is that if the another

**[13:15](https://www.youtube.com/watch?v=0JT8iDDS74k&t=795s)** port in the port group like a worker one in the in the in the above cases what the watcher side of coin worker two and three must somehow get a signal that the another another port in the port group is fail. So need to watch the watch the the failure conditions and and try and and then uh exit in some some ways so that the Kate will try to uh in place restart all container in in walk two and work three. So what if there's no water class and what if the training framework doesn't doesn't aware of the framework so it actually will fail. Yes. So we are trying to uh recraft uh the new container recreate API which will just

**[14:06](https://www.youtube.com/watch?v=0JT8iDDS74k&t=846s)** uh using the uh cruise stemon to uh to just recreate the container without without introduce the water side cost. Okay. Uh time is tight. So let's go faster. Uh I also introduce our new project called urban cruise project. Urban cruise agent. It's a uh uh a sandbox solution. Yeah, it solves the problem of of of sandbox allocation and state persistency and and uh AI AI friendly API exposures. Uh it has uh several key components like sangle manager which is both E2B and MCP related API and samball gateway which is envelope filter based efficient routting

**[14:55](https://www.youtube.com/watch?v=0JT8iDDS74k&t=895s)** capability. Another assemble controller which supports uh samples hibernation and wake up. Uh the sample sample life cycle now gets actually get extra states uh which is different from the ordinary ports. the port can get a paused or can we can get a snapshot of the running port so that we can just uh clone clone clone the ports to other other to other sandboxes. Okay. Okay. Oh yeah. Uh we have also have some uh sample clay operation which just try to fetch uh dispose samples from the warm pool which will greatly uh speed up

**[15:44](https://www.youtube.com/watch?v=0JT8iDDS74k&t=944s)** the sample allocations. Actually we can get uh we can get a samples in almost 20 milliseconds which is way much faster uh than even the some of lightweight microvm. Uh yeah, we also introduce a sample gateway and uh also a sample runtime inside uh inside inside the the port which just serve some command execution and file system operation. Yeah. So uh yeah uh we also introduce some uh pause and resume operations. uh in po if one sandbox is paused uh we can just save the the the root fs and the memory uh so that save them for example in in a

**[16:34](https://www.youtube.com/watch?v=0JT8iDDS74k&t=994s)** shared storage uh so that we can just restore them uh from shared storage the the the real use cases is that for some agent applications uh the the agent will just wait for some user uh user input put or just wait for the uh other agents to to give some task. So most most of the time actually is idle. So we can just just um put them into hibernation and just save the cost. Another is checkpoint. Uh we when the checkpoint is quite similar to pause and resume but for checkpoint we can just uh take a snapshot of the uh sandbox and save them in a shared storage then then clone multiple uh replicas of the previous

**[17:24](https://www.youtube.com/watch?v=0JT8iDDS74k&t=1044s)** sandboxes. Yeah, it's actually perfect for to to do some agent uh backup before before upgrades. For example, you can do some backup for for up before upgrade open core services. Also, you can just use uh use checkpoint to do some application startup speed uh speed up operations. Also, we have a commit. Uh in checkpoint, usually we save some uh private uh shared storage. But with with commit actually it's kind of customary resources by open cruise agents what it do is actually it just do a docker commit so that the the root fs of the container get saved in the image

**[18:13](https://www.youtube.com/watch?v=0JT8iDDS74k&t=1093s)** and so that one can just push them into some registry and maybe debug the uh symbols locally or just in your in a different classes. Uh okay. Uh so uh I we have uh open crew has just has a kiosk uh in the project pavilion and so every if everyone is interested in in our in our works you can just meet us there and here is QR code here. Yeah. Thank you. Any questions? Please.

**[19:12](https://www.youtube.com/watch?v=0JT8iDDS74k&t=1152s)** Um at the beginning of your talk you were talking about pre uh warming yeah um >> the um images. >> Yeah. >> Um what about um obviously this is for serving and and speeding up uh um >> getting your containers um sooner ready. >> Yeah. >> So what is the um consequence in terms of cost when you uh when you do that? uh to cause that maybe actually will get your local disk maybe in a very uh they cause a lot of storage spaces and may increase some IO load in your local disk. Yeah, that's maybe the the cost of this pre-warming. Yeah.

**[20:12](https://www.youtube.com/watch?v=0JT8iDDS74k&t=1212s)** Okay, thank you.
