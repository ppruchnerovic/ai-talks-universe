---
id: 66t87eHEzYI
title: "Training My Rival in Java: A Deep Q-Learning AI to Play Azul by Victor Uria Valle"
slug: training-my-rival-in-java-a-deep-q-learning-ai-to-play-azul
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2026
speakers: ["Victor Uria Valle"]
channel: "Devoxx"
duration_min: 17
published_at: 2026-03-30T17:48:30Z
video_id: 66t87eHEzYI
url: https://www.youtube.com/watch?v=66t87eHEzYI
youtube_url: https://www.youtube.com/watch?v=66t87eHEzYI
tags: []
topics: []
transcript: true
---

# Training My Rival in Java: A Deep Q-Learning AI to Play Azul by Victor Uria Valle

**Victor Uria Valle**

`Devoxx` · `Devoxx` · `2026` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=66t87eHEzYI) · [Conference site](https://devoxx.com/)

## Description

#VoxxedDaysCERN26
AI has become part of our everyday lives but we often forget one of its earliest and most fascinating uses: creating an opponent to play games with.

We’ve seen it in chess, Go, and countless video games, where AI opponents follow complex strategies or fixed rule sets. But who says you need PyTorch or TensorFlow to do it? Sometimes, the good old Java is all you need.

In this talk, I’ll share how I built a Deep Q-Network (DQN) in Java to teach an AI to play the board game Azul. I’ll cover environment design, state encoding, reward shaping, and training strategies.

## Transcript

*2,676 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=66t87eHEzYI&t=0s)** So, uh, hello everyone. I I'm Victor. I'm a full stack engineer at at CERN. We don't do this type of AI at CERN. We do more usual stuff, but this is a personal project that I wanted to showcase and it's about a deep Q-learning implementation to learn how to play a relatively complex board game. uh going over the agenda, I'll explain a bit the rules of the game because it's nice to understand what's happening. I'll explain what Q-learning is. Then I will go into deep Q-learning or DQM in short. A bit of neuron network, the DQN agent and the trainer. And finally, I'll do a tiny demo of me playing against the but not a lot.

**[0:50](https://www.youtube.com/watch?v=66t87eHEzYI&t=50s)** Uh very simple. The game has a common board. In the common board, there are some factories. In the factories, there are tiles of different colors. And then there's the central zone which has well more colors and the initial player tile. When a player takes something from a factory, the rest of the things that they don't take going into the central uh part of the board, the implementation because I'm going to show pretty much all the all the code because I think it's useful for someone that wants to do something in DQM would be useful. Well, the implementation of tiles and factories is very easy. Tiles are just an enum of colors and the factory is just a list of tiles. There's not much to much to do there. Now, the player board is just uh let's

**[1:42](https://www.youtube.com/watch?v=66t87eHEzYI&t=102s)** say kind of a pyramid. Once you fill a row with one color, you place that color into the color of the wall. So, if you put in the first row uh one red, then you at some point will put the red in the wall. For example, you can see that in the second row, when you put two blue, you get to put the blue color in the in the wall. And that's the objective of the game. The objective of the game is placing things on the wall to get points. If you put things in the floor line, which is a punishment when you don't have space to put things in the rows, you lose points. So, that's not good. Uh, the implementation of the player board is also pretty simple. Uh you have just a list of the penalties when you

**[2:30](https://www.youtube.com/watch?v=66t87eHEzYI&t=150s)** put things in the floor. Uh the pattern lines that you want to fill, the wall with the colors, uh a floor line that is just well how much have you placed into the uh floor, the current score that you have, and the last uh round score because it's useful for uh utilities when we get to the reward system of our AI. Now on to the valid actions. Uh imagine that you have a factory with uh three green and one orange and you want to place it in the first row. Well, you cannot because you already filled the green in that row. Now, if you try to put it into the second row, then yes, you can take the green and you put two of them in the second row and because you have one extra, you are forced to put it into the floor line. So, you're

**[3:17](https://www.youtube.com/watch?v=66t87eHEzYI&t=197s)** going to be kind of punished by it. Now, if you try to put it on the third row, which is already being started with pink, you cannot because you already started a color. So, you are not allowed to do that. If you try to put it on the fourth one, yes, but then you need a last green square to be able to put it in the wall. And then in the fifth row, you cannot because you already started with red. If you want to lose your game, you can place everything directly into the floor and lose for no reason, but it's legal. And for instance, you can take, for example, because that's the the point of the center board. You can take things from it. And for example, you would take the three pink. So you would put one on

**[4:05](https://www.youtube.com/watch?v=66t87eHEzYI&t=245s)** in the third row to complete it. The two that are spare are put into the floor line. And the initial player line, the initial player tile is put into the floor line directly. Onto the scoring. This may look uh slightly scary, but don't worry, it's pretty simple to understand. When you place a tile, you get one point plus an additional point per each uh adjacent tile. For example, the red one that is in the top left corner scores three points because it has two adjacent tiles in the vertical. the highlighted uh green one in the third row, second column, scores five points because it's three points for the vertical one and two for the horizontal one. When you complete a whole vertical, you get seven points. Two points for a

**[4:52](https://www.youtube.com/watch?v=66t87eHEzYI&t=292s)** complete horizontal and 10 for a complete color. Now onto Q-learning. Q-learning basically relies on what's called a Q table. A Q table is just one column that is the state action and it outputs a value. Now uh the easiest way to understand it in a simple example is imagine that you are this running guy and then you want to get to the flag. You have your state which is where you are. So one, two, five, whatever number and the action for example going right down whatever. For example, if you are in one and then you go to the right, we give a value of one because we are going to reward it because it's going to the uh to the

**[5:40](https://www.youtube.com/watch?v=66t87eHEzYI&t=340s)** finish line. But if you go down, you get punished because you set yourself on fire, and that's not good. If you're, for example, in number five and you try to go up, well, you're not setting up yourself on fire, but you're not advancing to the objective. So, let's just put it something neutral. And when you actually get to the finish line, which would be the action six down, you get a high value because it's the reward of completing your your objective. Now the thing is uh this Q table was extremely simple and it's not uh exhaustive which is good and bad. The good thing is that for simple cases you can use a Q table and it's it does the its job pretty fine. But when the amount of states and possible actions uh grow exponentially,

**[6:28](https://www.youtube.com/watch?v=66t87eHEzYI&t=388s)** this does not work. So how about instead of having this table, we can replace it with a neural network. Then we just pass the state and we get get a list of Q values which is its Q value for each possible action. That's the idea of uh DQM. But now if we wanted to improve it, because to train an AI, we could just make it play, let's say, against a random AI that just does random moves. It's like me trying to play chess against a toddler of two years old because I'm not going to risk saying more than two. Uh the thing will be that sure I will beat them, but then I will not improve because I I'm just beating a toddler

**[7:16](https://www.youtube.com/watch?v=66t87eHEzYI&t=436s)** that is not learning. So what if I put as an opponent another DQM that learns with me so that we can kind of improve together. That's the idea of dueling DQM which is uh a way of training the AI so that it improves faster. Now onto the implementation of the neural network. Uh this is uh slightly complex but we'll get to it. So the input size is just the uh number of uh input parameters uh which in this case will be the amount of possible actions and encoding of the state of the game. A hidden size which is well the hidden size uh it's the amount of neurons in the hidden layer of the neural network

**[8:04](https://www.youtube.com/watch?v=66t87eHEzYI&t=484s)** uh not so relevant. And the output size is the amount of possible key values that we have. So the uh worst case it would be the amount of possible actions but some of them are not legal as we saw in the in the previous example some of them are not possible so it wouldn't be those ones would have a null Q value but we're going to ignore them and then in those uh mat matrices and arrays uh we just encode the weights which are how much uh an neuron influences another and the bias which is well another utility to uh train the AI in a more let's say reliable way because if you set everything to zero in the start you don't get the best training results. Continuing with this, this is the init

**[8:54](https://www.youtube.com/watch?v=66t87eHEzYI&t=534s)** weights method that just initializes the weights with a he initialization which is just a normal distribution random values that follow a normal distribution not nothing to see there. Uh this is the forward which is let's say kind of uh you get your input you get you give your input you get your output using the signature of the method you give the state of the game then you do some calculations in the hidden layer and in the bottom loop you prepare the output which is just the array with your Q values each one for the for its possible action. Um so now getting into the DQN agent. This is uh basically your neural

**[9:42](https://www.youtube.com/watch?v=66t87eHEzYI&t=582s)** network, the other neural network which is the DN DQN idea that we showed before and then a memory buffer that just stores a list of possible actions and states so that we can remember them and use it let's say more efficiently. Continuing with the decing agent, we have some uh hyperparameters like gamma which is the discount factor which is basically how much into the future I care about. So if I put a gamma of.99 means that I pretty much care only about the future and I don't care about current rewards. I look more as to I want to get to a very big reward in the future and I don't care about small rewards right now. And the learning rate, you may think that it's just how fast you're going to learn, but it's just how much you're going to modify um

**[10:31](https://www.youtube.com/watch?v=66t87eHEzYI&t=631s)** the weights in your neural network, which is something that needs to be uh done with a grid search to see which is the best way of setting your learning rate on to encoding this state. Uh basically we encode the amount of colors that we have in the central zone. Uh this is a lot of code but is uh you can just look at the blue things to get the get the idea. Continuing to encode this state because this is a extremely long method. Uh we also check who is going first. We are going to encode the floor line of the player and encode the score of the player. We are also going to encode the scoring

**[11:23](https://www.youtube.com/watch?v=66t87eHEzYI&t=683s)** lines. Uh I know I'm going a bit too fast but the loops is is just I am iterating over the the walls and the pattern lines and everything. So it's just a lot of useless lines. The important thing is the idea of what we are doing. Then we encode the wall itself. First we were encoding the pattern lines. Now now we encode the wall. Um why not we also encode the tile back size because when we play this game physically there is uh tiles physically and maybe we run out of them. So why not encode that number as well? And now once we encoded the whole state of the game we encode the possible actions. And what's an action in this game is you take from a certain factory or the center of the board. You take a

**[12:10](https://www.youtube.com/watch?v=66t87eHEzYI&t=730s)** color and you put it into a line. So it's just encoding these three numbers. And finally we combine these two arrays that we had into one. We just take the state array, the action array, we combine them with array copy and we get the whole state action array. to select the actions we get the legal ones because this is just an utility method and we use an epsilon gre policy and epsilon gre policy means that if for example our epsilon is8 80% of the time we are going to find the best possible action based on our uh neural network output and 20% of the time we are just taking a random one because we want to explore epsilon greedy is a exploit explore uh policy so some sometimes we

**[13:01](https://www.youtube.com/watch?v=66t87eHEzYI&t=781s)** uh exploit. So we use the best possible action and sometimes we explore. So we try something new to see if we discover a new a new idea. And in the bottom you can see we found we find the best Q value when we don't use the epsilon GD policy. Uh this is a utility method to have this replay buffer that I mentioned before to store some moves that we have done. Uh this is the replay where we take a sample from the buffer, calculate the key values, we update the neural network so that we learn and sometimes as as we can see in that if sometimes we update the rival network so that we do the strategy of dealing that I mentioned before where we we try to improve faster

**[13:55](https://www.youtube.com/watch?v=66t87eHEzYI&t=835s)** for the trainer. We create the agent, the episodes which is the amount of games that we are going to play, the steps which is like I want to store the values of my neural network each a thousand games because I want to see if it improves and then some epsilons to see to start first exploring a lot and after some time we stop exploring so much and we take advantage of what we actually learned. uh how the trainer does it creates the game the AI plays we calculate the reward with a method that we'll get to later we save the things in memory and then we update the epsilon greedy policy don't worry too much about the amount of code and to calculate the rewards we basically take the score that we have

**[14:44](https://www.youtube.com/watch?v=66t87eHEzYI&t=884s)** now we substract the last uh round score and we give a extra penalty for the things that we put on the floor because I want to punish that extra so it basically just tells you if you gain points, you get a reward. If you lose points, you'll you get punished. Simple as as that as a reward system. And into the demo, basically, let's see if I can run something quickly. Come on, Gradle. Okay, choose the human player. Let's put zero load from file just because I trained it before and stored it in a file. And the file path is just my

**[15:33](https://www.youtube.com/watch?v=66t87eHEzYI&t=933s)** training.bing. Okay. And sorry about the UI stuff. I'm not the best UI developer. So we have this board with the factors that we see before. So we can just take say for example from factory zero the yellow and we take it into pattern line one. So that would be action say eight. We just take action eight. Boom. And then the AI does its move which was taking something uh to reds from a certain factory that I don't know exactly and put it into line one which is going to score them some point. So we can see that the AI does the reasonable stuff and goes for

**[16:20](https://www.youtube.com/watch?v=66t87eHEzYI&t=980s)** actually playing something that is reasonably human because it pretty much cloned what I did but with a different color and a different factory. And that was it. Thank you.
