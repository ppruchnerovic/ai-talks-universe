---
id: CvmZtAPmAW4
title: "78% Wanted This AI Feature. Almost Nobody Used It - Supriya Subudhi, Bumble"
slug: 78-wanted-this-ai-feature-almost-nobody-used-it-supriya
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Supriya Subudhi"]
channel: "AI Engineer"
duration_min: 15
published_at: 2026-10-31T09:00:01Z
video_id: CvmZtAPmAW4
url: https://www.youtube.com/watch?v=CvmZtAPmAW4
youtube_url: https://www.youtube.com/watch?v=CvmZtAPmAW4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Supriya Subudhi", "Bumble", "A/B testing", "AI product management", "generative AI", "AI evals", "LLM cost", "guardrails", "AI regulation", "experimentation", "product management", "AI Engineer", "AIE NYC"]
topics: ["Classic ML & data science", "Enterprise adoption & strategy", "Evals, observability & reliability"]
transcript: true
---

# 78% Wanted This AI Feature. Almost Nobody Used It - Supriya Subudhi, Bumble

**Supriya Subudhi**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Supriya Subudhi` `#Bumble` `#A/B testing` `#AI product management` `#generative AI` `#AI evals` `#LLM cost` `#guardrails` `#AI regulation` `#experimentation` `#product management` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=CvmZtAPmAW4) · [Conference site](https://www.ai.engineer/)

## Description

Bumble product manager Supriya Subudhi shares five lessons from A/B testing an AI photo feedback feature in a dating app with over 20 million monthly users. 78% of surveyed users said they wanted feedback, but only 10-15% used it; the average win hid odd outputs like telling smiling people to smile more; the best model cost about 10x more; switching to a cheaper model also shrank the results; and regulation meant the feature couldn't ship outside the US. She closes with five questions to ask before you call any AI test a win.

Chapters:
0:00 Intro
1:31 Bumble's AI photo feedback feature
2:38 1. Users ask for it, then ignore it
5:19 2. The average win hides the tail
7:54 3. Green dashboard, red bill
10:37 4. The win came from the model
11:49 5. There may be no global rollout
13:54 Five questions to ask

Supriya Subudhi

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,416 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=1s)** [music] >> Uh my name is Supriya. Uh happy to be here today. I'm here to talk to you all about why AB testing for AI products is weird. So, for those of you who don't know what AB testing is, it's just a method used to evaluate two versions of something with each other and see which is better. So, that could be two versions of an email where you're trying to see which one's getting more clicks. It could be two versions of a feature. It could just be a feature against what's already live right now. So, let me ask a quick question. Can I get a show of hands? Who thinks

**[0:49](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=49s)** that if an AB test comes back positive, that the feature should actually ship? Well, looks like a lot of you are smart and already know that uh when it comes to AI, things can get a little weird. But here, let's talk about why. So, what I found when um testing with AI features, specifically GenAI and using LLMs in consumer tech features, a positive result from an AB test is actually just where the journey begins. It's not where it ends. And we're going to go over um five reasons that I've specifically discovered that were problems that we had to overcome. So, I'm a product manager. I work at Bumble. Bumble's a dating app with over 20 million uh monthly active users.

**[1:39](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=99s)** And so, what does a product manager do? We represent our users. We know the problems that they face and we try to deliver things that can solve the problems while still being responsible for the P&L of a company because we don't have unlimited resources to be able to solve the problems. So, in order to talk through the five reasons that I think AB testing with AI was weird, I figured it'll be good for you all to have a visual example of what we actually shipped so that you can try to draw parallels with things that you're working on as well. The feature that we shipped was an AI photo feedback feature. In a dating app, naturally, everyone needs a dating profile. So, they would add pictures and they wouldn't know what good looks like. So, we essentially came up with with the

**[2:27](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=147s)** expertise that we had of what works and what doesn't work in a dating profile, we gave AI-generated suggestions of how people could improve the pictures that they were adding. So, let's go into the first one. That users ask for it and then they ignore it. Now, I mentioned that a PM is supposed to know the problems of our users, right? The tools that we have to do that is research. The journey begins with discovery. What are the problems that people have and how can we solve them? Surveys, customer interviews are great tools to find out. When we do research at Bumble, one of the almost unanimous problems that everyone always talked about was that they didn't know whether their dating profile was good enough and they didn't get any support from us in understanding

**[3:15](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=195s)** whether they were doing a good job or not. So, when AI came in and there was all that potential with LLMs, we knew immediately that this was a problem that we could solve. And so, we came up with different versions of how we thought AI could help people's dating journeys without actually doing dating for them. And so, when we showed people examples of AI support and guidance that we could give them, the the response was great. Almost 78% of the people that we spoke to came back and said they would love getting feedback from us and and tell us and and tell them how to do better. But when we shipped the AB test, which means that with 50% of the people getting the feature and 50% of the people not getting the feature,

**[4:02](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=242s)** we only saw 10 to 15% people actually using the feature. What that taught us was that openness to AI doesn't actually predict whether people are going to use the feature. And that's where we go back to product management 101, which is you need to really bake in the entire journey of using AI into what people are already doing in the app. Education and awareness are super critical. What we did was instead of building a standalone feature, which people could just somehow find within the app, we went into the journeys that people were already using. So, when they were adding pictures, we asked them, "Hey, do you want feedback?" When they were hitting a wall when they were trying to find someone to date and not finding any matches, we would ask them, "Hey, did

**[4:50](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=290s)** you go and check the feedback in your profile? Maybe you could change something." And that drove up adoption. It's really important that we obviously measure what it is we're trying to do. Um that is going to form the foundation cuz ultimately, if the survey is coming back with a positive result and you ship the feature, and you haven't actually looked at whether people are using it or not, and you won't be able to improve that adoption in the first place. The second thing that we found was that the average win hit the tail. So, when we shipped this feature again, the top-line results were great. More people were adding pictures to their profiles. The number of changes that they were making to adjust their profiles was more than the people who weren't receiving the feedback.

**[5:38](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=338s)** But when we went into the details, there were weird things happening. The AI-generated tips were actually telling people to smile more when they were already smiling in their pictures. And so, what that told us is that the positive average was not enough to evaluate the success anymore. We had to go into the details. Let's look at two examples before I share what we actually did. So, I think Spotify has something called an AI DJ. It generates playlists for people using AI. And then, let's imagine that there's your banking app which helps you budget and decide what you should spend on and how much you should spend in a month. The scope of error is quite different in both of these things. It's okay if two out of four of the songs that are

**[6:25](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=385s)** generated by AI are not good, but it's not okay if an app is telling you to spend $2,000 when you really can't. So, that's where guardrails come into place. That's where we started. Setting strong guardrails of what our AI-generated feedback should and should not do was super critical. We couldn't be telling people to change things that they can't control, their skin color, their height. These are things that the AI should not touch. The next thing we had to do was reading real outputs. So, this is where evals were super helpful. Now, there are way more experts here that know about evals than me. Uh you're in the right place to learn about that, but um setting up the right eval tools were super critical for us. We were able to dig in and see what real users were seeing when they were getting

**[7:14](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=434s)** feedback. And that was helping us actually see whether our prompt was actually doing a good job or not. And so, ultimately, the success criteria changed from looking at overall results of green versus red to what does the long tail of data have? Are we happy with the way different segments of users are receiving feedback? Um are women responding the same way to our feedback as men? Are different languages responding like people in different countries responding in the same way to feedback as well? Because maybe the language generated in French is different from the language generated in English. The third thing is that the green dashboard and the red bill. So, naturally, with generative AI, the

**[8:02](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=482s)** success comes with a cost. When we started, we knew that this was such a big problem for our users that we wanted the best quality of feedback and the highest accuracy. So, we went with the best LLM. Now, naturally, that was about 10x more expensive than a simpler approach. And then you add to that the cost of running evals on the solution that you've built. That was just too much. Now, Bumble is not a stranger to AI. I mean, the matching algorithm is also a use of AI. But, when it comes to ML, the cost is different compared to GenAI. In In an algorithm, there's a lot of upfront cost of compu- compute as well as uh training. But, then after after it's working, the incremental cost for

**[8:51](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=531s)** every user to use it is not that much. With generative AI, the more successful your product, the more people that use it, and the more often they use it, the more your bill increases. And so, what do you do? Maybe don't jump to the using the best model from the start. And it's very important to understand why you're using AI in the first place. There are a lot of my peers that I've spoken to who have just gotten mandates from their companies to use AI in their features and their product. But, you really need to understand why you're doing it. Is it for long-term benefits or is it for something short-term? Now, let's look at Amazon as an example. They have um an AI assistant that can help you buy something on Amazon.

**[9:39](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=579s)** Now, why would Amazon need to launch this assistant? Is it for short-term benefits that good recommendations lead to more purchases and therefore more revenue in the short-term? Or is it But, what if the recommendations aren't great? Does that mean they don't do it? Maybe not. In the long-term, having an assistant that you can rely on might make people choose Amazon over other e-commerce companies. And so, the reason to launch the assistant is just for brand equity and a long-term benefit of keeping your users on your platform. And so really understanding why you're trying to use AI is going to be critical here because your budget and how much you're willing to spend is going to come from that. From a short-term benefit, yes, maybe

**[10:27](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=627s)** the ROI can be a quick decision, but if it's for a long-term play, maybe it's worth getting that extra budget. So I spoke about the fact that we just jumped to using the best model. Naturally, the cost was way too high and we could not scale that. So we switched what we made the simple decision to switch to a cheaper model. But as the cost went down, so did the impact of the results because the accuracy went down as well. Which basically told us that the AI feedback that we were giving was and the the results that we saw from our AB test was due to the model that we were testing, not the concept of giving feedback itself. And so what did we do? What we learned at this point was just that we really need to test a lot and

**[11:17](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=677s)** being able to be data-driven was critical. And eval setups really help us do that. Looking at being able to test how much different models can impact different data sets, the difference in the cost, and then being able to retest different versions of prompts and feedback quite quickly, that was critical. And ultimately, we resulted in the cheapest option, which helped us get the good result. And now the last one, which is sometimes there just may not be a global rollout. So Meta recently launched Muse AI. I'm not sure if you all have used it. I'm from London, so I haven't yet. And that's because Muse AI is only available

**[12:06](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=726s)** in the US and Canada. And this is because AI regulation is constantly changing and is different all over the world. And there is a financial and legal risk to companies to not be compliant with that. So, when we started our project, we started in the US. We shipped in the US, but then that's it. Like we had to stop. We were not able to ship the feature that was available in the US as is to other countries. And so, what did we do? We realized almost immediately that whether you're a product manager or not, whether you're an aspiring product engineer, forward deployed engineer, everyone needs to start being a generalist and thinking about compliance and legal applications of products that they're

**[12:53](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=773s)** building early on. It can't come later. So, what that means is you can have multiple approaches. You could start with, "Oh, I definitely know I want to ship this feature all over the world. Therefore, let me understand all the restrictions and build something within all of those things." Or you could go the approach of, "Hey, I know that US is where I'm going to get my maximum impact and therefore I will launch the best thing possible in the US and then maybe not anywhere else." So, there's going to be a spectrum of decision-making that you will have to make with this new set of data. It's not just about building anymore. If you build the best thing, but you can't get it in the hands of users, it doesn't mean anything. So, you could take the path of, "Okay, one country." Or you could take the

**[13:43](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=823s)** additional cost of making a version of the app which works differently in different countries as well. That's the decision that now needs to be made. So, to summarize, I think whenever it comes to AI features, when you all are building, ask yourself these five questions. Are people using it or are they just saying that they will use it? Do you read real outputs or just look at the averages? Does it still pay off after factoring in all the costs that went into the solution? Is a win on the best model something you can afford? And are you clear legally on which markets you can ship in? Because the question is not just did the

**[14:33](https://www.youtube.com/watch?v=CvmZtAPmAW4&t=873s)** feature win the AB test anymore. Thank you. >> [applause]
