import re
import unicodedata

import pandas as pd


def strip_accents(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))

# Checked in order: product-form categories first, then scent-concentration types,
# so e.g. "Cologne Mist" lands in Mist/Spray rather than Eau de Cologne.
CONCENTRATION_RULES = [
    ("After Shave",       r"after.?shav|aftershav|rasage|barba|rasierwasser"),
    ("Oil",               r"\boil\b|huile|olio"),
    ("Solid",             r"solid|stick|compact|cushion|\bgel\b|cream|creme|crema|concret"),
    ("Mist/Spray",        r"mist|spray|brume|spritz|splash|bodyspray|body ?water|tonic|tonique|voile"),
    ("Eau de Parfum",     r"eau de parfum|eau de perfum|elixir de parfum|esprit de parfum"),
    ("Eau de Toilette",   r"eau de toilette|toilet water"),
    ("Eau de Cologne",    r"eau de cologne|\bcologne\b|colonia|acqua di colonia"),
    ("Extrait/Parfum",    r"\bparfum\b|extrait|extract|pure perfum|estratto|concentrat|profumo|essence|essenza|esencia|absolu|attar"),
    ("Eau Fraiche",       r"eau fraiche|fraicheur"),
    ("Perfume/Fragrance", r"perfume|fragrance|parfum|scent|senteur"),
]
COMPILED_RULES = [(label, re.compile(pattern)) for label, pattern in CONCENTRATION_RULES]

def classify_concentration(value):
    if pd.isna(value):
        return value
    normalized = strip_accents(value.lower())
    for label, pattern in COMPILED_RULES:
        if pattern.search(normalized):
            return label
    return "Other"
