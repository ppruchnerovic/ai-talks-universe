---
id: gqTWHmChmII
title: "Rich Caruana - Friends Don't Let Friends Deploy Black Box Models"
slug: rich-caruana-friends-don-t-let-friends-deploy-black-box
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2021
speakers: ["Rich Caruana"]
channel: null
duration_min: 51
published_at: 2021-05-18T16:00:19Z
video_id: gqTWHmChmII
youtube_url: https://www.youtube.com/watch?v=gqTWHmChmII
tags: ["Friends Don't Let Friends Deploy Black Box Models", "Rich Caruana", "machine learning", "data science", "mlops", "devops", "deep learning research", "ai", "deep learning", "ml", "artificial intelligence", "mlops community", "machine learning engineer", "automated ml", "ml engineering", "Black Box Models", "friends don't let friends deploy black box models", "intelligible/transparent modeling", "black box", "ml models", "DevOps for ML", "black box model"]
transcript: false
---

# Rich Caruana - Friends Don't Let Friends Deploy Black Box Models

**Rich Caruana**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2021` · `51 min`

`#Friends Don't Let Friends Deploy Black Box Models` `#Rich Caruana` `#machine learning` `#data science` `#mlops` `#devops` `#deep learning research` `#ai` `#deep learning` `#ml` `#artificial intelligence` `#mlops community` `#machine learning engineer` `#automated ml` `#ml engineering` `#Black Box Models` `#friends don't let friends deploy black box models` `#intelligible/transparent modeling` `#black box` `#ml models` `#DevOps for ML` `#black box model`

[Watch the recording](https://www.youtube.com/watch?v=gqTWHmChmII) · [Conference site](https://mlopsworld.com/)

## Description

💻 Abstract:
Friends Don't Let Friends Deploy Black-Box Models. In machine learning often a trade-off must be made between accuracy and intelligibility: the most accurate models usually are not very intelligible, and the most intelligible models usually are less accurate. This often limits the accuracy of models that can safely be deployed in mission-critical applications such as healthcare where being able to understand, validate, edit, and ultimately trust a model is important. We have developed a learning method that is as accurate as full complexity models such as boosted trees and random forests, but even more intelligible than linear models. This makes it easy to understand what a model has learned and to edit the model when it learns inappropriate things. Making it possible for medical experts to understand and repair a model is critical because most clinical data have unexpected problems. I’ll present several healthcare case studies where these high-accuracy GAMs discover surprising patterns in the data that would have made deploying a black-box model risky, and also allow us to learn important new insights from our healthcare data.

🔊 Speaker bio:
Principal Researcher, Microsoft Research
Rich Caruana is a Senior Principal Researcher at Microsoft. His focus is on intelligible/transparent modeling, machine learning for medical decision-making, deep learning, and computational ecology. Before joining Microsoft, Rich was on the faculty in Computer Science at Cornell, at UCLA's Medical School, and at CMU's Center for Learning and Discovery. Rich's Ph.D. is from CMU. His work on Multitask Learning helped create interest in a subfield of machine learning called Transfer Learning. Rich received an NSF CAREER Award in 2004 (for Meta Clustering), best paper awards in 2005 (with Alex Niculescu-Mizil), 2007 (with Daria Sorokina), and 2014 (with Todd Kulesza, Saleema Amershi, Danyel Fisher, and Denis Charles), and co-chaired KDD in 2007 with Xindong Wu.

If you enjoyed this talk, visit us at https://mlopsworld.com/ and come participate in our next gathering! 💼

Would you like to receive email summaries of these talks? Join our newsletter FREE here: http://bit.ly/MLOps_Summaries 📧

Timestamps:

0:00 Intro
0:11 Introducing the host
0:38 Introducing the speaker Rich Caruana
1:39 The importance of intelligibility in Machine Learning for HealthCare.
1:58 Brief history of machine learning
3:32 Accuracy vs Intelligibility tradeoff?
4:10 How interpretable and trustworthy are GAMs?
4:44 Broward interpretable models
5:26 Neural additive models
5:57 EBMs: Type of generalized additive models (GMAS)

Examples I

8:18 Pneumonia Mortality
10:25 What EBMs learn about Pneumonia Risk vs. Age
13:49 Can edit model to fix age- 100 Problem
14:19 Surprising statistical "facts" about pneumonia
16:12 intelligibility can create new medical science
17:41 Treatment effects ubiquitous in all medical data

Example II

17:53 ICU Mortality
18:51 Intelligibility helps debug data: PaO2/FiO2 ratio
19:12 SAPSII Calculator vs EBMs: HIV/AIDS?
20:45 "BMI" for Pregnancy
21:24 COVID-19: Mortality Risk vs. Age
22:42 COVID-19 Mortality Risk vs Gender
23:10 COVID-19 Risk Factors
24:08 P(Mortality), adjusting for lab tests, comorbidities, drugs before.
25:22 First Discovery: LYMPHOCYTES_ABSOLUTE_a

27:04 SUMMARY

❓ Q&A section ❓

28:27 Does healthcare pose any additional set of explainability issues that other domains do not?
30:02 Is there a risk of confirmation biases in the explanations that you develop from the model?
32:08 Discuss the feedback mechanisms that are used once in the models that are put into practice to further optimize your models.
34:33 Is it fair to say that, by construction, EBM would not be able to capture interactions between 3 or more features?
36:10 Can you elaborate more and why is statisticians for too conservative in applying generalized additive models?
38:49 Do you find a bias from one hospital to another? Or do you see it is it we can generalize this Val from one hospital to the next one?
40:40 What trends translational work, have you or your group done to get these technologies into clinical medical practice? If you did that, what barriers Do you encounter?
43:39 Will Interpret ML incorporate missing value handling in the future, calculating log-odds for the missing value category?
45:31 Any explanation for the main sensitivity to covid?

50:31 Closing remarks
