# Benchmark Report

**Generated from**: `results/pypowsybl_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Network

- **Mean time**: 437.8 ms
- **Min time**: 429.8 ms
- **Max time**: 450.0 ms
- **Std dev**: 10.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 923.6
- Total Size Mb: 7.3
- Buses: 105
- Lines: 90
- Generators: 39
- Loads: 73
- Substations: 57

### Pypowsybl Get Lines

- **Mean time**: 288.7 μs
- **Min time**: 261.7 μs
- **Max time**: 527.5 μs
- **Std dev**: 41.8 μs
- **Rounds**: 1209

**Metrics**:
- Line Count: 90
- Query Type: get_lines

### Pypowsybl Get Generators

- **Mean time**: 290.2 μs
- **Min time**: 246.6 μs
- **Max time**: 635.3 μs
- **Std dev**: 62.3 μs
- **Rounds**: 1158

**Metrics**:
- Generator Count: 39
- Query Type: get_generators

### Pypowsybl Get Buses

- **Mean time**: 163.0 μs
- **Min time**: 150.9 μs
- **Max time**: 373.9 μs
- **Std dev**: 23.5 μs
- **Rounds**: 777

**Metrics**:
- Bus Count: 105
- Query Type: get_buses

