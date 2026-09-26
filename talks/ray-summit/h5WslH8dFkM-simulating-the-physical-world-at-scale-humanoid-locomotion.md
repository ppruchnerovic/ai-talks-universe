---
id: h5WslH8dFkM
title: "Simulating the Physical World at Scale: Humanoid Locomotion with Ray | Lambda | Ray Summit 2026"
slug: simulating-the-physical-world-at-scale-humanoid-locomotion
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 13
published_at: 2026-09-17T16:01:51Z
video_id: h5WslH8dFkM
url: https://www.youtube.com/watch?v=h5WslH8dFkM
youtube_url: https://www.youtube.com/watch?v=h5WslH8dFkM
tags: []
topics: ["Classic ML & data science", "Inference, serving & GPU infra", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Simulating the Physical World at Scale: Humanoid Locomotion with Ray | Lambda | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=h5WslH8dFkM) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Scale humanoid locomotion and navigation training and simulation from a single GPU to a distributed Lambda GPU cluster.

At Ray Summit 2026, Amir Zadeh, Staff Machine Learning Researcher at Lambda, demonstrates Isaac Lab running thousands of parallel simulations while Ray orchestrates training jobs and hyperparameter tuning across multiple GPUs: building a navigation task, launching distributed experiments, and evaluating the resulting policy in unseen environments, with better visibility into experiment performance and GPU utilization along the way.

You'll leave with a practical blueprint for accelerating physical AI development while reducing training time and cost.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*1,760 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=h5WslH8dFkM&t=6s)** All right. Um my name is Amir Zadeh. I'm a staff ML researcher at Lambda. Um Lambda is a GPU provider, so you would be able to get uh different kinds of GPUs from us, uh public cloud GPUs and private cloud GPUs. Uh we also have an internal research team, and our internal research team is um mostly concerned with open research. Uh we make everything that we do open source. Uh and we want to sort of like understand the customers' workloads and by doing research in in those verticals that our customers are interested in. Um today I want to talk about how we use Ray for our robotic simulations. So,

**[0:56](https://www.youtube.com/watch?v=h5WslH8dFkM&t=56s)** one of the things that we're interested in is improving the gait of humanoids. So, let's say hypothetically you have challenging environments and um you know, you have a particular robot, let's say Unitree G1, that you're interested in uh improving the gait. Um so for those who don't know what the gait of the robot is is just a walking style, how you move your legs in order to be able to navigate the environment that you're in. Um so yeah, we we start from a checkpoint that already exists from Unitree, and we want to build on top of that using reinforcement learning and Nvidia Isaac Sim. The cluster setup that we have is we

**[1:45](https://www.youtube.com/watch?v=h5WslH8dFkM&t=105s)** have two total nodes. Each one of them have eight GPUs for this, eight B200s. Um so total of 16 GPUs that we have in this particular cluster that we use for gate improvement and other improvements on this particular robot, but for the sake of this presentation, mostly gate improvement is our focus. So, this is where things get interesting because Ray helps us get into you know, the distributed framework that we want to go in relatively easily. Relatively easily in the in the sense that the code is very similar to what we would have done if we wanted to use one GPU, but then we're able to scale it to

**[2:33](https://www.youtube.com/watch?v=h5WslH8dFkM&t=153s)** many GPUs. We're able to get 512 environments per each GPU. So, 512 environments basically means that let's say we come up with a relatively straightforward scenario, right? Where you have cubes that have different masses and different frictions with the flat surface of an environment and you just want to learn navigation in an environment like this. You would think that this would be an easy environment because it's just, you know, thousands of cubes scattered across, you know, some plane. But it's not. The robot falls in average of about 4 seconds as we will see. So, there's a lot of environments that we

**[3:21](https://www.youtube.com/watch?v=h5WslH8dFkM&t=201s)** need to cram in each GPU. And that's going to be 512 environments. So, it is roughly the same environment in terms of description. So, cubes, plane, same robot, just go in a different direction with different velocity, with different trajectories and paths to follow. And so, that gives us on the 16 GPUs 8,192 environments total. Um and we get about 139k environment steps. So, environment steps basically means you take a step to solve what the next iteration of the environment in Isaac Sim would look like. Now, this is something interesting because

**[4:10](https://www.youtube.com/watch?v=h5WslH8dFkM&t=250s)** we run these simulations headless. We don't care about what the camera is seeing. That's why we're able to get it running on these V200s despite the fact that they don't have ray tracing. So, that's a key factor here is that what we do is try to improve the robot's gait without changing the vision sensors or other sensors that are there. It's just the robot being able to walk better. So, the physics only concern is what we're after. So, what does the training environment as a whole look like? As I mentioned, there's going to be cubes, different sizes, different shapes, different masses, different frictions. The robot has no

**[4:59](https://www.youtube.com/watch?v=h5WslH8dFkM&t=299s)** idea what these cubes are. It will only see them the moment it has made contact with them. Right? So, the sensors on the robot are going to basically say what it has touched, but not in terms of, "Oh, you just touched the cube with this mass and this dimension." But, you're going to just get those forces that are applied back to the body of the robot. Um and our learning signal is pretty straightforward. Whether or not you have fallen. Um and it's easy to calculate whether or not you have fallen based off of the orientation of the robot. Another thing that we do is if you just want to to teach your robot

**[5:48](https://www.youtube.com/watch?v=h5WslH8dFkM&t=348s)** to follow that learning signal, there's nothing stopping this robot from learning to go on, you know, both hand and feet and walking like a dog right? So, you want to make sure that the humanoid still remains a humanoid because there are many ways that it can walk and some of those might be funny, but they might end up working really well in that environment, right? And as a result of that, you know, congratulations, your robot doesn't fall, but at the same time it's no longer a humanoid anymore. So, it's important to sort of like have this KL divergence towards some of the metrics that are desirable for you, towards the original policy as well. And if you're learning this in a PPO

**[6:35](https://www.youtube.com/watch?v=h5WslH8dFkM&t=395s)** setup, that's something that you can, you know, easily easily follow and easily um implement. So, some of the things that we look for in order to keep this robot moving like a human, uh the speed of joints is important. There's certain speeds that human joints cannot do. Uh the speed of the legs are important as a result of that. And the total amount of time that robot has feet in the air. So, you don't want the robot to go super fast or super slow uh because the robot can just cheat and learn that micro steps are better in solving a cube environment. So, those are the type of things that

**[7:22](https://www.youtube.com/watch?v=h5WslH8dFkM&t=442s)** you always want to penalize and you want to make sure in setups like this where you're fine-tuning for a particular environment that you get those nailed down. And we also do this kind of like between easy environments to difficult environments. It's good if the robot can can have some easy environments in this kind of training setup cuz you're going to get some easy gradients as a result of that and those easy gradients are going to make the learning curve a little bit smoother, a little bit easier. So, going through the code um the way we map this is we map environments to GPUs that do both the generation

**[8:10](https://www.youtube.com/watch?v=h5WslH8dFkM&t=490s)** and the gradient calculation. So, each GPU does its own generation natively and then it records those genera- generated results. And basically calculates the gradients based off of that. And so there's as you can see there's pretty much two main functions here, generate and compute grad. The second piece is where we use Ray. And this is the part that makes it, you know, relatively easy, straightforward to use Ray. Um each one of our workers are basically, you know, we just set them up and we have a for loop for the number of iterations.

**[8:58](https://www.youtube.com/watch?v=h5WslH8dFkM&t=538s)** We do the simulations based off of the policy that we have at time T in phase one where all workers roll out and then in phase two we calculate the gradients and we update for the next round. Um most of the time all the information remains on each individual GPU. We don't kill the bandwidth between the CPU and GPU this way. The only time that things are actually accumulated is the time that we're updating the weights for the next iteration. So this is this is kind of like interesting. Um the fall rate of the original

**[9:46](https://www.youtube.com/watch?v=h5WslH8dFkM&t=586s)** policy that was trained was about 4% 4. You know, close to maybe like 4.75-ish. Right? Now, the fine-tuned one goes down to around like 1 or closer to like, you know, 0.78. So, this improvement is big. But, there's a lot of big improvements that can be made. Is this improvement correct? Is the ans- is the question we got to ask ourselves. So, what if the robot just decided to stay where it is? There's no fall. I'm getting rewarded very heavily for me not falling. Right? So, you have to make sure the robot was following commands. Right? So, the distance per episode

**[10:35](https://www.youtube.com/watch?v=h5WslH8dFkM&t=635s)** before the fall is important. If you were not traveling before you fell, that's not good. So, the distance has also improved. Meaning that the robot indeed traveled. And it was able to fall fall far less. And a mean episode return is sort of like a combination of all of these factors that we have that we put into this robot. Our hope is that around that same mean episode return, the robot will be able to reduce the fall rate. So, we don't want it to start cheating in terms of like how the elbows are moving. We don't want it cheating in terms of how the torso is. Right? So, there's a lot of things you got to keep an eye on to make sure that

**[11:25](https://www.youtube.com/watch?v=h5WslH8dFkM&t=685s)** it is following the correct trajectory. And this is sort of like the final ones that we have. So, this is the original the policy released as a pre-trained policy on I in Isaac Sim. That the cube that has a different color is a particularly interesting cube because it's a little bit heavier, denser. And so, when it hits it, it immediately falls. And this is after fine-tuning it was able to bypass that and just go through it. Now, it may fall for another cube, but that particular cube Oh, it didn't. So, overall was a successful session.

**[12:14](https://www.youtube.com/watch?v=h5WslH8dFkM&t=734s)** So, Ray helps us kind of like get these trainings set up and running without having to deal with a lot of uh you know, cluster setup issues that can happen and we can just test around these hypotheses and make sure that the robot is doing what we expected um to do. So, as I mentioned, we are from Lambda. If you folks need GPUs, we have different kinds. Um we also have a research team. So, if you have interesting research ideas, let us know. Um yeah, I think that's uh that's it. Thank you.
