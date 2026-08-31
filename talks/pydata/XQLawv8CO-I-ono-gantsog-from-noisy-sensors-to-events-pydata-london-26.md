---
id: XQLawv8CO-I
title: "Ono Gantsog - From Noisy Sensors to Events | Pydata London 26"
slug: ono-gantsog-from-noisy-sensors-to-events-pydata-london-26
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Ono Gantsog"]
channel: "PyData"
duration_min: 29
published_at: 2026-06-15T15:54:08Z
video_id: XQLawv8CO-I
youtube_url: https://www.youtube.com/watch?v=XQLawv8CO-I
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Ono Gantsog - From Noisy Sensors to Events | Pydata London 26

**Ono Gantsog**

`PyData` · `PyData` · `2026` · `29 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=XQLawv8CO-I) · [Conference site](https://pydata.org/)

## Description

Ono Gantsog- From Noisy Sensors to Events: Event Detection in Sensor data with Kalman Filters and Hidden Markov Models

Sensors operating in complex environments produce noisy data. Determining exactly when a system transitions between states — and what values it is recording — is surprisingly hard: vibrations, environmental changes, and gradual shifts all conspire against simple threshold approaches. This talk walks through a real-world Python pipeline that solves this problem, starting with classical signal processing, exposing its failure modes, and then building a principled solution using a Kalman filter for noise reduction coupled with a Hidden Markov Model (HMM) for state inference. Attendees will leave understanding how to frame sensor problems as state estimation tasks and how to apply these techniques in Python using necessary libraries.

Objective
Many operations depend on accurate data from continuous sensor streams. Knowing when a system transitions between states, when a process cycle completes, and how much change occurred per cycle drives scheduling, monitoring, and operational reporting. This talk presents a complete data science pipeline — built entirely in Python — that automates event detection and value estimation from noisy sensor streams. The goal is to give attendees both a worked real-world case study and a transferable toolkit for tackling noisy, event-driven sensor data in any domain.

The Problem
Sensors record measurements continuously, but the raw signal is far from clean. Vibrations, speed changes, and environmental shifts all create noise that masks the true underlying state of the system (for example: wake, light sleep, deep sleep, REM sleep). A naive threshold-based approach — the initial "traditional method" — is brittle: it misfires on transient spikes, misses gradual transitions, and cannot estimate values reliably. This section sets up the problem visually with annotated sensor traces and shows concretely where simple methods break down.

Why Kalman Filter + Hidden Markov Model?
The key insight is that the system operates as a latent state machine: at any moment it is in one of a small number of discrete states (idle, transitioning, active, completing), and what we observe is a noisy function of that state. This framing motivates a two-stage approach: Kalman Filter — smooths the raw signal, handles sensor noise, and provides a principled estimate of the true instantaneous value with an associated uncertainty. Hidden Markov Model — takes the smoothed signal and infers the sequence of hidden states, including the timing of transitions and the most probable value estimate at peak. The talk explains the intuition behind both models without heavy mathematics, and then shows how to implement them in Python with filterpy (Kalman) and hmmlearn (HMM).

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
