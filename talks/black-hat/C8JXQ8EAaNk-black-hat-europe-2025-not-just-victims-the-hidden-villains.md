---
id: C8JXQ8EAaNk
title: "Black Hat Europe 2025 | Not Just Victims: The Hidden Villains Inside Infostealer Logs"
slug: black-hat-europe-2025-not-just-victims-the-hidden-villains
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2026
speakers: []
channel: "Black Hat"
duration_min: 29
published_at: 2026-07-06T14:45:20Z
video_id: C8JXQ8EAaNk
url: https://www.youtube.com/watch?v=C8JXQ8EAaNk
youtube_url: https://www.youtube.com/watch?v=C8JXQ8EAaNk
tags: []
topics: []
transcript: true
---

# Black Hat Europe 2025 | Not Just Victims: The Hidden Villains Inside Infostealer Logs

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=C8JXQ8EAaNk) · [Conference site](https://www.blackhat.com/)

## Description

Infostealer malware is malicious code designed to infiltrate users' systems and secretly extract sensitive data such as browser information, system details, account credentials, cryptocurrency wallets, and screenshots. This stolen data is often sold or leaked on dark web platforms. While many victims are innocent, some are involved in criminal activities, which our research focuses on uncovering. Preliminary analysis of stealer logs revealed distinct behavioral patterns like multiple similar accounts and criminal conduct indicators, suggesting links to scams and illegal operations.

To better analyze these vast and complex datasets, we integrated Large Language Models (LLMs) that assist in organizing, classifying, and enriching loosely structured or ambiguous textual data within stealer logs. The LLM helped normalize vague entries and group related data, which was then stored in relational databases for efficient querying and visual interpretation. This method improves investigative efficiency and reveals actionable intelligence.

Importantly, our data collection adhered strictly to ethical standards by only using publicly accessible data without purchasing illicit sources. Although infostealers are inherently malicious, this research demonstrates how their leaked data can serve as valuable leads in tracking underground criminals. Future research aims to fully automate stealer log analysis using LLMs, enhancing the speed and accuracy of cybercrime investigations.

By:
HyunPyo Choi  |  Researcher, StealthMole
DoHyun Hwang  |  Researcher, StealthMole
Yejin Kang  |  Assistant Researcher, StealthMole
SangMyung Choi  |  CTO, StealthMole

## Transcript

*2,387 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=3s)** Hello everyone. We are here today to share our methodology we have developed under the title not just victims the hidden villains inside impostor logs. Before we dive in, I do like to introduce the team behind this project. We all work as Thermal Intelligence a company specializing in the deep and dark web intelligence. Thermal headquarter is in Singapore, but our R&D center is based in Korea. So, our team is based in Korea. Korean names are hard to call so just call us Harper, Haley, Kate, Simon.

**[0:51](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=51s)** I'm Haley. Let me explain the reasoning behind our topic and the project name. First, we need to understand what an impostor is. Impostors are a type of malware designed to harvest sen- sensitive information such as passwords, cookies, and cryptocurrency wallet such uh from infected systems. This harvested data is distributed across multiple platforms such as the deep web, dark web, and Telegram. One day, a question struck us. Could

**[1:42](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=102s)** impostor logs contain the information not just from victims, but also from attackers? We visualized this idea simply here. Our hypothesis was that impostor victims could actually be categorized into two groups, normal user and criminal suspects. I will simply call them suspect. Here is our agenda for today. We will start with a brief project introduction. Then we will move on to some case study case.

**[2:29](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=149s)** Next, we will introduce our Stellar Log Analyzer. After that, we will explain how we find the suspect. Finally, we will wrap up with three takeaways. Let's look at the background. You have likely hear of romance scam. They are also known as love scam, online dating scam, or catfishing. Simply put, this is a fraud where someone pretends to be a romantic partner online to gain the victim's trust and then demands money.

**[3:17](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=197s)** They usually approach victims via text message, Instagram, or dating apps. Next, we have news regarding illegal gambling. This article covers the arrest of a group running illegal gambling sites. Seeing this case, we wondered relevant if relevant information existed within impostor log. Fortunately, we had a massive amount of data that we collected ourselves. So, we investigated it. Especially looking for digital footprints of romantic scams and

**[4:08](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=248s)** illegal gambling sites. We are forced to forced to inspect every single file manually to find the cases. For an entire week, we stared at nearly 5,000 logs. Just a small part of our massive data set. Still, that was a bit much, don't you think? But, thankfully, we found what we were looking for before finishing the full 5,000. Here are two those cases.

**[4:57](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=297s)** Here is the first case. We found highly suspicious text and image file in the impostor logs. With titles such as building a relationship, clinic billing, first walk, sexual love making, and trust me fully. In one text file, we found a script designed to gain a victim's trust. We also discovered signed document, photos of a woman, and forged flight ticket. Next is a screenshot of the desktop background

**[5:45](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=345s)** of a suspect suspected illegal gambling site developer. Of course, gambling is legal in some ways, but we are presenting this case assuming it involves illegal operations. On the desktop, we could see information implying the user is uh developer for uh gambling sites. We opened a few of these files. They are written in Malay, and the English translation uh is as follow. We can infer that

**[6:34](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=394s)** this is a text used to recruit victims. To be clearly, we selected these specific cases because they are easy to visualize to visualize and share. However, however, we examine a vast amount of data beyond just these two identify suspects. But we couldn't keep opening files on one by one. Before we move on, I want to mention a few important disclaimers.

**[7:24](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=444s)** The suspects we mentioned are just that, suspects, not proven criminals. We handled all information in compliance with privacy policies. Our data source were open-source, meaning information available to anyone. And we did not engage in any transactions with criminals. There was recently a major news story in Korea regarding job fishing. It involved luring people with offer of high-paying job only to kidnap and imprison them,

**[8:15](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=495s)** forcing them to join criminal organizations. These incidents mainly occurred in Southeast Asia. The victims were forced to work in romance scam, gambling, and voice fishing. Therefore, we focused on Southeast Asia, assuming a high concentration of these criminals. So, out of our vast amount of data, we decided focus focus specifically on the data from Southeast Asia.

**[9:10](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=550s)** The system structure is as follows. Our parsed the low impostor logs into JSON and stored them in a database, processing the data to make it searchable via simple query. Let me walk you through what the low data actually looks like. First, we have auto fill and cookies, which track user activity. We can also see installed software and system info, including a running process.

**[9:58](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=598s)** Now, regarding password, while the logs do contain them, we decided to mask them entirely to protect user privacy. However, to identify if the same or similar accounts were used across different sites, we utilized the locality-sensitive hashing algorithm instead of plain text. Finally, to search through all these data quickly, we needed to normalize it into JSON file. But,

**[10:46](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=646s)** this is where we faced some challenges. To parse the data efficiently, we need these two build a parser. Assuming that logs from the same Imposter family would share a similar data format, we decided to classify the stealer first. There were many way to classify stealers, but we focused on file names. As shown above, if the stealer's is include, it's easy.

**[11:37](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=697s)** However, as shown below, sometimes the Stellar's name is missing. This was our first challenging. The second problem was that even within the same Stellar family, we found different format and variable name as shown here. These two challenges are caused by their reprocessing or version changing. As a result, parsing these logs proved to be a challenging task. So, we turned to an LLM.

**[12:28](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=748s)** We primarily used the uh Python parser, but all at G cases, we deployed on LLM. Any data the Python parser failed to process was handled by the LLM. As a result, using Python combined with LLM improved our parsing rate by about 15 compared to using Python alone. This is how we built our Stellar log analyzer. Hopper will take over from here.

**[13:22](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=802s)** Hi, I'm a Hopper. I will take it from here and the of specific case study we analyze using our tool. We all process 6 terabytes over Input Stiller for this demo. So, how does it work? We have a defined of four stage pipeline. Step one is crime analysis and the profiling. We don't just look at the crime itself. We profile the suspect. We analyze the crime to understand exactly what moves the suspect needed to make. Step two is query formulation. We take those behavior patterns and

**[14:10](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=850s)** translate them into technical queries that we can use search through Stiller rows. Step three is search execution. Using our system, we cast our nets. Depending on the search range, we might gather handful results, around 10, or massive data set over 1,000 hits. The last step is verification. Ultimately, the system is there aid our judgment. We review and verify the data to confirm whether the result points the legitimacy suspect. Let's see the tool in action to understand its workflow and verify efficiency gains over conventional

**[15:00](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=900s)** analysis techniques. Simply put, this query looks for five or more auto login dating service account in the service. >> It is the impostor on screen and show reports of impostor overs.

**[15:57](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=957s)** And the password filters puf.com is dating service. And it is find or 125 account in single computer. With a traditional method analogy analyzing this hypothesis to seven full days. However, with our tool we identified exact same suspect in just five minutes. This is massive time reduction in the cycle of hypothesizing, detecting and verifying. It means we are no longer limited by

**[16:45](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1005s)** time. We can now formulate more hypotheses, validate them instantly through search execution and identify suspects faster than ever before. We explore various hypotheses to detect a wide range of crimes. However, for today presentation we selected a specific case with a clearly distance hypothesis to demonstrate a definitive result. Our target was online gambling operator. Due to nature their business, these operators manage a numerous customers remotely and rely heavily on messengers

**[17:37](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1057s)** for transaction like deposit and withdrawals. This led to key hypothesis. Gambling operator needed to multiple instance over secure messenger like a Telegram on single machine. Based on this, we focus our search species learning on usually high number of Telegram process to pinpoint the operator. Of course, this behavior pattern applies not only to gambling, but to any cyber cybercrime involving large-scale customer management. First, let's look on processing of client

**[18:25](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1105s)** suspect using the tool. Input query to count process name is Telegram five or more, or you can see several users. These users learning multiple instance of a Telegram. We will check some stealer rows screenshot. >> Clearly their activities do not look

**[19:20](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1160s)** like typical office work. However, since our specific goal today is find on online gambling operator, we will set these other cases aside for now. And focus strictly on the user who matches that profile. Take a look at the this user screen. They are user using their monitors with four active windows. Let's look at the left side first. Here we can see core their operation. First, the online gambling admin page is on left. And banking portal is on right. Now moving the

**[20:11](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1211s)** right side, we can see WhatsApp mobile chat window and Google spreadsheet. That is obvious or ledger. It's clear how they are operates based on this side. They are using WhatsApp communicate continuously with customer and verify transaction while managing their finance through the spreadsheet. And if you can look at the taskbar at the bottom, you can confirm multiple learning instance of Telegram filled with messages just as a hypothesis. With just a single query, we retrieve

**[20:59](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1259s)** these specific steal rows which gives direct view into the inner working of their gambling operation. While we cannot disclose every detail right now, this level of intelligence is significantly different than what could be obtained through standard searches or conventional investigation methods. For our second case is we target software to involve active hacking operation. Specifically within broad spectrum of attackers, we narrow our scope to those distributing impostor malware.

**[21:48](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1308s)** We selected this specific profile because we believe it aligned best with the core theme of our presentation today. We hypothesized that system.txt This default is a standard artifact collected by impostor. Therefore, we reasoned that an attacker distributing this malware and harvesting data would likely possess high volume of this file on system. Based on this logic, we searched the file list for cases containing five or more system.txt files.

**[22:36](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1356s)** Let's verify results through the video demo. This query is count file list in how many system.txt file. And some stealer logs too many system.dat file. And look at this. Let's look at this all screenshot captured from infected device. The user was active on web browser when the wall data was stolen. Now take a look at bird shape icon.

**[23:26](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1406s)** I don't really call it this is the logo in for Luma stealer. It tells that the user was actually doing Luma auditing dashboard at the exact moment of infection. However, we had be careful. We needed to ensure this wasn't just static wallpaper or saved image. So we cross-referenced all the data with two verified that the user in fact accessing the live page. We found the no saved credential for the URL in the auto login data. However, we identified cookies associated with that domain confirming

**[24:16](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1456s)** that the page was accessed. Furthermore, the leaked data revealed access logos and login records for dark forum. This allowed us identify specific post authored by the user. Finally, the user was found possession of 145 collected stealers. Notably, these logos were not limited single country, but were distributed distributed across variable nations. Both cases present today relied on specific threshold through various

**[25:06](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1506s)** hypotheses involving this and value. We compound clear trend as an increase the proportion of identified suspect lies within significantly. In fact, in the demonstrated cases that came the threshold of five or more resulted in approximately 90% of the 30 lasers being possibility identified as suspect. However, we are not stopping here. We also analyze analyzed pure keyword-based searches. While they can

**[25:56](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1556s)** distinguish normal user, they are suffer from high rates of false positive and false negative. Therefore, we are not discussing new hypothesis to improve our system. Our goal is combine both methods into hybrid approach. It is minimizing and errors and maximizing detection accuracy. And so, who else can we find with this methodology? The potential is vast. We are currently targeting two specific groups for our next phase. First,

**[26:46](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1606s)** North Korean IT workers who disguise their identities to operate illegally. Second, blockchain articles responsibly for cryptocurrency theft and exploits. We are confident that our approach can be successfully adapted to detect this specific threat. And ultimately, we expect to expand our coverage to a wide variety of cybercrime types. To wrap up our presentation, I would like you to leave with your eight three key takeaways. First, learn techniques for discovering

**[27:36](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1656s)** new actionable leads. Second is extended parsing coverage by combining ADM. And finally, learn practical approaches and identify potential criminal based on digital footprint within stealer logs. Thank you for listening. I'd happy to take any question now. >> [applause] >> Thank you, very interesting. Did you

**[28:24](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1704s)** talk about where you obtained the stealer logs from? Or are you able to share that? Cuz I guess the more that you had access to the better, but ethically, maybe there are concerns. Uh we collected stealer logs from deep web, dark web, and Telegram. Uh but we can't share that because uh our company collected that, so we can't. Sorry. Next. Do you have any question? No? Okay. Thank you for listening our

**[29:15](https://www.youtube.com/watch?v=C8JXQ8EAaNk&t=1755s)** session. >> [applause]
