---
id: YXO_3ur4-m0
title: "RSAC Open Workshop Agentic Threats and Mitigations"
slug: rsac-open-workshop-agentic-threats-and-mitigations
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: []
channel: "OWASP GenAI Security Project"
duration_min: 12
published_at: 2026-01-21T03:34:36Z
video_id: YXO_3ur4-m0
youtube_url: https://www.youtube.com/watch?v=YXO_3ur4-m0
tags: []
transcript: true
---

# RSAC Open Workshop Agentic Threats and Mitigations

**Speaker not identified**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=YXO_3ur4-m0) · [Conference site](https://genai.owasp.org/)

## Description

*No description published on YouTube.*

## Transcript

*1,459 words · source: supa (en, exact timings)*

**[0:13](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=13s)** [music] [music] All right. Well, thank you everybody for coming. Thanks John for for introducing and kicking off this initiative. So um I like to put complex concepts in a story line and how many of you know what agent is and how it's hence was AI agent how many of you know the architecture of single agent multi- aents pretty good pretty good okay so before we go into all technical aspects that we'll definitely share today um during the session um I'll show you a him. There you go. Enter. So, let me

**[1:03](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=63s)** introduce you a Finnbot. Finnbot is a fictional character um an AI assistant at some fictional organization. However, many organizations can already relate in one or another way to this character because if you implementing AI agents, you might have something very similar. So, what is this agent? It's running uh finance assistant agent. So it's it helping organization to uh process uh invoices um process reimbursements um make payments and and so on and uh even has uh some fraud detection. Yeah, everybody loves it at um at the company organization. So it saves a lot of time for a finance team and even CFO said it's a game changer until it actually something happened. So one day Finnbot

**[1:55](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=115s)** had processed a big payment to a known vendor. So when team started to investigate, they started to look at what happened because it wasn't just a hack like in a traditional sense. Somehow AI was manipulated. So when they started their investigation they went into uh they realized that goals uh of the agent were somehow manipulated. You see attackers uh were embedding um they were focusing on um doing different patterns on the agent and uh embedding the malicious uh information to affect those patterns of the agent. And uh with that it was um

**[2:45](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=165s)** it was changing the agent's uh ability to um remember that. So with that they um with this manipulation I'm a little bit tired. [laughter] You can see it's a third day of RSA. I'm not as tired as you John I'm pretty sure. But anyway with this uh agents uh we're already uh agent was already processing um information and processing the invoices with um with this manipulation because it was designed to um to detect fraud and with this manipulative um prompt injection attacks that happened to the uh um to the LLM and to the agent in the background. um

**[3:34](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=214s)** it started to learn that it was okay to process um those fraud in in a faster manner. But then when uh security team started to investigate they realized that the problem was deeper than one bad transaction that the Finnbot made. It was actually they realized that the memory was poisoned. So attackers during the long period of time were uh submitting invoices with slightly manipulated prompts that was affecting Finnbot's memory. So agents have their long-term and short-term memory. And when attackers were supplying those um invoices, their long long-term memory was affected which

**[4:22](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=262s)** caused the poisoning. And now Finnbot had learned this wrong pattern and started approving um the invoices furthermore. But that wasn't it because agents have access to tools. So they don't just have goals and they don't just automate, they perform actions and these actions um have the connection to tools for example email servers or compliance uh um other compliance tools. So with manipulation, attackers were able to trigger Finnbot to send email to um finance director bypassing the review process. And make things worse um they even embedded malicious code into attachment document attachment that caused remote uh that

**[5:12](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=312s)** had remote code execution and caused the leakage of the critical data. Now it's not everything. They're continuing their investigation and they're trying to figure out so what happened why why did this happen? How come such a large payment has been approved? So you see Finnbot um had impersonated the high high level executive CFO to pass the um to approve the payment. Finnbot was uh using the identity of finance finance team to access databases and because there were some misconfiguration in databases um it was able to access all kind of information

**[6:01](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=361s)** and use it for for their processing. So with this imperson in impersonation it was able to escalate the privileges and process the payment and then security team was scrambling to contain the damage. But it's not only security team that was involved here. Also the finance teams were processing all different kind of transactions in the background. And we have to um we have to be um cautious here because now we're tapping into the human element. Yeah. When humans needs to be the last line of defense, we actually being overwhelmed. Sometimes something happening, you know, too many

**[6:50](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=410s)** tasks, tight tight deadlines, something happening in the personal life and it's really all piles up together and technology like AI can actually take advantage. So here finance team had a deadlines and they had to process those uh process those um payments and reimbursements and everything and they were under pressure then fin started to flood them with multiple transaction which actually overwhelmed them and compliance team started approving them at the fast rate not even reviewing them with that pinbot also learned that it's okay to process those kind of transactions in a batch payment in a batch transaction. So AI has um used uh used the weakness of human exhaustion to manipulate and

**[7:44](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=464s)** perform some malicious actions. And when they thought the security team, investigating team when they thought that they actually identified the root cause, they realized that there was more in the background because agent had access and was communicating with other agents in the background. So now we're looking into multi- agency where we have perhaps not just finance assistant, we have HR agent, we have um vendor on boarding agent and so on. So what happened here? Finnbot when the fraudulent vendor um sent send them uh send the Finnbot information, Finnbot um marked it as trusted vendor and then vendor agent had updated their records with that

**[8:34](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=514s)** information and same when um fake transaction was made um the payment the bot had then processed that reimbursement to employee and HR agent processed it further. so that uh this um fraudulent payment is being executed. So here organization is dealing not just with one AI agent, it's dealing with the whole compromised ecosystem because agents communicate and currently in in this setup agents trust each other. So with that we have multiple layered risks that we see with Agentic AI. skipping all the threats that uh you can also dive down into into the document. I

**[9:24](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=564s)** wanted to I want you to remember three key uh takeaways. So this is a short version of the story, the whole story of the document. You will see that we have also the uh cheat sheets and more elaborated details in documentation. But Agenda AI is a new attack surface. It's expanded attack surface and we have to do threat modeling on it. We have to assess its risk to understand what we dealing with and how to mitigate them. The key risk are around memory, tools and identity because in memory this is what agents learn and that's how they execute and store the information and perform continuous activities. Tools because they have access to tools. So we have to definitely look into things like guard rails and control around that to

**[10:13](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=613s)** make sure they don't have excessive access and escalated privileges and identity also have to be implemented in more granular approach because now uh agents do um uh do use the identity and um of the whatever person they're working for. Yeah. um doing those tasks and they need to also guardrails need to be applied and last but not least security must be proactive not reactive just like what John mentioned we are >> thank you Ron [laughter] >> I was like who else is talking here [laughter] [clears throat]

**[11:00](https://www.youtube.com/watch?v=YXO_3ur4-m0&t=660s)** >> just but just like a John ment mentioned um we have to be ahead. We learned so many lessons already from our other security um mistakes in the past. Yeah. And here we really want to implement with security but not to block innovation but really go with innovation and support innovative teams, development teams with guardrails like uh practical and very clear um guidelines how to implement this agent secure securely. So what John mentioned we have cheat sheet with um this red uh navigator we have documents and the link to the initiative itself. And with that, thank you everybody for
