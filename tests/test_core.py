import numpy as np
from itertools import repeat, chain

from scarecrow import core


def test_simple_sampler():
    data = repeat(range(3), 3)
    seed = 10101515
    ss = core.SimpleSampler(data, seed=seed)

    sample = ss.sample(5)

    assert len(list(sample)) == 5


def test_weighted_sampler():
    data = repeat(range(3), 5)
    seed = 20191101
    ws = core.WeightedSampler(data, seed=seed)

    sample = list(ws.sample(5))

    assert len(sample) == 5
    assert sample[0] == tuple(range(3))

    data = chain(repeat(range(3), 3), [[1, 1, 1]])
    ws = core.WeightedSampler(data, seed=seed)

    sample = list(ws.sample(10))

    assert len(sample) == 10
