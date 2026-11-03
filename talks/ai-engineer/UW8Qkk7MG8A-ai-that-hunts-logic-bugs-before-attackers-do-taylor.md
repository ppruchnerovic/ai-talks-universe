---
id: UW8Qkk7MG8A
title: "AI That Hunts Logic Bugs Before Attackers Do - Taylor Luttrell-Williams, Sonar"
slug: ai-that-hunts-logic-bugs-before-attackers-do-taylor
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 14
published_at: 2026-10-28T19:00:15Z
video_id: UW8Qkk7MG8A
url: https://www.youtube.com/watch?v=UW8Qkk7MG8A
youtube_url: https://www.youtube.com/watch?v=UW8Qkk7MG8A
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Taylor Luttrell-Williams", "Sonar", "SonarQube", "SonarQube Hunter Agent", "AI security agent", "application security", "SAST", "business logic vulnerabilities", "broken access control", "IDOR", "OpenAI Daybreak", "AI Engineer", "AIE NYC"]
topics: ["Security, safety & red teaming"]
transcript: true
---

# AI That Hunts Logic Bugs Before Attackers Do - Taylor Luttrell-Williams, Sonar

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Taylor Luttrell-Williams` `#Sonar` `#SonarQube` `#SonarQube Hunter Agent` `#AI security agent` `#application security` `#SAST` `#business logic vulnerabilities` `#broken access control` `#IDOR` `#OpenAI Daybreak` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=UW8Qkk7MG8A) · [Conference site](https://www.ai.engineer/)

## Description

Pattern-based SAST catches bad code, but not valid code with flawed intent: broken access control, business logic gaps and authentication holes. Taylor Luttrell-Williams of Sonar introduces the SonarQube Hunter Agent, which maps a repo, runs three specialist agents and adversarially validates every finding, and announces Sonar joining the OpenAI Daybreak cyber partner program. The live demo turns up 46 issues in a Python app, including a user who can make themselves admin and an MFA bypass.

Chapters:
0:00 Intro
0:46 Why SAST misses intent bugs
2:37 How Hunter Agent works
4:12 Sonar joins OpenAI Daybreak
5:44 Layering SAST and Hunter Agent
6:27 Demo: running a scan
8:29 46 findings across three classes
10:01 Inside a broken access control bug
12:26 Scheduled scans
13:12 Automatic remediation

Taylor Luttrell-Williams

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*1,876 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=1s)** [music] >> Well, hello, good afternoon, and welcome all to my session on the SonarQube Hunter Agent. It's an AI security agent and built to detect the classes of vulnerabilities that SAST cannot and before attackers can. My name is Taylor Luttrell. I create developer content at Sonar. We're the makers of SonarQube. Today, I am very hyped to get y'all up and running with SonarQube Hunter Agent. So, to start, as we all know, in the agentic era, code is shipping at both

**[0:51](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=51s)** agentic velocity and agentic volume, and as a result, an unprecedented number of vulnerabilities are reaching production environments, leaving companies exposed and vulnerable. And if you're familiar or you actively use traditional pattern-based scanners like SAST, you may very well understand that there are classes of issues which it is simply not designed to account for. These are issues of intent rather than the patterns that it is adept at finding. And so, in explaining this, um basically, not all vulnerabilities are bugs in your code, at least according to SAST. And that's to say that the issues that it can find

**[1:41](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=101s)** are not always accounted for. These are issues of intent, issues related to logic-level vulnerabilities, wherein the code may very well be valid, but the intent itself is not. And that's to say that it's technically or it's functionally correct, but the intent behind it is flawed, right? It contradicts your underlying business logic, for example. Now, in many companies, pentests happen at most twice per year, perhaps once per quarter. But as attackers are now enabled with better models than ever, um and as the time between which these uh agent-generated changes are shipping, we

**[2:30](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=150s)** need a new class of agents to suss out, to detect, and to fix these vulnerabilities. So, I introduce SonarQube Hunter Agent to fill that gap exactly. So, in order to accomplish this, there's first an agent that maps the repository globally. And then, based on that global map, it starts three specialized agents, one per class of issue that it can find. And these issues look at relationships between all the components and try to define the security expectations, if you will. We then run adversarial validation to make sure that the issues are actually correct and not false positives. And we have noise gates as well to reduce the really low

**[3:17](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=197s)** um validity uh issues or issues that would be by design. And so, these playbooks essentially take a repository as input. They handle all the complex agent orchestration, and they output high-quality issues that you can then assign to your developers. In doing so, we assign a severity to these issues. We determine the impact that it can have on your overall codebase, and we point you to the exact location where they can be addressed directly. So, in representing these findings, if you already use SonarQube, these issues will surface alongside all of the other issues that we already look for using our SAST tool. As I said, you can assign a

**[4:07](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=247s)** um You can assign a severity to all of these. Um in the agentic era, where attackers are moving faster than ever, you need a solution that can keep pace with just that. As the time between a vulnerability being discovered and weaponized is shrinking, and it's shrinking now ever faster. And so, we are very excited to announce today, y'all are among the first to hear this, that Sonar is joining the Open AI Daybreak Cyber Partner Program. This is going to bring you governed access to advanced cybersecurity frontier models directly in products like SonarQube Hunter Agent. Because we recognize that security teams

**[4:59](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=299s)** need frontier intelligence, too. We have to keep pace with the very attackers that we are fighting against, and so we saw fit to include this as part of the very agent that susses out the classes of vulnerabilities that may be slipping through the cracks. We provide frontier reasoning inside SonarQube Hunter Agent. Playbooks run across the whole codebase. Every lead is investigated and validated before it surfaces, and these Daybreak class reasonings deepen the reasoning behind each playbook to ensure that all the findings are precise, they are repeatable, and are auditable, as well. In doing so, we recommend combining SAST and Hunter Agent and we do so in a

**[5:49](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=349s)** single platform to provide two layers of verification so that nothing slips through the cracks. SAST and SCA on one hand and Hunter Agent picking up the slack. This is layered security by design. It's zero trust, it's multi-layered, and it's independent to ensure that we can find zero-day vulnerabilities with precision and a repeatable manner. And that is SonarQube Hunter Agent in a nutshell. I'm now going to switch gears and I'm going to demo the product directly to give you all a sense of how it works in a real production setting. So, I have on screen a simple Python

**[6:40](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=400s)** application of mine which I have scanned with SonarQube Hunter Agent. I've logged in to my SonarQube Cloud dashboard here and if I navigate to Hunter Agent you can see that within the very same UI you can trigger an on-demand scan by clicking the scan now button. This is going to give you an estimation of the number of units required to perform the deep whole code base reasoning pass over your project on SonarQube. You should also note that this works either with SonarQube Cloud or with our self-hosted variant SonarQube server. So, were I to click scan now, it would kick off a scan of the project.

**[7:28](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=448s)** Depending on the size and the complexity of the project it can take upwards of an hour so I I went ahead and ran a scan on this project already which I'm going to walk you through now. The scan took about an hour to complete and then scanning the project at first securely clones the target repository to grant the AI engine direct access to the source code. It then analyzes the application architecture to map potential attack surfaces and build a comprehensive threat model. It next executes deep contextual scans to detect critical flaws like IDOR, broken access control, and business logic vulnerabilities and it aggregates and deduplicates findings from all specialized AI sub-agents into a single

**[8:17](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=497s)** unified issue list before lastly automatically exporting and logging validated vulnerabilities directly into your SonarQube's issue list. So after having completed, I can click into scan results to surface all of those issues that the Hunter agent found. You can see here that there are 46 open issues on this project broken across the three issue categories that I touched on earlier. Those being broken access control vulnerabilities, business logic vulnerabilities, and authentication and session vulnerabilities. So to quickly recap, these broken access control vulnerabilities relate to such things as insecure direct object references or IDOR, missing or incorrect

**[9:06](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=546s)** authorization checks, privilege escalations, sensitive data exposure, and cross-site request forgery. Moving on to business logic, this relates to such things as skipping required workflow steps, abusing repeatable actions, and missing rate limits. And then lastly, those authentication and session issues as I had mentioned pertaining to broken access or broken authentication, I should say, session fixation, non-expiring sessions, weak password recovery, missing multi-factor authentication, and brute-force gaps. So, I'll go ahead and click into these broken access control and I'll pick an issue at random. Note that these surface in the same issues list as every other issue that's scanned by SonarQube, so you don't have to navigate to a new

**[9:54](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=594s)** dashboard to surface um and inspect all of these. So, I'll go ahead and click into broken access control. You can see at the very top we have a an issue which has been rated high in severity. All of the issues are tagged with Hunter Agent as this was the AI agent used to surface them in the first place, and then also the class of issue that it pertains to as well. In trying to help you remediate these issues, we first show you where specifically within your code base the issue has surfaced, as well as providing an explanation as to why this is an issue. So, in this instance, as you can see, the issue pertains to any signed-in user being able to pass the admin access check

**[10:42](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=642s)** because they can write their own role field. So, you we walk you through basically why this is an issue and then also point you to how you can go about fixing it as well. Any activity as well related to the issue at hand, and you can assign the issue like you can any other SonarQube issue to the developers of your choosing. All issues um open uh are uh started in an open state by default, and you can either accept the issue, meaning that it is indeed valid, it's not a false positive, but it will not affect your quality gates, and therefore it will not prevent the code you're trying to ship from entering uh production. You can confirm it, meaning that the issue is valid and it will will

**[11:30](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=690s)** fact have an impact on the quality gate or you can mark it as a false positive if you really and truly believe that the fix is incorrect. So, navigate back to the scan that we had conducted. We have also uh five business logic findings and a number of authentication and session findings as well. I'll go ahead and click into one of these just for more breadth. You can see here at the very top, we have another high severity security vulnerability. This one pertaining to any user with only an account password being able to reach every protected route including admin functions without completing multi-factor authentication. Again, we point you to where in your code the issue resides as well as why

**[12:19](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=739s)** it's an issue, how you can fix the issue, and then again, any activity related to it. Note that while the Hunter Agent can be run on demand, it can also be run on a scheduled basis. So, if I navigate here to Hunter Agent, I can configure a scheduled scan whereby I can run it at the frequency of my choosing. It's highly configurable. Uh be that daily or weekly or monthly. And I can also select a specific branch should I not want to scan the main branch specifically. [snorts] This case, I scanned the main branch. And that is Hunter Agent in a nutshell.

**[13:12](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=792s)** In pointing you towards these classes of business logic level vulnerabilities, we suggest fixes, but I am excited to announce that as of this week these issues will also be able to be fixed in a remediated or in a automatic fashion. I should note. You can in fact assign these issues to the SonarQube remediation agent which can take care of remediating these classes of security issues for you and also on a scheduled basis. And that is SonarQube Hunter Agent which will enable you to catch logic level vulnerabilities before anybody else does so that you can hunt for issues before you yourself are

**[14:00](https://www.youtube.com/watch?v=UW8Qkk7MG8A&t=840s)** hunted. Thank you very much.
