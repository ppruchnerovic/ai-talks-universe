---
id: T3wRyXg_yVg
title: "Inside the AI Economy: What Stripe's Data Reveals — Nilofer Rajpurkar, Stripe"
slug: inside-the-ai-economy-what-stripe-s-data-reveals-nilofer
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Nilofer Rajpurkar"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-10-12T05:21:17Z
video_id: T3wRyXg_yVg
url: https://www.youtube.com/watch?v=T3wRyXg_yVg
youtube_url: https://www.youtube.com/watch?v=T3wRyXg_yVg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# Inside the AI Economy: What Stripe's Data Reveals — Nilofer Rajpurkar, Stripe

**Nilofer Rajpurkar**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=T3wRyXg_yVg) · [Conference site](https://www.ai.engineer/)

## Description

AI company revenue growth jumped from 120% to 175% in a year. Stripe's data shows what the fastest-growing companies do differently.

NEXT UP: AI ENGINEER CODE SUMMIT
Join us in SF for the second annual AIE CODE Summit, Nov 10–12, our last flagship summit of 2026. Applications live now: https://aie.codes

Nilofer Rajpurkar, product lead for agent and developer experiences at Stripe, uses Stripe data to describe four patterns among top AI companies: they build faster, sell globally from day one, price for the AI economy and adopt new go-to-market motions early. She demos adding payments to an app in Claude with Stripe's MCP server and agent skills, including a sandbox provisioned from the CLI. She also covers Replit's hybrid pricing, usage-based pricing across the Forbes AI 50, and why agent traffic to Stripe docs grew 10x in a year.

In this video:
• How Stripe's MCP server and agent skills guide Claude through a payments integration
• Why top AI companies sell in 48 countries in year one
• Hybrid subscription-plus-usage pricing, using Replit as the example
• Designing for agents as buyers

SPEAKER
Nilofer Rajpurkar, Product Lead, Stripe

LINKS
Stripe MCP: https://docs.stripe.com/mcp
Agents and AI on Stripe: https://docs.stripe.com/agents
Stripe AI toolkit (GitHub): https://github.com/stripe/ai

CHAPTERS
0:00 Intro
0:42 Four patterns among top AI companies
1:17 AI revenue growth data
2:12 Consumer AI adoption via Link
3:02 Building faster
4:26 Faster time to first paid customer
5:06 Demo: adding Stripe payments in Claude
7:26 Takeaways for building fast
8:21 Selling globally by default
9:10 Gamma's international revenue
10:25 Where AI spend is coming from
11:00 Local currencies and payment methods
12:25 Pricing for the AI economy
13:59 Replit's hybrid pricing model
15:04 Usage-based pricing principles
16:14 New go-to-market motions
17:14 Channel sales and agents as buyers
17:59 Agent traffic to Stripe docs
18:19 Adapting product and revenue infrastructure
19:53 Recap

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,655 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=1s)** [music] Good morning everyone and thank you for joining us here today. My name is Nil Farajj Par and I'm a product lead at Stripe. I work on our agent and developer experiences team and these are increasingly becoming one and the same. At Stripe, we work with some of the fastest growing AI companies, many of who are in this room today. And we get a front row seat into what's working, what's not, and how these companies scale. So today, I'm excited to show you some data from what we are seeing about how companies are building. So there's a few patterns that we're seeing across the top AI companies.

**[0:49](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=49s)** First, they're building faster. I think we can all see this happening in real time. Next, they're selling globally by default. On day one, the entire world is your market. Third, they're pricing for the AI economy. 10 years ago, subscriptions was the hot new model on the block, but this just doesn't work anymore. And last, they're adapting to new go to market motions very quickly. So, this is a bit of a big picture of what we're going to talk about today. And before we jump in, I want to ground us in a little bit of data. So in 2025, we saw AI revenue grow by 120%. A year later, we're seeing that now grow by 175%. Almost tripling. And so AI revenue growth isn't slowing down. In fact, it's on a tear. And uh this is uh what we're

**[1:39](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=99s)** going to be uh talking a little bit more about today. And the folks who are at the top of those AI companies are even more remarkable. Take Lovable for example. They uh reported 100 million in eight months and then eight months later reported 400 million. Curser had a 1 billion run rate in two years and then just three months later doubled to 2 billion. Anthropic shared that they went from zero in January 2023 to a billion just two years later and now they're at 30 billion. So the growth rate here is really wild. But we're not just seeing this in our B2B data. We're seeing this in our consumer data with our consumer product link as well. Our link data shows that consumer adoption of AI products doubled from just under 6 million to over 14 million in a span of a single year.

**[2:29](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=149s)** And all of those customers are spending more as well. Our top link buyers are spending almost $360 a month on AI tools and services, up from $183 just three months ago. So that's almost doubling in the span of a quarter. This is more than the average American spends on phone, internet, and streaming services combined. But the difference is users aren't treating this like a streaming service they might drop tomorrow. AI tooling is becoming a critical utility for them. So, we talked a little bit about revenue growth and adoption doubling, but the question is what's really behind all of this growth? So, I'd love to jump in with our first pattern that I mentioned, which was building faster, and talk a little bit about speed. So just like you no longer need months of engineering to accept a payment, you no longer need months of engineering

**[3:17](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=197s)** work to build and ship software. As of late 2024, iOS apps were releases were declining. And then you can see Agentic coding tools started to hit and that growth rate has grown quite uh substantially to 24% month- over-month. And we saw a very similar pattern with Delaware incorporations of new businesses as well. You can see where the graph starts to take off again aligning with the release of these agentic coding tools. So, everyone's talking about these non-technical founders who are vibe coding their way to new businesses and yeah, that's definitely true. But what we found interesting is that the share of technical founders is actually growing as well and grew 7% in the span of a year. Many of you in this room are technical and you're probably doing in a week now what was taking teams entire

**[4:07](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=247s)** months to do. And so what's really here uh salient here is that the speed is now available for everyone. For the nontechnical founders who are hosting and building using developer platforms or for the technical founders who are comfortable using things like cursor or claude locally. It's never been faster to build and monetize a product. And we actually see this in some of the data of developer platforms who are partnering with Stripe. So for some of our nontechnical users who are building with lovable forcell or replet, we're seeing something interesting in the data. Each successive monthly cohort is getting to a paid customer faster and faster. In fact, our latest cohorts are getting from a product to a paid customer in less than six weeks.

**[4:56](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=296s)** And that speed is available for a technical founder as well. So this should this experience gets better with some of the work my team is doing at Stripe releasing things like our MCP server and agent skills and steering. So I'd love to take you through an example here. I've got a new business vibe check and I am ready to add payments. So I'm going to jump into Claude, describe a little bit about my business model and tell Claude I'm ready to add subscriptions and invoicing support. Claude correctly recommends building with Stripe and it gets p it gets more powerful when you add in our MCP skills and our MCP server and our agent skills. But that uh information makes Claude deliver a better recommendation of how it should build the Stripe integration. So it uses our Stripe integration recommener MCP tool to ask me a little

**[5:43](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=343s)** bit of more information so that it can build the right integration for me. It's asking me where my customers are located so it can decide if it should recommend Stripe Tax or not. It knows to recommend Stripe Checkout over card elements because Checkout has a better subscriptions integration. So, I'll go ahead and tell Claude that my customers are located in both the US and the EU. And it tells me you probably want to go ahead and use Stripe Tax, which it learned from our agent skills, because in the EU, my digital subscriptions are subject to a VAT calculation and I am not a tax expert. So, I'll go ahead and take advantage of that. You can also see that Claude is provisioning a new Stripe sandbox for me. This is done via a new CLI command where an agent is able to create a Stripe sandbox without me needing to provide any Stripe credentials up front. It goes ahead and grabs API keys for the

**[6:32](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=392s)** sandbox and stores them securely. And so now I'm able to get to a working endtoend demo without having to exit Claude and see that checkout working completely. So Claude's gone ahead and managed my keys for me and then it's taking a look through the rest of our agent skills to make sure it delivers the right recommendation. It's now ready to ask me if I want to use the MCP tools to go ahead and build out my product catalog. And I'll say yes. And we'll skip a little forward to a completed product here. So now I have a subscription button on my website. I'll go ahead and click subscribe. And I can see a fully working checkout form ready to go for me to test this out. I'll provide some test card details. Go ahead and click subscribe. And I can see that test payment process. And there you go. Now I can see a full endto-end flow

**[7:20](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=440s)** of what my customers will see when trying to subscribe to my website without ever having to have left claude. So what does this mean for you in practice? First, you need to obsess over developer productivity. The best teams who are doing this are treating this like a priority and not as an afterthought because build times are compressing to be smaller and smaller. Our tools that we're building like our MCP server, our agent skills and steering as well as agent guard rails for sensitive uh actions like money movement should help you throughout this process. Next, you need to build, sell, and iterate all at the same time. The old playbook of building and taking a while before you get to your first customer just is too slow for the reality that we're living in. The best teams are doing this in parallel. And lastly, when confronted with build versus buy

**[8:09](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=489s)** decisions, top AI companies are doing both. They're building the things that they've identified are uh differentiators for them and buying the building blocks that they need to enable that. Okay, so building fast is one thing, but where you sell is just as important. So let's talk about what it means to sell globally by default. The old pattern here was that as a SAS company, I would focus on my home market and then once I feel good, start to expand into some other markets. A I might go hire a GM in London, build a new office and boom, now I'm an international company. But that just doesn't work anymore and is far too slow for what we're seeing with the top AI companies. The old SAS model would have had you in 25 countries in year one and then 50 countries by year three. But our top AI companies are

**[8:59](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=539s)** blowing that out of the water. In year one, they're selling in 48 countries and by year three, they're in 120 different countries. And this isn't about having a presence in those countries. It's about real paying customers in those places. Gamma is a great example of this. Perhaps they are. Let me tell you about them. So they uh are an AI powered slide and website builder and they've reported over a 100 million in revenue in their first year. Although they're based in SF, they're the majority of their revenue is actually coming from outside of the United States. And so what we're seeing is that they're not the exception anymore. They're actually the rule of how these top AI companies are building. Might get some slides back. I'll keep

**[9:46](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=586s)** talking anyway. And what we're seeing is actually across those top AI companies, 48% of that revenue is coming from outside of their home markets. So that's nearly half of every dollar that top AI companies are making. And so what we're really noticing here with this being up from 33% 3 years ago is that global revenue is no longer a bonus for your business model. It's actually becoming critical for how your business makes money. How we do it on slides. maybe. All right. Okay. So, I'll keep I'll keep walking us through here. Um, let's talk a little bit about some data that we're seeing uh of where people are spending the most on AI on Stripe. I'd show you a fancy map, so just pretend. Um, what

**[10:35](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=635s)** we're seeing is that some of the highest spend is coming from countries with the highest GDP. Unsurprising, right? So, countries like the United States, Japan, Germany. But what's more interesting is some of the hot spots that are emerging uh of where people are spending the most. This is in countries like Brazil and India and South Korea. And so it's clear that there's demand for AI services and tooling in those countries. But how do you make sure that you are capturing it? One way that we make that you can make sure you do this is by meeting your customers expectations and selling in currency that matches what they're used to and local payment methods that they know you want. they want you to support. In fact, we saw that companies who present prices in local currency saw almost 18% higher crossber revenue and

**[11:25](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=685s)** that companies who present and support at least one local payment method saw a greater than 7% conversion uplift and agents are increasingly knowing how to do this with our Stripe skills. You saw as we walked through the demo, Stripe uh the agent recommended that I use Stripe Tax, but it's more than just that. Through our skills, an agent knows that they should support local currency presentation and local payment methods so that you can help so they can help you optimize for selling in those local markets. You no longer need to be an expert in the markets that you are selling in because Stripe already is and can help you with that. So, here's a few things to think about to pressure test your global readiness. First, localize your prices and payment methods in the markets that you're going to be go going to be selling in. Next, automate tax collection because nobody

**[12:14](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=734s)** wants to get in trouble because they didn't know the tax rules. And last, track your revenue and conversion performance by countries and optimize ruthlessly. Okay, so let's talk a little bit about how pricing is changing for the AI economy because the models we're used to aren't quite working anymore. We're used to thinking about the value of software as a tool. You might spend 10k on Zenesk and then go buy go hire some customer support representatives to actually handle the customer support tickets that are coming into you. But AI is fundamentally shifting how we think about that value. As products gain agentic uh capabilities, we're actually able to see them deliver on value and we can think about their value as a as an output of that result. For example,

**[13:02](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=782s)** Intercom's Finn actually goes and manages and resolves customer support requests for you. So, as we start thinking about this new model, that value actually starts to become measurable, counted in things like resolutions commits workflows completed, and then we're forced and incentivized to start thinking about how we price our products to actually communicate that value. And thinking about this repricing isn't new. We've done this every time we've had a major technology shift. We started with the on-prem software where things were pretty stable after an install and so a one-time license made sense. But then we moved to cloud and your software was getting updated continuously and so a subscription model started to fit the bill. And about now is where you expect for me to tell you what the right model for AI is. So I've got some good news

**[13:49](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=829s)** and some bad news. The bad news is we're in the early innings. We're still figuring this out. But the good news is we are seeing some patterns emerge amongst our stripe data. Take replet for example, a developer platform that has been around for almost a decade. When agentic coding really started to take off, they re pivoted their product and rethought their pricing and have since seen hockey stick growth. They started with a flat subscriptions model and then added on credits as AI became core to their product. subscriptions for predictability for their users and then usage for value capture. And so the result is that Replet is aiming for a 1 billion ARR this year. And they're not alone in thinking about their pricing in this

**[14:36](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=876s)** way. Usagebased billing is becoming critical for anybody selling AI services. In fact, two and three of the Forbes AI50 companies have some form of usagebased pricing and many are delivering that sort of hybrid model that Replet is. The subscription piece helps you anchor in your relationship with your customer and provide them that predictability. And the usage based pill uh billing piece helps scale with the usage uh that your customer experiences as they grow. So knowing you need to be usage based is one thing, but what does that mean in practice? Here's a few principles to think about. First, price in your customers language. Developers think in tokens. Enterprises think in seats. But more and more everyone is being uh exposed to and becoming comfortable with consumption. And so think about how you

**[15:25](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=925s)** can communicate the value that your uh users are receiving in the way that you communicate the price. Next, you want to give your customers real time spend visibility before they get their bill. No one has opened up their electric bill and thought, "Huh, that's cheaper than I expected." And you don't want the same to be true with users of your products. So, make sure that you're communicating their real-time usage so that they understand what the the cost is going to be at the end of the day. This is not just a nice to have. It's critical to prevent user churn. Lastly, think about selling credits, not costs. Have your users exchange money for credits on your product upfront and one time so that when they're using your product, they're thinking about the value that they're they're experiencing and not the dollars and cents for every action that they're taking.

**[16:14](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=974s)** Okay, one more trend for us to walk through here and this is how companies or top AI companies are adapting to new gotom market motions. So the old pattern here was you'd build a product, you'd have a productled uh growth uh system here and you would expect companies and startups to find your product organically. Then at some point in a few years you'd transition to salesled as you found product market fit. And what we're seeing is that process is just entirely too slow in the way that new companies are building. And many companies are actually starting an enterprise sales motion early in year one of their uh build. Cursor, for example, started out in 2023 as a self-s serve model for developers, and they quickly realized they needed to

**[17:01](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=1021s)** build a salesled motion so that they could go land enterprise contracts. Now, Cursor has built a really impressive salesled motion that would have taken companies before months, if not years, to build. And that's not the only shift we're seeing. Yes, you're starting salesled emotions a lot earlier, but we're also seeing new motions emerge. For example, channel sales are becoming a much larger piece of the equation. Users are buying anthropic and open AI services directly through their cloud providers. And many of these AI uh uh products are actually introducing marketplaces so that others can do the same and sell through them as well. And then there's the billion or perhaps trillion dollar question. How do we adapt for our new buyers, agents? We've spent decades thinking about human

**[17:48](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=1068s)** psychology when pricing products, things like $9.99 instead of $10, good, better, best systems. But the thing is, agents don't care about any of these tricks. This chart might be the most illustrative of this. So in 2025, we saw agent traffic to Stripe docs 10x in a single year. This chart is showing human traffic to docs and agent traffic to docs. And you, as you can see, those lines are converging. And by the end of 2026, we expect that agents are going to be reading far more docs than humans and using that as discovery mechanisms for our products. So here's the part that most people underestimate. When you go to adopt new go-to market motions monitor, that's just the tip of the iceberg. There's a whole section that needs to move underneath. Every time you adopt a new

**[18:35](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=1115s)** motion, you have to adapt your product. You need to think about how onboarding is now going to change for those new channels. Your pricing model needs to adjust and your organization needs to be ready to support this. Supporting an enterprise customer is much different than supporting the long tale of self-s serve. So a new GTM motion really means a shift in the underlying business model of your company. Another place that's different is how uh companies actually build revenue infrastructure. Previously they would bolt things on and when you were going slowly this was okay. When you start to compress 10 years of go to market infrastructure into the matter of months the seams between each of these tools starts to become really really apparent and becomes a liability. As you're thinking about your customers as channel uh moving across any of these channels, here are some things to think

**[19:24](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=1164s)** about in your go to market motions. You need to have a clear articulation of how people move from self-s serve to an enterprise and how the pricing model changes when they do. You should build unified business systems. This means one representation of your customer, one product catalog, and unified data models across each of these services. And lastly, you need to think about how you're designing for agents as buyers. An agent needs to be able to discover, evaluate, and activate your product without a human in the loop. Okay, so we've talked about how the top AI companies are building, selling, pricing, and adapting to go to market motions differently now. building faster in the matter of hours and days, selling in 42 countries on day one, pricing for value, and starting an enterprise sales motion before they've raised their

**[20:12](https://www.youtube.com/watch?v=T3wRyXg_yVg&t=1212s)** series A. It's never been a more exciting or fun time to be a builder. My team at Stripe is focused on how we make sure that we're building the right things to empower you to monetize and build faster. So, if you've got any feedback or questions on how we can better support you in that journey, love to chat. Thank you so much. >> [applause] [music]
