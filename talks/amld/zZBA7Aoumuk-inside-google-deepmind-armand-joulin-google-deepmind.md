---
id: zZBA7Aoumuk
title: "Inside Google DeepMind | Armand Joulin, Google DeepMind"
slug: inside-google-deepmind-armand-joulin-google-deepmind
conference: amld
conference_name: "Applied Machine Learning Days"
category: "AI engineering & agents"
edition: "AMLD"
year: 2026
speakers: ["Armand Joulin"]
channel: "AMLD Intelligence Summit"
duration_min: 14
published_at: 2026-02-13T10:17:01Z
video_id: zZBA7Aoumuk
url: https://www.youtube.com/watch?v=zZBA7Aoumuk
youtube_url: https://www.youtube.com/watch?v=zZBA7Aoumuk
tags: ["AMLD", "Machine Learning", "ML", "Artificial Intelligence", "AI", "Applied Machine Learning Days", "EPFL", "AMLD EPFL", "AMLDEPFL22"]
topics: []
transcript: true
---

# Inside Google DeepMind | Armand Joulin, Google DeepMind

**Armand Joulin**

`Applied Machine Learning Days` · `AMLD` · `2026` · `14 min`

`#AMLD` `#Machine Learning` `#ML` `#Artificial Intelligence` `#AI` `#Applied Machine Learning Days` `#EPFL` `#AMLD EPFL` `#AMLDEPFL22`

[Watch the recording](https://www.youtube.com/watch?v=zZBA7Aoumuk) · [Conference site](https://appliedmldays.org/)

## Description

🟣 AMLD Intelligence Summit 2026

www.appliedmldays.org

## Transcript

*2,195 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=3s)** [music] >> All right. Thank you for having me here. I gave a talk here like 10 years ago and it's quite special for me to be back here 10 years later. Back then I was at Meta and now I am DeepMind still doing open sourcing. My talk is going to be about our newest models in open source from Google, but I usually get the question when I give this talk of why Google is doing open sourcing and how does it fit into the whole story. So I this time I I added a few slides at the beginning just to talk a little bit about where Google is in terms of AI and what is the philosophy behind all of that. Um So it starts first from the mission that is represented in everything we do. Like

**[0:51](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=51s)** we our goal is really to make AI helpful for everyone. This is not like a vague statement. This is something you can like experience in every of your Google products. Like in Google Maps, the fact that you have like way of of tracking your your or your roots is fueled by by AI to decide based on time what is the expected time. You see it in fast reply in Gmail, but you see it also in research where we regularly have nature papers and so on. It's really something where we think of AI as a tool that can change humanity and we want it for everyone everywhere. The second ingredient that is really key to the revolution that happened with Google the

**[1:40](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=100s)** merger of Google and DeepMind is that Google got into their hands fantastic machine that has been building AI breakthroughs since more than 10 years. The first one and I kind of the pivotal moment was AlphaGo that they did I don't know how many years ago, but this this breakthrough wasn't just like an amazing AI model. It's also way to to have AI breakthrough from the design of the project like thinking of like is it a good project? How do we tackle it? How do we do the infra on top of it? And when you see it from the inside it's it's not just all random ideas here and there. It's a really like powerful machine to build AI products. And that is now being put in the service of a lot of

**[2:30](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=150s)** AI tools and products within Google. Since AlphaGo, I'm pretty sure you've seen all of the changes that has happened in in in AI and has been fueled by Google. Like this has touched every possible aspect, chemistry education agriculture climate change, video games recently with Jenny. Like it's really everywhere and and Google has put their hands in all of these things and really because this is core to their mission of helping humanity everywhere with AI. Now the this has been what led to kind of the moment where they decided to do that merger. Because they they saw like a massive moment in AI that came to us thanks to ChatGPT, which was the fact that we were

**[3:19](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=199s)** able now to do we could be able to do like AI being able to do that is that are able to do anything. And so that's where started this fantastic journey that is Gemini that started two years ago that has started with a first model which was okay and now I think like it's getting into the place where it's it's becoming the absolute best AI model out there. In particular the 2.5 recent release that has come with in three different models, you know, the pro flash and flashlight, but basically kind of all of this knowledge from DeepMind on how to do good research as well as from brain has been kind of put together toward that unique goal. But these things just tell a part of the story just like the the focus point of

**[4:07](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=247s)** Google's strategy in terms of AI, but the reality is that we actually ship at a rate like at massive at massive speed. Like over the last two years we've released all these models. So some of them are Gemini, but others are like VO, Imagen, Gemma of course, Agent Space, Mariners. Like we are releasing models everywhere in every possible domain where we think we can have a breakthrough and then afterwards sometimes we integrate them into Gemini or they become their own product. It's true on the model side, but it's also true on the application side. Like every surface of Google now is completely fueled with AI. Like you've seen recently the AI mode deployment in in Google Search, like Gemini Live of course, Deep Research, VO3 and so on and

**[4:57](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=297s)** so on. Like it's every time we have one of these project that's bubbled from from DeepMind it's now almost automatically put into some kind of product or something like that. It's really leveraging that that muscle that that this this company has been building for the last 10 years to build this this models. And so it's in this ecosystem of model where we try to bring AI wherever we think it's important that we develop Gemma. That's this is why it makes a lot of sense to for us to open models. And that's where I'm going to talk a little bit about Gemma 3 here and this is going to be the focus on the the rest of this talk, but I hope now

**[5:45](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=345s)** you understand why Gemma has a lot of meaning for Google. We are tackling a real ecosystem, the open ecosystem that is pretty big and we try to bring there again AI to help that ecosystem. I mean just in terms of number to give you an idea a sense of how big is this this markets. Since we released Gemma 3, we had more than 300 million downloads. That was in October. Sorry, the slides are from there. I haven't updated the numbers. Probably now more closer to four or 500 millions. And this is just Gemma. So we are not the number one open model. Like we have things like Gwen and so on that are like incredible also and and very popular. That gives you an idea of how important this this ecosystem is and why it makes sense for Google to be in it

**[6:34](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=394s)** and to try to help it help developers build whatever they want with this AI. In this version we added a a lot of new features that we observed were quite popular among the community. The first one was to have a native multimodal model. By that I mean that it can take images in and and and think about them. We also added for some of the model, the smallest one that goes on phone, audio. The reason why we wanted audio on the model that were designed for phone is because a lot of the interaction that we expect people or developers to build within phones may come with

**[7:21](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=441s)** speech. And so we added this multimodal capability where we saw the needs from the developer. We also pushed very hard on the multilinguality with more than 140 languages. I think it's still one of the most popular model when it comes to other languages than English and Chinese even though it's now more than a year old. And the reason for it is again driven by trying to to meet the people who need open models where they are. That is we have seen from previous iteration that more than 80% of our users were outside of the US. Showing important need for for for touching a lot of of languages.

**[8:14](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=494s)** Popular languages as well as rare languages. We also back then added a capacity that now is kind relatively standard but was not as much then which was to have a long context which allows you to upload your documents and reason a little bit about them and so on. And that has also come from the fact that our previous model had small context window and people had a hard time developing apps with only 8K limitations. Everything put together kind of gave us a model that we are able to work in relatively complex scenario. Like here is an example of someone taking a picture of

**[9:02](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=542s)** some sign in a I don't know which country where there is different text in different languages and a user asking question about what's what's in the picture and translating it. Then when it's translated you can continue with a multi-turn fashion to um answer different question. So this is like the latest version we released as I said more than a year ago. Obviously we work on newer version as of now. But on top of that we also try to bring some of the innovation that I think that we think is important to specific communities, sometimes researcher and sometime AI

**[9:49](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=589s)** specialist that are within one domain. And that's why we also have a program in uh within our Gemma uh brand that is uh trying to get uh variants out. Like what I mean by variants is models that are built on top of Gemma but has a very specific uh use case um or that has a very specific architecture uh that is not common uh in the um uh in the uh long uh large language modeling uh community. Uh I'm going to just talk about two of them very rapidly because uh they are quite recent and and popular and I think uh show a little bit the philosophy we have uh behind this this uh um

**[10:36](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=636s)** uh variants. The first one is uh Med-Gemini which is a derivative of Gemini that is very tailored toward uh uh um anything that has to do with uh medical uh uh understanding. It is multimodal so it understands image and and so on and uh and since its release it has been one of the most popular model on uh Google Cloud and the reason is that a lot of people want to use medical models happens to wants open models rather than proprietary one. Um either for privacy reason or because simply they want to build uh their app around it and and they don't want that to be uh uh related to a uh closed model. So this one is a

**[11:25](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=685s)** typical example of where we absolutely need an open model because private data uh even though uh you have guarantees with closed models uh may may put some people uh uh more at ease if they use a open model. The second one is uh one that has been designed to uh work for with sign languages which is called Sign-Gemini. Uh it's focusing mostly on English uh uh at the moment but the goal is over time to also uh extend it to more uh uh um uh sign language than the American one but you have this uh idea that this is something that is uh a very particular case where uh can uh deliver one model for a community uh that is very specific

**[12:18](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=738s)** might be a bit too niche to have that in a you know, more bigger ecosystem but with this type of small models that we can uh easily fine-tune and so on we can bring uh that. This work has been done with specialists in in this domain um and has been uh received very relatively uh extremely good, sorry, uh feedback. Um in general the way we operate is a very community-driven uh uh uh development uh What I mean by that is that every time we do a release or when we plan for the next release we just uh stay in contact and and reach out to the open source community uh through either uh different um social media but just because also we

**[13:05](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=785s)** are very much intertwined with them and ask them what didn't work in the previous version, what do they want to see, where they see usage, why our model uh is less popular than another one and so on. So really try to build not just to make some kind of uh fancy model but also really with the community we are we are serving. And uh another part of of that effort is we have been investing a lot into the deployments. Like we are on a lot of surfaces uh this has been uh quite a massive effort because Google is historically a company that usually is not that embedded with the open ecosystem and so we had to build a whole new relation and so on around

**[13:52](https://www.youtube.com/watch?v=zZBA7Aoumuk&t=832s)** these these tools uh and uh and trust so that we were able to discuss with them and and be able to uh implement uh our model with them and now we are uh basically helping them deploying our models but also improving uh some of these tools. And with that this concludes my talk. Thank you. >> [applause]
