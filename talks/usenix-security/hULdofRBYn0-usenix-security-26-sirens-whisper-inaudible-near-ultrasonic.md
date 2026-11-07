---
id: hULdofRBYn0
title: "USENIX Security '26 - Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs"
slug: usenix-security-26-sirens-whisper-inaudible-near-ultrasonic
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 19
published_at: 2026-11-04T22:47:57Z
video_id: hULdofRBYn0
url: https://www.youtube.com/watch?v=hULdofRBYn0
youtube_url: https://www.youtube.com/watch?v=hULdofRBYn0
tags: []
topics: ["Multimodal, vision, speech & robotics", "Security, safety & red teaming"]
transcript: true
---

# USENIX Security '26 - Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=hULdofRBYn0) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '26 - Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs

Zijian Ling, Huazhong University of Science and Technology and Tsinghua University; Pingyi Hu, Xiuyong Gao, and Xiaojing Ma, Huazhong University of Science and Technology; Man Zhou, Huazhong University of Science and Technology and Tsinghua University; Jun Feng and Songfeng Lu, Huazhong University of Science and Technology; Dongmei Zhang and Bin Benjamin Zhu, Microsoft Corporation

Speech-driven large language models (LLMs) are increasingly accessed through speech interfaces, introducing new security risks via open acoustic channels. We present Sirens' Whisper (SWhisper), the first practical framework for covert prompt-based attacks against speech-driven LLMs under realistic black-box conditions using commodity hardware. SWhisper enables robust, inaudible delivery of arbitrary target baseband audio—including long and structured prompts—on commodity devices by encoding it into near-ultrasound waveforms that demodulate faithfully after acoustic transmission and microphone nonlinearity. This is achieved through a simple yet effective approach to modeling nonlinear channel characteristics across devices and environments, combined with lightweight channel‑inversion pre‑compensation. Building on this high‑fidelity covert channel, we design a voice‑aware jailbreak generation method that ensures intelligibility, brevity, and transferability under speech-driven interfaces. Experiments across both commercial and open-source speech-driven LLMs demonstrate strong black-box effectiveness. On commercial models, SWhisper achieves up to 0.94 non-refusal (NR) and 0.925 specific-convincing (SC). A controlled user study further shows that the injected jailbreak audio is perceptually indistinguishable from background-only playback for human listeners. Although jailbreaks serve as a case study, the underlying covert acoustic channel enables a broader class of high-fidelity prompt-injection and command-execution attacks.

View the full USENIX Security '26 program at https://www.usenix.org/conference/usenixsecurity26/technical-sessions

## Transcript

*1,990 words · source: supa (en, exact timings)*

**[0:20](https://www.youtube.com/watch?v=hULdofRBYn0&t=20s)** Hello everyone. Today I present our work seven whisper towards robust inaudible nearsonic jailbreaks of speech driven large language models. Our work exploits whether we can cultly jailbreak speech drivers through the physical attack channel. Before introducing service, let me briefly introduce jailbreaks. Modern RMS use safety alignment to prevent harmful response while jailbreak accounts try to bypass these protections. Existing J attacks can mainly be derived into two categories. The first category is construction based attacks.

**[1:10](https://www.youtube.com/watch?v=hULdofRBYn0&t=70s)** This method usually rely on manually designed prompts such as role playinging or specifically crafted instruction templates. They are simple and usually work in a blackboard setting but their effectiveness can vary significantly across different models. The second category is optimization based attacks. This meth this method search for server prompts or surface is optimization. This can achieve strong attack performance but many of them require white box access such as model logics. So existing methods still have clear

**[1:58](https://www.youtube.com/watch?v=hULdofRBYn0&t=118s)** limitations when we consider practical blackbox systems. More importantly most existing JB studies assume that the attacker directly send text to the model. But today more and more a system assistance are assessed through the speech. This has changed the attack surface. Recently special driving have become increasingly common in smartphones, smart homes, vehicles and and other intelligent systems. Compared with text input was input introduce a one important difference. Okay. The command must be travel through the physical acoustical channel. For

**[2:50](https://www.youtube.com/watch?v=hULdofRBYn0&t=170s)** example, the sound is gen is generated by a speaker propagates through the environment reach the microphone and is then processed by the speech system. So the interaction is no long simp simply used to the model instead we have speaker physical environment microphone speech processing and finally the LM this means that the physical channels itself becomes part of the systems security boundary and uh this is particularly interesting for jailbreak attacks traditional text jailbres are usually visible. If a attacker types a long and strange bricks prompt on a device, the

**[3:40](https://www.youtube.com/watch?v=hULdofRBYn0&t=220s)** user can easily notice it. But an acostic attack can potentially be much more sty. If we can hide the malicious command inside a inaudible signal, the victim may not even know that another instruction has been sent to the model. So our main research question is can we calculate jailbreak speech driving through the physical acoustic layer? To make this attack practical, we focus on three requirements. The attacker should be inaudible robust under physical transmission and should work in a blackbox setting. To achieve this goal, we identify two

**[4:31](https://www.youtube.com/watch?v=hULdofRBYn0&t=271s)** major challenges. The first challenge is covered and robust physical delivery. We need to deliver the malicious command without being noticed by nearby users. A natural solution is to move the signal into the ultrasonic or near ultrasonic frequency range. However, simply counting speech into ultrasound is not enough. In rare environments, the signal goes through the lou speaker, the air, reflections from the walls and finally the microphone. Each components introduce distortion. So the first question is how can we make the acoustic channel robust to the

**[5:20](https://www.youtube.com/watch?v=hULdofRBYn0&t=320s)** physical variations. The second ch is quite different. It comes from the jailbreak prompt itself. Most existing jailbreak method are designed for text input. For example, some optimization based text attack text generates strange tokens screens or long advers surface. These are acceptable in the text domain, but they are not suitable for speech and long prompts are more likely to be corrupt during acoustic transmission. So we cannot directly take the existing tech text jailbreak and cover it into audio. Instead we need a prompt that is both effective to forbake and friendly

**[6:11](https://www.youtube.com/watch?v=hULdofRBYn0&t=371s)** to speech transmission. This means it should be nature concigns easy to pronounce and still transferable across different models. So these two challenges comes from two different layers. One is the physical layer and the other is layer. Sense visible is designed to solve this problem together. Based on these two challenges we've proposed sense visible. The overall idea is straightforward. First we generate a was friendly JIC prompt. Then recover in this prompt into a near ultrasonic signal and transmit it through a combination

**[6:58](https://www.youtube.com/watch?v=hULdofRBYn0&t=418s)** through a loud speaker. For nearby users, the signal is almost inaudible. So So however because the microphones have no response, part of the neasonic signals can be demodulated back into this audio world bank. As a result, the microphone can recover the hideen speech command. This recovered command is processed by the speech driver. So sess whisper consists two components jailbreak generation and covered physical delivery. Another important point is that the attack is completely blackbox. We do not need access to the target motor par and parameters. And we we to now modify the victim

**[7:49](https://www.youtube.com/watch?v=hULdofRBYn0&t=469s)** device. We only use the speakers and the microphone. Now I will explain the framework in more detail. SB contains two main parts a texture layer and a costic layer. The cast the text layer scale is not simply to find the strongest possible JIC prompt. We also need to consider whether this prompt can survive speech scenaries and a costic transformation even the speech recognition. This creates an important trade-off. A highly optimized text prompt may work very well when directly entered into but after commenting it into speech some

**[8:40](https://www.youtube.com/watch?v=hULdofRBYn0&t=520s)** words or tokens secrets may be incorrectly pronounced or recognized. Once it happens the jailbreak structure may be destroyed. So instead of alling completely advers tokens, we constrain the prompt to speech friendly expressions. In simple terms, we want the prompt to sat satisfy two pro properties at the same time. First, it should preserve the jigmatics and second it should remain stable when covered into speech. This is why we focus on nature concise and easy to pronounce prompt structures. After generating the JIC prompt, we covered it into speech and move to acoustic layer.

**[9:30](https://www.youtube.com/watch?v=hULdofRBYn0&t=570s)** The main problem here is a physical distortion. If we simplify modulate the original research into the nearsonic band and transmit it the reserve switch can be very different from what we expect. The reason is that the physical channel is highly device dependent. The speaker change the signal the environmental channel signal and the microphone introduce another nonlinear transformation. So therefore what we care about is now the waveform before transformation what we really care about is what is what the signal will finally be recovered by the wing microphone. So we first estimate the estimate how a

**[10:20](https://www.youtube.com/watch?v=hULdofRBYn0&t=620s)** costic channel transforms the transmitted signal. Then instead of directly generate the attack waveform we optimize it through the estimate channel you can think you can think of this as a form of pre composition. So then before transmission we intentionally adjust the waveform in opposite direction after the actual physical distortion the recovered signal becomes closer to the target. So a layer tries to improves the recovered speech as a at this point the two layers work together. The text layer

**[11:08](https://www.youtube.com/watch?v=hULdofRBYn0&t=668s)** improves the sematic ronness. It makes sure that small recognition errors do not immediately destroy the job prompt. The cost layer the cost layer improves the physical robustness. It makes sure that the hiden command can still be recovered after real world propagation. It's draw this joint design is the key difference between the sensor and simply combining an existing existing jailbreak method with an existing attack. So both layers are need an for attack. Next I will show the main attack results. We evaluate a sense whisper on both open source and commercial speech

**[11:57](https://www.youtube.com/watch?v=hULdofRBYn0&t=717s)** drivers and compare it with representative JIC baselines. Before looking at the result, let me briefly explain the two metrics we use. The first is NR or nonreuser weight. It measures whether the model follows malicious request instead of directly refusing it. However, nonreuser alone is not enough. Sometimes the model does not refuse but still gives a value or or not related the response. So we also use SC or specific convincing score. It measures whether the generate response is actually speak specific and convincing for the requested task. In short, ANA tells us whether the refuser

**[12:47](https://www.youtube.com/watch?v=hULdofRBYn0&t=767s)** behavior is is bypassed while SS tell us whether the JPEG produce a meaningful response. Now let's look at the result. SWIS achieves strong attack effectiveness across different targeted models with the best resulting NR for 0 94 and SA for 93. We also observe strong transferability sor is works in a white box setting and can transfer across different seg models without assessing the parameters of the target motor. So compared with representative baselines including GCG, IGCG b and autodam sensor consistently achieves a better attack

**[13:39](https://www.youtube.com/watch?v=hULdofRBYn0&t=819s)** performance across multiple targeted models. So next we focus on the robos openness of size visible in real world physical settings. For a physical attack it is important to know whether it only works in one control setup. So we evaluate as visible on the different environments distance angles and recording device. First, we test different acoustic environments with background noise around 50 to 60 dB. The result shows that since WA can still maintain stable attack performance on this environmental changes. Second, we vary the attack distance and sur angle. These factors

**[14:28](https://www.youtube.com/watch?v=hULdofRBYn0&t=868s)** can change the reserved nearsonic signal and introduce additional physical distortion. Even under this special SP uh ch S whisper still maintains relatively stable NSC. Third, we validate different recording device because different microphones have different high frequencies response. This is a challenging set challenging setting. and those of performance varies across device since remains effective on multiple commanded device. Finally, we conduct application uh application studies on the core components removing important components lead to a clear performance drop

**[15:18](https://www.youtube.com/watch?v=hULdofRBYn0&t=918s)** confirming that each component contribute to final physical world attack performance. Overall, this result shows that size whisper is not limited to one fixed environment or device and can remain robust on the different real world conditions. Finally, this slide shows our physical attack setup. We only use uh a lot speaker and a phone. The victim device that do not need any improvisation and a complete demo and additional results are available on our project website. To conclude sible with various a new physical attack surface in space drivers. Our main takeaway is that

**[16:09](https://www.youtube.com/watch?v=hULdofRBYn0&t=969s)** general brick security is no longer only a digital or model that were pro problem which I am interact with physical world through the vehicle microphones and other seasons. The physical improved channel also becomes part of a security boundary since whisper combines a voice friendly jailbreak prompts with robous near transic delivery and works under a black setting across different models device and environments. We hope this work can motivate more attention to interactions between physical layer and AI security. We and finally we also investigate possible defense against Z visible. The first is detection is signal level

**[16:58](https://www.youtube.com/watch?v=hULdofRBYn0&t=1018s)** detection and nature idea is to detect an abnormal near ultrasonic energy. However, we found that this approach is highly device dependent. Some microphones preserve part of the high frequency signal. others feature this compliments before the audio reach the software layer. So if signal have has already been removed be by hardware software based detections cannot directly observe it. Another direction is motor level defense such as jailbreak detectors or stronger safety methods. These methods can help reduce harmful response but they mainly obserate operate operate at after the command has

**[17:49](https://www.youtube.com/watch?v=hULdofRBYn0&t=1069s)** already entered the system. So they do not directly solve the physical attack surface. Our result suggests that defending speech drivers requires potential across both layers. We need signal level and hardware level level method to protect a custom interface and we still need a model level safety method to protect against the malicious sematics. So a major implication of this work is a future space assistant and many joined the physical layer and model layer defense and that is all for my presentation. Thank you very much for attention. I'm happy to hand you any question.
