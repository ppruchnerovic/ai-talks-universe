---
id: eXwX066a17k
title: "How to Ensure Code Quality and Consistency in Distributed Teams - Denny Biasiolli"
slug: how-to-ensure-code-quality-and-consistency-in-distributed
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: ["Denny Biasiolli"]
channel: "NDC Conferences"
duration_min: 17
published_at: 2026-01-21T12:19:48Z
video_id: eXwX066a17k
url: https://www.youtube.com/watch?v=eXwX066a17k
youtube_url: https://www.youtube.com/watch?v=eXwX066a17k
tags: ["AI", "Cloud", "Languages", "People", "Serverless", "Soft Skills", "Tools", "DevOps", "Lightning Talks", "NDC", "Conferences", "2025", "Live", "Fun", "Copenhagen", "Developers", "Festival", "Denmark", "Denny Biasiolli"]
topics: ["AI in the SDLC & engineering orgs"]
transcript: true
---

# How to Ensure Code Quality and Consistency in Distributed Teams - Denny Biasiolli

**Denny Biasiolli**

`NDC Conferences` · `NDC` · `2026` · `17 min`

`#AI` `#Cloud` `#Languages` `#People` `#Serverless` `#Soft Skills` `#Tools` `#DevOps` `#Lightning Talks` `#NDC` `#Conferences` `#2025` `#Live` `#Fun` `#Copenhagen` `#Developers` `#Festival` `#Denmark` `#Denny Biasiolli`

[Watch the recording](https://www.youtube.com/watch?v=eXwX066a17k) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Copenhagen in Copenhagen, Denmark. #ndccopenhagen #ndcconferences #developer #softwaredeveloper

Attend the next NDC conference near you:

/         @NDC

Follow our Social Media!

In today's globalized tech landscape, development teams are often distributed across multiple time zones and locations, making it essential to uphold code quality and consistency for successful collaboration. This talk explores effective strategies for ensuring code quality in distributed teams, covering best practices for establishing coding standards, implementing automated quality checks, and enhancing collaborative processes like code reviews and pair programming. Attendees will gain insights into tools and techniques that facilitate clear communication and continuous learning, ultimately fostering a culture of high-quality, maintainable code across geographically diverse teams.

- Why code quality and consistency matter
- Key challenges faced by distributed teams
- Establishing coding standards and guidelines
- Automating code quality checks with CI/CD pipelines
- Collaborative code reviews and pair programming
- Communication and collaboration tools for distributed teams
- Continuous learning and improvement practices
- Real-world examples and best practices

## Transcript

*2,079 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=eXwX066a17k&t=5s)** Hi everyone. Thank you for being here right before lunch. I'd be quick, I promise. Let me time this one. So, I want to exceed my my time. And as a first thing, I'd like you to keep in mind this image. Sorry, it's AI generated. I f for AI as well. I try not to but I'm not able to draw. So that's this image and this image is um like imagine working on a big project with talented developers from all over the world and uh each one contributing to your codebase. Uh something super exciting. uh it can be like working on a open source project or uh if you like me

**[0:55](https://www.youtube.com/watch?v=eXwX066a17k&t=55s)** uh are working for a remote company then it's the same thing. So big project developer from all over the world and it's great but what if every developer has different coding styles and own preferences and so on. And again uh different time zones make real time communication really difficult. So you can just call them whenever you like and if there's no standardized review process then this can became chaos. That's the reason why code quality and consistency matter because of course the

**[1:45](https://www.youtube.com/watch?v=eXwX066a17k&t=105s)** first reason is uh a clean code is easier to extend and debug and helps team members understand each other because they are talking basically the same language coding language and that can lead to faster issue resolution. It's easier to add new teams, new team members and uh you can also add new feature uh faster and hopefully uh this leads to fewer bugs and a reduced technical depth hopefully. So now I challenge you to tell me why does this code return eight instead of 12? Well, back in the days, I am really old

**[2:33](https://www.youtube.com/watch?v=eXwX066a17k&t=153s)** in the technology board. I feel old. Um, the space wasn't was a problem because we were programming on floppy disc, the icon of saving things. And well, space was a problem. So a real rockstar developer was able to write super short code uh doing great things and that was a rockstar. Now space is not a problem anymore. So you can write this function uh this way. Sorry it's Python. I noticed there are a lot of net developers but I hope it you can understand a little bit. So the first one is a function that doubles a

**[3:21](https://www.youtube.com/watch?v=eXwX066a17k&t=201s)** number and then we have a list of numbers and we iterate through those numbers extracting just even numbers and if you are reading the code the problem is here. So we are checking if the number is odd instead of even. So this might be the problem. This is the problem. But of course you may notice that just giving proper names to functions and uh creating uh readable code is better and it's faster to understand what is doing. So uh the reason is that in distributed teams uh a synchronous work makes communication more challenging. So you can't ask the developer who wrote the

**[4:11](https://www.youtube.com/watch?v=eXwX066a17k&t=251s)** first piece of code, this one, oh what were you thinking here? What is this code doing? And you can just read the code and that's it. Because inconsistent code can lead to misunderstanding or like this example uh longer debugging uh times. Other than this, on boarding new team members can be difficult because you have to explain everything into the details of what the code is doing. So code quality becomes the language developer uses to communicate and you should instruct all developers, new one and old one especially to follow the same coding standards and guidelines. But well how

**[5:02](https://www.youtube.com/watch?v=eXwX066a17k&t=302s)** because each developer has its own coding standard and again time zones uh differences affect real-time communication and there is fragmentation of tools environments and developer preferences not working. Okay using this one. So the first one of the first developer war was this one. Uh they were debating between using tabs or using spaces and again you may lose a lot of time based just on developer preferences like this. So, what if a developer has an auto uh correction

**[5:51](https://www.youtube.com/watch?v=eXwX066a17k&t=351s)** setting in its own uh um code editor that changes spaces to tabs or vice versa, then when they open up a request, everything seems to be changed even if they just change days to these to fix our previous problem. Well, that's house. Same for camel case or snake case or whatever case you prefer. You can adapt your code because you like that way. But well, again, it makes your p request unreadable or difficult to read. And as I said, you can use auto formatting tools. uh they can help with consistency but if they are um they have

**[6:42](https://www.youtube.com/watch?v=eXwX066a17k&t=402s)** different settings uh this can lead to other issues. For example, in Python you may have this error because there are tabs and spaces mixed up in the code and everything is a is a mess. So you should set a clear set of coding standards and guidelines that everyone follows because this can help ensure consistency uh among team members. How can you do this? Well, you can define and force clear style guide. Then you should centralize your documentation of best practices in your projects. And uh you need to remember to update these guidelines regularly with the whole team feedback.

**[7:31](https://www.youtube.com/watch?v=eXwX066a17k&t=451s)** First one you can pick and stick to a style guide. For example, in Python um they have pepate or Airbnb style guide for JavaScript. You may like it or not. There are other style guides you may follow. uh you can decide the one to follow with the team and stick to that and then uh you can use llinters and formatters to automate compliance. So you can use a pre-commit or pre- push hook in your GitHub project git project to check for common errors or differences before committing or pushing your code to to git to GitHub. For example, in Python um they have black

**[8:21](https://www.youtube.com/watch?v=eXwX066a17k&t=501s)** sort and flake or slint and prettier for JavaScript and there are lots of other llinters and formatterers for all other languages. Then you should create a centralized knowledge base for example using GitHub pages, Confluence, notion wherever you like in order to store your um uh coding guidelines for the project, your best practice for the team, for the company and uh also if you like team expectation, share it for everyone there to read. You should also uh if you are using github uh document how to make changes to set up the project and perform

**[9:10](https://www.youtube.com/watch?v=eXwX066a17k&t=550s)** requests uh for that specific project in for example in the contributing markdown file because that allow uh newcomers to the project to be up to speed faster just reading documentation. Then remember to keep your documentation and standards up to date, reviewing them periodically. How to how can you automate these code quality checks? Uh well, as Mishi said in her talks, you can use and implement CI/CD pipelines to automate test linting and whatever. Again, you can also implement checks uh

**[10:00](https://www.youtube.com/watch?v=eXwX066a17k&t=600s)** in prerequest and then uh you should use automate testing tools. Everyone hates that but it makes your code safer trust me. And uh if you like you can leverage bots for code review automation. Uh we are using some sort of GitHub copilot uh auto out reviewer that like Mish said creates uh an automatic description of the request and perform basic checks or of your code in GitHub actions you can use that so wherever you push on your main branch don't do that please use per request or you open up a request on the main branch that everything runs and checks your

**[10:51](https://www.youtube.com/watch?v=eXwX066a17k&t=651s)** code automatically. Then again uh think about unit testing, integration testing and end to end test and maybe make them mandatory before deploying code to production. So you can use uh GitHub branch protection rules uh in order to require status check to pass before merging otherwise merging is blocked and uh also lock branch so people are not accidentally pushing to the main branch. Again you can use both to bots to flag issues before human review to speed up things. Uh I know there's review dog we tried that but now there is GitHub auto

**[11:43](https://www.youtube.com/watch?v=eXwX066a17k&t=703s)** reviewer uh compilot or AI tools again if you feel confident about using them. So automating code code reviews can help catch basing issues uh before human intervention. Then you can collaborate in code reviews. So the programmer who opened the code review and the person who is reviewing the code uh should establish um a clear code review process and checklist of things to do, things to check and uh if you're able to because in a remote world this is difficult. You can also leverage per programming for real-time collaboration and maybe

**[12:30](https://www.youtube.com/watch?v=eXwX066a17k&t=750s)** explanation about the new things you you did in the per request. Then make these code reviews part of uh the development process in order to enforce security, performance and maintenability. You should focus on that as well. And if you can assign a reviewer who has context but was not involved in writing the original code. So this provide fresh eyes to the issue and so you are able to better explain your prerequest to a person that was not involved because you are forced to explain better your your prerequest text basically. And uh Wednesday I heard a talk from Tess

**[13:20](https://www.youtube.com/watch?v=eXwX066a17k&t=800s)** Ferandes Norlander. I hope to it correctly. Uh you should VIP request like you have to review them. You you like to review them because they will be of course better. Last but not least, um example of tools. For example, don't use uh hundreds of llinters and formatters. just use the ones you you like and you you use and you feel confident about. For example, there's editor config. It integrates with almost every um code editor you may use and you can use uh a generic configuration for the chart set end of line style final line at the end of the file or trailing whites space.

**[14:11](https://www.youtube.com/watch?v=eXwX066a17k&t=851s)** And also you can use um a specific style for different file um different yeah different files sorry and uh for example indent size and indent styles and this will end your developer war as long as you share this file with within the project with other developers so they can stick to that for that specific project then sorry I don't have an example forn net but there should be something uh like some code formatter for net as well but for python you can use black and use it on your source files and that will check and maybe out format your code

**[14:57](https://www.youtube.com/watch?v=eXwX066a17k&t=897s)** I sort in order to sort imports uh before generic imports then your local imports or for JavaScript you can use prettier to format files check and or format files. Slint again for JavaScript. You can use uh go format in go or govette for potential issues for you. You can use cargo format or cargo clippy to achieve the same things. And last word about environments uh having different people all pushing to your branches. Maybe you want to have different environments. So for example uh you can use well for feature branches uh you can use your local host to check

**[15:47](https://www.youtube.com/watch?v=eXwX066a17k&t=947s)** it everything is okay. Then when you push your prest, you can push to a develop branch and everything will be deployed on uh onto a staging area where they can test things or even use um testing a testing environment specific testing environment when you want to merge to specific branches. demo when you want to merge for example to the main branch without deploying to customers. So you have a demo like style with preview about features without giving them to clients and then again production. So uh concluding set clear coding standards,

**[16:36](https://www.youtube.com/watch?v=eXwX066a17k&t=996s)** use CI/CD pipelines uh wherever you like and testing to catch issues early in your coding process and leverage code reviews and collaborative tools to share knowledge and maintain consistency. Foster communication and continuous improvement uh within your distributed teams. And again, another thing, continuous learning about best practices and improvements are essential for long-term success. So, communicate clearly, automate what you can, don't feed the spaghetti monster with ugly code, and remember, it always works on your machine until it doesn't. Thank you very
