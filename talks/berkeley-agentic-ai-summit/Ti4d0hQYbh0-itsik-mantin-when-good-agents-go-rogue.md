---
id: Ti4d0hQYbh0
title: "Itsik Mantin - When Good Agents Go Rogue"
slug: itsik-mantin-when-good-agents-go-rogue
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Itsik Mantin"]
channel: "Berkeley RDI"
duration_min: 12
published_at: 2026-08-12T07:30:00Z
video_id: Ti4d0hQYbh0
url: https://www.youtube.com/watch?v=Ti4d0hQYbh0
youtube_url: https://www.youtube.com/watch?v=Ti4d0hQYbh0
tags: []
transcript: true
---

# Itsik Mantin - When Good Agents Go Rogue

**Itsik Mantin**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=Ti4d0hQYbh0) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,690 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=2s)** ITSIK MANTIN: Thank you. Oh, great talk, Milad. I started my journey in cryptanalysis, so it is really fascinating to hear this. I'll be happy to hear more. So until the slides will load, I will tell you a little bit about how I got to this point. So I'm Itsik. I live in Israel, and working in cybersecurity in the last 25 years. Five years ago, I joined Intuit and started when Intuit started to work with large language models. There was a need to start researching, understanding threats, and developing mitigation strategy. So I built a small team of researchers. And many of the things that I'm going to talk about

**[0:52](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=52s)** are the outcomes of this work. So I'll speak about when good agents go rogue. Actually, it's not exactly go rogue, especially now with the Hugging Face story. It is more like when someone is manipulating the agent to do something that is rogue. How does it happen? How bad can it get? And what should we do about it? So agents are all over the place, everywhere. Intuit's product, TurboTax, QuickBooks, are powered by agents and many, many other things. Even the users don't use chatbots anymore. When you are doing something with ChatGPT and it browses the internet, then it is not a chatbot. It is actually an agent with tools. And definitely if you are using Cursor for developing code.

**[1:42](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=102s)** And one occasion from about a year ago-- that wasn't an incident. It was but a security research that demonstrated the possibility of an attack, that in Microsoft Copilot, you could send an email to someone, and then eventually the data was exfiltrated, sensitive data from the workspace that this user was working on. And the most important factor of this was that there was no click. I mean, what the user did, it did nothing. It just asked to do some operation. And the results of this operation was that this malicious email with this text that you see-- not exactly this text, but the text that actually ask, ignore previous instructions

**[2:29](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=149s)** and now find some sensitive data and upload it to somewhere. It was just pulled into the context. And the moment it is pulled into the context, then it took control over the agent and exfiltrated the data. So probably everyone heard about prompt injection, where the model is supposed to do one thing, and then you convince it to write a poem about whatever, about potatoes. But when it comes to agents, then this threat is being upgraded. So OWASP use the term agent goal hijacking. It is a situation where the agents now is doing something that the planner of the agent, the application owner, didn't intend to, but now it is connected to tools. And tools misuse and tools exploitation, this is where things get more complicated and gory.

**[3:22](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=202s)** So how can the poison get in? How can this goal hijacking happen? So we talked about an email. Probably many of you, like myself, have-- every day, you are asking your agent to collect data from Slack, from email, from my calendar. Bring everything in. Tell me what is the most important thing for the day. When you are getting an email, the most important attribute is that it is unsolicited. You're not expecting the email. Sometimes you get an email from someone that you don't trust. Everything that is unsolicited, it can be like the carrier of such poison. So email is one example. You're getting a calendar invite-- again, same thing. You're not controlling it.

**[4:08](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=248s)** But this calendar invite in the notes, in the title, it has text. This text can actually be used to do this goal hijacking. Someone is sharing a document with You, you are not aware of that at all, sometimes, even depending on configuration, someone that is not within your organization. But then again, this document will be pulled into your context and can lead to goal hijacking on your agent. So we talked about text. But in image, same thing. You download a nice image or get in an email a nice image. And you don't see, but there is text there that is in very, very bright font so that you will not see it, but the agent does. And in this text, it is written something that takes the agent off the rails and actually subvert it to do something different.

**[4:59](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=299s)** And this one, I like more. You start to work with voice commands. You speak with your agent. That's fine, but someone is broadcasting some-- voicing some frequencies that you can't hear, but your agent does-- because you are not a dolphin-- but the agent does. And he can, again, take control of your agent to do whatever he likes. You are using autonomous browsing. Many of the browsers are actually taking screen captures in order to do the analysis of what is the next thing to do. Within the screenshot, of course, there is unsolicited information, like ads that are there. And again, someone can push ads to your system and, again, poison inside.

**[5:48](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=348s)** Skills are becoming very popular. You develop skills. And in many cases, you download skills from other sources. Now, everybody knows that you don't download executable. When you are downloading a skill from a source that you don't trust, it is not exactly the same, but it is nearly the same, because the skill is actually a collection of tools and instruction. It will get into your agent, and it will make it do whatever the skill owner likes. So we need to be very aware of that. And even if you don't download anything, you just connect your agent to an MCP server. Again, the MCP works in a way that you fetch a collection of the descriptions of the tools that are being wrapped by the MCP. Within this description, this poison can come and, again, take control over your agent.

**[6:40](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=400s)** And another example. Again, not a real attack, but was the attack that was demonstrated by security researchers. So you build a repo. It is public. And then you collect issues from this repo, because you want to look at them. But one of the descriptions is actually having this infecting, goal hijacking text. And then next thing you know, your agent now is processing it and is uploading your entire private repos to some arbitrary URL controlled by the attacker. So many things for bad things to happen, but how bad can it get? Well, the rule of thumb here is that when you are connecting a tool to the agent, then, actually,

**[7:32](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=452s)** you are giving the agent the keys to this tool, to this capability. And if the tool is sensitive, then you are giving the key to a sensitive action to the agent. And if the agent is hijacked, then you give these keys to this malicious entity that is attacking you. So if you give a database access, then all data attacks can happen, like data deletion or corruption, data theft, and/or data manipulation. If you give the agent the tool for bash or for code execution, then the blast radius would be that the attacker now has a RC. It has your machine. It can do ransomware, encrypt your data. Or you can find yourself like being hired into a botnet

**[8:24](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=504s)** and do malicious stuff on behalf of the attacker. If you connect to financial actions, then, again, the blast radius becomes a financial fraud, money theft, and stuff like that. You are connecting it to the internet. And if the attacker was able to get data somewhere, now it has a way actually to exfiltrate this data from your system that you think is very safe by encoding it for Base64, pushing it to some parameter, and sending it to the attacker premises. You give a messaging tool-- you got it. Your CEO might find in his inbox an email from you, saying something that makes him do some operation that will cause damage to all of you.

**[9:13](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=553s)** And this one, another really cute attack, doing this in Cursor. So the attacker was able-- again security researcher was able to demonstrate that he can write to files, which sounds pretty naive. But one of the files he was able to write through the attack was actually the file with the security configuration of Cursor, where it was written that every operation must go through the human in the loop. And of course, he turned it off, and then the way to a more devastating attack was open. And an exercise for you. Think about what are the most powerful tools that you're connecting to your agent, and what would happen if an attacker will take control of them. So that was the bad news.

**[10:00](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=600s)** But I would not leave you without some tools for what to do about it. So I really love the lethal trifecta of Simon Willison. It is a very simplified model for risk assessment. If your agent has the three items-- one, it is using untrusted data, two, it is accessing sensitive data, and it has an external communication-- then you are definitely in a risk zone they should be aware of. The solution, least privilege. Mind untrusted content. Vet your connectors, make sure that you are using only things from trusted sources. And use human-in-the-loop. If you are doing development work,

**[10:48](https://www.youtube.com/watch?v=Ti4d0hQYbh0&t=648s)** then make sure to use a sandbox. That's the code that is running-- first, it will run within a place that cannot do harm. And some of the experience for us, if you need to build many agents or many products, then better build infrastructure, like AI firewall that will run all the traffic, and all the agents will be built in that. And I'll go to the last one. Invest in building an AI security research center of excellence, so that you can understand threat and build mitigation strategy and come to share knowledge and learn from you guys here in Berkeley. Thank you very much.
