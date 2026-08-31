---
id: HvMyYLTfvhg
title: "Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked"
slug: building-agents-is-trivial-now-context-is-the-next-frontier
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Jeff Ng"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-08-21T00:00:00Z
video_id: HvMyYLTfvhg
youtube_url: https://www.youtube.com/watch?v=HvMyYLTfvhg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked

**Jeff Ng**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=HvMyYLTfvhg) · [Conference site](https://www.ai.engineer/)

## Description

An agent built to enrich Linear tickets read a report that time to first character in Unblocked's own QA pipeline had gone from hundreds of milliseconds to three or four seconds, and recommended turning async dispatch back on. The recommendation was wrong. A support engineer had explicitly disabled that setting days earlier because it caused an outage. The agent had the ticket and the repository and reasoned soundly from both, but never saw the Slack thread where the engineers worked through the failure, or the postmortem that came out of it. Jeff Ng's point: standing an agent up has become the easy part, and missing context is what still breaks them.

Six months ago the same build took a team a quarter, because checkpointing, sandbox isolation, and observability all had to be solved first, none of which improves what an agent can do. Cloud primitives and agent frameworks have absorbed that work, so defining an agent now comes down to a model, instructions, tools, and a sandbox. What that removes is the plumbing, not the judgment a person supplies on every turn: why the code is the way it is, what broke last time, what the team decided to do about it. Something has to carry that load once nobody is babysitting, and Ng argues MCP does not, because access is not understanding and an agent left to reconcile contradictory results picks badly. He reruns the same agent against a context engine spanning docs, code, tickets, and conversations, and the recommendation flips from repeating the outage to preventing it.

Speaker info:
- https://getunblocked.com

Timestamps:
0:00 - Six months ago this took a team a quarter
1:02 - The taxes: state, sandboxes, observability
3:02 - Primitives and frameworks remove the plumbing
4:21 - Demo: enriching a Linear ticket
5:36 - The fix that had already caused an outage
7:00 - Why this does not happen locally
8:17 - What a context engine does
10:36 - The same agent, grounded

## Transcript

*1,949 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=1s)** [music] Hi all. Uh, my name is Jeff. I'm a founding engineer at Unblock and I'm here to talk to you about how building agents has actually gotten pretty easy, but unfortunately they still get things confidently wrong. So six months ago, it required a team's effort and basically a quarter to build out an agent. Um, an agent is more than just models and tools. It's the models, the tools, and everything required to build out a production service. Here are some examples of the different systems necessary in order to build

**[0:48](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=48s)** something out. Each one of these was basically its own company or at least a company function. Not going to go through each one of these, but you know, a few of that stood out to me. First one, checkpoint and state persistence. Agent runs, they're typically longived and stateful. U unfortunately, uh infrastructure itself though, those that's ephemeral. Crashing without durability can actually lead to a lot of state loss and that state kind of includes things like message history, tool calls as well as, you know, where you are in the loop. Without these things, you can't resume the session. Uh, one option is, you know, maybe you want to restart the session. Unfortunately, that's actually quite expensive as well. Uh, you lose out on

**[1:37](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=97s)** all the tokens that you'd originally used. uh as well as you know latency uh from a user experience standpoint you've already triggered that session now you have to wait for the whole thing to go again and lastly side effects your agent might have performed some side effects and now there's a chance of those doubling up so next thing sandbox infrastructure right so as we all know we're running more and more agent generated code as well as third party code this gets all run on your infrastructure And due to that there are some complexities. Uh because of that we want to introduce isolated signboxes which help prevent uh unnecessary reads of environment secrets, unnecessary network access. You know just in general we don't want to

**[2:26](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=146s)** take down the shared host. And then observability. How do we answer the question where did this fail? Typically, this includes tracking logs and traces from across half a dozen systems. Everything I've mentioned here, none of this actually improves an agent's capabilities. They're all taxes one has to pay in order to get an agent out there to play the game. Thankfully, things have changed quite a bit. Um the whole ecosystem has matured quite a bit and cloud infrastructure players such as cloudflare uh versel AWS they've gone and taken some of that complexity away and built primitives

**[3:13](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=193s)** that these frameworks flu Verscell Eve Mastra with these together you know they've taken a lot of complexity away and you can focus more on building the actual agent itself the core logic that actually helps you and your team and your customers. So here's an example of one. Uh I've played around with flu and cloudflare and as you can see on the left hand side, you know, we basically handle everything as mentioned before. So the primitives plus a framework lead to a situation where it's actually not that much code to define an agent. Uh, one of the things I was shocked at when I first took a look at the documentation to get in the details. All you really have to do when defining agent is a deciding

**[4:02](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=242s)** which model you want to use, b the instructions or you know the system prompt, c the tools that you want the act the agent to have access to skills, the things that can do as well as the sandbox location where things are being run. So uh to give you an example of this, I've actually gone and built out a issue enrichment system specifically for linear. So what this does is given a linear ticket and access to your code repository. It'll go out, you know, fetch a linear ticket, determine whether or not it's a feature or a bug. From there it'll do some code searching provide all that context to the agent and then come up with a plan of next

**[4:49](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=289s)** steps. On the left hand side here this is a issue that one of my colleagues support engineer had posted I think a month ago. Uh to summarize it what had happened was we had some pretty serious degradation in our agentic QA pipeline. time to first character was taken three to four seconds when it should realistically be in the hundreds of milliseconds. So let's see what happens when you know we put this through the system. So as you'll see here I've set up the agent to go fetch a given the skills and tools to actually go and fetch a code, search a code and query against that. That's being passed back to the agent which is doing some reasoning against that right now. And then just wait a little bit. At this

**[5:38](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=338s)** point, we've updated the linear issue ticket. The recommendation here is to reenable our async dispatch, which makes sense. It allows us to run a lot more of our QA pipeline in parallel on a single machine. Sounds great, right? Unfortunately, u this is wrong. This had actually caused an outage a few days ago and one of our uh support engineers had explicitly disabled this uh before this ticket was uh shown. So where did things go wrong? Why was the uh you know why did it get it wrong? The agent I had written it didn't have a full picture. it was missing the context from the slack discussion that happened after the issue where the engineers came together uh went through the actual

**[6:26](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=386s)** outage what went wrong what was the fix and the next steps it also was missing the postmortem uh linear ticket which came as a result of that in general it had a narrow understanding of the problem this concept of missing knowledge and intent that's sort across an organization and different systems is something that comes back in the back again. So I guess the next question is why don't we run into this locally? You know, we all use agents locally. We don't necessarily run into these issues. Well, you the human, the engineers, we currently act as that context layer.

**[7:14](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=434s)** When working with an agent, you know, you're there to ask questions, catch any errors, and supply the missing facts on every single turn. A person knew why the code is the way it is, what broke last time, and what we've decided to do about it. The agent though, it only has what's on the right hand side, right? It has instructions, the tools and skills we've specifically gated, the code, as well as a ticket in front of it. When an agent is in the loop, oh sorry, when a human is in the loop with the agent, we're there to catch the steer. Ultimately, we're there to babysit the agent. But as agents have gone trivally easy to deploy, as I've shown earlier with Flu, Cloudflare, the without the human in the loop, this issue becomes more and more prevalent. This missing context becomes a silent

**[8:03](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=483s)** failure. You know, all that intuition and knowledge that we've had as humans needs to be replaced. Something needs to carry the load. So that thing that's a context engine. A context engine is a system that provides task relevant information based on who you are and what matters. It also resolves all the conflicts across multiple data sets. It understands your access roles or their agents access roles and only uh respects that and only provides information that's relevant. And most importantly, it delivers a synthesized work.

**[8:52](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=532s)** What does an agent actually need? Agent needs clearly it needs context outside of just your source code. Think about everything that you need to work dayto-day. It's not just the code. It's you know the Slack discussions where decisions are made, the documentation where we show all the best practices. All that is important to your day-to-day process and that's true for your agent as well. So what we do here is we connect everything your docs, code, tickets, conversations. We then build a model of your organization, of your system, and we piece how all of these things work together and make it generally available to your agents. From that model, the agents are only provided a slice of that data which has been reconciled, ranked, and scoped to your permissions.

**[9:40](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=580s)** Scattered context comes in, grounded context comes out. The obvious next question is why can't we just do this with MCP, right? You could connect a Slack MCP, a linear MCP, a GitHub MCP, and with that all that data is accessible. MCP is great at access, but access isn't understanding. MCP hands agent the raw results and you know, you're now dependent on that agent to actually decide what to believe in. you end up flooding the agent with irrelevant data filling up the context window and you know overall context costs just go up. It also leaves a local agent to handle conflicts in data. You know your linear MCP and your Slack MCP may come back with different results. You're just leaving the agent to make

**[10:27](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=627s)** that decision somewhat ad hoc at this moment. So back to the original problem I had earlier. This is the same file, same agent, but now we've connected the context agent. Uh what we do here is is we're currently prompting unblock to do some research on the ticket and provide that context to the agent. So let's see that in action. Sorry about that. So here we go. Uh we're doing very similar thing. We're fetching the linear ticket, but you'll notice here that we're actually calling the unblock context engine. And what it's done here is actually it's found the relevant linear postmortem as well as a slack

**[11:14](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=674s)** conversation where we've had the entire discussion between the engineering teams. And as part of that, we've returned a understanding and that's now been provided to the agent as a summary. So the agent no longer has to actually reason from those documents. At this point, you'll notice here the agent now has been updated. Uh the recommendation has gone from breaking and causing another issue to actually preventing a another outage. So the example I've shown here is issue ticket enrichment. But this context layer can actually go a lot further. Uh for example, coding. Everyone here does

**[12:03](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=723s)** coding with claw code or codeex. Using an unblock context engine to actually hydrate the agent plan goes a long ways in terms of saving context and tokens. Uh code review, it makes their PRs look as if they've been reviewed by an expert on your team. Who doesn't like that? As well as surfacing the correct answers to your customer success team as well as sales. In general, there are many instances where you might want an agent to have institutional and tribal knowledge of your organization. Just want to leave you on this. I think this quote encapsulates what we're trying to solve at Unblocked. The gap isn't intelligence, it's context. So, thank you. U I'll be at booth P16 along with the rest of my team if you

**[12:51](https://www.youtube.com/watch?v=HvMyYLTfvhg&t=771s)** guys have any questions. There will be additional breakout sessions later tomorrow I believe that goes a lot more in depth of actually how the context engine works and you know how you can benefit from that. Cheers. [applause]
