---
id: dKZxUcuOb8A
title: "PyTorch and CPU-GPU Synchronizations [PyCon DE & PyData 2026]"
slug: pytorch-and-cpu-gpu-synchronizations-pycon-de-pydata-2026
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Tomas Ruiz"]
channel: "PyData"
duration_min: 27
published_at: 2026-08-04T22:21:37Z
video_id: dKZxUcuOb8A
youtube_url: https://www.youtube.com/watch?v=dKZxUcuOb8A
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# PyTorch and CPU-GPU Synchronizations [PyCon DE & PyData 2026]

**Tomas Ruiz**

`PyData` · `PyData` · `2026` · `27 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=dKZxUcuOb8A) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Tomas Ruiz reveal how to identify and eliminate hidden CPU-GPU synchronizations in PyTorch to unlock maximum hardware performance and throughput.

Speakers:
Tomas Ruiz

Description:
PyTorch executes GPU operations asynchronously, allowing the CPU to schedule tasks and run ahead of the GPU. Performance degradation occurs during CPU-GPU synchronization, which happens when the CPU must block and wait for data to return from the GPU to make a decision or allocate memory. This creates "bubbles" of inactivity on both the CPU and GPU, reducing overall hardware utilization.

Common triggers for synchronization include calling .item(), .cpu(), or printing tensors, as well as using GPU tensors within conditional if-else branching. More subtle synchronizations arise from operations that result in dynamic shapes, where the output size depends on the tensor data. Examples include boolean indexing, slicing with a GPU-resident integer, torch.non_zero(), and torch.unique(). Because the CPU manages memory allocation, it must synchronize to determine the output shape before the GPU can proceed.

To mitigate these issues, developers can reduce the frequency of synchronization—such as printing loss every 100 iterations instead of every one—or use padding to maintain static shapes. Some PyTorch APIs, such as torch.repeat_interleave(), provide optional parameters to specify the output size, bypassing the need for synchronization.

Profiling tools like NVIDIA Nsight Systems can visualize these delays as CUDA stream synchronize calls. For automated detection, PyTorch offers an experimental debug mode via torch.cuda.set_synchronize_debug_mode(), which can be set to warning or error. This allows for the creation of unit tests using decorators that fail if a function triggers a GPU synchronization, ensuring production code remains efficient.

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

*3,965 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=6s)** Yes, thank you very much. Um, super happy to be here. Um, yeah, so I'm a PhD student in Munich at the LMU University and um, I'm going to talk today about these uh, the synchronizations in PyTorch. Come in. So um, who is this talk for? I guess it's good for every anybody who is um writing PyTorch in their in their day-to-day and is using GPUs to accelerate their workloads. In this case, this talk is for you. I want you to take away like go leave the room understanding what are these synchronizations that I talk about um and why they are important namely because they they silently slow down the performance of your application.

**[0:55](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=55s)** And it's it's not that your code is incorrect. Your code is still going to be correct, but it's just going to leave a lot of speed on the table. And finally, I want you to to be able to spot them and then to fix them. So the the overview is going to be we're going to be looking at a basic training loop like everybody has probably seen uh before and this is going to have a synchronization. So that's problematic. We will then um dive into look at some real profiling traces so that you can see how if you use real profiling tools what what will you see in these case of synchronizations with Nvidia inside systems. [snorts] Then we will dive a little bit deeper into more subtle um patterns that trigger synchronizations. And finally um we will have a look at

**[1:45](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=105s)** unit testing to check that whether your code contains synchronization so that you can uh be confident that your synchronization free uh that your code is synchronization free. [snorts] So let's get started. This is the the familiar training loop that you might have written yourself um for your machine learning project. So basically we have um a loader where we're loading we're loading batches of data. Um we are calling the model on this batch of data like getting some output then based on this output computing a loss then doing a backward and using this optimizer and optimizer to step um to yeah change the model weights. And finally you probably want to have a look what how the loss is doing. You want to see it going down. So

**[2:33](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=153s)** you print the loss and we often start by writing it this on CPUs um to test and make sure it's working correctly. Then we move it on the GPU and we see that it uh indeed it gets faster but it's not as fast as we expected it to be. Um and Nvidia Nvidia provides this command line um command line tool that you can use NVIDIA SMI and it will show you like the metrics around your like your GPU and you might be somewhere around 50% utilization more or less and it definitely is probably not 100%. And you check different things and you see that well um everything seems to be correct. So what is it what is it that that's happening that's slowing down your code? And the hint is obviously well the synchronization.

**[3:21](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=201s)** [snorts] Good. So that is the familiar training loop. Now I want to take a step back and think about um or explain how the GPU actually is working. So how is the GP the CPU and the GPU collaborating and the the hello hello? I'm back right the GPU is actually a synchronous. So the principle that you need to keep in mind is the CPU is bossing around the GPU and telling it what to do. Um and what we see here is a timeline with GPU and CPU and the CPU is scheduling these operations, these PyTorch operations um to be to be um ceued and executed by the GPU. So you see these are the operations that we had in the loop. zero grad forward loss function backward and step

**[4:12](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=252s)** and it takes a little bit of time for them to be for them to move to the GPU and then start on the GPU and then they since the GPU is the one actually doing the work it takes a longer time each operation takes a longer time on the GPU than it takes it to be just scheduled from the CPU and importantly this means that the CPU finishes scheduling the operations um before the GPU finishes executing the operations. [snorts] And this is a healthy thing. This is this is what you actually want to have. Um and it's also very interesting to see that um the CPU is done like here at this step. It's already finished scheduling. The GPU is still in the middle of the forward pass and hasn't even started to do compute

**[5:01](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=301s)** the loss function backward or optimization step. [snorts] Um, this is why we say or it is said that the CPU runs ahead of the GPU because it finishes earlier. And if you were to naively times time how long it takes the CPU to finish all the operations, then you would be misled to think that it's very fast while the GPU is still working on the actual the getting the actual work done. And the question is so what is a CPU GPU sync? So it happens when the CPU gets blocked and it has to wait for data to come back from the GPU for example when the CPU needs to take a decision based on that data. So here we have an example. So we have in our code

**[5:50](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=350s)** something like if this coded tensor um is larger than zero then do something otherwise do something else right. So the the data resides on the GPU but the CPU needs that information to take the decision. So it has to move this information back and this is another timeline where now I have said let's call them up one up two up three and up one and up two are scheduled normally but up three cannot be scheduled until the CPU um gets this information back from the GPU. So what we see here is that the CPU blocks it has to wait. So all this time here is spent doing nothing. Waiting for the GPU to send information back. Then

**[6:40](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=400s)** it can schedule up three and send it back to the GPU. The GPU will be waiting in the meantime doing nothing. [snorts] So these are the bubbles on both sides of the hardware. On the CPU side you have bubbles. The GPU side you have bubbles. And this is going to slow down your code. So when is it happening in our training loop? It happens precisely here when we want to print the the loss that we currently have. Right? This call to item forces the CPU to fetch that information from the GPU and synchronize. And this is happening on every iteration. So you schedule these five operations or I don't know how many they are. Schedule them, synchronize, schedule them,

**[7:26](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=446s)** synchronize. And one simple fix would be just to say well I synchronize just every 100 iterations. That means these 100 iterations will be just batched batch scheduled executed tightly without bubbles. And um I still want to know my laws sometimes. So I just print it out. There are also um solutions where you as synchronously fetch back the data from the GPU but that's a bit more involved. All right. So let's say uh we understand this these timelines that I showed you but you want to actually see it with real real tooling. So we can use the Nvidia Insight systems profiler and I prepared a snippet of code that's

**[8:18](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=498s)** simpler because it doesn't have the backward pass and the optimization step which complicate the picture. So in this simpler simpler example, it's also a loop but it consists basically of a slow operation and a quick operation and then an optional print which is going to either trigger the synchronization or we leave it out and there is no synchronization. And the uh if you have a uh an Nvidia GPU then you probably have this NS encas command available um which which you can create a profile and this is basically the the program um that we're profiling. It's available on this uh GitHub gist if you want to try it out yourself maybe later today. And what we're going to see this is a screenshot from the ends inside systems

**[9:06](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=546s)** profiler. it it has again two traces. So there is a GPU uh sorry a CPU CPU timeline which is this one and on the top you see a GPU timeline which is the longer one. That's why I put the CPU on the bottom even though it would have made intuitively more sense to put it on the top but um this is just how how it's structured. And I want you to to u notice where you most most striking immediately is that the the CPU timeline is a lot shorter. So it is running ahead. scheduling all these operations uh slow fast slow fast slow fast slow fast scheduling everything quickly and then the GPU starts working on the stuff a bit later and the the slow operation is the yellow one I think you might be able to read it and the quick operation is the blue one

**[9:56](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=596s)** which is shorter and they're operating back to back um here on the top this light blue um bar is the GPU utilization. So you see that it has a little bump here, a little bump here, but in general it's continuous. So you're getting 100% utilization from here until all the way until the end. And this is a healthy run. So this is no synchronization whatsoever. Uh the print statement is disabled. And now if we enable the print statement, we have a synchronization. So this is the case where this is the this is the same screenshot but for the workload with synchronization. And what we see here is again the the the two timelines but the

**[10:46](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=646s)** lower timeline of the CPU is a lot longer and they both end up around the same finish line so to speak. This means the CPU is not really running ahead but rather it's it's being yeah it's being delayed. And here on the bottom you see these green bars which are completely new. And what they say if you can read it it says CUDA stream synchronize. So while this green operation is running your CPU is doing nothing else or your yeah basically that's your waiting time on the CPU. It's waiting for the information to come back from the uh from the GPU. The GPU operations look very similar. So you still have slow operations followed by quick operations but you have these gaps in between. And importantly on the top you see these the utilization has some some gaps there and that's precisely

**[11:37](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=697s)** where the slowdown is coming coming from. Um so you have on the top you have the slowdowns on the bottom you have the green slowdowns and um yeah this workloads this workload becomes like 400 microsconds slower. Um it could be a lot more. Uh this just happens to be a large a lot of matrix multiplications which occupy the the GPU very well. [snorts] Okay. So we say uh we understood this um we want to write fast code. So we're going to avoid some of the idioms that trigger synchronizations. So there is a pietorch performance team docs which has a section about this specifically and it mentions these bullet points over here.

**[12:24](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=744s)** So avoid item calls print and cuda tensors avoid these CPU call don't um put put it in conditionals and I I think once you've seen them it's easy to memorize them and be like okay those are easy to avoid I can do that. But the more interesting part of this talk is that there are more subtle um idioms or patterns that trigger synchronizations as well. And um those are related to dynamic shapes. So let's go through some of these dynamic shapes and understand what's behind them. These operations may look harmless, but they create also synchronizations

**[13:11](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=791s)** without you intending to. Right? So let's start with this one. This is um a case where both T and mask are tensors on the GPU uh torch tensors and this this is basically a boolean indexing, right? So mask is an indexing. You're selecting a subset of the of the tensor. Um it's it's I think it's a very common operation. You do it in numpy. You do it in torch. This is very very very common. The problem here is that the the length of X, how large X is, will depend on how many TRS there is on the GPU side, on the data that's living on the GPU side. [snorts] A very similar a very similar pattern is this one. This is slicing. So if K is

**[14:02](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=842s)** just an integer that's living on the GPU, let's say 10 20, it doesn't really matter. and um you slice another torch tensor with it. This would be like selecting the first 20 20 elements of this tensor then um the CPU will also not know how long the the resulting tensor will be um without fetching that information back from the GPU [snorts] and and more more more um torch APIs um have the same problem. So this is nonzero. What it does is it gives you the the indices of non-zero values. And how many non-zero values is there are there in a tensor? Well, that depends on the data. Um the same with unique. This is like calling set on a list in Python.

**[14:50](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=890s)** So how many unique numbers are there in a tensor? Well, that depends on the tensor and its in its data. So what they all have in common is that they synchronize because Python PyTorch needs to allocate this output tensor X X and it needs to know the shape in advance and if this shape depends on GPU data the CPU must be must ask the GPU and if you think about back about this boss and this relationship of boss the CPU is the boss but if the the CPU needs to ask the GPU then it's not the boss anymore. So you're having this inversion of the who's the boss in the in in in that usually usually both have this is basically what I mentioned um

**[15:40](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=940s)** before. So uh rule of thumb for you or mental model should be if the if your tensor has a static shape that is known in advance then you can you can have a sync operations on it. If it definitely has a dynamic shape then it's likely that you will have uh some operation that is uh triggers a synchronization. [snorts] It's um there are ways to fix to fix this this issue with dynamic shapes. So for example this this function from torch called repeat interleaf it has an optional parameter that you can pass that tells torch how large the output will be so you tell it the output size is total this can be an integer let's

**[16:28](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=988s)** say 10 20 and then um since torch doesn't have to ask the GPU anymore for the size it can allocate this uh without a synchronization and the code runs through without synchronization while the this this idiom does trigger a synchronization. So the so torch gives you some tools to work around this um and avoid the synchronizations. Yeah. So you try to use the APIs um to that that allow you to pass the the output size. um these these um this variable saying like what is the total size should definitely not be residing on the GPU. So keep that on the CPU side otherwise you will have a

**[17:14](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1034s)** synchronization again. Um and the padding is also a solution. So you which I I didn't so I'm not going to delve into that a lot but you can use padding to avoid dynamic dynamic shapes [snorts] and uh yeah finally let's let's talk about unit testing. So we saw that um that you can see the synchronizations with a profiler that you will see these long calls calling called uh CUDA stream synchronize. But do you need to do this every time just to to to identify a synchronization? The answer is no. There are tools to do this quicker without having to spin up a profiling. And for that um PyTorch offers an

**[18:03](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1083s)** experimental debug mode that flags every synchronization in your code. So how it looks like is is like this um torch.ca set synchronized debugging mode and you can set it to warning such that if you take a CUDA tensor and you trigger any type of synchronization on it, it will raise a warning for you. So you you can activate this run your code and if you see a warning then you know well there's something there's something uh there's some synchronization somewhere you can set it to a strict mode with error by passing error and then this same this same pattern will actually raise an exception and that is actually quite useful

**[18:52](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1132s)** because then you can uh use this pattern in unit tests. So what you can do here what you see in this case is a it's a unit test that is loading some inputs and then passing those inputs to something called my PyTorch function. It can be really anything. It could be your model. It could be some function that you wrote yourself and then there is some correctness check and what I have done here is to add a decorator that says fail on GPU sync. So this unit test will fail if my PyTorch function has a synchronization. And what's happening under the hood? Yes, is there's this decorator. I before calling the function I set it I set the debug mode to error such that it

**[19:42](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1182s)** raises an exception on the function and afterwards you deactivate it again. And the cool thing is that you're not touching the you're not touching this function under test. Uh you're only modifying test unit testing code. So the production code stays clean of this experimental API. And um you can test also code that is coming from a library, right? Or that is not your own code. You can still test it for synchronizations without modifying it at all. [snorts] Yeah. So the takeaways from this talk are the asynchronous mode is the default for for operations launched on the GPU. The CPU is supposed to run ahead. That's

**[20:29](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1229s)** healthy. The GPU is supposed to stay busy with work. A synchronization is when you are blocking the CPU while it waits for the GPU. Inverting this bossy relationship between both. And there are some really clear obvious triggers that you should easily remember like item print CPU if else branching. And there are more subtle triggers that you might have to reason about with dynamic shapes. Um and there are obviously solutions to that which the optional parameters that I showed but also padding or just you can still sync. It's fine. The world is not going to end by syncing. Um but you can do it just less often. And finally, obviously, if you want to unit test um your code for it, you can do so. And uh

**[21:18](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1278s)** PyTorch provides the APIs to to test this on your own code. That's it. Thank you. Thank you very much. [applause] [applause] Thank you very much for your presentation. Uh now we have some questions for you from our audience. Um one of them is how much of an issue is these on unified memory architectures such as Nvidia GB200 or Apple M series? >> Uh that's a very good question. So my understanding is that the in unified in unified memory you supposedly don't care anymore where where these tensors are.

**[22:09](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1329s)** Um, but I haven't actually gotten my hands on one of these systems to be able to tell uh how how how much of an issue it is. I assume it's less of an issue, but if you have one of these machines, reach out to me. [laughter] >> Thank you very much. Uh, do tools such as Tensorboard sometimes introduce an expectant synchronization? >> Um, good question. So I haven't looked at the code of uh tensorboard. My understanding is that they are very much aware of this and they um fetch these they fetch the those so they do this async solution basically where they are moving the memory asynchronously from the GPU to the CPU. Um but I'm I'm not sure I would assume they do. So um yeah

**[23:01](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1381s)** it it would be it would make sense. So you don't you're not synchronizing on the hot loop of the training. >> Okay. Thank you. Uh why does the CPU need to know the sizes if the resulting tensors are created slash continue to live in the on the GPU? >> Yeah, that's a that's a good question. Um I don't know the short question is I I don't know why it necessarily needs to know the shapes. Um, and why if you just tell it the shape, it can just go merily forward. Um, so that's a good question. I don't know. I would would be necessary to look into the into the the maybe the memory allocator or something like this.

**[23:50](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1430s)** >> GPUs. >> Yeah. Yeah, agreed. >> Thank you. Uh, do you need to run the unit test with your wrapper on a Nvidia GPU to detect the syncs or can will PyTorch also raise an error on CPU? >> I haven't tried on the CPU. Um, interesting question. Um, I'm not sure if the the concept of a synchronization even exists if you're running entirely on CPU. I I don't think so. So, so probably it won't do anything. >> Okay. One more. Is synchronization also

**[24:40](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1480s)** a problem in for example ONX models? Would Nvidia and site also work in this case? ONX. >> Mhm. >> I'm not familiar with the ONX ONX runtime. So, um I don't know. I don't know much about it. Sorry. >> Okay. Thanks. [laughter] Uh do all dynamic result operators have allocation hints or are there known exceptions? This is um so I I talked about this um repeat leaf and this is I would say one of the few functions that offers this this output size optional parameter. Um

**[25:28](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1528s)** let's have a look at the rest. I I don't think the others have this but um it's up to I mean the documentation is there and you can look it up and then um try to select always the the API that offers you this uh the p to pass uh the output output sizes. [snorts] >> Thank you. Uh the last question is do you need do we need CUDA and PyTorch versioning? In PyTorch what >> versioning? >> Do we need CUDA in PyTorch versioning >> and and CUDA and PyTorch versioning? >> Uh yeah. So this was entirely tested on CUDA devices. So GPU devices. I haven't tested it on other GPUs like MD or

**[26:18](https://www.youtube.com/watch?v=dKZxUcuOb8A&t=1578s)** whatever. But um I I expect similar similar problems uh if the devices are separate. So yeah. >> Okay. Thank you very much. Thank you for presentation and answers. [applause]
