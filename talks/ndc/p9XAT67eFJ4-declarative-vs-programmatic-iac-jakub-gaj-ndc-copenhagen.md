---
id: p9XAT67eFJ4
title: "Declarative vs programmatic IaC - Jakub Gaj - NDC Copenhagen 2025"
slug: declarative-vs-programmatic-iac-jakub-gaj-ndc-copenhagen
conference: ndc
conference_name: "NDC Conferences"
category: "General software conferences"
edition: "NDC"
year: 2026
speakers: ["Jakub Gaj"]
channel: "NDC Conferences"
duration_min: 16
published_at: 2026-01-21T12:13:18Z
video_id: p9XAT67eFJ4
url: https://www.youtube.com/watch?v=p9XAT67eFJ4
youtube_url: https://www.youtube.com/watch?v=p9XAT67eFJ4
tags: ["Jakub Gaj", "AI", "Cloud", "Languages", "People", "Serverless", "Soft Skills", "Tools", "DevOps", "Lightning Talks", "NDC", "Conferences", "2025", "Live", "Fun", "Copenhagen", "Developers", "Festival", "Denmark"]
topics: []
transcript: true
---

# Declarative vs programmatic IaC - Jakub Gaj - NDC Copenhagen 2025

**Jakub Gaj**

`NDC Conferences` · `NDC` · `2026` · `16 min`

`#Jakub Gaj` `#AI` `#Cloud` `#Languages` `#People` `#Serverless` `#Soft Skills` `#Tools` `#DevOps` `#Lightning Talks` `#NDC` `#Conferences` `#2025` `#Live` `#Fun` `#Copenhagen` `#Developers` `#Festival` `#Denmark`

[Watch the recording](https://www.youtube.com/watch?v=p9XAT67eFJ4) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Copenhagen in Copenhagen, Denmark. #ndccopenhagen #ndcconferences #developer #softwaredeveloper

Attend the next NDC conference near you:

/         @NDC

Follow our Social Media!

What is the difference between declarative and programmatic approach for developing your Infrastructure as Code? Why it matters and when you should use each?

Best practices for writing good Infrastructure as Code when using AWS CloudFormation, AWS SAM, AWS CDK, Pulumi, Terraform, SST, Serverless Framework, etc.

Quick demo to showcase the power of AWS CDK constructs, and how to deploy cloud infra from a frontend framework (SST + Astro).

## Transcript

*2,295 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=5s)** Hello everyone. It does work. Um, hi, my name is Akub guy. I'm a cloud solution architect at the Dansk Bank. I'm um I'm working with mostly with AWS cloud supporting different uh teams to move to AWS and build cloudnative solutions. And today I wanted to talk about different approaches to infrastructure as code um which u obviously becomes like a standard nowadays. But um what is infrastructure as code? Um it is basically a practice of provisioning and managing infrastructure from code as opposed to any kind of interactive tools or clickups. Um and I want to talk talk about differences between two approaches or multiple approaches and uh different

**[0:55](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=55s)** frameworks you can use for them. Um and some best practices basically. Um but coming back to you know like iron age of uh bare metal service in data centers we still have them uh we just don't see them much to be honest at the bank we still use uh mainframes and they're not going away really. Um but the real revolution happened with the virtualization kind of uh stage where where we actually visualized uh hypervisors and uh computing storage networking part and we could define that as a logical devices using as a as a logical resources using um some sort of uh CLI commands or API calls and we could actually write it in some sort of scripts. Um then of course the cloud

**[1:45](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=105s)** computing came over uh which is like a self-service um um layer on top of the virtualization. So as as everything has been logically uh defined as code uh basically with cloud computing uh this is what happening um for us if we click on a console um um basically this uh uh the resources get provisioned for us and then we have like entering AI era when where where we will be managing infrastructure using AI services uh which will help us uh identify some issues um and how to heal uh the infra infrastructure for us. Um some of the milestones of everything or anything as code u so when I started I don't know 25 years ago I was still

**[2:33](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=153s)** still writing a lot of scripts to automate certain OS builds and and virtual machine builds. Um so we use different sort of uh scripting to automate those things. Then configuration as code came in. So different frameworks which uh basically helped us apply certain configuration repeatably um in across hundreds of servers and virtual machines uh like puppet chef anible and uh of course with cloud it came all sort of frameworks like cloud formation terraform um crossplatform like terraform of course uh we which we we started to declare certain resources we want to have deployed and and uh we were just deploying them and we still use them. Right?

**[3:21](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=201s)** Then the function servers several functions and containers came in and we kind of kind of had to bundle them somehow and uh different extensions came out or different frameworks which would help us to uh to deploy to to the target platform our functions and containers. And then we kind of have an era of cloud development kits where you define your infrastructure from well-known languages like uh Python, TypeScript for example. Um so CDK, Terraform, Palumi, SSD those with the the most popular with some spin-offs um for Terraform um and for um um and for Kubernetes for example. And then we have a AI part assistant

**[4:09](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=249s)** which obviously we we we use to produce any sort of code. So any kind of uh declarative code which was um very lengthy to to define we can then speed up now with uh with AI assisted uh AI assistance and of course we can produce any any sort of u code for the cloud development kits. some of the aspects of u declarative approach. It is a domain specific language. So we had to kind of learn those languages. Uh they're not really difficult. They just uh YAML or JSON files. Um but they had some limited building logic capabilities I would say. So we had to um struggle a bit u with those. Uh we don't need like a massive logic in infrastructure scout. is just

**[4:59](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=299s)** more like defining resources and deploying them. Um but those those those frameworks those templates were very u readable I would say. So there's one to one relation between definition of the resource and um resource deployed in a cloud. Um and of course if you have a lot of those resources then it be it can become u really lengthy for more complex infrastructures. But from my experience those frameworks uh are very powerful for any kind of u focus on the infl layer. So if you're building any sort of platform which is used by multiple tenants like a shared platform then then um it's much safer to use them. Um so they really really good in like

**[5:46](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=346s)** low-level resource definition. Um mostly because if you if you need to change anything in your infrastructure and there are multiple tenants using your infrastructure um basically it's just much much safer to to to make modifications in your code because any changes uh to your infrastructure might be you know it might have a cascading effect on all the tenants which are using this uh for example like a shared networking um and so on. Some of the most popular frameworks are obviously cloud formation and spin-offs and uh extensions to it and as well as Terraform and forks like uh open tofu and and deployment manager and bicep for for Azure and Google clouds.

**[6:35](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=395s)** some of the aspects of the programmatic uh approach they use standard languages like Python uh TypeScript they have more advanced logic which you can use uh you don't necessarily need it but if you need to um define hundreds of resources you can of course use some loops which will speed up your um definition of resources and they also the the big p the biggest power is in my opinion um custom abstractions like patterns and and constructs which you can define for your organ organization and shared inside the organization across different teams and uh developers and of course they integrate with all sort of development ids uh test suits so you can basically write any sort of uh automated tests to to make sure your infrastructure is immutable

**[7:24](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=444s)** and if you're focusing on application layer and your infrastructure is just a side effect or like you know one of the layers which you have to build but you don't really want to focus on this uh but you want to focus on business logic then those uh those frameworks are super powerful and they they also very they very easy to start with for developers because they already know some of the languages um which which the framework is supporting. So they much better for this like high level up abentric deployment uh and uh development of your applications and some of the most popular are CDK is which is one of my favorites uh personally um Pulumi and SST which is more focused on the um

**[8:13](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=493s)** frontend frameworks I would say and you have some spin-offs spin-offs of as well like CDK for Terraform and CDK for Kubernetes. So you can use a um cloud development kit to generate terraform templates or kubernetes manifests. Um one of the one of the important aspects of the any kind of framework is a state management and different frameworks deal with this in a different way. State is a metadata or about deployments and uh what kind of resources have been deployed and who deployed when a history and so on and also a locking mechanism to make sure that only one deployment is changing the infrastructure. Um so so there's a locking mechanism and different services use different options. Um obviously the the cloud vendor

**[9:03](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=543s)** provided uh frameworks will be using some sort of cloud services like cloud for uses cloud for stacks to store those kind of data. Then you have uh kind of like a crossplatform engines like Palumi or or Terapform which will use uh some sort of remote stage uh remote storage and locking. So you have to define those and of course they provide some sort of enterprisegrade u tooling um paid option to to handle this for you together with CI/CD pipelines uh and all sort of automation around uh deploying infrastruct and I have um two examples just to show you the power of for example CDK. Um so this is a small stack of um AWS CDK and um I use it quite often in in any

**[9:52](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=592s)** kind of prototyping uh because it just deals with a lot of infrastructure for me. So this particular small piece of code will generate a load balancer with some uh docker serverless docker cont docker container cluster and some um https listener and ssl certificate and it will generate all sort of networking uh resources for me like VPC networking um you know the the computing computing service some certificates and DNS records and so on. Of course, I can define them uh by myself and kind of pass it into the construct. But if I don't have to I don't want to deal with this and I just need to prototype certain certain things quickly, then I can just use the power of constructs. I

**[10:42](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=642s)** can of course define a construct myself. So I can if I repeat the same job over and over again, I can just uh create a construct and just import it into my application every time I'm defining for example ECS cluster. Another example is uh it's a completely different approach to generate the infrastructure as um SST. SST is based on Palumi. So it will use a PUMI engine underneath um and it integrates with majority of the front-end frameworks. In this case, I'm using Astro and it just literally needs one extra file to define inside your Astro project. And this particular piece of code defines bunch of resources to deploy a static site to AWS. namely it will um package

**[11:31](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=691s)** and deliver all all static content into S3 bucket and it will also create a CDN distribution uh on cloudfront and some some records for DNS just to make sure that u um it's visible on your custom domain. Um so some of the key takeaways um I wanted to mention it's like when you're defining um infrastructure as code always define some life cycle policies for your resources especially for stateful resources um just to protect them from accidental deletion especially when you're using programmatic um programmatic approach and you put some weird conditions like create me a database on Tuesdays Um with the resource protections you can basically

**[12:20](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=740s)** protect yourself from from accidental um wiping out your data. Um use reusable patterns to create constructs and and some models and and all sort of smaller components or like repeatable infrastructures and share them inside your organization. You can also create some customized uh resources which will follow your security and compliance requirements inside your organization and then share it across uh different teams. Um obviously use continuous deployments of an infrastructure as part of your application um deliver the changes um from code. So you know githubs and cd pipelines um you can use static code analyszis. So most of the frameworks uh including

**[13:11](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=791s)** um the programmatic ones will produce some sort of static code like templates which will be then deployed to your target platform and you can use some any sort of uh llinters and security scanners like snake or check off to um to validate security posture of your infrastructure before actually deploying it. So you can fail it during your CI/CD pipeline before it um hits a hits a target platform like uh AWS. Um drift detection drift is something uh like a difference between a code and a resources deployed in your target platform like AWS or or any kind of uh cloud platform. And um and it's very important to actually detect any sort of drifts. So

**[14:01](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=841s)** if someone commits something to codebase and doesn't actually deploy that to cloud, that's a drift. If someone do does some clickups on um on the console and doesn't um represent it in a code changes on on your infrastructure, that's a drift. And it's very important to kind of detect those drifts and and remedate it as as soon as possible. Otherwise you can you can end up in a very very unstable um infrastructure as code and uh another one is uh automated rollback. So most of the frameworks deal with this quite quite well um but you don't want to end up in a half deployed infrastructure when when something happens on your CI/CD pipeline. So you still want to be informed and if the framework cannot resolve any sort of uh

**[14:51](https://www.youtube.com/watch?v=p9XAT67eFJ4&t=891s)** deployment issues and cannot roll back automatically, you still have to um you still have to kind of manually check it. So you still need to create some sort of uh monitoring around your deployments on infrastructure to make sure that the infrastructure is always deployed in a healthy manner. And uh that's it from me to be honest. So um if you want to connect or or like you want to see some infrastructures code um examples which I showed and then then you can you can uh check it on my link tree. Uh and yeah I do have some time for questions if you have any.
