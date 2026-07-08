# Fragrance Analysis
An exploratory data analysis of 59,000 fragrances from the Parfumo database, uncovering trends in scent composition, niche vs. designer positioning, and what drives high ratings.

![Python](https://img.shields.io/badge/python-3.13.5-blue) ![License](https://img.shields.io/github/license/JennyIseev/fragrance-analysis)



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

  
## Project Overview
Etwas ausführlicher als der Pitch oben: 2-4 Sätze, was das Projekt ist und warum du es gemacht hast (Kontext: Portfolio-/Capstone-Projekt, StackFuel-Kurs o. Ä.)
Kurz die Motivation: warum Parfum/Duftindustrie als Thema interessant ist (z. B. Verbindung zu deinem Psychologie-Hintergrund – Wahrnehmung, Marketing vs. Zusammensetzung)
Link zum vollständigen Notebook (relativer Link zu deiner .ipynb-Datei im Repo, oder zu einem gerenderten Report, falls du z. B. nbviewer nutzt)

## Key Questions
3-5 konkrete Fragen als Bullet-Liste, die die Analyse beantwortet
Sollte direkt mit deiner Hauptrichtung übereinstimmen (z. B. "What accord combinations correlate with higher ratings?", "Do niche fragrances outperform designer fragrances in ratings?")
Keine Antworten hier – nur die Fragen, die Antworten kommen später bei "Key Findings"

## Project Structure
Ein Code-Block mit dem Ordnerbaum deines Repos (wie wir ihn vorhin skizziert haben: notebooks/, data/, reports/ etc.)
Optional 1 Satz pro Ordner, was drin liegt, falls nicht selbsterklärend

## Requirements & Installation
Python-Version (Verweis auf Badge)
Kurzer Schritt-für-Schritt-Block: Repo klonen, venv erstellen, pip install -r requirements.txt
Falls du eine requirements.txt noch nicht hast: unbedingt erstellen (pip freeze > requirements.txt), sonst kann niemand dein Projekt nachvollziehen

## Data
The dataset was originally compiled by Olga G. Miufana via web scraping of Parfumo.com (CC0 license) and was later republished on Kaggle as "Parfumo Perfume Database 59K Fragrances" by ibrahimqasimi.  

⚠️ The Kaggle link is now no longer reachable (404).   
To ensure reproducibility, the file is also included directly in this repository under `data/02_Parfumo_Perfumes.csv`.  

The dataset contains 59,325 entries for different fragrances from 1451 brands.   
The column structure is as following:

| Column | Description |
|--------|-------------|
| Number | Internal Parfumo ID |
| Name | Perfume name |
| Brand | Fragrance house |
| Release_Year | Year first released |
| Concentration | EdT, EdP, Parfum, Cologne, After Shave, etc. |
| Rating_Value | Average user rating |
| Rating_Count | Number of user ratings |
| Main_Accords | Dominant scent families |
| Top / Middle / Base_Notes | Notes smelled over time |
| Perfumers | Creator name(s) |
| URL | Link to the full entry |


## Exploratory Data Analysis
Kurzer Überblick über deine Vorgehensweise: Cleaning-Schritte (fehlende Werte, Duplikate, Datentyp-Fixes), welche Explorationsschritte du gemacht hast
Kein Ort für Ergebnisse/Charts – das kommt in "Key Findings". Hier geht's um den Prozess, nicht die Erkenntnisse

## Key Findings
3-4 Kernaussagen, jeweils mit einem Satz Erklärung + eingebettetem Chart (Screenshot als PNG aus deinem reports/figures/-Ordner)
Das ist der wichtigste Abschnitt fürs Scrollen – hier sollte jemand ohne Code zu lesen verstehen, was du rausgefunden hast

## Technologies & Libraries Used
Bullet-Liste: Python, pandas, seaborn, matplotlib, Jupyter, ggf. scipy/statsmodels falls du Korrelation/Regression rechnest
Kann kurz bleiben, das ist eher Referenz als Story

## Limitations & Next Steps
Was das Dataset/die Analyse nicht abdeckt (z. B. keine Verkaufszahlen, nur Ratings; Sampling-Bias bei Nischen-Parfums mit wenigen Reviews)
2-3 Ideen, was du als Nächstes machen würdest (z. B. Machine-Learning-Modell zur Rating-Vorhersage, Sentiment-Analyse aus Reviews-Text, falls vorhanden)
