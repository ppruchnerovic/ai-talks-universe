---
id: 7lUPTxNNxM0
title: "Flipping Bits: Your Credentials Are Certainly Mine"
slug: flipping-bits-your-credentials-are-certainly-mine
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 41
published_at: 2025-02-03T18:15:36Z
video_id: 7lUPTxNNxM0
url: https://www.youtube.com/watch?v=7lUPTxNNxM0
youtube_url: https://www.youtube.com/watch?v=7lUPTxNNxM0
tags: []
transcript: false
---

# Flipping Bits: Your Credentials Are Certainly Mine

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `41 min`

[Watch the recording](https://www.youtube.com/watch?v=7lUPTxNNxM0) · [Conference site](https://www.blackhat.com/)

## Description

Did you know that if you change a single bit from 1 to 0 (or vice versa) in the first 'g' of the domain name google.com (which is 01100111 in binary) you will end up with a variety of valid "bitflip" domains like coogle.com, oogle.com, and woogle.com

So what happens if you generate and register a bunch of cheap bitfliped versions of popular cloud / Saas provider domains, point them to your VPS, log all incoming requests and then forget about the whole thing for two years?

Well, you will in fact receive a stiff bill, generate huge log files and eventually run out of disk space. But on the upside, you will also have collected a treasure trove of legit credentials and interesting stuff like valid OAuth refresh tokens, JWT tokens, bearers, cookies, emails, meeting invites with passwords and truckloads of internet scanner noise.

This accidental finding paved the path for the tool 'Certainly' a pioneering offensive / defensive tool. Designed to simplify long term passive credential harvesting and payload deployment of bitflip-typosquatting domains. 'Certainly' will intercept and analyze any incoming requests, employ Wildcard DNS matching and on-the-fly generated SSL certificates for any incoming requests, across various protocols. All with the intention of downgrading security, poisoning dns caches, harvesting credentials, capturing emails, replacing dependencies with custom payloads and bypassing current security protections.

In this session, we will not only revisit and expand on previously published bitflip research from the last decade and reveal its surprising frequency and impact on modern web technology and cloud infrastructure, but also showcase how you too can use 'certainly' in your next red-team engagement and explain the mitigations needed to defend against this kind of non-human generated attacks.

The open source tool "certainly" will be released to the public as a part of the presentation

By: STÖK  |  Hacker / Creative Director,
Joona Hoikkala  |  Head of Security Testing, Visma

Full Abstract Available: https://www.blackhat.com/us-24/briefings/schedule/#flipping-bits-your-credentials-are-certainly-mine-40040
