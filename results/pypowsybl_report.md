# Benchmark Report

**Generated from**: `results/pypowsybl_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Network

- **Mean time**: 434.0 ms
- **Min time**: 421.8 ms
- **Max time**: 455.6 ms
- **Std dev**: 18.7 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 899.5
- Total Size Mb: 7.3
- Buses: 105
- Lines: 90
- Generators: 39
- Loads: 73
- Substations: 57

### Pypowsybl Get Lines

- **Mean time**: 280.9 μs
- **Min time**: 258.3 μs
- **Max time**: 1.0 ms
- **Std dev**: 45.8 μs
- **Rounds**: 504

**Metrics**:
- Line Count: 90
- Query Type: get_lines

### Pypowsybl Get Generators

- **Mean time**: 273.5 μs
- **Min time**: 252.0 μs
- **Max time**: 1.7 ms
- **Std dev**: 70.9 μs
- **Rounds**: 1113

**Metrics**:
- Generator Count: 39
- Query Type: get_generators

### Pypowsybl Get Buses

- **Mean time**: 150.5 μs
- **Min time**: 142.8 μs
- **Max time**: 385.1 μs
- **Std dev**: 13.9 μs
- **Rounds**: 497

**Metrics**:
- Bus Count: 105
- Query Type: get_buses
