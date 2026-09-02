---
id: pPfsS9_4QMU
title: "Training My Rival in Java: A Deep Q-Learning AI to Play Azul by Victor Uria Valle"
slug: training-my-rival-in-java-a-deep-q-learning-ai-to-play-azul
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2026
speakers: ["Victor Uria Valle"]
channel: "Devoxx"
duration_min: 17
published_at: 2026-04-09T21:38:42Z
video_id: pPfsS9_4QMU
url: https://www.youtube.com/watch?v=pPfsS9_4QMU
youtube_url: https://www.youtube.com/watch?v=pPfsS9_4QMU
tags: []
topics: []
transcript: true
---

# Training My Rival in Java: A Deep Q-Learning AI to Play Azul by Victor Uria Valle

**Victor Uria Valle**

`Devoxx` · `Devoxx` · `2026` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=pPfsS9_4QMU) · [Conference site](https://devoxx.com/)

## Description

Please subscribe to our YouTube channel @ https://www.youtube.com/@DevoxxForever

AI has become part of our everyday lives but we often forget one of its earliest and most fascinating uses: creating an opponent to play games with.

We’ve seen it in chess, Go, and countless video games, where AI opponents follow complex strategies or fixed rule sets. But who says you need PyTorch or TensorFlow to do it? Sometimes, the good old Java is all you need.

In this talk, I’ll share how I built a Deep Q-Network (DQN) in Java to teach an AI to play the board game Azul. I’ll cover environment design, state encoding, reward shaping, and training strategies.

## Transcript

*2,702 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=4s)** Hello everyone. My name is Victor. I work at CERN in Geneva, Switzerland. And today I want to show a little project that I did uh trying to implement deep learning uh to play one of my favorite board games, Aul. To explain a bit how things go, the game has a common board that has these circles called factories. In the factories, there are tiles of different colors. And then there is a central zone which is where you put the remaining tiles. When you pick a color from a factory, you put them in the in your playerboard and the rest of them go into the central zone. Now, how does this look in code? Because I'm going to show as many examples as I can of the code. The tiles are just an enum of colors. Uh to recognize them when I'm

**[0:52](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=52s)** using the CLI, I just use some strings inside. And the factory is just a list of tiles. So nothing nothing big there. Now how does the player board look? It's just uh let's say kind of a pyramid. When you fill the par the row of the pyramid, you put that color into the wall and any excess tiles are put into the floor line to get a punishment in your score. Now how does this look into the code? So the floor penalties is just an array of the static scores that you're going to get punished if you put something in the floor. The pattern lines is just a matrix which is basically a list of lists. The wall is going to be static. So it's just a matrix that is just an array of arrays. And the floor line of

**[1:42](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=102s)** how many things you have actually put into the floor and our list. We track the score and the score of the last round because we are going to use it for the require function in our uh algorithm. Now onto the valid actions because we are going to take into account the action state space sorry. Uh so if we have to take the green color and put it in the first row we cannot because we have green there put already. We can put it on the second row but the excess green one has to be put into the floor. So we are going to be kind of punished there. The third one we cannot because we are already starting the pink project. We can put it into the fourth line and we can put we cannot put it into the fifth one. Now we could also put it onto the floor and uh lose points

**[2:32](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=152s)** for literally no reason. That's a legal move if you really want to. And uh another example that is useful is you can take things from the center but if the one that is the first player tile of the game gets taken it has to go immediately immediately to the floor. So you're going to be punished but for uh taking advantage of the center. Now the scoring seems a bit chaotic and it kind of is uh going all over it. If you put a tile in the wall completely alone you get a point. After that you get points based on the adjacency. For example, the squared uh red in the top left corner uh gives you three points because it has an adjacy of three vertically. If you take the uh border green one in the third row, second

**[3:23](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=203s)** column, it gives you a plus five because it's three adjacencies on the vertical and two on the horizontal. Now if you do a complete vertical like the fourth uh fourth one gives you seven points. A horizontal line gives you plus two points and the whole color like the pink one gives you 10 points. And then the punishments uh in the floor line are just as follows. So if you put something in the minus one, you get a minus one. On to how Q-learning works. Let's say that we have a Q table that basically takes a state and an action and spits out uh a value. It's easier to see it as an example. So let's imagine that we are the guy that is in the step well in the place one. So if we to if we took the

**[4:12](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=252s)** action right we are going to the goal. So we are going to give it a value of plus one because we are doing actually something that is good. But if we were in state one and we went and we took the action down would set ourselves on fire which is actually not that good. So we are going to punish ourselves. Now if we were in state five and we were went up we are not setting ourselves in fire but we are not getting to the goal either. So we're kind of putting a value of zero because it's not that bad but it could be better. And if we are in state six and we go down we actually reach the goal. So we give a very nice uh value to that because we are in a finished state. Now you can probably imagine that for this uh silly game uh these states and actions are pretty limited which is

**[5:00](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=300s)** basically like nine possible states and the amount of actions is four. So at most 36 actions but not all of them are possible because you cannot go to the left if you're in state one. But it can be even manually filled. Now for this game the state space spa state state action space is way bigger around the the size of chess approximately. So that's not something that I would be able to do manually. I would rather do literally anything else. So instead of creating a table we are just going to replace it with a neural network and hope for the best. That's the idea of deep learning. So instead of the uh table we pass the state of the game. Uh every variable in the state is just uh one part of the input layer and then

**[5:51](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=351s)** the uh amount of actions is the output layer. So for each possible action that you can take, you will get a possible Q value which is the values that we had in the previous table. not improve this even better because uh one way would be to train the neural network against random moves. Um it will probably learn but it would be like me trying to learn how to play chess by fighting a toddler of two years old. I'm not risking saying it's 5 years old because I may lose if they are a genius. Uh it's better to put another neural network so they fight each other. The one that is best replaces the other and they kind of improve faster. So that's the idea of the so-called D and DQN. So on to the implementation of the

**[6:38](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=398s)** neural network. There's going to be a lot of code and I'm going to rush through it. Uh I can accept the questions after. So you have the input size which is the amount of uh things in the state. The hidden size which is the amount of neurons in the hidden layer of the neural network and the output size which is the amount of uh actions that you can take which are going to be the Q values. So we can pick the best move for its possible state. Uh in those uh matrices and arrays we have the weight and biases. This is uh how a neural network decides how much an previous network influences each other. Now uh for initializing the weights we are just going to do some basic math of uh giving it a random value following a

**[7:27](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=447s)** normal distribution and that's how typically these states are are given for the well input size. Now to do the forward as you can see we pass uh the input as the parameter of the forward method which is the state of the game. We do some math in the hidden layer calculating the uh tage of uh of the previous weight. Uh this is used to improve the learning of the neural network. And then in the second loop, we take the things from the hidden layer and we multiply by the weight and do the math to get the output values which are going to be our Q values. uh how the DQ agent works is we have the

**[8:17](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=497s)** neural network that we are actually let's say actively training then we have the dealing one which is the target one and then we have a buffer because it's kind of useful to memorize some states and actions so that we don't like relearn something that we already know what to do in that case it's kind of useful when you don't have a amount of resources and if I'm running this locally in my Mac, I don't have that many resources. Uh, some hyperparameters. Gamma is the discount factor. Basically, how much into the future I'm willing to look. So, if I have a gamma of one, I just care about the future. Like, I don't care about my immediate move rather than I care about how well this will do in the next moves. And if I have a gamma of 0.1, then I care about the immediate

**[9:05](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=545s)** reward right now. And I don't care if I mess up something in my setup later. And the learning rate is the how much our weights are going to be affected by each training step. Uh on to encoding the state because we that's what we need to pass to our neural network. We just create an array and we encode the count of colors uh first in the central zone. This a lot of code, but just focus on the blue parts, let's say, because those are the relevant ideas. This is just kind of how the things are going. Now, we check who is going first. We encode that. We encode the floor line of the player. We encode the score of the players. More stuff that we have to encode for

**[9:54](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=594s)** the state. We go to the scoring lines of each of the players. This is just a couple of for loops. It looks like a lot, but it's just uh a few loops. We encode also the wall of the players. And now that we are pretty much encoding everything, we just encode the tile back size because this is a physical game. So there are tiles in the back. So why might as well just encode that as well. Now encode the action. So this is just basically one hot encoding. An action is just taking from a factory or the central song a color into a line. So it's just let's say three numbers. We fuse them together into this utility

**[10:43](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=643s)** method that just creates an array of the size of the state plus the actions and put everything together and we ship it. Now we have in the DQN agent the select action which is we get all the legal actions that we can do and we apply an epsilon greedy policy. An epsilon greedy policy is let's say we have a policy of8 which means that 80% of the time we are going to just do a random move and let's see what we learn from that and 20% of the time we are going to be greedy which means that we are going to take the actual best move. Why will we use this epsilon greedy policy? Because sometimes we want to explore and see the possibilities of something that we could learn that is

**[11:32](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=692s)** new and sometime sometimes we want to exploit which is take advantage of something that we already know and we're going to use it. So the epsilon greedy policy is something that should evolve over over time. We start with very random moves and over time we reduce this epsilon greedy so that we start taking advantage of the things that we learn but we still kind of want to explore a little bit. Uh as you can see at the bottom we just do the forward and find the best Q value we get the proper epsilon gre. Uh this is just a remember method which is which is basically we store the things in the replay buffer that I showed before so that we can save some computation space. Uh this is the replay which is we take a

**[12:25](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=745s)** sample from the buffer calculate the key values update the neural network and after some steps which I kind of believe it was like a 100 step we update the rival network. So the duelan part kind of does its job. Onto the trainer. Before we had the TQ agent. Now we have the trainer. We have the agent. The episodes which are the games that we're going to play the steps per episode which are how often we're going to do a save of uh our uh hyperparameters. And these are the epsilon greedy policy decay things. So we start at one. So everything random. And we kind of decay at 0495 until at some point just 5% of the moves are random. This is the train. Basically a lot of

**[13:14](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=794s)** code to just create the game, play with the eye, calculate the reward, save the move in memory and update the epsilon gre values. And how can we calculate the reward? Well, it's pretty simple. just take the new score h decrease it by the subtract the previous run score. So how much points we we gained by this move and that's just that onto the demo. I have one minute. So, uh I'm technically full stack, but my UI skills are terrible. So, it's just going to be a CLI. I hope it's readable. Yeah, it should be. Uh so, choose a human player. I'm the first one because why

**[14:01](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=841s)** not? Load from file. Yes, because I stored the hyperparameters somewhere. And my file pad is my training bin. So my train training okay so it looks terrible I know so these are the factories we can kind of guess what's happening so if I want to take from factory zero uh let's say these two yellow and put them in line one which has two slots we are going to take action let's say 14. So, we use action 14. And there we go. It went there. And the AI decided to take something in the

**[14:54](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=894s)** factory number three. the two red there and put them in row one, which is actually a pretty nice move because with this you're already completing that line and you're preparing a decent setup to score some decent points at the end of the run. So, surprisingly a very decent move for something that should have been not the greatest training, but you can see it kind of does the job. I could continue playing, but I'm pretty bad on time. So, I guess that's it. Thanks a lot. If you have any questions then? >> Yes.

**[15:41](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=941s)** >> So, this is what as I understand it's called reinforcement learn. >> Yes. And is there any tool or utility you use or you just use? >> I I literally used plain Java because the library that exists which is uh um deep learning for Java uh has a pretty complicated API. I was not very happy with it especially considering that the module that they have inside which is deep learning for Java is deprecated. Well, no, sorry. The reinforcement learning for Java is deprecated. So, I could not use that and I didn't want to use a deprecated library. So, I just coded the neural network and everything myself and it kind of worked. But yes, there are libraries for this. Although I

**[16:31](https://www.youtube.com/watch?v=pPfsS9_4QMU&t=991s)** would question how well they work.
