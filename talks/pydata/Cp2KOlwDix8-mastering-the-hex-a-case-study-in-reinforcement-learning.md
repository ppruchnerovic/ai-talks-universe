---
id: Cp2KOlwDix8
title: "Mastering the Hex: A Case Study in Reinforcement Learning for Strategy Games"
slug: mastering-the-hex-a-case-study-in-reinforcement-learning
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Simon Hedrich"]
channel: "PyData"
duration_min: 31
published_at: 2026-08-25T18:20:17Z
video_id: Cp2KOlwDix8
url: https://www.youtube.com/watch?v=Cp2KOlwDix8
youtube_url: https://www.youtube.com/watch?v=Cp2KOlwDix8
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Mastering the Hex: A Case Study in Reinforcement Learning for Strategy Games

**Simon Hedrich**

`PyData` · `PyData` · `2026` · `31 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Cp2KOlwDix8) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Simon Hedrich explore the complexities of reinforcement learning as he breaks down the challenges of building a custom AI agent to master the hexagonal strategy game Antiyoy.

Speakers:
Simon Hedrich

Description:
The project addresses the challenge of developing an autonomous AI agent to play a turn-based strategy game on a hexagonal grid. The game involves capturing territory, managing income, upgrading unit strength levels, and constructing buildings like farms and towers to secure borders. The primary technical difficulty lies in the complexity of the game rules and the vast state-action space associated with hexagonal movement and placement.

The approach involves rebuilding the game logic in Python using offset coordinates to represent the hexagonal map as a 2D array. To facilitate machine learning, a Gymnasium environment was implemented to provide the agent with observations, action masks, and rewards. The observation state consists of multiple Boolean channels representing territories, units, buildings, trees, and gravestones, with normalized values for income and money. The output layer manages approximately 4,000 theoretical actions, though typically only 100 are valid per turn. The architecture utilizes a Convolutional Neural Network (CNN) to process the map channels, paired with an actor-critic model to balance action selection and evaluation. Training was monitored using MLflow.

Key takeaways highlight the difficulty of reward shaping and state complexity. The agent was tested using sparse rewards (final win/loss), dense rewards (intermediate gains), and a hybrid approach. While the model showed some success on smaller maps, it struggled on larger maps, occasionally performing worse than random play. Furthermore, training the agent against itself led to infinite loops of indecision, demonstrating that scaling down the environment and carefully tuning reward functions are critical for convergence in complex strategy games.

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

*3,708 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=6s)** What you can see here is AI and I built it. But let me start from the beginning which was about a year ago. There was a weekend which uh where I was really bored and I scrolled through the Google Play Store and found this really nice looking game which uh reminded me of um something like Civilization um if any of you know it. And it has a quite unusual name. It's called anti yoy. I call it antiejoy but um this is only my preference. Now, let me reset this. And I want to show you just how this game works. It has a

**[0:58](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=58s)** really nice campaign. And um um all the games start with such a map and with different players with different colors. Each of the players have uh territories on this hexagonal beehive pattern map. Each tile um gives income and we earn money with this income. For example, to buy some units like this peasant which can in itself um capture new maps. Um the game is turnbased. So let's go to the next turn. the other players um did their turn and now the unit can again move um one turn uh one step. So we can capture even more tiles. There are also

**[1:49](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=109s)** trees. If the trees spread to our territory, the tiles with trees on them um aren't earning anything. So we should um um probably um try to remove the trees if so possible. And um then we come come to the situation that we need to capture enemy territories which we can do by upgrading our units. There are four strength levels of those units which are increasing in price and also um maintenance costs. So let's upgrade this unit. And now we can capture enemy tiles. And the goal of the game is to have all the map for ourself. and um winning. Obviously,

**[2:40](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=160s)** we can also increase our income by plan um building farms on the territory or to um secure our borders, our territory against um weak enemy units. We can also build towers to um protect our territory. Okay, so I hope you get a sense of uh how this game works. the um campaign gets increasingly difficult uh with size and strength of enemies. Um yeah, I played this game for a few weeks and uh then I got um kind of uh frustrated because I had to re uh play um those hard maps over and over again. Uh and I lost most of the times. Um, so I thought why play the game myself when

**[3:33](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=213s)** I could just um try to program a AI to play it for myself. And with this I got also the inspiration um of a YouTube channel. I I can see some of you know the channel Code Bullet which has some interesting videos um in which he trains AI to play different kind of games. they are quite entertaining and I thought if he can do it um why shouldn't I? So I set out to train or to build a game bot myself for the game anti-Joy which is isn't highly explored in this um arena.

**[4:21](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=261s)** Then to get started, I have to get access to the game. I thought about um running an Android simulator and um capturing the screen or something like this, but um this would be much complicated. That's why I looked at a source code which is um gladly open source. Um that's a good part. The bad part is that it's 100% Java. Um, and at Pyon I can admit that I didn't understand anything. Um, but I got at least the icons that were used in the game and also the colors of uh the territories to keep it uh similar to the original game. Okay. Then I set out um to build the

**[5:11](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=311s)** game from the ground up. And the first thing I um um I I saw when um researching those games is that there are different coordinate systems um to represent those hexagonal tiles. Um the first one is uh our cube coordinates. They have three uh variables to represent each tile. And um the benefit of this is that um you can easily calculate all the neighboring ties by um increasing one of the variables and um decreasing another one. But um also you have to store those three uh parameters which is quite a hassle. That's why I looked at um offset coordinates which is much more intuitive to um to think about because it's just

**[6:02](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=362s)** um a 2D um array essentially. There are also many other coordinate systems but they um have all their um downsides. So I stayed with offset. And now for the game itself, we have the map, we have the coordinates, each tile um needs then one entity um and a territory which I limited to max of two players to um keep it kind of simple. Okay. when then we have the map but um this is the core of the game uh but not at least all of it. One of the major um hurdles in implementation of such a game

**[6:51](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=411s)** is are the game rules and um the issue with with those is uh you can't test them with u unit tests or similar testing strategies because uh there are many edge cases which you all have to represent in your tests and when you want to do it um with static testing this would be um much too great of um of work. So to check if my game actually works, I had to implement also a playable game and I use Pygame for this. As you can see, there are also there's still a map um drawn with the coordinates on them. And with this

**[7:41](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=461s)** pygame I could uh test all the all the different scenarios and check for um correct implementation. And trust me I found a lot of errors in my initial game implementation. Um so this is um a really good strategy of doing such uh things. Okay. Now the game is finished. I can play it. But then I had to think um how an agent an ML model um they have to interact some uh how with a game and for this um there's a gymnasium environment available which is um only a template to um for an API an interface um by which

**[8:32](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=512s)** an agent can interact with some situation a game or um other things. This originated from um OPMI which was uh way smaller back then and uh yeah back then they were um they worked on uh balancing a stick on a card. Um so yeah what does this API uh prepare for us? There are three main functions. The first one is observe. By this um the agent asks the environment um how the current state looks and the environment um returns the observation state and an action mask by

**[9:22](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=562s)** which uh it tells the agent which actions of the um possible ones are um are really possible in this current state. Then the agent chooses one of those actions and um gives them by the step function to the environment and the environment acts um this uh this action and um returns the next observation state and um the next um action mask and also a reward to reinforce or um or penalize the agent for a good move or a bad one. Also, there's the reset, but this is self-explanatory. Okay. Now, what does the obs observation

**[10:13](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=613s)** state look like? Um, obviously uh you can't just um render an image and give this to the agent. You have somehow give put this in a format for the agent to um to really use it. And um there the question um is asked what does the model actually see? And first we look at the observations. There we start with our hexagonal map. I um I created a scenario which is quite uh interesting. And first we use our offset coordinates to convert this hexagonal map to our 2D array which is also implemented in the

**[11:03](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=663s)** background. And with this 2D array um we obviously cannot put a pickle function with a tile objects into an um ML model. So we have to somehow separate the information um in a way that is suitable for such a task. And for this I split up the map into multiple channels. Each of the channels um is made of boolean values in a matrix matrix style. And um for example, the um this channel here only represents where on the map a gravestone um exists. And oh, I forgot the gravestone. Um,

**[11:54](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=714s)** if if you can't um if you can't pay the um the units um and and have no money left in your turn, then all the units die and turn into gravestones, which is um not a thing you should do in this game. Um and the gravestone themselves uh convert to trees later on. Yeah, at this point I uh would also apologize to all the people who have a red green color blindness. Um just in last hour I I thought that those colors um aren't that um suited for this um visualization. But anyways, um we have multiple channels and those are all the channels um that

**[12:45](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=765s)** comprise the overall map. The top three are the territories. Um and then for each player there's a channel um for each unit and building. And also um on the bottom there are the um channels for trees or gravestones where they're located. This is not all the information um a agent should get but also the income and the money for each player. And to keep uh the um the format of those channels consistent, I implemented um other channels that represent this income and money. And there I used um I I took the number like

**[13:35](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=815s)** $5 and um normalized them between zero and one so that uh all of the um all of the channels all of the elements in the channels um have the same number. Okay. So we now know what the agent se is. Um and now we have to think about what the um the result of the model is the output. And this model needs to output what action should be taken next. And there we also start with the map. And one of the actions I showed is to um

**[14:25](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=865s)** place a unit, buy a unit and place it on the map. There are those four unit types and the environment has to think about where those units um may be placed on the map and um those are all the tiles. So each of the units uh have a limited number of tiles where they can be placed. The same goes for the buildings. They are the this visualiz visualization is not entirely accurate because um those channels shouldn't be the same but uh I was too lazy to um to change it up for and make it accurate. So there needs to be multiple channels

**[15:16](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=916s)** um to represent each each possibility of placing an entity. Okay. But placement is not the only actions action to be taken. Also we can move a unit and let's focus on this knight. The maximum possible movement is uh four tires which equates to 60 tiles to move to. But those are um this is only in theory possible. The tiles in practice are much more limited. Those are the example tiles for this night. And we take those tiles um with the indices in the spiral pattern and

**[16:07](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=967s)** map it onto a list not only for this um tile but for all the tiles in the um on the whole map because anywhere on the map a unit could um be. And so um this is all there are all the possibilities. Then we keep the same format of the movement and also have the placements um in a list and also at the end turn as an action. And now you can um imagine how this output um would look like if we concatenate all these lists to one long um so that we can use it as an output um

**[16:57](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1017s)** node for the machine learning model. Yeah, when we sum up all the possibilities together, they equate to about 4,000 actions in theory. In practice um they are maximum of around 100 actions per turn. Yeah. So now we looked at how the model gets its input and the output. Also I had to uh test if this implementation worked. Um so I prepared another um UI. This time I um skipped pi game um because u it's too complicated. Um so I just let claude wipe out code a

**[17:49](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1069s)** react app and uh this worked surprisingly well. Okay, now we have all this and we come to the core of the operation the model of course a deep learning model as you can imagine when we have um the input channels um these are well suited for convolutional layers. So this is why the first major part of the model um is a CNN to capture all the all the maps or all the channels which um represent the map and then I used a technique an actor critic model to um well I won't go into much

**[18:43](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1123s)** technical detail detail but um shortly the actor um does the action or learns um what action to take and the critic um learns if this action um of the actor is really a good one. And so they balance each other out um balance each other and um um learn in parallel and um hopefully um give a better result. Then after the models, after the model we also have to look at the reward there are um different methods. The first one is sparse which uh where we only look at the final result. So we let

**[19:33](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1173s)** the model do its thing and if it wins it gets um a reward of one and um if it uh if it loses it gets a penalty of one and this final reward is divided over all the steps it took to um get to the final result. This um has a benefit that it's really clear clean to implement and um and easy, but it's also um not quite um quite precise for the model to learn which um which of those actions resulted um in the win. That's why there's uh sparse um there's dense rewards there. We also look at wins and losses, but we only um account the last step for this

**[20:22](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1222s)** result. And um we al we also have intermediate rewards um for every single action. So for example, if the you um the model takes over an enemy territory, it gets a reward for it and if it loses an territory, it get gets penalized. This helps in fast um early training. Um and uh but the agent may game the game and um optimizes for rewards and not for the the output we desire. That's why I chose um a hybrid approach to mix them up and um get the best of both worlds. But this is um not quite easy to um to

**[21:14](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1274s)** implement. And also you have to really look at um look at how the model reacts to those um those um rewards that you um that you set at the beginning. It's more an art um than a science. So now we come to the training. I um did the training and let it run for I think two weeks and um in the middle of it I I looked at it and did some small adjustments. But after two weeks um I came to the conclusion that it didn't train really well. The green one is the um ML model. The red one is um randomness.

**[22:06](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1326s)** And as you can see um they are undistinguishable and because after um all this work of uh implementation and training I uh had to do some other things and couldn't invest uh that much more time in this project. I had to either give up or um lower my expectation uh a lot. That's why I trained on a much smaller map. And this was the result after a few more days of training. Again, the green one is um the machine learning model and the red one is randomness. And this result was come on, you can do it. Just another term. Yeah. And

**[22:58](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1378s)** it okay, it wins. And this was uh this was this is a representation of um quite consistent um consistent um actions. um that was also um viewable in MLflow which I used to lock all the parameters of the training and because I we are at Pyon I also want to have some Python code on my slides. Um uh with this I want to show that um imple um to implement integrate MLflow in your project is really easy. That's pretty much all you need. just uh import it, set experiments, start a run and lock how much you want.

**[23:49](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1429s)** Okay so in the beginning I hoped that um I master the hex with my superhuman AI, but uh as you saw it's not that exactly. But I um set up another training and just let it rain, let it run for I think a month and I found some really curious um results which I would like to show you. This is um again the green my model and the red is randomness and um as you can see it doesn't stack up um as well as I hoped which is quite peculiar that I made um the agent worse

**[24:42](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1482s)** than randomness. So what I thought is just um just look at what happens when I train my agent against my agent. And um this is what it looks like. And I think you can imagine why the agent uh didn't come to such a successful win. And this loops um for um infinity. So um what I would like you to take away uh from this is um that it's not really quite straightforward to come to an successful model. Um

**[25:31](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1531s)** especially if um it's so complex with such a such a huge map and um either one must to be must to be an expert or um really scale down the operation um and expectation. But um here at Pyon I have all of you and yesterday in the opening session we heard that uh community is um the most important thing about um this process. That's why I invite you um to try yourself to master the hacks and um go on my GitHub and um send me your results or your failures. And with that I want to close. Um and

**[26:19](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1579s)** also want to thank Inovax which uh made it possible uh for me to attend here and um they sponsored my stay. And thanks to you for being such an attentive audience. Thank you Zimon once again for wonderful really interesting uh talk and uh we have a couple of questions. So first of all uh your animations and presentation was really gorgeous with uh uh can you share a little bit more what you used for it? >> Um maybe some of you know the YouTube channel three blue run brown. Um, if you're interested in mathemat

**[27:06](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1626s)** mathematics, um, there those animations look really similar to mine, it's not um, yeah, it's because we use the same engine in the background. Um, his engine is open source. Um, it's called Manm. Um, and it's also Python. Um, so yeah, I just used this um, to create those animations. >> Great. Uh, thank you. So now we know how to do it properly. Uh the next one is your current model seems hardcoded for a two-player game. >> Uh how would you adjust the architecture for arbitrary amount of players? >> Scale it up. Um yeah. Um I think that's really the answer. um

**[27:54](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1674s)** for more players um you can just use even more channels and even more um I think the outputs would stay the same but um yeah the input channels would have to increase by the number of players. >> Good. Uh the next one is um you mentioned that you used the convolutional neural networks and uh the task seems to be like suitable for attention mechanism maybe uh have you tried to experiment maybe with something like attention mechanisms? No, I think as you can see this was um complicated enough and um I I used um um quite small of a model. So um I think attention

**[28:44](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1724s)** mechanism would be um even more complicated on another dimension. >> Okay, thank you. Uh another one thing is have you tried to change the reward for function? So you mentioned one is like for the whole game, one for the steps, one the hybrid. Uh any more experiments that you can share or >> Yeah. Um throughout the training the changing the rewards is 90% of the work and I did a lot of reconfiguring re um resetting the the rewards um adjusting them um depending on how it seems that the agent um is acting. So um this is the main work throughout the training

**[29:33](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1773s)** process um itself. >> Okay, thank you. And uh I think we have One last question here. Uh how long does it take you the overall process you mentioned? So like one month here, one month here. So but in general that's quite difficult to um to say well it was a few weeks of intermedially intermittent work um on the on the game itself and uh the whole testing in the background. I think the training um setup wasn't too hard, maybe two weekends, and the training itself was um um every other day a few minutes looking into the into the progress and adjusting

**[30:23](https://www.youtube.com/watch?v=Cp2KOlwDix8&t=1823s)** accordingly. Okay, so let's once again thank Zimon for his great talk.
