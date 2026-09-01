---
id: 9jqQbEU3tdY
title: "Chuan Li - A Lab Notebook for Agents"
slug: chuan-li-a-lab-notebook-for-agents
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Chuan Li"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-09T18:45:49Z
video_id: 9jqQbEU3tdY
url: https://www.youtube.com/watch?v=9jqQbEU3tdY
youtube_url: https://www.youtube.com/watch?v=9jqQbEU3tdY
tags: []
transcript: true
---

# Chuan Li - A Lab Notebook for Agents

**Chuan Li**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=9jqQbEU3tdY) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,592 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=3s)** CHUAN LI: Hi, everyone. So this is not a mistake. This is actually my first slide. So what you are watching is Gemma 4 play on the game of Tetris. And at the beginning, as you can see, Gemma does not know how to play and scores 0. Then we had Claude watching how Gemma played the game and try to teach it to play better. Before we get into details, here are some of the rules. You cannot touch the weights of Gemma, so this is not fine-tuning. This is supposed to be an auto research project, so no human instruction is allowed. However, Claude is allowed to do certain things. For example, model settings, prompt optimization-- sorry, that's a big gap between letters-- and inference speedup.

**[0:51](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=51s)** So these are the things Claude can do. Also, for each game, there's a 30-minute timeout. So Gemma has to think fast. So over a period of 2 and 1/2 days, Gemma was able to improve from scoring 0 to scoring 16 points. And the rest of the talk, I'm going to share some of the lessons we learned. And what is making it all work is not so much about Claude is smart. We all know Claude is smart. But it's more of how we force Claude to write things down systematically. Just imagine how human scientists would write things down when they do experiment. We have notebook. We have whiteboard. We have sticky notes. We have sign-up sheets for sharing lab resources. Researcher agent use these tools as well,

**[1:39](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=99s)** and they can get these tools via APIs. For example, a notebook can become a note-taking API. The whiteboard can be your leaderboard where an agent can query result from. The sticky note becomes the message that can be passed between agents, and your sign-up sheet becomes your job queue. Our own version of this implementation is a piece of software, called Lab API. It's open-source experiment tracker we built it for auto research. Let's zoom out a little bit here. Imagine human has to do all this bookkeeping by hand. Each one of us will do it slightly differently and inconsistently. On the other hand, when we have this standardized API, research agent can do all of this in the same correct way every single time.

**[2:28](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=148s)** So the question we ask is, what happens when we give Claude Code a good experiment checker? We run this study with this Tetris game for 2 and 1/2 days, and I'm going to share some of the lessons we learned. The first lesson, not a surprise, agents cheat. You define the rules, you set up your environment, you press the Start button, and they cheat. Apparently, Gemma was able to score 15 million points. And what really happened is the Claude completely bypassed Gemma, stopped coaching it and wrote a simulation into the game source code. It even left a comment saying, completely skip this LLM block and write your own simulation.

**[3:15](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=195s)** I think it's pretty funny. So what we can do? Yes, we can build a cage. For example, we can make the game source code and a bunch of other files read only. However, this does not solve the problem. Apparently, Gemma still was able to achieve thousands of points. And this time, the way in is the chat template, which is written in Jinja, where you can put a for loop, you can put things like if else, and update the variable value. Basically, the chat template is Turing-complete. Then Claude was able to put in this big for loop to go through all the rotation allocation and find the optimal solution, and Gemma just needed to read the result out. And the way we prevent this from happening is to replace this Turing-complete template by something much simpler or restricted.

**[4:05](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=245s)** And the lesson here is if there's ever a way for agents to cheat, they will do it. So build a strong cage. Otherwise, you are not measuring the problem-solving skill. Another lesson we learned is if you run the same idea multiple times, the result may not be always consistent. Just think about all the knobs you can tune for each idea, and the things like the temperature of the model will make a difference. An example here. We run the same idea twice. The first time we score 3 points. The second time we score 4 points, only because we changed the max token setting. A naive agent will run the idea once and see the score and make a decision. A more sophisticated agent would run the idea multiple times with different settings before making a conclusion. And in order to have that, you really need to have a good experiment tracker. This is where we commit every single idea to its own Git

**[4:54](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=294s)** branch, keeping all the code changes and settings so you can always go back and reproduce. This also allowed us to try different things from the same idea and take the average score, for example, instead of a lucky high or unlucky low. Of course, this comes with a cost. Nobody complains about the cost until the bill gets too high. And in this case, it was really expensive because we run frontier model around the clock. And every single experiment used to take $30 to run, but we were able to reduce the cost by 10-fold. And the way we reduce the cost is also very interesting, because the Lab was designed to be a general tool. So we actually used the Lab to optimize its own cost. The way we did this is to set up a separate goal and standardize the kernel optimization.

**[5:43](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=343s)** And the goal there is not actually to make kernel faster. It's to generate enough API traces so Lab can look at its own trace and decide where I can optimize my own API design. So every single experiment becomes a Lab optimizing its own cost. As an example of optimization, what the Lab found out is there's an API called get_experiment. It returns a tons of information about the infrastructure, for example, Slurm and Git, and now this is needed for kernel optimization or playing Tetris game. By removing all these informations, the cost of this particular API got 50 times cheaper. So those are some of the lessons we learned. But how did Gemma actually get from 0 to 16? The improvement didn't come smoothly.

**[6:31](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=391s)** It comes in jumps. The first jump is from 0 to 4, where the Lab find out the first thing to do is to let Gemma survive longer in the game. So it invented this timeout movement. Basically, slide the piece to the left or right on the game board. Totally makes sense. In order to get from 4 to 7, what Lab found out is a cheat sheet, basically a set of best practice for individual pieces. So Gemma does not need to figure out all these movements completely from scratch on the fly. They have a reference book. Apparently this is also a strategy used by the England goalie in the World Cup game. A day into the study, the score flattened. Then the Lab looked into its entire history in the past

**[7:22](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=442s)** and found out there are certain pieces that are harder to place than others. And these are the pieces that need rotation. So we try to prompt Gemma to be more proactive about rotating those pieces. And that brings the score to 9. Up to this point, all the prompt changes are made to the system prompt, which is a 1,000-word-long context. And the Gemma has to read all this before even seeing the game board. Then the Lab realizes it has never touched the user prompt. So it puts this single sentence. it basically says, don't overthink, make quick decisions, right in front of the moment that Gemma is going to see in the game board. And this increases the score, almost doubles the score. And the funny thing here is this is a single line of change.

**[8:12](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=492s)** It took about 100 experiments to find out. And this shows the power of auto research, where the agent can try a lot of different things until something sticks. Obviously, there's a lot of things that didn't stick. Overall, the Lab tried 90 different ideas, over 400 experiments. Most of them didn't work. And for the sake of time, I'm going to skip the things that didn't work. But we do have a workshop in this afternoon, not tomorrow, if you are interested. And this is the link to get the software. Again, this is completely open source under MIT license. You can pip install it. We also have a tutorial about how to reproduce a Tetris run. Before I end the talk, I just want to call out that there's actually

**[9:00](https://www.youtube.com/watch?v=9jqQbEU3tdY&t=540s)** a human behind this study. His name is David Hartmann. He and his friends, Jan and Daniel, won the second place in the ARC Prize last year. Some of you may have heard about the ARC Prize. It's a Kaggle competition built on top of François Chollet's definition of how to measure intelligence. There's one of my favorite things I want to call out here. It says, "Solely measuring skill falls short of measuring intelligence." I think my point here is the opposite is also true. Solely measuring intelligence will fall short of measuring skill. You need both to make scientific progress. Thank you. [APPLAUSE]
