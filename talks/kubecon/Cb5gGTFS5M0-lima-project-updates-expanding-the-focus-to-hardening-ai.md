---
id: Cb5gGTFS5M0
title: "Lima Project Updates: Expanding the Focus To Hardening AI - Akihiro Suda, NTT & Anshuman Sahoo"
slug: lima-project-updates-expanding-the-focus-to-hardening-ai
conference: kubecon
conference_name: "KubeCon + CloudNativeCon"
category: "Software dev with AI tracks"
edition: "KubeCon EU 2026"
year: 2026
speakers: ["Akihiro Suda"]
channel: "CNCF [Cloud Native Computing Foundation]"
duration_min: 27
published_at: 2026-04-09T05:25:42Z
video_id: Cb5gGTFS5M0
url: https://www.youtube.com/watch?v=Cb5gGTFS5M0
youtube_url: https://www.youtube.com/watch?v=Cb5gGTFS5M0
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Lima Project Updates: Expanding the Focus To Hardening AI - Akihiro Suda, NTT & Anshuman Sahoo

**Akihiro Suda**

`KubeCon + CloudNativeCon` · `KubeCon EU 2026` · `2026` · `27 min`

[Watch the recording](https://www.youtube.com/watch?v=Cb5gGTFS5M0) · [Conference site](https://www.cncf.io/kubecon-cloudnativecon-events/)

## Description

Don't miss out! Join us at our next KubeCon + CloudNativeCon events in Mumbai, India (18-19 June, 2026), Yokohama, Japan (29-30 July, 2026), and Shanghai, China (8-9 September, 2026). Connect with our current graduated, incubating, and sandbox projects as the community gathers to further the education and advancement of cloud native computing. Learn more at https://kubecon.io

Lima Project Updates: Expanding the Focus To Hardening AI - Akihiro Suda, NTT & Anshuman Sahoo, BITS Pilani

Lima (Linux Machines) is a command line tool to launch a local Linux virtual machine, with the primary focus on running containers on a laptop.

Aside from container workloads, Lima is also known to be useful for running an AI coding agent inside a VM. This setup ensures that even if an AI agent is deceived by malicious instructions searched from the Internet (e.g., fake package installations), any potential damage is confined within the VM or limited to files specified to be mounted from the host.

In this session, the maintainers will introduce the recent news in the project, including:
- Promotion to CNCF Incubating (October 2025)
- New features in v2.0 (November 2025)
- Plugin infrastructure
- GPU acceleration
- MCP server
- Other updates planned in v2.1 and onward.

Project website: https://lima-vm.io/

## Transcript

*3,074 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=0s)** Uh hi uh we are the maintener of the dimma project. I'm the horn entity in Japan. >> Hi thanks for joining in. I am on and I'm currently a prefinal year bachelor student at bits pilani. Last year I was also a Google summer code menty where I contributed to the lima project and I'm currently serving as a maintainer here. >> In this session we are talking about project updates of dimma. In the uh recent releases uh we are expanding the forecast to hardening AI. So LMA is no longer just for running containers. So what is Limma? So Lima means Linux virtual machines optimized for running containers and AI agent. So the name indicates that it's made for Linux gu.

**[0:51](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=51s)** However, despite the name in the latest release version 2.1 uh we reached this month uh we support macro guests and previously G as well and we are even planning to support Windows gifts as well in future and dimmer comes with automatic host file system sharing and porting features. Uh so this is really convenient for running containers but uh this can be also dangerous especially when running antist works such as AI agents. So you can also disable these features and dem integration for several container engines. The default is containerd with

**[1:43](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=103s)** ncttrl continue ctl uh it's a command line and ford but you can also choose to use other container engines such as jker pmer kubernetes and obainer. So rema was originally made for Mac OS host uh but uh we also support Linux and Windows NBCD and Dragon BD but in this demo we just use Mac OS and in the case of Mac OS you can use B install dimma to install dimma and run dimtrl start to start the virtual machine and you can use the dimma command to run Linux commands such as net ctl uh it's a Contrad CTL uh it's a command line client for with similar experience as to

**[2:35](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=155s)** so this is host and prepend the lima command to your name so it's now and you can also run container using n ctl For example, one NGX with proing and uh this uh port can be accessed as local host on the Mac OS host like this. So it's back to the presentation.

**[3:24](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=204s)** So uh we have uh similar similar projects. So WS2 is very similar to dimmer but WS32 only support Windows hosts and big is also similar to dimmer but uh it's now proprietary and background also supports port forwarding with manual configuration but it doesn't have automatic configuration for port forwarding and dim is actually also similar Dam machine but durkam machine is just made for joker and it's abandoned in the favor of jadis product uh which is propriatory and here's origin and the current status

**[4:16](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=256s)** of the project. So the project began five years ago for the sake of promoting control including Naz CL to mark users. So this was originally designed as contrad machine uh similar to docker machine. However through the growth of the community the scope has expanded. So we originally supported control ID but now we support other control engines such as docker programmer kubernetes and aptainer and we even support nonontainer works such as sandboxing AI coding agents and dimma is also useful for running uh nonubuntu operating system such as

**[5:05](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=305s)** feeder or box. So we can use dimma for testing features that is not available in vu for example s Linux and originally dimmer was made for Mac OS host but now we support uh several host operating systems including Linux, Windows, NBSD and even Dragon Fly BSD and the original guest operating system as a Linux but now we support MarQuest Free BSD And we also plan to support Windows in near future. And we have a very huge community across uh the demo project. Uh so we have uh several third party projects such as

**[5:55](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=355s)** Korea. Kimma provides alternative CLI for dimma with Joker as the default engine. And there's also Rancher desktop by Suzie. It combines dimmer with K3S and their own graphical user interface like this to manage the demon instances and different cluster running inside it. And we also have a project called Finch. Uh this is a Amazon's product made for local development with uh several Amazon service such as AWS serverless application model

**[6:47](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=407s)** and dimma GUI is a GUI uh made using cute framework and portman desktop it's uh of made for managing portal machine instances. But port desktop also has a plugin to support managing dimmer instances as well. And dimmer explorer plugin provides task tray icon and the menu for Mac OS. And 0 MA is uh another project for GUI dashboard. And dimmer debros is a set of steers for

**[7:39](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=459s)** crowd code and RW sorry RF swift project uh provides USB pass through for dimmer instances. It's uh made mainly for software defined radio devices but uh it should work for other USB devices as well and uh we have uh lot of uh other projects uh but we don't have time to cover everything in this talk and dimmer is also useful for GitHub actions uh so you can for example use Fedra not just Ubuntu so you can test uh your application with uh features that is not available on Ubuntu. For example,

**[8:30](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=510s)** you can test S3 Linux compatibility with your application using Fedra and you can also run multiple virtual machines inside a single GitHub action and actually dimmer is adopted by many projects such as kind Der NTL RNC and UTS uh which is a rust implementation of G core utils. So they use Fedra or LX8 or Alma Linux 8 to test compatibility with S Linux. And this is how it works. So here's the architecture. Uh so there is a dim CDL command line interface and

**[9:20](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=560s)** this is used by human users and GUI front end and MCP model contest protocol tools and this CI talks to host agent processes. And these host region processes launch virtual machines using driver. And driver launches virtual machines with guent processes inside them. And the guent process talks to the host regent for port flooding and file system events and for syncing clocks. And we also have several network drivers between these virtual machines. And for partial machine drivers, we support QMU and a brushization framework

**[10:12](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=612s)** known as BZ and Microsoft's WS2. And we also support Kan Kit. This is very useful because it supports GPU acceleration or Mac OS. So this is used for running AI locally. And you can also use gRPC to build your own BM driver plugin. And inside uh you can run inter binaries using QM user mode emulator running inside the guest and if you're using AR mark we can also use Rosetta 2 to run into binaries and for file system sharing we supports

**[11:05](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=665s)** part 9P and reverse SSHs. And in addition, we also support our sync and uh network drivers. The default is uh the user mode networking. So it doesn't need uh extra privileges. So you don't need sudo but uh you can also opt into use socket pminet for accessing virtual machine by real IP address not just by local host port but uh BMI needs a pseudo privileges and you can also use bz this is similar to solid bnet but it doesn't need the sudo however bzet only works with the bz driver

**[11:54](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=714s)** and for port routing uh we have EBF EBPF program to monitor the ports and we also have uh watch a program for Kubernetes service ports and you can choose uh a lot of templates uh so we cover several Linux distributions such as Alma Linux Alpine Arinux central system stream Deb open s or Linux ro key and Ubuntu and for container in addition to the default continer docker and fmer and you can also choose several distributions of kubernetes and you can also

**[12:45](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=765s)** use your own template file which is a yaml file. And you can also use third party template via GitHub. So you can just press dimma. In the GitHub repo to distribute your own template and the user can run the template by running dema citab column and template to name such as nix os dimma. So uh let me talk about the recent updates in Lima. Last year our project got uh promoted to CNCF incubating and we anticipate that we get promoted to CNF graduated uh by

**[13:35](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=815s)** the end of this decade. Also our GitHub stars are rising. Currently we have 20,000 plus stars and close to 170 plus contributors. So thanks to all the contributors and the users of Lima. Uh last year we also launched Lima version 2.0 which was one of our biggest update so far. Uh here are the basic uh I mean the highlights of that update. We added the plug-in infrastructure that means it allows you to implement new features in Lima without uh modifying the core of it. Uh inside that we have the concept of uh VM driver plugins. Uh that means you can bring your own hypervisor implementation and uh use it

**[14:24](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=864s)** with Lima to launch virtual machines. And for uh CLA plugins uh it means that if let's say you want to add a new subcomand to the existing Lima Ctl CLI uh you can do that too. And uh for URL schema plugins uh let's say if you have a template that is sitting somewhere remote you can use it to fetch it and configure and you know run the virtual machine. We also added support for GPU acceleration uh workloads using the KNID VM driver and also the model context protocol uh server which basically allows you to sandbox uh sandbox AI agents uh accense uh that is running on your host machine. So uh basically the original goal of the

**[15:13](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=913s)** project uh was to promote uh containerd workflows uh to Macintosh users but uh it really turned out to be uh very useful to sand to sandbox and running AI agents as well. So here is why you might want to uh sandbox agent. As we know AI can hallucinate sometimes and uh recently a clot code user posted this on Reddit that uh the clot code tried to remove bunch of stuff and as you can see uh at the end it also tried to remove the home directory of the host machine. So yeah it's uh very scary if you run on your host machine. uh AI may also help it and you know

**[16:03](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=963s)** convince you to install correct packages. uh let's say uh if AI suggests you some uh uh library which doesn't exist on popular package managers like uh npm pip or perhaps a go library and a malicious actor or a hacker may register a malicious code under that particular fabricated name and you as a developer uh you integrate that inside your codebase and you know deploy it in in production. So now it's uh compromised. So when we uh give AI the power to serve the internet uh it may get deceived by fake sites. Uh recently a security researcher reported that uh GitHub copilot was hijacked because a hidden

**[16:52](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1012s)** prompt injection uh made the AI to alter uh local VS code uh flags particularly the auto approve uh execution flag uh which basically meant that uh the AI literally gained uh permission to run anything uh without the consent of the human or Nowadays, uh, AI agents often come with, uh, built-in sandboxing, uh, like we have landlock on Linux and perhaps, uh, docker container, but uh, it is not as strong as a virtual machine. uh some a aents may use sandbox exec uh which is very similar to landlock but on Mac OS but uh it has been depregated for about

**[17:41](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1061s)** the decade now Apple recommends uh using app sandbox but uh it's also not a direct replacement because it's process level isolation so yes uh lima can be used as a universal sandbox for any asend because it offers a system level uh isolation. So when it comes to uh running AI uh with Lima, we have these two concepts. One is AI inside Lima and another one is AI outside Lima. AI inside Lima means you download and install your favorite AI coding asent like Cordex, Copilot or perhaps cloud inside Lima virtual machine and use it to make changes. AI LLM I mean LLM inference can also be

**[18:31](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1111s)** done inside Lima uh using the GPU accelerated uh virtual machine launched by uh launched by concrete driver and AI outside Lima means uh we provide a bunch of MCP tools uh for the AI agent that are that is running on your uh host machine and also VS code with remote SSS and copilot uh works well with lema So here is a small example of how AI can be used inside Lima. You basically start uh the a virtual machine instance using this dash mount only flag. Uh basically it uh mounts your current working directory in read and write mode and then you just SSH into the virtual

**[19:19](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1159s)** machine and use your AI coding agent uh to make changes. Here is how uh GPU acceleration using K and Kit uh works in Lima. So uh llama.cpp running inside a virtual machine uh uses vulcan API to talk to what IOG GPU or Venus and in turn it also invokes Vulcan API to talk to Molten VK and then the uh requests are forwarded to Apple silicon CPU uh using the metal API. I guess we can show a short demo here. enter into the and so it's using part GPU beas with a formax as the physical GPU and now

**[20:11](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1211s)** running 23. So let's talk to it. Introduce yourself. Yeah. And it talks uh very nicely. and the performance is not it's also good. Uh here is an example of how AI outside lima works. As I spoke uh before uh we expose a bunch of MCB tools uh like uh list directory read or write file and uh run cell command. So it is very similar to Gemini CLA's uh built-in tools but of course it's uh strongly sandboxed uh using a VM. Last week uh we launched Lima version 2.1 uh where we introduced uh sync mode

**[21:01](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1261s)** uh unlike mounts which are uh live and birectional. So that means any changes you make inside the guest it's uh automatically reflected back to the host machine. The uh sync mode prevents that uh by asking the user for the confirmation. Uh so here you know it uh prevents the AI from saying sorry I removed everything including the doggget directory. Uh I guess we can also show a s demo. So this is uh the host and I have a hero script which just runs echo herror and run dimmer sync to sync the current directory into the guest

**[21:49](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1309s)** and now let's modify the herosis. So suppose that I were a malicious AI and I'm a malicious AI. So I'm trying to inject some malicious script RM RF no preserve root to remove everything and I save this and the user now gives from the BM. And now the user is asked to accept the change yes or no or view the change the content. And as you can see this uh contains uh malicious change. So the user choose no to reject the malicious changes. So the change files are not

**[22:39](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1359s)** synced back into the host. Thank you. And addition uh to the Linux guest that we originally support uh we also added support for Mac OS and FreeBSDK. Uh you can get uh started with that uh using Lima CL start template Mac OS or template FreeBSD. So as we look ahead we want to make Lima more uh powerful and userfriendly. uh uh we are we have plans to add more VM drivers uh for managing infrastructure as a service instances more easily and uh in addition to Mac OS and FreeBSD guest we also plan to add Windows guest and uh we also need to uh you know uh

**[23:32](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1412s)** improve our uh user exper developer user experience using the TUI uh functionality and like uh docker compose we We're also planning to add Limma compose which will be beneficial for m uh composing and managing multiple VM instances and the support for uh AI workloads currently work on is Apple silicon Mac but uh we are planning to expand that to Linux and Windows host as well. So please uh come and meet us at the Pablon today. We will be there at uh uh from 1400 to700 hours at uh 24B K. Please uh join our community. Uh we have our website GitHub, Slack X and Mashedon. Uh we also have monthly

**[24:22](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1462s)** meetings on every third Thursday uh in a month. So yeah, thank you Thank you. Any questions? >> Can you please uh come up to the mic so that everyone can >> uh do you have a use case when Lima is run unprivileged in unprivileged container like is this useful case or not? So the question is is it possible to run dimmer inside a nonprivileged container? Yeah. So I think it's possible but you have to specify dash device uh /de/km

**[25:13](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1513s)** into local run >> and is it viable to run without KVM? >> Oh yeah it's possible but it's slow. Uh guys, thank you for the talk. Um have you thought about introducing firecracker as a VM driver for lemur? >> So firecracker driver. So we don't have a driver for firecracker but uh we have a plug infrastructure to implement your own boom driver using uh gRPC API. So you can implement a driver for fire cracker or any arbitary VM if you like.

**[26:00](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1560s)** >> I think we can show the documentation for that. >> Sorry. >> I I think we can show the documentation to add new VM drivers. Yeah. >> Yeah. So, we still don't have a good documentation but yeah. So we have our API for drivers. Yeah. So we don't have time to uh explain the details but uh yeah you can use uh this API to implement your

**[26:49](https://www.youtube.com/watch?v=Cb5gGTFS5M0&t=1609s)** own driver.
