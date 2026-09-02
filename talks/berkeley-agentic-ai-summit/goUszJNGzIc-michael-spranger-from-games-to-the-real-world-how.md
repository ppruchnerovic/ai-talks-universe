---
id: goUszJNGzIc
title: "Michael Spranger - From Games to the Real World: How Reinforcement Learning Is Powering Performance"
slug: michael-spranger-from-games-to-the-real-world-how
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Michael Spranger"]
channel: "Berkeley RDI"
duration_min: 11
published_at: 2026-08-09T23:26:52Z
video_id: goUszJNGzIc
url: https://www.youtube.com/watch?v=goUszJNGzIc
youtube_url: https://www.youtube.com/watch?v=goUszJNGzIc
tags: []
topics: ["Training, fine-tuning & model building"]
transcript: true
---

# Michael Spranger - From Games to the Real World: How Reinforcement Learning Is Powering Performance

**Michael Spranger**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=goUszJNGzIc) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,863 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=goUszJNGzIc&t=2s)** MICHAEL SPRANGER: Hi, there. So I'm going to tell you a story that we built at Sony AI over the last five to six years where we took reinforcement learning, we built racing agents in game, beat the best drivers, put them into product and then use exactly the same infrastructure, the same AI agent factory to solve problems in the real world. And so it starts-- everything starts in 2022, when we released our first nature cover on this project that we did on Gran Turismo, which is a racing game. It's a 30-year PlayStation title led by the visionary Yamauchi-san, who really is interested in recreating the sensation of racing. It's actually not a very easy game to play. You have to really hone the skill of driving in order

**[0:52](https://www.youtube.com/watch?v=goUszJNGzIc&t=52s)** to enjoy this game. And what we did is we built a reinforcement learning agent to beat the best drivers as a first step. And if you look at this race, this is a race from an actual competition against one of the best. There's more people on the track, but in this instance, against one of the best drivers in the world, I'll challenge you to tell me which of those two cars is driven by an AI versus a human. And I think you can't, because we've built this AI to be a really interesting, competitive, but in some sense also human-like driver. In fact, the car that's driven by AI is the gray car, and the White car is driven by Yamauchi-san, who is a world champion in Gran Turismo. Now, Gran Turismo is a very, very interesting benchmark test

**[1:43](https://www.youtube.com/watch?v=goUszJNGzIc&t=103s)** for us because it combines physical realism. The game itself is built around a physics engine that really recreates in high fidelity cars and their physical properties on, in some cases, real-world tracks. So there's a physical realism. So if you want to do racing, the first thing you have to do is, you have to master driving a car. Now it's not just driving a car. It's racing a car. And racing itself is really at the edge of control. It's sometimes going over the edge of control and pushing the limits. The second point is, you're not alone on the track. You have to manage tactics. If you make a move against an opponent, that opponent will counteract your move. And so you have to learn how to deceive, how to test your opponent.

**[2:31](https://www.youtube.com/watch?v=goUszJNGzIc&t=151s)** And then finally, sports etiquette, which is also very interesting. Racing, I would say, is an interesting sport because it's a sort of collaborative and competitive dance. You're not really supposed to crash into other cars. At the same time, you have to drive very aggressively, because otherwise, you're just going to be overtaken and lose the race. And so we trained an end-to-end system to solve all of those things at the same time. And, of course, we use reinforcement learning. So I think many people in the room will be familiar with this. We essentially use the game as the environment. We get inputs from the game. Those can take different forms, from visual to stage representation, similar to an autonomous car. Of course, the agent takes actions in the game. And then also there is a reward. And the reward, as you can imagine, is if you're fast and overtaking,

**[3:18](https://www.youtube.com/watch?v=goUszJNGzIc&t=198s)** that's great if you crash into other cars, bad if you're not really making progress on the track, bad. And so that alone is enough for us to build these highly specialized, very, very capable AIs in Gran Turismo and ultimately also in other games. So we'll need some infrastructure for this. So we worked a lot with PlayStation-- obviously, the maker of the game, but also PlayStation infrastructure. The game itself only runs on PlayStation, so we have to use Cloud Infrastructure of PlayStations to get the scale of compute that we need in order to build those agents. Now we can train those agents once we're done with the research relatively fast. So after 15 minutes of driving, we can basically get around the track and then it takes about 24 hours to get to a really, really [INAUDIBLE]. [CAR SCREECHING]

**[4:06](https://www.youtube.com/watch?v=goUszJNGzIc&t=246s)** But ultimately-- that was a bit too early. Ultimately, it takes a few days to train a superhuman policy. Now, what does superhuman look like? So this is a track called Dragon side-- Dragon trail seaside and this is just again, sick time. So it's a time trial example. But what you'll see is something coming up called the chicane of death. And this agent is taking this in a superhuman way. No human driver has taken this chicane, which is going to come up right now in this way. So that's the physical realism, learning how to manage the car. This is also very interesting actually. Let me go back for a second here and start from the beginning. What you'll see here is the agent tactically trading off positions in order to have a better entry

**[4:56](https://www.youtube.com/watch?v=goUszJNGzIc&t=296s)** and then exit in the curve. In fact, we're going to see a double overtake by AI white cars driven by humans, colored cars driven by AI is going to be a double overtake of AI to humans. So you can see the cars starting to trade off positions here in order to have a better entry. And then double overtake exit into the curve. So these really subtle differences, these really tactical choices of when to trade over position in order to have a better entry exit. That's also completely learned. Anyway, so all of this is enough to train agents to be really, really successful, superhuman, successful, superhuman, beating the best esports drivers in the world. Now, for us, that's not enough. We're actually very interested in building agents that are fun. And so we're going to listen to somebody

**[5:44](https://www.youtube.com/watch?v=goUszJNGzIc&t=344s)** that is also a high-end racer. Tell us about what she learned from the AI. [VIDEO PLAYBACK] - It was really interesting seeing the lines where the I would go. So there were certain corners that I was going out wide and then cutting back in, and the AI was going like in the whole way around. So I learned a lot about the lines and also knowing what to prioritize. Like the AI into turn one, for example, I was braking later than the AI, but the AI would get a much better exit than me and beat me to the next corner. So I didn't notice that until I saw the AI and I was like, oh, OK, cool, I should do that instead. [END PLAYBACK] MICHAEL SPRANGER: Of course, this is reinforcement learning.

**[6:31](https://www.youtube.com/watch?v=goUszJNGzIc&t=391s)** So in game. We can also train many other types of behaviors using exactly the same framework. So changing the objective from going very fast to burning as much time as you can gives us superhuman drifting agents. Now, so that's all great. It's all fun and games. Obviously, part of us being a part of Sony is also this opportunity to ship these products to millions of people. And so after the Nature paper, the team worked very, very hard on many iterations of this technology, integrating it into the game 6 months after the Nature paper, all the way to something that I'm very proud of, which is a power pack, the first ever paid power pack for Gran Turismo, where people pay directly for an AI experience. Because it's such a human like experience,

**[7:20](https://www.youtube.com/watch?v=goUszJNGzIc&t=440s)** we can have longer races, we can have more fun races, and PDI decided to build a power pack around this new capability. And now people pay directly for new AI experiences in this space. So this is the PlayStation part, the simulation part, the Gran Turismo, the racing part of the story. Now, I've told you that essentially we've built a system that we can apply not just to racing, but we can also apply this to different games, different titles, open world titles, casual games. But the thing that we did this year or that came out this year, I should say, is taking that same technology and applying it to table tennis. And table tennis obviously has many fundamental similarities with racing in the real world. There's physical realism, you have tactics,

**[8:08](https://www.youtube.com/watch?v=goUszJNGzIc&t=488s)** there's an opponent that you have to beat. And so building a factory for agents that can solve these highly specialized, competitive tasks is something that we showed with this work as well. And so I'm sure all of you know table tennis, this is one of the trainers that we use to train the robot. The ball is moving across the field, literally in the blink of your eye. The ball's rotation, the spin is the main difference between professional and amateur players. The ball spins at about 9,000 rotations per minute, reaches speeds up to hundred kilometers an hour. And all of in this interaction. So you have to master the physical skill. And at the same time, on the other side of the plate, there's somebody who's trying to beat you. And then, of course, you may have surprising situations.

**[8:57](https://www.youtube.com/watch?v=goUszJNGzIc&t=537s)** And so this video is going to slow down in a second-- because the ball hit the net, something we did not foresee in training or couldn't train for. And so within fractions of a second, this end-to-end policy-- there's no programming here. It's completely trained end-to-end. This robot has to react to this new situation, change the plan that it made at microsecond level. Now, the similarity with GT, Gran Turismo, doesn't stop there. In fact, we use a simulation, a custom simulation for table tennis, to train the policy and then bring it onto the real robot without any changes and just play professional players using that. So this is really cool. This is one of the top players that we beat with this robot.

**[9:46](https://www.youtube.com/watch?v=goUszJNGzIc&t=586s)** Miu Hirano, really, really successful table tennis player. And I think this is the second point. So she's going to make that point, which is going to be fun. [? I don't think ?] she's going to be very happy about that. So that's great. Unfortunately for her, ultimately, she's going to lose that game against the table tennis robot. And in the meantime, we've tested this system against many, many players. And we essentially have a flywheel now where if the robot still loses to a player because of an unforeseen or unexperienced tactic, we can use the data from that game to retrain the policy overnight and then have a robot actually beat that player. And so the argument I want to make here is that I think LLMs are great.

**[10:34](https://www.youtube.com/watch?v=goUszJNGzIc&t=634s)** I think world models are great. We should not forget about reinforcement learning and its ability to build highly specialized policies that can solve tasks in the real world and in simulation at superhuman capacity. And I think it's a combination of all those technologies that's going to ultimately help us to solve the big, big problem of physical intelligence. Thank you very much. [APPLAUSE]
