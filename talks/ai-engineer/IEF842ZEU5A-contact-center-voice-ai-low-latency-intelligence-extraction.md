---
id: IEF842ZEU5A
title: "Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams — Dippu Singh"
slug: contact-center-voice-ai-low-latency-intelligence-extraction
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Dippu Singh"]
channel: null
duration_min: 23
published_at: 2026-04-08T00:00:00Z
video_id: IEF842ZEU5A
url: https://www.youtube.com/watch?v=IEF842ZEU5A
youtube_url: https://www.youtube.com/watch?v=IEF842ZEU5A
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Enterprise adoption & strategy", "Multimodal, vision, speech & robotics", "Science, healthcare & applied ML"]
transcript: true
---

# Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams — Dippu Singh

**Dippu Singh**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=IEF842ZEU5A) · [Conference site](https://www.ai.engineer/)

## Description

"Processing real-time voice data is an engineering minefield of latency, accents, and interruptions. This session explores the architecture of a Real-Time Voice Intelligence Pipeline deployed in a high-volume contact center.
We will move beyond simple transcription to discuss Structured Intent Extraction. I will show you how to design:

1. Voice Capture Pipeline: The entry point for clean, multi-channel data acquisition.
2. Speech-To-Text(STT) Engine: Converting speech to accurate text.
3. Generative AI Core Structure: Using rigorous system prompts to force the LLM to separate ""Customer Intent"" from ""Operator Chit-Chat"" and output valid JSON, even from garbled transcripts.
4. Customer Data Sync: Translating AI insights into enterprise system actions.

We reduced post-call work by 50% by shifting compute from ""batch"" to ""stream.""

Speaker: Dippu Kumar Singh - Leader Of Emerging Technologies (Apps), Fujitsu North America Inc.

Dippu Kumar Singh has over 16 years of experience at the intersection of industry innovation and advanced research. He is a recognized authority in building scalable, trustworthy, and commercially viable AI systems. Being a Leader for Emerging Data & Analytics at Fujitsu North America, Dippu specializes in bridging the gap between theoretical AI concepts and enterprise-grade implementation. His strategic leadership has spearheaded multi-million in sales pipelines and delivered remarkable savings through AI-driven optimizations in transportation, manufacturing, utilities, and supply chain logistics.

Socials:

Slides:

## Transcript

*2,740 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=IEF842ZEU5A&t=0s)** Right, hello everyone. Welcome to the AI engineer 2026 online track. Um, good morning, good afternoon, good evening, depending upon your time zone. My name is Deepu Singh and I lead the initiatives in the emerging data technologies and AI architecture at Fujitsu North America. Um, and today I will be uh, giving you or maybe provide you a deep dive into a very specific but a very highly impactful engineering challenge, uh, which we have encountered in our uh, contact centers. So, with that, let me just quickly share my screen and get this going. Right so um

**[0:52](https://www.youtube.com/watch?v=IEF842ZEU5A&t=52s)** um, this is the topic of the discussion, VoiceOps-ifying low latency intelligence extraction from uh messy audio streams. Uh, when we talk about, you know, generative AI, we often, you know, focus on uh, clean text inputs, but if you go into the real world, specifically in the customer service or or maybe contact centers, specifically, um, the data does not start as a clean text, right? It starts as messy, quite overlapping, um, sometimes emotionally charged and and it it may have multi-channel audio streams also within that, right? And and today we will explore the technical architecture which is required to

**[1:41](https://www.youtube.com/watch?v=IEF842ZEU5A&t=101s)** capture that audio, process it with ultra-low latency and use the generative AI to extract structured, actionable, um, business intelligence out of it. Uh, so, with that, let's get started with this. So, here is our roadmap for the next 25 minutes. Um, first we will stage the, um, um, stage with what the current challenges are. Uh, we have to understand the operational realities and the intense human bottlenecks in in the modern contact centers to understand why this engineering matters. Uh, second, we will walk through the solution which is provided. I will break

**[2:29](https://www.youtube.com/watch?v=IEF842ZEU5A&t=149s)** down our high-level architecture into four key components, um, detailing how we move from raw audio to a structured JSON using advanced summarization workflows. Thirdly, we will look at the key outcomes, specifically like how these technical implementations they translate into hard ROI and operational impacts. And finally, we will discuss the, um, roadmap ahead. And being transparent about the current tech engineering constraints which we face now and then and where we are taking this technology and the roadmap ahead. So, to engineer a great solution, we first need to deeply understand the

**[3:18](https://www.youtube.com/watch?v=IEF842ZEU5A&t=198s)** problem. So, let's look at the current state of the contact center operations. So, contact centers, they are the frontlines of the customer experiences, but structurally, they are breaking under the pressure. If we look at the industry data, um, over 50% of the contact centers, they identify uh, hiring, training, and productivity as their most critical barriers. Why? Because the job is incredibly difficult. When we analyze the reasons why the operators they leave for the other professions, high stress is the number one factor as part of it. Now, operators are expected to handle

**[4:06](https://www.youtube.com/watch?v=IEF842ZEU5A&t=246s)** complex customer emotions, navigate the, um, multiple, uh, customer data platforms or the CRM systems involved into it, and and also document everything perfectly. So, if you think about this, this leads to a massive retention problem, right? Uh, we are caught in a negative spiral um, where understaffing leads to higher stress for the remaining operators, um, which leads to a high turnover and uh, that ultimately implies to more understaffing right? So, to break this cycle, we just uh, cannot hire more people. We have to fundamentally engineer the stress out of the workflow.

**[5:00](https://www.youtube.com/watch?v=IEF842ZEU5A&t=300s)** And the most glaring inefficiency in this workflow is something called, um, after-call workflow or ACW, uh, which we are going to discuss as part of this slide. Um, according to our baseline studies, the average contact center call it typically last about like 6.5 minutes. However, the average post-processing time where the operator types up the notes, summarizes the call, and selects the disposition codes, it it takes like almost 6.3 minutes. So, this is nearly like 1:1 ratio we are talking about. Um, and this also implies operators are spending almost as much time doing administrative data entry as they are

**[5:48](https://www.youtube.com/watch?v=IEF842ZEU5A&t=348s)** actually talking to the customers. Um, furthermore, because the summarization relies on an individual operator's memory and the writing skills, the data quality is highly inconsistent. Um, our core engineering mission here was clear, like use AI to target the after-call work which is ACW. Um, if we can mechanize the summarization and the data extraction, uh, theoretically, we can reduce the post-processing time, um, almost by 50% or even more. And and this shifts the enterprise, you know, focus from merely just handling the calls to actually, you know, analyzing the

**[6:35](https://www.youtube.com/watch?v=IEF842ZEU5A&t=395s)** voice of the customers for the business growth which we are looking out every now and then. So, how do we engineer that shift? Let's deep dive into the technical solution and the architecture we built to solve this. Um, So, we designed a four-stage low latency pipeline to transform the conversational audio into a structured business intelligence um, with minimal human intervention. And it starts with voice capture, which is tapping into the telephony system to extract raw, high-fidelity audio streams. And that flows into our speech-to-text

**[7:25](https://www.youtube.com/watch?v=IEF842ZEU5A&t=445s)** engine STT uh, which is responsible for high-accuracy transcription. Um, next is the brain of the system, the generative AI core. This is where we do the heavy lifting of the intent recognition and summarization. And finally, the customer data sync layer which translates those AI insights into API calls to update the, uh, uh, customer data or CRM data automatically. Uh, let's look at the engineering under the hood for each of these components in detail. So, the first component is the voice capture. In AI, um, the typical rule is garbage in equals garbage out. So, if your audio intake is

**[8:15](https://www.youtube.com/watch?v=IEF842ZEU5A&t=495s)** flawed, the LLM will hallucinate later on. Um, we do real-time uh, audio intake. So, applying noise filters to strip out the uh, back office chatter or, um, you know, anything of those sort which is creating an attenuation is important and normalize the audio level is very very very important for us. Crucially, if we perform these channel mapping, uh, we absolutely must spit split the, uh, stereo audio to isolate the agent on one channel, say, on the very left, and the customer on the other side, which is the very right, right? So, if if you mix them into a single mono track, um, like kind of overlapping with each other, the

**[9:02](https://www.youtube.com/watch?v=IEF842ZEU5A&t=542s)** AI will struggle to figure out who said what and and thereby, you know, ruining the entire downstream summary. So um it's important that we have that channel mapping intact and it separates which who is what and who is saying what, right? Um, finally, we apply a security layer because sometimes the audio streams can contain the credit card numbers or maybe passwords or any anything which is personally identifiable information, PII. So, we utilize buffer management and early-stage PII masking technique uh, so that the sensitive data it never hits the LLM memory banks whenever we are moving ahead in the channel.

**[9:53](https://www.youtube.com/watch?v=IEF842ZEU5A&t=593s)** Now, next, the audio it hits the, um speech-to-text engine for generative AI or the LLMs to summarize the um data effectively or your response effectively, we found that the speech-to-text, the STT um accuracy must be above 90%. Uh we utilize advanced acoustic modeling to map the um phonemes and filter out any regional dialects. We then apply the language logic utilizing like domain-specific dictionaries. Uh just for example, if it's an insurance agent, the um speech-to-text engine STT needs to know the difference between a term life

**[10:44](https://www.youtube.com/watch?v=IEF842ZEU5A&t=644s)** and a term right. Both of them are very close to each other, but still there should be a difference between them. Uh finally, post-processing is also vital. Uh we use inverse text normalization and auto punctuation. Uh for example, if if a customer says $5,000, the speech-to-text um engine, it should must output that into numerical fashion. And this numerical formatting, it it drastically improves the LLM's ability to extract the entities in later point in time. Now we reach the generative AI core. We are not just throwing a raw trask raw tras transcript at LLM, but we are also asking it to summarize it. Like we use a

**[11:33](https://www.youtube.com/watch?v=IEF842ZEU5A&t=693s)** highly orchestrated approach in this case. Um in our orchestration layer, we use specific prompt templates. Our um setup showed that if if you just ask an LLM to summarize a call, it outputs a messy narrative paragraph. So instead, we use few-shot libraries to instruct the LLM to output separate bullet points. Um one list for customer inquiry uh and a separate list for operator's action. Uh then comes the reasoning layer. In the reasoning layer, we extract the intent. We provide the LLM with a predefined list of customer uh call reasons like uh cancellation or new application or

**[12:24](https://www.youtube.com/watch?v=IEF842ZEU5A&t=744s)** any kind of claim status and instruct it to classify the transcript and output the reason why it chose that specific classification. And finally, the trust layer where we apply the token optimization to keep the um latency low and runs the uh automated hallucination checks to ensure the uh generated summary is strict um and it is grounded in the transcript. Now the final technical hurdle is getting this beautiful data back into hands of the business. Our API gateway acts as a schema mapper. It takes the JSON output from the LLM

**[13:15](https://www.youtube.com/watch?v=IEF842ZEU5A&t=795s)** uh and maps the field like customer intent or resolution status and and directly to some corresponding fields in the um based on the company CRM system or any customer data which we have laid out via some REST APIs. So we don't remove the human entirely in this. We use a verification step in between. Uh the operator, it sees the AI-generated summary auto-populated on their screen. Uh they do a quick visual field validation, make some minor edits if necessary, and then just click the confirm. Uh simultaneously, this structured data, it flows into our business intelligence models um aggregating the voice of the customer

**[14:03](https://www.youtube.com/watch?v=IEF842ZEU5A&t=843s)** data for management dashboards and automatically, you know, flagging the candidates for new FAQ um data entries. Now to tie the architecture together, this is the linear workflow logic of the data pipeline. We take the raw transcript complete um with the time indexing uh confidence is scoring and denoising. We passes we pass it through these speaker separation because we split the stereo channels um in the step one. Um we can easily stitch the dialogue together logically. Like customer said X, agent said Y.

**[14:51](https://www.youtube.com/watch?v=IEF842ZEU5A&t=891s)** Uh then we move to the context deduct deduction where the LLM spots the entities like account numbers um or product name or customer name run the sentiment analysis and recognizes the intent. And the final state is the structured output. So instead of a wall of text, uh the system, it outputs like clear uh and a clean JSON schema matching some predefined uh customer data or maybe CRM templates which we have in the enterprise and then categorize neatly into bullet points. And and this strict formatting is what turns an unstructured conversation into a database-ready asset. So what happens when we deploy this

**[15:42](https://www.youtube.com/watch?v=IEF842ZEU5A&t=942s)** architecture in a real contact center environment? Let's look at the outcomes. The operational impacts out of the implementation were quite immediate and and highly measurable. Um look at the ACW time under the manual operation, after average after-call work was 6.3 minutes. Uh powered by our AI workflow, that dropped to like 3.1 minutes, which is like almost 50% reduction in the processing time. Um if you calculate that across 500 seats handling thousands of calls a day, you are looking at a massive operational saving, the equivalent of almost

**[16:30](https://www.youtube.com/watch?v=IEF842ZEU5A&t=990s)** reclaiming dozens of full-time head counts purely from efficiency standpoint. Um [snorts] the next aspect is of data entry quality. It it moved from a highly subjective and a variable to highly standardized and uniform output. Uh the inquiry categorization or the call reason tagging, uh it moved from being dependent on an operator mode or memory um to um being a strictly logic-based resulting in a highly consistent voice of the customer data set for the management. And ultimately, by removing these repetitive administrative burden of typing out notes, we reduce the cognitive load on the operators,

**[17:18](https://www.youtube.com/watch?v=IEF842ZEU5A&t=1038s)** thereby stabilizing the operations and directly combating the stress which is linked with the staff. And and this ultimately reduced the turnover we identified um at the very beginning of our discussion. While the results were fantastic, the in the engineering work is never done um and and let's talk about the constraints we face uh and our roadmap for the future. Um We are currently navigating three main constraints. First is the um source to source to text accuracy, STT accuracy. The entire generative AI summary, it

**[18:06](https://www.youtube.com/watch?v=IEF842ZEU5A&t=1086s)** relies on the transcript. So if the STT engine uh fails to pick up heavy accents or poor audio quality, the LLM has nothing to work with. So the STT optimization is a continuous battle for us. Uh second is the initial setup cost. While the long-term ROI is massive, the initial consumption of the API tokens, especially running complex LLM reasonings on long 20-minute uh transcripts can be costly. And uh especially during the initial scaling phases, those are tough ones. And and we are constantly working on token optimization techniques to bring this number down. Uh the third is the security and compliance. Um handling PII uh per

**[18:57](https://www.youtube.com/watch?v=IEF842ZEU5A&t=1137s)** any kind of sensitive information in audio streams is very complex. Um and ensuring robust masking before the hit data hits the cloud endpoint is a strict requirement. Um and uh because of this, we add some layers and it ultimately reduces increases the latency and also adds some overhead from architectural standpoint. So we are still figuring it out how we can reduce those extra layers and make it much more robust component-wise. All right. So to address these constraints, and and push the boundaries of what's possible, our roadmap is currently broken down into three phases.

**[19:47](https://www.youtube.com/watch?v=IEF842ZEU5A&t=1187s)** Uh phase one, it focuses on explainable AI. Um we want to move beyond just summarizing calls to actually you know coaching the operators. We are engineering the systems to analyze the audio post call and provide operators with instant private feedback on their either soft skills or empathy level or any kind of accuracy from a information standpoint. The phase two it targets the predictive staffing by taking the massive amount of categorized intent data we are now capturing we can feed the same exact data intent data into a time series analytics.

**[20:34](https://www.youtube.com/watch?v=IEF842ZEU5A&t=1234s)** And this will allow the workforce management to accurately forecast the call volume spikes based on those specific topics and thereby optimizing the shift scheduling. The phase three is perhaps the most important for human well-being combating the customer harassment uh contact center agents they mostly face an increasingly amount of verbal abuse. And we are developing a low latency sentiment and acoustic analysis that can detect when a customer becomes abusive. Ultimately the system can you know uh trigger some triggers I mean alerts or something which is important from notification

**[21:24](https://www.youtube.com/watch?v=IEF842ZEU5A&t=1284s)** standpoint to supervisor or anyone who is there in the from the management upper management standpoint or maybe seamlessly transfer the call to an AI voice agent just to protect the human operator mental health in case of these tough conversations. All right. So uh by applying these rigorous engineering techniques to the messy audio data we can definitely transform the contact centers from uh cost centers of like high stress into a highly efficient and intelligence gathering engines that protect their

**[22:13](https://www.youtube.com/watch?v=IEF842ZEU5A&t=1333s)** workforces. That's the whole idea of having this right. Thank you so much for your time and listening to me. I have included my QR code which I will just flash in here uh so that you can grab me over LinkedIn. And please feel free to connect if if you would like to discuss the architecture or any prompt engineering strategies related to the discussion which we had in here and happy to connect and make things work things out between us and we can have more conversations. So thank you so much for listening to me and have a good one. Bye.
