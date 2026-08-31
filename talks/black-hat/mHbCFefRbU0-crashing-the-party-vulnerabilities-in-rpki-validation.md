---
id: mHbCFefRbU0
title: "Crashing the Party: Vulnerabilities in RPKI Validation"
slug: crashing-the-party-vulnerabilities-in-rpki-validation
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 28
published_at: 2025-01-30T18:19:28Z
video_id: mHbCFefRbU0
youtube_url: https://www.youtube.com/watch?v=mHbCFefRbU0
tags: []
transcript: false
---

# Crashing the Party: Vulnerabilities in RPKI Validation

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `28 min`

[Watch the recording](https://www.youtube.com/watch?v=mHbCFefRbU0) · [Conference site](https://www.blackhat.com/)

## Description

The Internet routing protocol BGP is vulnerable to routing attacks, like prefix hijacks. The vulnerability of BGP enables a range of attacks, from stealing TLS certificates to crypto-stealing or DoS. RPKI prevents BGP hijacks through cryptographic attestations, which routers can use to detect if a given BGP origin claim is authorized. Over half of all Internet resources are already protected with RPKI. This protection rests on a software component that networks install to interact with the RPKI called a Relying Party (RP) client. RPs download information from RPKI servers, validate the objects cryptographically and provide routers with compiled RPKI information they use to protect against hijacks.

This talk shows that RPs can be a prime target for hackers attacking supposedly protected systems. We present new critical vulnerabilities in RP clients, allowing a small-scale attacker to disable RPKI validation in over 80% of systems. For each found vulnerability, we show how an attacker could weaponize the flaw to develop exploits that target all globally running RP clients. We show how the most critical flaw we found could be exploited by hackers to silently circumvent RPKI cryptographic security and obtain arbitrary attestations validated in a significant fraction of Internet systems. A hacker could run arbitrary hijacks even on supposedly protected systems if exploited.

We uncovered 18 vulnerabilities, with five CVEs already assigned, including one rated as "critical". The issues we discovered range from a misinterpreted RFC requirement that left 6000 Amazon prefixes vulnerable to hijacks to other critical vulnerabilities that could compromise the security of a large number of Internet systems.

In our presentation, we will give detailed technical insights into how we found all of these problems by developing our own open-source red-team RPKI tool called CURE. CURE combines the functionality of an RPKI repository, i.e. a server to publish, sign, and store RPKI objects, with functionalities of differential fuzzing. We will conclude our presentation with a discussion on how the quick evolution of products from non-production experimental implementations to widely deployed production software, like in the case of RPKI, can outpace software maturity, leading to a large attack surface for hackers. The security community must carefully look at such cases and ensure the speed of improving software security matches deployment speed.

By:
Niklas Vogel  |  PHD Student, Goethe University Frankfurt, ATHENE
Donika Mirdita  |  Security Researcher, Technical University Darmstadt, ATHENE
Haya Schulmann  |  Professor, Goethe University Frankfurt, ATHENE
Michael Waidner  |  Professor, Technical University Darmstadt, Fraunhofer SIT, ATHENE

Full Abstract and Presentation Materials:
