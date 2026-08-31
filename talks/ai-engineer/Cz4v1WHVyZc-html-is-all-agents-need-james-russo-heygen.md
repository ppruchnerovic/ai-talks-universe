---
id: Cz4v1WHVyZc
title: "HTML Is All Agents Need — James Russo, HeyGen"
slug: html-is-all-agents-need-james-russo-heygen
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["James Russo"]
channel: null
duration_min: 15
published_at: 2026-07-21T18:54:01Z
video_id: Cz4v1WHVyZc
youtube_url: https://www.youtube.com/watch?v=Cz4v1WHVyZc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# HTML Is All Agents Need — James Russo, HeyGen

**James Russo**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Cz4v1WHVyZc) · [Conference site](https://www.ai.engineer/)

## Description

LLMs are great at writing code. So the question we kept asking was: can they write code that produces a video? We thought it would be easy. The reality was a year of trying. We started with massive prompts to get very mediocre output. We made it more agentic to iterate and improve its output. This worked okay but wasn't production-ready. Eventually we tried Remotion. It got us deterministic video, but the React framework kept boxing the agent in. The more guardrails we added, the safer and more boring the outputs got. When we utilized plain HTML, CSS, and JavaScript, the creativity came back to the output. So we set out to build a video rendering framework on top of HTML. But it needed to work with Gemini Flash. Why? Because one tell that a framework is fighting an agent is needing the biggest model just to get usable output. So from there we shaped the framework around what small models could reliably author. That left one real engineering question: can we keep the freedom of HTML and still render a deterministic MP4? Browsers don't want to do that. Image decoders, font loaders, and animation clocks all run async on their own schedule. Great for performance. Terrible for "render the same pixels every time." Throughout, we iterated constantly with agentic loops and self-improving evals to test out the framework, find issues in our renderer, and shape a set of skills that gave the agents Taste instead of guardrails. This talk is what it took to get there.

Speaker:
James Russo — Software Engineer, HeyGen
Engineering lead for HyperFrames. Currently at HeyGen building the future of video storytelling, Previously at Brex
X: https://x.com/Rames_Jusso

Timeline:

0:00 Introduction and the HeyGen mission
0:58 The challenge of creating launch videos
1:27 The importance of A-roll, B-roll, and composition
2:13 Why HTML, CSS, and JavaScript are the native languages of LLMs
3:06 Comparing HTML to other frameworks like Remotion
5:24 Designing the Hyperframes framework with Gemini Flash
6:54 How Hyperframes works in the browser
8:56 Leveraging browser-native technologies like Three.js and WebGL
9:25 Using Skills to teach agents video taste
10:56 Crafting videos: the human-in-the-loop workflow
12:09 Keyframes integration
12:35 Scaling and performance metrics
13:28 Future goals: Code-to-Video benchmarking

Quotes:

"Why not let the LLMs and agents talk in their native tongue when creating videos?" (2:58)
"One tell that a framework is fighting an agent is needing the biggest model just to get usable output." (5:24)
"We don't have to teach them the language. We just teach them how to create good videos." (9:46)
"Agents have made building incredibly easy. Launching is still quite hard." (14:31)
