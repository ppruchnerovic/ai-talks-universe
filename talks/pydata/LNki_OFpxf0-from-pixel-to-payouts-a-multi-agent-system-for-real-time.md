---
id: LNki_OFpxf0
title: "From Pixel to Payouts: A Multi-Agent System for Real-Time Insurance Claims Processing"
slug: from-pixel-to-payouts-a-multi-agent-system-for-real-time
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Claudio Giorgio Giancaterino"]
channel: "PyData"
duration_min: 30
published_at: 2026-08-04T22:20:22Z
video_id: LNki_OFpxf0
url: https://www.youtube.com/watch?v=LNki_OFpxf0
youtube_url: https://www.youtube.com/watch?v=LNki_OFpxf0
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# From Pixel to Payouts: A Multi-Agent System for Real-Time Insurance Claims Processing

**Claudio Giorgio Giancaterino**

`PyData` · `PyData` · `2026` · `30 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=LNki_OFpxf0) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Claudio Giorgio Giancaterino demonstrate how a sophisticated multi-agent AI system can disrupt the insurance industry by transforming raw damage photos into real-time, auditable claim payouts.

Speakers:
Claudio Giorgio Giancaterino

Description:
Insurance claims processing for vehicle damage is traditionally a slow manual process, often taking weeks or months due to the sequential nature of investigation, cost evaluation, and approval. Traditional deep learning approaches using Convolutional Neural Networks (CNNs) for this task are often limited by a lack of labeled datasets, a lack of adaptability to new pricing, and a "black box" nature that hinders explainability.

To address these inefficiencies, a multi-agent system was developed using a Python-based framework to maintain governance and stability without the constraints of external orchestration libraries. The system utilizes a ReAct (Reason, Action, Observation) loop, allowing agents to reason through tasks, execute functions, and observe results. The architecture consists of an orchestrator agent that manages a sequential pipeline of specialized agents: a vision agent powered by the OpenAI Vision API to identify damaged parts and classify severity (minor, moderate, or severe), and two cost agents using the Perplexity API to provide comparative repair estimates from web-based market data. A final shop finder agent identifies local repair facilities based on the user's location.

The system is deployed on Hugging Face Spaces using Gradio. In testing, the pipeline processes a claim in approximately 50 seconds. Key advantages over linear prompt flows or CNNs include modularity, the ability to perform end-to-end assessments (from image analysis to shop location), and transparency provided by the ReAct trace. While cost estimations remain approximations based on web searches rather than static databases, the system demonstrates how multi-agent collaboration can automate repetitive data review and accelerate the insurance payout lifecycle.

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

*4,314 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=LNki_OFpxf0&t=6s)** Thank you all to having me today here. Uh nice people, nice location. I'm happy and uh today I want to speak about the agent in the claim processing and um much more in the car damage evaluation. But before to start, I want to introduce myself. I work with numbers with uh uncertainty and risk. I'm an act during the day and I play with data in the AI and data science in the free time. Okay, look at the agenda is really h rich. Uh we start with the motivation, the use case introduction and we go also with the demo. So the motivation is coming from uh many years ago, not many but maybe six 10 years ago and about the whole

**[0:58](https://www.youtube.com/watch?v=LNki_OFpxf0&t=58s)** idea to develop an um deep learning car damage classifier. uh they was simple to use an app to upload the image and with a binary classification or the multi-classification depend of the damage part and also to uh annotation with the uh crypair cost. What is the issue? Issue that there wasn't the data set with the labels and also with the annotation cost. So I shoved the the the idea but some months ago uh this idea come back me in mind uh with because I thought about the use the agentic AI. Okay the this is the the state of heart about some years ago when I have the the idea of develop the app with the deep

**[1:47](https://www.youtube.com/watch?v=LNki_OFpxf0&t=107s)** learning classification. So I found this streaml and they are based on the binary classification multiple classification or otherwise with some parts with uh scoring but something about the guessing. So if you look about the claim processing is really slow because uh he start with when you have a car accident the customer give the notification and submit the documentation. Then there is a um clman handler that for the claims uh to investigate about the fault the valuation of the cost and there is also the pro approval about the the claims and then uh the there is the about the communication and uh the reimbursement

**[2:37](https://www.youtube.com/watch?v=LNki_OFpxf0&t=157s)** about the payment. So the claim processing start for can be for two three weeks for a simple claim or otherwise add more than one month one more than one year for uh litigation uh claims. So the idea what can be is if you use an agent AI you can um really became your claim processing faster with the data driven process and but before to start to talk about the agenti the evolution is coming from the transformers. Yes, because uh um years ago from uh the communication the paper attention is all you need from Google in 2017 uh these uh transformers changed everything. Um the idea is brilliant because data are not

**[3:27](https://www.youtube.com/watch?v=LNki_OFpxf0&t=207s)** processed sequencing to sequence but at once with attention mechanism that give the weight give the much importance what is the part of data must matters to each others. In this way you can uh take about the long range dependency between data. The model language language models are uh using transformers. Yes, different from the first used for translation and are similar for example for the GPT for the text generation to create responses text responses. The revolution for the computer vision is coming also from transformers because transformers is flexible and you can use transformers also for visual language models. Just to use a visual encoder that uh uh capture the images create the

**[4:19](https://www.youtube.com/watch?v=LNki_OFpxf0&t=259s)** uh visual features is this visual encoder is trained on large image or text data and image and create these visual features. Then there is a projector that is a bridge between this visual encoder and the transformer. Uh this uh projector map the visual features into the embedding language with the image tokens. In this way the transformers have the same uh embedding with the image tokens for the for images and text tokens for the text and can process both. So this this is the idea for a visual language models that can be now the state-of-the-art for the computer vision. But what happens if you give to your visual language models or language

**[5:09](https://www.youtube.com/watch?v=LNki_OFpxf0&t=309s)** models the possibility opportunity to act to interact with the environment became an agent. So an agent is a system where is able to um uh to perform a a task complex task or a simple task in one uh given by reasoning by the planning by the action. So it start with the perceiving with the perception retrieving the information from the external environment. And then uh reason and the uh reason about the act to do the the decision to do to make do and in this way is handled by the large language model or visual language models and then with action interact uh with the environment just calling some

**[5:59](https://www.youtube.com/watch?v=LNki_OFpxf0&t=359s)** tools such as APIs or other quering database or something else. At a layer up of this there are the planning that the the agent can plan breaking down the complex task in a subtask and also is able to give the priority each step. Also there is the memory and knowledge and with this memory and knowledge there contain the um retain the context of the interaction and for for some um agent there is opportunity also to um learning with some external knowledge. So why they use the agent? they use agent is why because they are able to give some complex task or repetitive task in autonomous way without the inter

**[6:50](https://www.youtube.com/watch?v=LNki_OFpxf0&t=410s)** human intervention. So they are also able with the tools to adapt of the context and in this way given that they are able to give some repetive task they are uh improve the augment the human knowledge uh with for brainstorming for uh problem solving for automation and they can be used in for repetitive task to increase the productivity link people with um into a level activity a um much more efficient, much more important activity. So improve the efficiency in inside the company and also for the customer is able with the knowledge with the external knowledge can be also memorize some personalization. So give some

**[7:38](https://www.youtube.com/watch?v=LNki_OFpxf0&t=458s)** personalization experience for the customer. So there are many uh opportunities to use agent. There are different type of agent uh just the two extreme point two extreme one is using a single agent in this way you have uh one agent that give the all task but uh it's easy to realize but it's less scalable but instead the other side there is the agency there with the agency you have multiple agent that work that collaborate in this way they are processing much more information and they are really good in the company but the problem is coming from the coordination. So what I realized I realized an app that and the stack that I used is coming in with using the python framework. I decide to don't use

**[8:26](https://www.youtube.com/watch?v=LNki_OFpxf0&t=506s)** any external framework for one reason. Okay, you have stack, you have lchain graph, you have power but you have some strict uh um framework. So with Python you have governance on everything you don't so you're free and you are not um linked with the external breakchange. So for the company you could be good because you have a stability and you are easy uh to implement and also you can grow in your implementation and there the others are framework the API open eye and perplexity open eye for the computer the vision agent and perplexity for the cost agent and the final shop agent. The deployment happens on hug interface. So for this reason I chose my first choice was gradio and okay for the

**[9:14](https://www.youtube.com/watch?v=LNki_OFpxf0&t=554s)** backup streamllet uh okay before to start with the demo uh we just um an introduction. Okay, I start months ago just for a simple pipeline with B based on the function the call API with open eye and perplexity for the this type three type of agent uh cost the visual agent the cost agent and sh the shop finder agent but it was easy uh so it don't it didn't uh adapt to the contest so I thought about something much more debable much more audible I thought about the to use the agent system with agent system but thought in in this way creating the react loop reason action

**[10:05](https://www.youtube.com/watch?v=LNki_OFpxf0&t=605s)** and observation with the reason okay you have the sphere react to the agent state there is what happens that the agent in this way think about the the um decision to make then there is a action so with the reaction action the agent and decide which function to use with the and then there is the um action fn that in this way it works because in this way call the API and retrieve the data the raw data and with observation there is the uh sees the data they are registered in the logs summary. So uh each agent have internal state with a Python dictionary with and when you call when you start your agent you

**[10:53](https://www.youtube.com/watch?v=LNki_OFpxf0&t=653s)** call with the create a state agent agent state with the type of agent and with the configuration. In this way you have uh the legend that is explainable. You have a self tracking with the direct trust and also is um stateful because you have every state. So this is the architecture of the of the app. Uh you upload the future with the location. You have the uh this information go to the into the orchestrator agent. This orchestrator agent map everything. So this plan uh each step of each agent. The each agent works sequentially. There is the vision agent is the first that analyze the images and provide the detailed information with the damage parts also with the um classification of

**[11:42](https://www.youtube.com/watch?v=LNki_OFpxf0&t=702s)** the severity minor moderate or several this information does if in to the context and arrive to the two cost agents uh in this way they have there is the dealer service and the independent shop why two cost agents because I don't have a data set so I use only the picture from Kaggle and um what I've trust about the the the cost the estimation of the cost using two uh cost agents. I have the opportunity to have a comparison because this this con this estimation coming from web and then there is uh the shop finder that it works looking about the uh from three to five uh loc shop location and shop repairing cost into uh the location and

**[12:32](https://www.youtube.com/watch?v=LNki_OFpxf0&t=752s)** then this information are grouped and then for the output in stream radio interface user friendly phrase. Okay. Okay, now I uh start with uh the the app. Okay, the demo live. Okay, you can see this is the um gradu on face. I upload the I written the API. I upload an images and I Okay, I put the the location just uh you uh push the button. Okay, it it takes just uh less minutes than 30 seconds. Uh so it's really uh quite fast, but because there is just one uh one loop and it's a I think that it's a really good um achievement for uh

**[13:22](https://www.youtube.com/watch?v=LNki_OFpxf0&t=802s)** for for for the customer also for the for the worker because it can be used both for the customer and both for the um the the worker. So you have the first of all you have the damage analysis in this way you have the description of the damage analysis you have the affected part in this way okay the uh hel bonnet form grill assembly left half map assembly right hand map assembly so on and you have also the classification in this way is several uh after that scrolling down you have the two comparison about the the the range of the cost and for each cost there is also the breakdown of the each component. After that also there is a shop finder. We have the description of the uh each

**[14:11](https://www.youtube.com/watch?v=LNki_OFpxf0&t=851s)** um repairing repairing shop with the details. Uh okay. And there are address, phone number, website maybe. Okay. um depends and okay in this way also we have at the end the uh react trace that is the nice things of this app because and we look about for instance we start with the orchestrator uh the to have received inputs with image yes and location M Germany I need to determine which agent to activate in what order the action is a build exaction plan so observation we have exction Plan will with four step vision cost primary cost primary cost alternative and shopfinder to I have a plan with four step I will execute H aent priority order vision

**[15:00](https://www.youtube.com/watch?v=LNki_OFpxf0&t=900s)** first then cost estimator then shopfinder passing results downstream and context action exact executive agent plan is the function observation all for agent task completed vision cost primary cost alternative shops for the vision agent we have uh the to I have received a car damage image. I need to call the vision model to identify damaged parts, assess the severity and extract a structure description. The action is the call open vision API. The observation is a visual API response successfully detected severity several confidence 78%. Cost agent we have the two cost agents with the tote I have damage information with severity server and I need to generate a detailed estimate for the primary repair philosophy in Munich Germany using Euro. I will query the perplex API with the structural

**[15:49](https://www.youtube.com/watch?v=LNki_OFpxf0&t=949s)** requirements. The action is a call of the API plex API. The observation is the cost API. The primary responded successfully estimated the the range. The same for the afterm market and also the shop finder agent. Yes. Okay. The to need to find out body per shop near Munich, Germany. I will require perplexity which strat request for shop names, addresses, rating and contact details. The action we have they call the API and then the shop the observation is a soft share shop search API responded successfully for location Munich Germany retrieved a shop listing three selection three section found in response. So this is the the app that I realized uh we come back to the presentation and to the slides.

**[16:37](https://www.youtube.com/watch?v=LNki_OFpxf0&t=997s)** So this part we have uh just watched about the demo but just to have a comparison between the generative AI the antici and tools using about convolutional neural network. So the the transition what happens okay with the think about the convolutional network you have a general in the internal generalization if you want to uh you change your task you have to retrain your model if you have your goal is only to make a classification single classification binary or multi-classification single task so is not adaptatable with the thatatability with the new prices require new training and also about the explanability is is a black box and also they are monolithic scripts. So the entire pipeline if you

**[17:25](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1045s)** change something you need to retrain with the genetic AI this with this model what happens and the first of all yes you have the reason patterns so you have something with the react loop you have a trace about your um you have a trace of your reasoning and also you have a description you have a language description so it's much more uh also for the goal you have end to end assessment much more tasks So you have a reply to much more questions the cost the the the analysis the the cost and also the find the repairing uh shops and also they you have all much more data update with the market because you have a web search data from the market is considered transparent because you have

**[18:14](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1094s)** the the description of each action from each agent and also from the modularity you can switch each step each specialized agent replace with uh also with the convolutional network for instance or or you can add other stuff other agent the other ways there are some constraints for instance yes uh your estimation is approximation because I haven't data set so it required um for instance for your this this cost estimation is coming from the web search so is necessary the professional uh And so human in the loop then also depend of the quality of the image because if the image is blurry yes your estimation is is bad and um okay you don't have for

**[19:04](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1144s)** instance uh your static you don't I don't have um a static database in this way what happens that the data is not guaranteed uh from this static database so it can be used for instance it can We implemented uh a database for a comparison because now I using only market search and then for for about the regularity the insurance world is much more regulated. Yes there is the h is auditable because you have the trace of each agent but maybe for uh the put in production requires other alignment. So what I've um [clears throat] learned from this experience from a for building from a

**[19:53](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1193s)** scra scratch is is [snorts] important because you will learn how it works the ecosystem and also is possible to realize for instance a multi- aent system. This app can be used as a starting point for the claim processing and maybe can be used at the initial process then in the building from scratch before to transition on external framework because at the moment the external framework are instable because they are changing a lot and also what is the important from the multi- aent system the opportunity is that you can um break down your complex tasks such as claim processing into subtask and then you can create end to end pipeline and then okay uh you can create your uh multi- aent system not only with the

**[20:41](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1241s)** specialized agent but also using uh different brains using so different type of language models visual language models I use open eye and use perplexity for different uh task okay there are the reference and that's it THANK >> [applause] >> THANK YOU VERY MUCH FOR YOUR INTERESTING TALK CLADIO and thank you for asking questions. If you have more questions you can access here talks.pyond and ask them right now. We have a little bit of time and the first question. >> Yes. So okay >> from the audience is how do your agents calculate confidence scores? For example, calculating confidence and uncertainty scores of a multiclassification task in the image

**[21:30](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1290s)** detection is a statistical challenge that vanilla agents are not capable of. >> Yeah. Yeah. Yeah. Exactly. This is important this question really good question because I talked about the confidence uh what happens this confidence is given by the the system by um the retrieved by the the agent h so is not I'm not able to check about how is calculated this is a a blackbox point but is important I consider to use the confidence for one reason uh because with the confidence you can understand how your result is good and for instance for in the next development for to to give the ne next step in the uh pipeline. So yes that uh uh good

**[22:20](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1340s)** question because you building a deep learning model you have the framework that you can build your confidence here is external confidence. >> Thank you. The next question, how do you quality assure the proposed multi- aent system? Okay. The it's difficult because good question because okay the problem exactly is that I don't have the data set uh welcome if something uh want to propose a data set with the database with cost and we can have the um quality assurance quality evaluation about the the multi- aent app. I created the uh two cost

**[23:08](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1388s)** agents for for instance for have to have a comparison and um but yes um a good compare a good quality is coming from a benchmark and I have to create so some that is working with this type of data is welcome to give the help for a comparison. >> Thank you. The next question is how do you leverage insurance conditions documents? For instance, how would you decide coverage determination using LLMs? Uh coverage determination. Oh, okay. Here there are not about the documents. Is this this app just about evaluation of the picture and the

**[23:56](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1436s)** location? So how it can work? It can work that you have the app the customer also the worker upload the picture is just for one picture but you can upload many pictures can realized and with the location you have evaluation it can be extended uh with for instance you think about server you can create my other app and you can assemble this app and you have for instance the um about the documentation you can retrieve a documentation from the the customer and then you can build a just a a rich pipeline. So this is a just a a piece of the claim processing. >> Thank you. The next question is how is such a system deployed in production? Which stack does it use?

**[24:44](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1484s)** >> Okay. Uh the is deployed in on a face. uh you have the address for uh for instance in the in the the slides also in the in the channel of the pakundi and uh from the my github repository and uh what happens that uh I deployed on dagens using gradio so simple deployment uh easy deployment not sophisticated deployment so to put in production require much more uh work so it's just a a prototype for instance But I think that it works and it this was the as I said the Python framework essentially. >> Thank you. The next question is why do you consider the agents more

**[25:34](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1534s)** transparent? How do you explain 78% for example? >> Yeah. Okay. Exactly. The the question is interesting. Okay. uh what [clears throat] happens uh what is the reason that I consider much more transparent uh pick up a learning model convolutional neural network okay it's fine is the state of art of some years ago it also can be used now but you have a deploying model that is a black box the agent inside you have the or visual LM is a black box what is the gain that you have between the previous system you have the trans you have the react loop you have the the the summary of each action taken by the agent the reason to the um the action so the calling from

**[26:22](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1582s)** the API and then the servation so you have the each step is just documentated so in the just you have the movement of the agent yes inside I am agree is a black box but uh it's it's just an upgrade respect despite of this convolutional neural network what happens about the scoring 78%. Uh I the threshold is 70% I put is a a general model with a computer vision from GT5.2 too you can improve your accuracy with the finetuning model just I think that is good with the generalization model you have it is used in a in a shot in zero short learning way so it's good for my for my opinion is good but it can be

**[27:11](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1631s)** improved with the uh fine tuning model fine tune yes >> thank you cladio the next question is given the flow seems very linear yeah >> have you tried to compare the multi- aent architecture versus a prompt flow-based architecture If so, where do prompt flows fall short in your experience? Okay, there I if you I haven't done okay uh just I created the the pipeline at the beginning just a linear flow and uh okay then I haven't now to uh to watch but uh what happens that you have the just um description you don't have I haven't the the multi classific the the the classification of the severity and I adjust the the range

**[28:01](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1681s)** of the of the cost. So the next step that with this app is much more informative than the previous depend you can build just with a flowchart uh but what happens that is not adapt adaptable with a contest if you use the computer uh the the vision agent and the vision agent give the information that is vag with a flow simple flow chart. uh this information is passed to the cost agent and the cost agent doesn't have the opportunity to improve the information. This this bug information is spread into the downstream falling in the into the the cost estimation. Instead with this multi- aent system the opportunity is is much more informative give the classification. So if the failing about the the cost vision in some some for

**[28:51](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1731s)** instance give a gav vag description but give a classification the cost agent is reason about which type of the cost estimation to do. For instance if is a server decide to give a detailed cost estimation. If instead is a a moderate or minor decide to have a decide to have a light estimation. So there is only one loop but if you improve with much more loop you have a reasoning. So with instead of just a flowchart you have one shot you have the result from the API and if is good okay otherwise it fails instead in this way you have the the loop that is able to reason by the the agent and understand what happens inside the system.

**[29:39](https://www.youtube.com/watch?v=LNki_OFpxf0&t=1779s)** >> Thank you so much Cladio Janatino. >> [applause]
