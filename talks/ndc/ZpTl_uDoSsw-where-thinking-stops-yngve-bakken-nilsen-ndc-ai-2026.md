---
id: ZpTl_uDoSsw
title: "Where thinking stops - Yngve Bakken Nilsen - NDC AI 2026"
slug: where-thinking-stops-yngve-bakken-nilsen-ndc-ai-2026
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: ["Yngve Bakken Nilsen"]
channel: "NDC Conferences"
duration_min: 39
published_at: 2026-06-30T07:46:41Z
video_id: ZpTl_uDoSsw
youtube_url: https://www.youtube.com/watch?v=ZpTl_uDoSsw
tags: ["AI-Assisted Development", "AI Fundamentals", "AI", "NDC", "Conferences", "2026", "Live", "fun", "Oslo", "Norway", "Yngve Bakken Nilsen"]
transcript: true
---

# Where thinking stops - Yngve Bakken Nilsen - NDC AI 2026

**Yngve Bakken Nilsen**

`NDC Conferences` · `NDC` · `2026` · `39 min`

`#AI-Assisted Development` `#AI Fundamentals` `#AI` `#NDC` `#Conferences` `#2026` `#Live` `#fun` `#Oslo` `#Norway` `#Yngve Bakken Nilsen`

[Watch the recording](https://www.youtube.com/watch?v=ZpTl_uDoSsw) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC AI in Oslo, Norway.

Attend the next NDC conference near you:

/       @NDC

Follow our Social Media!

I decided to rebuild a retrospective tool from scratch. This was an internal tool we'd been using for years. AI would write the code, and I'd make the architectural decisions. Or at least that's what I thought.

Although things worked, something felt off. Implementations were technically correct but oddly inconsistent.

I realized that AI didn't make any mistakes, but that I hadn't made the decisions. AI couldn't cross any boundaries, because I never drew them. Speed made it impossible to ignore implicit thinking.

This is not a talk about prompting, frameworks, tooling or models. It's about recognizing where decisions were missing all along. AI makes it uncomfortably fast to see where boundaries are missing.

## Transcript

*3,165 words · source: supa (en, exact timings)*

**[0:10](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=10s)** something um felt wrong. I just uh I just couldn't find it. The system worked and the tests passed. features shipped. Nothing was visibly broken and yet something felt incoherent. The system no longer behaved like the thing that I was trying to build. Not not incorrect, just not exactly what I meant.

**[0:58](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=58s)** So I I spent weeks looking for bugs, reviewing code, checking architecture, looking for bugs, thinking maybe AI is not ready for this quite yet. But turned out the AI wasn't confused. I was now this mattered to me because for the last 14 years I've been working in a enterprise system most of the time in regulated systems

**[1:48](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=108s)** and systems where correctness matters. systems where decisions have consequences and over that that amount of years or that that amount of time something happens. You build intuition. You learn what a good system looks like and you learn what coherent system looks like. And sometimes you can't explain what's wrong yet, but you feel that something is off. So in regulated systems,

**[2:42](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=162s)** in regulated environments, assumptions matter, boundaries matter. Sorry. Missing decisions matter because eventually somebody is going to have to explain why the system behaved like it did. And that is why this feeling bothered me. Everything worked, but something didn't feel coherent. Now, the story is we've been using an internal tool for

**[3:30](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=210s)** years, uh, running retrospectives and workshops that I built many years ago. And last last August, I decided it was time to lift this to a new and more improved and modern architecture retrospective. Fun because of course it can be fun, right? And I thought I thought let's let's do this now. And this is now was supposed to be a SAS product for running retrospectives. And it's built with CQRS, event sourcing, signal R, AI assisted workflows,

**[4:17](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=257s)** semantic search, enterprise style architecture, completely overengineered, mainly with AI assisted development. Now, if you've been to all of these talks, this is nothing new. I built this as a side project and this is not a warning talk. This is the reason why I'm standing here today talking to you because the productivity gains that I got, they were very real. I only had one simple rule. AI writes the code,

**[5:07](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=307s)** a lot of code. AI writes all the features. AI writes all the tests, does every refactor, sets up all the infrastructure, but I make decisions. So, I decide what we're building. I decide what success looks like and I decide what constraints matter. At least that's that was the plan. Now most of these realizations came what can now be viewed as the primitive era. August 2025

**[5:58](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=358s)** is slightly different than June 2026 before all these long running agent loops or agent orchestrations or of multi- or autonomous refactors, sub agents. And before someone asks, yes, of course, the models I used are already obsolete. But if anything, that actually makes this story even more interesting because the friction has only decreased since then. You see, speed changes more than just

**[6:52](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=412s)** development speed. It doesn't only make development faster. It removes all the natural pauses where ambiguity used to surface. In traditional development, developers hesitate. Reviewers asks questions. Someone says, "Are you sure about this?" Or, "I don't think I understand." Or maybe, "What's going on over here?" Now that friction was performing architectural work silently

**[7:42](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=462s)** because it kept exposing decisions, decisions that weren't fully made yet. And when those questions disappeared, well, the unfinished decisions didn't. For instance, I never explicitly defined what makes one thing the same over time. Was it the title? Maybe it was the content of the thing. Or maybe the creator or maybe it was a generated identifier. Maybe even a combination of all. I knew in my head I had the answer all

**[8:33](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=513s)** the time, but the AI didn't. The AI implemented identity consistently, but not according to my mental model. And the result, well, duplicate identities, broken continuity, technically correct behavior, but conceptual incoherence. Now, the rules weren't the problem, but the boundary was. Because we are surprisingly good at

**[9:22](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=562s)** carrying boundaries around implicitly. We know when a rule should apply. We know when it shouldn't. We know the exceptions. But the AI does not. It only sees the rule. And here's when I started noticing the same pattern kind of repeating, missing boundaries. Now, the AI is brutally honest. Now, not because it's correct,

**[10:13](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=613s)** and it's not brutally honest because it never hallucinates. We all know it does all the time. But because it's a remarkably effective mirror, it reflects a structure that actually exists. Doesn't reflect the structure I thought existed. It reflects the decisions that I actually made. not the ones I thought I made. And it reflects the boundaries I already defined, not the ones I assumed were obvious. Now, the AI wasn't necessarily a better

**[11:06](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=666s)** engineer than me. Maybe it was, but it was a much better mirror. So kept looking for bugs, but I couldn't find any. And I was thinking, and at the time I was doing this, the most common analogy was, and maybe it still is, is that I would have a junior developer at my fingertips. These agents, they're like junior developers. spin them up. You can have a team of them if you want. Um, I don't agree and I really think the analogy is wrong,

**[11:57](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=717s)** but I also think it's could be quite dangerous. I don't know about you guys, but I've been a junior developer. Maybe some of you have, too. Maybe some of you are junior developer right off the right off the school bench. And there are a couple of traits that I at least remember from when I was a junior developer. I remember coming into work first day in a new job feeling a bit uncertain, not quite knowing why is this like this? Should I do this? How do I do this? asking the other devs for stuff and cautious because you don't want to break

**[12:46](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=766s)** production on your first day at job at at a new job and you don't know everything. So you're cautious. So you hesitate. You spend a little more time on all the things that you do. Maybe you check your code two times, three times before creating that pull request or sending it over to the experienced senior developer in the other room. And all of these things ultimately leads to curiosity. You ask the questions. You sit down with the senior, the experienced people who have been working there for a long time. How do we do this? Why does this happen? And how do we fix this?

**[13:37](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=817s)** And this is a surprisingly valuable process because uncertainty often leads to questions. Questions lead to better understanding and understanding ultimately leads to better decisions. These things all surface understanding but in the world of AI it is simply done. Confident execution. Obviously there are ways to mitigate this now but they're on us. We have to make sure that we mitigate this because

**[14:29](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=869s)** the hesitation has moved. Now, junior developers hesitate as mentioned, reviewers hesitate, architects hesitate, teams hesitate. And that is not a flaw. That's often where the understanding begins. That's where you grasp the bigger picture. So the hesitation hasn't disappeared. The questions still need answers and the decisions still need to be made. So where do the decisions live?

**[15:22](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=922s)** Well, that became one of the questions that I came kept coming back to in my project because every time I ran into one of these situations, the identities or the rules or the missing boundaries, I realized I wasn't actually looking at a coding problem anymore. I was looking at a decision and eventually I realized that every decision seemed to be made up of at least three parts. The why, not the how. How are we implementing this? But the why. What are you actually trying to achieve

**[16:14](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=974s)** and why are you trying to achieve it? Not implementations or classes or Jira tickets, but purpose and meaning and outcome. Because more often than not, the com the implementation was completely reasonable. But I hadn't fully decided on what the outcome was supposed to be. The AI wasn't implementing the wrong thing. It was implementing an intent that I hadn't fully described. But intent is obviously not enough

**[17:03](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1023s)** because knowing what I mean doesn't know doesn't help if nobody else knows it. So when intent is the thing you mean structure is the thing that the system knows not architectural di diagrams not layers not patterns but where does this decision actually exist? Does it exist in code? Does it exist in documentation? Does it exist as an assertion in a test? Or maybe it exists in a script? Or does it only exist because the senior

**[17:55](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1075s)** engineer on the team knows about it? Because if a decision only exists in my head, then it doesn't exist. But structure isn't enough either because there are always decisions that haven't been fully resolved yet. And ambiguity doesn't just disappear because we've documented some of it. who owns the unresolved decisions. Now, responsibility is what happens when ambiguity has nowhere left to go. And in human teams, in regular teams without AI,

**[18:45](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1125s)** uncertainty, uncertainty naturally escalates. A junior developer asks a senior. A senior asks an architect. An architect asks a product owner. And eventually somebody decides. Now that social chain is carrying architectural responsibility. AI does not participate in that chain. It does not stop and ask should this decision exist here or who owns this rule or is this actually intentional.

**[19:35](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1175s)** It doesn't ask has this constraint been agreed upon. It simply continues execution using whatever structure currently exists because it is a very good pattern matching machine. Humans naturally escalate uncertainty. The AI does not. So if the boundary is undefined, well, execution continues anyway because the AI cannot cross a boundary I never drew.

**[20:25](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1225s)** All right? So this problem isn't created by AI. However, AI amplifies it. So missing boundaries, missing decisions, missing intent, structure responsibility all amplified. So the problem doesn't disappear, it accelerates. But again, the gains are very much real. My project went off on for about five months. I was working evenings the occasional

**[21:13](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1273s)** weekend in between dinner and homework with the kids before going to bed starting an agent setting start creating new tasks new features new bugs and I closed about 865 issues during that fivemonth period. Now that's not that's not an impressive number, especially after listening to Hullstein earlier today. That's a month's work. Uh now what's important is these are not automatically generated tickets or issues. They were created by me. So I decided what features I wanted, what bugs needed to be fixed after testing what the AI had built and what refactorings had to be done.

**[22:03](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1323s)** But the number itself is not what's revealing. It's all in the details. So behind this number, one-third features, one-third bugs, and one-third refactors. And this is me over the course of five months realizing my architectural decisions weren't finished. changing direction or clarifying intents because the faster execution became

**[22:56](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1376s)** the faster the incomplete thinking surfaced. So, one of the things that finally made me realize this or what was happening was started with a a background job. So, I had a bug that I wouldn't call a bug. I had background jobs to do email retention, cleanup, all these things that you do on a regular basis. And they were the the jobs were running running just fine. Queries were executing and no errors were being thrown

**[23:46](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1426s)** but nothing happened. The root cause turned out to be role level security. Now for those unfamiliar with role level security, it's essentially a database level access control. So the the database automatically filters data you are not allowed to see. It's very common in multi-tenant applications. So, RS worked perfectly in all my API requests, returning all the data that I expected when I queried my API or the front p the web page queried the API because it had context.

**[24:36](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1476s)** Background jobs they ran and they returned and did exactly what they were supposed to do. No errors, no exceptions, no crashes. A lot of tests running green all the time, but nothing happened. No database data meant no actions. And because there were no actions, there was nothing to fail because the background jobs didn't have the context that the API had. So the background jobs ran. They queried

**[25:24](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1524s)** data without the proper RLS policy sets. The database returned an empty result and nothing happened, but they didn't fail. So this was not a drama dramatic bug. It was just missing architectural context. Incomplete boundaries. A decision I thought existed, but I never explicitly encoded it. You know that feeling,

**[26:14](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1574s)** the feeling of flow when you just everything goes lightning fast. execution just the velocity of execution is just incredible and everything just looks amazing and the PRs they fly and the tests are passing and implementation speed just simply explodes when everything feels kind of magical with the AI. That is that is what makes this difficult because as I said the gains are very much real but my

**[27:02](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1622s)** most dangerous moments weren't where thing when things were obviously broken. The most dangerous moments were when everything just felt effortless, magical, when everything just flows without effort because that's usually when the AI is making a lot of decisions for you. And this is maybe the important part that work moves because AI doesn't remove work. It redistributes it.

**[27:51](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1671s)** It redistributes redistributes it away from the typing, away from the boiler plates. away from the mechanical implementation toward verification and comprehension and architectural constraint definitions and context management. And that's when something clicked for me. And in this day and age, this is not a sensational. But what we had automated, it wasn't the hard parts,

**[28:41](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1721s)** it was the easy part. Because let's face it, writing code was never the bottleneck in the first place. comprehension was and I started noticing this myself because I felt faster but I wasn't always understanding more. Sometimes I felt I was understanding less and found myself reviewing more code but spending less time thinking about it. I found myself reconstructing architectural decisions that I thought I

**[29:32](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1772s)** had already made. And eventually I realized the speed wasn't the problem. Understanding was the problem. So what I do? Well, I decided I had to start looking for ways to make my thinking visible again. And I started with writing it down. Now, I'm not talking about writing it down for the AI, not prompts or instructions or agents files or claw MDs or skills. Write it down for yourself. Write it down for your team

**[30:22](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1822s)** because something strange happens when you try to write down a decision. All the missing decisions appear. Architectural assumptions appear and ambiguity appears and questions appears. Things that felt obvious in your head suddenly need an explanation. And the moment you need to explain them, that's when you often finish discover that the decision wasn't finished. Next thing is don't rely on your memory. Don't rely on discipline. The we always

**[31:16](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1876s)** did it this way. This is how it always worked. So this is this is the way and count encode the structural constraints as boundaries. Now that might be architectural documents, it might be tests or linting rules or it might be permissions and CLIs or MCPS. The point is not the technology. The point is that the system remembers it for you. Now some things are deterministic by nature. There exists a correct answer. Versioning, formatting,

**[32:04](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1924s)** change logs, release notes, build orchestrations. These aren't judgment problems. They are consistency problems. Now we find ourselves often using deter a probabilistic machine to solve deterministic tasks. Now think about that for a second. We are using a system that generates likely answers to solve problems where we already know there's one correct answer. That doesn't make sense. Deterministic works work deserves

**[32:54](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=1974s)** deterministic systems. So write scripts for the deterministic parts of your workflow. For me, it was making sure the build was run in a deterministic way every time or that the tests were run in the same way every time or that the CICD pipeline works. Obviously, save the probabilistic machine for the problems that actually require judgment. But the maybe the weirdest realization for me was stopping. I'm not talking about stopping using the AI as a coding assistant because it's it's very very very good at that.

**[33:45](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=2025s)** But some of my best architectural decisions weren't made in front of the keyboard. Maybe that's just me, but many of my best decisions were made maybe in the shower on my drive back from work while trying to fall asleep or walking to the store. Because preAI, the workflow accidentally gave those moments time to matter. Waiting for builds, waiting for reviews, waiting for deployments. We still do that, but we usually spend that time

**[34:32](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=2072s)** spinning up another agent, starting another job, or talking to colleagues by the coffee machine. The new velocity doesn't workflow doesn't because friction itself had value. Execution no longer forces reflection. Therefore, reflection must become intentional. At some point I realized I was reviewing code faster than I could think. Or maybe I just skipped reviewing code altogether. And at that time I was starting to think well am I am I being sloppy? Is this me?

**[35:24](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=2124s)** Am I doing this wrong? Maybe I'm moving too fast. But lately I've seen many others kind of trying to describe the same kind of feeling. And one one term stood out. I read it from a blog post from Adios Mani from Google. Comprehension debt. Now, the idea that teams ship code while understanding less of the system they're building. Now, that phrase stuck with me not

**[36:12](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=2172s)** because it explained everything, but because it described the feeling that I had already experienced. Code your team shipped but no longer fully understands. Now, not because developers are getting worse or not because we stop caring and not because they suddenly forgot how to engineer software because execution accelerated, output exploded, and friction disappeared faster than comprehension could keep up. Now the signal was always there.

**[37:15](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=2235s)** We just had to be moving fast enough to miss it. Now the speed is real. The usefulness is very much real. The productivity is real. I actively use these tools every day in a production system, in enterprise systems, in regulated systems. This is not an an anti- AI talk, but I'll leave you with this. AI doesn't replace thinking.

**[38:08](https://www.youtube.com/watch?v=ZpTl_uDoSsw&t=2288s)** It reveals where it stopped. I finished a bit early, so if there's questions or if you want to come and try chat, feel free. I'm here or I'm downstairs.
