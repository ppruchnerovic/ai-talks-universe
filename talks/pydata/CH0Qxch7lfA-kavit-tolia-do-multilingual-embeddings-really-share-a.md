---
id: CH0Qxch7lfA
title: "Kavit Tolia - Do Multilingual Embeddings Really Share a Semantic Space? | Pydata London 26"
slug: kavit-tolia-do-multilingual-embeddings-really-share-a
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Kavit Tolia"]
channel: "PyData"
duration_min: 23
published_at: 2026-06-15T15:51:00Z
video_id: CH0Qxch7lfA
url: https://www.youtube.com/watch?v=CH0Qxch7lfA
youtube_url: https://www.youtube.com/watch?v=CH0Qxch7lfA
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: true
---

# Kavit Tolia - Do Multilingual Embeddings Really Share a Semantic Space? | Pydata London 26

**Kavit Tolia**

`PyData` · `PyData` · `2026` · `23 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=CH0Qxch7lfA) · [Conference site](https://pydata.org/)

## Description

Kavit Tolia - Do Multilingual Embeddings Really Share a Semantic Space? Practical Lessons Across Scripts and Languages

Multilingual embeddings are often assumed to place different languages into a shared semantic space. In practice, that alignment breaks down in systematic ways.

This talk explores where multilingual embeddings work, where they fail, and why. Using examples across multiple languages, I show how tokenisation, training data imbalance, and semantic ambiguity shape embedding behaviour in practice, along with practical diagnostics for evaluating multilingual embeddings.

Multilingual embedding models are widely used in retrieval, search, recommendation, and RAG pipelines under the assumption that semantically similar text across languages occupies a shared embedding space.

This talk examines how true that assumption is in practice.

Using pre-trained multilingual embedding models, I explore examples where multilingual alignment works extremely well, and others where it breaks down unexpectedly. Across multiple languages, we will look at how tokenisation, training data imbalance, and semantic ambiguity shape embedding geometry and retrieval behaviour.

Rather than focusing on benchmark performance, the talk emphasises intuition and failure analysis:
- Why do some languages align much more reliably than others?
- Why do averages often hide important multilingual failures?
- What happens when semantic ambiguity enters the embedding space?

Through UMAP projections, nearest-neighbour analyses, tokenisation patterns, and translation similarity distributions, we will build a practical mental model for understanding multilingual embeddings beyond the assumption of “one shared semantic space.”

The talk concludes with concrete diagnostics practitioners can use, along with common failure modes to watch for in applications.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*3,200 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=2s)** Hello everyone. Um, so today I'm going to talk about multilingual embeddings and the semantic alignment that a lot of people assume when it comes to these embeddings. And the key question that I'm going to try and answer is if we put many of these languages into one vector space, do the meanings actually line up to what we think? And the answer is mostly yes, but not evenly. And the interesting failures are not obvious from things like average metrics. So what we'll do is we'll use small examples first and then we'll try and scale up to language level patterns. Now

**[0:53](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=53s)** humans are you know very good with handling ambiguity right the same word can mean different things depending on the context. When I say I went to the bank almost everyone knows I went to the financial institution not the river bank. Um and we resolve this automatically. There's no kind of thought process that happens. Um or not implicit explicit thought process that happens. Flat sometimes can mean an apartment, sometimes can mean a flat tire, sometimes it's a musical note, but we know what it means depending on the context that it's being used in. So the meaning isn't fixed inside the word itself, but it's dependent on the usage. But the problem is that when we embed these things for machines, you have to

**[1:42](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=102s)** turn all of these things into numbers. And what does kind of first let's talk about how machines actually look at words, right? Because they don't think about words in the same way. When we see the word dog, we automatically think about the animal, a pet, maybe our own dog. But machines don't do that. They obviously they they essentially turn that word into a list of numbers that becomes a vector, an n- dimensional vector. And the assumption here is that that vector has that meaning associated to the word that we're seeing. And once we've converted,

**[2:35](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=155s)** you know, a word into vectors, then language isn't necessarily about text. It actually becomes about geometry. And if the embeddings work as expected, what you would like to see is words that are similar to each other living in the same kind of region and well, words that aren't living far apart. And because you've converted everything into vectors, you can actually now start mathematically thinking about how far away is dog from cat or how far away is dog from car, you know, and these are things that you necessarily don't think about when you think about human languages. But that's essentially what an embedding

**[3:22](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=202s)** is. So I wanted to get that out of the way before we start talking about multilingual embeddings. So this is a projection of the embedding space for different languages using um so obviously we're compressing a lot of information. We're going from something like 400 dimensions to just two here. But the important thing is that visually this space looks fairly shared. You know there's no different languages don't seem to cluster differently. What we're seeing here is it looks like things are looking as expected. And if that's true, then the translations should also land near each other when we think about translating a concept from

**[4:12](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=252s)** langu one language to another. But you might ask, you know, that's all fairly interesting, but why do multilingual embeddings even matter? And they matter because they these embeddings now sit beneath you know real production systems. You've got a user querying something in Arabic which gets embedded compared to a vector database and then things get retrieved in other languages like English, Spanish, Hindi whatever it might be right and the system here assumes that language is no longer a barrier. Right? So if alignment breaks then the quality of this retrieval becomes dependent on the

**[5:02](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=302s)** language that the user is using and the dangerous part is that these failures if and when they happen will be silent right the system is not going to crash the quality of the retrieval will just start degrading. So let's maybe start with a very simple example. So let's take the word dog. So these are the nearest neighbors of dog in the embedding space. And there's no surprises here. You know, it looks very reasonable. You've got the Spanish, German, French, Hindi, and Arabic word for dog here. Um, and this is exactly what we want, right? We we've got the same concept being very close to

**[5:50](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=350s)** the same concept in other languages and they're all in the same neighborhood as well. And if if every example looked like this, then multilingual retrieval would be easy. That would be a dream. But obviously, not every concept looks as simple as this, right? And now I'm going to stretch the uh concept of language a bit and talk about the fire emoji. So this is the nearest neighbors for the fire emoji, right? Uh the first one kind of makes sense. Yes, excellent. You know, that's um in internet usage. It it is often used for excellent or impressive or intense. But then we've got these Sanskrit words, right? These aren't Hindi by the These

**[6:37](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=397s)** are Sanskrit which is the Indian equivalent of Latin for for and fish and dog and very funny um very funny maybe I can get but for fish and dog are largely irrelevant to what we're trying to do here. So this kind of becomes a bit more serious because the issue isn't just that the neighbors look very strange. It's that these similarity scores are then being used to determine rankings when it comes to retrieval. And in the fire case right you the system may start retrieving unrelated content and this kind of becomes a silent failure as I mentioned. And what happens is the user just starts getting lower quality results and the

**[7:26](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=446s)** system still looks completely functional. And this is why multilingual embeddings start going from a geometry issue to a kind of productions and systems one. But let's even make it a bit more concrete. Right? So I've built a very tiny retrieval system here. So you enter a query gets embedded. I've got a few documents that I generated myself and then I'm ranking the retrieval by their similarity. So if this kind of works as expected, what you would see is the documents that get retrieved are very much linked to the query that you've got. So in this case, the query is the Spanish for dog and the documents the first two documents that get retrieved with a very high similarity score are related to

**[8:14](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=494s)** dog. So that's that's a good thing, right? So this is the kind of promise that you have from multilingual embeddings and it's genuinely powerful, right? You've got things that are happening in two different languages and they're somehow working very well. But then let's talk about the fire emoji. And you can see you've got the kind of the joke is funny. I actually was looking for a fire document which comes number four with a very low similarity score. But you've got, you know, joke is funny, product is excellent. Again, you can kind of see number three where it says number four becomes before number three and that's even before the fire document is very odd. And you know the the kind the key here is that the relevant documents go down

**[9:05](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=545s)** and the more relevant ones come up in the ranking. And again, they're they're, you know, silent failures, like I said. But why why is it so so different for the two different concepts? I think dog is a relatively concrete example, right? Across languages, it means one thing. There might be linguistic differences, but there's no there's no ambiguity there. Whereas with the fire emoji, there's there is genuine ambiguity. So it can mean literal fire, it can mean excellent, it can mean funny, can mean attractive, dangerous, whatever. You know, it's it's being used in a lot of different ways on the internet. And this ambiguity is what

**[9:54](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=594s)** creates unstable neighborhoods. And which is why we're seeing this retrieval coming up with completely unrelated topics. And the next question is kind of is this random or language dependent? Because you might say, well, maybe the fire emoji is an edge case. You know, no one's ever going to no user is going to enter a fire emoji into a retrieval system. And that is that is possible. But the more important question is whether the kind of failures are evenly distributed and do all languages behave similarly, right? Because if some languages are more stable than others, then that leads to this same problem. And we can test this out systematically. Right? So now we've got the same kind of projection that we had before, but now

**[10:44](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=644s)** we're looking for something else. Now we're trying to see if these different languages are uneven. And you can actually see English and Arabic are fairly similar. Uh Sanskrit is a bit more compact. and emoji is just its own little thing, right? There's there's something very odd going on there, which is kind of understandable. So, the kind of space is shared, but it's not uniformly distributed. But these kind of projections are helpful, but they do compress a lot of information into a two-dimensional chart. So, we kind of want something a bit more quantitative, right? So what we've got here is I'm measuring a similarity for different

**[11:32](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=692s)** concepts against English. So take a concept translate it to all of these different languages. So we've got French, Spanish, German, Hindi, Arabic, Sanskrit, which was hard to translate by the way, and emoji. Uh so we've got these box plots and you can see that the medians are actually quite high across all of these most of these languages right and that means that the model often works but the spread here matters quite a lot you've got quite you've got quite a few at the bottom there for some of the European languages as well and the emoji one is clearly just, you know, very

**[12:22](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=742s)** very much lower and less stable. And the Sunscript one is quite wide to be fair. But the median looks good. And if we just looked at the median, then we would miss all of the tail behavior that we're seeing here. And this is why, you know, things like averages can mislead us. So if you know if this was a benchmarking exercise, I might show this chart where I show the average similarity between translations across all of these different languages and it looks pretty good, right? I mean for most of these apart from Sanskrit and emoji, it's kind of 8 thereabouts and that single number is compressing a lot of information that we're seeing here. So

**[13:10](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=790s)** in production, these tail failures are what's going to matter rather than the average similarity that we're seeing here. So if let's talk about maybe what does alignment even mean between these languages, right? So good alignment here is talking about translations clustering together, but also making sure that neighbors in one language remain neighbors in another language as well. And those two together is what's going to let retrieval behave in a predictable manner. And on the in contrast, you know, bad alignment is essentially the opposite. You've got kind of unrelated concepts colliding like we saw before. um the neighborhoods start changing or drifting depending on

**[13:58](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=838s)** the language that you're seeing uh and that causes the retrieval to become unreliable as well. So for the toy data set that I created so this was um this was in all of these languages I created something like 75 concepts. What I wanted to see was what concepts actually strongly align and which ones don't. So before I did any analysis, I kind of was expecting something like this, right? So the concepts that are concrete like dog, cat, sun, moon, they should align well. Whereas concept that concepts that are a bit more uh abstract like love and freedom and justice and democracy, they might end up

**[14:48](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=888s)** start drifting away from each other. So this is what I expected to see but not that's not exactly what I observed. So this are these are the concepts that are that align strongly across all of the languages. And actually one thing I missed was numbers right? So numbers are going to align very well across languages because they are very concrete. But there are things in here that I didn't expect like fear or happy for example. Whereas when we think about the concepts that are hardest to align, that also surprised me because you see things like cat here and you see bread, you know, bird, whatever it might be.

**[15:37](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=937s)** And some of these come from ambiguity and we'll go through one of these. um some come from translation differences, some come from tokenization and there'll also be a bit of training data imbalance here as well. So let's try and zoom in on one example and let's try and look at flat tire. So which was by the way the le the weakest aligned concept. So flat tire the nearest neighbors of flat tire you can see here the first three make sense they're flat tire in French Hindi and German but then the last two are essentially just flat or apartment in English or in Spanish so this isn't a kind of simple

**[16:26](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=986s)** translation set anymore right we have kind of this ambiguity entering through the English concept label that we're using. So, and this type of failure is not evenly distributed, right? You've got a kind of the patterns are uneven. The concepts differ and then the languages differ and the failures differ because of that and a single overall score is just not going to be able to show this kind of detail. Um and to debug properly, you know, we need kind of examples, language slices, um distributional views, otherwise we kind of only see the average and miss miss the kind of behavior that affects the user. And kind of one reason for this

**[17:15](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=1035s)** unevenness as well is, you know, like I said, models don't see words the way we do. So when I said before that you know models or machines turn words into vectors. So an oversimplification you know it turns it into subwords and then it turns those subwords into vectors. Um those subwords here being tokens and you can see here that kind of English and Spanish are very compact. Most of them are one-word tokens. Um, Hindi and Sanskrit often get broken into more pieces and emoji again is just handled a bit inconsistently. And this means that you know the more pieces you have the mo the model then

**[18:05](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=1085s)** has to compose meaning from these smaller fragments and that makes embeddings noisier and less stable. uh when it comes to higher uh higher token languages um but maybe let's even take an example right let's talk about dog again and you can see here you know dog in English is one token dog in Spanish becomes two tokens dog in Sanskrit becomes three and dog in emoji is two tokens as well and what we're seeing here is that even before the model sees the vectors or the concept, it's already coming in different ways depending on the language

**[18:54](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=1134s)** that we're using here. But you know, tokenization is kind of only part of the story. So you've also got kind of training data imbalance to talk about because these models are essentially trained on internet scale text and internet text is not evenly distributed between different languages. Um here what I've got is the number of Wikipedia articles by each of these language. Uh obviously English dominates, European languages are up there as well. Uh Hindi and Arabic are small by comparison. Sanskrit is nonzero which is very surprising because I don't know of anyone who speaks that language and obviously emoji there's no there's no emo um Wikipedia articles uh written in emoji language um

**[19:43](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=1183s)** not yet yeah so the the kind of embedding space you know inherits all of this training imbalance that we're talking about as well but there's also a a a deeper issue here right that's not technical and that's to do with meaning itself. So let's take our favorite emoji again, right? We've got that one picture meaning literal fire, attractive, danger hot excellent chaotic you know, it's a it's a lot of different concepts and ideas being lumped into one single picture. And the model isn't always wrong to mix these different senses, right? It's it's kind of reflecting real ambiguity that

**[20:33](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=1233s)** the human language has. And essentially what the model is doing is it's not it's it's not removing this ambiguity, it's simply encoding it in numbers. So how do we actually debug this in practice? Right? So the lesson obviously isn't don't use multilingual embeddings there as we've seen extremely powerful tool but is to not assume alignment when it comes to these different languages. So starting with nearest neighbors, looking at translation similarities across different languages, breaking down metrics and uh tokenization examples per language and then focusing on the weird examples and the tail cases

**[21:23](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=1283s)** because that those are going to be often the most diagnostic in the work that you would be doing. Now, this isn't, as I mentioned, a benchmarking exercise. This was just something that I thought was interesting enough to play with, but if I was to do something like a benchmarking exercise, I think there there's a quite a few more steps that need to be done where I'll be looking at more embedding models. So, here I think I've just used a simple kind of sentence transformer model. Um, I would definitely need to validate translations against native speakers, especially for concepts that are a bit more abstract. Um, not sure how I would do that with Sunscript, but um, we would need to move from kind of, you know, just word probes to actual retrieval

**[22:13](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=1333s)** tasks with real documents. Um, and then evaluate, you know, per language, not just by an overall score. So multilingual embeddings are genuinely powerful. You know they do create shared semantic space. It's just that the space is uneven and alignment varies by language concept context tokenization training data you name it. Uh so the right approach isn't necessarily blind trust or uh rejection. It's just validation. validation to do with the languages that matter for the system and the users and validating the failure notes modes that you would notice as well. By the way, I'm Cav. I am actually not an embedding uh

**[23:03](https://www.youtube.com/watch?v=CH0Qxch7lfA&t=1383s)** researcher. I just like poking at models and seeing what breaks. And uh if you want to chat about anything embedding related or mathematical or whatever it might be, here's my LinkedIn profile as well. So please connect and feel free to chat. >> Thank you Kevin.
