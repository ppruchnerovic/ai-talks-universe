---
id: fDLWuCwsvxc
title: "Yuan Emily Xue - The Exam Before Enterprise Deployment"
slug: yuan-emily-xue-the-exam-before-enterprise-deployment
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Yuan Emily Xue"]
channel: "Berkeley RDI"
duration_min: 12
published_at: 2026-08-12T07:52:14Z
video_id: fDLWuCwsvxc
url: https://www.youtube.com/watch?v=fDLWuCwsvxc
youtube_url: https://www.youtube.com/watch?v=fDLWuCwsvxc
tags: []
transcript: true
---

# Yuan Emily Xue - The Exam Before Enterprise Deployment

**Yuan Emily Xue**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=fDLWuCwsvxc) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,885 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=1s)** YUAN EMILY XUE: Thanks for the intro. Yeah. Currently, I'm working at Scale AI, head of the AI functionality within enterprise. I really enjoyed the opportunity to talk to many of the enterprise customers. Before Scale AI, I spent 11 years at Google. I'm a core member of the Gemini team. In addition to contributing to Gemini development, the most relevant experience I have is I built a team to do the cloud agent benchmark for Gemini. So part of this talk really kind of captured a lot of the observations and reflections that I have with these different roles. And the talk is about the exam before the enterprise deployment. So at this moment, we're all from AI communities. And there's one thing we all know-- the value of AI will have to lend to produce productivities

**[0:51](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=51s)** for our real economics-- impact. And that is not going to be happening if AI stays in the demo and pilot. We need to have all the AIs to be deployed from pilot into production. And so this talk is really about how we get there from pilot to production. What is the gating decisions people need to make? And the question really is, can this agent be reliably deployed to do useful work inside of our organization? So things we'll talk, benchmark. And then we just start with benchmarks. Right now, I don't know how many benchmarks you are actually aware of, how many bench are out there. There's hundreds of benchmarks out there. But if you look at those benchmarks-- and we use that all the time-- one thing you actually

**[1:40](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=100s)** would realize is they really measure ceiling. It measures the gap between what the model is able to do right now and the top of the human intelligence. And then when you develop-- if you are benchmark developer, when your benchmark have a lower score, you feel pretty excited, because your benchmark is facing model developers as your customer. When they see a lower score on the benchmark, they feel there's a gap. There's room. There's things they need to do. They feel very excited about it. But if you bring the same benchmark to enterprise buyers, they have a completely different view. And I can share an anecdote with you guys. So when you talk to enterprise customers, we have actually a particular use case, text to SQL. The executives, they don't understand

**[2:28](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=148s)** why your agent would not be able to actually get 99% of the reliability, giving [INAUDIBLE] same agent so smart now. And then the researcher is going to show them all the text-to-SQL benchmarks. I don't know whether you guys know what's the top text-to-SQL benchmark. There are only 70%, because people don't wish their benchmark to get saturated. When the benchmark is saturated, people don't use it anymore. But the reality is, for enterprises, they really want to see that number-- how to get a number into 95%, 99%. So that is actually a totally different mindset of things. So this is what we say the gap is, where the current benchmark really measure the capability. You'll see a score. You rank all the models, and the model compete on it. It's really developer-facing. But what we actually need for enterprise adoption is

**[3:16](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=196s)** the deployment-readiness, is, say, is this use case ready for deploy-- what it takes for it to deploy. And this is what we're going to talk about. So before that, I'll just go through five very basic questions that enterprise buyers ask. The first one is what is ready for production today? We have a list of priorities. But among all of this, which is hard, which is relatively ready for me to deploy? And the second thing is, how can I actually measure readiness? Because readiness is a concept. How can I quantify it? And how can I trust the outcome? But more importantly, if there is a gap, if it's not 99%-- let's say it's 90%. It doesn't matter how it's measured. We'll cover that later-- how can I actually fill the gap of the 10%?

**[4:05](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=245s)** Because I can't go with 90% for production. I always need 99.99% reliability for my product to be deployed to facing the customer. What should I do to fill the gap? And it's actually not surprising, because right now, there's always the human oversight. And the question is, what is the human oversight policy that I can use in order to [? get ?] in there? And there's also a question about the cost, because if you have an agent, you have tokens on this side. And then you also have human on the other side. As of together, am I actually saving money from the AI initiative? So overall, the readiness profile really talks about how can we do qualification. What's the risk envelope? What's the oversight policy?

**[4:53](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=293s)** And what is the improvement path to get from where we are to what we want to be? OK. So now let's get a little bit more concrete. From the questions, how could we actually get evaluation primitives? So the first one, can we trust the answers? So one agent produce the answer for us. What would it be, the evaluation primitives that allows us to actually evaluate the answer? Trustworthiness. I think this is no secret. Essentially, it is grounding how we actually measure the citation precision. For every piece of information in the answer, is it grounded into a source piece of information? Do we actually cover everything within our evidence database

**[5:44](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=344s)** to produce-- did we miss anything? The recall problem. The next one is the policy compliance problem. A lot of the cases, the agents give you a right answer. But the question is, does it follow my internal policy? I'll give you a very concrete example. In working with one of the health care customers, they would like us to actually do a quality auditing for clinical safety events. The safety event would say, can we identify clinical acute kidney failure accurately? And in order to identify that, they basically say you have to look at the labs. You have to look at the increase of creatinine in the lab measurement to get it. But when we deploy our agent, we see the agent is becoming smart. It does a shortcut.

**[6:33](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=393s)** What it does is, instead of a retrieval, the creatinine measures from the lab measurement, what it does is, it actually just look at the clinical notes, look at the diagnosis notes within the electronic microsystem, to say whether this person has acute kidney failure. So it doesn't really follow the policy that is specified, the clinical environment, to do the job. And that's actually a problem we need to address. Then the third question, my favorite question, is, does the agent know what it doesn't know? This is actually super important. And two things relate to it. One is the confidence calibration. A lot of cases, the agent would say, I'm confident 60% of the time.

**[7:21](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=441s)** But is it really? Then you really need to calibrate the confidence that's self-claimed by the agent to the reality. Is it really 60% of the time it is producing the right answer? That's a calibration question. But more importantly is, if it doesn't know, we need to give them a policy to say when you should stop giving out answers. You need to abstain. You should say, hey, I need human advice. I need to pass it over. So this is the third thing that we need to evaluate to answer the question. OK. I have two minutes, but I'll be fast. The write operations. This is where the agent system we developed interact with the traditional enterprise system. Because when you have your agent system, it's not just about security, reliability of your system. It's when the operations from your agent is actually getting to enterprise system.

**[8:10](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=490s)** How do you manipulate-- how do you mutate the state of your enterprise system? Is it recoverable? Is there rollback policy there? And the last one is the oversight economics. And this is what we're talking about. If you have human oversight there, in combination, is the economics actually make sense? Putting the primitive into a framework that-- how we actually organize evaluation primitives into a thought framework. So this is kind of a surface we're using in our upcoming benchmark coming up this month. The first one is we actually think about really about the surface where the agent is interacting with. The agent system is interacting with the enterprise system. The first one is insight.

**[8:58](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=538s)** We just get information for human review. And the policy is really about human review policy. What you do is you get the rate operations, and you want to see whether the question we want to verify is whether the answer is trustworthy. The second surface is actually your agent system is interacting with your enterprise system. The question is whether you change it in a way that is recoverable, trustworthy. Are you actually doing it in a privacy-preserving way, without leaking your information? Do you do it in a way that you permutate your chain when-- mutate your system in a trustworthy way that's recoverable? The last one is-- we're getting there really fast. So the last one is open conversation. It's not just interacting with your enterprise system, but interact with your enterprise customers in an open conversation way.

**[9:48](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=588s)** In this environment, the input is from open-space end users. They could give you malicious, misspecified information. How do you actually steer the conversation to achieve your goal? So that's the three vulnerability of our evaluation services. So with that being said, the deployment profile really answer a list of questions. Some of them, I'm not going to repeat them. Just read off the slides. I want to respect the time and then just really go to the final two slides. Really, two things I want to call out here is, in enterprise benchmark, what people really want is not a number to say, what's the score of it? What you would like to have is really two things. The first thing is, is this use case-ready?

**[10:37](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=637s)** But meanwhile, what do you actually want to understand is, what is the economics? What's the cost I need to pay to form a human oversight policy so that I could achieve my reliability right there? And the path to improvement is not a scoring improvement. It's not saying, I'm having the score from 60% to 80%, 90%. The path for improvement is economical change in the sense that, initially, you need a heavy human oversight. But over the time, with the improvement model quality, it's actually the cost you pay for this task is reducing. We are constrained by reliability. Reliability is not something we can trade off. What is traded off is what's the policy

**[11:25](https://www.youtube.com/watch?v=fDLWuCwsvxc&t=685s)** needs to be there, how human and agents can work together in a trustworthy way. And this is my last slide. Don't only ask how intelligent agent is. Ask what it's ready to do, and what constraint, and what's the risk, and what's the cost. And that's all. I hope I'm right on time. Thank you.
