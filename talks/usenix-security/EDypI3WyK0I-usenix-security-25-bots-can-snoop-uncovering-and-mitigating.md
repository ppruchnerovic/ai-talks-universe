---
id: EDypI3WyK0I
title: "USENIX Security '25 - Bots can Snoop: Uncovering and Mitigating Privacy Risks of Bots in Group Chats"
slug: usenix-security-25-bots-can-snoop-uncovering-and-mitigating
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 14
published_at: 2025-10-30T20:03:02Z
video_id: EDypI3WyK0I
youtube_url: https://www.youtube.com/watch?v=EDypI3WyK0I
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - Bots can Snoop: Uncovering and Mitigating Privacy Risks of Bots in Group Chats

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `14 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=EDypI3WyK0I) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

Bots can Snoop: Uncovering and Mitigating Privacy Risks of Bots in Group Chats

Kai-Hsiang Chou, Yi-Min Lin, Yi-An Wang, and Jonathan Weiping Li, National Taiwan University; Tiffany Hyun-Jin Kim, HRL Laboratories; Hsu-Chun Hsiao, National Taiwan University and Academia Sinica

New privacy concerns arise with chatbots on group messaging platforms. Chatbots may access information beyond their intended functionalities, such as sender identities or messages unintended for chatbots. Chatbot developers may exploit such information to infer personal information and link users across groups, potentially leading to data breaches, pervasive tracking, or targeted advertising. Our analysis of conversation datasets shows that (1) chatbots often access far more messages than needed, and (2) when a user joins a new group with chatbots, there is a 3.6% chance that at least one of the chatbots can recognize and associate the user with their previous interactions in other groups. Although state-of-the-art (SoA) group messaging protocols provide robust end-to-end encryption and some platforms have implemented policies to limit chatbot access, no platforms successfully combine these features. This paper introduces SnoopGuard, a secure group messaging protocol that ensures user privacy against chatbots while maintaining strong end-to-end security. Our protocol offers (1) selective message access, preventing chatbots from accessing unrelated messages, and (2) sender anonymity, hiding user identities from chatbots. SnoopGuard achieves $O(\log n + m)$ message-sending complexity for a group of $n$ users and $m$ chatbots, compared to $O(\log(n + m))$ in SoA protocols, with acceptable overhead for enhanced privacy. Our prototype implementation shows that sending a message to a group of 50 users and 10 chatbots takes about 10 milliseconds when integrated with Message Layer Security (MLS).

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
