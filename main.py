import argparse
import numpy as np
import ast
from mujoco.mujoco import MujocoAnt, MujocoHopper, MujocoWalker, MujocoHumanoid, MujocoSwimmer, MujocoHalfCheetah

BENCHMARKS = {
    "swimmer": MujocoSwimmer,
    "humanoid": MujocoHumanoid,
    "ant": MujocoAnt,
    "hopper": MujocoHopper,
    "walker": MujocoWalker,
    "cheetah": MujocoHalfCheetah,
}
def numpy_array_type(arg_string):
    """
    Custom type function for argparse to convert a string
    representation of a list into a numpy array.
    """
    try:
        # Safely evaluate the string as a Python literal (list, tuple, etc.)
        list_representation = ast.literal_eval(arg_string)

        # Convert the Python list/tuple to a NumPy array
        np_array = np.array(list_representation)
        return np_array
    except (ValueError, SyntaxError) as e:
        # Raise an ArgumentTypeError for argparse to handle
        raise argparse.ArgumentTypeError(
            f"Invalid numpy array format: '{arg_string}' "
            f"Expected a string representation of a list/tuple (e.g., '[[1,2],[3,4]]'). Error: {e}"
        )
    except Exception as e:
        raise argparse.ArgumentTypeError(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Mujoco-v2 Benchmark',
        description='Provides some benchmarks',
        epilog='Enjoy the program!'
    )
    parser.add_argument(
        "--benchmark",
        help=f"Name of the benchmark. Options: {list(BENCHMARKS.keys())}",
        type=str,
        required=True,
        choices=list(BENCHMARKS.keys()),
    )
    # Create a mutually exclusive group for -x and -X
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--x", "-x", help="A single point with dimensions seperated by spaces", type=float, nargs="+")
    group.add_argument(
        '--X', '-X',
        type=numpy_array_type,
        help='A NumPy array passed as a string representation of a Python list, e.g., "[[1, 2], [3, 4]]"'
    )
    args = parser.parse_args()


    bench = BENCHMARKS[args.benchmark]()

    if args.x is not None:
        x = np.array(args.x, dtype=np.float32)
        y = bench(x)
        print(y.tolist()[0])
    elif args.X is not None:
        x = np.array(args.X, dtype=np.float32)
        y = bench(x)
        print(y.tolist())
