---
id: I7RIwkqTl1s
title: "Jonathan Welch - Building AI for the Physical World: Lessons from Accelerating Discovery for Chem..."
slug: jonathan-welch-building-ai-for-the-physical-world-lessons
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Jonathan Welch"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-11T19:52:19Z
video_id: I7RIwkqTl1s
url: https://www.youtube.com/watch?v=I7RIwkqTl1s
youtube_url: https://www.youtube.com/watch?v=I7RIwkqTl1s
tags: []
transcript: true
---

# Jonathan Welch - Building AI for the Physical World: Lessons from Accelerating Discovery for Chem...

**Jonathan Welch**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=I7RIwkqTl1s) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,103 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=I7RIwkqTl1s&t=2s)** JONATHAN WELCH: Thank you, everybody. I really appreciate you listening to me today. I'm Jonathan Welch. I lead AI at Albert. Albert is an AI native operating system that was built to be a collaborative surface, where AI agents and chemists can work together to accelerate discovery and bring new materials to market faster. We are an R&D platform for some of the largest chemical companies in the world. And when it comes to deploying AI at enterprise scale, we've learned that how skeptical bench chemists can actually be, because they are inventing things that-- sorry. They expect a lot of it, and they don't forgive even simple mistakes, much less costly, complex ones, very easily. But today I want to share with you some of the lessons that we've learned and what we think that actually means for developing authentic discovery tools for industrial chemistry and some things to consider if you're building for this domain.

**[0:51](https://www.youtube.com/watch?v=I7RIwkqTl1s&t=51s)** So industrial chemistry for us, this is the chemistry that makes up the room around us. This is the paints and coatings on the walls, the glass adhesive-- I'm sorry. The adhesives on your phones, the coatings on your glasses, the personal care objects or products you may have used this morning. And these are all formulated products. Formulation science is actually the largest domain in industrial chemistry. More than half of a $200 billion annual R&D spend goes towards formulated products like these. And it's in this domain that, actually, for agentic scientists, it is the least accessible. Because most of the knowledge today that determines success lives in tacit, unpublished, proprietary form, and it is seldom, if ever, surfaced to the actual public sphere. Now, in this domain today, Albert's co-scientists actually help our partners invent products at over a billion people depend upon every day.

**[1:39](https://www.youtube.com/watch?v=I7RIwkqTl1s&t=99s)** This is the way that these chemists carry into every decision, and it's exactly why building AI for scientific discovery has taught us that, above all else, trust is actually the most important feature. It's not accuracy in the abstract. It's not right capability or amazing, but often isolated results. But trust is when you have alignment with their domain. This seems obvious. And I realize that, and it's easy to lose track of this, though, when you're building capabilities without clear problem selection criteria. Because when your job as a chemist is to maintain a material market segment that reaches a billion people's hands, you have high expectations. And the truth is that once you reach a system and you begin to see that it's beginning to reason in a confidently wrong way, you don't just lose trust in the answer, you begin to lose trust in you, the one who's actually developing the agentic system. And winning either back is a very steep climb. Now, the crazy thing is that trust doesn't break down

**[2:28](https://www.youtube.com/watch?v=I7RIwkqTl1s&t=148s)** through some dramatic failure of complex reasoning. It breaks down through something simple and quiet. It's oftentimes just basic misalignment with their domain. This is a simple example of that. This is a real query from a formulation chemist searching for an actual patent for the agent to reason with. Two passages. Both of them look like they could answer it. One of them, however, is correct. And a leading embedding model actually ranks the correct answer in the 300th position. Well beyond, actually, the 300 position, which is well outside what typical reranking systems actually check in production. And perhaps even more surprising on this one was that the difference in similarity score between these two passages, despite their rankings with respect to the query, was actually almost the same. It was basically a zero difference, which means that the model has absolutely no within-domain discrimination when it comes to formulary chemistry. For an agentic scientist, this isn't just

**[3:16](https://www.youtube.com/watch?v=I7RIwkqTl1s&t=196s)** a bad retrieval at retrieval. At this point, it becomes a false belief that it begins to reason from very confidently. So to solve this problem, what we have to do is we dig under the surface and see what makes these passages actually different. Both passages share similar material ontologies. They have similar function and final application domain. But by using an ontological signal to actually surface what a formulation chemist would use to tell these things apart, this is how we actually begin to get domain alignment, and we can build powerful training signals for within-domain discrimination. Now, for our customers and our partners, this is a really important issue to be able to find the right information, and so we began to build benchmarks to understand where within-domain discriminations like this live for industrial chemistry. And using the same public corpus across every model, we find that commercial APIs score effectively zero on this. They have no within-domain discrimination. Open-base models do better, but even continued pretraining on those doesn't actually really work.

**[4:06](https://www.youtube.com/watch?v=I7RIwkqTl1s&t=246s)** What does work is when you get to task-specific, ontologically structured contrastive training which teaches the model the actual shape of the domain chemistry, not just showing it more chemistry text, but actually finding alignment with how the actual users think. That took us from a near-zero model in production to something that was actually meaningful at enterprise scale. We're finding that reasoning and discovery, where uncertainty can be really high, is only as good as the alignment between the system and the actual problem space that is applied to. This is why we think that a lot of the more scalable AI solutions are going to have to be very AI-- sorry, very domain-native, which I think some of the talks today we've seen, that as we get to more specialized domains, building AIs that really understand that is good. The example you just saw demonstrates trust in the-- sorry-- how to restore trust and the answer by aligning with the domain, but it's also focused

**[4:55](https://www.youtube.com/watch?v=I7RIwkqTl1s&t=295s)** on closing the gap on public data. Longer term, the more important piece of trust is actually the second kind, which is the trust that you have when building a genetic systems for actual users. The public record of science is survivorship biased, and so, as a result, we have a tendency to miss what's beneath the surface on a lot of these systems. But a lot of this knowledge does live inside of enterprise R&D today. And by focusing on asking yourself the question of, What are we doing to actually build trust in the AI that we're building for the end users? This is how you get access to this kind of data. Thank you very much.
