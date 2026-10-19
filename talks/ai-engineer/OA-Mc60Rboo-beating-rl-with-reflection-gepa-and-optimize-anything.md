---
id: OA-Mc60Rboo
title: "Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA"
slug: beating-rl-with-reflection-gepa-and-optimize-anything
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Lakshya A. Agrawal"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-09-26T17:00:06Z
video_id: OA-Mc60Rboo
url: https://www.youtube.com/watch?v=OA-Mc60Rboo
youtube_url: https://www.youtube.com/watch?v=OA-Mc60Rboo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "GEPA", "Lakshya Agrawal", "prompt optimization", "reflective optimization", "Optimize Anything", "GRPO", "reinforcement learning", "agent harness optimization", "agent skills", "ARC-AGI", "self-improving AI", "LLM as a judge", "DSPy", "UC Berkeley", "Sky Computing Lab", "autoresearch", "AI Engineer", "AI Engineer World's Fair"]
topics: ["Coding assistants & agents", "Evals, observability & reliability", "Multimodal, vision, speech & robotics", "Prompting & context engineering", "Training, fine-tuning & model building"]
transcript: true
---

# Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA

**Lakshya A. Agrawal**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#GEPA` `#Lakshya Agrawal` `#prompt optimization` `#reflective optimization` `#Optimize Anything` `#GRPO` `#reinforcement learning` `#agent harness optimization` `#agent skills` `#ARC-AGI` `#self-improving AI` `#LLM as a judge` `#DSPy` `#UC Berkeley` `#Sky Computing Lab` `#autoresearch` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=OA-Mc60Rboo) · [Conference site](https://www.ai.engineer/)

## Description

After one round of reflection on just three examples, GEPA doubled the gains that the RL algorithm GRPO reached after 25,000 rollouts. Lakshya A. Agrawal, creator of GEPA and a PhD student at UC Berkeley's Sky Computing Lab, explains why. RL squeezes a whole rollout down to a single score. GEPA instead has a model read the full trace, including chains of thought, tool calls and error messages, and write a better prompt. A Pareto pool of candidates keeps the search out of local optima.

The same idea works on anything you can write as text and score, which is where Optimize Anything comes in. Agrawal shows it taking a four-line program to a six-step agent that lifts Gemini Flash on ARC-AGI from 32.5% to 89.5%. It pushed an AMD NPU coding agent from 4% to 30%, and improved a GPT-5 mini coding agent on Go issues from 24% to 93%, using learned skills that also carried over to Claude Sonnet. He also covers Databricks tuning an open model to beat Claude Opus at 90x lower cost, learning evals from production traces, and co-optimizing prompts and weights.

Speaker info:
X/Twitter: @LakshyAAAgrawal (https://x.com/LakshyAAAgrawal)

Related links:
GEPA on GitHub: https://github.com/gepa-ai/gepa

Timestamps:
0:00 Intro: reflective optimization
0:30 How we teach AI new tasks
1:00 The sample-efficiency bottleneck
2:05 What RL throws away
3:00 Reflecting in text space
4:25 GEPA
4:50 GEPA vs. GRPO: 3 examples vs. 25,000 rollouts
5:40 What GEPA learns
6:55 GPT-4.1 mini beats GPT-4.1
7:15 A new AMD NPU: 4% to 30%
8:25 How GEPA works
9:00 Why a Pareto pool beats a simple loop
10:10 Results across benchmarks
10:35 Beyond prompts: Optimize Anything
12:05 The API
12:55 A 3D unicorn
13:35 Discovering agent harnesses: ARC-AGI from 32.5% to 89.5%
14:40 MATH-500
15:10 Optimizing agent skills: 24% to 93%
16:40 Three optimization modes
17:30 In production: OCR and a 90x cheaper agent
18:40 Why better models need better prompts
19:10 Learning evals from production traces
19:55 Fast-slow learning: prompts and weights
20:20 Who uses GEPA
20:45 Get started

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*3,581 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=12s)** Hi everyone, my name is Lakshia Agraal and today I'll be presenting on behalf of a very large effort uh the problem of reflective optimization or how can we self-improve prompts agents and models from textual feedback. The question we start with is how can we teach AI to perform new tasks. The standard way has been to perform weight updates with gradient descent either during pre-training, supervised fine-tuning or reinforcement learning. This has proven to be extremely effective, but it requires a huge number of examples. trillions of tokens for pre-training, tens of thousands of labeled examples for supervised fine-tuning or hundreds of thousands of rollouts for reinforcement learning in domains like math coding etc.

**[1:02](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=62s)** However, most teams do not actually have that much data or compute and in fact the problems are that we are trying to tackle with AI now are bottlenecked by sample efficiency. What do we mean by that? Two things. First of all, there is low availability of domain specific knowledge resources which means there is not enough data to perform offline algorithms like SFT. Second, the domains that we are trying to apply AI increasingly are having expensive rollouts where either the LLM workflow pipeline or agentic rollouts are itself uh very slow or expensive to do or the task metric is very slow or expensive to execute. We are seeing that agents can now work for hours on end and if you were to apply an online learning

**[1:49](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=109s)** algorithm to this uh it would require hundreds of thousands of rollouts and it would not be feasible. So we are seeing increasing use of agents for real world product uh applications where uh these invoke tools which can also be long running further exacerbating the sample inefficiency issue. The current dominant paradigm is reinforcement learning with verified rewards where given a model and a task, we perform any number of parallel rollouts and get rewards at the end. Finally, an algorithm like GRPO takes these rewards and converts it into gradients that are applied back to the model. However, as we can see, there was a lot of information in each of these rollouts, but we only learned an O of one score and propagated that via

**[2:38](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=158s)** gradient descent. We can see that there is chains of thought, the tool calls made to the environment, the envir environment's responses to those tool calls, which could potentially contain error messages which also provide diagnostic value and we learned almost nothing from all of that. So the question we ask is can we make use of this other extremely rich information. Our idea is to perform reflective optimization in text space where instead of only using the zero or one reward signal, we can have a language model or an agent look at the trace of the entire rollout and reflect on what worked in them, what did not work in them. And this reflection could potentially use all intermediate outputs and potentially even make other tool calls such as

**[3:27](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=207s)** retrieval from your company's knowledge base or some guide textbook and so on. So that's the first key idea and the second is that instead of only updating weights with small deltas, we can instead update a prompt where a single natural language update can give a very large behavior change. Let's take a simple example. Let's say you're tasked with writing a text summarization system and the prompt of that system says generate a oneline summary. If I just go and tweak that prompt to say generate a 10-line summary, we can all agree that the behavior of the system would change quite significantly with that just one word change. And making that one word change is quite quick and we can reflect on our own behavior and identify what needs to change. If we were to achieve a

**[4:15](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=255s)** similar kind of behavior update from our AI system, we would have to have thousands of gradient very tiny gradient updates sequentially. So with that key idea, we proposed JPEA which is a reflective prompt optimization technique for agents. It uses an evolutionary loop along with a novel parto-based candidate selection which I will come to later. It is akin to doing reinforcement learning in text space where instead of just rewarding receiving a reward score we are actually obtaining score along with textual feedback which can be very domain specific and learn all about the domain from it. Let's compare Japa with gRPO which is one of the leading RL techniques. On the x-axis we have the number of training steps uh also proportional to number of

**[5:02](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=302s)** data samples seen and on the y-axis we have the performance on our domain that we are training for. And what we can see is that Japa in just one round of reflection using just three data points is already able to get twice the performance gains that gpo got after 25,000 rollouts. Continuing to run Japa for a few more steps further increases that gap itself by another 2x. I want to note here that the model Quen 38B is optimizing itself here. There is no external expert teacher involved whatsoever. And what does Japa learn? Unlike prior prompt optimizers somewhat which would uh uh use model idiosyncrasies like my grandmother will be really angry if you

**[5:50](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=350s)** don't generate a good prompt. Here Jpa is actually giving a very detailed problem specification which includes how to make sense of the input. What is the purpose and context of this particular pip part of the pipeline? What are some key observations and lessons from the data? So the prompt we are seeing here is for the second hop of a multihop question answering system where given a question we need to retrieve some documents that could potentially answer that question. Look at those documents summarize it and then finally answer the question. And here what we see is Japa has found out that first hop documents that often cover one entity or aspect and the second hop should actually be uh recovering documents that are related to it. We have seen that human engineering teams whenever a new model comes out

**[6:37](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=397s)** spend weeks of their time manually tweaking one word here and there trying to discover the problem specification. This entire process is fully automated now with Japa which takes about half an hour to 1 hour to run depending on your uh pipelines. We can also apply Japa to leading proprietary models. Just for an example here we were able to optimize GPT 4.1 minis performance to outperform GPT 4.1 on a math task and we can see the kind of information distillation JPA has done in the prompt space itself. Coming back to the problem of sample efficiency, AMD developed a new hardware accelerator called NPU XDNA2 which had used a completely new API to program which had

**[7:27](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=447s)** almost zero available information over on the internet and because of this uh the leading models at the time which was GPT4 was failing miserably to perform this task. We are able to take an existing agent which was getting 4.25% 25% on this task and apply Japa without any other change to the agent itself and we got this prompt and pushed this performance 7x to 30.52%. So what this is uh what this goes to say is there can be lots of domain specific information which if you include in your AI systems prompts the models could actually perform much better and JPA can help you fully automatically discover that. I want to highlight the sentence saying avoid including ADF.h H. Now the interesting thing is AMD actually ships a library called ADF.h for programming

**[8:15](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=495s)** NPUs but that did not work with this latest uh generation of hardware that we were working with and Jeppo was able to discover that in just one step. So how does it work? It's an extremely simple algorithm which simply takes your AI pipeline written in any agentic framework or even raw LLM calls that you may have. It simply runs your systems on a few examples and collects domain specific feedback. whatever information your environment contains is observed. Second, it runs reflection with an LLM or agent that reads the feedback and proposes a better prompt. Finally, and most importantly, it keeps a parto pool where it keeps every single candidate that wins on even one training example and not just the top scorer. The question is, but why keep a parto pool?

**[9:04](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=544s)** And we kept getting asked this question a lot that is Jepper really better than running the model in a loop. So we went and tested it out and what happens is a loop keeps only the best and gets stuck in a local optima. So on the left hand side you see a search tree that was generated by using an LLM in a loop starting from a seed prompt at the top left where um we asked the LLM to improve the prompt. It improved the prompt and it generated a prompt that gave us the middle node. However, this prompt got stuck in a local optima and once again when we asked the LLM to try and improve it, it proposed something but that was not actually better. So, it went back and it again tried to improve it and it kept doing this and it exhausted all of the search budget. On the other hand, with Japa's parto based candidate selection strategy on the

**[9:51](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=591s)** right, we can see that it maintains a much more balanced search process eventually converging to a much higher score. Across four benchmarks, we saw that more than half of the gains seen with Japa actually account for this and it gets almost twice the performance gains that you would get with just applying the model in a loop. Japa can perform really well across diverse benchmarks. Here we see results on question answering, instruction following, claim verification as well as math which all the leading frontier model companies are already optimizing their models a lot for and we are still able to get plus 10% just by optimizing the prompt on it. So we have so far seen Japa only optimizing the prompts but Japa goes far beyond prompts. And because prompts are just text artifacts

**[10:38](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=638s)** that determine AI system behavior, the same algorithm can improve anything that you can express as a piece of text and you can score. For example, your entire agent harness is eventually just a Python or a JavaScript file and we can apply the same kind of reflective optimization process to that entire file and we can work with it. So if you can write it as text and score it, JPA can optimize it. So with that insight in mind, we propose optimize anything which is a universal API for optimizing any text parameter given any domain like code optimization where let's say you want to optimize the CUDA kernel code. The input is just that CUDA kernel code where an evaluator looks at this piece of code, maybe compiles it, profiles it, generates a bunch of related information

**[11:27](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=687s)** that we call as actionable side information which is then provided to an LLM which proposes an better candidate maintaining this parto and it keeps the uh repeating this process um till we get convergence. The same thing can be applied to numeric optimization where your numbers can actually be serialized as text or harness optimization where an entire harness can be serialized as text or even cloud scheduling policy optimization where the scheduling policy or heristic algorithm can be expressed as a piece of text and the evaluator can be something like the negative of cost or some function measuring accuracy uh efficiency and the actionable side information can be something like job traces SLA violations and so on. The API is dead simple to use. All it requires is you give us the set of problems that you care to be solved

**[12:16](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=736s)** along with an evaluator function or a fitness function that returns a score along with any available domain specific side information. If your domain produces expert feedback, return that. If your domain produces compiler error messages, profiler messages, tool call error messages, return that. If you have maybe a written up documentation, return that. any kind of it's a very open-ended dictionary. You can return literally anything and all you do is you call optimize anything with this fitness function and the set of problems that you have and optimize anything will sort of take care of it um and give you a optimized solution. Let's see some applications. Let's say you were tasked with generating a 3D unicorn. This is all the code that you would write or your agent can now write it because we have seen that optimize anything is a

**[13:04](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=784s)** very easy to use API for leading agents like plot code. So all you do is write this code which says optimize a Python program to generate a 3D unicorn. Um and the candidate is a Python script that produces a PNG rendering whatever and here is the result. On the left hand side we can see claude opus 4.6. If you gave it this task, this is what it generated. And on the right hand side, what what we the unicorn that we get with optimize anything. This just for fun. But let's say you were tasked with writing an agent to solve a specific task. Typically teams spend lots and lots of time tweaking their agents, building tools for it, writing tool descriptions, uh carefully orchestrating the control flow and so on. Here we started with a simple four-line Python program that was simply calling a

**[13:53](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=833s)** model's uh chain of thought to solve an RKGI problem. Within just 16 rounds of reflection, JEPA within optimize anything was able to find this sophisticated sixstep agent that took RKGI accuracy on RKGI uh that took RKGI accuracy of Gemini flash from 32.5% to 89.5%. And we can see that this agent is automatic like by itself doing rule hypothesis induction code synthesis. It executes and traces the code automatically debugs this code goes back and proposes new versions of that code. And finally it runs it on the actual test inputs and returns the output. This is a runnable example. You can go to this QR code and you can run this example right now. So um applying the same uh uh like

**[14:43](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=883s)** approach of discovering agent harnesses to math 500 we are able to push its accuracy of GPT 4.1 nano by 20% by simply creating a two-step agent and again I want to emphasize that all we did is we asked optimize anything to optimize an agent file and it was automatically discovering the sophisticated agent architecture and we did not have to do anything other than specifying the objective and the task. Finally, every single one of us is using uh some coding agent like cloud code or codex or maybe your favorite agent and agent skills has become a very leading part of the ecosystem where almost all coding agents understand skills. Let's say you want to optimize skills for your specific repository. This is the code that you write which says learn a skill

**[15:31](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=931s)** from the trajectory. When the coding agent is presented with similar problem, the skill should be helpful. We just gave it this natural language behavior. And what we see is we started with minisu agent with GPT5 mini because we were very budget constrainted and we were able to take its performance from 24% to 93%. An almost 3x jump on go repository issue resolution but more importantly the skills that were optimized very cheaply on a GPT5 mini agent we are able to take that and apply to the latest claude sonnet. This was done of uh about a few months back but we applied it to clots onet 4.5 pushing its accuracy to 100% issue resolution while more importantly cutting down the execution time or issue resolution time by almost 50%. We cut it down into half

**[16:20](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=980s)** which also means it spent less tokens because skills contain information about how the repository is organized, how to invoke the test cases, where a particular feature is implemented, um what are the build system used by this repository and so on. This is a a feature called GSkill. You can find it in the JPA repository and it's fully open source as well. So, optimize anything is a single uh interface that provides three optimization modes. If you have just a single problem like there is a single matrix multiplication kernel that you want to optimize you can use it that way. If you have any number of related problems like you want to optimize a matrix multiplication kernel along with a dot product kernel and you know there might be some information transfer between these two you can use what we call as the multitask search mode and finally build a skill which is if you want to optimize on a set number

**[17:09](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=1029s)** of problems but your uh deployment can actually come up with many new problems. So like uh in case of math op like in case of math prompt optimization we are training on some examples but when we deploy it we can receive a completely new kind of query. So we care about generalization mode. So there you can do prompt optimization agent architecture optimization and so on. So optimize anything is can be used for a broad set of domains including cloud scheduling policy optimization where we were able to cut costs by almost 40% compared to expert huristics write custom solvers to match and exceed Optina even in blackbox mathematical optimization create agent skills prompt optimization and so on. It is so easy to use that within just 20 hours of releasing it, people at Snorkel had

**[17:58](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=1078s)** already improved some of their internal benchmarks with it and were tweeting about it. So, and Japa also improves multimodel VLM models performance. Here we are able to cut OCR error rates for leading models by almost 35%. And this is an externally validated report. Um, similar similarly, data bricks actually achieved 90x cost reduction in their deployed agents performance. uh uh performance and here they were able to tune GPT OSS 120B to outperform Claude Opus while being 90x cheaper. More importantly, the performance delta improvement that you see on top of Claude Opus is actually bigger than the one you see on open source models. Some people have asked me that oh as models get better the importance of prompt optimization will go down. I argue the opposite which is as models get better

**[18:48](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=1128s)** they will get better at instruction following and the more precise instruction about your task that you have to give to a very smart model the better that model will be at a uh solving your task and this is exactly what we see happening here the better the instruction was claopus actually jumped much uh higher some people have this question of uh what if we have subjective tasks which are very hard to evaluate jpa can actually learn evals for your task from production traces. The way to do that is you collect a bunch of production traces from your agent. Get a human to annotate just about 50 of those trajectories giving very detailed feedback. This is a long response. This is a short response. This is a good response. This uses this terminology, whatever. And once you get those human annotations, you can use JPA

**[19:35](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=1175s)** to optimize an LLM as a judge prompt. And you can use that LLM as a judge prompt then to go back and optimize your agent and deploy that agent. And this becomes a data flywheel where you can keep improving it. And this is a successful paradigm that uh some leading teams in production are already using. Then the question we get asked is like can we actually use this uh reflective optimization to train models and we recently had this paper called learning fast and slow where we propose fast slow learning where we can co-optimize model weights and prompt harnesses and this shows some very strong properties that one would want in a continual learning algorithm. Um I don't have much time to go over details but please uh look at the uh papers and uh since uh since release Japa has been used in production by these companies as

**[20:24](https://www.youtube.com/watch?v=OA-Mc60Rboo&t=1224s)** well as the main methodology in these papers and here the CEO of Dropbox and Shopify are talking about their use of Japa and OpenAI also wrote a blog post about how you can build self-improving AI systems with Japa. Um so it's very simple to get started. It can plug into any framework, any model and it has absolutely zero hard dependencies. So you can deploy it any in any kind of setting. So um don't be afraid to optimize in the tech space and many problems can be framed as optimization. So bring actionable side information and surface as much domain specific information as you can to optimizers and the optimizers of future will be able to work with them. So please go and check it out. Thank you very much.
