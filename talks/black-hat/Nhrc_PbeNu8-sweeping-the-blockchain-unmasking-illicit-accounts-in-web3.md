---
id: Nhrc_PbeNu8
title: "Sweeping the Blockchain: Unmasking Illicit Accounts in Web3 Scams"
slug: sweeping-the-blockchain-unmasking-illicit-accounts-in-web3
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 20
published_at: 2025-09-19T17:06:38Z
video_id: Nhrc_PbeNu8
url: https://www.youtube.com/watch?v=Nhrc_PbeNu8
youtube_url: https://www.youtube.com/watch?v=Nhrc_PbeNu8
tags: []
topics: []
transcript: false
---

# Sweeping the Blockchain: Unmasking Illicit Accounts in Web3 Scams

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `20 min`

[Watch the recording](https://www.youtube.com/watch?v=Nhrc_PbeNu8) · [Conference site](https://www.blackhat.com/)

## Description

The web3 applications have recently been growing, especially on the Ethereum platform, starting to become the target of scammers. The web3 scams, imitating the services provided by legitimate platforms, mimic regular activity to deceive users.

We will provide a case study where attendees will learn how a malicious scam mimics a normal transaction to deceive users. Previous studies have primarily concentrated on de-anonymization and phishing nodes, neglecting the distinctive features of web3 scams. Moreover, the current phishing account detection tools utilize graph learning or sampling algorithms to obtain graph features. However, large-scale transaction networks with temporal attributes conform to a power-law distribution, posing challenges in detecting web3 scams.

In this talk, we will introduce ScamSweeper, a novel framework designed to address these challenges. ScamSweeper focuses on the dynamic evolution of transaction graphs to better detect Web3 scams on Ethereum. Attendees will learn how ScamSweeper improves on existing methods by utilizing a structure-temporal random walk to sample transaction networks, capturing both temporal and structural features. The framework also incorporates a variational transformer to analyze the dynamic evolution of transaction patterns over time.

To detect and analyze these scams, we've collected a large-scale transaction dataset for experiments consisting of web3 scams, phishing, and normal accounts, which are from the first 18 million block heights on Ethereum. Our experiments indicate that ScamSweeper exceeds the state-of-the-art in detecting web3 scams, with advantages of 17.29% in weighted F1-score. In addition, ScamSweeper in phishing node detection has an advantage of 17.5% in F1-score.

We will walk through how to collect large-scale datasets, what the distinctions of the datasets are in various attributes, how Scamsweeper samples the large-scale transaction data and reduces computational costs, and how Scamsweeper works in web3 scam detection. Attendees will gain a clear understanding of how to apply ScamSweeper to real-world Ethereum transactions, and how to incorporate dynamic evolution analysis into malicious behavior research.

By:
Wenkai Li  |  PhD Candidate, Hainan University
Zhijie Liu  |  Graduate Student, ShanghaiTech University
Xiaoqi Li  |  Associate Professor, Hainan University

Full Abstract and Presentation Materials:
