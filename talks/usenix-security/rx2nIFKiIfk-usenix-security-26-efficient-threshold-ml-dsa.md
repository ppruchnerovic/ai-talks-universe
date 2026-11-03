---
id: rx2nIFKiIfk
title: "USENIX Security '26 - Efficient Threshold ML-DSA"
slug: usenix-security-26-efficient-threshold-ml-dsa
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 15
published_at: 2026-10-28T01:28:36Z
video_id: rx2nIFKiIfk
url: https://www.youtube.com/watch?v=rx2nIFKiIfk
youtube_url: https://www.youtube.com/watch?v=rx2nIFKiIfk
tags: []
topics: ["Evals, observability & reliability", "Security, safety & red teaming"]
transcript: true
---

# USENIX Security '26 - Efficient Threshold ML-DSA

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=rx2nIFKiIfk) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '26 - Efficient Threshold ML-DSA

Sofía Celi, Brave Research and University of Bristol; Rafael del Pino and Thomas Espitau, PQShield; Guilhem Niot, PQShield and Univ Rennes, CNRS, IRISA; Thomas Prest, PQShield

Threshold signature schemes allow a group of users to jointly generate a digital signature, providing resilience against faults and enhancing decentralization. With the advent of post-quantum cryptography, lattice-based threshold signatures have gained attention as viable alternatives. Nevertheless, existing constructions frequently encounter challenges related to scalability, robustness, or compatibility with standardized schemes, particularly with the NIST-selected and standardised Module-Lattice-based Digital Signature Algorithm (ML-DSA) algorithm.
In this work, we present the first threshold signature scheme that is fully compatible with ML-DSA, supporting secure and efficient signing among up to six parties. Our construction leverages advanced short secret sharing techniques and integrates optimized rejection sampling to achieve a favourable balance between communication efficiency and correctness in distributed environments. We implement our construction in Go and evaluate its performance across local, LAN, and WAN network settings. Our benchmarks demonstrate that our threshold ML-DSA scheme is not only practically deployable but also well-suited for real-world applications, including multi-device cryptocurrency wallets, threshold-based TLS authentication, and for Tor's directory authorities.

View the full USENIX Security '26 program at https://www.usenix.org/conference/usenixsecurity26/technical-sessions

## Transcript

*2,129 words · source: supa (en, exact timings)*

**[0:19](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=19s)** Hi and thank you for uh listening to this recording. Uh today I will present our work that was uh published at USNIX security 2026 on uh distributing the recent uh NI standard for postquantum cryptography MLDDSA and this is a joint work with researchers at Picushield and at great research. First I want to start with a little bit of background and what are social signatures and the idea is that when you store a secret key uh centrally becomes a single point of failure both for uh security and availability say if that device breaks or is hacked and social signatures propose a solution for this by sharing your key among several devices such that you can tolerate

**[1:07](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=67s)** either the loss of some devices or uh some devices devices becoming compromised. So say even if the key the the the partial key of some devices is are leaked then uh it still does not allow to perform the uh signing algorithm uh on its own and it is in particular very interesting uh to design threshold schemes in the postquantum setting for the new uh standards. So uh here are the three of them for assigning MLGSA, FNGSA and SLHDSA. However, it appears quite difficult for the two uh last FNDSA, SLHDSA and we'll however show in this presentation that we have efficient uh

**[1:55](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=115s)** solutions for MLGSA and this is what we call MRI. So mysterial is signing special signing protocol that produces uh signatures that are compatible with MLDDSA verifiers. It's uh signing protocol that execute inferior rounds of interaction between the signers. Uh also it supports distributed key generation if you want to go even further in this distribution and it is pretty efficient uh for a few parties say up to six or maybe even 10 um with a communication that scales uh that ranges between 20 kilobytes and uh 1 megabyte. Now uh moving to the core of this talk uh with how we actually perform this uh

**[2:43](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=163s)** distributed signing. Um and I want to start this by recalling how MLDDSA works. Starting first with the key generation and the idea here is that you will have um a linear combination of a short secret SK together with an error E. So both of these have a short norm and a is multiplied by a uniform matrix modular q and under the mld assumption um vk will appear uh uniformly distributed and in particular uh the second assumption will be that it will be hard to recover a short secret uh given only this uh uniform key vk and then the idea of signing nmlddsa is

**[3:33](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=213s)** to basically prove the knowledge of the short secret SK [snorts] and similar to what was done with Schnore um it's a fat shame transform apply to a protocol proving the knowledge of SK and it works in three steps uh first we'll have the sampling of a short vector R together with the computation of a commitment W which is A * R then we compute the challenge C uh which is the hash function a hash of W and the message to be signed. And finally we compute a fat response Z which is the challenge time the secret plus R. And the idea here is that only one that actually knows uh the secret key within the the public key

**[4:21](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=261s)** would be able to compute uh this response. And finally for verification MLDDSA one just checks that uh the commitment that is passed in the signature W can be recovered from Z and BK and that Z is short. So at this point actually the scheme would be insecure if we stayed there. Uh but it's uh because uh the distribution of Z um since R is short would heavily depend on the the secret key SK. And so by observing D you would eventually even learn SK. But this is fixed in MLDDSA by performing rejection sampling here. Uh so we just reject Z's whenever they fall out of some sudden safe space. And then

**[5:10](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=310s)** it means that when you observe uh the uh signing uh the the signatures with Z you uh only observe some distribution that is actually independent of SK and and the the scheme is safe again. Now thinking about uh distributing this scheme actually most of the operations are linear and like pretty uh threshold friendly. So there is first the hash that you could think is hard to distribute but actually it's fine because you can kind of uh externalize this computation you can perform in publicly. So this is fine but the two main challenges that appear are in fact the sampling of the short randomness R and the rejection sampling here. So first the first the intuition is uh like say if you have to sample something

**[5:59](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=359s)** uniform you could just ask each party to sample something uniform sum it together uh and then you're good you have again a uniform sample and um you have a solution. However, here if you sample say short uh vectors ra I locally you sum them you don't have anything you don't have something um as short or equally distributed to before so it can be problematic and for the rejection sampling uh we need to perform a comparison over a secret vector u which is something that involves uh very advanced uh distributed computation techniques and in particular uh quite costly and less efficient. So these are things that we want to tackle in a simple and efficient manner in our scheme.

**[6:50](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=410s)** So let's start with uh an idea to how for how to perform these two operations and actually for the sampling of the runners R we'll do uh the the kind of naive ID of sampling some short uh vectors R I in each party and then aggregating them and the issue here that may occur is that then your aggregated R here is bigger than before and also may be biased by some malicious parties. Uh but we will show uh we show in our paper that uh we can do this safely uh thanks to the lattice setting. Uh yeah, basically um if one parties u bias biases are I they're only um like causing trouble for themselves.

**[7:42](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=462s)** And for the rejection sampling uh since now we have locally nicely sample R I will also just do u local rejection sampling on uh each party's uh partial secret. So each party will uh just basically perform the uh MLDDSA rejection sampling technique on uh its own secret and then we aggregate all of these responses uh together to obtain the final signature and of course the signature is uh you able to build it only if all the parties accept uh their rejection sampling at once. So for this to work, we actually need the partial secrets of uh each of the party uh to be short. So we just need to

**[8:32](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=512s)** have one skr part per party uh such that they sum to sk and they all have a small norm and then we can input it uh into the rejection sampling and this is just for the security of the the rejection sampling technique and also just to achieve a decent uh success probability. Now to instantiate this we can actually do it using a known technique uh a known secret sharing uh in the MPC community which is replicated secret sharing where we just adapt it to produce short shares instead of uniform shares and uh the idea of this sharing is to sample one share for each possible set of honest parties among the uh the set of signers. So here we have a loop of over all the

**[9:23](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=563s)** sets I of n minus t + one parties. Then we sample one share of one sk and one error ei for each of these sets. We distribute them for the selected set and then we define vk to be the sum of uh uh this uh partial vki obtained from these shares. And first when we select SKI EI to be short then we have again u short uh shares uh and also we have nice uh properties for this sharing. First if you leak uh the shares of up to t minus one parties then at least one of these uh secrets remain secure. So you preserve like the threshold uh security and uh also if you aggregate if you want

**[10:14](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=614s)** to sign with t parties they can collaborate to reconstruct the full secret. So it just means that you have a pool of many shares and you just uh select for each party a subset of this uh you aggregate them. they have one partial secret. Uh and then um when they these two parties come together uh they sum their partial secrets they uh um obtain SK which is basically just the condition that we had in the previous slide and this shares these partial secrets is short thanks to the shortness of sky. Now we can actually come up with a protocol to implement this ids and we'll start first with the sampling of the short ra. So actually for technical reasons we also need to uh introduce uh ei prime which has similar word uh

**[11:06](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=666s)** similar uh role. Uh it's just basically that we don't want to rely on rounding here as opposed to the mldsa signing. Uh so yeah first we compute RA I EI prime then we derive WI from these two and actually proceed in two steps here we first reveal a hash of WI then broadcast this is because we don't want an adversary to first observe the others uh WI and then choose their own for security reasons uh and in the third round um we actually compute the fia response so we aggregate the WIS then compute the challenge and finally compute the response ZI and do the rejection sampling in order to make sure that it still fits within an MLDDSA signature at the end. We uh just when we combine the ZIS verify that uh it's uh accepted by

**[11:57](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=717s)** the MLDDSA verification. So at this point actually the scheme would not be that efficient and the issue is that when T is assigned the probability of success scales with P to the T. So we have an exponential degradation. uh but we can actually solve this by uh kind of optimizing the rejection sampling within MLDDSA. This rejection sampling relies on hyper cubes. So it just means that R is sampled from some uh cube of a fixed infinite norm. Uh then Z is just the shift of this and cube in the middle is selected. And instead in our work we rely on hyperbols which again sample R from a hyperbol shift it then we select smaller hyperbol but the nice thing is that it's actually more compact it produces smaller

**[12:45](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=765s)** signatures than uh MLDDSA so it kind of compensates for uh this effect that we have of doing T rejection samplings. The drawback is that the implementation is a bit more complex. Now about performance. Um so we have um here uh the bandwidth that is required to produce a valid signatures for uh several uh parties two to six and it scales because like eventually the the success property uh degrades a bit but it remains under 500 kilobytes here. Uh so it's still pretty efficient. Also for local computation it scales up to 20 milliseconds. also quite efficient. And even if you move to the one uh setting, we have 30 milliseconds if you sign from

**[13:33](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=813s)** not too far devices and up to 600 or even 700 milliseconds if you do intercontinental and it basically corresponds to the network latency multiplied by the number of rounds of uh the protocol. Now also comparing to other techniques to um distribute MLDDSA that appeared um concurrently we have first from MPC and FHE uh so our work is actually the most efficient communication and computation wise but it's limited in terms of KBT whereas these two works can support more parties but have much lower efficiency and last I also wanted to mention that um NIST initiated a process for evaluating uh threshold protocols uh and it's actually um the call is actually going to be this year and we

**[14:21](https://www.youtube.com/watch?v=rx2nIFKiIfk&t=861s)** plan to submit misreil as a proposal and so we hope that it's going to get more traction and thank you for listening and if you want to have more information about our work I will invite you to uh check our uh work online uh our full version is available on print thank
