---
id: XiNsfhUxO2Y
title: "From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat R... Willem Berroubache"
slug: from-logs-to-decisions-autonomous-ai-agents-for-real-time
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: []
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 18
published_at: 2026-04-09T05:17:23Z
video_id: XiNsfhUxO2Y
youtube_url: https://www.youtube.com/watch?v=XiNsfhUxO2Y
tags: []
transcript: true
---

# From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat R... Willem Berroubache

**Speaker not identified**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=XiNsfhUxO2Y) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat Response - Willem Berroubache, Orange

Cloud Native environments evolve faster than traditional security can handle. This session introduces an open-source, autonomous AI agent architecture leveraging Kubernetes, Kubeflow, and lightweight protocols like A2A and MCP to deliver real-time, adaptive threat detection and response. Agents collect signals via OpenTelemetry, Falco, and Prometheus, correlate behaviors using ML models trained in Kubeflow, and reason about threats like account takeover, lateral movement, or privilege escalation. Integrated with policy engines like OPA and Kyverno and GitOps workflows, agents can trigger secure remediation actions such as rollback, isolation, or misconfiguration fix. Each decision is transparently explained via contextual LLMs, ensuring auditability and trust. Attendees will leave with practical templates, deployable AI pipelines, and actionable strategies to build explainable, autonomous, and scalable Kubernetes-native security defenses using CNCF and OSS technologies.

## Transcript

*1,995 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=0s)** In this session we're going to speak about AI agent security Kubernetes of course and how we can use all the solution against threats hacker and so on to protect our environment cluster and customers. Is there some people here who works on security topics and agent topics? No? Okay. Okay great. So just to quickly introduce myself. I'm William Burbage. I'm working for Orange in Paris. Today I'm an architect. I'm designing some security solution for security monitoring detect threats attackers hackers to protect our customers

**[0:51](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=51s)** infrastructure and I'm trying to add some AI security feature to protect and improve the security monitoring this architecture in our environment. In the past I I worked in 5G information system for network edge production Kubernetes cluster and I'm also the trainer for Orange Group one of the different trainer for Orange Group on Kubernetes and cloud native solution. So just a quick disclaimer. All the things you will see during this session is unfortunately if I can say it like that

**[1:40](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=100s)** based on different true story and it's not a fairy tale. So let's start. There is a big gap between what we expect about security from our partners and what we can have in our different environment and we all know this case where some people said yeah we are secure. Yeah, we are cloud native and so on. But if you check if you are looking what you can have behind all this environment solution and so on sometimes you can have legacy stack all feature

**[2:28](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=148s)** and if you are going to check and audit what you can have you can for example have a lot of CVs. Okay? So you are going to check exactly how they can deploy the application the animal file the helm chart and so on and trust us sometimes it's not very beautiful. So with all these problems we can have some breaches in our infrastructure and this a direct threat for customer trust user data and Orange environment. So the audit is great. Okay? But runtime monitoring is non-negotiable

**[3:18](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=198s)** because the audit say okay you're secure with this release in this version. But you need to prove you're real you're really secure in production. So okay. During security audit you can check our bug CVs and so on. Okay, but the hackers can try to exploit your application to find some exploit. Okay? And for example destroy your application. So you will check the application the manifest the helm chart all the declarative information to deploy this application but it's just the map. Runtime events are the real world general. So

**[4:05](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=245s)** we have full stack observability of course in our different environment. It could see the pod bridge the security issue but we need to understand to see how we can improve this automatic detection and have immediate remediation. So the threat is life. Okay? And the defense should to be too. So sometimes security and not only security operation could breaks at scale because we have a lot of logs we have lot of events lot of metrics alarm and so on and we can have some fatigue with because everything could fire. Okay? No signal

**[4:56](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=296s)** matters and people could mute the alarm. We have some event which are visible but the threats could be stay invisible. Okay? So that's why we're trying to improve the context to better to have a best understanding with this different alarm to don't be blocked to take some decision. Okay? And avoid remediation lag with manual fixes slow response and all these elements raising the risk for our environment and customer. So the idea to use AI and to silence the noise understand all the signals

**[5:45](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=345s)** and automate the response. So AI is not just a tool. It could be the brain of our different infrastructure was missing. Today we have a lot of a lot of tools a new protocol like A2A MCP cloud chat GPT and so on. So we need to try the best product the best solution to improve our operation our security operation and detect the threats. So the idea here is to use different agent different tools to improve the detection. So we collect a lot

**[6:36](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=396s)** of data with logs metrics alarms from elastic from a few tools and so on. You know all the observability stack on the CNCF landscape but we need to use all these data to detect some security events. So we have Falco for example. Okay? We can get all this message all the event try to correct to correlate sorry with application logs with some machine learning model isolation forest and so on to detect if it's an abnormal behavior and then send them to our different agent. Here we have the coordinator agent.

**[7:24](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=444s)** This agent will talk to the threat and the list agent with A2A. This agent will collect different information different event to say and try to give you this information if it's a real threat to give you some information about matter attack matter of fact if you work on 5G environment and so on and then pass this information give this information to this remediation agent. This agent deploy in different cluster will help you to understand which tools you have in your environment offer you the best remediation possible. Okay?

**[8:10](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=490s)** And then will send this information this coordinator will send this information to the notify agent. You can use matter most slack teams and so on. There is a lot now of tools in the market to send this information to operational people. Okay? To help you to give you the remediation and know what to do against this threat this attacks. Okay? And to approve this remediation. Okay? To keep human in the loop. Okay? To have a feedback loop on improve this detection. Okay? And it allows teams to validate and to take the right choice. Okay? So

**[9:01](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=541s)** Finally there is three big axes feedback loop training pipeline. Okay? To improve the detection work signals and so on. Okay? And real time inference to have more context more understanding against against the threats and take the right decision. Okay? So here it could be an example on what we can have in an alarm. We have a a little demonstration just after. So you can have the pod the name of the pod. Okay? What happened? Justification impact of if it could be a false positive. So totally straight side we have developed a web application

**[9:50](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=590s)** based on real vulnerability. We continue to fight in 2026 unfortunately. So this application is like a shop where you can buy some swag and so on. You can try to bypass some security feature and so on. Okay, so here this is your orders. So you can use this web interface maybe to inject some command. Here nothing. No order found. But if you check the response of the server you can list the file in this container. And yes in some environment we have this not in production of course, but some product could have this security issue. And we don't want to be to to have these

**[10:40](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=640s)** vulnerabilities in production. So okay, let's continue. Let's try to list the files, get some secret rights and so on. Okay. I can have the file in ETC directory. Let's try to get all the file paste W paste W D shadow and so on. Okay. So we have some security issue. We have an alarm. Okay. A shell spawned in a container with a a command injection. And we can have what an attacker could be do with is this exploit. We have what happens, justification and so on. Okay. So now let's do something else. So we know we can now inject some command. So let's

**[11:30](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=690s)** try to send in this container a crypto miner to be rich. Why not? So now we will have a new alarm because we are continuing to injecting some commands in our container. Okay. And we are downloading a crypto miner. So now we have all the path all the chain to understand what the hacker have done in our application. Okay. It allows us it allows us to have a deep understanding of what this guy is doing in our environment. Okay. So great. Now we have

**[12:17](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=737s)** new alarm. Okay. With XML. Okay. Crypto miner. Okay. With the previous alarm that we can have here and what happened, first positive present and so on to have a deep understanding of this alarm. Right. So here crypto miner as you can see and the response. So what to do now to protect our environment against this attack. So here you will have a more detail explanation about this remediation, how to implement it. Okay. And you can have the choice to approve it or not. Okay. Because we know sometimes

**[13:03](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=783s)** I can give you not very beautiful remediation. So keep human in the loop and approve it. So we have the attack the path, what could be the impact. Okay. So now apply this remediation. Our agent is working to implement all this remediation. So now okay everything seems to be okay. So let's check in our cluster what we have. So we have label now threat detected here. Let's stop. Okay. Great. So now we know in this container in this pod we have a threat. Okay. And let's check the other remediation implemented here in this container.

**[13:51](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=831s)** Cilium network policy to isolate and block the ingress traffic. So now the crypto miner could not send the information. Okay. What else? We have a vulnerable image. Okay. So now we have a policy with key word now to block now this image to prevent new deployment of this vulnerable application. Okay. So Some practical outcomes about that say it's allows teams operational teams to have a contextual fidelity with cluster set cluster set tool set. Okay. And

**[14:39](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=879s)** we can eliminate some operation noise to be focused on real attacks, real incident. And it will assist the teams during the defense because you can have fast commitment block the application. Okay. And keep human in the loop to validate this remediation. It allows for one sec teams and help them to have this even correlation history for deep investigation. So today we are continuing to finalizing this robustness the solution. And we will test it in more sensitive environment.

**[15:27](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=927s)** So we know I I can have some risks. Okay. Hallucination, cascading errors model drift, overconfidence effect and we have human safeguard. So we have ethical judgment. Okay. Context awareness of your company environment, human oversight and validation. So that's why today is still very important to keep human in the loop. Okay. So agentic AI is a new operating paradigm. So we can offer scale and speed to the different teams, the different

**[16:15](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=975s)** project, the different environment. Humans have great judgment. And AI could help you to be and process all these alarms elements and so on. So classical automation execute some rules based on trigger, environment, message and so on. Okay. And agentic AI could help you to understand the goal. Okay. Choose the tools and adapt to your context. It's like a new primitive stack because agents are ones plugins. Okay. It's like a new layer. So containers change deployment.

**[17:03](https://www.youtube.com/watch?v=XiNsfhUxO2Y&t=1023s)** But agents could help you to change your operation be more efficient. So agentic AI is a new paradigm and the real challenge is how we adapt it. Thank you for this session. If you have some question if you want to follow this topic, don't hesitate to send me emails to reach me to send me message and LinkedIn and so on because I think we have some great things to do with this topic, to share some code, some resources some resources and feel free to reach me. Thank you everyone.
