---
id: uFgB_aMw5-g
title: "Black Hat Asia 2026 | Large-Scale macOS PID-Domain Vulnerability Discovery with LLM Reasoning"
slug: black-hat-asia-2026-large-scale-macos-pid-domain
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2026
speakers: []
channel: "Black Hat"
duration_min: 25
published_at: 2026-08-29T14:30:03Z
video_id: uFgB_aMw5-g
url: https://www.youtube.com/watch?v=uFgB_aMw5-g
youtube_url: https://www.youtube.com/watch?v=uFgB_aMw5-g
tags: []
topics: ["Governance, ethics & regulation", "Security, safety & red teaming"]
transcript: true
---

# Black Hat Asia 2026 | Large-Scale macOS PID-Domain Vulnerability Discovery with LLM Reasoning

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=uFgB_aMw5-g) · [Conference site](https://www.blackhat.com/)

## Description

For years, macOS researchers have focused on high-privilege system and user domain services—yet a vast class of background daemons has quietly operated beneath the radar: PID-domain services. These processes, often reachable even from sandboxed apps, expose privileged functionality and sensitive system controls. Despite their enormous attack surface, they've remained largely unexplored and unprotected—until now.

In this Briefing, we will unveil the first large-scale automated framework for discovering logic vulnerabilities in PID-domain services, powered by LLM-assisted static analysis. We will start by dissecting historical flaws and Apple's patching patterns to formalize a repeatable attack model. Building on that foundation, our framework automatically enumerates connectable PID-domain daemons, decompiles their exported APIs, and leverages LLM semantic reasoning to classify sensitive operations across five categories—from file and privacy access to interprocess privilege crossing. We then map entitlements to these operations and apply taint analysis to trace attacker-controlled data into privileged sinks—surfacing hidden logic flaws that manual auditing would almost certainly miss.

Our evaluation uncovered 12 previously unknown vulnerabilities, including multiple sandbox escapes and TCC privacy bypasses—six of which have already been assigned CVEs by Apple. This research exposes a massive, underestimated attack surface within macOS's userspace and demonstrates how LLMs can be weaponized for scalable vulnerability discovery in closed-source ecosystems. Attendees will gain new insights into Apple's userspace attack surface, automated bug-hunting methodologies, and the next frontier of human–AI collaboration in exploit development.

l_m_h l_m_h  |  Independent Security Researcher
Yinyi Wu  |  Security Researcher, Dawn Security Lab, JD.com
Yingqi Shi  |  Security Researcher, DBAPPSecurity
Yuchong Xie  |  Security Researcher, The Hong Kong University of Science and Technology
Cheng Li  |  Security Researcher
Yizhuo Wang  |  Security Researcher

## Transcript

*1,887 words · source: supa (en, exact timings)*

**[0:10](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=10s)** Hello everyone, welcome to our section. Today we are thrilled to present our research AI in the loop large scale Mac OSP domain vulnerability discovery with large language model reasoning. This is a joined effort by our teams of independent security researchers down security lab from Jingong DB app security and the Hong Kong University of Science and Technology. Our agenda today covers five main parts. First, we will start with the fundamentals of the Mac OS sandbox and service navigation. Second, we will dive

**[1:00](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=60s)** into a previously overlook chop scone attack surface. Third, we will introduce our large language model assist automatic vulnerability discovery framework. Fourth, we will showcase our evaluations and the real world impact sharing the results of our largest scale analyze and responsible disclosure. And finally, we will conclude with key takeaways. Let's dive into the first part background and the fundamentals to fully grasp the vulnerability. we will be discussing today. We first need to quickly review how Mac OS handles

**[1:51](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=111s)** process isolations and service delegation and let's start with the basis without the application sandbox and net has restricted access to all user data and system resource. However, with the sandbox enabled, an app is strictly isolate. It can only assess its own user data and system resource. So the question aris apps assess other system resource when necessary.

**[2:43](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=163s)** The answer to this question lies in the service delegation model. Let's break down how it works step by step. It starts with a request. This is usually an app running inside street application sandbox. Suppose this app wants to assess an external system resource because of its limit privilege. It cannot do so directly as you can see by the rack X. Instead, it must initiate a request. This is where the dep comes in. To solo the permission issue, Mac OS introduced

**[3:31](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=211s)** a private system service to act as this deputy. It job is to step in, receive the request and actually perform the restrict operation on behalf of the cing app. But how do they communicate? This digation is achieved by interprocess communication and the MAC blast is ecosystem. This is primarily done using XPC. The restrict app safely send it request this XPC boundaries to the dep key service. And here is the final outcome.

**[4:27](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=267s)** The privilege deputy service successfully assess the target system resource using its own higher predictions and then hands the result back. So ultimately through the delegation mechanism the send both the app indirectly g access to the restrict data. Now let's focus on a specific types of service P domain service. These are incredibly prevalent making up about 40% of Mac OS assisting service. When an app register a P domain service, it is registered directly into the app's

**[5:16](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=316s)** own namespace and the service is launched with the exact same execution connections as the calling application. It is dynamically responded specific to server this pack. But what about is it send boss context as they communicate vy xpc the p domain service runs under a specific sandbox profile depending on its configuration. It runs either inside a case service sandbox or directly inside application sandbox.

**[6:09](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=369s)** This is a critical detail especially the fact that a privilege service might be operating within the ex that same sample boundaries as our unprivilege app. Keep this in mind as it sets the stage for our attack surface. With that foundation in place, let's move to the c of our research. We call this the chov scone attack surface. We are not the first to look at p domain service. There is excellent previous work in this area. Specifically, we want

**[6:59](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=419s)** to highlight MC Jin's research at PC 2024 and force 2020 findings regarding XPC service abuse. Let's look at MC's approach. The identifier specific API bundle with pass which made Apple's internal P doain service accessible by targeting the service samples of this service. We successfully achieved samples escaped and uncover over 10 new vulnerability. Before that super port focus on a different API XPC add bundles he use a pass traversal chick to break past

**[7:52](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=472s)** constraint allowing him to register a third party P doain service directly into a root process retrieving provide excavation. Now here is the interesting part. Both of these APIs despite looking difference share the exact same lowle launch in li xpc dynamic library. They both ultimaries send message to launchd. This brings us the question why is there a fiery gap between these two discoveries? Why did this massive attack surface remain largely untouched for so long? We believe it stem from a difference in

**[8:42](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=522s)** research scopes and perspective. Unlike previous search focus on service sets, we shift our perspective. We focus on P domain service running directory inside exact same application sandbox as the caller. This leads to our cause problem. If both run in the exact same samples, why can the service assess assessed data that the app cannot? The answer is entitlements

**[9:31](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=571s)** beyond send post restriction. Entitlements act as hiden keeps that grand higher privilege. Entitlements are embedded code signature. When the service tries to access the restrict data, the system check it entitlements because the service has done the assess is granted. The calling app simply knock this signage. This re reveals a messy overlook attack surface.

**[10:21](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=621s)** Malicious apps can use XPC to trick this very legit service into doing dirty works for them effectively exploiting this subto entitlement difference. So the ultimate question is how can we systematical and automatically uncover this vulnerabilities escape to answer that exact question and turn this west of the text surface into concrete fightings. Let's dive into our core solution in large [clears throat] language model static analyze framework. We designed an large lamb model assist

**[11:16](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=676s)** static analyze framework with three phase. First identify the source the exposed XPC APIs. Second defy the same inferring page from entitlements to map sensitive function. Finally, hence checking verifying if data flows from our source to the sync to find valid source. We must first fit out secure service.

**[12:06](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=726s)** We observe that secure service always verify course entitlements and the success flag is aside multiple times. So we perform a backlo data flow analyze to detect these patterns and exclude them. Next, we identify the export APIs because they are defined in the NSXPC protect. We automatically locate calls to interface with protect to extract exact

**[12:57](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=777s)** API names. for since previous blocks relate on incomplete manually collect list. We improve this by extracting the compile function data and leting and large language model automatically construct a comprehensive sync list all covering both sandbox and TCC operation. We then built an entitlement capability

**[13:47](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=827s)** table. We combined Atlas public documentation with our provide data using enlarge language model automatic with retrieval automatic generation. We automatically infers the edge capability granted by each entitlement. With both list ready, we again leverage the large language model. This time using noiseware and selfrefraction property to map which sync function expose which entitlement capability. Finally, we implement a light where

**[14:44](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=884s)** static tent propagation engine. It builds a C graph and simulates check data flows across C function object C massive and block call. Now that we had walked through how the large damage model assist framework operates, let's look at the edge results we produce. This brings us to part four evaluations and real world impact. We deployed our automate framework

**[15:35](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=935s)** across the Mac OS ecosystem and the results were highly reint. Our analyze identified a total of 300 P domain service. want this connectable service. We discovered nearly 2,400 expose APIs by applying our automate mappings and tent tracking. pinpoint multiple zero date

**[16:24](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=984s)** vulnerabilities. We report this findings through Apple's responsible disclosure process leading to the acknowledgements of 19 vulnerabilities and the issuance of seven seniors so far. Let's dive into three specific real world case study. This first vulnerability occurs in the CM varate movie data reference service XPC components

**[17:13](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1033s)** within the core media framework. This XPC operates within its own service box. If we look at it as Sos profiles, we know it's something critical. It is explicited granted permissions to read all files and issue read only extension. When analyzing the XPC server, we found that it receives a fire pin

**[18:04](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1084s)** from the client. Because of its higher privilege, the service directory caused the sandbox extension issue fire to generate or read extension for this specific fire and then simply returns this extension back to the requesttor. Why is this dangerous? The answer is a sandbox extension functions essentially like an authorization token. Since this service can read any fire, it

**[18:55](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1135s)** can issue a token for any act fire on the system. a local um private process can consume this return token to get access to that specific file. Ultimately, this creates a clean sandbox escape vulnerability allowing for up toate fire risk. Our second case is located in match measurement helper. Looking at should set new connection delegate. You can see it hard codes and return truth.

**[19:45](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1185s)** This means the XPC can connect directly without any entitlement validation. Once connect, they expose several NSXPC APIs that any requesttor can invoke. The one that catch our attention is the terminaliz process method. Using our framework's capability mapping we observe that this termin is directly related to a highly privilege entitlement

**[20:38](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1238s)** by reversing the API implementation. We found that this API receives a process named from the client and leverage the underlining private mechanisms to kill it. The result an entirely unprivileged sandbox app can simply pass a process name to this API and successfully cute a root process. Our final case exist in the distribution helper of the distribution kit framework. Note two things here. First this XPC service once completed

**[21:29](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1289s)** outside the sandbox. Second the connection validation method also returns true meaning any client is allowed to assess it. Examine the distribution helper tackle. We found only a single method. It's called logic relies on quantify control to to determinate whether a files is in an APFS graph state to check the component is granted an inote

**[22:19](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1339s)** provides Apple entitlement. However, if the fire control call fails, for example, when the target fire does not existed, the callback function returns the specific error values. Consequently, an attack can use this behavior as an oracles and um private sandbox app can query actuate fire past and based on the return errors deduce whether a fire exist here or not. As this three real world case demonstrates

**[23:07](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1387s)** this overlook attack surface can lead to severe consequence from arbitrary bias release to curing root process and with that let's write up our sections and move to the conclusion. To wrap things up, we want to leave you with three key takeaways from our research. First, P domain service expose a message. Previously, it's overlook user speak attack service on Mac OS. Second entitlements acts as the true hiden career legit boundaries

**[23:55](https://www.youtube.com/watch?v=uFgB_aMw5-g&t=1435s)** even within the exact same sand boss. Subto entitlement difference can be abused for private exploration. And third, by combining air launch large damage modeling reasoning with traditional automate static analyze, making large scale binary vulnerability discovery is not just possible but highly in efficient. That concludes our annation. That's all. Thank you for watching.
