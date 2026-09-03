---
id: 0i8UhpUgw_0
title: "Black Hat USA | LLMs-Driven Automated YARA Rules Generation with Explainable File Features & DNAHash"
slug: black-hat-usa-llms-driven-automated-yara-rules-generation
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2026
speakers: []
channel: "Black Hat"
duration_min: 25
published_at: 2026-03-07T14:00:04Z
video_id: 0i8UhpUgw_0
url: https://www.youtube.com/watch?v=0i8UhpUgw_0
youtube_url: https://www.youtube.com/watch?v=0i8UhpUgw_0
tags: []
topics: ["Governance, ethics & regulation", "Security, safety & red teaming"]
transcript: true
---

# Black Hat USA | LLMs-Driven Automated YARA Rules Generation with Explainable File Features & DNAHash

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=0i8UhpUgw_0) · [Conference site](https://www.blackhat.com/)

## Description

Malware on the cloud is growing massively every day, and an automated rule generation solution is needed to improve operational efficiency. YARA is a widely used tool for creating malware signatures and detection rules, however, existing YARA-based automated rules generation solutions suffer from limitations in three key areas: rule quality, false positive rates, and the interpretability of features. These shortcomings restrict their effectiveness in real-world malicious threat detection scenarios.

In this presentation, we will introduce LLMDYara, which is an automated rule generation solution that integrates expert knowledge with large language models. We first utilize expert knowledge to pre-extract string, function, and file DNAHash features. Subsequently, we design a function signature algorithm and an efficient querying similarity search mechanism to filter these features against a billion-scale white database, thereby enhancing feature quality. We then leverage large models for string feature evaluation and functional identification of function fragments, where the latter enhanced the interpretability of opcode features. Finally, we generated YARA rules through an ensemble decision based on selected features. Our newly introduced file DNAHash feature ensures rule usability even when other features have lower quality, further reducing false positives.

Our automated rule generation solution has made efforts to address challenges such as reducing false positives, enhancing feature interpretability, and improving rule quality. Additionally, we will share our experiences in feature engineering and large language model fine-tuning, with the hope that these insights will help advance the application of large language models in the program analysis domain.

By:
Xiaochen Wang  |  Security Engineer, Alibaba Cloud
Yiping Liu  |  Security Engineer, Alibaba Cloud
Xiaoman Wang  |  Security Engineer, Alibaba Cloud
Cong Cheng  |  Senior Security Engineer, Alibaba Cloud

Presentation Materials Available at:

## Transcript

*2,770 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=2s)** Uh good afternoon everyone. My name is Wango. Today I would like to present our work on I am diara driven automated yara ros generation with explanable features and dashi. Uh first please allow allow me to introduce our team. We are from Alibaba cloud, one of the most leading cloud storage providers, globals. Uh this work involves four researchers. First my co-speaker Liu Eping who will later present the second part of this work. Uh in addition to her, we have two other contributors uh Wang Xiaom and Chong uh who could not be with us today. uh they

**[0:50](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=50s)** are both excellent security engineers engineers and all of us currently work on malware wire analy analysis at Alibaba cloud security uh when it comes to to the mire analysis in recent years the number and the diversity of mire have been global growing rapidly it's more difficult for security analysts to rely on traditional uh manual methods for raw based detection. As a result, automated row generation methods have been proposed. Uh most existing automated row generation methods focus on YAR rows uh which are the most common static

**[1:39](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=99s)** detector to there are there's approach use machine learning or deep learning to extract static features. uh for example uh yard focus on stream based features while the uh autoarara handles battle sequences well. However, they still face challenges in raw quality false positive rates and the interpretability of features. To address this issues, we propose our solution. In summary, we f the same following challenges. Uh first, how to reduce the false positive and improve raw quality. Second, how to make selected features more interpretable. For example, we hope

**[2:30](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=150s)** the selected features have meaningful sematics and related to the sensitive behaviors. Uh finally, large models show strong performance across domains. However, how to along their prediction for automated RO generation is a still major challenge. Uh so in light in light of this challenge, we will introduce our solution method. First we broke down the task into four parts. uh feature extraction, feature filter, feature decision by large model and the raw generation. Specifically, this is the framework of um Diara

**[3:20](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=200s)** as shown in a picture feature extraction models extracts three types of features string function and field in high features. Uh then the next uh filter model use a pre preolcted benign simple database to filter string and dehy features and identify third party or sensitive codes to filter function features in the feature decision model. A large large model is used to select string features identify fun function behavior and extract op code sequences. Finally, the last model generation rules based on the evaluation results and the feature distribution. Now I will uh present each

**[4:12](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=252s)** model by addressing the problem and the corresponding solution. First is the feature extracting model. Uh string features are common commonly used in the yara ros. So how to define and extract high quality strings? Um we first define uh 17 IOC related string patterns and extract these features and it is based on our expert knowledge and we then collect all strings with a minimum length of six characters. uh to improve the meaning meaningless strings an AOP model is designed to identify natural language strings.

**[5:01](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=301s)** Overall the string features in um they are uh classed into two types. Uh the first is IOC related strings and the next is natural language strings. So uh besides the string features what other features can be extracted? Uh the first idea to cameas was extract function features since large models are better suited for uh analyzing decompiler code but the generation rules are based on the assembly code. So it's important to connect them. Therefore during uh feature extraction we include address offsets and the line number information

**[5:52](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=352s)** with the extracted deco compiler code. During the third model the large the large large model will output the line numbers and the size of the selected sequences by using the offset information. A mapping to the corresponding assembly code can be est established. A more detailed est explanation of this process will follow in the third model. Uh notably if the function uh decomplion the assembly code. Additionally uh a faction call graph is extracted partly to provide the large model to with the connection information

**[6:43](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=403s)** and the other is to assist in generating rules uh more details will be also given in the raw generation part. However, uh in the presence of challenges such as uh selfodering code, string and function features are not yable. Uh so what alternative features can be used while controlling false positives to address this issue? Uh we introduce a new feature called a field in hy feature. The feature uh calculate hy values for different parts of the binary field based on its structure result in a set of field high features.

**[7:34](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=454s)** Uh so the feature extraction model uh provide an initial set of features to make the large model work. First IMDR address a feature filtering step as the second part for stream features. We observe that there are many of interest in the natural language stream. uh to improve more information for raw generation we filter deeply these strings into most specific subtypes such as sensitive uh APIs format strings and so on. In addition, we maintain a benign simple report at the several mailing scale by building a feature database. From these benign samples, we filled out

**[8:22](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=502s)** string features that top frequently match them. However, that is a one point to note. A single feature matching to bite its is not a concern uh because many fe such features may together form a gold rule to detecting more wire uh for function features. The question is how do we decide which functions are more valuable? However, define what makes a function valuable or sensitive is a not easy task. After all, if we have already the valuable function features, we just uh generate the detection rules. Uh so we filter the function features from positive and

**[9:14](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=554s)** negative aspects and the resulting functions are called a suspicious sensitive functions. First we aim to fill out a library functions. On the one hand we can directly use the uh capabilities of the uh disassembler such as some APIs of IDA. On the other [snorts] hand we design a function signature algorith called finger and build a third party function signature database. So we use this signature based approach to field out the library functions. In addition we aim to directly identify some suspicious sensitive functions. First we start from the main function

**[10:04](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=604s)** and extract the sub functions it calls. Second, we use open source static raw match tool called kappa and apply its rules to mark partitionally sensor functions. Third, we design a function importance evaluation algorithm to select the functions that call most more strings or are called more frequently. By com comparing s signature based filter ring and the collection of suspicious functions, we complete the filtering of function features. Uh after filter feature filtering we expect the large model to provide a decision making information for row

**[10:53](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=653s)** generation for screens. We ask the large model to select the top key uh useful features for row generation. However, our test shows the large model are not good at such specific task. So how to fine-tune the large model? First, we can construct a database using yara rows accum accumulated over the over the past years and select many strings from the benign symbols. During fine turing, we first use SFT model SFT method to help the model understand the task and follow the designed output format. We then apply the GPO method to adjust the

**[11:43](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=703s)** model. Finally, we resolve two issues, unexpected features and invalid output format. Uh next, um my co-speaker Li Pin will present the left part. Thank you guys. Uh function features are important for creating explainable rules with low force positives. Uh so what what types of functions and which op code sequence within them uh can be used as function as function features in yava rules. uh our rule generation framework

**[12:33](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=753s)** works at the mware family level. So like your jam and autoara which looks for common streams or shared binary by we first clasper clustered functions AC across family samples with the SSD hashio of function content. Uh then we picked the cluster centers as representative functions and feed them into the arm for analyze. Uh we break down area analyze task into three steps. Uh first analyze the given pseudo code and contest information. Uh second based on the analyze label the function and explain the reason and

**[13:22](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=802s)** third select the code segments from the function that are suitable for generating our rules. Uh in the proont of taxport uh we provide a series of labels and explanations for common malicious behaviors. Uh if the model believes a function matches one of these behaviors, it should give the representative label. Uh besides the pseudo code, we also give the function contest information uh such as kapa labels of its sub sub functions and the global vari variables it refers to help analyze the function. Uh for the model output,

**[14:11](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=851s)** it should include the function label and the explanation and the line numbers and length of the code segment uh suitable for a part of Yara rules. And the left bottom is an example from a backdoor mware family. Uh this function performs an hour decor uh decorion operation. This model suggest line line 19 to 25 is suitable for OB code feature. Uh this family was covered by by our human experts handwriten rule before and they used the assembly instruction at line 20 in the in the same function as one of the key features uh which is also

**[15:00](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=900s)** included in the area suggestions and after getting the models suggested line numbers uh we first map these pseudo lines back to the corresponding assembly code. This assembly functions may not be continuous. Uh we then convert the OB code sequence into Yara signature. Uh applying wild cars to dement and removing uh stack balancing instructions at the end and and or the beginning of the functions. And the uh here is an example from pseudo code to Java signatures. Uh through our experiments, we found that queen 3 uh queen 32B

**[15:51](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=951s)** model performs very well in in identify function behavior and assigning correct labels based on pseudo code and the contest information. Uh however if there are street requirements on model response speed or the cost we suggest use quinctory as a teacher model to generate a high quality training data for funuring smaller models. Uh the label information come from two sources of the dyn the dynamic behavior sandbox and capacic analyze. Uh these sandbox provide ground truth behavior labels for each training sample and we can use queen tree model to label the functions

**[16:39](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=999s)** in our training set. If the model's label is in the list of behavior detected by the sandbox, uh we will keep the function and the corresponding label. Uh in this way we can build a data set of real function pseudo code with with accurate labels uh ready for training smaller models. Uh after the feature extraction uh filtering and selection stages we will get high quality features for each sample in a marrier family. uh for OP code and stream features we use a two-dimension clustering uh method based on both files and features to find the frequent patterns within the family and

**[17:31](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1051s)** uh for DNA hashy feature we apply a hyeratic clustering uh setting the maximum number of different hashy segments between files to identify shared hashy segments across file Uh once the clustering is complete for all three feature types, we will combine the results with uh rule scoring mechanisms designed for each feature type and generate the error rules. uh if situations where there are strict requirements on rule count and the file size for example in our business uh situations uh rules need to be update and deployed frequently. Uh there is a rule compre compression part including

**[18:22](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1102s)** two steps uh subset compression and the intersection rule margin. Uh this helps combine similar frequent patterns and reduce the total number of rules. Uh here below are two examples from the final Yara rules generated by our system and uh this one is in the button is the native native version and the other includes the DNA hy module. Uh the experiment part in the experiment we compare our rule generation method with two open source tours uh YJ and Autoara the compare comparison includes detection rate and false positive rate

**[19:13](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1153s)** on our collected set of 2.3 million benign samples. uh to ensure a fair comparison we remove the f the feature filtering step in AMD Yara in all experiments uh this avoids any advantage from using a large set of clean files during training uh which the other tools don't have access to in experiment first we use a public mware data set collected from three open sources after 2025. Uh for each family, we randomly picked one/ird of the samples and up to the maximum of 1,000 as the training set and use the rest as a test set.

**[20:05](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1205s)** Uh here we show the detection performance of three tools on the top of 60 families by uh sample count for both training and test sets. Uh the head map the heat map below shows detailed detection results on the top 30 families. Uh as you can see Java performs better than the other two tools in both the training and test sets. And on the left is a bar chart shows the average detection rate across all families. uh yj on the line gn refers to uh yjam's simple rule mode which allows to generate simple rules for files including included in super rules while

**[20:56](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1256s)** this mode behaves uh achieves a high detection rate. It also produce significantly more false positives compared to the other tools. We separately evaluate LMD Yara's native Yara rules mode and the uh versions enhanced with DNA hashi. Uh the results shows that DNA hashi can help improve the detection rates. Uh but even when using only the native yara rules without da hashi yara still performs better than your gen and auto yara. Uh here we test the rules generated by the three tools against our collected

**[21:44](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1304s)** benign sample data set to measure the false positives as shown in terms of both the numbers of false positive samples per family and the total number of false positive samples. MD Yavar performs significantly better than the other two tools. And these results shows that using interpretable function level features can help reduce force alarms, making the generated rules more precise and reliable. And here is a detailed example of a rule generated by the three tools for one one family among the top 20 uh 30 recent active marriers. uh in this family the

**[22:36](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1356s)** common string across samples system API names uh this string are filter out by yara that by your jam's built-in string w list so your gem has to rely on the rare and special strings that appear only in a few samples uh this results in a low carriage for this family uh although yara's rules also use this API streams uh it include the tower dete decraption function as a key feature. Uh this allows the rules to achieve a 100% detection without any false positives in the benign sample dete data set. Uh autoara also performs well on this family. However, uh AMD Yara's

**[23:26](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1406s)** interpretable rules reveals that the malware family may have behaviors such as self-decorption, process injection, and modify files or registries. Uh information that goes beyond the detection. Uh this makes our rules not only effective for detection but also useful for explaining alarms in real world situations. uh we noticed that autoara's paper provide the data set used in their experiments. So we also run the same comp comparation on autoara's public data set and the results show that on this data set as well MD yara performs better than the

**[24:16](https://www.youtube.com/watch?v=0i8UhpUgw_0&t=1456s)** other two tools in both detection rate and false positive rates. uh further confirming the effectiveness and the robustness of our approach. And here is the false positive results on the benign data set. And we leave our email here for these who are not on site or for any follow-up questions. And we got >> [applause]
