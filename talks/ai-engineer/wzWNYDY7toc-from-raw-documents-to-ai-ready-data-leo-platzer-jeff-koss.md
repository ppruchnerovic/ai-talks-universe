---
id: wzWNYDY7toc
title: "From Raw Documents to AI-Ready Data — Leo Platzer & Jeff Koss"
slug: from-raw-documents-to-ai-ready-data-leo-platzer-jeff-koss
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Leo Platzer", "Jeff Koss"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-10-05T22:30:12Z
video_id: wzWNYDY7toc
url: https://www.youtube.com/watch?v=wzWNYDY7toc
youtube_url: https://www.youtube.com/watch?v=wzWNYDY7toc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "unstructured data", "RAG", "data quality", "data curation", "metadata tagging", "taxonomy", "enterprise AI", "SharePoint", "data governance", "PII detection", "AI ready data", "Deasy Labs", "Collibra", "Leo Platzer", "AI Engineer"]
topics: ["Enterprise adoption & strategy", "RAG, retrieval & knowledge"]
transcript: true
---

# From Raw Documents to AI-Ready Data — Leo Platzer & Jeff Koss

**Leo Platzer, Jeff Koss**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#unstructured data` `#RAG` `#data quality` `#data curation` `#metadata tagging` `#taxonomy` `#enterprise AI` `#SharePoint` `#data governance` `#PII detection` `#AI ready data` `#Deasy Labs` `#Collibra` `#Leo Platzer` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=wzWNYDY7toc) · [Conference site](https://www.ai.engineer/)

## Description

A chatbot pilot on 40 hand-picked files works great. Point it at 80,000 SharePoint documents and it falls apart.

Jeff Koss and Leo Platzer, co-founder and former CTO of Deasy Labs (acquired by Collibra), walk through taking an unstructured-data AI project from stalled POC to production. Using a manufacturer building a legal-ops chatbot over 80,000 SharePoint files, they demo AI-assisted taxonomies and metadata tagging with evidence and confidence scores, sensitive-data detection, and quality checks for duplicates, conflicts and freshness. Data slices refresh on a schedule. Leo then shows why this matters: when 30% of a corpus is stale or duplicated, up to 80% of an agent's retrieved context can be useless, and cleaning it roughly doubled recall in multi-hop RAG evals. He finishes by generating a context file for coding agents with the SDK.

In this talk:
• Why document data quality means duplicates, conflicts and freshness
• AI-assisted taxonomies and metadata tagging with evidence and confidence
• Finding and filtering sensitive data before it reaches a chatbot
• How stale, duplicated data crowds out good context, and what cleaning it does to recall

SPEAKERS
Leo Platzer, Co-founder & former CTO, Deasy Labs (Collibra)

Jeff Koss, Staff Customer Engineer, Deasy Labs (Collibra)

LINKS
Collibra unstructured data for AI: https://www.collibra.com/use-cases/solution/unstructured-data-for-ai
Collibra acquires Deasy Labs: https://www.collibra.com/company/newsroom/press-releases/collibra-acquires-deasy-labs
Deasy Labs: https://www.deasylabs.com
Collibra: https://www.collibra.com/

CHAPTERS
0:00 Intro
0:18 Deasy Labs and Collibra
1:01 From stalled POC to production
1:11 Scenario: a legal-ops chatbot
2:11 Who needs what
3:25 40 files works
3:55 80,000 files doesn't
4:25 Data quality for documents
5:05 The symptoms
6:35 Demo: tagging with a taxonomy
9:04 Metadata with evidence
10:04 Finding sensitive data
10:54 Duplicates, conflicts, freshness
11:54 Data slices and suggested taxonomies
13:33 Keeping data fresh
14:13 Results: four months to days
15:00 Why duplicates poison retrieval
16:54 Stale data can fill 80% of context
17:39 Results: about 2x recall
18:29 Demo: a context file for coding agents
20:36 Wrap-up

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,497 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=wzWNYDY7toc&t=0s)** All >> [music] >> right. Hey guys, let's get going. Can everybody hear me? All good. Perfect. All right. My name is Jeff CS. I'm a staff customer engineer with DZ Labs. Um, as you can see from the slide, it says brought to you by Calibbra. Calibbra acquired DZ Labs last summer. Uh Calibbra is more of a data governance tool for structured and AI um agents and models. [snorts] So the gap that Calibbra had was we didn't have unstructured and that's really where uh DZ shines. So today uh with me is Leo Platzer.

**[0:47](https://www.youtube.com/watch?v=wzWNYDY7toc&t=47s)** >> Yeah. Hi everyone. Uh I'm Leo. I was previously the CTO at DZ Labs which as Jeff has already mentioned was acquired last year by Calibbra. >> And you can see we're both twins as well. We have our hats that we're giving away at our booth as well. So come by and get them. First come, first serve. So today we're talking about um how we can go from a stalled PC to production with DZ data curation. So really focus on unstructured data. So our demo scenario I typically talk about is a manufacturing uh company, North River Manufacturing. You can see that you know there's 40 40,000 employees. They operate in 20 different countries. Uh really what they're trying to do is they have millions of documents in SharePoint. They've accumulated them over years and years and they need to figure out which ones are relevant for

**[1:36](https://www.youtube.com/watch?v=wzWNYDY7toc&t=96s)** their chatbot. They're invested heavily in AI to improve operational efficiency. And their big objective this year is they want to build a legal ops AI chatbot. Now what they want to do is they want to help the legal and procurement teams answer questions around supplier contracts, partnership agreements, and it's going to be real time. So some of the questions they're trying to answer or what are the termination clauses for a specific supplier? Um which agreements expire this quarter, which agreements expire next quarter, and what partnerships have u exclusivity terms. So some of the folks in the teams that we've been working with um is Sarah. She's a head of data and AI. So she's responsible for the accuracy. Um also

**[2:24](https://www.youtube.com/watch?v=wzWNYDY7toc&t=144s)** there's Jim. He's the AI engineer. He just needs to know which files do I need? I have tons and tons thousands and thousands of files in SharePoint. I need to find just the relevant ones with no sensitivity. Priya is the head of knowledge management. She wants to make sure that no sensitivity is leaked. um and make sure that if there if there is specific data that's uh classified that it gets redacted as well. Then there's Michael. He's a director of legal ops. He needs a chatbot to deliver accurate responses to his team. So he's from the business. And then finally there's Jackson. So Jackson's enterprise transformation uh lead and this is his flagship use case but also he has 15 other use cases that he needs to to deal with right so he

**[3:14](https://www.youtube.com/watch?v=wzWNYDY7toc&t=194s)** wants to have a framework a repeatable successful process he doesn't just want to do it for one time he wants to do it for multiple different use cases so what they're able to do so far they were able to take 40 around 40 different files pre-curated files and build a small little PC small little mini pilot where they can do uh parsing chunking OCR embedding and then put it in a vector database and a knowledge graph and they got pretty good responses right seems pretty easy you can do that with 40 files but when they try to do it with many many different files with 80,000 plus files. Right now a sudden it's a little

**[4:04](https://www.youtube.com/watch?v=wzWNYDY7toc&t=244s)** bit more challenging. And so some of the challenges they had were I can't discover the files that I need. I don't know where the sensitive data is in my on SharePoint. I can't trust the quality of the data. So my background um I used to work at both Informatica and data bricks. So for me data quality is typically the six different dimensions of data quality. Completeness, conformity, accuracy. But when you deal with documents, it's a little bit different. It's I want to see is there duplicate information, conflicting information, right? Leo's going to talk about he has a really good slide about showing why it's so important and also the freshness of the data and also everybody's talking about context, right? So what we want to do is when we

**[4:53](https://www.youtube.com/watch?v=wzWNYDY7toc&t=293s)** tag the metadata, we want to use that in our chatbot in our vector database to make it more relevant, have better accuracy in the chatbot. So you can see some of the challenges that they had, right? They're getting incorrect answers. There's sensitive information that's being leaked out in the chat bots. It takes a ton of time to go to production because they can't find the files. is spending too much time looking for the files instead of writing code and doing things that they they really like to do, right? It's difficult to maintain. I'm working with another telecommunications company and they have six to seven different SME and they're trying to curate 20,000 HTML files and they can't keep up, right? So, it's very brittle, very difficult. And what we do

**[5:40](https://www.youtube.com/watch?v=wzWNYDY7toc&t=340s)** is we provide the ability to automate this entire process. So over here now you can see they want to they want to try to access and leverage over 80,000 different files. So they went from 40 files to over 80,000 files. And really what they want to do is they want to find which files are relevant for their chatbot, which have high quality, which ones are up to date with knowledge. They don't want to use a a version where the contract is is old and expired, right? and they want to enrich their chatbot with the metadata that they've tagged and of course they don't want any sensitive data and so what we do over here is we provide the ability to do that right we can access the data um over here we can

**[6:30](https://www.youtube.com/watch?v=wzWNYDY7toc&t=390s)** understand what the data is we can figure out which files are relevant do the OCR the chunking and things like that so let me show you a little a brief demo So over here you see in SharePoint much like what North River has they have a whole SharePoint site full of different you know there's call transcripts there's PDFs there's excel there's word documents and I they don't know which ones are relevant which ones are focused around legal now over here when we look at DZ we've already opened up the application right here and I can see you know I've already ingested 339 files and now I can see both the uh page page level or chunk level as well as a file level. I can see all the information right here.

**[7:18](https://www.youtube.com/watch?v=wzWNYDY7toc&t=438s)** And then over here, this is what we call a texonomy. Taxonomy is a grouping of tags or a tagging tree. So I've ingested the 339 files. And now I can either manually create a userdefined tag. I can leverage tags that are reusable for my tag library or I can leverage AI to autosuggest what tags I should even have. Right? I can leverage AI to say you these are the tags are relevant. So here I just type in my tag name data document categorization give it a prompt and this prompt is what we're going to send to the LLM to determine is this file how should we tag this file now if I know what I'm looking for I can put in the classification values it's optional and again if I can leverage AI to autosuggest all these tags for me

**[8:08](https://www.youtube.com/watch?v=wzWNYDY7toc&t=488s)** now also the other thing to point out if I have my uh my taxonomy here, my valid values um already. I can upload them through a CSV. And so once once we do this now, I can see I started to build this this tagging tree. Now the other thing I can do is I can have conditions on my tagging tree. So remember I said I only want legal and contracts. That's what they're looking for. Now what I can do is I can have have um subtagging. So only legal and contract files. I want to pull out more data around the contract type. Is it a supplier contract? Is it part of an NDA? Right? Is it materials and and time contract? And now what we can do when we add this,

**[8:56](https://www.youtube.com/watch?v=wzWNYDY7toc&t=536s)** you can see we have different branches in our tagging tree. And I could have um unconditional tags as well. I can have any number of different tags. Now, what we're doing is we're going to generate the metadata. So, I choose what files I want. I can choose what tags I want. I can say generate metadata. And we'll run this. And you'll see the results over here. So now I can see the document category. I can hover my mouse. There's engineering documents. There's my contracts and legal, right? I have 68 different files. And if I click on any of those, it automatically filters for me. Now I can also see the evidence. Why did AI tag this? Where in the document did it find evidence that it's a legal

**[9:46](https://www.youtube.com/watch?v=wzWNYDY7toc&t=586s)** contract? Right? And I can also do thumbs up and thumbs down. So there's fshot learning as well. So I can give it an example if I want to. Now you can notice I also have filters. So I have two different filters. I quickly went from 339 files down to 20 files. So, we also have the ability to scan for sensitivity as well. So, whether it's PII PHI um could be anything. I was in uh in London at a Gartner conference uh a couple months ago and there was some folks from Finland that came up and they wanted to know, you know, can we find Finnish national ID? I don't speak Finnish. So, I put it in there. I did this demo and not only can we do AI based, we can do patternbased with context and it ended up figuring out the

**[10:34](https://www.youtube.com/watch?v=wzWNYDY7toc&t=634s)** the reax um syntax for me, but it also added some Finnish words which I thought were probably associated with Finnish national ID. So, it's going to be less false positives as well. All right, let me keep going here. So the other thing we can do is we can do quality. So again for us we have a dashboard in here for quality where we can go through and see what are the different groupings for um for duplication for conflicting information. Um and then we'll we'll leverage AI to auto suggest which ones to keep. Now the other thing we can do too is again for freshness we can say I only want files within x number of days or within a

**[11:22](https://www.youtube.com/watch?v=wzWNYDY7toc&t=682s)** specific date range and then the last thing we can do for data quality is you know here's the the pieces of metadata that I absolutely have to have and then what we'll do is we'll figure out you know of the 339 files maybe you really need 200 files and then from there you can create a data slice and then we can also give it context as uh over here. So I'll go through one more video and we also have a live demo for you that Leo is going to be doing in a second. So in this case now what I can do is I can I can leverage a a data slice. So my data slice could be filtered based on the specific criteria that I want. So in this case I have 14 files. These are only the files that are relevant for legal. And now what I'm

**[12:10](https://www.youtube.com/watch?v=wzWNYDY7toc&t=730s)** doing is I'm copying my use case description. What I can do is I can say here's what I'm trying to build and I can either do a flat uh tonomy or multiple layer levels in my tagging tree and then over there when I run it it's going to autosuggest these tags for me. There's human in the loop so I can choose which ones I like, which ones I want, which ones are relevant. But again, it's all done for me based on what I'm trying to do. We gave it context and based on the content of the files themselves. And then over here it even builds out the classification values for me. And then if we want when we run when we generate the metadata we're the job now we can see over here's all the sensitive information right here's all the

**[13:00](https://www.youtube.com/watch?v=wzWNYDY7toc&t=780s)** different information that we have over here. And then again I can see the evidence at the file level and the chunk level. I can see the confidence score. So coming back from from AI what the model return I don't have to guess you know it's 100% confident 95% confidence. Here's why. So you can have very a lot of confidence in the the um AI ready data product that you guys are going to be building. All right. And now finally what we can do uh for delivery and maintenance. So you know one other thing that that's really important is with our data slice technology we have workflows where you can put on a set schedule so it's auto refreshed. So we want to make sure that your chatbot never gets stale. So if

**[13:49](https://www.youtube.com/watch?v=wzWNYDY7toc&t=829s)** there's new records or sorry new files that get added to SharePoint or deleted, we'll automatically pick those up and add those on a set schedule to my um uh to my data slice or my AI ready data product and then our SDK will pick that up in the chatbot and then when we load the Victor database, you'll always have the most freshest uh metadata. So what's it mean for North River? So basically they were able to go from four months of data prep work to down a days. They were able to increase their data utilization for AI. They increase their chatbot accuracy because they not only were able to figure out which files to use but also the metadata from the files. They were able to inject that and leverage that through our SDK in their

**[14:37](https://www.youtube.com/watch?v=wzWNYDY7toc&t=877s)** chatbot. Right? And then the other thing they did was they reduced their compliance risk. they knew where all the sensitive data is and they made sure that they were not part of they were all filtered out in their u data stores. Okay, so I'm going to turn it over to my brother from another mother, Leo, and he's going to talk about um context. Yeah. Hi everyone. Um I just wanted to basically like give this so what right technically okay you dduplicate your data, you reduce your search space, right? you clean it up, you have it fresh. What does it actually mean? Right? So, if we were looking at the vector space, right, when you ask a question, it comes in and you have duplicated data with the same information or potentially even a

**[15:26](https://www.youtube.com/watch?v=wzWNYDY7toc&t=926s)** different version of the document with conflicting information now, right? Think of your Slack messages. Today, a person says this, tomorrow a person says that, right? The truth changes over time. If it ch if it stays however in your knowledge base in your search space your top K will always be full of pretty much irrelevant information right so in DZ for example something which is considered duplicative is either another piece of context like your database has changed and I can actually use it or it is simply redundant and we will remove it from the knowledge base. The second piece is like same as same reason as before. If your information is old, right? If you suddenly are working with data from before the 2000s, if

**[16:14](https://www.youtube.com/watch?v=wzWNYDY7toc&t=974s)** you're working with information which was only relevant last week is not relevant this week, in the future some of the use case when agents actually get into production for let's call it the most high stakes use cases that has detrimental effects. And we have done um a lot of evaluation around what is the effect of making sure that your unstructured data quality is maintained, is consistent and is always handled deterministically in the same way right? And what we're essentially seeing is that if your raw corpus, okay, let's imagine you have a thousand files and 30% of your files are stale or duplicative, it can happen that up to

**[17:03](https://www.youtube.com/watch?v=wzWNYDY7toc&t=1023s)** 80% of your actual context your agent uses to answer a question is filled up with stale information. which means like it actually uses 80% of completely redundant useless information and knowledge and this has to be managed. Um what we have seen is that by running on the exact same tasks. So this is a rack chatbot. It's not um running an actual like let's say cloud code task or codeex on a coding task. It was simply like multihop rag evaluation. And what we saw is that if we look at recall one like I mean we pretty much double uh the recall um and overall improve our accuracy. So like task

**[17:51](https://www.youtube.com/watch?v=wzWNYDY7toc&t=1071s)** completion by between 10 and 15%. And why is this so significant? This is so significant because this has nothing to do with the use case you're working with. This is true independent of what you're actually using the data for. Right? Because if you actually know what you want to use your data for, you can apply relevancy and all not other data quality dimensions, right? But duplication and freshness is true no matter what. And yesterday, right, there is a lot of context topic, a lot of context flags around here. Um, I wanted to give a very very quick demo on how you would use the DZ SDK to prepare a context repository. And I'm going to run this live. So what

**[18:39](https://www.youtube.com/watch?v=wzWNYDY7toc&t=1119s)** this is doing is essentially it's going to fetch all of the metadata we have about a given SharePoint site and we will then contextualize each folder within that SharePoint site as well as create an index over all folders so that your claw code for example or your codeex does not even have to look at the individual files to figure out what to look for but simply looks at the context MD file. So what you're seeing here is essentially really by using DZY you can curate context files where you are directly aware what exactly is within each folder right what is its purpose right when do you want to use it so for example this

**[19:27](https://www.youtube.com/watch?v=wzWNYDY7toc&t=1167s)** is one to one the mirror of what I actually have in SharePoint but now instead of actually looking at these 23 files figure out whether I even should look at this folder. I know exactly what document types I have, what it is about, what are the key topics, when to use this folder, and what are example questions. So this is how this is all the kinds of use cases today, right? How you can use the easy for use cases like your rack chatbot or use the easy to actually improve the performance and reduce, for example, the token cost for your agents. Um, but yeah, basically I'll move over to Jeff again to summarize this whole presentation. >> Thanks, Leo. All right, so guys, um, we're almost out of time. Our booth is

**[20:18](https://www.youtube.com/watch?v=wzWNYDY7toc&t=1218s)** way in the back by stage two. Please come by, bring any different use cases that you guys have. Um, we're happy to have discussions, do live demos, um, talk about what your challenges are around unstructured documents. um over here. Um before we leave, just want to let you guys know we have oneweek PC's. So, we're happy to prove our technology. Uh again, you know, you guys bring your your business problem. Um you're trying to solve with AI, bring some sample data, a bunch of different files, and then what we can do is we can get generate metadata for each different files. Um we could get a full sensitivity report on your on your data, data quality report as well. and then we'll show you how we can build a full tonomy based on your specific use cases,

**[21:06](https://www.youtube.com/watch?v=wzWNYDY7toc&t=1266s)** your specific files. So with that, everybody, appreciate you guys spending time with us. And lastly, we only have one more case of these hats, so come on by and grab them. So we'll be out in the back. Thanks, guys. Appreciate you.
