---
id: Buxmr0juFoo
title: "What's Inside: A .NET assembly! (and how does Hot Reload change it?) - David Wengier"
slug: what-s-inside-a-net-assembly-and-how-does-hot-reload-change
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2025
speakers: ["David Wengier"]
channel: "NDC Conferences"
duration_min: 54
published_at: 2025-06-03T09:15:00Z
video_id: Buxmr0juFoo
url: https://www.youtube.com/watch?v=Buxmr0juFoo
youtube_url: https://www.youtube.com/watch?v=Buxmr0juFoo
tags: [".NET", "Programming Languages", "Tools", "Roslyn", "C#", "NDC", "Conferences", "2025", "Live", "Fun", "Melbourne", "Australia", "David Wengier"]
topics: []
transcript: false
---

# What's Inside: A .NET assembly! (and how does Hot Reload change it?) - David Wengier

**David Wengier**

`NDC Conferences` · `NDC` · `2025` · `54 min`

`#.NET` `#Programming Languages` `#Tools` `#Roslyn` `#C#` `#NDC` `#Conferences` `#2025` `#Live` `#Fun` `#Melbourne` `#Australia` `#David Wengier`

[Watch the recording](https://www.youtube.com/watch?v=Buxmr0juFoo) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Melbourne in Melbourne, Australia. #ndcmelbourne #ndcconferences #developer #softwaredeveloper

Attend the next NDC conference near you:

/         @NDC

Follow our Social Media!

We all create .NET assemblies every day, but you might not know what they actually look like inside. I certainly didn't, and in fact deliberately avoided knowing, because I liked C# too much. Turns out, once I was forced to learn for my job, it's actually super interesting, and I think it's very informative to talk about how it works under the hood, why some things don't work, what things might work in future, etc.

At the same time, I'll cover how Hot Reload broadly works, and manages to efficiently change a .NET assembly without actually modifying the DLL file, let alone stopping your application or going through a full build.

This session will be a dive into the details of .NET DLLs, how they work, how Roslyn compiles deltas for them, and how the runtime applies them. All of that wonderful information you've always wanted to know, but were too afraid to ask! You'll learn absolutely nothing about AI, JavaScript, microservices, or anything else your company actually uses, but at least you'll have a better understanding of what's in a .NET DLL, and a better idea of ILSpy is showing you next time you run it.
