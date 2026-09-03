---
id: MnPHMweTp-E
title: "From Voice to Data: Designing Real-Time Pipelines on Top of Scraped Sources"
slug: from-voice-to-data-designing-real-time-pipelines-on-top-of
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 24
published_at: 2026-08-23T07:00:31Z
video_id: MnPHMweTp-E
url: https://www.youtube.com/watch?v=MnPHMweTp-E
youtube_url: https://www.youtube.com/watch?v=MnPHMweTp-E
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science"]
transcript: true
---

# From Voice to Data: Designing Real-Time Pipelines on Top of Scraped Sources

**Speaker not identified**

`PyData` · `PyData` · `2026` · `24 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=MnPHMweTp-E) · [Conference site](https://pydata.org/)

## Description

Welcome to the PyData & PyCon Yerevan 2026 video collection - our biggest edition yet, held on 24-25 July in Yerevan, Armenia.

From data science and machine learning to Python tooling, production systems, research, and open-source technologies, these recordings capture the ideas, experiences, and practical knowledge shared on stage.

🌐 Website: https://pydata.am

📅 24-25 July 2026 · Yerevan, Armenia

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*2,667 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=MnPHMweTp-E&t=5s)** Um so, the main project that we are working on and I have a process is making voice assistant. Um there are so many times that we just searched in the ChatGPT or maybe other LLM agents to know some real-time data. For example, the thing that I have mostly worked on is searching about apartments and knowing which one is available now, which um price range does they have, and how many rooms there are, and which one is more appropriate for my uh special willingness. Um Hello everyone who is coming just now. Um

**[0:56](https://www.youtube.com/watch?v=MnPHMweTp-E&t=56s)** okay, I'll continue. Uh so, ChatGPT maybe give you an answer, but you cannot rely on it on it because it may because it may not be uh precise because the data is go is always live and changing. Maybe the availability has changed or the price changed. Uh so, um we constructed a pipeline where the data is being scraped over time to be always up to date and we can rely on it and to know every uh special attribute that we need for booking one. Uh for example, I need to know um apartment which is under $900

**[1:45](https://www.youtube.com/watch?v=MnPHMweTp-E&t=105s)** and um has two two bedrooms. Uh so, the user sees only asking the voice assistant and the system retrieves the information and gives an answer. What What is under the hood? Anyone doesn't know. So, I'll try to explain it how it works and what are the parts of it. So, as I told, the problems may be because the data is dynamic. It change. It's inconsistent in different websites and structures are different. They have different HTMLs, GS renderings, and spread across the website and it makes sometimes very

**[2:37](https://www.youtube.com/watch?v=MnPHMweTp-E&t=157s)** difficult to scrape even if even if the data is available in the HTML. You have to be aware to change the sources time by time. For example, what I mean that for one website, you might need a scraper a a system doing a scraper, for example, Apify. Then, you might see that it's not working for this one and you have to have a fallback system, another scraping doing a system that will make the this all thing right to not lose the information coming from that website. And afterwards, you have to store it in the database or

**[3:26](https://www.youtube.com/watch?v=MnPHMweTp-E&t=206s)** The first The first option that we were doing is a storing it in the database, validating it before storing to have the good schema and structure of the tables and database so that afterwards, the data retrieval, the data searching, and other processes will be easy and will not take uh more time and will be very optimized. So, the system's architecture is drawn there. It's first first the voice input coming from the user. Then it goes through the STT, which is speech-to-text transcript.

**[4:15](https://www.youtube.com/watch?v=MnPHMweTp-E&t=255s)** There are different models to do STT. Um To have an optimized way of working, we have tried to use different STTs and to check which one is much which one is quicker, which one gives more reliability, and which one has less latency because these are the two main things that we we want to have in a good uh state. The latent low latency and good and good reali- reliability. What I mean when I say that I want my name is is Sara Bennett. I don't want it to read um I don't know to read Sara Benedict.

**[5:04](https://www.youtube.com/watch?v=MnPHMweTp-E&t=304s)** Benedict is my favorite breakfast. I remembered it. Um so, this is very essential because we want to get the authentication right because we also considered the part of authentication very uh we put a lot of attention on it because I don't want want another person to know which apartments or maybe what businesses I own in some other business uh or some other things that are very personal because I believe that for users the uh and the security is very essential. So, that afterwards uh it may be took a lot of longer, but the second part is LLM

**[5:55](https://www.youtube.com/watch?v=MnPHMweTp-E&t=355s)** reason. So, we attach an LLM to eat because just what that comes after STT is just a text, a text that user gave us. Maybe also it understood a little bit wrong, a little bit um he he left a little gaps and LLM should understand it uh should understand that I want 2,000 dollar apartment is mean that I want to pay monthly for apartment so much money. So, for understanding what I the user said, we need LLM. Also, we can give the LLM schema and structure to give in that way the data. So, afterwards we might not

**[6:44](https://www.youtube.com/watch?v=MnPHMweTp-E&t=404s)** need it going over that data to put in some JSON type. Afterwards, we come the again plan. Agent is not something um just LLM and functions called on it. He should decide which function at this time he needs to call for executing the understanding of you what user said. Maybe there might be a chance that we need a live data. So, we going to need retrieving the information from the website and we might need to attach an OpenAI web search to it to go through a website and extract the information real time.

**[7:35](https://www.youtube.com/watch?v=MnPHMweTp-E&t=455s)** That's um mostly about the scraping pipeline that I have just told and um then comes the validation before giving an answer to user because again the JSON type is not that we are going to uh put into the TTS which is text-to-speech. So, the main So, the data we uh have at this point after LLM format is the text which again needs to be uh converse to the speech again through some models. The models may be Deepgram or 11 Labs.

**[8:23](https://www.youtube.com/watch?v=MnPHMweTp-E&t=503s)** These are the main models that LifeKit supports. LifeKit is a system that uh uh gives a lot of opportunities to make a voice assistant. Through LifeKit, you could given a call uh that is inbound calls and then receive outbound calls that is when the assistant calls to your phone. Like isn't it amazing that an assistant can call you exactly on the time when your payment is coming to the end and the same deadline that you have mentioned before and there is no human working and that is there is no human error that no one that someone couldn't

**[9:14](https://www.youtube.com/watch?v=MnPHMweTp-E&t=554s)** call you or uh they forgot just you No, no one can forget if you are using voice assistant. So um uh after LLM reasoning that comes an answer and live data is external. So, the backend is essential part to connecting or today's data with the models used. >> [sighs] >> We need to control the data going over and over. There are budget states, locations uh and we have to carry the state between um changing data. Also, there are policies

**[10:05](https://www.youtube.com/watch?v=MnPHMweTp-E&t=605s)** may related to the to the business. >> [sighs] >> And we should have a failure awareness and our pipeline when working and sometimes he can fail. We should know what kind of failures they might be to uh to stand them. For every failure uh for every failure uh uh option, we need to know how to solve how to solve that. >> [gasps] >> Uh all right. How to stand How to stand this? So, as I have told, if a scraper system, for example, um

**[10:57](https://www.youtube.com/watch?v=MnPHMweTp-E&t=657s)** if I is not working, I have found another scraping system that is Zen rows. He has its MCP um very good working compatibility with this whole pipeline or about STT or TTS or LLM models. There are a lot of models that we can try and after one model is not working, we have we could have a try exact block, for example, and try another another option for um converting one type of data to another. Um also, when the data is not available in the database by the by the current user wants such kind of apartment exactly for from a these apartment

**[11:46](https://www.youtube.com/watch?v=MnPHMweTp-E&t=706s)** building, we can go and use the Open AI web search when we see that it is not available in the database. >> [sighs] >> Uh also, why I spoke about the Apify and ZenRows differences, maybe Apify uh some of you know about Apify's scrapers or actors that go and do Google search or other very convenient things, but uh sometimes it lacks the opportunity to scrape because the website has a very strong um human identifying or uh the uh JS rendering may makes a lot of troubles, the captures, and other things. There is why ZenRows became my

**[12:36](https://www.youtube.com/watch?v=MnPHMweTp-E&t=756s)** favorite one. Uh he uh goes um he overcomes it overcomes very easily. Uh so, we should know a lot of uh different ways to solve the same same problem. Um okay. Well, uh the traditional extraction of data from some websites where uh like a CSS selectors, HTML scraping, just I have mentioned. Uh and the other other types like DOM uh specific rules, but uh when the data goes uh very inconsistent, the DOM rules um uh might even uh uh

**[13:24](https://www.youtube.com/watch?v=MnPHMweTp-E&t=804s)** um make uh harm to a data extraction pipeline. And on the other hand, LLM assisted extraction has a semantic understanding, adaptable extraction. So, from the HTML, he could easily find the necessary information by uh checking the dollar symbols or or other things under the hood to find the necessary type of attributes. But, there is also a downgrade. He can LLM can hallucinate or give invalid fields. And sometimes there goes another problem. It's the cost-effectiveness and the time

**[14:11](https://www.youtube.com/watch?v=MnPHMweTp-E&t=851s)** the time that we don't have a lot. So, we need need to optimize it. And optimization comes with a lot a lot of ways. For example, parallel parallelizing earlier. We don't need to wait until the STT is totally and fully finished to start the LLM reasoning. When the first important and the first ready sentence is Why don't you tell told it earlier? Okay.

**[15:00](https://www.youtube.com/watch?v=MnPHMweTp-E&t=900s)** >> [laughter] >> Optimization STT should be done not fully and the reasoning should come until the STT ends. And same for TTS. When the first reasoning formatted text is already, it should go already. Um, at the should transform the text to to the speech and uh other optimization techniques as well. The one that I came that the one that came to my mind is using some pre cached um uh sentences, for example, "Hello, how can I help you?" or something like that to be pre-reserved so that the um LLM will not uh put

**[15:50](https://www.youtube.com/watch?v=MnPHMweTp-E&t=950s)** over time on thinking on it and the TTS will um will work on it very quickly. And also when the user interrupts the voice assistant, it should stop the generating, the reasoning, and other processes because the information might be changed after the user's new words and we do not need the uh the same uh text that the LLM was about to generate. It should be very aware to interruptions, to listen to the new sentences, and uh try to uh generate on it. Um, I might be going a little bit out of time but but that's all uh I wanted to

**[16:39](https://www.youtube.com/watch?v=MnPHMweTp-E&t=999s)** introduce and tell about voice assistants and how I have uh created it. Um, if there are some questions, I would be happy to answer that. Yes. >> Um, uh so I have two questions. Uh first uh you when you are telling about extractions of the materials from a scrap data with LLMs, there is a problem that there are a lot of hidden text in that page and it's used two kinds as an input you can be sent it to the LLM and it's make it more expensive for us to use. So,

**[17:28](https://www.youtube.com/watch?v=MnPHMweTp-E&t=1048s)** how we can make a balance between that your situation your um >> Yes, I >> procedures and the traditional ways and how we can customize the cost. It's my first questions and one question. >> Um the first thing that comes to my mind if there are not where thousands of website that you need to scrape. Sometimes you need to be aware what type of website it is. Maybe you could scrape or extract the information just using the classical ways like beautiful soup or some other type of scrapers when the information you know that it is hidden in inside some specific tags and

**[18:19](https://www.youtube.com/watch?v=MnPHMweTp-E&t=1099s)** not spread like over this HTML. Or other technique when you want to use only LLM, you could make slices and um um to give only the part of the HTML that you need know for sure that information is inside it. >> Okay. Uh thank you for the presentation. According to your evaluation, what is the best speech-to-text model for Armenian language? >> Um I guess for Armenian language mainly I could speak about the models that came from the podcast or now it is

**[19:11](https://www.youtube.com/watch?v=MnPHMweTp-E&t=1151s)** its name is async. My main work was done with English languages and um uh for English English language, if I can recall it correctly, uh it's a um um Cartesian, I guess. Thank you. >> Uh hi, thank you for your speech. So, actually, I have a question. >> Speak up a little bit. >> Louder. Uh have you ever measured the latency of this pipeline? So, and actually, have you ever tried like multimodal model multimodal models uh to replace this pipeline from um voice query to the uh speech query and

**[20:03](https://www.youtube.com/watch?v=MnPHMweTp-E&t=1203s)** as output? >> Um the first question, rather whether I tried checked the latency, yes, every time in every running uh because that is the main evaluation technique that we understand I understand where is the bad part come the the heaviest latency coming from and for example, it is if it is from STT to LLM, I've thought about changing either that pipeline or the main model itself about rather if I um uh we used a multi model models. Uh um I get Yes, yes, we used it. We tried that. And um

**[20:53](https://www.youtube.com/watch?v=MnPHMweTp-E&t=1253s)** the best approach was that mainly. >> So, what's the average latency? >> Um >> [sighs and gasps] >> Um different different um um, parts of the pipeline were very much different. I can give you the exact numbers afterwards if you are interested in. It depends on um, what user mainly asked for. If it is the cached information uh, or it is just something that the voice assistant doesn't need to go and search for the database, those answers were quicker. Oh, by the way, I would be happy to

**[21:44](https://www.youtube.com/watch?v=MnPHMweTp-E&t=1304s)** connect you via LinkedIn. That's and the QR code of my LinkedIn page. >> If you don't mind, the second question. >> Yes, sure. >> Another question is I had that uh, generating the uh, text and sending to a STT it's a time-consuming. So, do you test that making a buffer for text uh, generation uh, streaming send it while generating this audio while LLMs are still generating the text? For example, uh, LLMs try to make a four five sentences together and you send the first sentence to TTS and later second sentence and uh, somehow buffering the audio and after

**[22:36](https://www.youtube.com/watch?v=MnPHMweTp-E&t=1356s)** the generations uh, finished, uh, play it for the user. Make it more real time. Do you test the this approach? >> Oh, yes. I guess I I thought I have talked about it not to wait the full uh, response to be received from one model to give it to another model to uh, get the real-time uh, approach. Uh, so when the first sentence from a user is kept it is directly given to LLM the same way way when the first ready text give to a user like the first meaning full sentence is received from the LLM it is directly given to the TTS to receive the real time ness. Thank you.

**[23:36](https://www.youtube.com/watch?v=MnPHMweTp-E&t=1416s)** Thank you. >> [applause]
