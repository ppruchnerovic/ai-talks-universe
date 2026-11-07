---
id: br66tabsgN4
title: "USENIX Security '26 - Inference Attacks Against Graph Generative Diffusion Models"
slug: usenix-security-26-inference-attacks-against-graph
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 15
published_at: 2026-11-04T22:47:57Z
video_id: br66tabsgN4
url: https://www.youtube.com/watch?v=br66tabsgN4
youtube_url: https://www.youtube.com/watch?v=br66tabsgN4
tags: []
topics: ["Inference, serving & GPU infra", "Multimodal, vision, speech & robotics", "Security, safety & red teaming"]
transcript: true
---

# USENIX Security '26 - Inference Attacks Against Graph Generative Diffusion Models

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=br66tabsgN4) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '26 - Inference Attacks Against Graph Generative Diffusion Models

Xiuling Wang and Xin Huang, Hong Kong Baptist University; Guibo Luo, Peking University; Jianliang Xu, Hong Kong Baptist University

Graph generative diffusion models have recently emerged as a powerful paradigm for generating complex graph structures, effectively capturing intricate dependencies and relationships within graph data. However, the privacy risks associated with these models remain largely unexplored. In this paper, we investigate information leakage in such models through three types of black-box inference attacks. First, we design a graph reconstruction attack, which can reconstruct graphs structurally similar to those training graphs from the generated graphs. Second, we propose a property inference attack to infer the properties of the training graphs, such as the average graph density and the distribution of densities, from the generated graphs. Third, we develop two membership inference attacks to determine whether a given graph is present in the training set. Extensive experiments on three different types of graph generative diffusion models and six real-world graphs demonstrate the effectiveness of these attacks, significantly outperforming the baseline approaches. Finally, we propose two defense mechanisms that mitigate these inference attacks and achieve a better trade-off between defense strength and target model utility than existing methods. Our code is available at https://zenodo.org/records/17946102.

View the full USENIX Security '26 program at https://www.usenix.org/conference/usenixsecurity26/technical-sessions

## Transcript

*1,599 words · source: supa (en, exact timings)*

**[0:19](https://www.youtube.com/watch?v=br66tabsgN4&t=19s)** Hello everyone. I'm Shirley Momoh and I'm going to present our paper inference attacks against graph generative diffusion models. This is joint work with and Professor Hong Kong University of Science and Technology and Professor Gu from the University. Graphs often encode sensitive information. We know social graphs may reveal private relationships and behavior patterns as illustrated by 2018 Facebook Cambridge Analytica scandal. And by biological graphs may contain proprietary discoveries and tracing rates of medical knowledge such as My Heritage private BRCA variant database

**[1:10](https://www.youtube.com/watch?v=br66tabsgN4&t=70s)** and also has graph settings and so on. Graph neural networks are vulnerable to privacy attacks that leak sensitive information about the training graph data. A typical example is that users train the model with their own data on a training adversary's platform and then the attacker can obtain certain information about other users' data by carefully crafting input data that causes the platform to reveal information about other users' data. This paper will focus on privacy leakage in graph generative diffusion models. So first I'll briefly introduce the graph generative diffusion models which aim to learn the underlying distribution of real data and generate realistic synthetic samples.

**[1:58](https://www.youtube.com/watch?v=br66tabsgN4&t=118s)** These models include a forward process and a backward process. reverse division process. The forward process would rather add noise to our general graph on multiple time steps, so the model catches how the graph change at different noise levels. The reverse process starts from a noisy graph and it progressively removes the noise, so the model learns to generate models that approximate uh the forward version dynamics. Once the reverse process is learned, the model can start from noise and generate simulated graphs. Here are some examples of the training graphs and generated graphs. We use three separate emails where emails can weather there's ambiguity of the training graphs from these and generated

**[2:47](https://www.youtube.com/watch?v=br66tabsgN4&t=167s)** uh and generated graphs. So, this is a black box attack. So, we design three different types of inference attacks against the generated diffusion models. We uh abbreviated graph generated diffusion models as GGDMs. The fundamental idea here is that if the target model memorizes the real graph, it is likely to generate multiple similar graphs to this graph. First, we assume the attacker has an op- optional set of graphs that contain their own graph structures and distributions, uh which may be different from the training set. The attacker has black box access to the target model, which means he can only access to the model's output.

**[3:37](https://www.youtube.com/watch?v=br66tabsgN4&t=217s)** Then, the attacker can gather a set of similar graphs that can capture the distribution between that. Then, uh we do the three types of attacks which aim to recover generated graph structure, inference on the property of degree density uh of the training graphs, and infer whether the target graph is in the training set. There are two challenges here. The first is that the language team finds a time for the graph network. For different graph models, I think the attacks there is no one to one mapping between the input graph and output. Won't have feature construction. And second, the previous attacks against generative models mainly focus on attacks on image data. These attacks cannot be generalized by cheating

**[4:26](https://www.youtube.com/watch?v=br66tabsgN4&t=266s)** the graph based on that because of the structural complexity of the graphs. The challenge is the large size of the prediction environment and structural complexity. I've introduced the backgrounds, motivations, and types of attacks. Next, I'll introduce our attack models. The attack [clears throat] reconstruction attack includes steps: graph generation, graph alignment, and graph inference. >> In the sub graph generation, the

**[6:50](https://www.youtube.com/watch?v=br66tabsgN4&t=410s)** attacker inputs a set of shadow graph GS into target GDM model by all executed by the rating difference, obtain a set of sensitive graphs and GJs. Here, this is why I'm going to attack the shadow graph in option. Um then, for each GI generated graphs, we identify the most similar graph GJ to GIN, line them with algorithm called Rego. After identifying all the line pairs, we select the top 10% most similar graph pairs GI and GJ to reconstruct target graph structure, where the reconstructed nodes are the most similar of GI and that are in the intersection

**[7:38](https://www.youtube.com/watch?v=br66tabsgN4&t=458s)** edges in GI and GJ. Okay next. Uh let's take a look at the second attack, the property inference attack, which aims to infer predefined properties or aggregate characteristics of individual records or a group within the attribute set. This attack illustrates that the graph generation and computing properties of many graphs and property inference. For web generation, the attacker uses a set of shadow graph GS into target GDM model 5. Or ask you by the relative 10 as sudden celebrity wrong GS. For target of TP with the relative computer P from GS, we can say there two types of wrong diseases paper. The first one is the average statistical

**[8:27](https://www.youtube.com/watch?v=br66tabsgN4&t=507s)** properties which mean which is the mean value of the celebrity wrong and the the ensemble of the distribution of the probability ranges in which we can do the frequency and the ratio of the celebrity wrong per probability range. Regarding the estimated probability of the chain wrong of that of the celebrity wrong. Okay, the last point is the membership inference attack which is energy determined whether the given wrong is a true set. It includes first of all the shadow model training and wrong generation. Attack feature construction, the shadow model training and shadow inference. Regarding first of all, the attacker trains a shadow GDM using memory shadow wrong. And choose their memory wrong as members. And then

**[9:15](https://www.youtube.com/watch?v=br66tabsgN4&t=555s)** generates a sudden celebrity wrong on condition on each member or non-member shadow wrong GS. Second, for each shadow wrong GS, the attacker has started the feature reading a number of working bodies from a of the S. And of course the magic features mainly in dot product. Because I think the similarity between distance and generation diversity, we consider two types of the attack features. Try to generate some celebrity which is based on the first principle that member wrong are more similar to their generated samples than non-members. The second one is generate two generated similarity. Um which is based on the principle that samples generated from member wrong is in the high parallel

**[10:05](https://www.youtube.com/watch?v=br66tabsgN4&t=605s)** with similarity compared with the non-member wrong. For each pair of the input and generated wrong also have similar values of combined to one of that feature. To the attacker, um change the attack classifier by the numbers and numbers features and blocks. In the influence of that a stop, um given a target graph that that release the target distribution with the type graph and fast charges attack utility, then we have a dynamic option phase. This is then in order to obtain that that classifier to obtain the membership. We model attack um stream widely using the down models and find the sets. The graphic construction we use two batch images, average F1 which calculate the

**[10:54](https://www.youtube.com/watch?v=br66tabsgN4&t=654s)** link overlap between the reconstructed and trimmed graphs of all aligned pairs and the coverage ratio of the above in the added match rates. From table we observe that the reconstructed graphs of the signature graphs in Jimmy said always average F1 ranging from 0.78 to 0.9 and the exact match rate ranging from 0.03 to 0.22. Regarding property inference performance, on the average property we measure the absolute difference in average node degree and and density between the estimated property and the real property and find that the difference is quite small, less than 0.312 and 0.049.

**[11:44](https://www.youtube.com/watch?v=br66tabsgN4&t=704s)** The average node degree and density is about to be. And the bottom figure show that the inference distribution close alignment with the solution result. Regarding membership inference of performance, which is measured as attack AUC, we observe that our attack two which is the black box attack from the baseline white box by most of the settings. Um okay, after introduce attacks, now let's I introduce the two defenses. Um the first of edge deletion of our defense strategy elective flipping edges and non-edges that are deemed least important. But the the approach minimizes quality loss of original graphs while providing

**[12:33](https://www.youtube.com/watch?v=br66tabsgN4&t=753s)** sufficient privacy protection against these attacks. We design two defenses noisy training graphs and noisy generated graphs which achieve good results. Step one, uh rank edges and non-edges by importance which we do that by using the signing small. Step two, we flip the least important edges or non-edges. And step three, we update the train predictor to the original graph and and repeat step one just re-entering the chain with the budget. Then we can tune the GGDN on the predictor graphs or on the predicted graphs. Um from the right figure, we can see that first our pre-evasion master highly valued against all straight out of the box. This really uh

**[13:22](https://www.youtube.com/watch?v=br66tabsgN4&t=802s)** reducing the performance. And second, one defense performance dropped below 0.6 for GIA, MIA1, and MIA2 which indicates uh ineffectiveness of the attacks. Our attack mainly fire more model utility compared to the baselines. Um with degradation less than 0.05. So, to summarize, graph diffusion generation are powerful but not privacy free. Um our MIA, PIA, and structural structural leakage attacks revealed complementary risks. And perturbing training and auto encoder by flipping the least important edges and non-edges offer provided defenses

**[14:12](https://www.youtube.com/watch?v=br66tabsgN4&t=852s)** with favorable privacy utility tradeoffs. So, we save the end of my talk. Thank you for your time and to Toshi. I'm happy to take questions. If you have any questions, just email me. Thank you very much.
