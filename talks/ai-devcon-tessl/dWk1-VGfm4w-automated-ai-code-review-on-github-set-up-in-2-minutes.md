---
id: dWk1-VGfm4w
title: "Automated AI Code Review on GitHub, Set Up in 2 Minutes"
slug: automated-ai-code-review-on-github-set-up-in-2-minutes
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 9
published_at: 2026-10-28T17:00:22Z
video_id: dWk1-VGfm4w
url: https://www.youtube.com/watch?v=dWk1-VGfm4w
youtube_url: https://www.youtube.com/watch?v=dWk1-VGfm4w
tags: []
topics: ["AI in the SDLC & engineering orgs", "Coding assistants & agents"]
transcript: true
---

# Automated AI Code Review on GitHub, Set Up in 2 Minutes

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=dWk1-VGfm4w) · [Conference site](https://tessl.io/devcon/)

## Description

See Tessl Code Review in action as we review a real pull request from Nuclei, an open-source vulnerability scanner, and uncover issues missed in the original review.

In this walkthrough, you'll learn how to:

- Connect Tessl Code Review to your GitHub repository in minutes.
- Automatically review new pull requests and get actionable, line-level feedback.
- Configure reviews to run in comment-only or blocking mode.
- Identify bugs, reliability issues and potential performance problems.
- Use review feedback in automated workflows to improve code quality before merging.

Tessl Code Review can also be integrated into a software factory, where issues are passed back to coding agents for automated fixes and further review.

Try Tessl Code Review for free: tessl.io/code-review

## Transcript

*1,324 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=0s)** Hi there. My name is Simon Maple, and in this video, we're going to play with the Tessl code review. We're going to take an existing, well-known repository, an open source repository, which is called Nuclei. And our Nuclei is in the ProjectDiscovery organization. And it's a fast, customizable vulnerability scanner provided by the global security community, as they describe themselves. So the first thing I'm going to do is fork this repository. And I'm going to add this into my sjmaple environment. So I'm going to create that fork. And then on that forked repository, I'm going to clone that into my local environment, which we're going to then be able to see on my machine. So let's grab that, go over to a terminal, let's git clone

**[0:49](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=49s)** that repo. And then I'm going to cd into Nuclei, and I'm going to just run Claude. And we'll leave it there just for a second. Let's jump over to Tessl now. Now, in Tessl, there's a reviewer. Once you've logged into a Tessl account, there's a Reviewer option here on the left-hand side. I'm going to go ahead and click that. Now, I uninstalled the Tessl app from my GitHub account just to show you what the flow would look like. So you won't see this message about Tessl Reviewer being uninstalled. But what you will need to do is click the Install on GitHub button here. And then when you click that, you choose where on GitHub you want to install that. And then you can select all repositories or just selected repositories from your organization that you will allow Tessl to view.

**[1:38](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=98s)** So I'm going to select Only select repositories here. And let's grab this Nuclei environment there. I'm going to install and authorize. And once that's installed, I can now see my repository down here in the list. Now, that doesn't necessarily mean code review is enabled. It just means Tessl has access to that. So what I need to do is, on the right-hand side here, click Turn on. Now Tessl code review is turned on for that repository. That's all we needed to do. Any new pull requests that are now sent to that repository, raised against that repository, will now have Tessl review on it. We can, at this stage, choose some configuration options on this code review installation. So we can say when they should be reviewed. So right now, code review is running when a pull request is opened or requested.

**[2:30](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=150s)** That's absolutely fine. You could also do it on every update. And you can also state whether you want the review behavior to actually gate your process or just provide you with informational, you know, code review data only. So I've got Comment only. This means it's just going to provide me with a comment on that, the information for the code review. It's not going to block or necessarily approve. So we're going to leave that as it is. That's all installed. Let me now go back to Claude. Okay. I'm going to go back to pull request 7814. That was only six pull requests ago. But what I did notice is there are some potentially major issues with that pull request. So I'm going to ask Claude: roll back to pull request 7814. When it does this, what I'm next going to do is

**[3:26](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=206s)** replay that pull request. And what that essentially means is when that pull request gets added back into that repository, we're going to see Tessl code review run and provide us with those results. Okay. Now that's done. So if I were to go back to my Git repo and refresh, you can see that this branch is already 28 commits behind. Perfect. Now what I want to do is I want to replay that pull request. So let's ask: replay the PR, what was it, 7814, so that the PR contains all the code committed in that PR, with PR comments. So this triggers

**[4:17](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=257s)** the Tessl code review. Let me know what the results of the code review are. Okay. Now what's happening is I'm going to replay this pull request. What that's essentially going to do is it's going to re-push the same code that was committed probably only a week or two ago. And what we're going to do now, at this time, though, because the Tessl code review is enabled on that repository, it's going to run and provide us with all the suggested changes back. Okay, this looks good now. So we've opened that pull request, and it looks like the original review discussion, inline comments, etc., is being added into it.

**[5:09](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=309s)** Let's make sure. Let's go into that pull request. Now, if I scroll down, we have the Tessl Reviewer. Now the Tessl Reviewer is running. That may take a few minutes. This is now going to run that full code review against the change. And we should hopefully see in a few minutes some output, some suggestions as to what needs to be changed. Right. So now you can see the Tessl Reviewer has completed. It took two minutes to run, and you can see there's a tick by it. So this is because it's a non-blocking test. I could change that if I wanted, but it's non-blocking for now. If I scroll up, you can see a number of comments that were added, as well as, you know, a summary here. And this summary says that it's found two major

**[6:04](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=364s)** issues and four minor issues. Now, of course, if we were to run using Tessl in a software factory environment, this could actually be passed back to the implementation stage. And the implementer would use these, understand them, and actually make changes to the pull request. And we would go through a number of cycles to make sure that these issues were reduced and eliminated. But here, as a human, I might look through and actually say, well, let me take a look at these. Can take reports. Fractional refill as a media admission as a minor. I can go through and understand whether I'm fine with these or if I actually want to make changes myself. Some of them, potentially the major ones, I might want to take a look at. And of course, here you can see it actually picks very specific lines and provides information about them. So the evicted host limiters continue independently of

**[6:54](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=414s)** replacement limiters. So this is obviously a capacity issue. You know, overload a target when, you know, multiple limiters are being executed. Another major here: stop at first match does not cancel HTTP work already in flight. So the worker context is canceled after the first match, but the execute request method receives more impact whose context remains the original input context. So it gives great information about what the issue is. I can then go ahead here, make my changes, or potentially even block. Once we're used to Tessl commenting on these pull requests, potentially block CI pipelines and so forth, as we wish and as we want to set that up. So this is Tessl code review. We also add a number of other things, including a more

**[7:45](https://www.youtube.com/watch?v=dWk1-VGfm4w&t=465s)** deterministic test called Tessl verifiers, as well as something newly being brought in, which is security code review, where Tessl can pull in information from existing security tools such as Snyk and other tools. And it can pull that in and potentially even, as a software factory, provide that cycle where we pass that security information and the issues back to the implementer, that can essentially remediate those types of security issues before we push that forward into production. So that's Tessl code review. It's available today. You can install it for free. Just create a new Tessl account and follow the instructions that I laid out in this video. Thanks for watching.
