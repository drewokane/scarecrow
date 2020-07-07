import numpy as np
from functools import partial
from itertools import repeat, chain
from more_itertools import ilen, nth

from scarecrow import core


def test_simple_sampler(seed):
    data = repeat(range(3), 3)
    ss = core.SimpleSampler(data, seed=seed)

    sample = ss.sample(5)

    assert ilen(sample) == 5


def test_weighted_sampler(seed):
    data = repeat(range(3), 5)
    ws = core.WeightedSampler(data, seed=seed)

    sample = list(ws.sample(5))

    assert ilen(sample) == 5
    assert nth(sample, 0) == tuple(range(3))

    
def test_weighted_sampler_weights_samples(seed):
    data = chain(repeat(range(3), 3), [[1, 1, 1]])
    ws = core.WeightedSampler(data, seed=seed)

    sample = list(ws.sample(10))
    r_subset = lambda a: np.equal(a, range(3)).all()
    one_subset = lambda a: np.equal(a, [1, 1, 1]).all()

    assert ilen(sample) == 10
    assert ilen(filter(r_subset, sample)) >= 6
    assert ilen(filter(one_subset, sample)) <= 4


def test_dimension_sampler(seed):
    data = chain(repeat(range(3), 3), [[1, 1, 1]])
    ds = core.DimensionSampler(data, seed=seed)

    sample = list(ds.sample(10))
    print(f'Sample:\n{sample}')

    assert ilen(sample) == 15
    assert [0, 1, 1] in sample
    assert [1, 1, 2] in sample
    assert [0, 1, 2] in sample
