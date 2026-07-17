import pandas as pd

from fragrance_analysis.concentration import classify_concentration


def test_product_form_takes_priority_over_scent_type():
    # "Cologne Mist" contains both a scent-type keyword ("cologne") and a
    # product-form keyword ("mist"); product form must win by rule ordering.
    assert classify_concentration("Cologne Mist") == "Mist/Spray"


def test_plain_scent_type_is_matched():
    assert classify_concentration("Eau de Parfum") == "Eau de Parfum"


def test_accented_input_is_matched_after_stripping():
    # "Colônia" only matches the "colonia" keyword once diacritics are stripped.
    assert classify_concentration("Colônia") == "Eau de Cologne"


def test_unmatched_value_falls_back_to_other():
    assert classify_concentration("Something Unrecognizable") == "Other"


def test_missing_value_passes_through():
    assert pd.isna(classify_concentration(None))
    assert pd.isna(classify_concentration(float("nan")))
