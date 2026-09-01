---
id: mJR1g4UJcLI
title: "Building next-gen audio-first experiences: Lessons from PlayStation"
slug: building-next-gen-audio-first-experiences-lessons-from
conference: google-cloud-next
conference_name: "Google Cloud Next"
category: "Vendor & platform"
edition: "Next 2026"
year: 2026
speakers: ["Haris Ioannou", "Golda James"]
channel: "Google Cloud Tech"
duration_min: 22
published_at: 2026-06-25T16:22:46Z
video_id: mJR1g4UJcLI
url: https://www.youtube.com/watch?v=mJR1g4UJcLI
youtube_url: https://www.youtube.com/watch?v=mJR1g4UJcLI
tags: []
transcript: true
---

# Building next-gen audio-first experiences: Lessons from PlayStation

**Haris Ioannou, Golda James**

`Google Cloud Next` · `Next 2026` · `2026` · `22 min`

[Watch the recording](https://www.youtube.com/watch?v=mJR1g4UJcLI) · [Conference site](https://cloud.withgoogle.com/next/)

## Description

Speech is the next frontier of multimodal interaction, transforming how users engage with technology. Move beyond basic voice commands and discover what it takes to deploy low-latency, audio-first agents at global scale. In this session, we’ll break down how PlayStation partnered with Google Cloud to redefine their player experience, evolving from standard voice tech to an intelligent system that achieved a massive reduction in operational costs while significantly increasing caption accuracy. We’ll dive deep into the technical architecture behind these results, demonstrating how Gemini Audio on Gemini Enterprise Agent Platform enables real-time multilingual speech-to-text (STT) support and hyper-natural text-to-speech (TTS) cues that improve accessibility for everyone. Whether you’re solving for immersive gaming or enterprise support, join us to get the production-ready blueprint for building voice interfaces that are faster, smarter, and more cost-effective.

SSubscribe to Google Cloud Tech → https://goo.gle/GoogleCloudTech

Speakers: Haris Ioannou, Golda James

BRK2-088
#googlecloudnext

## Transcript

*2,469 words · source: supa (en, exact timings)*

**[0:13](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=13s)** Good morning, Las Vegas. I know it's Friday. I know it's too early. Thank you so much for coming. My name is Harris. I am a product manager here at Google. And today, along with Sony, we will talk about building next generation audio first experiences. On stage with me shortly will be also with James, Director at Cloud engineering at Sony Interactive Entertainment. So what we're going to talk about today, first we will walk you through about Gemini app audio. We'll have a small overview. Then we'll talk about what is the latest about Gemini app audio at Google. And then, of course, we have PlayStation and Sony on stage to walk us through how exactly they utilize

**[1:02](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=62s)** these voice first capabilities into their production environment. For us here at Google, voice is the next modality for authentic first interactions. But what exactly does that mean. It means that we want to supercharge in-domain voice accuracy. That means being accurate, being natural, and being real time accurate means that speeds understanding what we use to refer as speech to text should be accurate in all the languages that we want to support globally. Currently, we support more than 75 in use cases like live captioning, call center, and of course, media and entertainment. Natural speech generation with support

**[1:53](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=113s)** of more than 88 languages, 30 pre-trained voices and with voice replication capabilities to power authentic experiences using natural disfluencies and nuanced intonation. And all of these things should work in real time. People come here at Google that they are expecting the latest in real time capabilities. That means latency to extract real time insights and actions through conversational workflows is one of the primary factors. We power so many use cases across the industry, like conversational AI gaming, that we'll talk about health, financial services, education, devices, media and entertainment all the way to social media and media

**[2:43](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=163s)** across our portfolio. So let's go through exactly what is new with Gemini audio. Last year on speech to text API, we introduced Chirp Chirp three was the latest in speech understanding and captioning capability. In fact, three days ago, Sierra, a leader in conversational agents, released a public benchmarks placing Chirp three on top of the benchmark in accuracy. So we are very, very happy today to reintroduce Gemini app ASR a-star stands for automatic speech recognition. What exactly does that mean. It means that we're taking the main line Gemini

**[3:31](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=211s)** app that many people come and love, and we fine tune it, distill it, and fine tune it for speech understanding task for multilingual, real time transcriptions. So what we gain, we gain 7570 to 75 language support cross-lingual. So mid sentence speaker speakers can change, their language can change on how they pronounce digits and alphanumerics how they pronounce terms. And at the end of the day, the model can understand and can caption in real time. Market leading features. As I explained, streaming support, automatic language detection, word level timestamps, and of course, long long file transcription support. These were landing as part of the Vertex AI API later in May.

**[4:26](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=266s)** This is a small example talking about puppies. The important part is to see the real time aspect of it, so how fast it generates transcriptions. Yeah, that's the dream. Want to be burrowed in a pile of puppies right now. Who doesn't. People who don't like puppies are insane. I feel like I can smell their puppy breath just looking at this. And their little noses, their little wet noses, they look so soft. I also love how sleepy they are when you just like something that is important. If you paid attention. Yes, the captions were there, but at the same time we had Engel brackets that, for example, were expressing the sight or excitement. So this is part of the question of what we gain by using a multilingual LLM based model.

**[5:20](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=320s)** The second part of the speech of the speech and Gemini app audio portfolio is Gemini app TTS. Again, similar to what we do for the ASR task, we're doing it for the speech synthesis task. That means that again, we take the big model, we distill it and specifically perform reinforcement learning on top of it for the speech generation task, adding controllability, expressivity and overall quality. Gemini TTS was introduced late late last December with 5030 pre-trained voices, support for audio tags and support for multi-speaker. We introduced 2.5 last December using the Pro, the Flash and the flashlight model, and we're

**[6:10](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=370s)** extremely proud because last week, we introduced 3.1 Flash in public preview. Of course, going later in GA later in the quarter. Let's play a small example, because what we will see here is that similar to what we discussed with the square brackets for the speech understanding task, here you will see the same. The same in essence a similar paradigm using square brackets to control the speech. So hello. Hello bonjour. Konnichiwa Hola, marhaban. Welcome back to the show.

**[7:03](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=423s)** Let's get into it. Thanks for having me. Really glad to be here. I think that's fascinating. So what are customers want. Customers in call centers. They need a workhorse model. They need a robust voice across 4,000 queries per second to power all of their call centers here in the United States, in Europe, in Asia and whatnot. Some other customers need more expressivity. So with one model, by giving this control over the control tags and also the style prompt that you briefly saw on the demo, we provide all this control capability over speeds, and that is true for both real time

**[7:51](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=471s)** and on real time use cases like for example, podcasts or notebook use cases. So we're extremely proud. We introduced Gemini 3.1 last week. Another example because I love it. This app is powered by the New Gemini. Text to speech model. Let's use it to explain the latest improvements in style and pacing with this model. Type or paste your text and the app will help out by adding modifiers to make the speech model output even more expressive. Using square brackets, we can modify the style, transitioning seamlessly from a slow, suspenseful whisper to a really, really fast paced sequence in case you're in a hurry. The model can now sigh and laugh, but my favorite feature is dynamic pacing,

**[8:44](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=524s)** because sometimes the most powerful thing you can say is nothing at all. That's incredible. So again, we power the classic Gemini voices, the 15 male, 15 female. And we will also talk about voice replication. Something that I wanted to mention is that we provide this capability through an API through a user interface. And you might say at scale, how am I going to write all this manually. Manually all these tags. Of course, most of our customers are using Gemini with a tag list to make sure to prompt the model correctly, and this is also available through MCP. Improved speech quality and controllability. You can see on artificial analysis we actually

**[9:32](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=572s)** topped up the leaderboard. We went from 15 all the way to second actually. So let's talk about voice replication using the same model capability. We allow we allow our customers with only 10 to seconds of their voice to also replicate, replicate it. We are actually pre-announced that Gemini 3.1 Flash voice replication is going to private preview next week. And what is actually the gain here. The gain is that you are able to replicate your voice in the same language that you pre-recorded it. And again, with style prompt and voice tags,

**[10:22](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=622s)** you can also control exactly the flow. Let's play a small example. Two things that I want to note here again based on the 10 to 30 seconds. Of course, the longer the audio that is representative of the user, of course, the better the model can adapt. That's one. And the second will see how it replicates in the script. Can we play please audio first and second. No, it seems that will not be able to play it, actually. But it's fine. A little later in the month, we will also release a blog. A blog spot on this one, we will have all the audio examples available. So let me pass it to Sony and let's talk about how audio is actually helping Sony and PlayStation being

**[11:10](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=670s)** successful into their gameplay. Please welcome on stage, James. There you go. Thank you. Thank you Harris, and thank you, everyone, for joining us today. Good morning. Happy Friday I'm Golda from Sony Interactive Entertainment. And today, as Harris said I'm here to share with you our journey when we integrated with Google's pages APIs over the last couple of years to enable an audio first gaming experience for our players. So what is audio first gaming players today expect and deserve interactions that feel instant, real, natural, and global. Audio is not just a feature anymore, it is an entire interface that can enable that experience

**[12:01](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=721s)** for our players. And our mission is simple to remove every pause between intent and action to help our players play more and pause less. At PlayStation, we are continuously pushing the boundaries of play, inspiring remarkable experiences for gamers everywhere to enrich lives through games and connect the world through the power of play. We truly believe that play has no limits and should have no limits, and we constantly strive to remove any barriers and reach. Players of all abilities, and voice and speech capabilities are key technology to making that audio first gaming experience possible for our players.

**[12:48](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=768s)** So what does this look like in practice. Voice is embedded across the gaming experience at PlayStation. I'm going to share a few use cases with you all today for gameplay. Party chat transcription converts voice to text and text to speech reads messages back to players. Voice dictation allows players to search just by using their voice on screen keyboard for creators, broadcast comments allows them to focus on their game while messages are being read aloud. Then we have the voice agent. This is still in preview mode, but you can use your voice to find or open games. Search for apps settings, get help,

**[13:37](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=817s)** and control media playback as well. So I'm going to share a quick demo with you today. And there is some loud music because we had to turn up the volume so you could hear the player interaction. Let me see if this works. Hey, PlayStation Final Fantasy. I found these for you. Which one do you want. Number two. OK hey, PlayStation. Street fighter. I found these for you. Which one do you want. Show more. OK hey, PlayStation.

**[14:33](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=873s)** Go to home. OK hey, PlayStation. Station Media Gallery. OK hey. Police station. Captured setting. OK Police station. Go to home. OK start recording. Hey so listen up.

**[16:14](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=974s)** Hey PlayStation. Go to rest mode. Your PS5 is about to go to sleep. Say yes to confirm or No to cancel. Yes OK. That's awesome, isn't it. Feel free to try this out at home. Now, behind the scenes, this operates at massive scale. Transcriptions are processed over millions of user sessions, with usage growing at a very high rate month over month. This powers not just accessibility, but also player connection and safety and moderation. And the voice agent drives interactive gaming experience

**[17:05](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=1025s)** with context awareness. But at this scale, this is not an easy problem to solve. We had to balance accuracy, latency, and cost the trifecta. And solving for all three is where the challenge began and why we chose Google speech services. Let me explain a little bit more on the why and then go to how. So why did we choose Google speech services. We needed more than just speech APIs. We needed a platform that could scale globally, that could transcribe in real time models, that could be trained to understand game specific slang and titles like tek and 8 or Final Fantasy 9 in Roman numerals, and meet a high bar of enterprise requirements and be cost efficient at scale.

**[17:57](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=1077s)** We needed a partner that could evolve with us as we build a foundation for our Player community. So how did we do it. We took a phased approach. We evaluated data start with data, write, benchmark everything across vendors, and chose the best for our players. We integrated across a long period of time in parallel with our partner. We validated in production and scaled. The key to this was our shadow mode functionality. This allowed us to run legacy and new vendor services in parallel with real production traffic. Our aim was to achieve a 0 disruption migration for our players. But of course, we didn't do it alone.

**[18:44](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=1124s)** We build lasting partnerships internally. We were moving from integration to platform transformation with multi-vendor capabilities and abstraction layers. Partnering with cross teams with a one team approach. With Google, we focused on rapid iteration from addressing gaps to evaluating models that continuously fit our player needs. And the results were amazing. The player experience improved with faster, more accurate interactions. Communication became more seamless with less friction. We achieved major cost efficiency while scaling globally in real time. And most importantly, we enabled our players to play more and pause less without limits. We are already building even better experiences

**[19:36](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=1176s)** for our players every day. So what you see here today we are building even next Gen audio first gaming experiences that you'll see tomorrow. So friends the future is not just voice, it's systems that can understand and respond and scale in real time. And there are no limits to what we can achieve together. So with that, I'm going to invite back on stage Harris to close this out. Amazing job. Yeah thank you. So to recap, first we announced Gemini 3.1. It's in public preview coming later in GA later on next month,

**[20:33](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=1233s)** we pre-announced Gemini 3.1 voice replication BTS coming private preview next week, and we pre-announced Gemini ASR coming late in May. This is how we at Google. We believe that voice is the next interface. This is how we're planning and already powering all the voice first experiences here at Google externally and with amazing customers. And thank you so much Sony for this amazing experience. Going through scaling globally and reaching to so many millions of end users. It has been an incredible partnership. Thank you so much for your time. Thank you so much for coming on a Friday. And thank you so much, Sony, for being part of this amazing journey.

**[21:20](https://www.youtube.com/watch?v=mJR1g4UJcLI&t=1280s)** Everyone appreciate the time.
