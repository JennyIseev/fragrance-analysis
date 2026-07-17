import numpy as np
import pandas as pd
import pytest

from fragrance_analysis.ratings import cohens_d, weighted_rating


def test_equal_exposure_and_shrinkage_gives_50_50_blend():
    # v == m is the point where a brand's own average and the population
    # mean get equal weight, by construction of the formula.
    assert weighted_rating(v=100, R=9.0, C=7.5, m=100) == (9.0 + 7.5) / 2


def test_zero_exposure_returns_population_mean():
    assert weighted_rating(v=0, R=9.0, C=7.5, m=100) == 7.5


def test_very_high_exposure_approaches_own_average():
    wr = weighted_rating(v=1_000_000, R=9.0, C=7.5, m=100)
    assert wr == pytest.approx(9.0, abs=0.001)


def test_works_on_pandas_series():
    R = pd.Series([9.0, 6.0])
    v = pd.Series([100, 100])
    wr = weighted_rating(v=v, R=R, C=7.5, m=100)
    assert wr.tolist() == [8.25, 6.75]


def test_cohens_d_of_identical_samples_is_zero():
    a = np.array([7.0, 7.5, 8.0, 6.5])
    b = np.array([7.0, 7.5, 8.0, 6.5])
    assert cohens_d(a, b) == pytest.approx(0.0)


def test_cohens_d_hand_computable_case():
    # var([1,2,3], ddof=1) == var([4,5,6], ddof=1) == 1 -> pooled_sd == 1
    # mean diff = 2 - 5 = -3, so d = -3 / 1 = -3
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, 5.0, 6.0])
    assert cohens_d(a, b) == pytest.approx(-3.0)
