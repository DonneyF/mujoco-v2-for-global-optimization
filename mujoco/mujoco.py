import warnings
from typing import Any

import numpy as np

from .benchmark import Benchmark
from .utils.mujoco import func_factories

class MujocoBenchmark(Benchmark):

    def __init__(self, dim: int, ub: np.ndarray, lb: np.ndarray, benchmark: Any):
        super().__init__(dim=dim, lb=lb, ub=ub)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.benchmark = benchmark.make_object()

    def __call__(
        self,
            x: np.ndarray
        ) -> np.ndarray:
            if x.ndim == 1:
                x = np.expand_dims(x, axis=0)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                y = self.benchmark(x)[0]
            return -np.array(y)


class MujocoSwimmer(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=16,
            ub=np.ones(16),
            lb=-1 * np.ones(16),
            benchmark=func_factories["swimmer"]
        )


class MujocoHumanoid(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=6392,
            ub=np.ones(6392),
            lb=-1 * np.ones(6392),
            benchmark=func_factories["humanoid"]
        )


class MujocoAnt(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=888,
            ub=np.ones(888),
            lb=-1 * np.ones(888),
            benchmark=func_factories["ant"]
        )


class MujocoHopper(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=33,
            ub=1.4 * np.ones(33),
            lb=-1.4 * np.ones(33),
            benchmark=func_factories["hopper"]
        )


class MujocoWalker(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=102,
            ub=0.9 * np.ones(102),
            lb=-1.8 * np.ones(102),
            benchmark=func_factories["walker_2d"]
        )


class MujocoHalfCheetah(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=102,
            ub=np.ones(102),
            lb=-1.0 * np.ones(102),
            benchmark=func_factories["half_cheetah"]
        )