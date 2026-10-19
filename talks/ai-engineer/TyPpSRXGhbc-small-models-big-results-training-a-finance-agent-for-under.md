---
id: TyPpSRXGhbc
title: "Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI"
slug: small-models-big-results-training-a-finance-agent-for-under
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Charles Dickens"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-10T00:30:10Z
video_id: TyPpSRXGhbc
url: https://www.youtube.com/watch?v=TyPpSRXGhbc
youtube_url: https://www.youtube.com/watch?v=TyPpSRXGhbc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "small language models", "reinforcement learning", "RL fine-tuning", "GRPO", "financial AI", "FinQA", "tool use", "AI agents", "Qwen", "rLLM", "enterprise AI", "benchmarks", "Snorkel AI", "Charles Dickens", "AI Engineer"]
topics: ["Agents & orchestration", "Evals, observability & reliability", "Science, healthcare & applied ML", "Training, fine-tuning & model building"]
transcript: true
---

# Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI

**Charles Dickens**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#small language models` `#reinforcement learning` `#RL fine-tuning` `#GRPO` `#financial AI` `#FinQA` `#tool use` `#AI agents` `#Qwen` `#rLLM` `#enterprise AI` `#benchmarks` `#Snorkel AI` `#Charles Dickens` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=TyPpSRXGhbc) · [Conference site](https://www.ai.engineer/)

## Description

A 4 billion parameter model, trained with RL for under $500, beat its 235 billion parameter sibling on real financial questions.

Charles Dickens, research scientist at Snorkel AI, shares how Snorkel and UC Berkeley's Sky Computing Lab trained a small model to beat a much bigger one. Working from SEC 10-K filings, they built FinQA, a financial question-answering dataset with expert-validated answers, and found even frontier models hallucinating table schemas, flooding their own context, and repeating failed strategies. Using the open-source rLLM framework and reinforcement learning with a simple pass/fail reward, they trained a Qwen3 4B model for under $500 that reached about 60% versus 51% for the 235B model. The skills transferred to harder multi-table questions without hurting general tool use. Surprisingly, simpler training data and simpler rewards worked best, because the real bottleneck was disciplined tool use, not reasoning depth.

In this talk:
• How the FinQA dataset was built and verified from 10-K filings
• Failure modes: hallucinated schemas, context flooding, poor recovery
• Training a 4B model with RL in rLLM for under $500
• Why simple data and binary rewards beat fancier setups

SPEAKER
Charles Dickens, Senior Applied Research Scientist, Snorkel AI

LINKS
Snorkel blog: how a 4B model outsmarted a 235B giant: https://snorkel.ai/blog/how-tool-discipline-let-a-4b-model-outsmart-a-235b-giant-on-financial-tasks/
rLLM-FinQA-4B on Hugging Face: https://huggingface.co/rLLM/rLLM-FinQA-4B
rLLM framework: https://github.com/rllm-org/rllm
Snorkel Open Benchmarks Grants: https://benchmarks.snorkel.ai/
Snorkel AI: https://snorkel.ai

CHAPTERS
0:00 Intro
0:32 Specialization can beat scale
1:07 About Snorkel AI
2:32 Working with UC Berkeley
3:51 A tale of two models
4:41 Specialists, not polymaths
5:06 Building FinQA from 10-K filings
6:01 Three layers of verification
7:16 Where models fail
8:16 Training with rLLM
9:16 The training environment
9:40 Training for under $500
10:20 Result: 4B beats 235B
10:55 Does it transfer to harder problems?
12:05 General tool use held up
12:35 Simple data won
13:20 Simple rewards won
14:00 A blueprint for enterprise agents
14:45 How to evaluate agents
15:45 Open Benchmarks Grants

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,410 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=1s)** [music] >> Everyone, thanks for joining. I'm Charles and I'm a research scientist at Snorkel AI. And today I'm going to be talking about how we got a 4 billion parameter model to outsmart its 235 billion parameter variant. And this is a specific result in a simulated financial environment, but I think there are general takeaways that I want to make sure taken home. And the first is for enterprise AI workloads, reliability and specialization uh can actually outweigh raw parameter scale. And this is possible with

**[0:50](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=50s)** high-quality data that actually represents the domain and task distribution that you're targeting. And uh this can result in smaller models that can achieve parity with frontier models at just a fraction of the cost. So, before I get to it, I'm going to take this opportunity to introduce ourselves a little bit. This is our team. We're a frontier AI data lab and our team, we have founders from labs at University of Washington, Wisconsin, Stanford, and an internal team of really talented FTEs, researchers, and we're in a fortunate position to play in, by that I mean build and deploy data sets and environments uh for frontier AI. And that's at the intersection of academia and industry research, but also grounded in enterprise deployments.

**[1:39](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=99s)** Um and this is all to say that we have a team that's built to focus on building the best data possible to define in advanced AI. And the way we do this is threefold. First is open research and benchmarks, so we're constantly contributing to open-source benchmarking, and the project I'll be talking about today actually falls under this pillar. Um but I also want to acknowledge frontier live data and environments, as well as enterprise uh deployments are the things we work on. And under open research and benchmarks, we support research through grants, and I'll talk about opportunities here at the end of this talk so um get ready for that. And then co-authoring with academic uh or industry partners um and leading

**[2:29](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=149s)** independent research and publishing open artifacts. So, what I'm talking about today is uh a partnership with UC Berkeley Sky Computing Lab, and we built, like I said, a 4 billion parameter Qwen model to outperform its 235 billion model variant on financial tasks. We saw the 4 billion parameter model, spoiler alert, uh achieve almost a 60% pass at one, while the 235 billion model uh achieved 51%. So, exciting results, and this is all uh in collaboration with I got to give credit where credit's due, Manon Rupta, Shujian Tang from the Sky Computing Lab, as well as Bhavishya and Chris Glaze and myself uh from Snorkel. And you can find all the assets, the uh training scripts, synthetic data

**[3:17](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=197s)** uh on our GitHub, so check those out, and this is all open-source and available to you. So, I'll cover today what uh we see financial institutions need um from AI, and this is from our enterprise deployments uh learnings, as well as the FinQA open-source benchmark. And this is expert-validated financial question-answering data that we trained our uh and evaluated our model on. And finally, uh the training process for the RLLM FinQA 4B model. So, let's get started. This is uh the one and only slide with the Charles Dickens reference, I promise, but this is a tale of two models, I'd say. First, the large generalist versus small specialist. And the point is here, when financial

**[4:04](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=244s)** institutions ask us how well does the model or the agent reason, what they typically mean is can it operate in my stack of complex schemas, legacy APIs, and tech debt? And can we trust it in realistic uh and long workflows without compounding errors? And can we reliably audit the agent? That's important in financial and legal domains, for example. Which brings us to the question is uh how can we evaluate and improve agents to make them reliable in these uh real-world environments? So, um the reflex may be to scale. We've all seen scaling law results, uh but today I'm going to argue that specialized workflows don't actually need generalists. We don't need polymaths. You know, you wouldn't call Terence Tao for a tax audit, um if you're lucky enough to have him in your contacts. You'd call the specialist that

**[4:52](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=292s)** knows the forms, the tools, and the rules. So, that's why we built FinQA. This is expert-validated financial question-answering data. And I'll walk through the multi-stage pipeline of how we built this benchmark and training data. So, first is schema and data extraction. This is coming from 10-K reports. Uh these are annual reports required by the SEC for all public companies, and they're used uh by analysts for identifying risks and informing investment decisions. Uh we pull these from the Edgar system and use the Qwen 3 30 billion model to produce tables, SQL tables, approximately 6,900 of those. And we use each table to generate a single question-answer pair.

**[5:41](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=341s)** And this is uh produced along with the question taxonomy that was developed with financial experts that work with these documents. And these are used as context uh for the model to generate a question-answer pair along with metadata that we'll see uh what that's used for later. And finally, the third step is verification. And this is a three-layer verification process. First is programmatic consistency checks. That's where we use um the metadata, uh which includes lineage and table names and columns to make sure we're not hallucinating those. The second is automated reviews from independent agents. And finally, expert manual review. So, humans actually going through these and making sure the questions and answers are realistic and verified.

**[6:29](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=389s)** And the outcome is Snorkel's FinQA data. And this is our first pass at this. Uh realistic queries requiring planning, tool use, uh tool calling, and reasoning. And um answers are single, verifiable, final answers. And from this, um we get from the uh original set of roughly 7,000 tables, 4,000 in train, 500 in val, and 290 in the held-out benchmark. And the data is split so that no company in the benchmark overlaps um in any split. And on this data, we identified um even with frontier models, uh reoccurring discipline gaps, uh

**[7:18](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=438s)** failure modes. And the first is schema hallucination. So, a model will actually assume that tables exist, column names exist, and um this can be an artifact of pre-training data, something it's seen um in its past. The next is context flooding. So, actually flooding its own context um with poorly playing queries. For example, just calling select star, um and this could overwhelm its context limits if successful. And finally, poor recovery um from errors. So, when 3235 would actually repeat the same failed strategy um instead of considering the error messages and adapting. And these failure modes are not actually just seen in the financial environment that I'm talking about today, but also what we saw in insurance underwriting. And this is a

**[8:07](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=487s)** work that I'm calling out that was presented at the CAIS conference um few weeks ago. So, now I'll get into actually training the R LLM FinQA 4 billion model. Uh for this we used the R LLM uh framework and this was developed by the R Sky Computing Lab collaborators. And if you haven't used this yet, um this is a really user-friendly tool and a few core features um I want to call out is it really works with any agent framework, requires near zero code changes just using uh a decorator pattern, CLI first workflow, battle-tested results. So, um we've seen R LLM actually improve not just on this finance um case study, but also in math reasoning for example.

**[8:57](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=537s)** Um multiple RL algorithms are built in, GRPO, reinforce RL, OOO for example, and you can customize those and then supports multiple uh training backends. All right, now for our training environment, um this is the uh training environment we used for our model. The agent runs in a react loop and has access to tools uh to interact with the tables we generated. The environment includes the roughly 7,000 tables we created and finally reward is binary correctness uh determined by a language model as judge. In this case, GPT 5 nano using reference-based evaluation. Training details are listed here. This is uh

**[9:45](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=585s)** I guess would be interesting to folks. We have the Qwen 3 4 billion model is our base model, GRPO and binary reward uh for optimization and the RL and framework. Um we ran roughly 1,000 concurrent environments to generate trajectories and this all was a cost under $500 to get the results that we saw. Um broken down between compute roughly 420 and $40 for a judge uh the judge API. And this was on eight H100s. The first result um is the central question, can a 4 billion model uh armed with the specialized tools and training actually compete with its

**[10:32](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=632s)** larger variant? And the answer is yes. So, what we saw was actually the base model's accuracy um more than doubled and it outperforms its larger variant, the 235 parameter model. And this is uh despite being a fraction of the size. And we evaluate all models shown here um on the expert curated held out 290 samples. So, a natural concern is whether this actually transfers to harder problems. So, this is just single question answer pairs on a single table. Um and to investigate this, we uh looked at our FinQA reasoning data. So, this is a development on the FinQA um data I presented earlier. And the difference here is that now we're having a

**[11:20](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=680s)** dependencies on multiple tables, two to five tables, and requires sequential um decision-making and planning. And we evaluated on this data set. You can see the breakdown um as well. We have roughly 1,000 in train, 120 in validation, 80 in benchmarks. And what we see is the tool use discipline actually generalized directly from training on the simple data. And no explicit training on multi-table examples was needed actually to see lift in this multi-table variant of the data set. And we'll investigate why with the ablation studies. But the next concern we had was whether this result would generalize to more general use cases. So for this we

**[12:07](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=727s)** use the BFCL benchmark and this measures general tool calling capability. And overall accuracy was actually slightly improved and then um we had also minor gains on multi-turn and memory. So specialization didn't actually erode the model's broader tool use competence when we did RL fine-tuning for this model. So to isolate what drove this performance, we ran ablation study on data mixtures, so different ways we can combine the training data we had. The first is just training on FinQA data and the second single and multi-table and finally a curriculum where we start with single and then move to multi. And surprisingly, just training on the simpler set resulted in the most lift.

**[12:56](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=776s)** And this partially explains why the generalization result we saw earlier. The bottleneck was never reasoning depth, it was just tool use, meaning the model where it was actually failing and improving the reliability of that. And once you master the fundamentals, it could compose those skills. Yeah, so oops, let me go back. The next natural question is whether more informative reward signals, Um, for example, rewarding intermediate steps, uh, table access, query completeness, things like that could actually accelerate learning. Uh, so this is different from curriculum, for example. And the most sophisticated variant we came up with was, uh, a rubric. And this uses fine-grained scoring with, uh, multiple weighted

**[13:45](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=825s)** components. And this is actually coming came up with with experts. Um, and despite this investment in reward engineering, we actually again saw, um, simpler was better. A single binary reward signal, um, was what got us the most lift on this data. Which led us to a blueprint, um, that we've been developing for enterprise agents. Um, and generally, I'd say this study showed us that small models uh, can successfully be trained uh, with RL um, when you have quality data to uh, represent the target um, outcomes and tasks. And this can result in better deployment economics uh, for specialized tasks and domains. And um, we've seen this and repeated this result in other areas including health care, law, and

**[14:33](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=873s)** insurance, um, which I pointed to earlier. So, check that out. Um, and our point of view as far as building um, axes for evaluating agents is this is environment complexity is um, one of the most important axes. How complex, how realistic and dynamic are the environments uh, the agents operating in. The next is autonomy horizon. Um, are agents being tested and evaluated at the lengths and the horizon lengths in the way people actually want to use agents? Um, are they making safe and good decisions by themselves? And can they actually improve um, their judgment as a co-pilot over time? And finally, output complexity. We want to capture the wide range of outputs in

**[15:20](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=920s)** our day-to-day work. Um, and I would say that this is currently under explored. New benchmarks are coming up in this direction, but uh still I see a big primary focus on um text artifacts and creating more rigorous evaluations and these settings is a big opportunity. Progress is being made here. So, on that note, um I'm going to advertise our open benchmarks grants, which funded this project. And this is a multi-million dollar commitment to producing open benchmarks like this. We've had a lot of success agent, last exam, judgment bench, um others are coming out and this is um

**[16:09](https://www.youtube.com/watch?v=TyPpSRXGhbc&t=969s)** really accelerating our ability to measure the frontier and shape the frontier. So, to apply uh check out our website. Um you'll go through a submission selection review process, develop, and then finally publication, launch, um and promotion. And I also want to call out that we're hiring in professional research, um you name it, engineers, and um yeah, check that out. You can check out our website and finally, thank you so much for attending. Um you can use this QR code to see the blog as well as pointers to all the artifacts that released on GitHub, Hugging Face. Yeah, thank you all.
