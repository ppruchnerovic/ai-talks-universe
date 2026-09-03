---
id: 2FZtNtU9RNQ
title: "Ian Fischer - An Optimization Perspective on Recursive Self Improvement"
slug: ian-fischer-an-optimization-perspective-on-recursive-self
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Ian Fischer"]
channel: "Berkeley RDI"
duration_min: 11
published_at: 2026-08-12T01:56:10Z
video_id: 2FZtNtU9RNQ
url: https://www.youtube.com/watch?v=2FZtNtU9RNQ
youtube_url: https://www.youtube.com/watch?v=2FZtNtU9RNQ
tags: []
topics: []
transcript: true
---

# Ian Fischer - An Optimization Perspective on Recursive Self Improvement

**Ian Fischer**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=2FZtNtU9RNQ) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,547 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=1s)** IAN FISCHER: My name is Ian Fischer. I'm a co-founder and co-CEO of Poetiq. And Poetiq, if haven't heard of us, is a startup we founded about a year and a half ago, that's entirely focused on recursive self-improvement. So we're building AI that improves itself. And in the past year, and a little less than a year, our focus has taken us from nothing to a system that automatically can set state-of-the-art on a wide variety of major public benchmarks. We're 10 scientists and engineers, mostly from Google DeepMind and Apple, Microsoft, Amazon, ByteDance. Some of our early results we had on reasoning, and knowledge extraction, setting state-of-the-arts on all of these, and coding. So, let me dive into this.

**[0:51](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=51s)** I want to define carefully what RSI is. And so, it should be really simple. There's only three letters. And really two of them are doing all the work here. So recursive means that the new improvements at each step are going to drive the next round of improvements. And self is the system really is going to improve itself, not some other target. Improvement is really obvious. Everybody is doing improvement of some sort. But R and S really come together as a pair. If you don't have both of them, you really aren't doing the right thing. And the reason that I'm being a little pedantic here is that common use of RSI is both too permissive and too restrictive. So some people have described approaches

**[1:41](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=101s)** as being RSI that are really just a standard iterative improvement loop. And other commentators, other people think that RSI is something is only RSI if you are improving the parameters of a large language model. And this is too restrictive because there are a lot of other pieces of an intelligent system that can be improved quite effectively. And so, why does RSI matter? We think that RSI is the most important frontier in AI research because the improvements of RSI systems compound. And this is going to lead to superintelligence much more quickly than human-driven improvements are likely to achieve. The obvious reasons that humans don't become inexorably smarter

**[2:30](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=150s)** while improving models. But RSI systems can. So I'll talk a bit about the landscape here. We can split RSI approaches on two axes. On the y-axis, we're going from cheap at the top to expensive at the bottom. And on the x-axis going from things that really aren't RSI. So just standard iterative optimization approaches on the left to things that RSI on the right. And so, the upper right quadrant here is a nice place to be. Of course, we put Poetiq there. But that's not arbitrary. We put ourselves there because our loop does in fact compound. It really is RSI. And each step of RSI only costs an inference run rather than a training run for an LLM. In the lower right are where the best funded efforts are.

**[3:22](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=202s)** This is what people generally think of when they're talking about RSI. Again, this LLM-centric perspective where Anthropic, OpenAI, and Google are putting a lot of effort. And these are genuinely RSI, but they do require to train an LLM from scratch at every step. In the upper right, we have a few neighbors. And they're also genuine RSI. And they're also cheap. But they're a bit narrower than our approach. Like Darwin Godel machines and SICA are both targeting coding primarily. And the MiniMax harness trains on some of its own generated data. So, as I mentioned, basically, you can partition this landscape into two pieces. And on the bottom, we have LLM-centric approaches that focus primarily on improving a particular LLM.

**[4:14](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=254s)** And then on the top, we have more systems oriented approaches that view the LLM just as a component of a broader system that should be improved. And shifting from an LLM-centric view to a systems-oriented view opens up a lot of possibilities for improvement that you would otherwise miss. Also, they tend to be faster and cheaper. So I'll talk a little bit about two of the really prominent approaches. One is what the recent Anthropic post AI that builds itself describes where you take a version of Claude. You put it inside of a Cloud Code, And then humans plus Cloud Code improve Claude. And so this is partial RSI. Clearly, Claude is part of the system

**[5:06](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=306s)** that's being-- it's the thing that's being improved. And it's part of the system that's improving it. But there are humans in there. So I don't want to count them. And Anthropic doesn't count them either. On the right, we have another common approach called an automated AI scientist. This is similar also to auto research. And this is typically not going to be RSI. There's a number of nodes here that are doing different things. But basically, the system generates a hypothesis. And then it implements that hypothesis. And then it measures it. And then it writes a paper about it and puts that paper back into some knowledge store. And this usually is not targeting a piece of its system itself, so it's not actually going to be RSI.

**[5:54](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=354s)** But we can make both of these into pure RSI systems. In the case of Anthropic, we can just get rid of the humans. They've indicated that that's where they're headed. And that's maybe something that they're worried about. For the AI scientist, it's also a simple fix. You just target the LLM that you use in your ASI-- excuse me, in your AI scientist loop. Of course, doing that makes it a much more expensive than what most people are doing with automated AI scientists. So what does Poetiq do? So what we're doing is what we call self-optimizing optimizers. So what does this look like? We start with a general purpose optimizer, where a general purpose optimizer

**[6:42](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=402s)** is one that doesn't rely on any specialized signals like gradients. It just requires measurable feedback from the optimization target. So this is more general even than black box optimizers like hill-climbing, because it doesn't have to be quantitative in nature. So then, given that optimizer, that general purpose optimizer, let's use it to optimize something. So we'll have some optimization target. It's providing feedback to the optimizer. And as I said, the feedback here can be quite arbitrary. So it could be standard approaches like accuracy, costs, things like this, or more unusual feedback like rubric evaluations or reasoning targets. So, once we have these two pieces,

**[7:29](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=449s)** this clearly is still not RSI. This is just a standard iterative optimization. But we have this framework of a general purpose optimizer that we can then apply to the optimizer itself. So now, the optimizer is optimizing the optimizer that's optimizing the optimization target. And this is now RSI. So in order to have an optimizer that can optimize itself, you only need two things. It needs to be a general purpose optimizer. And the optimizer needs to provide feedback about its performance. So since we started with a general purpose optimizer and every optimizer can do that, we don't have a problem here. But I want to be clear, this is very different from saying that the optimizer is Adam or SGD.

**[8:20](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=500s)** That would not work. So this is what we call the Poetiq metasystem. It is RSI. And we use it to optimize everything. So every task that the metasystem optimizes helps it optimize itself, which makes it become a more powerful optimizer. And again, since it is a general purpose optimizer, we can point it at any part of the metasystem itself, as well as at any other measurable task like benchmarks, the benchmarks that I showed you at the beginning, customer data, things like this. So talking about what we-- empirical results here are most recent empirical results. We have this blog post where we pointed out that benchmarks are dead for us.

**[9:08](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=548s)** And what this is really referring to is not that benchmarks aren't useful, but that in the presence of a properly, recursively self-improving system, static benchmarks have fairly limited value because we are able to fully, automatically get SOTA results, state-of-the-art results on every benchmark we've turned it on. And so again, as I said, it's fully automatically. We saw zero human interventions and usually quite quickly. So concretely, here's a table, a bunch of results. The interesting thing, or one of the interesting things here is that on half of these benchmarks, which are across a wide variety of different domains that we've never worked on before.

**[9:56](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=596s)** We got SOTA using older, cheaper models than whoever held the previous SOTA, typically table five. So what's next after now that we're not focusing on benchmarks? We are working with early customers in a variety of domains. And I want to leave you with just this perspective on the frontier that the next phase transition in AI is going to come from a system that invents its own improvements. And so, at Poetiq, we're intentionally casting a very wide net for that phase transition, again, by taking this optimization perspective on RSI and using it to optimize everything, including

**[10:45](https://www.youtube.com/watch?v=2FZtNtU9RNQ&t=645s)** the optimizers themselves. Thank you. And we're hiring.
