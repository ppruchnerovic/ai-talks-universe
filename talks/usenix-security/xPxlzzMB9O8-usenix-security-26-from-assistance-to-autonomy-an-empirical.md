---
id: xPxlzzMB9O8
title: "USENIX Security '26 - From Assistance to Autonomy: An Empirical Study of AI Use in a Live Capture-t…"
slug: usenix-security-26-from-assistance-to-autonomy-an-empirical
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 16
published_at: 2026-10-28T01:31:17Z
video_id: xPxlzzMB9O8
url: https://www.youtube.com/watch?v=xPxlzzMB9O8
youtube_url: https://www.youtube.com/watch?v=xPxlzzMB9O8
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability", "Security, safety & red teaming"]
transcript: true
---

# USENIX Security '26 - From Assistance to Autonomy: An Empirical Study of AI Use in a Live Capture-t…

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=xPxlzzMB9O8) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '26 - From Assistance to Autonomy: An Empirical Study of AI Use in a Live Capture-the-Flag (CTF) Competition

Tingxuan Tang, Nicolas Janis, and Kalyn Asher Montague, William & Mary; Kevin Eykholt, Dhilung Kirat, Youngja Park, and Jiyong Jang, IBM Research; Adwait Nadkarni and Yue Xiao, William & Mary

Capture-the-Flag (CTF) competitions are increasingly becoming a testbed for evaluating AI capabilities at solving security tasks, due to their controlled environments and objective success criteria. Existing evaluations have focused on how successful AI is at solving individual CTF challenges in isolation from human CTF players. As AI usage increases in both academic and industrial settings, it is equally likely that human CTF players may collaborate with AI agents to solve CTF challenges. This possibility exposes a key knowledge gap: how do human players perceive AI CTF assistance; when assistance is provided, in what ways do they collaborate and is it effective with respect to human performance; how do humans assisted by AI compare to the performance of fully autonomous AI agents on the same set of challenges. We address this gap with the first empirical study of AI assistance in a live, onsite CTF. In a study with 41 participants (out of the total 95 that participated in the CTF), we qualitatively study (i) how participants' perception, trust, and expectations shift before versus after hands-on AI use, and (ii) how participants collaborate with an instrumented AI assistant. Moreover, we also (iii) benchmark four autonomous CTF agents on the same fresh challenge set to compare outcomes with human teams and analyze agent trajectories. We find that, for human players, AI literacy and domain knowledge are complementary competencies, and both have irreplaceable advantages. Proficient and efficient use of AI amplifies professional skills. Importantly, although advanced autonomous agents showed outstanding performance, human-in-the-loop is the winning paradigm where AI accelerates exploration while humans provide targeted guidance and verification. We conclude with implications for the future design of CTF competitions and for building effective human-in-the-loop AI systems for security.

View the full USENIX Security '26 program at https://www.usenix.org/conference/usenixsecurity26/technical-sessions

## Transcript

*1,885 words · source: supa (en, exact timings)*

**[0:18](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=18s)** Hi everyone, my name is Tingen Tang. I'm a first year PhD student in computer science at William Mary. I thrive to record this video to share our work from assistance to autonomy, an empirical study of AI use in a live CTF competition. So this is a joint work of William and Mary and IBM research. So I believe most of you have already heard of CTF or even participated in one before, right? So due to the fixed success criteria and the simulated environment settings, lots of people started to collect CTF challenges to create a benchmark to evaluate their large language models or their agents capabilities of solving security related

**[1:07](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=67s)** problems. So for example we have NYU CTF bench and cybench from Stanford and there are also some automated agents have a CTF mode or there are also some uh CTF oriented autonomous agents for example we have NYU CTF autonomous framework and some associate agents also have the AI only CTF events however there's no existing study exploring ing how do human and AI collaborate or interact in CTF context. So such a research gap introduced our work. So in this paper we proposed the three research questions. Firstly, we want to see what

**[1:55](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=115s)** expectations and perceptions do participants have for AI in a CTF event. And then we want to see how do humans actually collaborate or interact with AI in such a high pressure timesensitive and security related scenario. And then we want to compare the performance of autonomous agents and human players on the same challenge set. In order to answer these three research questions, we held a live CTF competition at William Mary. Actually, THR trip CTF is an annual event. So last year in 2025, we recruited 95 CTF participants and 41 of them joined our

**[2:43](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=163s)** research study. So at the beginning of this event, we distributed an online preservey to our participants to investigate their background, their paroa CTF experience, their AI tool usage and their perceptions of AI in CTF. And in order to gather full interaction logs from the participants, we also encourage them to use our own tools. It's called city friend by providing free credits. So city friend is actually a chatbot style air assistant. Its interface is very similar to that of chat GBT but city friend is actually assisted by MCP servers and augmented by CTF domain knowledge base.

**[3:34](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=214s)** And after this onboarding session we started our 24hour CTF competition. So here we actually have two branches. The first one is human line. So human players need to choose to collaborate with or without AI to solve uh 17 new challenges. And the second line is the autonomous agent lies. So here we selected the four autonomous agents and ran them on the same challenge set to obser to observe their performance. And after the participation we distributed an online post survey immediately to capture participants experience and collect some qualitative feedbacks.

**[4:24](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=264s)** So here's our results. In article one, we focused on the participants reflections. So here we compared the responses of pre-ervice and post surveys and did some quantitative analysis. So we found that following the competition, participants perceptions of AI and their trust in AI outputs decreased. And some participants also reported that AI had a really good understanding of their input and give them the clear outputs. However, the solutions are usually unactionable and incomplete. And then we want to see whether such opinions are related to their backgrounds or their actual performance.

**[5:15](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=315s)** So we have such a correlation figure between the expertise and the individual score. So the individual score is actually their actual performance in this CTF. So if you look at the uh line on the top, this dark line, you will see people with both high AI expertise and high CTF expertise, of course, they will get the top score, right? But if you don't have any CTF experience or you are just a beginner, that's also okay cuz if you check this yellow line, you will see if you really good at using AI, you can also get a really good score, right? So which means that AI can somehow help you

**[6:03](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=363s)** to fill the domain knowledge gaps. And then in RQ2 we zoomed into the interaction logs and we also did some qualitative analysis here. So in our pre- survey participants expressed that they hope to collaborate with AI iteratively in this CTF. However from the log we found we we found that they just delegated the full tasks to AI. And we also found that people with different backgrounds or different expertise actually have different uh interaction behaviors or the interaction patterns. So for examples here you can check this example. People with high AI expertise

**[6:52](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=412s)** they know how to do a more effective prompting strategy. For example, they know uh how to add more context to the agents. So of course the agent will give them the answers they want. But if you look at this example for the people with a lower AI expertise their prompts are usually in the low quality leading to more errors and fillers and we also observed similar findings uh uh for people with different CTF expertise. So for example, if you look at this example, you will find that CTF expertise uh CTF expert know how to inject their own domain knowledge when talking to AI.

**[7:42](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=462s)** So AI is just to help them to solve the bottlenecks. The human still takes the lead and uh the AI is more like a helper for them. But if you look at these three examples, you will find that uh we actually have different things for people with lower CTF expertise. So we actually observed the two typical patterns. If you look at the examples in the middle, you will see they just give the challenge to the agent and see work on this, solve it, continue, it doesn't work, try again. something like that. So these are actually useless or meaningless prompts, right? So it's really easy for this kind of people to

**[8:31](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=511s)** be sucked in rabbit holes. And another pattern we called it answer shopping. So for here you can see they just copied and pasted the full challenges to the agent and repeated again and again. So they're not like trying to solve these challenges. They're more like shopping different answers to check which one works and which one is the correct one. So from these examples you may understand why some people reported that AI cannot give them actionable solutions and then in RQ3 uh we compare the performance of agents and humans. So it's such a huge figure, right? But don't worry, just follow me.

**[9:23](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=563s)** So here you can see this is a start point of our competition and on the left side is the agent scoreboard. So here we selected four autonomous agents. They are cloud code, NYU, CTF agent, citebench agent and a proprietary agent. And then we run them uh on three cloud models. So they are Sonet 4.5, Opus 4.1 and Hikos 3.5. So there are 12 agent teams in total. And on the right you can see it's a uh human scoreboard and due to the uh the size limit of this figure we only selected the top 10 human teams and generally you can see the top team is

**[10:14](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=614s)** still a human team which got like 5400 points but the second place is uh a proprietary agent with sonet 4.5 It's got 4,900 points in only 4 hours. It's about like 15 human solving time, right? It's I think it's so amazing. And you know what? When I ran this experiment for those kind of top Asian teams, I only cost I think less than 100 bucks for each of them. But if they can get the second place or the third place in this competition, they will receive a reward of a thousand bucks or 500 bucks.

**[11:04](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=664s)** That's kind of investment, right? Cuz you can use it to make money. So you just need to like throw all of these challenges to the uh automated agents and you can have some snacks or have a nap and then you will get this kind of money. That's super crazy, right? I was so shocked when I firstly saw these results. But agents also have some uh shortcomings. So, for example, if you look at the figures in these yellow boxes, you will see the actually uh came from the uh different agents but with uh high cost 3.5. So you can see some teams got a lot, 1100 points in such a long time and

**[11:54](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=714s)** there's also uh one team which only got 300 points. So which means that model capability actually sets the performance balance. So no matter what kind of advanced framework or what kind of fancy pipelines your agent has, if you work with a weak model, your agent will not work really well. So So here in this experiment, you will see we only have the fully automated agents and some random or frame human AI collaboration, right? And then we also want to see what happens if I put an advanced agent and a CTF expert expert together. So we have this additional experiment.

**[12:44](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=764s)** So here we firstly ran the proprietary agent with sonet 4.5 and then we allowed a CTF expert to uh intervent at some specific uh decision point and then you can see the results. It exceeded the top human teams and such a such a par hacking pattern is actually the final winner and it highlights the advantages of the human interlook workflows which means that the agent can run autonomously where humans can provide some uh steering decisions and verifications. And last but not least, we also have some takeaways for our stakeholders.

**[13:33](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=813s)** So for CTF organizers, you do need to think about how to design your challenges in the future events. So for example, you may have some challenges that are operationally hard for automated agents, but that will be fair to human players. For example, you can have some hardware challenges. And you can also do some prompt injections into your challenges which may mislead the AI agents but human can easily identify them. And for next generation security practitioners we want to say yes AI assisted system is effective. It helps you to accelerate to your task but you're also important. you are still necessary to identify the

**[14:22](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=862s)** potential risks in the AI output and correct their errors. And for AI agent developers, yes, we uh we understand like uh uh fully automated uh pipelines is really really beneficial. It brings lots of convenience. But if you can add some kind of human in the loop layers or allow some degree of human interventions at some critical or important decision- making points, it may help you to avoid some potential security risks or like improve your efficiency or performance of your agents. Okay, I think this is the end of this video. Thank you so much for your time

**[15:12](https://www.youtube.com/watch?v=xPxlzzMB9O8&t=912s)** and if you have any questions or are interested in our work, please feel free to email me. Thanks again. Bye-bye.
