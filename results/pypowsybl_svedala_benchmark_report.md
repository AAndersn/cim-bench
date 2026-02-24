# Benchmark Report

**Generated from**: `results/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 477.4 ms
- **Min time**: 455.7 ms
- **Max time**: 501.6 ms
- **Std dev**: 21.2 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 944.1
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
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Lines

- **Mean time**: 404.5 μs
- **Min time**: 383.1 μs
- **Max time**: 4.4 ms
- **Std dev**: 134.7 μs
- **Rounds**: 929

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 383.5 μs
- **Min time**: 360.1 μs
- **Max time**: 640.0 μs
- **Std dev**: 32.0 μs
- **Rounds**: 1220

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 275.3 μs
- **Min time**: 259.2 μs
- **Max time**: 468.6 μs
- **Std dev**: 22.1 μs
- **Rounds**: 1646

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 198.6 μs
- **Min time**: 186.4 μs
- **Max time**: 370.8 μs
- **Std dev**: 17.7 μs
- **Rounds**: 2443

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
