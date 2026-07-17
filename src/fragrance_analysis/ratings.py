import numpy as np


def weighted_rating(v, R, C, m):
    """IMDB-style Bayesian shrinkage: WR = v/(v+m) * R + m/(v+m) * C."""
    return (v / (v + m)) * R + (m / (v + m)) * C


def cohens_d(a, b):
    """Pooled-SD effect size -- comparable across WR and weighted_avg despite their
    very different within-group variances (shrinkage compresses WR's spread)."""
    na, nb = len(a), len(b)
    va, vb = a.var(ddof=1), b.var(ddof=1)
    pooled_sd = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    return (a.mean() - b.mean()) / pooled_sd
