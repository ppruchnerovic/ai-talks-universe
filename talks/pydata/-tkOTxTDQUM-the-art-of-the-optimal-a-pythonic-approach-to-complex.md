---
id: -tkOTxTDQUM
title: "The Art of the Optimal: A Pythonic Approach to Complex Decision-Making [PyCon DE & PyData 2026]"
slug: the-art-of-the-optimal-a-pythonic-approach-to-complex
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Justine Broihan"]
channel: "PyData"
duration_min: 33
published_at: 2026-08-04T22:21:03Z
video_id: -tkOTxTDQUM
youtube_url: https://www.youtube.com/watch?v=-tkOTxTDQUM
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# The Art of the Optimal: A Pythonic Approach to Complex Decision-Making [PyCon DE & PyData 2026]

**Justine Broihan**

`PyData` · `PyData` · `2026` · `33 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=-tkOTxTDQUM) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Justine Broihan demonstrate how to move beyond basic heuristics and leverage mathematical optimization to solve complex decision-making challenges in Python.

Speakers:
Justine Broihan

Description:
Complex decision-making problems, such as optimizing a car assembly line's paint shop, are often addressed using heuristics or greedy algorithms. In a scenario where vehicles of various types must be painted in alternating base coats (black or white) with minimum color changes, a greedy approach—such as painting cars in one color until a duplicate type appears—often results in sub-optimal outcomes. For example, a greedy algorithm might produce 38 color changes for a specific sequence, whereas the mathematically proven optimal solution for the same constraints is 23.

Mathematical optimization solves this by shifting the focus from defining a sequence of rules to describing the problem space through decision variables and constraints. By formulating the problem algebraically—defining binary variables for color choice and objective functions to minimize changes—users can employ off-the-shelf solvers to guarantee a mathematically proven optimal solution. GAMSpy is a Python library that facilitates this process by providing a syntax close to algebraic notation and interfacing with 36 different solvers.

The integration of machine learning (ML) and optimization allows for the handling of systems without known mathematical equations. By embedding a PyTorch model into GAMSpy, a predicted defect rate from a neural network can be treated as a constraint. For instance, in a curing oven, the conveyor belt speed and heater temperature can be optimized to maximize throughput while keeping the predicted defect rate below 5%. This hybrid approach is applicable to smart energy grids for minimizing coal usage, dynamic pricing for maximizing sales, and neural network verification to identify minimal perturbations that fool a classifier.

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

*4,973 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=5s)** Thanks for this introduction and I hope everyone can hear me. Um I'm going to kick off my talk with a little mental game. So it's a mental exercise for all of you and everyone is participated to or is introduced to participate. Um so what do we see on this picture? This picture um shows arriving cars in an assembly line on a conveyor belt. And in the picture, like in the bottom of the picture, there is a guy that has to decide um how these cars are going to be painted because these cars, they will either be blue, black, white, green, you name it, the color. And based on the color that those cars will be in the final product, they need to get a base coat. And the base coat that's either

**[0:53](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=53s)** white or black. And the guy in the bottom is deciding which to paint in which color. So which one's going to be white and which one is going to be black. Now the game here is you are that person in charge of deciding what car is going to get what color. We're going to make it a little bit more complex. Um so let's assume there is different car types that arrive on this conveyor belt we just saw. Um, and I'm depicting the um the different car types here with different um letters A to F. And um these car types, they arrive in a very specific order. And as they are arriving on the conveyor belt, you cannot change the

**[1:41](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=101s)** order they are arriving. So the thing here is each car needs to be painted with the space code black or white. And each vehicle type A to F arrives exactly twice in this sequence. So there's one A and a second A, one B and a second B. Now one of each type must be white and the other one has to be black. And as I said, you cannot adjust the order. And the key here is that changing the color from white to black and from black to white, that consumes time and resources. So the idea is try to find a coloring sequence that colors each

**[2:29](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=149s)** vehicle type, one black, one white, with the minimum amount of color changes. So how low can you go? If you have like a paper and pen or like a tablet, um you can like take it and try to use two colors to come up with a coloring sequence um that has well the least amount of color changes. Uh you can also do like a dots or and um like dashes notation or just think about it. Just take like a minute to think about how you would go about this. for this sequence >> just for this sequence. So, I'm going to ask you um if you found like what is the minimum number of changes you found? You can just yell it

**[3:17](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=197s)** in. Just yell a number. Two. Anyone that can go lower or that has a higher number? >> Five. Cool. >> Four. >> Four. Okay. So, we see there's different solutions here. Um and we heard the optimal solution which is two. Um I'm going to show it to you. Um so you start a b um bd oh it that actually oh it's not showing. Okay. Sorry. So I'm not going to show the optimal solution to you. Just just not working. Um but let me let let's just assume or let believe me that two is the optimal solution. you can do it with two. Now the second mental game is

**[4:07](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=247s)** how did you how did you get there? Like can you describe what like how you got to this solution? Um so usually what I hear is when I do this with different audiences this mental game um somebody says well I started in the very beginning um and um so I started in the very beginning using one color in this case here using white and I use white as long as I can until the second the second car arrives that has already been painted white and then I'm going to change the color and I keep on doing is with this solution you get to four color changes. Now if somebody tries to do that from the back starting at the back of the sequence with the same same basically

**[4:56](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=296s)** the same way same solution approach you would get to the solution of two. I've also heard very interesting things about let's pick the maximum length of non-changing letters and start from there. That's also a cool approach and all of them lead to a solution. Um, and this solution approach that we were just talking about, this is what we usually in mathematical optimization call a heristic kind of a brute force algorithm. We describe basically on how we get to a solution like different steps you take, right? You start with one color and then sometimes you change or you pick the longest sequence and then you change. Um, and basically what this does, it it's a local search and it does do decisions based on like a local

**[5:47](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=347s)** optimum. You're not looking into the future. You're just making decisions based on where you currently are. And I've been to a lot of companies that all do something like this. Usually they do it in an Excel notebook or it's a Python script where they have kind of a written description on how to get to such a solution. It basically automates manual decision making. Um and this is something we see very often and it's what we love most, right? We can just think about the solution approach, the different steps we need to make and we just put this into a Python script, right? Um, you don't need to follow along all the lines here. I'm just going to, you know, briefly go over

**[6:34](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=394s)** them. But the idea is, you know, you put the sequence of cars in. Um, and in this case here, we have six different car types. And then we're going to like have a function that paints a car, basically tracks our decisions. Um, and in the end, we're going to have an algorithm. We're going to start with a white color. We walk through the sequence of our cars. Um, if we have not yet painted the car in the current color, we're going to paint it in this color. If we have already painted it, we're going to switch to a different color and track that there is a change in color. So that's basically a very greedy brute force algorithm to come to as I said this solution here for color changes. Very cool. The cool thing here is now that I have this implemented in kind of

**[7:25](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=445s)** like a structured way, I can use even larger sequences, right? That on a piece of paper or as a human brain has problems to approach. Um, I can use this for a lot larger sequences. So here we have 18 types of vehicles, not just six. Um, and then with the solution approach, we get to 10 color changes. And we can even make it more complicated, right? Try to approach the real well the real world problem as it is in practice um by saying okay now a vehicle type does not arrive exactly twice in the sequence but at arbitrary times um basically the demand um that we have. So um you can do that as well. So you have again a random sequence. 128

**[8:14](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=494s)** vehicles arrive. Um and we do have a demand for white cars and a demand for black cars. So very cool. You can do some adjustments to the greedy algorithm in your Python script. Um oops. And that leads you to number of changes 38. So 38 changes with our solution approach to get um well all the demand covered with our solution approach. And I bet in this room there is at least a handful of people that have done something like this or exactly like this. Just to give me like an idea of who has done something like this. Give me like a raise of hand. Okay. So there's a bunch of people that can well relate to what I'm doing here. So this is nothing new I'm telling you. Um but

**[9:03](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=543s)** the problem is how do I know if my problem or the solution approach that I chose is actually good. If we recall the start of this discussion we thought about okay so we can start from the front. This gives us four color changes. We can also start from the back gives us two color changes. Maybe for a longer sequence, starting from the front is best. For other sequences, maybe starting from the back is better. Maybe there's a total different algorithm or approach I could use to give me an even better solution. The point I'm trying to make is there [snorts] is thousands of approaches you could come up with to tackle such a problem. And depending on the sequence

**[9:50](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=590s)** and how those cars arrive, one performs outperforms the other. And you never know which one is the best. And in real in the real world, you cannot just brute force and try all approaches. At some point, you have to decide which one to use. And that is somehow problematic. But the good news is here is the art of the optimal. This is where mathematical optimization um can work for you. So the art of the optimal mathematical optimization what is the idea? The idea is that we change our perspective. So in the first part of the talk we focused on as I said defining rules and like steps procedures on how to get to a solution.

**[10:39](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=639s)** So you can voice this to a colleague. You can easily tell who how you got to the solution. And now we change the perspective to basically describing our problem and not the rules but steps that we have to take to actually come to the solution. So we do describe the problem basically saying we do have a decision to make. So we have to decide which car to color in what kind of color and that's going to be our decision variable. And then there's going to be a set of constraints that says each vehicle has to be painted white and black. The cool thing is if you can model something like this in a mathematical optimization model um you [snorts]

**[11:25](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=685s)** define the problem space and once you have the problem space you can use off-the-shelf software that can mathematically solve this problem to prove an optimality for you. So there is no hallucinating or anything about it. It's just the mathematically proven optimal. Now, I'm going to show some math here. Um, you don't need to understand the math. Um, if you want to use it, there's O specialists like operations research specialists or mathematicians that can do the math for you. Um, we do also offer consulting. Um, but I just want to get the idea across what optimization is. So here we do have two sets I and J and a subset I J. Basically what this does it just a way of coding or encoding

**[12:15](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=735s)** the sequence of arriving cars. So I J is basically a tupole one and J or one and A basically says well at position number one um A type A is going to arrive and 2D is going to be well the second position there's a car of um type D arriving and then we have the decision X variable. So X represents the choice of the color if X3 is going to be one. So it's binary it's either one or zero. So if it's one, we say it's going to be black painted and if it is zero, it's going to be white. And this way we can basically decode our sequence. Now we want to find the minimum amount of color changes. So what we do is

**[13:02](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=782s)** basically retract the decision X and the next X. So X at the position one and X at the position two. And if they're not equal, then this is a color change. So it basically um gives us one point in our optimization in our objective function. And then we define that well every vehicle has to be painted black once and once white and x can only take binary values zero or one and that is all we need to do and then this opens up the world of optimization solvers off-the-shelf solver that we interface to um that as I said do guarantee the optimal solution. So if you are able to formulate your decision problem as a mathematical optimization problem, you can use off the shelf solvers and you

**[13:52](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=832s)** know there's no superior solution. So it guarantees you that there's no better solution than the one you are getting within the constraints you defined. And now you need to translate what you've written down on piece of paper like your algebraic model into something that can be processed by solvers and computers. And this is where Gamsspi comes into place. It's a Python library that interfaces uh 36 different solvers. Um and it's basically a wrapper around our execution system. Um the syntax is very close to what you would write on a piece of paper and the only thing you need to do is to say pip install gamspie. to give you an impression of how this would look like. Everything related to your model is living in a container. Um and then you do create the sets. So I

**[14:44](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=884s)** inj um we just talked about those. You say there's the number in the sequence and the card type. Um you have the subset of the sequence decoding. Um and then you have the decision variable. You're going to say this is um over all of the I. So the domain is I. It's a binary decision variable. Um, and it indicates the color. And then, as I said, it's very close to the mathematical formulation. You say the objective function is the sum over all the i's and you square of the x i and the x plus um i + one. And you do this for also the constraints. So you sum over the i j's and the x i's. And then you say, okay, this is going to be equal to one. Now once you've done this um you can

**[15:32](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=932s)** just call this is my paint shop problem. This is the equations I'm going to look at. It's a minimization problem and then you can call paint shop.solve and you can select from a v variety of solvers 36 as I said. Now what we get here if we print the solution is our optimal number two color changes. But we already knew that right? But the great thing is now that we have it we can also make it more complicated and also we know we cannot go lower. So two was all is the is a proven solution. No better solution exists on the planet. Now let's extend this model right not have the arbitrary amount of cars and different car types arrive. Um there's little changes we need to make to our

**[16:20](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=980s)** algorithic model, little changes we need to make to our um implementation. And what we get is an optimal solution of 23 different uh different 23 color changes. And if we recall that with our like start from the beginning approach, we only got 30 or we got 38 changes. So you see it's like there's a real difference in trying to write a solution procedure to get to a solutions or really getting the optimal solution. You can think bigger, right? Um there's a lot of potential to really optimize the decisions you making every day. And the cool thing is this was just an example from like a car assembly line,

**[17:10](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1030s)** but you can use optimization basically everywhere. Everywhere where you have to do complex decision- making is a place where you can really use optimization to improve different KPI measures. So just uh to name some of them logistics right energy sector agriculture portfolio management how to pick a good portfolio. This is all those applications um where mathematical optimization can accelerate. And before we're going to wrap this session up, I want to invite my friend Muhammed to basically give you a sneak peek into what you can do with machine learning and optimization. [applause] All right, I guess the microphone works.

**[17:58](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1078s)** Nice. Thank you, Justine. So Justine already gave the example of paint shop, right? But let's make it a bit more realistic. Whenever you go into one of those car factories, there is this machine like a oven, right? On on each side there is a curing heater and at the low there is a conveyor belt. As you can see, conveyor belt moves the car and curing heater heats the paint so that it sticks. Otherwise it bleeds or it sags down right? Uh and these are two important parameters but uh there is no mathematical equation for this known right. So as a good old Python developer what you do you usually train an ML

**[18:47](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1127s)** model right maybe a linear regressor to find the defect rate right and we want to minimize the defect rate as much as possible so that we don't lose money. [snorts] So normally when people think about machine learning and optimization they think of it like two very different things right and they are not so wrong in the regard in software optimization software in terms of software packages until gamy. So gamy is basically converging uh machine learning with optimization. Normally in machine learning, you have some sort of data, you did some experiments and you train a model on it, maybe a neural network and you make a prediction. But in the world of or you specify basic rules, your

**[19:37](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1177s)** constraints and your objective like what do you want to optimize basically and you make a informed decision. So here is uh an example of a model. It's a very simplified model. So we have two features which is the speed of the conveyor belt and the temperature of the heater. If the conveyor belt is too slow uh or the temperature of the curing heater is not that great then you have more defects right. Uh you already have a lot of experiments in your factory. Okay. Okay. So you load your data and you make predictions with this model. But uh here is how you can turn it into

**[20:30](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1230s)** Oh, can I see the cursor here? Nice. Uh here is how we can embed that uh PyTorch model into Gamspy. Uh we have a we have certain formulations like torch sequential in this example. So we first define our machine settings. We have one batch and two features which are uh the temperature and the speed of the conveyor belt. Uh we did some re labeling. This part is not important and we put some constraints on it. So this means that the conveyor speed belt uh conveyor belt speed can be between 10 and 100 uh m/s and the temperature can be between 150° and 300° just like in a real production uh setting.

**[21:22](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1282s)** And this is all you need to do to turn your uh PyTorch model into games by algebra. You just give it to it and Gamespy generates the mathematical equations for you which is pretty cool. We do a lot of uh magic in the background so that you don't have to uh come up with the mathematical equations and you just put your machine settings and it gives you the predicted defect rate. Right? And let's be a bit more smart about it. Right? Our main constraint is that we don't want too much defect rate. Let's say up to 5% is acceptable. Right? So we have a quality control equation and we put a constraint saying that it cannot

**[22:12](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1332s)** be more than 5%. And we define our objective variable which is the speed of the conveyor belt. So what we are interested in is to optimize the speed of the conveyor belt. so that our defect rate is as low as possible. Uh here uh you define your model. Uh it says smart paint shop model. You get the equations and you want to maximize the target speed. That's your goal. Sorry. Uh since we have a reliearch model uh it's and it's a nonlinear function. It's a non-ontinuous function. uh it becomes an MIP problem which is mixed integer problem

**[23:00](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1380s)** and you solve it and it gives you the best value [snorts] for the conveyor belt speed without exceeding the defect rate of 5%. So in this way you actually combine machine learning and optimization right it's pretty cool uh and beyond pain shop there are lots of use cases for this thing and I think it's very promising not a lot of people are working on it it's my feeling because it might be a potential gamecher for example there are smart energy grids uh like just like in the paint shop model you have a prediction and you have this you have something to optimize for here you predict for the energy output

**[23:48](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1428s)** and you optimize for the uh coal power right for example currently in Germany they are pushing more and more for renewables but renewables are not enough to uh satisfy the whole demand but we don't want to use coal plants too much because it is destroying the environment so we actually want to minimize the uh call usage that we have. That's one case. Or you can use it for dynamic pricing. You usually predict the customer demand based on the previous year's data and what you want to optimize is the price so that you can sell more. Or you can also do neural network verification. Uh this is a very classic example. Probably most of you already know about it. it basically

**[24:37](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1477s)** tries to recognize the number here. Uh but what you can do is that you can train a optimization model to find the minimal perturbation to fool the neural network like how many pixels should I change to make neural network think that it's not a four but it t it's actually a two let's say so there are some fun use cases like this as well. So that's the end of it. Uh this is our booth. You most of you probably have seen us but for those of you who didn't visit our booth yet uh we expect you any time if you have any questions about potential use cases uh we would be happy to help uh L panel answer your questions

**[25:27](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1527s)** and you can contact contact us via our emails or our website. Thank you. >> [applause] >> Thank you very much for your presentation and for the time management was very good. Uh we have some uh questions for you. Uh one of them is how does gams pie uh differs from pyomo? That's a very good question, one that we get very often. So, um, as I said, Gamsspay and Pyomo, they both are Python packages and they both allow you to write your mathematical models in Python. Um, and they are solver

**[26:17](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1577s)** independent. So, they interface the different solvers. The main difference here is first of all the syntax um, which is for GAMS PI much closer to what you would write on a piece of paper. It's super easy readable. Um, and the main difference is probably the performance. So what pi what pyomo does is it just generate the model instance in python. So like it populates your algebraic formulation with the data on python speed. Gamspy is not doing this. Um gamspy kind of generates instructions and then passes them to our C++ implemented back end. We're doing all the heavy lifting um in C++ and then we're only you know passing back the results. Um and this is the main main difference between um gams and gam gams

**[27:04](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1624s)** pie and pyomo. >> Yeah, >> thank you very much. >> Another question is uh gamesspy open source? >> It is open source. Uh it's on GitHub. You can just do you can just go to github.com games/gamespy and you can see the whole source code. But uh the back end that it uses is the game's language itself and its propriety. So uh but it comes with a demo license and you can develop many models uh up to 2500 variables. So it should be fine to play with. But we also have free trial licenses in case you are interested just to play with it as a company and uh if you if you need more time we can extend it as well.

**[27:56](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1676s)** Thank you. Uh are ML plus O solutions still mathematically proven to be the global optimum? >> Yes. For example, uh I can actually share the code for this example, paint shop example and uh the solver uh gives you actually like what's the sol status. I mean for this one it was a global optimum uh but for some problems it might be like local optimum or it might be infeasible etc which is another valuable thing like sometimes let's say you have a problem and you're trying to convince your boss that this is not possible right you actually write your constraints and your objective and it says yeah this is inasible bro you know then you can go to your boss and say

**[28:44](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1724s)** this is mathematically proven that it's you know inasible and you're trying to give me crap for this, you know. [laughter] [snorts] >> Thank you. [laughter and clears throat] >> Thanks. Uh, which torch models operations are supported in gams gams py all of them? How about other backends like jacks? >> Uh, we have a pretty good coverage of pytorch. So we support sequential models. We support like linear layers, convolution rail, convolution layers, uh many activation functions like relu etc. uh but uh we don't really have any support for jack or tensorflow at the moment but if there is a demand we are

**[29:33](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1773s)** willing to work on it. I mean we started with pytorch and scikitlearn. We also support a lot of models from scikitlearn because they are the most popular libraries so to say but if there's a demand for other frameworks yeah we can easily uh translate those as well. >> Thanks. Uh how do the solvers deal with nonlinear equations? >> So how do solvers deal with nonlinear equations? Well that's up to the solver right? um we basically interface the solvers and um as gams pie we are just providing you well as I said the interface to it and then it's up to the solver on on how to how to do how to do that. >> Thanks. Uh what do I do if I am not able to formally write down my objective

**[30:23](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1823s)** function in terms of my variables or parameters and also do not have a model or similar available or maybe do not even know it precisely. Okay, that's a very open question. So, if you don't know what you want to optimize, well, a very easy thing to do is just reach out to us. We're providing consulting services. We can do the math for you. That was an invitation here. Um, but also there's like online courses on optimization or operations research, mathematical optimization on how to formulate this and um yeah or you hire someone that can do it for you. But I mean in many cases it's very obvious right? I mean if you are selling something you probably want to optimize your profit like

**[31:12](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1872s)** >> or minimize your cost while producing that product etc. But of course the real deal is to come up with the mathematical representation rather than finding the objective. >> Yeah. But but maybe also like there's we do offer like a model library with over how many >> hundreds of models. Yeah, >> hundreds of models um that do cover problems from different areas. They're basically all toy models, but they might be a good starting point um based on your industry. They might give you like a good starting point of like extending them or getting to know operations research or mathematical optimization. >> Thanks. And the last question is uh if there are many solutions, how do I know my solution is the best possible one?

**[32:00](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1920s)** >> So if there is many solutions um the solver knows mathematically how how much better it can get. Um so if there is a better solution then the solver would basically tell you okay there's still a gap. I'm I'm this percentage away from like a certain bound that I can get when I violate some of the constraints. Um and the idea of a solver is to close this gap and once the gap is at 0% then you know it's optimal and there is no better solution. Maybe there is different like different solutions that are all optimal. Um but sometimes there's also only just one solution. >> Thank you very much Den. Thank you for your presentation and um now we move on

**[32:49](https://www.youtube.com/watch?v=-tkOTxTDQUM&t=1969s)** to the next. Thank you. >> Thank you. [applause]
