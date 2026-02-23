# Benchmark Report

**Generated from**: `results/triplets_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Realgrid

- **Mean time**: 1.37 s
- **Min time**: 1.20 s
- **Max time**: 1.46 s
- **Std dev**: 107.8 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 602.9
- Triplets Count: 1146215
- Unique Objects: 149174
- Instances: 4
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: triplets
- Dataset: realgrid

### Triplets Get Lines

- **Mean time**: 72.8 ms
- **Min time**: 66.0 ms
- **Max time**: 92.6 ms
- **Std dev**: 9.9 ms
- **Rounds**: 9

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: triplets
- Dataset: realgrid

### Triplets Get Generators

- **Mean time**: 68.1 ms
- **Min time**: 65.2 ms
- **Max time**: 83.0 ms
- **Std dev**: 5.5 ms
- **Rounds**: 15

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: triplets
- Dataset: realgrid

### Triplets Get Loads

- **Mean time**: 205.4 ms
- **Min time**: 194.6 ms
- **Max time**: 253.3 ms
- **Std dev**: 23.5 ms
- **Rounds**: 6

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: triplets
- Dataset: realgrid

### Triplets Get Substations

- **Mean time**: 65.5 ms
- **Min time**: 65.0 ms
- **Max time**: 66.1 ms
- **Std dev**: 294.2 μs
- **Rounds**: 15

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: triplets
- Dataset: realgrid
