---
id: VE496fhRapw
title: "Lightning Talk: Alcoholless: Lightweight Security Sandbox for Homebrew, AI Agents, E... Akihiro Suda"
slug: lightning-talk-alcoholless-lightweight-security-sandbox-for
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "Open Source Summit + ELC NA 2026"
year: 2026
speakers: []
channel: "The Linux Foundation"
duration_min: 9
published_at: 2026-06-03T18:23:58Z
video_id: VE496fhRapw
url: https://www.youtube.com/watch?v=VE496fhRapw
youtube_url: https://www.youtube.com/watch?v=VE496fhRapw
tags: []
transcript: true
---

# Lightning Talk: Alcoholless: Lightweight Security Sandbox for Homebrew, AI Agents, E... Akihiro Suda

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit + ELC NA 2026` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=VE496fhRapw) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Lightning Talk: Alcoholless: Lightweight Security Sandbox for Homebrew, AI Agents, Etc. - Akihiro Suda, NTT

This presentation introduces "Alcoholless" Homebrew, which protects macOS hosts from potential malicious Homebrew packages by running Homebrew with a separate user account. A command running with this tool is only allowed to read and write its current directory.

While Alcoholless puts focus on Homebrew, it is also applicable to other package managers such as `pip install`, `npm install`, and `go install`. Aside from package management, it is even useful for running AI coding agents that may potentially execute harmful commands.

Alcoholless is also an attempt to reexamine the necessity of Linux-style containers that emerged in this century. It just utilizes 1990s' commands (`su`, `sudo`, `rsync`) and the macOS equivalent of `useradd` to implement container-like environments, without extending the XNU kernel to support Linux-style container syscalls.

Repository: https://github.com/AkihiroSuda/alcless

## Transcript

*1,042 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=VE496fhRapw&t=0s)** Uh, I'm a curator at NTT. Uh, today I'd like to introduce uh, our quiz. Uh, it's a lightweight security sandbox designed for homebrew, uh, but it basically works with any command line programs uh, such as AI agents. Uh, so uh, here's an overview. Uh, it's not a VM, uh, it's not a container either, but uh, with regard to the user experience, uh, it's uh, tastes like a container. Uh, it's uh, just plain old utilities under the hood, uh, so it just uses sudo commands, sudo commands, and other sync commands, uh, but it tastes like a container. Uh, so for example, uh, you change the directory to some uh, directory and run

**[0:48](https://www.youtube.com/watch?v=VE496fhRapw&t=48s)** our quiz command to run uh, brew command to install uh, xc command, and run our quiz xc to run the installed xc command. And when you run our quiz, uh, only the uh, current directory is exposed to the command, and the changes to the directory is uh, synced about on exit uh, with a confirmation screen. Uh, so here's a background. Now open source is under serious attack. So even well-maintained software can be compromised. Uh, for example, uh, 2 years ago deep uh, xc uh, MA was uh, compromised by one of the maintainers to inject a backdoor. And

**[1:37](https://www.youtube.com/watch?v=VE496fhRapw&t=97s)** since then uh, lots of well-maintained software are being compromised. Especially this year, uh, the AI is emerging, and uh, famous software like tre b and mister r were recently compromised. And in uh NPM uh there are lots of other libraries that have been compromised. Uh so, today basically when you install something, uh basically you have to presume that you are going to install compromised software. And besides the security issues, uh there are problems in using AI. Uh so, if you are to search a Reddit, you

**[2:28](https://www.youtube.com/watch?v=VE496fhRapw&t=148s)** will see a bunch of people complaining that a crowd code deleted their project files. Uh so, this is a not a security issue technically, but it's a very similar to such a security issues. So, I'm introducing Alcohol OS. Uh the target OS is macOS, and the target use cases are Homebrew and AI agents. Uh so, I choose a macOS as a target OS because Linux and FreeBSD already have good containers. And it's not a container, but uh it's a similar to container, and under the hood it just uses

**[3:14](https://www.youtube.com/watch?v=VE496fhRapw&t=194s)** sudo and rsync. And here's a demo. So, this is macOS, and I don't have XD commands. And I can run Alcohol OS to XD commands from Homebrew. Yeah, so Wi-Fi is slow. But it's running Homebrew. >> It should take some time, but it should

**[4:04](https://www.youtube.com/watch?v=VE496fhRapw&t=244s)** finish within 2 seconds. And xz is installed, so I can run xz to some file. And now I can see a configuration screen to think about a compressed file to the host file system. So, I can choose return or control C, so I can choose return to accept this change. So, now as a hello xz is compressed using xz. And this is not a VM, not a container, so I have a GPU.

**[4:54](https://www.youtube.com/watch?v=VE496fhRapw&t=294s)** So, I can run Alchemist uh Ollama to run Gemma. So, this is using a GPU of my MacBook. So, I can use GPU with a native performance. Uh so, how does it work? So, it's a very simple. It's just switch the user and run everything and run the command and everything backs directly on exit. So, this quite simple. Uh so, why not use VM? Because a VM has several disad- advantages.

**[5:41](https://www.youtube.com/watch?v=VE496fhRapw&t=341s)** Uh so, the performance overhead is not negligible. And disk consumption is also not negligible. And the most important problem is that the VM doesn't support direct access to GPU, especially when running macOS this. And also Apple prohibits running more than two instances of macOS this. It's a licensing restriction. But without doubt, it's obvious that for a stronger isolation, VM is uh still preferable. And the next FAQ is why not use macOS sandbox? Uh so, macOS has sandbox exact tool, uh but it's deprecated for decades. And their successor is App Sandbox, but

**[6:31](https://www.youtube.com/watch?v=VE496fhRapw&t=391s)** it's not a direct replacement and it's not designed for CLI applications. And why mix up su and sudo? Uh so, I don't just use su because su requires a password or every invocation. And I don't just use sudo uh because it doesn't fully switch the user or macOS. Uh so, macOS is based on BSD, but it it's not just a plain BSD. Uh so, macOS is composed of of BSD subsystem and Mach kernel, which is uh well known as a microkernel. Uh but Apple's fork of Mach kernel is not a

**[7:19](https://www.youtube.com/watch?v=VE496fhRapw&t=439s)** microkernel. It's a monolithic. But there is a still solid border between the Mach kernel and the BSD subsystem. Uh so, sudo command is not sufficient to switch the user. So, this is quite different from Linux. So, I have to combine su and sudo to enable passwordless commands and full user switching. And of course, it's not a panacea. Also, user isolation is not as strong as VM. Uh so, in uh this month, uh several privilege escalation vulnerabilities were found in Linux kernel uh such as copy-fair and dirty frag and the frag nizer. Uh so, maybe uh Mac OS may have a similar vulnerabilities in

**[8:08](https://www.youtube.com/watch?v=VE496fhRapw&t=488s)** the kernel. So, the user isolation is not strong. And also, malware may steal waste your electricity electricity bill by mining uh cryptocurrencies. And also, AI may attack somebody or somebody's computer. Uh so, for example, AI may publish a blog uh to attack uh other people on the internet. Uh so, you have to be You have to check your responsibilities even when there is no direct damage on yourself. And so, uh here's the result. Uh it's a lightweight security sandbox designed for Homebrew and AI agents. It's not a VM. It's not a container, but

**[8:57](https://www.youtube.com/watch?v=VE496fhRapw&t=537s)** uh it's uh very similar to containers uh in the perspective of user experience. Uh so, it it just uses sudo and sudo commands and other simple commands. Uh so, it's uh very easy to use, and you can download uh my project from github.com/ahyhiroshi/agress. Uh thank you.
