# Benchmark Report

**Generated from**: `results/triplets_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Full Model

- **Mean time**: 124.8 ms
- **Min time**: 114.9 ms
- **Max time**: 148.4 ms
- **Std dev**: 9.9 ms
- **Rounds**: 9

**Metrics**:
- Memory Mb: 27.6
- Triplets Count: 95539
- Unique Objects: 14540
- Instances: 5
- Total Size Mb: 7.3
- Files Loaded: 5
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 57

### Triplets Get Lines

- **Mean time**: 6.0 ms
- **Min time**: 4.4 ms
- **Max time**: 8.2 ms
- **Std dev**: 957.1 μs
- **Rounds**: 90

**Metrics**:
- Line Count: 97
- Query Type: get_lines

### Triplets Get Generators

- **Mean time**: 6.4 ms
- **Min time**: 4.4 ms
- **Max time**: 10.3 ms
- **Std dev**: 921.4 μs
- **Rounds**: 166

**Metrics**:
- Generator Count: 39
- Query Type: get_generators

### Triplets Get Loads

- **Mean time**: 17.6 ms
- **Min time**: 13.5 ms
- **Max time**: 24.7 ms
- **Std dev**: 2.6 ms
- **Rounds**: 64

**Metrics**:
- Load Count: 73
- Query Type: get_loads

### Triplets Get Substations

- **Mean time**: 6.0 ms
- **Min time**: 4.5 ms
- **Max time**: 9.0 ms
- **Std dev**: 982.6 μs
- **Rounds**: 197

**Metrics**:
- Substation Count: 57
- Query Type: get_substations
