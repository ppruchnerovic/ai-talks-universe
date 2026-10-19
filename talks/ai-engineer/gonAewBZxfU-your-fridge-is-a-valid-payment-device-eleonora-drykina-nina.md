---
id: gonAewBZxfU
title: "Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket"
slug: your-fridge-is-a-valid-payment-device-eleonora-drykina-nina
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 25
published_at: 2026-10-14T12:00:07Z
video_id: gonAewBZxfU
url: https://www.youtube.com/watch?v=gonAewBZxfU
youtube_url: https://www.youtube.com/watch?v=gonAewBZxfU
tags: ["AIE NYC 2026", "Livestream Priority 15", "Online Talk"]
topics: ["Evals, observability & reliability", "Inference, serving & GPU infra", "RAG, retrieval & knowledge"]
transcript: true
---

# Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `25 min`

`#AIE NYC 2026` `#Livestream Priority 15` `#Online Talk`

[Watch the recording](https://www.youtube.com/watch?v=gonAewBZxfU) · [Conference site](https://www.ai.engineer/)

## Description

A question about payment rules can require one table row, an entire section or several rulebooks. Eleonora Drykina and Nina Žižakić describe a RAG assistant built for an anonymous Belgian payments client whose source material spans about 270 PDFs and 6,000 pages. Much of the answer bearing information sits in tables. Their indexing pipeline preserves section paths and chunk order so a larger passage can be reconstructed, and converts tables into CSV while retaining the relationship between headings and values. Combining dense retrieval with BM25 raises the reported retrieval hit rate from 92% to 97% on 63 questions; that measures retrieval, rather than complete answer correctness.

The serving agent can widen its search through four tools, moving from search results to sections, full documents and multiple rulebooks. Limits prevent an oversized rulebook from flooding the context, and the prompt asks the agent to reconsider whether another tool call adds evidence. A median answer takes 38 seconds, which makes the interface part of the engineering problem. Streaming Markdown separately from a completed source card avoids waiting for one large structured object before showing anything. The speakers also explain traces, citation checks and Promptfoo evaluations, including cases where an automated judge's apparent regression did not survive inspection of the source. Their early internal rollout reached 34 users and roughly 900 questions; external release remained planned. The practical lessons concern reconstructable evidence, bounded retrieval, visible progress and evaluation that can be challenged against the documents.

Speaker info:
Eleonora Drykina:
- https://www.linkedin.com/in/eleonora-drykina-3a1212233/
- https://www.elu.sh/

Nina Žižakić:
- https://www.linkedin.com/in/ninazizakic/

Timestamps:
00:00 - A payment rulebook assistant in production
2:42 - PDFs, tables and the source corpus
5:47 - Indexing and the system architecture
7:05 - Reconstructable sections without overlapping chunks
9:52 - Turning complex tables into usable evidence
11:42 - Dense retrieval, BM25 and reciprocal rank fusion
13:26 - Four tools that widen the search
14:22 - Context limits and tool call discipline
15:32 - Latency and streaming the answer
17:38 - Traces, citations and evaluation
20:37 - Early internal use and planned external release
22:46 - Lessons from the build

## Transcript

*2,810 words · source: supa (de, exact timings)*

**[0:01](https://www.youtube.com/watch?v=gonAewBZxfU&t=1s)** Hallo und willkommen zu unserem Vortrag mit dem Titel „Ihr Kühlschrank ist ein gültiges Zahlungsgerät: Unauffälliges RAG in der Produktion“ . Lassen Sie mich den Titel kurz erklären. Dies ist eine Seite aus den Regelwerken eines unserer Kunden. Es ist eines der vielen Dokumente, auf denen unser RAG-System basiert. Man würde eigentlich trockene Finanzdokumente erwarten, und genau das sind sie größtenteils auch. Aber es gibt dort auch einige amüsante Kleinigkeiten. Zum Beispiel diese Seite , die eine Liste von Geräten zeigt, mit denen man bezahlen kann. Es sind Dinge dabei, die man erwartet, wie Telefone oder Karten, aber auch kreativere wie Manschettenknöpfe, eine

**[0:50](https://www.youtube.com/watch?v=gonAewBZxfU&t=50s)** Handtasche, ein Kleidungsstück und sogar ein Kühlschrank. Ich fand es wirklich cool, so eine lustige Tatsache in Dokumenten zu finden, die man eigentlich als sehr langweilig einstufen würde. Stellen wir uns also kurz vor. Dies ist das einzige Foto, das wir von uns beiden zusammen haben. Wir tragen normalerweise keine XR-Headsets, aber an diesem Tag im Büro haben wir alle möglichen lustigen Gadgets ausprobiert. Ich bin Nina. Ich bin KI-Ingenieurin. Und ich bin Eleonora. Ich bin Produktingenieurin. Wir arbeiten bei In The Pocket, einem Studio für digitale Produkte mit Hauptsitz in Belgien. Wir

**[1:38](https://www.youtube.com/watch?v=gonAewBZxfU&t=98s)** unterstützen unsere Kunden bei der KI-Transformation und maßgeschneiderter Software. Heute sprechen wir über ein RAG-Projekt, das wir für einen unserer Kunden entwickelt haben, ein großes belgisches Fintech-Unternehmen. Der Name bleibt für diesen Vortrag anonym. Im Kern ist dies ein klassisches RAG-Problem. In diesem Vortrag möchten wir die technischen Entscheidungen aufzeigen, die wir treffen mussten, und tief eintauchen, wie wir das aufgebaut haben. Es ist der Vortrag, der für uns zu Beginn dieses Projekts sehr nützlich gewesen wäre. Was ist also das Problem, vor dem wir stehen? Unser

**[2:31](https://www.youtube.com/watch?v=gonAewBZxfU&t=151s)** Kunde betreibt das größte Zahlungssystem in Belgien, und alle Regeln dieses Systems sind in Regelwerken niedergeschrieben. Es handelt sich um etwa 270 PDFs. Oder insgesamt rund 6.000 Seiten. Ein Großteil der Informationen befindet sich in Tabellen. Es sind etwa 3.000 Tabellen. So strukturieren sie ihr Wissen. Viel wichtiges Wissen steckt direkt in den Tabellen selbst. Und die Regelwerke verweisen oft aufeinander. Ein Regelwerk verweist also auf ein anderes, und dieses dann auf ein weiteres usw. RAG für ein Finanzinstitut umzusetzen, bringt

**[3:21](https://www.youtube.com/watch?v=gonAewBZxfU&t=201s)** einige Herausforderungen mit sich. Die erste sind die Quellenangaben. Natürlich müssen die Antworten immer korrekt sein. Aber besonders im Finanzkontext ist das noch wichtiger. Jede Antwort muss daher den genauen Regelwerksabschnitt und die Seite zitieren. Damit die Leute sehen können , woher die Antwort stammt. Und der zweite Punkt ist das Grounding. Das zugrunde liegende LLM ist ein allgemeines Modell, es wurde also mit allgemeinem Wissen trainiert. Es weiß also viel, auch über andere Zahlungssysteme, wie sie funktionieren oder welche Gebühren sie haben. Wir

**[4:10](https://www.youtube.com/watch?v=gonAewBZxfU&t=250s)** mussten also entscheiden und sicherstellen, welches Wissen verwendet werden darf. Es ist zum Beispiel in Ordnung zu wissen, was eine Bank ist, das ergibt Sinn und ist nichts, was in den Regelwerken definiert werden muss. Aber was ein anderes Zahlungssystem berechnet oder wie es funktioniert, sollte nicht in einer Antwort auftauchen, es sei denn, es steht in den Regelwerken. So sieht also die Lösung aus, die wir gebaut haben. Es ist ein Chatbot. Man stellt eine Frage und er antwortet auf der Grundlage dieser Regelwerke. Wenn die Antwort in einer Tabelle steht, zeigt er diese auch an. Unter der Antwort befindet sich die Liste der Quellen, die er zur

**[4:57](https://www.youtube.com/watch?v=gonAewBZxfU&t=297s)** Erstellung der Antwort verwendet hat, einschließlich der Angabe des Abschnitts und des Teils des Regelwerks , damit der Benutzer das Regelwerk öffnen kann. In diesem Beispiel habe ich gefragt: "Kann ich mit meinem Kühlschrank bezahlen?" Ich habe eine Antwort erhalten und kann dann auch Folgefragen stellen. So sieht das ganze System aus. Es besteht aus zwei Teilen. Auf der linken Seite ist die Indizierung, das ist das, was wir quasi offline machen. Bei jeder neuen Version der Regelwerke wandeln wir die PDFs in Chunks um und speichern sie in der Vektordatenbank. Und auf der rechten Seite geht es um das Serving, also den Online-Teil für jede Frage, die ein Benutzer stellt. Der Agent durchsucht

**[5:47](https://www.youtube.com/watch?v=gonAewBZxfU&t=347s)** diese Vektordatenbank, und dann wird die Antwort an den Benutzer gestreamt. Ich werde über die Indizierung sprechen und Eleonora wird den Serving-Teil erläutern. Zum Thema Indizierung: Der Aufbau ist ziemlich einfach. Wir beginnen mit den PDFs, teilen sie in Chunks auf und fügen jedem Chunk Metadaten hinzu. Wir führen eine spezielle Verarbeitung für die Tabellen durch und generieren dann die Embeddings. Wir erstellen zwei Arten von Embeddings: ein dichtes und ein BM25. Ich gehe nun näher auf die ersten drei Schritte ein, und Eleonora wird später über die Embeddings

**[6:35](https://www.youtube.com/watch?v=gonAewBZxfU&t=395s)** sprechen. Der erste Schritt, das Aufteilen von PDFs in Chunks, funktioniert so: Wir extrahieren den Text von jeder Seite, teilen ihn in Absätze auf und packen diese in einen Chunk, bis er etwa 2.000 Zeichen erreicht. Dabei achten wir darauf, Tabellen nicht auf zwei Chunks aufzuteilen. Wir erkennen außerdem Abschnittsüberschriften mithilfe regulärer Ausdrücke, also Dinge wie Kapitel drei oder 4.2.1. Damit erhält jeder Chunk seinen entsprechenden Abschnittspfad. Dieser befindet sich beispielsweise in Kapitel vier,

**[7:23](https://www.youtube.com/watch?v=gonAewBZxfU&t=443s)** Abschnitt 4.2. Dieser Pfad wird verwendet, um ein Zitat hinzuzufügen, aber auch, um den gesamten Abschnitt abzurufen, wenn der Agent mehr Kontext benötigt. Das funktioniert alles so gut, weil wir die Chunks nicht überlappen lassen. Ein Abschnitt ist also einfach eine Sammlung von Chunks. Wenn man sie wieder in die richtige Reihenfolge bringt, entsprechen sie dem Ursprung. Für den zweiten Schritt fügen wir jedem Chunk Metadaten hinzu. In diesem Beispiel sehen wir den Text des Chunks aus diesem Kühlschrank-Regelbuch. Darunter befinden sich einige Metadatenfelder. Wir benötigen den Namen des Regelbuchs

**[8:15](https://www.youtube.com/watch?v=gonAewBZxfU&t=495s)** und die Seitenzahl, damit wir sie im Zitat oder in der Quellenkarte für den Benutzer anzeigen können. So kann der Benutzer das Ganze dann auch mit dem PDF verknüpfen. Wir verwenden die Abschnittspfade sowohl für die Zitate als auch, damit der Agent den gesamten Abschnitt auf einmal abrufen kann. Zusätzlich haben wir den Chunk-Index, der es dem Agenten ermöglicht, einen Abschnitt oder sogar ein ganzes Regelbuch wieder zusammenzusetzen. Der Agent verwendet Regelbuch-IDs, um eine Liste aller verfügbaren Regelbücher

**[9:03](https://www.youtube.com/watch?v=gonAewBZxfU&t=543s)** abzurufen. Zum Zeitpunkt der Indexierung erstellen wir für jedes Regelbuch mithilfe eines LLM eine Zusammenfassung, die dann an jeden Chunk des jeweiligen Regelbuchs angehängt wird. Und auf diese Weise weiß der Agent, aus welchem Dokument ein Abschnitt stammt. Und der Rest, ähm der restliche Teil der Metadaten, besteht aus Geschäftslogik-Feldern. Also, um welches Regelwerk es sich handelt, welche Regeln angewendet werden, ob es eine Tabelle enthält– das sind Dinge, die der Agent mit den Suchergebnissen erhält. Der dritte

**[9:53](https://www.youtube.com/watch?v=gonAewBZxfU&t=593s)** Schritt ist dann die Tabellenverarbeitung. Dieser ist wichtig, denn wie gesagt steckt sehr viel Wissen in den Tabellen. Das war uns anfangs nicht wirklich klar. Die ursprüngliche Verarbeitung bestand nur darin, den reinen Text aus dem PDF zu extrahieren, was die Tabellen nicht gut formatierte. In diesem Beispiel sehen Sie, dass das Feld für Inlandsgeschäfte über mehrere Zeilen reicht, grenzüberschreitende über zwei weitere und die Rückerstattung über beides. Wenn das nicht klar im Text abgebildet ist, kann der Agent falsche Informationen abrufen;

**[10:42](https://www.youtube.com/watch?v=gonAewBZxfU&t=642s)** besonders bei wichtigen Dingen wie Gebühren ist es entscheidend, die richtige Zeile und Spalte zu erfassen. Deshalb wandeln wir die Tabellen in ein CSV-Format um, indem wir diese Felder im Grunde duplizieren, und dann...So ruft der Agent sie ab, und wenn er das tut, erfasst er die korrekte Zeile. Genau die, die er benötigt. Das hat einen großen Unterschied für die Korrektheit der Antworten gemacht. Das war also alles zum Thema Indizierung. Wir haben jetzt etwa 4.000 Chunks. Und

**[11:34](https://www.youtube.com/watch?v=gonAewBZxfU&t=694s)** nun wird Eleonora über den Serving-Teil sprechen. Ja. Okay, der vorherige Teil hat den Index erstellt. In diesem Teil geht es nun darum, aus den 4.000 vorbereiteten Chunks die 10 richtigen zu finden. Der naheliegende Ansatz wäre, bei der Frage dichte Embeddings zu verwenden, jeden Chunk in einen Vektor umzuwandeln und die Distanz zu vergleichen. Das ist großartig für die Bedeutung, aber Regelwerk-Codes, Nachrichtennamen oder exakte Kennungen würden für ein Embedding wie Rauschen wirken, während sie für den Anfragenden oft die Essenz der Frage darstellen. Mit BM25 haben wir das Spiegelbild dazu. Exakte

**[12:24](https://www.youtube.com/watch?v=gonAewBZxfU&t=744s)** Begriffe funktionieren, Paraphrasen jedoch nicht. Also haben wir beides in einem Quadranten-Aufruf kombiniert und mittels Reciprocal Rank Fusion zusammengeführt. Dense Top 50, BM25 Top 50, zusammengeführt auf die Top 30 , neu gerankt nach Abschnittskohärenz und die Top 10 gehen an den Agenten. Das Schöne an RRF ist, dass wir die Ergebnisse dieser beiden Zweige nicht kalibrieren müssen. Bei der reinen Abrufevaluierung von 63 Fragen stieg die Trefferquote durch den hybriden Ansatz im Vergleich zu reinen Dense-Embeddings von 92 auf 97%, ohne eine einzige Frage zu verlieren, die bereits durch Dense-Embeddings gefunden werden konnte. Okay, wir haben also unsere 10 guten Chunks, aber nicht jede

**[13:16](https://www.youtube.com/watch?v=gonAewBZxfU&t=796s)** Frage passt in 10 Chunks. Manche sind verkettet. Ein Regelwerk verweist auf ein anderes, und die Antwort ist erst vollständig, wenn man diesem Verweis folgt. Manche benötigen mehr Kontext. Die Gebühren für diesen Transaktionstyp passen niemals in die Top 10 irgendeiner Suche. Anstatt einer festen Abruf-und-Generieren-Pipeline verfügt unser Agent daher über vier Werkzeuge. Von eng zu weit. Die Suche in Regelwerken steht immer an erster Stelle. Das sind die 10 Chunks, über die wir in der vorherigen Folie gesprochen haben. Wenn das nicht reicht , ruft „Regelwerk-Abschnitte abrufen “ den gesamten Abschnitt sortiert nach Abschnittspfad ab. Das ist genau der Ansatz, den Nina vorhin erwähnt hat. Das Speichern des Abschnittspfads. Und das „Herauszoomen“ hier

**[14:02](https://www.youtube.com/watch?v=gonAewBZxfU&t=842s)** bedeutet einfach, jeden Chunk mit diesem Pfad, sortiert nach Chunk-Index, abzurufen. Darüber steht „ Vollständiges Regelwerk abrufen“, was nur bei kleinen Regelwerken funktioniert. Und „Verfügbare Regelwerke auflisten“, falls der Agent wissen muss, was überhaupt existiert. Also, Sicherheitsvorkehrungen haben dies in der Praxis ermöglicht. Erstens: Wenn ein Regelwerk zu groß ist, etwa über 100.000 Token, weigert sich das Tool zum Abrufen des gesamten Regelwerks, den Inhalt in den Kontext zu laden, und gibt stattdessen die Liste der verfügbaren Abschnitte mit einer Warnung zurück, dass das Regelwerk zu lang ist. Zweitens: Wenn ein Abschnittsname nicht übereinstimmt,

**[14:50](https://www.youtube.com/watch?v=gonAewBZxfU&t=890s)** gibt es die verfügbaren Abschnitte zurück, damit der Agent es erneut versuchen kann, anstatt aufzugeben oder den Namen zu erfinden. Und zuletzt gibt es eine Disziplinierungsanweisung im Prompt. Da die meisten Fragen zwei bis vier Aufrufe erfordern, wird der Agent vor dem sechsten Aufruf angewiesen, sich selbst zu fragen, ob er wirklich etwas Neues abruft oder nur eine Suche umformuliert, die zuvor bereits gescheitert ist. Das kam daher, dass wir echte Traces beobachteten, bei denen der Agent immer wieder dieselbe Suche durchführte, in der Hoffnung, dass die Zahl irgendwann auftauchen würde. Der Preis für all das ist Latenz: ein Median von 38 Sekunden pro Antwort. Es ist nicht nur eine

**[15:41](https://www.youtube.com/watch?v=gonAewBZxfU&t=941s)** Chat-Antwort. Es ist eine kleine Rechercheaufgabe. Und wir setzen auf Streaming, damit sich 38 Sekunden so anfühlen, als würde tatsächlich etwas passieren und der Chat nicht einfach feststecken. Das bringt mich zur nächsten Folie. In unserer ersten Iteration wollten wir uns wirklich von der einfachen Chatbot-Benutzeroberfläche entfernen. Wir haben UI-Komponenten vorbereitet und sie als Pydantic-Modelle beschrieben, die dem Agenten zur Verfügung stehen, mit der Anweisung: „Hier sind die Komponenten, die du hast. Verwende sie in deiner Antwort zusammen mit dem Text.“ Zum Beispiel war eine Quellenkarte eine Komponente, ein Ereignis konnte eine Komponente sein, es gab einklappbare Checklisten-Komponenten und so weiter. Die Idee war eine Art KI-generierte Benutzeroberfläche, die lesbarer sein

**[16:28](https://www.youtube.com/watch?v=gonAewBZxfU&t=988s)** sollte als eine einfache Textwüste. Das Problem ist, dass man kein teilweises Pydantic-Objekt streamen kann. Es wird erst dann zu einem gültigen JSON, wenn das allerletzte Token eintrifft. Wie Sie hier sehen können, bedeutete das bei einem System , dessen Antworten 38 Sekunden dauern, 38 Sekunden Leere auf dem Bildschirm und dann erscheint alles auf einmal. Die Lösung, die die Benutzererfahrung gerettet hat, war die Aufteilung der Antwort in Teile. Der Agent streamt nun Markdown-Text Token für Token, und das Frontend formatiert es live, während es eintrifft. Die Quellenkarte ist dabei ein separates Element, eine echte UI-Komponente. Sie enthält keine Informationen, auf die man klicken müsste, bevor man die gesamte Antwort gelesen hat. Wir verlieren also nichts, wenn wir das Streaming der

**[17:16](https://www.youtube.com/watch?v=gonAewBZxfU&t=1036s)** vollständigen Antwort abwarten, bevor wir diese Komponente hinzufügen. Das gibt uns eine anklickbare Karte anstelle eines einfachen Links im Text, was für den Benutzer angenehmer ist. Aber sobald diese Antwort auf dem Bildschirm steht, stellt sich die Frage , was der Benutzer tatsächlich damit macht. Klickt er auf die Quelle, kopiert er die Antwort, führt er das Gespräch fort oder steigt er aus? Genau diese Benutzererfahrung wollen wir verfolgen, und das bringt uns zum Logging. Wir haben uns vorerst für die einfachste Logging-Lösung entschieden: Azure Table Storage. Wir protokollieren jede Frage, jeden Tool-Aufruf, jede Antwort, jedes Feedback–ob gut oder

**[18:04](https://www.youtube.com/watch?v=gonAewBZxfU&t=1084s)** schlecht–sowie Ereignisse wie das Klicken auf Quellen oder das Kopieren von Antworten, zusammen mit dem Gesprächsverlauf, der bewusst klein gehalten wird. Es sind lediglich die letzten 20 Nachrichten als Kontext. Für den aktuellen Stand unseres Produkts ist das ausreichend. Wenn das Produkt wächst, werden wir sehen, was wir dann tatsächlich benötigen. Und woher wissen wir, dass das alles tatsächlich funktioniert? Unsere Testfragen stammen aus echten Quellen, wir führten zwei Runden Nutzertests mit tatsächlichen Mitgliedern durch sowie Verhaltensrichtlinien, was unser KI-System tun darf und was nicht. Zum Beispiel: keine Ratschläge geben, neutral gegenüber Wettbewerbern bleiben und klar sagen, wenn etwas

**[18:52](https://www.youtube.com/watch?v=gonAewBZxfU&t=1132s)** nicht in den Regelwerken vorhanden ist. Wir haben etwa 86 End-to-End-Tests mit Promptfoo durchgeführt, mit einem vollständigen Agent-LLM als Prüfer anhand der Rubrik sowie einer Überprüfung, ob das richtige Quelldokument zitiert wurde, plus die reine Retrieval-Evaluierung von vorhin. Zwei Dinge, die wir dabei gelernt haben und die wir teilen möchten: Erstens haben LLM-Prüfungsbewertungen ein Grundrauschen, und man muss sie erneut durchführen, bevor man der Veränderung vertraut. Als wir beispielsweise unsere eigene Auswertung durchführten, ließen sich fünf von zwölf Abweichungen nicht reproduzieren . Und zweitens ist manchmal die Rubrik selbst der Fehler und nicht das Modell.

**[19:44](https://www.youtube.com/watch?v=gonAewBZxfU&t=1184s)** Wir hatten ein halluziniertes Datum, das der Prüfer ständig sanktionierte, und dann stellte sich heraus, dass dieses Datum tatsächlich ein echter Text im Regelwerk war. Ja. Kommen wir nun zur Nutzung. Wir haben diesen Regelwerk-Assistenten im Juni eingeführt. Anfangs wurde er nur für interne Benutzer unserer Kunden gestartet, und das Ziel ist, ihn bis Ende des Jahres auch deren externen Mitgliedern und Kunden zugänglich zu machen. Für den Moment haben wir also bereits einige Nutzungszahlen. Wir

**[20:37](https://www.youtube.com/watch?v=gonAewBZxfU&t=1237s)** haben bisher etwa 900 Fragen. Aufgeteilt auf mehr als 100 Konversationen, nutzen ihn etwa 34 Personen aktiv. Wir haben auch das „ Daumen hoch“-und „Daumen runter“- Feedback erfasst, aber die meisten Leute haben diese Funktion nach dem ersten Monat kaum noch genutzt. Wir haben auch Informationen darüber, wie oft Quellen angeklickt oder Antworten kopiert wurden. Das sind also die Zahlen. Wir nutzen auch KI für die Analysen. Auf der rechten Seite sehen wir, wie das LLM das interpretiert hat. Was wir sahen, war, dass wir im ersten

**[21:26](https://www.youtube.com/watch?v=gonAewBZxfU&t=1286s)** Monat, als wir die Leute baten ihn zu testen, etwas Red Teaming hatten. Die Leute versuchten also, den Assistenten zu manipulieren, vom Thema abzukommen oder Fangfragen zu stellen. Aber im dritten Monat waren mehr als 90%der Fragen tatsächlich echte Anfragen. Zweitens nutzen die Leute es für reale Fälle. Wir sahen, dass die Leute es nutzten, indem sie eine E-Mail ihres Kunden einfügten und um Hilfe bei der Beantwortung baten. Oder sie fügten eine echte Protokollnachricht, eine Tabelle usw. ein und entwarfen dann eine Antwort, die sie überprüfen lassen wollten. Und drittens haben wir, da wir nicht viel Feedback über „

**[22:16](https://www.youtube.com/watch?v=gonAewBZxfU&t=1336s)** Daumen hoch“ oder „Daumen runter“ bekamen, versucht, die Stimmung der Konversation durch die Analyse der Folgefragen zu interpretieren. Also, wenn Leute sich bedanken oder zum nächsten Thema übergehen, äh, würden wir das als positive Interaktion werten. Und wenn sie das Gleiche noch einmal fragen, dann war es wahrscheinlich eine negative Interaktion. Und das war das meiste, woraus wir gesehen haben, dass die meisten Konversationen gut verliefen. Also, um das Ganze zusammenzufassen: Was sind die wichtigsten Erkenntnisse aus diesem Projekt bisher? Auf der Dokumentenseite haben wir festgestellt,

**[23:06](https://www.youtube.com/watch?v=gonAewBZxfU&t=1386s)** dass es wichtig ist, die Struktur beizubehalten. Der Abschnittsteil ist also wichtig, sowohl für das Abrufen der Antwort als auch dafür, dass der Agent sozusagen aus dem Wissen herauszoomen kann. Wir haben auch gesehen, dass Tabellen eine spezielle Behandlung und eigene Verarbeitung benötigen. Auf der Agentenseite war es , wie erwähnt, wichtig, mehrere Zoom-Stufen anzubieten und zu entscheiden, wie viel Kontext benötigt wird. Generell war es sehr vorteilhaft, von einem Single-Shot-Aufruf an ein LLM auf einen agentenbasierten Abruf umzustellen. Wir haben gesehen, dass

**[23:57](https://www.youtube.com/watch?v=gonAewBZxfU&t=1437s)** die Evaluierungsergebnisse deutlich gestiegen sind. Aus der UX-Perspektive war das Streaming der Faktor, der es nutzbar und zu einem guten Werkzeug machte. Und wir fügen nur dann eine strukturierte Komponente hinzu, wenn dies von der UX gefordert wird. Und der letzte Punkt: Wir fanden es wichtig, frühzeitig mit echten Nutzern zu testen und diese Tests sowie Nutzerinterviews zu nutzen, um Prompts für Evaluierungen zu erstellen, mit denen wir das Produkt gestalten und entscheiden können, ob das, was wir

**[24:46](https://www.youtube.com/watch?v=gonAewBZxfU&t=1486s)** für eine Verbesserung halten, tatsächlich eine ist. Vielen Dank, dass Sie sich unseren Vortrag angehört haben. Danke.
