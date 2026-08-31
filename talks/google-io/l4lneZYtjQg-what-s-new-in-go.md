---
id: l4lneZYtjQg
title: "What's new in Go"
slug: what-s-new-in-go
conference: google-io
conference_name: "Google I/O"
category: "Vendor & platform"
edition: "I/O 2026"
year: 2026
speakers: ["Marc Dougherty", "Cameron Balahan"]
channel: "Google Cloud Tech"
duration_min: 15
published_at: 2026-05-22T16:15:49Z
video_id: l4lneZYtjQg
youtube_url: https://www.youtube.com/watch?v=l4lneZYtjQg
tags: ["pr_pr: Google I/O;", "ct:Event - Cloud PA Keynote;", "ct:Stack - Cloud;", "Go 1.26", "Go 1.25", "Golang performance 2026", "Green Tea Garbage Collector", "Go Fix Modernizers", "native vectorized instructions", "archsimd package", "Green Tea GC benchmarks", "GO SIMD optimization", "goroutine leak detection", "low latency microservices", "Go 1.26 release notes", "Memory management in Go"]
transcript: true
---

# What's new in Go

**Marc Dougherty, Cameron Balahan**

`Google I/O` · `I/O 2026` · `2026` · `15 min`

`#pr_pr: Google I/O;` `#ct:Event - Cloud PA Keynote;` `#ct:Stack - Cloud;` `#Go 1.26` `#Go 1.25` `#Golang performance 2026` `#Green Tea Garbage Collector` `#Go Fix Modernizers` `#native vectorized instructions` `#archsimd package` `#Green Tea GC benchmarks` `#GO SIMD optimization` `#goroutine leak detection` `#low latency microservices` `#Go 1.26 release notes` `#Memory management in Go`

[Watch the recording](https://www.youtube.com/watch?v=l4lneZYtjQg) · [Conference site](https://io.google/)

## Description

Go is “boring” in the best way: stable, reliable, and built for scale. Explore what's new in Go 1.25 and 1.26, including the Green Tea garbage collector, native vectorized instructions, and the code-modernizers behind the “go fix” command. Whether your focus is developing AI agents or traditional microservices, discover how Go continues to deliver industry-leading advancements that make it the best choice for your mission-critical, high-performance applications.

Resources:
Go website → https://goo.gle/4ulzTWq
Go 1.25 is released - blog → https://goo.gle/4wzLwKJ
Go 1.26 is released - blog → https://goo.gle/3RJPujR
Using go fix to modernize Go code → https://goo.gle/4fotQeL
//go:fix inline and the source-level inliner → https://goo.gle/3PlrzGU
Allocating on the Stack → https://goo.gle/4wyU3O3

Watch the cloud sessions from Google I/O 2026 → https://goo.gle/Cloud-at-IO2026

#GoogleIO

Event: Google I/O 2026
Speakers: Marc Dougherty, Cameron Balahan
Products Mentioned: AI/Machine Learning, Cloud, Go

## Transcript

*2,141 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=l4lneZYtjQg&t=0s)** [MUSIC PLAYING] CAMERON BALAHAN: Hi. I'm Cameron, and I'm the Product Lead for the Go programming language at Google. MARK DOUGHERTY: And I'm Mark, the Developer Relations Lead for Go. CAMERON BALAHAN: For decades, developers struggled with a difficult trade-off. You could choose productivity using dynamic interpreted languages, like Python or JavaScript, that are fast to write but often struggle with scale and reliability. Or you could choose production-readiness, using strongly typed compiled languages, like C++ or Java, that offer raw power but come with significant complexity. This was the exact challenge Google faced nearly 20 years ago, when Robert Griesemer, Rob Pike, and Ken Thompson sat down at a whiteboard to see if there wasn't a better way. Together, they created the Go programming language.

**[0:49](https://www.youtube.com/watch?v=l4lneZYtjQg&t=49s)** And today, millions of developers don't have to choose between productivity and production-readiness. They can have both. But in the era of AI, does this challenge still matter? The truth is, AI has only made these fundamentals more critical. Languages that are clear for humans are also better for AI models and, again, for the humans who verify their output. And as AI accelerates the volume of code we produce and put into production, making it easy for both AI and humans to write more secure, performant, and maintainable code matters more than ever. Go is boring in the best way. But what really makes go different from almost any other programming language is that it's not just a language. It's an end-to-end platform for software engineering. Software engineering happens in teams.

**[1:37](https://www.youtube.com/watch?v=l4lneZYtjQg&t=97s)** It's the act of collaborating with others, now including both humans and AI, to design and implement durable systems that evolve over time. Programming is a part of software engineering, but just a part. Go was built to serve the whole of software engineering through a robust end-to-end platform with deterministic tooling all around the software development lifecycle. This broader objective is also why we prioritize simplicity, performance, security, and reliability. These principles are the foundation for building systems that remain maintainable years or even decades after the original author has moved on. Today, we're going to show you how we're evolving the Go platform while continuing to fulfill these foundational principles. As you'll see, nearly 20 years after its start,

**[2:25](https://www.youtube.com/watch?v=l4lneZYtjQg&t=145s)** Go continues to make significant, industry-leading improvements to productivity and production-readiness. Off to Mark to get us started. [MUSIC PLAYING] MARK DOUGHERTY: Thanks, Cameron. Go releases major updates twice a year, in February and August. In the last year, we've released a lot of exciting new features in 1.25 and 1.26 to help you and your team be more productive. All languages evolve over time. And as they do, older code can feel less idiomatic, less readable, and harder to maintain. This can also affect new AI-generated code, as newer features and patterns are less prevalent in training data. To combat this, we've rebuilt the Go Fix command to enable continuous modernization.

**[3:13](https://www.youtube.com/watch?v=l4lneZYtjQg&t=193s)** Go Fix leverages the Go analysis framework to deeply understand your code and apply deterministic changes, leaving you with code that takes advantage of the latest language features. The centerpiece of this new engine is the modernizer framework, which enables code transformations that prioritize correctness, ensuring the updated code preserves the original behavior. Go Fix includes over 20 modernizers today to help keep your code clear and readable. Go Fix can help when your own code base evolves, too, thanks to the power of the source-level inliner. Just add a go fix inline directive to your deprecated API and Go Fix will replace calls to that function with the new implementation all across your codebase.

**[4:03](https://www.youtube.com/watch?v=l4lneZYtjQg&t=243s)** Thanks to insights from the Go Compiler, Go Fix can preserve the original behavior of your code even when there are side effects. Go Fix can help you speed up API migrations, so you can remove deprecated methods sooner and keep your whole codebase cleaner. At Google, Go Fix usage has resulted in over 18,000 committed changes across Google's internal codebase, bringing modern Go features to one of the oldest Go code bases. One of Go's core ideas is that source code should be easy for machines to read, write, and edit to support automated refactoring. This idea led to Go's easy-to-read syntax and standardized formatting and continues to inspire our work on Go Fix and modernizers.

**[4:53](https://www.youtube.com/watch?v=l4lneZYtjQg&t=293s)** This very principle has come full circle to supercharge AI code authoring and unlock sophisticated source tools, like modernizers, that operate at scales we could only imagine when ghost started. Next, let's talk about one of Go's most celebrated testing features, the testing synctest package, which graduated to general availability in Go 1.25. Concurrency is naturally complex because operations can happen out of order. As a result, testing concurrent code is also complex, often relying on timeouts or sleep calls, which can lead to flaky tests. Synctest dramatically simplifies testing concurrency by introducing the concept of a bubble, an isolated

**[5:44](https://www.youtube.com/watch?v=l4lneZYtjQg&t=344s)** environment where goroutines use a fake synthetic clock. Within a bubble, time advances automatically when all go goroutines are blocked. This test used to wait five seconds for a timeout, but with synctest, it finishes in milliseconds, deterministically and consistently. Synctest makes it simpler to adjust the order of events in concurrent tests, and ensure that all goroutines finish by the end of the bubble. Go is intentionally boring. We rarely make direct language changes. So code in Go 1.26 looks nearly identical to code from Go 1.0. In Go 1.26, we've made a small but very high-impact change to the language itself, new expression.

**[6:36](https://www.youtube.com/watch?v=l4lneZYtjQg&t=396s)** Go users noticed some awkwardness in dealing with deep structs that make heavy use of pointers, a common pattern in data interchange formats like protobuf. In response, we've expanded the new built-in, allowing it to create pointers from expressions, including basic data types and function return values. Some users and libraries have created their own helper methods to accomplish the same result-- for example, proto.string. Circling back to go fix in modernizers, in many cases, Go Fix can identify these helper methods automatically and replace them with calls to new instead. These tools work together to ensure your code base stays modern, readable, and most importantly, correct.

**[7:24](https://www.youtube.com/watch?v=l4lneZYtjQg&t=444s)** But writing the code is only half the battle. Next, Cameron will show you how we're making that code perform better than ever in production. [MUSIC PLAYING] CAMERON BALAHAN: Mark just walked you through some of the new features and Go 1.25 and 1.26 that make you more productive. But remember, Go isn't just about productivity. It's also about how that code performs in production. Go was built to solve Google-scale problems, so it's no surprise that Go has become the backbone of the modern cloud. Many of the world's best known cloud technologies are written in Go, including Kubernetes, Docker, Terraform, and more. This ubiquity is a direct consequence of Go's enduring focus on production-readiness. And part of what enables us to pursue that focus is Go's compatibility promise, a formal commitment

**[8:13](https://www.youtube.com/watch?v=l4lneZYtjQg&t=493s)** from the Go team that code written to the Go specification will continue to compile and run correctly, without changes across all future releases of Go. Because of the compatibility promise, many of these things get better from version to version with almost no work. You upgrade, you recompile, and your system is simply better. In other ecosystems, as code ages, it becomes a liability. In Go, it becomes an asset. If you do need to change your code to realize a new feature or benefit, Go Fix, which Mark showed you earlier, will do that for you. With that in mind, let's go over some of the ways we've improved the platform over the last few releases. This year, the biggest headline for performance is the new Green Tea Garbage Collector, introduced as an experiment in Go 1.25 and enabled by default beginning in Go 1.26.

**[9:03](https://www.youtube.com/watch?v=l4lneZYtjQg&t=543s)** Green Tea is a major departure from traditional garbage collector design that moves beyond the hardware-imposed limits of traditional algorithms. Green Tea operates by shifting the fundamental unit of work from individual scattered objects to large, contiguous memory blocks called pages. This works with modern hardware design instead of against it, minimizing high-latency memory fetches and letting the runtime use incredibly high throughput vector acceleration. The result is a 10% reduction in garbage collection CPU costs for most applications and up to 50% for those with complex memory layouts, all without changing a single line of code. Green Tea is an evolution of our runtime designed to leverage modern multi-core systems more effectively.

**[9:50](https://www.youtube.com/watch?v=l4lneZYtjQg&t=590s)** It's also a brand-new foundation that unlocks previously impossible opportunities for transparent optimizations, like NUMA awareness in modern server CPU architectures. In a similar vein, in Go 1.25 and 1.26, we introduced runtime optimizations that shift significantly more memory allocations from the heap to the stack. Stack allocations are considerably cheaper and present no load to the garbage collector. They also enable rapid reuse and have better cache locality, resulting in faster memory access-- another transparent win. Again, you don't have to touch your code to get it. But we aren't just making existing code faster. We're also opening doors to new types of workloads. In Go 1.26 we've optimized the transition between Go and C making Cgo calls 30% faster.

**[10:42](https://www.youtube.com/watch?v=l4lneZYtjQg&t=642s)** For any high-performance systems that rely on low-level system APIs or specialized hardware libraries, this significantly reduces the cost of crossing that boundary, which makes possible new use cases in areas like machine learning, gaming, and graphical user interfaces. In other words, we've changed Cgo from a tool of necessity into an opportunity to build entirely new classes of applications. We're excited to see what you do with it. Looking closer to the metal, in Go 1.26 we've introduced first-class support for SIMD. SIMD enables modern CPUs to perform vectorized array manipulations, running certain kinds of loops in parallel. These capabilities are essential for many kinds of performance optimizations, including the sort required for certain kinds of AI infrastructure.

**[11:31](https://www.youtube.com/watch?v=l4lneZYtjQg&t=691s)** In fact, we're using SIMD ourselves to make the Green Tea Garbage Collector even more efficient. And speaking of AI, last year, we launched an official SDK for the Model Context Protocol, or MCP. MCP allows your services to provide context and tools for LLMs through a unified protocol. With this SDK, you can reliably leverage goes signature capabilities to expose data and functionality to your AI applications. We're using our MCP SDK to build servers that expose more of the Go toolchain to agents and AI-powered development tools. You may have seen a prototype MCP server in Gopls, our language server. And you can expect to see more in the year ahead. Next, we've made observability more ergonomic with the new flight recorder.

**[12:19](https://www.youtube.com/watch?v=l4lneZYtjQg&t=739s)** Tracing can be expensive, so the new flight recorder allows you to keep tracing always on in a ring buffer, only flushing it when you need it, giving you the data you need with minimal production overhead. Finally, we're keeping go secure for the next decade with expanded post-quantum cryptography, randomized heat-based addresses, and improved FIPS 140 support. These sorts of proactive security features are how we stay well ahead of the curve and how we ensure that go can continue to be used in the most critical workloads. And there's lots more that you can read about in our release notes on go.dev. Together, all of this continues our focus on keeping go both productive and production-ready. And as we do all this and more, you can rest assured that any changes we make now

**[13:06](https://www.youtube.com/watch?v=l4lneZYtjQg&t=786s)** and in the future will continue to fulfill the Go promise of compatibility. Go remains and will always remain fully backward-compatible to Go 1.0. [MUSIC PLAYING] MARK DOUGHERTY: As you just saw, Go remains laser-focused on improving productivity and production-readiness, continuously adapting it to the changing needs of software engineering and the workloads we create. After all these years, we're still delivering monumental, groundbreaking improvements. How do we do it? Well, we do it together. Today, our ecosystem is larger and more robust than ever. And we continue to see a lot of really high-quality tools and libraries emerge, especially for new use cases around generative AI. And we see hundreds of thousands of Gophers

**[13:57](https://www.youtube.com/watch?v=l4lneZYtjQg&t=837s)** around the world meeting up, attending Go conferences, and collaborating online, all because they love go. So thank you to the Go community. It's because of your contributions that Go is growing and bigger than ever before. We're very proud to be a part of this journey with you. For more information on anything we discussed in this video, be sure to check out our homepage at go.dev. Thank you for joining us this year at Google I/O. We can't wait to see what you build with Go this year and in the years to come. [MUSIC PLAYING]
