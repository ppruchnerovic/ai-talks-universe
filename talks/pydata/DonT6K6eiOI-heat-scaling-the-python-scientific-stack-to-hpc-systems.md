---
id: DonT6K6eiOI
title: "Heat: scaling the Python scientific stack to HPC systems [PyCon DE & PyData 2026]"
slug: heat-scaling-the-python-scientific-stack-to-hpc-systems
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Claudia Comito"]
channel: null
duration_min: 30
published_at: 2026-08-04T22:21:05Z
video_id: DonT6K6eiOI
url: https://www.youtube.com/watch?v=DonT6K6eiOI
youtube_url: https://www.youtube.com/watch?v=DonT6K6eiOI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Inference, serving & GPU infra"]
transcript: true
---

# Heat: scaling the Python scientific stack to HPC systems [PyCon DE & PyData 2026]

**Claudia Comito**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=DonT6K6eiOI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Claudia Comito and Thomas Saupe explain how Heat breaks the "memory wall" by scaling the Python scientific stack across multi-node, multi-GPU HPC systems.

Speakers:
Claudia Comito, Thomas Saupe

Description:
HEAT is an open-source Python library designed to scale scientific data analysis from local workstations to high-performance computing (HPC) systems. It addresses the memory and compute limitations of NumPy, which is restricted to shared-memory parallelization on CPUs. By mirroring the NumPy API, HEAT allows users to develop code on a laptop and deploy it on large-scale clusters, such as the Jupyter system with 6,000 compute nodes, without significant code modification.

The library introduces the DND (distributed n-dimensional) array, which distributes data along a single axis across multiple MPI ranks. Under the hood, HEAT leverages PyTorch for local tensor operations and device acceleration, supporting CPUs and GPUs (including NVIDIA and Apple MPS), while using MPI4Py for inter-node communication. A key technical advantage of HEAT is its implementation of complex linear algebra functions that are difficult to parallelize, such as QR factorization, distributed Singular Value Decomposition (SVD), and Dynamic Mode Decomposition (DMD).

Performance benchmarks demonstrate that HEAT provides significant speedups over serial NumPy and scikit-learn baselines, particularly for large matrices where GPU acceleration is utilized. In weak scaling tests, HEAT maintains a flat memory footprint per compute node, whereas alternatives like Dask show increasing memory consumption as the number of nodes grows. This memory efficiency enables the processing of datasets that exceed the memory capacity of a single GPU or node. The library effectively combines shared-memory parallelization via PyTorch with distributed-memory parallelization via MPI to maximize HPC resource utilization.

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

*4,666 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=DonT6K6eiOI&t=5s)** and also thank you for being here at this late time. Um, so yeah, I'm going to present heat which is a Python library for distributed data analysis. It's an open source code that's developed uh at Fortune Central Mulich and KIT in Kazour. Uh so let's start with a bit of a motivational slide where we have some pretty pictures of people doing science with data like they they somehow analyze some data and a lot of the time when you do that you use like numpy or the related libraries to do that and for very good reason because they're very robust. Uh they they work we know how to use them at this point. Uh but there's one fundamental limitation of NumPy and the related uh libraries which is that they're limited

**[0:53](https://www.youtube.com/watch?v=DonT6K6eiOI&t=53s)** to shared memory uh parallelization and CPUs and that's unfortunately not really the landscape of uh the compute resources that we have these days. Um so maybe if you want to do some data analysis you start coding on your code on your laptop. Um and this has a few gigabytes of memory and a few CPU cores. Um but this is really limiting in the size of data that you can process in the end uh because you need to fit your data into memory and then you also need to have the patience uh until all of the data is processed. So you want to use some larger compute resources. Maybe you have a big workstation available um or access to some high performance computing system um and then if you have written code in

**[1:41](https://www.youtube.com/watch?v=DonT6K6eiOI&t=101s)** numpy then this will give you access to maybe a single node of the HPC system um which will maybe 10x the amount of memory that you have available um and the CPU cores um but maybe this already has some GPUs that you then can't leverage with your numpy code. Um, and like we we now have a new system in Uli called Jupiter. This is not actually an image of Jupiter to be honest. It's not very photogenic. It's in some containers. Uh, so this is some old I think at this point decommissioned CPU system. Uh, but it is a system that has once been in UI. Um, this like the the new Jupiter system. Anyways, uh, I'm getting a bit sidetracked. there's like

**[2:29](https://www.youtube.com/watch?v=DonT6K6eiOI&t=149s)** 6,000 compute nodes. So if you could scale to all of them, you could increase the size of data set that you can process by uh orders of magnitude. Um but you need the software to scale there. And this is sort of the point of heat. Uh let's try again. Okay. So the point of heat is to work very similar to numpy like we try to mirror the numpy API as much as possible and then you code on your laptop works fine uh but then you just go to the big system and it still works um but now you can process large data sets and it does that by distributing uh the data so

**[3:18](https://www.youtube.com/watch?v=DonT6K6eiOI&t=198s)** here's an example of a 3D data set and the three different ways that heat can distribute this data uh because it only supports distribution ution along one axis. Um but yeah, hopefully this uh this will work. Uh before we talk a bit more about the details of heat, I want to mention that there is a lot of similar libraries available. So you probably heard this uh pitch before like give us your numpy code and we make it fast and distributed and GPU and everything. Um, and it's not like heat is fundamentally better than any of these in in some amazing way. Uh but I think all of these libraries have a few advantages and disadvantages like in the feature set that they support and in

**[4:07](https://www.youtube.com/watch?v=DonT6K6eiOI&t=247s)** their API like they are a little bit different now than what you're used to from numpy or uh they don't support all of the operations in a distributed fashion because some some of them really uh are not trivial to parallelize and I think this is where uh heat does have some selling points because uh it implements a lot of these linear algebra functions that are not trivial to parallelize. Um, and maybe this is now the best fit for you, but maybe not. So, uh, feel free to to check it out and see what's available. And by the way, if at any point you are convinced that this is something that you maybe want to try out, uh, this QR code that's, uh, almost always there will lead you to the GitHub repository. Um, all right. So now let's uh look a

**[4:56](https://www.youtube.com/watch?v=DonT6K6eiOI&t=296s)** bit under the hood and see how it works. Um I took a simple screenshot of a little interactive session that I ran on my laptop to illustrate the very core concept of heat which is the DND array the distributed n-dimensional array that's kind of the equivalent of the numpy array. So first let's start with writing some numpy code right. So we uh oh you can't see my cursor well. [laughter] So we import numpy as we normally do and then we define some numpy data. Um and now this is what we want to accelerate with heat. So we import heat instead and then we call exactly the same function on heat with some additional heat specific arguments.

**[5:45](https://www.youtube.com/watch?v=DonT6K6eiOI&t=345s)** Um what does this give us? First of all, it gives us the same data and we can use this heat dnd array pretty much the same way as we would the numpy array. So most of of our favorite numpy functions have a heat equivalent that we can just plug this into uh and we're good to go basically. But let's look at the additional arguments. So we have split equals zero here. The split tells heat how you want to distribute the data. uh earlier we've seen this 3D data where we had three options for distributing plus no distribution I guess this is uh 1D data so there's only one way of distributing that uh along the first axis and this is how you do that very simple um and then the second argument that numpy also doesn't have is the device uh here I use

**[6:34](https://www.youtube.com/watch?v=DonT6K6eiOI&t=394s)** MPS which is somehow the accelerator in my laptop uh heat says this is a GPU um whatever Um and then there's some additional information regarding the parallelization. Uh so we have MPI rank zero and a local shape which in this case is equal to the global shape because I execute this in serial. But uh if I ran this with multiple tasks then uh we would have multiple NPI ranks and smaller local shape than the global shape of course. Um now what's happening underneath? Uh we can check out the local data on the task by just looking at L array. So local array um and this is just a torch tensor actually. So heat is uh built on torch. Uh of course we don't reimplement

**[7:24](https://www.youtube.com/watch?v=DonT6K6eiOI&t=444s)** all of the things like whenever we call a serial operation we just pass this onto torch uh which also supports all the devices. So that's good. Um another heatsp specific attribute of the DND array is the communicator.com. Um we have some abstraction around communicators. So this could be different parallelization uh frameworks but for now uh it's just a wrapped MPI for pi MPI communicator um which works on a lot of machines I think. So the the DND array is really a torch tensor which supports all kinds of devices and they have of course good implementations for serial operations which we can just leverage in uh in heat plus the MPI for PI communicator which I

**[8:14](https://www.youtube.com/watch?v=DonT6K6eiOI&t=494s)** can use to parallelize on my laptop and also on big machines like Jupiter. So it really uh runs on a lot of machines. Um, and it has a numpy like interface which should make it very easy for you to get going if you're familiar with numpy. Uh, let's look now at a parallel example. So I I executed this script uh with four tasks. Now we first define some data again. So we just call heat a range uh with 16 elements. Now uh here we we haven't passed a split argument. So we define the same data on all tasks. Um then we call a reshape operation which we're familiar with from numpy as well. And then we call a heat specific function called re-plit. Um and this

**[9:03](https://www.youtube.com/watch?v=DonT6K6eiOI&t=543s)** just changes the distribution. Uh it's kind of a dangerous function maybe because this will do a lot of communication underneath and depending on the data set you might run out of memory if you like transpose it. Um but anyways, if you want to change the distribution, it's really very easy. Um now we can print what we got. Uh and you'll notice it looks quite pretty, right? So it's a single output on the first rank. There's no matching uh the output to MPI rank and print statement because the order is uh unexpected. Um so this should also make it easy to develop the code for people who uh are maybe not experts in parallelization. Um like our target audience is really

**[9:50](https://www.youtube.com/watch?v=DonT6K6eiOI&t=590s)** people who who are experts on analyzing the data and not necessarily uh on parallel computing. But of course we can uh take a look under the hood and print for instance the rank of the communicator that's associated with the array uh and the local data. Um and then we see how the distribution works. So we actually have only a patch of the data on each task. Uh and again this is just torch tensor. Um now I wrote here the distribution behaves sely across operations. So maybe the distribution changes if you sum along the distributed axis. For instance, this axis is uh gone afterwards. And how should this be distributed? Probably it shouldn't be.

**[10:37](https://www.youtube.com/watch?v=DonT6K6eiOI&t=637s)** And this is exactly what happens in heat. Uh if on the other hand you sum along the non-distributed axis, you would expect it to still be distributed. Um and that's what heat does, right? So ideally you don't have to worry. That's uh that's the point. Um okay, so so far if you're familiar with a bit of NPI, this seemed very trivial. [snorts] Um but really the selling point of heat is that it uh implements functions that are not trivial to parallelize. uh and I thought a good example maybe is QR factorization. Um so here we we take some matrix and we factoriize this in a orthogonal matrix Q and an other triangular matrix R um which we can multiply together to recover the original matrix. Um and now in this example we we start again by defining

**[11:27](https://www.youtube.com/watch?v=DonT6K6eiOI&t=687s)** some data um which is split along the first axis and then we just call the functions just like a numpy and it will give us this these matrices and they're all split also along axis zero. Um so if you if you have some code and you want to distribute it you have to distribute really when you define the data or when you load the data right like in pract in practice if you are doing some data analysis you will load data and during the load step you you just say split along this axis and then heat will just continue distributing along this axis uh and also it will maintain the the device. Okay. Now let's look at some actual parallel scaling results because this is of course uh the important thing like is

**[12:15](https://www.youtube.com/watch?v=DonT6K6eiOI&t=735s)** it at all faster and we start with a very basic operation uh which is matrix multiplication. Um I show here what you have to communicate with a simple example on top which is multiplication of two 2x2 matrices um which are split along the first axis. So the color denotes which element uh or which task the element started out on. And then in the result you will see in the first line some blue things which we had to communicate from the second task and in the second line some red things which we had to communicate from the first task. So there's a lot of like fine grain communication going on in matrix multiplication. Uh but even though we have to communicate a lot we still get uh some decent speed up with heat. Uh so I did here some like weak scaling strong

**[13:03](https://www.youtube.com/watch?v=DonT6K6eiOI&t=783s)** scaling combination um runs first of all on on CPU. Uh I have here the numpy baseline that is this black dashed line. Um and then the blue line is heat with one CPU. We see for tiny matrices we have some overhead in the heat library. But for large matrices, we essentially spend all of the time in torch matrix multiplication, which uh is very similar to numpy matrix multiplication performance-wise in in this test. Um but then heat allows us to also distribute this. Um then this yellow line is heat on two tasks. Now we see for tiny matrices we have just some communication overhead that is not worth doing. But that's not what heat is about. It's about uh

**[13:51](https://www.youtube.com/watch?v=DonT6K6eiOI&t=831s)** processing larger data. Uh and pretty soon we cross over the serial line and then we're faster than uh than serial and then yeah here we we increase the number of tasks and we gain even more speed up. Uh this is the largest example that I had the patience to run with numpy. And so for this uh example, I show the speedup plot on the right um where the blue dots are like reasonably close to the ideal line, I think. Uh but of course there's also the dots which are like 100x speedups which is GPU, right? Because we uh we base it on PyTorch rather than numpy. Uh we can just do it on GPU and that's really much faster. Uh so again for like tiny matrices the GPU is not better but

**[14:40](https://www.youtube.com/watch?v=DonT6K6eiOI&t=880s)** pretty soon there's a crossover point where then the GPU is faster than CPU u multiGPU uh it like you now need to do more compute um to to gain something by distribution on multiGPU but also here we we eventually have a crossover point where uh heat with multiGPU is faster than PyTorch uh with single GPU Um okay but a very important metric is also the memory consumption right because you need to fit the data set into memory. Uh so here I have a different uh weak scaling test that I didn't record myself. Uh so let's look at the top plot first which is again time and we see if we increase the number of GPUs we we have

**[15:29](https://www.youtube.com/watch?v=DonT6K6eiOI&t=929s)** increased the data size uh even more so that we expect it [snorts] to to be slower uh if we increase the the number of GPUs which is maybe not ideal for a weak scaling test but anyways that's that's the test we ran here uh and we we tested different combinations of split matrices right you can have different split in in both matrices that you multiply and you get different results. But anyways, if you split for instance both along x is zero, it's fine. Uh the this top dash dotted line is the projection on a single GPU and the dashed line is the ideal speed up that we expect and we're somehow in the middle. Uh so okay, timing could maybe be better. Um but yeah, like if you if you've done some GPU programming, you

**[16:16](https://www.youtube.com/watch?v=DonT6K6eiOI&t=976s)** know that the single GPU memory limit is really can be very annoying, right? Um and at some point you need to distribute regardless of whether you you gain uh time or not, like time speed up or not. Uh and the the maximum memory consumption per GPU that we measured during these runs is on the bottom plot here. Again the like projected single GPU memory usage is the dash dotted line which goes up a lot very fast and then the sort of ideal memory consumption is the dashed line and now going from single GPU to multiGPU we need a lot more memory from uh on each GPU because like we we do the communication and then we have some additional data from other tasks now on the GPU. Uh but once we are multiGPU it

**[17:05](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1025s)** scales pretty well. Um and this allows us to fit a lot larger matrices. Um yeah good. All right. So now also the QR factorization we looked at earlier I recorded very similar scaling results uh or scaling tests for this and the the result is similar like the speed up is a bit worse but that's not very surprising considering you need to do additional computation also in this parallel QR factorization because um because of the algorithm um but you you do get speed up which I think is Good. Uh and then we also have a very similar test with memory consumption. And here uh again going

**[17:53](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1073s)** from single GPU to multiGPU we do like we need a lot more memory but once we're there uh we're pretty flat. So that's good. Uh and we could factoriize even larger matrices still. And also here on on the top uh plot there's not different splits of the input matrix but both are somewhere between the ideal scaling and and the worst scaling. And yeah I think this this doesn't look too bad. Uh okay so a very nice feature of heat is also the distributed singular value decomposition um or principal component analysis. Um here I I have an illustration from the paper that describes the algorithm that we implement in heat also on the right uh which describes the algorithm a

**[18:40](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1120s)** little bit. So we we split the matrix along tasks then we perform the local singular value de composition and then we we merge the local uh SVDs and compute an SVD on the merge matrix um which is somehow faster because we can exploit some structure there. uh but because we we need to merge this data um you know we we cannot communicate everything because then we run out of memory. So typically we limit the rank of of these matrices. I should mention that uh this is kind of a simplified version where you you merge all of them on on a single task but there's also a tree version of this which is better. Uh and I think in heat we also implement the tree version. So uh you don't have to truncate uh at super small matrices.

**[19:32](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1172s)** Um but these these beta plots here on the left they are now for different truncation rank. I know this might be a bit small but um here the left plot is very small truncation for rank five. Uh and this is larger truncation with 500 ranks. Um now we we test against scikitlearn that is the uh the baseline here. um on a single compute node like this is now a hybrid parallelization with uh shared memory in PyTorch and distributed memory in heat. Um and yeah so the single node compute node uh baseline is scikitlearn here the green line. Um then these three lines these are heat with different number of tasks uh per compute node and then yeah

**[20:22](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1222s)** x-axis is number of compute nodes and we we see for for low rank this scales really quite well. Uh this is GPU which is again much faster and also scales decently well. Uh if we maintain a larger rank then we have to communicate more so the scaling is a bit worse. Uh but still we get pretty decent speed up over the serial baseline here. uh which is not bad. Okay, heat also supports uh dynamic mode decomposition which is uh kind of a funny algorithm I think. So you uh you look at a time series basically and you you say uh the next time point is related to the previous time point by a matrix multiplication.

**[21:10](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1270s)** Um and then you try to approximate this matrix using this dynamic mode decomposition. And then here are some uh scaling results for heat um when doing this in parallel. So the strong scaling is actually quite poor. I will admit that. Uh but the weak scaling uh this looks decent I think. Um like these are the the fitting stages. uh the fit stage is the approximation of this a matrix and then the predict stage is to uh like guess the next point in the time series I guess if you want uh but regarding memory consumption it scales pretty well and like again you you kind of need both you need uh short time um and low memory consumption

**[21:58](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1318s)** uh so here we have also a comparison with a Dask implementation uh there's a paper last here written by one of our unfortunately former collaborators at this point uh which has a lot more detail on this. So I have to speed up a bit now and I suggest if you're interested to to read the paper uh but I will very briefly highlight a few things. So loading data with Dask it uh keeps taking longer and that's bad because eventually you will run out of time whereas heat nice and flat. Um and then for most of these operations, heat on GPUs uh is faster than task uh which is limited to CPUs. Um in these tests uh very important also the memory

**[22:48](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1368s)** footprint where we see the same thing as in in the time to load data. So this is here the average memory per compute node and the x-axis is number of nodes and if the average memory goes up with a number of nodes at some point we hit the limit uh of every node and this is exactly what happens with dask like here we're at like 300 gigabytes already which uh like the typical node has not a lot more I would say uh heat on the other hand is nice and flat once we reach a full node. So um here you you could continue to scale further with heat uh but with dask maybe not so much. Um all right and then seems that was fast enough. So,

**[23:35](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1415s)** uh, to to summarize, heat is supposed to be a sort of plug-in back end for for numpy code, right? Like I I'm supposed to avoid the phrase porting code to heat, but uh because that sounds scary. So, you're you're supposed to use heat as a back end for your numpy code. Uh, and it makes it very easy to distribute the code. Um, and also to make use of accelerators. Uh and we really we have to do that because that's the compute power that we have. We we have no choice but to do this. Um if you're interested in heat uh reach out to us again, scan the QR code for the GitHub repository. If you're looking for a feature that is missing, open an issue. If you're just interested in anything such as is heat the right code for you, uh open a

**[24:25](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1465s)** discussion maybe. I think discussions are a good feature for that. Uh and our development really is userdriven like we we recently uh published version 1.8 where we added a few missing numpy things uh that some users requested and yeah we're happy to to help you out if you want. Thank you. [applause] Oh that's nice photo. Thank you Thomas for this excellent talk. Um, quick reminder, you can ask questions on talks.pyon.de as well as upload existing questions so they're more likely to be asked. And we already have the first question. Is heat compatible for all types Nvidia GPUs or is there any limitation in terms

**[25:17](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1517s)** of hardware? Uh well to be honest I'm not 100% sure but essentially we just use PyTorch uh for for all of these operations. So my impression is that PyTorch support a lot of devices that you would normally use. Uh there probably are some niche GPUs maybe that it doesn't support but uh like again it even supports the the accelerator in my laptop. So, uh, my guess is probably it does support the GPU that you're looking for. >> Uh, the next question is, um, what kind of inter node connection did you have for your benchmarks? >> Uh, I used

**[26:05](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1565s)** two different machines actually. Uh so I I can't speak to these these memory benchmarks unfortunately because I didn't record them. Uh they were on on a DLR machine actually and I I assume they use some infinity band connection uh because that seems to be very popular in uh in the machines that I work on anyways. Uh but here I used um for the GPU tests the Jules booster machine. Uh actually I used only a single node. So these are connected with NVLink uh which is quite fast. Um and for the CPU tests uh I I used a very like it's a smallish machine called Yuf and this is connected with some infinity band connection. Uh yeah I I hope that answers the the

**[26:55](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1615s)** question sufficiently. And the next question a little bit confrontational um also refers to the beginning of your talk. Uh chunked distributed ND arrays have been attempted multiple times. Tusk Zar Blask Blask 2 cubed. What is heat better at? >> Yeah. Uh so first of all I have to admit that I'm pretty new to the heat development team and so I don't have a lot of experience with the competitors. uh but I think at the end of the day it really boils down to which features are implemented in the library that that you might want. So again the the selling point from from my point of view of heat is really uh if you are looking for a parallel implementation of some linear algebra that's not very easy to do.

**[27:44](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1664s)** Maybe heat uh has implemented this and if so then that's great. uh and also the the numpy like interface of heat is uh good like I know many other libraries also have that uh and I'm not going to say that heat is better than them um but I think there there's a niche of people that maybe are not uh coding experts and they maybe don't have access to to a lot of stuff and then maybe we can take care of them. We take the time. [laughter] Uh and maybe what they're looking for is already implemented in heat, but uh yeah, I mean there's there's plenty of competition and I'm not going to tell you that heat is better than the

**[28:30](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1710s)** competition. Uh maybe it's right for you, maybe it isn't. Uh but feel free to try it out. >> Exactly. Try it. The next question is which limitations have you faced uh with data or projects using heat? Uh yeah, unfortunately like I I really haven't because I'm I'm too new in the development team, I guess. Uh so I unfortunately I can't really answer that question. I'm sorry. [snorts] Last question. Have you considered adding implementing an X array back end? A lot of scientists prefer labeled data. >> Uh I don't think that's going to come

**[29:20](https://www.youtube.com/watch?v=DonT6K6eiOI&t=1760s)** anytime soon. Um I can only speculate but I I haven't heard that in any internal discussion. So I don't I wouldn't hold my breath uh for that I guess. >> Great. Thank you Thomas again for your wonderful talk. Check out the project. Thank you all. [applause]
