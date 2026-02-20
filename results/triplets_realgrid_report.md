# Benchmark Report

**Generated from**: `results/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.31 s
- **Min time**: 1.31 s
- **Max time**: 1.32 s
- **Std dev**: 6.1 ms
- **Rounds**: 3

**Metrics**:
- Memory Mb: 516.9
- Triplets Count: 1146215
- Unique Objects: 149174
- Instances: 4
- Dataset Size Mb: 86.5
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875

### Triplets Get Lines Realgrid

- **Mean time**: 67.5 ms
- **Min time**: 62.0 ms
- **Max time**: 75.3 ms
- **Std dev**: 5.6 ms
- **Rounds**: 11

**Metrics**:
- Line Count: 7561
- Query Type: get_lines

### Triplets Get Generators Realgrid

- **Mean time**: 62.2 ms
- **Min time**: 61.3 ms
- **Max time**: 63.3 ms
- **Std dev**: 554.1 μs
- **Rounds**: 17

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators

### Triplets Get Loads Realgrid

- **Mean time**: 190.9 ms
- **Min time**: 186.3 ms
- **Max time**: 200.9 ms
- **Std dev**: 5.2 ms
- **Rounds**: 6

**Metrics**:
- Load Count: 6687
- Query Type: get_loads

### Triplets Get Substations Realgrid

- **Mean time**: 62.6 ms
- **Min time**: 61.2 ms
- **Max time**: 64.3 ms
- **Std dev**: 1.0 ms
- **Rounds**: 17

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
