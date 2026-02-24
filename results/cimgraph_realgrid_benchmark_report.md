# Benchmark Report

**Generated from**: `results/cimgraph_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Cimgraph Load Realgrid

- **Mean time**: 34.55 s
- **Min time**: 33.26 s
- **Max time**: 36.41 s
- **Std dev**: 1.55 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 3037.3
- Triples: 892139
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Lines

- **Mean time**: 2.13 s
- **Min time**: 2.11 s
- **Max time**: 2.15 s
- **Std dev**: 18.3 ms
- **Rounds**: 5

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Generators

- **Mean time**: 2.14 s
- **Min time**: 2.10 s
- **Max time**: 2.21 s
- **Std dev**: 44.5 ms
- **Rounds**: 5

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Loads

- **Mean time**: 6.34 s
- **Min time**: 6.28 s
- **Max time**: 6.43 s
- **Std dev**: 57.4 ms
- **Rounds**: 5

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd

### Cimgraph Get Substations

- **Mean time**: 2.12 s
- **Min time**: 2.10 s
- **Max time**: 2.13 s
- **Std dev**: 10.8 ms
- **Rounds**: 5

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: cimgraph
- Dataset: realgrid
- Display Name: CIM-Graph
- Color: #9467bd
