---
id: ttGYcUFCok0
title: "Keynote: The Future of Cloud Native Is… Agentic - Lin Sun, Head of Open Source, Solo.io"
slug: keynote-the-future-of-cloud-native-is-agentic-lin-sun-head
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "General software conferences"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Lin Sun"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 16
published_at: 2026-03-27T06:13:25Z
video_id: ttGYcUFCok0
url: https://www.youtube.com/watch?v=ttGYcUFCok0
youtube_url: https://www.youtube.com/watch?v=ttGYcUFCok0
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Keynote: The Future of Cloud Native Is… Agentic - Lin Sun, Head of Open Source, Solo.io

**Lin Sun**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=ttGYcUFCok0) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Keynote: The Future of Cloud Native Is… Agentic - Lin Sun, Head of Open Source, Solo.io

Kubernetes and cloud native are powerful, yet often complex. Users spend too much time reading documentation just to deploy, debug, or operate systems, or to configure networking and security. As “vibe coding” reshapes how we write software, the future of cloud native is agentic. By composing AI agents and MCP servers, we can move users from manual configuration to intent-driven, natural-language operations.

Through live demos, from flying a drone to analyzing audience engagement, we’ll explore how AI agents and MCP servers can make cloud native more intuitive, approachable, and human-centered.

## Transcript

*1,989 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=ttGYcUFCok0&t=0s)** I still remember my first Cube Con. It was in Seattle 2016. It's the very first Cube Con organized by the CNCF. Like many of you, first time attending Cube Con, I was trying to figure out what Kubernetes is. What is pod? What are the declarative YAML? And Helm is like one of the biggest thing at the conference. Fast forward 2 years ago, as part of the TOC, I surveyed the cloud native community, the leaders, and the end users, uh what are the biggest pain point we have in the cloud native ecosystem? And I repeatedly heard from the leaders and users in the community, it's the complexity of our ecosystem.

**[0:50](https://www.youtube.com/watch?v=ttGYcUFCok0&t=50s)** Well, we have too many things, too many things for user to learn, too many things for people to pick, and and just navigate the ecosystem. I still remember last year in May, I had the opportunity to go to KCD Texas, where Chris Aniszczyk was on big stage giving a keynote about how we were able to scale cloud native users from 0 to 10 millions in less than 10 years. That's a super impressive number to reach 10 million users, but I started to think about how can we do better? How can we reach the next 10 million users a lot faster, hopefully without a lot more complexity like what we have today? And

**[1:40](https://www.youtube.com/watch?v=ttGYcUFCok0&t=100s)** with the rise of agentic AI, I believe it's going to play a huge role in the future of cloud native. And I'm going to try to show you a demo for that. If we can switch to my laptop, All right, let me know. Can you guys see my screen? Yes? Is the font big enough for folks in the back? Yes? All right, I hear yes. Okay. No? >> [laughter] >> All right, this is my cursor configuration. As you can see, I have MCP server config, which is MCP server running in my Kubernetes cluster. And I'm going to zoom in this thing a little

**[2:29](https://www.youtube.com/watch?v=ttGYcUFCok0&t=149s)** bit for you, so you can see I have two MCP server running. One's the Argo CD MCP server. I have the GitHub MCP server running proxy through agent gateway proxy. I also have my AI agent exposed as MCP server. And let's hop over to cursor. You can see I have the Argo and K agent config. So, what I'm going to do is I want to show you a demo application I built for all of us today. Hello, can you please create an Argo CD application for me using the Argo CD MCP server? Let's call it demo.

**[3:18](https://www.youtube.com/watch?v=ttGYcUFCok0&t=198s)** And the namespace is default. The path is YAMLs. Repository is All right, that's too long. I'm going to copy paste. Uh this is my demo repository. >> [laughter] >> And uh let me massage my message a little bit. So, it's YAMLs. Can you please create an Argo app crew using the Argo CD MCP server? Call it demo and the name space All right, let's send it. Looking okay. Fingers crossed. This is all live, you can see. >> [laughter] >> By the way, I'm using the standard model, if you can see it.

**[4:06](https://www.youtube.com/watch?v=ttGYcUFCok0&t=246s)** Um And it's asking me for approval. Let's go ahead approve that, cuz I want that Argo CD demo application so badly in my cluster. What? >> [laughter] >> Okay, the Argo CD doesn't have our bot. Is this a network issue? Okay, let me actually disable my network. Let me make sure my network is good. I'm sorry about this. All right, let me try this again. Okay, sorry about that. This is a little bit unpredictable. Create an Argo CD user using the Argo CD MCP server

**[4:56](https://www.youtube.com/watch?v=ttGYcUFCok0&t=296s)** application called demo. Let's just make it simple. All right, let's try it again. Hopefully my network is good. Um Okay, I'm going to check on my network here again. Um All right, let's go ahead approve that request. Okay, it was network issue. Um apparently the conference Wi-Fi, you can't rely on that. All right. You can trigger a sync. Okay, it's in our sync. Let's hop on to Argo's UI. All right, let's go ahead sync that baby down to my cluster. All right, it's progressing. Fingers

**[5:47](https://www.youtube.com/watch?v=ttGYcUFCok0&t=347s)** crossed, I'll have the demo application deployed. Uh let's hop on to my cluster here. You can see Okay, the front end, the back end is running. I also deploy a dedicated gateway for my application. Okay, everything looks healthy. Uh what I'm going to do is uh using what we all love is uh access the application from a gateway. So, and I'm going to try to access this um Okay, so there's no routes yet. So, what I'm going to do next is asking Hello, what K agent agents do you have access to? K agent agents do you have?

**[6:37](https://www.youtube.com/watch?v=ttGYcUFCok0&t=397s)** All right, let's see if it can figure out what agents I can have running in my Kubernetes cluster on top of K agent, which is a CNCF sandbox project. Okay, it has two agents running, and it asked me if I would like to involve a specific task. Okay, given my network had a issue, I'm going to copy paste this message here just save some time. So, basically what I'm going to do is asking the AI uh reliability agent, can you create an HTTP route from the agent gateway proxy in the default namespace to to the front end service also in the default namespace. And I am also asking

**[7:26](https://www.youtube.com/watch?v=ttGYcUFCok0&t=446s)** the agent, can you go ahead create a PR for me and grab the repository from the Argo CD application? All right, so while this is running, uh let's see if uh Fingers crossed, the agent is going to do the magic and create a PR for me. And then we can all as a team review the PR together. All right, looks like there's a PR. Do you guys see that? Yes? Let's click on the PR. Team cloud native, I'm going to rely on you all review the PR together. I mean, there's so many experts here in the room. Uh does this look okay? HTTP routes from agent gateway proxy to the front end. I think it's

**[8:16](https://www.youtube.com/watch?v=ttGYcUFCok0&t=496s)** running on port 80. Should we approve this? All right. All right, I'm going to go ahead hit the magic approve button. Sorry, I'm going to make this a little bit smaller for me to navigate. And I'm going to go ahead merge the pull request. All right, once it's merged, let's go ahead use our magic from Argo to sync that new PR into the cluster. Looks like it's synced. Fingers crossed, this is the magic moment. All right, we have our application running. >> [applause] >> Now, it's the even challenging part. We just accomplished our mission number

**[9:04](https://www.youtube.com/watch?v=ttGYcUFCok0&t=544s)** one. Now, our next mission is even challenging. We need to fly this drone on stage. So, I'm just lighting it up, and I'm going to place it right here next to me. And I'm going to try to attempt to connect to the Wi-Fi of the drone. So, you do good. The network here is always complex to navigate. So, hopefully I can see the Wi-Fi of the drone soon. It's trying to come in up. So, going to All right, I'm going to disable that and try it again. You guys are using all this Wi-Fi? >> [laughter]

**[9:51](https://www.youtube.com/watch?v=ttGYcUFCok0&t=591s)** >> It wasn't this busy before. All right, let's see if I can connect to my drone. Uh let me double check what's going on my zone. All right. >> [laughter] >> This is a little bit unpredictable. I didn't realize there's so many Wi-Fi here. All right. I did see my zone Wi-Fi. All right. Apparently somebody has been very busy with the network here. All right. Let's There's one thing I need to do. I need to start a proxy to here allow my laptop to connect to the zone. So looks like I'm able to reach the network of the zone. And everything looks okay. I'm going to

**[10:37](https://www.youtube.com/watch?v=ttGYcUFCok0&t=637s)** click on connect. All right. And we're going to start the camera together. Fingers crossed. All right. We have the lights on the audience. We just need that the camera or the video from the zone to fly through so I can see you all on the big screen. All right. Is it running? I'm not sure. Let me double check. Okay, looks like stream is there. Um but it's black. So I'm going to try to take it off. All right. Let's do this team cloud native. All right. It's flying. >> [applause]

**[11:28](https://www.youtube.com/watch?v=ttGYcUFCok0&t=688s)** >> All right. The camera is still not working. I'm not sure why. I'm going to fly a little bit up. And I'm going to try to stop the camera and restart the camera. That was a little bit surprise to me and see if I can get the camera running. All right. Looks like address already in use. Okay, I disconnect. Uh looks like I can only fly the zone. I burned my demo gods to fly the to have the camera stream going on. I'm going to try one more time. I'm going to get out of here and reconnect and see if I can fix it. If not, we may have to uh swap back to a camera on my phone. But at least I proved to you I

**[12:16](https://www.youtube.com/watch?v=ttGYcUFCok0&t=736s)** can fly a zone on stage. Okay, I'm going to disconnect here. And let me check the Wi-Fi just making sure. Restart the camera. One more time. Last time. Let's check how much time I have. All right. I have to give up on that. I apologize for that. I'm going to disconnect and we're going to fall back to our backup plan which is the web camera on my phone. You always need a backup on stage. All right. Are you guys ready to take your pictures? We're going to capture the picture on

**[13:04](https://www.youtube.com/watch?v=ttGYcUFCok0&t=784s)** this side. All right. And we're going to try capturing engagement on this side. Come on. I need more engagement than that. All right. And then we're going to compare with AI. And while this is comparing, I want to show you what the application looks like. If I can make this bigger enough. So I have the front end application reaching through agent gateway and I have the Argo and GitHub and every single connection is secured through mutual TLS and I'm using SPIFFE because I'm running everything in Istio service

**[13:55](https://www.youtube.com/watch?v=ttGYcUFCok0&t=835s)** mesh with ambient so there's no sidecar. Let's come on see what's going on here. Still being analyzed? All right. >> [laughter] >> All right. Unfortunately we've made >> [laughter] [applause] [applause] >> All right. So looks like our analysis did work and in order for me to remember this moments together, I'm going to submit a PR and if the Wi-Fi network works, we can you can see the PR over all of your faces on my GitHub repository. All right. Looks like

**[14:43](https://www.youtube.com/watch?v=ttGYcUFCok0&t=883s)** >> [laughter] >> there's another issue. I will fix that later on. But uh really quickly just to wrap up. Uh we were able to show um Argo CD and MCP server. We were able to show K agent exposed as MCP server. We were able to show agent gateway serving as MCP gateway in front of MCP server. We were able to use agent scale. That's how I was able to craft the perfect HTTP route for you for my agents. So I believe the future of cloud native is with agentic. So that's all built on top of the ecosystem. Build more MCP server. Build more AI agents. Build more skills and let's share it. Do it in the open and let's keep cloud native moving.

**[15:33](https://www.youtube.com/watch?v=ttGYcUFCok0&t=933s)** Thank you. >> [applause]
