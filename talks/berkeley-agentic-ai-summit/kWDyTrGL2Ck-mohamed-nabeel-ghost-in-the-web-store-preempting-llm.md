---
id: kWDyTrGL2Ck
title: "Mohamed Nabeel - Ghost in the Web Store: Preempting LLM Hallucinated Browser Extension Supply Chain"
slug: mohamed-nabeel-ghost-in-the-web-store-preempting-llm
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Mohamed Nabeel"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T07:30:42Z
video_id: kWDyTrGL2Ck
url: https://www.youtube.com/watch?v=kWDyTrGL2Ck
youtube_url: https://www.youtube.com/watch?v=kWDyTrGL2Ck
tags: []
topics: ["Evals, observability & reliability", "Science, healthcare & applied ML"]
transcript: true
---

# Mohamed Nabeel - Ghost in the Web Store: Preempting LLM Hallucinated Browser Extension Supply Chain

**Mohamed Nabeel**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=kWDyTrGL2Ck) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*915 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=kWDyTrGL2Ck&t=2s)** MOHAMED NABEEL: All right. Good evening, everyone. So last talk in this session. After that, I believe it's a workshop. So I won't keep you waiting. As the moderator mentioned, I am a researcher at Palo Alto Network. I've been working in web security space. Recently, we've been looking, thinking, and also working a lot in what would happen with the proliferation of LLMs and agents. Now, it's not the humans who are browsing the web for which we've been building protections over the years. Now, we've been thinking a lot about, how can we build a web which will protect agents and, in turn, will protect the humans? And today's talk is specifically going

**[0:51](https://www.youtube.com/watch?v=kWDyTrGL2Ck&t=51s)** to be on AI hallucinations. And some of the talks already briefly touched upon it, but I'm going to double down on specifically hallucinations on browser extensions, browser being the new operating system. It's very important for us to understand this attack surface. And I want to show you some real-world results we identified through our research. So before that, I just wanted to get a measure of how many of you have seen-- I'm sure most of you are using some kind of a chatbot. How many of you seen any kind of hallucination when you ask for a fact and it confidently tells you that it is true? All right. That's good. I mean, most of you are aware of it. So the level of hallucination can differ from what you ask.

**[1:42](https://www.youtube.com/watch?v=kWDyTrGL2Ck&t=102s)** Most of the existing research, actually, even the benchmarks, are mainly looking at hallucinations on summarization, not on supply chain security or related artifacts. So in this talk, as I mentioned, we are going to hunt for ghosts in browser extensions before attackers go and bring them back to life. So before that, a side story. Sometime back-- I have a young daughter. She asked from me, dad, if I stand on Mars and look at the sky, what color would be the sunset? And I didn't want to disappoint her. So I said, let me look it up and get back to you. So I went to my favorite chatbot and asked about what color would

**[2:34](https://www.youtube.com/watch?v=kWDyTrGL2Ck&t=154s)** the sunset be. And it beautifully described, the sunset will be in red, and with a lot of historic aspects. And then I went back to her and told her. She was happy that I was able to find the answer. But it turns out to be, the sunset is not red color. Anybody knows what color it is? It's blue color. So the reason is-- I mean, we see-- I mean, LLM generalize what we see in Earth to Mars. And also, Mars has this Martian sky. And it used those facts to deduct that it is red color. But the theoretical fact is, red has a longer wavelength,

**[3:25](https://www.youtube.com/watch?v=kWDyTrGL2Ck&t=205s)** and they can't go through particles. And blue has shorter wavelength, and that's why you see blue from-- even the rover that ran on Mars was having pictures with blue. That's a side story. So ever since then, I always double-checked my answers. So the hallucination in the security, it's not a hypothetical problem. There are research showing hallucinations in PyPI and NPM packages. And we also recently did a research on hallucinating domain names. And why this problem is important in browser, because browser extensions are dangerous. They have excessive permissions. They see your session tokens, cookies. And if any of these get compromised,

**[4:12](https://www.youtube.com/watch?v=kWDyTrGL2Ck&t=252s)** the attackers have a front row to your operating system. And the attack is deceptively simple. Attackers don't need to break into a system. They just need to trick the AI to get through your front door, basically use some kind of a hallucination. So the problem arise because of the inherent nature of how LLMs work. So I'm going to show you what is called this hallucination-prone zones. These are the zones at which LLMs don't perform very well. So one of the biggest trends we see is there is a proliferation of extension because of AI. And now, every month, we see around 20,000 extensions. Previously, that many extensions were created within the whole year. LLMs are not good at recency detections.

**[5:02](https://www.youtube.com/watch?v=kWDyTrGL2Ck&t=302s)** So they try to hallucinate and try to be helpful. Another thing is, at the same time, these extensions are created, around thousands of extensions are deleted as well. And LLMs are snapshot learners. They don't have an understanding of deleted extensions. They think they are still existing. And the third one is, not all extensions have a brand, and this also leads LLMs to hallucinate. And these are some of the extensions that LLM hallucinated. These are real extensions, but they are all deleted. And many of them are marked as malware in the browser extension store. And these are another set of extensions which are not claimed, but LLM confidently hallucinated that you can install them.

**[5:51](https://www.youtube.com/watch?v=kWDyTrGL2Ck&t=351s)** And attackers can use them to exploit. And the final slide-- these are the extensions we've been monitoring. We've been rescoring these extensions, and we've been monitoring these highly hallucinated extensions. And after our study, we saw about a dozen of extensions being registered and used for malicious activities. So the key takeaway here is, just don't blindly trust the recommendations that you get from browsers. Always double-check it because it's inherent in LLMs. The hallucinations will never go away, so you will have to always fact-check what you get. Thank you.
