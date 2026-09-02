---
id: OlhZGw39AHw
title: "Marco Gorelli - The Polars vs SQL differences nobody is talking about | Pydata London 26"
slug: marco-gorelli-the-polars-vs-sql-differences-nobody-is
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Marco Gorelli"]
channel: "PyData"
duration_min: 20
published_at: 2026-06-15T15:52:36Z
video_id: OlhZGw39AHw
url: https://www.youtube.com/watch?v=OlhZGw39AHw
youtube_url: https://www.youtube.com/watch?v=OlhZGw39AHw
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
topics: ["Classic ML & data science", "Data engineering & MLOps"]
transcript: true
---

# Marco Gorelli - The Polars vs SQL differences nobody is talking about | Pydata London 26

**Marco Gorelli**

`PyData` · `PyData` · `2026` · `20 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=OlhZGw39AHw) · [Conference site](https://pydata.org/)

## Description

Polars is a dataframe library which has taken the world by storm over the last 4-5 years. Because people love benchmarks, people often compare it with SQL-like engines such as DuckDB, PySpark, Daft, and others. But what if, instead of comparing performance, we compared semantics?

This talk will make no mention whatsoever of performance differences. Instead, it will focus entirely on the semantic differences - which don't get nearly enough attention - of Polars vs SQL. Attendees will leave with a heightened appreciation for the differences between the Polars and SQL models, and an understanding of the consequences this has on their code.

Polars is a dataframe library that started gaining significant traction in the data science community around 2022/2023. It is now generally regarded as a safer and more performant alternative to its extremely popular counterpart pandas. As such, it has attracted several performance comparisons with SQL-like engines such as DuckDB, PySpark, Daft, and more. What's typically missing from these comparisons is an explanation of the semantic differences.

For example:
- Why does Polars let me do pl.col('price') - pl.col('price').mean(), but SQL doesn't?
- Why does Polars let me filter using window functions, and how can I get SQL to?
- Are there operations that are more dangerous in Polars than in SQL?
- How do they differ when working with time zones?
- Why did SQL reorder my rows when Polars didn't?

Outline of the talk:
- Motivation: why care about Polars or about SQL?
- Relational model background, row order
- Polars model, how it differs from the relational model, and what this means for you
- Abstracting the Polars and SQL differences away in Narwhals, and advice for non-Narwhals users
- Q&A

This is a technical but accessible talk aimed at data practitioners. Data engineers, data scientists, data analysts, and anyone else working with data will leave the talk with stronger theoretical foundations regarding the Polars and SQL data models. Most importantly, they will learn what this means for them, and what they can do about it.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps

## Transcript

*3,222 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=OlhZGw39AHw&t=1s)** Hi everyone, my name is Marco Gerelli. Super excited to be here at PI Data London 2026. All right, talking about the polars and SQL differences that absolutely nobody is talking about until now, right? Feeling lots of energy in the room, feeling pumped. Nonetheless, I am seeing a few empty seats. So maybe I do need to justify why on earth we should care about polars and SQL and the differences between them. So roughly here's how today is going to work. Going to start with a bit of motivation. Why on earth should we care about polars? Why should we care about SQL? Then once we're feeling motivated and pumped up going to describe some mental models we can use for the two. This is

**[0:49](https://www.youtube.com/watch?v=OlhZGw39AHw&t=49s)** going to be a bit dry and theoretical but don't worry we are then going to go forwards with some concrete examples of underappreciated differences between polers and SQL at least three if there's time maybe a few bonus ones and then we'll talk about abstracting away the differences and I'll leave you yes you all of you with some concrete and simple rules that you can follow to make polers and SQL migrate ations easy and painless for yourselves. Finally, all of my talks end in exactly the same way. That is to say, with some uneven split between engaging Q&A and awkward silence. You're free to contribute to either. You're also free to heckle me during the

**[1:38](https://www.youtube.com/watch?v=OlhZGw39AHw&t=98s)** talk and to ask questions and to make comments. I like it when things get a bit interactive. So, yeah, feel free to um either raise your hand or just shout things out, you know. Let's uh offer we're going to try to offer something that goes beyond just watching a talk on YouTube. All right. So uh yeah, without further ado, what's pol? Polas is a massively popular Python data frame library. Give us a cheer if you're using polars. All right. I it feels like just yesterday when you would ask this question to a room full of people and maybe a couple of people would say that they've heard of it and everyone else would look at you as if you had three heads and say, "Don't you mean pandas?" But it's good to see that the library has been gaining adoption. Fun fact, it actually started as the author's fun little lockdown project and it quickly

**[2:25](https://www.youtube.com/watch?v=OlhZGw39AHw&t=145s)** spiraled out of control and became the data science behemoth that it is today. For common data science tasks, I think it's about as fast as it as it gets. If you want a good generalpurpose dataf frame library in Python, I don't think you can do much uh better than polers. It does have its own API. So there is a bit of a learning curve involved, but I'd argue that it's a lower learning curve than there is with pandas because of how consistent it is and the infinite number of edge cases that you don't have to constantly remind yourself of. But how does it compare with SQL? Right? SQL is a structured query language introduced, will you believe it, over 50 years ago. It's now mostly standardized, although some variations do exist

**[3:14](https://www.youtube.com/watch?v=OlhZGw39AHw&t=194s)** between different engines. And you can find it absolutely everywhere. By everywhere, I mean, every job interview I ever had when I was job hunting, I was asked about SQL. Every company I've worked at, somebody was doing SQL. When I'm doing grocery shopping, I see SQL absolutely everywhere. And when people compare polers and SQL, they're often very quick to make comparisons related to their performance or to their syntax. And I'm here to ask where are the comparisons between their semantics? Where are the comparisons between the mental models? All right, so that's what we're talking about today. How does your mental model need to shift when you're switching between polars and SQL? So let's start with SQL. How do we how do we think about it? When we're

**[4:03](https://www.youtube.com/watch?v=OlhZGw39AHw&t=243s)** interacting with SQL, we're often running queries against tables, which are typically represented as two-dimensional structures where you've got column names, you've got values, you've got rows and columns. This is how they're often represented, but I think it's a bit of an inaccurate repres representation. It makes it look like the rows all appear in a certain order and that's just how they're stored in memory. But in fact a more accurate way to describe it would be as a bag of records where each record contains some information but there is no defined row order. So unless you specifically order your table by some column then the row order is undefined and the engine is often going to just uh take liberties with reordering rows in between your

**[4:53](https://www.youtube.com/watch?v=OlhZGw39AHw&t=293s)** commands for example for some performance optimizations. But even though it may reorder your rows, each row is considered to be atomic. So who comes first, Jod or Jaden, we don't know. But uh you're not all of a sudden going to end up with Jodi Archer who's 18 years old. Like each row is considered indivisible. In polars on the other hand I typically teach it as a collection of columns which we typically call series when we just take out the one-dimensional structure by itself but it's a collection of columns which all have the same length which are all named and within each column there's a the elements are all of a homogeneous data type and here's the

**[5:42](https://www.youtube.com/watch?v=OlhZGw39AHw&t=342s)** big difference with SQL you can operate on each column independently. And if this feels a bit dry and abstract, don't worry. We will make this a bit more concrete soon. I will show you some concrete examples about whatam what exactly this means. But the other big difference with SQL is that actually row order is well defined. Polas doesn't always promise to preserve it, but it is well defined and very often it is preserved. Again, I did say that this would be quite dry, so don't worry. We will see some concrete examples very soon and all of this will make a lot more sense. So let's look at three concrete examples of where things differ. Starting with row order. So

**[6:29](https://www.youtube.com/watch?v=OlhZGw39AHw&t=389s)** in polars if you write select or with columns polers is going to make a new column or modify an existing column but what you don't touch should stay the the same. It should stay in the same order. For example, if we start with a data frame like the one in the top left with columns A and B and values 1 2 3 1 2 1 and then we take a cumulative sum of column A partitioned by the unique values in column B. Then let's take a look at what we get. We get a new column C which contains the values one to four. So I've colored it to make it a little bit easier to pass. We've got the partition corresponding to value one and then the partition corresponding to col to value two. And within each partition

**[7:19](https://www.youtube.com/watch?v=OlhZGw39AHw&t=439s)** we are taking a cumulative sum of the values in column A. All right. So far so good. We just added a new column and we left the other columns exactly as they were. They didn't change order. Didn't didn't change values. They stayed as they are. In SQL, however, there's no guarantees about row order. So when we do the same operation which here we write as sum a over partition by b rows between unbounded preceding and current row. The syntax may feel a a little clunky but you quickly get used to it. We get the same results but not in the same order. we see that we get um the the rows corresponding to the same unique values of column B just clustered together presumably because of some

**[8:07](https://www.youtube.com/watch?v=OlhZGw39AHw&t=487s)** performance optimization that duct DB is doing here. So we do get the same results but um no guarantees of row order. So unless you explicitly put an order by then there's no guarantees about which order the cumulative sum will happen in. And unless you specifically put us an order by outside the query at the end, there's no guarantees about which order the uh results are going to be displayed to you. Right? So in particular, if you're porting between Polers and SQL and you don't specify orders, then much like Ralph Wiggum in the Family Guy and Simpsons crossover episode from 2014, you're going to be in danger. So let's look at underappreciated number two. underappreciated difference number two and that has to do with column independence feels like a

**[8:57](https://www.youtube.com/watch?v=OlhZGw39AHw&t=537s)** abstract idea but let's make it concrete it's actually very easy to pass so polars lets you operate on each column independently SQL on the other hand as we've seen it may reorder its rows but each row is atomic so let's start with a data frame inspired by Frozen the musical in which we've got some characters their voices and their roles. Let's then select columns voice and roll and drop the null values in each of them. We then end up with a with a 2x two table in which look at yeah what's happened. So we've got tenner and supporting but then meds soprano and lead like we got the voice from Anna and the role from Elsa. We got this Frankenstein's monster of a row. What what happened there?

**[9:47](https://www.youtube.com/watch?v=OlhZGw39AHw&t=587s)** And uh yeah, this is just a result of polars letting you operate on each column independently. Polos gives you great power, but with that great power comes great responsibility. And if you're not careful, you can end up in situations that you weren't really anticipating. I do think this is somewhat unusual, but uh very often if you try to do this kind of expression, you might get length mismatches. The worst thing that can happen is if you don't get a length mismatch and it accidentally just gives you a result but it just happens to be meaningless. So the rule of thumb I generally provide when I'm teaching polars is don't use drop nulls by itself. Instead if you're using drop nulls make sure that it's followed by an aggregation or if you want to drop nulls from the entire dataf frame use dataf frame do

**[10:36](https://www.youtube.com/watch?v=OlhZGw39AHw&t=636s)** drop nulls instead. Same consideration for sorting and any other expression which either reorders values or lengthens or shortens an expression. Yeah. All right. Let's talk about underappreciated difference number three. And this one has to do with literal values. So in polars lit one this represents a scalar of length one. It's just a single value. So if you're starting with lit one and write dot sum polers is just going to take that singular value sum it with nothing else because it's the only value that's present and you'll end up with a result of one. But in SQL it's it's a bit

**[11:26](https://www.youtube.com/watch?v=OlhZGw39AHw&t=686s)** different. One means repeat the value one for each row in your data frame. So when you sum that, you actually end up with a total of three. And I feel like this is an underappreciated difference in particular because if I ask Claude to translate the polar code to SQL, uh Claude gets it wrong too. So uh maybe after this talk makes it into Claude's training set, it'll get it correct. But for now, if you're porting Polus to SQL using AI, then make sure to triple check your results. the as a for a rule of thumb here uh don't mix lit with aggregations. You really don't need it when you're doing polars. A literal is just something of length one. So aggregating it isn't going to change the result in in SQL

**[12:17](https://www.youtube.com/watch?v=OlhZGw39AHw&t=737s)** like something like sum lit one. It's the kind of thing people might do to count the number of rows, but you can just do count star like uh no need to mess around with literals. Uh yeah, fork in the road. Uh right, bonus differences. Some some more differences that people aren't talking about because we're we're doing all right for time. Uh and in fact, we might end slightly early, but I think it's nice to leave people with a bit of space for Q&A and uh polite heckles. Let's yeah, let's see if I can handle them. So null sorting. When you sort a data frame by a column, then in polars, the nulls by default go first. This is in contrast with SQL where by default nulls go last. I'm not saying

**[13:05](https://www.youtube.com/watch?v=OlhZGw39AHw&t=785s)** that one is wrong and one is uh right. It's just uh the kind of decision that needs to be made when you design a system. And the defaults are different. This is also something that last time I checked AI models weren't familiar with. You can configure them to be the same. there is like a null's first argument in polars but the default is different so just something to be aware of if you're porting between the two empty sums right this is where I do have an opinion so let's start with the data frame with values one two and null for column A if we then empty the data frame so just by filtering on rows where column A is greater than three then we end up with an empty data frame and if we then select column a dot sum then what happens? Well, Polas tells us that the

**[13:55](https://www.youtube.com/watch?v=OlhZGw39AHw&t=835s)** answer is zero and SQL tells us that it's null. So, Polas is going for the additive identity. It just goes for zero because you can always add zero to to anything and it'll stay the same. Whereas SQL is saying, well, if there's no values, it should be null because zero could well be the result of an aggregation. And uh this is where I feel like polers is more mathematically correct but SQL is more useful. Uh I don't know if that's a controversial opinion in this space. Like if I'm recording sensor measurements or something and my sensor measurements are all broken or something. I I kind of want to get a null rather than a like yeah I kind of want to be alerted that something's gone wrong. I don't know. Do people here have a feeling like who who's on team zero?

**[14:45](https://www.youtube.com/watch?v=OlhZGw39AHw&t=885s)** All right. Oh, yeah. I think you said you did a maths PhD. Yeah. Okay. Doesn't surprise me. He was on team null. All right. Um, not sure what this proves. Just Yeah. API designed by popular response. Uh, okay. Let's talk about broadcasting. That's another fun little difference. So, in Polas, I can select expressions of different lengths. For example, starting with a beautiful data frame like the one above, I can select column A and then I can also select column B dots sum. When I select column B dots sum, I just get a single value of four. And when I select both of them, Polus is going to automatically repeat that value of four for all of the rows in the data frame. This is something that SQL does

**[15:34](https://www.youtube.com/watch?v=OlhZGw39AHw&t=934s)** not let me do. Uh yeah. Anyone know how to fix that SQL query to to get the same result? >> Pardon? >> Partition. >> But yeah, what would you write >> over? Yes. Just over and then empty brackets and then Yeah. You're doing a well not partitioning by anything but sure. Yeah. Uh partitioning by a constant. Sure. Yeah. Exactly. Uh so yeah, this is where I give a point to polars. I feel like for scientific computing, it's just really handy to be able to, I don't know, take a column and subtract its mean and divide it by the standard deviation. You know, the kinds of things we like doing. So, it's really convenient to me that this just happens automatically and you can write things a

**[16:22](https://www.youtube.com/watch?v=OlhZGw39AHw&t=982s)** bit more readably. Uh, yeah. So, let's talk about abstracting away the differences between polers and SQL. And to to do that, I'm going to have to introduce Narwhals to you, which I actually presented here at PI data London 2025. So sorry if anyone's getting this slide again, but nals is a lightweight compatibility layer between data frames and it provides you with a single API with which you can support polers, pandas, pyro, ductb, pispark and others. It's uh widely used across the data science landscape in projects like Alter Bokeh Plotly and more recently scikitlearn. There's zero dependencies stable API and it's fully statically typed. And the question is if Narwhals is supporting both polars and duct DB then how does it

**[17:11](https://www.youtube.com/watch?v=OlhZGw39AHw&t=1031s)** deal with these semantic differences between polers and SQL? How do we deal with that? All right, let's uh take a look. Now introduces certain rules for lazy backends. So first of all length changing expressions such as drop nulls must be followed by an aggregation. So if you try to write select expert.dropnulls dossum, it'll give you an an error. Sorry, it it won't it'll allow you to do that. But if you just put drop nulls by itself, it'll give you an length changing error. You cannot aggregate a scaler. So like this we get away from that problem of uh polars and SQL doing different things but I maintain that in polars aggregating a scaler is always useless anyway so it's

**[17:58](https://www.youtube.com/watch?v=OlhZGw39AHw&t=1078s)** likely a user error and then finally most importantly orderable aggregation orderable expressions always have to have order by specified. So if you want to take a cumulative sum you cannot just take a cumulative sum based on the physical order that rows appear. All right, seeing some enthusiastic nodding from some people in the audience. Nice to see. You must specify the order in which the values should accumulate. And then now we'll also deal with the other differences such as null placement in sorting by default, broadcasting and empty sums. Right? So in uh confusion, what have we talked about today? We've talked about how Polas is a widely used dataf frame library and how SQL is absolutely everywhere.

**[18:46](https://www.youtube.com/watch?v=OlhZGw39AHw&t=1126s)** So if you want uh code that's easy to migrate between them, then we've looked at three concrete steps which you can take to make sure that your code is easily portable. So first of all, avoid expressions which change length or which reorder values unless you follow them by an aggregation. Uh second, don't rely on physical row order. Instead, always make sure to explicitly specify the order in which you want operations to happen with an order by statement. And finally, avoid mixing lit with aggregations. And uh extra finally, I couldn't resist the temptation to plug novels if you want a Python API which deals with these differences for you. Right? I hope this has left you with some useful learnings. Sorry, throat really drying up or

**[19:42](https://www.youtube.com/watch?v=OlhZGw39AHw&t=1182s)** punishing me for plugging narwhals. I'm not really sure what. Uh, so um, yeah, I hope that this this answers your questions about why you should care about polar SQL and the differences between them. Thanks everyone. Happy to take some questions.
