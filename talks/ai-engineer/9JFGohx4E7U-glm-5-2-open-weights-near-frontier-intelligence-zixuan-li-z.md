---
id: 9JFGohx4E7U
title: "GLM-5.2: Open Weights, Near-Frontier Intelligence — Zixuan Li, Z.ai"
slug: glm-5-2-open-weights-near-frontier-intelligence-zixuan-li-z
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Zixuan Li"]
channel: "AI Engineer"
duration_min: 14
published_at: 2026-09-27T17:00:01Z
video_id: 9JFGohx4E7U
url: https://www.youtube.com/watch?v=9JFGohx4E7U
youtube_url: https://www.youtube.com/watch?v=9JFGohx4E7U
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "GLM-5.2", "GLM", "Z.ai", "Zhipu AI", "Zixuan Li", "open weights", "open source AI", "open models", "frontier models", "coding models", "agentic AI", "Z Code", "fine-tuning", "Hugging Face", "AI Engineer", "AI Engineer World's Fair"]
topics: ["Training, fine-tuning & model building"]
transcript: true
---

# GLM-5.2: Open Weights, Near-Frontier Intelligence — Zixuan Li, Z.ai

**Zixuan Li**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#GLM-5.2` `#GLM` `#Z.ai` `#Zhipu AI` `#Zixuan Li` `#open weights` `#open source AI` `#open models` `#frontier models` `#coding models` `#agentic AI` `#Z Code` `#fine-tuning` `#Hugging Face` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=9JFGohx4E7U) · [Conference site](https://www.ai.engineer/)

## Description

Zixuan Li, head of Z.ai, introduces GLM-5.2 to the world. On the hardest long-horizon coding and agentic benchmarks, it lands between Claude Opus 4.7 and 4.8. Even its non-thinking mode beats GLM-5.1 with thinking turned on, and it leads other open-weight models on the Artificial Analysis Intelligence Index.

Li also explains where the GLM name comes from (a 2021 paper that put Z.ai among the earliest LLM labs), and why GLM is more than a coding model. The core of his talk is why Z.ai releases near-frontier models as open weights. It lets enterprises and governments run models on their own servers, lets companies fine-tune for law, finance and security, and lets customers co-design where the models go next. He closes with one more thing: Z Code, Z.ai's own coding harness built for GLM-5.2 that also works with other frontier models.

Related links:
Z.ai: https://z.ai

Timestamps:
0:00 Intro from swyx
0:47 Z.ai and GLM
2:05 Where the GLM name comes from
3:10 Intelligence beyond IQ
4:25 GLM-5.2 benchmarks vs. frontier models
5:20 A new high thinking level
5:55 More than a coding model
6:55 Why open weights
8:00 Fine-tuning for law, finance and security
8:45 Co-designing the future
9:15 Thanks to the open-source community
10:00 Tech blog, API and coding plan
11:00 One more thing: Z Code
12:10 Wrap-up

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*1,986 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=9JFGohx4E7U&t=12s)** Without further ado, we're going to bring on Zishan for for his keynote if we're all set. Hey, how are you? >> Great I'm here. >> Yes, to the magic of the internet. It's really good to see you again. Zishan has you've been speaking with AI Singapore and obviously GLM is the talk of the town right now. There's been an amazing booth downstairs in the expo and I think a lot of people are just very excited to hear from you on what all is going on with ZIAI. So if you want to take it away. >> Yes, sorry again for not showing up in person, but I have a team whole team coming to the town and we have a booth. So you have any questions, feel free to reach out to me on X link and also you can look for my

**[1:02](https://www.youtube.com/watch?v=9JFGohx4E7U&t=62s)** team on our booth. And since I cannot see my slides, so I will need Swee to help me flip through all the slides for me. Yeah. >> You're good. >> Here Swee, like what which slides we are in right now? >> Yeah, so we're we're on the opening slide. We're talking about intelligence and ZIAI. >> Okay, so yeah, so you can you can see that it's the first time for us to introduce GLM 4.2 5.2 to the world and also we are going to share something about Z.AI and GLM because maybe people will think Z.AI and GLM they're irrelevant, right? You are your company is not G.AI or your model's called Z1 or Z2. And you can find my X and our company's

**[1:52](https://www.youtube.com/watch?v=9JFGohx4E7U&t=112s)** X account here, so you can just search for my name Zishan Lee and the Z A I org. And you can follow them for the follow-ups. So, yeah, we can go to the second slide. Yeah actually I cannot see the slide, so I'll try to >> So, we we >> Yeah, try to make sure that it is correct. So, the company actually is called Zhipu. Maybe some people have heard of it. And the all the models, it's it's called GLM. Actually, it's not a a brand name, it's a generic term. So, GLM actually represent general language model pre-training with auto-regressive blank filling. And that paper was published back in 2021. So,

**[2:42](https://www.youtube.com/watch?v=9JFGohx4E7U&t=162s)** actually we were the one of the first labs to do explorations on large language models at the same time with OpenAI, and Anthropic, and DeepMind. And even today, we we no longer use GLM as the architecture, we still use the name GLM as our brand name. So, we use GLM 5.1, 5.2, and it become like one of our like most prod uh proddest product and model. And the second thing that we look for is intelligence upper bound. So, in terms of intelligence, we we may feel that it's represent IQ, something something like that. And when Deep Seek launched one 01 launch, people are talking about the model's capability to solve math

**[3:30](https://www.youtube.com/watch?v=9JFGohx4E7U&t=210s)** problems, physics problems. But what actually intelligence mean is not just like IQ or AIME or other other physics problem. So, from GLM 4.5 to GLM 4.7, we are exploring like several things, like reasoning, coding, and agentic capabilities. So, as you can see from the slides, So, we add like Yeah, the last slide. Yeah, we were actually I haven't like finished that slide. Yeah so Okay. Yeah, need to go back to the two two slides. >> I don't have back I don't have a back button. Thank you.

**[4:17](https://www.youtube.com/watch?v=9JFGohx4E7U&t=257s)** I would you I don't understand clickers that don't have back buttons. Like why Okay, I you know, anyway, go ahead. >> Yeah, never mind. Yeah, because people want to see the GLM 5.2. They they don't want to see you like GLM 4.1 or 5. But like GLM 4.2 actually specialize in coding and genetic task as you can see from the graph because there are a lot of rumors whether your model is close to mythos, fable, but actually I want to share these slides to all of you. So, you can see it's somewhere between Opus 4.7 and 4.8 and we use the hardest problems like Deep Sweep, Terminal Bench 211, which was mentioned by the Open AI team uh several minutes ago. And all the like long horizon task and benchmark shows that the capabilities

**[5:07](https://www.youtube.com/watch?v=9JFGohx4E7U&t=307s)** are on par with at least Opus 4.7 and it it it shows a significant improvements over 1.1. Also, for GLM 1.2, we add a thinking uh level called high. So, because we also noticed as we move to the harder task it may consume more tokens and also we we care a lot about the token efficiency. So, it's the first time we add the high level for thinking budget. But even without thinking, the non-thinking model is better than the 5.1 thinking model. So, I think it's a huge improvement for the open weight model. That's what really impressed the world and why people are talking about GLM 5.2 lately. Okay, the next slide.

**[5:59](https://www.youtube.com/watch?v=9JFGohx4E7U&t=359s)** And one one thing that I want to mention is that GLM is more more than coding model because people use it inside clock code code X, open code. But actually, we have trained a lot of things outside coding. For example, we improve a lot in GDP valve and also math problems. We also care about math problems, frankly speaking. And also, we train a lot of thing uh related to role play, general chat. We want to improve every aspect of the model. So, you can see from the artificial analysis intelligence index actually leads the other open way model a lot and close to the frontier model. So, I want you if you are you haven't experienced GLM yet, you can use GLM to

**[6:49](https://www.youtube.com/watch?v=9JFGohx4E7U&t=409s)** do general chat, use it to process your daily workflow, not just for coding, but you can explore the model like beyond the coding scope. Next slide. And GLM 4.2 is a open weight model. So, people always ask me, "Why do you open weight? So, do you care about your business or like do you care about losing market to some infra suppliers?" But actually, we open the weights for several things because there are users' needs and there are our own needs. If we can meet their needs, I think it's okay. It's definitely okay for us to to open the model. For example, if our users want security and control and we want to build trust, we can open

**[7:38](https://www.youtube.com/watch?v=9JFGohx4E7U&t=458s)** weight model. For for some cases, if enterprise or government especially in the Western world, want to use the model, we open way, we upload to the hugging face so that they can use the model on premise. I think it's very beneficial for the whole ecosystem it to explore the model, especially when the capabilities is close to the frontier model. And second, if people want diversity. So, in terms of diversity, I mean the capabilities in legal, finance, security, they can fine-tune the model. So, we need to open the model to let them fine-tune. For example, Harvey is fine-tuning GLM 4.1, and maybe they're thinking about fine-tuning

**[8:26](https://www.youtube.com/watch?v=9JFGohx4E7U&t=506s)** GLM 5.2 afterwards. And I've I have like talked to a lot of other companies. They're also thinking about fine-tuning GLM as their like next step or next strategy to differentiate themselves from other application company. And third, if our customer or an individual want to co-design and predict the future, sometimes they need to see the architecture of the model. They need to see the recipe of how you train the model. So, we want to make the norm. We want to make my bets. So, we want to co-shape the future with our customers with the open source uh community. So, I think our needs and our ecosystem

**[9:16](https://www.youtube.com/watch?v=9JFGohx4E7U&t=556s)** really like fits into each other. And GLM 5.2 couldn't succeed without you, all the open source community players like Onflos and Media and and some like individuals, super developers, they are part of it. And thanks a lot to application builders like Peter. Right? Because open source doesn't just include open source model, but also open source softwares and open source other sorts of support. So, all your support and what are you you're doing right now pushes to to make better models. I think uh you you are the true hero. And the last, I want to share a a great

**[10:06](https://www.youtube.com/watch?v=9JFGohx4E7U&t=606s)** resource for you to go through. Geo 5.2 is our tech blog. So, actually in that tech blog, we share several things like our hugging face repo, how how you can try the Geo and 5.2. You can try the inside the chatbot agent, and also you can call the API. And also we have a coding plan like the Codex or cloud core subscription for you to use your tokens as individuals. And also we share something about our training pipeline training recipe, which you can understand why it's a good model. So, there are a lot of things behind the behind the model, not just um a a model that had great data. We also have fantastic technologies behind

**[10:54](https://www.youtube.com/watch?v=9JFGohx4E7U&t=654s)** the model, so you can export the model yourself. You can see what difficulties we have gone through. And the last slide, actually it's kind of a one more thing. So, it's the first time we share the code to the whole community. Woo! So, that one more thing is we actually have our own harness. The Z code, actually it's built for Geo 5.2, but also support all frontier models. You can bring your own key. You can connect to Z code. Actually, the I think the operation is is similar to Kodak. Actually, you you can try some techniques like go or other like compact technique

**[11:41](https://www.youtube.com/watch?v=9JFGohx4E7U&t=701s)** techniques like what you've done in in Kodak and car code. And this harness is I think it's the perfect one for GLM 102. If you haven't experienced it, you can just search Z code or you can go to our booth. We have our team members showing this harness to you. And welcome to to our booth. And welcome to like talk to me in the future. And next time I'll definitely be in SF talking to everyone. Yeah thanks. >> Thank you very much. Um So uh trust me, the very first World's Fair, I wasn't allowed to come back in the country for my own conference, so I know exactly this feeling. Uh but it it it's all

**[12:30](https://www.youtube.com/watch?v=9JFGohx4E7U&t=750s)** good. Uh the ZAI team, I really appreciate them uh making the effort. They really want to meet you. They're here to meet you. And this is the whole point of the World's Fair, to bring all the top world's AI uh companies and labs uh all in one place, so you can do business together, uh meet the people behind the models that you use, ask the questions that he cannot answer in public, but you can ask in private. Um I'm also very proud. Uh he showed uh Zhicheng showed that that list of uh Hugging Face uh you know, top uh contributors. I think we are four for eight uh in that list uh present at World's Fair. Uh we're working with Nvidia and Unsloth and Ollama and then uh all those other fine-tuners as well to uh to make our our sort of the inference and the local tracks uh that you're going to see over the next few days. Um with that, thank you so much to Zhicheng. Uh I'm going to invite on uh

**[13:20](https://www.youtube.com/watch?v=9JFGohx4E7U&t=800s)** the next uh couple folks. I think I I I think I might be doing Ali's job here, so uh we'll we'll talk to Hugging Face next and Minimax. Thank you.
