# Mujoco v2 For Global Optimization
This project builds MuJoCo tasks as benchmarks for global optimization problems.
This is adapted from [BenchSuite](https://github.com/hvarfner/BenchSuite), stripping away the non-MuJoCo benchmarks and
other dependencies. We provide a binary executable as well as container images.

- Supports multiple benchmarks:
    - Swimmer (16D)
    - Humanoid (6392D)
    - Ant (888D)
    - Hopper (33D)
    - Walker (102D)
    - Half Cheetah (102D)

- Flexible input methods:
    - Single-point input (list of floats)
    - Multi-dimensional NumPy arrays as string representations

## The Tasks

These benchmarks are based off [MuJoCo](https://gymnasium.farama.org/environments/mujoco/) v2 Reinforcement Learning (RL)
tasks, where the problem is to learn a policy over time that achieves high reward. This project casts the
RL problem as a global optimization problem by modelling the policy learned during RL as a one-shot input.
For example, the Hopper input space `y` is 3 dimensions, with 11 observable dimensions `x`. A 33D matrix `A` of parameters
is used to define a policy. That is, at time `t` the input is `y[t+1] = A * x[t]`. The observation is adjusted
based on learned experts (i.e. https://github.com/berkeleydeeprlcourse/homework).

## Installation

See the `Dockerfile` for installation instructions. MuJoCo 2.1.0 is needed. This project uses the `mujoco-py` wrapper.

It is recommended to use the provided binary file (based on dockerc) or one of the containers for Docker/Singularity/Apptainer.

## Usage
The program is executed via the command line. Below are the general usage instructions.
### General Command Format
When using the binary, simply pass the options as if calling `main.py`

``` bash
python main.py --benchmark <BENCHMARK_NAME> [--x <X_VALUES>] [--X <X_ARRAY>]
```
### Parameters
- **`--benchmark` **_(Required)_: Specify the name of the Mujoco benchmark.
Options: `"swimmer"`, `"humanoid"`, `"ant"`, `"hopper"`, `"walker"`, `"cheetah"`.
- **`--x` **_(Optional)_: Provide space-separated numeric values as input (single point).
Example: `--x 1.0 2.0 3.0`
- **`--X` **_(Optional)_: Provide a NumPy array as a string representation (multi-dimensional input).
Example: `--X "[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]"`

_Note_: You can only specify one of `--x` or `--X`. Attempting to provide both will result in an error.

### Output
- For **single-point (`--x`)**, the output will be the result of the benchmark evaluation at the specified point. Example:
``` 
  -3.407524
```
- For **multi-dimensional input (`--X`)**, the output will be a list of benchmark results for all evaluated inputs. Example:
``` 
  [-3.407524, -2.309753]
```

## Docker

Docker image is available at `ghcr.io/donneyf/mujoco-v2-for-global-optimization:main` for `linux/amd64`.

## Singularity/Apptainer

Provided in the releases is a Singularity/Apptainer `.sif` file, which can be ran in the typical `apptainer run` fashion
similar to docker, or in instance mode:

```
apptainer instance start mujoco-v2-apptainer.sif mujoco --port 11111
```

A minimal client example is provided in `client.py` to interface with the server, which is exposed above,
communicated via XMLRPC on port 11111.