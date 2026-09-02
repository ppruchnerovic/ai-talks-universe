---
id: dtq2qQaNStc
title: "Agentic AI Security Summit, Europe: ASI:04 Agentic Supply Chain"
slug: agentic-ai-security-summit-europe-asi-04-agentic-supply
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: []
channel: "OWASP GenAI Security Project"
duration_min: 9
published_at: 2026-01-21T06:44:57Z
video_id: dtq2qQaNStc
url: https://www.youtube.com/watch?v=dtq2qQaNStc
youtube_url: https://www.youtube.com/watch?v=dtq2qQaNStc
tags: []
transcript: true
---

# Agentic AI Security Summit, Europe: ASI:04 Agentic Supply Chain

**Speaker not identified**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=dtq2qQaNStc) · [Conference site](https://genai.owasp.org/)

## Description

In this session from the OWASP Agentic Security Summit (London, December 9, 2025), presents the Agentic Supply Chain risk, a core entry in the OWASP Top 10 for Agentic Applications. The talk explains why supply chain security fundamentally changes when systems move from static software builds to runtime, autonomous agentic systems.

Unlike traditional supply chains—where risk is introduced through package registries, CI/CD pipelines, or external dependencies—agentic systems dynamically select and interact with tools, MCP servers, other agents, and prompts at runtime. This creates new attack surfaces where legitimate-looking components can change behavior after deployment, silently expanding privileges or enabling data exfiltration.

Real-world examples highlight the danger, including MCP server updates that introduced subtle but malicious behavior, such as unauthorized blind carbon copies of emails to attacker-controlled addresses. These risks are difficult to detect because system functionality appears unchanged, while sensitive data quietly leaks.

Mitigations build on traditional supply chain controls but extend them for agentic environments: runtime verification of signed components, strict version pinning, avoiding automatic updates, enforcing least-privilege access, using organizational gateways or proxies for MCP servers, and maintaining rapid kill-switches to contain cascading failures. The talk also emphasizes sandboxing and isolation, especially where agents run with high privileges.

This session reinforces a key message: in agentic systems, the supply chain is no longer static—it is alive at runtime, and securing it requires continuous verification, monitoring, and containment strategies. These efforts are part of the broader work of the OWASP GenAI Security Project, including emerging initiatives like AI SBOM and MCP security guidance.

#OWASP
#owasptop10
#AgenticAISecurity
#GenAISecurity
#AISupplyChain
#MCP
#AgenticSystems
#Cybersecurity
#SecureAI
#AIAgents
#AIThreats

## Transcript

*1,290 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=dtq2qQaNStc&t=3s)** Thank you, Kayla. I'm so excited. Uh my name is Kapukin. Um and I'd like to to talk with you about the supply chain. Uh I led the supply chain item together with Amir and a very amazing team and we managed to get the emphasize how supply chain is different for the agentic system. As as many of you know as a practitioners the supply chain has been for a while and uh it's not going anywhere but we have some differences towards the agentic system because previously uh the system been compromised through the registry from the external dependency from uh CI/CD problems and now we have a genic system that are running in runtime deciding

**[0:54](https://www.youtube.com/watch?v=dtq2qQaNStc&t=54s)** whatever components they want to use and this is The major point we want to emphasize in the supply chain item for the agentic what are actually the vulnerabilities specifically to agentic supply chain and uh we know the system contains tools other agents and pron dynamically and this can be put in the system in a way the system is not expecting for them to behave. For example, when when our AI coding assistant gets a prompt uh from the description of the GitHub rep, it might it might get in the description the wrong meaning and it would lead to the AI coding assistant to behave in a different way. And that's only the the

**[1:42](https://www.youtube.com/watch?v=dtq2qQaNStc&t=102s)** briefly how we we already can see it when we use this tool. the system will be more in production and the problem will be more complex later on and uh while the system also is uh trusting the external components like the MCP servers uh we need to verify the privilege access is uh limited to only allowed actions because these MCP servers might change and they they might be different uh in the next version and I'll show you the one of the examples from the real world later on. And uh what basically we see the supply chain is not in a static way as in manifest when we built the system. The supply chain moving towards being dynamic and runtime. That's uh

**[2:31](https://www.youtube.com/watch?v=dtq2qQaNStc&t=151s)** that's the major difference and uh we specifically uh skipped some of the recommendations that were listed in the top 10 supply chain because this is a great source to learn about the in a in a static way when you do the system and highlighted the items in a dynamic uh what are the major risks and as Kayla explained the agent call can be can be moved by the simple instruction instruction and there is nothing can be done because LLM is mixing the data and instruction that's the way it works and for example uh when we use a tool when we get the tool looks right the names legit the description is okay but if you download the tool it can behave in a different way in a malicious

**[3:18](https://www.youtube.com/watch?v=dtq2qQaNStc&t=198s)** way uh and uh the problem might get worse when the system will rely on the tool for example we have an FCP serial and many many agents within the organization will trust on the serial because it is internal one and once the error propagates from the single agent that can go wild in the entire system that's the another risk and as as we saw in npm uh the types quoted problems with the libraries already a bit were noticed in MCP server registries so be careful when you uh when you find your MCP server and check the because uh it could lead in unintended action or behavior of the entire system. And uh to demonstrate the risk there

**[4:08](https://www.youtube.com/watch?v=dtq2qQaNStc&t=248s)** there are many examples and I I encourage you to explore the references in ASI foreign supply chain and other items and for for this talk I picked up the uh the research uh the co team uh shared with the community for the um postmark MC. So what what what happens few months ago uh there was a uh looking good MCP server that helped the agent to send the email via the service and it worked well. The developers was trusted the good GitHub repo everything is okay but with the new update the very little change came in just allowing this MCP server to blind copy towards the external address and obvious to the main controlled by an attacker and that's the

**[4:56](https://www.youtube.com/watch?v=dtq2qQaNStc&t=296s)** problem and when AI system updated the with the newer version of the MCP server the issue uh happened uh when the data excfiltration started getting through this MCP server and It's not easy to detect because uh when you update the version the mail is still going. You can see the data coming. Uh but if you don't have the proper control on a on a domain on external resources uh you will uh hardly notice uh this added behavior. And for the mitigations, uh the agentic supply chain of course is based on a traditional security measures. And on top of that, we want to highlight u something uh you can add to protect your

**[5:46](https://www.youtube.com/watch?v=dtq2qQaNStc&t=346s)** system is to use the signin components like MCP servers or agents and not only verify it at the build time and when you statically prepare the system to be run in production but it's recommended to to do it in a runtime as well uh because of the dynamic nature. Um and also the uh version pinning using the well tested version and avoiding the auto update for the uh for the components of the shending system uh might help and uh also the way you get the uh this external agents or MCP servers uh you could use the additional gateways in your organization to avoid uh having the untrusted MC let's say the example with the postark Mark having the new version

**[6:33](https://www.youtube.com/watch?v=dtq2qQaNStc&t=393s)** of CP server which was not tested uh which is untrusted but if you go for the company's gateway your security team uh can be able and to protect and avoid the data exploation in this case and uh in OASP in agentic security team the new MCP guides there is already guides for using FCP for party server and uh Tom and team they presented us a while ago and there will be more recommendations toward the securing this part in the future and also the initiative AI bomb which has already mentioned which will uh Helen will lead uh this also will help to uh to secure the components and make your system more secure and the last two mitigations um will help in a way if somehow you need

**[7:24](https://www.youtube.com/watch?v=dtq2qQaNStc&t=444s)** you will know that the system might be compromised you need a way to quickly uh damage control and turn off the engine or the tool or the MCP server or whatever just to avoid to propagate from the entire uh solution and the thing is very interested in particular I'm interested in how to sandbox and isolate environments because we know this is the best practice this is obviously we we as a developer many of us use AI coding tools but we use it on our own machines which has quite a lot of privileges sometimes and the case with shyut uh which exploded this very vulnerability show showing that when the engineer has an access to production when the agent go wrong it can lead to the detection and uh that's uh it for

**[8:15](https://www.youtube.com/watch?v=dtq2qQaNStc&t=495s)** the mitigation so the uh to summarize use the proxy uh gateways for the MCP servers version pinning and signing components and uh I'd like to pass the board to Stefan to talk about the inter agent communication
