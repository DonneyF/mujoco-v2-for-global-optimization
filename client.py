import xmlrpc.client
import numpy as np
import argparse

HOST = "127.0.0.1"  # Localhost
PORT = 11111       # Must match server

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--benchmark",
        help=f"Name of the benchmark. Options: {[]}",
        type=str,
        required=True
    )
    args = parser.parse_args()

    X = np.random.rand(1, 16)
    server = xmlrpc.client.ServerProxy(f"http://{HOST}:{PORT}")
    y = server.eval(args.benchmark, X.tolist()) # See server.py for function specification
    print(y)