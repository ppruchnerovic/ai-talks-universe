---
id: 5eIrd7bHy9I
title: "USENIX Security '24 - Inference of Error Specifications and Bug Detection Using Structural..."
slug: usenix-security-24-inference-of-error-specifications-and
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 11
published_at: 2026-06-02T20:54:10Z
video_id: 5eIrd7bHy9I
url: https://www.youtube.com/watch?v=5eIrd7bHy9I
youtube_url: https://www.youtube.com/watch?v=5eIrd7bHy9I
tags: ["usenix", "technology", "conference", "open access"]
topics: ["Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: true
---

# USENIX Security '24 - Inference of Error Specifications and Bug Detection Using Structural...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2026` · `11 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=5eIrd7bHy9I) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

Inference of Error Specifications and Bug Detection Using Structural Similarities

Nora Dossche and Bart Coppens, Ghent University

Error-handling code is a crucial part of software to ensure stability and security. Failing to handle errors correctly can lead to security vulnerabilities such as DoS, privilege escalation, and data corruption. We propose a novel approach to automatically infer error specifications for system software without a priori domain knowledge, while still achieving a high recall and precision. The key insight behind our approach is that we can identify error-handling paths automatically based on structural similarities between error-handling code. We use the inferred error specification to detect three kinds of bugs: missing error checks, incorrect error checks, and error propagation bugs. Our technique uses a combination of path-sensitive, flow-sensitive and both intra-procedural and inter-procedural data-flow analysis to achieve high accuracy and great scalability. We implemented our technique in a tool called ESSS to demonstrate the effectiveness and efficiency of our approach on 7 well-tested, widely-used open-source software projects: OpenSSL, OpenSSH, PHP, zlib, libpng, freetype2, and libwebp. Our tool reported 827 potential bugs in total for all 7 projects combined. We manually categorised these 827 issues into 279 false positives and 541 true positives. Out of these 541 true positives, we sent bug reports and corresponding patches for 46 of them. All the patches were accepted and applied.

View the full USENIX Security '24 program at https://www.usenix.org/conference/usenixsecurity24/program

## Transcript

*1,619 words · source: supa (en, exact timings)*

**[0:08](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=8s)** I will be presenting our work inference of error specifications and bug detection using structural similarities. This is a work of static analysis to detect uh error checking books and there are three types of error checking books that we are interested in. Incorrect checks, missing checks and propagation books. So an example of an incorrect check comes from this snippet of open SSL in which we have a function call drawn to bytes X and we compare the result with zero. If it's less than zero, we jump to an error bot. However, if you were to look at the implementation of this function, you can notice that zero is also a possible return value and in this case the error path is not taken. Second example for missing check is um this snippet of code in which you have

**[0:57](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=57s)** two function calls XML start element and XML end element. But notice that the second if check doesn't actually do anything because the assignment of redfall is missing. Finally, propagation bugs. These occur when we have different data types to propagate errors with but the valid values between the two types differ. So when an implicit or explicit cost happens the the propagation is incorrect and so any error checking that uses these values can be incorrect to know how to detect these issues we first need to know how to model errors. So I consider two broad categories in our work either model errors by convention or by specification.

**[1:46](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=106s)** So conventionbased approaches use the fact that error handling go often uses null e inval go to error those typical kind of keywords. Specifications on the other hand create like a list of functions that can return errors and what the possible error return values for those functions are. So for me this is zero for open this is negative one and finally z get property info depends on has two possible values depending on the error condition specifications will be what I will focus on and either you can create these cu manually or fully automatically so a state-of-the-art uh in error specifications is easy which is c manually it starts with domain knowledge that a programmer needs to provide and then it expands the

**[2:35](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=155s)** knowledge Automatic approaches are like apex, a res and our approach esss. To illustrate how these kind of work, I'm going to show a lot of codes. And I know this can be overwhelming, but it will show my points because for us humans and for convention based approaches, it's still very easy to notice all the error handling codes like err race rays is probably short for error race. We have a null check, a go to error and so on. However, this can be very specific to the codebase you're working with. Our approach, on the other hand, uses similarities. And to illustrate that, let's take a look at, for example, these two code segments. And we're going to simplify them. We're going to create like a summary of them, simplified representation that does away with the control flow. Um, the first code segment

**[3:25](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=205s)** has a call to arrays and returns zero. The second code fragment um calls arrays also calls an other function and then returns zero. Notice how in the original source code that it returns red but our tool deducts that at this point only zero can be valid for red. If you now compare the two summaries, we can see that they both call the same function and return the same value. In fact, you could say that the first one is a subsequence of length two of the second one. Similarly, if you take a look at the B and null error handling codes, we can see that well, they both jump to the same label. So, the tail is the same and we can have a subsequence match of length two. So, what's the idea here? Well, we we notice that all error

**[4:15](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=255s)** handling code is more similar to each other than all the code around it. So the idea is that we create these matches. The best matches are marked as error handling blocks and once we know what the error handling blocks are, we know what values they can return and so we know what the error returning values for the functions are. However, this is not enough on its own because take a look at this example. So we call a function, compare it with zero and then call error rate. But there's only a single check. There's no similar code to compare against. Fortunately though, we do see the arrays function again. And the idea here is that well, if you notice during similarity matching that a

**[5:02](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=302s)** particular function is often occurring in error handling codes and we don't yet know the purpose of some other codes, but we do see a typical error handling function in it, then the code is probably error handling related. So that's basically using association analysis to overcome this problem. A very similar problem occurs when we have like a call a check and then there's no other call that can tell us the purpose of the code. However, if you already uh infer that malo returns zero on failures, then we can easily conclude that f must return negative one on failure. So the entire pipeline starts with LLVM bit codes. We perform the similarity matching that creates an initial set of specifications. Then we apply the two techniques that

**[5:50](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=350s)** we've discussed and that will give us a new set of specifications. Then we repeat the process until we eventually reach a fix point. And once we have the specifications, we can use that to detect violations thereof. So we applied this technique on seven different open source projects. So open SSL, open SSH, the PHP interpreter, ZLIP, lip ping, free type and lip. We got a lot of reports from them. Most reports are from open SSL and PHP because they are also the largest code bases. If you then take a look at the split between missing check, incorrect check and propagation bugs. You can see that most bugs are missing checkbox. However, personally, I find incorrect checking bugs the most interesting case because they are a lot more subtle to catch.

**[6:38](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=398s)** Finally, what we did is we looked through every report and manually categorized them in false positives, true positives and unknowns. The unknowns is simply a fallback category for when we did not have enough domain knowledge to u confidently say what's uh if it's a true or false positive. Then we obtain these results. So not a lot of unknown cases first of all. Second of all, we notice that the highest false positive rate is for OpenSSL. And this is because of a particular coding pattern in the OpenSSL codebase in which we often have first a function call that um performs some validation of the parameters. Then we repeat the function call to do the actual uh to do the actual work. So and in this case only the first function

**[7:26](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=446s)** is actually error checked and not the second one. So every time that pattern occurs u the second one is incorrectly marked as a missing checkbook. Highest false second highest false positive rate is for PHP followed by ZLIP. All the orders are below 25%. In practice we notice that it's relatively uh easy to go through the reports uh even the false positive rate of 25% for example. We also took a look at how well we performed in terms of memory usage and time usage to infer these specifications when compared to state-of-the-art easy. First of all, easy is already very fast. Um, it can analyze OpenSSL in about 3 minutes with only 20 gigs of memory. Uh

**[8:15](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=495s)** notice there's a dash for PHP in the table and that's simply because the program easy went out of memory uh even on a 128 gig machine. So it does show some scalability limitations. On the other hand, our tool ESS um um uses an order of magnitude less time and less memory. Um, so we were actually able to uh fully analyze uh PHP. Um, and if you take a look at the bottom four rows, you'll see that they have been analyzed um with less than uh in less than a second. So that makes our tool an ideal candidate to, for example, integrate into an IDE plug-in in the future so that programmers can actually

**[9:05](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=545s)** get feedback at the point they're writing the code. So the results um we inspected 827 bugs in seven projects. Um 541 of those inspected bugs were true positives and we sent patches for 46 of the most severe bugs uh in three different open source projects and all of the uh patches have been accepted into the into upstream. Um it amounts to 16 fixes in open SSL. Most were incorrect check bugs there. One fix for open SSH and 29 fixes for PHP including one bug that uh got a CVE. Uh there's much more experiments and

**[9:53](https://www.youtube.com/watch?v=5eIrd7bHy9I&t=593s)** details in the paper. It's also fully open source on GitHub and the artifact is fully evaluated. So if you want to play with it um you can just check out the source and it's relatively simple to uh get going with it. Um artifact evaluation should be the artifact repository is already online so if you want to check that out uh you can do so as well. So that's it for me now and I think we can uh go to the questions now. Thank you.
