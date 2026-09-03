---
id: PEJakKxVh1c
title: "Building Secure Environments for CLI Code Agents [PyCon DE & PyData 2026]"
slug: building-secure-environments-for-cli-code-agents-pycon-de
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Harald Nezbeda"]
channel: null
duration_min: 30
published_at: 2026-08-25T18:20:05Z
video_id: PEJakKxVh1c
url: https://www.youtube.com/watch?v=PEJakKxVh1c
youtube_url: https://www.youtube.com/watch?v=PEJakKxVh1c
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Agents & orchestration", "Classic ML & data science", "Security, safety & red teaming"]
transcript: true
---

# Building Secure Environments for CLI Code Agents [PyCon DE & PyData 2026]

**Harald Nezbeda**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=PEJakKxVh1c) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Harald Nezbeda demonstrate how to build secure, containerized environments to safely harness the power of CLI code agents without compromising your host system.

Speakers:
Harald Nezbeda

Description:
Running CLI code agents directly on a host machine introduces significant security risks, including accidental data exfiltration, destructive file system operations, and the installation of malicious packages. Because these agents operate with the user's full permissions, a "lethal trifecta" occurs when an agent has access to private data, external network connectivity, and processes untrusted content.

To mitigate these risks, the VibePod framework implements an isolation pattern using Docker containers to sandbox the agent's runtime. This approach restricts the agent's scope by mounting only specific project workspaces and using a deny list to prevent access to root and home directories. VibePod utilizes a Python-based CLI, built with Typer and PlatformDeers, to manage these containers across different operating systems.

Observability is achieved through a man-in-the-middle (MITM) proxy that intercepts all HTTP and WebSocket traffic between the agent and the LLM provider. This traffic is logged into a local SQLite database, which is then visualized via a Dataset dashboard. This system allows users to monitor raw prompts, track response times, and analyze token consumption—including input, output, and cache tokens—by aggregating data directly from the raw HTTP responses.

While containerization reduces the attack surface, it does not eliminate risks such as prompt injection or data exposure via misconfigured mounts. Effective security requires combining these technical isolations with the principle of least privilege and consistent human review of agent actions.

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

*4,832 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=PEJakKxVh1c&t=6s)** Um we are going to discuss today how um we are going to build those um environments to secure our uh container agents. Uh before a few things about me I'm um Harald. I'm working um at a company in Austria. It's called Anexia. I'm there having the role of Python technical lead and in my day-to-day um activities I do lots of things with Python DevOps and also recently a lot with AI. Um in my free time I'm an open source maintainer. I do uh technical blogging and I'm also a part-time uh lecturer at two universities in my area and I also do photography. So before I start I want to see some hands. I'm curious how many of you are actually using CLI um coding agents.

**[0:56](https://www.youtube.com/watch?v=PEJakKxVh1c&t=56s)** Okay perfect. And how many of you are actually running them directly on the machine without any sandboxing? Okay, then who of you or how many of you are actually knowing what the agent is doing? Okay. So, um what we want to do today, we want to look a bit at the risks of running those agents directly on your machine. We um will look at a pattern. Um I will propose how how you can um isolate the agents so you can run them more securely and how to observe what they are doing. And um then I will have a quick demo. um I will show the system that I built and

**[1:44](https://www.youtube.com/watch?v=PEJakKxVh1c&t=104s)** I will also show you how you can uh look over the logs um of the agent. So a bit of history um how this whole thing started. So back in 2017 uh we had a paper um which introduced um the whole transformer architecture and with the transformer architecture the first LLMs were built and it took some time um until 2022 which we had the main breakthrough of a chat interface that became very popular. Um and we still had this approach of um you put some text in you get some text out. Um few years later um we had some new capabilities with those LLMs. Um the most important one is the tool use um because this one allowed now um to to

**[2:34](https://www.youtube.com/watch?v=PEJakKxVh1c&t=154s)** introduce those agentic flows. So now models are capable of reading your files also run commands um call external APIs. So this means um we can now also act based on the information that the model um generates. So this means we had an assistant mode. Um we had actually those applications that were able to explain things for us. Um they were not able to execute anything. So it means the risk for us was whatever we typed in the chat interface that could be somehow sensitive or or risky. Now we're moving um at the agentic mode where our tool is capable of executing commands. it can write and edit files and also make network requests. So um this means um we now have a much higher

**[3:23](https://www.youtube.com/watch?v=PEJakKxVh1c&t=203s)** risk. How does the landscape now look for those agents? So from from my experience we have those those three parts. We have the VS code forks um tools like cursor and windsurf. Um they are uh offering you the capability um to use those agents. Then we have the the the second iteration would be IDE plugins. Um you have things like copiland or juni um or augment code. you can install them in your existing IDE and start using them. And more recently um we have the CLI agents uh things like cloud code like codeex um or Gemini CLI open code um you can start them directly in your terminal and already connect them with your codebase and start to do things. So this means those agents have access to your workspace. They can execute things. They have network access u and so on. The most important thing is

**[4:14](https://www.youtube.com/watch?v=PEJakKxVh1c&t=254s)** the agent acts on your permissions. So it has actually the permissions the user has. So this means we are introducing some new risks. And this brings us to a concept that Simon Willis introduced which is called lethal trifecta which means if you have private data and external access and also your tool is acting based on untrusted content you're really in danger. Um because now a lot of things can happen. Something like this scenario um where we have accidental data exfiltration. Um this happens because you um give the agent a specific prompt. The pro the agent uh decides to help you based on some documentation. um it reads that um it needs to send the files to a specific API and like this

**[5:04](https://www.youtube.com/watch?v=PEJakKxVh1c&t=304s)** your local environment file can't be now um posted to some um external vendor. Another scenario would be um a very messy cleanup where you just say the model, hey, I want to um clean up all my files. And for some reason, it reads um not just your your test or temporary files that you created, but also your git history also. Um probably heard uh about the recent attacks uh in in the um npm package manager. This is also something that the model um can can do. uh it can read some sort of external documentation and decide this is the package that you need to solve the problem and will install it on your system and I don't know um you maybe seen the the Axios um vulnerability where you suddenly had a

**[5:53](https://www.youtube.com/watch?v=PEJakKxVh1c&t=353s)** crypto miner installed on your system just with an npm package. Okay, those were all hypothetical scenarios but these are some real ones. So those are um issues and stories um where users used cloud code and they suddenly got their uh home directory deleted which is not really that cool. And also the the last story is is a Mac user who also was running uh cloud code with dangerous escape permissions and also the whole home directory uh was wiped which means the whole Mac was destroyed. Okay. Also I ran some queries on the repository um of of cloud code and see there are some some issues. So also the slides are shared afterwards. You can use the links and you can also see it for yourself.

**[6:43](https://www.youtube.com/watch?v=PEJakKxVh1c&t=403s)** So actually what this means you're kind of having a sort of democ. So you are actually using the tool you operate with it. It works fine until you have something catastrophic. So this um leads me to the first isolation pattern I built. It's a um project. It's called cloud container. And the idea was um to have an isolated runtime in this case put everything in a container um and make sure um that we limit the scope um of what is actually accessible um from the perspective of the agent and um in the meantime I was also curious. I wanted to see what the agent is actually doing. So I ended up with this architecture and my first iteration um used this entropic base URL uh which means I started cloud code set

**[7:32](https://www.youtube.com/watch?v=PEJakKxVh1c&t=452s)** the entropic base URL which is actually meant for um changing the provider. So you can use something um like AWS bedrock um as uh your entropic API or entropic itself and um in this case I just created a proxy container and my proxy container is actually intercepting the traffic and by this I can actually see what the container is doing. The SQLite database is actually on your local machine and this way you have your own system uh where you can track what the container is doing. We have a project workspace. The project workspace is actually the code that is mounted from your machine and we have another dedicated volume where we are storing um the whole um configuration files that are required for the agent. So um in this case if you once log to the system you will stay

**[8:21](https://www.youtube.com/watch?v=PEJakKxVh1c&t=501s)** logged in if you run another container. What they didn't had in this iteration was also um tracking um things like uh calls to search tools or other websites. this was was not part of that project. Okay. So the idea is we keep uh everything separate in a container. Uh we route the traffic to the proxy and this way at least we can isolate um those um failures to the machine itself. So if we have something bad, if uh a bad application is installed or if the um agent decides to remove things, it's going to be at least isolated to that specific container that we are running. I showed this um to a few of my

**[9:09](https://www.youtube.com/watch?v=PEJakKxVh1c&t=549s)** colleagues and then they said, can we have one for Gemini? Can we have one for codeex? Can we have one for open code? And so on. So I decided to dig deeper into each of those agents and I created those projects and soon I realized um this is not really easy to maintain now um because I now have a different command line for every agent um don't really want this also um for each agent I now have a dedicated database which is running and it's is really hard to onboard um other team members into it. So I decided to build something totally different on a new approach and I created this project which is called Vipod and in this project I tried to generalize the pattern and I created it mainly uh for making a better experience

**[9:57](https://www.youtube.com/watch?v=PEJakKxVh1c&t=597s)** with a CLI. So before everything was created with bash, I moved it now to Python and um the CLI allows you to use it with all um the containers and we can now reuse the patterns for the proxy and also for uh the database for logging for all agents. There are some tools um that I use for this. Um the most important are um the typer for for creating um the CLI also platform D for making sure that the configurations run um on multiple operating systems. This is how the architecture looks right now. So um instead of having just a single proxy that is used for routing the traffic um of the um entropic API u we are now having a man-in-the-middle

**[10:46](https://www.youtube.com/watch?v=PEJakKxVh1c&t=646s)** proxy. This is something that I uh found for for other agents and it works very well because like this we can now really monitor the entire traffic and we can add everything to our database really each individual request. Um at this point I also extended it to also track activity um that is made by websocket connections. Um now also um the the agents they have also their own um repository. So with uh time those um agents can also evolve and also multiple agents can be supported. How does this look? You have now um this VP as the CLI tool um and you can just say VP run cloud and it will start your cloud instance and like this you can use it for all the other agents.

**[11:36](https://www.youtube.com/watch?v=PEJakKxVh1c&t=696s)** Then um if you want to see what the agents are doing, you just have to list um command. You can just see like this what is running on your system. You can stop them individually or you can stop um all of them if you want. And now it's time for the live demo. And let's hope this works. So I have here my um system currently. So I have um the VP CLI installed and I can see here if I run this VP version um I'm going to see what is currently on my system. I see the version of the CLI tool. I see the version of Python which is also important. also the version of Docker because this is the tool that is currently based to run on. And if I now want to run cloud, I can just say VB run clot. And first thing um it will ask you um if

**[12:24](https://www.youtube.com/watch?v=PEJakKxVh1c&t=744s)** you give permissions um to this specific folder to run. I will say yes. And then it will start my container. Um also important if you try to run it on your home directory which might happen by accident. uh this thing will prevent it because um root directories and home directories will actually be on a deny list. So don't do this by accident to share your entire home files. Okay. Then what we can do now is I will take a simple task from my GitHub repository and I will just tell the agent to do something and the whole idea now is that agent will start um working in the background will do some API calls um and um based

**[13:14](https://www.youtube.com/watch?v=PEJakKxVh1c&t=794s)** on the skills that I have configured to ask me questions and so on. So the important part is now how does the logging look. So we have here our HTTP um proxy log. So maybe I will just say show you how the database looks. Uh so the tool that I'm using for the visualization is called data set and um it's a tool that is um very cool if you're having a SQLite database and want to analyze some data. So the first thing is here we have the proxy database and inside the proxy database you can see you have all your HTTP requests and also all your HTTP responses uh and also here you see the websocket messages. So if I want to go over the HTTP requests I see here I can sort them descending and I can now see the API calls that we have just done.

**[14:03](https://www.youtube.com/watch?v=PEJakKxVh1c&t=843s)** And what I've um also done here, I showed the um responses also also the requests and responses just as binary. So you can download them and you can see the entire prompt uh that claude is actually um doing in order to um operate. Also here you can see the responses individually but um the most important part is you can now use these data also to create dashboards which are a bit more nice to see. So um currently there is a HTTP dashboard implemented. The HTTP dashboard will show you how many requests um your agent is actually doing and you can see here uh each individual request and you can see also the timing of the request. So um you can also um kind of um isolate

**[14:54](https://www.youtube.com/watch?v=PEJakKxVh1c&t=894s)** requests that take longer u based on the payload. Uh and also you can see failing requests. So in case that um the entropic API is currently not available, you can also track it like this and see when a downtime happened. The other thing that we have are um the dashboards for the token usage. They're currently implemented for cloud and for codeex. And the token usage here happens a bit differently than on other projects um that are available on GitHub. Typically uh those dashboards are built using uh the JSON L files um that the agent is storing. What I do here is I use the raw HTTP request. So entropic gives me with every response also the token consumption which means I can aggregate that data and I also show it um here. So this means I can look at each individual request. I can see how many input tokens

**[15:43](https://www.youtube.com/watch?v=PEJakKxVh1c&t=943s)** I had, how many output tokens I had. I can also see um the cache tokens for reading and for writing and also um the response time. If I have a response like this here, this probably means that the uh I I cut up the agent and the response didn't finish. That's why it's not stored. Also, if you are curious, you can look with data set into each individual query and you will have some messy SQL here uh with which you can play. You can also uh edit it um lively if you want and also um see and analyze the data. Okay, then let's just see how our agent performs exactly. So now we have this thing. Um, every time uh you run the agent, the agent will ask you questions. If you don't want to do this, there is a

**[16:34](https://www.youtube.com/watch?v=PEJakKxVh1c&t=994s)** special mode you can use which is called I know what I'm doing. And if you start it like this, it's going to directly append the dangerously skip permissions for you. Um, and the idea was every agent is calling that mode differently. So you have one syntax for for claw, you have one for codeex, for Gemini, you have uh I think on Gemini it's called the yolo mode. Um, and I wanted to to just have one parameter and I wanted to to kind of group them. So so you don't have to think about what's what's the parameter actually called. Um, yes. And like this I can rerun the prompt and it will just go through and will auto approve. Uh it will only stop if there is really some

**[17:21](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1041s)** some direct input needed. If if um the agent um considers that there is not sufficient input, it will ask me for text input. Okay, then let's just see where we are. So what we did in the demo flow quickly. So we looked um an isolated agent run. We just run a small task and we looked a bit at the data set dashboard. Uh, one quick thing that I forgot to mention, the data set dashboard is actually also um running using the VP CLI. So all you have to do is run VP UI and this will start your container and will automatically open in the browser. So if you want to install it yourself,

**[18:09](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1089s)** here is a quick run. Uh you can just do it with pip install wipeout. Um if you're on a Mac, you can do it with this um long command. Uh it's actually a private tab. That's why why it's so long. Um then you can go into your project um run VP list just to see what's available and um with the VP run um and a specific agent. You can see the agent. You can either use the short hand the VP UI or you can just say the long commodity VP logs start and this will um start um your um logging service. So what you can also do I forgot to show you the VP command itself. If you run just this you can get the help of the command. Um, you can also install auto completions if you want and you also have the VP list command which is very

**[18:56](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1136s)** important because this one will show you what agents are available on your system and it will also show you on which directories you're currently having an agent running and will also show you the context uh that is actually bound to your agent and this data by itself it's also available in data set. If you go into the logs, you can also see here you have the sessions and here on the sessions you can see uh which agent you used and to which directory you bounded and also with which version of the CLI you were working and um also another thing it's also collecting the messages that you type into the agent but this doesn't work perfectly now because the agent also has some sort of of artifacts um in the CLI. So this works kind of okayish but but

**[19:46](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1186s)** use it with caution. So just continue there are some limits however so which um you should consider um the container uh will reduce the attack vectors but it will not completely protect you. So you're really not protected to prompt injection attacks. So the things that I show in the scenarios, if if you by accident get some sort of mpm package installed, this will still happen, but it's isolated to your container. If you are misconfiguring the mounts um and you have some some critical files in your context, you will also expose those uh informations. So be careful. Um and the logging um will actually help you

**[20:39](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1239s)** find how um the agent works but this is not a prevention. Um it's just for for history purposes. So what's what's important? You should still do human review and should make sure that you have right policies in place. So main takeaways try to use those agents isolate them as good as possible. Give them only the context that they need to work um by applying a least privilege to file networks credentials and also from time to time uh make sure that you look over what they are doing and try to measure um on on your uh observability part what um what's actually matters. have some resources here to to the different projects that are available and from here I'm ready for your questions.

**[21:41](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1301s)** Uh we have a few questions in the chat and maybe we can take some from the audience. Um how do you handle credentials credentials and login for hyperscalers uh IE1 agent credential per container? >> Okay. So what you can do is uh since you're running them individually um I I I typically work with docker containers also for my application. And so why I end up is I have an environment that I set up for my application containers and then I have um the um container uh with the agent itself. So they are separated and when I run my environment for the applications is loaded just with the credentials that are needed for the application to run and um my my agent doesn't see those uh environment files.

**[22:29](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1349s)** >> Okay. Um, is there a minimal VP version without all the monitoring termed overhead? Uh, if all I care about is the is the isolation. >> If you only care about the container, um, you can go into the VP agents repository and there are all the the images also. So, in fact, let me show you this. Um, down here in the documentation, you can see the pre-built images. So if you just want to run the container by itself, you can do it like this directly. The VPCI is actually taking care of creating uh the docker network uh connecting um your container with the agent with the proxy container and also making sure that all configurations are in place um for for the tracking. >> Uh okay. How does VP compare with the

**[23:19](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1399s)** under sandboxing projects like anthrop anthropic experimental or sandbox runtime or docker sandboxes? >> Yeah. So there it is in fact the docker sandbox. Um and um the thing is you can manage it yourself. What what you can also do here is uh since you are able to overwrite the images, you can just start from uh that specific pre-built image or you just create um your own image um as you want it. You can also install all the tools that are required and you can pretty much reuse it over your projects. Uh >> okay. Can you run uh remote containers into Kubernetes with VB? Uh >> haven't thought about that. Maybe I don't know.

**[24:08](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1448s)** >> Um, are all sub agents also isolated and monitored? >> Can you repeat a question, please? >> Are all sub agents also isolated and monitored? >> Sure. Um, if you if you want to run sub agents, um, you're basically running uh those agents inside the container. So if you are starting cloud code uh cloud code will be in a container. Um if you have the teams uh function enabled or simply using the sub aents this will be uh by default enabled. So cloud will start those sub aents or subprocesses inside the container. >> Okay. Uh Cano, should you also use dedicated git repo for the agent so you can keep it separate from your own work

**[24:57](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1497s)** in progress and maybe then it doesn't have to it doesn't have the remote configured. >> I'm not sure if I understand the question correctly. Yeah, please. >> Uh sure. So as I said those all all those um projects here are individually available. So this means there is also um the source here for how you can build the agents itself. So you can look over the source here and you can find the docker files for each individual agent and you can start from here if you want. >> Uh okay. Um uh does your

**[25:47](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1547s)** MITM proxy support or is it possible to support approving or denying network request would be very useful uh to control exactly what request it is or to make. >> Yeah, I I always thought about this. It's it's a bit of a trade-off now between um easy handling and and kind of having now I don't know the whole network operations tech on on your local machine where you are handling whitelisting and blacklisting. Um if you have any ideas how how this would be easy to to manage uh I'm happy to discuss uh because I I want to introduce something like this but I don't want to have that much overhead. >> Okay. Okay. Can you still use plans like cloud code with the with your MIT proxy or do

**[26:36](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1596s)** you need to use payer use API? >> Oh no, you can you can use the the the regular plans. So so in this case um here in fact I'm using a pro plan. So um you see this when you start the agent because the tool itself it's not changing the agent. um you have the um the agent as provided by the vendor installed in your container and you're um just having the tool to provision the container for you and forward um the the request. So that's all it's doing at the end. It's just for convenience. So you have it for for all the agents um in um the same way. But as you see here, I have the code pro subscription. there is absolutely no problem with it because um they're they don't change the requests uh themselves that are sent by the

**[27:22](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1642s)** agent. Uh maybe we can take like two questions from the audience. There is anyone who would like to um is there an easy way to integrate it with pre-existing dev containers for example the monitoring spec? >> Um so you have the containers already in place. You should try it. Honestly, um I'm not using myself that much dev containers. I'm I'm I'm more on that part where I build my compos configurations and I'm happy with that. Um but you can try it. >> Yeah. Um on Mac there's a new

**[28:13](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1693s)** application container. >> Okay. >> Um would it be possible to replace Docker? Is it easily or is it it has similar? Um >> the the whole thing is I I also try >> it's closer to Mac architecture. >> I see. Um the important part is um does it have a Python API exposed? So so we can we can communicate with it if it has that in place. We might have a starting point. Um the other part is maybe the permission handling. I'm also trying for some time uh to make this work with Potman. A Potman is a bit more strict on on um on permissions on your files. So I I kind of want to also finish and integrate this to make it more agnostic. So you can also run it with different uh container runtimes. But sure, let's just

**[29:02](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1742s)** talk after after the the session. >> Yeah, maybe quick question. Um so how much of the wipe pot is actually wipe coded? >> A lot. A lot. So I have I have to to say uh the first project the cloud container I I built it um from scratch and I built it manually and um afterwards I actually decided I want to have this thing in place with a CLI since I had all the learnings and the patterns from the previous projects I actually reused them and I actually also used all the projects as a reference to build this. Um but at some point I hit a I hit that that the limit where I now have to feed it new input and new perspectives. >> Uh uh last question. How does VI port compare to Docker

**[29:49](https://www.youtube.com/watch?v=PEJakKxVh1c&t=1789s)** Sandbox? >> Docker sandbox um as I said so the Docker sandbox itself I think it is um also working with those pre-built images uh but I haven't used it that much. I'm not sure if they have those al also a unified CLI tool might be worth discussing after the session. >> All right. Thank you very much for the wonderful presentations. >> Thank you.
