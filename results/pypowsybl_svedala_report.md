# Benchmark Report

**Generated from**: `results/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Network

- **Mean time**: 474.4 ms
- **Min time**: 464.6 ms
- **Max time**: 491.7 ms
- **Std dev**: 15.0 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 887.4
- Total Size Mb: 7.3
- Buses: 105
- Lines: 97
- Ac Lines: 90
- Dangling Lines: 7
- Generators: 39
- Loads: 73
- Substations: 57

### Pypowsybl Get Lines

- **Mean time**: 318.4 μs
- **Min time**: 259.1 μs
- **Max time**: 1.2 ms
- **Std dev**: 90.6 μs
- **Rounds**: 1043

**Metrics**:
- Line Count: 90
- Query Type: get_lines

### Pypowsybl Get Generators

- **Mean time**: 293.7 μs
- **Min time**: 262.4 μs
- **Max time**: 501.7 μs
- **Std dev**: 36.5 μs
- **Rounds**: 994

**Metrics**:
- Generator Count: 39
- Query Type: get_generators

### Pypowsybl Get Loads

- **Mean time**: 212.5 μs
- **Min time**: 196.0 μs
- **Max time**: 367.8 μs
- **Std dev**: 15.3 μs
- **Rounds**: 1270

**Metrics**:
- Load Count: 73
- Query Type: get_loads

### Pypowsybl Get Substations

- **Mean time**: 129.9 μs
- **Min time**: 117.7 μs
- **Max time**: 312.6 μs
- **Std dev**: 16.5 μs
- **Rounds**: 1538

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
