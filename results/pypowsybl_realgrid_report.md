# Benchmark Report

**Generated from**: `results/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.41 s
- **Min time**: 4.28 s
- **Max time**: 4.58 s
- **Std dev**: 119.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 5463.5
- Buses: 6051
- Lines: 7561
- Ac Lines: 7561
- Dangling Lines: 0
- Generators: 1347
- Loads: 6687
- Substations: 4791
- Dataset Size Mb: 86.5
- Library: pypowsybl
- Dataset: realgrid

### Pypowsybl Get Lines

- **Mean time**: 37.5 ms
- **Min time**: 33.7 ms
- **Max time**: 58.4 ms
- **Std dev**: 6.3 ms
- **Rounds**: 29

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid

### Pypowsybl Get Generators

- **Mean time**: 2.8 ms
- **Min time**: 2.3 ms
- **Max time**: 7.5 ms
- **Std dev**: 863.8 μs
- **Rounds**: 165

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid

### Pypowsybl Get Loads

- **Mean time**: 19.2 ms
- **Min time**: 17.8 ms
- **Max time**: 24.2 ms
- **Std dev**: 1.2 ms
- **Rounds**: 42

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid

### Pypowsybl Get Substations

- **Mean time**: 3.7 ms
- **Min time**: 2.8 ms
- **Max time**: 84.3 ms
- **Std dev**: 5.7 ms
- **Rounds**: 206

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
