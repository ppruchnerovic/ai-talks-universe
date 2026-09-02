---
id: O68AuHFU590
title: "Bio-Inspired Image Quality Assessment: Challenges and Solutions."
slug: bio-inspired-image-quality-assessment-challenges-and
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 22
published_at: 2026-08-23T07:00:22Z
video_id: O68AuHFU590
url: https://www.youtube.com/watch?v=O68AuHFU590
youtube_url: https://www.youtube.com/watch?v=O68AuHFU590
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: true
---

# Bio-Inspired Image Quality Assessment: Challenges and Solutions.

**Speaker not identified**

`PyData` · `PyData` · `2026` · `22 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=O68AuHFU590) · [Conference site](https://pydata.org/)

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

*2,811 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=O68AuHFU590&t=5s)** Let's say we have this this is originally image. And then we have two methods. Let's say one what do we improve this image? And then second one, this one. Now the question is that how computer can understand what what the best among this. Let's say I have another another examples. But here this case there are two questions here. You have these two images. We have to make decision. They're similar images. Or what the best image? They're two different problem. And then the computer has to understand what the best and

**[0:51](https://www.youtube.com/watch?v=O68AuHFU590&t=51s)** are they similar these images or the same person or some others? This is what two questions which you will investigate. But this is another problem which we have images which depend image enhancement algorithm which depends of parameters. Let's say A. And then this is parameters for A is equal zero, that's mean original image and different parameters. And now again the question is how computer can choose the best parameters. Now I will give you another examples. Here simple algorithm which will show this mean. Let's say you have this image. And then you are doing so called Fourier transform. What is Fourier transform?

**[1:41](https://www.youtube.com/watch?v=O68AuHFU590&t=101s)** That representation an image by combination of sine and cosine transform function. And then this is what you are doing Fourier transform and then this is coefficient. And then image enhancement is very simple. You are taking this coefficient taking absolute value modulus and taking power alpha minus one. And then changing alpha, you will get different kind of quality images. Now, the question is again what the best image, what the parameters. What people are doing, they are testing. All students, many people are doing this way. They are trying to buy hand [clears throat] to choose. Check one parameter, second one, third

**[2:30](https://www.youtube.com/watch?v=O68AuHFU590&t=150s)** one, eventually make decision what the best one. That's what That's what I when I started uh working on this problem, we had hundred of methods and then maybe I don't know videos and so many and then we have to detect small object tank moving and then you have to detect. But you have to enhance because it's war is the quality so bad and then we had hundred of methods and the first day we had 10,000 and then reduced them five 10 hundred and then among hundred we had to choose the best one and the real time. That's the That's the what I I started work on this problem.

**[3:17](https://www.youtube.com/watch?v=O68AuHFU590&t=197s)** Now, and this here we are showing that now we have two parameters. One, this what image enhancement is power alpha, how to choose the best alpha. But the second, there are different kind of methods. Now, we have two different problems. How to choose parameters and simultaneously how to choose the method. This is what I said that we use hundred wavelets to do this kind of thing. Okay, now this is what examples. The practically, it's a recently we develop this in Armenia right. And then here what we have this is images and difference kind of image enhancement is totally difference thing. And then we wanted to see how we can choose the best

**[4:09](https://www.youtube.com/watch?v=O68AuHFU590&t=249s)** one. It's understandable yes this is several several problems but all the same thing. And this is what here. Now we are doing a little bit more harder problem. We are using difference combination of image enhancement and then also we are using difference kind of combination of image enhancement. Now you have difference method and we combination. We have three parameters of more parameters how to choose the best one. Now [clears throat] applications is so many. Image transmission, testing and so on so on. A lot of application. Now the problem we can formulate this way. We have input only one image.

**[4:57](https://www.youtube.com/watch?v=O68AuHFU590&t=297s)** You don't have anything and then computer has to make decision is the best or not. Is good image or not. Okay, this is what the problem. Practically there are two approaches using neural network and then using simple way. The simple I will explain simple all guys. Because when I develop this it was the government job. They know they needed to have this output as very fast and real time seconds. This is what we will do it. And now this is what problem formulation. This is you have one image and then you don't have any reference any information about this image and then you wanted to make

**[5:46](https://www.youtube.com/watch?v=O68AuHFU590&t=346s)** decision of this quality. And I will say this is what I developed this 1996 and then published 1999. Now I have approximately 50 publication in this subject and became new area of research. No reference quality image. Okay, and now what this is the problem which it can solve this method. You can choose monitor image quality and then you have a compare make benchmark to choose the best algorithm. You can optimize parameters. And then also benchmark image system if you are doing several steps. And also

**[6:34](https://www.youtube.com/watch?v=O68AuHFU590&t=394s)** you can use to fuse images. Let's say you have two images, how combine this image get the third one. And then also use only about this idea to create image similarity measure. Okay now >> [sighs and gasps] >> what people doing how they solve this problem in the beginning they solve using so-called entropy which develop uh Shannon in US Shannon and here in Russia and adult. Now but entropy is not good method. Why? Because look this this images visually are different. But entropy which people are using in neural network everywhere it shows the same.

**[7:21](https://www.youtube.com/watch?v=O68AuHFU590&t=441s)** The same result. >> [snorts] >> This this is all this equal because it's based on histograms and this better image which is right develop here. Look this this image we shuffle rows and then shuffle pixels and then you can see entropy and then another entropy is another modification of Shannon entropy, standard deviation. You can see the images are totally different, but visual but numbers are the same. How computer can understand this? Okay? And then, this [clears throat] is what new the measure which is very simple developed. This is the first measure which we developed. This is 1996.

**[8:10](https://www.youtube.com/watch?v=O68AuHFU590&t=490s)** And then, this is a recent for thermal images. Now, idea how we can create this image this measure is very simple. Let's say you are having image. You are giving taking block by block, free block, free by free blocks. And then, this is what taking this free by free block, and then taking maximum values, and then taking minimum values, and divided this, and then taking log, and then creating image, and then summing. It's very simple algorithm. And I will say this is very simple, but government US government give me $500,000 to continue this because it's so powerful.

**[8:57](https://www.youtube.com/watch?v=O68AuHFU590&t=537s)** It's surprisingly. And now, we have several No, I will say color cases one mirror 2,000 citations or thousand citations. That's so popular. Okay. Now, this is what I did the same idea how we creating. Now, a little bit history. This is what I develop and publication. And now, I said that it's new direction on image process. Second question which we will investigate here is this. Linear algebra, that's what classical algebra is not good for image processing application. Let's say neural network you are doing addition, subtraction. Yes and the first

**[9:44](https://www.youtube.com/watch?v=O68AuHFU590&t=584s)** And then what you will see that what happened. Let's say visually see what can happen here. Let's see, you have these two images. If you add these together, what will be this image? If you add this image with this image, you will get you will get this image. Yes? And then it's not good because you this image is good, this image visually good, and this image visually good. You are adding together, getting something which visually is not realistic. And then now when you are using in neural network or other places, you have to do additional tricks, which is computer doing or sometimes you have this

**[10:31](https://www.youtube.com/watch?v=O68AuHFU590&t=631s)** this problem. And this is what linear algebra. And then this is what new addition. Now now what we did, we introduce, I will formulate later, the algebra which we will use here, which based in human visual system. How human visual system adding two images or subtracting two images. But that's what we will do it. Now I will show that why it's not working. Then you will understand the problems. Let's say you have these two images. You are adding this. You are getting this. If you take small block, let's say this part one block, and then some part of this block, and then adding together the your image it's takes from 0 to 155 or 56 numbers. Yes?

**[11:25](https://www.youtube.com/watch?v=O68AuHFU590&t=685s)** When you are adding together these two blocks, look this is become 400 something. What computer is doing, it's only looking eight bit, yes? And then it's a removing. That's a whole problem. That's what is coming problem from there. Now, when we do this, and then we put additional requirement. Let's say, this image is good. I'm coming here new new person, and then now image you are you have a this and you are adding my image. The quality is not changing, yes? It's quality the same. You didn't make bright or dark this part. And that's what we wanted to have that requirement that will help us to add two

**[12:15](https://www.youtube.com/watch?v=O68AuHFU590&t=735s)** images or subtract two images that we will not lose so much information. If two images are good, then if we add together, it will be also good. That's what we use that for image enhancement and restoration and others. This is new algebra. It's parametric, and this is what algebra. Let's say, one image, this is original image. You are taking maximum 255 minus original image. And then addition is this two. You are taking two images minus multiplication of these two images divided some parameters. Similar this we publish I triple transaction, you can read it. Now,

**[13:03](https://www.youtube.com/watch?v=O68AuHFU590&t=783s)** what we have done to see that this method is working, we took existing method and I replace directly simple this addition subtraction with this parametric all the operation. Look this how quality is this. And this is images, and then quality I will show better case. And then here, look this. This is what original image. And then different kind of image enhancement, and this is our image enhancement. Look this. It's bring up. Very simple, only changing operation. But you have to fill this operations, yes? This is what Another This is what breast

**[13:51](https://www.youtube.com/watch?v=O68AuHFU590&t=831s)** uh images, and then this is existing method. Uh this is guy from Harvard University, and then this is what ours. Unfortunately, if you see that white spots, this is cancer. And you don't have practically here, but you can see cancer there. Okay, that's what only changing operation, you're already getting some good result. This is another case is for medical images. Now, a little bit more. This is what one image. But this is hotel, it's very hard because in image processing, when you have white dark place, and then also white section, it's always hard to enhance. But it's working

**[14:41](https://www.youtube.com/watch?v=O68AuHFU590&t=881s)** so well. And this is another enhancement you can see practically we are making so good enhancement is become 3D images. Okay now Based on this operation, we decided to introduce new a new quality measure. Idea is this. This is human visual system based Weber law. This is entropy, classical entropy. We wanted, and then also this is logarithmical new operation. We wanted to combine all these three and created new so-called entropy, and then will help us to do this measurement. And this is what This is entropy.

**[15:29](https://www.youtube.com/watch?v=O68AuHFU590&t=929s)** This is one model entropy. This is Michelson. This is another model. Okay? This is another human visual model, and then we are trying to use this to to create the images. It's simple idea. It's just that this is what the image, and then we are doing this. Uh this is max-min. This is what I said that small blocks image in small blocks taking maximum divided minimum. But here we are adding something additional things. What is additional things? If you Let's say I will say it's called GND, but I will explain uh this way. Let's say you are having coffee,

**[16:16](https://www.youtube.com/watch?v=O68AuHFU590&t=976s)** and you want it to make sweet, and then you are putting sugar. If you put a little, you will not see any But if you add slowly sugar, and then you will feel that it's a sweet. The same image visual system human visual system is not seeing everything. It has some kind of threshold. Under that threshold, we don't see it. Okay? Well, that's what this threshold we are plugging here. That's what because we don't see it, we decided not to include this information there. That's why we are having this image, [clears throat] and then taking only this part. Each blocks, let's say 5 by 5 blocks center, we are replacing with this value,

**[17:04](https://www.youtube.com/watch?v=O68AuHFU590&t=1024s)** and then creating this image. And then having this image, and then we are adding together. This is what adding together. That's what we will call image quality. It's very simple definition. But it's also uh practical information. Now, let's look at what we have here. Now, I'm coming back to this problem. The uh choosing problem. Let's say image we have and then we are taking Fourier transform. This is Fourier transform. And then we are taking a coefficient alpha and then doing inverse Fourier transform. This is what this part is here. This is coefficient Fourier coefficient multiplying to this and taking alpha.

**[17:54](https://www.youtube.com/watch?v=O68AuHFU590&t=1074s)** And then this is what alpha. And then uh this is what one parameters, a second parameters. Let's say you are choosing different kind of method. Second parameters, this is That's mean we are putting uh this method here and then parameters value is here and creating this 3D the image book. And then taking maximum value. That's mean we are getting maximum value. That is the best method. And then this is the best parameters. And then you are having this and then you will get this output. And then now you can see the measure only using what the simple measure. And this is what uh choose the best parameters is 93.

**[18:43](https://www.youtube.com/watch?v=O68AuHFU590&t=1123s)** And then this is uh we measure original image and this is what parameters how it change. That's mean you have one image then a very simple algorithm is helping us to make better images. And this is another medical sound with this new algebra. Here, if you look there's the minus I'm using new algebra, addition new algebra. This is the same concept. This is entropy concept and this is we are giving some kind of weight and then we are creating this image based on this this image and then combining this all information and then we are getting the score the best. Yes okay. Okay, now I'm coming back to this

**[19:32](https://www.youtube.com/watch?v=O68AuHFU590&t=1172s)** problem. Problem how to this images are similar or not. Now uh Okay, I'm there are different kind of similarity measure and today we they talk this is mean square error. This is mean square error. This is uh this is uh Oh my god, I forgot. I will tell you. This is Chebyshev, this is Manhattan. Manhattan distance and distance let's say this is block the street and then distance between here to here you this is mean square error. This is Manhattan distance and this is Chebyshev and this is what uh Minkowski measure. Now, why we are bringing this? If you look that

**[20:23](https://www.youtube.com/watch?v=O68AuHFU590&t=1223s)** this images are totally different. Mean square error the same. Differences between this this this this but you all using mean mean square error and neural network, yes. That to handle that what you are doing you are adding more information database and uh layer that you will be able to fill this. Okay, this is measure. Now you can see that my measure is distinguish all this. That's mean we will very simply distinguish not only distinguish this differences but also we can pick the best one. This is what one and I you said that. Thank you. And I didn't specially put conclusion because I'm

**[21:14](https://www.youtube.com/watch?v=O68AuHFU590&t=1274s)** thinking I will say my conclusion is this that you have two let's say >> [clears throat] >> Yes, you have two rabbits. You learn how to handle these two rabbits and then months later it became six eight four and then you started to work with these four learn how to handle this it became 16 and so on. The research also this way different kinds of different kinds of applications. Okay, thank you.
