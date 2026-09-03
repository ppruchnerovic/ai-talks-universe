---
id: aRaqkmDv-MU
title: "Piotr Stepinski-From Handwritten Notes to Smart Knowledge_ Build Local AI Agents with Python"
slug: piotr-stepinski-from-handwritten-notes-to-smart-knowledge
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: null
duration_min: 31
published_at: 2026-01-09T17:57:14Z
video_id: aRaqkmDv-MU
url: https://www.youtube.com/watch?v=aRaqkmDv-MU
youtube_url: https://www.youtube.com/watch?v=aRaqkmDv-MU
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Agents & orchestration"]
transcript: true
---

# Piotr Stepinski-From Handwritten Notes to Smart Knowledge_ Build Local AI Agents with Python

**Speaker not identified**

`PyData` · `PyData` · `2026` · `31 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=aRaqkmDv-MU) · [Conference site](https://pydata.org/)

## Description

Your notebooks are full of insights—but they’re scattered and hard to search.
In this live-coding session I’ll show how to turn handwritten notes into a searchable, connected knowledge base using local AI and minimal Python.

We start with AnythingLLM’s UI for quick wins, then move to Python agents that:
• classify note types,
• extract key ideas,
• build a personal knowledge graph.

The entire stack runs on your laptop with MLC-AI—no cloud, no data leaks.
You’ll leave with a reusable agent blueprint you can drop into any data-processing workflow tomorrow.

## Transcript

*3,721 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=6s)** Hi. Hi. Welcome everyone. So sorry for that little delay, but without further ado, please help me welcome um PR. Take it over. >> Hi, good afternoon everyone. Welcome to Pi Data Global. Um my name is Pampinsky. I lead data science and development teams at Infinity AI specializing in industrial IoT platforms for water management. Uh the focus of my work and my goal today is to show you a practical real world demonstration of the agentic approach to knowledge management. We are all facing the same problem knowledge fragmentation. Uh we live in a world of piles and everything is seems

**[0:56](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=56s)** to be a file now displayed documents, meeting notes, research papers, confluence pages. Uh we have all the data but the knowledge is trapped. just to think about Tom new engineer in my team asking where can I find all the definitive guide on rag and my answer would be guess what uh it's split across five docs to slide decks something on GitHub confluence page so it seems like we have all the pieces but uh no picture on the box so why build this system locally there about several critical reasons. Uh privacy, you have sensitive documents, you cannot share across public API. You

**[1:47](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=107s)** want to keep this privacy for yourself. Second is cost. Processing high volumes of data quickly becomes uneconomical and third is ownership. So you want to process your data without relying on third parties. If the internet goes down, you still need to process your data. So our goal would be to build a 100% local pipeline uh for knowledge synthesis. Let's uh jump into architecture of this uh solution and uh yeah so we require modular agentic design uh that's why you use crew AI to orchestrate specialized agents uh preventing one weak input from

**[2:38](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=158s)** sabotaging the entire system and um yeah the the the brain So this those are eyes of our system. We we want to also are these handwritten notes. But uh there's also brain which is LM here. And let me quickly jump into um another another view because I'm going to just introduce local uh inference. If somebody's not familiar with how to do those things, it's pretty simple. Uh I'm running this presentation right now on my uh Mark uh M4 um metal u and what I'm doing here um let me stop

**[3:26](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=206s)** sharing this. So this is my this is my console and um um so this is basically uh the command that runs for you. It's basically it's docker. So in your docker you may run anything other than this is how I'm going to present uh communication with local service that I run here. Okay sorry here um here you have is a proof that it's running uh in the back end. So what I what I did in order to to have those pretty uh pretty looking APIs uh log um I I run this command. Um

**[4:36](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=276s)** And here here we go. So uh if you just look into documentation MLC AI um you you can see what exact comments I use to basically to set up cond environment in which I have this tool called MLCI and it I can serve it directly uh as a hugging face model. As you can see here, uh it's quantized. So, uh it's pretty fast if you keep in mind that this still local inference and uh and pretty powerful at least for uh for the purpose of this presentation. So, um and let me jump now into uh something called anything LLM that I've just showed how how I run it

**[5:24](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=324s)** in Docker. And um I'm going to prove uh that it's it's running uh that it's up and running um this server this local interest um and it's here. So I've set up for you this this thing in a docker. You can see it's on my local host. So uh I communicate from docker and it's pretty simple approach if you if you have um documents and you want to talk to your documents basically. So you create workspace here and you add some some files into your uh workspace and you can basically chat with it like the similar experience like like you would have with one of the cloud uh LLMs. Yeah, chat GPT or cloud or whatever. So I don't know uh

**[6:14](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=374s)** that just just to prove that it's uh uh defined here. It's it's system default 11 preference box. But if if you actually if you go deeper into into setup of this thing you you may see believe me that this is local and um and I asked him to summarize my note and and here's the point actually this note was in PDF. So there was no chance for me to analyze this PDF. Yeah. because it's not a this this no this model this LM is not capable to to um accept PDF as an input. It it needs to accept uh clear text. So at the end when I provided him the clear text of my

**[7:06](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=426s)** note, it was able to to summary this this text and that's fine. And now I'm going to jump back into my presentation where I'm going to prove you how with this agentic approach I may actually actually achieve the the thing that I wanted to to have from the beginning. So I may have the whole chain of uh different tasks from OCR our PDF and then improving OCR with LM and then up to um retrieving real knowledge from this the set of set of nodes that I have. So um let me jump back into um presentation. We are here. So um yeah let's let's think about it for

**[7:55](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=475s)** the purpose of this presentation. I prepared 10 uh notes on different subjects. Some of them are related, some of them are technical. Maybe there is meeting note somewhere all handwritten. Um I'm going to show you some example uh moving forward and I what I would like to do here I would like to actually OCR those those files digitalize them and uh and and find out what is related uh and build a cluster probably of nodes that are related but not only on keywords search I don't want to only have traditional retrieval but I want to have something something more advanced and um first problem that we that you would face so okay if you look at the

**[8:43](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=523s)** system design uh there is agentic approach we use crew crew AI to orchestrate specialized agents preventing one week input from sabotaging the entire system um so the workflow is fit first we have this vision specialist u for the roex and then you have also librarian and senior editor And those guys are going to clean uh um are going to deliver you context of the node and also uh they're going to clean clear the row output from OCR. Uh so let's think about it as an eye and brain. That's also good use case for LLN that that uh this improvement of OCR. So let's jump into phase one. Um the

**[9:35](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=575s)** phase one is called TI. It's pre-processing and um as I said standard OCR uh would be um uh is is not that great with a very messy notes messy handwritten text. So we need to use split pipeline. And I'm just to briefly introduce you an example from my code uh because this is maybe most interesting part of it. So it's uh uh yeah we observed what I said that sometime OCR fails on thin pen strokes. So um the key of this solution is I I use opencv deation operation to fatten the ink strokes and um transforming fragmented uh

**[10:26](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=626s)** handwritten handwriting into a clear marker pen uh for the OCR model. Um and I use two version of the image. The first version of the m im image uh a sharp version uh to find text boxes and preventing ghost boxes. Second, a thick end high contrast version for reading the text making find look like a B marker. And this grant is high quality input for the LLMs and I I'm going to let you let me explain how LLM is used in next phase. So uh with Clintex the LLMs um apply uh contextual reasoning. So the librarian uh agent uh tags the domain

**[11:15](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=675s)** and the senior editor agent uh uses that context to correct technical jargon errors ensuring clean JSON output and for pedantic and um absolute it's fuel for our graph I'm going to show you at the near to the end of this presentation and uh now uh let's look at two seemingly disconnected files Um so those are handwritten notes uh that I mentioned in the beginning of presentation. Uh the note number uh 10 and number three just for presentation sake. Uh first is about use case of rag and another chain setup. Um um so documents used for building a rack

**[12:06](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=726s)** pipeline note number 10 note number three details on lchain setup mentioning chain of retriever lm ready to integrate with pipeline. Uh so we want our system to retrieve connections between these automatically. Um and the these nodes are connected in two ways. There is exact keyword match on pipeline and uh secondly there is semantic architecture match. So the concept of rack system in note 10 is semantically equivalent to retriever plus llm in note 3. So uh if we can find those connections and build this u build this network based on those

**[12:57](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=777s)** connections, we prove that uh the system in some way synthesizes knowledge comparing to traditional rag where you just retrieve documents based on your query. Um so let's jump into uh into demo how it's how it work how it works and how it is built. So um change the window here. Um okay we are back into our console and um by the way this whole presentation and code um uh is uh is published to GitHub

**[13:46](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=826s)** so it's it's you can just um just play with it if you want after the presentation um and and you know feel free to feel free to have uh some fun and for now uh I focus some part of this this uh this code which is basically the the place where we uh where we process um our data uh where we initialize our agent workflow basically. So um okay here we have two definitions. So uh

**[14:33](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=873s)** it's pretty simple. So in order to run your crew AI uh pipeline, you need to build your agents and give them tools basically and define tasks for them. That's the concept. Uh there is some code prior to that as you can see but mostly those are um help helper functions for OCR and things like that. Uh there is setup of this local LLM um somewhere like here but I want to jump directly into into this uh crew AI because this is maybe the most uh interesting part. So uh yeah so we can we define um our basically our tools um based on based

**[15:28](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=928s)** from them and then um there is also place where we uh initialize. Okay this is process single node. So having the path to your uh PDF file, our crew uh is going to Oh, here we have um here we initialized object of llm uh even if you have open i openi qu here it's really is this qu that I'm serving in the back end no problem um I can prove with uh showing that conf it's it's here it's all local uh so uh yeah that's app group and we go further

**[16:18](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=978s)** uh we have agents here as I said uh this first OCR agent uh is going to read your is going to provide you OCR row output which is already improved because we did this trick uh of two phases as I explained before in my presentation and then we have a library agent that uh because we u as I said um after row ACR OCR they're going to be very messy output and you need to understand actually um the context of this node and once you understand it you may use LLM to further improve uh your node basically this row output and uh so that's why we have librarian you want to

**[17:06](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1026s)** understand the the class of this document to help our senior editor agent to basically reconstruct notes and I'm going to give you a funny example of how it actually it actually works. there are yeah it yeah that's how we we with this trick we make use of LLM as a brain and then we have uh another definition and a set of definitions of task like extraction rotex and blah blah blah things like that um at the end of this whole thing we we would like to produce JSON we'd like to force our to give us clean JSON in order to do something with it. In my in this case, for this for the

**[17:54](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1074s)** sake of this presentation, uh what we're going to do, we're going to uh show clusters of relationships between our nodes and we're going to visualize um type of relation uh in in our graph. So um here we are and I'm going to show you how it work. Um so it's going to take some time prepare for that even for those 10 uh PDFs it's going to be I don't know from minutes to to dozen not minutes. So I plus I wanted to make sure that nothing fails during presentation. So I'm going to show you only the output uh this code in my console and it's pretty

**[18:46](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1126s)** it's pretty good. So and just to show you how it was able to actually to improve uh OCR this is the one interesting part. So as I said so we have here we have this vision specialist and what he did this guy help us to get the row uh output from OCR model which is kind of messy and I may show you uh if I have more time I probably may show you the true content of this of this uh note we can see something there is date here there's Alice Bob whoever vector DB options Kirana debas line up whatever may guess that there is something different here. Yeah, actually

**[19:33](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1173s)** chromodb doesn't exist in text. So we need to ask librarian to help us analyze draw text and he's going to determine the domain. Yeah. uh as you can see here and yeah uh he answered that the domain is technology and uh then having domain and having this row output we ask senior editor to uh review their own text and we give him we inject this huge uh prompt uh into this um agent and wait for completion. And voila. And it's uh it's pretty decent the output. Yeah, we can see that

**[20:23](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1223s)** there is uh markdown even formatted output. And we can see that vector DB options now are chromadb like and then shows us uh what he transforms into chromad because what was the the question mark was unknown from original row. So yeah, that's a huge success. we're able to um to basically to get something from this this messy data and then um as the last step uh we have another agent called librarian who knows why but uh he was able to extract main topic and keywords for from each uh note which is um is going to be used moving forward for our network x library

**[21:15](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1275s)** to build the graph. So having that um we have JSON file this whole output from all nodes is now there are now it sits now in JSON file and uh with this JSON file we are building entance uh G knowledge graph and uh there are different types of you know connections I don't want to uh show all of them the most interesting to me uh is this final visualization of this JSON file because this this actually is going show you uh what is the final um what is the final knowledge that you actually extracted. Yeah, it's it's interesting kind of interesting. So um for instance for those nodes three and 10 we see that uh there is community

**[22:03](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1323s)** that uh our code found. Um and and let me see if if we can actually uh if you can actually um understand example. Let me switch to another view which is here. Uh and this is this this graph is basically is based on this JSON which is output which is the work of our whole crew AI team. Um this is the full graph. Yeah. So I will search for node uh three now. And node three is

**[22:53](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1373s)** here as you can see. Um what it shows it shows different kind of relationships between those those nodes. So the similarity check between and it says not that much because for for for the similarity check there is yeah it's not that descriptive if you know what I mean there's something around 70 uh something 0.7 for each so it's like who knows what is similar which is not um so the the more important one is the semantic semantic similarity semantic connection and also shared keywords connection. So here we can see that note three and 10 are

**[23:44](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1424s)** directly related based on keywords but um there are also semantic there is also semantic relationship between them. Uh so um they form a group um together. Yeah. Basically here we can see only this this connection because for for our library to build communities basically the shared keyword connection is is more important than than semantic. uh so we can't actually so so it looks like there is only direct keyword in both nodes but here it's even more obvious uh for note uh two and five if you click at them that um node two is

**[24:35](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1475s)** here and five it's semantic relationship so and there is no on vector DB and there is nothing in node two about Uh so we note this about vector DB but in node five there's no explicit keywords related to vector D that shows that somehow we were able to identify this uh semantic relationship between those nodes and actually it makes sense because this is about hybrid um related hybrid search strategy and this one is database service comparison. So yeah um not uh so uh it's it's proving that the system finds nonobvious and high value

**[25:24](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1524s)** connections as well. Um let me jump back into my presentation. How much time do we have? Oh we are almost uh that's interesting. Uh yeah, I need to wrap uh up. Okay, we are this demo part. Okay. Uh okay, let's uh summarize this whole presentation. Um so we didn't just build a text structure. Yeah, we demonstrated that you don't have to compromise on quality to get privacy. Yeah, because was it was all local and we were able to extract quality interesting information from very messy very messy data

**[26:16](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1576s)** by using a modular agent architecture uh we allowed smaller smaller local models to punch above their data class basically because it was yeah as I said it's on my metal it's on M4 uh Mac OS we fixed errors and we found connections that would usually require massive cloud computing. So for sensitive private data, this proves that the local agentic pipeline is not just a backup plan. It's the responsible choice for knowledge management. And yeah, that's uh pretty it. If you have I'm ready to take any questions uh if any. And um yeah, you can uh you can find me on uh you can just uh grab this

**[27:09](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1629s)** code through GitHub. You can uh connect with me on linkin if you want. Step in sky. So sorry I didn't thank you very much. It was a pleasure to present here. Yeah. Yeah. Deepsec OCR. Uh so with DeepSync models, uh I don't have much experience. There are not only deepseek they they have OC. You may you may you have many um different vision models that in theory you may uh you may run. But those are uh from my

**[27:57](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1677s)** experimentation there were it was rather um more expensive computationally even locally is I don't know how deep co works um in cloud I have no experience I assume it's fast uh but from I was testing locally five model for for vision and I couldn't get any quality results from it so I say that for local inference we have to do something simpler basically so smaller OCR models and and small element to fix the output basically that's the concept of course you if you pay plus deepseek I don't know if there if exist deepseek

**[28:46](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1726s)** version uh quantized and small in the past I I tried to run deepseeek um on super powerful machine in my lab and it was uh super slow. There is a question about GitHub repo I've shared. I can so it's here just grab the QR code or Or I can even click here. Uh share this through.

**[29:34](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1774s)** It's here. Uh it's not that clean to be honest. I I tried to clean what? Ah okay. Somebody did that. Um how is your experience at the conference? Hope you find product. Okay. question and configuration library is okay. Okay, that's great. Yeah. Um, okay, we'll do that. No problem. Moving forward. Um, I have dot files basically. Uh, I don't know if my dot files are public. Um, okay. Okay. Let me uh after the conference uh I'm going to make sure that there is uh something on

**[30:25](https://www.youtube.com/watch?v=aRaqkmDv-MU&t=1825s)** my GitHub um that contains lazy it's lazy pin basically my lazy pin configuration >> I I Pedro >> sorry we might need to end the section now thank you so much for your Take care. >> To the next section. >> Yes. >> All right. Bye, everyone. So, see you in the next section.
