# AI Conferences & Recorded Talks

Curated list of leading AI conferences with a practical focus (software development, AI engineering, AI adoption, security), with links to their sites and the YouTube channels/playlists where recorded talks are published — for later transcript extraction.

Verified 2026-08-30. Availability legend: **✅ free** = full talks openly on YouTube · **⚠️ partial** = keynotes/subset on YouTube, rest gated · **❌ gated** = not usable for open transcript extraction.

## Already watching

### AI Engineer (World's Fair / Summit)
- Site: https://www.ai.engineer/
- YouTube: https://www.youtube.com/@aiDotEngineer/videos
- The flagship practitioner conference for AI engineers (agents, LLM apps, MCP). ✅ free — full talks from all tracks.

### AI Dev (DeepLearning.AI)
- Site: https://ai-dev.deeplearning.ai/
- YouTube: https://www.youtube.com/@Deeplearningai/search?query=AI%20Dev%2026%20x
- DeepLearning.AI's developer conference. ✅ free.

### QCon AI
- Site: https://ai.qconferences.com/
- YouTube: https://www.youtube.com/infoq
- InfoQ/QCon's enterprise production-AI conference. ⚠️ partial — fresh recordings go to the paid Video Pass first; a free subset drips onto the InfoQ channel and https://www.infoq.com/presentations/ (with transcripts) over subsequent months.

### WeAreDevelopers
- Site: https://www.wearedevelopers.com/en
- YouTube: https://www.youtube.com/@_wearedevs/videos
- Agenda: https://app.wearedevelopers.com/events/16 (World Congress 2026, seeded — see below)
- Europe's largest developer congress (Berlin), heavy AI programming. ✅ free.
- The World Congress recordings are on that channel but **not on its `/videos` tab**, so enumeration cannot reach them: exactly 1 of the 358 congress talks turned up in the 700 videos it lists. Their ids come from the congress agenda API instead, via the corpus at `../presentations/kb`, and are registered as a `"videos"` source reading `data/seeds/wearedevelopers-wwc26.json`. `import_kb.py` writes that seed; nothing about it touches the network. That source carries `"scope": "all"`, so the whole congress programme is kept — the security, testing, reliability and platform sessions included — while the channel listing above stays filtered to AI talks.

### AI DevCon (Tessl)
- Site: https://tessl.io/devcon/
- YouTube: https://www.youtube.com/@tessl-ai
- Tessl's conference on AI-native software development. ✅ free.

## AI engineering & agents (top picks)

### LangChain Interrupt
- Site: https://interrupt.langchain.com/
- YouTube: https://www.youtube.com/@LangChain — [Interrupt 2026](https://www.youtube.com/playlist?list=PLfaIDFEXuae2uJrYpdMZz_HbFfCfYIlVR) · [Interrupt 2025](https://www.youtube.com/playlist?list=PLfaIDFEXuae3LIv3FbwVmqxw-s_WqP8iy)
- LangChain's agent conference — production AI agents at Apple, Cisco, LinkedIn, Toyota. ✅ free (also at interrupt.langchain.com/recordings, no signup).

### Anthropic — Code with Claude
- Site: https://claude.com/code-with-claude
- YouTube: https://www.youtube.com/@claude — [2026 SF](https://www.youtube.com/playlist?list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR) · [2026 London](https://www.youtube.com/playlist?list=PLmWCw1CzcFilPJdvw6scjHjbBripZWFps) · [2026 Japan](https://www.youtube.com/playlist?list=PLmWCw1CzcFinrtcyN6EMIp6KqrDj8sxD7) · [2025 (on @anthropic-ai)](https://www.youtube.com/playlist?list=PLf2m23nhTg1P5BsOHUOXyQz5RhfUSSVUi)
- Anthropic's developer conference — Claude, Claude Code, MCP, agent building. ✅ free (workshops not published).

### OpenAI DevDay
- Site: https://devday.openai.com/
- YouTube: https://www.youtube.com/@OpenAI — [DevDay 2025](https://www.youtube.com/playlist?list=PLOXw6I10VTv8-mTZk0v7oy1Bxfo3D2K5o) · [2024](https://www.youtube.com/playlist?list=PLOXw6I10VTv_o0ZLpFu2IQyQOho1l-v7y) · [2023](https://www.youtube.com/playlist?list=PLOXw6I10VTv-exVCRuRjbT6bqkfO74rWz)
- OpenAI's annual developer conference (next: Sep 29, 2026). ✅ free — keynotes + breakouts.

### MCP Dev Summit (Agentic AI Foundation)
- Site: https://events.linuxfoundation.org/mcp-dev-summit-north-america/
- YouTube: https://www.youtube.com/channel/UCgkApalw5crKXOtr_mqtPQg — [NA 2026](https://www.youtube.com/playlist?list=PLjULwdJUtFdhIBhibLEogtK1XYCNaFyFl) · [Europe 2025](https://www.youtube.com/playlist?list=PLjULwdJUtFdjEl2jZif3XgtTgvNDpJFlO) · [May 2025](https://www.youtube.com/playlist?list=PLjULwdJUtFdigAsQ_GMzcPyXaZOeLG04L)
- The Model Context Protocol's own conference, now under the Linux Foundation's Agentic AI Foundation — servers, gateways, auth, tool design, agent interop. ✅ free — full sessions. Registered per edition rather than by channel: the same channel also carries "The Context" livestreams and shorts, which are a podcast, not a programme.

### MLOps World | GenAI Summit + Toronto Machine Learning Summit (TMLS)
- Sites: https://mlopsworld.com/ · https://www.torontomachinelearning.com/
- YouTube: https://www.youtube.com/@tmls-ai — [MLOps World 2025 sessions (66 videos)](https://www.youtube.com/playlist?list=PLlcxuf1qTrwDJjGqDG0XuCzCeTEaEZ-uo)
- Practitioner events on production LLMs, RAG, agents, MLOps; one channel covers both. ✅ free — full sessions.

### Ray Summit (Anyscale)
- Site: https://www.anyscale.com/ray-summit/2026
- YouTube: https://www.youtube.com/@anyscale — [Ray Summit 2025 keynotes](https://www.youtube.com/playlist?list=PLzTswPQNepXnD-PksryocyeOPdK6CyZw6)
- Distributed AI infra, LLM serving, vLLM/Ray ecosystem. ✅ free.

### PyTorch Conference
- Site: https://events.linuxfoundation.org/pytorch-conference-north-america/
- YouTube: https://www.youtube.com/@PyTorch — [PyTorch Conference 2025 (117 videos)](https://www.youtube.com/playlist?list=PL_lsbAsL_o2BUUxo6coMBFwQE31U4Eb2q)
- PyTorch Foundation's annual NA + Europe conference: open-source AI engineering, vLLM, LLM infra, agents. ✅ free.

### PyData
- Site: https://pydata.org/
- YouTube: https://www.youtube.com/@PyDataTV — [PyData Global 2025 (84 videos)](https://www.youtube.com/playlist?list=PLGVZCDnMOq0qmerwB1eITnr5AfYRGm0DF) + per-city playlists
- NumFOCUS-run global series on practical Python ML/LLM tooling. ✅ free — one of the largest practical ML talk archives.

### The AI Conference
- Site: https://aiconference.com/
- YouTube: https://www.youtube.com/@aiconference
- Annual SF builder conference with LLM, agentic AI, and infra tracks. ✅ free.

### Berkeley RDI — Agentic AI Summit
- Site: https://rdi.berkeley.edu/events/agentic-ai-summit
- YouTube: https://www.youtube.com/@BerkeleyRDI — [2026 talks](https://www.youtube.com/playlist?list=PLVQ6wYubSX6A) · [2025](https://www.youtube.com/playlist?list=PLS01nW3RtgorSROLaDrF1YR34f0A3CnJS)
- UC Berkeley's summit where agent research meets production practice (Dawn Song's centre; the LLM Agents MOOC lineage). ✅ free. The per-talk playlist is registered, not the parallel [whole-day stage streams](https://www.youtube.com/playlist?list=PLVs8SZOx0kX8), which would enter the corpus as four-hour "talks"; the channel itself is not registered, since most of it is MOOC lectures and blockchain work.

### AI Council (formerly Data Council)
- Site: https://www.aicouncil.com/
- YouTube: https://www.youtube.com/c/DataCouncil/videos
- Builder-first conference on the AI and data stack, renamed from Data Council for the 2026 edition; ten years of technical talks on one channel. ✅ free. Registered `scope: "ai"` with a recency cap — the older Data Council years are data engineering (Kafka, Airflow, warehouses), and only the AI half belongs here.

### dotAI
- Site: https://www.dotai.io/
- YouTube: https://www.youtube.com/@dotconferences
- Curated single-track European conference (Paris) of 20-minute talks for engineers building AI. ✅ free.

### Weights & Biases — Fully Connected
- Site: https://wandb.ai/ (event: fullyconnected.com)
- YouTube: https://www.youtube.com/@WeightsBiases — [Fully Connected Tokyo 2025](https://www.youtube.com/playlist?list=PLD80i8An1OEEh-4vRV5PF6MgN7OYRB7v4)
- Practitioner series (SF/Tokyo/London) on LLM evaluation, agents, MLOps. ✅ free.

### Applied Machine Learning Days (AMLD)
- Site: https://appliedmldays.org/
- YouTube: https://www.youtube.com/c/AppliedMachineLearningDays (now branded "AMLD Intelligence Summit")
- EPFL Lausanne (Feb); Europe's largest applied-ML event, applied-research/industry mix. ✅ free.

## Software dev conferences with strong AI tracks

### GOTO Conferences
- Site: https://gotopia.tech/
- YouTube: https://www.youtube.com/@GOTO-/videos
- Multi-city software engineering series with growing AI/LLM content. ✅ free — released ~daily over the year after each event.

### NDC Conferences
- Site: https://ndcconferences.com/
- YouTube: https://www.youtube.com/@NDC/videos
- Year-round dev conference series (Oslo, London, Copenhagen, Sydney…); heavy practical AI/LLM/Copilot content. ✅ free — batch-uploaded ~a month after each event.

### Devoxx
- Site: https://devoxx.com/ (flagship: https://devoxx.be/)
- YouTube: https://www.youtube.com/@DevoxxForever/videos
- Community-run dev conference family; Belgium publishes all ~200 talks during/right after conference week. ✅ free. (France/UK/Poland editions use separate channels.)

### InfoQ Dev Summit / QCon
- Sites: https://devsummit.infoq.com/ · https://qconferences.com/
- YouTube: https://www.youtube.com/@infoq/videos
- Senior-engineer conferences, now very AI-engineering-dense (agents, RAG, context engineering). ⚠️ partial — free versions drip out over months; not every talk guaranteed.

### KubeCon + CloudNativeCon (AI day / AI inference & agentic tracks)
- Site: https://www.cncf.io/kubecon-cloudnativecon-events/
- YouTube: https://www.youtube.com/@cncf — [KubeCon EU 2026 (411 videos)](https://www.youtube.com/playlist?list=PLj6h78yzYM2MXCOWSN9CqqID6OOvF7wxL) · [Cloud Native AI + Kubeflow Day 2026](https://www.youtube.com/playlist?list=PLj6h78yzYM2PnalRBhPCbxEm_rup1b3X0)
- Production AI infra — GPU scheduling, inference, agentic workloads on Kubernetes. ✅ free — all keynotes + breakouts shortly after each event.

### AI_dev / Open Source Summit (Linux Foundation)
- Sites: https://events.linuxfoundation.org/ai-dev-europe/ · https://events.linuxfoundation.org/open-source-summit-north-america/
- YouTube: https://www.youtube.com/channel/UCfX55Sx5hEFjoC3cNs6mCUQ — [AI_dev Europe 2025](https://www.youtube.com/playlist?list=PLbzoR-pLrL6oAsF17rJsdZ0NiKnb2-xD1) · [AI_dev Europe 2024](https://www.youtube.com/playlist?list=PLbzoR-pLrL6oII-dLqw9vpif0U_kTycj6) · [AI.dev 2023](https://www.youtube.com/playlist?list=PLbzoR-pLrL6qDStieLBJLajZMcQVgwlxA) · [OSS + ELC NA 2026](https://www.youtube.com/playlist?list=PLbzoR-pLrL6p2URzlq8xlNtBhPspd2xpi) · [OSS EU 2025](https://www.youtube.com/playlist?list=PLbzoR-pLrL6qKwLt8A787ggMLHNivOHve)
- Open-source GenAI and ML infrastructure — training, inference, model serving, governance. ✅ free. AI_dev ran standalone through 2025 and is folded into Open Source Summit from 2026, which is why one conference here carries both: the AI_dev playlists override to `scope: "all"` (the whole event is AI), while the Open Source Summit playlists keep the conference's `scope: "ai"` and contribute only their AI sessions.

### GitHub Universe
- Site: https://githubuniverse.com/
- YouTube: https://www.youtube.com/@GitHub — [Universe 2025](https://www.youtube.com/playlist?list=PL0lo9MOBetEFKNlPHNouEmVeYeyoyGTXC) · [Universe 2024](https://www.youtube.com/playlist?list=PL0lo9MOBetEF_de7yKAWpnMkTsKH6aJ4P)
- The key event for AI-assisted development (Copilot, agentic coding). ⚠️ partial — keynotes + curated sessions on YouTube; full breakout catalog via the (free) registration portal.

## AI security

The corpus keeps talks from 2023 onwards; **CAMLIS, DEF CON AI Village and
BSides Las Vegas** are the exception and keep their whole back catalogue
(`"min_year": null` in `conferences.json`). Elsewhere 2022 and earlier is a different subject —
applied ML, data engineering, MLOps before LLMs — and reads as noise beside
what the same conference publishes now. Here it is the same subject: adversarial
ML, model evasion, data poisoning and deepfakes were being presented years
before the vocabulary changed, and the work has not been superseded by it. It is
also most of what these three have — 36 of DEF CON AI Village's 37 talks are
2019-21, and a flat floor would leave the conference with one.

### CAMLIS — Conference on Applied Machine Learning in Information Security
- Site: https://www.camlis.org/
- YouTube: https://www.youtube.com/channel/UCmIY4lIVsotxeUDRCQb2ZXA/videos
- The premier practitioner conference at the ML/infosec intersection — AI red teaming, LLM attacks, ML for detection. ✅ free.

### DEF CON AI Village
- Site: https://aivillage.org/
- YouTube: https://www.youtube.com/@aivillage/videos + DEF CON playlists at https://www.youtube.com/@DEFCONConference/playlists (e.g. [DEF CON 27 AI Village](https://www.youtube.com/playlist?list=PL9fPq3eQfaaBy_EIgmLzo45NLo9o9dAHZ)); archive: https://media.defcon.org/
- Hands-on AI hacking/red-teaming community at DEF CON. ✅ free — but recent years' AI Village talks are mixed into the main DEF CON per-year playlists rather than a dedicated one.

### OWASP GenAI Security Project (LLM Top 10 / Agentic AI Security Summits)
- Site: https://genai.owasp.org/ (events: https://genai.owasp.org/events/)
- YouTube: https://www.youtube.com/@GenAISecurityProject/videos
- Ongoing community talks and summit recordings on LLM/agentic app security. ✅ free.

### SANS AI Cybersecurity Summit
- Site: https://www.sans.org/cyber-security-summit/
- YouTube (SANS Institute channel): [2025 playlist](https://www.youtube.com/playlist?list=PLtgaAEEmVe6Bscw43BFiPMw9G9TdTKq2F) · [2026 playlist](https://www.youtube.com/playlist?list=PLtgaAEEmVe6AWHpSUtDRQnNzJ_2tuv1Hh)
- Annual summit on AI in cyber defense and securing AI systems. ✅ free — full talks.

### Black Hat (AI Summit & AI briefings)
- Site: https://www.blackhat.com/
- YouTube: https://www.youtube.com/@BlackHatOfficialYT/videos
- Flagship industry security conference; AI Summit since 2024 plus many AI/LLM briefings. ⚠️ partial — briefings hit YouTube free but with a ~6–12 month delay.

### OWASP Global AppSec
- Site: https://owasp.org/events/
- YouTube: https://www.youtube.com/@OWASPGLOBAL — e.g. [Global AppSec DC 2025](https://www.youtube.com/playlist?list=PLpr-xdpM8wG8MryXHpJ_KqCuJMplXB5-K) · [Global AppSec EU 2025](https://www.youtube.com/playlist?list=PLpr-xdpM8wG8uwnHl-vyoUiKXcUbMElDc)
- Appsec conference with a growing share of LLM/AI-security talks. ✅ free (posted months after each event).

### BSides Las Vegas (Ground Truth track)
- Site: https://bsideslv.org/
- YouTube: https://www.youtube.com/@BsidesLVorg/videos
- Community conference; the Ground Truth track is dedicated to ML/data science in security, plus LLM/MCP/agent content. ✅ free.

### IEEE SaTML — Secure and Trustworthy Machine Learning
- Site: https://satml.org/
- YouTube: [SaTML 2024](https://www.youtube.com/playlist?list=PLFG9vaKTeJq62wZPv6tPW23q-xYJxixMV) · [SaTML 2023](https://www.youtube.com/playlist?list=PLFG9vaKTeJq7MklvBGk31GeceuDB4Ofmp)
- Top peer-reviewed venue for adversarial ML, privacy, and trustworthy ML (academic). ✅ free for 2023/2024; newer years unconfirmed.

### USENIX Security Symposium
- Site: https://www.usenix.org/conference/usenixsecurity26
- YouTube: https://www.youtube.com/@UsenixOrg/videos
- Top academic security conference; substantial adversarial-ML and LLM-security track, fully open access. ✅ free.

### RSAC Conference
- Site: https://www.rsaconference.com/
- YouTube: https://www.youtube.com/@OneRSAC
- World's largest security conference with a big AI security track. ⚠️ partial — keynotes/highlights on YouTube; most breakouts in the registration-gated site library.

## Big vendor & platform events (AI adoption at scale)

### Microsoft Build
- Site: https://build.microsoft.com/
- YouTube: https://www.youtube.com/@MicrosoftDeveloper — [Build 2026 (224 videos)](https://www.youtube.com/playlist?list=PLlrxD0HtieHicIn65R7Oi_1nFXQr4SbtU) · [Build 2025 (274 videos)](https://www.youtube.com/playlist?list=PLlrxD0HtieHgFYS4DKbJ_xCYNE94ZLJjj)
- Hundreds of Copilot/agents/Azure AI breakout sessions. ✅ free — excellent for transcripts.

### Microsoft Ignite
- Site: https://ignite.microsoft.com/
- YouTube: https://www.youtube.com/@events_msft — [Ignite 2025 (502 videos)](https://www.youtube.com/playlist?list=PLQXpv_NQsPIDXiR9PcpggZ34mzko_-12C) · [Ignite 2024 (377 videos)](https://www.youtube.com/playlist?list=PLQXpv_NQsPID0sNvENCDMADnd1M5aOfv4)
- Microsoft's enterprise event, the counterpart to Build: Copilot, agents, Azure AI, Fabric and AI security, agentic AI throughout. ✅ free — the full session catalogue, not just keynotes. Registered per edition because the channel carries every Microsoft event, Build included, and conference attribution has to stay right.

### AWS re:Invent
- Site: https://aws.amazon.com/events/reinvent
- YouTube: https://www.youtube.com/@AWSEventsChannel — [re:Invent 2025 breakouts (585 videos)](https://www.youtube.com/playlist?list=PL2yQDdvlhXf9gdFFBcDPUHAJS7kkIkIet)
- Massive Bedrock/GenAI/agents breakout volume. ✅ free — best volume of the vendor giants.

### Google I/O
- Site: https://io.google/
- YouTube: https://www.youtube.com/@GoogleDevelopers — [I/O 2026 all sessions (68 videos)](https://www.youtube.com/playlist?list=PLOU2XLYxmsIJ6IFQouiKfM169TVOKx6Ej) · [I/O 2025 all sessions (82 videos)](https://www.youtube.com/playlist?list=PLOU2XLYxmsIL4mCDJICu2vLPNw-zdcGAt)
- Gemini/AI, Android, Web. ✅ free — complete session catalog.

### Google Cloud Next
- Site: https://cloud.withgoogle.com/next/
- YouTube: https://www.youtube.com/@googlecloudtech — [Next 2026 sessions (47 videos)](https://www.youtube.com/playlist?list=PLIivdWyY5sqLZY4WH03ns4Pt2B8VzE1fq)
- Enterprise cloud + AI. ⚠️ partial — keynotes + ~50 curated sessions on YouTube; full catalog in the free session library on the site.

### NVIDIA GTC
- Site: https://www.nvidia.com/gtc/
- YouTube: https://www.youtube.com/@NVIDIA/videos — [GTC 2026 (32 videos)](https://www.youtube.com/playlist?list=PLZHnYvH1qtOYKcOvqqLtmfpLntjXc4LqT) · [GTC 2025](https://www.youtube.com/playlist?list=PL5B692fm6--tCLg1NBPpsFGsIXOGbpVUa)
- Flagship AI/accelerated-computing conference. ⚠️ partial — keynote + ~30 curated talks on YouTube; full catalog (thousands of sessions) on [NVIDIA On-Demand](https://www.nvidia.com/en-us/on-demand/) behind free registration.

### Databricks Data + AI Summit
- Site: https://www.databricks.com/dataaisummit
- YouTube: https://www.youtube.com/@Databricks — [DAIS 2026 (35 videos)](https://www.youtube.com/playlist?list=PLTPXxbhUt-YV2itez3KGq_6FY1xgl8NKd); breakouts on https://www.youtube.com/@Databricks-Events — [2025 AI track](https://www.youtube.com/playlist?list=PLdcsMc3thIRw3qMnFcsaDAbi9zgwKIWQ1)
- Lakehouse + agentic AI platforms, 800+ sessions. ✅ free — keynotes + many breakouts across two channels; full catalog on the site behind free login.

### Snowflake Summit
- Site: https://www.snowflake.com/en/summit/
- YouTube: [@snowflakedevelopers Summit 2025 (75 videos)](https://www.youtube.com/playlist?list=PLavJpcg8cl1Eit8AmQHB3fmhMug2883Nf) · [@SnowflakeInc Summit 2026](https://www.youtube.com/playlist?list=PL4IM5KTx_T7gNwtams0rYZ-McLFy0dbIH)
- AI Data Cloud conference. ⚠️ partial — dev sessions on YouTube; most breakouts gated behind a registration form.

### Meta Connect (+ LlamaCon)
- Site: https://www.meta.com/connect/
- YouTube: https://www.youtube.com/@MetaDevelopers — [Connect 2025 (32 videos)](https://www.youtube.com/playlist?list=PLb0IAmt7-GS2cONiFVhtdKWEsyNkF6uUP) · [LlamaCon 2025](https://www.youtube.com/playlist?list=PLb0IAmt7-GS3JHFIJ0mQVsPJeDawImtf-)
- Meta's AR/VR/AI developer conference. ✅ free.

### Apple WWDC
- Site: https://developer.apple.com/wwdc
- YouTube: https://www.youtube.com/@AppleDeveloper — [WWDC25 sessions](https://www.youtube.com/playlist?list=PLjODKV8YBFHZKEn1wsUCL1n-q7tzysEBM)
- Apple Intelligence, on-device ML. ✅ free — and developer.apple.com hosts official written transcripts (ideal for extraction).

### Salesforce Dreamforce
- Site: https://www.salesforce.com/dreamforce/
- YouTube: https://www.youtube.com/@Salesforce — [Dreamforce 2025 keynotes](https://www.youtube.com/playlist?list=PLnobS_RgN7JZhBxLcql2XQ8U2iLxVfEdM)
- AI/Agentforce-heavy enterprise conference. ⚠️ partial — keynotes on YouTube; 500+ breakouts on Salesforce+ (free account required).

## Broader industry & business AI

### Web Summit
- Site: https://websummit.com
- YouTube: https://www.youtube.com/@WebSummit/videos
- Massive general-tech conference (Lisbon + Rio/Doha/Vancouver) with heavy AI programming. ✅ free — individual talks/panels posted.

### Slush
- Site: https://slush.org
- YouTube: https://www.youtube.com/@slush (per-stage yearly playlists)
- Startup/VC conference (Helsinki) with substantial AI content. ✅ free — all stage talks.

### SXSW (AI track)
- Site: https://www.sxsw.com
- YouTube: https://www.youtube.com/@sxsw — [2025 keynotes & featured sessions](https://www.youtube.com/playlist?list=PLXs_3rGeYdInegaGGlB6g6_DU3NZK0sgX)
- Annual Austin festival with a dedicated AI track. ⚠️ partial — keynotes/featured on YouTube; most AI-track breakouts audio-only on schedule.sxsw.com.

### TEDAI Vienna
- Site: https://tedai-vienna.ted.com (hub: https://conferences.ted.com/ted-ai)
- YouTube: https://www.youtube.com/@tedxvienna — [2025 playlist](https://www.youtube.com/playlist?list=PL8yrjrxWR4NPkB0xXzC8PaXXtZ_A61hqZ)
- TED's annual AI conference (SF edition discontinued after Oct 2025). ⚠️ partial — panels free on YouTube; mainstage TED talks only selectively on TED.com.

### Cerebral Valley AI Summit
- Site: https://www.cerebralvalley.com
- YouTube (Newcomer's channel): https://www.youtube.com/@newcomerpod — [summit playlist](https://www.youtube.com/playlist?list=PL0Yg1id5olJP-rgqHPQ32fOSgr_xDtJKV)
- Invite-only SF summit; on-stage interviews with AI founders/CEOs. ✅ free.

### Sequoia AI Ascent
- Site: https://www.sequoiacap.com/
- YouTube: [AI Ascent 2026](https://www.youtube.com/playlist?list=PLOhHNjZItNnOkkZThzULo1Ygg7JR6T3MG) · [AI Ascent 2025](https://www.youtube.com/playlist?list=PLOhHNjZItNnMEqGLRWkKjaMcdSJptkR08)
- Invite-only founder and researcher summit; short single-track talks from frontier-lab leaders (Karpathy, Hassabis, Brockman, Jim Fan). ✅ free — the talks are posted individually. Playlists only: the rest of the Sequoia channel is portfolio and podcast material.

### Y Combinator AI Startup School
- Site: https://events.ycombinator.com/ai-sus
- YouTube: https://www.youtube.com/@ycombinator — [AI Startup School](https://www.youtube.com/playlist?list=PLQ-uHSnFig5NPx4adxl97CZb8vU4numwi)
- YC's single-track AI school for student builders — Karpathy, Ng, Fei-Fei Li, Altman, Musk, Jumper. ✅ free — full talks. Only this playlist is registered; YC's channel is mostly clips, shorts and general Startup School.

## Academic research conferences (not on YouTube)

- **NeurIPS** — https://neurips.cc — free recordings via the virtual site (e.g. https://neurips.cc/virtual/2025, SlidesLive, free account, ~1 month post-event).
- **ICML** — https://icml.cc — free recordings at https://icml.cc/virtual/2025 (1,600+ talks via SlidesLive).
- **ICLR** — https://iclr.cc — free recordings at https://iclr.cc/virtual/2025.

Research-oriented rather than practitioner-focused; recordings are on SlidesLive, so a YouTube transcript pipeline won't work for these.

## Checked but weak sources (skip for transcript pipeline)

- **HumanX** — https://www.humanx.co — ❌ gated: full recordings in attendee app / behind lead-capture form; YouTube has promos only.
- **World Summit AI** — https://worldsummit.ai — ❌ full talks were posted through ~2023 ([2021 playlist](https://www.youtube.com/playlist?list=PL86bY2GqrAEFVhIAliVwnVhezTQkGRiVE)); 2024+ editions have only interviews/promos.
- **Ai4** — https://ai4.io/ — ❌ YouTube channel (https://www.youtube.com/@Ai4) stale since Aug 2024; newer sessions registration-gated.
- **ODSC** — https://odsc.com/ — ⚠️ curated free subset on https://www.youtube.com/@ODSCAI; complete catalog on the paid Ai+ platform.
- **MLconf** — https://mlconf.com/ — ❌ appears dormant (last event Mar 2025, newest videos from 2022).
- **AI Security Summit (Snyk)** — https://aisecuritysummit.com/ — ⚠️ videos linked individually from https://aisecuritysummit.com/videos; no single owned playlist found.
