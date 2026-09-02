---
id: 0RNNfxpdbQk
title: "Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest"
slug: medic-for-apache-spark-first-aid-for-failing-jobs-drasko
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Drasko Profirovic"]
channel: "AI Engineer"
duration_min: 11
published_at: 2026-07-20T06:24:50Z
video_id: 0RNNfxpdbQk
url: https://www.youtube.com/watch?v=0RNNfxpdbQk
youtube_url: https://www.youtube.com/watch?v=0RNNfxpdbQk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Classic ML & data science", "Data engineering & MLOps", "Evals, observability & reliability"]
transcript: true
---

# Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest

**Drasko Profirovic**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0RNNfxpdbQk) · [Conference site](https://www.ai.engineer/)

## Description

In this talk, we’ll share the journey of building an agentic diagnostics tool to address one of the most time-consuming challenges in data engineering: troubleshooting Spark job failures at scale. As Spark workloads and platform complexity continue to grow, traditional dashboards and static playbooks are no longer sufficient. Our goal was to build an intelligent agent capable of automatically ingesting logs, correlating relevant context, and producing human-quality diagnoses and actionable recommendations in minutes rather than hours.

We’ll begin by covering the core design goals behind the system—accuracy, extensibility, and trustworthiness—and the architectural foundations we put in place to support them. We’ll discuss how we designed the agent around modular capabilities such as log parsing, pattern recognition, root-cause inference, and remediation suggestions; how we integrated it with Spark and broader platform metadata; and how we made it easy to extend the system to new error patterns and domains. We’ll also share how we approached evaluation and testing by building a corpus of real incidents, turning them into regression tests, and using them to continuously measure reasoning quality and safety. From there, we’ll explore what it takes to push agentic systems to their limits in production, including lessons on prompt and tool design, handling ambiguity in logs, reducing hallucinations, reasoning over partial or noisy signals, and striking the right balance between automation and human oversight. Along the way, we’ll highlight a few unexpected failure modes and how those informed later iterations.

We’ll close by discussing where we’re headed next: expanding beyond Spark into other data systems, and using engineer feedback loops to continuously improve its reasoning over time.

Speakers:
- Drasko Profirovic (Pinterest): Drasko is a Staff Engineer at Pinterest focused on agentic systems, drawing on a background in full-stack engineering and experience at Stripe and OpenAI to build the primitives and frameworks that enable scalable diagnostics, orchestration, and automated resolution.

## Transcript

*1,569 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=1s)** Hi. My name is Draško Proferović. I'm a staff engineer at Pinterest. Today, I'll cover Medic for Apache Spark, which is our agentic diagnostics tool built to troubleshoot Spark failures. We'll dive into why we built the Medic, the journey from prototype to the current architecture, lessons learned along the way, and what's next. A bit of background about myself. I had the opportunity to work at a few companies under the data platform org. Despite many differences between those companies, there's at least one similarity. The high bar for providing quality support to partner teams who rely on the infrastructure owned by the data platform org. I'm sure I'm not alone when I say that the support rotation feels like a

**[0:50](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=50s)** never-ending stream of questions or problems to resolve. Moreover, it's easy to forget how difficult it is to troubleshoot Spark or any distributed system for that matter. This is particularly true for anyone just getting started with the framework. The other challenge with supporting a load-bearing system comes down to ambiguous priorities. Do you focus on helping one team with their failing job, or do you unblock another team with a looming deadline? It's not always straightforward to rank these asks, but as humans, we often have to decide how we'll spend our time. The same is not true for LLMs. We can easily scale out knowledge and capabilities on demand. Our vision for a diagnostics agent

**[1:38](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=98s)** was to ask it simply, "Why did a job fail?" and get back a deep research document which provides evidence on the root cause of the failure. The agent would also need to provide suggested fixes that are grounded in the context of the job. Needless to say, this agent would need to be available on all the surfaces where our users operate today, like Slack or the Airflow UI to name a few. We started by exposing our data resources by way of the model context protocol as a way to connect them to the LLMs. At this point, we could start an LLM conversation with the MCP tools enabled and ask the model to reason about our Spark job. This worked in practice, but it required a lot of careful prompting from the

**[2:26](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=146s)** human operator. We extended our prototype by creating a single reasoning and acting agent, React for short. The agent was given a single prompt, which embodied the problem-solving approach it would take, how to structure the responses as a report, and specific examples to common failure patterns. At this point, we had enough capabilities to start trialing the solution with our beta users. From those early trials, we found a lot of shortcomings with our solution. Prompt tuning became unsustainable. One prompt had to do everything, and adding detail in one area degraded the behavior in another. Response quality was inconsistent. Sometimes analysis was shallow or other

**[3:16](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=196s)** times too verbose. We lacked controls to keep the agent on track. And we often hit context window issues for production jobs. As an example, large tool outputs from logs would click quickly consume tokens and brought a halt to the agent's reasoning. Lastly, our end-to-end testing strategy up to this point relied on manual tests from production. This felt anecdotal since production data would be retentioned away. Overall, it was hard to know if changes broke earlier wins. To improve the system, we invested in observability and testability. We used open telemetry to publish traces to LangFuse. And by viewing the agent's execution as

**[4:03](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=243s)** a waterfall diagram of steps, we could better understand the cause of lower quality responses. The reliance on manual end-to-end testing highlighted the need for a more reliable and scalable solution. We built an end-to-end test harness to snapshot production state. And we could codify expectations as offline evaluations. Lastly, this allowed us to tune our prompt based on the results. In practice, the end-to-end test harness is simple. In record mode, the agent calls real downstream systems, and tool responses are captured as fixtures. These are then saved to the file system and checked in as code. Playback mode, the agent runs against

**[4:52](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=292s)** fixtures instead of production data, but this time performs the analysis and generates the report. The test suite then grades the report based on the offline evals we have authored. For example, an offline eval might check for a limit of three suggested fixes. The eval would score lower if the agent provided too many fixes towards managing the verbosity of the final report. Our end-to-end tests allowed us to quantify quality instead of relying on intuition. And as we grew our test coverage, we gained confidence that improvements did not introduce regressions. Once we had the testing coverage in place, we invested deeper in our handling of logs. Logs are noisy, and many exceptions we

**[5:41](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=341s)** see in logs are benign. So, simply focusing the last exception may not always be suitable. Initially, we kept it simple with a heuristics based approach using regex to filter out certain exceptions. But, this didn't scale well. Instead, we built the exception classifier pipeline. The core idea was we would learn which exceptions commonly appear in successful jobs, treat those as likely red herrings, and filter them out in the future analysis. The agent would fingerprint and cluster exceptions, then rank them based on content relevance, and how recently they occurred compared to the termination of the job. The agent stopped consuming logs directly, and instead was given two MCP tools.

**[6:28](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=388s)** Get the top K truncated exceptions, or get full log details for a specific exception. This resulted in an improvement to our signal-to-noise ratio, and reduced the chance of the LLM to anchor its investigation with a misleading exception. Like logs, we found that we could improve the overall quality by investing in how we handle metrics. Raw time series metrics are not context window friendly. Simply feeding the raw data to an LLM works in the small scale, but fails for long-running jobs in production. Not to mention, it's horribly token inefficient. The approach we took was to perform metrics analysis in a quarantine sub-agent.

**[7:15](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=435s)** We would convert the raw time series data into graphs, which are then collaged into an final image. The appearance of which isn't much different than a Grafana dashboard, albeit with annotations that we found useful, like calling out the min and max values. The image is then attached the LLM conversation, and we would prompt the model to reason about patterns in the the Images worked better because we could guarantee how many input tokens would be used for analyzing any given Spark job irrespective of its duration. Examples of useful signals we would be able to get included executors dropping down to zero or near zero, long plateaus or bottlenecks, effectively any resource behavior

**[8:03](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=483s)** inconsistent with healthy progress. Our sub agent would summarize its findings and return the results back to the parent agent, thereby ensuring the context window is kept healthy. Lastly, we overhauled our agent harness. We went from a single react agent with multi-agent architecture. This was accomplished by building on top of LangGraph's deep agent library. Each agent now had a dedicated prompt and a subset of MCP tools. Meanwhile, the deep agent library itself provided built-in tools to keep the agent on track, like a to-do list or a virtual file system. This approach mirrors what we come to expect from our coding tools like Cloud Code or Codex, to name a few.

**[8:53](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=533s)** We could finally decompose our single prompt into specialized roles. This refactor provided clear separation of each agent and it made it easier for developers to maintain each prompt separately while performing focused testing on the system using our end-to-end test harness. A pleasant consequence of this architecture was that the effort to expand the scope of the project was as simple as adding a new prompt. And this is how we were able to extend the Medic to also help users optimize their Spark SQL jobs. Our workflow started starts with the user's request entering the system, whereupon intent is classified as either requiring a simple answer to a question or a deep diagnostic session. If it's the latter, the triage agent

**[9:42](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=582s)** determines the Spark job's life cycle state. And if it's failed, it'll use a subset of tools to generate a set of failure hypotheses. Each hypothesis is researched in parallel where we gather evidence to validate it. These research agents then return a score and a root cause. The supervisor selects the highest confidence root cause and invokes the healer agent to offer remediations based on runbooks ingested into our vector database. Lastly, the supervisor agent would assemble the final report ensuring proper formatting. The multi-agent architecture proved very effective offering us the greatest control over the system's behavior.

**[10:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=631s)** Enhancements to log handling led to substantial reduction in inaccurate root causes. We trialed using LangGraph's workflows to make the agent more deterministic, but this approach proved to be brittle compared to the reasoning and acting agent paradigm. What we're experimenting with now is incorporating user feedback from prior sessions to automatically improve the agent. Lastly, we see a broader opportunity to apply this pattern to other distributed systems like Flink and Trino. Medic for Apache Spark project was made possible by the hard work from these contributors. Thank you for your time.
