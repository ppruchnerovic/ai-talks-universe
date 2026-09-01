---
id: XKnubeU14Vg
title: "USENIX Security '25- A Crack in the Bark: Leveraging Public Knowledge to Remove Tree-Ring Watermarks"
slug: usenix-security-25-a-crack-in-the-bark-leveraging-public
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 17
published_at: 2025-10-30T20:03:05Z
video_id: XKnubeU14Vg
url: https://www.youtube.com/watch?v=XKnubeU14Vg
youtube_url: https://www.youtube.com/watch?v=XKnubeU14Vg
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25- A Crack in the Bark: Leveraging Public Knowledge to Remove Tree-Ring Watermarks

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `17 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=XKnubeU14Vg) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '25 - A Crack in the Bark: Leveraging Public Knowledge to Remove Tree-Ring Watermarks

Junhua Lin and Marc Juarez, University of Edinburgh

We present a novel attack specifically designed against Tree-Ring, a watermarking technique for diffusion models known for its high imperceptibility and robustness against removal attacks. Unlike previous removal attacks, which rely on strong assumptions about attacker capabilities, our attack only requires access to the variational autoencoder that was used to train the target diffusion model, a component that is often publicly available. By leveraging this variational autoencoder, the attacker can approximate the model's intermediate latent space, enabling more effective surrogate-based attacks. Our evaluation shows that this approach leads to a dramatic reduction in the AUC of Tree-Ring detector's ROC and PR curves, decreasing from 0.993 to 0.153 and from 0.994 to 0.385, respectively, while maintaining high image quality. Notably, our attacks outperform existing methods that assume full access to the diffusion model. These findings highlight the risk of reusing public autoencoders to train diffusion models—a threat not considered by current industry practices. Furthermore, the results suggest that the Tree-Ring detector's precision, a metric that has been overlooked by previous evaluations, falls short of the requirements for real-world deployment.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
