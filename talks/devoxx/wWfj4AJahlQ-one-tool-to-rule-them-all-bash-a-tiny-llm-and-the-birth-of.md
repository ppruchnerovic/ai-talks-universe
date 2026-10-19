---
id: wWfj4AJahlQ
title: "One tool to rule them all: bash, a tiny LLM, and the birth of a coding agent by Philippe Charrièr"
slug: one-tool-to-rule-them-all-bash-a-tiny-llm-and-the-birth-of
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2026
speakers: []
channel: "Devoxx"
duration_min: 30
published_at: 2026-10-06T05:30:08Z
video_id: wWfj4AJahlQ
url: https://www.youtube.com/watch?v=wWfj4AJahlQ
youtube_url: https://www.youtube.com/watch?v=wWfj4AJahlQ
tags: []
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# One tool to rule them all: bash, a tiny LLM, and the birth of a coding agent by Philippe Charrièr

**Speaker not identified**

`Devoxx` · `Devoxx` · `2026` · `30 min`

[Watch the recording](https://www.youtube.com/watch?v=wWfj4AJahlQ) · [Conference site](https://devoxx.com/)

## Description

*No description published on YouTube.*

## Transcript

*3,643 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=3s)** [music] [music] BACK. [music] [music] DOWN. [music] OKAY, it's me. Uh, hello. Uh, thank you to be here. Uh, my name is Philip Sher. As you can hear, I'm French, but I will try to speak English correctly. Uh, I'm solution architect at Docker. That means I'm the geek of the team and I'm helping the customer, the account executive, the solution engineers and other people um

**[0:53](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=53s)** at Docker. You can send me some question if you want uh with my um job email and you can follow me on blue sky. Today the goal of the presentation is to explain what is an adjunk loop. So I will use local model because I like to work with small uh language model. For this presentation I'm using a model that is that was made by um Jet brand. So the model name is Melum 2. Uh it's a model with 12 billion parameters and the model at each token use 2.5 billion of parameters. That means you can use it on um correct machine uh with a MacBook Air

**[1:41](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=101s)** for example. I prepare this presentation with a MacBook Air and 32 GB of RAM. This computer is a lot powerful. My LLM engine is docker model runner. So docker model runner is a wrapper around uh lama cbp or vlm. You can choose the model engine and it's an open source project. I will use sorry for that golong and gen kit but my source code is really I did the source code without the EI almost and it's easy uh to reproduce with cotlin and even java [sighs] uh I started to do it in cotlin uh and it will be inside the the repository little disclaimer uh I'm using small

**[2:30](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=150s)** models so small models can be unpredictable so sometimes Perhaps if I'm not lucky, my demo will uh fail. But it's not my fault. It's the fault of the model. So uh for that we need a model. Most of the time I will search my model on face. So like this I will just increase the size and I use the drop done money like this one. and I choose docker model runner and I just copy the command and go to a terminal and I paste the command like this. It's very fast because I already did it before and I pulled the model uh before

**[3:20](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=200s)** the presentation and I can ask uh hello I'm Phil what can you do for me this is the first contact with docker model runner model runner is a plugin of docker desktop so if you use the desktop you can I need to increase again. You can go to the model section, go to the request panel and you can see my request and the response of the model. It's very useful for debugging generative application. You are not obliged to use the model runner. If you want, you can just change the endpoint and use something like for example and the all the source code will

**[4:10](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=250s)** will work. Let's go back to the presentation. So let's talk about uh function coding. So function coding now most of the models are have the tool support that means they can understand your intention to run something. So for that the model need a catalog of tools to compare with to compare with your question like uh I would like to know the [gasps] temperature or the weather at envelver. So the model will uh recognize the tool get weather and the model will be able to extract the parameters from your question. Very important the model cannot execute any tool. the model can

**[5:00](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=300s)** only generate text or data and then your application or the agent will execute the tools. Uh for example, if you type uh what is the weather in on verb today, the uh agent will send a payload to the model with the list of tools like get weather a description. It's important then the model is able to recognize the tool and the parameters and I have another tools for example send email with all the parameters. The model will um think with this data and generate a completion and we'll return something like the tool is get weather and the value of the parameter is envelurp and

**[5:50](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=350s)** then with that the model will be able to create a new answer and the agent will be use the JSON payload to execute the get weather tool in a more visual way. uh we can see like this it's a little bit small so I'm I am a user I will ask to the agent uh I need three keyboards and to my what is the total then the agent will use this information and use the command from genkit genkit generate and pass the list of the messages and the tools and then genkit will create a tool loop to detect. Thanks the model the the tool call. And if the model emits a tool

**[6:42](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=402s)** call, the agent will execute the related tool and the agent will add in the list of the messages to keep the history all the tool result and at the end the model with all this data will provide a final answer. um a little demo first. So this is this one. The source code is very easy in fact to understand because go is simple in fact we have the ID of the model some sampling parameters. So sampling parameters is uh the instruction to help the model to uh have um a kind of behavior. the C system prompt. So it's the first

**[7:31](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=451s)** message. So you are a helpful assistant for a computer store for example. A list of question how much is 21 + 21? What is the price of mechanical keyboards and so on and then I will connect to the model thanks to a client. I choose an open API compatible client because docker model runner is uh exposing an API uh which is openi compliant and with genkins and the model I will able to connect to the model I'm creating a toolbox so the catalog of my tools so you can see that I have four tools a tools is very easy to define with genkins It's only a function with a description

**[8:22](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=502s)** to help the model to detect the tool and uh the the model will use the signature of the function per input. So a and b for the parameters [cough] [clears throat] and then I will loop into the array of questions. I will create a set of messages. So with the system message and the user question and then after that it's very simple. I just run genkit generate with the model name the list of messages the catalog of tool of tools sorry and with the config and that's it. So let's start it

**[9:10](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=550s)** go on dot and let's see if the model is with me. So the model is able to do the addition to find the price of the product. The model is able to detect that there is several tool call inside the user prompt. So to find the price of uh keyboard of the mouse and to do the multiplication and the total and to check that a model is or not in the catalog an itm sorry um same code but with different tool um so it's the same uh exactly the same code in fact but this time I will use uh I I call

**[10:00](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=600s)** real world commands but I will use something like curl uh grape and so on. So for that I created a new toolbox and for the curl command for example I'm defining a new description and I will run the curl command from the go code and this is the same with the the other tools so and the list of questions sorry it's important uh I will ask the agent to fetch example.com to create a go module with a name inside a directory and to check if the word module exist in the go mode file. So I will open a new terminal. The rest of the code is the same as the

**[10:51](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=651s)** previous example. Go on dot like this. So the model was able to fetch the page. You see it created a playground directory with a hello directory with a go mode file and the model detected that module exist in the go mode file. So you see the the the the agent can interact with uh with your machine with your laptop. Now if I need to uh add new tools like copy mkdia and so on I need to change the source code for each tool and each time I'm adding a tool I'm adding a description and then I will

**[11:41](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=701s)** increase the size of the context window. The context window is the place that the it's like the memory of the model. So the more the context windows is big, the less the model will be able to stay focused. In fact, I'm speaking about small models or local models. You don't have this kind of uh issue with uh entropic endpoint for example. So I can do something else. I will remove all the tools and I will use only one tool. I name it bash because in fact all the models [snorts] the local models already know thanks to their training corpus the shell and unix command like curl g find and so on and then thanks to

**[12:34](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=754s)** that you don't need to describe every tool so you will save space uh and then you will save space inside the context windows and if the model don't know a tool the model can use the d-help option or even the man command to uh discover how to use the the command. So I used again the same source code but with a different toolbox. So if I return I in fact I duplicate the source code. If I return inside the code I ask the same question. I did one more which version of Go is installed here. And this time my toolbox contain contains only the bash uh tool. So this time the description is a little little bit more

**[13:24](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=804s)** longer to help the model to understand what he can do with the bash tool and then I will run I I created a kind of helper to run command detected by the the LLM. So let's test it. Uh where I am I will go inside this one. Yes, I will type go run. So remember I have only one tool this time. So the model was able to fetch example.com to create a new directory to

**[14:15](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=855s)** change directory and create go mode um in it to check if module exist inside go mode and run go version to check the version of go. And for this one again the go mode file was created with only one tool for doing in fact everything. [cough] So what I did in fact is the foundation of all the coding agent. I took the code from the last example and I do some gardening and I put the

**[15:04](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=904s)** code inside the loop. So I mean a loop where the user can type a message and wait for the answer of the model. Uh this time I'm using YAML file to be able to change the settings of the agent. Again I'm using only one tool, the bash tool. Um, and I put the aent loop inside the aent packet. Again, I'm using the car model runner for the connection to the LM engine, but engine, but you can use uh the engine you want you want. Uh, let's go to see some source code. Where is my source code? Yeah. Internal agent. Aent go.

**[15:56](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=956s)** So this is my agent loop. I'm waiting for the user point. So hello, I'm Philip. I would like to know the weather in on verb. [gasps] Then I will update the list of the messages to keep the history of the conversation and then I will call again the generate method of the um of genkit in fact of docker model runner and I created all of the plumbing inside the generate method but it's the same almost the same source code as the previous example [snorts] and I will update the history of the message with the answer and at the end I will display all the tool calls to check that the agent or the LLM was able to uh

**[16:45](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1005s)** recognize a tool call and the agent was able to run the tool call and that's it. So let's run it. So I build the code and now I have a Bob agent and I will run my agent uh inside a sandbox because this time my agent is able to do a lot of thing on my machine. At Docker we did a sandbox we name it uh SBX. So to to be quick it's a m micro virtual machine and inside the microvm you have a docker engine uh so you can run docker without any problem without any uh container escape and the sandbox is coming with kind of proxy that uh will protect your

**[17:37](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1057s)** API keys for example. So the agent is not able to see the value of your secrets and uh we will have we will have a booth tomorrow. So if you have very technical question about SBX don't hesitate to come at the booth and we have stickers of course. Uh so let's start uh the sunbox like this. Okay. So uh oh I need to show you the settings of my agent. Uh so I'm using meloom 2 again. Uh this endpoint to connect to the model runner and I added some instruction to

**[18:28](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1108s)** the system prompt. I even add some uh instruction about go please. Go please is the [gasps] um language server protocol implementation for golong [gasps] and I have my sampling parameters. So this one let's start bob for real. So Bob [sighs] go please agent. So the UI is very very simple. Uh I did some script to use it. Yes. So I will ask Bob to create kind of hello world program with um a

**[19:22](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1162s)** dog structure, a cat structure, human structure and a human as a dog and a cat. I will ask Bob to save the program to build the program and to run the program and I will cross my finger. Uh no it's not ah copy. So let's see what will happened. Apparently Bob created the hello directory with the mango file. Okay, he's thinking again. He build two times. So I have a hello program and the main program. I don't know why, but I think the same program. Uh and he was able to run the program.

**[20:11](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1211s)** So let's have a look to the source code. I have a dog structure, a cat structure, human structure with a grit method. Okay. Uh, please run it. Don't ask why I say please. I have no idea. So, the model is able to run the program again. Where is my script? Uh, I will ask where is grit defined? And the model was able to the the agent was able to uh tell me where grit is defined. But you see there is no command. The model use only its memory. Uh so let's ask something like explain what is go please.

**[21:03](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1263s)** So apparently the model know the go please cla. So I will ask the model to run go please help. So the model run go please help and now the model has all the command in the memory that means that the model know I think how to use go please so search great in workspace and then display the references there is a B so you see the model was able to use go please workspace symbol and go please reference es and give me some information with the number line. So

**[21:53](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1313s)** thanks to go please we have more information than using gp for example. Uh let's try again use go please to tell where is defined and what calls it. So thanks to the bash tool, a model is able to use with the documentation uh almost any CLI. And I will try something else like asking the model to rename the grit symbol with welcome using go please of course. Apparently it's okay. Let's just check.

**[22:43](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1363s)** You see the model was able to use go please rename dashw for write otherwise the the agent won't do the the change. Uh yes it did. It did it. Run it just to check. Okay. Perfect. And for um bigger um uh codebase you can use for example um red grip. So reg is a CLA to uh dig in the source code and find some information. Uh yes. So

**[23:33](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1413s)** to conclude but it's a long conclusion in fact um we saw the fundamentals of uh that the fundamentals of coding agent is in fact very simple to go further you can use other CLI like uh I did with ribbre but uh there is est g and so Um you can add other built-in tools. So I use only bash but sometimes you need more like uh edit tools for editing and making diff between uh several version of same files. You can add a skills tool and then your model will be able to read skills and to use the skills. Uh

**[24:23](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1463s)** something that is very important, you should add something um you should implement something to detect the hallucination and the silent andless loops because a small model sometimes is running without doing nothing and then your program never stop. You can use rag for retribal augmented generation to add some knowledge to the to the agent. You can implement context compression. That means you will take all the history of the messages, ask the model to do a summary and replace all the history with the summary. And then you will again you will save place uh with your um context windows. You can use MCPU of course for um for adding super power to your agent and then you will create a

**[25:15](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1515s)** complete agent. um when I'm when I prepared this tool in action I wanted a longer version of the presentation in fact so and you see there is there are other steps inside the repository but at the end uh I add a new side project I call it mini uh so it's a nent that is optimized for the local uh models and by the way I'm using it uh almost every day for my day-to-day job um with bigger model of course. Uh let me show uh show you mini me. Uh it's just the the the result of the the the first demonstration.

**[26:05](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1565s)** Uh I need to open a terminal. I will. So, it's the same principle with a better UI. Um, and I can search for a file like this and then >> [sighs] >> uh tell me what are the toid. So I added a lot of guard rails for detecting the hallucination and so on.

**[26:53](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1613s)** Uh you can use it with a lot of um local model. And uh by the way uh David is David Gajou from Docker and he will present uh a deep dive about um EI agent and about Docker agent and uh a talk about how to create an EI agent without code only with YAML. So don't hesitate to uh have a look to uh the the deep dive or the the talk or or both. So um thank you to be here. First you can get the source code of all the presentation on code be with this um QR code and with the with with the other QR code you can put some feedback. Um

**[27:46](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1666s)** and please no remarks about the accent. Um one more thing um I present you docker sandbox SBX uh we did a cloud version of SBX so cloud sandbox. So if you scan the QR code uh today you can have a credit to use um cloud sandbox so on the cloud otherwise uh docker sbx uh is running uh locally on your machine for for free but the they they they share um some piece of code. Thank you for your attention [applause] and uh if you have any question I think

**[28:35](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1715s)** we have less than two minutes but I will be outside. Yes. >> How smart does a model need to be to be able to call? Um in fact uh two years ago people said that it's not possible to do a uh function coding with small model but uh some of them uh appears like the small quen for example and they were not bad but uh one other the name is Lucy I think was pretty good in the test and no uh Melum for example is pretty good and he almost never missed a tool Uh but I think with if you start with a 4 billion parameter model with the support tool you [sighs]

**[29:24](https://www.youtube.com/watch?v=wWfj4AJahlQ&t=1764s)** should be able to do almost all the demonstration I did. Uh the coins are pretty good and uh Lucy and um Rano I think from Menllo. You can find the two models on Ging face. uh they they have more than one years I think but uh they are pretty good with function calling so you can mix this models for the function calling and other model for the rest of the completion other question I think it's too late but we can speak outside thank Oop.
