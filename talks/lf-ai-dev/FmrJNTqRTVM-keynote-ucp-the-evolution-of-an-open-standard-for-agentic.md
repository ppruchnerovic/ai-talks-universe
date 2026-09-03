---
id: FmrJNTqRTVM
title: "Keynote: UCP: The Evolution of an Open Standard for Agentic Commerce - Anurag Sinha"
slug: keynote-ucp-the-evolution-of-an-open-standard-for-agentic
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "General software conferences"
edition: "Open Source Summit + ELC NA 2026"
year: 2026
speakers: ["Anurag Sinha"]
channel: "The Linux Foundation"
duration_min: 11
published_at: 2026-06-03T18:24:51Z
video_id: FmrJNTqRTVM
url: https://www.youtube.com/watch?v=FmrJNTqRTVM
youtube_url: https://www.youtube.com/watch?v=FmrJNTqRTVM
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Keynote: UCP: The Evolution of an Open Standard for Agentic Commerce - Anurag Sinha

**Anurag Sinha**

`AI_dev / Open Source Summit (Linux Foundation)` · `Open Source Summit + ELC NA 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=FmrJNTqRTVM) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Join us at the premier vendor-neutral open source conference, where developers and technologists come together to collaborate, share knowledge, and explore the latest innovations and advancements in open source technology. Learn more at https://events.linuxfoundation.org/

Keynote: UCP: The Evolution of an Open Standard for Agentic Commerce - Anurag Sinha, Senior Staff Software Engineer & Manager, Google

The commerce landscape is undergoing a fundamental shift from a "click-to-buy" web to an "intent-to-execute" agentic ecosystem. At the center of this transformation is the Universal Commerce Protocol (UCP), an open-source standard designed to eliminate fragmentation between AI surfaces and merchant platforms.

This session provides a deep dive into UCP's foundational architecture, exploring its core primitives and its unique capability-based system that allows AI agents to interact seamlessly with diverse retail backends. We will trace the journey of the protocol from its initial launch to its current state, highlighting key milestones in its technical evolution—including expanded support for diverse transport layers and its integration into major AI-native environments.Beyond the technical specifications, the talk will examine the real-world impact of UCP: how it is lowering the barrier to entry for smaller retailers, decentralizing commerce, and enabling a more fluid, secure, and interoperable future for global trade.

Attendees will gain a clear understanding of how this evolving standard is becoming the connective tissue for the next generation of digital transactions.

## Transcript

*1,558 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=0s)** Hello everybody and welcome to this talk on Universal Commerce Protocol UCP and how it is enabling agentic commerce to stay interoperable, extensible, and open. Commerce, as we know it today, is moving from a traditional show-me model to a help-me model. What that means is today when we do online shopping, the standard is to go look for products, browse for them, compare products, and then when we have made up our mind, we go ahead with a purchase. In the agentic era, this is something that is completely delegated to agents that ask, decide, and act on our behalf across the full funnel of commerce operations from product discovery until purchase. This is a very empowering paradigm as with everything agentic and hence is

**[0:47](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=47s)** gaining steam. A research from Bain and Morgan Stanley shows that agentic shopping could hit 10 to 25% of US e-commerce by 2030. Let's take a minute to talk about the complexity behind the scenes for powering agentic commerce. Despite having the same unilateral commerce operations such as catalog, catalog lookup, checkout, discovery, etc., different businesses have different systems, rules, and workflows that power them, which is very esoteric to their domain and has a bunch of nuances. Add to that the complexity that every agentic or a general consumer surface has to go through when they have to integrate with each of those businesses for those nuances.

**[1:35](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=95s)** It results in a lot of bespoke connections between agents and businesses and a lot of fragmentation across the ecosystem. This fragmented bespoke convolutional mesh is something that becomes a bottleneck for training AI agents in performing streamlined commerce operations and hence this necess- necessitates a need for a shared language, without which it is akin to a mall where the escalators don't connect with each other. This is where UCP comes in, being the same language in this new frontier. UCP solves couple of problems. The first one is it provides common building blocks for these commerce operations that have a unified interface across businesses

**[2:24](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=144s)** and makes it easy for agents to speak the same language. So, there is for example, there is going to be a common interface for how checkout can be done, a common interface for how catalog operations can be done, a common interface for how cart operations can be done. And the the esoteric complexity of each business is abstracted away because of that common language across. This results in one standard and many possible experiences across agentic surfaces, businesses, and payment providers. The second problem it solves is that every business has its own way of selling. So, for example, a local shop that is selling goods probably doesn't offer ship to home, whereas a marketplace or large retailers probably

**[3:12](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=192s)** offer more sophisticated omni-channel fulfillment methods that range from the spectrum of ship to home to pick up online, reserve in store, etc., so on and so forth. UCP, through its mechanisms of discovery and profile agentic profile agentic and business profiles, offers the ability for businesses to advertise exactly the spectrum of commerce operations that it supports and allows agents to autonomously crawl and discover where the discover those and figure out if there is the right compatibility for an agent to perform those operations. So, the same standard can serve retailers, marketplaces, store builders, payment providers, and smaller merchants across the spectrum. Next, let's take a quick look at the

**[4:01](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=241s)** architecture of the Universal Commerce Protocol and how it enables these. UCP has a multi-layered architecture. The top layer is something that we call as services. Services effectively represent the different common the different verticals and domains which the which the protocol is powering. So, for example, shopping is a domain. Because UCP is built to be vertical extensible, tomorrow domains like travel, etc. can very well emerge. We have a common vertical which houses capabilities which can be reused across verticals today. The second layer is what we call as capabilities. Capabilities are the core features of a particular domain that need to be supported. For example, in

**[4:50](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=290s)** case of shopping, checkout can be a capability. Order management can be a capability. Catalog lookup, etc. can be a capability. In the common services, something like identity management or identity linking can be a capability, a core feature that is shareable across different verticals. The third layer is extensions. Extensions are are exactly that, extensions. So, one of the conscious choices that we made when designing UCP was to ensure that the protocol is composable enough. So, for example, there is no need to tie something like fulfillment tightly with checkout because as mentioned in the example before, depending on the size and the spectrum where a business lie, the fulfillment options provided by the

**[5:38](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=338s)** particular business can be very different compared to that of, you know, a differently sized business. Which is why something like fulfillment is modeled as an extension that can decorate different capabilities across checkout, uh ca- ca- catalog, cart, and order in the context of that operation, ensuring that we have we don't have a rigid structure, and it is very composable. The last layer of this protocol is the transport layer. UCP has been built to be transport agnostic. The fundamental tenant behind this is that UCP capabilities and extensions define the shape of objects for different verticals and services, which can communicate over different types of transports. So, today

**[6:26](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=386s)** we support REST, MCP, A2A, and it is since it's open source, anytime a new transport comes in, it's relatively straightforward to add a binding for that transport. This allows agents, businesses talking over different transports to still preserve the UCP shape, to still preserve the rules of the protocol and the interactions, and perform commerce operation as needed without having to worry about rewiring their existing stack. All of these come together between the consumer platforms or agentic platforms and business platforms, uh and enables the facilitation of agentic commerce. So, the end goal behind this is this becomes as as this evolves and as UCP proliferates more and more within businesses and more and more

**[7:14](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=434s)** agentic surfaces accommodating it, it it becomes the shared language over agents can easily connect over businesses. They crawl, they discover that business A does five capabilities over UCP. They know the exact contract and the exact interfaces that are exposed, and they can start performing commerce operations with them. In the spirit of open source and the great uh uh conversation that uh Jim just had. Uh, this is a standard that is for everyone and should definitely be shaped by everyone. And that is the primary reason why UCP is an open source protocol. Uh, it's very easy for merchants, retailers, uh, businesses of different sizes, or community contributors, all sorts of parties to open up a GitHub discussion or a pull

**[8:03](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=483s)** request about their uh, unique use cases, which is then reviewed by a group of council members, and then we eventually get it into uh, the broader ecosystem. This goes in the protocol and that that is and then eventually is exposed to the broader ecosystem. This allows the diversity that UCP effectively needs to account for all sorts of different use cases that are there still being provided under that unified interface of commerce operations and allowing agents to work autonomously and equitably for all types of use cases and all types of businesses. This openness keeps the ecosystem moving. A quick timeline on where we started and where we are today. So, January 11th, 2026 is when UCP was launched co-developed by Google and key industry

**[8:52](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=532s)** partners. After that, we launched UCP-powered checkout in AI mode on Google Search and on Gemini with a couple of partners. March 2026 is when the protocol was modified and more new capabilities such as cart, catalog, et cetera were added. April is when Amazon, Meta, Microsoft, Salesforce, and Stripe joined the tech council to help shape the protocol's technical direction and bring in the goodness of their respective industries. And we have more UCP updates and strategic expansions being announced. So, please stay tuned. This is more of a call to action. I think UCP by nature is an open infrastructure. An open infrastructure works best when participants can plug in. The goal is broad inter interoperability across all businesses,

**[9:40](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=580s)** all entities, and not a closed system. So, code development here matters really more. And similarly, we are in the nascent stages of agentic commerce. There is still a lot to shape on how agentic commerce manifests. There is still a lot of lot to shape on how agents can be trained to perform streamline commerce operations. These are some resources on UCP. This is definitely This is the perfect place for a call to action in this open source community. Please learn, experiment, build, and contribute. Take a look at the repo, suggest issues, raise PRs or different use cases, and how to make this protocol better. Look at the knowledge base there on how folks are using this protocol for different sorts of use cases. Finally, thank you. This QR code allows you to earn a skill badge for your

**[10:28](https://www.youtube.com/watch?v=FmrJNTqRTVM&t=628s)** Google developer profile that shows your knowledge on UCP. Thank you. >> [applause] >> Thank you for
