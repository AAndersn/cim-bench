# Benchmark Report

**Generated from**: `results/pypowsybl_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Svedala

- **Mean time**: 423.2 ms
- **Min time**: 409.5 ms
- **Max time**: 439.2 ms
- **Std dev**: 13.7 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 1021.9
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

- **Mean time**: 332.3 μs
- **Min time**: 317.8 μs
- **Max time**: 3.0 ms
- **Std dev**: 86.0 μs
- **Rounds**: 1025

**Metrics**:
- Line Count: 90
- Query Type: get_lines
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Generators

- **Mean time**: 319.7 μs
- **Min time**: 304.1 μs
- **Max time**: 667.1 μs
- **Std dev**: 18.8 μs
- **Rounds**: 1604

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Loads

- **Mean time**: 225.7 μs
- **Min time**: 216.8 μs
- **Max time**: 404.9 μs
- **Std dev**: 11.7 μs
- **Rounds**: 1840

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e

### Pypowsybl Get Substations

- **Mean time**: 159.1 μs
- **Min time**: 148.7 μs
- **Max time**: 516.2 μs
- **Std dev**: 12.5 μs
- **Rounds**: 2361

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: pypowsybl
- Dataset: svedala
- Display Name: PyPowSyBl
- Color: #ff7f0e
