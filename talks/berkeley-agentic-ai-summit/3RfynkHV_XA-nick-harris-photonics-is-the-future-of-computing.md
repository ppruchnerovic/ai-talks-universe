---
id: 3RfynkHV_XA
title: "Nick Harris - Photonics Is the Future of Computing"
slug: nick-harris-photonics-is-the-future-of-computing
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Nick Harris"]
channel: "Berkeley RDI"
duration_min: 8
published_at: 2026-08-11T05:08:59Z
video_id: 3RfynkHV_XA
url: https://www.youtube.com/watch?v=3RfynkHV_XA
youtube_url: https://www.youtube.com/watch?v=3RfynkHV_XA
tags: []
transcript: true
---

# Nick Harris - Photonics Is the Future of Computing

**Nick Harris**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=3RfynkHV_XA) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,446 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=3RfynkHV_XA&t=2s)** SPEAKER: All right. Looks like we're getting slides up. Great to be here at the Agentic AI summit here at Berkeley. My first visit to Berkeley, I went to MIT. Lots of love for Berkeley. But, yeah, good to be here. So today, I'm going to be telling you about light matter and some of the stuff that we're doing. Ten minutes. So let's jump in. If you zoom out on what's happening in AI, and especially with the advent of Agentic AI workloads, which I remember hearing about starting in 25, which felt pretty early. Really, what's going on, is the world is undergoing a massive AI build out. We're building data centers in Texas and British Columbia that are using as much power as the biggest cities on Earth. Think about New York City, something like seven gigawatts. That's going to be a pretty average data

**[0:49](https://www.youtube.com/watch?v=3RfynkHV_XA&t=49s)** center in Texas, in Abilene. And why is this happening? Like, what's the motivation behind building these energy consuming objects that have hundred times the density of a city. Why are we doing this? Go to the next slide here. My clicker is not clicking. There we go. So here's why. If you look over the past several years at the runtime for AI models, how long can they run given a complex task and have a 50% chance of completing that task? That's been growing exponentially. So now we're at a spot where the latest AI models can run for something like 24 hours and have a 50% chance of getting a problem solved. I don't know anybody who can work for 24 hours

**[1:37](https://www.youtube.com/watch?v=3RfynkHV_XA&t=97s)** nonstop and have a 50% chance at solving a hard technical problem. Certainly I can't do it. And so we're on this trajectory. I can't see any saturation in the data, to be clear. We're on this trajectory where AI models are going to be solving harder and harder, longer time horizon problems all in one go. So it's a pretty incredible capability that we're unlocking. And this is what's underlying the build out, the amount of energy that we're going to spend. All the buildings, the GPUs, the custom AI ASICs that are going to be going into these buildings. This is what underlies it. We're starting to be able to have machines perform calculations and solve problems that are incredibly hard for humans, and we're compressing the amount of time it takes to do very hard and valuable work. So there's one backdrop here to keep in mind.

**[2:29](https://www.youtube.com/watch?v=3RfynkHV_XA&t=149s)** I'm in the hardware space. Lightmatter is building photonic interconnects that link up AI supercomputers. And one of the things we're tracking is the amount of power that's being used for building these systems. And you can see in the White curve, this is the frontier AI model power consumption curve versus the US Energy grid growth rate. You're something like, a few percent per year growth in energy coming online in the US. And AI is really going to smash through what the US Energy grid is going to be able to bring online. There's a lot of work on nuclear reactors. They'll have 1,000 megawatt nuclear reactors per gigawatt data center. I just want to think about a gigawatt with you for a second. A house is a few kilowatts. A rack is starting to be a megawatt. 1,000 racks is a gigawatt.

**[3:18](https://www.youtube.com/watch?v=3RfynkHV_XA&t=198s)** This room could hold a few hundred racks. So think about the energy density of what we're talking about. It's pretty incredible. So how are we going to close this gap? How are we going to let AI continue on this progress curve? I've got an idea and I'll tell you all about it. So it turns out that interconnect is actually the principal challenge. How you allow GPUs and XPUs to communicate is the principal challenge today, in enabling this roadmap for driving AI workloads and enabling growth in the amount of computation that we can do. And that comes from first principles. But I'm going to jump to the conclusion first here. Given a 10-minute talk with ultra fast interconnects. At Lightmatter we use light to connect GPUs and chips. We have single waveguides that transmit 1.6 terabyte per second per optical fiber.

**[4:10](https://www.youtube.com/watch?v=3RfynkHV_XA&t=250s)** That's 1,600 homes worth of bandwidth in a single optical fiber. What we're able to do is improve time to train by 3x. So the same number of GPUs running the same workload three times faster time to train. So your data center finishes that training job for the next fable model. And one third, the time and you can train maybe the next two versions over that month that you're planning to do. Significant improvements in prefill and decode. These are phases of inference 3x for prefill and 11x interactivity tokens per second per user for decode. So linking computer chips together these XPUs these GPUs using light is going to deliver an enormous performance uplift for AI workloads. And why is this happening?

**[4:58](https://www.youtube.com/watch?v=3RfynkHV_XA&t=298s)** What's the fundamental thing that we're driving towards? What is the photonic technology that we build at light matter enable? It enables you to build gigantic computer systems that behave as a single brain. These are strong scaling systems in computer science, if you want to talk about it that way. Strong scaling systems. So normally, you've got two computer chips and you'd like them to run a workload together and you'd like to get two units of performance. And if I have 1,000, I'd like 1,000 units of performance. The challenge is that most workloads are not embarrassingly parallel. You can't run them in parallel like that. They need synchronization. They need to share parts of the operation. And so how do you build a computer that acts over 1,000 chips like a single chip? Well, at the limit, you want to have zero latency in communicating between GPUs and you want to have infinite bandwidth.

**[5:47](https://www.youtube.com/watch?v=3RfynkHV_XA&t=347s)** If you had zero latency and infinite bandwidth, well, there's really no difference between these GPUs that are many meters away. So that's what we do at Lightmatter. We build interconnects that are so blazingly fast. We already have chips that are 114 terabyte per second. State of the art is about ten terabyte per second. We have fibers that are 1.6 terabyte per second, state of the art is 0.2. There's 10 X's all over the place. What we're doing is we are approximating this perfect interconnect, and this perfectly strong scaling supercomputer. Over the next two years, you're going to see the first systems with 1,000 GPUs or XPUs communicating and acting as a single giant GPU or XPU. And this is going to drive those inference and training results that I talked about earlier.

**[6:37](https://www.youtube.com/watch?v=3RfynkHV_XA&t=397s)** So this is what the tech looks like. This is one of our chips M1,000. It's the fastest optical communication device in the world 114 terabyte per second. You can see the optical fibers on the top and bottom. Each one of those fibers is moving 1.6 terabyte per second of data. 1.6 terabyte. 1,600 houses. This chip moves 114,000 houses worth of bandwidth. That's how fast it is. The cables that connect North America to Europe are about 200 terabyte. That's less than two of these chips. This is what's coming. And this is what's going to enable these very large AI supercomputers that act like a single chip. And I'll leave you with this. This is what the systems look like. On the left, we're showing one of our M1000 racks.

**[7:26](https://www.youtube.com/watch?v=3RfynkHV_XA&t=446s)** This single rack is several petabyte per second of IO. So the entire world's traffic internet traffic is a single rack from Lightmatter, M1000 there on the left. And we build out data centers today, because one of the big challenges in computer science and scaling these AI workloads and AI platforms is reliability. You have, let's say, 100,000 GPUs in a data center and ten million connections that are linking them together. Those ten million connections, they better not have any errors. If there are errors, they're going to freeze the AI training workload run. They're going to crash your inference workload. We have to make sure that these systems are extremely reliable. And at Lightmatter we build out entire validation data centers where we're operating hundreds to thousands of these platforms and proving that they just won't crash. They're going to be rock solid as they transport

**[8:15](https://www.youtube.com/watch?v=3RfynkHV_XA&t=495s)** the kind of data on the scale of the internet between the continents. And so with that, I'll thank you guys for the time, and I hope you enjoy the day today.
