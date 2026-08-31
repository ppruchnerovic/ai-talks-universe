---
id: Z7zx_sTbFPI
title: "Deploy Android on-device AI with ML Kit GenAI and LiteRT-LM"
slug: deploy-android-on-device-ai-with-ml-kit-genai-and-litert-lm
conference: google-io
conference_name: "Google I/O"
category: "Vendor & platform"
edition: "I/O 2026"
year: 2026
speakers: ["Caren Chang", "Erin Walsh"]
channel: "Android Developers"
duration_min: 17
published_at: 2026-05-21T23:36:37Z
video_id: Z7zx_sTbFPI
youtube_url: https://www.youtube.com/watch?v=Z7zx_sTbFPI
tags: ["Android", "pr_pr: Google I/O;", "ct:Event - Technical Session;", "ct:Stack - Android;"]
transcript: true
---

# Deploy Android on-device AI with ML Kit GenAI and LiteRT-LM

**Caren Chang, Erin Walsh**

`Google I/O` · `I/O 2026` · `2026` · `17 min`

`#Android` `#pr_pr: Google I/O;` `#ct:Event - Technical Session;` `#ct:Stack - Android;`

[Watch the recording](https://www.youtube.com/watch?v=Z7zx_sTbFPI) · [Conference site](https://io.google/)

## Description

Differentiate your app and elevate your user experience with on-device AI. Learn about different ways to bring on-device AI to your Android apps through ML Kit GenAI APIs for turnkey solutions powered by Gemini Nano and LiteRT-LM for customized use cases with your own models.

Resources:
AICore Developer Preview → https://goo.gle/3QOCdGt
Automated Prompt Optimization → https://goo.gle/4dquC9N
MLKit GenAI APIs → https://goo.gle/mlkit-genai-apis
Speech Recognition → https://goo.gle/mlkit-speech-recognition
Prefix Caching → https://goo.gle/3RnvLGv
Structured Output → https://goo.gle/mlkit-structured-output
Model Selection → https://goo.gle/mlkit-model-selection
Run LLMs on-device with LiteRT-LM → https://goo.gle/42VglvD
AI Edge Gallery App → https://goo.gle/4tBazdT
Google Hugging Face → https://goo.gle/4tfrvpK
Gemma Cookbook → https://goo.gle/4upOIqh

Speakers: Caren Chang, Erin Walsh

Watch the Android sessions from Google I/O 2026 → https://goo.gle/Android-at-IO2026

#GoogleIO

Event: Google I/O 2026

Products Mentioned: AI/Machine Learning, Android

## Transcript

*2,563 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=0s)** [MUSIC PLAYING] CAREN CHANG: Hi, everyone, I'm Caren. And today, I'm joined by Erin to talk about the latest developments of on-device GenAI and Android. In this talk, we'll cover why and how you should consider on-device AI use cases for your app; AICore Developer Preview, a new way for you to preview the latest on-device models and improve your overall development process; ML Kit GenAI APIs that help you bring most use cases to production; along with new capabilities like speech recognition and improvements to prompt API with caching and structured output; and LiteRT-LM to help you enable even more customized use cases. Let's start by talking about why you should consider

**[0:49](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=49s)** on-device GenAI in your apps. On-device GenAI refers to the ability to process prompts and data directly on a device without sending data to a server. Since a server is not required, this offers a few advantages. Sensitive user data can be processed locally on the device. Functionality of the model does not depend on internet connectivity, meaning the model can output reliable results even with spotty or no internet connection. And lastly, there is no additional cost for each inference, since everything runs on the user's hardware. With these advantages, on-device makes a great solution for use cases like handling sensitive user data, such as banking or medical records; personalization to build tailored experiences for your users, such as customized summarization of news

**[1:39](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=99s)** articles tailored to a user's specific interests; and scenarios that require a smaller context window and compute power, such as translating short sentences or classifying content into specific categories. Building these types of differentiated use cases elevates the experience for users. And Google is committed to making this possible for you on Android with access to models like Gemma and Gemini Nano. Gemma is a collection of state-of-the-art open models built from the same technology that powers the Gemini models. On supported Android devices, Gemini Nano builds on Gemma's architectural foundation and is further optimized for maximum battery and performance efficiency. This means that prompts you write for Gemma for today will automatically work for the next generation of Gemini Nano models when it's shipped on flagship devices.

**[2:29](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=149s)** To make it easy for your apps to utilize the capabilities of these powerful on-device models, we provide a complete stack of production-ready solutions. First, for the majority of use cases, ML Kit GenAI APIs offer the most direct path to production. These APIs provide access to Gemini Nano with the Android OS automatically managing model updates, so apps are always using Google's most powerful on-device model. Alternatively, if your app targets niche domain areas, LiteRT-LM allows you to manage and run small, customized models on users' devices. Let's dive first into ML Kit GenAI APIs that allow you direct access to Gemini Nano. On supported devices, Gemini Nano is deployed and managed through AICore, an Android system service.

**[3:17](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=197s)** By using Gemini Nano through AICore, apps gain advantages such as optimizations based on the device hardware to enable lower inference latency and reduce power consumption; no extra effort in managing model deployment, including updates to the Gemini Nano model; and built in privacy and safety. AICore is designed to isolate each inference request. This means that requests are handled independently and processed from one app at a time to mitigate the risk of data being exposed to other apps that use AICore. Input data and the resulting outputs are never stored anywhere on the device. To give you a more concrete idea of the developer journey when integrating ML Kit GenAI APIs, let's see what it takes to go from prototyping to productionizing use cases. With AICore Developer Preview, you

**[4:07](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=247s)** can now test both production and preview models at Gemini Nano, allowing you access to the latest capabilities of Gemini Nano before its launch to production. Using the app, you can download models, explore new use cases by testing prompts, and have control over developer settings such as bypassing quota limits. Preview models are currently available for testing on AICore-enabled devices from Google and select device manufacturers. To further improve the developer journey when prototyping with preview models, we've introduced the Model Selection API. This API allows apps to target preview models for their prompt API integration in order to test the full code path of a new model. When initiating a model to make inferences through prompt API, you can now specify the target model.

**[4:55](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=295s)** By providing the ability to download and prototype with preview models, such as Gemini Nano 4, we hope you can get a head start on refining prompt accuracy and exploring use cases before the model's launch on consumer devices. To get started, check out the step-by-step instructions at our official documentation. Next, after prototyping and refining prompts, it's time to implement use cases directly in your app. ML Kit GenAI APIs makes this easy for you by providing out-of-the-box quality through a high-level interface for common use cases such as summarization, proofreading, rewriting, and image description. Last year, we introduced APIs that require no prompts and just a few lines of code. To add on to these popular use cases, we recently unlocked on-device audio experiences with ML Kit's Speech Recognition API.

**[5:46](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=346s)** This API transcribes audio content, either from the device's microphone or an audio file, to text. On supported devices, the API will use the on-device Gemini model. And on all other devices, developers have the option to use a traditional on-device speech recognition model. This means that the API is compatible with all devices running Android 31 and above. With the on-device Gemini model, ML Kit's Speech Recognition API provides the following benefits-- higher quality transcriptions for languages such as Arabic, Indonesian, Dutch, and more. Less storage required-- the traditional, on-device speech recognition model requires downloading a single model between 100 to 200 megabytes for each language the user uses. However, the on-device Gemini model only requires one small lower adapter to transcribe all supported languages--

**[6:37](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=397s)** and a more friendly developer API for streaming audio capabilities. Start implementing Speech Recognition API in your Android apps today with guidance from our official documentation. Now, if your app wants to implement a user journey beyond the predefined use cases just discussed or you want more control over the output, we recently introduced Prompt API. Prompt API allows you to send any natural language requests to Gemini Nano by accepting text and images as inputs and emits a text output. The versatility of this API has enabled Adobe Photoshop to utilize it in multiple ways to improve the user experience from start to finish. From the beginning of the creation process, the app is able to intelligently rename images during imports and exports.

**[7:26](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=446s)** This use case is enabled by Prompt API's multimodality support with image inputs. While editing assets, users often have to manage multiple layers in Photoshop. Using Prompt API, the app is now able to automatically rename unorganized layers as Actions in the Layers panel. And finally, the app generates a caption and hashtag for the direct-to-social sharing workflow. It's been exciting to see the different ways apps have used Prompt API to fully embrace on device GenAI for use cases such as translation, classification, user content inspiration, and much more. And since Prompt APIs initial launch last year, we've made a couple of key improvements to help you further productionize your use cases. Let's talk about the new APIs that

**[8:13](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=493s)** make it easy for you to maximize performance and quality so you can ship your features to users. The first is Prefix Caching. Prefix Caching reduces inference time by storing and reusing the intermediate LLM state of processing a shared and recurring part of the prompt. For example, if a prompt contains a long prefix portion that's the same for every request, the Prefix Caching API can preprocess this to save overall inference time. To get a better idea of the efficiency prefix caching can provide, for most devices, inferences were, on average, two times faster for prompts with a 1,000 token fixed prefix and a 100 token dynamic suffix with prefix caching enabled. And on Pixel 9, it was four times faster. There are two ways to enable prefix caching,

**[9:01](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=541s)** with automatic or manual cache management. With automatic cache management, the app is only required to define a shared portion of a prompt. Whereas, manual cache management gives apps more control on cache creation, querying, and deletion. For more information on how to enable prefix caching, including code samples and storage considerations, check out our official documentation. Next, to improve the accuracy when requesting specific output formats and ease the overall developer workflow, we've introduced Structured Output API. This API allows apps to define object classes to be returned as outputs from Prompt API requests. For example, imagine we want to implement a use case where we extract information from a short email to create a calendar event.

**[9:51](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=591s)** Using prompting, we could craft a long prompt in plain English with specific instructions about details to extract from the email, such as the title, date, and location of the event, and include an example JSON object we want as the output. However, this approach is error prone and can return inconsistent results. The output may be an incomplete JSON object, or the returned JSON object may not have all the fields we requested. With structured output, we can now define a calendar event data object and use generateTypedContent when making an inference request. generateTypedContent will take a Kotlin data class marked as generable to better understand what the expected output should be. Inside the generable, you can further define guides to specify how each field in the data class

**[10:40](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=640s)** should be generated. This approach with structured output reliably returns consistent results and makes code simpler with Kotlin data objects that integrate seamlessly into your Android codebase. To get started, visit the official documentation for using structured output with prompt API. Lastly, to remove the guesswork from prompt engineering, we introduced Automated Prompt Optimizer, or APO, targeting on-device models. APO is an advanced tool for developers seeking to maximize quality by utilizing a well-prepared evaluation set. It helps you automatically find the optimal prompt by taking the guesswork out of manual prompt engineering. Using server-side models, such as Gemini Pro and Flash, it proposes improved prompts, uses data sets and evaluation

**[11:30](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=690s)** metrics you provide to measure variations in results, and finds the best prompt for your specific use case. To try out an early version APO, check out the official documentation on Vertex AI. Now that we've seen the ways ML Kit GenAI APIs can enable different use cases in your Android apps, let's hand it over to Erin. We'll dive into how LiteRT-LM can help you unlock even more use cases. ERIN WALSH: Thanks, Caren. ML Kit and AICore are incredible for getting AI features running out of the box. But what happens when you need a custom solution unique to your needs? What if you need to run a highly specialized model or maximize reach on a wide variety of Android hardware? Beginning a custom solution starts

**[12:17](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=737s)** with choosing the best model for your use case. You may want to use an open-source model such as Gemma or bring your own. For the best Android performance, always use the smallest possible model that reliably solves your use case. We'll demonstrate fine tuning a specific task using Gemma 270M, a highly efficient 270-million-parameter model. Let's imagine a real world scenario. Maybe you're building an agritech app for farmers in rural Maharashtra, India. Your backend provides agricultural insights and weather warnings in English. But you need to translate this information into Marathi so your users can actually understand it. You need the model to capture the actual nuance of the language, specifically, the Varhadi

**[13:07](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=787s)** dialect, local farming colloquialisms, and regional slang. But it needs to run offline due to rural farms in regions with no connectivity. Gemma 270M can solve this. But it will perform much better if we fine-tune it for this exact dialect. Start by curating a specialized data set, or grab a conversational English to Marathi data set publicly available on Hugging Face that provides the model with thousands of paired sentences. You can fine tune directly in a Google Colab notebook. Using community tools like the Hugging Face TRL library and SFT Trainer, you load your regional data set and train the model until it reliably generates accurate, localized translations. Once your model speaks the local dialect,

**[13:55](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=835s)** convert and quantize the model into a format optimized for the constraints of mobile hardware using the LiteRT-LM command-line tool. This tool transforms your fine-tuned model and converts it directly into the LiteRT-LM file format. Check out the LiteRT-LM CLI documentation for more information on how to convert your model. When you are ready to integrate your custom, LiteRT-LM model into your own app, you can use the LiteRT-LM API to manage sessions and run inference natively in Kotlin. First, you initialize the engine with your model path and preferred hardware backend like CPU, GPU, or NPU, and load your model in the background. From there, you instantiate a conversation object which automatically manages the context window and chat

**[14:44](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=884s)** history for you. Finally, to give your users that fast-typing-effect experience, you can use sendMessageAsync. This returns a calling flow, allowing you to stream tokens directly to your UI as the model generates them. Getting your model up and running on your own developer phone is a huge one, but how do you guarantee your custom model will run smoothly across the ecosystem, even on older devices? The Google AI Edge portal automates this by benchmarking your LiteRT-LM file across a fleet of over 100 real, physical Android devices hosted in Google's labs. So then you can see how your model performs across all these devices before you ever even hit production. Even though we are using Gemma 270M as an example today,

**[15:34](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=934s)** it is important to note that this flow with Google AI Edge works for any open model. And to recap, when you need a truly custom experience, like an offline translator for regional dialects, Google AI Edge and LiteRT-LM are your solution. And by packaging your fine-tuned models in the LiteRT-LM format, you reach beyond the newest devices, scaling to a broader and more diverse range of Android devices. If you're ready to get hands-on, we have three great resources for you to check out. To learn how to train your own custom models, head over to the Gemma Cookbook. When you're ready to drop those models into your app, the Google AI Edge documentation has everything you need, from API references to performance evaluation tools. And if you just want to dig straight into the code

**[16:23](https://www.youtube.com/watch?v=Z7zx_sTbFPI&t=983s)** and test out different open-source models today, download the AI Edge gallery app on the Play Store or fork it on GitHub. CAREN CHANG: We hope this overview gives you more confidence when implementing on-device GenAI with ML Kit GenAI APIs for the majority of turnkey solutions and LiteRT-LM for more customized use cases. We're excited to see the different ways you will bring on-device GenAI to your Android apps. Check out the resources linked in the video description below on everything covered in this talk to get started. [MUSIC PLAYING]
