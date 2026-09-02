---
id: XWNfBM5VFcU
title: "Lightning Talk: Why Don't AI Technologies and CI/CD Pipelines Get Along? - Ryo Sugahara"
slug: lightning-talk-why-don-t-ai-technologies-and-ci-cd
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "Open Source Summit + ELC NA 2026"
year: 2026
speakers: ["Ryo Sugahara"]
channel: "The Linux Foundation"
duration_min: 15
published_at: 2026-06-03T18:23:14Z
video_id: XWNfBM5VFcU
url: https://www.youtube.com/watch?v=XWNfBM5VFcU
youtube_url: https://www.youtube.com/watch?v=XWNfBM5VFcU
tags: []
transcript: true
---

# Lightning Talk: Why Don't AI Technologies and CI/CD Pipelines Get Along? - Ryo Sugahara

**Ryo Sugahara**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit + ELC NA 2026` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=XWNfBM5VFcU) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Lightning Talk: Why Don't AI Technologies and CI/CD Pipelines Get Along? - Ryo Sugahara, NTT DATA GROUP Corporation

AI technologies are fundamentally transforming the landscape of IT system development. While they are increasingly applied across a wide range of development tasks, their potential remains largely untapped within CI/CD pipelines.

I have personally experimented with applying AI technologies to CI/CD pipelines in an effort to build more effective and intelligent workflows. However, these attempts did not lead to the expected results. This experience raises an important question: why is the integration of AI technologies into CI/CD pipelines so challenging?

In this session, I will explore the practical and conceptual barriers encountered when applying AI technologies to CI/CD pipelines, and examine the underlying reasons behind their apparent lack of compatibility, drawing on firsthand experience. This exploration is still a work in progress. Rather than presenting a success story, this session aims to frame the problem clearly and honestly.

Also, by raising key questions and sharing lessons learned from failed attempts, this session seeks to encourage broader discussion and invite more practitioners to engage with this challenge and collaboratively explore possible paths forward.

## Transcript

*1,225 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=0s)** Hello hello again everyone. >> [laughter] >> Thanks to the opportunity to speak today in this session. I'll share my journey exploring why AI technologies and the CCD pipelines serve to work well together. By the way, uh English is not my strongest skill, you know. So, please go easy on me. Ready to get started. Uh before I dive into that topic, my name is Rio Sugahara. I'm already from Tokyo.

**[0:46](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=46s)** Uh working at the NTT Data Group as a DevOps infrastructure engineer, a technical manager, and a platform modernization evangelist. Uh so, actually, uh I got the email from the foundation, and it was late of March. So, that in my e- hometown, so the cherry blossoms tourists just have just started to bloom. So, I decided to use cherry blossom uh photo background, you know. Let's move on. Uh first, what do you expect from AI in software development?

**[1:34](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=94s)** In general, uh we expect things to become faster, cheaper, and smarter. Uh expectations, however, vary depending on your role. If you are developers, uh you may expect a smarter automation. If you are managers, you may focus on productivity gains. If you are executives, you would do often care most about the cost to reduction. In my case,

**[2:21](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=141s)** I expected that the CI/CD pipeline could be much smarter uh with AI. Like a pipeline could suggest a solution to deliver faster at the same time as errors occurred in the pipeline. I think it's already uh uh reality on some IDEs such as VS Code. Uh but I haven't to really heard of such a feature being implemented in CI/CD pipelines. So, why doesn't AI fit naturally into CI/CD pipelines? The very place where automation should

**[3:11](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=191s)** shine. CI/CD pipelines are fundamentally deterministic systems. The same input to always produces the same output. If the output changes without any changes in input, the system is considered broken. To achieve this, CI/CD pipelines must satisfy three key requirements. First, reproducibility. Every task must produce consistent results. Second, IDM potency. Running the same task multiple

**[4:02](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=242s)** times with the same input should always yield the same outcome. Third, reliability. The pipeline must be dependable. After all, and no one wants to rely on an unreliable pipeline for critical assistance. Of course, me neither. I don't want to get yelled at by my boss if I make my boss getting angry. It's so terrible. On the other hand, what about the case of AI systems? I will mention it on the next slides.

**[4:54](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=294s)** AI systems, in contrast, are probabilistic. The same input doesn't always produce the same output. AI generates answers that are statistically likely to be valuable. In a CI/CD pipeline that run daily, this become a serious issue. Even if nothing changes in the source code, there is no guarantee the system will behave the same way tomorrow. This is a critical problem for operators and of course users. This is applying AI to CI/CD pipelines

**[5:46](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=346s)** is difficult even in a where it could potentially reduce costs. In contrast, in coding tasks, human intervention bridges the gap. Developers review, validate, and modify AI-generated code before using it. That's why AI works well there. It improves productivity without requiring full trust. Uh let me summarize. CI/CD pipelines require determinism, repeatability,

**[6:35](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=395s)** and verifiability, and stability. AI, on the other hand, is probabilistic, non-deterministic, hard to verify, and the continuously improving. CI/CD demands certainty. AI introduces uncertainty. This creates a fundamental tension between the two. In many high-impact cost-saving use cases, this uncertainty is acceptable because humans are involved. For example, code suggestion tools.

**[7:24](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=444s)** CI/CD pipelines, however, are designed to minimize or eliminate human intervention. That means AI can only be applied to limited use cases within CI/CD, such as generating notifications or recommendations. But do those use cases deliver significant cost reductions? The answer is no. Now, let me share my experience. I proposed to introducing AI into our CD pipelines.

**[8:12](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=492s)** I discussed the idea of using AI much more smartly with the team members and presented my approach to assets and managers. For example, automated solution suggestions and log analysis and the similar smart features. Technically, the ideas were interesting and should improve the developers' experience. We also estimated the potential cost savings. Despite this, only a few of those benefits could be quantified clearly.

**[9:02](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=542s)** As a result, the proposal was rejected. The expected to return didn't justify the cost of implementing AI. Honestly, that decision was reasonable. It was difficult to argue against it. Here is my conclusion this transfer. First, there's no doubt it was it for developers. I I agree there was a value for developers. However, um that value doesn't really translate into return on investment to at the

**[9:53](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=593s)** organizational level. Second, um not worth the return on investment. It might be a little extreme way of serving. If you accept it to at the first value, uh what do I want to say is that it's extremely difficult to explain that cost reduction when using traditional manual based cost estimation. Third, find the value uh beyond cost reduction that executives actually care about. If we want to want to executive buy-in, we need to go beyond the manual based

**[10:46](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=646s)** cost unfortunately. It should be quantitative quantitative benefits because we can already experience explain qualitative benefits using AI on the CI/CD pipelines. Ultimately, to justify the investment, we must translate this into clear explainable system-level quantitative benefit. Integrating AI into CI/CD pipelines is like walking a thorny path. In Japanese, we call it Ibarano Michi.

**[11:36](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=696s)** You know, it's valuable. But, every step comes with the challenges and pain. Still, it's pain. And it's a path was exploring. Thank you. >> [applause] >> Sorry? Uh well, my executive told me that you know, introducing AI system is a really high cost of elements such as and also GPUs or SASU elements like

**[12:26](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=746s)** critical or something like that. But, uh uh executive expects to reduce manpower developing costs. So, they rejected my idea. Is it the answer? Okay. Thank you. Okay. Uh you mean open source

**[13:15](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=795s)** uh module using for CI/CD. It's uh uh Sorry. >> Mhm. Yeah. Yeah, of course I agree with it's one thing but I I don't I know not to say why it's Japanese experience to culture. So we have to explain about that how reduce

**[14:05](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=845s)** manual cost. So but it's so difficult to explain. Is this answer? Okay. So could you I guess you're talking tomorrow to discuss further how you deal with the fundamental problem that real world most of AI is not deterministic. It's fundamentally probability and and CI we're used to thinking of it as absolutely deterministic. So will you discuss that tomorrow or is that a Yeah, I can also like just in a nutshell we basically do things like we have deterministic qualifications Mhm. that we pass by the AI and we only use AI to reduce the algorithm of AI and we have gaining and scoring on AI on the basis of

**[14:51](https://www.youtube.com/watch?v=XWNfBM5VFcU&t=891s)** and if it goes through So you you process what So your way of bridging the gap is strive to make AI deterministic at the places where it's important to be deterministic. Yeah, we have our own algorithm. Got it. Sorry. [laughter] Thank you. Thank you. Thank you. >> [applause]
