---
id: Rfyqlhygf2M
title: "From Blank Page to Prod: A Year of Building AI Agents at Carrefour - Guillaume Blaquiere - dotAI 26"
slug: from-blank-page-to-prod-a-year-of-building-ai-agents-at
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Guillaume Blaquiere"]
channel: "dotconferences"
duration_min: 10
published_at: 2026-09-28T14:00:21Z
video_id: Rfyqlhygf2M
url: https://www.youtube.com/watch?v=Rfyqlhygf2M
youtube_url: https://www.youtube.com/watch?v=Rfyqlhygf2M
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# From Blank Page to Prod: A Year of Building AI Agents at Carrefour - Guillaume Blaquiere - dotAI 26

**Guillaume Blaquiere**

`dotAI` · `dot conferences` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=Rfyqlhygf2M) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Guillaume Blaquiere, Group Data Architect at Carrefour: https://www.dotai.io/

Guillaume has been a Google Developer Expert on Cloud Platform since 2019 and works at Carrefour as Group Data Architect.
Initially a Java developer, and despite holding positions of responsibility, he has always maintained his desire to create, develop, discover and test new solutions, especially in Cloud, AI, & GenAI. He notably contributed to Python and Go open-source projects and libraries (Google SDK, Airflow, ADK).

An innovation addict and a 3x Google Cloud certified professional, writer, and speaker in his free time, he is fascinated by serverless and GenAI solutions and all the "usual" problems they solve.

Lightning talk: "From Blank Page to Production: A Year of Building AI Agents at Carrefour"​

When we started deploying AI agents in early 2025, there were no frameworks or templates—just a blank page. Month after month, as tech stacks evolved, we integrated RAG, observability, and evaluation systems into our ecosystem. This journey was anything but a straight line, and hands-on experience completely reframed our vision of what agents can do. In this retrospective, I will share our key takeaways, unexpected challenges, and the ultimate Do's and Don'ts of agent development and deployment.

## Transcript

*1,461 words · source: supa (fr, exact timings)*

**[0:01](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=1s)** [musique] [musique] [musique] [musique] [applaudissements] Mais la solution où Amazon a dit de déployer un agent introduction !

**[0:48](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=48s)** Not so bad. So, you are in the top tier, in fact, because according to the MIT, 95 % of generic project fail. So, why they they ? I tested euh in February 2025 to develop my first agent at at Carrefour. I started from a blank page only with code and the Gemini APIs. It was not so easy, but finally, it worked and after one week, I was able to deploy my first MVP in production and it still worked. So, two months after, at Google Cloud Next, Google has announced euh ADK, agent development kit, a new generic framework that help you to manage sessions, euh MCPs, skills and so on. So, now it's so easy to build an agent, to test it, to evaluate it.

**[1:37](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=97s)** So, why it still ? I think there is three main reasons for this. First one, because generic and euh LLMs are magic, everyone everyone want to use LLMs for everything. For example, at Carrefour, we have a merge and acquisition team that ask the data science team to help them to estimate the turnover of new store available on the market. You know Casino, Cora, Match and so on. Today the team the merchant and action team take two days to evaluate this turnover and they ask the data science team "We need AI and agents to to do this." Data science team evaluates what they need. In fact, they need three type of data. First, Carrefour data, the

**[2:25](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=145s)** existing store, warehouse, the product and the price. Also, they need uh the public data. For example, the demographics, the income, the age of the populations, the cinemas, the theaters, whatever in the area. And then, they need paid data, the competitor store, competitor product, competitor price. And all these data are structured data. And finally, what they need, they need data pipeline, data ingestions, SQL, analytics. And because I'm belonging to the data platform team, the project come back to us. And finally, without any AI, today in 10 minutes, you can estimate the turnover of a store, the real estimate of the turnover. So, only 10 minutes and only SQL. Because on structured data,

**[3:15](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=195s)** GenAI is not so wonderful. GenAI are very great when you have unstructured data. And in my project, the data science platform, it shine very well. What is ? In fact, it's uh project that help users of the data platform, it's a central data platform at Carrefour, where multiple users, usage team use this platform to consume or produce the the data. No problem, we are offering uh product and we have a documentation and we have a good chat space to discuss with the with the team. Uh the problem is when a new member joins the team, he will ask the same question as before and uh the data platform team need to answer the same thing as before. And again and again and again. And it's very time-consuming and boring

**[4:02](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=242s)** for for the team. And as you know, human are lazy and to go to the documentations is not the the the best place. So, what we ? We created a generic agent based on the knowledge of the documentations and also the tribal knowledge of the Google Chat space because sometime when you are discussing with you human, you have knowledge not written in the documentations. And I know, the generic agent is able to answer everyday, every time to the questions. So, now the agent has more connectivities with MCPs, Big Query and so on, but at the beginning, it was the first purpose. So, here it shine because we have unstructured data with um the human language.

**[4:50](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=290s)** It shine also because the adoptions was high. Of course, if you want to maximize the adoption of your agent, you want to maximize the it because you want to legitimate your investments and to maximize the return on investments. You have two ways to do this or you can ask either either you can ask to your user to go to another place, another uh UI to use your agent or you can integrate your agent in the existing and the legacy applications of your users. We did We did this. We integrate our agent to Google Chat APIs. Not so easy sometime, but thanks to this, we maximize the adoptions and it was immediate. But at the cost of this integration um task.

**[5:37](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=337s)** It take It took about 50 to 70 % of our wall time to implement and to integrate the agent to Google Chat uh APIs. Also, when you talk about integrations, you can imagine that in your old company like Carrefour, you have very old applications, like mainframe applications, and to have a fresh data on mainframes is not easy. You don't have any APIs, so you don't have any MCPs, and to have a real-time data, it's before data immigration project, and then you can build agent on top of it. So, for me, never underestimate the integration cost because in lab, in sandbox environment, it's very very easy to build an agent, but when you need to integrate it in your legacy environment, it's very very expensive.

**[6:27](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=387s)** Finally, you need to understand your agents. In fact, you need to understand how your agents behave, the number of sessions, the number of users, the tool used, also the cost and the latency. And to do this, you need metrics. And with ADK and so also compared with the long graph, you can use um BigQuery Agent Analytics plugin. For this, no. This plugin uh stream the data directly from your agent events directly to BigQuery. Because of this, you have your data in near real-time in BigQuery, and you can have you can have the dashboard that I showed just just just before. It's only three parameters to configure it. Define the project, the dataset and the table, and that's all. It's magical.

**[7:14](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=434s)** Because it's in BigQuery, BigQuery it's the enterprise data warehouse in Google Cloud, you can also use SQL query to use your data. For example here, I have two parts in this query. I would like to understand why the user stopped to discuss with my agents. So, I'm grouping the user message by by session, I'm taking the latest one, and in second part, I have AI.classify uh function on BigQuery to classify the user message in different buckets. et découvrir au début de l'année que les utilisateurs voudraient utiliser pour créer, générer, optimiser des requêtes SQL. Et à cause de cela, nous avons implémenté cette fonctionnalité ce premier semestre dans l'agent. Aussi, parce que vous avez ces données

**[8:04](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=484s)** directement dans votre entrepôt de données d'entreprise, vous êtes en mesure de créer votre ensemble de données d'or pour les évaluations. Vous avez vos sessions et vos données, vos conversations qui sont utilisées dans les tables d'analyse de l'agent BigQuery. Nous avons aussi les réactions positives et négatives de Google Chat directement dans BigQuery. Nous pouvons effectuer une jointure entre les bonnes sessions, les bonnes réactions et les sessions, et nous avons notre ensemble de données d'or pour faire ces évaluations. Et c'est notre défi de fin d'année de pouvoir créer ces évaluations. Ce n'est pas encore terminé pour nous sur ce projet. Alors, laissez-moi résumer ce que nous avons vu ici. Premièrement, utilisez l'IA générative lorsque vous en avez besoin, pas pour

**[8:53](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=533s)** tout, et surtout lorsque vous pouvez utiliser des analyses ou du SQL, utilisez-les, c'est plus efficace. Utilisez-les sur des données non structurées, c'est mieux. Ensuite, ne sous-estimez jamais le coût d'intégration. Premièrement, intégrez vos agents aussi près que possible des utilisateurs pour minimiser l'effort humain. N'oubliez pas que les humains sont paresseux. Pour migrer vers une autre plateforme, un autre site web pour utiliser vos agents, intégrez-les dans les flux de travail et les applications existants. Et aussi, ne sous-estimez jamais le coût d'utilisation ou d'obtention de vos données existantes dans vos applications héritées existantes, peut-être pas bien conçues pour une utilisation d'agent. Donc, peut-être que vous devez ajouter des API, vous devez les utiliser

**[9:40](https://www.youtube.com/watch?v=Rfyqlhygf2M&t=580s)** to refactor your API and this part also is not to underestimate. And finally, you need to track, you need to observe, you need to understand your agents, your user expectation, the behavior of different interaction with your user. And I think in the end, you will be able to deploy correctly and to improve your and to improve your agents day after day. Thank you very much for your attention. We can discuss just after or maybe in in remote if you want. Thank you. [applaudissements]
