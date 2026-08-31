---
id: V-L0INGTEOg
title: "Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs"
slug: reverse-engineering-a-viking-voip-phone-protocol-with
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Boris Starkov"]
channel: null
duration_min: 20
published_at: 2026-05-29T14:00:06Z
video_id: V-L0INGTEOg
youtube_url: https://www.youtube.com/watch?v=V-L0INGTEOg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs

**Boris Starkov**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=V-L0INGTEOg) · [Conference site](https://www.ai.engineer/)

## Description

A Viking VoIP phone sat in the ElevenLabs San Francisco office for a year. Three senior engineers and ChatGPT could not get it working. Boris from ElevenLabs cracked the undocumented protocol with Claude Code in a couple of days: brute forced all 676 possible two letter command combinations, found 80 valid ones, then set up a TCP proxy between a Windows virtual machine and the phone to intercept and log what the proprietary Windows XP software was actually sending.

The last piece was a one byte checksum in the persistence command. Claude reverse engineered the formula by running known input output pairs through it, confirmed the pattern in a closed loop, and derived a simple subtraction. Boris describes his own role as being the hands: Claude orchestrated, he physically rebooted the phone and reported how many beeps he heard. The protocol is now open sourced as a Claude Code skill so anyone with a Viking phone can configure it directly without the Windows software. The outcome at AI Engineer Europe: a red phone booth on the third floor where picking up the receiver connects you to a Michael Caine voice agent that quizzes you on British AI history.
