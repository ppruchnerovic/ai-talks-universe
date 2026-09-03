---
id: nk5BNz8v_9E
title: "Demystifying Agentic AI Using Small Language Models [PyCon DE & PyData 2026]"
slug: demystifying-agentic-ai-using-small-language-models-pycon
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Serhii Sokolenko"]
channel: null
duration_min: 32
published_at: 2026-08-25T18:20:23Z
video_id: nk5BNz8v_9E
url: https://www.youtube.com/watch?v=nk5BNz8v_9E
youtube_url: https://www.youtube.com/watch?v=nk5BNz8v_9E
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Agents & orchestration", "Classic ML & data science", "Inference, serving & GPU infra", "Training, fine-tuning & model building"]
transcript: true
---

# Demystifying Agentic AI Using Small Language Models [PyCon DE & PyData 2026]

**Serhii Sokolenko**

`PyData` · `PyData` · `2026` · `32 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=nk5BNz8v_9E) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Serhii Sokolenko demystify agentic AI as he reveals how to build powerful, scalable data agents using Small Language Models and Iceberg tables—without the need for a GPU farm.

Speakers:
Serhii Sokolenko

Description:
Agentic AI utilizes language models as decisioning engines to perceive environments, make decisions, and execute actions to achieve specific goals. While large language models (LLMs) are often used for these reasoning loops, they are computationally expensive and contain redundant data. Small language models (SLMs), defined as models with 10 to 30 billion parameters that fit within 16 to 32 gigabytes of consumer RAM, provide a cost-effective, private alternative for agentic workflows.

Effective agents require four core capabilities: task decomposition, tool calling, glue code generation, and instruction following. The Salesforce xLAM-2 model, a 32-billion parameter open-source SLM created via supervised fine-tuning on synthetic function-calling data, demonstrates accuracy comparable to much larger proprietary models on the Berkeley function calling leaderboard.

A practical implementation stack for local experimentation includes xLAM-2 with 4-bit quantization, the Llama.cpp inference server for GPU acceleration on Apple silicon, and the LangChain framework for orchestrating agent logic. To prevent hallucinations and ensure data integrity, agents can be integrated with Apache Iceberg lakehouses to access verified business data. This approach allows developers to replace rigid directed acyclic graphs (DAGs) with flexible business rules and guardrails.

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

*4,811 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=6s)** Thank you everyone. Um I am based in Berlin. Uh Tower is a um startup in the Berlin area. Uh we got founded about 18 months ago. But uh this talk is not about Tower. Uh this talk is about a passion project of mine. um understanding all the hype about um Aantic AI and trying to make it you know understanding what we can do with this. Um about eight months ago I um uh came across this concept of a small language model uh and started experimenting and uh using tower for this and uh uh turns out uh there's u a pretty interesting stuff happening in the space. Who of you have heard of small language models? raise your hand. I would say maybe 60ish% um who of you have actually tried

**[0:55](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=55s)** to use it uh for agentic work. Smaller percentage but maybe 25%. Okay, nice. Uh there will be some new ideas here for you. Uh some of the stuff you probably already know. Uh for the rest of the audience, uh you will learn entirely a new concept of uh uh small versus large. Uh yes, there's a sing thing called small language models. If you traveled 150 years ago in United States, if you're one of the uh uh travelers during the gold rush, uh you would see a sign like this advertising uh Clipper um uh routes to California promising promising you riches during the gold rush. If you go to the Bay Area today, you will see a different kinds of advertisements

**[1:44](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=104s)** advertising another gold rush, uh the Aentic gold rush. Salesforce will try to sell you the agent force. Uh some consumer service company will try to sell you AI agents for customer service. Uh even Postman the API company will ask you are your APIs ready for agents. Um a smart person Sadella CEO of Microsoft has recently said that AI agents will become the primary way of uh interacting with computers in the future. So, how do we survive this uh this hype, this uh temporary craziness and madness? And if you take anything away from this talk, um it's uh it's this it's this uh uh phrase of getting your hands uh

**[2:31](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=151s)** dirty. Uh use the tools from the talk, use the ideas that we'll present uh on your laptop today uh and lean on small language models as a way of experimenting. Uh by the way if you have questions um I think there is a um website to submit your questions to please use that if you know the link I think it's talks.pyond PyonD. Uh we also have micros microphones in the audience. Um and at the end of the talk I'll try to take uh several several questions and we'll also talk to you after after the uh after the talk uh at the table. Uh tower has a booth uh where I will be after this talk. So if you want to talk more about SLMs um about what I do uh come downstairs in the sponsor area. Uh a

**[3:20](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=200s)** little bit about myself. Um I uh I worked um for several big tech companies uh including Google. I worked on a product called cloud data flow in GCP. It's a data processing service um high scale streaming and batch analytics. I then went to uh snowflake where I broke a few things including search optimization and metadata. Uh and then I went to data bricks and broke more things including shipping uh serverless filtering for spark clusters and dedicated clusters that teams can use to share GPUs. Uh all very exciting stuff. Um so as you can see I spend most of my career either in databases or in data processing. Now and nowadays I work on tower uh with uh several co-founders and uh and engineers founding engineers. uh

**[4:09](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=249s)** we're building a Python native data backbone for your data pipelines and agents. So now that we've got the motivational example out of the picture, the temporary madness of humanity, the agentic madness, uh let's uh I wanted to spend the rest of the time motivating how LLMs became equated with autonomous intelligence. uh and then I wanted to compare large models with small models and see if we can use the smaller ones u better for the task tasks at hand and then I'll give you a few tips for using SLMs um how how to experiment with them and how to run aic flows in in in a in a sense uh the reason why we are here where we are with this uh

**[4:58](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=298s)** hype about agents uh is because of the agelong uh quest by humanity to create something that is more human than humans. To quote Dr. Eldren Tyrell from the Tyrell Corporation who of you have heard talks by Mr. Tyrell. Uh he was right. I see maybe two hands here. Um it's a reference to Bladeunner. Okay. So it's it's a bit of a u um it was a test in 1995. So almost more than 30 years ago. The concept of an agent uh was already explained in a seminal book by uh Russell and Norvik. Uh they defined an agent. So it it's not a new concept. Uh agents were defined and existed for a while now, three decades.

**[5:48](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=348s)** So uh Russell Norvick defined an agent as an entity that perceives its environment, makes decisions uh and takes actions. And why does it do it? To achieve goals. So there's a goal. There's a goal and the agent perceives the environment, makes decisions and takes actions. It's very simple really. Agents are not new. They were classic agents in the '9s, 2000s, 2010s. Uh the most important reasoning or decisioning frameworks for agents uh are the utility theory and the re and reinforcement learning. Uh if you think of elevators in our buildings uh the oices and the shind shindlers um they all used some sort of a uh reinforcement learning uh

**[6:39](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=399s)** mechanism to decide uh which floor to go first, how to optimize the routes between different elevators and using uh a common resource u uh in order to sh to to uh to bring the passenger the fastest um uh to the destination. So it's not a entirely new concept but um recently more recently I would say fiveish years ago uh language models started becoming decisioning engines so that is new uh and it um and this process started with GPT3 who of you have has you has used GPT3 in their lives all right maybe 60 70% u so when GPT3 was trained And the interesting thing that happened was it

**[7:29](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=449s)** was trained on data that contained reasoning like patterns. So it was trained on stack overflow on coding tutorials on forum answers and uh if you've ever visited stack overflow it's a site where you start ask a question and then people start responding to it uh explaining their their thinking process and giving you answers. So it's a treel like structure. It's a reasoning structure. Then a couple of years later um they and other authors have published another very important paper uh on chain of thought prompting uh and their their ev um innovation um and new idea that they brought in was

**[8:17](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=497s)** using intermediate reasoning steps and embedding it into training data. So the way they trained models was they had a prompt and the final answer, but they also had intermediate reasoning steps. The user wants me to do X. In order for me to do X, I need to do ABC. And to do A, I need to do one, two, and three. So these are the intermediate reasoning steps. And they were part of the training data. And so now uh they ran they they use expensive hardware to run these tupils of uh prompts, intermediate reasoning steps and final answers to create new models. And this is how reasoning got injected into large language models. So they became our decisioning engines

**[9:06](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=546s)** because we used reasoning patterns from GPT3 training area and intermediate reasoning steps. So now how does it all work uh in a simplified form uh in an agent uh that uses an LLM to make decisions. A prompt comes in. This is the question from the user. Uh the agent enters a reasoning loop. The reasoning loop divides the prompt into a plan. The plan will contain uh an execution of multiple tools. The tools can be API calls. They can be analytical database data access patterns or operational database access um uh patterns. And this loop continues until a token is emitted in one of the outputs. The token is final answer. It's

**[9:56](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=596s)** literally final answer final underscore answer. This is the token that the agent is looking for. Uh at which point the agent will stop create the final textual output. It will store the prompt the input and the output into a thing called memory so that it can use later on and the loop begins again uh begins again. Now some smart folks have realized that uh large language models contain a lot of useless data to operate this reasoning loop. Does it really matter to know who the queen of England was in 1980s in order to make a decision whether to call a data access um API?

**[10:46](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=646s)** Probably not. The problem with large language models is it contains compressed information from training data. These models are large which means inference is expensive. And because inference is expensive and the models are large, you cannot experiment with them as um easily as as you you would like because they don't fit on the hardware that is readily available to you. Couple of months ago um some researchers from Nvidia and Georgia Tech published a paper on small language models as the future of agentic AI. What is small? There are a couple of definitions. Small versus large. Um I

**[11:34](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=694s)** and a few others prefer a definition that is time based. So in 26 2026 uh small is um um well the definition is independent of time. A definition is whatever fits into a memory of a uh regular consumer device. And this year this happens to be maybe 16 or 32 GB of virtual uh virtual memory. With this amount of memory, a model that will fit into the virtual RAM will probably have somewhere between 10 to 30 billion parameters. Um, and the consequences of using these models typically the strengths of small language models are uh you get more privacy because you can run them on your private hardware. Um, the cost is much lower. Uh I can

**[12:23](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=743s)** literally run many of these models on on this laptop which is already two years late uh two years old. I already depreciated it. It costs me zero. However, the problem with the SLMs is it doesn't know who the queen of England was in in 1800s. So uh there's some hallucination. If I do ask it who was the queen of England, it will probably some fake me some name out of its uh waiting model. Now the authors of the of the paper h have made three statements that those were the the three main statements of the paper. Statement number one is that today SLMs are now sufficiently powerful to handle the demands of agentic

**[13:12](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=792s)** workflows which is a qualified statement. It means they didn't claim that they were as good as OPUS 4.6 for generic tasks. They only said for agentic workflows these SLMs are good enough. And because they're small, they are more flexible in where I deploy them and they're more economical. I can deploy them on local hardware. I can deploy them on really cheap Nvidia GPUs in the cloud. Uh cost becomes less of an issue. So what is important for agentic workflows? Uh there are four four real um factors that are that are important uh four important capabilities of language models as they relate to use in agents. Number one is the ability to break down

**[14:03](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=843s)** a task into subtasks. This is what reasoning is. The first task is always the prompt. you break it down into subtasks and then um you continue and um um yeah you break it down in subtasks and you keep going the subtasks into smaller tasks. The second uh important quality is tool calling the ability to initiate pass parameters and format your output. Uh quality number three is um for the use cases where you don't have the tools to solve a problem you need to generate some glue code. So the ability to generate glue code is important. And lastly the ability to follow guard rails instruction following that's also

**[14:50](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=890s)** important. Now there's a uh table comparison table in the paper which I'm not going to read you line by line but the main idea of this table is to say that for agentic the the four uh tasks that are important for agents the small language models of u a size x are now as good as large language models of 10 times that size which is pretty awesome if you ask me Who of you have has heard of uh the Berkeley uh function calling leaderboard? Yeah, a few of you. So, this is a uh leaderboard by uh UC Berkeley. Uh they keep track of uh about 110 different model families. Uh all the

**[15:40](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=940s)** important ones are there. Um GLM, CL, Quan, Meta, everything. uh vendors kind of supply the uh the execution and benchmark runs and there's verification going on as well. Uh as of December 25 um so last year December 25 I I need to check if there's a newer version. They typically do um updates every 3 months. Uh as of uh December the top models uh for these four important qualities were still the usual suspects. Claudeopus 45, Gemini 3, GLM 4.6, but they all proprietary. So you cannot use them for local experimentation. You cannot use them for experimentation in your environment.

**[16:28](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=988s)** Now in positions kind of 10 to 20, you're beginning to see open-source models. So you see things like Kim 2, uh, Deepseek 3.2, 2 and a model from Salesforce on position 18 XLAM 2. And this is the first model that is not only open- source but also smallish. So it has 32 billion parameters and it provides overall accuracy um that is comparable to state-of-the-art. Remember there there are 110 models in this leaderboard and in the top 20 you have a open-source small model. This is actually the model that we're also going to use uh for our experimentation here in our little demo recording. Uh those of you who want to understand how this

**[17:15](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1035s)** model was work uh was created uh two things. I'm going to speed up a little bit um uh my talk. Uh they used a synthetic data set with function calls uh and they they used a process called supervised fine-tuning to um create the uh the final model. So you can actually do it yourself if you generate synthetic data and u u uh use this process. So are we now ready to learn how to survive the agentic AI hype? We'll have to science the out of it as uh as per movie the Martian. Uh for this setup we'll need five things. We'll need a uh small language model and um we recommend the Salesforce XLM2 because it's open source. It's small uh you can run it today. Uh we used a

**[18:04](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1084s)** particular quantization uh of this model that actually fits 16 gig gigabytes of RAM. It's the 4bit quantization um version. Um we'll need a inference server or service. For local inference, we recommend Llama CPP. Uh there are reasons why we do this. I will explain it later. Uh for remote inference, once you're ready to move your workload to maybe a cloud production, uh there are services like together AI, hugging face. We like together AI and hugging face. Uh you might also want to consider uh a runtime service to run your Python code. There are a couple of examples. I work on tower but you can also use model or fly.io. And I recommend using a framework for aentic um aentic framework. Uh longchain is a good one. I personally prefer that

**[18:52](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1132s)** one. Uh there's also llama index and others. Uh why do we recommend llama cpp? Uh this is more a little bit for folks who use uh Apple silicon and uh like simplicity. Um uh there are several good inference servers, local inference servers. Um but Llama actually is able to use local uh GPUs on Apple uh whereas VLM for example does not. Uh and second good reason to use Llama CVP is it uses um very simple hugging face model naming conventions which Lama doesn't follow. So, uh, how does a Pyth how does a Python runtime help you in your work? Um, well, it helps you take any Python that you write on your laptop and then package it up into an application and uh

**[19:41](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1181s)** test it locally, but then ship and run in production uh remotely maybe in your cloud or in their cloud. Uh, that's what Tower does. Uh, some of these runtimes have a self-hosted version uh such tower does does have one. uh and they usually offer you an orchestrator for control flows. Uh what else can you do with tower? Well, you can do boring but necessary things like feature transformations or ETL. You can run ingestion uh frameworks such as DT on on tower. You can move data into analytical storage based on Apache iceberg. Uh you can do transformations transformation jobs using dbt core or polars or other libraries. Uh and you can even run uh your UI uh on tower as well uh including Mario notebooks or lang chain agents.

**[20:33](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1233s)** Uh a little bit about iceberg. Who of you has heard of iceberg? Apache iceberg. Okay. Fairly uh um popular uh technology here. Um the reason why iceberg becomes important with agents is because um two years ago uh some lawyers in New York state uh made a terrible mistake of using the normal GPT to completely fake a legal brief. They actually submitted this brief to the court and got burned because uh many of the case numbers mentioned in this brief we are hallucinated and they were hallucinated because uh GBT didn't have access to real uh legal cases. So since that time people realized we have to give agents access to real business data and uh iceberg has very good properties on

**[21:23](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1283s)** scaling and um uh uh performance and accessibility that allows both inference engines as well as data warehouses access a single data set stored in uh public storage. So uh how do we do experimentation uh with uh uh with the setup? Uh you'll first install Llama CPP. You'll start running a model the XLM2 model. Uh and you'll write your agent using lang chain and maybe perhaps use tower to debug and run it in production. Uh for my demo I uh I took took an example of a uh agent that retrieves stock information. uh but I made it a little bit more complex and I said uh look uh there are external stock APIs for example Yahoo uh finance uh where

**[22:14](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1334s)** the agent can take this data however I I don't want to consistently or constantly go to this external API I want to be able to uh cache my data in a database uh so this agent will make decisions if the data is already in a database it will take it from the database our lakehouse Apache iceberg lakehouse uh if the data is not there it will go to the external AP API. Uh the interesting piece about agents is how we define what they do, the business rules. So we don't do our typical airflow DAGs anymore. Uh we write business rules. We write things like you can take stock data from an external source, but you should probably take it from a from a cached source from a database uh if you can if it exists. And this is the preferred way of doing this. So we can now define our flows not in

**[23:03](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1383s)** graphs but perhaps in business rules. Uh some of you might ask well how does um uh agents uh uh decide which tools to call? It's very interesting because uh if you use longchain uh it uses information in your code including names of functions including the arguments you have and uh also including even your dock strings to feed it into the decisioning process and determine which tools which tool uh uh is the best one to accomplish a task. All right. So I have a quick recording here. I have about like two minutes to uh to go through. Of course, I use Claude to develop my pipeline. Uh and this pipeline looks like this. I

**[23:51](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1431s)** basically ask Claude to develop a tower application that writes a that is a data agent that answers stock prices. Um and the stock prices should be uh for a particular set of uh stock tickers. And um uh there's a time range and I I I'm just looking for the biggest volume of stock trades. So what cloud will do it will first learn based on examples that I provided to it code examples how to write tower applications and once it's um uh knows what the structure of tower applications is it will start generating um uh it will start generating my new application which is a data agent. Uh it uses the tower MCP server. Uh the tower MCP server provides basic commands

**[24:39](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1479s)** like create an app, create a configuration file, um add parameters, remove parameters. Um uh here you're looking at the business rules that I uh previously defined in my like in the in the prompt that I gave to Claude. These were the business rules I wanted to follow. So Claude inserted it as a as a string into my agent. And what will happen is uh I want to show you kind of the process to to deploy this agent into cloud production. I will probably take another minute. Sorry guys, I know I'm running a bit over time. Um tower requires accepts any Python code. You can literally give you give us your existing Python code and we'll run uh run it. Uh the only ask we have is uh we

**[25:29](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1529s)** need a config file to know what the name of the app is and whether you have any parameters. So this is the what we call a tower file. Uh but everything else from your Python project you can throw over to us uh as is. Um just showing you how it looks in cursor. Uh here's my here's the uh longchain agent exeutor that will be started. Uh, and we'll we're getting to the end of the uh to the reveal as they say in magic and uh the magicians. Um, all right. So, there's some validation happening. The app is almost done and now it's being deployed to our production environment uh using the MCP server. uh and I will share something with you that uh you will see later in

**[26:20](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1580s)** the demo. The first version of the app will kind of work but not really. Uh and this is a this is something that you will see a lot in your uh development of agents using other agents AI assistants. uh the first versions will probably fail for some for in this particular reason it will be because a dependency is not installed or it's the wrong dependency uh but runtime services the Python runtime services like tower are able to feed production logs back into claude so that claude can learn and adjust and this is what is happening right now uh the logs from tower are being routed into claude uh the dependency will be modified in pi project toml and the second version of the app the agent will

**[27:10](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1630s)** actually be successful. So you'll see how it all succeeds. Uh I'm going to speed up a little bit. Uh you'll have to trust me on the successful execution of the second uh second app. So um hopefully I'm at the end of my uh uh my talk. Happy to take questions maybe later or even at the table before the next speaker comes. Um hopefully you were able to uh see that um experimentation is possible. This is the recommended way of learning about agentic workflows. Small can be powerful. Uh use local setups, use open source models. Uh you don't always have to use airflow tags to define your workflows. You can actually start writing your jobs using guardrails and uh free form uh uh text. Would like to connect with me a bit later. Uh I will

**[28:00](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1680s)** be at the booth tower booth downstairs as well. You can take a uh you know QR code pick and um connect with me on LinkedIn. Uh thank you for attending this talk. Appreciate it. [applause] Uh we'll take maybe two questions from the chat. Uh so let's say you uh let's say we have a scenario for a multi-agentic workflow. Does each agent need to have its own SLM? In the case that each agent does not does a specified task, would that be more efficient compared to using a single LM? >> Um, well, you wouldn't use a custom SLM per task. You would um you it's totally fine to use existing SLMs

**[28:50](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1730s)** such as the XLM2 from Salesforce and just modify your prompt and your business rules. um works totally well. Um you might want to maybe invest later on in uh fine-tuning uh a model and actually create your custom copy of a SLM for your task based on synthetic data that you will generate and run through uh a model generation process but you can start with existing versions of SLMs. >> Okay. Uh for selecting a SLM, what would you say a user should prefer? High parameter with low quant quantization or higher quantization with lower number of parameters and why? >> Uh right. So this is kind of a trade-off you'll have to make. Um remember I

**[29:38](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1778s)** recommended a 32 billion parameter XLM2 model with 4bit quantization. Um I I I think you the the 8 billion parameters didn't really work for us. Uh they are still stupid and dumb. Uh but kind of starting with 30 billion parameters, uh things get uh interesting. Uh for agentic workflows, they begin really good. They start getting really good at uh reasoning loops. Uh they they don't they terminate correctly. They don't run infinite loops. Uh one of the interesting things you'll encounter uh these agentic loops can never terminate. um they will continue running uh because the SLMs are incentivized to call as many tools as they can. Uh this is a interesting fact that you will learn. Uh I would say starting with 30 billion parameters uh 4bit quantization is great. Yep. It will

**[30:29](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1829s)** fit your consumer device. Um if you can use a 70 billion parameter model, you'll get slightly more accuracy. >> Uh do we have any anyone in the audience that would like to ask a question? We can pass a mic. Thank you. Uh quick question to the uh to the leaderboard you showed, right? So 70% was like the the highest number 70ish. >> Y >> that does not mean that >> 70% of answer or questions are correctly answered. It does. Yeah, it does. Sorry, I'm leading. I'm >> No, no, you you you guessed my question, right? Because if seven out of 10 requests were like garbage, agent workflows would be like garbage, too. combined score of four uh other scores. Um uh you can actually if you go to this

**[31:16](https://www.youtube.com/watch?v=nk5BNz8v_9E&t=1876s)** leaderboard you'll see uh individual scores. Uh the numbers here the 77.47 doesn't mean that 23% of your questions will be garbage. Answer it in uh wrongly. Um it's a combined score of four other scores. Think of it as a index. It's just a index and accuracy is the wrong name for it. It should be called overall index. Yep. All right. I'm happy to take maybe questions at this table to give the next speaker a chance to uh set up. Uh I will also be available uh downstairs close to the mark plan plenary uh for more questions. Thank you. [applause]
