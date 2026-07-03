# Fragrance Analysis
An exploratory data analysis of 59,000 fragrances from the Parfumo database, uncovering trends in scent composition, niche vs. designer positioning, and what drives high ratings.

![Python](https://img.shields.io/badge/python-3.13.5-blue) ![License](https://img.shields.io/github/license/JennyIseev/fragrance-analysis)


## Table of Contents

## Table of Contents
- [Project Overview](#project-overview)
- [Key Questions](#key-questions)
- [Project Structure](#project-structure)
- [Requirements & Installation](#requirements--installation)
- [Data](#data)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Key Findings](#key-findings)
- [Technologies & Libraries Used](#technologies--libraries-used)
- [Limitations & Next Steps](#limitations--next-steps)

  
## 1. Project Overview (incl. link to full notebook/report)
Etwas ausführlicher als der Pitch oben: 2-4 Sätze, was das Projekt ist und warum du es gemacht hast (Kontext: Portfolio-/Capstone-Projekt, StackFuel-Kurs o. Ä.)
Kurz die Motivation: warum Parfum/Duftindustrie als Thema interessant ist (z. B. Verbindung zu deinem Psychologie-Hintergrund – Wahrnehmung, Marketing vs. Zusammensetzung)
Link zum vollständigen Notebook (relativer Link zu deiner .ipynb-Datei im Repo, oder zu einem gerenderten Report, falls du z. B. nbviewer nutzt)

## 2. Key Questions
3-5 konkrete Fragen als Bullet-Liste, die die Analyse beantwortet
Sollte direkt mit deiner Hauptrichtung übereinstimmen (z. B. "What accord combinations correlate with higher ratings?", "Do niche fragrances outperform designer fragrances in ratings?")
Keine Antworten hier – nur die Fragen, die Antworten kommen später bei "Key Findings"

## 3. Project Structure
Ein Code-Block mit dem Ordnerbaum deines Repos (wie wir ihn vorhin skizziert haben: notebooks/, data/, reports/ etc.)
Optional 1 Satz pro Ordner, was drin liegt, falls nicht selbsterklärend

## 4. Requirements & Installation
Python-Version (Verweis auf Badge)
Kurzer Schritt-für-Schritt-Block: Repo klonen, venv erstellen, pip install -r requirements.txt
Falls du eine requirements.txt noch nicht hast: unbedingt erstellen (pip freeze > requirements.txt), sonst kann niemand dein Projekt nachvollziehen

## 5. Data
This project uses the [Parfumo dataset](https://www.kaggle.com/datasets/ibrahimqasimi/parfumo-perfume-database-59k-fragrances) from Kaggle, 
licensed under CC0: Public Domain.

Anzahl Zeilen/Spalten, was für Felder enthalten sind (grober Überblick: Name, Brand, Accords, Rating, Release Year etc.)
Hinweis, falls die Rohdaten nicht im Repo liegen (meist zu groß für Git), sondern nur der Download-Link

## 6. Exploratory Data Analysis
Kurzer Überblick über deine Vorgehensweise: Cleaning-Schritte (fehlende Werte, Duplikate, Datentyp-Fixes), welche Explorationsschritte du gemacht hast
Kein Ort für Ergebnisse/Charts – das kommt in "Key Findings". Hier geht's um den Prozess, nicht die Erkenntnisse

## 7. Key Findings (with embedded screenshots/charts)
3-4 Kernaussagen, jeweils mit einem Satz Erklärung + eingebettetem Chart (Screenshot als PNG aus deinem reports/figures/-Ordner)
Das ist der wichtigste Abschnitt fürs Scrollen – hier sollte jemand ohne Code zu lesen verstehen, was du rausgefunden hast

## 8. Technologies & Libraries Used
Bullet-Liste: Python, pandas, seaborn, matplotlib, Jupyter, ggf. scipy/statsmodels falls du Korrelation/Regression rechnest
Kann kurz bleiben, das ist eher Referenz als Story

## 9. Limitations & Next Steps
Was das Dataset/die Analyse nicht abdeckt (z. B. keine Verkaufszahlen, nur Ratings; Sampling-Bias bei Nischen-Parfums mit wenigen Reviews)
2-3 Ideen, was du als Nächstes machen würdest (z. B. Machine-Learning-Modell zur Rating-Vorhersage, Sentiment-Analyse aus Reviews-Text, falls vorhanden)
