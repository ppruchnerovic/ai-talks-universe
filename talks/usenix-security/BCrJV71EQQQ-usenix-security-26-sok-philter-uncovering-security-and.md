---
id: BCrJV71EQQQ
title: "USENIX Security '26 - SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing We…"
slug: usenix-security-26-sok-philter-uncovering-security-and
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 17
published_at: 2026-10-28T01:28:34Z
video_id: BCrJV71EQQQ
url: https://www.youtube.com/watch?v=BCrJV71EQQQ
youtube_url: https://www.youtube.com/watch?v=BCrJV71EQQQ
tags: []
topics: ["Security, safety & red teaming"]
transcript: true
---

# USENIX Security '26 - SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing We…

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=BCrJV71EQQQ) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '26 - SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing Website Detection Literature via an LLM-based Reasoning Framework

Mahbub Alam, Texas A&M University; Muhammad Lutfor Rahman, California State University San Marcos; Sonjoy Kumar Paul, Amy W. Hays, Aftab Hussain, Md Imanul Huq, and Nitesh Saxena, Texas A&M University

Phishing websites remain a dominant enabler of cybercrime. In response, many academic AI-based phishing website detection methods have been developed, often inspiring the design of real-world systems. Although most studies report high accuracy, it remains unclear whether they meet real-world requirements such as resilience to evolving phishing tactics, robustness on diverse benign pages, interpretability, and privacy. We present PHILTER (PHishing detection literature Inspection via LLMs and Targeted Expert Review), a scalable framework for qualitatively assessing phishing website detection studies across four functionality and three security metrics. PHILTER leverages LLMs to extract evidence and draft rationales, which experts then validate and use to produce the final assessment. Applying it to 55 academic approaches reveals systemic gaps. No study fulfills all functionality and security requirements. None show evidence of effectively addressing diverse phishing tactics. Most approaches struggle to preserve privacy and adapt to evolving attacker strategies, and many risk elevated false alarms in practice due to limited testing on diverse benign pages. We also introduce a taxonomy of detection strategies (feature-based, similarity-based, identity-based, and hybrid) that highlights design trade-offs and helps explain these shortcomings. Our study reveals that accuracy-driven evaluation overlooks blind spots that undermine practical effectiveness and exposes a key open challenge: achieving high accuracy while fulfilling all functionality and security requirements. We provide actionable recommendations to guide the design of future defenses that pursue this simultaneous goal against evolving and adaptive phishing campaigns.

View the full USENIX Security '26 program at https://www.usenix.org/conference/usenixsecurity26/technical-sessions

## Transcript

*1,590 words · source: supa (en, exact timings)*

**[0:19](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=19s)** Welcome to the presentation of filter. In this SO paper, we uncover security and functional gaps in AI based fishing website detection literature. My name is Mahabu Alalom and this is joint work with my co-authors at Texas&M and California State University San Marcos. Fishing detection papers report really high accuracy obtain over 98%. But fishing is the most reported cyber crime to the FBI. 191,000 incidents last year

**[1:08](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=68s)** and it's a gateway to major cyber crimes like ransomware and databases. Total cyber crime losses reached $20.9 billion in 2025. The problem is that benchmark accuracy doesn't tell us how these detectors actually perform in the real world. To understand the gap between benchmark accuracy and real world performance, we distilled four functionality and three security requirements and then developed a code book defining high, medium and low fulfillment

**[1:57](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=117s)** criteria for each. On the functionality side, we have fishing tactic diversity, benign page diversity interpretability and evaluation transparency. Attackers use many fishing tactics. Some impersonate popular brands like Facebook or Amazon. Others impersonate an organization's internal portal or regional sites. Some hide behind trusted shared hosting domains and some even put a capture in front so fishing content onlyly appears after you solve it. The problem is a method that works well

**[2:46](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=166s)** against a fake Amazon page may fail completely on a fake HR portal. So with fishing tactic diversity, we ask two things. Does the paper clearly scope which tactics its method can detect? And does it report a performance breakdown for each tactic it claims to handle. Similarly, we check if it is tested for false positives on diverse benign pages. Does it explain its decisions and does it report metrics that account for class imbalance? On the security side, the key challenge

**[3:36](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=216s)** is that fishing is not static. Attackers constantly change their techniques. New fishing kits, new page designs, new brands to impersonate. So a detector that performs well today may quietly degrade over time. We assess whether the method account for this evolution. We also ask can it resist adversarial and evasion attacks and does it protect user privacy. We followed Prisma guidelines to select a representative set of fishing website detection papers. We searched in DBLP using the query

**[4:25](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=265s)** combining fishing with URL or P terms and with detection or attack terms. That gave us an initial corpus of 288 papers from 178 venues. Then we performed abstract and full text screening to keep only the papers with AI based detection methods. This process left us with 55 papers in the final corpus. Then we categorized the selected papers into four groups by detection strategy. Feature based, similarity based, identity based and hybrid.

**[5:15](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=315s)** Feature based methods they train a machine learning classifier using features extracted from the URL or the page. Similarity based methods on the other hand compare visual or structural similarity with a set of reference sites. And if they find uh like using this method they identify whether the page under evaluation is actually mimicking a reference legitimate site and identity based methods. They infer whose brand or organization the page claims to be using the logo or the text in the page and the design and then

**[6:06](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=366s)** check whether the domain actually belong to that brand. and hybrid methods they combine two or more of this approach. This is filter our LLM assisted framework. First is paper goes to the two evaluator LLMs. So we have a LLM assisted preliminary assessment pipeline and it consists of two evaluator LLMs and one arbitrator LLM. So each paper is evaluated by the two evaluators and when they disagree the arbitrator LLM takes a second look

**[6:57](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=417s)** and this gives the evidence like relevant evidence to that specific requirement from the paper and give a rational for its uh first pass assessment. Then the two authors independently validate every assessment. So the experts take the evidence go to the paper and check if those actually uh makes uh the assessment correct or not and they give the final assessment. And we found that the experts agreed

**[7:47](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=467s)** with the ALM in 90 uh 89% of the time. And finally, we analyze these assessments and derive our recommendations across all 55 papers. A clear pattern emerged. Every detection strategy is strong on some requirements and weak on others. Here in feature-based method, 40 43% of them rate high on privacy. They use only page or URL features and run entirely on the client device. However, 83% rate low on B9 P diversity.

**[8:39](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=519s)** They evaluated mostly on popular domains. So, we don't know their false positive rate on small or regional sites. Many similarity based methods as high interpretability. They flagged the specific page elements that look suspicious, but 86% read only medium on drift adaptation. They perform temporal evaluation to check if the detection holds up if the page design change over time. But because the reference set is static, they cannot detect if an attacker impersonate a brand that is outside that

**[9:29](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=569s)** reference set. On the other hand, identity based methods are interpretable by design. They check they identify the brand it is claimed to be based on the logos and the text and the design of that uh page and then they check if that identified brand or the brand intention it matches the original domain. But brand domain verification requires an external lookup. So although they are interpretable, all of them rate low on privacy. Finally, 44% of hybrid methods rate high

**[10:23](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=623s)** on drift adaptation. They combine strengths from multiple approaches. For example, an identity verification step builds its reference set automatically, so it grows as new brands appear. But 89% rate low on privacy because of the same external lookups. Here's the key findings across all papers. Not a single study reported part tactic results. So we don't know which attacks these detectors catch and which they miss. Most studies test false alarms only on popular sites

**[11:10](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=670s)** overlooking the regional businesses and about half don't account for evolving fishing tactics. So a detector trained today can quietly go still and most of them transmit page content or screenshots of the device. So it risk privacy. Overall no paper satisfied all seven requirements. So how do we close this gaps? We give a recommendation for each requirement. For example, to address the fishing tactic diversity, we call for community maintained tactic annotated fishing

**[11:58](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=718s)** benchmarks and to report per tactic evaluation. This will help us to understand where our current detection methods can detect and which fishing techniques are still need uh attention from future research. For benign page gen generalization, we recommend for testing false positives on regional sites and also pages that use third party logos for uh legitimate reasons. For example, a benign page can use login with Google or share on Facebook buttons. Although they are

**[12:47](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=767s)** using Facebook or Google logo or buttons that does not mean that they are impersonating uh Facebook or Google they are just using them for legitimate reasons. So if we include all those diverse benign pages in the evaluation set, it will help us to understand that whether our detectors can differentiate between impersonation and the legitimate use of the third party brand assets. And we also recommend for enhancing the interpretability by surfacing suspicious page elements and brand domain mismatches. On the security side, we

**[13:38](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=818s)** recommend to develop drift adaptive mechanisms. For example, in uh similarity based method, the reference set is static. So we recommend to add a way to automatically refresh that reference set and also to test for temporal evaluation. So testing on the future uh fishing sets that that is not used in the data set for training. Another recommendation is to combine strategies with complimentary strengths. We have seen that many methods are good at some requirements and not good in others. So if we combine the

**[14:27](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=867s)** complimentary strength and keep uh the weaknesses u considered then it will be able to help overcome those limitations. So in next slide I will show how we can combine those strengths. This is an illustrative design combining complimentary strengths on the client side. A similarity based detection. It compares the page against a reference set against the uh sites legitimate sites with uh their brand logos and screenshots to understand uh or detect the

**[15:16](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=916s)** impersonation and it also flags suspicious page elements. Since it is in client side, no page content or screenshot leaves the device. This gives privacy and interpretability. But the reference set it can become outdated if it is not refreshed automatically. To keep the reference set current with the attacker as uh as the attacker impersonate new brands, new businesses, we have a serverside component. So here we have a crawler that crawls new p collects new pages and then it uh the new collected pages goes to the identity based method. We know that

**[16:04](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=964s)** identity based method it is able to infer the brand of that and then it can check whether that uh intended brand is actually belongs to that particular u organization. So using this identity verification method we can gradually and automatically update that reference set. So reference set will be always current even if attackers move to new targets to impersonate. If there is new business and attackers uh wants to uh impersonate them then this reference set will be automatically updated to catch that. So in this way the detection becomes

**[16:56](https://www.youtube.com/watch?v=BCrJV71EQQQ&t=1016s)** drift eruptive privacy preserving and interpretable. Thank you for listening.
