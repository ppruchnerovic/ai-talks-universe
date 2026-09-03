---
id: VhfAVA3BG2I
title: "How Transformers Finally Ate Vision – Isaac Robinson, Roboflow"
slug: how-transformers-finally-ate-vision-isaac-robinson-roboflow
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Isaac Robinson"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-05-08T17:00:06Z
video_id: VhfAVA3BG2I
url: https://www.youtube.com/watch?v=VhfAVA3BG2I
youtube_url: https://www.youtube.com/watch?v=VhfAVA3BG2I
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Multimodal, vision, speech & robotics"]
transcript: true
---

# How Transformers Finally Ate Vision – Isaac Robinson, Roboflow

**Isaac Robinson**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=VhfAVA3BG2I) · [Conference site](https://www.ai.engineer/)

## Description

Vision used to belong to CNNs. This talk explains why that changed, and why transformers only recently started winning for vision despite looking like the less natural fit for images. The answer runs through pretraining, scaling, borrowed infrastructure from the LLM world, and the long arc back to the simple architecture that scales best.

Using the evolution from ViT and Swin through ConvNeXt, Hiera, SAM, and RF-DETR, Isaac Robinson walks through what actually made transformer vision systems practical, where the tradeoffs still are, and why deployment flexibility now matters as much as raw benchmark wins. What comes next for VLMs, world models, and physical AI?

Speaker info:
- https://www.linkedin.com/in/robinsonish/

## Transcript

*2,383 words · source: supa (en, exact timings)*

**[0:14](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=14s)** Hi, I'm Isaac Robinson. I'm the research lead at Roboflow and I'm here to talk to you today about how transformers finally ate vision. Uh So, I'm going to start off with a brief summary of the competition. Then we're going to go through an overview of the evolution of the transformer, why that ended up winning out, some consequences of that, and what's next. So, where we started, convolutional neural networks. I'm sure everyone here is aware of how these work, but just to summarize, they have excellent inductive bias motivated by looking at how the eye works. So, you have a a filter that you convolve against your image, and you have activations that light up

**[1:02](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=62s)** the same way regardless of where in the image the thing is happening. Great inductive bias. A person in an image is a person regardless of whether they're in the upper left or the bottom right. And you we build these uh interesting hierarchical structures out of these, ResNets etc. This is how we've done vision for a very long time. Then comes the transformer. Again, I'm sure everyone is aware of how a transformer works, but just to summarize, we uh have a just a set of tokens. We run a set-to-set operation. So, there's no inductive bias. This is just an n-squared transformation. We inject the inductive biases into the transformer. So, for example, a classical uh autoregressive transformer, we add a causal mask to the attention matrix matrix,

**[1:50](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=110s)** and that gives us a sequential modeling. Uh for vision, we have a vision transformer. And this is very complicated. A lot of engineering went into this. We take our image, we split it into uh patches. 16 by 16 was the original. And we add a learned positional encoding, and then we throw that into a transformer, and that's it. So, transformer is n-squared set-to-set. We've got patches in our image. This is uh we've got uh n over 16 patches for the side length, and and we end up actually with

**[2:39](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=159s)** n to the fourth power with the resolution uh compute scaling. We have no inductive bias. The thing that is in the upper left can have a totally different activation pattern if it's in the bottom right. And so, the question naturally arises, which is better? The high inductive bias n-squared convolutional network or the no inductive bias n to the fourth power VIT? So, as everyone would expect, it's the VIT. So, how is this possible? And I'm I'm going to make the argument that it is because of massive VIT-specific pretraining, and then we get to borrow a lot of speedups and infrastructure from the fact that LLMs are blowing up. So,

**[3:29](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=209s)** to trace this evolution, we're going to talk about we we just talked about the introduction of the VIT, then how it how people tried to say, "Okay, well, this this cannot possibly be the best thing that we can do. How do we make this better?" So, we go to Swin, then back to a a convolutional-based network, ConvNeXt, then uh Hera, um which I think is a kind of a ha- has some really really beautiful takeaways. And then, as always happens with machine learning, we come back better listen to the simple thing that scales well, the VIT. So, uh first we're going to start with Swin. So, we have this patchify operation, and we take our uh our patches, and we split

**[4:17](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=257s)** them instead of doing global attention across all the patches at once, we just say, "Okay, we're going to do attention this window." If we just keep doing attention in this window, though, the the uh tokens will not be able to interact with each other. So, these two will never see each other. And so, the next layer, in fact, we shift the window a little bit. So, we've got these back-and-forth overlapping windows, and this looks very very similar to what I described with the convolution. Yes, so we've got this uh similar-looking operation that is happening on these sections of the image, and uh then we end up with like overlap between the filters, the locations that they get applied on. And this is how we proceed. And this actually gets us down to n-squared if your window size is independent of your resolution,

**[5:05](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=305s)** and it adds a locality inductive bias following the convolutional net. So, that that seems logical. That makes sense. Um then we go to the uh someone said, "Okay, look, there's this transformer operation that has no inherent relationship with vision. Let's go back to the convolutional network. Let's take all the learnings that we've had from the vision transformers and just spit them into a convolutional network and see what do a patchify operation. We do a I think it was a it was a 4 by 4 patch instead of a 16 by 16 patch, and we're going to say, "Our VIT was as all transformers, a self-attention feed-forward self-attention feed-forward etc.

**[5:53](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=353s)** And that self-attention is mixing your spatial information. Okay? So, for the convolutional network, what if we just say, 'Okay, we're going to have the convolution mix the spatial information. We're going to do the same pattern. Uh mixer, feed-forward mixer feed-forward onwards.' And we're going to borrow the same hierarchical structure that everyone has been using for these convolutional networks." And uh also throw in layer norm and a couple other innovations, and that's it. We're going to try that. Turns out that beats VIT and Swin when you apply it on the uh standard ImageNet reference. That's great. Finally, we have something that makes a little bit of sense. Um turns out that's not super fast. So,

**[6:42](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=402s)** someone uh Meta decided, "Okay, what what what are what are the actual important things here? The ConvNeXt has a bunch of these beautiful inductive biases. It's following this formula that we got from the transformer. Let's look at what those inductive biases are actually useful for. So, we're going to take a really really good inductively biased transformer model. We're going to strip out the biases one at a time. We're going to get a speedup because we don't have all the specialized equipment anymore for the inductive bias, and we're going to use pretraining to learn the bias instead." So, this is I think a really really great example of the balance between pretraining and inherent inductive bias, which ends up being how transformers ultimately win out. Here we're using uh uh MAE, masked autoencoder, um for those of you who are not

**[7:31](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=451s)** familiar, you take your image, you take your patches, you drop a bunch of the patches, and you ask the the model to reconstruct what would have been in the patches just based on the context. Very very similar to BERT for those of you who come from the language space. Uh you do this at scale, and it turns out the model actually learns back the inductive biases. But, you can't actually apply MAE to a convolutional network. How do you drop out a patch when you're doing this convolution that's invariant across patches? So, it's a VIT-specific uh pretraining technique that adds inductive bias that would otherwise be missing from the structure. Um So, that's great. That's super interesting. That That works nicely.

**[8:20](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=500s)** Turns out it doesn't You can take that to an extreme, and you throw in DINOv2, DINOv3, these really again, VIT-specific pretraining techniques, and you at the end of it don't just have these inductive biases towards how to process an image. You actually have really really really fit uh rich feature maps out of the box. So, for example, this is a PCA decomposition of the feature maps produced by a DINOv3 pretrained VIT, and we see that the paws of the cat have different colors, and that it's tracing the paws correctly for each of the different cats. The satellite imagery is decomposed in a way that is semantically meaningful. And uh in fact, the self-supervised learning objective is is catching up

**[9:07](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=547s)** with the best that we have from supervised learning, and this is via linear probe. So, you have your frozen features, you're just probing into them. You're not training anything specifically on your data except for that linear projection at the end, and you're getting very very very close to the best that we know how to do with self- with uh fully supervised learning. Okay, but what about the speed issue? This is still n to the fourth power. Uh it turns out that people are care a lot about attention. So, in the LLM world, we start introducing these tools, uh flash attention, the biggest one, and uh Hera explicitly showed a speedup for the same accuracy versus VIT, but they have a

**[9:55](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=595s)** note in their paper where they where they say, "Okay, we see the speed up and we're not going to measure with flash attention." So, then you add back in flash attention, suddenly it doesn't really matter. You've got you're back to this very silly ends end of the fourth power thing that benefits from this VIT specific pre-training method, and that's it. We're uh we've kind of we're we're we've kind of won. So, this is a a talk about this is a an evolution of the backbones. How it is how it is that the end of the fourth thing ended up beating out everyone that tried to beat it. What does this mean in practice and application? So, SAM is a very famous series of models.

**[10:46](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=646s)** Again, if I I I don't know where people come from, but SAM was a what from my perspective one of the most important uh foundation model series in vision period. And we actually see the same pattern. So, SAM to mobile SAM to SAM 2 to SAM 3, if you look at the backbones that are underlying it, it's a VIT trained with MAE. Then someone says, "Okay, well, surely this cannot be the best that we can do." So, they uh mobile SAM actually uses a specialized convolutional transformer hybrid uh called tiny VIT and replaces the the VIT backbone. And then SAM 2 actually uses Hera with uh this MAE pre-training, and then SAM 3 just gives up on the architecture ablation and just says, "Okay, well, we've got this massively

**[11:34](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=694s)** pre-trained backbone. Let's just stick it in. That's the best that we can do." Um So, that's all good and fine, but where does that actually leave us? Um this is really expensive if we're relying on these huge pre-training strategies in order to recover the performance that is lost due to the fact that our architecture is not biased towards the subject at all. Uh that means we have to spend a huge amount of money every time we want to do a deployment. So, no deployment flexibility means that we have these one-size-fits-all models. So, SAM 3 is this very very powerful thing, but is also 800 million parameters. It takes 300 milliseconds to run on a T4 GPU.

**[12:23](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=743s)** It's not actually usable in a lot of cases, uh especially because vision historically has been focused on these very low-power edge devices, these uh resource constrained deployment scenarios. So, uh at Roboflow, what we have done is we've attempted to say, "How do we actually take these fixed foundation models and to transform them into something that has flexibility?" So, we introduce a data set, RF100VL, that measures how well uh foundation models transfer to downstream diverse tasks with respect to object detection, which is one of the canonical vision-centric

**[13:11](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=791s)** tasks. And we see about a 40x speed up for the same accuracy versus fine-tuning SAM 3, uh and for merely a 15x speed up, we get a a meaningful improvement. Um So, this combination of this huge advancement in foundation model pre-training and these strong deployment methods combined with uh an actual ability to deploy these in hardware constrained environments ends up being the uh uh final nail in the coffin for these classical convolutional-based methods. Uh these at the time of our publication of RFDetR, these were the best convolutional

**[14:00](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=840s)** uh these were the best real-time instance segmentation models, and we uh we we we we outperformed them in a in a meaningful way. Uh Um and so, this is all those models on that line use actually the same foundation model. We just modify the foundation model using neural architecture search such that we generate an entire family of uh high-performance models in in one go. To do this, we actually introduce a bunch of uh flexible knobs. All of these are drop-in compatible with the existing foundation model infrastructure, and by mixing and matching them in a way that is dependent on target data and target hardware,

**[14:47](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=887s)** we can uh resolve the issue that uh these foundation models do not have deployment flexibility. Um So, massive VIT specific pre-training plus speed ups from LLMs plus uh pre-training compatible neural architecture search, and uh that's it. Do we have architectures that support like video or video plus image plus text pre-training already? Is someone working on that? So,

**[15:35](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=935s)** there are a lot of people working on like a huge amount of different combinations of things. I actually think SAM 3 is a good example of that. They do Well, in terms of in terms of vision-specific video processing, it does video processing in the in from the perspective of tracking objects through video. So, they do massive-scale pre-training. They do the perception encoder pre-training for the backbone, and then they do a huge amount of downstream pre-training. Or I guess you would just call it training at that point. Um What about JEPA like Yeah, the video Yeah, JEPA and the VJEPA, those are uh I mean, yeah, those are another variety of foundation model. I think in terms of single like image-centric pre-training, JEPA doesn't seem to outperform a lot of

**[16:26](https://www.youtube.com/watch?v=VhfAVA3BG2I&t=986s)** the other ones. Video JEPA, I haven't seen anyone use it meaningfully in a video context for downstream transfer yet, but you know, we'll see. Yeah. Yeah. Any other questions? Cool. Okay.
