# Benchmark Report

**Generated from**: `results/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.33 s
- **Min time**: 4.24 s
- **Max time**: 4.47 s
- **Std dev**: 106.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4559.9
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
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Lines

- **Mean time**: 35.6 ms
- **Min time**: 33.9 ms
- **Max time**: 39.3 ms
- **Std dev**: 1.5 ms
- **Rounds**: 28

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 2.7 ms
- **Min time**: 2.5 ms
- **Max time**: 4.9 ms
- **Std dev**: 322.0 μs
- **Rounds**: 151

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 22.3 ms
- **Min time**: 19.0 ms
- **Max time**: 32.5 ms
- **Std dev**: 3.6 ms
- **Rounds**: 45

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 7.2 ms
- **Min time**: 3.7 ms
- **Max time**: 64.4 ms
- **Std dev**: 5.6 ms
- **Rounds**: 131

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
