---
id: CJa6YRq-tjU
title: "AI Vector Searchat at Scale - Ewa Szyszka"
slug: ai-vector-searchat-at-scale-ewa-szyszka
conference: wearedevelopers
conference_name: "WeAreDevelopers World Congress"
category: "General software conferences"
edition: "WeAreDevelopers"
year: 2026
speakers: ["Ewa Szyszka"]
channel: "WeAreDevelopers"
duration_min: 11
published_at: 2026-09-02T09:22:09Z
video_id: CJa6YRq-tjU
url: https://www.youtube.com/watch?v=CJa6YRq-tjU
youtube_url: https://www.youtube.com/watch?v=CJa6YRq-tjU
tags: ["conference", "congress", "Europe", "tech", "technology", "IT", "people", "code", "future", "coding", "programming", "programmer", "software", "engineer", "developer", "developing", "WeAreDevs", "WeAreDevelopers", "wearedevelopers", "wearedevs", "wearedeveloperslive", "tech talks"]
topics: []
transcript: true
---

# AI Vector Searchat at Scale - Ewa Szyszka

**Ewa Szyszka**

`WeAreDevelopers World Congress` · `WeAreDevelopers` · `2026` · `11 min`

`#conference` `#congress` `#Europe` `#tech` `#technology` `#IT` `#people` `#code` `#future` `#coding` `#programming` `#programmer` `#software` `#engineer` `#developer` `#developing` `#WeAreDevs` `#WeAreDevelopers` `#wearedevelopers` `#wearedevs` `#wearedeveloperslive` `#tech talks`

[Watch the recording](https://www.youtube.com/watch?v=CJa6YRq-tjU) · [Conference site](https://www.wearedevelopers.com/en)

## Description

Join us for a fascinating chat over coffee with Ewa Szyszka on saving token usage and the power of vector databases at Agent Conf, Berlin. Share your thoughts!

00:00 Introduction
00:39 Token Optimization
01:59 Real-World Application
03:25 Vector Database Insights
05:42 Data Quality Challenges
10:31 Evolving Software Development

-----------------
WeAreDevelopers is the global platform for developers and AI professionals to grow, connect, and lead in the age of AI. Millions of professionals use our year-round platform to build skills, explore thousands of hours of expert content, find career opportunities, and engage with a community that shares knowledge at scale. Companies partner with us to reach developers authentically, strengthening their employer brand, engaging top talent, and showcasing their products to a global network. Our flagship events in Europe, North America, and India bring together the world’s leading engineers, tech leaders, and companies. Together, we are driving the innovations that define the next era of technology.
Head to worldcongress.dev and wearedevelopers.us to secure 10% with the code "wearedevs_yt"
-----------------

## Transcript

*2,073 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=0s)** Hello and welcome to another coffee with developers live at the agent conf in Berlin. I'm here with Eva who gave the second talk today. What did you cover? >> Oh, so I covered today ways that you can save your token usage and cut that nasty bill and not hit rate limits. >> So you talked about optimizing and maximizing your data and minimizing your tokens was the title. How do you do that? >> Exactly. So well, I come as a developer relations engineer from Quadrant. So we think that the approach is to use vector search. So we've conducted multiple experiments to figure out how can we retrieve information more efficiently. So the whole thesis of the talk was that the retrieval part is really important in making sure that you don't burn

**[0:46](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=46s)** through all the tokens. >> So interestingly enough, I'm going to talk in like 25 minutes and I'm going to be talking about how to optimize your code outputs so that other people don't burn too many tokens by reading the content out there. Cuz I mean it fascinates me how the formats that we use these days are just so unoptimized. People are basically throwing five agents at something and wonder when but that battle each other and wonder why the data is so so strong. In terms of vector vector databases, of course, like how does that work? Do you do you install it locally? Do you use a service or what what would you tell people is the easiest way to get started with that? >> I think the first way is to figure out what kind of data are you're dealing with, what's your use case, and also just not shove everything into the context window and take a pause and

**[1:35](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=95s)** figure out, okay, so what data I I'm dealing with, how can I embed it, how can I chunk it before I even store it as vectors so I can very quickly retrieve my most relevant answers. So I'd spent quite a long time figuring out what kind of data sets I'm dealing with and then load it to a vector store and search your most relevant results. >> We do the same actually and we are developers we actually have 4,500 hours of footage every every year of our events. Uh like 4K video footage. So we create like transcripts from them and then we run it through our own vector database to actually make it available for you to search things. So if you want to know about MCP, we give you a playlist of where everybody talked about MCP in each of the talks. And we realized that the

**[2:22](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=142s)** caching in the database was the big winner here as well. But as somebody who came from originally SQL databases, like how do you get your head around a vector database? What's the main difference for you? >> Ooh, okay, this is a really good one. So I would say if you're conducting search at scale, this is where you might run into a bottlenecks. And also you said video data. So I think one big strength of vector databases is that you can have multi-modal data. So you can have anything from audio to video. Um and you can store it very efficiently um at scale. So Quadrant specifically we sit at that like um we like to say when the search gets serious, this is when you should use Quadrant

**[3:10](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=190s)** uh because you can parse it very efficiently through like the HNSW algorithm or recently uh what came out was Turbo Quant which is another very uh fast way to go through uh through the data that you have stored. So I would say that that puts us on the bleeding edge uh among other things and other use cases would be if you're using like IoT devices. So Quadrant Edge is one solution that helps you um in those um environments if you need um to have like a specific data residency, it's very easy to switch it with like um Quadrant Cloud or hybrid solutions too. >> Or Neo4j and all the other vector databases out there that are available as well. >> Sure. >> [laughter] >> I'm just saying, okay. Uh but you said

**[3:58](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=238s)** that you're actually working in this space as a dev rel person. Like uh what what is that like? Like do you come up with the use cases that you showed or did you have some customers information some some case studies that you could show here as well? >> Sure. So, developer relations engineer is a fairly new role, I would say, in the industry. It's just a couple years old. And um it depends on the company how they define it. What I do day-to-day is I come up with ideas of how to build workshops based on uh both customer stories of what um uh different teams are building um and also what people are asking from conferences from client side. Uh so, I get to figure out how does that fit in the ecosystem, what can we build for people so they see themselves in the solutions that we build.

**[4:46](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=286s)** >> Hm. In terms of uh in terms of people uh demos that you showed or things that you talked about, what was the most impressive gain that you've seen so far? >> Hm. I think I'm really looking forward to one demo that's uh being currently built, uh which is multimodal data and parsing specifically audio data. Um so, looking into beyond LLMs, uh I think this is like a sweet spot where people can think of all of that unstructured data uh beyond like the first use cases and first chat GPT-like uh solutions. So, one of the um demos, for example, that was built by my colleague was looking at CCTV cameras and looking for anomaly detection uh for

**[5:35](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=335s)** potential um criminal activity. And I think that just opens the world of possibilities out there. >> But you're not working for Palantir, are you? >> Cannot disclose. >> No, cannot disclose. [laughter] Fair enough. Uh it's an interesting space where people where people don't realize that data comes in so many different formats. And always when I worked when I worked on Microsoft, we always got these demo databases that we showed people and then the workshops and they were like perfectly aligned and perfectly clean. I never had that in real life. I never ever had a database that was not full of errors or very bad very bad data. How do you deal with that those outliers? Like when you when you basically uh is the clean-up process one of the first steps before you put it into the database? >> That's one of them, but um actually Identical Evals, it's a really big

**[6:23](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=383s)** space. So um I would say the process never stops. So once you put something to production, you have to evaluate it and um anything whether that's a tool that's a skill needs to go through the continuous evaluation process. Um today's keynote from Microsoft mentioned that a continuous cycle as well and this is what both we recommend and we do. It's never the end. It's um have we caught those cases or not? So one way to to do it is to have some sort of uh evaluation data sets with sample uh perfect golden answers that you can compare things to as as a starting point. >> It would be interesting to turn that around. I remember when when we talked about talking to the press, we always create a root Q&A with like the most annoying questions that they could ask

**[7:10](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=430s)** us so we can prepare for them. It would be similar to have like a really messed up database as a as a first step. >> Absolutely. I think that's cuz you want to figure that out before you push things to production. >> Cool. Now uh one of the things that in terms of your career, how you ended up where you are right now. You told me before there was a wild thing. You had your startup. You you do you did this like How does How does that compare to like I had my own thing and then I now am now doing devrel for somebody else? Is it Is it more relaxing? Is it less stressful? What What is the career that you would tell people is a better thing to do? >> Well, um so first thing that I did out of college was to try to run a startup uh here in Berlin, actually. Um there was so many things that I haven't learned, but I think it was the best

**[7:57](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=477s)** decision to give it like a legit shot because you learn a lot of things by doing, and that's what I think turned me um into a person who really likes developer relations cuz you have to build in front of people. Um so if you don't know something, you have this uh feeling that like, "Okay, I have to keep up my game. I have to stay very sharp, as sharp as I can." And I would like that environment both in startups um and developer relations. I think that's the like if there's a Venn diagram, this is where the two overlap. It's obviously very different to work on like a series B company and a larger team versus when you're the one in the steering wheel. >> Mhm. Do you think that with the world that we have right now with gigantic software development, it's much easier for you to

**[8:45](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=525s)** start a company cuz I remember the the meetups here in Berlin and when you said that you're technical, it it was like low-cost jumping on you. Everybody wanted to have a technical co-founder because they were actually happy to be a founder of a company but didn't know how to do it or didn't even know if it's possible. Do you think nowadays these iterations is much faster that you can actually do it yourself without needing an extra technical co-founder? >> I would say the moat is the technical expertise that is like a domain expertise. So having fluency in a technical like software development domain is fantastic, but then having on top of that another like domain expertise um it really is very powerful cuz with the tools, I don't think anymore it's about the next feature. It's about how fast can I figure out what people want

**[9:36](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=576s)** to be solved. and what's a nice have and you probably want to get as close to okay this is a pressing issue that someone would actually put a dollar sign to to resolve and not a nice have so the main expertise plus technical skills is where strongest founders lie. >> Which is tricky though because now that we say like we you have to do a genetic development you have to do download 50,000 models on your machine every day or you're falling behind how do you get get to become a domain expert when you actually try to be a jack of all trades in the AI world? >> Yeah I think like even people who are at the bleeding edge are asking themselves questions so

**[10:23](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=623s)** you can't like be the know-it-all in a way it it is such a fast evolving environment that you you just don't sleep but learning how to delegate for founders like I think working together with great founders around they just find people who are absolutely obsessed about a certain topic and they bring them on the team. >> Cool now we're coming here in Berlin 2nd of July for the VR Developers World Congress are you going to be part of it are you going to be come around? >> Am I invited? >> Well we can we can sort something out we always need moderators we need people that help us there as well and I mean in general I guess we can get you in will be fun to have you on the show as well 15,000 people 600 speakers so we can try something there.

**[11:10](https://www.youtube.com/watch?v=CJa6YRq-tjU&t=670s)** Cool. >> Thank you so much. >> Thank you very much bye-bye. >> Bye.
