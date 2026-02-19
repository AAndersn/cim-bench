# Benchmark Report

**Generated from**: `results/triplets_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.14.2
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Triplets Load Eq Only

- **Mean time**: 55.0 ms
- **Min time**: 51.5 ms
- **Max time**: 59.9 ms
- **Std dev**: 2.3 ms
- **Rounds**: 19

**Metrics**:
- Memory Mb: 17.4
- Triplets Count: 47718
- Unique Objects: 8231
- File Size Mb: 3.8

### Triplets Load Full Model

- **Mean time**: 123.6 ms
- **Min time**: 120.0 ms
- **Max time**: 125.6 ms
- **Std dev**: 2.1 ms
- **Rounds**: 9

**Metrics**:
- Memory Mb: 23.0
- Triplets Count: 94861
- Unique Objects: 14456
- Instances: 4
- Total Size Mb: 7.2
- Files Loaded: 4

### Triplets Query Performance

- **Mean time**: 12.3 ms
- **Min time**: 10.0 ms
- **Max time**: 14.3 ms
- **Std dev**: 869.5 μs
- **Rounds**: 95

**Metrics**:
- Results Count: 97
- Query Type: ACLineSegment

