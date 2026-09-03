---
id: Jwz0k8ZK9TE
title: "We Scored Oracle's Database Skill Live: 95% Isn't Enough"
slug: we-scored-oracle-s-database-skill-live-95-isn-t-enough
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: null
duration_min: 15
published_at: 2026-07-29T18:30:20Z
video_id: Jwz0k8ZK9TE
url: https://www.youtube.com/watch?v=Jwz0k8ZK9TE
youtube_url: https://www.youtube.com/watch?v=Jwz0k8ZK9TE
tags: ["AI agent continuation", "AI agent development", "AI-native development", "AIDevCon", "Oracle database", "Oracle skills review", "SQL skills", "Tessl skills review", "ainativedev", "best practices for SQL", "coding agents", "database MCP server", "database security", "how to write secure SQL", "what is a database skill"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# We Scored Oracle's Database Skill Live: 95% Isn't Enough

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `15 min`

`#AI agent continuation` `#AI agent development` `#AI-native development` `#AIDevCon` `#Oracle database` `#Oracle skills review` `#SQL skills` `#Tessl skills review` `#ainativedev` `#best practices for SQL` `#coding agents` `#database MCP server` `#database security` `#how to write secure SQL` `#what is a database skill`

[Watch the recording](https://www.youtube.com/watch?v=Jwz0k8ZK9TE) · [Conference site](https://tessl.io/devcon/)

## Description

Oracle's database team designed a skill to enhance AI agents' ability to write safer, more efficient SQL. During a live review at Tessl, it scored 95% on first go. The surprising part? It then corrected itself. It sounds like it shouldn't happen. Yet it does. The skill rewrote its own mistakes to perfection.

Anders Swanson, a database developer advocate at Oracle, brought this skill to the Tessl skills clinic for examination. He focuses on making Oracle's database system accessible for new developers, highlighting its wide-ranging capabilities from vector to relational features. His expertise ensures the skill encapsulates years of database knowledge in user-friendly tools.

What we cover:
• Why Oracle chose to develop a skill for encoding database practices
• How do live skill reviews ensure SQL security?
• Evaluating Anders' skill with Tessl's best-practice checks
• The role of skills in minimizing SQL hallucination and enforcing safe patterns
• The process of using a database MCP server for local development

Chapters:
00:00:00 - Introduction
00:00:28 - Meet Anders Swanson, Oracle's database developer advocate
00:01:29 - Digging into the Oracle Skills GitHub repo
00:03:27 - Running Tessl's automated skill review
00:03:51 - What the Oracle database skill actually does
00:04:54 - Pairing skills with a database MCP server
00:06:02 - Less hallucination: encoding niche SQL syntax
00:06:24 - Baking security best practices into the skill
00:08:24 - The results: a 95% review score
00:12:26 - How Anders builds skills for his own Oracle workflow

What aspects would you want your database skill to cover? Share your thoughts in the comments.

🌐 Try Tessl - we help you build a software factory, one step at a time: https://tessl.io
🔔 Subscribe for weekly episodes on AI-native development

What aspects would you want your database skill to cover?

## Transcript

*2,439 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=0s)** So we've done a review. It's giving you a 95% success rate which is actually very very high. I create skills for myself to kind of like encode this into different sub-agent workflows so we can split out, do all different steps of the SDLC, pull it back, clean it up, you know, tie it in a bow. I’m trying to encode the patterns that I did as a developer. Hey there Simon Maple here at the skills clinic, which we're running at the Tessl booth in AI Engineer in San Francisco. And joining me is Anders Swanson. Anders, you are a developer advocate in Oracle. A little a little startup that was born. To small a small startup. Yeah, yeah, I think I've been to the Oracle headquarters.

**[0:49](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=49s)** Headquarters? Right where the two. The big database building. Yeah. Campus actually. Really, really, really lovely. Just around the corner from here. Awesome. So you're a developer advocate. What area of Oracle? You're developer. So I cover all things database, which is quite a large area. I'm particularly focused on making the database attractive, easy to use, approachable to developers who might not have heard of Oracle. Never used Oracle. Just a little neutral in that area. And help them understand all of the amazing capabilities that a multi-model modern database can do. So things from vector to relational to graph spatial JSON documents all in one place. Amazing. I'm going to look at some of the skills that you've created. I'm very curious to see what's going. To happen there on GitHub. I think you mentioned right.

**[1:35](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=95s)** So slash oracle slash skills. Okay. And we have. Okay. So in here in fact what I'm going to do is if that wasn't I won't I quickly fork this over to my. So we'll put that as Oracle Oracle skills. Oracle Skills and we'll create that fork. And then I'm going to I'm going to clone this. And we'll have a look at some of the skills that exist in there. Now there's quite a few there's quite a few skills here. Right. So this is ranging different products. So we we have different directories organized by products and then subdirectories within those like in the database directory there's different skill directories that cover different components of the database. Right. Now there's a ton here right.

**[2:23](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=143s)** Which ones what which skills would you suggest we take. Let's drop into the database directory. Okay. So it's a CD db. Yeah. And then let's take a look. So this this is one overarching database skill that covers all kind of different things you can do with the database. I wouldn't say it's all encompassing but it has a lot of information there. So I think this is a good one to analyze. Okay. So what I'm going to do is I'm going to run. I'm going to run Tessl agent from this directory. And Tessl agent is essentially an agent. That is it's its life goal is to improve context and to understand what you're doing and how we can how we can make agents better with the context. So here I might say, take a look in this in this directory and see how many skills you can find.

**[3:16](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=196s)** Let's see what it can find across here. So each of these each of these directories are separate skills. Did you say. Separate information for the database skill. Okay. Gotcha. So there's one SKILL.md in that case. Yeah. Okay. So okay let's let's do a review of this skill. Now as we do this this is essentially it's kicking off its own review essentially comparing this to Anthropic best practices okay. You can override that if, you know, if. You have organization specific. Exactly exactly. So while this is running, tell us a little bit about what the skill is. So the skill if you're doing database development working on the database from really any perspective, the skill is to help you write better SQL, write better database code. The so your agents are knowledgeable about what the database can do.

**[4:05](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=245s)** It's not only to help your agents, but help you discover what the database is capable of, because when you ask, you know you maybe you want to do something with graphs, and then it's going to create a property graph of your schema using the database skills. So it can help discover it can help you. Right. And improve your database applications. Interesting. Just and who would be the user of this kind of skill. Is that is that maybe like another developer or it. Could be another developer. It could be a DBA. There are some operational level skills, like how do you start the database in a container, how do you deploy different components, connect to things. So some operational DevOps related stuff, some development stuff, basically any user of the database I think this could be applicable to. It's going to help them use it better. Nice.

**[4:54](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=294s)** And I would also suggest to use this in conjunction with a database MCP server, especially if you're doing local development, because then the skills can talk to the database directly using that tool. Calling activism. And what would you say as some of the things that because obviously skilled skills are great when you want to almost like supplement an agent's knowledge, right? So what is it? Would you say that an agent isn't as great at when, when when doing those database interactions that a skill is actually super needed to supplement that? Yes that's. Very like niche syntax. I spoke about property graphs before, but if you are working with something like that, you may want the skill to encapsulate the exact SQL syntax rather than having the agent go look up documentation, go look up blog posts.

**[5:44](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=344s)** I want it to be right there in the local file. It can pull that, add it to its context window, and Bam! It can go out and create a property graph over my relational schema without having to do as much work. And it's going to do it right because the skill has been refined. It's been it's been tested and it works. Yeah. So less chance of hallucination there. Yeah, yeah. Super interesting. Super interesting. Yeah. Because I guess one of the, one of the key things, because we know about a number of software security vulnerabilities as well when building SQL queries, particularly from code and things like that with. Oh. Sure, SQL injections and things like that. Yeah. Is there information in the skill here as well that will avoid those types of problems? We want to encode best practices as well. So not just the how but how to do it well in a way that is is scalable, is secure and you implies are known best practices.

**[6:35](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=395s)** Do you use do you use examples in the skill as well? Perhaps we should open up the skill actually. Yeah. Let's pull some up. Let's. I've got a code. Okay. Let's just keep this off. So if you pull up, for example the database containers one, it should have Docker commands or, or links. Where do I put this. Put it in here. No. Oracle or. Oracle skill database. Let's leave it there. So in the MD so obviously reference there's a whole. Bunch of lays it out. Yeah.

**[7:25](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=445s)** If you say open up containers for example. And then there's the whole set of how containers like a database container works here. Yeah. Tells you all about it. Like click on ADB Free. So tell you this is where the image is. There's the repository path. Here's the pull command. Additional information about it. Yeah. And then there's a run pattern down there as well. So if you wanted to set up a free container this this could help you with that. Yeah. Awesome awesome. I like the way you kind of, like, very much, you know, having small, contained pieces of context as well. That's, that's that's linked from a skill. Tree hierarchy.

**[8:12](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=492s)** So it can the agent can start at one place and then move down depending on what task it's trying to accomplish. Absolutely. Okay. Okay. So we have let's take a quick look. We have. Oh wow. So it's a really strong really strong result. So we've done a review. It's giving you a 95% success rate which is actually very very high. The validations all pass. So this is essentially more likely. Limiting and. Making sure of things. Everything's good. The markdown is such as correct. So I looked at your description. Now I thought your description is actually pretty good right. The description the ultimate. There's two things in the metadata of the SKILL.md right. Which is super important that the the agent will use early doors, which is the name and the description. It's the description that really unlocks the activation. So as I type something, the agent will say, oh yeah, I've got

**[9:02](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=542s)** I've got something like that that I know, I know can help me with. So your description is really strong. And, you know, it really helps with the, with the with the triggering content looks great. Conciseness is good. Workflow clarity these types of things. So recommended small improvement and verification for slow for slow query diagnosis and those types of things. But more verification steps with some examples and things like that. One thing that we could do is we could just say run, review fix. And what this actually does. Is. It applies those changes. So this is actually it's going to run again like a more agile style approach. And it will redo that review, add the changes and then rerun the run. So maybe we'll let that run and see you see how that goes.

**[9:52](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=592s)** See what I can do. See how that goes. Yeah. So so how long did it take. Like obviously there's a lot of context here. Yeah. How long does it take to actually grow over time. So this is the culmination of a lot of different subject matter experts at Oracle. So developers, product managers, very technical smart people who are extremely knowledgeable in their specific domain. Yeah. And this is why that's important is it's a lot of people in very different areas, which probably no one person has all of this information. And their efforts of contributing this making it available puts it in one place so your agent can be that one person. And this is also information that has been accumulated over probably cumulative hundreds of years of database experience.

**[10:41](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=641s)** Yeah. So yeah, that's. How. I you know, it. Have there been other folks outside in the community who have contributed to it, or is it mostly like. The check on the GitHub? Yeah, I think there's been a decent amount of contributions. Oh sorry. As we, as we look at like to pull in developers, we like to make, make sure people are aware of this when they're doing agentic work with Oracle. Yeah. Yeah. Yeah. I mean it's a. Relatively new within the last few months. Yeah. We had a decent amount of activity. Yeah. Always looking for if I mean, if you use Oracle and you have workflows or if you're interested in using Oracle. Yeah. Like it's a great place to start. It's great to see this interaction like not just to show.

**[11:30](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=690s)** Yeah that it's it's continually improving but also to show that people are using it and people are finding value out of it as well. Right. Yeah. So let's jump over to let's jump back here. Okay. So we're still we're still we're still running. And one of the interesting things here is you can see we have a max iteration. So what it will do is it'll make sure. Yeah. Doesn't just. Run. One couple. More times a. Couple of times before actually finding that providing those results. That's that's. That's good. Is this going to take in the information that it used previously. Yeah it can do. Sometimes it actually run it because because it runs multiple times. It will take those different sets of information. We have a workspace. In this case it's actually running this against the Rohan workspace. So what this is doing is it's also storing that data historically as well. So we. Can always. Work

**[12:20](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=740s)** for all of that as well. Yeah very cool. Let's see what I can come up with. Yeah. So how. Do you use skills internally Oracle. So I I've been a software engineer like my whole career somehow got into DevRel, but I still do a lot of hands-on coding. And the software development lifecycle is very important to me. Yeah. So making sure when we do software development, we're following the right processes. We're not, you know, adding undue complexity. Everything's all like dried up. It's it's simple and it's really like beautiful code. So I create skills for myself to kind of like encode this into different sub-agent workflows so we can split out, do all different steps of the SDLC, pull it back, clean it up, you know, tie it in a bow and make sure

**[13:13](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=793s)** these are trying to encode the patterns that I did as, as a as a developer. Yeah. Nice. Yeah. So I was finished actually made some changes. And those changes actually did put it up to 100%. So the threshold was reached and it was applied. So these changes have been made into the into the SKILL.md. In fact, what we'll do is if we jump here and take a look at the end, let's. See if. That's in the container. Oh, that is a. Drop it in a pull request to see what the yeah. Actually what it looks like. So what it's done is it's added a task with a recommended sequence. So for. Each of these various things it then tells you okay go to the explain weight events optimizer stats AWR reports and so forth.

**[14:02](https://www.youtube.com/watch?v=Jwz0k8ZK9TE&t=842s)** And it believes would have been really interesting is actually to create some scenarios here and see if there are see if there is value with and without the skill on your original management. Get some feedback out of that. Yeah, yeah. Awesome. I can send a pull request back. Yeah. Be great. Oh totally. I really, really appreciate you joining us on the Skills Clinic. Thank you so much. You said it. Yeah. Awesome.
