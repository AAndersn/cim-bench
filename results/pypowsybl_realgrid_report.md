# Benchmark Report

**Generated from**: `results/pypowsybl_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Pypowsybl Load Realgrid

- **Mean time**: 4.79 s
- **Min time**: 4.71 s
- **Max time**: 4.91 s
- **Std dev**: 107.3 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 3371.9
- Dataset Size Mb: 86.5
- Buses: 6051
- Lines: 7561
- Ac Lines: 7561
- Dangling Lines: 0
- Generators: 1347
- Loads: 6687
- Substations: 4791

### Pypowsybl Get Lines Realgrid

- **Mean time**: 40.2 ms
- **Min time**: 34.2 ms
- **Max time**: 48.2 ms
- **Std dev**: 3.7 ms
- **Rounds**: 26

**Metrics**:
- Line Count: 7561
- Query Type: get_lines

### Pypowsybl Get Generators Realgrid

- **Mean time**: 4.1 ms
- **Min time**: 2.4 ms
- **Max time**: 10.5 ms
- **Std dev**: 1.2 ms
- **Rounds**: 172

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators

### Pypowsybl Get Loads Realgrid

- **Mean time**: 22.3 ms
- **Min time**: 18.9 ms
- **Max time**: 27.3 ms
- **Std dev**: 2.1 ms
- **Rounds**: 46

**Metrics**:
- Load Count: 6687
- Query Type: get_loads

### Pypowsybl Get Substations Realgrid

- **Mean time**: 5.5 ms
- **Min time**: 3.6 ms
- **Max time**: 8.4 ms
- **Std dev**: 1.1 ms
- **Rounds**: 110

**Metrics**:
- Substation Count: 4791
- Query Type: get_substations
