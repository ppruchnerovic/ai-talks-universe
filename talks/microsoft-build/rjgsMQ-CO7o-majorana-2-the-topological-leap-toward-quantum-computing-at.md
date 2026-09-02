---
id: rjgsMQ-CO7o
title: "Majorana 2: The Topological Leap Toward Quantum Computing at Scale | DEM314"
slug: majorana-2-the-topological-leap-toward-quantum-computing-at
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Roman Lutchyn"]
channel: "Microsoft Developer"
duration_min: 15
published_at: 2026-06-04T12:44:30Z
video_id: rjgsMQ-CO7o
url: https://www.youtube.com/watch?v=rjgsMQ-CO7o
youtube_url: https://www.youtube.com/watch?v=rjgsMQ-CO7o
tags: ["132d2247-cf6e-4b4d-92b1-e9040df49d5b_M9Z7-DEM314-1", "Cloud Platform & Data", "DEM314", "Majorana 2: The Topological Leap Toward Quantum Computing at Scale | DEM314", "Roman Lutchyn", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Majorana 2: The Topological Leap Toward Quantum Computing at Scale | DEM314

**Roman Lutchyn**

`Microsoft Build` · `Build 2026` · `2026` · `15 min`

`#132d2247-cf6e-4b4d-92b1-e9040df49d5b_M9Z7-DEM314-1` `#Cloud Platform & Data` `#DEM314` `#Majorana 2: The Topological Leap Toward Quantum Computing at Scale | DEM314` `#Roman Lutchyn` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=rjgsMQ-CO7o) · [Conference site](https://build.microsoft.com/)

## Description

Go beyond the keynote with Majorana 2 - our latest topological quantum chip, enabled by a reimagined material stack and AI‑accelerated R&D. Learn what one-minute qubit lifetimes mean for error correction, and discover the latest advances in the Microsoft Quantum software stack on the path to a scalable quantum machine.

To learn more, please check out these resources:
* https://aka.ms/build26-next-steps

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Roman Lutchyn

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

DEM314 | Cloud platform & data

Demo | (200) Intermediate

#MSBuild

Chapters:
0:00 - Breakthrough in Material Stack and New Quantum Processing Unit
00:04:03 - Overview of quantum chip powered by topological core
00:04:55 - Introduction to the science behind the qubit design
00:06:33 - Challenges in quantum device fabrication and recipe development
00:08:55 - Accelerating innovation and shortening development cycles
00:10:08 - Miniaturization potential – million-qubit chip on credit card size
00:11:46 - Capacitance changes indicate qubit states 0 and 1
00:11:55 - Qubit lifetime extended to a minute—1000x improvement over aluminum devices
00:13:33 - AI-driven optimization over hundreds of design parameters

## Transcript

*1,847 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=0s)** OK, now, now we have it. Thank you. OK, So the reason why we are interested in quantum is because quantum can potentially change entire industry. It can disrupt healthcare industry because if we can enable certain drug discoveries through quantum computation, we can shorten the cycle for therapy development. It can disrupt our energy and climate industries because certain catalysts will enable faster carbon capture or nitrogen fixation fix solve nitrogen fixation problem. So in order for us to be able to to take advantage of it here at Microsoft, we are thinking about a unified approach which combines AI, quantum and high

**[0:54](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=54s)** performance computing. So AI for design and optimization, quantum to enable faster computation and enable to generate high quality data that will be used by AI and HPC. All app basically supports these hybrid workflows and makes the whole approach useful. So we are uniquely positioned to take advantage of quantum by leveraging over 3 components that we are developing within Microsoft. So from the very beginning of this program, we were thinking about full stack quantum machine. It's not about individual qubits or the count of them, but it's about all layers in the stack.

**[1:46](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=106s)** They involve building physical hardware quantum processing units, thinking about quantum error correction and classical compute that is needed for that, and ultimately thinking about the highest layer which involves applications and making the machine useful for for consumer. So at the end of the day, one should think about the CPUGPU and QPU all working seamlessly together within our cloud offerings and enable solving, you know, commercially valuable problems for us. So of course, for us to be able to do that, we need to think strategically and need to think about qubits bottom up. And so from, you know, doing a lot of studies,

**[2:37](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=157s)** we realized that we need to build qubits that are small, roughly Micron size, that are fast, They're doing operations at the microsecond scale, and most importantly, that are reliable. And that's where topological approach shines. Because the idea of topological approach is that if you encode information in these Majorana modes, these exotic quantum degrees of freedom, this information will be inherently protected from or immune from errors and decoherence, which is a difficult problem for all the other platforms. And so in order for us to be able to solve this problem, we had to invent new material stack, new phase of matter that supports these degrees of freedom.

**[3:29](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=209s)** And so we're happy to announce that we developed much better material stack that gives us enormous improvement in cubic lifetime. And we also built a new quantum processing unit with this material stack. And this processing unit is shown here in the picture. It just, and I wanted to showcase it to you right here. This is Majorana 2. So you can see here to the left, a quantum chip that is powered by the topological core. Our cubits are digitally controlled, so we couple them with the cryocemos on the same chip, which helps us to

**[4:21](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=261s)** solve input output problems. And you know, the, the idea is that these qubits, they operate at very low temperature, millikelvin temperatures. And therefore, we want to make sure we, you know, solve, solve this input output problem by placing the cryo CMOS, which controls the operations at the same sort of millikelvin stage as our topological qubits. All right, so, so right, So what is the science behind our qubit? So as I said, we want qubits to be fast, small and reliable.

**[5:09](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=309s)** There are very there. It's very difficult to satisfy all these constraints. And so as I said, we needed to invent a new phase of matter, which is called topological superconductor or in short, topoconductor. So commonly we know phases of matter such as solid, such as liquid, such as gas, but our phase of matter is totally different. It's, it appears when you combine materials such as superconductor, just conventional superconductor and conventional super semiconductor. Superconductor conducts electricity with 0 resistance. Semiconductor has electrons and you can control density of these electrons.

**[5:57](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=357s)** But when you combine them together in the right proportions and use magnetic field, we generate a very unique state that supports these Majorana modes, exotic modes that we encode information in. And so we had to engineer the right, you know, interface between superconductor and semiconductor and make sure that this layered material appears as as one sort of phase of matter, as unified phase of matter. For us to be able to support the stringent requirements, we have to develop new recipes for fabrication quantum devices. They live or die depending on the quality and depending

**[6:47](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=407s)** on the constraints, whether we can satisfy these constraints or not. And so here we are showing device quality that we've achieved last year and here we're showing where we started from. And you can see that the interface between semiconductor, which is down below and superconductor has improved tremendously. And that was, you know, one of the key ingredients that we had to solve. And we've done this by essentially fabricating our devices atom by atom as was shown in this movie. So that was the key recipe for success. And this year we are showing even more improvements by introducing this new material stack. This new material stack has LED superconductor instead of aluminum

**[7:40](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=460s)** 1 and the key advantage of lead superconductor is that it has parent gap 4 times larger than aluminum. And this difference in parent gap directly translates in 1000 X improvement in cubic performance as as as reported in this paper over here. So you know, we had to introduce new superconductor, but we, it's not just drop and replace the superconductor, we actually had to change entire semiconductor stack. We switched the substrate, we optimized quantum well, we've optimized all the interfaces in this stack and make it work with this lat superconductor.

**[8:28](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=508s)** And all these improvements happened within one year. And I have to say, I've been with the program 15 years and the level of improvement which was enabled by AI and simulations that happened over the last year is equivalent to the level of progress that we've made in the first decade of my tenure within Microsoft. So the point is we are accelerating, we're introducing this changing faster, we are shortening development cycle. And if you are interested in more details, we posted the paper on Microsoft based website. This paper also appears on archive and I will encourage you to take a take a look. So once we have the recipe for the material stack

**[9:18](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=558s)** we want to press on, we want to build qubits out of it. So this is how our qubit array looks like. We, our qubits are based on 8 structures that are shown here. So these are superconducting layers that are patterned on top of semiconductor. So here you see two by two array. This two by two array is connected by different gate layers and they correspond to tuning, control and read out layer. And when we want to do single qubit or two qubit measurements, we just activate the right quantum dots, the right layers in order to be able to do these operations. Also, please pay attention to the scale here. The scale is microns.

**[10:08](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=608s)** And I already show you that you know 4 cubits, they are occupying very small area 10s of microns square. So if you want to build million cubit chip, we can put it on a on a on a chip on the the size of the credit card. So our idea is that the qubits that are of this size and densely packed unable to build 1 modular structure that is capable solving, you know, very large complicated commercially viable problems. So, so this is how device actually fabricated device looks like.

**[10:57](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=657s)** So you see these false color 8 structures and you see different gates. As I mentioned, they're used for tuning control and readout. And also you, you, you see here data for the lower qubit, you've tuned up the lower qubit and you've done one of the fundamental measurements on this qubit by, you know, connecting this loop that is shown here at the top and measuring the state of the qubit in AZ configuration in Z basis. And So what you see here is a capacitance trace as a function of time. This is the capacitance that is measured by the readout scheme that we have RF readout scheme that is very fast.

**[11:43](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=703s)** And so we we see these small changes in capacitance and these small changes in capacitance, they correspond to different states of the cubit 0 and one. And the important point that I want to make here that the lifetime of a qubit has increased up to a minute, which is enormous on the scale of qubits. So in the previous device based on aluminum, the maximum lifetime that we were able to achieve was 10 milliseconds. Here we increase this lifetime by a factor, you know, thousand X more. And this is the power of thinking about everything altogether from materials to design enabled by AI and simulations and

**[12:35](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=755s)** optimizing the entire, you know, array, qubit array. So, so this gives us confidence in the approach. It tells you about the velocity of changes that we are introducing in our program that you are able to iterate and introduce new material stack, new design, new system, measure the devices just within one year. And you know that that basically gave us confidence that we can accelerate our road map to building a commercially viable quantum machine from 2033 to 2029. So you know I will. I would like to mention, you know another thing that

**[13:33](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=813s)** this design was really accelerated by AI. We worked with our partners on the discovery team to to use all the design rules, all the requirements and we optimized over more than hundreds of parameters. And by by using some of the tools, AI enabled tools that were provided by our partners, we were able to accelerate the design cycle for such a system tremendously. And we're able to, you know, design essentially such a complicated chip in less than a month. So, so that's sort of the punchline for the story. And you know, again, as I said at the beginning,

**[14:23](https://www.youtube.com/watch?v=rjgsMQ-CO7o&t=863s)** the turn the hard physics problem into a road map for a scalable quantum computer. And we introduce new materials because we think that the secret to be able to make new devices that satisfy the stringent requirements that are needed for quantum computing at scale is through better materials, through better interfaces for better fabrication, round up for better algorithms, through better designs. And so we are we are trying to push on all the cylinders and accelerate moving forward. So with this I want to close the talk and thank you for attention and take questions.
