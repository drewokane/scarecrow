import random
from more_itertools import ilen, nth
from typing import Union, Sequence


class SimpleSampler(object):

    def __init__(
        self, 
        data: Sequence[Sequence[Union[str, int, float]]],
        seed: Union[int, None] = None
        ) -> Sequence[Sequence[Union[str, int, float]]]:
        """
        Initializes the class with the data to sample.

        Paramters:
        -----------
        data: Iterable[Iterable[Union]]
        """
        self.data = data
        self.len = ilen(data)
        self.rng = random.Random(x=seed)

    def sample(self, n: int):
        for _ in range(n):
            i = self.rng.randrange(self.len)
            yield nth(self.data, i)