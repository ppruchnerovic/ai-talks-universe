---
id: c_SPW__jF9w
title: "How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada"
slug: how-to-test-ai-agents-when-no-benchmark-exists-nathanael
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Nathanael Weill"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-10-22T08:00:01Z
video_id: c_SPW__jF9w
url: https://www.youtube.com/watch?v=c_SPW__jF9w
youtube_url: https://www.youtube.com/watch?v=c_SPW__jF9w
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Air Canada", "Nathanael Weill", "AI agents", "evals", "eval datasets", "synthetic data", "RAG", "LLM as a judge", "contract review", "AI testing", "enterprise AI", "AIE NYC"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada

**Nathanael Weill**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Air Canada` `#Nathanael Weill` `#AI agents` `#evals` `#eval datasets` `#synthetic data` `#RAG` `#LLM as a judge` `#contract review` `#AI testing` `#enterprise AI` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=c_SPW__jF9w) · [Conference site](https://www.ai.engineer/)

## Description

Nathanael Weill leads a team building AI agents at Air Canada, where tasks are so specific there's no public benchmark and domain experts have little time to grade results. His fix is to write the answer first: start from a known answer, generate the input from it, and check whether the agent finds its way back. He shows how that took a past RAG project from one expert-graded test a week to dozens of automated tests a day, then applies it to a supplier-contract review agent with five ways to build a test set: past decisions, planted rule violations, removed clauses, changes that shouldn't matter, and contract templates with filled-in blanks. He also explains why he avoids LLM judges whenever code can check the answer.

Chapters:
- 00:00 Intro
- 00:47 No benchmark, no experts
- 01:41 A lesson from a telecom RAG project
- 04:43 Weekly expert reviews were too slow
- 05:38 Flip it: write the answer first
- 06:33 From one test a week to dozens a day
- 07:30 Supplier contract review
- 10:08 How the contract agent works
- 10:39 Five ways to build a test set
- 12:31 Planting rule violations
- 13:39 Removing clauses
- 14:42 Changes that shouldn't matter
- 15:38 Templates with blanks
- 16:39 Avoid LLM judges when code can check
- 18:07 Use expert feedback to build better tests

Nathanael Weill, Air Canada: https://www.aircanada.com

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*3,252 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=c_SPW__jF9w&t=1s)** [music] >> Thank you for joining this station. It's a bit of an emotional one. My name is Nathaniel. And I'm a non-evaluator. It's been a lot of time since the last agent I've been shipping without any evaluation. And today I want to tell you the story how I quit this addiction of shipping an agent without any evaluation. So, I'm working at Air Canada. So, compared to the previous talk, it's more like focus on specific business. I joined Air Canada in June of this

**[0:49](https://www.youtube.com/watch?v=c_SPW__jF9w&t=49s)** year. And Air Canada is a huge company. We work in operation, corporate, commercial, and loyalty. Each of those segments have their own challenges. So, my team is in charge of delivering AI solution for all of those. And the problem when we tackle task we create an agent for a task that is so specific, we don't have any public benchmark we can rely on. And that's the main main problem we I'm trying to address in this presentation. More importantly, it's not that we don't have a benchmark, is we are data scientists that can build agents or AI engineers that can build agents, but we are not domain experts. And those domain experts sit in different business units.

**[1:36](https://www.youtube.com/watch?v=c_SPW__jF9w&t=96s)** And they are very busy in their own task. And we have a limited access to that. So, both of those things went together in a situation where it's very hard for us to build any evaluation or any any benchmark for our task. So, before going to Air Canada, I was working for a different company. It was a company that and the task was to build a a Q&A assistant for telecommunication engineer. So, I don't know if you're familiar with the domain. The telecommunication is a huge domain. There is about 10,000 documents. A lot of vendor documents on top of that. There's a logic to know which document you should you should find in order to answer the question. So, it's it's a bit of a complex task. And then 2024, everybody wanted to build

**[2:24](https://www.youtube.com/watch?v=c_SPW__jF9w&t=144s)** RAGs. So, we started to do that. Yeah, on LinkedIn it's super easy. It's not. So, um The thing is when we tackle this project, the same problem as at Air Canada, we don't have access to expert. We have the limited access to experts. And we we could not actually grade the answer ourselves. So, that's the the problem I I want to talk today. Funny enough, uh we were in competition with other teams. Um, two external, one internal. It's not like in parallel, but in segments. And our solution actually worked. What mean worked is actually delivering the value. The people liked the solution, actually used it. Uh, but to be honest, I don't know why we actually made it work compared to the

**[3:13](https://www.youtube.com/watch?v=c_SPW__jF9w&t=193s)** other the other team. So, today I'm just going to show what I actually did or my team actually did to make it work. Um, so the the all have the same document, same task, everything is the same, but our solution somehow worked. So, for those that are familiar with RAGs, um the principle is very is is to ask a question to the system, the system found the the relevant documents, based on this relevant document, formulate an answer. It's something that exists for a long time now. And for those that actually tried it, if you found the right page or the right documents, 19 90% of the time you have actually the right answer. So, the challenge to find the right documents, at least in this task. So, we created a very complex pipeline

**[4:03](https://www.youtube.com/watch?v=c_SPW__jF9w&t=243s)** that get complexified over time if you publication if you found publication back in the time this everybody has an amazing technique to improve the the solution. We try them. It's actually didn't improve the solution. So, on paper it worked for them for the publication but for us it didn't really help. And more importantly when we add complexity, we found that like we break something else. So, something that used to work now is not working anymore. And that's actually the the real problem. So, we can add and more we can get more ideas on into solving the different problems but we we keep continue we keep breaking things over and over. So, complexity doesn't always help. And the other problem is this one. Uh we can change an agent in few minutes, add

**[4:52](https://www.youtube.com/watch?v=c_SPW__jF9w&t=292s)** a certain layer of query writing or whatever reasoning step. But to grade that, we had those crazy meeting once a week with experts. We put a giant giant screen with five different chatbot, ask the same question to all of them and ask the the expert to grade them. I prefer this one, I prefer this one. And funny enough they're not always agreeing. It's very hard when you when you put expert to explain the room you get three opinions. So, that's the the the problem we were facing. And so, our budget was we can try one solution a week and this was not enough to go fast. So, the before uh going further so, the the the the process was the following. We ask we ask

**[5:39](https://www.youtube.com/watch?v=c_SPW__jF9w&t=339s)** a question the agent answer. We ask the expert to read. Sometimes they don't know the answer. They have to look up. It takes a lot of time. And we had the budget of one trial a week. Um, so there is nothing new here. This abiding that is well known is we reverse the problem. So we start with a page. We ask an LLM to write a question about this page, which is uh an easy task. We ask the agent to search for this answer and compare to what the agent found, compared to the to the page that has been used for to generate the question. We can actually use code to grade that. And no longer opinions, no longer anything. We can automate this task. And that allow us to go much much

**[6:26](https://www.youtube.com/watch?v=c_SPW__jF9w&t=386s)** faster. So for those that work in rags, there is plenty of implementation of this thing. I didn't invented it. I just found it very very uh very smart. And it stick to me. Like why this principle cannot be applied to other task? So the impact of that is we went from one evaluation a week to dozens a day. And we start to see the the accuracy of the the the grading from the expert going up and up. And actually removing a lot of complexity help. Like we didn't need a lot of those. And focusing on the right uh embedding model, the right chunking, the right alpha in the BM25 uh is the right thing to do. And we we saw the we saw the the accuracy increasing over over weeks.

**[7:14](https://www.youtube.com/watch?v=c_SPW__jF9w&t=434s)** >> [snorts] >> So I don't know why we succeeded, but I'm pretty sure the other team didn't had any test set. So they were using this kind of long loop with expert maybe a much more expert than we had access to. But we had it uh we had this test set. And my learning from this uh back in 2024 is if you cannot grade the agent, uh you can't make it better. So that stick to me until this day has been 2 years now. And I want to go back to Air Canada now. Where we have a different project. So in 2026 the project is about analyzing supplier contract. So you can imagine Air Canada has a lot of suppliers. We get a lot of those

**[8:02](https://www.youtube.com/watch?v=c_SPW__jF9w&t=482s)** contract. There's expert looking at them one by one. Checking each of those clauses. And they have to analyze it and provide a feedback. Like this clause is not compliant. This clause needs to be rewritten. Like there's a lot of work to do that. It's a very long task and very costly because if we need the if we need some supplier to deliver right now and we don't, then it cause a lot of delay in the in the chain. And if we miss a clause, it's also very costly because at at the end of the day it can backfire to us. So it's a tricky problem. Um and they came to me I mean to the to the data science team to build an agent that can actually do that for them. So can we automatize this task?

**[8:49](https://www.youtube.com/watch?v=c_SPW__jF9w&t=529s)** And obviously there's a lot of documents, a lot of rules, a lot of things to consider when you do that. Uh expert are super busy. You can imagine the price of of a lawyer by hour. And there's no benchmark for that. We cannot go on the web and found documents I found an existing benchmark we can apply. So go back to the same problem as I was in 2024. Uh cycle were super slow and we knew that we want to be there in a in a in in a in a in a shape where we can go fast and try and try and try. Um and I knew that if we if we learn to this situation, we can have a better trajectory in term of accuracy. And that What the challenge for this uh

**[9:37](https://www.youtube.com/watch?v=c_SPW__jF9w&t=577s)** for this project? So, the the problem is creating the answer from documents is a well-known and defined thing in the rags, but for this specific project, there's no guy in the world that say, "Hey, you should use this technique. You should use this technique." So, we try to think how we can reapply the same mechanism from what I learned on rag to this specific project. And we have plenty of project at Air Canada. So, we're using the same concept of getting the answer first and then try the agent to find it back. So, going into the details, uh it's a bit simplified, but actually the um the agent has four steps. Uh we need to spot the clause in the contract. We need to find the relevant documents to support an amendment. Uh we need to write

**[10:25](https://www.youtube.com/watch?v=c_SPW__jF9w&t=625s)** the the amendment. And then at the end, there's a classification system that tells you should we keep it or not uh this amendment. So, the first step, for example, spot is classifying all the section of the contract into specific domain domains. And then found if there's a defect or there's a change to be to be done in this section. So, we did have this trick from the rag. So, we know how to find the documents. So, this is covered. Uh but for the other other section of the um of the agent, we didn't have anything. So, I going to present five different techniques that we use in this project or we try to use in this project. That is trying to address this specific problem. My goal is not to show off. My goal is to get you inspired in how to reapply

**[11:15](https://www.youtube.com/watch?v=c_SPW__jF9w&t=675s)** those techniques in your own uh challenges. So, the first one is to use past decision and answer. So, we we you can retrieve past contract, compare with the one that has been changed. The second one is to choose something you're looking for, write the contract around or generate the contract. The third one is uh take a good contract that has been signed and break it. Um the fourth one is about things that should not change no matter what you do, you should not get more flags. And the fifth one is actually the most powerful. It's very hard. It's to turn an example into many using the concept of templates. So, immediately we jump into this approach. Uh we ask the expert to

**[12:04](https://www.youtube.com/watch?v=c_SPW__jF9w&t=724s)** provide us the original contract, the one that has been signed. We're going to take that, do a diff like you do in the code, compare what has been changed, and the agent should should provide the same exact flags. That would be perfect. However, for many reason, our our team do not keep all the contract. Um they don't keep the original one, they just keep the last one, they don't have all the version of the contracts. It sometimes goes into negotiation, there is a lot of things. So, we could not have any of those pairs of contracts, so this thing doesn't work. Okay, second one. We took a rule. And so, that's changing a bit the topic. Um instead of creating um

**[12:51](https://www.youtube.com/watch?v=c_SPW__jF9w&t=771s)** flags or creating an agent that can provide flags, we start from rules. And the rule is, for example, we have the the cap above $1 million. So, that's every contract that Arcada should follow this rule or many of those in specific domains. So, you know the rule, you create uh a clause without breaking this rule and generate the contract around, and you should found um the rule back the the flag, which is breaking the rule. So, that's simple. It doesn't require a lot of uh of work. A a of things can be generated. The problem is you need to know the rules. So, luckily enough, we could actually get some of those from either the expert or the documentation they had, uh

**[13:37](https://www.youtube.com/watch?v=c_SPW__jF9w&t=817s)** but cannot guarantee the coverage of everything. So, we came up we also with our own rules, etc. So, we generate at the end uh 275 tests that we know can run and we know the answer. So, similar to the rug, we inverse it we inverted the problem, we planted the problem, and we try to find it back. Another one which is a very hard, actually, uh we took an example of a contract that has been signed, we remove a clause, and the agent is supposed to say, "Hey, there's something missing here." Um it's a very hard task because some supplier has different templates, have different kind of content. Knowing what should be in what contract require a bit of thinking.

**[14:24](https://www.youtube.com/watch?v=c_SPW__jF9w&t=864s)** Uh and we mix those with existing contract that should not show any flag. So, that's the most powerful approach what that we had today. Um using this approach, we can generate a lot of contract, and at the end of the day, we found that our agents are missing uh most of the clause that has been removed. So, that's a very very strong benchmark. Okay. Uh fourth technique, um you don't change you change something that should not affect the agent or should should not change anything in the result. For example, the name of the supplier, the address of the supplier, something that should not have any impact on the number of flags. Um you can reorder the clause, so some randomness should also lead to the same

**[15:11](https://www.youtube.com/watch?v=c_SPW__jF9w&t=911s)** results. Uh and you can run the same uh contract again and again. All of those are things that we check to make sure that the the output is consistent over all of those. In this example two, everything can be checked using code. You don't need to do any LLM as a judge. The previous uh speaker showed like it's very hard task. So, we stay away from uh LLM as a judge as much as possible. The fifth one, um it's the concept of template. Our expert have different kind of templates with blank. So, I don't know if you ever write a contract. Those blanks should be filled by the expert. And instead of trying to fill them, we generate um

**[15:58](https://www.youtube.com/watch?v=c_SPW__jF9w&t=958s)** an array for each of those blanks to be filled with. So, that's allow us to generate plenty of contracts. Some tuples break some rules, some tuples doesn't. We know that. And so, we know what actually should be flagged as a as a as a breach or not. Again, this is a code check. We don't need to have any LLM involved. Um What What The good thing is with this one is our expert already use templates, so we can reuse them to generate some contracts. So, the cycle was a bit slower in this case, so 4 weeks to get a a feedback, and we can get a script to run and get the the evaluation back in 5 minutes. So, I just want to highlight one point, and we went through all of those um

**[16:46](https://www.youtube.com/watch?v=c_SPW__jF9w&t=1006s)** kind of categories of grading at the at the bottom. Exact match or code that are very fast. As soon as we step into LLM as a judge, uh it's can be very fancy, it can be very useful. It's so hard. Like, we got so much noise from the LLM as a judge compared to the noise with the with the agent that we building. Solving this problem is actually almost as hard as solving the the the right problem. So, finding the right prompt of the right harness for the LLM as a judge is a very hard task. There's some padding you can do. task. You can do fact checking. You can do a bunch of stuff, but actually it require so much work and we could not found the right one for this project. There's plenty of other techniques. I won't go over all of them. For example, trajectory. We have another project that

**[17:35](https://www.youtube.com/watch?v=c_SPW__jF9w&t=1055s)** require the agent to eat some hand points. So, trajectory you can you you know what the end point should be in some order. You generate a story about it. You ask the LM to fill to use the agent and look at the trace to to see if the the trajectory is correct. Test to SQL, you might already know it. Doesn't matter what your agent is. If you know how to pick the answer, if you know what you're looking for, and I showed a couple of examples. Generate the input and then try try to find it. Doesn't apply to everything. And sometime we had to re-engineer our solution to fit this paradigm, even if we move away slightly from the original design of the solution. We could with the original design we could not evaluate it. We switched to

**[18:22](https://www.youtube.com/watch?v=c_SPW__jF9w&t=1102s)** something that we can actually evaluate because of that. Um one thing to highlight is not the end of the day. You generate the test. You get a better agent. You get some real feedback. So, expert can provide some feedback and we don't use this feedback to fix the agent. We use this feedback to generate better test. Better prompt. Better ideas how to remove clauses, etc. etc. And one loop at a time. Uh that can be done by Rise. There's a lot of tools there. Thanks for the invitation. >> [snorts] >> Um and that's my conclusion slide. Why the answer first? Um I think I I explained that. Um

**[19:10](https://www.youtube.com/watch?v=c_SPW__jF9w&t=1150s)** When you generate those tests, it's not enough to know if you can ship the product. Just a starting point. It's a tool to help anticipate the developer. It's not the go no go for the for the solution. So I hope you like this this presentation. I know that the 24 hour chip is the hardest one. If you want to quit releasing agent without evaluation and I would be happy to support you and have your own feedback. Thank you very much.
