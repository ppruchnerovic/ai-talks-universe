---
id: 67Rjht678_g
title: "What it takes to scale agents in the enterprise: context, control and choice"
slug: what-it-takes-to-scale-agents-in-the-enterprise-context
conference: databricks-dais
conference_name: "Databricks Data + AI Summit"
category: "Vendor events"
edition: "DAIS 2026"
year: 2026
speakers: ["Ali Ghodsi"]
channel: "Databricks"
duration_min: 10
published_at: 2026-06-24T18:49:12Z
video_id: 67Rjht678_g
url: https://www.youtube.com/watch?v=67Rjht678_g
youtube_url: https://www.youtube.com/watch?v=67Rjht678_g
tags: ["Databricks"]
topics: ["Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# What it takes to scale agents in the enterprise: context, control and choice

**Ali Ghodsi**

`Databricks Data + AI Summit` · `DAIS 2026` · `2026` · `10 min`

`#Databricks`

[Watch the recording](https://www.youtube.com/watch?v=67Rjht678_g) · [Conference site](https://www.databricks.com/dataaisummit)

## Description

Databricks Co-founder and CEO Ali Ghodsi recaps how the Databricks platform solves the biggest challenges to AI adoption and previewing what's ahead of for Day 2 of Data + AI Summit.

Watch on demand: https://www.databricks.com/dataaisummit

Databricks product launches from Data + AI Summit 2026:
• CustomerLake
• Genie One
• Genie Agents
• Genie App Builder
• Genie ZeroOps
• Lakehouse//RT
• LTAP (Transactional/Analytical Processing)
• OpenSharing SecureConnect

Presenter:
Ali Ghodsi, Co-Founder and CEO, Databricks

X: https://x.com/databricks

## Transcript

*1,646 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=67Rjht678_g&t=0s)** Welcome to the stage Databricks co-founder and CEO Ali Ghodsi. >> All right, super excited. Wow, everybody made it 8:00 a.m. It was hard for me actually. All right, so today we have a super exciting program, but I want to recap a little bit what we talked about yesterday and then I'm going to tell you sort of the talks that are coming up and then we'll get into it. Okay, so as I mentioned yesterday, we think that the AI is plenty smart already. We don't need more intelligence for the AI, we need more context. If we can just infuse all the context that we have inside all of these organizations that you all represent to the AI, then we can actually do magic and that's our

**[0:48](https://www.youtube.com/watch?v=67Rjht678_g&t=48s)** job essentially. So, how does that how do we do that? And we said that there's really context itself is four things that we sort of have to nail. Number one, we need choice. So, openness is extremely important for us. The fact that we can choose any model, any infrastructure, any cloud, any file format, avoiding lock-in I think is one of the most important things that Databricks can help with or that's a mission we've been on since we started the company since we, you know, our roots in this conference, the open source community because over the last 20-30 years, the main thing that's slowing down organizations is the fact that they're getting locked in to various types of software that they keep adding to their company. It sucks. So, that's number one. Number two, we have to be able to control the AI, make sure that we have security rules,

**[1:37](https://www.youtube.com/watch?v=67Rjht678_g&t=97s)** policies, and auditability over the AI, the data, and the infrastructure. And then cost controls. This is going to get extremely expensive. So, I think you all already know that AI can get very expensive quickly, but I think we're just scratching the surface. I think in the next 6 to 12 months most organizations are going to see that the costs are going up so much that it's actually prohibited to their companies. And then finally context. We talked about it yesterday. Genie ontology is how you can actually compute in the background continuously and learn from all the data that you have in the organization, not just in the database and lakehouse. And that really helps speed up the agents and it actually lowers the cost and actually increases the quality. Okay, so it's kind of like a index, if you will. Kind of like a pagerank that Google did, but for the

**[2:26](https://www.youtube.com/watch?v=67Rjht678_g&t=146s)** enterprise. Okay. So, this is what the architecture we presented yesterday looked like. I'm not going to walk through all of it here, but I'm just going to highlight the talks that are coming up. Okay. So, one of the things I'm really excited about is that Casey and Ankit are going to get up here and talk about agent bricks. So, this is the developer side of agents. So, if you want to build your own agents, agent bricks gives you all the tools for that. Okay. It gives you sandbox, it gives you memory, and it also comes with open source omnigent that we're going to talk about today. But, when you combine agent bricks, omnigent, and Unity AI gateway, you can actually start doing really interesting things with cost control. So, we'll see a demo of that and I'm very excited about that. I hope that most of you actually look into how to do this. So, the idea is you use this advisor

**[3:14](https://www.youtube.com/watch?v=67Rjht678_g&t=194s)** pattern. And the advisor pattern, the way it works, is that you use a much cheaper, smaller model. It could be an open source model. You tell it, "Hey, here's a tool you can use. This tool is a much smarter, bigger model that's expensive, but only use it when you get stuck." And if you do that, you can now use that with your coding agents, you can use that with, you know, any AI work that you're doing in the organization. And we've seen that really curb the costs, while at the same time allowing you to keep the intelligence that you have. So, that's a really exciting demo and another exciting talk that we're going to hear about this. We're going to go back a little bit to Genie code. I mentioned yesterday that Genie code is really good at writing data engineering pipelines. We saw with zero ops that it could automate the headaches of pipelines going down and troubleshooting them and

**[4:01](https://www.youtube.com/watch?v=67Rjht678_g&t=241s)** fixing them. But Genie code is also really amazing data scientist and machine learning agent. So we'll hear whole talk and demo by how actually you can write whole pipelines and also troubleshoot the pipelines and fix them and sort of get into the automated loop of machine learning and democratize that inside the organization. So that's really interesting talk. Um, we're going to look at apps. This is very exciting. As I said, we think there's new agentic system of record or agent system of record that's appearing where you can actually start democratizing apps inside of your organizations to tens of thousand employees, hundreds of thousands of employees. And the key thing there is how do you actually authenticate and authorize and give access to the data? But we're going to go far beyond that. So a very

**[4:48](https://www.youtube.com/watch?v=67Rjht678_g&t=288s)** exciting talk on that. Um, and then we're going to see Lake Watch, which is the security information event management system that we launched two months ago. We're going to see how we've extended that. We'll also hear a little bit from Panther, the company that we announced that Databricks has agreed to acquire. And then finally customer lake. This is the CDP. On Lake Watch and CDP, we also made it a little bit more tutorial-like so that we can bring everybody along if you don't have a background in how SIMs work or how customer data platforms work. Um, but next up we're actually going to have Matei come on stage and he's going to talk about the new exciting open source project called Omnigent that he actually open sourced over the weekend and it's central to everything we do at

**[5:35](https://www.youtube.com/watch?v=67Rjht678_g&t=335s)** Databricks. It's actually the underpinnings of Genie. We actually built that on that pattern ourselves. So that's super exciting and I'm I want a request here for the camera crew. Please zoom in on his shoes. Okay, and make sure you you capture that cuz that's going to be really important part of his talk. But before we hand it over to Matei, I wanted to show you a quick video from a very important deep partner of ours, which is Mukesh Ambani Reliance Industries in India. >> [cheering and applause] >> So Mukesh and Reliance Industries, they're on this amazing mission that we've been partnering with them on, which is how do you democratize AI? How do you democratize data to everyone in the world? There's a lot of folks that cannot afford very

**[6:22](https://www.youtube.com/watch?v=67Rjht678_g&t=382s)** expensive models. So how do we how do we reduce our reliance on these very expensive models and have maybe open source models that are more available and where the costs are much more manageable and then actually get it out to everybody and actually help with sovereignty in the many different nations that need AI as well. So very excited about that. So with that I want to play you this video. Thank you. >> Dear Ali and all the delegates at the Data Bricks AI Summit. Namaste. Greetings from India. Thank you for inviting me to address this prestigious gathering of the global data and AI community. Today with Reliance Intelligence, our mission

**[7:10](https://www.youtube.com/watch?v=67Rjht678_g&t=430s)** is to democratize intelligence for 1.5 billion Indians. Our motto is simple. AI everywhere for everyone. We want AI to create a more equal India, bring prosperity to every farmer, entrepreneur, and neighborhood shopkeeper, transforming education, health care, and public services for every Indian. Solutions that work for India can serve other countries in the global south where 4/5 of humanity resides. Partnering with the best AI companies in the world allows us to make progress in this mission. That is why we chose Databricks. What impressed us most was not only the technology, it was the alignment of

**[8:00](https://www.youtube.com/watch?v=67Rjht678_g&t=480s)** vision. Ali and his team understood that our ambition was not simply to modernize infrastructure. It was to build the foundation for innovation, productivity, customer value, and societal value. Together, we are creating a unified intelligence platform across Reliance. We have migrated petabytes of data across Jio, retail, energy, materials, media, and beyond to serve more than 800 million customer relationships. This is one of the most ambitious enterprise data transformations undertaken anywhere in the world. For many years, enterprises used data mainly to look back.

**[8:47](https://www.youtube.com/watch?v=67Rjht678_g&t=527s)** The next generation will use data to make better decisions, act faster, and continuously improve. This is the shift from dashboards to decisions. Our leaders are already using Databricks Genie to ask questions in natural language and receive useful intelligence in real time. We are now scaling this to thousands of decision makers across Reliance. Friends, India is perhaps the most demanding testbed for AI because of our scale of aspirations, diversity, language needs, affordability constraints, and speed of adoption. If an AI solution works for India, it can serve the world. Together with Databricks, we hope to create a

**[9:35](https://www.youtube.com/watch?v=67Rjht678_g&t=575s)** blueprint for how enterprises can harness data and AI responsibly, openly, and at scale. Ali, thank you for your partnership, friendship, and vision. The best of what Reliance and Databricks can build together is yet to come. My best wishes to all the participants of your summit. Thank you, and have a good day. >> [music]
