---
id: LmQtSORYPfw
title: "How Clay runs 350 million GTM agents a month | Interrupt 26"
slug: how-clay-runs-350-million-gtm-agents-a-month-interrupt-26
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 12
published_at: 2026-06-24T12:39:07Z
video_id: LmQtSORYPfw
url: https://www.youtube.com/watch?v=LmQtSORYPfw
youtube_url: https://www.youtube.com/watch?v=LmQtSORYPfw
tags: ["Clay GTM agents", "go-to-market AI", "scaling AI agents", "LLM production", "agent infrastructure", "LangGraph", "LangSmith", "AI at scale", "go-to-market alpha", "outbound AI", "LLM caching", "agent cost optimization", "Jeff Bard Clay", "LangChain conference", "AI agents production", "rate limits LLM", "token cost reduction", "agent quality evals", "GTM engineering", "Clay Claygent"]
transcript: true
---

# How Clay runs 350 million GTM agents a month | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `12 min`

`#Clay GTM agents` `#go-to-market AI` `#scaling AI agents` `#LLM production` `#agent infrastructure` `#LangGraph` `#LangSmith` `#AI at scale` `#go-to-market alpha` `#outbound AI` `#LLM caching` `#agent cost optimization` `#Jeff Bard Clay` `#LangChain conference` `#AI agents production` `#rate limits LLM` `#token cost reduction` `#agent quality evals` `#GTM engineering` `#Clay Claygent`

[Watch the recording](https://www.youtube.com/watch?v=LmQtSORYPfw) · [Conference site](https://interrupt.langchain.com/)

## Description

Jeff Barg, Head of AI at Clay, breaks down what it actually takes to run go-to-market agents at production scale — not just one agent, but 350 million a month across an entire addressable market. He covers the four hard problems Clay solved: infrastructure reliability, throughput under spiky workloads, cost (including a 70% reduction via caching), and agent quality. He also introduces Audiences, Clay's new product for giving agents the context they need to recommend plays autonomously.

Chapters:
0:00 What Clay does and why GTM is an agent problem
0:55 350 million agents a month: Clay's scale
1:10 Why no creative advantage lasts forever
1:44 How to actually win: the fastest to iterate wins
2:00 Go-to-market alpha: the three levels
3:16 Why most teams stay stuck at level one
3:47 The loop Clay's best customers run
4:18 Why this looks like an engineering challenge
4:47 Four challenges at production scale
5:25 Challenge 1: infrastructure and durable workflow execution
6:21 Challenge 2: rate limits and the TCP/IP approach to throughput
7:30 Challenge 3: cost and caching strategies
8:36 Challenge 4: quality, context, and evals
9:39 What's next: Audiences and agent memory
11:12 Recap

Extra resources:
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview
• Meet LangSmith Engine: https://www.langchain.com/blog/introducing-langsmith-engine
• About LangChain: https://www.langchain.com/

## Transcript

*1,964 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=LmQtSORYPfw&t=4s)** >> Hi, everyone. I'm Jeff Barg. I'm the head of AI at Clay. Today I'm going to talk about scaling go-to-market agents. Not just running a single agent productively, but what happens when you need to run agents across your entire addressable market at production scale. First, I wanted to give some brief background on Clay. We like to think of Clay as the creative tool for growth. So put simply, we help you build lists of companies and people from our go-to-market data sets. We help you enrich those lists with 150-plus data integration providers and AI agents, and we help you orchestrate those lists into things like CRM enrichment, outbound campaigns, and more. We do this at quite high scale, and so we run over 350 million go-to-market agents every month.

**[0:55](https://www.youtube.com/watch?v=LmQtSORYPfw&t=55s)** We have a proprietary data set of over 40 million companies and 900 million contacts that our agents research over. And so you can think of Clay as go-to-market infrastructure for running these workflows. So why is go-to-market a hard problem? And why are we running so many agents? Well, we think in go-to-market that no creative advantage lasts forever. And you can think about this from the lens of cold email. Cold email deliverability rates have been going down for the past couple of years, for many reasons. But one of them is just the floor has continued to rise. Ever since GPT-4, you can write human-sounding emails. And you can think about this from the lens of your own inbox, where you're probably drowning in a bunch of outbound emails that may or may not be targeted for the things that you care about.

**[1:44](https://www.youtube.com/watch?v=LmQtSORYPfw&t=104s)** So how do you actually win in this environment? And we believe that the fastest to iterate wins. So you actually need to continuously evolve and build new outbound strategies and plays to be able to actually do better than your competitors. And we call this go-to-market alpha. So similar to in finance, where alpha is outperformance against the market, we believe there's a similar concept in go-to-market. So better audiences, better timing, better signals, better positioning than your competitors can yield actually great results. So how do you actually get to that go-to-market alpha? We believe there are three levels. So level one is individual AI access and literacy building. So deploying tools like ChatGPT or Claude to your sellers for things like call analysis or outbound copy writing.

**[2:34](https://www.youtube.com/watch?v=LmQtSORYPfw&t=154s)** That's great. But level two is actually centralizing that and deploying it across your sellers. So using Claude skills at the workspace level or after every call generating post-call notes. Level three is creating advantages that your competitors can't copy. So think about — we work with a lot of AI coding companies, and many of them build outbound campaigns where they're looking for people — they're looking for companies that are hiring for a head of engineering and have a lot of engineers that have starred their GitHub repo. So these are plays that are not transferable to their competitors and they're unique to them. So reaching that go-to-market alpha. We find that many teams get stuck here at level one. So their sellers might be using tools like Claude to analyze call transcripts or write outbound emails.

**[3:25](https://www.youtube.com/watch?v=LmQtSORYPfw&t=205s)** But it's fairly low leverage. Because you can write the best outbound email. But if someone doesn't want to buy your product or service, a creative email isn't going to actually change that. Much higher leverage is actually fixing targeting. So finding customers who already want to buy your product or service — you can actually get much more meaningful results. So our best customers really do this using a loop like this. They'll scan their entire addressable market, layer on signals like news articles, fundraising announcements, or bespoke data points like that GitHub stars metric that I talked about, they'll use agents to score those accounts to find out when is the right time to reach out to them and act at that time.

**[4:12](https://www.youtube.com/watch?v=LmQtSORYPfw&t=252s)** Finally, our customers will learn from those outcomes and iterate on those plays over time. So this looks a lot like an engineering challenge because you need to run agents across your entire addressable market. And so that's why many of our customers use tools like Clay to orchestrate this. And at Clay, we have our agent Claygent, which does a lot of these workflows. So it will do things like company research in order to find out: is this account a good company to reach out to at this time? We run this over 350 million times a month. It processes trillions of tokens every week. And I'm going to talk about four challenges that we've encountered and lessons that we've learned on deploying this agent at scale. The first challenge is on infrastructure, where we actually deploy this in a reliable way. Second is on rate limits and throughput.

**[5:02](https://www.youtube.com/watch?v=LmQtSORYPfw&t=302s)** So being able to maximize our inference capacity without negative impact. Third is on cost. As much as we'd like them to be, trillions of tokens are not free. And fourth is on quality. If our agents don't yield meaningful results, then none of the other points really matter here. So we need to make sure that our agents are high quality. First challenge: infrastructure. If you're a prolific client, or probably like many of the agents that you all are building today here, most of our agents are actually just spending their time waiting. So they're waiting on, in our case, browsers or APIs or inference. So we used to run Claygent on Lambda, and Lambda was prohibitively expensive, because Lambda charges for wall time.

**[5:50](https://www.youtube.com/watch?v=LmQtSORYPfw&t=350s)** So we moved that to ECS. But with ECS — we traded cost for reliability. So we needed to re-architect our system to be able to recover from things like random host failure or things like that. So the right architecture looks actually much more like a durable workflow execution. So using things like queues, checkpointing your agent at periodic steps. So using a tool like LangGraph or LangSmith deployments would help here. The second challenge that we've run into is rate limits. We have a lot of dedicated inference capacity at Clay, but our workloads are fairly spiky. And so we need to be able to maximize the inference that we have in order to productively run our agents. There's so much effort at the inference layer

**[6:37](https://www.youtube.com/watch?v=LmQtSORYPfw&t=397s)** to make sure that GPUs are always hot. And a lot of that gets lost at the application layer unless you're actually maximizing the inference that's available to you. So we've actually built a system with back pressure to be able to adaptively throttle against our downstream inference providers. And it looks a lot like the TCP/IP congestion algorithm, where we basically will send as much traffic as we can. And as soon as we run into rate limit issues, we'll progressively dial back that traffic. And we've found from some of the experiments that we've run internally that this can yield four to ten times as much throughput as a more naive system. So it's actually quite meaningful, especially at Clay's scale. We also had to build fairness across our customers because we don't want a single customer who's running millions of agents across their market to crowd out the customer who just signed up for Clay

**[7:26](https://www.youtube.com/watch?v=LmQtSORYPfw&t=446s)** and is running their first 10 agents. The third challenge that we've had to deal with is cost. And cost is meaningful at our scale. We've built our own agent harness at Clay for a variety of reasons. But one of the learnings that we've found from building our own agent harness is that caching strategies have a really meaningful impact on the cost of your agents. And you can actually build agents around those caching strategies to make sure that you're maximizing that. For providers like Anthropic, this can yield up to 70% cost savings — quite high. The second strategy on cost that we found is actually bounding retries and tool calls before they sprawl. So you have to do this in conjunction with your evals. But we found that many times, if you force an agent to return

**[8:15](https://www.youtube.com/watch?v=LmQtSORYPfw&t=495s)** after a certain number of steps or a certain amount of research, it will actually yield better results than if you were to let it run to completion. And so again, you have to do this in conjunction with your evals. But use-case specific, this can be quite effective. The third point is actually measuring costs tied to quality and outcomes, which leads to our fourth challenge on quality. We spend a lot of time on Claygent quality, and we think it starts with great context. So for us, we give Claygent access to great web data and proprietary go-to-market data sets. We have an entire team dedicated to making sure that data set is accessible to agents in a great way. We also tune our agent harness specifically for go-to-market use cases. So we have offline evals, but we also have online evals to make sure that our harness is really targeted

**[9:03](https://www.youtube.com/watch?v=LmQtSORYPfw&t=543s)** for the things that people are actually trying to do in our product. And this is again where tools like LangSmith are really helpful to understand what you're optimizing for. One additional note on quality is that quality is also a product problem. So we built an agent builder in Clay where people can actually test and iterate on their agents before they run it at market scale. And by giving users these kinds of iteration tools, they actually have way more confidence to be able to run their agents at market scale. And yeah, we found a lot of success with this. Okay, these are the four challenges that we've run into: infrastructure, maximizing throughput, cost, and quality for running these agents at production scale. But what's next for Clay and what's next for Clay's agents?

**[9:53](https://www.youtube.com/watch?v=LmQtSORYPfw&t=593s)** Piggybacking off what I was talking about on quality and context, we really think that agents need great context to do great work. And so we spent the last six months or so building a product that we call Audiences. Audiences lets you aggregate all of your go-to-market data into one place. So from tools like Snowflake, Salesforce, Gong, and other call recordings, you're able to aggregate all of your data in one place. Layer on third-party signals like fundraising announcements, news articles, and more, and give that to Clay agents to be able to run outbound campaigns. Audiences is also the foundation for our agent memory. And we're using this to build what we call go-to-market intelligence, where agents are actually able to recommend plays based on the things that they've tried before and the

**[10:44](https://www.youtube.com/watch?v=LmQtSORYPfw&t=644s)** context that they have. And so they're able to actually complete this flywheel of improving over time based on the things that have actually worked before. This comes with all sorts of additional infrastructure challenges that we have — things like virtual file systems that are able to actually reason over the context that we have in Audiences, things like sandboxes. And if you're interested in these challenges, I would love to talk to you after this. To recap, a couple of things that I've talked about. One, go-to-market is fundamentally an engineering challenge. You really want to optimize your agents for infrastructure reliability, throughput, cost, and quality to be able to get meaningful results. You need to actually run your agents across an entire market to get great go-to-market alpha. And finally, observability is a feedback loop

**[11:35](https://www.youtube.com/watch?v=LmQtSORYPfw&t=695s)** that actually makes these agents better over time. And with that, thank you. Have a great rest of your day. (audience applauding) [BLANK_AUDIO]
