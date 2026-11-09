---
id: Dm1xeKOzfP4
title: "USENIX Security '26 - Identifying Provenance of Generative Text-to-Image Models"
slug: usenix-security-26-identifying-provenance-of-generative
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 13
published_at: 2026-10-28T01:28:26Z
video_id: Dm1xeKOzfP4
url: https://www.youtube.com/watch?v=Dm1xeKOzfP4
youtube_url: https://www.youtube.com/watch?v=Dm1xeKOzfP4
tags: []
topics: ["Evals, observability & reliability", "Multimodal, vision, speech & robotics", "Security, safety & red teaming", "Training, fine-tuning & model building"]
transcript: true
---

# USENIX Security '26 - Identifying Provenance of Generative Text-to-Image Models

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=Dm1xeKOzfP4) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '26 - Identifying Provenance of Generative Text-to-Image Models

Anna Yoo Jeong Ha, Wenxin Ding, Stanley Wu, Shawn Shan, Haitao Zheng, and Ben Y. Zhao, University of Chicago

Fine-tuning provides a fast and cheap way to produce new text-to-image models that are often indistinguishable from ones trained from scratch. Unfortunately, misrepresentation of fine-tuned models creates problems for AI companies and users alike, by disincentivizing competition and misleading users on model quality and ethics of its training process.
In this paper, we propose a model provenance system that identifies models produced by fine-tuning on existing text-to-image models, using only black-box query access. Our design is informed by analysis showing that one can quantify the feature space difference between text-to-image models by analyzing their responses to detailed prompts. Our system analyzes model output, extracts visual features using a generic feature extractor, and compares their distributions against those from a reference pool of base models using Jensen-Shannon divergence. Applying statistical hypothesis testing then determines if a target model is trained from scratch or fine-tuned, and if the latter, the likely base (parent) model. We evaluate our system across seven widely used diffusion models and numerous fine-tuned variants. Our results show high accuracy in attributing model lineage, even under adversarial conditions such as image post-processing or weight perturbations. Finally, we demonstrate real world efficacy of our system by tracing provenance of in-the-wild models from popular online platforms.

View the full USENIX Security '26 program at https://www.usenix.org/conference/usenixsecurity26/technical-sessions

## Transcript

*1,398 words · source: supa (en, exact timings)*

**[0:18](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=18s)** Hello, I'm Anna from the University of Chicago. Today, I'll be presenting my work identifying providence of generative text-to-image models. This is joint work with my labmates, Wenxin, Stanley, and Shawn, and my advisors, Heather and Ben. New text-to-image models are released constantly, and they're usually described as new, proprietary, or trained from scratch. But, with black box access, how can we verify those claims? We see only the generated images, not the model's weights, training data, or training history. That is the model provenance problem we tackle. Well, why does it matter?

**[1:06](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=66s)** There are several situations where someone may need to verify a model's provenance. For example, if a model is leaked or stolen, the owner needs a way to detect if that unknown model is actually derived from theirs, whether it was fine-tuned, repackaged, or released under a different name. If a provider claims a model is ethically or independently trained, we need a way to verify that claim, instead of just taking it at face value. And if a suspicious model service appears in the wild, investigators need to trace which model it came from. So, provenance matters in several different settings,

**[1:53](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=113s)** and all three cases come down to a single core question. Where did this model come from and was it fine-tuned from an existing model? Most existing provenance tools usually require stronger assumptions. Watermarking requires the model owner to embed a signal. Fingerprinting instead uses requires white box access to the base model to create a model specific adversarial prompt. And these specific signals or responses can also become unreliable after fine-tuning. So, they either require collaboration from the model owner or the signals are unreliable. And instead, our method compares the

**[2:44](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=164s)** models overall feature space distribution using only model outputs. So, this brings us to the main question behind our paper. Can we determine if a model was fine-tuned from a known base model? And importantly, can we do this purely from generated outputs? And to answer that, we first need to define the setting we operate in. First, we have a target model that we're trying to find the provenance of. The trainer either trains the target from scratch or fine-tunes an existing base model, then releases it through black box access. And we have provenance investigators,

**[3:33](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=213s)** which is us. We have a pool of verified candidate base models. We send prompts to the target model and collect the generated images that it returns. We then compare those outputs with outputs from the candidate base models. There are two possible cases. The target may have been fine-tuned from one of the candidate base models in the pool. Or it may have no parent model in the pool. Either because it was trained from scratch or because it was fine-tuned from a base model that's outside of our pool. And our method supports both decisions. The first key insight is that training

**[4:23](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=263s)** from scratch and fine-tuning affect a model very differently. Independently trained models may use different training data, architectures, and training procedures. So, they produce distinct feature space distributions. So, base model A and base model B can have very different underlying structures. Fine-tuning, however, doesn't rebuild the model's learned representation from the beginning. It modifies the model's behavior while preserving a lot of the statistical structure inherited from the parent model. So, if a target model was fine-tuned from base model B,

**[5:13](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=313s)** we expect its output feature distribution to remain much closer to B than to an independently trained model like A. Now, if fine-tuned models preserve inherited structure, the next question is, how do we observe that structure? We can't inspect the model's internal representation directly. So, prompts let us probe its behavior through generated outputs. Using the same prompt across models gives us a controlled way to sample and compare the feature space distributions. When we probe independently trained models using the same prompts, their output distributions can differ because

**[6:02](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=362s)** of the different structures they learned during pre-training. But when a model is fine-tuned from a base model, those same prompts produce similar distributional patterns because a lot of the parent model's statistical structure is still preserved. So, with using same prompts, independently trained models produce different response patterns, while fine-tuned models remain similar to their base model. And that similarity becomes our provenance signal. Choosing the right prompts is important for making provenance reliable. First, we use common and popular objects like cakes, surfers, and that appear

**[6:53](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=413s)** frequently during pre-training. Because these concepts are well represented in the training data, the model has learned stable feature space representations for them, making them much closer and much harder to change through fine-tuning. But common objects alone are not enough. Image generation is inherently stochastic. These images were all generated by the same model using the same short prompt, a photo of a cake. But they look very different in composition, style, and details, with one being a chocolate cake and another one being a slice of cake. The generations become very noisy,

**[7:42](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=462s)** making provenance comparisons less reliable. Instead, we use detailed prompts. These four images were also generated by Flux using the same detailed cake prompt. They're not identical, but their content and composition are much more consistent. Reducing variation within a model makes differences between models easier to detect. We repeat the test using other common objects, so the method doesn't depend on one special prompt. Now, let's put everything together. We begin with the unknown target model MT. We also have a pool of known candidate

**[8:30](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=510s)** models. Here, I'll use two, M1 and M2, as our candidate base model. Using the same prompt for every model, we generate 100 images from each model. We want to compare distributions here, rather than individual generations. Next, we extract S3 clip features from those images and reduce the dimension, giving us a feature space distribution for each model. Third, we compare the target model's distribution against each candidate base model's distribution using Jensen-Shannon divergence. This equation represents the divergence between the outputs of MT and M2 under

**[9:20](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=560s)** prompt P. A smaller value means the two output distributions are more similar. And here, the target distribution is much closer to M2 than to the unrelated model M1. If the target was fine-tuned from one of the candidate models, we expect its parent to produce the smallest distance. And finally, we determine provenance. We use the base-to-base distances to construct a statistical threshold using a Z-test. We compare the target against every candidate model, and if the closest candidate falls below the threshold, we identify it as a likely parent.

**[10:07](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=607s)** And in this case, that will be M2. Otherwise, we return null, meaning the target was either trained from scratch or derived from a base model outside of our candidate pool. The main result is that the separation is very clear. Fine-tuned models stay much closer to their parent model than to other independently trained models. And on the left, we start with SD21 as the base model. The X axis shows multiple fine-tuned variants of SD21 under different training configurations, like training amount of training data, and the number of epochs. The Y axis shows the JS distance to the original SD21 model on a log scale.

**[11:00](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=660s)** Notice that every fine-tuned model stays clustered very close to its parent. Now, compare that with the independently trained models on the right side of the plot. There is a large separation, and because the Y axis is in log, the numerical gap appears much larger, is actually lot much larger than it appears. And on the right, we see the same pattern for base model Flux. Fine-tuned Flux models remain substantially closer to Flux than to any unrelated base model. This gives strong evidence that fine-tuning changes model behavior, but doesn't completely erase the underlying statistical structure inherited from the

**[11:50](https://www.youtube.com/watch?v=Dm1xeKOzfP4&t=710s)** parent model. So, to wrap up, fine-tuned models retain measurable traces of their parent model, and we can detect those traces using only generated outputs. We also evaluated robustness to countermeasures. We tested weight perturbations and adaptive image-based attacks, and neither was enough to erase a provenance signal without introducing significant trade-offs. We also tested the system on in-the-wild models and identified the true base models correctly. We also had the opportunity to use it in a real-world legal investigation. Thank you.
