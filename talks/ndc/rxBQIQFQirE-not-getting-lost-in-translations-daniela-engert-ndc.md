---
id: rxBQIQFQirE
title: "Not getting lost in translations - Daniela Engert - NDC TechTown 2024"
slug: not-getting-lost-in-translations-daniela-engert-ndc
conference: ndc
conference_name: "NDC Conferences"
category: "General software conferences"
edition: "NDC"
year: 2025
speakers: ["Daniela Engert"]
channel: "NDC Conferences"
duration_min: 58
published_at: 2025-01-09T20:00:27Z
video_id: rxBQIQFQirE
url: https://www.youtube.com/watch?v=rxBQIQFQirE
youtube_url: https://www.youtube.com/watch?v=rxBQIQFQirE
tags: ["C++", "Language", "Technique", "Software", "NDC", "Conferences", "2024", "Live", "Fun", "TechTown", "Kongsberg", "Norway", "Daniela Engert"]
topics: []
transcript: false
---

# Not getting lost in translations - Daniela Engert - NDC TechTown 2024

**Daniela Engert**

`NDC Conferences` · `NDC` · `2025` · `58 min`

`#C++` `#Language` `#Technique` `#Software` `#NDC` `#Conferences` `#2024` `#Live` `#Fun` `#TechTown` `#Kongsberg` `#Norway` `#Daniela Engert`

[Watch the recording](https://www.youtube.com/watch?v=rxBQIQFQirE) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC TechTown in Kongsberg, Norway. #ndctechtown #ndcconferences #developer #softwaredeveloper

Attend the next NDC conference near you:

/     @NDC

Follow our Social Media!

Languages are difficult. Foreign languages even more so. This applies not only to people, but also to computers. Nevertheless, we must always try to find the most appropriate formulations that convey our intentions as clearly and comprehensibly as possible, regardless of the language in which we express ourselves.

As software developers, one of our tasks is to ensure intuitive operation - regardless of the language the user (or compiler) understands best. Otherwise, the risk of errors increases and operational safety may no longer be guaranteed.

National language adaptations - possibly dynamically at runtime - appear to be a solved problem area. There are libraries for this. However, if you want to use them together with std::format or std::print, you will realise that none of them allow translation at runtime, because the format strings must be C++ literals! The compiler analyses these during program translation in order to detect errors in the use of formatting instructions and argument types. This is one of the main advantages of std/fmt formatting over the other options, which only detect errors during runtime!

I am currently developing a library for our company's machines that allows error detection at translation time, but still allows dynamic translation into the user's preferred language.

Human languages do not always follow immediately recognisable rules, e.g. when it comes to the correct choice of a linguistic form in connection with statements about several things. The Unicode Standard describes such rules in machine-readable form, which the library uses to provide the correct translation.

For the implementation of the library, it is crucial to convert known idioms from the programming of runtime code into semantically correct equivalent code for execution at translation time. Despite 'constexpr', some code looks unfamiliar at first when it is translated into the language of execution at compile time.

In the course of the presentation we will therefore talk about
- a widely used system for language translation
- existing libraries for this and their APIs or embedding in the build process
- plural rules and their processing
- differences and similarities of code execution at runtime and translation time
- the 'language rules' for translation between the two

Code excerpts from my library serve to illustrate the points mentioned.
