---
id: KiJCHbzS3BM
title: "Keynote: Where AI Meets the Physical World: The Robot MCP Ecosystem as an Ope... Rohit John Varghese"
slug: keynote-where-ai-meets-the-physical-world-the-robot-mcp
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "General software conferences"
edition: "Open Source Summit + ELC NA 2026"
year: 2026
speakers: []
channel: "The Linux Foundation"
duration_min: 15
published_at: 2026-06-03T18:22:28Z
video_id: KiJCHbzS3BM
url: https://www.youtube.com/watch?v=KiJCHbzS3BM
youtube_url: https://www.youtube.com/watch?v=KiJCHbzS3BM
tags: []
topics: ["Agents & orchestration", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Keynote: Where AI Meets the Physical World: The Robot MCP Ecosystem as an Ope... Rohit John Varghese

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit + ELC NA 2026` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=KiJCHbzS3BM) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Keynote: Where AI Meets the Physical World: The Robot MCP Ecosystem as an Open Bridge Between AI and Robotics - Rohit John Varghese, Director of Systems Engineering and Product, Contoro Robotics

## Transcript

*2,153 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=0s)** Well, it's good to be here. Just for my context, if you could humor me, I'd like to get to know who I'm talking to. So, just a quick show of hands, how many people here are actually, you know, familiar with MCP and used it? Okay, that looks like most of us in here. All right. How many people have worked with robots? A good number know what ROS, the Robot Operating System, is? Okay perfect. I guess with that I can jump in. And before jumping in, who am I? I'm I consider myself a roboticist. I was part of the founding team at Harmonic Bionics, where we did robotic exoskeletons as a medical device. Took

**[0:48](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=48s)** it from NSF-funded research concept to FDA-registered product. It's in hospitals today helping people recovering from stroke and spinal cord injury. Uh I've Oh, there's a video, of course I forgot. I'm also part of the founding team of Conturo Robotics, that's where I am right now, working with robotics for the warehouse. Uh proud Longhorn, briefly faculty at the University of Texas at Austin, which was probably the most rewarding piece of everything on this slide. I physically couldn't take the long hours alongside a startup. But why I'm here today is as part of an open source project using MCP to bridge agentic AI and robotics.

**[1:36](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=96s)** So, before jumping in, a sort of disclaimer is, you know, in the physically I world, we have end-to-end policies and VLAs, vision language action models, advancing on their own track led from the self-driving world, but also starting to penetrate the robotic space quite heavily. Today, what I'd like to talk is an alternate path. Uh, not applicable everywhere, but applicable in a lot of spaces. Uh, where bringing AI agents to already existing robots deployed on the field via MCP. So, I typically, when I'm talking to roboticists, I start by describing what MCP is. I don't think I need to do much of that in this room. Uh, I then introduce robotics middleware with ROS as the example, and then go into how an

**[2:26](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=146s)** MCP server, you know, connects the two. So, I'll really skip past this. What is MCP? It's the way that you connect, um, agentic AI, or AI AI models, really, to external tools. It It, you know, before MCP, you had a host of bespoke connectors that went between every every tool you had to every model. And I'm old enough to to remember when that was how external tools work for computers. MCP promised a unified Oh my gosh, I've been looking at the wrong screen all this time. I apologize. Uh, MCP promised a unified connector, which allows you to essentially connect

**[3:16](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=196s)** any tool that you build to any model. And enables you to get your agents and complex workflows on top of that existing infrastructure. It's all of the good things that we know about it. Coming to ROS, the Robot Operating System. It's really hard to describe what it is. It is so many things. But, in the context of today's talk, I'd like to focus on one part of it that it standardizes communication between different nodes that you might have inside a robot system. So, you could have hardware drivers that run your motors. That as one node, you could have your perception stack. Multiple nodes starting from your

**[4:03](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=243s)** cameras to different different nodes that process it. You could have motion planners for robotic arms. You could have um slam that gets your mobile robots. And within ROS, so this middleware you have topics, services, actions, and other ways of communication between these nodes. Again, ROS is it's hard it's hard to say it's so many things, but another piece that I really love is the vast library of community built tools. Of all the things that I told you just now, there are examples in ROS like MoveIt for uh motion planning of robot arms, Nav that does it for mobile robots. And so, bringing the two together. So, um

**[4:52](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=292s)** again, structure of ROS, don't need to go too deep, but bringing the two together. Essentially, if we could write a MCP server that on the back end is plugging into existing robot middleware. And on the front, exposing that as an MCP server to your AI models, essentially right now you've got something that's compatible across AI systems cross-platform. And as a roboticist, what excited me the most is it plugs into existing robots without any custom code required. Because using existing middleware, existing protocols that go through, again taking ROS as this example, I did not need to write or modify the

**[5:41](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=341s)** other nodes on my robot. I just had to add one more. And that created surprisingly emergent behavior. It surprised us as we first started it. And the response, I'm going to actually say over here, this is my first contribution back to the open source community and it's been quite humbling the the growth we've had since we went public in September as a, you know, collaboration between us and university lab. But I want to point out over here that this is not really a strength of what we did, but right place, right time, right idea. That adding agentic capabilities to existing robots can really create some emergent

**[6:31](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=391s)** behavior. So, at this point, I'd like to invite you to see some examples of this. Um going to feature a lot of what I saw in the community and one of our own. So, this is Wilson. It's built by It's a little custom robot, completely designed and built by Trace LaRue uh at the University of Texas at Austin. And it's a mobile base. It's got a little robot arm on it. It's got It's It's running ROS under the hood to to handle most of its internal operations. But then using ROS MCP added Gemini as a layer on top of it. Now, I'll let you see some things that uh that he's done with it. Uh Nate, do we have the audio on that? I'll just jump back. All right, let's

**[7:21](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=441s)** go. Hey Wilson, can you get me a Coke from the mini fridge and bring it to the living room? Got it. I'll get you a Coke. I brought your Coke to the living room. It's the goal of every robotic student, right? You have your your your little robot helper that gets you your Coke from the mini fridge. Uh but over here, what you had him do is of course you can recognize Gemini doing uh handling the interaction, the the voice interaction to the robot commands. The navigation across the room is handled by Nav 2, which is a slam package within ROS.

**[8:08](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=488s)** The when the fridge is opened, I saw a different demonstration of his where there was a Coke and a 7 Up. And so, the photo taken by the robot goes back up to Gemini, which says the Coke is on the left, and aims the robot that way. Okay, the Coke is now centered in the frame. Grab. So, really nice interplay between the two. I'm going to jump to the next example. This was asset control. Now, we're coming to industrial robots. So, over here I'm using Claude. I've got Robot MCP connected to the robot. And it's vanilla Claude, no no pre-training, but I have given it access to the technician manual. And I'm going to say, "Go debug my robot." Of course, I'll introduce a fault to start with. And that's a vacuum gripper. So, what

**[8:59](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=539s)** you're going to see is it testing the whole system there. After exploring, it's realized how to control the robot. It's enabling the valves. Reading pressure sensors. And then from the manual, it detects that the red values are too low. Going into the manual, decides to perform more tests. Let's It decides to isolate where is the fault. Opens and closes a few more valves, reads the pressure. Analyzes and summarizes as language models do very well. Correctly identified the issue, told me a leak. And my my favorite part

**[9:46](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=586s)** over here is it recognized that this is by the pressure reading when it opened just that zone being extremely low, comes back and tells me this is a big leak. So you're you're not talking just like a crack in your hose. One of your cups has fallen off or the hose has been unseated. Uh go inspect. And this is something that I now have my my field crew run periodically. Just run the gripper tests. And it finds a small leak somewhere, isolates it to a zone, and says go inspect that. It's something I use for debugging when I'm when I'm working on on robots. Like, "Oh, my gamepad didn't work." Just examine it. Find out where in the whole system you've got the problem. There's other people in the community. Oh gosh, me and my bad clickers.

**[10:36](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=636s)** Going to do that. No. It's Ah! Let's try this one more time. I'll be patient. There we go. There's other people in the community who have uh who have used this on mobile robots. So on the left you've got controlling and orchestrating a drone. And Dongbin over here has has actually done this even outdoors. Again, using other packages of SLAM and other forms of navigation involved in ROS to navigate several miles, draw a circle go in circles at a 1-mile radius around our building. And on the right, controlling a Unitree Go.

**[11:23](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=683s)** If you look at the prompt that Bharat gave over here, it's extremely vague. It says, "Do various flips and shake a hand." And what you had cursor doing over here was again going through the the API that this little robot has and sees that backflip is send a command three, shake hand is send a command 22. And it's it's doing those things. Also, in simulation So, over here you've got two robots being orchestrated by the same model. One to push a box out of the way, an obstacle out of the way, and then bring the other one into that space now that the obstacle's cleared. And use the cameras to see what you can see.

**[12:12](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=732s)** It's a simple demo, it's only a fire extinguisher but the the the research that uh they were proposing at Harco Lab, they were our collaborators who actually worked with us from the early days of the MCP was that this can be used probably to send your your little robot around the warehouse and look for anomalies, look for open doors, and other things. Tying all this together, kind of the vision that I'm hoping to see with this is giving an option to combine the reasoning and adaptability of modern AI as it matures. I forgot to mention the previous example was using a local model. So, not the cloud-hosted ones. And connecting that to the repeatability and maturity of robotic tooling today.

**[13:01](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=781s)** Now, we just joined the AgentiKI Foundation under the Linux Foundation. We hope to support, you know, I have a lot to learn about about doing things open source, but I hope to actually uh join the effort. And something that makes me personally excited for this is when you use this modular approach all of the safety layers that you bake into robots, especially important in industrial robots, are preserved. The agentic layer is not able to override them. And allows you to be reliable and trustworthy. And another piece that we already saw in the examples today is that this lowers the barrier to entry for agentic physical AI orchestration. Uh by essentially putting together

**[13:50](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=830s)** modules that already exist and having the emergent behavior that many people today believe is only possible with end-to-end trained VLAs and models. So, if I were to leave you with one message, it's that physical AI doesn't always need the bigger model. Sometimes it just needs a common interface. And Robot MCP is one such example of that. Where we took reasoning and orchestration from both local and frontier models combined with the control of existing mature middleware. Open and modular, it allowed us to skip retraining using just vanilla vanilla AI models without any custom glue.

**[14:39](https://www.youtube.com/watch?v=KiJCHbzS3BM&t=879s)** And again, I have to say that this is not in the physical AI world is so big that no one approach is going to solve all problems. So, VLAs, end-to-end approaches, learn policies extremely powerful and have high use where low latency and dexterity demanded. But, there could be a vast space where MCP could enable existing middleware to create emergent behavior. And with that, thank you. Uh this is an open-source project, so please do get in touch, try contributing, and uh thank you very much.
