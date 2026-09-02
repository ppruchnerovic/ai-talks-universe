---
id: rZ4yJ2IvWCk
title: "Nikhil Chandhok - Building Infrastructure for the Agentic Economy"
slug: nikhil-chandhok-building-infrastructure-for-the-agentic
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Nikhil Chandhok"]
channel: "Berkeley RDI"
duration_min: 7
published_at: 2026-08-09T23:37:48Z
video_id: rZ4yJ2IvWCk
url: https://www.youtube.com/watch?v=rZ4yJ2IvWCk
youtube_url: https://www.youtube.com/watch?v=rZ4yJ2IvWCk
tags: []
transcript: true
---

# Nikhil Chandhok - Building Infrastructure for the Agentic Economy

**Nikhil Chandhok**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `7 min`

[Watch the recording](https://www.youtube.com/watch?v=rZ4yJ2IvWCk) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,290 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=1s)** NIKHIL CHANDHOK: All right. Thank you for the kind introduction. I know it's late, so I'll also be quick. All right. So I work at a company called Circle. Circle is a stablecoin issuer. For a lot of people who don't know stablecoin, stablecoin is a new type of money that exists in the world. Its roots are in crypto, as in traditionally understood as Bitcoin, or Ethereum, or whatever that is. But as of June last year, a law was passed in the United States called the GENIUS act. And the GENIUS Act made it so that you can transact with stablecoins just like you transact with money. And the law, it goes through 18 months of rulemaking. Rulemaking ends end of this year. By next year, GENIUS is live. Stablecoins are real money that real companies and real people

**[0:50](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=50s)** can use to do things, much like they do with bank money or any other money that they have. So I want to set that background, so people understand why I am here. So we're going to talk about building infrastructure for the agentic economy. Know that as we talk about that, my roots are on chain, like blockchain ecosystem from which USDC came out. And now, USDC is legal tender in the United States, hopefully, by next year. So a lot of the discussion today has been about agents, agent governance, and making sure that agents are secure, but a lot of that discussion is inward-facing. And one of the things that USDC does is it lives on the public internet. It is open money that lives on the public internet, like a user. And the typical user of USDC today, but changing rapidly is somebody who doesn't have access

**[1:41](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=101s)** to dollar banking rails. So if you live in the United States, there are 330 million of us. A lot of us have access to good banking. And it is very easy for us to go get a dollar bank account and get access to dollar payment methods. If you live across the world, and there are eight billion people around the world, six billion of them have a phone, and they don't really have a way of transacting with dollars. And so what USDC did first was made it possible for all of those people to start interacting with dollars. So those dollars live on the public internet. They don't live inside a bank. They're just on chain. You can see their transactions on chain. Agents, similarly today, much like money that lives inside are going to turn outwards.

**[2:29](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=149s)** That's our bet. Our bet is like, agents are going to be endpoints on the internet, much like websites are endpoints on the internet. And we are going to be racing to build these new agents as soon as we get the tech right. So I'm analogizing it with FSD. FSD, the way to think about it is like, hey, FSD was designed with the assumption that the roads are not going to change. But what if you could design with the assumptions that you could actually redo the entire transportation system, you could redo the entire highway system? That's what we think about when we think about using agents in USDC. So here are some examples. Agents don't tap to pay. This is a common modality. You go out, you tap to pay. Agents don't have a way of doing that. Next slide.

**[3:18](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=198s)** Agents can plug into existing financial rails. So you can give your agent your credit card. You can say like, hey, go spend money with my credit card. Now, imagine a world in which your agent spawns 100 subagents. And each one of them need value. And each one of them need governance. And each one of those actions by those subagents need to be programmable. It's not possible to do with existing payment rails. So a lot of the things that actually exist in the world, in commerce, and even in systems, like sophisticated systems like Android and otherwise, are built around what payments can enable and not enable. And what stablecoins do is they give you the ability to have programmable money, where you can assign logic to it, and you can do it without requiring the agent to have a bank account, without requiring the agent

**[4:07](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=247s)** to have a credit card. So if my agent spawns another 100 agents, which then spawn another 100 agents, each one of them can have a wallet, they can have an on chain wallet, they can have rules that govern that wallet. And you can actually do all of the tracking out in the open. So what are some of the other assumptions we've made? So in both traditional payment systems and in on chain systems, there's this concept of finality. What does it mean? Finality is when I have paid you money, and that transaction is final. That is a very important consideration. When you do a payment, when an agent swipes a credit card, the merchant is only going to get the money after the issuer bank has cleared the funds. So it is not full finality.

**[4:54](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=294s)** It's a really important concept. When you send money in on chain, you want to make sure that there is absolute finality for when the money has moved from wallet 1 to wallet 2. So probabilistic finality essentially compounds the risk in the system. If you have multiple agents, and if you're imagining a future in which there are millions and millions of agents, or there are more agents than there are humans, which is true for web pages and websites today on the internet, you cannot have probabilistic finality. Also, so far, a lot of the blockchain payments happen out in the open. They happen using a public ledger, which is great for auditability, but it's not great to do real economic value. If my wallet is fully public on chain, and you can see how much balance I have, it's very hard for me

**[5:44](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=344s)** to actually do a real economic activity, because I would be leaking out too much information. So we assume trust can be at the application layer. At agent scale, it is really, really difficult. Each assumption breaks for a reason, every assumption in our current payment system. And payment system essentially, which moves all of the values, assumes that the human is one step away, is always ready, is present for governance. What is the way to fix this? We believe there's a way to do this, which is open architecture, which is to make sure that all of these agents are running on open systems. They're able to interact with other agents on these open systems. Payments for these interactions are

**[6:32](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=392s)** happening in not just our stablecoin, but in any stablecoin that's available in the market. And it is open by design and open by necessity, because that's how the web evolves. The web evolved from a few NNTP and FTP servers back in the early '90s, for those who remember, to what is now an innumerable number of websites and web pages in the world. So this is what we're doing. We're doing it at agents.circle.com. We have a CLI. Please try it out. It's a marketplace of task-based activity that you can do. You can do payments as low as a millionth of a cent to actually get a task done. People are trying different kinds of tasks, everything from go infer this for me to go do this research or go write this piece of code for me. All of this is designed to be operated by agents for agents and off agents.

**[7:22](https://www.youtube.com/watch?v=rZ4yJ2IvWCk&t=442s)** Thank you. [APPLAUSE]
