# Benchmark Report

**Generated from**: `results/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 443.4 ms
- **Min time**: 425.3 ms
- **Max time**: 460.3 ms
- **Std dev**: 13.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1251.5
- Buses: 105
- Lines: 97
- Ac Lines: 90
- Dangling Lines: 7
- Generators: 39
- Loads: 73
- Substations: 57
- Total Size Mb: 7.3
- Library: pypowsybl
- Dataset: svedala

### Pypowsybl Get Lines

- **Mean time**: 301.8 μs
- **Min time**: 267.1 μs
- **Max time**: 23.3 ms
- **Std dev**: 677.6 μs
- **Rounds**: 1157

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala

### Pypowsybl Get Generators

- **Mean time**: 270.8 μs
- **Min time**: 258.1 μs
- **Max time**: 725.8 μs
- **Std dev**: 20.6 μs
- **Rounds**: 1440

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala

### Pypowsybl Get Loads

- **Mean time**: 195.0 μs
- **Min time**: 180.7 μs
- **Max time**: 403.7 μs
- **Std dev**: 22.1 μs
- **Rounds**: 1963

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala

### Pypowsybl Get Substations

- **Mean time**: 125.0 μs
- **Min time**: 118.6 μs
- **Max time**: 325.0 μs
- **Std dev**: 11.1 μs
- **Rounds**: 3571

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
