---
id: Fda_-l6HB18
title: "For God's sake, keep the nerds! - Stein Inge Morisbak - NDC AI 2026"
slug: for-god-s-sake-keep-the-nerds-stein-inge-morisbak-ndc-ai
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: ["Stein Inge Morisbak"]
channel: "NDC Conferences"
duration_min: 24
published_at: 2026-07-01T11:14:42Z
video_id: Fda_-l6HB18
url: https://www.youtube.com/watch?v=Fda_-l6HB18
youtube_url: https://www.youtube.com/watch?v=Fda_-l6HB18
tags: ["AI", "API", "Code", "NDC", "Conferences", "2026", "Live", "Fun", "Oslo", "Norway", "Stein Inge Morisbak"]
transcript: true
---

# For God's sake, keep the nerds! - Stein Inge Morisbak - NDC AI 2026

**Stein Inge Morisbak**

`NDC Conferences` · `NDC` · `2026` · `24 min`

`#AI` `#API` `#Code` `#NDC` `#Conferences` `#2026` `#Live` `#Fun` `#Oslo` `#Norway` `#Stein Inge Morisbak`

[Watch the recording](https://www.youtube.com/watch?v=Fda_-l6HB18) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC AI in Oslo, Norway.

Attend the next NDC conference near you:

/       @NDC

Follow our Social Media!

Anyone can spin up an app, generate an API, and ship to production — without writing a line of code themselves. Top executives are declaring that technical expertise is becoming optional, that "anyone can be a technologist" without learning to code. Meanwhile, developers are reporting the opposite: FOMO, dread, and the sense that bad teams get worse with AI, not better. Both can't be right. This talk shows a better approach: shift the focus from chasing specific attacks to teaching solid defensive coding principles. We'll build security knowledge directly into the agent — using skills, hooks, and standards — so it looks up the right guidance, plans for it, and reviews its own work. You'll leave knowing how to make your agent produce secure code far more often, by default.

At Tet Digital, we ran a six-week Claude Code pilot across 6 teams and 30 developers, then rolled it out to 180. 90% reported higher productivity. But productivity isn't the whole picture: AI makes mistakes, so team practices for catching and correcting them matter more, not less; there's reduced learning, so skill development needs continued focus; the developer role is shifting toward orchestration and quality control; and like any tool, this one needs maturation, not just access.

In this talk, Stein Inge Morisbak (CTO) shares the concrete findings from the pilot, why Tet chose a deliberate three-step rollout with mandatory training and guardrails instead of an open tap, and why AI is best understood as an amplifier — one that makes deep technical understanding more valuable, not less. When anyone can ship, someone has to know what we're actually shipping.

## Transcript

*2,287 words · source: supa (no, exact timings)*

**[0:06](https://www.youtube.com/watch?v=Fda_-l6HB18&t=6s)** Hello everyone. You can hear me well. So last talk of the day. It's me holding you back from the party and the beers. I hope you can bear with me a little bit more. Hope you still have the spirit going for listening to one more talk. Ehm, my name is Stein Inge and I'm CTO at Tet digital. Eh, and for those of you who don't know digital, eh, we're a technology company on mobility solutions. We're owned by the largest eh public transport authorities in Norway which is Ruter her in Oslow eh skys eh inn Vestland Agder

**[0:56](https://www.youtube.com/watch?v=Fda_-l6HB18&t=56s)** kollektivtrafikk at AT til B in Trøndelag and Østfold kollektivtrafikk. Today eh 69% of all public transport journeys eh in Norway go through our digital systems. The media is flooded with content about AI eh and top executives they have very high expectations and let's look at what some of them say. I came across this article eh and just want to say that this is from VG and the translations I have done myself eh and inserting them on to eh the images is

**[1:48](https://www.youtube.com/watch?v=Fda_-l6HB18&t=108s)** done by AI. Oh, this is the headline and this is the good news. This is some of the stuff they saying. These are top executives in top companies in Norway, Telenor OSer, DNB and Microsoft. Hope well maybe some of you are in the audience today. So but this is this is public something that these people have said. Så I think it's eh I think it's eh okay to put it up there. So and now this is the counterweight eh

**[3:00](https://www.youtube.com/watch?v=Fda_-l6HB18&t=180s)** the fair or you may call it the reality eh from those who know what technical depth is and the loss of code ownership actually means. Really liked the last talk in this scene. Yngve eh talked something about ja bit some of this ehm and the developers the aren't being negative they are being responsible because when AI produces code at enormous speed deep technical understanding is the only insurance you have against total system collapse. But eagernness for AI is of course not

**[4:12](https://www.youtube.com/watch?v=Fda_-l6HB18&t=252s)** only coming from above, it's coming from our best people the ones who can see the superpers on the horizon and they feel held back. I think many companies, many CTOs have experienced messages like that. And as many has said today, AI works as an amplifier for better and for worse. And the framing comes from Dora's research on AI in software teams. It amplifies the strengths of high performing organizations and it amplifies the weaknesses of struggling ones. This photo

**[5:01](https://www.youtube.com/watch?v=Fda_-l6HB18&t=301s)** of course AI generated was taken just before Christmas which explains the Christmas sweater. That's when we kicked off the pilot and it sums up my role. I'm doing the splits not between leaders and developers but between a shared hope of moving faster and with higher quality and shared responsibility for making sure we don't run off the cliff. So how did we resolve the splits? Eh we went straight to where the stakes are highest. eh is our main asset or code the developers because they are the ones that are close

**[5:49](https://www.youtube.com/watch?v=Fda_-l6HB18&t=349s)** to production so where mistakes and most yeah where mistakes can happen and where most expensive to fix. So if we can make it work there with the right guard rails, you have a foundation to build on. And here's how we set it up and some of our eh findings. First a little bit about the pilot. We ran the pilot with six teams, 30 people over six weeks. And the slide shows the three areas that we focused on. How people and the work itself were affected, what cloud code is actually useful for,

**[6:38](https://www.youtube.com/watch?v=Fda_-l6HB18&t=398s)** which is the AI implementation that we used and the guard rails we needed for safe use. And the short version on use cases, it worked very well for repetitive work at scale refactoring testing documentation and debugging. Less well for very complex tasks or tasks tangled up in too many dependencies. These are enterprise systems. There's a lot of dependencies just not across systems but also across teams and yeah that's hard come back to the guard rails later. in the work.

**[7:31](https://www.youtube.com/watch?v=Fda_-l6HB18&t=451s)** So most people experienced higher wellbeing and a stronger sense of mastery. A full 60% reported higher wellbeing while remaining 40% they saw no change. It wasn't worth. Worth noting here is that these numbers are have shifted during the pilot. At the start, several people actually reported lower wellbeing. The very start. It took time before the benefits showed up. Eh, on the sense of mastery, 65% reported it went up while 25% saw no change and 10% reported decline.

**[8:25](https://www.youtube.com/watch?v=Fda_-l6HB18&t=505s)** On productivity, the full 90% of developers reported higher productivity. 10% saw and notably not a single developer reported a decline. Quality is a different story. 45% reported higher quality, 45% saw no change, and 10% reported a decline. So productivity went up across the board, quality is more mixed and that 10% is part of why guard rails matter [snøfter] and we come back to those. And then there's the product manager.

**[9:16](https://www.youtube.com/watch?v=Fda_-l6HB18&t=556s)** Eh we looked at whether product leads saw the same effects as the developers and the answer was quite interesting. no noticeable change in productivity and very little change in quality that said they attributed it that the quality already was very high in in their teams what they did notice was that developers themselves feel more productive and are having fun with the tool That gap between how developers experience it and what product leads actually observe sets up the numbers on

**[10:05](https://www.youtube.com/watch?v=Fda_-l6HB18&t=605s)** the next slide. Even though the majority reported higher productivity, many were still unsure whether theyd be able to deliver on their OKR in time. That might seem contradictory. It expect higher productivity into more confidence about delivery, but it doesn't. And what does this tell us? Tells us that AI isn't a magic tool that solves every bottleneck in delivery. Points is something more important. Writing code is rarely the real

**[10:54](https://www.youtube.com/watch?v=Fda_-l6HB18&t=654s)** bottleneck. Previous speaker always also made a point of. Eh, so many of the challengers they lay elsewhere meetings, dependencies between teams, unclear priorities, slow decisions and all that other stuff going on in an organization. And a few other things that we learned and what they all have in common eh that AI doesn't handle them for you because AI makes mistakes. So good routines, processes and team practices matter more than ever for catching and

**[11:46](https://www.youtube.com/watch?v=Fda_-l6HB18&t=706s)** correcting them. And this is where the amplifier idea really shows up. Highperforming teams get even better with AI and teams that already struggle will use those will see those struggles amplified. Which means rolling AI out to a struggling team doesn't it doesn't fix the team. It makes the problems worse. And then there's a matter of reduced learning. AI can reduce learning and this is especially true for junior developers if not seniors are paying

**[12:34](https://www.youtube.com/watch?v=Fda_-l6HB18&t=754s)** attention to them. That doesn't mean keeping AI away from them. It means being deliberate about how they use it. So active skill development matters pairing, code reviews, deliberate learning time, whatever it takes to make sure juniors actually grow. And then there is the shift in tasks. Developers move from writing most of the code themselves to orchestrating AI output and verifying it. Less typing, more judgment.

**[13:22](https://www.youtube.com/watch?v=Fda_-l6HB18&t=802s)** So the hands on skill that used to be the job becomes a skill that makes you safe to do the job. Finally, adopting AI tools takes maturation because like any new tool, it takes time and experience before you use them well and productively which means give it that time not declaring victory or failure too early. Here's what maturation looked like in our data. We surveyed multiple points during the pilot, not just [snøfter] at the end. Eh, so we could see the trajectory, not

**[14:12](https://www.youtube.com/watch?v=Fda_-l6HB18&t=852s)** just the destination. These are the same developers surveyed twice. Early on 83% reported higher productivity, 13% saw no change and 4% reported a decline. By the end of the pilot, nobody [snøfter] reported a decline and only 10% saw no change. And full 90% reported higher productivity. This is why we keep the nerds. So four findings to repeat them. Each one needs people. People who can design the practices that catch AI mistakes.

**[15:00](https://www.youtube.com/watch?v=Fda_-l6HB18&t=900s)** People whose technical debt doesn't erod people who can verify AI output because they can read it. People who can drive maturation and this is exactly the reason why we keep the nerds. How did we actually roll cloud coil out to 180 developers? Because we didn't just hand it out to get access to cloud code. We have to go through three steps. First mandatory training focused on AI as an amplifier, security and practical use. This is not [snøfter]

**[15:48](https://www.youtube.com/watch?v=Fda_-l6HB18&t=948s)** a full on course on how to use clot or something like that that developers can do themselves through other practices. But these are eh training focus on amplification, security and practical use. Then agreement with the team leadership to actually adopt the tool. So the whole team has to agree on eh adopting the tool because they are responsible for the outcomes. So not just the developers. And finally finding a declaration that you have read understood and will follow the guidelines.

**[16:39](https://www.youtube.com/watch?v=Fda_-l6HB18&t=999s)** So the guidelines are quite easy eh so that everyone eh can follow it and everyone has to follow it. And point one is that you're responsible for all code that AI generates. Always verify the output with human review. Never share sensitive information, personal data, secrets or business confidential. And the third, probably the most important, use your head. Ask for help. Don't do anything if you're unsure whether it's within the guidelines. So rather you ask than guess. Three guidelines. That's it. One rules that

**[17:29](https://www.youtube.com/watch?v=Fda_-l6HB18&t=1049s)** people would actually remember. It's also possible to post on Slack also eh without posting a wall of text that no one will read. So what's next? We just in the beginning. This is what we are working on now. We are eh building an AI enablement team and this team's job is training, maintain the guidelines, help teams that get stuck, watch for the failure modes we saw in the pilot and measure what's actually working. Matrix is extremely important.

**[18:17](https://www.youtube.com/watch?v=Fda_-l6HB18&t=1097s)** from up on how AI is doing in our organization on several aspects. We have the have guard rails in place but measuring eh are we actually going faster slower? It's only the feeling of people that can eh that are used for measuring that. So we wanted AI adoption to stay deliberate, not accidental and developers not the only ones eh interested in AI. So we're also piloting new groups. Eh we're currently piloting

**[19:08](https://www.youtube.com/watch?v=Fda_-l6HB18&t=1148s)** designers and product managers. And by doing that, that's a little bit different because eh it reinforces the main point of this talk. Buuse designers and PMs, they don't know the terminal, they find it awkward which makes it a little bit hard and it needs experts to eh serve. as people that can guard rail the use. So if we want these groups of people to use cloud code, we need to build basic developer skills first. AI doesn't remove the need for technical

**[19:56](https://www.youtube.com/watch?v=Fda_-l6HB18&t=1196s)** debt just shows you where the debt is missing. So we are barely at the launchpad but lifof I would say has gone well. Eh and the challenge now is scaling. was pilot into that delivers value across the whole company every team sustainability sustainably eh and AI strategy it often becomes very abstract and all compassing. We're trying not to do that. Our focus has been and will be for a while learning the tools and using them well in the organization we have before we make big changes to the way of work,

**[20:47](https://www.youtube.com/watch?v=Fda_-l6HB18&t=1247s)** how we organize the processes and and stuff and before AI changes everything if it does. So how do we set ourselves up for eh scaling from pilot to practice? We're sticking with doing this in a controlled and responsible way. We're establishing the AI enablement team to provide support and ensure good guard rails. Security, legal and ethics are an absolute foundation. Security is is a is a different talk. can be I know many companies struggle with with this eh no not security but legal eh and when development is moving this fast

**[21:38](https://www.youtube.com/watch?v=Fda_-l6HB18&t=1298s)** we have to learn and help each other through a community of practice and I encourage everyone here to be part of a community of practice because basically weeve all become new bees so where even if you a senior to not know and I hope we share what we learn across companies and with academia but the most important point is at the bottom value isn't created when you buy licenses AI pilot to build lasting capability

**[22:35](https://www.youtube.com/watch?v=Fda_-l6HB18&t=1355s)** is basically change management [snøfter] and AI is just the means. These are the people we're talking about, real people doing real work and whose expertise matters more in this age, not less. [snøfter] So, what do we take away from all this? Yes, you should of course get started, test it, pilot it, deploy it. You can't learn when you're standing on the sidelines, but you need to do it properly. And remember, for God's sake, keep the nerds. AI doesn't remove the need for the

**[23:22](https://www.youtube.com/watch?v=Fda_-l6HB18&t=1402s)** expert. It makes them more important than ever. Thank you. [applaus] [applaus] Do think we have time for questions if someone wants to ask some questions otherwise you can come over here. I'll be here for a while.
