---
id: yEeXwZzkgj8
title: "Andrew Schoen - Solving Quantum Sci Problems with SMART: A Self-evolving Multi-Agent Research Tree"
slug: andrew-schoen-solving-quantum-sci-problems-with-smart-a
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Andrew Schoen"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-12T08:05:28Z
video_id: yEeXwZzkgj8
url: https://www.youtube.com/watch?v=yEeXwZzkgj8
youtube_url: https://www.youtube.com/watch?v=yEeXwZzkgj8
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Andrew Schoen - Solving Quantum Sci Problems with SMART: A Self-evolving Multi-Agent Research Tree

**Andrew Schoen**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=yEeXwZzkgj8) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,474 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=1s)** MINGYU KANG: I guess I could take one question. Yeah? Yeah. Yes please. AUDIENCE: What kind [INAUDIBLE]? MINGYU KANG: As you'll see, we're starting with neutral atoms because we're solving a very interesting problem there. It's about moving atoms around. You'll see later. Hopefully, a video, which will be really challenging for this presentation system. But yeah, we're starting from neutral atoms. But really, we're not even limiting ourselves to quantum science. We're certainly not limiting ourselves to a particular platform. Perfect. Solving Quantum Science Problems with SMART Self-evolving Multi-Agent Research Tree. My name is Mingyu Kang, and this is a joint work with Daniel Lee and Andrew Schoen. That's what I was talking about, three pillars

**[0:52](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=52s)** of scientific discovery. First is intelligence. Second is computation. And third is validation, doing actual experiments. So in the agentic system that can go over this loop, would lead us to transformative scientific discoveries. And our first target domain for scientific discoveries is quantum science, which is our strategic Everest. Why start with quantum? One reason is that quantum science is very challenging and multidisciplinary. Quantum science is a mix of frontier research and math, physics, computer science, engineering, material science, and so on. Another reason is that quantum science demands extreme rigor. Unless every single piece is correct, the quantum experiment simply would not work. Another reason is that the quality delta in quantum research is massive.

**[1:41](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=101s)** So the high quality research is very rare, and the experts are very concerned about AI slop. So once we climb this strategic Everest, then we believe that the agentic system will be capable of leading scientific discoveries in any domain. Here's a single slide review of quantum computing, which is at the center of quantum science. First, quantum logic works with qubits, not bits. A bit is a 0 or 1, just like a coin flip. But a qubit can be in a superposition of 0 and 1 states, which can be at any point on a sphere. Second, quantum physics gives us access to qubits. For example, you can take two of the stable electronic energy levels of an atom to form a qubit. And finally, quantum hardware platform

**[2:29](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=149s)** gives us full control of quantum physics to compute with qubits. What you see here is an array of atoms that you can control with lasers. So building a quantum computer like this is obviously very challenging experiment. And that involves a lot of deep theories, which makes this a strategic Everest for scientific discovery agents. Now, let's move on to the agentic system that we're building. We strongly believe that transformative scientific discoveries will come from human-AI collaboration. And this leads us to three key design principles. The first design principle is that the workflow tree keeps getting updated as the agents explore. And the second design principle is that the agentic system is structured but also flexible. And another design principle is that the agents

**[3:17](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=197s)** are autonomous, but also allow humans to intervene at any time. And that means we need a completely different agentic system than loop engineering, which is widely used for tasks that are much simpler than scientific discovery. That leads us to SMART, the Self-evolving Multi-Agent Research Tree. The main feature is that we have a tree consisting of nodes, where each node is consisting of planner, worker, and verifier agents. Then the verifier agent outputs are fed into the tree planner agent, which designs the workflow tree of the next set. And here are some example trees. Each node can be either a goal or a task. And at the next step, the task can be split, merged, selected, or added.

**[4:11](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=251s)** And here's an example user interface. In research, unpredictable things always happen, just like slides not appearing or the laptop crashing. So it's really important to have the flexibility to allow human intervention. Here's another user interface example, where the human researcher is probing the outputs that the agents produced. And here, the key features are managing the context, using the models, choosing the models, and tracking the cost. Now, let's move on to the benchmark results. Well, there are many different agentic systems for scientific discovery. SMART has advantages in that it is both steerable and adaptive. And that's because we designed it

**[4:58](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=298s)** to be structured and structured and flexible at the same time. We compared the performance of our alpha prototype of SMART against frontier models and systems on the scientific reasoning benchmark called frontier science, made by OpenAI. And as you can see here, our prototype is achieving the highest accuracy with a cost that is only one fifth the cost of the second best system, which is Codex 5.5. And the low cost is achieved by using GLM-5.1 as the underlying model. And the high accuracy is achieved by orchestrating the agents. We can plot the same thing on a 2D chart, where y-axis is the accuracy, and x-axis is the cost. And it's very clear that SMART defines the Pareto frontier with high accuracy and low cost.

**[5:47](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=347s)** And this is just a prototype, so I'm sure we can boost the performance by further optimization. Now, let's move on to how we can use SMART to solve real world problems in quantum science, which is speeding up neutral atom quantum computers. Quantum computing is all about doing computation faster. So we want to reduce the wall clock time. In this case, we want to speed up performing the quantum circuits with neutral atoms. So what you see on the left is a quantum circuit. The horizontal lines are the qubits. And we apply these things called quantum gates. The blue ones are called entangling gates. And they are performed by putting two qubit atoms close together in the entanglement zone. So to perform a quantum circuit in the zone architecture

**[6:38](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=398s)** neutral atom quantum computer, you first need to allocate these qubit atoms in the slots of the storage zone. And then you shuttle the atoms in and out of the entanglement zone so that you can perform the entangling gates. But there's a caveat. We can't just arbitrarily move the atoms around. As we're using laser beams to move around the atoms, there are certain constraints that need to be satisfied. For example, what you see on the top left corner is that the rows and columns that define a block of atoms cannot cross the rows and columns of the other block. So this leads us to a very interesting problem. Given the quantum circuit and the zoned architecture, what is the optimal allocation and routing of the qubit atoms

**[7:28](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=448s)** such that the rearrangement time can be minimized while satisfying the atom movement constraints? It's a very challenging where the solution space is very vast. And it's also really important for neutral atom quantum computers. And that's why we choose this as the first problem to discover better solutions with our agentic system SMART. And here are the results. Here, lower numbers are better because that means it takes less time to perform the circuit. And across these four benchmark quantum circuits, smart solutions achieve achieved from 83% to 25% lower re-arrangement time compared to the state-of-the-art. And now, let's look at the ablation studies to understand how the agents find better solutions. Here are multiple agents explore different strategies

**[8:18](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=498s)** as listed below the chart. And here, really, the takeaway is that different circuits are improved by different combinations of strategies. For example, on the left, for the graph state circuit, the rearrangement time is reduced by 83% by solely using the structure of the circuit. While on the right, for the QPE [INAUDIBLE] circuit, the 25% reduction comes from a combination of parameter tuning and they start redesign. And here, using the structure does not help at all. So really, this complementarity of different strategies is what makes the multi-agent framework so powerful. And here is how SMART is used for this problem. First, agents explore different strategies,

**[9:05](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=545s)** and then the tasks are split, merged, and so on, until they find the better solution. Now, here is a simulated video of rearranging the atoms. Please focus on the right panel as it finishes very fast. Oh, it works. So as you can see here, the smart solution clearly exploits some kind of structure while the baseline state of the art fails to do so. So it takes much longer time. With that, I'll just put the conclusion slide here. But I just want to point out that there are other tremendously interesting and challenging problems in quantum science, such as error correction, that we can solve with SMART.

**[9:54](https://www.youtube.com/watch?v=yEeXwZzkgj8&t=594s)** And that would be the proving ground for building agents that lead us to transformative scientific discoveries in various frontier domains. Thank you for listening. [APPLAUSE]
