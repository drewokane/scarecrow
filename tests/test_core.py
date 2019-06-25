import numpy as np
from itertools import repeat

from scarecrow import core


def test_simple_sampler():
    data = repeat(range(3), 3)
    seed = 10101515
    ss = core.SimpleSampler(data, seed=seed)

    sample = ss.sample(5)

    assert len(list(sample)) == 5