---
id: RTQdC6IgBzc
title: "FrameworkDesktop and IncusOS, a perfect combination for running LLMs locally by Peter Smink"
slug: frameworkdesktop-and-incusos-a-perfect-combination-for
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2026
speakers: []
channel: "Devoxx"
duration_min: 19
published_at: 2026-04-08T20:18:24Z
video_id: RTQdC6IgBzc
url: https://www.youtube.com/watch?v=RTQdC6IgBzc
youtube_url: https://www.youtube.com/watch?v=RTQdC6IgBzc
tags: []
transcript: true
---

# FrameworkDesktop and IncusOS, a perfect combination for running LLMs locally by Peter Smink

**Speaker not identified**

`Devoxx` · `Devoxx` · `2026` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=RTQdC6IgBzc) · [Conference site](https://devoxx.com/)

## Description

Please subscribe to our YouTube channel @ https://www.youtube.com/@DevoxxForever

If your are seriously developing AI Applications, a framework desktop server running IncusOS is a must have.
I will discus the pro and cons of such a setup,
go through the setup process and issues I run into when setting it up and using it.

I will give a demo how to you can run your own AI application on a laptop that use AI models running on the Incus server.

key take aways
you have a guide how to setup your own configuration and what issues you can encounter
you have an good impressing how this setup can help you own AI development
a solution to run LLM locally for privacy reasons
a solution to run LLM locally on a GPU for performance
a solution to keep cost under control. If your application has many mcp tools the costs per call are high when using public AI's
a solution that can run LLM that do not fit in graphical cards
You are a devops and just want to see how a modern tools like Incus can be used for running any container or VM
You want to be eco-friendly, to control/reduce your own energy usage for running AI

Target audience:
AI developers, Devops, Anyone who wants to run LLMs locally in a relative efficient way.

## Transcript

*3,011 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=4s)** Welcome everybody. This is my talk about the framework desktop and incorus OS. That's actually a framework desktop that's based on the next generation hardware of AMD. That's the AMD AI max processors used inside that. And Incos is a quite recent uh yeah u uh system to run VMs and containers. Who's who's familiar with VMware and Proxy Mox? A few. Well, it's a bit similar than that only it's completely newly written uh by the people who also wrote Alex and work on LXD. So, they they know what they're doing. So, I'm a bit I'm confident in that. Well, uh my name is Peter Mink. Uh I work for team Roxy and in daily life currently I work for AMD.

**[0:54](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=54s)** But in my uh next to that I also work on other project which is a project on domain modeling uh software domain modeling application and this is just an example that what I want to achieve for that with AI. So here you see a system a prompt which I use to define some uh object definitions like person and department set some attributes on it and also define some relation between it. It's just an example. But then in the same prompt, you can say well start this uh this model. Then you're able to also use the same prompt to to get data into that system. And the last line uh of the of this one is an example query that you say okay now you know this all and the data is in list give me all the person's first name last name and then from the

**[1:43](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=103s)** department I need to know the the name they work on. So that's what I did. I did first try to do that with running a local LM on my laptop that did not have specific uh GPU hardware in that but that was as you can imagine quite slow so I had to use a small model like quen two for example but also the results well that's also generic for AI what was especially with this one was a bit unpredictable the implementation was done using uh MCP so there were two MCP tool sets in there that also did result in that uh well if you use it for a while you got quite a high count of tokens that was used with it because the all the LM configuration all the MCP configuration is pass v call so if I would do that against the system

**[2:33](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=153s)** in the cloud that would give a reasonable price to that so that was the reason why I was going to look is there an alternative to to have better hardware to do this well I prefer to have it uh locally for privacy reasons also prefer to have the possibility to experiment with bigger lens than would fit in a graphical card of these days. I prefer to have uh well not that expensive hardware to get it done and because it's local you don't have recurring costs and I also would like to have a system that is doesn't require that much power uh when it's being used and uh well because it's hardware that when uh uh if you buy a graphics card and you can't use it anymore for running

**[3:22](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=202s)** LM there's a graphic card which is expensive at the living is in the corner But if you have a genic uh hardware then you can even use it for your normal system and it's still usable at the end. So it to be reusable hardware. So my choice was uh at the right you see here that's the uh AMD Ryzen that's the framework desktop system and uh well it has the maximum size for that 120 gig internal memory and I start from 80 watt until higher. So it's has a low power usage. Actually, I did not order this system, but I did order the ETX board. That was because the original uh uh system had issues with the power supply that was generating noise at some moment. So, for that reason, I switched to this one. And also because uh if you put in your own uh case, you also have

**[4:11](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=251s)** the possibility later on to put an extra card in it for for what might be needed in two years maybe. So, it's more expandable. Okay. Why Incas? Well, performance the LM is running on the GPU, not on the CPU. It's uh it's flexible. I chose to have you also can run any container or VM on the same system where you run your LM on. It's modern. It's completely rewritten and go. But there's active development done by the team right now. Well, there's an easy command line. I'll give an example later. Tool for both VM and um why is the dialogue there? So both for the VM and running containers. It is safety by design. So it has secure boot TPN. It's also immutable. Linux OS is used below

**[5:00](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=300s)** the surface and as part of the package it also keeps itself up to date. The so the OS with AB page partitioning that means that when a newer version fails you can switch back to the older versions. it support out of the box. That's actually the also the only UI interaction can do with the device because everything is controlled by its network port using the APIs. So uh well here in the middle you see Incas on the left side you see a way you can use it from as a user you have a web UI you have a command line UI tools and at the bottom side you see also there also anible open tofu plugins available to to control it or manage this configuration at the right side you see uh OS at the bottom that's what's runs on my box but you also free to run it on your own link system and that could for

**[5:48](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=348s)** example be handy to run a container that is used to uh use cloud code. If you want to run cloud code in an isolate environment, you can use that setup. So uh what do we have to do to get this done? Well, actually the second step is to install inks on your framework desktop. But in order to I already told you you only have you need an API to communicate with it. So you need to first have a client uh available then you can generate the installer for the for the for the system itself and then you can connect the client to the to the ink OS system. So you first have to start with installing an ink client. The third step if you have it up and running install in a VM on that well give the VM access to the DPU and then

**[6:37](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=397s)** you can continue with alarm in that VM to get things working. So uh to get you start with uh making an image on USB stick that's the first thing. So you need a client certificate that's why you need to install the client first you can specify the disk you install on you can specify the graphical drivers you need it for them and you have to specify PCI pass through to the GPU. This is one of the configuration files that is used to specify uh that you need uh the drivers for your AMD uh card. It's uh and this is the second one that's a different file that here. This contains a certificate from your client installation so it can connect to that system. This is the uh file that specifies the drive to install inks on. You can leave

**[7:25](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=445s)** it empty but I prefer to specify it. So if you put your disk in another system, it's will not automatically wipe that system and you get that might be a bit bit hard. And this is the this is the file where you specify the PCI pass through. And this is just the the configuration of the graphic part and the sound part of your uh what's in the system. That's why the two in here. Uh you have all those files configured. Now you can uh you have to set you have to make an image. That's done by the flasher tool which you can download and uh this will download the latest release of Angus OS. when you run it from the system, it will uh include the configuration that's in the seatp which is generated there uh as a configuration.

**[8:13](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=493s)** Then we'll create a new image that you can copy to your use basic and can plug into your system to get started. So uh yeah, what are the preparations you have to do on the on the on the framework framework desktop yourself? Why you have I prefer to not specif you can configure the installer to wipe your disc but I prefer not to do it for safety reasons. So I manually clean the disc here in the BOS you have to enable secure boot and you have to clean the secure boot certificates if they're there because the installer will install their own. You can set the CPU you can set the CPU memory to the lowest value and uh then you can boot the image. it'll automatically install and you're ready to run. Uh some looking back, what was the hardest

**[9:00](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=540s)** part of this? That was actually um making the client work with the uh with the with the server. Uh there is a recipe later on in in this uh how the exact command but if you make it in do it in the wrong order or you forget to add sudo to it then you get an system that will never work. So that was an issue at the beginning. So okay uh actually this is the part which I was just referring to. So there is I have removed all the uh uh the the the the calls you have to do to get the configuration right to the appendix because it's too much time to discuss the mirror and it doesn't make

**[9:47](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=587s)** sense I think for now. So uh go to the next slide. Well these are actually the steps once it's up and running. The first line actually creates a network because you want your VM to be able to connect to the outside world or the other way around. you want to get from the outside to your VM. And the line two here is that's actually the command that uh you specify an image of a mobuntu. You give the image a name. It's this case II server. And you specify how much CPU and memory to be used. In this case, it uses 83 of those 128. And you specify an initial disk and the network to be used. uh you need at least 30 internal disk space to have this running because of the size of the graphical drivers. It's

**[10:36](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=636s)** enormous. And the third point is that uh you're going to give access to uh so the I server can access your GPU. That's command. And then you're ready to start at the end at the bottom the server. It it all works. Uh lama. Then you bring your in your VM. Uh you have to install updates. install some tools like curl. Be sure you have the newest kernel because otherwise it won't work. And you have to add users to the video and render group to be able to access your graphical card. And all the details for this are again in the appendix. This was also uh installing a newest kernel. uh they made kind of an AP IP API API change in January and so it was very hard to get it working because stuff was

**[11:24](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=684s)** not really uh aligned with each other but since recently with the newest version of kernel like it's here it's it's much better than it was a few months ago it uses rock 7.2 two. That's the AMD uh graphical drivers. Here you see it's uh 721 that's released uh almost just more than a week ago. That already is a lot more stable than the older version. That is a great improvement. This is the first line is actually installing in the installer. The second line is uh running the installum and then you can uh verify the confiration of rockom info and if everything works all right you have an agent too that is actually connected to the GPU. Well this is just alarm out of the box but don't forget to specify the

**[12:14](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=734s)** environment host host otherwise you can't connect from the outside. Uh demo time. Well, uh I already said I have two minutes left. Great. Uh when I pass a query that's on the top, I put it in the chat. It it responds because internally I use GraphQL to uh to do the calls to the back end and I is doing that for me actually. So it produces this this uh GraphQL statement and then if you wait for the results, you get the details as it's given here as an example. Let me see. Two minutes. Escape. Um okay.

**[13:05](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=785s)** Not that one. Oh, escape. There it is. Here. This is an example of Incas OS how it runs. uh when you've installed it and uh here you see oh yes this is okay here you see all the uh the system I have installed not correctly should click here there there it is here you see at top you see the AI server that is currently running and uh well uh I showed you the commands to do it from the command line from your Incas client but you can al also here that's just general functionality you can browse images that are available. Suppose I want to click suppose I want to run a sent OS. In this

**[13:56](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=836s)** case, it's uh it's container. I select this one. Give it a name demo 2 and create a start. This is all what it takes from the UI to to start up a new VM or this container. But for a VM, it doesn't make a difference. Also in the command I showed you earlier that the first step to install the AI server just sping adding minus minus VM to it or removing it is the difference between starting it as a container or starting it as a as a VM if that image is is supporting that feature. So this is uh it I have closed this one apparently. Okay.

**[14:49](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=889s)** Close. Well, I've started this building first. I should have uh not started the debugger. Close. Run. Run. If I now go back to uh that one, I can click here for example. Let's just uh go back to the terminal here. in uh or this one. This then for example shows that it's running you see on the right side here you see a GPU column and you'll see that currently it it's using

**[15:36](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=936s)** it's running not on the CPU but it's running on the GPU inside this VM. This is what alarm is doing. So this is very quick uh what can you can do in let's go back to the presentation it's here. So the summary, it's a private local M. It's energy friendly. PU I choose out is has a high efficiency. So it runs I've measured it between 18 and 130 W. So you can even power it with your solar panels. It's a very flexible setup for containers and VMs. It has limited costs because yeah, you can uh the only way you can get better performance if you buy the high-end AM high-end Apple stuff, but that's almost twice the price. Then you go to €8,000. This whole setup cost me about uh €2,400. Although that was last year. This year

**[16:25](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=985s)** it's around €3,000. It's uh relative silent. If it's idle, it it doesn't make sound. It has upgradeable because there's a slot in and when it all doesn't work and doesn't make sense anymore, it's reusable as a normal server. So yeah, um I left away most of the comm the installer commands. They are actually in the slides below this. So I will if you want if you're interested download the slides and check out those things if you want to do it yourself. Uh already mentioned the party tip to also use ink to run for cloud code on your local setup. Uh for that you don't need inks at all anyway. And uh yeah this some links you can follow. I will uh skip those. Are there any questions?

**[17:16](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=1036s)** Yeah. Okay. >> How many per second? >> Good questions. Uh the highest I've seen was around was above 80 or just below 90 and uh on average it is between 25 and 60. But maybe that maybe can be get better if because I run a llama and if you own LLM CCP it should become better. So it should could be better even than that. But that's what I get right now. >> Yeah. Yeah. So, so the question was by the way uh how much tokens you can get, but that I

**[18:05](https://www.youtube.com/watch?v=RTQdC6IgBzc&t=1085s)** think that was clear. Yeah. like >> well uh if you are an an AI addict and you run against the services that run in America maybe then you'll find out that sometimes when Americans wake up they are not longer available for you then maybe this is also a fallback scenario for that case so yeah there's several use case you can use this okay my time is over so thank you very much if you contact me and that will be the link where the slides will be available later on. Thank you very much.
