# Benchmark Report

**Generated from**: `results/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.85 s
- **Min time**: 4.72 s
- **Max time**: 5.03 s
- **Std dev**: 126.3 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 4433.3
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

- **Mean time**: 35.3 ms
- **Min time**: 34.4 ms
- **Max time**: 36.2 ms
- **Std dev**: 570.3 μs
- **Rounds**: 28

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 3.1 ms
- **Min time**: 2.8 ms
- **Max time**: 18.0 ms
- **Std dev**: 1.1 ms
- **Rounds**: 193

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 18.6 ms
- **Min time**: 17.9 ms
- **Max time**: 22.1 ms
- **Std dev**: 637.4 μs
- **Rounds**: 43

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 4.8 ms
- **Min time**: 4.2 ms
- **Max time**: 13.9 ms
- **Std dev**: 1.0 ms
- **Rounds**: 106

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
- Library: pypowsybl
- Dataset: realgrid
- Display Name: PyPowSyBl
- Color: #ff7f0e
