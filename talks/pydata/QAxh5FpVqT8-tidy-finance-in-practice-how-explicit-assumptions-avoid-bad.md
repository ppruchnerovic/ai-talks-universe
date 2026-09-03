---
id: QAxh5FpVqT8
title: "Tidy Finance in Practice: How Explicit Assumptions Avoid Bad Investment Strategies"
slug: tidy-finance-in-practice-how-explicit-assumptions-avoid-bad
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Christoph Frey"]
channel: null
duration_min: 30
published_at: 2026-08-25T18:20:19Z
video_id: QAxh5FpVqT8
url: https://www.youtube.com/watch?v=QAxh5FpVqT8
youtube_url: https://www.youtube.com/watch?v=QAxh5FpVqT8
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Governance, ethics & regulation", "Science, healthcare & applied ML"]
transcript: true
---

# Tidy Finance in Practice: How Explicit Assumptions Avoid Bad Investment Strategies

**Christoph Frey**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=QAxh5FpVqT8) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Christoph Frey explain how to use Tidy Finance principles in Python to uncover hidden assumptions and avoid the pitfalls of misleading investment backtests.

Speakers:
Christoph Frey

Description:
Investment strategies often suffer from misleading performance metrics due to implicit assumptions and data manipulation. A common pitfall is the omission of extreme negative observations or the use of non-linear scaling to mask volatility, which creates an illusion of stability and growth. Furthermore, the "replication crisis" in financial research highlights how opaque code and hidden parameter choices make it difficult to validate results published in high-impact journals.

The Tidy Finance approach addresses these issues by prioritizing explicit assumptions and "tidy" code. Rather than relying on high-level libraries that hide internal calculations, this method implements optimization functions by hand using standard Python packages like SciPy. This transparency allows for the precise definition of inputs, such as the choice between arithmetic and logarithmic means for expected returns ($\mu$) and the application of shrinkage techniques to handle the curse of dimensionality in variance-covariance matrices ($\Sigma$). The approach explicitly models constraints, such as long-only positions (positive weights) and transaction costs, the latter of which is implemented as a quadratic penalty term to account for market impact.

A critical technical takeaway is the prevention of look-ahead bias. By implementing a strict one-step-ahead forecast using a rolling window (e.g., 120 months), the methodology ensures a clear separation between estimation data and evaluation data. Failing to shift the evaluation period by one interval can lead to artificially inflated returns. By focusing on the input side—explicitly defining window lengths, risk aversion ($\gamma$), and trading cost parameters ($\beta$)—investors can avoid overfitting and create more robust, reproducible backtests.

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

*4,762 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=6s)** Hi everybody from my side. I'm very happy to be here. Um I'm not really sure how my talk fits into the general agenda. It's my first PI data conference so newbie. Um I'm a research fellow at Lancaster University and I also work for private investment firm in Hamburg and we look at all kinds of um strategic investment opportunities and investment strategies and uh some of the tools I'd like to present to you are part of my day-to-day life and uh uh I do a lot of uh my analysis in Python. So I just saw to share a little bit of the pitfalls you have when you talk to investors uh that are not so mathematically trained as uh as you are or um yeah so I thought to start with an investment proposal. I

**[0:59](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=59s)** have strategy one for you. You can decide if you like it and I have strategy two for you. Maybe you like that strategy even more. um I give you $100 or $100 euros and you can decide which strategy you want to put your money in and I'm not sure but maybe 99 of percent of us would choose strategy two of course uh if you be invested from the early 2000s to the end uh you would have almost double your money in comparison to strategy one. So you might have some more uh bumps on the on the way there, but of course it looks so much better. Huh. Um that's the first impression. However, when I tell you that strategy 2 and strategy one are very highly correlated

**[1:48](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=108s)** and the only difference between the two is that um from strategy one I deleted the three worst observations and set them to zero and then let the plot uh go ahead and see um that these strategies are very very similar. Yeah, out of those uh 26 years of um returns, only three of those are different and all the other returns, monthly performance numbers are the same. And it's just a graph that makes it hard to see the difference. So what you can do is you can change the y scaling. Instead of an linear scale, you can use a log scale. And you would say, okay, well, they are both uptrending. That's nice. But you can also see that they are now shifting in parallel. So um if you would have

**[2:37](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=157s)** invested in strategy two in I don't know after 2016 uh you would have get the same return as as if you would have invested in strategy one. So both of the strategies are not very diff different in most of the times uh just of course in the extreme times and it makes such a big difference and for our perspective and perception of those two strategy it makes everything different. Yeah. So um it's just three rows of data that changes our whole um yeah impression of of what we are seeing actually and that's a a very common trend in finance and I'm I'm not sure how often you talk to your representative at your bank or how often you look at your scalable

**[3:24](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=204s)** account uh or trade republic account. um numbers can misleading and especially when they are compounding and that's a problem in finance in very general terms and um me and some of my colleagues we not only saw this effects in real life we also saw that in research uh we were trying to replicate some papers published in very good journals journal of finance um very highly a regarded journal a journals and we couldn't replicate the code. So we thought okay let's try to write down our experience and that's how we started a project called tidy finance. It is a website and also a book that you can uh

**[4:15](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=255s)** read. Um and what we are trying to do there is show the reader professional student um the students or also professors how you can reproduce a certain um example data set or um certain strategy and um it is tidy in two ways of course first of all when you use finance data is usually um um structured data but um still we want to have tidy data but we also want to have tidy code. So those two principles we try to um uh to apply on yeah various topics in finance and I'm going to show you today some of the examples that you see when you see back tests what we call

**[5:03](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=303s)** you have a trading strategy idea and you want to test it in the past to see oh is that strategy actually a good idea. Yeah. So we have our website that you can go to with many different chapters and we have uh two books one is an R and then we realized ah many people are doing Python let's do all the analysis analysis that we did in R also in Python so now we have two books and how are our um chapters structured well we combine code results and the theory behind so you see mostly we start with some text some real textbook applica um introduction to in this case a classical portfolio optimization uh problem then we give you some code how you can write

**[5:54](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=354s)** up this formula and then we also give you some uh results so all together all um uh available to use at home so you don't have to um yeah figure it out yourself and um um three of my colleagues or two of my colleagues are at university. So they are using the book to teach master students, bachelor students about um finance and in this connection with uh with explaining the models um um the feedback is uh very nice. So what I want to talk about today is back testing. Back testing is okay you have an idea for I don't know model or trading and you want to apply it to real data and then you Google how can I like build this uh in Python for example

**[6:43](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=403s)** and you find a lot of great um libraries that give you very nice outputs and that do the aggregation of the information very well. Yeah. So you have PI portfolio op that gives you a lot of different um portfolio strategies already implemented that you can apply and see okay what kind of risk do I want to use or can I can I withstand how much draw down is okay for me. Then you have back testing libraries that um yeah do all the calculations in the background. How you get your portfolio weights and how these portfolio weights are translated into actually performance times here. And then you have PyFolio and Quanstat that gives you these nice nice outputs that generate PDF files for

**[7:32](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=452s)** you that you can just yeah summarize the information for you. And um we really like those tools and I use them often. Um but I want to point out that these tools are just one side. Yeah. They take whatever input you gave it and then you they give you a very nice output. Yeah. If the performance looks good or bad that is up to you to decide that but those tools are not really talking about the inputs and that's what I want to talk about. Yeah. what inputs do I use for my back test for my model validation estimation procedure to figure out oh this is actually um realistic or this is not very realistic um and then I looked into the pep 20 and it says explicit is better than implicit

**[8:21](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=501s)** so um what we try or what we are doing and hopefully you cannot find any spot in the book where it's not like that that we put every assumption every parameter set that we use, we put it explicitly in there and usually we also comment on it. Yeah. So you you we try not to hide any parameter choice that might be um that might be impact the total performance at the end. Uh we really try to be explicit about that. Yeah. So and um an example where it's not very explicit is this for example. So you download some kind of library and it tells you okay there's a portfolio optimizer with two inputs mu and s mu is the mean return. So just say um I don't know maybe the arithmetic

**[9:09](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=549s)** mean over the past or it is some kind of factor model. U we call it the capital asset pricing model. It's a very famous one. Um, but what mean do you use? Maybe you can also use the the logarithmic mean or you can decide, do I use all the data from 2000 until now or do I only use the data from 2010 because the 10 years before they weren't really important to us and all these kinds of decisions that you have to do beforehand um um are left to you basically. The same goes with the matrix S. It's a n byn matrix for let's say you have n stocks you're looking at. Uh when you have monthly data for over I don't know five years is I don't know 50

**[9:57](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=597s)** observation points uh a little bit more. Uh but when you look at I don't know 500 stocks um you can still calculate s but in order to calculate the portfolio weights you usually use the inverse of it. So you have this invertability problem. Um this course of dimensionality what the finance people call it. So you do some kind of shrinkage but uh the back testing tools I showed you they're not really talking about shrinkage. So you have to think about that yourself beforehand and with tidy finance we're trying to give you all the good inputs and um some good outputs. Um the next question is okay do I want weights that are just positive? That's the usual case that you do. But when you

**[10:46](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=646s)** work for a big investor that can trade in I don't know derivatives or futures for example where you can also take short positions is that in your optimization where do I put this in? What what is the standard? What's the default setting? I have to look at that. And also what are my transaction costs? Yeah. When I do the back test, every trade you do has a market impact or I mean the assumption of financial market is that there's no assumpt that there's no impact of your single trade on the whole market prices. But of course there are trading algorithms that trying to optimize how much trading costs you use or you produce. So um you really have to be thinking about that in your back test how you model that. You cannot just say okay 1% is all the time. It's just I put into trading. When you

**[11:35](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=695s)** want to buy or sell a Nvidia stock, for example, that's not very costly. But if you want to sell or buy a very like small stock that is not traded very often, the transaction costs are much higher. Another problem is um overfitting. So um you can think about um it yeah training and testing. Yeah. Yeah. And in the test set, you put all the parameter choices in there and you do this big big grid and then uh you don't really control for that in your test set. So you just go through all kinds of windows for example or threshold parameters to that you might use when you estimate your mean or your variance matrix or um yeah and then you just append append append all your

**[12:25](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=745s)** results. So each one is a new trading strategy and then you just use the best one based on a certain criteria. I don't know the out of sample performance or what we use very often is the sharp ratio. That's the return divided by the variance. So um so to say the uh risk adjusted return um and then you plot the best performance. But is that really a good choice? Is this in sample optimization good when you do it out of samp when you do your live traits and uh yeah maybe you have seen examples I've seen tons of example or like what they are saying is I've never seen a bad back test so um we really want to to or I would like you to be aware of that that this is the case for all of us um

**[13:16](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=796s)** right so Um what is tidy finance about? It's about the input side. Yeah, we want to be explicit how you get to a certain mean, how you when you get a data set that is well known, for example, farmer French factory data, how you use that, how you transform that into actual trading strategies. And we want to be explicit about how you do the sorting for example of of for example of your assets that you use in your portfolio. How you determine which one um is a is is a good fit for your risk aversion or there are so many choices and all these choices are different for us. But we just want you to give you one I don't know let's say template maybe so you can see that um the you have to think about this a

**[14:07](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=847s)** lot okay so one example is um um this chapter and I can show you this is uh from the website it's con called constraint optimization and back testing and what we do is well we first load all the packages ages um that we use and you will see that most of them are very standard packages. So we try to program um all the optimization functions by hand and of course that might be not very efficient in terms of computation time and that but for learning purpose that's perfect because you see what is happening and what are the assumption what is the mathematical model and this combination that I think is is unique um in the

**[14:56](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=896s)** space where we operate with this book. So you get the returns you see uh um we use um um farmer French data here. Those are standard industry uh return. And then we give you some more ideas about um yeah what what do we try to optimize and you can see here what we want to do is well we want to minimize the portfolio variance. So the omegas are your portfolio weights and sigma is your variance coariance matrix what I called as before. And we have one assumption here. The weights they sum up to one. Yeah, cannot invest more or less than 100. And um yeah, then we calculate those weights here. And you see uh you get some weights and you see well when you add those up they might be all one but you see one. For example here down

**[15:46](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=946s)** here this is um less than zero. So you might be well I can only go long. So we have to put in some constraints at the later end. Um the first optimization I showed you was uh the minimum variance portfolio. So I just want to minimize my risk. I don't really care about the returns. But you can also yeah make this very famous formula from I don't know 1952 and people are still talking about it or at least we are and all the finance people I talk to talk about it is okay but yeah I want to minimize my variance but I also have some kind of assumption of how much return I want to have. Yeah, I want at least 5% per perom or maybe 15% if I only go on equity um and do that and um

**[16:35](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=995s)** then you can write down a solution how this portfolio would look like and you see what I need here is the sigma inverse. Yeah, I need those uh inverse of the variance coariance matrix. So and then we go into explaining this formula and explaining to you okay what are these inputs and how do we get good estimates for these inputs. Yeah because as you can see here this sigma has no head on it. So it's an theoretical optimal but you have to estimate it from real data and there the tricky part starts. So we give you an overview of the literature of all these um estimation and then we like show you one example how to do it and um we do it in two two ways. We on one side try to like

**[17:28](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1048s)** tackle the estimation problem in the sigma inverse. So how to get a robust estimate that is also valid when the market dynamics change. So you have dynamic market participants and maybe the participants today are AIdriven and much more volume than you had 20 years ago. So the dynamics and how asset prices are built are much different than they were uh yeah in the past. So we want to get this estimation uncertainty that is dynamic and we want also want to look at okay how do we model transaction costs and how do we do that we just use a pen penalty term on that. So the more you trade um the more the trade is penalized. Yeah. Um and we do this through in this case a quadratic function of the weights in t + one and

**[18:18](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1098s)** t+. So that's the the the performance or the weight just after you have seen the return of t+1 but you're still in the position of the period before. So uh you have to be very specific about that too. And then you can rewrite the optimization problem in a in a in a in a transformed way where you have all these stars and there you can see okay this quadratic term it enters um um in here. So, and then you can um uh write it down again and you can see actually um that you get now penalty term here that um uh is somewhat connected to the to a

**[19:08](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1148s)** naive portfolio when I have no information. I have give you a $100 you just put in each asset you put the same fraction for example that would be one one very naive that's why we call it a naive solution and there are papers out there that show that this is a very strong benchmark hard to um beat out of sample and so we derive at those um optimal weights and then we estimate those and uh calculate an um efficient frontier. So, and this goes on and on and on, and I don't want to dive in too deep. Um, but um um going back to my slides, you see uh uh we put some parameters here and what those parameters are, we explain in the in the text. So, the window length for example,

**[19:57](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1197s)** it gives you like I do rolling window estimation. I like in this case for 120 uh months. So, for 10 years, I estimate by parameters. Then I do a one step ahead forecast of the optimal portfolio and then I shift my estimation um period again in one period and do the same thing again. And so I get a what we say pseudo out of sample test for a certain trading strategy. The beta you have just seen that's connected to the trading cost parameter. Yeah. Um the penalty term and gamma is my risk aversion. Yeah. So how much risk I'm willing to take and then we give you this evaluate performance um function where you just get out okay we get out the the raw

**[20:44](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1244s)** returns of my portfolio we calculate the turnover I also get the net return so the return after cost and I put it all in an array yeah and here is the function that you can also see on the website how to compute my uh portfolio your weights and you see we here define this objective function I've just shown you uh with some initial weights and then we give you sum of uh of the constraints that we use yeah equality constraints that you always sum up to one um and then uh we use in this case the sky by minimize function uh with all the um um um um parameters you can see yeah so not just putting in one

**[21:34](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1294s)** line of code says calculate uh efficient portfolio. We give you the whole thing where you can see all inputs and all parameter choices. And then um we calculate the back test and we do this in a very oldfashioned sense. Maybe you would say it's not paralyzable because we go from PE every period. So we do this um out of sample back test one period at a time. So when you read the book you understand at each point in time what is going to happen and um uh we always um define the returns I use and then the next return is the return I use to evaluate my trading strategy and that's why this minus one I have um marked it um just to show you that um uh it is important um

**[22:26](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1346s)** to have a difference between the evaluation data and the estimation data and then you use this returns window to calculate your sigma and your mu and then you calculate your W1. So these are your portfolio weights and then you put it into a performance characteristics to get um to that. So um to go back to the to the beginning there I showed you some performance charts and now I show you some performance charts again. So um and it's about this minus one this very crucial parameter. If you forget about that you might end up with your um with your performance chart that uh uh is the red line but when you do it correctly uh and you have the minus one in there your

**[23:15](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1395s)** actual performance is this blue line and um that's the uh look ahead bias. Yeah, you use past data to come up with your portfolio weights and then you use returns that you have not used to calculate the weights. And the difficulty here is a thing in your mind that the return at a certain day t you only observe it at the end of the day. Yeah. So you don't see it at the start of the day but at the end of the day. So that's why this lag is very important. you cannot use that day to calculate your performance. And when I do the same for the lock scale again because I like to look at back tests on the lock scale, you see that uh the performance

**[24:04](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1444s)** difference now it's much more wider. Yeah. So you really see there's a difference in the actual strategies. Sorry. And um yeah, so it's not as parallel as in the beginning where I just changed three rows of observations. Um but now you can see it um here much more. So um we have this principle of very clear code in the whole book for different chapters. Beta estimation, farmer French replication, option pricing. So just look at it and maybe you can find some nice things. So three things to remember when you have applications be explicit about your assumptions. uh when the assumptions are not in your code, they might be in your head and your head might be here or there or you never know. And when somebody uh um uh

**[24:53](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1493s)** shows you a back test, don't ask about the sharp ratio, ask about the assumptions and the look ahead bias. Thank you. Oh wrong. A real quick reminder, you can ask questions on talks.pyon.de as well as upvote existing questions so they are more likely to be asked. We have already the first question. >> Oh wow. >> Do you think it is scientifically surely possible to outperform a simple world ETF portfolio with optimization? Um

**[25:44](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1544s)** this question is a theoretical question and of course that's not possible but when you look at your ATF positions um um it might be possible to outperform it but um market change dynamically. So I think it's good to think about the Olympic principle. Sometimes uh to be there is the most important thing and what kind of strategy you use is um is not as important. So um as a disclaimer there are trading firm out there that use a lot of AI tools and a lot of market data um prioritary market data to get the edge. Yeah. to get a trading position 51% of the times right and

**[26:33](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1593s)** that's enough for a certain volume um to produce alpha performance um I work at a investment firm my private portfolio is still just the ETF index very simple um but of course um I would not put all eggs in one basket I would of course try to use different asset classes and the examples in our book are just equity data because that's the most available. >> Awesome. Um the next question is who is the target audience of Tidy Finance? >> So we started with there are many papers a couple of years ago about the replication crisis in finance. Um so the first audience was um um academic audience. Yeah. for students who might

**[27:21](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1641s)** not have a big background in programming to make it very easy and accessible for them um to start coding and to understand the models because they get very technical very quickly and finance people have a very unique jargon how they turn name parameters and things. So we wanted um to make it easier for students to see the cool stuff that that we care about. Um but uh in my daily uh workings I see that most of the tools I use for the students I can also use for some of our investors to explain to them what we are actually doing. >> And the next question is can the code your library account for current market conditions world events in the portfolio

**[28:10](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1690s)** um of political or other nature? >> Yeah. So um we are not coming up with a new trading strategy that is better than everything that's out there. We're just showing to you okay those are the standard models that are used by mostly everybody in finance and you can check that with new data yourself if these models are stable robust and if the claims of your banking advisor are really valid in very dynamic um yeah markets. Yeah. Um I'm reading it's a long question. Okay. Um is there a big difference between the R and Python implementation? >> So that's um so we did that three years ago. So we didn't have good LLMs that

**[29:02](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1742s)** help with that. So it was actually done by by hand I would say. Um we have to maintain both repos so to say. Um but we really try to um use as little packages that are um available as possible just for the stuff that is really standard and most of the things where it gets to the detail about the finance implementation of certain things like I don't know when you do a certain uh sorting of stocks um and how you sort them we do that by hand. So this code is logically the same in R and Python. So, and um all the results are the same. So, um yeah, they should be be the same. >> Last question. Um what's the difference?

**[29:51](https://www.youtube.com/watch?v=QAxh5FpVqT8&t=1791s)** I guess it's like for an average person, what's the difference between a robot advisor and optimization from TD Finance? >> There is no difference. We just explain to you what the robot advisor does or what is going on under the hood of the robot advisor. Yeah. So these packages I showed you, they show you the performance of the robot advisor maybe, but we try to make you understand what is actually happening there. Yeah. So um that that's the goal. So yeah, thank you Kristoff. A round of applause. Thank you very much.
