---
id: qga209nIUUY
title: "Exploring the Nearly Endless Chemical/Materials Space | Phillippe Schwaller, EPFL"
slug: exploring-the-nearly-endless-chemical-materials-space
conference: amld
conference_name: "Applied Machine Learning Days"
category: "Practitioner AI conferences"
edition: "AMLD"
year: 2026
speakers: ["Phillippe Schwaller"]
channel: null
duration_min: 16
published_at: 2026-02-13T09:00:27Z
video_id: qga209nIUUY
url: https://www.youtube.com/watch?v=qga209nIUUY
youtube_url: https://www.youtube.com/watch?v=qga209nIUUY
tags: ["AMLD", "Machine Learning", "ML", "Artificial Intelligence", "AI", "Applied Machine Learning Days", "EPFL", "AMLD EPFL", "AMLDEPFL22"]
topics: []
transcript: true
---

# Exploring the Nearly Endless Chemical/Materials Space | Phillippe Schwaller, EPFL

**Phillippe Schwaller**

`Applied Machine Learning Days` · `AMLD` · `2026` · `16 min`

`#AMLD` `#Machine Learning` `#ML` `#Artificial Intelligence` `#AI` `#Applied Machine Learning Days` `#EPFL` `#AMLD EPFL` `#AMLDEPFL22`

[Watch the recording](https://www.youtube.com/watch?v=qga209nIUUY) · [Conference site](https://appliedmldays.org/)

## Description

🟣 AMLD Intelligence Summit 2026

www.appliedmldays.org

## Transcript

*2,061 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=qga209nIUUY&t=2s)** [music] Thanks a lot for the introduction. Uh it's a great pleasure to be here on that stage today. Sorry for the voice. I will have my slides speaking for me. So yeah, you probably all know that we have a nearly endless materials or chemical space to explore and you should care about that because almost everything around you is made or driven by materials and chemical innovation. In my lab, we think about how we can apply machine learning to accelerate the design cycle of new chemicals from what molecule we want to make. always keeping the chemists at the end, the

**[0:51](https://www.youtube.com/watch?v=qga209nIUUY&t=51s)** experimentalist in our mind because we want to push towards experimental validation. And because this is often a challenge, we have also part of the lab that is working on how to make molecules and materials. And today you will hear about small language models for the novel design and also large language models in chemical research. But when we want to apply language models in chemistry, we need kind of a representation of molecules as text. Luckily, back in the 80s, they developed smiles. And you can maybe follow the text, the CNC, the branching with the brackets. You have ring openings and closings. You can represent almost any molecule as a string. And this is not a

**[1:41](https://www.youtube.com/watch?v=qga209nIUUY&t=101s)** new kind of idea. It might be obvious today but uh I've been working on using smiles for example for reaction prediction back in 2017 and we published the first transform in chemistry back at IBM research. But let's [laughter] take a step back and just think about how we can teach a language model to generate molecules. For that we would take a large data set of molecules described as smiles and similar how you would train a general purpose language model. You would just teach it to predict the next token and now not language token but uh atom by atom and it would learn that

**[2:28](https://www.youtube.com/watch?v=qga209nIUUY&t=148s)** distribution. This is a cool model but not that useful because often as we have seen also from the first talk you kind of have a specific property profile in mind and to do that in kind of the low data regime you would take that pre-trained model and one way is to do goal directed learning basically sample the pre-trained model take a batch of molecules score them according to the distance to the target properties and then update the model using reinforcement learning. But here the big problem is that scoring and labeling is expensive and that's why with Jeff a recent PhD graduate who now joined ISO we worked on sample efficient learning.

**[3:19](https://www.youtube.com/watch?v=qga209nIUUY&t=199s)** Okay, this is not exactly yeah but uh yeah if we think about sample efficiency it's just like how few labels or calculations or in the future maybe also experiments do I need to have optimized molecules and this allows us to move away from machine learning models that are cheap but very bad out of distribution to more and more costly simulations or maybe at some point also having direct feedback from simulations. Um to that end we worked on different algorithms inspired by reinvent from Astro Zenica and more recently with Saturn where we use Mamba as the language model and we could show that

**[4:10](https://www.youtube.com/watch?v=qga209nIUUY&t=250s)** kind of on sample efficiency benchmarks where for once they constrained the number of Oracle calls that you can make the numbers of labels that you can collect during training to 10,000 we could show that the LSTM based methods like augmented memory were actually working a lot more sample efficient than like fancier machine learning techniques. Serena who is here today in the audience like worked on took Saturn our most sleefficient method and said hey why can I use that for organo catalysis we looked at the Morita Bis Helman reaction over there for this there was somewhere in the literature a physics based oracle

**[4:58](https://www.youtube.com/watch?v=qga209nIUUY&t=298s)** and we just started to use a pre-trained model and do this reinforcement learning loop to generate new organo catalysts And this is one example that came out like somehow if you look at that it has the amine functional group that is require a rigidified linker and then perfectly placed on the other side a hydrogen bone donor which should stabilize the transition state of that reaction. The fascinating thing here is that we're basically generating in 2D in smiles, but the model just by having this feedback from the physics-based oracle is kind of capturing 3D functionality. And yeah, I think at the moment those are really kind of more like idea

**[5:48](https://www.youtube.com/watch?v=qga209nIUUY&t=348s)** generators where like maybe then experimental collaborators like in our case go and say, "Whoa, this looks super exciting. I haven't thought about the putting those functional groups in that position yet. Let's try let's experimentally validate. A big warning here like lots of the cases that were exciting even for human experts then yielded zero yield in the end and uh it's just because the physics-based oracle is still only an approximation. What we will need is more and more rounds of experimental validation. And in chemistry, we have to address synthesizability, we have something called retroynthesis where you want to go from a target molecule to

**[6:37](https://www.youtube.com/watch?v=qga209nIUUY&t=397s)** commercially available building blocks. And you do that step by step backwards. And uh with Jeff we thought about why can't we just like use existing retroynthetic models and add like whether the target molecule can be solved or not to the objective in the generation and we could show that we could actually with a super reasonable budget solve the specific tasks in D drug discovery and not only have an interesting property profile but also a valid route. If we want to push that even further, we can kind of think of we've seen some automation in this conference. Yes, but automation is

**[7:27](https://www.youtube.com/watch?v=qga209nIUUY&t=447s)** typically not super flexible. So we can push this further by enforcing specific building block also specific reactions that can be done in automation. And just to give you one example use case, imagine to have the stock of enamine that can be delivered in like less than a week. Some byproducts of the European industry and then you enforce specific reactions that you can perform on your robotic platform or in your lab and you are able now to optimize for all those constraint and still find interesting molecules. So the sampling of molecular space works. So how do we develop more realistic scores? I I will skip that in interest of time and just switch to more

**[8:19](https://www.youtube.com/watch?v=qga209nIUUY&t=499s)** like how we use general purpose LLMs. A few years back you had they were really bad at chemistry and uh now they're a bit better and you also don't have that you have not only an LLM but the larger framework around that has access to diverse tools. Back in 2022, end of 2022 2023, we worked with Andrew White on improving language models in chemistry by adding chemistry tools. And if you want one example from that paper back then, we managed to get GPD4 to plan an in execute the synthesis of an insect repellent by we first think what is an

**[9:09](https://www.youtube.com/watch?v=qga209nIUUY&t=549s)** insect repellent, do a literature search, find a few examples, select one, convert that to a representation that other machine learning tools can actually use, then predict a a retroynthesis route and a recipe using another tool and in the end because we connected it to a robot actually do the synthesis. This preprint and paper had like impact beyond academia. Andrew White was invited to the White House to actually brief the president and it was cited in the human development report back yeah in 2025. We have more work on engine tech systems where we go more to from like LMS using

**[10:01](https://www.youtube.com/watch?v=qga209nIUUY&t=601s)** tools to LMS doing quick scale acquisition having some like few basic meta tools or addressing like things that we have in human research where basically we do an optimization we observe a few things and then we change we adapt the goal and uh we have agents for goal. Yeah. Evolvement. And tomorrow I was also present in one of the in the rush track something about dynamics. In the end in all those things like projects evaluating agents and LMS is super challenging and uh my lab contributed to ChemBench and also to humanity's last exams but we're never

**[10:50](https://www.youtube.com/watch?v=qga209nIUUY&t=650s)** sure like kind of if what those benchmarks capture actually help us to to do better research. So one thing we've worked on recently is uh that to make them useful for retroynthesis. Basically we we observe that language models get better at understanding chemical reactions and combined with traditional retroynthetic tools that can give you plenty of routes towards a given target. We can basically use the language models to kind of align expert queries with the routes that are predicted. Like for this example here, break a pyramid in in the early stage, but get all other

**[11:40](https://www.youtube.com/watch?v=qga209nIUUY&t=700s)** rings from commercially available materials and it's able to go through 15 steps routes and basically say that some of the routes are more aligned than others. And on our benchmarks for that for the strategic synthesis planning, GPT4 which was used by chemro had a zero scores where score now newer models actually perform quite well. This is just to show you how this could look like in practice on top of any like synthesis planning tool that uh you could imagine. You can add the steering prompt can also be just give me highly probable routes if you don't know what exactly you're

**[12:29](https://www.youtube.com/watch?v=qga209nIUUY&t=749s)** looking for. But it basically gives you like a new scoring and not only that like kind of you get a a description of every single reaction step in your route plus an overall assessment. For chemists, this really means that they can kind of start talking to their synthesis planning tools. And if you want to know more about that, uh, Andres and Slotcore, they created a startup based on that and we'll present tomorrow afternoon. Last short bit, whatever you have, you at some point you have to optimize your experiments. what the ML model would predict at first will not work. And in

**[13:18](https://www.youtube.com/watch?v=qga209nIUUY&t=798s)** chemistry, invasion optimization became really popular based on this paper here. And what they use, at least in chemistry, is quantum mechanical descriptors. And this is also what our industrial collaborators typically use when they describe their lians, for example, in a reaction. But whenever you want to move to a new process, reaction experiments, it's typically three to six months of discussion. So what Buana like developed in my lab is just like why don't we kind of encode whatever experimental procedure as text and use a language model for featurization. didn't work quite well two and a half

**[14:06](https://www.youtube.com/watch?v=qga209nIUUY&t=846s)** years ago because it was far away from the best chemical features. But now we found a way by training the GP and the language model jointly and passing the marginal likelihood gradients to the LLM to like kind of uh beat standard chemical features and we can really adapt in the low data regime and go from a problem that is hard to optimize to something that is a lot easier to optimize and I think this is not the most upto-ate slide so if We even increased I guess to 23 benchmark data sets a single set of hyperparameters and uh yeah we can show that this is robust to prompting and pre-training that uh we can tackle tasks across

**[14:58](https://www.youtube.com/watch?v=qga209nIUUY&t=898s)** synthetic chemistry process chemistry material science and catalysis and even molecular property optimization and yeah like But yeah, I think everything can be ex represented as text. And if you want to try it out, all I've shown you today is open source. So yeah, went from small language models for the noal molecular design to large language models for like reasoning and chemical synthesis to how we can take language models and then adapt them quickly in the low data regime. With this I would like to thank the whole team also former members and the amazing funding which makes that work possible. Thank you very much for your attention. [applause]
