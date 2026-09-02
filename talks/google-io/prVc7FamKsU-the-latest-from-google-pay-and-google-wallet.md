---
id: prVc7FamKsU
title: "The latest from Google Pay and Google Wallet"
slug: the-latest-from-google-pay-and-google-wallet
conference: google-io
conference_name: "Google I/O"
category: "Vendor events"
edition: "I/O 2026"
year: 2026
speakers: ["Edson Yanaga", "Kushagra Patel", "Gokmen Goksel"]
channel: "Android Developers"
duration_min: 19
published_at: 2026-05-21T16:30:14Z
video_id: prVc7FamKsU
url: https://www.youtube.com/watch?v=prVc7FamKsU
youtube_url: https://www.youtube.com/watch?v=prVc7FamKsU
tags: ["Android", "pr_pr: Google I/O;", "ct:Event - Technical Session;", "ct:Stack - Android;", "Google Pay", "Google Wallet"]
topics: ["Agents & orchestration", "Enterprise adoption & strategy"]
transcript: true
---

# The latest from Google Pay and Google Wallet

**Edson Yanaga, Kushagra Patel, Gokmen Goksel**

`Google I/O` · `I/O 2026` · `2026` · `19 min`

`#Android` `#pr_pr: Google I/O;` `#ct:Event - Technical Session;` `#ct:Stack - Android;` `#Google Pay` `#Google Wallet`

[Watch the recording](https://www.youtube.com/watch?v=prVc7FamKsU) · [Conference site](https://io.google/)

## Description

Discover the evolution of Google Pay and Wallet in the age of agentic AI. Learn about new tools and capabilities that offer greater flexibility and ROI, while providing a frictionless user experience. Discover API updates, expanded Digital ID global coverage, and new digital receipt support.

Resources:
Google Wallet developer documentation → https://goo.gle/io-26-wallet
Jetpack Credential Manager → https://goo.gle/io-26-jetpack
W3C Digital Credentials API → https://goo.gle/io-26-w3c-dc-api
Google Pay & Wallet Developer MCP Server → https://goo.gle/3R3RRxG
Life cycle notifications for Merchant Initiated Transactions → https://goo.gle/pay-mit-lcm
Cross device transaction confirmation → https://goo.gle/pay-x-device

Speakers: Edson Yanaga, Kushagra Patel, Gokmen Goksel

Watch the Android sessions from Google I/O 2026 → https://goo.gle/Android-at-IO2026

#GoogleIO

Event: Google I/O 2026

Products Mentioned: Google Pay and Wallet

## Transcript

*2,518 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=prVc7FamKsU&t=0s)** [MUSIC PLAYING] KUSHAGRA PATEL: Hello, everyone. My name is Kushagra Patel, and I'm a Product Manager working on Google Pay. It is a pleasure to have you with us. Our team has been developing a variety of powerful new capabilities for the Google Pay and Google Wallet Developer platforms, all designed to facilitate commerce and deliver exceptional user experiences. Let us begin by exploring the latest updates for Google Pay. Today, we are looking at how Google Pay is evolving for the era of agentic commerce. We'll show you how the new universal commerce protocol makes your existing Google Pay merchant ID and payment processing backend fully

**[0:49](https://www.youtube.com/watch?v=prVc7FamKsU&t=49s)** usable for AI-driven services. We'll also unveil the new MCP server to bring AI assistance directly into your development environment. And finally, we'll walk through a suite of new features from express checkout on Android to least cost routing, all designed to streamline your checkout funnel and help you reach your business goals. Let's dive into it. We know the value of the work you've already put into your payment stack. While Google Pay SDKs handle the front end UI, the heavy lifting happens in the backend processing of secure tokenized credentials. Good news, developers. Your existing Google Pay backend, and even your current merchant ID

**[1:36](https://www.youtube.com/watch?v=prVc7FamKsU&t=96s)** are fully compatible with the new universal commerce protocol, Payment Handler. This means you can power new agentic commerce experiences using the same Google Pay infrastructure NPSB relationships you use today. This allows you to extend your reach to agentic surfaces without rebuilding your core payment logic or reconfiguring your business identity. To learn more, find the link in the video's description to get started with your Google Pay integration and get you set up with future agentic experiences. Now, let's take a closer look at what the Google Pay and Wallet Developer MCP server looks like in practice. This is a tool that enables your AI agents

**[2:27](https://www.youtube.com/watch?v=prVc7FamKsU&t=147s)** to streamline the integration process and help you complete end-to-end API integrations without leaving your preferred development environment. The Google Pay and Wallet Developer MCP server includes tools to manage your integrations, troubleshoot errors, analyze trends, or generate code to add Google Pay and Google Wallet to your applications, all to simplify your integration workflows and accelerate the time to first transaction. Use prompts, "What is the status for my Google Pay integration?" Or "List Google Pay transaction errors for the last seven days." The Google Pay and Wallet Developer MCP server is available today in public preview,

**[3:15](https://www.youtube.com/watch?v=prVc7FamKsU&t=195s)** and will graduate to general availability later this year. Check it out at goo.gle/pay-wallet-mcp. While the MCP server is designed to remove friction from your development workflow, we are equally committed to removing friction from the buyer's journey. After all, checkout friction is good for no one. That is why we are excited to bring the power of onPaymentAuthorized and onPaymentDataChanged callback to Android, providing parity with our web platform. With these updates, you can now move the Google Pay button upstream, positioning it directly on your product detail or card pages to offer a true express checkout experience.

**[4:06](https://www.youtube.com/watch?v=prVc7FamKsU&t=246s)** This transforms your Android app's journey into a streamlined, one-click flow, with Google Pay providing the user's shipping address, payment credentials, and contact details all within the pay sheet, delivering a true one-click experience. With onPaymentDataChanged callback, you can present shipping options dynamically based on the user's shipping address, including total price, factoring in the taxes, and options as the user interacts with the payment sheet, and display the updated final price in the pay sheet. With onPaymentAuthorized callback, you can authorize transactions, handle retries, and deliver instant feedback without ever closing the payment sheet, helping you improve authorization rates, and hence, conversions.

**[4:56](https://www.youtube.com/watch?v=prVc7FamKsU&t=296s)** By integrating the Play Services Wallet SDK version 20.0.0 or later, developers can now implement logic to handle these DPU-specific event callbacks within their applications. Following our announcement last year regarding Google Pay support for Android webviews, which enables secure purchases through device tokens, we are advancing our capabilities by extending Google Pay support to social apps. This single integration now facilitates seamless payment experiences across apps, the mobile web, desktop environments, and social platforms. To guarantee that Google Pay functions optimally across your digital platforms, utilize the isReadyToPay API.

**[5:47](https://www.youtube.com/watch?v=prVc7FamKsU&t=347s)** This allows you to programmatically verify whether the Google Pay button should be displayed to the user for your web-based implementation. Next, we are updating support for merchant-initiated transactions. You or your PSP will now have the ability to receive lifecycle notifications for Google Pay payment tokens when underlying credentials change. This enables you to proactively contact customers and request they update their payment methods before the next billing cycle, ensuring continuity for recurring transactions. These notifications will include the updated state of the token, if any changes have occurred since the initial transaction or the last update. Find more information by checking the link below.

**[6:37](https://www.youtube.com/watch?v=prVc7FamKsU&t=397s)** Beyond just facilitating fast transaction, we are committed to helping you optimize the economics of every payment. We know that managing processing costs is a top priority for any growing business, so we are introducing new tools to give you more transparency and control over how transactions are routed and processed. This starts with the card funding source signal. Google Pay's card funding source signal helps you customize the checkout journey and manage transaction processing costs. Google Pay API response now includes card funding source, and you will receive whether the card is credit, debit or prepaid, allowing you to implement sophisticated business logic, like intelligent surcharge price

**[7:27](https://www.youtube.com/watch?v=prVc7FamKsU&t=447s)** modifications and dynamic payment routing. For instance, you can use this data to instantly apply discounts or add surcharges right on the confirmation screen, based on whether a debit or a credit card is being used and the cost associated with them. We also have great news for our developers and merchants operating in Australia. We are officially bringing EFTPOS, the domestic payment network, to Google Pay API to help you further optimize your transaction processing. We recognize that managing transaction costs is a critical part of your operations. By leveraging the new merchantPreferre dCobadgedCardNetworks parameter you can explicitly prioritize the local network and dynamically route transactions to EFTPOS.

**[8:17](https://www.youtube.com/watch?v=prVc7FamKsU&t=497s)** This provides you with granular per-request control with no heavy back end lifting required. To get started, simply add EFTPOS to your allowed card networks and to your list of preferred cobadged card networks, and you are ready to go. While mobile commerce is growing, desktop remains a critical surface where friction continues to fuel card abandonment, particularly where MFA, multi-factor authentication, is a regulatory requirement. In these regulated markets, the challenge is balancing security mandates while delivering a seamless user experience. Today, I am introducing cross-device, a Google Pay capability that moves high friction desktop checkouts into a secure, mobile-first authentication

**[9:08](https://www.youtube.com/watch?v=prVc7FamKsU&t=548s)** flow. Cross-device creates a bridge between platforms. For qualifying transactions on your desktop site, users are prompted to authenticate on their phone via secure notification or a QR code. This helps meet the requirements of MFA by using the phone as a possession factor and user's biometrics as an inherence factor. This removes the need for disruptive SMS OTPs or clunky redirects that often break the checkout flow. Instead, customers approve the payment using a familiar biometric unlock or pin on their trusted Android device. For merchants, this helps increase conversion rates by replacing traditional authentication hurdles

**[9:57](https://www.youtube.com/watch?v=prVc7FamKsU&t=597s)** with a more direct journey. Cross-device provides built in MFA compliance support for your transactions. This helps you meet local mandates while supporting your ability to achieve fraud liability shift by leveraging Google's secure tokenized credentials. Top global merchants are already using cross-device to refine their online checkout. It was a great year for Google Pay. We are excited for the future enabling agentic commerce journeys, and stay committed to make sure developers have a delightful experience when integrating our API. And now, I'll turn it over to Gokmen and Edson to tell you about the latest from the Google Wallet. [MUSIC PLAYING] GOKMEN GOKSEL: Hi, everyone. I'm Gokmen, working as a Staff Software

**[10:45](https://www.youtube.com/watch?v=prVc7FamKsU&t=645s)** Engineer for Google Wallet. It's great to be here at I/O. Let's dive right into what is new with Google Wallet. We have major updates, starting with Identity. We are expanding our digital ID coverage to be available to an estimated 1.5 billion eligible users globally. In India, we launched support for Aadhaar, the national ID for over 1.4 billion Indian citizens. In Japan, we are bringing the My Number Card to Wallet late this year. We are also expanding our passport-verified ID Pass to over 10 more regions, including Brazil, Taiwan, and several other countries. If you need to perform ID verification or write checks, you can securely request the user to share the specific attributes of their ID as needed. For Android apps, you can use the Jetpack Credential Manager

**[11:34](https://www.youtube.com/watch?v=prVc7FamKsU&t=694s)** library. While it also handles passwords and passkeys, it includes a dedicated flow for verifiable credentials. For websites, you can use the W3C Digital Credentials API, which follows a nearly identical pattern. This API now supports cross-device requests, meaning a desktop website can request a credential right from the user's phone. Together, these APIs lets you seamlessly and securely request credentials from native apps, mobile web, and desktop web. To see this in action, let's look at how Uber is already using the Credential Manager API. They use it to securely verify a driver's identity with just a few taps. When a user needs to verify their account, Uber simply requests the necessary details. The user sees a secure prompt from Credential Manager, selects Google Wallet, taps to agree, and the verification

**[12:24](https://www.youtube.com/watch?v=prVc7FamKsU&t=744s)** is complete in seconds. Intuit is also using a similar flow with the Credential Manager API to simplify account recovery. By securely requesting a verified ID, they help customers regain access to their accounts quickly and safely. We have also helped improve user's privacy by open sourcing our Zero Knowledge Proof libraries. Zero Knowledge Proof is a cryptographic protocol that lets users prove that something about them is true without sharing any other data. This means you can securely verify a user's age without ever revealing their personally identifiable information. Beyond Identity, Google Wallet is becoming an even more useful tool for travelers. We want to make travel feel less stressful and disconnected and be with travelers throughout their journey.

**[13:12](https://www.youtube.com/watch?v=prVc7FamKsU&t=792s)** Take Flights, for example. We are enhancing the experience for flyers before, during, and after the trip. Starting before the trip, we will soon enable contextual loyalty enrollment directly on the boarding pass. This makes it easy for flyers to discover and enroll in their favorite airline's frequent flyer programs. Any airline that implements our loyalty API can take advantage of this feature to help grow their enrolled user base. Another reason for you to ensure your users add their passes into Google Wallet is we are expanding Chrome autofill. Chrome can now seamlessly recall your Wallet Pass information and autofill things like your passports, driver licenses, booking confirmation and loyalty cards into forms, natively in Chrome on both desktop and iOS. During the trip, we are building on Auto Linked Passes, which lets you automatically push related passes into user's

**[14:03](https://www.youtube.com/watch?v=prVc7FamKsU&t=843s)** Wallet. Azul Airlines in Brazil is using this to streamline the check-in experience for their customers. After a user checks in, whether on mobile, web or at the airport, Azul automatically pushes their boarding passes into their Google Wallet. This creates a seamless travel experience at the airport. You can also use Auto Linked Passes to enable other value-added experiences, such as linking relevant offers, baggage tags, and more to a user's existing boarding pass or loyalty card to easily reward frequent flyers. Finally, during the flight and after the trip, we recently introduced Live Flight Updates. This enables flyers with a boarding pass in Google Wallet to receive real time updates, like delays or gate changes, directly on their Android devices lock screen.

**[14:52](https://www.youtube.com/watch?v=prVc7FamKsU&t=892s)** Airlines and other ticket issues, such as event organizers, can take advantage of this to alert users to any urgent, time-sensitive changes by simply pushing up-to-date information directly to the pass. Now, I will hand it over to Edson to talk about retail and preview what's next for the Wallet platform. EDSON YANAGA: Thanks, Gokmen. Hello, I/O. I'm Edson, a Developer Relations Engineer for Google Wallet. Let's shift to retailers and merchants. We are taking those same engagement foundations and expanding how you connect with customers. To help you acquire new customers in store, we are rolling out the contactless loyalty enrollment for both smart tap and non-smart tap setups. When a customer taps to pay at your store,

**[15:41](https://www.youtube.com/watch?v=prVc7FamKsU&t=941s)** we send them a push notification inviting them to join your loyalty program if they haven't signed up before. Or if they have, they can sign into their account and save their loyalty card. To help you more easily integrate with Google Wallet, we've partnered with Salesforce. If you use Salesforce loyalty management, a native integration is available today. You can manage your loyalty programs entirely within Salesforce and natively issued passes directly to Google Wallet. This allows you to easily create loyalty cards, coupons, offers, gift cards, and more, ensuring your customers have all of them available right in their Wallet. Last year, we introduced Nearby Passes Notifications to send silent notifications to users near your store.

**[16:31](https://www.youtube.com/watch?v=prVc7FamKsU&t=991s)** You previously had to manually define up to 10 merchant locations. Today, we are making this much easier. Wallet will now use Google Maps to automatically infer the right locations for your passes. We're enabling these for some loyalty passes soon, and we'll be rolling out more in the future. If you don't want this, you will be able to disable the feature via the API. On the topic of notifications, many of you are already using the Wallet's API to engage users via push notifications. While those messages previously relied on standard templates provided by Google Wallet, we are now launching a highly requested feature, Customizable Push Notifications. For your text and notify messages,

**[17:20](https://www.youtube.com/watch?v=prVc7FamKsU&t=1040s)** you now have full control to craft the exact message you want. Coming soon for developers, we are also working on a dedicated API that will allow you to share digital receipts directly into Google Wallet. This will enable you to keep your customers informed and significantly reduce support friction throughout the post-purchase lifecycle. To wrap things up, let's look at the new Google Wallet interface that is available today. On the Wallet home, we are providing dynamic quick access to your favorites. For time-sensitive content, like a boarding pass right before a flight, we have a new updated visual design. The new View More section serves as a comprehensive, highly searchable hub for everything in Wallet,

**[18:11](https://www.youtube.com/watch?v=prVc7FamKsU&t=1091s)** including detailed transaction information. Similarly to travel, users can leverage Chrome autofill to help recall your merchant loyalty cards in Chrome to make it easier to ensure you accrue your loyalty points and rewards. It's been a highly productive year, and we look forward to seeing what you build next. Cheers. [MUSIC PLAYING]
