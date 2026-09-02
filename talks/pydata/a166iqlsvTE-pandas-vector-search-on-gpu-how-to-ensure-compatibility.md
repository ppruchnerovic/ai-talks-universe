---
id: a166iqlsvTE
title: "Pandas + Vector Search on GPU: How to Ensure Compatibility"
slug: pandas-vector-search-on-gpu-how-to-ensure-compatibility
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: []
channel: "PyData"
duration_min: 30
published_at: 2026-08-23T07:00:33Z
video_id: a166iqlsvTE
url: https://www.youtube.com/watch?v=a166iqlsvTE
youtube_url: https://www.youtube.com/watch?v=a166iqlsvTE
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science", "Inference, serving & GPU infra", "RAG, retrieval & knowledge"]
transcript: true
---

# Pandas + Vector Search on GPU: How to Ensure Compatibility

**Speaker not identified**

`PyData` · `PyData` · `2026` · `30 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=a166iqlsvTE) · [Conference site](https://pydata.org/)

## Description

Welcome to the PyData & PyCon Yerevan 2026 video collection - our biggest edition yet, held on 24-25 July in Yerevan, Armenia.

From data science and machine learning to Python tooling, production systems, research, and open-source technologies, these recordings capture the ideas, experiences, and practical knowledge shared on stage.

🌐 Website: https://pydata.am

📅 24-25 July 2026 · Yerevan, Armenia

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*2,944 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=a166iqlsvTE&t=5s)** Hello everyone. My name Alexander Boger. I more investment free time it's open source. It's a very hard technology GPU and low latency computing. It's a my like it this dominance. Yeah. Oh my god. Hm. Ah, yeah. Ah, now my like it's this pet project it's a auto stack. It's a eating all free time. But started it's stories. Ah, I more working and consulting it's my friends. Ah, my friends called me and Alex needs this help. I wanted it's a grow it's a money and new target it's a showing this advertising information.

**[0:57](https://www.youtube.com/watch?v=a166iqlsvTE&t=57s)** Ah, and more activities. Ah. Okay, it's not problem. Please this detail it's um this daily ah, people it's a more click impression and show advertising information. This ah, personal it's a generate more ah, activities and sessions. But this sessions it's ah a little bit problem. It's a more options it's a activities it's a very problem separated and needed calculated it's more propagation at and ac- needed it's a relation this content it's a showing.

**[1:46](https://www.youtube.com/watch?v=a166iqlsvTE&t=106s)** What it's a more sessions? This ah, users separated ah authorized users and anonym users. It's a multiply it's it's a phone, home, PC, and another devices. This situation is not easy. It's a browser, it's a mobile app, it's all element generate more sessions. And uh needed it's a segmentate and analysis. Um This is a situation needed it's very easy. It's a needed deduplication. It's a segmentate, look-alike, and uh this needed it's a

**[2:36](https://www.youtube.com/watch?v=a166iqlsvTE&t=156s)** targeting, searching, it's a content for currently group users. This all session uh has its a user ID for finger. Us is a finger bits. Fingerprints building its element is a user agent, hardware parameters, time zone, and all information it's a capturing, it's application, or maybe it's mobile scraping. It's a building in um user agents. And uh naive idea it's a using it's a front of matching fingerprint string by

**[3:26](https://www.youtube.com/watch?v=a166iqlsvTE&t=206s)** string. It's a very bad idea. It's a problem. It's a one fleet bit. It's a two string not matching. Uh idea it's a 10 years ago it's a good it's a particle matching it's a fuzzing it's a compatibility it's a substring. It's a substring and substring and fuzzing this so maybe. But now needed it's a new idea. This new idea it's a using this vector search. This vector search pre-exist step it's a using this needed it's a transform it's abstraction it's a very good working in in multiple dimensional space. Uh needed it's a get fingerprint put

**[4:17](https://www.youtube.com/watch?v=a166iqlsvTE&t=257s)** encoded model and get this fingerprint vectors. Fingerprint vectors. Vectors it's a array it's a format it's a Yeah. Yeah. Okay. Uh it's a is a 256 of array int. Uh what is needed? Uh this array needed it's a Uh needed it's a this compa- compapability array to array. Uh basic idea it's using a cosine distance. Cosine distance it's a brute force algorithm it's a

**[5:06](https://www.youtube.com/watch?v=a166iqlsvTE&t=306s)** has it's a problem it's a still bound and full match 1 million element it's not realistic. It's a needed it's 1 million needed processing it's laptop. This task it's needed it's a make it a strategy it's a fingerprint 3 millions in cosine distance now it's not real. Needed another approach. Another approach it's NNN. NNN is a approximate nearest neighbor. It's a abstraction it's a implemented it's a graph and groups on uh on I'm sorry. I will repeat it.

**[5:54](https://www.youtube.com/watch?v=a166iqlsvTE&t=354s)** It's It's implemented this cluster and graph on groups and needed it's a searching it's a fast jumping fast jumping for element itself look up it's a parse parse to byte to byte and very fast look up this needed groups and and find this uh um similar elements. um graphs abstractions it's very very fast. In CPU it's a very good parallelism. uh

**[6:42](https://www.youtube.com/watch?v=a166iqlsvTE&t=402s)** But this CPU it's a uh absolutely using this abstraction for parallelism. This abstraction and then it's a very good working in GPU. It's a GPU it's a parallel only. It's only idea it's a parallel only. um And not problem it's still bound it's a problem it's a close it's using GPU. Okay. I'm deep dive to GPU a little bit not more. This uh CPU and RAM it's

**[7:28](https://www.youtube.com/watch?v=a166iqlsvTE&t=448s)** to both is a host. This GPU and VRAM is a device. Device and host connected in using this PCI bus. PCI bus it's a very good connector for batch processing. Don't like it's a small data transfer. Needed it's a batching. It's a more batch information transfer. It's very good. This a little bit now it's API like it. It's a I think I synchronize batching, but now it's a classical batching. It's a good work. Okay. Okay. It started make it this bridge. Uh

**[8:17](https://www.youtube.com/watch?v=a166iqlsvTE&t=497s)** Pandas data frame uh it's Pandas other two 2. Uh 2.2.0, it's using more uh backends. Uh default backends it's a NumPy. It's a before it's a two .2.0 version Pandas, now it's a default it's a the arrow. Arrow it's a very good up- abstraction in memory. What is it? Uh classical NumPy it's uh using this abstraction. It's a Python object. It's a using it's a element

**[9:06](https://www.youtube.com/watch?v=a166iqlsvTE&t=546s)** Okay, large element in NumPy NumPy array. But, it's a one row, it's a one NumPy array. It's a needed it's a new look up in a a row. Needed it's a change. It's a not fast. It's a look up in It's a needed it's a unpacking. It's a seize this information and new new the new result. Arrow, it's a seize this situation. It's a making another It's a all data in data frame. It's a mapping in native memory. This not problem. It's look up row by row. It's a native using this memory. The

**[9:55](https://www.youtube.com/watch?v=a166iqlsvTE&t=595s)** approach it's a interesting side effect. It's a This is zero copy. It's a native memory. It's very very easy and re-using. It's not problem. It's a zero copy for another device. Not it's a pandas or Python linear. No, no, all using it's arrow. It's a unified memory. Not unified abstraction memory, but it's abstraction memory for unified. Arrow It's a backdoor. It's a zero copy to GPU. This classic This classic collect needed it's a copy host to device.

**[10:44](https://www.youtube.com/watch?v=a166iqlsvTE&t=644s)** Make it and loading data in arrow. Needed it's a building N N index. Next step is the search in a and needed download information for host. Two moment it's a very large task takes on this all solutions. Okay. This problem now it's not fixed. It need needed it's a research. Okay. Needed it's analysis. It's a more classical N N algorithms. It's a very good working in the server sites. Server sites it's best of the best working.

**[11:32](https://www.youtube.com/watch?v=a166iqlsvTE&t=692s)** Needed its algorithm working only GPU. Karga implemented focus on GPU. This zero start implementation on GPU it's a special algorithm. This uh Karga it's implemented it's using it's a abstraction this graph. It's a very fast implement. It's using all version caching in GPU. This GPU it's a more level caching. It's implemented it's a more uh segmentation and jumping. It's a very fast. And this algorithm it's a easy eating it's a one 10 20 million uh vector. It's not

**[12:21](https://www.youtube.com/watch?v=a166iqlsvTE&t=741s)** problem. Okay. Algorithm exist. Needed them implemented. Pandas is a very extensibility this uh libraries. Uh all algorithm NumPy uh has its a special namespace. All algorithm it's a string. I'm sorry with string. It's living in namespace STR. Data another situation. It's a living it's a special namespace. Needed implemented this new namespace and add the new uh

**[13:07](https://www.youtube.com/watch?v=a166iqlsvTE&t=787s)** method vector search. Okay. It's started. Pandas it's easy. It's not problem. It's a interesting [snorts] moment fun. QDF QDF special libraries uh make it it's a rapid lapse. I a little bit forgot this naming. It's a rapid. This libraries it's implemented all pandas algorithm. It's a and a more another algorithm in GPU. CuPy This libraries implemented all NumPy algorithm in GPU. Okay. This using this decoration it's a register

**[13:56](https://www.youtube.com/watch?v=a166iqlsvTE&t=836s)** new namespace vector for classify class vector accessor. You need it's a take accept this element serials. It's a validate serials it's a vector serials is a vector type of vector. And initialized and initialized index none. Okay. Needed to implement this search. Search it's not super magic but it's clean. Needed it's a building index. First the one initialize index.

**[14:47](https://www.youtube.com/watch?v=a166iqlsvTE&t=887s)** Needed it's a built index. Transformation and loading this data it's accessory it's a loading this data this GPU. And building this index next next then step it's a search and result. This analytics it's a wow it's a more very small work it's a wow it's a working it it's a processing one three million yeah cool it's make it this new strategy it's a needed uh targeted it's a relations content. It's easier. Working day to free. It's interesting moment. It's a guy. It's analytics come back me, Alex. I

**[15:37](https://www.youtube.com/watch?v=a166iqlsvTE&t=937s)** more working in pandas. It's a more transform a data for pandas. It's a Maybe it's small problem may but my laptop it's a little bit warming. It's a little bit warming. It's a kind of of talk. It's a more work. It's a very more format. Mhm. I research this problem. Um and it's a classical pandas approach. It's not problem. It's uh It's uh makes this data frame not problem. It's a another second data frame. It's a little bit mutation. It's It's normal practice. It's under in pandas uh

**[16:25](https://www.youtube.com/watch?v=a166iqlsvTE&t=985s)** like it it's a using this index. It's a pandas element using this index and using another fastly processing. It's uh see this problem. It's uh all operation working in CPU. This index processing in GPU. This problem it's a more retry and rebuilding this index in GPU. Little bit problem maybe but it's a huge problem. This problem needed it's a fixed. Uh fixed uh I like it's a tricks. It's a more tricks. This tricks it's a It's a one line. This needed other than one line. It's

**[17:13](https://www.youtube.com/watch?v=a166iqlsvTE&t=1033s)** uh in one first pandas import and all pandas working in GPU. It's a very hacker cheat. All operation it's a normal working in GPU. Uh not magic, but it's normal practice. It's all algorithm it's not change, but it's working in GPU. Uh what it's work? Uh reading this parquet for fingerprints, it's a loading this the portal the pool automatically. It's a all operation it's a in GPU it's a very fast and comfortable. Maybe, I'm sorry. Uh

**[18:00](https://www.youtube.com/watch?v=a166iqlsvTE&t=1080s)** but then potential maybe it's not hacker cheats, but it's I'm sorry, it's a small one string it's a all algorithm working in GPU. >> [sighs] >> Uh what it's work? Pandas it's a very good using more abstractions. It's a abstractions middle one. It's a catering a call currently method and change implementation to pool on GPU implementation. It's very fast. It's very interesting. And very fastly. This tricks

**[18:49](https://www.youtube.com/watch?v=a166iqlsvTE&t=1129s)** it's a drop to cost. All transformation in GPU it's a very easy transferring to index. It's not problem. It's not problem. It's a rebuilding index. It's a cheap. Not needed it's a transferring more element to host to device it's easy situations. Okay. This full example. This uh code it's not strong but it's needed it's a moment in production ready situations. Uh hacker chips it's one liner it's a

**[19:38](https://www.youtube.com/watch?v=a166iqlsvTE&t=1178s)** transform all operation in GPU. This loading it's a special accessor. And next step it's a reading packet from uh fingerprints and loading metrics and fingerprint uh for advertising metrics. It's a make it it's a one to one and make it this report. Report it's easy it's not interesting but it's needed the show. This analysis report it's a using it's a all teams. All teams. In company it's a but

**[20:25](https://www.youtube.com/watch?v=a166iqlsvTE&t=1225s)** this slide it's interesting moment too. This knowledge deploying it's a catch this information, put it your error flow task and uh started in your cluster. Needed it's a not large GPU. It's a all situation it's a implemented it's a two laptops. Laptops does not have has it's a ultra GPU it's working it's a small GPU. All reports working it's a mm classical laptops not problem it's using. Needed it's a mm Needed it's a tried experiments. I I I am sorry.

**[21:21](https://www.youtube.com/watch?v=a166iqlsvTE&t=1281s)** Oh my god. Um It's a finished by as a back step. It's analytics like it is a solution for GPU on laptop. This analogy is called working in laptops and airflow task. Um Uh this CTO it's a favorite close fast problem close. It's a processing not needed it's a building it's a data center this fixing this problem it's a two guys, two laptops, and small server is good.

**[22:13](https://www.youtube.com/watch?v=a166iqlsvTE&t=1333s)** Pandas it's a very customizable libraries. It's a very comfortable using and not stop it. It's a cool question it's a maybe it's using this Polars. Yes, Polars is good. Yeah but Polars it's a don't like is customize. It's a the span Polars like it this approach it's a embedded database. This close it's a more customized points. Pandas and this it's a like it it's a libraries approach not problem it's customize it's more hooking. I show today it's a one hook. It's a real it's a free hooks, custom

**[23:02](https://www.youtube.com/watch?v=a166iqlsvTE&t=1382s)** map. It's a middle where maybe it's a name space and internal hooks. It's a transform in loader. It's a more more element. It's a automatic custom. Not needed. It's a senior Python developer. No, no, no, no. It's a junior developer. It's not problem. It's a custom contest. Next uh Now future is is here. It's a not using needed using GPU. It's a usually task. It's [clears throat] a typical task in development. Maybe it's analytics. Maybe it's development. It's not problems now. It's using GPU. GPU it's not future now. This is

**[23:50](https://www.youtube.com/watch?v=a166iqlsvTE&t=1430s)** more element against now. It's working and what it's a problem this using GPU. All laptops has its a GPU. Now it's not problem. Next step it's a good F. I'm sorry. It's repeated but it's It's a favorite points. Good F it's a best of the best libraries working in a GPU. It's more algorithm implemented in GPU. It's a fast support in GitHub. It's not problem. And more interesting elements in GPU. It's not Maybe it's a one problem. It's focus one GPU vendors but it's okay. Now it's a best

**[24:39](https://www.youtube.com/watch?v=a166iqlsvTE&t=1479s)** of the best vendors. Okay. Yeah, I'm sorry. Yeah. Uh it's Thank you. >> [applause] >> Questions? >> Uh hello. Thank you for the talk. Uh just maybe start with a quick question. When

**[25:28](https://www.youtube.com/watch?v=a166iqlsvTE&t=1528s)** you're doing host to device data transfer, are you >> Mhm? >> Yeah, roughly. Are you putting this on a specific CUDA stream, like >> CUDA streams yeah? >> Yeah. >> CUDA streams It's a very clever questions. Yeah, I'm sorry. Continue, yeah. >> Yeah, I was just wondering if cuz if you know this trick that if you can put data movement on a separate CUDA stream and have compute on the other CUDA stream, then you're sort of overlapping the the two. Um but I'm wondering if you you can use that here for this vector search case. >> Yeah. It's my question it's a more part. I'm sorry. It's answer it's not small.

**[26:16](https://www.youtube.com/watch?v=a166iqlsvTE&t=1576s)** >> Mhm. >> Um classical uh PCI bus it's uh using this normal working. It's a hardware. It's not software this. It's a hardware. It's a batching load and download. This hardware it's implemented it's a not asynchronous style. This streams in CUDA um abstractions on hardware. And um it's not good working. It's Um, this hardware like it it's batch load and download. This uh classical it's a throughput latency and bandwidth. Needed it's a balancing it's a three elements.

**[27:04](https://www.youtube.com/watch?v=a166iqlsvTE&t=1624s)** The streams it's a maybe it's a five streams it's a potential it's a block it get PCI bus. More algorithm it's a normal working this situation. But it's a uh more algorithm it's a very specific a low latency. It's a normal working it's uh only batch. It's a single um single user not multiple streams it's a emulate a a sync approach on batching. Yes, it's a more algorithm it's a adaptation but it's a not all algorithmics. Yeah. Maybe it's a close your answer. Maybe it's I will

**[27:54](https://www.youtube.com/watch?v=a166iqlsvTE&t=1674s)** restructure it no problem. >> Uh hi. So, how does moving uh basically data to be resident in GPU affected your latency and throughput? >> Um ple- please repeat it's um it's a little bit high your voice. I'm sorry. Yeah. Yeah. Yeah. >> Uh Uh I wanted to know how does moving your data to GPU to be resident or to be fully in the GPU affected your throughput and latency of your whole

**[28:42](https://www.youtube.com/watch?v=a166iqlsvTE&t=1722s)** analysis? >> Ah, all. Yeah. I understand. Yeah. I'm sorry. Yeah. Um I started it's on CPU stores. Uh Remember this brute force algorithms. This brute force it's this stop at normal working in CPU. It's 1 million. This uh A moment, yeah. This it's uh um bandwidth this PCI bus. But it's not real This more algorithm it's not a real loading this data in moment. What What

**[29:31](https://www.youtube.com/watch?v=a166iqlsvTE&t=1771s)** is the problem? Bus it's okay. It's supported. Needed this GPU it's more processing. It's very very fast, but this memory it's a laptops. Maybe it's uh 10 GB, okay. It's using. This multiple using it's this shows this desktop. It's a using this GPU. It's a using this algorithm. It may be it's 10. Needed it's not close. Not again situation in CPU. It's a brute force. Needed it's a balance. It's a load in particle. Okay? Yeah. Thank you. Thank you.
