---
id: SWdcSCRYhds
title: "Brian Joe: Runtime is Where AI Lives"
slug: brian-joe-runtime-is-where-ai-lives
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 10
published_at: 2026-10-07T23:08:34Z
video_id: SWdcSCRYhds
url: https://www.youtube.com/watch?v=SWdcSCRYhds
youtube_url: https://www.youtube.com/watch?v=SWdcSCRYhds
tags: []
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: true
---

# Brian Joe: Runtime is Where AI Lives

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=SWdcSCRYhds) · [Conference site](https://aiconference.com/)

## Description

Your AI stack didn't add a new application. It added a newparticipant. Agents now make calls, invoke tools, read untrusted content, and act on your systems with credentials of their own — and almost all of it happens at Layer 7, in runtime, where your existing controls were never designed to look. AI opened four new doors at once: autonomous agents, prompt injection, the model supply chain, and identity sprawl. Meanwhile attackers do what they've always done — move across identity, apps, APIs, data, and infrastructure without respecting the tool boundaries we bought. This session makes the case that runtime is becoming the control plane for modern security, and shows what that actually changes day to day: vulnerability management driven by what's exposed and reachable instead of a CVSS backlog; detection built on behavior instead of static signatures; and the shift frompanic patchtorapid protection— reduce risk now, patch on your timeline. Brian Joe, CPO and co-founder of Impart Security, will walk through the four AI threat vectors, the unified runtime view, and a practical picture of SecOps in the AI era.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,538 words · source: supa (en, exact timings)*

**[0:15](https://www.youtube.com/watch?v=SWdcSCRYhds&t=15s)** [applause] Good afternoon everyone. Hope you're all having a good conference. I'm happy to be here today. I'm going to be uh having a conversation with you. I'm going to be asking you some questions and I'm hoping that some of you will raise your hands. So, the first question we're going to start with is where does AI live? So, uh raise your hand if you think AI lives in the browser. Nobody. Cool. Raise your hand if you think it lives in the harness. Nobody again. I thought someone would say yes. How about the laptops? Raise your hand if you think AI lives in a laptop or endpoint. One person and then put his hand down right away. Two people. All right. Uh raise your hand if you think AI lives in the cloud. All right. We're getting some more here.

**[1:06](https://www.youtube.com/watch?v=SWdcSCRYhds&t=66s)** Raise your hand if you think AI lives everywhere there's a computer running. All right. All right. That's what that's what I thought. Okay. Now I'm going to flip the question. Now, where does AI risk live? Raise your hand if you think it lives in the browser. >> Oh, interesting. What if it lives in the Raise your hand if you think it lives in the harness? Raise your hand if you think it lives in the end points. Raise your hand if you think it lives in the cloud. And big finish. Raise your hand if you think air risk lives everywhere there's a computer running. All right. So uh I think we've established that uh AI lives everywhere there's a computer running. What was interesting to me is

**[1:54](https://www.youtube.com/watch?v=SWdcSCRYhds&t=114s)** the difference between the two questions. Almost nobody thought AI lived in the first three things. Uh but everybody realized that AI risk lives in the first three things. Um so that begs the question if AI lives everywhere where is the best control point to reduce AI risk? For those of you who uh don't work in cyber security, uh there was a big cyber incident about a month ago with OpenAI and Hugging Face. It's gone pretty mainstream, so probably most of you have heard about this. Um one of the things I'll point out that uh you know some people might not realize is the scale of this attack. Uh so the key metric and this is from the hugging face report that stood out to me is that over a period of five days

**[2:42](https://www.youtube.com/watch?v=SWdcSCRYhds&t=162s)** uh an attacker sent 17,613 malicious requests to hugging face. This is simply a scale and speed that has historically been reserved only for nation state attackers and is now happening on accident. Furthermore, if you look at how the attack uh happened and unfolded in in real life, you'll see that it actually touched a lot of different parts of the internet. It touched a sandbox in the open AI environment where they were running training training jobs. It touched a third a third party code sandbox where malicious code was hosted. It touched the hugging face network perimeter where injection attack was successfully executed and it touched the

**[3:31](https://www.youtube.com/watch?v=SWdcSCRYhds&t=211s)** hugging face cloud where data was uh exfiltrated from and it also um and it also touched a few other places. So seeing as how risk lives everywhere and AI lives everywhere, what would have been the best AI control point using hugging face as an example? So we're going to go through all the different parts of the the ecosystem and evaluate them one by one. So first let's think about where the model was running. Model training model alignment. Is this something that could have seen the AI attack? No, because training happens before beforehand. The attack happened after the model was trained. Now if the model was properly trained,

**[4:19](https://www.youtube.com/watch?v=SWdcSCRYhds&t=259s)** could it have stopped attack? Yeah, maybe. But it never uh wouldn't have actually seen it happening. Let's look at the next uh part of the the ecosystem, the browser. Was there a browser involved in the hugging face attack? There was no browser. So browser could not have seen the attack nor could it have stopped anything. Let's think about the laptop the endpoints. Were there any laptops involved in this situation? No. Again, uh this is all happening in the cloud. So a laptop or endpoint would not have been able to see an attack nor stop it. Third party code sandbox. Could this have seen the attack? >> No. It's just code. It's like it's like a GitHub in the cloud sort of thing.

**[5:07](https://www.youtube.com/watch?v=SWdcSCRYhds&t=307s)** Could it have stopped the attack? Sure. But are code sandboxes really going to be inspecting all the code that's running in them? Probably not. >> Again, another note. >> Cloud security, cloud monitoring. What if? What if Hugging Face had been monitoring all of their cloud logs? Maybe they would have seen something. Maybe they would have seen something in the 17,000 actions that took place. So maybe they would have seen the attack. But would they have been able to stop it? No. Because it would have been too slow and the attack would have already finished. Lastly, think about let's think about the runtime. And there's two kind of critical parts of the runtime. First is the egress or the the sandbox that uh the model escaped out of. I think that's been well publicized. The other is a perimeter control on the hugging face

**[5:55](https://www.youtube.com/watch?v=SWdcSCRYhds&t=355s)** side where the attack that ultimately succeeded was a simple injection attack. Could these have seen the attack? Absolutely. Could they have stopped the attack? Absolutely. What was the fail? The failure. The failure is that they weren't turned on properly or configured properly. So, uh, what have we talked about so far? We've talked about where the AI lives and we've talked about a good control point, the best control point for AI. >> So, with that said, what does a good control look like? What if we know the best control point would have been the runtime? What could we have done? What is a control we could have put in place that would have helped in this situation? First thing we would have needed in a control is some sign of some sort of

**[6:42](https://www.youtube.com/watch?v=SWdcSCRYhds&t=402s)** programmability, right? There are a lot of security tools today or a lot of detection techniques that rely on blackbox pre-trained machine learning classifiers which are really difficult to understand how they make decisions and really difficult to fine-tune, really expensive to fine-tune. The challenge with that is when you're dealing with runtime scenarios, security teams need consistency. They need determinism. They need logic that they can see, that they can understand, and that they can interpret and change. That's what the idea of programmability would mean in a control. Being able to define exactly what you want to happen, express it in any business logic, express any security logic that you like. Code is the best way. And have it execute at the point of control.

**[7:33](https://www.youtube.com/watch?v=SWdcSCRYhds&t=453s)** The next thing >> is a the control should be testable. A control that uh you just ask chat GPT for hey I want a firewall rule that will help me with an attack. You can ask chat GPT for that. You can ask cloud for that. But no one in their right mind would take that firewall rule and deploy it into production. And what's the reason? The reason is the risk of making a mistake is too high. You have to be able to take a security control and test it thoroughly. You have to be able to design design the control. You have to be able to come up with test cases, regression regression tests. You have to uh test it robustly before it goes to production. And then after production, you have to be able to monitor it on ongoing basis and look for false positives. Lastly,

**[8:23](https://www.youtube.com/watch?v=SWdcSCRYhds&t=503s)** you need a control that's adaptable. Thinking back to the the size and the scale of this attack, we're talking about 17,000 actions in 5 days. There is no chance that any security policy could have been constructed that would have successfully stopped a determined attacker. What actually matters is that any security policy needs to be able to adapt. Just as attackers adapt to how defenses are configured and change their tactics, defenders need to be able to adapt and change their defenses as well. So what are the key takeaways uh for all of you? So um at the last few days at this conference, I've been talking to a lot of people and not everyone here works in security like I do, but everyone I've talked to understands the importance of security

**[9:10](https://www.youtube.com/watch?v=SWdcSCRYhds&t=550s)** and AI. So here are the key takeaways. First, runtime is the ideal control point for AI safety and security. And second, effective security controls need to be three things. programmable, testable, and adaptable. Thank you very much for the time. Uh, if you have any questions, I'd love to tell you more and dive in. This uh QR code will take you to where you can learn more about my company. And this is my LinkedIn profile.
