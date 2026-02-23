# Benchmark Report

**Generated from**: `results/veragrid_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Veragrid Load Realgrid

- **Mean time**: 16.88 s
- **Min time**: 15.14 s
- **Max time**: 18.65 s
- **Std dev**: 1.25 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2657.0
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Cgmes Version: UNSERIALIZABLE[2.4.15]
- Dataset Size Mb: 86.5
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Lines

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.9 μs
- **Std dev**: 0.0 μs
- **Rounds**: 199641

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Generators

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.8 μs
- **Std dev**: 0.0 μs
- **Rounds**: 122026

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Loads

- **Mean time**: 0.1 μs
- **Min time**: 0.1 μs
- **Max time**: 0.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 70642

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c

### Veragrid Get Substations

- **Mean time**: 0.0 μs
- **Min time**: 0.0 μs
- **Max time**: 0.7 μs
- **Std dev**: 0.0 μs
- **Rounds**: 121729

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: veragrid
- Dataset: realgrid
- Display Name: VeraGrid
- Color: #2ca02c
