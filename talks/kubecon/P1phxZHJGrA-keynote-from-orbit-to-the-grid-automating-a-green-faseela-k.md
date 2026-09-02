---
id: P1phxZHJGrA
title: "Keynote: From Orbit to the Grid: Automating a Green... Faseela K, Chris Holmes & Michael Reichenbach"
slug: keynote-from-orbit-to-the-grid-automating-a-green-faseela-k
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 18
published_at: 2026-03-27T06:12:35Z
video_id: P1phxZHJGrA
url: https://www.youtube.com/watch?v=P1phxZHJGrA
youtube_url: https://www.youtube.com/watch?v=P1phxZHJGrA
tags: []
transcript: true
---

# Keynote: From Orbit to the Grid: Automating a Green... Faseela K, Chris Holmes & Michael Reichenbach

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=P1phxZHJGrA) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Keynote: From Orbit to the Grid: Automating a Greener Future - Faseela K, Cloud Native Developer, Ericsson; Chris Holmes, Vice President, Planet Labs; Michael Reichenbach, Senior Platform Engineer, 1KOMMA5°

Cloud native changed how we build software. Now it is changing how we protect the planet.

As AI workloads accelerate and energy demands rise, the question is no longer just if we should act, but how we can architect systems that are as sustainable as they are scalable.

In this interactive keynote, we will take the audience on a journey through three distinct layers of cloud-native sustainability. Chris Holmes starts from orbit, showing how cloud-native processing of satellite imagery delivers real-time planetary insights. Faseela K then brings it down to sustainable cloud infrastructure, highlighting how organizations are rethinking their systems for efficiency and using CNCF projects, observability, and Kubernetes tooling to make energy, cost, and carbon visible and actionable. Finally, Michael Reichenbach connects it directly to the grid, showing how Kubernetes drives real-time decisions to optimize renewable energy in everyday homes.

This is not just a slide deck. You are invited to join a live interactive simulation using your phone. Together, we will create a virtual power plant and test our collective ability to stabilize the energy grid in real time.

Leave this session with a clear understanding of what’s possible today, what gaps remain, and what the cloud-native community can do next to build a greener future.

## Transcript

*2,207 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=P1phxZHJGrA&t=0s)** Good morning everyone. And welcome to this interactive discussion on cloud native sustainability. So in Europe, sustainability is no longer a future ambition. Which means Kubernetes and the cloud native systems we are designing are part of our planet's energy story now. So when we design cloud architectures, it's very important to think in three layers. So are we designing cloud native systems that are maximizing resource utilization? Are we making use of these systems to solve environmental challenges? And are these systems powered by renewable energy? Before we get into the details, I'm Fasiha, a cloud native developer at

**[0:47](https://www.youtube.com/watch?v=P1phxZHJGrA&t=47s)** Ericsson, a member of the CNCF Technical Oversight Committee, a CNCF Ambassador, and one of your KubeCon CloudNativeCon co-chairs. So today, I'm going to drive this discussion that basically spans three layers of sustainability, sustainability of the cloud, in the cloud, and through the cloud. So let's get started with sustainability through the cloud first. Please welcome Chris Holmes, VP at Planet Labs. Chris is from Amsterdam and he's going to share with us Planet Labs story of cloud native adoption for planet Earth. So welcome Chris. >> [music] [applause] >> So Chris, when we look at the planet

**[1:40](https://www.youtube.com/watch?v=P1phxZHJGrA&t=100s)** from the orbit, what does cloud native make possible today which wasn't even possible before? Thanks Fasiha. The answer is visibility at a scale that was unimaginable a few years ago. At Planet, we operate the world's largest fleet of Earth observation satellites. Imaging the entire Earth's landmass every single day with over 200 on orbit. The satellites generate more than 7 petabytes of data annually. All processed through Kubernetes to deliver real-time planetary insights that make environmental change visible and actionable. Our mission is to use space to help life on Earth. Let me show you what that looks like in practice.

**[2:29](https://www.youtube.com/watch?v=P1phxZHJGrA&t=149s)** In Brazil, we're working with the federal police to combat illegal illegal deforestation in the Amazon. Using our daily satellite imagery and AI-powered change detection, authorities have collected nearly 3 billion euros in fines for illegal logging and mining. Over 100,000 users across 500 institutions now monitor 8.6 million square kilometers in near real-time. Identifying illegal operations and not just assessing the impact, but giving authorities the timely insight to stop the deforestation before it finishes. We've also built the world's first global scale forest monitoring system at 3-m resolution.

**[3:20](https://www.youtube.com/watch?v=P1phxZHJGrA&t=200s)** Updated quarterly, it provides precise measurements of carbon stocks plus canopy height and cover for every hectare of forest worldwide. This is critical infrastructure for voluntary carbon markets and regulatory compliance like the EU Deforestation Regulation, enabling governments and companies to actually measure and manage their carbon impact. And a year and a half ago, we launched Tanager One, our hyperspectral satellite built with Carbon Mapper and NASA JPL. It detects and quantifies methane and CO2 emissions from individual facilities with unprecedented precision. In its first year, it detected over 5,000 methane plumes across nearly 3,000

**[4:10](https://www.youtube.com/watch?v=P1phxZHJGrA&t=250s)** sources globally, giving operators the data they need to find and fix leaks fast. So this is really amazing, Chris. So how does cloud native fit in your story? Well, with so much data coming down every day, it's a massive challenge to process it all and make it available in near real-time to our users. The only answer we found that to scale is Kubernetes and the CNCF ecosystem. We've built a fully cloud native platform running on Kubernetes with Prometheus and Grafana for observability across our entire pipeline, Argo and Keita for event-driven workflow orchestration that scales dynamically with satellite

**[4:57](https://www.youtube.com/watch?v=P1phxZHJGrA&t=297s)** downlinks, Helm and Crossplane for reproducible infrastructure as code management from dev all the way to petabyte scale production, and Backstage powering our internal developer platform for hundreds of engineers. This infrastructure enables us to process 30 terabytes daily through ML and AI pipelines, deliver near real-time insights to thousands of customers through our Planet Insights platform of web UIs and APIs, and scale seamlessly as we launch new constellations. This isn't just supporting our business, it's infrastructure for planetary scale sustainability. From predicting protecting rainforest to detecting methane leaks, cloud native architecture enable us to deliver near

**[5:46](https://www.youtube.com/watch?v=P1phxZHJGrA&t=346s)** real-time actionable data that governments and companies need to make better decisions for our planet. Thank you. Thank you so much for Chris for sharing this amazing story. And uh so this story actually highlights >> [applause] >> So this story actually highlights one thing, like we are no longer observing the planet after the fact. Which is definitely great, but that brings the next question. What what how it looks like when such massive compute is being run, how do we operate responsibly at scale? So that that's the next biggest question that comes. And that is exactly what the CNCF sustainability ecosystem

**[6:36](https://www.youtube.com/watch?v=P1phxZHJGrA&t=396s)** is tackling. So let's come back down from the orbit and now discuss about sustainability in the cloud. So this map here shows the global footprint of data centers. So for many organizations, moving from on-premises to cloud was the first step towards, you know, efficiency through better resource utilization and shared infrastructure. But then, the next question is how do we measure the impact? Organizations are now measuring scope 1, 2, and 3 emissions. Governments are including sustainability goals in public bids, which means carbon reporting is slowly becoming mandatory, and all major cloud providers are now, you know, offering carbon footprint tools as well. Within CNCF, this work becomes

**[7:27](https://www.youtube.com/watch?v=P1phxZHJGrA&t=447s)** practical. It starts with measure. So we make energy and carbon as visible as cost and latency, so that teams can see impact in their day-to-day operations. Then comes observe. Signals become insights, where waste is happening, what is improving, and where we should focus next. From there, based on the insights, we decide we get to decide scaling, placement, and scheduling policies. And then we act. We execute, right-size workloads, reduce idle capacity, and make efficiency the default behavior. And finally, we close the loop, report, repeat, and improve. Small improvements

**[8:19](https://www.youtube.com/watch?v=P1phxZHJGrA&t=499s)** add up across the entire system, and that's how sustainability becomes an operational property. And this is exactly what CNCF TAG Operational Resilience does. As a CNCF TOC member, I'm so proud to see how the TAG helped the community run some of these guidelines into repeatable practices. And it's also exciting to see other projects like Sylva under the Linux Foundation Europe making use of these guidelines. For example, using Kepler in Telco CNF deployments. So how do we get involved in the sustainability mission? So beyond CNCF TAG Operational Resilience and across the Linux Foundation ecosystem, we have got initiatives that powerful stack

**[9:09](https://www.youtube.com/watch?v=P1phxZHJGrA&t=549s)** green ops. So if you want to be part of any of these, scan the QR codes, join the discussions, and contribute your expertise. So so far, we have seen how cloud native choices shape sustainability within our platforms. So now, let's go and check how these systems are also enabling sustainability within real energy infrastructure. So now, let's move from clusters to homes. Please welcome Michael Raihan Bach, senior platform engineer at 1,5, and he is going to show us how virtual power plants are run using cloud native technologies. So welcome Michael. >> [applause and music]

**[9:59](https://www.youtube.com/watch?v=P1phxZHJGrA&t=599s)** [applause and music] >> So Michael, what happens when actually this energy systems move from static infrastructure to cloud native software? Thank you, Vassila. So, we've all been through a revolution. We took monolithic applications and broke them up into microservices. We went from one server to 1,000 containers. It was hard. It was messy. But, we've built the tools to make it work. And right now, the exact same revolution is happening [clears throat] to the energy grid. For a century, massive power plants have been powering the entire country. Burning coal, burning gas. Simple, centralized, and destroying our

**[10:48](https://www.youtube.com/watch?v=P1phxZHJGrA&t=648s)** planet. But, what if every home could become its own power plant? What if we could live on wind and sunlight forever, for free? That's exactly what's happening right now. Solar panels on roofs, batteries in basements, EV chargers in garages. Every home becoming a tiny power plant. But, here's the problem. Just like a million microservices without Kubernetes is chaos, a million power plants without orchestration is 1,5 we're solving this exact problem with the same tools and technologies whose creators and maintainers are sitting right here in the room with us. With cloud native technology.

**[11:37](https://www.youtube.com/watch?v=P1phxZHJGrA&t=697s)** We call it Heartbeat AI, one of Europe's largest virtual power plants. With over 50,000 connected systems and 4.8 million optimization decisions every single day, 1,5 is driving the new energy revolution, decentralizing the power grid. And in the last years, we've already saved over 2 million tons of CO2. That's 90 million trees, a forest stretching all the way from Amsterdam down to Frankfurt. That's really amazing to know. So, >> [applause] >> So, how does that actually look like for someone who is completely new to virtual power plants? That's a great question, Vassila. Come, join me, everyone, on this brief journey into the future of

**[12:26](https://www.youtube.com/watch?v=P1phxZHJGrA&t=746s)** new energy and the architecture behind Heartbeat AI. Everyone, take out your phones and scan this QR code. Join me in our very own KubeCon virtual power plant. And while you're connecting and stress testing the Wi-Fi, let me show you the architecture behind the power grid of the future. This is a home. There's solar panels, a battery, a heat pump, an EV charger. It stores energy. It produces energy. It consumes energy. It is a tiny power plant. And it's connected to the cloud through an IoT gateway. But, when you go from 12 power plants behind fences to 12 million power plants in people's basements, your

**[13:15](https://www.youtube.com/watch?v=P1phxZHJGrA&t=795s)** attack surface explodes. That's why we use Falco, detecting threats and intrusions across our entire fleet. Well, but how do you observe 12 million power plants? Well, the same way you would observe 12 million containers, using OpenTelemetry. OTEL is the very reason this decentralization is possible at all. It's free, it's open, and it scales to infinity. And all of this flows through Kubernetes, the orchestrator that connects every home to the cloud, to Heartbeat AI, making consumption follow production. And on our dev stack, we're using OTEL, Prometheus, and Grafana for observability, Helm for

**[14:05](https://www.youtube.com/watch?v=P1phxZHJGrA&t=845s)** deployments, and Backstage as our developer portal. This is really amazing to know about that whole architecture. So, maybe you could show us this idea live, probably how cloud native architecture is really orchestrating real energy grid. Yeah, of course, Vassila. >> Let's try. Let's get to the fun part here. So, for the next minute, you're all part of our KubeCon virtual power plant. Your phone is a node, and you are simulating Heartbeat AI. Is everyone connected? Good. Then let's have a look at the day in the grid of the future. Today, we need to use a little of imagination. Let's just imagine it's a sunny day in Amsterdam. The wind is blowing hard, but there is so much clean energy that the grid can't

**[14:53](https://www.youtube.com/watch?v=P1phxZHJGrA&t=893s)** handle it. In the old world, we would shut down wind turbines, disconnect solar parks, waste that free and clean energy just to keep the grid stable. But, we saw this coming. You saw this coming. Our batteries have the space, and we were waiting exactly for this moment. On your phones, tap charge. Store that clean energy. Relieve the grid of its stress. And as you do this, you can see that Heartbeat AI is sending out thousands of individual signals to the nodes in our virtual power plant, filling our battery with clean energy. But now, the day is coming to an end. The wind is

**[15:41](https://www.youtube.com/watch?v=P1phxZHJGrA&t=941s)** dying down. The sun is setting. People are coming home. Demand is surging. In the world of old energy, we would burn fossil fuels to meet demand, blowing CO2 in the atmosphere, polluting our planet. But, our batteries are full. We have our cars on charge. We have the energy. Let's give it back. On your phones, tap discharge. Give that energy back to the grid. Help me stabilize it again. What you just did is what Heartbeat AI does 4.8 million times a day. And we're just getting started, orchestrating the power grid of the future, always providing the cleanest and cheapest energy.

**[16:30](https://www.youtube.com/watch?v=P1phxZHJGrA&t=990s)** That is the power of cloud native technology used for good. The same tools we use to scale our applications, we use to scale clean energy, living on wind and sunlight forever, for free. Thank you. Thank you. Thank you so much, Michael. So, >> [applause] >> with that, we have seen sustainability over the three layers of cloud, sustainability of the cloud, in the cloud, and through the cloud. And together, let's make sure sustainability is a default property of cloud native systems. And with AI being everywhere and being part of every stack, let's not forget to ask the question, how green is your prompt? And before we wrap up, we would like to

**[17:19](https://www.youtube.com/watch?v=P1phxZHJGrA&t=1039s)** thank everyone who helped us shape this keynote, CNCF contributors and maintainers, the events team, and our friends and colleagues who supported with our visuals and reviews. So, thank you once again, and enjoy the rest of KubeCon. Thank you. Yeah. >> [applause]
