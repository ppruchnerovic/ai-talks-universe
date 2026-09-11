# Data notice and licence

This repository holds two kinds of content under two different terms. The
code is under the MIT licence in [`LICENSE`](LICENSE). This file covers the
data.

## What is ours, and its licence

The parts of the corpus that were authored here are licensed under
**Creative Commons Attribution 4.0 International (CC BY 4.0)**:

- the conference registry, `conferences.json`, and its human-readable
  curation, `ai-conferences.md`;
- the topic taxonomy and the keyword rules behind it, and every topic
  assignment they produce;
- the speaker extraction rules and the `speakers` field they derive;
- the corpus layout: `data/talks.json`, `data/talks.csv`, the per-talk
  markdown under `talks/`, the search indexes under `data/tindex/` and
  `data/search-meta.json`, and the compilation, selection and arrangement of
  records in them.

You may share and adapt these for any purpose, including commercially, as
long as you give appropriate credit and indicate whether changes were made.
A link to this repository is sufficient credit. The full terms are at
<https://creativecommons.org/licenses/by/4.0/legalcode>; the SPDX identifier
is `CC-BY-4.0`.

## What is not ours

Titles, descriptions, tags, thumbnails, and above all **transcripts** are the
work of the speakers, the conferences and the channels that published them.
They were collected from public listings on YouTube and infoq.com, through
the routes documented in `docs/GUIDE.md`, and are reproduced here so that the
talks can be searched, quoted with a timestamp and linked back to the
recording. The project makes **no claim of ownership** over any of it and
grants no licence to it. CC BY 4.0 does not apply to that material.

If you reuse a transcript or a description beyond searching, quoting or
linking, the rights holder is the speaker or the conference, not this
project, and their terms apply. Every record carries a `url` pointing at the
original recording so that credit can go where it belongs.

## Takedown

If you are a speaker, a conference or a channel and want a talk removed from
the corpus, open an issue or use the contact in [`SECURITY.md`](SECURITY.md).
The talk will be removed from the corpus and added to the registry's exclusion
list so a refresh does not bring it back.
