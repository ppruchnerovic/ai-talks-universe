---
id: lpTeJ0WpWyE
title: "Do you know how well your model is doing? Evaluate your LLMs [PyCon DE & PyData 2026]"
slug: do-you-know-how-well-your-model-is-doing-evaluate-your-llms
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Cheuk Ting Ho"]
channel: "PyData"
duration_min: 34
published_at: 2026-08-04T22:21:34Z
video_id: lpTeJ0WpWyE
youtube_url: https://www.youtube.com/watch?v=lpTeJ0WpWyE
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Do you know how well your model is doing? Evaluate your LLMs [PyCon DE & PyData 2026]

**Cheuk Ting Ho**

`PyData` · `PyData` · `2026` · `34 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lpTeJ0WpWyE) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 16.04.2026

🎓 Watch Cheuk Ting Ho demonstrate how to rigorously evaluate, benchmark, and fine-tune your LLMs using Lighteval to ensure your models deliver objective and high-quality results.

Speakers:
Cheuk Ting Ho

Description:
Evaluating Large Language Models (LLMs) is critical for benchmarking performance, ensuring safety through railguarding, and verifying that fine-tuning actually improves model capabilities rather than degrading them. This process mirrors software testing, where systematic evaluation prevents the deployment of buggy or toxic outputs and ensures the model meets specific hardware performance and response-time requirements.

The technical approach centers on the Hugging Face ecosystem, specifically using the Transformers library for model training and LightEval for benchmarking. To demonstrate these tools, a small GPT-2 model is fine-tuned on math logic data to improve its reasoning capabilities. The workflow involves loading a GPT-2 tokenizer to process question-and-answer pairs and using the Transformers training pipeline to create model checkpoints.

LightEval provides a framework for measuring model quality through built-in tasks and metrics. Available task categories include knowledge and reasoning, question answering, chat and instruction following, coding, and multilingual support. Evaluation metrics range from simple multiple-choice accuracy and log-likelihood to advanced methods such as using a second LLM as a judge to score the primary model's responses.

For specialized business use cases, the framework supports custom tasks and custom metrics. This allows developers to reserve a specific test set from their training data and define precise scoring logic—such as a binary correct/incorrect point system—to measure success against real-world data. While LightEval is optimized for open-source models via the Hugging Face Hub, it can technically evaluate closed-source models by comparing model outputs against defined targets, provided the user manages the specific API prompting requirements.

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

*5,288 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=5s)** Yeah. Oh, good. Okay. Uh because I want to show you this link. This is uh the most important thing today because uh all the setup instructions and all the exercise are on the link. So um yeah, if you can uh it's actually uploaded a bonus point if you have already start installing and you know um but if not you can do it now because I would do a little bit of yapping uh at the beginning. So I think it's a good time that you started the downloading process then you know then you can pay attention to me. So um yeah. Oh, also uh I think okay uh I think you know um my style of workshop is quite flexible. So I'm happy to run around. I know the camera person will hate me for

**[0:53](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=53s)** that. But um but but if you let let's say oh I have an error and then just raise your hand. I will try to come over or you can you know just interrupt me anytime ask questions I'm okay with that because uh it's a workshop. We share the space together and learn together. That's what I believed in. So um if you're watching online, sorry um you can you know u we have a very good host here that can help you to ask the question but unfortunately I can't see your screen so maybe can't help you as much um so okay I hope all of you got the link um and yeah good okay for folks who just come in maybe your neighbor can help you to access the link it's on GitHub type my name there and then a life eval exercise. Um, so yeah, cool. Um, yeah, I hope all of you got it. If

**[1:45](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=105s)** not, you know, ask your neighbor. They are your best friend today. So, um, first of all, I want to talk a little bit about why we need to evaluate our RM. So, I'm going to, you know, I love telling stories. So, I'm going to give you a story time. Um, now that um, why I start like looking into this, right? So a while ago I am trying to write a blog post about fine-tuning a um error M which is uh GPT. So um I was trying to you know see if I can fine-tune it so you get like you know because GB2 is uh the the open you know open source model is not like very sophisticated yet. So, I'm trying to fine-tune it to see if um I can make it

**[2:36](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=156s)** to do something more specific. For example, like understanding math logic because um unfortunately GB2 is well I mean like now if you use the newest you know model by entropic or open AAI it will be very good at um math reasoning but for those older and um open source smaller models they are not that good. So I'm trying to see like okay I don't have the power to create a model that is you know general purpose you know I'm not competing with those companies. So um I'm just trying to see if I can train the small model to be good at a specific task. So um that's the story of you know oh that's why I read the blog post trying to um you know train the small GBT2 model on my local computer. So it's you know quite

**[3:25](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=205s)** challenging. So um if you have a you know cluster at home or whatever like way you can you know feel free to use those resources if you are comfortable with doing that but today we are also aiming to train a small model. Hopefully it will work on your computer. Um and mine is not new as well like mine is like a few years back like when I bought it. So if you have a new computer maybe you know you're you're better off than me already. Um cool. So um so today we're going to try to do it again but uh with the help of other tools from hacking phase hopefully we can retrain the model today we can um learn how to use lightl also provided by hacking phase to compare models and then maybe compare our refined model to the original model to see if it's any

**[4:14](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=254s)** better. So um yeah evaluating is very important I think um so first of all how many of you are data scientists yes uh you probably know the important of evaluation right like um because you can't just be like oh push out a model and you know say that it is better than the other one because you don't have a mean to measure it right so um it's very important for comparing also when you fine-tune it. Is the new one better than the old one? Because you know again like data scientists you must know that like sometimes keep training on something doesn't mean that your model get better. It could be worse like if you have a task that you know it's if you have a new data that's not

**[5:02](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=302s)** in your train set. So uh so so benchmarking is very important. Another thing is uh rail guarding is another thing that um you know maybe we don't think that much is that um so is the response from your model being weird and give something that is like not what you're expecting. So you know this is kind of like I would compare it as like testing in software. So if you write code we all know you know um we have to test it to make sure there's no bug before we deploy it. So you know if we testing the software we should also evaluate our RM that's as simple as that. Um so uh sometimes also performance as well because we may have hardware limitation

**[5:51](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=351s)** we may have other limitation like how much response time we're trying to achieve. you know um having the evaluation is also like it may be something you want to measure right the time that it's uh you know got some you know good enough result um so yeah again like f fin fine tetuning I already explained it um you know sometimes more training doesn't mean it's always better so we have to measure it right um how many of you have used hucking face very familiar with hucking face yes yes good so okay good so you'll be able to do something nice to date them. Um I love hugging face. Uh it's kind of like you know they have a lot of resources there kind of like I like playing with what they offer. um including open source model including um you know transformer which we will use

**[6:40](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=400s)** today and also um light eval um so yeah transformer is you know I guess I don't have to explain too much a lot of you is already familiar with hugging face is um basically you can use it to you know get a trained model from hugging face hub and then you know you can use it to get some projection result uh you know or um fine-tune it by training it. Um and then light again like it's the tool over by hugging face to do some um benchmarking and evaluation. Um we'll dive a little bit more into the detail later today. Uh you know again like I feel like I I have to really like you know um dive deeper because a lot of you

**[7:28](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=448s)** are data scientists. Um so light eval allows you to set up your own task and metrics which is really good because um again like to a good evaluation need to have the right metrics so it's measuring the right thing so again like we will look into that later so don't worry about it right now. Um yeah rail guarding again like we don't want the area to respond something that's like super weird. We want it to be you know um sometimes you can do some evaluation to see like if there are there will be like toxic comment or toxic text got generated so that's also very helpful um and you know so nowadays if you build a agent I know there's like a lot of like gut rail you can put in there um for example some human in the loop thingy

**[8:16](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=496s)** but again like we are not building a agent today we're just training a model So uh we don't have to worry too much about that today. Right. So coding exercise. Um I hope you have cloned the ripple and have you know set up all the dependencies. So um now we have some exercise that we would have to do. So let's look at mine set up. So I have mine here. Um I've cheated a little bit because I've created an answer. I'm not that good at live coding. So that's why like I will panic if I'm like you know live coding right now. So I already have it um created. So um cheat a little bit but again like you know um we have a lot of things to do today. There's like free part in this exercise. If you are you know oh I'm like a super user of hugging

**[9:04](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=544s)** face. I know a lot of things already. You can thrive fluid. You can just like you know um finish off them or jump to the pot that you're interested in. Again everything is kind of um I try to put everything in writing. So in case today I know everybody have different speed um you know of competing exercise in case today you can't finish it you can always finish it afterwards. Um so but hopefully today we have time to at least like look through all of them but even if not again like all the materials are in your pocket so you can do it later. Um the first exercise we're trying to fine-tune um the model and um so it's kind of like a warm up for you. So um we are now trying to fine-tune the GB2 model and then this basically trying to

**[9:54](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=594s)** um do what I've done for the blog post is to try to see if I train some um math logic data with it then you will be better at math problems. So um there's already a file there for you. Um however uh as a you know I want your brain to start you know warming up and working. So um there are some to-dos that is not done um that would like you to for example here um you know this is not completed. So just for you to remember how to use the tokenization um like you know uh from hucking face the the tokenizer in from hugging face and also the um yeah and then we would use some uh transformer here to train um here see uh so so this is the tool to do for you to do again like all the all the

**[10:43](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=643s)** instructions are in the readme so after you have completed your code NA should be start training and then um it would take some time. Uh but you know good thing about huging phase is that it will create the checkpoints and then you would have this and then we we will use that in part three. So um I'll give you time now to do the exercise. What time is it now? Okay. So maybe I would give you half half an hour is too much. I give you 20 minutes to try go through it. Oh again like you can also use AI to help if you want to. I mean nowadays who doesn't use AI anyway? So you know uh 20 minutes try to clack on it you know get your hands on it again. Like if you don't finish it's fine. We would um you know you can do it

**[11:31](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=691s)** at home. So cool. Right. We're back here in 20 minutes. Okay. How's everybody doing? Yay. Uh I want to use the last few minutes to show you the quote unquote answer. You can use other method but this is kind of working. So I'm going to show you in case you are kind of new to this. So um yeah. So this is okay let let me check back into what we were trying to do right. So we have the fine tune here. So first of all we need to tokenize the um the data right. So um what happened here is that um so uh we got the tokenizer of GP2 here

**[12:21](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=741s)** loaded in and then afterwards then we want to tokenize our new training data. So we are doing it here. So um yeah we process it a little bit because the format of the um the training data will have the question and answer there but we want to extract um the text from it. So that's why we do this um thing so we can have a pair of question and answer um that so it's just kind of um reformatting the data and afterwards then we would just um do it in a loop and then for each of them we will tokenize it. So um yeah, I can also upload the answer for you afterwards, but um I always encourage you to try it yourself first.

**[13:11](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=791s)** And also this is not the only way to do it. So um don't worry too much about it um right now. So we would move on to what we're trying to do next. So, um, let's go back to part two. So, I'm always bad at navigating my windows. Sorry about that. [laughter] Okay. So, what are we doing next? Yep. Uh, light eval. So, so far we have only used the tokenizer and the um the transformer from hugging face. So, we haven't used light eval yet, right? So um let's look at what is life eval. So um I really like it uh because you know um

**[14:01](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=841s)** it's always good to have a good evaluation tool and um hugging face also providing it. Um so it has a lot of tasks that's already there so you don't have to write your own task if one of them works for you. Um and also I'm sure that on the hockey face hub there's also a lot of um things you can use with together with light eval for example you can use um a uh a task that someone already uploaded or a metrics that someone already uploaded or some kind of evaluation data that someone already uploaded. So you can also get the resources from there as well. Um right so um all those building tasks that is already provided to you and you don't have to write it yourself they are the the common one that you know a lot

**[14:50](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=890s)** of researcher will need for example knowledge and reasoning um there there there are a more specific name for it but it's this is just a category that um is available. So knowledge and reasoning, question answering which is you know like our math uh you know logic training set is question and answer. Um there's also chat and instructions following. So if you are building a chatbot maybe that's uh for you. Um coding and math also something we can consider for our um own use um in this specific exercise. And multilingual if you are training something other than English then that could also be helpful to you. So um so that's the task. So what you want to so this is very specific right like uh you're expecting an answer from a question or you're expecting um a translation for the

**[15:39](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=939s)** multilingual ones. So these are the tasks to measure how good the results are when you get back from the model. Um there are also different ways to measure it. um just like any other you know machine learning algorithm you have to um of course check the answer but um you know if it's not perfect then how good it is right we also need to give it a score so there are different ways to do it um so for example you can do a multiple choice so if it's choose it correctly then yeah you know you know one point for that maybe you know if it's wrong then zero point so it's kind of like a lock likely hood kind of you know once you have a lot of question you can kind of you know check how good your model is at this multiple choice exam.

**[16:28](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=988s)** So uh another thing is that you can also have um more advanced metrics. Um so this could include a lot of more complicated things. So for example um you can tokenize the result and then maybe compare the the likelihood of it to your perfect answer. That's also a way to do it. Um and other thing is to use errorm as a judge which is you are using an errorm to mark the results of this error which is kind of funny. Um but that's more complicated. So um I I would say that try the other first because that's more straightforward and if those doesn't work then maybe you know you can use arm as a judge but but you have to find a reliable arm to do it. So yeah, next we also have another coding exercise that would be um we are

**[17:15](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1035s)** starting to use light eval. So there's actually two ways of using light eval. Let me show you that. Um so here right so um you can use slice once you have pip instin I'm sure like if you do u sync in the ripple you already have it. um you can use as a command line tool which is the most straightforward way to do it. However, sometimes we don't want that right sometimes you want to maybe rerun the evaluation then you may want to store it as code. So to do that you can also write a Python script and then you know pull in large event so you can run the evaluation multiple times or you can run it later with the same settings. So you can do that. Um again all the details are pushed in the readme and we

**[18:05](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1085s)** do have a script that again uh it's kind of like uh you know you have to fill in the to-dos. So just to make make you familiar rise with what um live event is available. So uh make sure you have the documentation handy so you can you know check the detail. Um again like I'm going to give you 20 minutes again it's not enough to complete everything but um or try a few of these command just just try a few things so it's again like it's time for you to explore to learn you can always do that later if you haven't finished it um and yeah so you can you know get a feeling of what light offers you cool questions? No. Okay. Okay. So now let's uh you know

**[18:55](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1135s)** have 20 minutes of exercise. Okay. Um yeah I will quickly again like show you the script. Um if you are you know trying to get the script running uh so it's here [snorts] in the evaluation model. So um yeah so uh we use pipeline uh so I didn't talk about pipeline um in part one but I hope you know you you're familiar with it if you are familiar with um hugging phase but um basically pipeline just let you to put everything together and just um get it running. So it's very useful if you run the evaluation because then you can um kind

**[19:43](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1183s)** of you [snorts] know uh run it multiple times with the same configuration. So yeah so this you know um that's the file I again I would upload for you um later if you want to check it. So um the last one the last one is >> yes what is it actually >> okay so it h it depends on the task that you ch you have chosen so like you will use a task that you have chosen and then use a metric that you have chosen so the task will be actually what you can think of it as the the evaluation data that you use to um or or test data I don't depends on how you you call it but the

**[20:32](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1232s)** data that you use to um test the model that you have finished training and then the metrics is how to score um your model. So if you put it in like uh machine learning terms, yeah, it will be the the the the test set that you have you know reserved for um testing after you have trained your model and then um that that would be the task and then the metrics are the metrics that you use to measure the result um of it. Does that make sense? Oh yeah. >> Yeah, you can choose the task. Um you can choose to use a different one

**[21:19](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1279s)** because um we are using the built-in task at the moment and light provides a lot of built-in task that you could use. So you could either use that or path three which we would use a custom one. So yeah, any more questions. Okay. Um right. So uh okay. Sorry. Um let me I lost my train thought. Okay. Here. Um so last we are talking about the um how to have made a custom task and custom metrics. So um you know it's nice to choose from the uh the built-in task but what if you

**[22:07](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1327s)** know you have something super specific uh that for example you are training something that is specific to your business use case but the information are not propic so you want to design something that's custom for it that is not open to everyone to use. Um so uh like I said before it's kind of like after you train a model even if it's let's say a machine learning you know um logistic regression model you would probably want to see how it does with some you know real life data or some data that you know you haven't used in training. So um we are kind of probably doing that. So let's say when you fine-tune your model, you also reserve some of those um data that you

**[22:56](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1376s)** use to retrain refine your model and you want to create a custom task to train it uh to to measure uh evaluate it to see if it's you know you have achieved your goal then you know custom task would be the way to go. um custom me uh custom metrics also like if your task is super super specific and the current metrics doesn't really measure what you want then again like that's an kind of a um potential for you to do something yourself um so it's quite straightforward um I think I'll just let you do coding exercise and um so let's look at path three. Oops. Okay. Uh, path three is here. So,

**[23:47](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1427s)** um, again, like there are some to-dos that you have to fill in. I like when people are really getting their hands dirty and writing code. Um, so here we are trying to define a um c a custom metric first. So this is um we want to you know this is how we measure the the score, right? How we check the answer. So um for example we are making one that is like you know you just check if it's correct or not. If it's correct then yay one point. If it's not then zero point right. So very very simple but again like it's an exercise then you can try to see how like custom metric works. Um another one is to set up your own task. Um so uh there are already some parameters for you to do it and then um we are using

**[24:37](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1477s)** uh a test set here. So yeah we are putting in the test set and you know just set it up and works. We should have the test set loading in somewhere here. Yeah. So we using the same um the same data that we have but we would create a test set out of it and you know and measure it. So, yay. Um, yeah, we'll use an other tr okay 15 minutes maybe to to finish this and then um we'll wrap up and um may maybe I'll just tell you now because some of you may leave early. So I don't want you to escape me um without helping me at the end because I want you to help

**[25:26](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1526s)** me with this little thing. Um you may see this image in the GitHub repo as well because uh you know once you finish your exercise I also want your help to help me fill in the survey because I want to know um how you use AI at work or maybe you can tell me oh you use AI in this completing the exercise and you know those things as well. So there are just not too many questions. You can probably do it in two minutes. So the last two minutes of the workshop, please help me to do that then. Yeah. But anyway, okay. Uh I don't have more to tell you now. So just do the exercise and ask questions. That's it. Good. Okay. Yeah. Sorry. I'm >> I'm still in the website checking out your questions.

**[26:14](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1574s)** >> Yeah. Do we have questions online for people? >> Yeah, I mean we don't yet. >> Oh, we don't. >> So, I'm just coding. >> I hope it's [laughter] self-explanatory. That's why there's no question. But if uh if you have questions, I guess you have the GitHub repo. You can write me questions as well. So, we are very interactive. Yay. Yeah. Cool. Um I will show you the read me. Okay. This is not the GitHub. Show you the read me of free. Uh yeah, here. Cool. Oh, by the way, once you finish the the the to-dos in the file, you can actually uh run light event with those. So, because uh we will load in the file,

**[27:06](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1626s)** the custom task and metrics from the file and then you know, so that's how you can use it. Um yeah. >> Um so we have a question. >> Okay, cool. Nice. Um how this uh sorry how this tool differs from tools like LM evaluation hardness. Uh, Adam evaluation. >> LM error. >> M LM evaluation. I've never heard of that actually. [laughter] >> Maybe it's pronunciation. >> No, I think I think I've never heard of

**[27:53](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1673s)** it. uh RM evaluation harness I don't know every single tool uh for for errorm because you know RM is a hot topic right now and I'm sure that there are other company um using other you know um tools it may be better but I need to look into it um I just think that if you're using hacking face you're using um their model um you know light is a very good tools to use together with the tokenizer the the the uh you know transformer the pipeline and if you're using things on hing face then why not like yeah another one um How does light eval

**[28:55](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1735s)** compare to prompt 4? uh again like judging from the name of that tool that you mentioned it's um it's more of evaluating the prompt or other again like I don't know all the tools in the AI and ARM space is a huge space um however like is kind of um I already showed you all the all the all the bells and whistles that come with it and um you know So I think if again like it it provides a lot of open source tools. So it's kind of like another benefit of light is open source. So um if you love open source if you love to contribute your own metrics or own um

**[29:45](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1785s)** task then you know you can do that. You can upload that on hugging face hub and people can use it. So I think that's one of the thing I like about it is because it's open source you can share things. Yeah. >> Thank you. Um, with this custom metrics, could you also do more targeted evals on models that are closed source? Uh, right. So, um, I guess you mean close. Okay. So, it depends like uh what do you mean by uh close source? Um, Yeah, if you want to uh use it to evaluate those model I think

**[30:36](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1836s)** so technically well technically you can um if you have a custom model uh you can't of course you can't fine-tune a um a closed source model because you don't have the tokenizer you you know you can't do that but um with the light eval with the um okay I'm just clicking on it right now. So with the these um task that you set up so it would just you know um you know put in the input of the model and then get it out and then you know do some calculation of the result and compare them. So technically I don't think you need it to be open source but again like I can see the challenge there could be like because you are like how you send your prompts to let's say uh claude is

**[31:27](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1887s)** different from how the the way that you know um uh hacking phase is sending uh information to transformer. So you can't use the pipeline you know those those things. Um, so it may be a little bit more challenging than that. Um, so I think that that that's the issue that I would have in my mind and I have to sort that out before I can attempt to do that. Yeah. >> Thank you. [laughter] Yeah, I hope I answer your questions and yeah like um so I guess there are other tools for those like closed source model um but again like val is very um customized to work together with everything that hugging face offer um yeah >> right Oh,

**[32:25](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1945s)** okay. We have four minutes until Is it four minutes until the end? No, >> no, we have 14 minutes. Uh, sorry, I didn't calculate it correctly. As you can tell, I'm very bad at timing. Um, I thought it's stop at half past, but if you um so you have options. You can go have coffee. you can um complete um the rest of the tasks and ask questions, you know. Um or uh you know Yeah, you free to do anything you like or we can take a selfie together. I don't know. Do you want Yeah. Cool. Any more questions? No.

**[33:15](https://www.youtube.com/watch?v=lpTeJ0WpWyE&t=1995s)** Yeah. Yeah. I think we can finish. Sorry, I I thought it's end and a half past. I don't know why I'm like Okay. Sorry. Uh we thank you very much. Uh so yeah, an applause to her. [applause]
