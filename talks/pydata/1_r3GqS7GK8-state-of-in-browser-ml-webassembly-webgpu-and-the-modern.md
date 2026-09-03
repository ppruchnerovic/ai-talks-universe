---
id: 1_r3GqS7GK8
title: "State of In-Browser ML: WebAssembly, WebGPU, and the Modern Stack [PyCon DE & PyData 2026]"
slug: state-of-in-browser-ml-webassembly-webgpu-and-the-modern
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Oleh Kostromin"]
channel: null
duration_min: 28
published_at: 2026-08-04T22:20:34Z
video_id: 1_r3GqS7GK8
url: https://www.youtube.com/watch?v=1_r3GqS7GK8
youtube_url: https://www.youtube.com/watch?v=1_r3GqS7GK8
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Classic ML & data science", "Inference, serving & GPU infra"]
transcript: true
---

# State of In-Browser ML: WebAssembly, WebGPU, and the Modern Stack [PyCon DE & PyData 2026]

**Oleh Kostromin**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=1_r3GqS7GK8) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Oleh Kostromin and Iryna Kondrashchenko explore the modern in-browser ML stack to discover how WebAssembly and WebGPU are enabling secure, serverless, and scalable on-device inference.

Speakers:
Oleh Kostromin, Iryna Kondrashchenko

Description:
In-browser machine learning leverages WebAssembly (Wasm) and WebGPU to execute code and models on the client side, reducing server costs and improving user privacy. WebAssembly provides a binary instruction format that allows near-native execution speeds in all major browsers. Because Wasm lacks a standard library for system-level tasks, toolchains like Emscripten are used to compile C/C++ code into Wasm, providing necessary runtime layers and virtual file systems.

Python integration in the browser is primarily achieved through Pyodide, a port of CPython to WebAssembly. Pyodide allows the installation of pure Python packages via micropip and provides pre-compiled builds for libraries with native extensions, such as NumPy and Pandas, through the Pyodide package index. For developers seeking higher-level abstractions, PyScript enables Python logic to be embedded directly in HTML. Alternatively, MicroPython can be used for faster startup times and smaller bundle sizes (under 300 KB), though it supports fewer features and packages than CPython.

Model inference is handled separately from the Python interpreter to avoid overhead and enable GPU acceleration. WebGPU allows for general-purpose compute, moving beyond the graphical limitations of WebGL. The ONNX Runtime Web serves as a universal adapter, executing models converted to the ONNX format on both CPUs and GPUs. For large language models (LLMs), WebLLM provides GPU-accelerated inference, while vLlama enables the execution of GGUF-format models on the CPU via Llama.cpp. While Wasm is currently limited to 32-bit addressing (capping RAM at 4 GB), these tools collectively enable the deployment of models up to 3 billion parameters directly in the browser.

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

*4,231 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=4s)** Yes, good morning everyone. Thanks for coming. For the next 25 minutes or so, we are going to talk about how to run Python and ML models directly in the browser. If you'd like to follow the slides on your own device, please feel free to scan this QR code. And meanwhile, I'll do a quick survey. I would ask you to raise your hand if you have ever tried to train or run an ML model directly on the client side. Yeah, I guess maybe 10% at most. Um if this topic is rather new for you, and I assume it is for most of you, you're in the right place because by the end of the talk, you will know what technologies are available,

**[0:52](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=52s)** where and how to use them, and what are their limitations. But before we proceed, let us introduce ourselves. I am Oleg, this is Irina, and we are co-founders of Data for Solutions. At Data for among other things, we develop Lumal, an open-source ML Ops LM Ops platform that helps you build, deploy, and monitor your models. The project is available on GitHub under Apache 2 license, and we would really appreciate if you check it out, provide your feedback, or maybe just support it with a star. However, this slide is here not only for the advertisement purposes, but actually Lumal is the reason why we got into the topic of in-browser ML. A few years back, we started to explore the initial concepts of the product, and

**[1:40](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=100s)** while our initial ideas were quite different from what we have right now, there was one idea that persisted. That idea was really simple. A lot of products don't allow you to do anything until you sign up. And to us, this didn't feel like a right thing to do uh because it creates a lot of friction for the users before showing any value at all. Therefore, we decided that we wanted to build a module that might not be as important for the platform in a greater picture, but that would allow users to experiment with some of the functionality at least a bit without creating an account. The module we made in the end is called Express Tasks, which basically allows you to build uh models that are compatible with other modules of the

**[2:29](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=149s)** platform out of the box. For example, we have no-code interface to train tabular models in the AutoML fashion. We have Jupyter Lab instances. We have a no-code builder that allows you to define an LM chain and automatically optimize the prompts and so on. But, as you might have guessed, uh this all works 100% on the client side using the tech stack we are going to talk about today. But, obviously, there are even more use cases. You can have an um interactive documentation of your Python library. You can create a shareable data tool without any backend infrastructure, and you can even run a large language model directly in the browser on the client side. So, that was a rather long introduction.

**[3:16](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=196s)** So, let's finally proceed to the next um part uh focused on running Python inside of the WebAssembly. First, let's figure out what WebAssembly even is. As per webassembly.org, WebAssembly is a binary instruction format for stack-based virtual machine. WASM is designed as a portable compilation target for programming languages enabling deployment on the web for client and server applications. So, it's an instruction uh for a virtual machine, kind of like what Java promised 20 years ago with its compile once, run everywhere. Except, it operates in a much lower level than the Java bytecode. And because it's so low level, runtimes can cheat compile it really efficiently. In practice, you can achieve near native

**[4:04](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=244s)** speeds. Obviously, there is some overhead, but it can be much faster than running JavaScript for compute heavy stuff. You can also run WebAssembly almost everywhere. There is currently huge traction around running WebAssembly on the server side as a possible alternative for Docker containers, but it's not really our focus today. Uh we are interested in the browser compatibility. And here everything looks great. WebAssembly is supported by every major browser, even the mobile ones. So, compatibility is really not an issue anymore. Now, the question is how to use this on practice. After all, we wouldn't want to write the WebAssembly uh manually. You might have guessed that uh there are compilers that can target

**[4:51](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=291s)** WebAssembly, and you would be right. But, this part is a bit less intuitive than it seems. The thing is that WebAssembly can only do computations on its own. Therefore, only mathematics on integers and floats. It cannot open file. It cannot do a network request. It doesn't have anything like a standard library. And so on, which means that A, WebAssembly modules should rely on the functions provided by the hosting environment for many of its capabilities. And B, it's really beneficial if the communication between the WASM module and the hosting platform is standardized. After all, if every runtime exposed its own set of functions, portability would quickly fall apart. Therefore, for WebAssembly um ecosystem, the big part is not only compiling the code, but also defining

**[5:40](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=340s)** common ways to um for WASM to interact with the outside environment. There are several projects that try to this. For example, WASI and WASIX are efforts to standardize system uh style APIs for WebAssembly. However, they are also more focused on the server side. Therefore, for us, Emscripten is much more interesting. It's a rather mature uh tool chain for compiling C and C++ uh to WebAssembly, especially for the web. It ships as a large runtime layer, includes a standard library, virtual file system. It also bridges to browser and JavaScript functionality, and overall allows to bring a lot of native code to web with relatively small changes. This sounds great, but we are at PyCon, therefore it means we must be more

**[6:27](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=387s)** interested in writing Python, not C or C++. But luckily, the reference implementation of Python that we're using every day happens to be written in C. Which means that there should be a way to compile the interpreter itself into a WebAssembly module, and use use it inside of the browser. And Pyodide is exactly that, a port of CPython to WebAssembly that, among other things, allows to run Python inside of the browser, install Python packages, call JavaScript from Python, and vice versa. I will show how to use Pyodide a bit later, but for now, I would like to focus a bit more on the packages. Basically, if the package doesn't have any non-Python extensions, it can be installed from PyPI right away using a

**[7:15](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=435s)** tool called micropip, which you would use more or less the same way like you use a normal pip. However, if a package is not pure Python, it gets a bit more tricky as the extensions have to be built for WebAssembly as well. For popular libraries like NumPy, Pandas, and so on, there are already precompiled builds that can be installed from Pyodide index. This index is separate from PyPI. Currently, it has around 250 packages and is constantly extended. Therefore, there is a high chance that the package you need is already there. However, if not, you would have to build it manually using a utility called Pyodide build. Usually, it's not a big deal to build it, basically just a single terminal command, but sometimes it can be a big

**[8:03](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=483s)** headache and also require a lot of code changes and in your library. Therefore, I would say if the package that you require is not pure Python and there is no precompiled builds, then it might be a good reason to consider not using Pyodide and WebAssembly at all. There are also some other limitations you should consider before using or not using Pyodide. First of all, the functionality that would require sub processes or native sockets wouldn't work. For example, this means that you cannot easily to connect to a SQL database and retrieve the data. Also, WebAssembly is 32-bits, meaning that the maximum amount of RAM is kept at 4 gigs and on top of that, some browsers limit it at half that size. Therefore, if you

**[8:53](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=533s)** need more than 2 GB of memory, it's not always possible. There is a WASM 64 spec that is already implemented by some or probably many of the browsers at this point. However, it's not supported by Pyodide yet. Finally, the persistence is also a bit trickier. You get the virtual file system out of the box, so there is some persistence layer. However, at the same time, it's sandboxed to the browser tab in the domain this tab is running. And yeah, therefore, it's a bit limited. At least in Google Chrome, there is an API for native file system access. However, I think it is still considered experimental and anyway, it's not integrated into Pyodide out of the box. There are still other limitations. For

**[9:42](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=582s)** example, Pyodide runs slower than native CPython. However, and so on. However, those limitations are not as important as the ones as the ones outlined on the slide. So, now let's talk about how one would practically use Pyodide. In a nutshell, two main types of use cases are in-browser dev environments and Python driven front-end applications. So, let's start with the first one. The best example that would fall into this category is Jupyter Lite. It's basically a Jupyter Lab running in the browser without the back-end server. It has the same front-end, the same UI, even supports some of the extensions, but it uses Pyodide instead of the regular Jupyter kernel. From the user's perspective, everything

**[10:32](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=632s)** stays mostly the same and in fact, if you were given a Jupyter Lite instance instead of the normal Jupyter Lab, there is a high chance you wouldn't immediately notice that something is different. Running a Jupyter Lite instance is also extremely easy. You can even host it for free on GitHub pages because it's just a static web server. And there is a dedicated page in the documentation that shows how to do it. And yeah, there's not much else to say about Jupyter Lite, but I would encourage you to try it because it only takes a couple of minutes to set up. So, now let's go back to building front-end applications with Python. We already talked a lot about Pyodide, but we didn't really have a single example that shows how to use it. And in fact, it's really really simple.

**[11:21](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=681s)** You simply initialize the Pyodide instance and then pass the Python code snippets as strings into the run_python method. Specifically, in this example, we are calculating the average of an array using NumPy. It's also to It's also possible to access the JavaScript scope using a built-in JS module, which, for example, allows us to manipulate the DOM. So, all in all, we can run Python, and we can access JavaScript scope from Python, which should allow us to build pretty much anything. However, at the same time, it feels a little bit low-level. Which brings us to the last project in this section called PyScript. PyScript is developed by Anaconda and largely

**[12:10](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=730s)** builds on top of Pyodide, but adds some convenient abstractions so that the whole experience of writing Python for the browser feels a bit more native. First of all, it allows to supply a PyScript config that defines the packages that need to be installed, the files that need to be placed into the virtual file system, and so on. Then, Python itself becomes just another script tag in your HTML code. And similarly to JavaScript, you can either write it inline or provide a reference to a pre-existent Python file. Finally, there is also a bunch of helpers provided by PyScript that simplify the bridging of your Python and JavaScript logic. For example, you can easily create event listeners and assign the handles handlers using a simple

**[12:57](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=777s)** decorator. And one more thing that is really cool about PyScript is that it's possible to use MicroPython as an alternative interpreter instead of Pyodide. For those unfamiliar with it, MicroPython is another implementation of a Python interpreter, which was originally meant for micro devices, but currently fits into the whole WebAssembly ecosystem really naturally. The pros and cons of using MicroPython instead of Pyodide can be summarized in just few sentences. First of all, uh MicroPython itself is less than 300 KB, which means that uh your final bundle size is approximately 25 times smaller than when you're using Pyodide, and by extension, this usually results

**[13:45](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=825s)** in much faster cold starts. However, at the same time, MicroPython differs from standard CPython in feature support. Obviously, it largely depends on the version you're using, uh but uh your available Python code is not guaranteed to work with MicroPython right away. And on top of that, you're losing the rich ecosystem of packages because they need to be rebuilt for MicroPython separately. Okay, and with that, we conclude the part about Python ecosystem in the browser and I hand it over to Iryna, who will talk about the inference stack. >> Yes, so the inference stack in the browser is rather different from what was discussed in the first part of the presentation, uh mainly because it's not

**[14:33](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=873s)** Python-based. There are a few key reasons for that. First, remember that we cannot compile Python to WebAssembly, but only the interpreter. While Python itself is not nearly as fast as the compiled languages, here we add even more additional overhead. Therefore, it would be really non-optimal for larger models and especially language models. Secondly, to the best of my knowledge, there are no uh libraries that would allow you to use GPU for model inference for Python. But let's first talk about the possibility of using the GPU in the browser. There is a common misconception that running the ML inference on the GPU in the browser is impossible because the only way to access the GPU is via WebGL, and WebGL is designed mostly for um

**[15:21](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=921s)** graphic processing and not the general compute. While the second statement is mostly true, WebGL is not the only way anymore as there is also WebGPU, which is much more modern and was designed with supporting general compute in mind from the beginning. It's also widely supported by the desktop browsers and the support on mobile is also steadily growing. So now let's see how we can run it how we can use it for ML inference. Easiest way is if you have your model converted to ONNX. ONNX is a universal format in which you can represent your models as a directed computational graph of standardized compute nodes. In other words, it acts as a universal adapter where you can convert the model from almost any framework into ONNX and

**[16:10](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=970s)** then it can be consumed by a large number of platforms. Though ONNX is just a specification of the format. In order to do the actual inference, we need a runtime that supports ONNX models. And here we don't have that many choices as far by far the most complete and accurate one is ONNX runtime maintained by Microsoft. As you can see, it's available on all major platforms and has bindings to many languages, but obviously the most interesting for us is ONNX runtime web. It can run on both WebGPU and CPU via web assembly. It's really simple to use basically just several lines of code to load the model and generate the predictions. There are also some libraries that built

**[16:58](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1018s)** on top of ONNX. For example, Hugging Face has an official Transformers.js library, which allows to run pre-trained models. It's very actively developed and by the way got a major V4 release by just at the end of the last month. There is a rather big collection of spaces that currently support around 200 model architectures, including large language models like when or deep seek. You can try it out without doing any setup. However, this is not the only way to run um LLMs in the browser. You might have heard about the MLC, which is the project that compiles and runs the models on the MLC engine. Similar with ONNX, it has a web-based

**[17:47](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1067s)** front-end called Web LLM. And if you go to chat.webllm.ai, you can try it directly as it provides a small library of models and the chat interface. Overall, we've been using Web LLM on and off for about 1 and 1/2 years, mostly for exploratory purposes. It behaved quite stably with only some occasional failures to generate the predictions, and while I don't have hard numbers in mind um the speed of the generation always felt very impressive. However, one thing that I would consider a huge drawback is that it does not have a CPU back-end. Obviously, GPU is much more performant, but not yet universally supported, so having a fallback option would be great.

**[18:36](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1116s)** Speaking about running LLMs on CPU, if you ever tried to run one, you must be familiar with the project called llama.cpp for running models in the GGML format. The project has a huge adoption and ecosystem. For example, Hugging Face Hub has more than 160,000 GGML models. Under the hood, llama.cpp is powering, for example, Ollama, another very popular project with more than 50 million monthly downloads and many other tools. And the reason why I'm mentioning this is because llama.cpp also has a web version called llama. Similarly to web LLM, there is a web app you can try out. Um so, feel free to do so.

**[19:27](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1167s)** And this concludes the inference um stack part of this presentation. So, let's do now a quick recap of what was discussed today. WebAssembly provides a way to run a Python interpreter directly in the browser. This can be used to either have a Python dev environment directly in the browser using Jupyter Lite or make front-end Python-based application using Pyodide and PyScript. Pyodide supports most of the pure Python packages out of the box. Many popular packages with native extensions are precompiled and can be used right away. For performing ML inference in the browser, the most flexible option is ONNX and by extension Transformers.js that can run on both CPU and GPU.

**[20:16](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1216s)** Specifically for LLMs, the alternatives are web LLM that has its own format and supports GPU only. And llama that allows to run GGF models on CPU. In conclusion, the ML ecosystem in the browser is still relatively new, but it's steadily maturing and allowing to implement more and more use cases every year. So, we definitely encourage you to experiment with it. Before ending the talk, a couple of quick announcements. First of all, we have brought around 200 sheets of our new 2026 edition sticker pack. So, please pick one up after the talk. We definitely don't want to carry them back home. Uh in addition to that, we are looking

**[21:03](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1263s)** for volunteers that to to a 15-minutes questionnaire-style interview about your usage of LLMs and uh agents for data science work. So, if you're a data scientist and would be so kind to donate 15 minutes of your time, please ping one of us on LinkedIn. We would be very thankful for that. And uh if you don't want to do the interview, it's fine. Please uh also free add us and uh we're always happy to chat and answer your questions. And that's it. Thank you for your attention and I I hand it over BACK TO OLEG. >> [applause] >> THANK YOU FOR THE GREAT TALK, Oleg and Iryna. It was really interesting and fascinating to learn about the state of

**[21:51](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1311s)** affairs of uh how good browsers and on-edge devices have become to be running these models. >> Thank you. >> Uh I'll just take some questions at this point. We have quite a few. Uh the first one that I see is uh "How does the bridging between the inference in JavaScript and any code that you write in Python work? Can you show any demo by chance?" >> Um so, I'm not sure that I got the question correctly, but basically the question is how to use the inference stack from the from Python, I guess. Um it's really simple because from Pyodide to PyScript you can access anything that is in the JavaScript scope. So, you

**[22:38](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1358s)** can access the JavaScript objects, you can call the uh JavaScript functions and so on. And the inference stack has a bindings for JavaScript, so by extension you can also call them from Python. So, this shouldn't be an issue. I don't have the examples on the slides, but yeah, you can ping me on LinkedIn and I probably can provide it. >> Okay, thank you. Um take the next question as well. What models can you run with the 32-bit limit of WebAssembly? >> Actually, quite a lot. So, you can run even 3 billion models, and at this point, 3 billion models are quite capable. I would say that even 450 million models don't feel as dumb as they were a couple of years ago. I wouldn't really recommend you to use a

**[23:27](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1407s)** anything below probably 1.7 billion for any serious work, but yes, uh you can do a lot more than you think. >> Okay. Yeah, so running, I don't know, 100 billion models I still >> definitely [laughter] not possible. >> Still not there. Um can you recommend something to do robust voice activation for a custom word in browser, something in a fashion of okay Google? >> Uh no, >> [laughter] >> but uh as you mentioned, there is a large collection of spaces on the Hugging Face, and I'm pretty sure you would find something for that. We unfortunately don't really work with audio, so I don't know. >> Okay.

**[24:15](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1455s)** Yeah, I think in that case, some sort of speech recognition on edge system. >> Yeah. >> And what's what's the primary motivation of these frameworks when they get started? Like, is it motivated by Is it privacy centric that like your data is not being sent to >> I would say there are two main drivers. First of all, privacy, because yes, you don't have to send any data to the servers, but also the scalability, because everyone has a compute device. Uh and yeah, for example, I'm not really sure about the name, but there is an educational platform that teaches Python and I guess they're running their whole stack on GitHub pages for free and it has like thousands of users, so it can be really really cheap to do so.

**[25:03](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1503s)** >> think Codecademy, right? >> No, the Codecademy Codecademy is different. There is a specific platform that teaches Python to kids again. >> To kids, I guess. Yeah, so basically, if you have a really small instance to host your static web server, you can scale it to probably tens of thousands of users at almost no cost. >> Okay. And probably the final question that I see, which common machine learning packages are available pre-compiled via Pyodide? >> A lot of them. So, scikit-learn, pandas, numpy, polars. So, So, PyTorch is not available, which is a big problem, but everything that is not too big, I think, is available at

**[25:52](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1552s)** this point. And you can go to Pyodide. I don't remember the link exactly, but it just Google Pyodide package index and there is a list of the packages and their versions. >> Yeah, I see one last question as well. This one's probably interesting. If I start to to work with Python machine learning in the browser for the first time, what will be my biggest pain points? >> Yeah, it's it's an interesting question depending on what's your background and what you want to achieve with it. Mhm. Maybe it's it's really difficult to answer, but I would say it's really annoying when a transitive dependency for a package is not

**[26:40](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1600s)** available and there is no easy way around it. Yeah, so at least for us it was a big problem. But as we said, it's maturing really rapidly and right now it's much better than 3 years ago and for a lot of use cases you wouldn't have any problems at all. >> Yeah, I I guess in the beginning you would have to do some sort of assessment whether the packages that you want to run are available or whether you have >> to build them. >> to build them. >> And building as I said because we had a case when we need to build a package and it was a huge pain. Uh as I said if the package is not already available maybe it's a good idea to stick to a normal CPython and not go into this direction.

**[27:29](https://www.youtube.com/watch?v=1_r3GqS7GK8&t=1649s)** >> Right. Uh that's all for the questions. Thank you so much for the talk and answering these questions. Uh can we please give a huge round of applause for their talk again. >> [applause] >> Thank you. Please grab the stickers.
