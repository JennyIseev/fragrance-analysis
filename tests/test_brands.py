from fragrance_analysis.brands import classify_brand


def test_known_designer_house():
    assert classify_brand("Chanel") == "Designer"


def test_known_niche_house_not_on_either_list():
    assert classify_brand("Amouage") == "Niche"


def test_known_unclassified_brand():
    assert classify_brand("Avon") == "Unclassified"


def test_unknown_brand_defaults_to_niche():
    # Unlisted brands default to Niche, not Unclassified -- the notebook's own
    # np.select(..., default="Niche") makes this the intentional behavior.
    assert classify_brand("Some Totally Made Up Brand") == "Niche"
