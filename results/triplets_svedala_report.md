# Benchmark Report

**Generated from**: `results/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Svedala

- **Mean time**: 124.5 ms
- **Min time**: 114.8 ms
- **Max time**: 129.9 ms
- **Std dev**: 4.4 ms
- **Rounds**: 10

**Metrics**:
- Memory Mb: 45.3
- Triplets Count: 95539
- Unique Objects: 14540
- Instances: 5
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57
- Total Size Mb: 7.3
- Library: triplets
- Dataset: svedala

### Triplets Get Lines

- **Mean time**: 6.0 ms
- **Min time**: 5.7 ms
- **Max time**: 7.1 ms
- **Std dev**: 281.2 μs
- **Rounds**: 77

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: triplets
- Dataset: svedala

### Triplets Get Generators

- **Mean time**: 5.6 ms
- **Min time**: 5.0 ms
- **Max time**: 7.7 ms
- **Std dev**: 451.4 μs
- **Rounds**: 159

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: triplets
- Dataset: svedala

### Triplets Get Loads

- **Mean time**: 17.3 ms
- **Min time**: 16.4 ms
- **Max time**: 19.0 ms
- **Std dev**: 602.6 μs
- **Rounds**: 53

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: triplets
- Dataset: svedala

### Triplets Get Substations

- **Mean time**: 5.8 ms
- **Min time**: 5.4 ms
- **Max time**: 7.0 ms
- **Std dev**: 311.4 μs
- **Rounds**: 175

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
- Library: triplets
- Dataset: svedala
