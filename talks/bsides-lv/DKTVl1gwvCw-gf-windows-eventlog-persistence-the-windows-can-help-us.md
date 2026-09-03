---
id: DKTVl1gwvCw
title: "GF - Windows EventLog Persistence? The Windows can help us"
slug: gf-windows-eventlog-persistence-the-windows-can-help-us
conference: bsides-lv
conference_name: "BSides Las Vegas"
category: "Security conferences"
edition: "BSides Las Vegas"
year: 2024
speakers: []
channel: null
duration_min: 32
published_at: 2024-09-04T22:15:14Z
video_id: DKTVl1gwvCw
url: https://www.youtube.com/watch?v=DKTVl1gwvCw
youtube_url: https://www.youtube.com/watch?v=DKTVl1gwvCw
tags: ["WLWZN8"]
topics: ["Security, safety & red teaming"]
transcript: false
---

# GF - Windows EventLog Persistence? The Windows can help us

**Speaker not identified**

`BSides Las Vegas` · `BSides Las Vegas` · `2024` · `32 min`

`#WLWZN8`

[Watch the recording](https://www.youtube.com/watch?v=DKTVl1gwvCw) · [Conference site](https://bsideslv.org/)

## Description

GroundFloor, Tue, Aug 6, 20:00 - Tue, Aug 6, 20:45 CDT

This research aims to show some phases/techniques used during a red team operation even in a Windows environment.

Thinking about how to use a new way to abuse Windows environments, we mapped three methods that could help you in your assessment with a focus on showing bypass and persistence techniques using Windows.

First, this topic aims to show how we can bypass constrained language using run space with some csharp code.

The second method uses the XML file to create malicious files and elevate the privileges to the NT\AUTHORITY user.

And third, this is a particular point where I demonstrate how we can abuse Windows EventLog to maintain undetectable persistence. I created a new event log containing a HEX shellcode stored in raw data to establish communication with C2.

We can make numerous attacks using windows as our ally. Some protection mechanisms were built in, such as "Applocker to block Powershell Script, Privilege Elevation, and Persistence using the event log.".

To end of this talk, we hope the offensive team can use those new tricks and the defense can figure out some detections and mitigations.

People
Fabricio Gimenes
