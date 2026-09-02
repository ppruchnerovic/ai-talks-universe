---
id: 59EVOp8r0aw
title: "The Promise of Trustworthy AI by César Soto Valero"
slug: the-promise-of-trustworthy-ai-by-cesar-soto-valero
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2026
speakers: ["César Soto Valero"]
channel: "Devoxx"
duration_min: 33
published_at: 2026-04-01T08:04:19Z
video_id: 59EVOp8r0aw
url: https://www.youtube.com/watch?v=59EVOp8r0aw
youtube_url: https://www.youtube.com/watch?v=59EVOp8r0aw
tags: []
transcript: true
---

# The Promise of Trustworthy AI by César Soto Valero

**César Soto Valero**

`Devoxx` · `Devoxx` · `2026` · `33 min`

[Watch the recording](https://www.youtube.com/watch?v=59EVOp8r0aw) · [Conference site](https://devoxx.com/)

## Description

#VDZ26 Teams building with AI are often presented with a false choice: share data to get frontier models, or protect privacy and accept weaker results. It is a convenient story, especially for anyone who benefits from accessing your data, but it is not the full story.

This session introduces a counterintuitive paradigm where AI models can improve without ever collecting your raw data, and where organizations can collaborate without giving up control. By combining Federated Learning, the idea of training locally while learning globally, with cryptographic computation on encrypted updates using Homomorphic Encryption, the result is a system that treats privacy not as a policy or a feature, but as a structural property by design.

Through practical examples, this session explores why centralized training creates hidden constraints like security exposure, compliance friction, and data gravity that limit real-world adoption. You will learn how Federated Learning flips the classic “bring data to the code” approach, and how Fully Homomorphic Encryption closes the final subtle leak: what model updates can reveal, even when your valuable data never leaves your yard.

## Transcript

*3,337 words · source: supa (en, exact timings)*

**[0:15](https://www.youtube.com/watch?v=59EVOp8r0aw&t=15s)** So, good morning once again everyone. I'm super happy to be here. Not sure if I you listen well. So, I hope it's going fine. So, I'm super super excited to be here today. Today is Vox Days Zurich 2026 and this event happens only once in a year. Once in a year we join here all together to exchange to learn to talk to each other as humans, right? >> [snorts] >> And I think that nothing is going to beat this

**[1:05](https://www.youtube.com/watch?v=59EVOp8r0aw&t=65s)** this human-to-human interaction is going to stay for longer and I actually think that the value is going to increase as other forms of content get commoditized, these live events are going to get more and more valuable. Actually, a good uh person that I admire told me the other day something very profound and it is that you know, you may work remotely and that is perfectly fine. But your career is actually in person. Think about it. So, and that's why we are here. We are here for an in-person

**[1:53](https://www.youtube.com/watch?v=59EVOp8r0aw&t=113s)** experience. Very important. So, my name is Cesar. Uh I'm originally from Cuba. I came to Sweden to do a PhD in computer science 7 years ago. I was looking for freedom, was [snorts] looking for challenges. So, I did. Very happy about that. Then I decided to transition to the industry and then I moved to the financial sector in Stockholm. I came here to give you this content and very very excited about this and today

**[2:40](https://www.youtube.com/watch?v=59EVOp8r0aw&t=160s)** I'm very excited about one thing. And this thing is AI. You know, we are developers. We love code and today we have something that produces code. It's like a meta-programming kind of thing, right? So, we have some entity that creates a lot of code that we have to handle, right? And this is very exciting. I mean, the whole world is crazy about AI these days. So, I am. Right? But I'm interested not in any AI, but in one particular kind of AI. Trustworthy

**[3:28](https://www.youtube.com/watch?v=59EVOp8r0aw&t=208s)** AI. And I know what you may be thinking. Well, does such a thing even exist? Can we really trust AI? It's really tricky, right? But my promise is that by the end of this section you will learn about two paradigms that combine will give us very close to the promise of trustworthy AI, which is the title of this session. But before going into the

**[4:15](https://www.youtube.com/watch?v=59EVOp8r0aw&t=255s)** super cool technical details let me reflect about something very very profound, very very important for us humans. We all we all have to comply with this, right? And this thing is trust. If you think about it, trust is very important. We have to trust. There is no other way simply because we cannot verify everything. It is impossible to verify everything, right? For example, you go to the doctor because you get sick. You have to trust the skills of the doctor to cure you,

**[5:06](https://www.youtube.com/watch?v=59EVOp8r0aw&t=306s)** right? In the education system, you have to trust the knowledge of the teachers to educate your children, right? For your money, I mean, your assets, you have to trust the banks, the financial institutions to save your your your assets, right? So, trust is everywhere across society. We cannot get rid of it. We have to trust. And today there is one thing that is kind of new and it is AI. And AI is, you know, this really huge

**[5:55](https://www.youtube.com/watch?v=59EVOp8r0aw&t=355s)** neural networks, immense. They are large language models, right? Trained on massive amount of data. The whole internet is put there, right? And we use them, right? We interact with the with these AI systems today almost every day, right? It's pretty cool. We can write to them, we can talk to them. They seems to understand everything and it's pretty cool. And as a result, we get something that we really value, we really love, right? Sometime, most of the time, right? And through this process of inference,

**[6:47](https://www.youtube.com/watch?v=59EVOp8r0aw&t=407s)** which is an activation that happen across the the neurons in the big neural network, right? We get something. We value this. That is why all the all the excitement about and then we repeat the cycle again and again, right? We keep asking question, getting uh uh answers, right? But there is a problem here. There is a big issue. And the issue is in the interaction with these AI systems. More particularly, there, in the way we communicate with the AI system, right? Because today we send the messages

**[7:35](https://www.youtube.com/watch?v=59EVOp8r0aw&t=455s)** in plain text, right? The message is is not encrypted because these AI systems are by design engineered in a way that they will only handle data that they can directly understand. So, this is a big problem. And today we we have been told that if we want to have a more powerful AI, then we will have to be okay with compromise in privacy. On the other hand, if we have not so powerful AI, but we want more privacy,

**[8:23](https://www.youtube.com/watch?v=59EVOp8r0aw&t=503s)** then we will have to make compromise, right? We have been told that in order to get access to the frontier models, we will have to send them our data. That there is no other way. But I think this is not completely true. I think there are other ways. So, this dichotomy, not really. And in order to understand why we have been told this again and again, we need to reflect on how we have been building these AI models across in the last years. The pattern has been the same. We first

**[9:12](https://www.youtube.com/watch?v=59EVOp8r0aw&t=552s)** centralize data. We collect a lot of data, centralize it, right? Then we train bigger and bigger and bigger models with them. And then we hope for the best. We hope that the a scaling law from this uh very uh [snorts] important paper that that was published at in 2020 by the team of researchers from OpenAI. They say that the more data you put into the model, the better it will be. So, this is the pattern. This is how we have been train training uh big large large language models.

**[10:01](https://www.youtube.com/watch?v=59EVOp8r0aw&t=601s)** But this is very problematic. It is very problematic because of security. Imagine if you have all your data, everything there in one single place. So, it is an easy target. For example, if you have like a all your data is for the from the same company, the same vendor, you know, you rely a lot on one single model that is not good. It is also a problem for compliance right? I know many of you work in the financial financial sector, which is very strong here. And

**[10:48](https://www.youtube.com/watch?v=59EVOp8r0aw&t=648s)** uh and you know that if you have to move data across borders, or you have to rely on hardware that executes in another country, then this creates many legal complexities. And also it's a problem for data gravity, right? Not all the data have the same weight. We have data that is so sensitive that we we cannot use. For example, sensors, right? We cannot have sensors everywhere because of privacy. So, this centralization, this way we have been building AI these days is very problematic.

**[11:37](https://www.youtube.com/watch?v=59EVOp8r0aw&t=697s)** And the thing is that all the time we have been bringing the data to the AI. Something like this. Let's say you have three organizations, all of them calling the model. But now, I would like you to think the other way around. What if it is the model that reuses the data in the organizations? This is bringing the AI to the data. This is not

**[12:27](https://www.youtube.com/watch?v=59EVOp8r0aw&t=747s)** new. This paradigm existed, right? Uh the idea is to have like a global AI model, and then to have local models in devices. Like it started with the revolution of big data triggered by sensors in cell phones, right? Around the 2010s, right? And it's called it federated learning. And federated learning works very simply. So, first you have uh the first step, you initialize, so you have a global model over there, and then let's say you have three institutions, A, B, and C.

**[13:18](https://www.youtube.com/watch?v=59EVOp8r0aw&t=798s)** And after that, you train models locally with private data. So, you have the private data, which doesn't go outside the organizations, then you train local versions of this global model with this particular data. And then you share the updates. The updates of this local training are shared, and then they are aggregated. And with this federated learning approach, we end up with a better version of the global model. In this case is version 1.1. And it works.

**[14:06](https://www.youtube.com/watch?v=59EVOp8r0aw&t=846s)** Federated learning really works. And it has many advantages. First of all, data stays local because the organizations don't share the data, they train with the data locally. Doesn't escape from there. And this allow collaborations. So, this way you have in the previous example, three organizations training local models, and then sharing the learning. And number three, you have better control, of course. If you don't share the data, you just share the weights of the training,

**[14:52](https://www.youtube.com/watch?v=59EVOp8r0aw&t=892s)** that's a good thing. And it has been used it has been used massively. Particularly, Google has really a scale federated learning. A typical example is the deployment of production on device language models, right? The classical example is Gboard. So, if you have a cell phone uh there is an Google app that you can install. It was actually the most popular app in 2019, Gboard. And uh it's basically a digital keyboard you have in your in your phone. And the

**[15:40](https://www.youtube.com/watch?v=59EVOp8r0aw&t=940s)** thing is that this app trains local versions of the language model, right? So, and then it shares the updates using the principle of federated learning. So, this way you have uh next word prediction that is particularly for you, right? And this way they were able to learn new words because the the language also evolve from everybody, right? And it is it is pretty cool. Gboard is uh is amazing that they deployed So, this is the idea. And now,

**[16:26](https://www.youtube.com/watch?v=59EVOp8r0aw&t=986s)** I am hearing better myself. So, this is the idea of federated learning. But there is a problem. There is a catch here. And uh I'm not sure if you can guess what it is. I hope yes. I'm going to give you a hint. It is related with privacy. Do you see the problem? Yes? This is the unique data to the federated model. Yes, you are absolutely right. So, the issue is there. It's in the weights. It's in the way the training of the local models is shared when doing this aggregation because this is

**[17:18](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1038s)** >> [clears throat] >> training results that are not encrypted. And research have shown that gradients can reveal data, right? There is a paper published on NeurIPS in 2019 called "Deep Leakage from Gradients" that shows that you can also actually do reverse engineering on the on the weights of the models, right? So, this is a problem. And with federated learning, raw data stays local, but privacy can still be compromised. So, what is the solution? Well, the solution I think is something called it

**[18:05](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1085s)** homomorphic encryption. I know it's a pretty cool term. Encryption, we are engineers, we are developers, so every time we hear encryption, it's like, "Huh, this is for me. This is This is hard. This is challenging." Should be cool. But before going deep in homomorphic encryption works, I would like to tell what problem it solves first. Because you will see, we have actually three states in which data can be. Only three. So, data could be at rest, that is data that is stored on disk. Data could be in transit, that is data that goes over the network,

**[18:56](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1136s)** or in use, that is when you are actually running the data you have locally in memory, and you are using it. And today, we have very good encryption algorithms when data is at rest. These are the encryption algorithms that we learn when we went to uh school. We also have very good algorithms to encrypt when data is in transit, like for example, TLS, uh VPNs, point-to-point encryption, and so on. But when data is in use, Houston, we have a problem. We don't have good ways to encrypt data when it is in use.

**[19:48](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1188s)** So, the whole idea of homomorphic encryption is to facilitate this. Is to do computing on encrypted data. Sounds fascinating, right? So, the idea is that you have for example, A and B. You have data. Then you encrypt that data. And then you perform operations on the data. And it should be a map between the execution of the operation when data is plain, is not encrypted. And it should be the same when data is encrypted. Same output.

**[20:36](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1236s)** I know it sounds very abstract this way. That's why I prepared a demo for you. And it is a physical demo. Going to show you. This will explain homomorphic encryption. So, let's say you have A and B here. Right? And I have encrypted them. So, A is going to be 30 and B is going to be 32 after encryption.

**[21:23](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1283s)** Right? And then I have the key. So, I have encrypted these two values with this key. This is mine. Going to put the key here without revealing. And then I want to do one operation on these two encrypted values. Then I would say >> [snorts] >> A plus B right? And then let's imagine that my computer is the server. I'm going to ask the server to perform an operation

**[22:11](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1331s)** on these two encrypted values. Notice that the server have no idea what these 30 and 32 actually means. He doesn't know because they are encrypted. They are actually encoded, but it serves the purpose. Right? And now the server is going to bring the result to me. Right? The server did the operation on the encrypted data. And now he sent me the sum. 62. So, the server

**[22:59](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1379s)** did the sum, but I have the key. So, I can use the key use the encryption value here. This equation. So, what I did is that A it was 30 because I assume 10. And the other value B was 32 because I added 10. So, for me, since I know what is the encryption way I know I have the key. Then I can get the actual value, the actual result of the computation that is 62

**[23:51](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1431s)** minus 20. Because they were two values. I know that I just have to uh rest 20. And then I get 42. Which was the actual on encrypted number. Right? And notice that the server it never knew. It never knew what was the actual the actual values. And that is how homomorphic encryption works. So, just in case you miss it, what I did, I encrypted A and B. They were actually 20 and 22. Then the server got 30 and 32. It made a

**[24:41](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1481s)** computation. Then I decrypted. And that's it. So, the server computed on encoded values without seeing the original numbers. And this is pretty cool. It works. And of course, in this case I use a very simple addition, but in reality it works using lattice-based cryptography, which is a very interesting techniques. And the whole idea is that the operation is projecting the values over a multi-dimensional space. Here is just two dimensions, but when you grow it to 1,000 dimensions, it gets it gets really hard.

**[25:30](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1530s)** Immensely hard. It's quantum resistant. Quantum computing cannot break it. Because it says at the root of very, very hard problems. Closest vector kind of problems. Super hard. So, this is the pattern. You first encrypt. Then you compute on the encrypted data. And then you decrypt. That is how it works. And homomorphic encryption is actually a mega trend, especially in research. This is a post by Vitalik Buterin, which is the author of you know, creator of Ethereum

**[26:18](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1578s)** blockchain. And he said that homomorphic encryption was expected to become the mega trend. It actually it actually is, especially in research. And it's getting better and better and better. Advancements in algorithms. So, there are better encryption algorithms to work with this. To improve the process called bootstrapping. And it's the way the server does the computation of the encrypted data. They are new and new genera- generations that really improve the the speed. Eight times faster. Every year is getting. Also because of hardware, of course. Actually a paper

**[27:06](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1626s)** published last year in in June proof that you can increase the speed by 1,000 times for certain operations when working on encrypted data for homomorphic encryption. That is pretty cool and pretty promising. And homomorphic encryption has an ecosystem. For example, Microsoft SEAL is a well-known library that allows you to do operations on encrypted data. It's pretty cool. Also OpenFHE which is a open source tool that has a very good community.

**[27:55](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1675s)** There is also HEIR, which is a compiler that allows you to do compilation on data that is encrypted. It's also very good tool, very active research that exists on it. And there are many applications. For example, uh for Microsoft Edge they use homomorphic encryption to check for the password if they are leaked or not. So, this is something used in practice. There is also research made by the Apple. And the idea is to use homomorphic encryption to know where you

**[28:45](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1725s)** are. So, you to encrypt your coordinates. >> [snorts] >> So that they would not don't know exactly your position, but still they can do uh neural networks operations on that to figure out for example your position, the closest path to a certain place, and so on. It's pretty cool. So, two layers I have shown. First, federated learning. And with federated learning you can protect the raw data. And second, homomorphic encryption, which protects the updates. And with this we can reach very close to trustworthy

**[29:34](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1774s)** AI. So, let's put it all together. Let's say we have a global model. Then we have the three institutions as I showed before. They train local versions of the model by using private data. Then they encrypt the updates. They share the encrypted updates, the weights. They are aggregated, right? And now they create better and better versions of the model of the global model. And this is the main slide in my deck. So, this is the whole idea that I've shown you today. And with this, we can create amazing

**[30:22](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1822s)** things. We can make edge computing global learning a reality. On every device, we will be able to share the learning without making compromises. Oh, the whole idea is to get a smarter models with a smaller exposure. So, what to remember from this talk? First, keep data local. You know, data is our most valuable assets. It's very important to protect it. Don't share it. Don't send it to third-party vendor. Encrypt the updates if you train the model.

**[31:10](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1870s)** Take into account that the weights also hold information. And third, share the learning because sharing is how we will grow as a society. There have never been a time in human history with having more intelligence is not better. So, that's the idea. The idea is to get trustworthy AI by design, not by promise. Um I think that the smartest AI systems will be the ones that need to see the least. And with this, this is the end of my presentation, but

**[31:58](https://www.youtube.com/watch?v=59EVOp8r0aw&t=1918s)** I'm going to be around. And as I said in the beginning, we are here for the human-to-human experience. We are here to share. So, I would be very glad to take your questions, to talk to all of you. We'll be the whole day here. So, please reach out. I'm going to be very happy to discuss more about this content. Thank you so much.
