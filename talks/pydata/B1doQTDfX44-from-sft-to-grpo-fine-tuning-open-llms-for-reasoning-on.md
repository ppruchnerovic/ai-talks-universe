---
id: B1doQTDfX44
title: "From SFT to GRPO: Fine-Tuning Open LLMs for Reasoning on Real GPU Budgets"
slug: from-sft-to-grpo-fine-tuning-open-llms-for-reasoning-on
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 28
published_at: 2026-08-23T07:00:14Z
video_id: B1doQTDfX44
url: https://www.youtube.com/watch?v=B1doQTDfX44
youtube_url: https://www.youtube.com/watch?v=B1doQTDfX44
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science", "Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: true
---

# From SFT to GRPO: Fine-Tuning Open LLMs for Reasoning on Real GPU Budgets

**Speaker not identified**

`PyData` · `PyData` · `2026` · `28 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=B1doQTDfX44) · [Conference site](https://pydata.org/)

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

*3,618 words · source: supa (en, exact timings)*

**[0:08](https://www.youtube.com/watch?v=B1doQTDfX44&t=8s)** So thank you very much for being here and then for organizers to to inviting me here. So well couple of words about how I ended up here. So uh first of all I work in this building and I do some teaching and some research and well the main direction of my research is is machine learning and deep learning and I work with both u images and and some uh problems related to languages. So well I know that the hype nowadays is more about the agents not the finetuning LLMs and the staff but we had specific data sets for which we realized that

**[0:59](https://www.youtube.com/watch?v=B1doQTDfX44&t=59s)** first of all well some existing models are not operating properly and we need to have some adjustments and well we have some other constraints as So another one can be that well we have so we work with some companies which are not interested to have the data uploaded into uh different spaces or they don't want to share it with other companies. So we have some restrictions. We're interested to do something uh in house and or even if we are planning to buy something as a GPU or some online compute, we're interested to understand how much we will need at all. So

**[1:47](https://www.youtube.com/watch?v=B1doQTDfX44&t=107s)** again given all this hype, I tried to understand whether people are still doing this finetuning. Um and here I tried to extract the number of papers that appear in in archive.org or which use several fine-tuning approaches and well this is uh this represents that data for for recent couple of years and you can see that some of them some people really use it and for example for the simplest approach which probably uh all of you know is is supervised finetuning well uh there are more than 600 papers appearing there. So I guess there will be many more attempts in in

**[2:36](https://www.youtube.com/watch?v=B1doQTDfX44&t=156s)** GitHub and so on. So again not being a person who does this fine-tuning regularly I try to answer to several questions first of all for for myself and for teams u I work in uh first of all which kind of LMS I can fine-tune does it make sense at all and well what should be the budget if I want to do something in particular how much compute do I Can I do it in in local GPUs that we have um here or I need to buy something and I try to do some basic estimation. So well I'll try to briefly speak about some

**[3:26](https://www.youtube.com/watch?v=B1doQTDfX44&t=206s)** fine-tuning approaches on a high level and then I'll try to show some experiments that that I did using my own machine and and some approach I adopted for for scaling up and understanding how much compute will I need. So first approach and the one people use quite often is is supervised finetuning. So uh the the formula you see here can can look a bit ugly but it's it's uh basic uh cross entropy loss. So you basically tell the following here. Well my model is able to do something

**[4:13](https://www.youtube.com/watch?v=B1doQTDfX44&t=253s)** and well in general. So if if we speak about the machine learning and and deep learning core thing is the loss. So you try to minimize loss. So you want to have a model which which understands or is able to distinguish between many possible answers the correct one. So if let's say there are 10 possible answers and your model um guesses that the correct answer has the probability of 99 or 0.99, it's a good model. It means that we will have a small loss for this observation and hopefully we have similar small loss for others. So on average we're doing a good job. So we're interested in minimizing this loss. So in this supervised finetuning you just say okay I have prompts or questions and

**[5:04](https://www.youtube.com/watch?v=B1doQTDfX44&t=304s)** I have correct answers to them and I try to push it into into the model and and try to make sure that some some weights or all of the weights are adjusted in the way to make decision on this new examples better. In other words minimize minimize the loss. So another approach is is DPO and here there is one main difference. So now you don't give one correct answer but you say you know there are two answers one is a correct one another one is a wrong one. And so you have kind of two two let's let

**[5:52](https://www.youtube.com/watch?v=B1doQTDfX44&t=352s)** let me put it in this way. You have two models. one is the main the reference model you have. Let's say you took a 7 billion model. Uh in this case we're going to use Quen. So this is your reference model. This is what your model knows and you want to train something on top of that and you have some policy model. So you train you try to adjust some additional um parameters onto it. And in this case you know that your base model knows something regarding this question. So you have a basic question. We have an example here. So I tried to put the same example on several approaches. Probably I will shift for a moment back to just read it for you. So Natalia sold 48 clips in April then half as many in May.

**[6:45](https://www.youtube.com/watch?v=B1doQTDfX44&t=405s)** How many all together? So well it's easy for us. 48 plus half of it. So it's 72. It's going to be a correct answer. So in this case we can generate some wrong answer which would be 96 in our case and well at some point if you don't touch your model it knows answer to it. So it's either does it correctly or or in a wrong way. And by training this you want it to understand uh the true answer better or predict to answer true answer better and avoid predicting the wrong answer. So here you try to kind of teach what what what is good and what is bad. Well, another approach stands for well

**[7:41](https://www.youtube.com/watch?v=B1doQTDfX44&t=461s)** the name is OPO. In this case, instead of comparing this behavior with the reference model, you try to just define the odds ratio. So if um if this model does this correctly or probability of answering correctly is high we will calculate the odds ratio. So we will have probability of um true answer and probability of wrong answer divided onto each other and if this ratio increases it's good. Okay. So again you try to you have two answers good and bad one and you try to differentiate between them and you try to teach the model to understand correct things better. So

**[8:35](https://www.youtube.com/watch?v=B1doQTDfX44&t=515s)** the advantage of this approach is that here you don't use reference model. So each time it is not uploaded to your GPU to to understand uh what's going on. Instead you use this odds ratio at the same time it is accompanied with supervised finetuning which is which was the first basic approach and we have GRPO something which is uh used and uh introduced by the by dips so it's more fancier and it's related to quite related to PO approaches which is uh reinforcement learning. So I'll try to just again speak about the idea here. So in this case you say well instead of

**[9:28](https://www.youtube.com/watch?v=B1doQTDfX44&t=568s)** two let's have several of them let's say 10 10 answers and it would be good idea to and be able in the beginning to differentiate between them. So the the simplest form is in this scenario you have correct answer which is 72 and nine wrong answers. But well in in more realistic example where you have a text you try to have several answers and understand which ones so the the relative correctness and you try to teach the model the same thing. So you try to well give all these examples in the training period and if model starts differentiate between them understand

**[10:16](https://www.youtube.com/watch?v=B1doQTDfX44&t=616s)** their relative ranking it's good uh it means that loss will increase and the the results are going to be better. So there are many other approaches but these are the the ones which are pop up when you start to digging into this direction. So uh well besides this this approach is there is another decision to make is uh which is related to like to what extent you want to fine-tune the model. The first simple thing I mean simple in terms of um idea not the implementation to to do full fine tuning. So try to adjust all the parameters which most probably will be a a huge task and uh mostly people nowadays try to avoid it.

**[11:09](https://www.youtube.com/watch?v=B1doQTDfX44&t=669s)** Well some claim that it's useless in other uh on the other side it is it is quite costly. Another two approaches people adopt nowadays is are Lora and and Qura. This is this is the approach I was uh speaking about. So you try to kind of train additional layer based based on your model or or around your model which tries to understand some some new uh logic or tries to capture some new information you have in in your data set. Q Laura basically does the same thing but it's u uh has a huge advantage in terms of of compute it uses because a

**[12:01](https://www.youtube.com/watch?v=B1doQTDfX44&t=721s)** regular Laura uh uses 16 bit system for for reservation of the data and and uh the information in particular here the parameters which we are interested to adjust. On the other hand, Kora does this in in um in well does it in in four and it's relatively cheap to run it especially because you're going to from model to model you are going to upload all or part of these parameters to to GPU and it's it's a good idea to have smaller weights. Of course, this is not something which comes without a cost. If you want to preserve the reference model

**[12:50](https://www.youtube.com/watch?v=B1doQTDfX44&t=770s)** in a cheaper environment, uh it loses some kind of information or sharpness, let's say. So, one more slide on on this and probably I will switch to to some basic results I have. So as you can see for two of the models it is mentioned that we need reference. So for example for DPO you need to have this reference model which every time for for every batch or for every example tries to understand what's going on and whether you're doing good compared with this reference model. uh on the other hand for for RPO you don't need this need it and instead you what you do is

**[13:40](https://www.youtube.com/watch?v=B1doQTDfX44&t=820s)** just OTS ratio and the regular SFT for which you again don't need it. So again if if you are planning to fine-tune a model you have a huge a huge choice uh and and there are many models you you all heard about uh here we do a basic experiment based on this coin models we pick three of them and we are going to work with this GSM8K data set you have seen one example from it so it's basically a school mod you have something like 8K training data and uh a bit more than 1K test data and we're going to

**[14:29](https://www.youtube.com/watch?v=B1doQTDfX44&t=869s)** use one machine with RTX 3019 90 sorry and okay so probably these are a bit small but I'll try to elaborate on them okay so we have three models as I said uh so the smallest one has 0.5 billion parameters the next one has 1.5 billion parameters the third one has 7 billion parameters so beyond this it was uh not possible to generate some reasonable results on on RTX 3090 and well what I did here I tried to run uh this approaches on these three

**[15:16](https://www.youtube.com/watch?v=B1doQTDfX44&t=916s)** different different uh models and see what's going on. So on this green highlighted ones you see for for each row which one generates a better result. Well, again this is just a toy uh data set and they may not be very informative but again even though having uh some small data set some uh well you can affect the results and and accuracy. So the first column is just reference on the base model. The rest ones are uh the references after applying one of the approaches mentioned earlier. So

**[16:05](https://www.youtube.com/watch?v=B1doQTDfX44&t=965s)** well some time that that is consumed during this process is this pairs generation for DPO or ORPO and well I didn't have at the moment accounted for for this time spending uh so this is just the another visual visualization of one row so for 1.5 billion parameter model uh we have that DPO outperforms the rest but again so if if you check the literature there are results where if I'm not mistaken there is a 1 billion parameter model which is able to go beyond 80% uh on on this toy data set uh so here I have some information

**[16:54](https://www.youtube.com/watch?v=B1doQTDfX44&t=1014s)** regarding how many pairs were generated for this experiment and probably well what I'm trying to do at the and and I have some information which is useful for this is for for each observation or for each pair or for each prompt uh how much time was consumed to to generate to well uh fine-tune uh the model and as one may expect uh well the cheapest one is SFT so this DPO and GRPO in my case on my machine generated more or less the same uh results in terms of speed and gpo is uh something huge related to them and what I did and how I'm planning to

**[17:43](https://www.youtube.com/watch?v=B1doQTDfX44&t=1063s)** use all this stuff is to understand what would happen if I scale this in particular. So I have some problems uh to solve and I'm interested to devote some budget to it and uh well in this case I just try to scale for for 10k training data set and to see how it will work and how much time I how much GPU time I need for this and as as expected for gpo it's the highest So this is the same for SE seven uh billion model though I excluded GRPO here because well it's not that uh useful in this case in general but for

**[18:34](https://www.youtube.com/watch?v=B1doQTDfX44&t=1114s)** example again this is something that I can mark for me so I have well I need to have three I need to have some three hours of GPU to just train uh 7 billion model. This model highlighted here for for one epoch for for 10,000 examples. Well, so I am running out of time. So two slides briefly. So I tried to check well of course whether some information which is known or or publicly available is binding for my case or not. So here I have the the GPU memory requirement for different models and the ones which are highlighted or in

**[19:23](https://www.youtube.com/watch?v=B1doQTDfX44&t=1163s)** in bold are the ones which I generated well when I was running this experiments I've seen in in my machine some maximum numbers and well for example for for if I do if I use 7 billion model and I do Laura the maximum G GPU memory use that I have seen was 22.2 two um gabytes and well if if you know the capacity of it is 24 so it was quite close but it was able to uh run. So okay one more slide and then so the main purpose of me doing this uh well probably two two reasons of doing this. So first of all I'm interested to estimate uh how

**[20:13](https://www.youtube.com/watch?v=B1doQTDfX44&t=1213s)** much I will spend if I do some real experiments. Uh and here I have some estimates. So for example for the same 3090 you can find it online for for 50 cents per hour and well I try to understand okay how much money do I need to for example fine-tune um a 1.5 billion model uh if I choose let's say two three models I train each of them three two three times for from two to four epochs and this kind of stuff. So based on my estimates, I try to understand how much money do I need. Of course, numbers here are small because I chose small model uh and and number of training data is small. So

**[21:04](https://www.youtube.com/watch?v=B1doQTDfX44&t=1264s)** advantage of having something like this done in house is that you know that you already have some CS which are running properly uh and you can easily scale it up and you can try to just uh pick pick the models you're interested in and estimate some some realistic budgets for it. So this is this is how I'm going to use it. Okay, I think that's it from my side. Thank you very much. So uh is in your setup uh everything is

**[21:55](https://www.youtube.com/watch?v=B1doQTDfX44&t=1315s)** fixed like uh training and testing data and uh only variation is uh done regarding the objectives. Um well since again this was a small scale experiment um I tried to minimize the difference to to make it it comparable. uh for example for I mean it's it's difficult to compare in terms of accuracy SFT with let's say DPO because for SFT I use all all samples for DPO we just generate some pairs which well uh to have some smaller scale and to have enough

**[22:45](https://www.youtube.com/watch?v=B1doQTDfX44&t=1365s)** um well compute and time to get some some reasonable results but there there can be some other differences as well in this case what I can claim regarding let's say this basic approaches be DPO or GRPO uh if we preserve like a rank or or uh the batch size and increase just the number of samples I'm going to use more or less the similar compute and I can use the same RTX and just the time is what is going to be challenging for me. So I can just simply linearly scale it up and and hopefully get some reasonable estimate.

**[23:32](https://www.youtube.com/watch?v=B1doQTDfX44&t=1412s)** >> So sorry, can I follow up? >> Sorry, >> could I follow up? >> Uh if there are no other questions, by all means. There are other questions. Give your question and then >> get back. Um thank you for the talk. I just wanted to have your opinion in something. So for example the the quint 1.5 billion uh billion parameters u I'm trying to I'm trying to fine-tune it for the SQL query creation for example. I have whole company curies and I want to fine-tune it with this model. in your opinion like how how many hours will it take if I'm using 4090 for RTX 4090 for example and

**[24:23](https://www.youtube.com/watch?v=B1doQTDfX44&t=1463s)** uh because here you are using uh 3090 right if I'm not mistaken okay let's say 3090 uh how much how much time will will it take and if the data is a company data like >> okay >> uh like maybe 20 years old company for example So this is exactly what I try to do here for myself. But in to be order to be able to answer to your question. So we need to try to understand well this dimension is simplified a bit like how many observations you have it depends on how huge are they and the stuff. Uh the next thing is just to do small experiment which would be which would cost uh which would cost you like a several dollars to do with this go with

**[25:11](https://www.youtube.com/watch?v=B1doQTDfX44&t=1511s)** this SFT uh GRPO and DPO for small scale and try to scale it up to have some some reasonable >> the problem is not the the budget it is the we already have the GPU so I'm just just want to know the important thing is the time It's not the it's not the budget. >> Again, we need to try to have a basic setup to see how it it consumes. I mean, the easiest way you can ask like any LLM to to estimate it for you. But in my case, so well what I get as a first guess and what I uh get as an answer as a basic estimates as a basic experiment were quite different. But again, you

**[26:00](https://www.youtube.com/watch?v=B1doQTDfX44&t=1560s)** need to do some basic setup to see how it goes, then scale it up. So this is exactly what I suggest. >> Okay, thank you. >> Uh thank you for the talk. Uh is scaling always linear? the scalability is it always linear or there's some logarithmic growth or uh how how fast if you scale your graphs or linear but is growth always linear as you increase uh data >> so first of all for gpo it's it's completely different story and you're going to have problems so it's not linear and I didn't even try to uh scale it up uh well if if you don't have any other

**[26:49](https://www.youtube.com/watch?v=B1doQTDfX44&t=1609s)** problems with let's say the memory issues and the stuff if you preserve the same rank the same uh batch size for for a given um GPU I don't see any any reasons for it to to scale to have nonlinear increase so you can put a regular checkpoint even if you have some other issues you can go back with it it's not going to be perfectly linear I prefer to have myself done like several uh experiments for for different data sizes to make sure that I have a better estimate rather than just a line drawn there. Okay, thank you very much. So maybe one more question to prepare

**[27:41](https://www.youtube.com/watch?v=B1doQTDfX44&t=1661s)** for the next index stage with thank you so much. >> Okay. Thank you very much.
