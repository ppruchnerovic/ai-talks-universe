---
id: 9gWjqjHEM8g
title: "To nest, or not to nest? Nested data types in Polars with big data [PyCon DE & PyData 2026]"
slug: to-nest-or-not-to-nest-nested-data-types-in-polars-with-big
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Daniel Finnan"]
channel: "PyData"
duration_min: 26
published_at: 2026-08-04T22:20:10Z
video_id: 9gWjqjHEM8g
url: https://www.youtube.com/watch?v=9gWjqjHEM8g
youtube_url: https://www.youtube.com/watch?v=9gWjqjHEM8g
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# To nest, or not to nest? Nested data types in Polars with big data [PyCon DE & PyData 2026]

**Daniel Finnan**

`PyData` · `PyData` · `2026` · `26 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=9gWjqjHEM8g) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Daniel Finnan explore the critical trade-offs between nested and flat data structures in Polars to optimize your big data pipeline's performance and readability.

Speakers:
Daniel Finnan

Description:
Polars provides nested data types, specifically lists and arrays, to store multiple values per row. While lists allow variable lengths, arrays require fixed lengths. These types are often used to express cardinality explicitly or to maintain a relational structure that avoids repeating observation data across multiple rows.

To evaluate the efficiency of these structures, a benchmark was conducted using simulated limit order book data consisting of 9,000 observations with 5,000 levels of bids and asks. Five different schemas were compared: no nesting (flat), flat arrays, nested arrays, flat lists, and nested lists. The dataset, totaling approximately 43 million rows in the flat format, was stored using the Z-standard compression algorithm.

The results indicate that no nesting is the most efficient approach for both storage and query performance. Flat formats resulted in the lowest storage overhead, whereas nested types increased file sizes and created more pronounced peaks in storage usage. In terms of execution speed, the no-nesting schema performed approximately twice as fast as the nested alternatives. Nested lists showed the worst performance, particularly during sophisticated queries involving filtering and aggregation.

The analysis concludes that while nested types offer a more intuitive relational structure, they introduce significant storage overhead and result in more complex, less readable query syntax. Despite the need for more frequent group-by operations and joins, flat data structures provide superior performance in Polars. For high-performance requirements with large datasets, avoiding nesting is recommended.

⭐️ About PyCon DE:
PyCon DE is the leading conference on open-source Python applications in AI and data science. It brings together industry professionals, researchers, AI and data science practitioners, and software engineering communities, providing a unique platform for collaboration, knowledge sharing, and innovation.

The PyCon DE & PyData 2026 conference delivered an exceptional experience, fostering stronger connections within the Python community while showcasing the latest advancements in artificial intelligence and data science. Attendees enjoyed a diverse and engaging program of talks, workshops, and networking opportunities, further establishing the conference as a premier event for Python, AI, and data science enthusiasts across Germany.

PyCon DE 2027 will take place in Heidelberg from 19 to 23 April 2027.

•  Newsletter: https://2027.pycon.de/newsletter/
•  LinkedIn: https://www.linkedin.com/company/pyconde
•  X: https://www.x.com/pyconde

Links:
• Conference website: http://pycon.de
• Other sessions: https://2026.pycon.de/talks/

The conference was organized by
• Python Softwareverband e.V.: http://pysv.org
• Pioneers Hub gemeinnützige GmbH: http://pioneershub.org
in collaboration with NumFOCUS Inc.: http://numfocus.org

If you enjoyed this session, please like, and subscribe to our channel for more insightful talks and discussions.
Share this video with your network to spread the knowledge!

Hashtags:

Acknowledgements:
Special thanks to all the volunteers and sponsors who made this event possible.

About:
Python Softwareverband e.V.:
PySV is a non-profit that promotes the use and development of Python in Germany through events, education, and advocacy, fostering an open Python community.

Pioneers Hub gemeinnützige GmbH:
is a non-profit fostering innovation in AI and tech by connecting experts and promoting knowledge exchange through events and collaborative initiatives.

NumFOCUS Inc.
supports open-source scientific computing by providing financial and logistical support to key projects like NumPy and Jupyter, promoting sustainable development and collaboration.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

## Transcript

*4,090 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=5s)** Good afternoon. Um, so very happy here to present at PI data my first time. And we're here in Dharmstad in this wonderful building called the Darm Stadium. From what I understand, that's because Dharm Stadium, the chemical element, was discovered here in Dharmstad. And we're here. Actually, I don't know if you've noticed, all the different rooms are different chemical elements. This one is helium. So, I did wonder whether it would be appropriate to do the presentation in a very squeaky voice like this. Moving on. So, my name is Daniel Finnen. I'm uh in the second year of a PhD contract at the leas laboratory at the conservator national aameier in Paris. Uh my thesis is on um decentralized

**[0:53](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=53s)** finance and specifically it's on um centralized and decentralized exchanges and the liquidity flows between them. Um but I'm here today because um I use polers extensively in my data pipeline. Um specifically I tend to um ingest and um create my features using Python and then onto R for my um econometric analysis. So I kind of went down a little rabbit hole last year looking at nested types in polers. So that's why I'm here today talking about that. So what are polers? Uh nested types. So they're vector- like containers um for storing multiple values per row. They have the same uh data type. Um and why would you want to use them? Well, you may think that it's better to structure the relations in your data using nested

**[1:42](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=102s)** types if you're maybe from a relational database background. Um, if you like the idea of expressing the cardality explicitly, you might want to use nested types. And you may find them maybe a little bit more intuitive. Um, maybe it kind of triggers you to see um, observations, several observations uh, with just one variable changing. So very very basic outline of a basic list and I won't dwell on this for too long. Um, if you've used polars, you've seen these data frames before. Um what are the characteristics? Well um a list can be variable length. An array must be a fixed length. It's got the same uh square bracket syntax as Python lists, but these are not Python lists. Um Polers assumes uh list by default unless

**[2:30](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=150s)** you specify it. And the name space is list and um R or array provide access to the methods. So just a little bit of context in terms of the Polers library. And I've got to say I've become a big fan of the Polers library and it's been um rapidly developing over the last few years. Um lists and arrays are a kind of long-standing feature in Polers and um more things have been added to the name spaces to give extra functionality. So for example last year with filter um list aggregate uh array aggregate that was also added last year. Um other expressions such as filter on arrays that's um still in the feature list for the moment. Um, so I wanted to show you a few examples. We're going to look at just some basic examples and I'm going to go on to the benchmarking which I've done. Um, and I wanted a few kind of toy

**[3:18](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=198s)** data sets. So given we're here in Germany, I was kind of thinking, you know, what's appropriate to show Germans and what what are Germans uh known for? So beer, of course, very simple. Um the first beer there actually I think is a beer from uh which is brewed here in in Dharmstad. Um we've got three columns in this uh in this data frame um which are lists uh energy containers and ingredients. Um the source for this uh for these few items is actually from a website which um has a nice uh database of beers. So, if you like beers and maybe you're going to have a beer after this talk, um you might want to check out the different beers on this website. Sebastian runs it. It's called beer universal. So, some basic queries. Uh find all the

**[4:07](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=247s)** wheat beers. Calculate units of alcohol for each container. Determine the percentage of recommended uh calorie intake per container. So, I'm just going to I was going to do this live coding, but um I've got lots to go through. So, we're just going to step through the code um in real time. So you can see the data frame there and it's activating my environment and let's hope that the laptop doesn't die or anything unexpected happens. Okay, so just to show the data frame. Um we'll step through to the first which does contains on the list name space looking for um wheat malt if you like wheat beers. Uh,

**[5:00](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=300s)** how can I do that? I'm not There we go. Okay. Uh, yeah, we're on the wheat beers. So, uh, it didn't show us our first query. Okay. Well, you can see that we can we can pull out the results of the query here if we look in the um debug window, but we'll run through onto units. So calculating uh this is using um two of the columns which contain lists um alcohol containers um we explode that then because we've got some of the

**[5:46](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=346s)** results which are empty just in order to drop those um empty lists and then we um show the data frame at the end. Yeah. And for some reason, I'm not getting the results in my console, which is kind of strange. Yeah, it should still usually show it in the um No, it should be coming in the terminal. >> Ah, there we go. I think I must have pressed it twice. No worries. Okay, now you can see the results. Um, we were on the wheat one. Well, it's picked out should

**[6:36](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=396s)** have picked out I think three uh wheat beers there. The point really isn't kind of the results. The point is just to see a little bit of how the query structure is using the nested types. Um next one on units and uh you can see the calculation there. Um and finally we've got the uh calorie intake. So, um this is based on um recommended calories per day from the German Nutrition Society. Um I don't think you'll be thinking about that later at the bar though. And okay, anyway, the point was just to show you um briefly some queries on a very very basic data frame. Um the next example I

**[7:26](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=446s)** have, well, Germans are also known for their punctuality. So um I thought that we could look at train punctuality. We've got four operators here. Deutschban SNCF so uh France uh SN CB uh Belgian and SBB which is Swiss. So you can see the construction of the data frame there. uh some very very basic statistics uh operating on the array name space mean and standard deviation and uh Deutsche Ban kind of comes in second there in terms of the average train punctuality um just after SNCF and number of months below the EU average of 87% um so we're not using um filter because we haven't got that yet in the array name space we're using uh the evaluation on the elements of the array below 87

**[8:15](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=495s)** and then we count the number of matches in that. Uh you can see that the Belgians and the Swiss they do quite well really. And now looking at the mean across seasons. So we're pulling out um various elements of the array and then calculating an average for each season. And this is just really to show you it kind of starts to get a little bit messy. Um I kind of I don't really like this personally. Um the array name space doesn't have gather yet. But if we switch it into a list, then we can use the gather. We can create another column and we can have the seasons in there and then we can start to gather them from the array and calculate the mean on those elements. So um I'm showing you this because there are a few different kind of design decisions

**[9:03](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=543s)** going on here and maybe um it kind of panics me not to see this sort of data in a panel format really having each observation according to the temporal element. Um and really it depends on your data format. Um but it also leads you down this road where the syntax for your array and list um calculations kind of changes according to how you have it structured and it can kind of result in something that's quite nice and expressive or you can kind of end up in this space where you've got something rather inscrutable these series of methods on name space that look rather convoluted. um also to say that the ability to work across element sorry to work elementwise across columns is kind of crucial to the usefulness of nested types. So now moving on to the kind of main part of this which is to try and

**[9:51](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=591s)** demonstrate how the different nested types perform and the storage implications and I'm going to go on to an example which is kind of drawn from my work um which is using limit order books. So I ingest a large number of limit order books. Um and these are kind of a very basic economic design where you have a number of bids and a number of asks on two sides of the book at different prices and at different quantities. And so my work involves creating features from this and then using those features in order to econ to to e econometrically look at the relationship between different types of exchange. Um I'm not going to use real data. I'm using some data which is simulated from numpy just to make it uh reproducible and I'm going to have the git github available for you so you can take a look at that if you're interested. Um we do a random walk which

**[10:39](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=639s)** uh uses hourly observations over one year. So we're looking at about uh 9,000 observations and uh order book snapshots of 5,000 levels on the bid and the ask. And that's kind of typical for crypto exchanges. and the spread in terms of the the the book as well as the volume and the shape are are randomly generated according to different um um different limits that I've I've created using uh numpy. So the goal is to compare the storage performance and the query structure as I said and in particular looking at five um different schemas uh no nesting um a flat array a nested array a flat list and a nested list. So, just to show you very uh very basic idea with this random walk and um I I simulated these using a bitcoin price

**[11:27](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=687s)** from last week which is around $70,000 but who knows where it'll be next week. I mean it's very very volatile. Um and the orderbook snapshots look like this. So at um each point in time the shape changes, the um spread changes uh and the volume changes. Um, so with your 5,000 levels and around 9,000 observations, um, if you've got it in a flat format with no nesting whatsoever, we're talking about 43 million, um, rows. Um, and this is not massive massive data. So in terms of my simulation, uh, I first of all saved this in in in pickle format and the file is around 1.4 GB. So it's I think it's useful to see um how Polas performs but it's not really massive massive data

**[12:16](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=736s)** that you might be treating um if you're really doing big data stuff. Just to look at the structure. So you can see uh no nesting. We've got both an extra column for uh price on the bids and the ask and the volume or the quantity on the bids and the ask. With the flat array, we've got just two elements in the array indicating price and the quantity. And then the nested array, we have the whole thing nested together uh with the price and the quantity inside a larger array which will be 5,000 long. Same for the for the lists. It's the same principle. And I'm not actually comparing here the variable um size of um lists um that feature. We're just looking as if the lists are um just the same length as the array. So onto the storage. So um I just went

**[13:07](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=787s)** for the default here using the Z standard um compression algorithm which is the default in polers. Um and you can see that no nesting uh wins by far. You're talking about uh this is in in bytes on the um on the y-axis but you're talking about 100 megabytes difference really. And we've got some strange peaks here which I think is really down to the compression algorithm uh rather than polers itself. um zed standard kind of uh sells itself as a good kind of um balance between um compression and performance. So I think there's something going on there um with those peaks that we see. Um and you you also notice that the peaks are much more um pronounced for the uh the nested types. So the queries for this um I'm looking at first of all a very very basic query the mid price and the spread um these

**[13:57](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=837s)** are just acting um on the prices and uh looking at the um maximum bid and the minimum ask and then the difference between the maximum bid and minimum ask then the total Q imbalance. So we're then looking at the total volume and summing that and we're doing a calculation to indicate whether there's buying pressure or selling pressure on one side of the book. And finally we're doing slightly more sophisticated query looking at the depth at a given level. So I've chosen here the depth at 500 on the ask side of the book. So we're looking um we're first of all finding um the minimum ask and then we're going 500 levels up and then we're summing the volume within that interval. And just to kind of demonstrate the query structure to you, I've I did actually have this in um in graph format

**[14:46](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=886s)** which is quite nice to look at but in presentation they kind of get a little bit unwieldy. So I've kind of bastardized the syntax here so you can get an idea of how the queries are constructed. Um you can see the nested um nested versions we go from a select into an aggregation on the array and then a further get on the um the nested array. Uh for the flat list, we're doing a group by and an aggregation and then a get on the uh the array. And for no nesting, we're simply doing a group by and an aggregation. Um the structure is pretty much the same for a list and array except we're just changing the name space. So for the Q imbalance, uh we're doing a select array aggregation, then array get uh and then further with columns. uh flat list, flat array, group by aggregation, then um a get on the

**[15:36](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=936s)** array and a select um no nesting, select by aggregation. So you get the idea. And the most sophisticated one, we've got several things going on. Uh with columns, uh array aggregation, array get, with columns, explode, filter. You get the idea. You see the the differing uh levels of complexity in the queries with no nesting. uh we simply go by group by aggregation with columns join um filter and the join might possibly be expensive. That was kind of my thinking to begin with. So um performance what does it give? Does anybody have any ideas? Does anybody no nesting wins by how much? Not quite. So um this is run just on this laptop. uh 100 repetitions, taking

**[16:27](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=987s)** the minimum value of those repetitions. Nesting, sorry, no nesting does indeed win. Um it's about two times better. Um nested list, nested array, uh much worse. Uh what's kind of curious is on the most uh sophisticated uh query, which is I mean not a crazy calculation really, um we've got considerably bad performance on the nested list. Um so what's the conclusion? Um nested types add storage overhead. The query structure can become rather inscrutable. Um not nesting has much better performance despite needing to use both group buys and joins. Um and so really are the gains in the kind of relational

**[17:14](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1034s)** structure. If you're um a relational database person and you really like this idea of using the nested lists um is it really worth it? Um and would any further development really make any difference? And I can't really answer that question. I'm not really I'm not uh a Polar's um core developer. Um but I really liked the lists and the the arrays when I first discovered them. It kind of solved that um little bit of a niggle that I had in seeing um the same observations over and over again with just one value changing. And you know, in comparison to looking at SQL de databases, I kind of thought, yeah, this is maybe this is a nice way of doing it. But um it's obviously not. Um and you just have to get over it, I think. So what's the

**[18:02](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1082s)** what's the what's the alternative? Well, um I played also a little bit with um uh UDFs. um number works works well um vectorzing it. Um there's also a great presentation I think at the last PI data by uh Mario Guerrelli where he um he actually live coded a Rusk Rust uh plugin which I wouldn't have attempted but um you know good on him and I think that would offer also um an increased like performance gain. So, um, yeah, there you have it. Um, the results of a little rabbit hole that I went down and, um, would be happy to answer any questions that you have. Thanks for your attention. [applause] >> Thank you, Daniel, for the deep dive in

**[18:51](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1131s)** nesting. Um, yeah, we have for now, uh, one question. Uh, how is the performance with strcts? with struts. I didn't play with that although I did play with that using userdefined functions. It's kind of the the best way of passing stuff into the userdefined functions. Um so I can't answer that. I can't answer that in any comprehensive way. >> Um yeah, maybe someone has question from the audience. Yeah, [clears throat] >> sorry. Maybe just one quick note for like a use case outside of polars that I know of is Spark because Spark ML

**[19:40](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1180s)** actually kind of wants you to use this format as an input for model training or output. So I don't know just a quick note. >> So Spark wants you to use the nested types. >> Yeah, the vector transformer function specifically they want you to use like nested list com like kind of like array columns. Yeah. So this is just one single use case that I know of. >> Okay. >> Okay. We have a new question. Uh would the difference in performance be similar in other libraries or pure Python >> uh in terms of the the node library and the R library? Is is that what they >> um I know what what meant uh You mean other libraries aides from

**[20:41](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1241s)** polers? >> Um, >> I'm not sure to be honest and I think it would probably depend on the the library itself. Um I think they're using the pi arrow implementation behind um what they're doing with polars and and they're writing it in rust. So that all relies on vectors. Um so I think by adding the the nested element then you're purely you're you're simply adding more and more vectors inside vectors. And so I think that's probably what destroys the performance. Um, in terms of how that would perform on the other wrappings for polars in R and in node, I think it would be the same thing. Um, >> anything I think if you're going for performance

**[21:33](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1293s)** with large data, yeah, I think the nesting is going to be a concern. But that's my kind of um that's my quick take. and I haven't done any benchmarking on any other libraries. So, um yeah, you mentioned pispark and um I've not got access to a you know to a pi spark um setup. So, I'm not sure is to to be honest. Um, have you tried extracting nested data with libraries like gloom before importing it in polars? Um, the intention [clears throat] here really wasn't about the problem of nesting. Um, [clears throat] the the data the crypto exchange data which I'm handling um is nested in uh

**[22:24](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1344s)** JSON. Um, but this wasn't really a question about having problems with the the JSON nesting. Um, it's quite simple in Polers to um to specify whether you want to ingest it um just as is or whether you want to create a schema to handle it as a nested list or nested array. So, um but but to answer the question, no, I haven't tried uh tried that. >> All right. Um is it RAM or CPU issue that's so expensive? Did your whole data set fit into RAM or was there uh some streaming from polars involved? >> Uh so these were all done in streaming mode. Um but the data set will will fit into RAM. Um it wasn't bigger than 16 gigs which is the RAM on this machine.

**[23:15](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1395s)** um and also on my home machine which does regularly have problems with um the size of the data. So to avoid that and just to get the the kind of unadulterated um benchmark I I didn't create a data set which was larger than RAM but that would not be too difficult with the simulated data setup that I've got with NumPy. >> So yeah, that could be added as quite a nice extra actually. Right. Thank you. Um, does the flattening of complex data types cost any performance? What is your experience? >> Uh, these are the flattening in terms of the width uh of the the data set. I'm kind of imagining the questions about there. So, this is a very very simple straightforward simulation on quite a

**[24:07](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1447s)** quite a flat data set. the the limit order book doesn't have um a lot of fatness to it. It's um simply two variables um times by two. So yeah, I think that would also be interesting to benchmark to go further on this. >> You're right. Thank you. Um, yeah, we don't have more questions on Talksp on the Um, yeah, but we still have time. Maybe someone has a question. Okay, thanks for your talk. Um what is the performance of converting the two ways

**[24:56](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1496s)** for example from nested lists to no nesting because if you're if like the representation is nicer as a nested list but the performance is better in nesting. Did you look into this? How how long compared to the scales does it take to convert the data frame from one version to the other? >> You mean at the ingestion stage when you're ingesting the data? So let's say you have the data frame as a nested list representation and now before you run your um like your data processing step you flatten um or you explode these nested lists into your no nesting version like how long would that take? >> Uh I think that's a a valid question. I didn't run those as a benchmark. Um, but

**[25:47](https://www.youtube.com/watch?v=9gWjqjHEM8g&t=1547s)** I think you're right. That's that's also a consideration to take in to account for your whole pipeline in terms of taking the raw data and then turning it into a data frame into a parket file. So, no, I didn't run those benchmarks. Um, but they they do take longer. I can't tell you to what magnitude they run longer. Um, yeah. >> Thank you. >> Any more questions? No. All right, that's was it then and thanks again Daniel and warm applause. >> Thank you. [applause]
