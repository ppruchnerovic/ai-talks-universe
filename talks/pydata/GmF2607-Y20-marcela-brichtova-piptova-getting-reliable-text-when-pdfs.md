---
id: GmF2607-Y20
title: "Marcela Brichtová Piptová - Getting reliable text when PDFs lie and OCR fails (PyData Prague #35)"
slug: marcela-brichtova-piptova-getting-reliable-text-when-pdfs
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Marcela Brichtová Piptová"]
channel: "PyData"
duration_min: 18
published_at: 2026-07-01T15:02:31Z
video_id: GmF2607-Y20
url: https://www.youtube.com/watch?v=GmF2607-Y20
youtube_url: https://www.youtube.com/watch?v=GmF2607-Y20
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Evals, observability & reliability", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Marcela Brichtová Piptová - Getting reliable text when PDFs lie and OCR fails (PyData Prague #35)

**Marcela Brichtová Piptová**

`PyData` · `PyData` · `2026` · `18 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=GmF2607-Y20) · [Conference site](https://pydata.org/)

## Description

Marcela Brichtová Piptová - Getting reliable text when PDFs lie and OCR fails

LLMs need text as an input. So before a model can reason about a document, we have to read the text, a step often treated as the “easy part” or a solved problem. But is it?

In this talk, we will explore the hidden complexities of text extraction. This is especially critical for models like Rossum’s T-LLM, an encoder-only architecture which heavily relies on high-quality input. You will learn why transactional documents are sometimes surprisingly hard for OCR, why you can’t always just copy-paste text from a PDF, and why text extraction is still a topic for Rossum researchers (and our customer support team).

Presented at PyData Prague #35 - Probably unreliable vulnerabilities (26.5.2026 at Aisle)

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*2,535 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=GmF2607-Y20&t=6s)** Hello. My name is Marcela and I work in Rossum as AI research engineer. And today I will tell you something about challenges of text extraction. So in in Rossum we do intelligent document processing with focus on invoices and other transactional documents. And for that here our own transformer model which we call TLM and that stands for transactional large language model. And it's part of our Aurora engine which is here in this super detailed schema. And well how it works. First we read a text. Then we create something we call spatial text which is a data structure capturing all words and

**[0:55](https://www.youtube.com/watch?v=GmF2607-Y20&t=55s)** their positions on the page and that is then the input into transformer model and that's where all of the Aurora magic happens. And one thing you should know about our our TLM is that it's an encoder only model. So it's it's a generative model. We use it only for classification. So it basically tells you this part is address, this part is amount etc. So what it means is that it doesn't suffer from hallucinations. Which is great. It can't predict anything that's not in those in that input. On the other hand um it's like the quality of the text extraction is extra important for us because if

**[1:43](https://www.youtube.com/watch?v=GmF2607-Y20&t=103s)** something is not predicted in that phase, it will never be fixed. It will never be predicted. So that's what I'm going to talk about. And what we do. Rossum supports both images and PDFs. So, if there is PDF with available PDF text layer, we use that. If not, we use OCR, which sounds very simple, right? And I will dig a little bit deeper. And spoiler alert, the tricky part is that if available Uh but first disclaimer, I wanted to show you a lot of funny examples, but Uh those come from our support tickets and I'm not allowed uh well, naturally, to show you any customer data. So, I just made my I did my best to

**[2:34](https://www.youtube.com/watch?v=GmF2607-Y20&t=154s)** like re- recreate them in a way that it still captures the the essence, but I'm not showing you something that I'm not supposed to. So, all of those examples are a bit fake, but I will just pretend that those are real and they are very close. Trust me. Um Uh I will start with OCR. And we um we had our own OCR solution, but we needed to support other languages and script like Japanese, Chinese, etc. So, we decided for third-party OCR, which also supports handwriting and vertical text, which is amazing. So, we just went with went with it. And um last year, we spent over a month trying to improve our PDF processing pipeline.

**[3:24](https://www.youtube.com/watch?v=GmF2607-Y20&t=204s)** And I've been asked a lot if it's even necessary if that OCR is so great, we can just like ignore PDFs and use OCR everywhere. Um so, the question was basically, is OCR solved? Is it Is it good enough? And um we will try to answer these questions together now. Um so, this is the first example. Uh here, the OCR just ignored that part of that handwritten text which is there. It read only the first and the last digit. Uh which might be a uh well, not ideal. Uh but well, to be fair uh it's handwritten text. It's sometimes hard for humans to read that. Uh so and there's no PDF text layer anyway. So, maybe that's like Okay, maybe OCR is

**[4:15](https://www.youtube.com/watch?v=GmF2607-Y20&t=255s)** good enough at least for printed text. And uh well, let me let me explain what you're looking at because I had to erase all those all of those words. So, uh those blue rectangles are detected words which our uh OCR detected. And uh the red ones are those that are there but were ignored. And the issue is here is that those documents have uh large diagonal watermarks which are very very problematic for some reason. Well, it's overlapping text so it kind of makes sense. Uh in the left case uh it got so confused that the uh well the that line is like really warped and some words were completely ignored. On the right side, uh amount was ignored which also might be problematic. Uh

**[5:03](https://www.youtube.com/watch?v=GmF2607-Y20&t=303s)** so but those are overlapping words which is probably hard to. So, okay, maybe OCR is good enough at least for printed text with no overlapping words. Uh and here is represented This is actually very common issue and uh that is uh words with single um sing- uh text with uh single characters, single digit or single letter are often ignored and that's extra prominent in uh tables which those uh columns with all zeros for example. Uh so, they are not detected at all. They are just missing and as I already mentioned uh we cannot fix that later. They are just gone forever. Um Okay, so maybe OCR is good enough at least for printed text with no

**[5:49](https://www.youtube.com/watch?v=GmF2607-Y20&t=349s)** overlapping words and no tables. Uh and there is another example. Uh this is this is funny to me because uh the OCR that we use uh kind of prefers consistency and has issues with reading uh words which are mixing letters and digits like here. This one, it's nice one, but it it's between D and C, so it was read as I. And below it, it's U uh but it's between one and seven, so it was read as O. And uh those those texts are kind of rare in like real world, but in documents that we we process, those are uh really common, so this is a big issue. So maybe OCR is good enough at least for

**[6:38](https://www.youtube.com/watch?v=GmF2607-Y20&t=398s)** printed text with no overlapping words and no tables and no codes mixing letters and numbers. And I I guess you can already see where I'm going here, so uh uh to be fair, uh those examples were uh cherry-picked. Those are quite rare in general in the sea of documents that we process. Uh so maybe we don't need to care too much because we don't expect 100% accuracy from machine learning models, so we expect that there there are some mistakes always, right? Um but unfortunately unfortunately, we really need to care because even though uh these issues are kind of rare in general, uh there might be uh customers which process one

**[7:26](https://www.youtube.com/watch?v=GmF2607-Y20&t=446s)** type of documents and that error is always present there, so that's a bad for them and so so we should they care, so we should care, too. Um So the answer to the question is OCR solved is not for us yet, unfortunately. But as I already mentioned, uh we process PDFs also, so we can uh we can use that PDF text layer, which is there. Um But the the issue with PDF is that it was uh made originally for printing and it rendering of the document. It basically contains just instructions for for rendering. Uh and you know that you can select the text and copy paste it, but the text that you copy paste doesn't have to

**[8:13](https://www.youtube.com/watch?v=GmF2607-Y20&t=493s)** correspond to the thing that you see rendered. Uh which is wild. Why would anyone do that? Uh well, uh I don't I don't know, but uh it turns out that you can even play Doom in PDF. Uh and that's the issue. Uh it's it's too it's too powerful. It can do so many things and everything is possible. And if everything is possible and you process millions of documents, you will see some weird things and I will show you some of them. Um This is the first example from one support ticket. Uh I really like this one. Uh yes, this is PDF text. This We didn't run any OCR on this and those those blue letters are what what

**[9:03](https://www.youtube.com/watch?v=GmF2607-Y20&t=543s)** it says that is what what is in the PDF text layer. Um and uh What happened here? Uh well, you probably can see that it doesn't look like nice digitally born PDF. It like it looks like it was printed and then scanned again. And that's exactly what happened. And it was scanned probably with some scanner with uh some amazing OCR feature, which created that PDF text layer for it. And what happened here is that it was scanned upside down. Uh and that OCR didn't recognize it. So, that's the first common source of errors in in in PDFs is that it was uh it's from the source which is not uh which we don't want

**[9:53](https://www.youtube.com/watch?v=GmF2607-Y20&t=593s)** don't want to trust. Um, we have better OCR, so we want to use our OCR and not not that. Uh, that's the first issue. Uh, yeah. Another one is some kind of broken encoding. Uh, you um that's what I already talked about. It's um uh that happens when uh the text that is there in that PDF text layer doesn't correspond to the thing that you see see rendered. And sometimes it happens only for some characters like uh accents, which you can see in the first example. Sometimes the whole text is just wrong. Um Another issue is invisible text. Uh, some sometimes someone wants to uh

**[10:42](https://www.youtube.com/watch?v=GmF2607-Y20&t=642s)** add some extra information, some meta metadata uh to the PDF. And uh the best way apparently is to put it there as invisible text. Uh, which causes some issues for us. Uh, and actually you can you can detect invisible text in PDF. It's possible. But uh in this case, what mostly happens is that it's for example white text on white background, so it's not truly invisible. And that's uh that's harder. Um And then you can have for example incorrect reading order. All the words are there, but uh uh ordered incorrectly, uh which is not a big issue. We can fix that. And uh lastly, this is the most common one, and that's that uh the

**[11:31](https://www.youtube.com/watch?v=GmF2607-Y20&t=691s)** bounding boxes are uh are bad. The text is all right, um but the position, which is like in that PDF text layer, um is not correct. It can be The first example is is correct. This is nice. This is what we want. But it can be shifted. It can be too small like the third example or it can be too large and that's worse for us because it can be overlapping with other text that's on the page and that's causing a lot of issues. Um then I have some examples of less common issues. And after more than 4 years, I in Rossum, I'm still sometimes surprised by a creative ways ways to create broken PDFs.

**[12:21](https://www.youtube.com/watch?v=GmF2607-Y20&t=741s)** Uh you can have text outside the page uh with like negative coordinates um something like that for some reason. It's possible. Um you can have like the text the page can be rotated, but the text is not. Just the the rotation of the text doesn't have to correspond to the rotation of the page. Uh and then my favorite one uh it's it's not too common, but but uh uh uh sometimes it happens that someone wants to write text in bold and apparently the best way to create bold text is just to uh duplicate it and shift it a bit little so it looks like it looks bold, but and it's um it's kind of similar to the way you

**[13:10](https://www.youtube.com/watch?v=GmF2607-Y20&t=790s)** would create bold text on old typewriters. Maybe that's the inspiration for that. And another thing, the last one, uh mixing fonts in one word. Uh that happens with sometimes capital letter is with different font or different size or letters with accents are different font. And the processing Python processing libraries that we use for to read that PDF text just read it as different words. Like like it doesn't belong together, so some post processing is needed. And it's annoying. Um Okay so I already mentioned that we kind of use both as we decided we want to use PDF or OCR

**[13:58](https://www.youtube.com/watch?v=GmF2607-Y20&t=838s)** and that wasn't entirely true. Actually, we combine those two in most cases. So first we have to somehow decide if we can trust the PDF. Um We do it in few different ways. It's nothing super sophis- sophisticated. Um Then we com- we we always run the OCR and we compare the the output of the OCR and of the PDF text. And we kind of uh-huh >> With the with this classification whether to use PDF or text extraction, is there any Are you using also the metadata because sometimes the creator the metadata gives you the good hint that it could be trusted or not?

**[14:46](https://www.youtube.com/watch?v=GmF2607-Y20&t=886s)** >> Uh yes, that's what we used to use and it always there there were always some holes in that. Like we we thought that we have it and then a document came and it didn't work. Uh so we can uh we we used the metadata for that. And then what happened is okay, this producer, which is in met- metadata or creator, produces broken PDFs, so we will put it into blacklist and always OCR for it. So we had like this long blacklist of producer and wasn't ideal. So what works for us is that we compare the PDF text to the output of OCR and we assume that OCR can be a bit wrong, but not completely completely wrong. So, if those texts are

**[15:35](https://www.youtube.com/watch?v=GmF2607-Y20&t=935s)** a bit little bit different, we assume that OCR made some error. And if they are completely different, we assume that it's the PDF that is broken and that usually works very well. No, it's not 100%, but it's better than any solution that we had in past. And then we do some other things like I mentioned that invisible text or bad bounding boxes and what that causes is that there are some overlapping words, which is like weird for us. It's probably wrong. So, and we don't know which one we want to keep and which one we wanted to throw away. So, we remove everything that every like both overlapping words and just let OCR fill the gaps.

**[16:24](https://www.youtube.com/watch?v=GmF2607-Y20&t=984s)** And that's also useful for like PDFs can contain some embedded images like often headers or footers don't contain any any PDF text. It's just image. So, OCR can read those and we combine that together and get something like we we hope it's better than OCR pure OCR or pure pure PDF. So, what I'd like to like I'd like you to take away from this presentation. First, don't trust your PDFs blindly if you don't know the source. And second, please please don't create broken PDFs.

**[17:12](https://www.youtube.com/watch?v=GmF2607-Y20&t=1032s)** And I'd like to end with this image which is from one support ticket where in this case rendering was broken because we some fonts were probably missing and just whole page was filled with A's and it looks like the document is screaming for help and I can relate to that because that's how I often feel when I'm dealing with all support tickets. And that's all from me. Thank you for your attention. I'm >> [applause]
