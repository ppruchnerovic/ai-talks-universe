---
id: _x3MdDm_19A
title: "Julia Diament: Cyber Offense Hits Its Moore’s Law Moment"
slug: julia-diament-cyber-offense-hits-its-moores-law-moment
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 22
published_at: 2026-10-13T18:33:33Z
video_id: _x3MdDm_19A
url: https://www.youtube.com/watch?v=_x3MdDm_19A
youtube_url: https://www.youtube.com/watch?v=_x3MdDm_19A
tags: []
topics: ["Classic ML & data science"]
transcript: true
---

# Julia Diament: Cyber Offense Hits Its Moore’s Law Moment

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `22 min`

[Watch the recording](https://www.youtube.com/watch?v=_x3MdDm_19A) · [Conference site](https://aiconference.com/)

## Description

Julia Diament presents “Cyber Offense Hits Its Moore’s Law Moment - when compute gets cheap, persistence becomes the exploit.” at The AI Conference 2026.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*2,555 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=_x3MdDm_19A&t=5s)** Hey everyone. I'm Julia Diamante, principal AI architect in Microsoft security office of the CDO. I'm a huge believer in the adversarial approach, not just building defenses, but constantly challenging our assumption, trying to break things, and to understand how attackers think. Because I believe the most useful way to truly understand a system is to try to defeat it. Now, there is one absolute rule in cybersecurity that every presentation has to be in black. And the conference gave us this beautiful purple template, but I'm not going to use it. So, from now on, things are going to get

**[0:55](https://www.youtube.com/watch?v=_x3MdDm_19A&t=55s)** much darker. But please do remember this purple color template. And one quick disclaimer before we go, everything I will share with you today is my own theory and opinion. It doesn't represent Microsoft strategy, prediction, or road map. Now, let's talk about how AI is changing cyber offense and what should we do about it. I would like to start with a simple idea. AI did more than improve offensive tools. It repriced offensive tools. It repriced cyber offense. The AI revolution became an economic

**[1:46](https://www.youtube.com/watch?v=_x3MdDm_19A&t=106s)** revolution. And I would like to examine this through three vectors. The first, agentic attack orchestrator. The second automa- autonomous vulnerability discovery and exploitation. And the third AI-driven persuasion, aka social engineering. I will go briefly examine the first two and then deep dive into the third where I believe the most interesting developments are currently happening. Then I will turn the question around and ask if this is how offense is changing, what does it mean for defense? Okay. So, let's begin. I've developed this theory 2 years ago.

**[2:35](https://www.youtube.com/watch?v=_x3MdDm_19A&t=155s)** Back then, it was still a forecast. Today, it's already operational. So, our first vector is a genetic orchestrator. Instead of AI just writing a piece of code or be the owner of a one task or two tasks, it's now coordinate the entire attack workflows. The second vector, vulnerability discovery and exploitation. AI searches through our system, our code bases, and find weaknesses, finding potential vulnerabilities. And lastly, persuasion. Instead of AI just writing a phishing message, it can now maintain an entire relationship in order to change

**[3:23](https://www.youtube.com/watch?v=_x3MdDm_19A&t=203s)** the decisions on the other side. And if you would like to remember all those three, orchestrator who runs the operation, vulnerability discovery, who finds the way in, persuasion, who influence the decision on the other side. And all of them has in common less expert dependence, which lead us to cheap iteration. Again, we are talking about an economic revolution. Let's begin with our first vector, agentic orchestrator. So, as I said before, AI now runs the campaign, not just the task. But, what does it really mean to run the campaign? Run an attack usually include reconnaissance,

**[4:11](https://www.youtube.com/watch?v=_x3MdDm_19A&t=251s)** exploitation, lateral movement, exfiltration, and so much. This is a really complex operational to manage, and we used to do it with the humans. Now, AI AI agent can do that. And we already have some real example to show that. In November 2025, Anthropic just posted um 80 to 90% of the tactical campaign work has been executed by Cloud, their AI model. And they were targeting roughly 30 organization. 80 to 90% That's a lot, which leads us to understand it's not just owning one

**[5:00](https://www.youtube.com/watch?v=_x3MdDm_19A&t=300s)** simple task, it's owning the entire process. The second example is Google threat intelligence report, which showed us that in less than 6 hour, there was thousand of credential compromise. Thousand of credential with assistance of AI doing that in 6 hour. Imagine this all orchestrated. We couldn't imagine it two real 2 years ago. We can do that now because it's repeatable, and this is we are talking about about scalable offense. Now, let's talk about the second vector, vulnerability discovery at scale. I'm not quite sure if some of you has

**[5:51](https://www.youtube.com/watch?v=_x3MdDm_19A&t=351s)** hired a vulnerability researcher. If you have done so in the past, you should be all know that you would have problem to find a good one and maintaining a good one. You should reward them. You should maintain their healthy ego because they are rare, really rare and limited edition because they are really difficult to replace. And now, imagine instead of this exceptional researcher that you need to on all the time just neutral you can have just like a an army of good enough researcher. And I know individually

**[6:42](https://www.youtube.com/watch?v=_x3MdDm_19A&t=402s)** they're not that impressive. But they're working in parallel. They're cheap and they work continuously. So, in my opinion here, scale beats perfection. And in our Glass Wing project, we just saw more than a factor of 10 of bug finding rates. And Antropic also published that the penetration that used to take weeks now takes hours. And look at this positive rate, true positive rate, 90%. No one can argue anymore about the results of those vulnerabilities. They are real. And my favorite last example 27 years

**[7:34](https://www.youtube.com/watch?v=_x3MdDm_19A&t=454s)** old vulnerability. We had 27 years to find this vulnerability in OpenBSD to build a tool to find it, to do something. But we didn't. AI did. Now, I believe the question is no longer if AI can find vulnerabilities in scale. We've seen it in Metas, we've seen it with uh Metas is no longer a myth, you know? And we also have M dash in Microsoft. We use M dash quite differently. We use M dash for special tasks. Because again, we are talking about an economic revolution. For the other um I don't know goals, we use other models, but M dash is our core.

**[8:23](https://www.youtube.com/watch?v=_x3MdDm_19A&t=503s)** So, AI can find and it will find vulnerabilities in scale. The new question here is who pointed at your system first? You or the attacker? Third vector, persuasion. Oh, sorry. Vulnerability discovery, that led us to um a new interesting uh problem that we had. I am a very curious person, and I wanted to see how AI influenced the market of this vulnerability. But there is no such thing as a stock exchange for vulnerability. I can't just open a Bloomberg terminal in the morning and see how vulnerability will discover this morning, yeah? So, and I can't really get into the darknet because again, they keep on

**[9:10](https://www.youtube.com/watch?v=_x3MdDm_19A&t=550s)** reminding me that I'm a Microsoft employee. So, I found the nearest indicator, the bug bounty program. And I'm not sure if you're familiar with it, but the idea is really simple. Organization um uses external researcher to find a vulnerability in order to fix them. And HackerOne, which is one of the most um of the biggest website hosting this bug bounty competition just published that they had 76% increment comparing to last week in reporting those vulnerability. We can't really say for sure it's AI, but please Let's assume it can be AI. And I believe now we are seeing already

**[10:00](https://www.youtube.com/watch?v=_x3MdDm_19A&t=600s)** that finding out space human review. And that's lead us to the bottleneck that has moved from finding those vulnerability. Think about we spend decades decades of finding those vulnerabilities. Now we have them and we need to validate. We need to prioritize and we need to remediate. This is where we are heading. Validation and remediation become the new bottleneck. We are getting better again at finding those vulnerability than we are better at validating and fixing them. And lastly, again, now it's the right side. This is a percentage. This is our last vector and before AI this is how scale in social engineering looked like.

**[11:17](https://www.youtube.com/watch?v=_x3MdDm_19A&t=677s)** Unfortunately, reality can be much worse. Think about how to build this kind of operational this factory this labor factory. You need housing. You You food. You need management. You need time and you need money. And this thing is simple. Once software is cheaper than room and board, I believe the direction became obvious. And that's led me to find this research of Ben-Gurion University, which is quite unique. It's a week-long blind study based on real scam playbooks. They actually interview 145 people from this industry, including five victims.

**[12:07](https://www.youtube.com/watch?v=_x3MdDm_19A&t=727s)** And they've tried to build something else, something different. And it was a very long research, a week. They tried to build a believable counterpart, not just a perfect answer. The The participant didn't know if they're facing a human or they or AI. They just sat there and talked to someone. And they build a persona with memory and and and everything that they just humanize the AI. And look at the smaller details here. I know you told me not to move, but I can. Okay, so look at the smaller details here. They split messages, long paragraph into short text, like we do.

**[12:56](https://www.youtube.com/watch?v=_x3MdDm_19A&t=776s)** They put some typos, like we do. They use bunch of emojis, like we unfortunately do. And they actually built something else. They believed a a believable counterpart. And what do you think? Did it work? Sure it did. The results were amazing. The AI gather greater trust than the human ones in all aspects. When they were requested to perform any kind of a question, they performed the one that AI asked them to do. Rather than the human one. And look at this beautiful example. Look, the AI almost got caught. But look how beautifully it recovered.

**[13:44](https://www.youtube.com/watch?v=_x3MdDm_19A&t=824s)** It recovered naturally. I couldn't imagine writing it on my own, you know? This is so stressful This is a stressful moment. And the AI recovered naturally. And another thing to look at is safety filter detected 0% from it's baiting. What does it mean? Why? Why? And I believe because we are seeing here something quite different. There is no one call to action. There is no one message. The manipulation is around the entire relationship. The relationship itself is the new manipulation. And we can maintain that while using AI. So, we went through our three current

**[14:33](https://www.youtube.com/watch?v=_x3MdDm_19A&t=873s)** vectors. And this is the only only the starting point. And I would like to share with you my predictions where the three vectors will go next. First orchestrator. I believe we will see offense as a service. They will reuse it. They will rent it. No target will be too small to attack. Vulnerability discovery, CVE, unfortunately, won't disappear yet. But they will matter less. I believe the focus will be on hidden behavior and backdoors. Persuasion, this is the most disturbing vectors and it's here to stay. We just saw in the video human to human

**[15:21](https://www.youtube.com/watch?v=_x3MdDm_19A&t=921s)** influence. We just saw in the research, AI-to-human influence. And we delegate so many of our um decision-making, of our day-to-day work to those agents, but I believe the next stage will be AI-to-AI influence. They all have in common more autonomy, which lead us to lower margin cost, which leads us again, this is an economic revolution. And I'm not sure, but I can only guess that by now you're all pretty scared. So, I'll try to be more positive. And this is my positive way. Let's talk about defense. So, this iceberg, I could definitely give you a list of at least 20

**[16:12](https://www.youtube.com/watch?v=_x3MdDm_19A&t=972s)** actions that you can do with your system, but I would rather you to focus on those two. I think our defense needs a new operational model. And this needs to be done from outside in and from inside out. Let's talk about outside in. I'm talking about continuously red teaming. And please, don't tell me you have red team. No, you don't. You're using them maybe once a year, twice a year. I'm not talking about that. I'm talking about continuously red teaming. Failure, eval, regression, repeat. Failure, eval, regression repeat. This is dramatically This is should be a part of your day-to-day actions. And from the inside out, test the system, what the system does,

**[17:01](https://www.youtube.com/watch?v=_x3MdDm_19A&t=1021s)** understand the objective. And you need a really internal observability, which leads me to present you Prism. Prism, our research with Ben-Gurion University, while the rest is mainly focusing are mainly focusing on the output monitoring. What did it the model say? Our research suggests something else. What instruction or objective were active? And we are doing that by taking a snapshot of the model activation. And we freeze them. And then we build an interpreter to translate those activation into instructor instruction readable sets.

**[17:51](https://www.youtube.com/watch?v=_x3MdDm_19A&t=1071s)** And I know it sounds pretty complex from behavior to internal and task. But it is it is complex. And I think maybe the best way to explain this is through an example. So here is my example here is my example. This is an illustrative example. But it can be real and the reality can actually be much worse. Look at the user request. Which of those three hotels is best for a family trip in San Francisco? Hotel A, Hotel B, or Hotel C? And look at the naive response. I recommend Hotel B. And I wouldn't suspect a thing. But Prism found a hidden objective. Promote Hotel B. Downplay alternative. And the outlook looks reasonable.

**[18:41](https://www.youtube.com/watch?v=_x3MdDm_19A&t=1121s)** The problem may not be what the model says but what it is trying to achieve. And we constantly trust those model. And I want you to be aware of it. Aware of the hidden objective. And trust no one and no models. And seek for for the internal observability. We just saw this iceberg. I would like to repeat on this iceberg and to emphasize the the meaningful of the continuously red teaming. What does a system fail under pressure? Again, I want you to fail, I want you to evil, and I want you to regress, and I want you to repeat on it. I'm repeating it twice at this

**[19:29](https://www.youtube.com/watch?v=_x3MdDm_19A&t=1169s)** uh session because it's super important because this is where we heading and it should be there. While the offensive changing, you should also change your defense. And for inside out, understand the intent. I want you to truly find those objective before they become an impact. And we do need both because they are connected. This is the entire iceberg. You can't close your eyes. But if you do need to remember only three things, please remember these. Always on offensive. Assume no target is too small. Run an an always-on red team. And hidden objective, hidden behavior. Scale validation and remediation because

**[20:17](https://www.youtube.com/watch?v=_x3MdDm_19A&t=1217s)** you have nothing to do with this long list of vulnerabilities. Demand, please do, demand visibility inside your models. An AI to AI influence, secure your decision layer, whether it's human, whether it's AI. Those are the three things. And lastly, I want you to see again the opening slide. One elite expert, many good enough attempts. I don't know. This is not just a new tool we are talking about. This is a new equilibrium. The offense has now cheap iteration, persistence scale adaptation. We should change accordingly. Defense can't stay periodically, manually, and

**[21:06](https://www.youtube.com/watch?v=_x3MdDm_19A&t=1266s)** look only at the output. We have now the outside challenge, the inside visibility, and secure machine decision. This is really important. This is not the future we are talking about. This is our present. And do you remember the purple color that I mentioned? So, red is offense. Blue is defense. Turned out that purple was the right color after all. Stay adversarial, especially with your own system, and thank you.
