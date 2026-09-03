---
id: 0FacVWoVKkw
title: "AI Attribution: Measuring What AI Actually Did | Shopify"
slug: ai-attribution-measuring-what-ai-actually-did-shopify
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "Practitioner AI conferences"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: null
duration_min: 21
published_at: 2026-06-17T22:22:04Z
video_id: 0FacVWoVKkw
url: https://www.youtube.com/watch?v=0FacVWoVKkw
youtube_url: https://www.youtube.com/watch?v=0FacVWoVKkw
tags: ["AI"]
topics: ["Classic ML & data science"]
transcript: true
---

# AI Attribution: Measuring What AI Actually Did | Shopify

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `21 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=0FacVWoVKkw) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 2 - ANALYTICS & DATA SCI] As AI features become standard across products, teams face a critical measurement challenge: understanding how much AI actually contributed to user outcomes.

This talk introduces a practical framework for AI attribution — measuring not just whether users engaged with an AI feature, but the degree to which AI shaped the final result. We'll cover the full spectrum: from full acceptance, to partial edits, to abandoned attempts where users generated output but ultimately reverted to manual input. We'll explore AI attribution measurement approaches and a clearer understanding of how to assess AI feature impact.

SPEAKER:
Jill Cates - Senior Data Scientist, Shopify

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*2,792 words · source: supa (en, exact timings)*

**[0:19](https://www.youtube.com/watch?v=0FacVWoVKkw&t=19s)** my team will eventually run into. Once people start using your AI feature, how do you know that it's actually helping? I'm going to be using Sidekick, Shopify's AI assistant, uh for merchants, as a running example to walk through this problem. The story is about what happens when you move past measuring AI usage and start measuring what AI actually did and whether it lasted. So, just for a little bit of context, um at Shopify, I work on merchant onboarding, where we care about helping merchants get their stores up and running. We track milestones like first product added, first theme edit, and the first time that they unlock their store.

**[1:09](https://www.youtube.com/watch?v=0FacVWoVKkw&t=69s)** Traditionally, these are the signals that would help us understand whether or not a merchant was really making progress. But now, an AI assistant, Sidekick, can now do many of these things. So, they can easily uh the assistant can create a new product, um it could change a theme, or it could also set up payments. Which means that when a merchant hits one of these milestones, a new question comes up. Did AI drive that, or would it have happened anyway? That's the attribution problem that this talk is about. So, when you first hit this problem, the natural instinct is to use the metrics that you already have.

**[1:58](https://www.youtube.com/watch?v=0FacVWoVKkw&t=118s)** I like to think of these metrics as a ladder ordered by level of evidence. At the bottom, we have usage. Did people open the feature? With more messages and more sessions, it's easy to think that the AI assistant is doing a good job and that it's useful. But, it's also possible that somebody is constantly using AI and nothing's coming out of it. And in that case, it could be that the assistant is confusing and causing friction. Next, we have acceptance. Did the user apply AI suggestion? But, acceptance is just a moment in time. A merchant can click apply and accept the suggestions, but then revert back to the original state 10 seconds later.

**[2:46](https://www.youtube.com/watch?v=0FacVWoVKkw&t=166s)** These are the metrics where most teams stop because they're the easiest instrument. But, AI or sorry, but usage and acceptance um only tell you what happened within the AI session. Doesn't tell you whether or not it ended up in the product itself. So, the more meaningful layers are retention and outcomes. Did the AI-generated work survive and was that retained work associated with better results? And then finally, at the top is incrementality. Would this have happened without AI? That's the hardest question to answer and you can't really get there without uh the layers below it. So, how do you climb from acceptance to

**[3:36](https://www.youtube.com/watch?v=0FacVWoVKkw&t=216s)** retention to incrementality? This is where attribution comes in. It is the missing layer that helps you connect the AI output to the final product state. All right. So, what does attribution look like in practice? Well, it depends on the type of task. Some tasks are deterministic, which means that um >> [clears throat] >> I guess some examples include toggling a setting or enabling a field. Um and it means that AI either caused the state change or it did not. Other tasks are non-deterministic or creative. So, examples of these include writing a product description, editing a

**[4:24](https://www.youtube.com/watch?v=0FacVWoVKkw&t=264s)** theme, or choosing a color palette. The output is very subjective because there's no right answer. For deterministic tasks, full attribution makes sense. There's only one correct outcome. So, the So, if a merchant has to fix AI's work, um that's a signal that something probably went wrong. For non-deterministic creative tasks, partial attribution can actually be very valuable. AI gave the merchant something worth editing, and the edited version survived. When I first started looking into AI attribution, I assumed more automation was better.

**[5:11](https://www.youtube.com/watch?v=0FacVWoVKkw&t=311s)** In my mind, the ideal scenario was an AI doing a task end-to-end without any human in the loop. But, that's not how most people use AI. Someone with a strong vision of what they want to build, but no design background, doesn't know what color to choose, what fonts to pick, or how to make their homepage feel more polished. That blank page adds cognitive load. There are too many decisions with no starting point. This creates hesitation, and in some cases, it can also cause user to drop off. So, AI gives us or gives the users a starting point. It's not always perfect or final, but it's something to work off of.

**[5:59](https://www.youtube.com/watch?v=0FacVWoVKkw&t=359s)** In education research, this is called the scaffolding effect. So, what this means is a teacher provides a student just enough support so that they can get unstuck. And that's sort of what AI is doing here. It's not doing all of the work for the users, but it's helping them get past that blank page. If our metrics only counted full automation, we would miss out on the scaffolding effect that AI creates. So, if you start comparing AI suggestions to what actually got saved, four patterns show up. First is attributed. The final saved state matches the AI output. Next, we have assisted. The final state

**[6:49](https://www.youtube.com/watch?v=0FacVWoVKkw&t=409s)** is derived from the AI output, but the merchant made some changes. Next, we have abandoned, which is when AI suggested something, but the merchant or the user just threw it away. And then finally, we have um Oh, whoops. The bottom The bottom um title should be manual, which means that AI was just not involved at all. In my opinion, the boundary that's most interesting to study is between assisted and abandoned. Because assisted means that the user built on what a AI gave them, abandoned means they threw it away, and looking at that distinction starts to tell you whether AI is producing a useful starting point, or if it's just creating noise.

**[7:40](https://www.youtube.com/watch?v=0FacVWoVKkw&t=460s)** Okay, so let me show you what this attribution taxonomy looks like in practice using Sidekick as an example. Let's say a merchant opens Sidekick and says, "Help me create a product." AI suggests three things: a product title, a product description, and a product image. The merchant keeps the title exactly as proposed. In this case, it would be called attributed. For the description, they make some changes before saving, which counts as assisted. And then lastly, they reject the image entirely, which is, in this case, considered abandoned. If If we measured this as just one session, all we know is that the

**[8:28](https://www.youtube.com/watch?v=0FacVWoVKkw&t=508s)** merchant used AI. But if we measure each field separately, we can really see where AI worked, where it got edited, and where it got thrown away. When we start analyzing these patterns at a larger scale, we can see where AI is strong and where AI needs work. For example, if one particular field consistently has a high abandon rate, that could signal um for where we should um invest next. One of the hardest decisions in this whole framework, though, is defining the concept of similarity. How do we define the difference between an edit and a rewrite? Here's an example.

**[9:15](https://www.youtube.com/watch?v=0FacVWoVKkw&t=555s)** AI proposes a product title called "Handcrafted Ceramic Mug Ocean Blue 12 oz." But the merchant saves "Ocean Blue Ceramic Mug." Now, if we use the Levenshtein edit distance, it would tell us that it's a 64% rewrite. And in that case, we could probably label it as manual. But token overlap says that four of seven tokens survived, which is labeled as assisted. And then embedding similarity says that the semantic meaning is nearly identical, which counts as full attribution. So, we have three methods, three different labels for the same pair of strings.

**[10:02](https://www.youtube.com/watch?v=0FacVWoVKkw&t=602s)** Now, there's no right answer here. In practice, simpler methods like token overlap probably work fine for structured fields where the vocabulary is more narrow. And embedding similarity probably makes more sense on larger free text fields where people can rephrase an AI suggestion, but the meaning still stays the same as the meaning still stays the same. Um at the end of the day though, you just need to pick a method, pick a threshold, and in doing so, you've defined what similar enough means for your product. Okay so. In engineering, there is this classic meme of an iceberg. On top is this beautiful, pristine front-end experience.

**[10:51](https://www.youtube.com/watch?v=0FacVWoVKkw&t=651s)** And underneath it is this spaghetti mess of infrastructure keeping it all afloat. Well, in data, I like to think of this as our version of the iceberg. On top is a beautiful, clean attribution table ready for analytics downstream. But below the waterline is where the real work lives. Your data is likely scattered across many different systems. You have AI suggestions, admin events, back-end saves, um each with different IDs, different schemas, different latencies. And though And there are also product decisions that we have to make as well. For example, we need to decide on the right grain. Do you score attribution per session, per

**[11:40](https://www.youtube.com/watch?v=0FacVWoVKkw&t=700s)** field, or per suggestion? If you choose a field that's too coarse, um you lose this you lose the signal. But too fine and you're measuring edits within edits, which don't really mean anything on their own. So choosing a grain that makes sense for your team is super important. Okay. Then we have the scoring window. If you score at the end of the session, something looks attributed. But if you score 7 days later, that same thing could appear as abandoned. So the window that you pick defines your metric. We also need to define credit assignment. Let's say a merchant interacts with AI multiple times on the same field.

**[12:29](https://www.youtube.com/watch?v=0FacVWoVKkw&t=749s)** Which suggestion gets the credit? Last match is a natural default. Um you compare the saved state to the most recent suggestion. But in that case, the first suggestion that unblocked the user gets zero credit. It's just a trade-off that you're going to have to be willing to make. And then lastly, we have deduplication. The same action fires events across multiple systems, and if you don't collapse them, you could be crediting an AI multiple times for the same work. So the attribution table is the tip of the iceberg, but the decisions and data transformations that live below the water are what keep it all afloat. And I just want to add that as a data

**[13:15](https://www.youtube.com/watch?v=0FacVWoVKkw&t=795s)** engineer, this is a huge part of my job. So even though it's like a small part of the talk, um it's it's a big part of of what data engineers do. Um it's not always the most glamorous, but data foundations are really important to be able to build proper attribution models. All right. So, when you score attribution at a more granular level, you see that the aggregate was hiding something completely different. Fields like SEO tend to survive because merchants don't have strong opinions there. They're happy to take whatever AI gives them. But price and vendor fields are the opposite. Merchants already know how

**[14:04](https://www.youtube.com/watch?v=0FacVWoVKkw&t=844s)** much they want to charge, and they already know who the vendor is or who made the product. So, those fields end up being mostly manual. Creative fields like titles and descriptions land somewhere in between. There might be less full attribution, but assisted rates are often very high. Merchants have opinions about how to describe their product, but AI gave them a first draft to start with. The moral of the story is, when you exclusively report at the aggregate level, you miss out on where AI is actually working and where it's not. And all of this is extremely valuable implicit feedback. You don't need to ask the merchants what they thought of AI suggestion and have all of these

**[14:51](https://www.youtube.com/watch?v=0FacVWoVKkw&t=891s)** [clears throat] questionnaires. They already told you by what they chose to keep, what they edited, and what they threw away. And that signal can feed directly back into the AI assistant to make it better. So, if creative fields are more assisted than fully attributed, should we be trying to close the gap? It's tempting to think that the LLM should just be a little bit better. But, let's think about what it would take to actually fully automate a product description. The AI assistant would need to know the merchant's brand voice. They would need to know their target customer, and also what makes their product different from the 10 other variations on the market. That's a lot of context to get right.

**[15:42](https://www.youtube.com/watch?v=0FacVWoVKkw&t=942s)** For some merchants, especially ones just starting out, full automation full automation might be a good start. But, for merchants who have stronger opinions about their product, we really just need to give them a draft that they can personalize on their own. And that is usually enough to unblock them. Um and there is recent research that backs this up. So, there's a paper on the economics of AI automation, which found that for most tasks, partial automation is not the compromise. It is the long-run equilibrium. The reason for this is that AI follows scaling laws. The cost curve is convex, which means that getting getting from decent to good is relatively straightforward and easy,

**[16:32](https://www.youtube.com/watch?v=0FacVWoVKkw&t=992s)** but getting from good to nearly flawless is wildly expensive. At some point, pushing for more accuracy costs more than the human labor labor it would replace. The paper also found that complexity matters, too. They confirmed that low-complexity tasks lean towards full automation, but complex multi-step tasks usually have a human in the loop. The takeaway here is for a lot of tasks, human AI collaboration is not the stepping stone to full-blown automation. It's actually the end desired state. All right. So,

**[17:21](https://www.youtube.com/watch?v=0FacVWoVKkw&t=1041s)** attribution gives you the full picture of what AI contributed. The problem is when it becomes a number that people optimize for. That is when Goodhart's law kicks in. And Goodhart's law, for the people that don't know, is when a metric becomes a target, it ceases to be a good metric. Um and in this case, teams can inflate the metric by showing AI AI more aggressively. For example, defaulting users into AI-generated states or making manual paths less visible. Attribution goes up, but the actual experience could get worse. So, you need guardrail metrics to stay honest. Things like edit rate, revert rate, retention. If attribution goes up and

**[18:10](https://www.youtube.com/watch?v=0FacVWoVKkw&t=1090s)** retention goes down, something's wrong. It means the suggestion was good enough to accept in the moment, but not good enough to keep long-term. And you can also go one step further. Do merchants who keep AI's work actually hit key milestones faster? And do they also make more sales? That's the real test. Not whether AI contributed, but whether the contributions really mattered. And this brings us to a very important point, which was definitely covered in the previous presentation on incrementality, but attribution does not replace experimentation. There's one question attribution cannot answer. Would this have happened anyway?

**[18:58](https://www.youtube.com/watch?v=0FacVWoVKkw&t=1138s)** Let's say that we found that products with AI-generated descriptions have a 15% higher conversion rate than those with manual descriptions. It's tempting to say that AI is driving better outcomes. But think about who's using AI in the first place. It's probably not a random sample. Merchants who use Sidekick might be more motivated or more tech-savvy, or they could be selling in categories where descriptions matter more. The lift might have nothing to do with AI at all. It could just be pure selection bias. Unfortunately, attribution cannot untangle that, though. What it can do is make your experiments better and more targeted.

**[19:46](https://www.youtube.com/watch?v=0FacVWoVKkw&t=1186s)** Instead of testing does AI help as a global question, you can use attribution to target specific surfaces. For example, it probably makes more sense to run an exper- experiment on descriptions where we see high assisted rates versus price fields where it doesn't seem like AI is as beneficial. So, attribution surfaces the pattern, but experimentation is needed to really prove the lift. At the end of the day, you need both. All right. So, to wrap up, here are five takeaways. One, assisted is sometimes a success rate, especially for creative tasks. Instead of optimizing to replace the user, you should be

**[20:33](https://www.youtube.com/watch?v=0FacVWoVKkw&t=1233s)** optimizing to unblock them. Two, uh Okay, this is also the wrong version, but I will tell you what two should be. Um pair attribution with guardrails. Attribution on its own doesn't tell the whole story. You need to track guardrail metrics alongside it. If attribution goes up, retention goes down, something's wrong. Three, attribution surfaces the pattern, experimentation proves the lift. You need both to get the full picture. And lastly, don't measure don't stop at measuring usage and acceptance. Measure what survived. THANK YOU.

**[21:20](https://www.youtube.com/watch?v=0FacVWoVKkw&t=1280s)** >> [applause] [music] >> ALL RIGHT.
