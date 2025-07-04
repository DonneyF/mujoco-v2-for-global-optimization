# Base image
FROM python:3.10-slim as build

# Set environment variables
ENV LANG=C.UTF-8 \
    LD_LIBRARY_PATH=/opt/mujoco210/bin:$LD_LIBRARY_PATH \
    MUJOCO_PY_MUJOCO_PATH=/opt/mujoco210 \
    BD_PATH=/app/BenchSuite

WORKDIR /opt
# Install dependencies
RUN apt update -y && apt install --no-install-recommends -y \
    gcc \
    build-essential \
    git \
    wget \
    swig \
    patchelf \
    libosmesa6-dev \
    libgl1-mesa-glx && \
    wget https://github.com/google-deepmind/mujoco/releases/download/2.1.0/mujoco210-linux-x86_64.tar.gz && \
    tar -xf mujoco210-linux-x86_64.tar.gz && \
    rm mujoco210-linux-x86_64.tar.gz && \
    git clone https://github.com/hvarfner/mujoco-py.git && \
    cd mujoco-py && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r requirements.dev.txt && \
    python setup.py build install && \
    cd /opt && \
    pip install gym==0.23.1 mujoco-py && \
    apt remove -y build-essential git wget patchelf libgl1-mesa-glx && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Copy BenchSuite from current directory to the container
COPY . /app/BenchSuite/
WORKDIR /app/BenchSuite

# Command to run the application
ENTRYPOINT ["python", "/app/BenchSuite/main.py"]

# Default CMD to append additional arguments
CMD []
