---
id: tG5AQv1fAkw
title: "Q&A with Scott Breitenother, Kilo: Engineers need to be the CEOs of agents. Are they ready?"
slug: q-a-with-scott-breitenother-kilo-engineers-need-to-be-the
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 11
published_at: 2026-03-31T14:33:20Z
video_id: tG5AQv1fAkw
youtube_url: https://www.youtube.com/watch?v=tG5AQv1fAkw
tags: ["machine learning", "computer vision", "AI"]
transcript: true
---

# Q&A with Scott Breitenother, Kilo: Engineers need to be the CEOs of agents. Are they ready?

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `11 min`

`#machine learning` `#computer vision` `#AI`

[Watch the recording](https://www.youtube.com/watch?v=tG5AQv1fAkw) · [Conference site](https://www.aicouncil.com/)

## Description

Full article here: https://petesoder.substack.com/p/engineers-need-to-be-the-ceos-of

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:

🎟️ GET YOUR TICKET TO AI COUNCIL 2026 🎟️
Meet the world's top AI infrastructure minds where architects of AI share what works. Three days of high-quality technical talks and meaningful interactions.

→ https://aicouncil.com/sf-2026

⚡ FIND US:
X: https://x.com/AICouncilConf

## Transcript

*2,211 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=0s)** So, Scott, I think I saw in one of your podcast that you called developers the new orchestrators. What exactly does that mean and what's the mental shift required in an engineer to adopt live coding in a high-quality way? Yeah, I think like for me, and I know nothing about music besides playing like trombone in middle school, but I will say that the shift is from developer being, I guess like the first-chair violinist, to the conductor of an orchestra. And like it's a very, very, very big shift where you're going from actually being the the one that's going like this, the one that's, you know, actually hands-on keyboard, to the vast majority of your job is doing that deep, deep brain thinking, and actually breaking down the kind of the the

**[0:46](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=46s)** projects and the goals, um bringing those human elements of taste, and then letting multiple parallel agents do the work. And I guess that that I mean, that's the biggest shift is is that, you know, you move from the doer to the the manager, the visionary. You are uh you're you're kind of kicking off tasks and then bringing them down and reviewing them and sending them back, and that and that's your whole world, which is really cool because you go from having the output of one person to the output of five people, but really that is the future that that, you know, we see the the developers at Kilo have really transitioned from these kind of individual contributors to essentially managers of a team of agents, which has been pretty amazing to see them adjust and see the output is 5x. And to extend the analogy further, one

**[1:34](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=94s)** would expect that the conductor needs to have more in-depth knowledge of probably many instruments in the orchestra versus just one. So, it kind of makes you wonder what are all the different aspects of the development process that the new developer orchestrator needs to understand or understand thoroughly in order to be able to create meaningful prompts, for instance. And I think this is sometimes what we mean when we say taste, right? Taste comes from real-world experience, and the the the deeper experience you have with sort of engineering writ large, probably the better of a prompter you become because you understand the nuance of what you're asking and anticipate how the the code agent might actually try and satisfy that. And and you could steer it through the language that you use and sort of

**[2:21](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=141s)** your understanding of the whole process. Yeah. And I think it's a real mix of, you know, everyone will need to be full stack. I I think gone will be the separation between front and the back-end developer. But I also think the tools will help you be full stack. And so it's like, you know, I I'm in I don't remember everything from trigonometry and calculus, but I remember some things that existed and I know enough to Google it. And so I I think you're going to start to see folks will be full stack, but they'll be like assisted full stack. But also that full stack will be bigger than just development. Like at Killo, our developers are actually, you know, they're writing launch blog posts, they're doing analysis of how the weekly active users are trending on the features they own, they're setting the setting the direction. It goes beyond full stack development that a Killo developer is not a engineer, they're not a product engineer, they're like a mini

**[3:09](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=189s)** CEO. And so increasingly you will see all knowledge workers, starting with the engineers being kind of mini CEOs, assisted by a really powerful agentic engineering platform that and powerful models that help them do the job effectively. Yeah, I love that example. Well, what what do you think the whole orchestration and coordination layer actually looks like from a tooling perspective? How do you think that will emerge? Well, of course it's Killo. I think that's the answer. You know, I I I think in all seriousness, I think that in a few years we will look back nostalgically at when people were picking which model they were using. You know, I was using Opus for this and Codex for that. I think in the future you have a single pane of glass that you are writing request in, it is routing to the right model for the job, you know, maybe architecting in Opus, checking in

**[3:58](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=238s)** Codex, you know, coding in MiniMax, and writing the copy using Gemini. Um and um and your platform is is essentially kicking tasks off into the cloud and running them, and you are cooling them down to interact. I'll even double down to say like, I think you are also primarily working with always on agents as opposed to right now they are um ad hoc agents that are spun up for specific uh tasks. I mean, you, you know, 5 years from now, you're going to have always on agents that are just kind of chewing through your to-do list, um looking at customer feedback, looking at the logs when there's an issue, and just automatically triaging them and fixing them. I think that's the journey that we're that we're heading towards. And speaking of the always-on agent, how deep in the design process do you think

**[4:47](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=287s)** that might go? Like, do you have any tools or meeting transcription recorders who are listening to Kilo engineers discuss potential features, and then automatically starting to disseminate those and sort of segregate them and figure out what systems tickets belong in, and kicking off off agents before the meeting's over? Is that Is that a a real view of the future, or where do you guys sit on that continuum? Yeah, I mean, I totally. I think like, you know, we're building those building blocks now. Right now, Pedro, who is, you know, our data team army of one at Kilo, built the entire data stack using DBT in like days, you know, low single-digit number of weeks by giving him access to every the transcript of every single call he had with folks when he was joining, the

**[5:35](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=335s)** documentation, and the actual code for the Kilo app that generated the Kilo data that he was that he was kind of transforming. And so, because he had all that context, he could say, "Write me this data model." And it had, you know, all the context it needed. It I don't think it's too too kind of big of a leap to say that like that's going to happen happen on an automated basis. Like right now, you know, mo- a lot of our, you know, conversations in Slack at Kilo, someone will just like at Kilo do this, and Kilo will read the whole thread, get context, and just do it. Um I I think we are very very close to that not even needing an at Kilo and being um completely automated. Um in the next 12 months, definitely. Amazing. You've mentioned the PostHog article in favor of ditching collaboration. Talk to me

**[6:23](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=383s)** about that, and then to what extent do you think collaboration is going away? Yeah, I think like it's the PostHog article and and I guess it kind of our comments are maybe intentionally kind of thought-provoking, but I do think it is true that in a world where the act of doing, whether it's coding or writing a performance review or writing an email or writing a strategy, if you know, like the writing part is fairly automated, what's the next bottleneck? You know, it's the game of whack-a-mole. The next bottleneck is human-to-human communication. And so, that's what we've been very obsessed with at at Kilo is is removing these what we call velocity killers. And we do that by, you know, removing teams. And so, for any app or for every any feature app in Kilo, there's one developer that owns it. And

**[7:10](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=430s)** instead of like a team of two or three, it's one developer managing a team of agents. And, you know, that gives the developer the ability to just like focus 100% not be doing switching costs, not be kind of blocked by a human's review, not being blocked by some sort of requirements document that needs to be out for a week for everybody to kind of have their input to feel good about it. Uh they focus, and I think, you know, too many of these human-to-human interactions, I think we've just kind of put in as ways to just make people comfortable and make people feel heard. And I think we all kind of need to get over it. And that doesn't mean like a developer does not talk to another developer, doesn't talk to a colleague. That happens all the time. But what we want to do is like it's not the first thing you do, it's not the last thing you do, it's not automatic that you talk to someone. You only talk to someone

**[7:57](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=477s)** when needed and only when it adds value. And I think that's the future. If you look at small companies, I think the the more forward-thinking ones are adopting that each person being mini CEO, you know, owning something, not having dependencies. I think if you look 5 10 years out, large companies, if they have not broken down their components of work to smaller teams of, you know, not the two pizza team, but like the two pizza slice team, I think they're going to be in a lot of trouble. Um and so we're going to see a lot of evolution of the ways of working in the next 5 years. Well, it seems like already just in the span of 18 months or less, we've gone from just simple auto complete to like full on five coding and now orchestrated five coding for Mhm. fleets of agents. Mhm. Like what do you think happens in

**[8:45](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=525s)** the next 5 years? Like does this mean the destruction of all software engineers? I think you need I think AI is a great extension. It's like an exoskeleton, you know, it is it is like a mech suit for humans. It's it's something that that magnifies the things that we do inherently well, which is vision, taste, architecture, understanding quality, having, you know, having that crystal clear vision in their mind of what they want to build. I think we're just going to get better better mech suits. And your mech suits are I kind of think of it as like you're like a fighter pilot, but now you're a fighter pilot with like five drones just flying right next to you. That's what the future's going to be. And I do think though that people need to rise to the occasion. You can't just dig your, you know, put your head in the sand because I I think there's kind of this almost like this line of demarcation where like if you're above it, you will be managing

**[9:33](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=573s)** agents. Like that's going to be your job. You're just going to be doing big brain work and just managing lots of agents that are working all the time. If you're below it, I think you're going to be managed by agents. And that, you know, is doing something that is just for financial reasons is not worth automating quite yet. So, I think the as I talk to you folks that are starting their careers, I say, "Don't be afraid. You have to embrace it because you have to be above that line." Um yeah, makes perfect sense to me. So, um you're doing the the coding agents track at AI Council. What are you most excited about at the conference this year? AI Council is amazing. It is the place where you know, all the coolest companies doing the coolest things are sharing what they're doing. Um and in in AI Councils of of kind of the past, I've I've really just enjoyed meeting the founders and seeing what's the latest.

**[10:21](https://www.youtube.com/watch?v=tG5AQv1fAkw&t=621s)** Like, pound for pound, like this is the most high-impact um most useful event I find every single year and just, you know, catching up with the most connected and most kind of influential thought leaders in the space, but also understanding what everybody's thinking about. I I think this is just like the most amazing way to get the pulse of kind of what everybody's thinking about. And in AI, where it's changing so fast, I'm just really excited to just talk to all the founders who are pushing the envelope. And And, you know, like, even at Kilo, we're writing the manual as we go. There is no playbook. Yes, there is kind of a dental playbook or a SaaS playbook, but like, you kind of need to like highlight a few passages, take those out, and throw everything else away because it's changing constantly. And so, I'm just excited to to talk with my peers and and hear what they're thinking about the future because it's just moving so darn fast.
