from utils.rng import RNG


def test_rng_is_reproducible_for_same_seed():
    first = RNG(seed=17)
    second = RNG(seed=17)

    assert first.gauss(0.0, 1.0) == second.gauss(0.0, 1.0)
    assert first.uniform(-2.0, 3.0) == second.uniform(-2.0, 3.0)
    assert first.bernoulli(0.5) == second.bernoulli(0.5)


def test_bernoulli_probability_bounds():
    rng = RNG(seed=1)

    assert rng.bernoulli(0.0) is False
    assert rng.bernoulli(1.0) is True


def test_bernoulli_rejects_invalid_probability():
    rng = RNG(seed=1)

    try:
        rng.bernoulli(1.1)
    except ValueError:
        pass
    else:
        raise AssertionError("Probability above 1 should be rejected")