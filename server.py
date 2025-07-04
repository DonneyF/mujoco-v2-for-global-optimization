import argparse
import numpy as np
import ast
import xmlrpc.server
from mujoco.mujoco import MujocoAnt, MujocoHopper, MujocoWalker, MujocoHumanoid, MujocoSwimmer, MujocoHalfCheetah

BENCHMARKS = {
    "swimmer": MujocoSwimmer,
    "humanoid": MujocoHumanoid,
    "ant": MujocoAnt,
    "hopper": MujocoHopper,
    "walker": MujocoWalker,
    "cheetah": MujocoHalfCheetah,
}

class BenchServer:
    def eval(self, benchmark: str, X: list):
        bench = BENCHMARKS[benchmark]()
        y = bench(np.array(X, dtype=np.float32))
        return y.tolist()

    def ping(self):
        return "PONG"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Mujoco-v2 Benchmark',
        description='Provides some benchmarks',
        epilog='Enjoy the program!'
    )
    parser.add_argument("--port", "-p", help="Port", type=int, default=9000)
    args = parser.parse_args()

    server = xmlrpc.server.SimpleXMLRPCServer(
        ("localhost", args.port), logRequests=False
    )
    server.register_instance(BenchServer())
    server.serve_forever()