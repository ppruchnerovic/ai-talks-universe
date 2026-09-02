---
id: 6yQmEvqMDCQ
title: "Metashade: Compilerless Immediate-Mode Shader Generation in Pure Python [PyCon DE & PyData 2026]"
slug: metashade-compilerless-immediate-mode-shader-generation-in
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Pavlo Penenko"]
channel: "PyData"
duration_min: 27
published_at: 2026-08-04T22:20:28Z
video_id: 6yQmEvqMDCQ
url: https://www.youtube.com/watch?v=6yQmEvqMDCQ
youtube_url: https://www.youtube.com/watch?v=6yQmEvqMDCQ
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Metashade: Compilerless Immediate-Mode Shader Generation in Pure Python [PyCon DE & PyData 2026]

**Pavlo Penenko**

`PyData` · `PyData` · `2026` · `27 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=6yQmEvqMDCQ) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Pavlo Penenko demonstrate how to leverage Python metaprogramming to build a compilerless GPU shader generator using pure Python.

Speakers:
Pavlo Penenko

Description:
Metashade addresses the challenges of shader programming, specifically portability across different rendering APIs, the permutation explosion in real-time shading, and the lack of high-level abstractions and modularity in C-like shading languages. While existing solutions like Warp or Taichi use introspection to capture Python's Abstract Syntax Tree (AST) and compile it via C++ backends, Metashade avoids the compiler approach entirely.

The system utilizes a tracing mechanism and immediate-mode code generation. Rather than parsing the AST, Metashade emits target code eagerly as Python code executes. This allows for the interleaving of arbitrary Python logic with shader generation, enabling powerful metaprogramming. A central polymorphic generator object manages the semantic model of the shader, tracking scopes and local variables to ensure semantic correctness without relying on simple string concatenation.

To emulate C-like semantics within Python, Metashade employs specific architectural patterns. It captures symbols by treating meta-variables as members of the generator, which enforces static typing and value-based assignment. Operator overloading is used to implement an expression builder pattern, allowing the system to enforce stricter type safety than the target language—such as prohibiting the addition of a color and a point. C-like scopes are emulated using Python context managers.

Metashade supports multiple targets, including HLSL and GLSL, and integrates with the MaterialX standard for physically based rendering (PBR). By moving design-time decisions to Python, it replaces complex C preprocessor macros with readable, maintainable Python code. This approach improves debuggability, as semantic errors trigger Python exceptions that can be analyzed with standard Python debuggers.

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

*3,623 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=6s)** Let me rephrase maybe the title a little bit. So I'm going to speak about Python hacks that uh make it possible to write uh shader generator without writing a compiler. I'm going to use my open source project Metashade as as an example of implementation. But first the fun part, the disclaimer. Uh I work at Autodesk and uh I'm obliged to say that I'm here in my personal capacity and uh the views expressed are my own and not those of Autodesk and the uh information presented here does not nec necessarily represent the views of Autodesk or its partners. Uh and now on a slightly less professional note, uh one of my favorite memes, what's a shader? So basically

**[0:55](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=55s)** there are well two intuitive uh definitions of a shader. On the one hand, it's a program that's used in um in a rendering pipeline to eventually compute the the value of a of a pixel either at real time or in um uh offline uh rendering. On the other hand, a shader is something that's executed on a GPU. So the the uh top left cell is probably the uh the most famous example of a shader. So a fragment shader or a pixel shader that executes on a GPU in a video game. Uh but then uh Open CL or CUDA for that matter. Uh they're also well executed on the same hardware and uh well the difference the only

**[1:45](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=105s)** difference here is that they they're typically not used for rendering. So in some way uh there they're shaders and there's definitely some overlap here and we can reuse some techniques between shaders and kernels and on the other hand there's there but in in reality uh while a good example would be CPU shaders uh written for uh production path tracers like Arnold or Renderman. They've traditionally been run on CPUs and but these days they're ported to GPUs as well. Uh and well before we um so why would anyone would want to write shaders in Python? Uh aren't there good enough tools for that? Is the the area of shader programming hard? So I I

**[2:34](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=154s)** I I would I would claim that these are uh some major challenges that are present there and they don't actually have very good solutions to this day. So, uh, challenge number one is portability. This, this is pretty self-explanatory. Uh, well, if a game studio develops a a game which needs to run on a console, on PC, on uh on uh on a Mac, on a mo mobile device, there are differences between uh the uh rendering APIs and the shading languages that are supported on on on those APIs. But uh going beyond that there there are sometimes uh portability requirements between real-time shading and offline shading. So for example uh virtual production is is becoming

**[3:21](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=201s)** popular in v visual effects pipelines. For example, the Mandalorian was filmed with huge LED screens behind characters so that they cast realistic lighting onto the characters and those LED panels were driven by were driven by Unreal Engine. So you ideally should have a shader that looks similar in a game engine and a and a production rate tracer used for for the same show. Uh and uh lastly, it's not only the rendering pipelines uh uh the graphics uh sorry the graphics uh uh platforms or shading languages that are important. The applications themselves require certain API for developing shaders for them. So for example, well Maya uh expects one uh API and Unreal Engine

**[4:10](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=250s)** expects another and ideally you should be able to accommodate these uh uh existing APIs. Uh then another big one and uh this one is uh unique to realtime shading is the permutation explosion. Some of you uh may recognize this infamous UI element from Unreal Engine. Uh compiling shaders that well when when you you you often need to wait for many minutes or maybe maybe even hours uh when the level compiles. So what is happening there? Do shader writers really write thousands of shaders? Of course not. So they they do write they do create some materials either by coding or in the visual

**[4:58](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=298s)** editor. But then the engine has to create uh a lot of permutations of those shaders because in real time shading uh those permutations depend on a number of uh conditions. Uh what kind of material is is mapped onto a surface? What kind of geometry is there? What kind of vertex inputs it provides? and what kind of lights apply to uh the surface. Uh and it's important to note that this is fundamentally a design time problem. So these are not runtime conditions. These are not if statements in the shader. Uh these conditions that they're evaluated in as part of the shader uh pipeline. So uh and all all of all all of these permutations they need to be baked in in separate pieces of in in separate

**[5:48](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=348s)** shaders. Uh next up low level of abstraction. So uh a majority of of the shading languages are very C like they don't actually introduce much on top of C. So on on in the CPU programming world a lot has changed since C was a thing. uh um so uh but not not so much in in in shaders. So for example, the lack of generic programming is very notable uh taking into account the this permutation explosion problem. And finally, uh, modularity and code reuse. Uh, certain languages and ecosystems lack the most basic features like linking it pretty much is not

**[6:37](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=397s)** non-existent for uh, well, JLSL or HLSL. Uh, even includes are not part of the JLS specification. And there is no uh, as I as I like to to to term it, there's no STL for shaders. and STL is the standard template li library uh for C++. I just as a C++ developer I remember the days before C uh before the STL be became widespread. It was pretty much impossible to write generic algorithms in C++ and I I would claim that this is the the uh status quo in the world of shader uh uh programming these days. Uh so how do I know that these are the pain points and that the struggle is real? Uh so I worked with with shaders from different angles

**[7:26](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=446s)** throughout a couple of decades. I worked for about a decade in in game development. I uh worked on some VR projects at AMD on uh an animation pipeline at Tunebox. Uh uh and uh well most recently I've been working in the DCC area. So DCC stands for digital content creation. It's applications like Maya uh Max uh and so on and so forth. Right now uh I work at Autodesk working uh on shared visualization tech shared between our products and that involves a lot of open source too such as material X and uh Hydra/ OpenUSD. And I have to confess that I'm most mostly um uh C++ programmer by day but Python is really uh essential in in the visual

**[8:15](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=495s)** effects industry that uh we serve. Uh so what are the existing solutions to uh those pain points? So, first of all, the C pre-processor and uh uh uh if you're familiar with C, I I guess you would agree that this is kind of an evil, sometimes a necessary evil, but in the shader programming world, it's even more pervasive than in CPU programming. Exactly. Because we need to generate those permutations. And so we're left with like uh technology from the 70s basically. Uh yeah, generics and templates are a good replacement for that. But while they have some downsides as well like C++ templates are also kind of infamous and some of the platforms uh

**[9:06](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=546s)** like GLSL doesn't have any generic programming uh mechanisms. Then micro shader frameworks a really popular approach and and a very efficient one for sure. The idea is to uh author small fragments of shader code and then to combine them somehow and the the the most uh well productive way of combining them is some kind of graph which can be edited uh in a visual editor. So unre Unreal has a mechanism like that. Maya as well and material X is the the new open source standard for that. And transpiling is the go-to solution uh for portability these days. So spir slang tint the idea is you you write your shader once in in one shading language

**[9:54](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=594s)** and then it gets transpiled to a different one. Uh but then there's the idea of uh EDSL's embedded domain specific languages. So the idea is that you take a general purpose programming language like Python or C++ and you embed your uh well little EDSL into it. The closest thing uh to shading the closest um examples to shading in DSLs in Python are these four warped H number and Triton because they target uh the GPU at a much more lower level than PyTorch or even Jax and they all share some common common uh architectural decisions. So basically you decorate

**[10:42](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=642s)** your uh Python function and then you um the uh the framework uses introspection to capture the P python's a and compile it something else and the compilation is actually done with uh with something is is usually implemented in C++. So it's not a a pure Python solution. And one downside of this is that um this approach supports only a subset of Python that maps onto the target platform. So you're essentially compiling uh the um uh well Cike language with Pythonic syntax. Uh and now uh finally we get to Metashade. Metashade uh is specifically designed to program shaders. Uh well that's the GitHub link.

**[11:32](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=692s)** it's uh the the licenses of Apache 2.0 uh and it does take a different approach to shader generation than uh those for like warp and and so uh well here we have some Python code and it generates this HLSL code and uh next I'm going to go into detail how about how that actually is implemented. So but first of all some some demo just to prove that it works. Uh it's it's a very meat and potatoes kind of uh uh rendering some restorization. Uh the the uh basically I'm taking uh um uh host application developed by AMD uh and I replace uber shaders implemented

**[12:20](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=740s)** with the C pre-processor with shaders generated by Metashade. Um so how is metach different from uh warp or um taichi? So first of all we don't rely on in introspection. We most we rely on tracing kind of like jacks or pietorrch. Uh we don't parse the uh python a yeah we we don't we don't write a compiler. we just uh emit code uh when executing Python code in in a in a Python interpreter. And uh the the second principle is immediate code generation. Immediate mode code generation kind of similar to how PyTorch eager mode launches computations immediately eagerly. We generate code

**[13:09](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=789s)** eagerly line by line uh without building some kind of intermediate representation. And this uh uh uh provides some uh nice benefits. it's becomes possible to uh interle uh this meta code with arbitrary Python code and also this enables meta programming because we can build abstractions with Python around this basic uh code gen uh implementation and well uh yeah just just a diagram to um um illustrate this. uh then um I I need to talk about generators. This is a central concept in met in Metashade. So it's basically a

**[13:57](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=837s)** polymorphic object that everything uh goes through uh in the cogen process. Uh it's named SH by convention, but uh well it yeah well it's just a convention. So basically you always create a a concrete generator for specific target. So for example for HLSL of a specific version or GLSL of a specific version but then you can write a generic AL algorithm that works with this polymorphic uh generator and doesn't need to know what the actual implementation is. Uh what's inside a generator is basically a semantic model of the shader being generated. So well it keeps track of the uh uh stack of scopes and uh each scope has uh dictionary of locals and so

**[14:47](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=887s)** on and so forth. So uh it goes to show that even though we're not writing a compiler doesn't mean that we're just concatenating strings. Uh uh so we actually do verify the uh the semantic correctness of what we're generating. The next pattern is perhaps the most uh important one and and maybe the the strangest one as well. Capturing symbols. So how do you capture symbols if you don't use introspection? And also a related question how do you how do you overload assignment to have se like semantics because uh well in in C assignment is by value in Python it's always by reference. So the hack to make it happen is to pretend like uh these

**[15:36](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=936s)** meta variables are members of the generator. So it's always sh uh something and yes it it does it does produce uh uh kind of idiosyncratic syntax but this is a trade-off that we're making to to enable meta programming capabilities. Uh so this allows us to in to enforce seal like behavior that would be otherwise uh impossible to implement in in Python. Uh things like lifetime management and static typing. So you uh well in Python you can just point X to a different object, right? But in in C you cannot uh change change the the type of of of of a

**[16:26](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=986s)** variable uh after it's been initialized. [snorts] Uh and a very nice consequence of this is that uh regular Python variables and these meta variables live in different name spaces. So this really enables you to do anything you want in Python. um uh on top of uh your code gen. Okay. Operator overloading is kind of self-explanatory. Instead of uh um performing the ma the mathematical operation right there and then we build an expression. So it's it's the expression building expression builder pattern. Uh and here uh we have another uh great uh uh u

**[17:19](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1039s)** play great spot to check uh our semantics. We can enforce stricter semantics than the target language allows. So for example, we can prohibit the uh addition of a color and a point even though they're represented by the same type uh in uh in the target language. So representing data types it's kind of continuing on that theme of polymorphic tracer objects. So these we uh unlike some other solutions we don't map uh Python types to target types. We instead have these polymorphic tracers which encapsulate their semantics in their implementation. some uh more examples of what [snorts] uh the source and the generated code look like.

**[18:07](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1087s)** Uh then another big one is emulating cel like scopes and uh I I kind of uh covered it already. So basically because well the shader knows when the scope is uh is is closing it can uh uh we can track that a variable goes out of scope and this and uh to implemented on the in our EDSL uh we're using uh um uh context managers the with uh statement uh just some uh to to make it more um uh well obvious how the difference between design time and runtime code which you can uh mix freely. So the Python uh

**[18:57](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1137s)** control flow still exists but it uh it's responsible for design time decisions and those are the ones that are so important in real time shading. Uh function definition syntax. Uh one pattern is using a con context managers uh again and the other one is using a decorator. Um uh oh I'm sorry uh here we have um a meta programming example which is uh admittedly a bit too involved uh but um uh yeah well it it's just something that you would need you you would typically implement with the C pre-processor

**[19:46](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1186s)** otherwise uh and in this case we are using the pygtf lib to parse um GLTF assets, GLTF materials and we generate code based on that source uh source asset. So it gives us an example of how you can integrate with arbitrary uh Python code. Uh and then uh there is now a prototype integration of Metashade with material X. Uh, material X is becoming the standard for material authoring in and exchange in um the visual effects world. Uh uh and it's an example of a micro shader framework. It has a visual editor and this here is is an actual shader graph

**[20:35](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1235s)** for the uh open PBR surface node which is the latest and greatest standard. PBR stands for physically based rendering the latest and and greatest uh physically based rendering um uh surface model. So as you can see it's completely unmanageable in a visual editor and uh it just uh demonstrates that visual programming is not always the uh the silver bullet and code is uh still better at expressing complexity. And then um uh h why it was easy to implement a metach integration because like many visual effects uh pieces of software material X even though it's implemented in C++ it

**[21:23](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1283s)** has a material X API so it's easy to get the um metadata for for a specific uh material X node. So you can call material nodes from metashade and vice versa. And this concludes my presentation. Uh here are some links. Please uh check them out. Uh thank you for uh listening. [applause] [applause] Thank you Paulo for the talk. Uh so Q&A time. Um first question. So a rather straightforward question, what is introspection? >> Uhhuh. So yeah, introspection is basically when a when a uh a program can

**[22:14](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1334s)** treat itself as as as data. So when in Python you can use the inspect module uh uh inspect package to uh in to inspect the structure of the Python program itself. So you can analyze well the control flow uh the types of uh u function parameters with type annotations and so on and so forth. >> All right thanks. Uh next question uh why not write your shaders in rust is the cost of switching too high? >> Well there there are definitely projects around that. There is Rust G Rust GPU I think it's called which is uh which is what it sounds basically but

**[23:03](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1383s)** the the the the difference here is that that's still a compiler based approach so it doesn't really offer this kind [snorts] of meta programming uh actually the closest thing that I would compare Metache to would be circle I don't know if anyone is familiar with it it's it's this C++ extension developed by one person Sean Baxter uh which offers [snorts] superior meta programming to C++. So imperative meta programming for example. So uh I I would compare metade to that approach. >> Okay. Thanks. Uh moving on. Next question. So yeah, first of all acknowledgement for the grid project. >> Uh are you planning to support exporting to go dot shaders at some point?

**[23:55](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1435s)** Uh absolutely, but it's a question of bandwidth because uh yeah, my time is limited. So I'm definitely more familiar with shaders and um right now material X is really my priority because it already has these multiple backends and it already integrates into uh tons of host applications. But with with CUDA, I would encourage uh well, anyone who's interested to contribute their own uh generator for sure. It would be well a great application. All right, thanks. Um, next question. Any opinions on Mojo? It seems like it has similar goals, albeit more general. A shader could just be another compilation target.

**[24:45](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1485s)** >> Yes. Yeah. I'm just I I definitely know about Moa, but to me it it it it feels more like a warp or H. So it's an it's an extension of Python where where where you compile to kind of see like with C like semantics. So again uh this is a compiler based approach and uh again the meta programming tricks and meta shade would not be possible there. All right. Uh, final question of the talk. Uh, does Metashader improve the debugability of shader code? >> Yes, I would say so because so on the one hand um

**[25:35](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1535s)** the the readability of the target code matters. Metachade generates target code uh that's very readable unlike some other approaches. So for example with transpilers it's a common problem that of uh you usually uh just uh lose comments for example and you use any well generic programming that happened upstream but also you well with tint specifically you you get some not so readable code and that complicates debugging on the back end. But second of all, uh those uh examples where um some semantic check is enforced in Metashade, it basically just throws an exception. So you can use your uh favorite Python debugger to just see the whole stack and

**[26:23](https://www.youtube.com/watch?v=6yQmEvqMDCQ&t=1583s)** and see in Python what what kind of semantic check failed. If it was something based on a compiler, you would get a compilation error and then well you you wouldn't debug a a compiler written in C++. So I would say that debugability is is uh even better in in the area of meta programming. >> All right, thank you audience for your wonderful questions and being a good audience and let's end this session by applauding our speaker Paulo. Thank you.
