---
id: Blcrurhsy5A
title: "Simplify The Entire Data Development Lifecycle with Snowflake CoCo"
slug: simplify-the-entire-data-development-lifecycle-with
conference: snowflake-summit
conference_name: "Snowflake Summit"
category: "Vendor & platform"
edition: "Summit 2026"
year: 2026
speakers: []
channel: "Snowflake Inc."
duration_min: 6
published_at: 2026-06-09T15:30:29Z
video_id: Blcrurhsy5A
url: https://www.youtube.com/watch?v=Blcrurhsy5A
youtube_url: https://www.youtube.com/watch?v=Blcrurhsy5A
tags: ["Snowflake", "Snowflake data warehouse", "Snowflake computing", "Snowflake company", "Snowflake database", "Snowflake cloud", "Data warehouse", "Business software", "Data warehousing", "Cloud storage", "cloud computing", "Data Science", "Data Engineering", "The Data Cloud", "big data", "artificial intelligence", "data scientist", "predictive analytics", "business intelligence", "data economy", "Data driven economy", "Data cloud", "data lake", "Data Warehouse"]
transcript: true
---

# Simplify The Entire Data Development Lifecycle with Snowflake CoCo

**Speaker not identified**

`Snowflake Summit` · `Summit 2026` · `2026` · `6 min`

`#Snowflake` `#Snowflake data warehouse` `#Snowflake computing` `#Snowflake company` `#Snowflake database` `#Snowflake cloud` `#Data warehouse` `#Business software` `#Data warehousing` `#Cloud storage` `#cloud computing` `#Data Science` `#Data Engineering` `#The Data Cloud` `#big data` `#artificial intelligence` `#data scientist` `#predictive analytics` `#business intelligence` `#data economy` `#Data driven economy` `#Data cloud` `#data lake` `#Data Warehouse`

[Watch the recording](https://www.youtube.com/watch?v=Blcrurhsy5A) · [Conference site](https://www.snowflake.com/en/summit/)

## Description

Accelerate your data development lifecycle from days to minutes with Snowflake CoCo. Learn how to effortlessly connect data sources, fix broken pipelines, build real-time apps, and surface instant business insights with "Snap-and-Ask"—all using natural language prompting.

❄Join our YouTube community❄ https://bit.ly/3lzfeeB

➡️ Website: https://www.snowflake.com
➡️ Careers: http://careers.snowflake.com
➡️ Podcast page: https://www.snowflake.com/thedatacloudpodcast/
➡️ Twitter: https://twitter.com/Snowflake
➡️ Instagram: https://www.instagram.com/_snowflake_inc
➡️ Facebook: https://www.facebook.com/snowflakedb
➡️ LinkedIn: https://bit.ly/2QUexl4
➡️ Sign up for our weekly live demo program and have your questions answered by a Snowflake expert at https://bit.ly/2TdVCmJ

Listen on:
🔈 Apple Podcasts: https://apple.co/3cCdrCU
🔈 Spotify: https://spoti.fi/39vCNjH
🔈 Simplecast: https://bit.ly/3rFCrgA

## Transcript

*843 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Blcrurhsy5A&t=0s)** Today, our demo will focus on a fictional business, Snow Music, which manages live tour operations and a high-traffic fan application. Snow Music is preparing for a massive global tour and wants to ensure that their VIP fans, the biggest drivers of revenue, have an absolute epic experience. To do that, we need a VIP fan command center, a Streamlit application that merges Salesforce data with live fan activity. And we need to ship it in days, not weeks. Let's jump into Cocoa to get started. So, I'm starting here in Snowflake Cocoa Desktop, which is purpose-built for heavier development work, writing

**[0:48](https://www.youtube.com/watch?v=Blcrurhsy5A&t=48s)** complex logic, connecting data, and overall data management. Here, I'll prompt Cocoa using natural language to build our VIP fan command center. Here's my prompt. Build a Streamlit dashboard to monitor our Snow Music tour data pipeline with live streaming metrics and engagement analytics. And then deploy to Snowflake. And just like that, Cocoa gets to work, immediately begins building code based on a deeply context-aware understanding of our environment. Now, for the purpose of this demo and our time constraints, I've already built and deployed this app using Cocoa. I'm going to navigate straight over to the running Streamlit app in Snowsight. And show you how we can use Cocoa to

**[1:37](https://www.youtube.com/watch?v=Blcrurhsy5A&t=97s)** diagnose and fix a broken pipeline live. Here's a live fan command center application running in Snowsight. Everything looks incredible, but looks like we've hit a couple roadblocks. The app is highlighting a couple of broken pipeline steps. In the old world, diagnosing a stale data pipeline across live apps, CRMs, and other data sources would take hours of troubleshooting across multiple engineering teams. But, Cocoa is here to help, meeting builders where they are to solve real complex challenges. All right, so here we go. My fan app events data pipeline tasks failed. Can you diagnose the root cause, fix it, and verify the full pipeline run successfully? We use Cocoa Desktop to build, and now I can open Cocoa right here in Snow sight

**[2:26](https://www.youtube.com/watch?v=Blcrurhsy5A&t=146s)** to investigate the broken pipeline in context of our live app. While Cocoa is thinking, scanning our task history, checking failed runs, and tracing the dependency chain, here's what's happening under the hood. In the background, Cocoa is analyzing an incredibly elegant modern data stack. With just that single prompt we used earlier, it successfully managed connections to Salesforce via zero copy integration alongside streaming data from the VIP fan app. We can see that the live streaming data refreshing in our app here in every few seconds. The ingestion of that live fan data is coming in via Snowflake data stream. We simply activate it it by connecting our existing Kafka producer to a data stream topic with zero code changes. And the

**[3:17](https://www.youtube.com/watch?v=Blcrurhsy5A&t=197s)** live data materializes into a native Snowflake managed Iceberg table almost immediately. Because the fan app data lives in a managed Iceberg table, it is cleanly governed through Horizon catalog. Horizon automatically registers this Iceberg table in the universal catalog, making it instantly accessible to any engine. One data copy, fully governed, zero duplication. This is exactly why Cocoa is a category-defining tool. It is the industry's first truly data-native AI coding agent, meaning it operates with a deep intrinsic awareness of Snowflake's data compute governance and operational semantics. And look at that, Coco has already generated the precise

**[4:05](https://www.youtube.com/watch?v=Blcrurhsy5A&t=245s)** code fix and verified the downstream dependencies. Now you can see that the pipeline status cards are green. Coco turns what used to be an exhausting multi-team engineering escalation into a simple intent-driven interaction. Safely accelerating our time to production with high accuracy and trust. Let me show you Snap and Ask. Now that the data is flowing perfectly, I'm noticing a massive drop in fan engagement in San Francisco. So instead of jumping into a separate worksheet to write complex SQL, I can use Snap and Ask directly inside our app. By making the selection on the chart and asking a direct question of the data using Snap and Ask, Coco instantly understands the exact data segment I'm referencing to surface business insights. Now this is

**[4:53](https://www.youtube.com/watch?v=Blcrurhsy5A&t=293s)** only possible because our live fan app activity joined with Salesforce records in real time, proving that Coco doesn't just confirm data movement, it deeply understands business context. Right here, Coco instantly identifies app activity and live fan engagement plummeting. It highlights this specific localized dip, giving us a real-time warning so our local team can step in and check on the venue's fan experience immediately. What you've just seen is the power of the industry's first truly data-native AI coding agent. Coco redefines how data and developer teams work, seamlessly interacting across the entire modern data stack. This demo showed how we can turn application development, complex

**[5:41](https://www.youtube.com/watch?v=Blcrurhsy5A&t=341s)** data engineering, and advanced analytics into a simple natural language interaction, and how Coco dramatically compresses the distance between a creative business idea and secure trusted implementation. With that, Sofie Coco empowers builders to optimize workflows and speed time to value faster than ever before.
