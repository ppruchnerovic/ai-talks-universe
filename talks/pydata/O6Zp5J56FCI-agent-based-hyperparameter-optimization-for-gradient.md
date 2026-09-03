---
id: O6Zp5J56FCI
title: "Agent-Based Hyperparameter Optimization for Gradient Boosted Trees [PyCon DE & PyData 2026]"
slug: agent-based-hyperparameter-optimization-for-gradient
conference: pydata
conference_name: "PyData"
category: "Practitioner AI conferences"
edition: "PyData"
year: 2026
speakers: ["Huijo Kim"]
channel: "PyData"
duration_min: 28
published_at: 2026-08-04T22:20:31Z
video_id: O6Zp5J56FCI
url: https://www.youtube.com/watch?v=O6Zp5J56FCI
youtube_url: https://www.youtube.com/watch?v=O6Zp5J56FCI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
topics: ["Agents & orchestration", "Classic ML & data science"]
transcript: true
---

# Agent-Based Hyperparameter Optimization for Gradient Boosted Trees [PyCon DE & PyData 2026]

**Huijo Kim**

`PyData` · `PyData` · `2026` · `28 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=O6Zp5J56FCI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 14.04.2026

🎓 Watch Senior Data Scientist Huijo Kim demonstrate how to transform hyperparameter optimization from a tedious search into an intelligent reasoning process using agent-based workflows.

Speakers:
Huijo Kim

Description:
Hyperparameter optimization for Gradient Boosted Trees, such as LightGBM and XGBoost, typically requires tuning 14 to 19 parameters. While frameworks like Optuna use Bayesian optimization to navigate this search space, they often require hundreds of iterations to move from exploration to exploitation. When model training times are long, this iterative process becomes computationally expensive and time-consuming for human operators to monitor and adjust.

The proposed approach integrates Large Language Models (LLMs) into the decision loop using the Model Context Protocol (MCP) and a structured "skills" framework. In this architecture, MCP acts as a toolset—providing the LLM with specific capabilities to fetch campaign status, summarize rounds, and review history—while skills provide domain-specific recipes and step-by-step instructions in markdown format. Instead of running a single massive batch of 200 trials, the process is split into multiple smaller rounds. After each round, the LLM analyzes the results against the provided domain knowledge and official documentation to decide whether to continue the current path, discard specific hyperparameters, or shift the search region.

Testing on four public scikit-learn datasets demonstrated that this agent-driven framework consistently achieves competitive performance compared to standard tuning. The system functions as a guardrailed loop where the LLM proposes actions that are executed via a predefined CLI, ensuring the agent cannot perform unauthorized operations. This pattern is extensible to other computationally intensive decision loops, such as deep learning training, infrastructure scaling, and A/B test management.

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

*3,874 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=6s)** Today I'm going to teach you how to leverage large language model to tune your some machine learning model or even beyond working on your um workflow. So my name is Suk Kim. I work as a senior data scientist at voice. So boys is Hamburg based uh fast-pacing growing startup and we do offer AI powered procurement software to maximize availability minimize cash flow investment and cut 90% of manual planning time for e-commerce brands. So after this talk I will promise you that you are going to learn a design pattern using MCP as a tool set and your domain knowledge in your industries.

**[0:54](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=54s)** So I'm going to demonstrate on hyperparameter optimization as a one sample cases but it will be beyond of this only hyperparameter optimization or tuning. So you are going to leave with a blueprint for putting large language model into your decision loops and also with some guard rails. So if you do machine learning that's great. Please take as a sample project that hey I can do hyperop parameter optimization with large language model even though you don't do it. So you can reus re this will be a reusable pattern for agent optimization. So gradient boosted tree is one of the very famous machine learning framework. It's

**[1:42](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=102s)** really winning across over competition or even industries. I used to talk to like other machine learning or data scientists. Hey, what do you use for your data to make some prediction or to forecast to be honest? It's not always really deep learning which people are really like crazy about. But mostly I'm hearing that hey I use light GBM or XG boost or when you go to Ko competition more than 60 70% of winners are utilizing this light GBM or gradient boost these three. So this is super powerful but there's some limitation of using this machine learning uh model framework because there are 14 to 19 uh tunable hyperparameters that you have to really select and then really tune hey this value should be zero 0.1.001.

**[2:34](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=154s)** So this is something we have to iteratively search for the uh best parameter. So one famous thing is learning rates or other thing regression parameters for noise data or [snorts] is this model really have to go to deep or really the wide or some when we are doing some subsampling some strategies. So this right parameter is not something you can get from the um textbook that means it really depends on your industry and data set. So often senior to junior telling hey you start with this hypo uh five hyperparameter and you run some tuning overnight then you will get decent result. So this is what has been happening and optuna is one of the very famous uh

**[3:25](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=205s)** framework in this uh hyper parameter optimization because we don't want to do every greedy grid searchy over whole um dimension because we are going to fall into curs of dimensionality that's why optuna is doing a smart job already what it does is doing some basian optimization based on previous our um training or fit and it tried to do more promising region we do more uh fit and try but still it needs some exploration before doing it needs some like exploitation. So which means we have to run like a few um decades or hundreds of like run before do some exploitation. So for five parameters in practice about

**[4:12](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=252s)** 200 iteration is a good exciting point. So if your model require just one minute of a fit or train time then it takes 200 minutes so three hour acceptable but if it takes 100 minute or longer then it's five parameters is already like hard and when it comes to I want to exploit everything I want to find the best parameter for my like forecasting or prediction model then you can't really make it within the time. So our goal is we are going to find some middle ground utilizing hey logic language model is so powerful to do some reasoning and why don't we use it so before really going to agent thing so I want to uh get us aligned with some

**[5:01](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=301s)** terminology I'm sure like all of us are hearing a lot about cloud uh chip codeex and gemini And people are like link uh sending some LinkedIn post hey I have built this MCP and this is a skill you can integrate this and everybody has some slight different like definition of their own. So let me let us like align with entropics uh definition because to be honest they have invented MCP and they are pushing for very hard for the skills. So based on their definition which I also very like MCP is about connectivity. So one analogy is a kitchen. So it provides tools, ingredients, equipment. So in our case, we can get some realtime data

**[5:49](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=349s)** access such as like database and there's a tool invocation, what kind of tools are available and then explain what it does. So it's all about what cloud or codeex gemini can do and skills is about uh domain knowledge. So it's a recipe focus keyword is stepbystep interaction. So there's step one you do this, step two, you do this and based on step two's result agent is supposed to do action A or B or C. So this is something we are going to enforce and our whole goal is user unc accomplish complex task without giving too much of like manual intervention. So in our case I'm talking about um hyperparameter optimization then cloud code will utilize MCP tools.

**[6:41](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=401s)** So MCP will which is a kitchen will give eight tools. So um large language model or agent is not going to do some random stuff. So we will predefine hey you are supposed to do this eight tools. So in our case, get campaign status, get round summary, get campaign history. So here campaign means hey let's run one campaign and it's going to run like 200 or 2,000 um iteration and each round we will define I will get more details and then in the end agent is going to act on hey what action I want to propose and then just run the next and at the same time skill is about tuning guide. So not only you are just owning as a team or as

**[7:29](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=449s)** a company you can document it a if this is what is happening around this par parameter then we need to do this action A action B so let's get to more details so this is one iterated like uh slides one say existing one go hyperparameter optimization we submit hey there this is a five hyperparameter that I want to optimize and then just run over 200 cycle maybe over one night or a week. But what we can really leverage is let's not just do 200 trials is just one goal. We can split into multiple and in the middle of that LLM with the power of MCP and skills and make a decision hey should we keep going on this or maybe

**[8:20](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=500s)** dump this par hyperparameter or we like switch it. So this is something we can really give a guidance in in between. So we don't have to wake up in the middle of the night and then check revise agent is supposed to do it. So let's do one demo call. I think that's where uh I hope it works out. Okay. Okay, I'm using cloud for the sample case. So this will be the thing that I will ask I will just make it bigger. Hey, let's do some tuning for certain data set. Of course, you can define that

**[9:09](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=549s)** I have data set of e-commerce data. I have data set of farming. I have data set of something. Then based on skills, we are supposed to define what you need to do. It looks like fancy initially but it's nothing but we just write it down as a skill file. Hey step one this is something you have to clarify with user and let me just follow what uh needs to be I want to use light GBM I will use this we'll just keep it very simp one what is shortest I think almost same so you can define some different mode hey is it the right one just agent is doing whatever we have defined you have to really make get the proper input to the run uh this Optuna

**[9:59](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=599s)** or other hyperparameter tuning uh framework and unfortunately postgress is not running so I actually didn't run docker yet but it is going to run yeah during this is yeah it's running let me just continue on presentation. I will get back to you. So this is running on the left side. Okay, I think it's better make it big. So this is the summary because it's going to take couple of minute. Maybe we can revisit later. So each round rather than we go full round at once we will split into multiple round and then LLM

**[10:51](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=651s)** can just sit again and then use MCP as your kitchen tools check from the previous uh run is it good or bad we we define coming from let's say uh light GBM or XG boost official documentation and then what is each parameters is supposed to do and then we also write some so many knowledge about industry and it makes the decision over the time and this is one like bigger sample I have just already prepared last night so I made like 20 sample cases so each 20 of like rounds it makes decision okay keep going keep going I think we have to really reduce these two parameter and add these two this will be the m it's going to

**[11:39](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=699s)** make this decision in the middle of the work it does nothing but it requires skill based on your guidance. So [snorts] this is how we can not only training go to 200 it can because what I have some impression about uh using agent workflow is I just want to have a really the best moment. Okay, let me just skip it. Achieve best model performance but I don't want to really spend my time but let um some electricity burn so we can achieve the best performance. So this is the way or framework that we can achieve this uh goal. So not only one uh sample case I also included some more public data set

**[12:30](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=750s)** want to really see hey it can pro it can produce some more meaningful better performance. So then these are four public data set coming from scikit learn and I just compare with just using 10 parameter all parameters and our uh agent tune uh framework and then it got always not the worst but here the catch point is okay this is going to change the everything about hyperprime optimization I don't think this is the right like conclusion that we already have our very well performing framework on top of that we will just iterate with the loop. Agent is going to uh make a decision in the middle of it. I want to

**[13:20](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=800s)** Yes. So during this talk, this is the one that we get some summary during the round and then after this round agent is making next propose and then run it on and on and on. So okay so this is the pattern. So beyond hyperpire optimization first agent is very powerful at obser some structured signals because it can read like very hugely uh manufactured JSON data and then really keep tracking of it. Second agent can diagonal uh via domain knowledge but it has only like limited knowledge coming from the public or pre-trained data set. So we really need

**[14:07](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=847s)** to define as a skill. skill is nothing but rhythm file or markdown file that we are really specifying this is condition A B C D and then based on that you do it and next agent can propose an action but this action should be guard rail based on our thing so it's not supposed to do some delete of our database or it only supposed to do define our predefined tools through our MCP which is our kitchen and we can enforce uh this guard rails that only can do the predefined tools and keep repeating until we reach the point that we are happy with our results. I really strongly believe that it works for any domain with some

**[14:55](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=895s)** decision loops. If you have to make some um computation or some experimentation and then you have to revisit and revisit on and on then this uh framework will really shine. So it can be certain optimization or infrastructure scaling or AB test management it will really work out. So in short large language model will decide and code in force and MCP is the interface that it will really connect each other. Thank you so much for listening my talk and [applause] all all the frameworks are in open source in

**[15:43](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=943s)** the GitHub repo so you can check out. So also very short advertisement. So our team is hiring for data scientists and data engineers. So just get back to me then I love to talk to you. Thanks. >> Thank you for the invite insightful session. Uh there are a few questions. What are examples of domain knowledge you would provide to our agent uh to your agent? Do you have to modify this for each data set or each customer? >> Um, I would say it's really dependent on data set level, not the customer set. Of course, if one customer has a very strong seasonality data set, then of course you can enforce it. Let me make

**[16:30](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=990s)** some simple example. So in my former work, I used to have the count of red berries. So this count of red berries are detecting from certain camera and then we detect it. But there could be some blur from foggy air or leaf is blocking or there's some ants is blocking the camera lens then this can mean it's a noise for uh the counting the number of fruits counting the number of some leaves. So this kind of domain knowledge we can enforce that hey if you see some certain drop you might ignore this or you can do some like smooth thing. So this is the domain knowledge that I can think of as an example.

**[17:18](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1038s)** >> Okay. Is the agent able to tune parameters beyond the ML model for example data prep-processing? >> So I think it will even shine more when it comes to like deep learning. So when I was doing like computer vision uh training it takes day or couple of days for one training because for light GBM it takes mostly likely one minute or 10 minute hardly go like more than hour for just one fit. But when it comes to deep learning or other framework then one cycle become very very long. So we really want to reduce the the um waiting time for the human is deciding. So I think light GPM is one

**[18:07](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1087s)** example but there are potential to apply other machine learning or deep learning framework. >> Okay. Instead of running an agent and a custom MCP, wouldn't it be easier to have a call back to a model from the training pipeline after a run to ask for the next parameters to test? This is actually very good question and also some like counterargument because I al just here define which is following entropics uh guideline skills as a recipes but there's another approach that in skill you can write it down here hey this is API or this is a callback you can just immediately run this uh query or you can make some like uh request it will also work and some

**[18:55](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1135s)** people say hey this is more token of efficient and it's going to work so I won't say this is a bad approach but there is two different word how to achieve the same goal but to me this is a simple and clean approach >> okay uh could you show an example of skills you use for example this problem what exactly the skills look like what knowledge and rules do they provide >> yes for sure I love to show really the case so one skill I already uh present is when I start some campaign the question list that uh asked I think I it's better I make it bigger okay and the other skills that I so it's all about markdown file and I

**[19:50](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1190s)** don't write this skill if you go to cloud Cordex ask there's a skill called create skill then you are going to create skill using this skill so please don't write down this thing and cloud will ask you the very good question hey what should I solve and what should I do and then based on that it's going to create these skills and there will be tons of very nice materials in YouTube go and check out but if you come back to me after this talk I love to give some more demos and examples Similar question. What exactly have you provided? Like what information does the skill provide? >> Again please. >> What information is provided in skills here >> in this demo cases? >> Yeah.

**[20:35](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1235s)** >> So in demo in this demo cases I have prepared or injected only public data set which I can just download from the public because I can't really expose our client data set from our work. But what in your workflow you are what you need to do is one you define how to fetch your data from either S3 or from your local machine. Don't write it yourself. Ask cloth hey I have this framework and then I want to inject my data set not the public one. And second I am using light GBM just fit probably you are supposed to have some pre-processing post-processing again ask your cloud hey I need to do some pre-processing post-processing so this is the extra work you need to do

**[21:26](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1286s)** >> how do you avoid going into an overfooting mode >> this is uh I think beyond of this uh topic. I think I have to really come back to just standard answer or some boring answer. Please check your validation and accuracy and also regression term for we should never drop this parameters for regularization and then we can also check out from the log uh this gradient boosted tree but others can also check out the other uh so delta between validation and test results. Yeah. >> Can you do the same thing

**[22:12](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1332s)** programmatically instead of calling an agent? >> Yes. Because what it does in the end is just calling some CLI that I define agent tune. So my project and agent is not doing anything fun. It just call I'm doing agent tune in it with some parameter just to the CLI. So we don't really need uh agent to do it. But I think it's much easier for us human that just write a natural language. Hey agent do xyz. Maybe you can spend 72 hours until you get the maximum output. So this is something much better to use. >> Okay. Do you think we could use a VLM and use training plots as inputs for the hyperparameter optimization loop? >> Vlm. [snorts]

**[23:02](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1382s)** >> Yeah, that is what is written right. >> Yeah. Yeah. I think uh I can't really answer. So yeah. >> Okay, we I can ask the next one. How is the performance of past trials passed as part of the agent context? >> So the question was how much context is consumed by this iteration. >> It is like how is the performance of the past child's past uh to as agent context. You could read it here for clarity if you want. Um if I get the question right this is something I can't memorize but we agent is supposed to loging every performance

**[23:50](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1430s)** over each run and it also looks at what was the previous uh performance validation also test and then just keep tracking it. So I think I just answered. >> Okay. Uh do you start with a coarse grid of hyperparameter values in the first trials to quicker determine which parameter to dump from optimization? >> So this is I think something you will start uh with your default value that you are uh putting the default as a skill again. I'm repeating the same term again and again and then agent will start from this uh starting point. Okay, I think these were the questions that were asked. Are there any other questions in the room? Yeah, just a moment. I can give you the

**[24:38](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1478s)** mic. >> Thank you so much. Um I suppose there was a sequential setup on Optuna, right? So it wasn't parallelized. If it's possible to extend uh the MCP framework, the kitchen in order to use a parallelized uh hyperparameter optimization, say I would like to um I would like to use a cluster as a back end or maybe even to use multiore setup. So this is for sure it won't work immediately because this our tool is predefined to call just uh sequential optuna but of course you may define the

**[25:27](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1527s)** tool that um run next round marty yeah so I don't think uh there is any limitation because in the end what this tool will do is call again this optuna input some uh hyp input arguments which is Mart is true and put the rest of like relevant input there. Yeah. >> Okay. Are there any other questions? Okay. Just give me a moment. >> Yep. >> Hey, uh thanks for the great talk. I was just curious uh whether you have seen Andrew Kaparthi's auto research that he published about one month ago that is doing like something similar. Um could

**[26:17](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1577s)** you maybe elaborate on what are the differences or whether you have also like considered using that for the purpose of your work? I think I am for sure get inspired from this auto research but I really like narrow the scope of only focusing on this uh this problem solving. So I believe this is fundamentally the same approach to handle like complex and looping problem but Andrea's approach was more generic and really like any

**[27:07](https://www.youtube.com/watch?v=O6Zp5J56FCI&t=1627s)** research paper I will really uh build it but for me I just limit my scope to hyperparameter optimization. So my short answer is it's doing the same job but just problem was slightly different. Yeah. >> Okay. Thank you so much for this session and um that's it for today. Uh this was the final session in this room and now you all are invited to go on spectrum in on the first floor for the lightning talks.
