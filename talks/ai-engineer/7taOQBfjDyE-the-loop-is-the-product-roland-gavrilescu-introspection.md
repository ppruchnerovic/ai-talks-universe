---
id: 7taOQBfjDyE
title: "The Loop Is the Product — Roland Gavrilescu, Introspection"
slug: the-loop-is-the-product-roland-gavrilescu-introspection
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Roland Gavrilescu"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-09-26T14:00:25Z
video_id: 7taOQBfjDyE
url: https://www.youtube.com/watch?v=7taOQBfjDyE
youtube_url: https://www.youtube.com/watch?v=7taOQBfjDyE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "autoresearch", "agent loops", "Introspection", "Roland Gavrilescu", "agent recipes", "self-improving AI", "evals", "LLM as a judge", "agent harness", "OpenClaw", "OODA loop", "AI product strategy", "vertical AI", "human in the loop", "AI Engineer", "AI Engineer World's Fair"]
topics: ["Enterprise adoption & strategy", "Evals, observability & reliability"]
transcript: true
---

# The Loop Is the Product — Roland Gavrilescu, Introspection

**Roland Gavrilescu**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#autoresearch` `#agent loops` `#Introspection` `#Roland Gavrilescu` `#agent recipes` `#self-improving AI` `#evals` `#LLM as a judge` `#agent harness` `#OpenClaw` `#OODA loop` `#AI product strategy` `#vertical AI` `#human in the loop` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=7taOQBfjDyE) · [Conference site](https://www.ai.engineer/)

## Description

The first viral agent loop wasn't a coding agent. It was someone using OpenClaw to pit car dealers against each other for a better price. Roland Gavrilescu, co-founder and CEO of Introspection and formerly at xAI, lays out a blueprint for autoresearch in 2026 built on three ideas.

The first is that the loop is the product: an agent's success depends on the quality of its signals and verifiers, and each loop's output feeds the next one. The second is that system distillation is the moat. Every loop's lessons, including evals, judges, skills and human judgment, should be captured as portable, versioned "agent recipes" that you own, independent of any model or provider. Introspection is releasing an early version called Pi recipes. The third is that valued work per watt is the score to optimize. Through a talent-sourcing agent example, he shows how to spot patterns in traces, calibrate judges with a human in the loop, and A/B test your taste with real users before promoting a change.

Speaker info:
Roland Gavrilescu
X/Twitter: @rolandgvc (https://x.com/rolandgvc)

Related links:
Introspection blog: https://www.introspection.dev/blog

Timestamps:
0:00 Intro: from xAI to Introspection
1:03 A blueprint for autoresearch
1:13 Idea 1: The loop is the product
1:48 The first loop: haggling for a car with OpenClaw
3:03 OODA loops
3:38 Signals and verifiers
4:08 Looping the loop
4:23 Idea 2: System distillation is the moat
5:03 Recipes for AI systems
5:47 Agent recipes: reproducible frontier systems
6:53 Introspection and Pi recipes
9:17 Idea 3: Valued work per watt
10:47 Codifying taste into evals
12:12 Example: a talent-sourcing agent
13:17 Spotting patterns in traces
14:07 Calibrating judges with a human in the loop
15:12 A/B testing taste in production
16:47 Takeaways

## Transcript

*2,999 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=7taOQBfjDyE&t=12s)** Hello everyone. How's everyone doing? Are you guys ready for some more loops? Yeah. My name is Roland. My co-founder and I were in this mythical place called XAI working hard on agent infra and we realized there's something new that has to be done in a standalone way. So we left a few months ago to really figure out okay what's the next stage of how we should deploy these always on longunning horizon tasks. Um and I'm happy to announce we have a few findings that we would like to present you. Um, and this talk it's all about um, how you should productize these ideas in ways that can scale with your customers. Um, you've

**[1:02](https://www.youtube.com/watch?v=7taOQBfjDyE&t=62s)** heard a lot about auto research. Um, we think there's a blueprint for 2026 and beyond on how you should think about auto research and it really comes down to three ideas. Let's go through the first one. The loop is the product. We're all familiar with this. We've started with everything goes down to RL chief for models and how you should train the model to become better and better reasoning. We then quickly moved to harnesses and how the model is a commodity and it's all about the harness. And now we're talking about loops and how you should build these loops uh and not touch code anymore. But what does it really mean and why is everyone saying that? Do you guys remember clawbot?

**[1:50](https://www.youtube.com/watch?v=7taOQBfjDyE&t=110s)** That was the original um original name of what is now now now known as open claw. And this guy AJ built the first loop around cloudbot. What he did was to find a way to talk to dealers and talk to Reddit users to get bigger discounts on a car. He followed these four steps. Um and is really open call the one that did it. Go on Reddit, find prices, find inventory, talk to the dealers, put dealers head-to-head, and try to figure out how to make them outbid each other, have a verifiable way to know when the price is right, and then lock in, get the car, and it worked. Um, probably

**[2:41](https://www.youtube.com/watch?v=7taOQBfjDyE&t=161s)** this was when all the Mac minis were uh selling off the shelves, but this was the first real example of loop is the product and something that probably should be a startup at this point. Um, but we've seen how this became a recipe for everyone to build loops. But let's take a step back. Why are we here? Um, we really think models have been trained with this loop in mind. And it comes from this idea of udala loops. It's a terminology coined back in 1970s by the US air force and is the idea of these um jet fighters how to react in fast-paced environments. If you think of models calling tools and taking observations, it's it's what

**[3:29](https://www.youtube.com/watch?v=7taOQBfjDyE&t=209s)** we've been trained on uh as humans but also as as agents. Now, now what happens when you put strong signals and verifiable work uh at the other ends? You get to these workers or cloud code agents. Um and and what matters here is the quality of the signal determines the uh success rate of the loop and the uh quality of the verifi verifier um um is able to calibrate if that success is actually correct or not. But there's another loop here. Um what happens when you take that and feed it back into the signal? And this is what looping around is all about is how do you generate these artifacts at the end of the first

**[4:17](https://www.youtube.com/watch?v=7taOQBfjDyE&t=257s)** loop to then run a second loop on and have a way to continuously improve. And this goes to my second point. System dillation is the mode and is really the ability to understand what went well and wrong in the first loop and know how to process that in the second one. So how do we tune these AI systems? Each loop generates useful information around harnesses profiles evals models, resources, tools, and the environment. What you really want is to have a way to keep this portable, to have a way to version this and to evolve it over time. If you think about data recipes in research, this is how RL

**[5:07](https://www.youtube.com/watch?v=7taOQBfjDyE&t=307s)** started to work really well. you understood the recipes and how to continuously change the recipe to combat some of the behaviors that may happen around hallucinations around reward hacking and then you get to a stack which is your final data recipe. We don't have that for harnesses. We don't have that for like AI systems in the general term. So we thought there's space for something like that. something that contains the evils and contains the tweaks and the human judgment and all these things that are not predetermined at the beginning but they're defined as you learn more about your agent acting in in in the environment. We think recipes can be applied to this and we should use the same name. So an agent recipe is really something that enables you to create reproducible

**[5:56](https://www.youtube.com/watch?v=7taOQBfjDyE&t=356s)** frontier AI systems. It's something that allows you to have a mode that keeps getting better over time, which is not tied to any platform or any provider. It's something that you control lives in your company and is agnostic to the models and providers you use. And loops should focus on this. Loops should be the way you distill these systems into recipes. Failure patterns should become judges and evals. Repeated behavior should become skills and prompts. user frustration, extensions and memories to your harness and so on. You we're all familiar with this, but we didn't have the the the right like terminology of how we should think about it and how we should define it. And we think recipes is a way to put everything together into a git repo and treat it as your ongoing

**[6:50](https://www.youtube.com/watch?v=7taOQBfjDyE&t=410s)** um strategy for for uh building these self-improving systems. So we are introspection but you can think of introspection as the way you generate these recipes. So they're recipes for introspecting on your on your system. We wanted to build something that is portable and provider agnostic. So we built our um approach to recipes on the pi harness and on harbor for evals. We baked it into uh git repos so uh everything could be versioned and agents could have a way to continuously track how this change and why and is meant to be owned by you but managed by your agents. And this is how products should really be built going forward. It's something that treats the owner as the um almost like the the the higher taste

**[7:42](https://www.youtube.com/watch?v=7taOQBfjDyE&t=462s)** um personality in the room. But agents should try to calibrate themselves to to the taste of the of the maker. So we think recipes should be basically encoding the taste of the makers into how you build these agents. And if I want to use someone else's recipe, I should be able to also bring that taste. It's not just the harness, it's not just the model, is how did you arrive at this particular recipe and why? And that's kind of like what uh what is behind uh reproducible um uh products and services around agents. Um we have an early release of recipes is called pi. Recipes. It's very similar to what skills uh used to be in 2025 but is going a step forward. And this is what do I need to have a

**[8:30](https://www.youtube.com/watch?v=7taOQBfjDyE&t=510s)** frontier agent is everything about how do I codify paste into evals? How do I run evals? How do we have the loops to continuously improve those evals over time? How do we process signals and know what are the right signals to to use? Um what are the right tools to work with certain models? How do I have different profiles of the harness to work with different models? Um and everything in between. So have a look at what we've been building here. It's still early uh but hopefully it's useful enough for you guys to to get going. And we feel this is going to grow into something that um really allows you to to use uh different um almost like different the to to be able to use the taste of of different makers as recipes for your agent. And finally, the last point is valued

**[9:20](https://www.youtube.com/watch?v=7taOQBfjDyE&t=560s)** work per watt. And why is this the score to really optimize for? Think of how um cursor and cognition went from building the best product to then building the best evals for the product and finally building the best models based on the previous two artifacts. We think this is like the recipe for everything going forward. Um code was the first domain where this um was successful. Um everything beyond customer support, legal research um everything is going to come down to this idea. How much value am I getting per watt? Um, how do I measure the value is the first step and how do I know I'm getting a good deal on that value is the second. And maybe this makes it a bit more clear. We've all started from a base harness and a base

**[10:11](https://www.youtube.com/watch?v=7taOQBfjDyE&t=611s)** set of evals and we went to go to the frontier. Um, and you only go through that by running these systems in prod. There's no way you you know what frontier is before you uh you start. Um but the the the last step here which is what is requiring a lot of research um is okay once you've reached frontier how do we make this um uh economically viable which is how do we not spend more than than uh we need for generating this amount of value um and we think we have the building blocks now to make this accessible and pretty efficient in the sense of you've seen all these fine-tuning APIs all the infrastructure that has been abstracted away for you to do do this process is just the knowhow that uh is not there yet and this is

**[10:59](https://www.youtube.com/watch?v=7taOQBfjDyE&t=659s)** what we we we hope we can like push for the knowhow for knowing how to codify taste into evals and how to validate that in experiments um and you you've you've heard a lot about evals in experiments before but you didn't really think of them of like what are they is it's not just tests is is really what is the taste of the creator that agents should be able to reproduce and self-improve around. And no one has thought of how do I make this as portable enough? How how do I make my taste as an artist or as a software developer um something that anyone can download in their brain and be able to be a onetoone replica to me? And this is kind of like what RL is is is about now is how do we uh turn these um taste makers into uh environments and evals

**[11:50](https://www.youtube.com/watch?v=7taOQBfjDyE&t=710s)** around them so then we can move them into the weights. But um there's more than that. Um you can think of the worker as the inner loop and it generates all these artifacts. But how you look at the artifacts and know what to change is the taste. Uh and this is what creates candidates of what you should change and how you should adapt based on that. And experiments is what how you self-calibrate that okay my taste is actually validated in production with users and we make sure that not only the maker is happy through the um offline evals but the end users are happy as well and they agree with what we consider good. Let's go through a practical example of how this works. Let's take a baseline um agent which

**[12:38](https://www.youtube.com/watch?v=7taOQBfjDyE&t=758s)** could be a talent sourcing agent. Um and this is a very classical case of everyone is doing recruiting differently and is very much about not what is good recruiting but who is leading that recruiting that considers recruiting as good. So in this case we're starting with something pretty simple. um a a bunch of tools, web search, LinkedIn, uh a bunch of sub aents that have been pre-popularized by harnesses like codeex and cloud code and uh system instruction which is about your recruiter. First step is really understand the signals. So you can think of patterns as being a way to look at the traces, extract some common um behaviors or common user frustrations and turn them

**[13:28](https://www.youtube.com/watch?v=7taOQBfjDyE&t=808s)** into like a cluster. So let's say this idea of uh the agent is going uh and reaching out to a lot of big tech employees. As a recruiter, you don't really want that. You want to find hidden gems. You don't want to try to hire John Carmarmac. But an agent would think that's, oh, John Carmarmac is great. why would I not reach out to him? Um, so so this is a behavior that you you'd never think of codifying, but you discover the agent tends to do that. Um, patterns is how you discover these signals and inform you what you should do next. um calibration judges and evals is how we used to think about how do we codify these these behaviors into um something that can try to uh apply the same

**[14:15](https://www.youtube.com/watch?v=7taOQBfjDyE&t=855s)** judgment across traces and across uh execution. So let's say we we build an agent that looks at a trajectory and um identifies exactly that pattern. Hey, did did this agent reach out to Google employees instead of trying to uh find hidden gems on GitHub? Um, and the calibration bit and the eval generation bit is not that hard. It it it should be doable by agents to build. You just need a human in the loop to say, hey, um, this is the approach we're taking. Do you agree with this judgment? Do you really agree that we should look more towards hidden gems rather than reach out to um um big tech employees? And that's about it. You don't need the human to actually build the evals. You need them to calibrate

**[15:02](https://www.youtube.com/watch?v=7taOQBfjDyE&t=902s)** the evals. And agents should be the ones that really take the the the taste of the maker and and put them in into code. Once you have this, it's pretty easy to create recipe candidates. And this should be the the diffs that you really want to taste. Um, and you can have a pretty good offline evil set around this, but the the the test here is when you go to prod. So, do the end user agree with your taste of not hitting up um big tech uh employees, right? And this is kind of like what you want is you build a product that really emphasizes your taste and then you you make sure that your users appreciate and value that taste. and AB tests have been a way to to to make sure that that's the case. Um so with a multi-arm banded um

**[15:51](https://www.youtube.com/watch?v=7taOQBfjDyE&t=951s)** scenario for example you you'd be able to do that pretty well. So once you validate okay I have great taste and my users believe uh I have great taste as well that's when you promote and that's kind of when you go to to the next version of an agent recipe. The secret is you keep doing this over and over again and you know how to continuously codify your taste and your um what what what good is to you into an agent that can reproduce the same service or product uh for other people and they also agree you have great taste and you have great execution. And this is really kind of like the the secret of building good loops is okay can can someone iterate on my um system in a way as uh you know um a good example here is like Miranda from the Delor product right what would Miranda do uh in certain

**[16:40](https://www.youtube.com/watch?v=7taOQBfjDyE&t=1000s)** cases and you kind of want to codify that that thinking into like agents that can do the same stuff at a higher level. So the takeaways are this. Um the loop is the product. You try to automate yourself as the u as a um higher level judge and you want to make sure your second loop agents are able to apply the same judgment to to the agents you're trying to to to push to prod. Second bit system dissolation is the mode. So, how do you continuously inject that taste into these uh workers and they how how they continuously self-verify and work together is uh the biggest thing that you should focus on and the faster you do it uh the the the faster you you build a defensible um approach to to becoming a vertical AI company. And finally, valued work per

**[17:30](https://www.youtube.com/watch?v=7taOQBfjDyE&t=1050s)** watt is how you should measure um am I making progress or not. So first make sure that uh the the the work you're generating is valuable. Second make sure that the economics makes sense and the um the the difference in price is is basically what um people would would switch away from cloud code to to something you provide. We've been thinking a lot about these ideas and we're building some very interesting products around how to deploy this in production. We'd love to hear from you. would love to get um to to understand more about how how certain um vertical SAS companies are are looking to go to prod with um or how agent labs have been thinking about this idea of um um creating these like auto research uh labs around their their own

**[18:19](https://www.youtube.com/watch?v=7taOQBfjDyE&t=1099s)** products. um get in touch. Uh we're gonna be around the block for for chatting more about this. And thank you very much.
