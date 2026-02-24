# Benchmark Report

**Generated from**: `results/cimgraph_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Cimgraph Load Svedala

- **Mean time**: 1.66 s
- **Min time**: 1.60 s
- **Max time**: 1.77 s
- **Std dev**: 63.0 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 277.1
- Triples: 47710
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Total Size Mb: 7.3
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Lines

- **Mean time**: 113.4 ms
- **Min time**: 109.1 ms
- **Max time**: 128.4 ms
- **Std dev**: 6.4 ms
- **Rounds**: 9

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Generators

- **Mean time**: 110.3 ms
- **Min time**: 108.3 ms
- **Max time**: 113.1 ms
- **Std dev**: 1.5 ms
- **Rounds**: 9

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Loads

- **Mean time**: 333.8 ms
- **Min time**: 325.1 ms
- **Max time**: 343.5 ms
- **Std dev**: 8.8 ms
- **Rounds**: 5

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Substations

- **Mean time**: 108.1 ms
- **Min time**: 106.9 ms
- **Max time**: 111.5 ms
- **Std dev**: 1.4 ms
- **Rounds**: 9

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: cimgraph
- Dataset: svedala
- Display Name: CIM-Graph
- Color: #9467bd
