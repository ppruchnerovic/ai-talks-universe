---
id: _dTUUKlvKx8
title: "Build AI-first business apps that turn dashboards into actions | ODSP911"
slug: build-ai-first-business-apps-that-turn-dashboards-into
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Paul Usher"]
channel: "Microsoft Developer"
duration_min: 14
published_at: 2026-06-03T11:06:49Z
video_id: _dTUUKlvKx8
url: https://www.youtube.com/watch?v=_dTUUKlvKx8
youtube_url: https://www.youtube.com/watch?v=_dTUUKlvKx8
tags: ["AI", "Build AI-first business apps that turn dashboards into actions | ODSP911", "DevTools", "Developer", "Developer Frameworks", "ODSP911", "ODSP911_v1", "Paul Usher", "Software Development Company", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Build AI-first business apps that turn dashboards into actions | ODSP911

**Paul Usher**

`Microsoft Build` · `Build 2026` · `2026` · `14 min`

`#AI` `#Build AI-first business apps that turn dashboards into actions | ODSP911` `#DevTools` `#Developer` `#Developer Frameworks` `#ODSP911` `#ODSP911_v1` `#Paul Usher` `#Software Development Company` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=_dTUUKlvKx8) · [Conference site](https://build.microsoft.com/)

## Description

Business apps are shifting from dashboards and filters to AI-driven experiences. In this session, we show how users can ask questions, get insights, and take action instantly. Using DevExpress components, we demonstrate how structured UI brings AI responses to life, turning data into clear, actionable outcomes.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Paul Usher

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

ODSP911 | English (US) | Developer tools & frameworks

Pre-recorded | (200) Intermediate

#MSBuild

Chapters:
0:00 - Session focus: Integrating AI for natural user experiences in Blazor apps
00:03:31 - Exporting grid data to Excel
00:03:47 - Difference between chat answer and application assistant
00:05:03 - Registering tool methods such as filtering and exporting
00:06:38 - Chat client integration with Azure OpenAI configuration
00:07:58 - Using AI to translate report content to English within the report viewer
00:10:59 - Rendering AI findings with formatting for the side panel
00:11:11 - Explanation: Report logic independent from AI, focused on clause risk
00:12:48 - Summary of AI integration across demo pages and synergy of Azure AI, DevExpress, and Visual Studio

## Transcript

*1,922 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=0s)** PAUL USHER: Welcome to this Microsoft build 2026 session. I'm Paul Usher from DevExpress. Today we're looking at how AI can create a more natural user experience inside a modern Blazor application. This is not about generating code and it's not about dropping a chat bot beside an existing app and calling it done. This is about connecting AI to the controls, to the data, and to the workflows users already rely on. The demo app is built in Visual Studio using.NET. DevExpress Blazor controls, DevExpress reporting, and Azure Open AI through iChat client. We'll look at three examples. First how AI drives DevExpress grid using tool calling. Second AI is built in to the DevExpress report viewer

**[0:49](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=49s)** for translation. And third Azure Open AI to review a contract and DevExpress report to visualize the risky clauses. We have a simple command center here featuring some KPI cards, a DX chart control, DX grid, and on the right-hand side DX AI chat. I've got some prebaked recording prompts. So we're starting on the main home razor page. The cell's data is coming from a CSV loaded through a data service and a simple method call to get orders. It's also using a get summary for the KPI cards and a get region metrics for the chart. The grid itself is bound to around 10,000 rows of USA sales data. Now traditionally users will work with data by filtering,

**[1:39](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=99s)** sorting, grouping, paging, and exporting. And that still matters and the DevExpress grid is very good at that. Let's filter to just Texas. And then maybe group by region. Expand. And sort by customer name. We could also create some buttons that will build that functionality in. They only cover the scenarios we thought ahead of time. So the question is can we give the user a more natural way to work with this data. Well, on the right-hand side I've got a DX AI chat control. And what (inaudible) here is the fact

**[2:26](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=146s)** that the user can ask questions in a more natural language. For example, how did we perform this week? The prompt is going to be handled by the cell's analysis tool. It can call methods such as summarize performance which uses a build executive summary method and produces a concise business summary. What if we want the chat to actually interact with the grid? Let's ask, "Group the orders by customer." And we can see that the grid has now responded and is grouping the data by customer. What if I was to actually say instead of customer group by profit? And we can see that the code behind has been set up to allow specific functionality. The user doesn't just get told no.

**[3:15](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=195s)** It's provided an explanation as to what's going on. Maybe now I ask it to highlight the payment risk accounts. And again that grid information is updated. In the background it's calling a filter risk account method. Now that I've got that information I want to export it to Excel. So just ask export. And we can see now that a download's been created with an Excel SX file. This is the difference between a chat answer and an application assistant. The AI is not telling the user how to export. It's triggering the exports for a controlled DevExpress API. Think in terms of the AI handles the intent. DevExpress handles the interaction.

**[4:05](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=245s)** Jumping in to Visual Studio we'll take a peek inside home.razor. First thing we want to do is find the chat control. This is the DX AI chat control for the page. The important setting is the chat client service key equals DX tools. This is telling the chat control to use the tool enabled AI client that we register in program.CS. I've said include function calling for to true so the demo can show the calls the tool actually makes. Typically in production you'd set it to false. Now if we scroll down to the on after render we can see the creation of a new AI tools context builder. And this context registers two live targets,

**[4:55](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=295s)** the actual DX grid instance and the cell's data service. Then it registers the methods that the AI is allowed to call. Filter by region. Filter by state. Filter risk accounts. Group by. Clear view. Export. Summarize. And list top customers. Think of this as the toolbox for the current screen. The AI does not get the whole application, simply the approved capabilities that we register here. And we can see at the bottom of the method the context is added to the AI tools container which makes it available to the DevExpress tool calling pipeline. Switching across to the cell's grid AI tools we'll scroll down to the filter by region method. So this is just one of the tools the model can call

**[5:45](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=345s)** and it's just normal static C Sharp method with meta data. So the AI integration tool gives the model the function name. And then we've got the description which tells the model when to use the function and what the parameters mean. Now these descriptions matter because they guide the tool selection. So this is the DevExpress specific part. The model does not provide the grid. DevExpress injects the live DX grid instance from the tool's context at run time. The body then calls the normal DevExpress grid API. It's the same sort of code that I could write from a button click. And the rest of the tools follow exactly the same behavior. Not every tool changes the UI.

**[6:32](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=392s)** Some of them provide an analysis. Jumping in to program CS we can see where the actual chat client has been added. We can see the configuration is picking up from our.NET user secrets the Azure Open AI end point, the Azure Open AI key, and the deployment name. This next element is an important one for the grid demo. We can see that we're creating a key chat client called DX tools. And then we use DX tools as the DevExpress tool definitions. Use function invocation executes the tool calls and feeds the results back to the model. And that's what's being used by the DX AI chat back on the home razor page.

**[7:22](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=442s)** One of the key take aways here is that this is the main loop. The user prompt Azure Open AI DevExpress tool public control API real UI action. Let's jump back and look at some more built in AI functionality. This time we're going to jump in to the report viewer. And what we can see here is a generative report using the DevExpress reporting tools and it's actually a quarterly memo report. The problem is it's been written in French. Using the built in AI tooling I can select that I want to translate the entire document back to English. I'll press the translate button. Now note that there's no custom chat (inaudible) on this page.

**[8:10](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=490s)** The DevExpress report viewer owns the AI experience. Now the report itself is a standard extra report. It sets up for French memo section and builds a simple report header, detail banned footer and page footer. And if we jump back in to Visual Studio and scroll down to where the report engine is initialized so the AI behavior's enabled in program CS through the ad Blazor reporting AI integration methods and ad translation. We can see that the configured languages include English, French Spanish, German Japanese. The enable translation method adds the translation and enable inline translation allows the translated content to appear inside the rendered report experience. In this pattern the control owns the AI experience.

**[9:05](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=545s)** So let's jump back to the app and take a look at where we can compose our own workflow. This time we're going to go to contract review. We've got a master service agreement rendered inside the DevExpress report viewer. So the goal here is not just to ask AI for a tech summary. We want Azure Open AI to identify risky clauses and then we want the document itself to show those risky clauses. I've wired up a button to ask the chat control to review for issues. So the AI's now reviewing the contract. It's going to identify risky or one sided clauses. And the report renders with visual warnings. We can see the side panel findings.

**[9:55](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=595s)** We can see the highlighted clauses, a warning tag, and the red border on the left as a warning. The answers are on the right-hand side, but the experience is inside the document. Back in Visual Studio we'll scroll down and take a look at the review async method. Inside review async we know that there is no DX AI chat control. The page injects the iChat client directly. The system prompt asks the model to act as a commercial contract attorney and the user prompt sends the full contract text using contractreport.getfulltext. Chat client get respond async sends the request to the configured AI client. And then the response is stored for the findings panel.

**[10:46](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=646s)** The parse risky clause numbers extracts references like clause four or clause nine and then the page creates a new contract report passing in the risky clause numbers. Finally render findings formats the AI response for the side panel by preserving the line breaks and bold headings. So the key take away here is that the report doesn't know anything about AI. It only knows whether a clause is risky. So a contract report contains the 12 contract clauses and clauses source. Get full text joins those clauses in to a plain text that's sent to the model. The constructor receives the risky clause numbers and projects each clause in to the report data source with a is risky set to true or false. So the report doesn't know anything about AI. It only knows whether each clause is risky.

**[11:37](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=697s)** And if the clause is risky it's going to change the band color and add the warning tag. AI creates the state. DevExpress presents the state. If we take a quick look at the program structure we've got our component pages, AI folder, report services, and then the data. And what I like about this structure is that the AI layer doesn't swallow the application. The page still uses the DevExpress controls for the user experience. The services still own the business data. And the AI tools expose selected capabilities. The report renders through the DevExpress reporting APIs. And the DevExpress controls help make the AI useful because they give the AI somewhere structured to act. A grid can filter, group, sort, and export.

**[12:28](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=748s)** A report viewer can translate and render document content. And a report can visualize AI derived state through conditional formatting. So the AI is powerful, but the control gives it shape. Across three pages we've shown practical ways to bring AI in to a DevExpress application. On the demo page AI drives the DevExpress grid through tool calling. On the report viewer page AI is built directly in to the control. And on the contract review page AI becomes part of a custom workflow and DevExpress reports visualize the result. The point is not add a chat bot beside every app. It's to let users express intent and then use controls such as the DevExpress tools to turn that intent in to action.

**[13:22](https://www.youtube.com/watch?v=_dTUUKlvKx8&t=802s)** Azure Open AI provides the intelligence. DevExpress provides the application service. And Visual Studio brings it all together.
