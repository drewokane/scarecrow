import random
from collections import defaultdict
from copy import copy
from more_itertools import ilen, nth, SequenceView
from typing import Union, Sequence, Optional, Dict


class BaseSampler(object):

    def __init__(
        self,
        data: Sequence[Sequence[Union[str, int, float]]],
        seed: Optional[int] = None,
    ) -> None:
        """
        Initializes the class with the data to sample.

        Paramters:
        -----------
        data: Iterable[Iterable[Union]]
        """
        self.data = list(data)
        self.len = ilen(self.data)
        self.rng = random.Random(x=seed)
    
    def sample(self, n: int):
        return NotImplementedError('Sample method needs to be implemented!')


class SimpleSampler(BaseSampler):

    def sample(self, n: int):
        for _ in range(n):
            i = self.rng.randrange(self.len)
            yield nth(self.data, i)


class WeightedSampler(BaseSampler):

    def __init__(
            self,
            data: Sequence[Sequence[Union[str, int, float]]],
            seed: Optional[int] = None,
    ) -> None:
        super().__init__(data, seed=seed)
        self.hist = self._get_data_hist(self.data)

    def _make_hashable(self, thing):
        return tuple(thing)

    def _get_data_hist(
            self,
            data: Sequence[Sequence[Union[str, int, float]]]
    ) -> Dict[int, Sequence[Union[str, int, float]]]:
        d = defaultdict(int)

        for i in data:
            key = self._make_hashable(i)
            d[key] += 1

        return d

    def sample(self, n: int):
        keys = list(self.hist.keys())
        freqs = list(self.hist.values())
        for i in self.rng.choices(keys, weights=freqs, k=n):
            yield i


class DimensionSampler(BaseSampler):

    def __init__(
        self,
        data: Sequence[Sequence[Union[str, int, float]]],
        seed: Optional[int] = None,
        ) -> None:
        super().__init__(data, seed=seed)
        self.dims = self._make_dimensions()

    
    def _make_dimensions(self):
        zipped = zip(*self.data)
        return [col for col in zipped]
    
    def sample(self, n: int):
        for _ in range(n):
            yield [self.rng.choice(d) for d in self.dims]
