import abc
from enum import Enum

import numpy as np

class BenchmarkType(Enum):
    CONTINUOUS = 1
    BINARY = 2


class Benchmark(abc.ABC):

    def __init__(
            self,
            dim: int,
            lb: np.array,
            ub: np.array,
            type: BenchmarkType = BenchmarkType.CONTINUOUS,
    ):
        self.dim = dim
        self.lb = lb
        self.ub = ub
        self.type = type

    @abc.abstractmethod
    def __call__(self, x: np.array) -> np.array:
        raise NotImplementedError()
