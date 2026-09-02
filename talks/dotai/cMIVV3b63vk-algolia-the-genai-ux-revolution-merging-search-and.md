---
id: cMIVV3b63vk
title: "Algolia & The GenAI UX Revolution: Merging Search and Conversation at dotAI Tech Track AI Day"
slug: algolia-the-genai-ux-revolution-merging-search-and
conference: dotai
conference_name: "dotAI"
category: "AI engineering & agents"
edition: "dot conferences"
year: 2026
speakers: ["Xavier Grand"]
channel: "dotconferences"
duration_min: 16
published_at: 2026-02-17T13:58:46Z
video_id: cMIVV3b63vk
url: https://www.youtube.com/watch?v=cMIVV3b63vk
youtube_url: https://www.youtube.com/watch?v=cMIVV3b63vk
tags: []
transcript: true
---

# Algolia & The GenAI UX Revolution: Merging Search and Conversation at dotAI Tech Track AI Day

**Xavier Grand**

`dotAI` · `dot conferences` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=cMIVV3b63vk) · [Conference site](https://www.dotai.io/)

## Description

Speaker: Xavier Grand, CTO at Algolia

Description:
Drawing from 10 years of search evolution, Xavier Grand, CTO at Algolia will explore how conversational AI agents bring new possibilities. Acting as domain experts, they can ask the right questions to unblock users. Through a live demo, you'll see how conversational discovery and traditional search can be blended together. Don't waste time searching, focus on finding.

dotAI Tech Track organized by dotConferences at AI Day on February 10, 2026, at Station F.

## Transcript

*2,074 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=cMIVV3b63vk&t=5s)** [music] Hello everyone. Happy to present you how the let me keep the mic there. It will be better. Uh how the genai uh revolution how the search works. Um and so let's start before we deep dive by introducing myself. So I'm Xavier. I joined Alolia now 12 years ago. I joined a small startup of five people as an intern and 12 years later I'm now the CTO of 800 people company worldwide. Uh it was a great journey not only for me also for search. Uh we started when

**[0:54](https://www.youtube.com/watch?v=cMIVV3b63vk&t=54s)** search was the last thing you wanted to touch. If you remember Amazon, that's where they were hiding the search to now it's the the entry place. You see that at the center and it's potentially going to be the only place to start your journey. Now um let's speak a bit about Alolia. Uh so Alolia is the search as a service that you need to build your uh search experience. Today we power 1.8 trillion searches per day in on average 20 m per year sorry and in uh only 20 millisecond. We do that thanks to our search engine that we built internally. We store now 30 billion records and are

**[1:42](https://www.youtube.com/watch?v=cMIVV3b63vk&t=102s)** trusted by uh 18,000 customers. uh we we are uh trusted by those customers because we provide the front-end libraries to help you build uh quickly the experience that you want. We also provide you the search and agentic engine to power this experience and the analytics to to help you understand how to create this feedback loop and improve uh improve it. Now, uh, we all search every single day and recently I had to upgrade my remote setup and I needed a new desk and my wife had some requirements about that to make sure it fits in the room. I'm not really into the look of uh things and so

**[2:31](https://www.youtube.com/watch?v=cMIVV3b63vk&t=151s)** that's where we I had a pretty strict requirement in term of color, in term of size and also a budget. uh in this kind of case we categorize this kind of behavior as don't funnel that's where you have people with strong intent so they want to find something now you have also the explicit criteria they already know how to narrow down the the product to what they are looking for and location if I was not finding what I wanted on a website I would just move to the next on and we all experience the case uh where you spend the time to properly input your criteria

**[3:20](https://www.youtube.com/watch?v=cMIVV3b63vk&t=200s)** uh press enter wait few seconds to end up with the no result page so that's where you usually give up and go back on Google and that's what we wanted to fix uh when we started which is to provide the experience where it's not only about the relevance of the search engine but also the speed. This way customers can interact with the search engine and as you select uh criterias adapt the result set. That's the first phase where humans us started to adapt ourself to how the search engine works. It's not natural the way we input the the keywords, the

**[4:09](https://www.youtube.com/watch?v=cMIVV3b63vk&t=249s)** criterias and so on and the [clears throat] sorry and and the the thing is we have been trained for decades about that. So that's why it's pretty uh it feels natural for us but it's really the search engine that is imposing this experience. After that, the second case that I had recently was to buy a gift for my niece for her birthday. That's where in this kind of case, I had no idea what I wanted to buy. I'm not anymore a kid, so I don't know what is trendy. I just had few affinities. I prefer something where kids can learn. Uh ideally not made of plastic but

**[5:01](https://www.youtube.com/watch?v=cMIVV3b63vk&t=301s)** something else. And uh that's where as a consumer we are more at the top of the finel behavior one where up our uh intent is weak. We don't know if we will buy today or later. We have uh just needs in term of affinity. we don't know clearly what are the criteria that we want to apply on what we are buying and uh high intent uh higher patience meaning that if I'm not buying that today I can go on another website spend my time to explore and refine what I'm looking for and in this kind of case uh that's where you don't want to act you want to be

**[5:49](https://www.youtube.com/watch?v=cMIVV3b63vk&t=349s)** guided so you you want the website to basically guide you through your journey. And in this case of case, there is one uh moment where this can be frustrating is when you buy the tool, but the battery uh is not included. And so you discover that when they unpack and that's where it's a pretty bad experience and you want the website to push you telling you, hey, uh maybe you should buy the battery at the same time because there is a lot of people doing so. And that's the the case where the second evolution of the search engine was more natural because the the search engine and experience started to adapt to you. The the results were ordered based on

**[6:40](https://www.youtube.com/watch?v=cMIVV3b63vk&t=400s)** what you prefer. The the suggestion were pushed to you. And this was done by ma mainly two uh main thing. The personalization where the system is able to understand the past interactions and adapt the result set based on that. And the second one is the recommendation. Based on what people are doing, they will uh suggest you similar items. And this is really deeply integrated in the current search journey. So you you when this has been introduced, you didn't already notice a change compared to when the search initial UX changed. Now uh with conversational and let's

**[7:32](https://www.youtube.com/watch?v=cMIVV3b63vk&t=452s)** speak first about the problem that I encountered where I was invited for a wedding with a specific dress code, a casual one. I had no idea what it meant. Uh and so it took me a while to discuss with CHP to understand what this means, how how I can understand what from this uh need of I need something casual for a wedding, I could find the corresponding uh clothes. And this is more a midfunnel where the intent start to surface. So it's more medium intent. I have explicit needs, but I still don't didn't convert that to specific product requirements. And I have a medium patience because I

**[8:20](https://www.youtube.com/watch?v=cMIVV3b63vk&t=500s)** need to finish my exploration. And that's where uh we move to next slide. Up. Let me go for a demo. Up. Up. If I'm up let I can do this this so it's where ideally what I would love to have at that time was so I will type with one hand so I may make mistake so is to ask for casual wedding so I'm not typing a full question because I cannot do that with one hand then ask This I don't have internet. Let me reconnect to my phone.

**[9:18](https://www.youtube.com/watch?v=cMIVV3b63vk&t=558s)** Yeah, that's the demo effect. Perfect. [laughter] And so now let's restart. Come on internet. Okay, let's go back. Casual waiting. So, it's usually faster. Uh, and so then I can be guided. So, here I don't want a dress. I potentially want a suit. uh potentially a blazer because yeah that's more casual. Then once I have that, okay, I can decide if I want to specific size

**[10:10](https://www.youtube.com/watch?v=cMIVV3b63vk&t=610s)** and so on. And then go back to the up sorry with one hand. Uh I want now to ask for [gasps] uh shoes and then I'm more Yeah. sneakers. I can then select specific color so that it's nicer and if I want to explore more, I can use the full potential of the search experience while at the same time I'm able to be guided through the the agentic one and yeah, there is only 10 products. So, uh it's that so up. So, let me go back to it.

**[11:02](https://www.youtube.com/watch?v=cMIVV3b63vk&t=662s)** Yep. So um so this kind of experience that I described is not the common one. That's what you will experience the most when you buy something that you occasionally buy. So for example, another one is when I had to buy a TV and I had to learn all the specs. Do you want AMOLED? Do you want OLED 3D curved screen? and you usually do that outside of the website and then go back to the website to realize that it doesn't exist and so on. So it's pretty uh painful experience compared to having that integrated in the website and able to recommend what you want. Uh uh

**[11:50](https://www.youtube.com/watch?v=cMIVV3b63vk&t=710s)** so uh to sum up really the the progress of Genai helped us to create something that was impossible before. You couldn't have an expert helping you to find what you were looking for. So either you were at the top of the funnel and able to uh to navigate the full website to find what you wanted, the bottom funnel where you knew exactly what you wanted and for the middle you had to use something else. And uh it's really a step function where the it's not just a fraction of the of a better expense. It's really a way better as you as you were able to see. I was able to scan through the website and the

**[12:39](https://www.youtube.com/watch?v=cMIVV3b63vk&t=759s)** different categories with one intent which is I want a complete outfit not a single product. Um [cough and clears throat] and we start to see this expenses emerging on different websites. They are interesting because it's really helping but today they are not really integrated. So, it's more the uh chat on the bottom right or the search bar uh at the center. And it's really complex because how do you merge an experience which is more a keywords and structured one with the the conversation which is purely text. And so that's all the complexity where we are investing to understand how this is merged. And the issue is that without this

**[13:28](https://www.youtube.com/watch?v=cMIVV3b63vk&t=808s)** integration we we are creating more friction than we are solving because customers uh and us we need to figure out should I start a chat journey because I'm unsure about what I'm looking for or a search journey and I don't know for you but every single time I have an option where I can choose from one or the other I'm often taking the third one which is okay I will figure out that later. That's the same when you have the different experience uh separated. And so that's why it's really important to merge those so that the friction is removed and we can really get the full potential of the genai. Now uh I drove you to uh an example which is specific to e-commerce

**[14:19](https://www.youtube.com/watch?v=cMIVV3b63vk&t=859s)** but this applies to every single search experience which is media knowledge or support. I don't know for you but for example with the amount of news coming these days I'm purely overwhelmed on the different topics I would really love to have an expert able to gather different articles to have a diverse point of view on something and that's where this kind of experience could help where I could ask not only okay give me this article but give me the articles showing different point of views And to uh sum up on this uh search is not really the finality. You don't search purely by pleasure. You search to find

**[15:08](https://www.youtube.com/watch?v=cMIVV3b63vk&t=908s)** something. And uh the thing is with conversational we are already improving what was the default for the past at least 10 years where all the previous technologies that was launching were there and now we're already improving the the experience for everyone and even if the technology is there the c the core is there the the experience is not really surfacing the full potential of it. We're only at the beginning where the chat is there. You you see the chat, you see some integrations, but you don't have the deep integration when the potential of Genai is visible everywhere on the search journey. And that's why I'm excited about what is coming next because that's where we

**[15:57](https://www.youtube.com/watch?v=cMIVV3b63vk&t=957s)** really leverage the full potential of it. And thanks for your attention. >> [music]
