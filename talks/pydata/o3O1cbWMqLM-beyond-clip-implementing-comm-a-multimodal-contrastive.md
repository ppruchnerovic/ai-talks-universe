---
id: o3O1cbWMqLM
title: "Beyond CLIP: Implementing CoMM - A Multimodal Contrastive Learning Paper from ICLR 2025"
slug: beyond-clip-implementing-comm-a-multimodal-contrastive
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 19
published_at: 2026-08-23T07:00:17Z
video_id: o3O1cbWMqLM
url: https://www.youtube.com/watch?v=o3O1cbWMqLM
youtube_url: https://www.youtube.com/watch?v=o3O1cbWMqLM
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Beyond CLIP: Implementing CoMM - A Multimodal Contrastive Learning Paper from ICLR 2025

**Speaker not identified**

`PyData` · `PyData` · `2026` · `19 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=o3O1cbWMqLM) · [Conference site](https://pydata.org/)

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

*2,620 words · source: supa (en, exact timings)*

**[0:08](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=8s)** Hello everyone, thanks for coming to this talk today. Uh I'm Bas Gentin. I work at World Quant and today we are going to discuss one paper from ICLR uh 2025 and its implementation. Uh before uh going into details uh let's take a moment and understand what is modality. Modality is just a data type. Uh for example when you have image and text those are two different modalities because they preserve information in different ways even though the information might be quite the same. And we humans perceive the world from multimodel signals. we simultaneously see, hear, touch and feel and those help us to make decision in our environment.

**[0:58](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=58s)** However, it was not the case with uh traditional machine learning and uh traditionally each models were trained one modality at a time. So you had only images uh working in counter vision or text in when you were working in NLP. So there was this need to have a system which will learn generalized representation which will capture this multimodal uh multimodality right and uh fortunately for us uh with the emergence of selfsupervised learning and their impressive capabilities researchers could come up with a way to learn these representations uh after training on multimodel data later on These representations can be

**[1:48](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=108s)** easily used for various tasks for downstream tasks after some finetuning. Let's uh take a look two famous models uh siml and clip. One uses intra model, the other one cross model and but they share the same objective. The objective is contrastive learning. Uh let's take a closer look to clip. We have two modalities. one is a text uh uh one is a text and image. The idea is to learn embeddings in a way that you will end up uh uh in a scenario where those embeddings of two modalities they become very close to another. You don't want that uh you will have a embedding uh of a text where dog is mentioned but it's

**[2:38](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=158s)** close to some other animal. Right? So you want uh this similarity closed when you have the same observation. But these uh models had one limitation. They learned only shared information. What I mean by this? So there is this uh terminology partial information decomposition. So when you have label Y that you want to predict and you have two different modalities the information is uh consist of three different components redundancy it is shared information sorry the words might be confusing but this is what they use in literature so it's not really redundant this is the shared information uniqueness and synergy so shared information is where

**[3:27](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=207s)** you have image and text cat is mentioned right you this is shared information but what if in an image you also have a dog which is not mentioned in a text so dog is also becoming unique information and synergy on the other hand you get when you combine those modalities together for example sarcasm is a synergy you can't detect sarcasm when you rely on only facial expression you need more context to detect it Right. So who is here familiar? What is information or entropy? Cool. So ent information is surprise that you get from a random variable and entropy is average of that surprise. Uh if I come up and ask you to predict the genre of

**[4:18](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=258s)** the movie uh and just give you the title. So your entropy is high because there is high uncertainty. You can't uh predict the J genre only based on the label. But once I show you the poster or plot, the entropy will decrease as uncertainty and mutual information uh just asks this question. How much seeing one uh variable saves uh for you information for other one? How much knowing text? How much surprise will you get when you see the image? I'm sorry for this m equations but if you look at it couple of times it will make sense. So just where we had this joint uh uh information we apply chain

**[5:09](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=309s)** rule and we end up with this three equation. Here we can just see that when you have only one modality when you oops when you have only one modality with the label you only capture uniqueness and shared information and uh with this three-way function you can capture the synergy. The key thing that I'm want to say here, clip only maximized uh shared information between those two modalities. We can go back and let's take a look here. So each had its own encoders. So they never like attend one into another. So that's why they only learn shared information. We never fuse them. We maybe for fine tuning you can

**[5:57](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=357s)** concatenate and fuse them. in self-supervised uh settings they never attend one another and you only learn this shared information so you lose uniqueness and synergy there and this is the problem that we are going to solve today oh I need to go this way yeah okay enough for the clip now let's talk about com contrasted multimodel learning so we have uh again each modality has its own encoders uh with uh it goes through Latin converter we concatenate them fuse them in transformer block in the end you want to learn this representation this embedding we will see this Z few many times here today but the idea is to have this embedding in a way that it will

**[6:46](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=406s)** capture synergy uniqueness and shared information how to train such models where we are talking about unlabelled data we still don't have the labels and it turns out when you apply some augmentations you can capture this information. Uh please treat X1 here as a representation where text is there but you mask image. The same for X2 but the opposite image is there and you mask the text and those X primes are just few views but augmented correspondingly this Z1 represent X1 but this time it's already embedding and the rest uh corresponding uh the rest of the

**[7:36](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=456s)** features and once we have this embeddings we can apply uh contrastive learning right I try not to uh I try to avoid uh to dive into math a lot but I want to build some intuition I think it's not very hard to understand so the idea is that they have this assumption when you have label and you have all features together here is both both modalities all modalities together it says that there exists some augmentation strategy that can capture all information as if you had the label as well So you don't need to have label when you uh have multimodel uh data. You can capture approximate that information. Once you

**[8:24](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=504s)** have this uh you can approximate this Z uh Z prime and you can capture all components that we've discussed alongside with the synergy and explicitly we can only we can also use one modality where the other one is masked. we can capture shared information and uniqueness. Uh let's uh just uh recall Boris influency. It's just standard loss which is applied in contrast of learning. Uh you just want to maximize this the ratio because in numerator you have positive pairs uh denominator negative pairs and you can just put minus in front. It will become loss for you to minimize. and uh com is basically applying this influency

**[9:14](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=554s)** few times with the features that we've discussed. So in first component we have full views against one another and in the in in the other uh uh component of the loss we can capture shared information and uniqueness just for you to remember we have those right. So z1 is uh representation of one modality where the other one was and primes are when they are concatenated and some augmentation uh strategy was applied. Okay. Now let's talk about the implementation. So the problem that we are uh going to apply our solution is multilabel genre

**[10:04](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=604s)** prediction. Here you need to capture those pieces of information to be able to classify movie. And we we are dealing with multi- label classification. So each movie can be up to I don't know many labels. But uh here in this example we have 23 labels. The data set that I used is uh the same that the authors one of the data set that authors of the paper used. We have 25 movies uh paired with plot and fantasy. The sample here you see a very good movie seventh seal. If you are into chess or philosophy I recommend you to watch this movie. It's about one guy who came from the war and he was unhappy that came to take his life away and he somehow convinced that to play chess to prolong his days. uh

**[10:54](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=654s)** the dialogue is there very good and my professor used to say that ultimate goal of AI is to prefer this over Kardashians. Yeah. Uh so enough uh we uh still as I said had our encoders. We need to freeze those uh encoders I use for text u Q former from bleep tool and uh for images vitg uh those things are going to be fro freezed for us while training. Yeah. uh I just want to you don't have to understand all the code but just want to show that implementation is much easier than the uh concepts uh so we just have one transformer block with CLS learnable uh token which we prepared

**[11:44](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=704s)** after this concatenation just with a eight heads for image augumentation the whole configuration was taken from CCLR paper the same grayscale I randomly flip the images basically the same for text I just randomly mask 15% of the tokens that's it and we uh now about the loss fortunately for us influency is implemented by uh pytorch and I just for com uh construct it with just basic algebra and that's it we have everything what we need for pre-training and uh I use some hyperpar parameters uh basically I use warm up cosine shadow

**[12:33](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=753s)** layer I turn 100 epochs okay once pre-training is done and we need to classify this label right so we can freeze the whole architecture and the beauty about this that this representations uh can be applied in many different tasks so you are not limited to one specific task and uh actually funing is much much easier you just need to have one single liner probe. Uh 23 is the number of labels. Uh there is multi- label classification. We use our familiar binary cross entropy and uh rest is quite similar and we can see whether this setup is working or not. Some plots we see that the losses

**[13:21](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=801s)** converge in pre-training for fine tuning. we achieve uh vetted F1 score 0.62 62 and macro F1 score 0.53 which is quite good when you are dealing with multi-lel classifications and number of labels are 23 and uh we can see it outperforms all the other benchmark models and this is just a one simple example out of few experiments they have done they have also generated synthetic data where they explicitly had synergy generated it with some exor function. So even in that setup they outperform the rest of the models. The takeaway is that when you are dealing with multimodel uh

**[14:08](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=848s)** learning you need to be aware of those pieces of components that you need to capture. The budget is quite small. Uh we saw that it's just basic uh transformer block. Uh and yep I guess that's pretty much it. Uh, I hope you learned something new today and happy to take any questions if you have some. Thank you for the presentation. Are there any questions? Uh, thank you for the talk. Uh, sorry. Uh for the classification, do you use all of the embeddings combined like the shared ones, the redundant ones? And also a second question, uh is there a

**[14:58](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=898s)** way to verify that indeed the redundant ones learn the same uh information and the not shared ones learn different information and are also helpful? >> Yeah. Uh great question. Uh let's go back. So the architecture we saw this one right after the training uh you just concatenate them and with this contrastive objective while while training you had these four zeds right when you compare compare that but in inference time you just uh concatenate them and fuse them and you already have this embedding. So no need already to do masking or uh augmenting it will uh generate for you the first one. For the

**[15:48](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=948s)** second question they had this synthetic data set which is called three feature. They explicitly have a shared information uniqueness and uh synergy with exor function. Even in that setup they uh show that coms uh performs much better than the benchmark. So they actually prove it there. Thank you. >> Okay. >> Nice. Any other questions? Okay. I want as I have a chance exclusive chance. Uh as I'm totally newbie to this uh subject. How long does uh uh training takes? How long is the feedback loop for you as designer developer of this thing

**[16:36](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=996s)** to be able to detect or oh something went wrong I'm going to do it again? >> Yeah. Yeah. So uh I'm not the author of the paper. Uh so I know the one of the authors Benoid I used to work with him on another research but that research is closed because he's in industry myself as well. So uh about implementing for this it was uh two years ago it took uh a month for me to get familiar with the topic with multimodel learning I I think even more you know because it required also to recall vor information theory for the training the data set that I used was 25,000 ob observations and I think uh just few hours on uh 800 I use 800 uh GPU for

**[17:26](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=1046s)** pre-training that amount of time few hours not not big when you are uh because the data set is small and uh you and that's the benefit so the budget is small and you can uh compare with models such as clip which was trained on tremendous amount of data >> okay thank you >> thank you So thank you for your presentation and the question that I would like to ask is that you have mentioned that you have uh 23 genres if I'm not mistaken but there are some genres that are part of the like broader genre. How are you going to get information from the embeddings for example to uh detect a genre that is not so popular?

**[18:13](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=1093s)** >> Yeah. So uh good question. We are talking here about imbalanced data where you have some labels which are not not enough to represent the whole uh observation right. So when you have imbalanced data like few examples you can synthetically generate similar movies even if those are not real movies. So you can generate some text and some plot just to mimic those and try to learn them. So this is one uh strategy. Another one will be uh if you have enough data set under sampling. So if drama is majority of the classes, you can just randomly remove some uh dramas and makes this

**[19:02](https://www.youtube.com/watch?v=o3O1cbWMqLM&t=1142s)** fairness there. >> What about grouping them in a broad genre and after that do prediction? Ah, that's a good uh Yeah, that that's that's good way to do some research and see what genres ended up together. Yeah, but that's good direction. Yeah, it needs to be explored.
