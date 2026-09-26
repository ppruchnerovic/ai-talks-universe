---
id: n0C1igDgNAU
title: "LeRobot Dataset v3.0: Scaling Reads with Ray | Anyscale | Ray Summit 2026"
slug: lerobot-dataset-v3-0-scaling-reads-with-ray-anyscale-ray
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 14
published_at: 2026-09-17T16:07:44Z
video_id: n0C1igDgNAU
url: https://www.youtube.com/watch?v=n0C1igDgNAU
youtube_url: https://www.youtube.com/watch?v=n0C1igDgNAU
tags: []
topics: []
transcript: true
---

# LeRobot Dataset v3.0: Scaling Reads with Ray | Anyscale | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=n0C1igDgNAU) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

LeRobot Dataset v3.0 is an emerging standard for robot manipulation data, but scaling reads from it is challenging: the format splits each episode across multiple video files while concatenating many episodes into the same file, so naive parallel processing requires opening each MP4 many times.

At Ray Summit 2026, Artur Niederfahrenhorst, Member of Technical Staff at Anyscale, looks at the format and at approaches for using it efficiently in Ray-powered pipelines.

You'll leave knowing how to read LeRobot data at scale without redundant decode work.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*2,369 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=n0C1igDgNAU&t=5s)** Um hey I'm at from the any scale team uh and I'll tell you now about the robot data set v3 format and our journey to solving reading it at scale. So we'll start with the data format itself and what a single row looks like and we'll then see why it's not easy to scale reads like with more homogeneous data formats and then comes our own implementation to the rescue and we'll go through some problems and solutions on the way and finally we'll close with some uh with with two small case studies. All right. So, HuggingFace came up with this uh data set format and they describe it as the standardized data format designed to address the specific

**[0:53](https://www.youtube.com/watch?v=n0C1igDgNAU&t=53s)** needs of uh robot learning. And Li Robot has recently gotten a version three and V3 uh stores more metadata in Paret and it also gives us long uh video files with multiple episodes inside of them instead of just images. And so an episode commonly spans multiple video files and um a a video file commonly spans multiple episodes. So this is how a L robot data set looks uh in memory and so we can uh see a bunch of rows here and the rows contain what you'd expect from uh when you are training a a robot, right? So we have some indices here, a task, uh the state of the robot, u an action and um camera images. But the data is not stored in a

**[1:42](https://www.youtube.com/watch?v=n0C1igDgNAU&t=102s)** table. Um it is scattered across files. So we have metadata files, we have uh other data files and we have video files. And so in order to understand how we resolve all this data, let's start with how uh this data looks when it's actually on disk. So this is one li robot uh data set called xvla soft fold and it has 1,500 examples of robots folding clothes. So we have three directories here uh with different uh access patterns. We have a per data set metadata that can be clo loaded into memory very quickly. We have a data directory for any per timestep data that goes into parquet files and we have images and videos with compressed image data. So we can see here that the

**[2:31](https://www.youtube.com/watch?v=n0C1igDgNAU&t=151s)** physical layout does not uh correspond to the unit of work that we currently that we like have in in in such workloads. So um the the unit of work would be an episode here and you know we have like anything but episodes on disk basically. Um so for those who are new to robotics here we can understand an episode as a series of time steps that belong together under one attempt to solve some robotics task. So for the XVLA softfold data set an episode would be one try of the robot folding clothes basically right and uh this is where we hit our first issue. So when we want to read all of this data in parallel, spreading reads across processes is trivial for like the tiny metadata part and also the state

**[3:19](https://www.youtube.com/watch?v=n0C1igDgNAU&t=199s)** action pairs that are in parquet files. But in each video file, we can have multiple episodes and they may or may not be consecutive. One sec. So um if you open and decode these video files, let's say per episode, you would pay a lot of uh IO and decoding. So for our XVLA softfold data set that would mean that we would open each file each video file uh 45 times on average and this number is from our engineering block. So if you're interested um you can you can find that online to dig deeper. So when you parallelize reading the robot data sets there should be two modes of reading. The first one is the naive one. So each retask gets one episode and it just opens the video files that it needs and you pay a bunch of IO overhead and uh but you can

**[4:08](https://www.youtube.com/watch?v=n0C1igDgNAU&t=248s)** squeeze a lot of like parallelism. And uh the second one is the slightly more sophisticated one where each uh read task gets uh a set of episodes that share video files. Uh so you basically just save a bunch of overhead that way. So for our um example data set for the clothes folding data set here is some um stats for these modes. So the baseline is a single process here. This is what you get when you don't parallelize at all like you don't use ray data for example, right? And uh so that's um 104 uh uh video opens. So that's pretty good. Um and then for one retask per episode, you can get to a very high parallelism. And when you group your reads by video files, you get

**[4:55](https://www.youtube.com/watch?v=n0C1igDgNAU&t=295s)** that efficiency. So specifically, you get 99 reads with only 300 file opens versus 1,500 retasks and 4,600 video file opens. And note that you still get three file opens per file in this example because the robot does not enforce that episodes are consecutive within video files. So in our implementation, we split reading um from files with non-consecutive episodes. And we implemented this in ray data uh and it's released already. So this more efficient file grouping mode uh is the default in our ray data implementation. Uh so our implementation you you can access it uh today by calling ray data readler robot and it has everything that you would expect from ray data. So it reads from cloud storage in place. It uh

**[5:44](https://www.youtube.com/watch?v=n0C1igDgNAU&t=344s)** spreads the load across uh of decoding across uh workers and it aligns frames uh and and outputs the robot data in the format um that you saw in the table that we started from in the beginning. And the API is in in alpha right now. So, you know, please submit lots of issues. And aside from this grouping, the following slides are about the uh ray data implementation and all of the problems that we needed to solve along the way. So uh how do you get started with this? Uh you call read robot. It will be lazy. Um this will just parse the metadata on the driver process. So in this example, it downloads the metadata from S3 and figures out how to divide episodes across retasks and how many rows we have and so on. So this bit of code up here

**[6:32](https://www.youtube.com/watch?v=n0C1igDgNAU&t=392s)** is safe to run at pabyte scale. And you can inspect the data set with a ds.s schema to get a sense of ray what ray data has planned for you and this would be the output output of the data set doss schema call from the previous slide um and you can see here that it's a full row of the robot data uh including images and everything but note the bottom row uh the stats so for one data set this row will be constant and it represents the stats of the entire robot data set that this sample belongs to and this really practical ical in a in a streaming framework like ray data. Uh so we don't have to side channel that sort of information and it just comes together with the data. But it also means that you as a practitioner need to be aware that this is per data

**[7:20](https://www.youtube.com/watch?v=n0C1igDgNAU&t=440s)** set statistics. So if you combine two data sets naively uh the the stats won't be accurate anymore obviously. uh and this is a high level view of how we execute uh reads with this li robot uh functionality. So as I said before we do all planning before we start streaming a single row and um the outcome of that planning is a pretty big table of uh indices and and metadata and each retask only gets a local view of that very big table. So each retask gets only the necessary metadata and uh paths to files and so on that it needs to download. um in order to compile the the actual the robot u um rows. So uh each task will then decode MP4 frames and uh

**[8:08](https://www.youtube.com/watch?v=n0C1igDgNAU&t=488s)** at the correct time steps and um there's like some tolerance there and it will start streaming PR blocks from there on and downstream we can then run pre-processing uh and and normalization and stuff and uh finally after that we can we we can potentially feed that data into ray train and that gives us an automatic sharding and bra pressure and busy uh GPU workers during training. So if you want to use our robot uh implementation with ray train this is how it would look we create a lazy data set first we set up the torch trainer with rate train and inside the training loop we iterate over a shard of the robot data set so this blob of code up here it enables us to decouple GPU workers from data ingestion and pre-processing and it turns them into

**[8:56](https://www.youtube.com/watch?v=n0C1igDgNAU&t=536s)** two separate processing pools uh that are connected via a uh backressured stream. And so earlier I mentioned that um the stats are per data set and this is this is not really worth mentioning if you're dealing with a single the robot data set but in the industry a lot of folks want to use many data sets in conjunction and so we did this in a way where you can just pass a list of data sets to our entry point and these data sets should have aligned keys such as you know like camera one or camera two because otherwise the the samples will have different columns and we have to error out. But since we do all the planning uh ahead of time, you know, like um on the driver, you don't end up with a with a cryptic column mismatch or something in the middle of a training epoch. And this

**[9:44](https://www.youtube.com/watch?v=n0C1igDgNAU&t=584s)** is also reason why we prefer to plan um the read tasks up front on the driver process because planning becomes much easier and you can catch errors like uh like this uh early. So these two knobs, the the episodes um and episode selector and the the read granularity um are probably the parameters that that you care about most when you use this. You get a predicate push down with an episode selector and um so you can use that for evaluation subsets and and debugging and you can set the read granularity to episodes here. So the alternative to doing that would be to filter downstream, but downloading and decoding is very costly and we'd rather filter at retime already.

**[10:34](https://www.youtube.com/watch?v=n0C1igDgNAU&t=634s)** So more often than not, you will be training over uh windows of data. That's a like a common thing. Um and hugging phase defines such windows uh through a timestamp selector. Um which which we call here delta time stamps. Uh so for each column you get uh random access across an an entire episode. So naturally we had to match hugging faces implementation in ours and this makes reading even more interesting because you want to reuse decoded frames um multiple times for efficiency. Right? So uh when you build consecutive rows you can uh cache decoded frames within episodes. And so by doing this uh in your data ingestion pipeline there's a lot to be gained here. But you also need to be careful that the frames don't uh

**[11:21](https://www.youtube.com/watch?v=n0C1igDgNAU&t=681s)** bleed across episodes for example or across episode boundaries. Um and that you account for for padding. Um so so these are stuff that you know we basically do behind the scenes for you. And the payoff of doing it is that uh you don't need to compile windows in your VLA training loop uh by hand and uh the reads become even more efficient. So finally let's uh wrap up with two small uh case studies. So we led with the uh XVLA softfold data set. Um and and first the IO savings that uh you get from grouping episodes uh episode reads by video files. Um that's that scales very well for large data sets. So if you go from the XVLA uh soft fold data set to the Droid data set

**[12:09](https://www.youtube.com/watch?v=n0C1igDgNAU&t=729s)** which has 100,000 episodes uh we get from 15 times fewer video opens video file opens to 135 times fewer video file opens and this because Android uh more episode files more episodes share video files which is uh kind of the trend or like what you would expect from larger data sets. And then secondly, another small case study that we did uh was for for actual training. So here we were able to decouple all the data mangling from our GPU workers. Uh so no uh IO and video decoding on the GPU workers and with that we were able to maximize throughput without local data set copies here. So um again like this enables you to use data sets at pabyte scale, right?

**[12:56](https://www.youtube.com/watch?v=n0C1igDgNAU&t=776s)** Without local copies essentially. And we we tried this out with PI 0.5. And you can find our training code on GitHub under the VLA fine-tuning examples repository that we host. All right. So finally our takeaways um for you know all the all the work that we did here um on Ray data. So the unit of storage and the unit of work in the robot don't line up at all which makes parallel reads very challenging at scale. And you can gain lots of efficiency by reading episodes uh grouped by files. And with ray data you get this this uh grouping sort of efficiency plus um you know we thought of a couple of other little robot particularities like the caching of frames uh for for Windows. Um finally I want to thank my colleague Omar Sherbaji

**[13:45](https://www.youtube.com/watch?v=n0C1igDgNAU&t=825s)** who's over there uh who worked with me on this. So um uh you know we'll be around after this talk and if you're using the robot data sets um me and also him will be very happy to to talk to you. Um that's all I have. Thank you very much.
