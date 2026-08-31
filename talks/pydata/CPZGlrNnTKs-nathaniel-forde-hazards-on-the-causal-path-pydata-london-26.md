---
id: CPZGlrNnTKs
title: "Nathaniel Forde - Hazards on the Causal Path | Pydata London 26"
slug: nathaniel-forde-hazards-on-the-causal-path-pydata-london-26
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Nathaniel Forde"]
channel: "PyData"
duration_min: 21
published_at: 2026-06-15T15:51:49Z
video_id: CPZGlrNnTKs
youtube_url: https://www.youtube.com/watch?v=CPZGlrNnTKs
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Nathaniel Forde - Hazards on the Causal Path | Pydata London 26

**Nathaniel Forde**

`PyData` · `PyData` · `2026` · `21 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=CPZGlrNnTKs) · [Conference site](https://pydata.org/)

## Description

Nathaniel Forde - Hazards on the Causal Path: Bayesian Time-Varying Survival Analysis with PyMC

Dynamic Path Analysis (DPA) extends survival analysis with a causal, time-varying perspective. This allows causal effects to be decomposed into direct and indirect pathways that evolve over time. The perspective is particularly valuable when interventions (exercise) act through mediators (weight loss) whose influence changes dynamically in time, because we get to distil when each driver of our survival probabilities are active and whether their combined effects are harmful or positive.

Despite its conceptual appeal, DPA remains niche, with existing implementations limited to frequentist R packages and no Bayesian or Python-native alternatives. In this talk, I present a Bayesian, generative implementation of Dynamic Path Analysis using PyMC. By discretising time and modelling cumulative hazard effects with smooth spline priors, we obtain interpretable time-varying causal effects with coherent uncertainty quantification. I benchmark the approach against canonical dpasurv examples and discuss why DPA focuses on hazards rather than survival curves.

This talk is aimed at Python users interested in survival analysis, causal inference, and Bayesian modelling.

Survival analysis is often used to answer when an event occurs, but in many real-world settings we also care about how and through which mechanisms interventions exert their effects over time. Dynamic Path Analysis (DPA), introduced by Aalen and colleagues, addresses this by decomposing time-varying effects on the hazard into direct and mediated causal pathways, allowing these relationships to evolve dynamically.

In this talk, I present a Bayesian, generative reinterpretation of Dynamic Path Analysis implemented in PyMC. The model discretises time into intervals and represents cumulative hazard effects using smooth spline-based priors, enabling stable estimation of time-varying direct and indirect effects with full posterior uncertainty. I show how this approach recovers the qualitative behaviour of canonical dpasurv examples while extending them to a fully probabilistic framework.

The emphasis is on the causal decomposition of hazards, clarifying why DPA is well suited to reasoning about evolving mediation structures and intervention planning. The talk highlights how generative Bayesian models make these ideas more flexible, interpretable, and extensible within the Python ecosystem. We end with practical recipes for using g-computation to derive non-parametric estimates of direct, indirect and survival-curve-differences from the fitted DPA model.

Target audience: data scientists and researchers with some familiarity with survival analysis or Bayesian modelling.

Takeaway: attendees will understand when and why to use dynamic causal hazard models, and how to implement them in practice using PyMC.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
