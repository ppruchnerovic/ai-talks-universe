---
id: ILnTkeuxPPw
title: "Black Hat Europe 2025 | Token Injection: Crashing LLM Inference With Special Tokens"
slug: black-hat-europe-2025-token-injection-crashing-llm
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2026
speakers: []
channel: "Black Hat"
duration_min: 28
published_at: 2026-06-18T05:27:33Z
video_id: ILnTkeuxPPw
url: https://www.youtube.com/watch?v=ILnTkeuxPPw
youtube_url: https://www.youtube.com/watch?v=ILnTkeuxPPw
tags: []
topics: ["Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: true
---

# Black Hat Europe 2025 | Token Injection: Crashing LLM Inference With Special Tokens

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=ILnTkeuxPPw) · [Conference site](https://www.blackhat.com/)

## Description

As large language models (LLMs) are deployed at scale, their underlying inference frameworks (e.g., vLLM, SGLang, TensorRT-LLM) have become critical operational pillars. These systems must splice user prompts with control structures, tokenise them, and schedule requests within milliseconds. Within this high-speed pipeline, we identify an underappreciated attack surface: special tokens.

We introduce the first "Token Injection" attack model, showing how a single prompt composed solely of special tokens can trigger uncaught exceptions in embedding and CUDA computation stages, resulting in denial of service (DoS) or full-service crashes. It can also cause inference manipulation, such as chat interruption and context pollution. The attack requires no authentication and works via standard input interfaces, affecting both self-hosted and managed deployments. We validate impact across multiple inference frameworks, including vLLM, SGLang, TensorRT-LLM, MLX, Ollama, and Hugging Face TGI; and across major platforms, including NVIDIA NIM, Google Vertex AI, Azure AI Foundry, Hugging Face, Meta AI, and OpenRouter.

This work shifts the AI security focus from "model output" to the security of inference infrastructure, offering practitioners a new perspective and a concrete defence paradigm.

By:
Pengyu Ding  |  PhD Student, Infra Security, Ant Group & Huazhong University of Science and Technology
Ziteng Xu  |  Senior Cybersecurity Expert, Infra Security, Ant Group
Zhiniang Peng  |  Associate Professor, Huazhong University of Science and Technology
Dongliang Mu  |  Associate Professor, Huazhong University of Science and Technology

## Transcript

*2,997 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=2s)** Hello everyone. Welcome to Black Hat Europe. It's a great honor to be here. This is my first time speaking at Black Hat. So, I'm very excited. Today, we are going to talk about token injection. Our topic is crashing LLM inference with star token. First, let me introduce our team. I'm Hongyu Ding, uh PhD student from Huazhong University of Science and Technology. I also play CTF with the team a level three helmet security. My co-speaker is Zitong Xu, uh senior security engineer from Ant

**[0:51](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=51s)** Group. Unfortunately, he cannot make it due to travel issue. So, I will be presenting our work on his behalf. We also have two amazing contributors, Professor Junliang Pang and Professor Dongliang Mu. They give us a lot of help and guidance on this research. Here is our agenda for today. First, the introduction. We will cover the background and the basics of LLM inference. Second, token injection. We will define what it is and how it works. Third, case study.

**[1:39](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=99s)** We will show you real-world crash in vLLM, TensorRT-LLM, and Ollama. Finally, the impact. We will discuss why it matter and how to fix it. Let's start with the introduction. Take a look at our title on the screen. It looks like a normal English sentence. But actually, what you see not everything. There are invisible characters hiding inside the text. Okay, let's make them visible. Now you can see tags like I am start tag, return tag, and I am end tag. First, this is token injection,

**[2:29](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=149s)** our attack method. Second, this is LM inference framework, our target like VLM. Third, they are the special tokens. We will explain exactly how these invisible tokens interact with the system. Why so loyal so important? Because LM inference infrastructure is one of the most important part in AI era. It's the standard acceleration engine for the industry. It's only bridge between user text and GPU hardware. Most importantly, it use multi-tenant architecture.

**[3:18](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=198s)** This is a fancy word for shared loyalty. One single instance serves hundreds of users at same time. If one user crash it, everyone goes down. It's huge risk, but nobody is watching. Usually, AI security research focus on jailbreak or prompt injection to trick the AI model itself. Uh as you can see, everyone goes left to attack prompt, but today, we are turning right. We targeted the infrastructure. And we don't want to trick the AI. We want to drift car off the road. Now, let's look at the ecosystem. This is current open source LLM

**[4:08](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=248s)** landscape. Uh as you can see, there are so many tools and the framework out there. We focus on this red box. The serving engines. You will see familiar names here. vLLM, TensorRT, Ollama. If you're building a app Now, let's start with core concept, token injection. But before we attack this we must understand how it works. Okay, let's look at the life of single request. From left to right. Stage one and two. The user sends a request like "Tell me a joke."

**[4:58](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=298s)** The system receives it and wraps it in a template. Stage three, tokenization. This is most critical steps for our talk. The tokenizer converts your human text into a list of numbers, token ideas. Stage four, batching. Then the scheduler takes over. It It packed multiple requests together. Like playing Tetris. To send them to GPU. Stage five and six. The GPU calculate the next token. And decoder turns that number back into text for you. Everything looks at fine there. Right? It's standard a pipeline.

**[5:48](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=348s)** So, where does token comes from? Let's go into hugging face, the most popular hub for AI models. We will use popular model as example Queen. We click enter the models main page. Then we go to files and versions tab to see source code. Here we find the most important file to be neither comfy convert point json. Think of this file as a rule book. It define every single token the model can understand. Let's look inside the file. On the left, you can see a list of special token. Look like look like this example I am

**[6:37](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=397s)** start, video pad, vision start. There's not words. They are control command. It tells model to start sentence. Process a video or handle image. We analyze these special token and found they fall into four main categories. Boundary like end of text. It simply It simply tells the model when to stop. Context feeling. These act as placeholder. They mark a blank space like mask waiting for the model to fill in. Structure. These define a role like user versus system. Multi model. They are place hold for

**[7:27](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=447s)** image and visions. As you can see, every major company Open AI, Meta, Google rely on this logic. We scan the distribution of this token. Please look at the top chart. The thinking and the child role markers, they just small number, but look at the big orange bar at the bottom. They are multimodal tokens. They are over 1,300 of them. Compared to simple text markers, multimodal tokens are the vast majority. We also count the specific token by vendors. Please look at that color. The red bar on the left are green.

**[8:16](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=496s)** The teal bars are DeepSeek. The green bar are Metalama. And and look at the huge yellow bar uh on the right, that's the Kimiko. Uh some of these models define hundreds or even thousands of spec token. Why does it matter? Because more spec token means larger tax surface. So, what is token injection? Look at this cartoon on the right. In an ideal world, user text and the control token are separated. The machines are happy. But, in reality they are mixed together. Token injection happens when an attacker put these control token into the input. We trick the infer inference engine into

**[9:08](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=548s)** executing command instead of just in reading text. It confuse the internal state and boom. The engine is crashed. Let's start with our first case. Vera. As many of you know, this is one of the most popular inference engine in the world. Here is our attack payload. We are targeting the green vision language model. Normally, you need to upload an image file to use this model. But here, look at content, it's text only. We manually injected the special token video start and video pad.

**[9:58](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=598s)** We sent just one single HTTP request and engine crashed immediately. On the server side, this is what we see. 500 internal server error. If you look closely at the log, the error is index error. List index out of the range. Uh basically, the server is trying to read data that doesn't exist. The server is confused. It seems video token, so I believe there is a video. But we didn't upload one. It's like ordering a burger, paying for it, but open the box and finding

**[10:47](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=647s)** nothing. Wow, it's so easy. Let's trace data flow to see why it crashed. Please look at the diagram from left to right. First, the attack. We send the malicious text. The API and chat layers do not validate. Then just pass it through. Second, the tokenizer. This is a key moment. Tokenizer turned our text video pad into the number ID 151656. From now on, the system trusts this ID. Finally, the is crash. The engine sees ID 151656 and thinking, "Okay, this is the video."

**[11:39](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=699s)** The code try to get the video size from list. But, because we never upload a file, and that list is empty. The code touch the empty list and the index error. The workers died. Here is the cause in Python code. Look at the variable video nums. The system counts the token to decide how many videos there are. So, videos nums becomes one. Then, it enters the loop. It try to access metadata list at index zero. But, remember, no file was uploaded. So, the list is empty.

**[12:26](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=746s)** Accessing the index zero of an empty list causes crash. So, strictly speaking, VOM is down with just a few text token. We killed the service. But, this is make us wonder, if most popular engine is vulnerable, is other infrastructure vulnerable, too? Let's find out. Next, let's look at our second target, TensorRT This is NVIDIA's own high-performance engine. It's widely used in service production environment. This is This tag is different. It's a

**[13:15](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=795s)** little complex. We call it two-step attack. Step one. We send the malicious text payload contain image path. Result, surprisingly, the server does not crash immediately. It stays alive, but internally, its memory is corrupted. It's likely we planted a landmine. Step two, we we send a second request. It can be anything, uh such as hi, hello anything. It can uh as soon as the second request hits, the GPU worker explodes. Let's investigate here in the log. After the first request, we see the C++ error.

**[14:03](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=843s)** Assertion failed, chunking is only possible during the context phase. This proves that, although the process still running, the internal state is already broken. Then, after the second request, we get a fatal error. Look at the red text. CUDA error, device side assert triggered. This is a very scary error. It means the crash happened deep inside the GPU hardware, not just in Python code. The GPU itself said, "I cannot handle this data." and it kills process. How did we achieve this? It's a chain reaction across three

**[14:53](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=893s)** layers. Please follow the dotted arrows. Layer one, Python. We inject the token, the Python logic calculate garbage dimension for non-exist image. Layer two, C++. This garbage data cross boundary into C++. It cause memory corruption. It corrupted the state machine. We didn't dig uh dig deeper to exploit, but the memory is clearly broken. Layer three, CUDA. Finally, the system tried to launch a GPU kernel with these invalid numbers. The GPU hardware catch the main catch the mass error and triggers crash.

**[15:43](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=943s)** Let's verify this in code. First, in Python code, the code search for vision start in the size. Because we injected the token, it thinks there is a image. It calculate the highs and the whites. But since there is no real image, these value become garbage and they are passed the C++ engine. Second, the C++ side. The function move to next contact trunk. It's bad the system to be in a specific state. But our injected token messed up the sequence. The assertion failed because the scheduler is lost. It does it doesn't know which phase

**[16:33](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=993s)** of generation is it is in. Third, the crash. This is a GEMM function, matrix multiplication. It takes dimensions M and K. Because of our injection, these numbers are wrong. When we force the GPU to multiply matrix with invalid shapes, it trigger a device side error. This is an unrecoverable error. The service must restart. Now, let me watch video. We send the first request and the server returns 200 okay. It seems fine. Now, and we send a second request to

**[17:23](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1043s)** simulate multi-tenant environment. And we send another request without payload. Finally bombed. And if we send another request, connection refused. Let's talk about Ollama. This is most popular tool uh popular tool for running LLMs, as well. For Ollama, we test Gemma 3 uh sorry, Gemma 3 models with payload use a different token, image soft token.

**[18:10](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1090s)** But, the logic is same. We send text only. We send a single request. We get an immediate crash. But, look at the log. This is different for uh from VRAM. We don't see a nice Python error message. We see this. This is a register dump. It means the program died violently. The operating system had to step in and kill it. If we look closer at the tree stack, we see the cause, segmentation fault. The program tried to access memory address that did not belong to it. This is a hard crash. Why does it happen?

**[19:00](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1140s)** It's a failure of communication between two language, Go, Glang, and C. Please follow the uh follow follow the flow in in diagram. Layer one, we send a special token. The go code believes there is a image, but the image image list is empty. Layer two, the model calculates the dimensions because the input is empty. They calculate negative or random dimensions. Layer three, there this is a critical moment. Go past these bad number to C engine. Layer four, the C engine blindly trusts the numbers. It tried to read memory as negative

**[19:49](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1189s)** offset. This triggers the segmentation fault and the service died. Now, let's talk about the impact. First, what is the cause? It's a in-bind signaling problem. We are mixing two things into in the same streams, control signals and user data. This is exactly like SQL injection, but for LLMs. It the same has a blurry boundary. It blindly trusts the tokenizer. Once the tokenizer create a special token, the model thinks, "Oh, this is a system

**[20:37](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1237s)** command." It's executed even though it came from malicious user. The immediately impact the in-memory corruption or system crash. But theoretically it opens the door for much worse attack, like stealing data or manipulating output, the model's inference logic. This issue is universal. It affects the core of the LLM ecosystem. We tested popular open source framework. Please look at icon. The explosion symbol means the entire engine crashed. The whole service went down. The red X means the request failed

**[21:28](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1288s)** causing a denial of service for that user. As you can see, widely used framework like vLLM, S3 large, and the NVIDIA TensorRT LLM all suffer from full engine crashed. But, it's not just open source code. It breaks real-world cloud platform, too. So, this meme sums it up perfectly. The dashboard might say stable, but the GPU workers are actually on fire. Why is this dangerous? Because of the multi-tenant architecture. One stacker sending a bad token can crash service for everyone else. It's not just open source code. It

**[22:19](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1339s)** breaks real-world cloud platform, too. First, look at Silicon Flow and Med AI. We simply put the special token in the chat box. And the service maybe breaks immediately. Next is NVIDIA name. We send a request. The result of 500 internal server server error. The inference workers crashed instantly. This even happens to top-tier provider like Google Vertex AI. When we send a payload, we get a failed to submit prompt error. This maybe improves we triggered the unhandled error inside Google's backend. We also test Open Router.

**[23:07](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1387s)** After sending a malicious token, the interface say no response generated. Here is a hugging face. We try to describe the image. We injected injected the token and the immediate error. Finally, this is Microsoft Azure AI Foundry. By injecting token, we can confuse to see some output like manipulate and causing failures. Let's see it in action. Here is a quick demo on Azure. First, we send end of text 10 tag. The model response is correct. The second time we send a message. It output an other.

**[24:03](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1443s)** Incomprehensible content. We have seen the crash. The demo is over. You might think this is end of story. But we want to go deeper. We didn't want to stop just crash. Crash are bad, but cross-user tag are dangerous. So, we design a specialized black box fuzzer. Our goal was to find two things, data leaks or and inference manipulation. For example, can I use special token to leak another user conversation? Or can I mess with their model logic? This are the fuzzer architecture.

**[24:53](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1493s)** It simulate real world cloud environment with three process. Process one, a baseline user. Process two, a benign user acting normal. Process three, attacker sending malicious token. We monitor the traffic if the benign user suddenly receive data from the attacker. We know we have cross-user bug. The result uh we failed with the fatter. We didn't find any low-hanging hanging fruit for data exfiltration or influence manipulation. Mhm, however, remember this is only black box text. The limitation is in our research deeps, not in the tax surface. We believe this risk is still there. It

**[25:41](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1541s)** just need more deep white box research to trigger it. Now, the most important part, how do we fix this? Does nobody care? No. Actually, the solution already exist. The hugging face tokenizer library has a native defense. It's a parameter called split special tokens. If you set it true, the tokenizer will break the malicious tokens apart. So, I'm start become the plain text, not a control command. It completely neutralized the attack. It sound like perfectly fixed, right? But, look at the number. How many open source models use this

**[26:30](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1590s)** protection by default? Approximately 0%. Why? Because the default setting is false, and the problem is a compatibility. If you simply turn it to true, many inference engine will fail to start. So, we are stuck stuck with default insecurity. We reported this issue to the major vendors. The response were mixed. Real M, Nvidia, Microsoft, and Google confirmed this issue and fixed it. Meta acknowledged it, but called it self-DoS, meaning you know you are only crash your own session.

**[27:17](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1637s)** MLX starts and not a vulnerability. And for SD long or llama, we are still waiting for a response. Finally, here are the three takeaways from our talk. New tech service, we are moving beyond the prompt injection to token injection. Simplicity, it's scary how easy this is. One simple chat message can crash an entire server. But, it does not stop here. It's vulnerable, can lead to further exploitation like cross-user attack, data leak, or even manipulating the model's inference. Defense, we need to sanitize the special

**[28:05](https://www.youtube.com/watch?v=ILnTkeuxPPw&t=1685s)** tokens. We cannot blindly trust the tokenizer anymore. That concludes our presentation. We are now open for questions. >> [applause]
