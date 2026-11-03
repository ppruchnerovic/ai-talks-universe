---
id: WHIc6MMeMEU
title: "USENIX Security '26 - CompLeak: Deep Learning Model Compression Exacerbates Privacy Leakage"
slug: usenix-security-26-compleak-deep-learning-model-compression
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 13
published_at: 2026-10-28T01:28:37Z
video_id: WHIc6MMeMEU
url: https://www.youtube.com/watch?v=WHIc6MMeMEU
youtube_url: https://www.youtube.com/watch?v=WHIc6MMeMEU
tags: []
topics: ["Classic ML & data science", "Evals, observability & reliability", "Governance, ethics & regulation", "Inference, serving & GPU infra", "Security, safety & red teaming", "Training, fine-tuning & model building"]
transcript: true
---

# USENIX Security '26 - CompLeak: Deep Learning Model Compression Exacerbates Privacy Leakage

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=WHIc6MMeMEU) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '26 - CompLeak: Deep Learning Model Compression Exacerbates Privacy Leakage

Na Li, School of Cyber Science and Engineering, Nanjing University of Science and Technology, China; Yansong Gao, School of Cyber Science and Engineering, Southeast University, China; Hongsheng Hu, School of Computer Science, Shanghai Jiao Tong University, China; Boyu Kuang, School of Cyber Science and Engineering, Nanjing University of Science and Technology, China; Anmin Fu, School of Cyber Science and Engineering, Nanjing University of Science and Technology, China; and School of Computer Science and Engineering, Nanjing University of Science and Technology, China
Distinguished Artifact Award Winner

Model compression is crucial for minimizing memory storage and accelerating inference in deep learning (DL) models. Users can access different compressed model versions according to their resources and budget. However, while existing compression operations primarily focus on optimizing the trade-off between resource efficiency and model performance, the privacy risks introduced by compression remain overlooked and insufficiently understood.
In this work that focuses on typical classification tasks, through the lens of membership inference attack (MIA), we propose CompLeak, the first privacy risk evaluation framework examining three widely used compression configurations that are pruning, quantization, and weight clustering all supported by the commercial model compression framework of Google's TensorFlow-Lite (TF-Lite), and first two supported by Facebook's PyTorch Mobile and the open-source toolkit of Microsoft NNI. CompLeak has three variants, given access to the available number of compressed models and/or the original model. CompLeakNR starts by adopting existing MIA methods to attack each individual compressed model, and identifies that different compressed models influence members and non-members differently. When the original model and one compressed model are available, CompLeakSR leverages the compressed model as a reference to the original model and uncovers more privacy by combining meta information (e.g., confidence vector) from both models. When multiple compressed models are available with/without accessing the original model, CompLeakMR innovatively exploits privacy leakage info from multiple compressed versions to substantially signify the overall privacy leakage. We conduct extensive experiments on six diverse model architectures (from ResNet to BERT and GPT-2), and five image and textual benchmark datasets. Our experimental results show that CompLeakMR achieves the best MIA performance on all evaluation metrics, including TPR @ 0.1% FPR, proving that model compression exacerbates privacy leakage.

View the full USENIX Security '26 program at https://www.usenix.org/conference/usenixsecurity26/technical-sessions

## Transcript

*1,372 words · source: supa (en, exact timings)*

**[0:22](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=22s)** I'm Nanli from Nanjing University of Science and Technology. I'm going to present our work complete deep learning model compression exists ways privacy leakage. This is a joint work with Yindong Gao from Southeast University, Hongshuo Wu from Shanghai Jiao Tong University, Boyu Quan and Aimin Fu from Nanjing University of Science and Technology. In this work, we investigate an important but largely overlooked question, whether model compression can introduce additional privacy leakage. Let me first briefly introduce model compression. >> [snorts] >> Deep learning models have become larger and larger, which makes deployment on resource-constrained devices more difficult. Model compression is a common solution to this problem.

**[1:10](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=70s)** It reduces the number of parameters, computation, and memory usage. In this work, we consider three common compression methods. The first is pruning, which removes weights with small magnitudes. The second is quantization, which converts 32-bit floating-point weights into compact lower bit integers. The third is weight clustering, which groups similar weights together and replaces them with shared values. These methods can significantly reduce the cost of model deployment. To elevate privacy leakage, we use membership inference attacks, MIAs. The idea is simple. Suppose a model is trained on private data set.

**[1:58](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=118s)** Given an attacked sample, the attack was to determine whether the sample was part of the model's training set. If it was used for training, we call it a member. Otherwise, we call it a non-member. In our setting, the attacker has black box access to the target model and can observe its output. For [snorts] example, in this figure, the model predicts dog with 95% confidence. Membership inference attack use this output information to distinguish members from non-members. However, the privacy risk of model compression has been largely overlooked. We identify two important issues. First, many compression methods require

**[2:45](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=165s)** fine-tuning on the original training data. This means that compression does not simply make the model smaller. The fine-tuning process may also change how the model memorizes its training samples, potentially introducing additional privacy risk leakage. Secondly, in practice, model providers may release multiple compressed versions of the same model. For example, they may release models with different pruning rates. An attacker may be able to query all these models and then combine the information from them. However, the combined the privacy impact of multiple compressed models remain largely unexplored. This leads to our main research

**[3:35](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=215s)** question. Does compression exist with privacy leakage as access to multiple compressed models grows, and if so, by how much? Now, let me introduce our threat model. As shown on the left, a model provider releases our original model together with several compressed versions. Such as models with 16, 17, and 18% of pruning. The attacker can query every released version. We consider a black box setting where the attacker only observes outputs from the original model and its compressed versions. The attacker also knows the model architecture and the compression configuration. Since this information is usually published by the model provider.

**[4:25](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=265s)** In addition, the attacker has a shadow dataset from the same distribution as the victim's training data, but with no overlap. The attacker uses this side to train shadow models that mimic the behavior of the victim models. Finally, given a tagged sample, the attacker's goal is to determine whether it was part of the victim model's training set. Based on this shadow model, we propose our framework complete, which has three variants according to how many models the attacker can access. The first is complete NR, where NR stands for no reference. Here, we applies existing MI's to one model in isolation. This serves as our

**[5:14](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=314s)** baseline. The second is complete SR, where SR stands for single reference. Here, we compare the original model with one compressed model. By comparing their outputs, we capture the changes introduced by compression. Finally, we have complete MR, where MR stands for multi-reference. Here, we combine information from the original model and multiple compressed models to investigate why the multiple released versions can further amplify privacy leakage. They are supposed to look at a complete analog. Complete analog is not a new technique. Instead, [snorts]

**[6:01](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=361s)** we use six existing MI's to audit the original model and every compressed version independently. These messages include tree-based attacks magic based attacks, and the Sota MI. The purpose here is to establish a baseline and measure how much each compressed model leaks on its own. Now, let us look at the experimental results. We evaluate four datasets with four different model architectures. Cifar with ResNet 18, Cifar 100 with ResNet 15, mini ImageNet with VGG 16, and tiny ImageNet with MobileNet V2. For compression, we consider pruning

**[6:51](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=411s)** from 16% to 19% sparsity, 8-bit quantization, and the weight clustering with four weights and 16 clusters. We report balanced accuracy, AUC, and TPR at 0.1% FPR. Interestingly, we observe that highly compressed models are harder to attack indirectly. For example, as the pruning rate increase, attack performance generally decrease. The reason is that highly compressed reduce model overfitting, making members more similar similar to non-members. However, this is all what we observe when each model is considered in

**[7:39](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=459s)** isolation. And this motivates our next method, complete ISR. This brings us to the key insight of our work. Although a highly compressed model may be harder to attack by itself, compression changes the posterior distributions of members and non-members differently. Look at the figure. Here, we compare the posterior outputs of the original MobileNetV2 and the uh pruned version on the same samples using KL divergence. As we can see, members shift much more than non-members. This difference provides a strong membership signal. Therefore, in complete ISR, we use the

**[8:27](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=507s)** original model as a reference and then compare it with one compressed model. The attack contains five main steps. First, we train the shadow models. Second, we generate posterior outputs from both shadow, original, and the compressed models. Third, we combine these posterior outputs to construct metadata. Also, we use the metadata to train a binary attack membership classifier. Finally, we apply the attack to the victim models and then infer membership. Now, let us look at the results. Regardless of the compression type and level, complete ISR consistently outperforms complete LLR.

**[9:17](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=557s)** Let me highlight one example. For the 19% pruned VGG16, TPR at 0.1% FPR increases from 2.3% to 25.5% These results show that compression introduces privacy leakage and that can be observed by attacking either model independently. Next we consider what happens when the attacker can access multiple compressed versions. This motivates complete MR. Our key observation is that different compressed versions leak membership information differently. We identify two useful signals.

**[10:06](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=606s)** The first signal comes from the complete isometric classifiers. Different compression levels produce different isometric classifiers. And these classifiers make different membership predictions for the same sample. This disagreement itself provides useful membership information. The second signal comes from the loss. As the pruning rate increase, the loss of member samples shows a clear increasing trend where the loss of non-member samples mainly fluctuates. Complete MR combines these signals across multiple compressed models. The pipeline includes shadow model training, post posterior connection,

**[10:55](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=655s)** loss connection, attack method classifier training, and finally membership inference. Now, let us look at the complete MR results. For pruning, we combine four compressed models with sparsity levels from 0.6 to 0.9. For weak clustering, we combine three compressed models with four, eight, and 16 clusters. The results clearly shows that multiple compressed models can further amplify privacy leakage. For all three compression operations are combined with any model seen today. ComLeak MI replaces 95.7% TPR at

**[11:42](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=702s)** 0.1% FPR. With AUC close to 100%. Therefore, multiple compressed models further amplify privacy leakage. To summarize, we propose ComLeak, a framework for evaluating the privacy risk of model compression through membership inference. First, ComLeak MI implies existing MIs. Relying solely on information from the underlying model. ComSize privacy leakage per compressed model. Second, ComLeak IS also side. Compression affects members and non-members equally. Combining a compressed model with the original model reveals additional privacy leakage. Third,

**[12:32](https://www.youtube.com/watch?v=WHIc6MMeMEU&t=752s)** ComLeak MI is also side. Combining information from multiple compressed models can further amplify this privacy leakage. Thank you very much for your attention.
