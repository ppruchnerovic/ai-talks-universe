---
id: nlTn6-kyyFI
title: "Small Language Models for Tool Calling Are Better Than You Think [PyCon DE & PyData 2026]"
slug: small-language-models-for-tool-calling-are-better-than-you
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Gabi Kadlecova"]
channel: "PyData"
duration_min: 29
published_at: 2026-08-04T22:20:26Z
video_id: nlTn6-kyyFI
url: https://www.youtube.com/watch?v=nlTn6-kyyFI
youtube_url: https://www.youtube.com/watch?v=nlTn6-kyyFI
tags: ["PyCon DE", "PyCon DE 2026", "PyData", "Python", "conference talk", "data science", "machine learning"]
transcript: true
---

# Small Language Models for Tool Calling Are Better Than You Think [PyCon DE & PyData 2026]

**Gabi Kadlecova**

`PyData` · `PyData` · `2026` · `29 min`

`#PyCon DE` `#PyCon DE 2026` `#PyData` `#Python` `#conference talk` `#data science` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=nlTn6-kyyFI) · [Conference site](https://pydata.org/)

## Description

🔊 Recorded at PyCon DE & PyData 2026, 15.04.2026

🎓 Watch Gabi Kadlecova reveal how to leverage knowledge distillation to build small language models that outperform LLMs in specialized tool-calling tasks.

Speakers:
Gabi Kadlecova

Description:
Small Language Models (SLMs), typically defined as models with under 4 billion parameters, offer significant advantages over Large Language Models (LLMs) regarding latency, energy costs, and data privacy. Because SLMs can be deployed locally, they allow organizations to freeze model versions to ensure pipeline stability and keep sensitive data off external servers. While SLMs excel at classification, routing, and structured information extraction, they often struggle with complex tool calling—the process of selecting a function and providing correct arguments based on a user request—due to a tendency to omit arguments or select incorrect functions.

To improve tool calling performance, a knowledge distillation approach is used where a teacher LLM generates synthetic training data for a student SLM. The pipeline involves providing the teacher model with task descriptions, constraints, and a small set of real examples to generate a synthetic dataset of 1,000 to 10,000 examples. To ensure data quality, the pipeline filters out malformed JSON, removes hallucinated tools, and uses ROUGE comparisons to eliminate duplicate examples. The student model is then fine-tuned using supervised fine-tuning with Low-Rank Adaptation (LoRA) over a few epochs.

Experimental results using the Qwen 0.6B model demonstrate that this method can move a model from under 50% accuracy to near-perfect accuracy on simple tool-calling tasks. Key challenges in this process include ensuring full coverage of all available functions and parameters, varying user phrasing to increase robustness, and managing the complexity of multi-turn conversations. In multi-turn scenarios, the model must maintain accuracy across long sequences, as a single error in a chain of five calls can render the entire workflow incorrect.

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

*4,600 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=5s)** I'm Gabby. I'm a researcher at Dist labs. We are a startup based in Berlin but uh remote. Before I did my PhD on automated machine learning and now I am working on small language models and on tool calling and a bunch of other things with small language models. So I uh will first give you an intro what are small language models and then on tool calling and also on more complex cases of tool calling and then I will tell you how to make small language models better on tool calling by uh using synthetic tool calling data and last at the end unless I talk for very long I would like to talk you about uh challenges in generating good synthetic data for tool calling.

**[0:53](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=53s)** So, what are small language models? I don't think there's a formal definition. I'd say it's something that fits on your computer. If you have a good GPU, it might be larger. If not, then it's usually under four billion parameters. Um, I think for us it's uh yeah, under four billion, but it could be also under 10 billion, under 40 billion. Anything larger gets uh harder to train. and also possibly to deploy and uh we know that LLMs are much much larger than this [snorts] and when you want to create a small language models then you can either train it just like you would train an LLM or you could uh create it from LLMs so you could uh like prune them into a

**[1:41](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=101s)** smaller model that's one option or what we are doing uh is that you distill the knowledge from the larger model into the smaller one so that you can do roughly the same as the large one and that's what we do. Uh the question is why would we even use SLMs when we have the great amazing LLMs that can do almost everything nowadays and as we know they are large [snorts] which has also some disadvantages. So already it's been mentioned here that the energy costs are quite large. um also can be uh the latency can be large compared to a smaller model. So I'd say uh there's like two classes of advantages with small models. First is that usually they can be local and also uh they are small. So uh the local part

**[2:33](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=153s)** goes into data privacy. If your data shouldn't go to a foreign server, then you want to use either a smaller LLM or directly an SLM. And you can save a lot by using SLMs because they are small. And uh another thing is more like with uh the stability and data. So [snorts] when a new LLM version gets released, if your uh for example prompt engineering pipeline relied on that, then it maybe no longer holds because the newer LLM was trained a bit differently. So you kind of want to use the older version, but maybe you can't. So that's where you want to have the local model that you can just somehow freeze in time. And then the last part is that sometimes you want to fine-tune because uh either it's

**[3:22](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=202s)** more convenient for you than prompt engineering or you just really want to make sure that the model gets your data format right. Um so small language models can handle all kind well not all but some kinds of tasks. uh pretty well. For example, classification on routting. I think it's a good uh task for an SLM or even like an encoder model could be then uh extracting structured information that's also a pretty good task. And then question answering I think like in general text generation is also a good task for an SLM but if it gets more and more uh like uh complex let's say with a coding assistance if your SLM has only

**[4:12](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=252s)** like a few hund uh like let's say 300 million parameters it gets harder and harder to make it do the task. So maybe there's also like a trade-off between the task that an LLM cannot do and what an SLM can do. And today we will be focusing on function calling. So that is when a user has a request it should respond with a tool call. So how it works is that uh the model gets a list of available tools functions in the system prompt and it call can call some of them. So uh the user has a request and then the model should select one or sometimes more functions that will satisfy the respect and ideally it should fill in also good function arguments. [snorts] So for example if we

**[5:02](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=302s)** have here the user is asking to amend something to the last come uh latest comet then you call get comment you should say that it should amend and then you put the function in there uh the message in there but uh ideally it does that sometimes it doesn't so just a disclaimer this was generated using Q3 uh 0.6 six billion which I think is a pretty good SLM in terms of how you can train it. Uh nowadays you've got the newer Quen Q 3.5. Also Gemma 4 uh didn't have time to benchmark them yet. So I can assume they are a bit already better with uh function calling. Um maybe they are not perfect. Let's see in uh like a few weeks. And uh usually when you like have

**[5:52](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=352s)** a data set and you evaluate an SLM without training on it, it sometimes just forgets to add a good argument there. Uh so it's uh one of the outputs I got there just wasn't any amend just the message or uh when it was on bash function calling uh when you told it to go up one directory level it instead wanted to stay in the same directory and sometimes it just doesn't select the correct function. So when you have task like this technically you could do prompt engineering uh but uh I would maybe later get to the uh parts where I think this might be more uh more appropriate like to fine-tune that. Um this was a pretty simple case because

**[6:42](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=402s)** you had only one user request and one model response but you can have more complex workflows. So you might want to select the um tool call based on previous conversation history including the tool calls. Um so if you're working on a problem that's uh a sequence of task that go one after each other. Uh if you also include everything the performance may be better. Uh but the disadvantage is that the errors hurt a bit more or like more a property. So if you have a single tool call accuracy that's like 95% then that's quite good because only five times out of 100 you are incorrect. But if it's uh in multi-turn two calling and you respond with five two calls and

**[7:33](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=453s)** you have to like if you make at least one mistake in the sequence of 52 calls then uh almost like a quarter of your uh workflows is incorrect. So getting it right is really important here and uh that's perhaps why many many SLMs weren't or aren't usable out of the box for some of the like agentic tasks because you make one mistake and then it's kind of could be a crucial mistake and you cannot really use it. So there the bar on accuracy is quite high. Um just also uh to say there are more complex setups in multi-turn and sometimes you need to do use them because for example if you want to reason on contents on a file um

**[8:25](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=505s)** or on what the names of the directory are. You also need to include the tool response and uh that uh again makes it a bit larger and also you have to somehow um somehow deal with it. Similar when you have more complex user requests, you might want to have multiple tool calls. So it's not no longer one function but multiple functions you have to get them right and it's no longer select one function out of uh the available ones but it's multiple functions possibly with repetition. So like it's quite a hard machine learning problem in general and the last part is that you could also uh like have it like an chatbot mode. So not uh not only it will uh call the tool

**[9:17](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=557s)** call but it will also summarize it somehow or aggregate multiple uh two calls into one content. So it can get quite complex. Uh I will try to have like a simpler use case so that we know how uh to how to train for the simplest use case and then at the end we can talk about how it gets more complex with uh those uh cases. So how to train a model for tool calling? Uh so the thing is maybe you don't have enough data. Uh because to get to calling data you need users interacting with your functions. You need to create a large data set and have a sufficient coverage of what functions you have. So for us the answer is to

**[10:06](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=606s)** have synthetic data and use knowledge distillation. And how um how we can create the data is using an LLM. And knowledge distillation broadly is that a student model mimics outputs of a teacher model. And it can be either very simple or a bit more complicated. Either you can just predict the same text or you could try to align the logits like the outputs of the two models or sometimes when you have two similar models you could even try to align their layers. Uh for our case uh we have the simplest case. So we just create a synthetic uh collection of texts uh a synthetic training data set and uh it's basically we uh show real data to the

**[10:54](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=654s)** teacher and tell it create more data like this and then we train the student on this uh data and also on the real data. And as you may think the challenge here is uh making the data good and so to look into the whole pipeline. So we want to create the data and so we need to instruct the teacher well. So we take task description so that the model knows what uh are we solving. Maybe there are some constraints stuff like that. Then we collect training examples. Um, of course, probably the more the better, but uh we had cases where we had only like 10 or 20 training examples. Of course, for tool calling, it should

**[11:41](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=701s)** somehow cover the available functions even though you might have them in the task description because uh the list of tools is also part of task description. Even though you may have them, it would be nice to show their usage. But you can also supplement that with additional data. You could for example put in their man pages and uh something unstructured, no longer tool calling uh to make it better. And then you get to data generation. So you generate a batch of data and then you look if your data is good or not and you throw out the data points that aren't good, keep those that are and repeat until you have a sufficient size of your data set. Um then you fine-tune and then you have your SLM. So I will uh show you the pipeline on a

**[12:30](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=750s)** simple task is it's been adapted for a nice uh like benchmark leaderboard uh BFCL uh that's uh on function calling both single turn and multi-turn also some agentic parts but uh to kind of test the pipeline I created something more simple because for multi-turn there are parallel two calls and that overall just gets more complicated. So as the first step we allowed only one to two call per assistant turn and so I kept the same tools and then we generated a simpler conversation where we respond only with one to two call um and if we want to generate data from that we will instruct the LM. So generate an example on fun uh function calling you have these functions and it

**[13:20](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=800s)** should follow and then you make a list of JSON formatting requirements how it should look like etc. And finally you say it should look like those examples and you put in the conversation that's like user tool call user tool call and then a final tool call and uh then the LM generates something uh which is sometimes correct sometimes not. So you want to throw out obviously misformed examples. So if the JSON is not correct if there are some hallucinated tools you throw them out. uh sometimes but this is more like for smaller LLMs it's like certainly I will generate something for you okay let's just uh either toss it out or regex out your tool call just to

**[14:09](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=849s)** make it correct but then an really important part is to remove duplicates because sometimes the models uh tend to generate similar examples especially towards the end. So if you just have a data set of a lot of similar data then it's not going to be that good. Um we uh by default just have like a simpler rou uh comparison. So if it's like on token level too similar we throw it out. But you could get really creative here. Like if for example there's like a simil uh the sequence of the two calls that are called is always the same then you maybe want to instruct it to do something different or just throw it out and hope that something will get generated next time.

**[14:58](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=898s)** Uh so to repeat we generate a batch validate keep something and go on until we have the data set. Usually we end with something like uh 1k to 10k examples depends on the task. Uh but this is already enough. Uh some of the really simple ones were even okay with 100 examples. So it it doesn't need to be like 1 million of two calling scenarios to make it uh decent. Uh and then we fine-tune and that's just classical supervised finetuning. So we make it uh mimic the uh assistant responses only we do Laura and again only for a few epochs are necessary and uh yeah then we can just um it's

**[15:47](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=947s)** still like uh a public model no architecture changes so it integrates well with VLM or LMCP anything you like. So for this simple case uh the Q base QN that's the bottom row uh started with 85% accuracy which gets to less than 50% examples correct but then after the finetuning it got to like perfect or like near perfect accuracy. Uh so you can get pretty far if your task is simple and the nice part is that you can also like there some function calling models supported only single turn to calling that was with Gemma 3. Gemma 4 by the way can do multi-turn tool calling. Uh and when we did that uh we were able to

**[16:37](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=997s)** like make it learn multi-turn function calling. So that was like a nice uh use case of the approach like um learned a new way how to uh how to solve tasks also. Uh the fourth uh the third model is uh the liquid model and uh yep it's uh I mean it works [laughter] um it works but there may be some challenges like this was already quite simple which is okay because um some practical tasks just are simple but then there are like some challenges that you need to solve. So in identifying when a JSON is not a correct JSON is pretty easy on a code

**[17:25](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1045s)** level. Um but then identifying if the synthetic data is actually good like does it make sense like is it something that the user would ask or is it similar to the distribution that you're going to get in practice? That is a good question and uh if you have another answer than this then please tell me because it's uh I mean it's uh it's something that probably everyone who works with LM is asking yourself like I would just look into the generated data and see if it makes sense and see if there are any gaps like is there something that the model didn't capture or you could maybe use LLMs to judge like is this example okay or is it like conflicting with the job description that you had?

**[18:16](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1096s)** An important part here is coverage because uh if you don't generate a function at all, then you're just not training on that. Simple as that. And if an LLM thinks like a particular set of functions is good because it saw it a lot in the training data, then it might just generate more of that. So you want to somehow maybe stratif stratify sample and say hey please generate this function now or please generate this uh sequence of functions. Uh so that's one thing it could also forget to use some uh like parameters. When I started with the simple demo uh the function ls wasn't called with like a like list all files at all and then there was a single error on the test set. So you need you need to make sure

**[19:05](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1145s)** that the LLM generates like everything that you need to have there because we're fine-tuning and if it's not in the finetuning data then you're relying on what the model knew beforehand and also you're fine-tuning so maybe it's already forgetting what it knew before. Um but uh another point is that uh you should also like vary what the user requests are. So sometimes the user will say list or files. Sometimes they will just say like uh show me the directory and you should probably have different varants there so that it gets more uh robust to that and I think this is like a you have to compromise here because you can't or maybe you can but usually you can't generate 1 million data points. So you have to somehow make the data

**[19:53](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1193s)** representative enough and then like balancing both the functions and maybe the wordings is uh not trivial and uh you could do that for example via some clever mutations of the prompt. So you would know that you want like in 50% of time focus on function coverage in 50% of time change just uh like the user messages and uh then hopefully that helps uh we have an intern working on that so hopefully next pyon or something we'll have a talk about that so let's see uh then there are specific challenges with multi-turn these are really fun so just because there is a specific number of turns and you have to train it for your task that maybe the SLM or even the

**[20:43](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1243s)** LMS have never seen before. You have to cover all the realistic scenarios. So if you can have conversation up to 50 turns then you should make sure that you have the 50 turns because likely if it goes beyond that it's not going to be good or you need to do some windowing or summarization of the conversation. So that's definitely one challenge. It's also a question whether you should like uh train on uh parts of the conversations because when I started I didn't didn't train on like uh sequences of length one. So the model was really bad at the beginning and then it got better when the conversation got uh longer. Uh another part is like uh the tool outputs. uh if you generate them via LLMs then they may be just like

**[21:31](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1291s)** completely hallucinated like uh it will hallucinate the contents of your file if you want to do that. Uh so you could like connect it to an environment but then it uh might take a lot of time because uh you need to generate them tool by tool rather than just spitting out the whole conversation. So unless you are caching that's on also going to make the generation last longer. And then there's a separate part on the tool calls actually they have really nice blog post so you can check that out like um if it's like more agentic or if there are paral involved it gets much more complex because different sequences of two calls can lead to the same result and then you need to somehow reconcile that. So it's no longer comparing the function to function but it's also the

**[22:18](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1338s)** state of the environment and gets more it gets more complicated and fun. And the very last uh part is that when I started working on that I was a bit surprised because there weren't that many benchmarks or like suitable benchmarks. I mean uh there's the BFCL there's also some T square uh that's useful because most of the other ones and including some part of BFCL like test for example the performance over a lot of APIs but we are focusing on a one like specific task. So usually you would get like 10 test points or 20 test points per one function family. And if I want to evaluate if I fine-tuned my model, well, that's not exactly a lot because like okay, I got better by one

**[23:09](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1389s)** example. Yay. Um so it's uh I think hard and we are creating some of our data sets and uh maybe there will be even more or for example there will be some production traces that you can evaluate on but I think it makes sense to focus on this problem because in practice a lot of the uh workflows are on a limited uh function set so it's not like we should just study what LLMs can do across all possible APIs that we have but it makes sense to also look on specific tasks and then this is like a selling point for why we should do it like this even though like other approaches are totally valid for some specific use cases. So let's say you add a new function. So

**[23:56](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1436s)** you've got a nice set of 20 functions and you add a new one. So if you're using a a good LLM then you mostly don't care because you will just add it to the prompt and then it probably just works. Um then like if you can handle the costs then okay you don't need to listen to this talk necessarily. But uh if you want to use something smaller or open weight model, you probably now need to either do the prompt engineering. But uh I think that can be a bit unstable because if you prompt engineer on a new function, then it may like break everything that you had before. And in that case, I think just fine-tuning an SLM where you just add it to the existing data set. Okay, you have to pay some training costs, but then you have something small that

**[24:44](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1484s)** hopefully works and that you can control. So thank you for listening and uh I'm looking forward to the discussion. We can also talk afterwards after the talk and you can check uh we have other blog post and things. So thank you. [applause] [applause] >> Yeah, thank you very much for your talk and there's like a lot of interest in this room. There's a lot of questions so that's good. um we won't make all the questions but so yeah then talk afterwards and we'll probably move them to discord. So the first one how do you make sure that you do not overfit to the synthetic examples all produced from the teacher model. Um so we have a test set. So the test set should be different from the

**[25:33](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1533s)** training set. So hopefully that um makes like like it should be sufficiently different from the training set and the synthetic set so that you capture it. Um otherwise it's just like any other machine learning you try to combat it with all the machine learning techniques that you have for overfitting but I would say also like if you generate just more data and try to make it more diverse uh then you can somehow make it better. Hope that answered that. So then um we have another question. What was the motivation that you had to use an SLM instead of LLM in your use cases? Um so that company called Distill Labs. So the distill is distillations. So it's a company that works on SLMs. So that's

**[26:22](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1582s)** like the use case. [snorts] But uh it's also like I think it's interesting because um difficult like there are some task that are difficult. So those obvious need those LLMs. You need to like when you are coding then you want a really good coding agent that will just do it well but a lot of the task are simple and using an LLM on a really simple task is just like you could just go and burn those trees yourself like I mean so I'm a big fan of using a small tool for a small problem. Yeah. Okay. Then in which sectors or settings did you test this fine-tuning approach are SLM suitable for rack systems currently? >> Sorry,

**[27:10](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1630s)** which one is it? >> Okay. >> So it's like in which sectors or settings did you test your fine-tuning approach and would do you say SLM are suitable for the rack system? >> Yeah. Um as I said you can check out the website. There are other demos that you can look at. uh so I focus on tool calling mostly my colleagues I think there were some uh rack uh cases as well in general we uh do like many text generation cases yeah I think this would be like more a question to our colleagues because I don't also remember everything that we do all right we have another question did you try to adapt an SLM to a specific agent harness Yes. Oh, no, not yet. Easy answer.

**[28:01](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1681s)** Uh, let's see the next one um that we have. Yeah, I think we have time for one more. Um, how did you handle missing information in some of the teacher generated varants? Data set issues have caused my SLM to hallucinate quite a bit. Like I think those tasks were still pretty constrained. So I don't think I saw much hallucination there. Like obviously if it's going to be more complex then it gets more uh like more problematic. So I haven't seen hallucination after training especially when it's tool calling which is like a JSON output. So it's pretty easy to do that. Of course if there would be like open form uh parameters that may be an issue. Uh but the idea here is to just

**[28:52](https://www.youtube.com/watch?v=nlTn6-kyyFI&t=1732s)** fine-tune for the simple cases where um the models still make make mistakes. So then that is like a step three or four. >> Yeah, that's indicator. Yes. So thank you so much. I think yeah we're running out of time but like there we might move the other questions to Discord and so another applause for Gab. Thank you for sharing your insights. [applause]
