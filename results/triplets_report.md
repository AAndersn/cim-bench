# Benchmark Report

**Generated from**: `results/triplets_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Eq Only

- **Mean time**: 52.7 ms
- **Min time**: 45.5 ms
- **Max time**: 70.2 ms
- **Std dev**: 4.8 ms
- **Rounds**: 19

**Metrics**:
- Memory Mb: 17.8
- Triplets Count: 47718
- Unique Objects: 8231
- File Size Mb: 3.8

### Triplets Load Full Model

- **Mean time**: 112.3 ms
- **Min time**: 105.4 ms
- **Max time**: 116.3 ms
- **Std dev**: 3.2 ms
- **Rounds**: 9

**Metrics**:
- Memory Mb: 22.9
- Triplets Count: 94861
- Unique Objects: 14456
- Instances: 4
- Total Size Mb: 7.2
- Files Loaded: 4
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56

### Triplets Query Performance

- **Mean time**: 9.8 ms
- **Min time**: 7.1 ms
- **Max time**: 13.2 ms
- **Std dev**: 1.6 ms
- **Rounds**: 103

**Metrics**:
- Results Count: 97
- Query Type: ACLineSegment
