#!/usr/bin/env python3
"""Offline checks for the speaker extraction in sync_catalog.py — no network.

speakers_from_title() and speakers_from_description() are pure functions of
the text, and a mistake in them is the worst kind of silent: a brand or a job
title lands in the field weighted 4× in both rankers, under every talk that
carries it. Each case here is a shape the corpus actually has — the review of
2026-09-02 measured 1,057 talks under a bold-Unicode "Speakers:" heading and
~440 under "A & B, Company" titles — or a false positive it actually produced.

    cd tools && python3 test_speakers.py
"""

import sys

sys.path.insert(0, ".")
import sync_catalog as S

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


B = {"devoxx", "goto", "ignite", "microsoft"}
BOLD = "\U0001d5e6\U0001d5fd\U0001d5f2\U0001d5ee\U0001d5f8\U0001d5f2\U0001d5ff\U0001d600:"  # 𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:

# --- descriptions -------------------------------------------------------------
got = S.speakers_from_description(f"Learn how.\n\n{BOLD}\n * Scott Hanselman\n * Simon Willison\n\n\nSession Information:\nBRK123", B)
check("a bold-Unicode Speakers: heading with bullet lines yields every bullet",
      got == ["Scott Hanselman", "Simon Willison"], repr(got))
got = S.speakers_from_description("About the Speaker:\nAnnie Lee \nAnnie En-Shiun Lee is an Assistant Professor at OntarioTech.", B)
check("a bare line under the heading is one name and the bio below it is not",
      got == ["Annie Lee"], repr(got))
got = S.speakers_from_description("Speaker:\nJane Doe\nHead of Product\nAcme Corp", B)
check("job title and employer under a bare name are not a second speaker",
      got == ["Jane Doe"], repr(got))
got = S.speakers_from_description("Speakers: Ada Lovelace, Alan Turing & Grace Hopper", B)
check("names on the heading's own line still split on comma, & and 'and'",
      got == ["Ada Lovelace", "Alan Turing", "Grace Hopper"], repr(got))
got = S.speakers_from_description("\n\nSpeakers:\n * Joshua Corbett\n", B)
check("blank lines above the heading do not shift which line is read",
      got == ["Joshua Corbett"], repr(got))
check("a description with no heading yields nothing",
      S.speakers_from_description("A talk about agents. By the way, it is good.", B) == [])

# --- titles ---------------------------------------------------------------------
got = S.speakers_from_title("Agentic Evaluations at Scale — Nicholas Kang & Michael Aaron, Google DeepMind", B)
check("'A & B, Company' after a dash yields both people", got == ["Nicholas Kang", "Michael Aaron"], repr(got))
got = S.speakers_from_title("Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind", B)
check("'A and B, Company' yields both people", got == ["Chintan Parikh", "Weiyi Wang"], repr(got))
got = S.speakers_from_title("Scaling Up — Ada Lovelace and Hours of Speech", B)
check("a joined segment is rejected unless every part is a name", got == [], repr(got))
got = S.speakers_from_title("Scaling Up — Nick Ung and AI Agents", B)
check("… even when the first part is a real name", got == [], repr(got))
got = S.speakers_from_title("Agentic AI Patterns by Kevin Dubois and Mario Fusco", B)
check("'… by A and B' at the end of a title yields both", got == ["Kevin Dubois", "Mario Fusco"], repr(got))
got = S.speakers_from_title("Is AIOps the Future? Real Use Cases by Danilo Banjac, Iveri Prang", B)
check("'… by A, B' yields both", got == ["Danilo Banjac", "Iveri Prang"], repr(got))
got = S.speakers_from_title("Accessibility powered by AI by Ramona Domen", B)
check("the last 'by' wins and 'AI' is not a person", got == ["Ramona Domen"], repr(got))
check("'powered by Red Hat' style tails need a name shape, not a brand",
      S.speakers_from_title("Observability powered by Google Cloud", B) == [])
got = S.speakers_from_title("[VDBUH2026] Andrei Mihai & Bianca Bulbuc - How Agentic AI Empowers Creative Thinking", B)
check("a leading [TAG] is stripped before the segments are read", got == ["Andrei Mihai", "Bianca Bulbuc"], repr(got))
got = S.speakers_from_title("Green AI: Making ML Sustainable • Charles Humble • YOW! 2025", B)
check("a plain dotted title still yields its one name", got == ["Charles Humble"], repr(got))
check("a conference's own words are blocked", S.speakers_from_title("Keynote — Devoxx Belgium", B) == [])
check("a role is not a name", S.name_like("Chief Architect", B) is None and S.name_like("Assistant Professor", B) is None)

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: " + "; ".join(FAILS))
    sys.exit(1)
print("all checks passed")
