# Benchmark Report

**Generated from**: `results/rdflib_realgrid_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Realgrid

- **Mean time**: 34.76 s
- **Min time**: 33.29 s
- **Max time**: 36.39 s
- **Std dev**: 1.45 s
- **Rounds**: 5

**Metrics**:
- Memory Mb: 2765.0
- Triples: 892139
- Lines: 7561
- Generators: 1347
- Loads: 6687
- Substations: 4875
- Dataset Size Mb: 86.5
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Lines

- **Mean time**: 2.0 ms
- **Min time**: 1.9 ms
- **Max time**: 2.7 ms
- **Std dev**: 71.0 μs
- **Rounds**: 329

**Metrics**:
- Line Count: 7561
- Query Type: get_lines
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 370.6 μs
- **Min time**: 358.9 μs
- **Max time**: 641.6 μs
- **Std dev**: 17.3 μs
- **Rounds**: 1257

**Metrics**:
- Generator Count: 1347
- Query Type: get_generators
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 1.8 ms
- **Min time**: 1.7 ms
- **Max time**: 4.9 ms
- **Std dev**: 240.4 μs
- **Rounds**: 293

**Metrics**:
- Load Count: 6687
- Query Type: get_loads
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 1.2 ms
- **Min time**: 1.2 ms
- **Max time**: 1.8 ms
- **Std dev**: 59.3 μs
- **Rounds**: 418

**Metrics**:
- Substation Count: 4875
- Query Type: get_substations
- Library: rdflib
- Dataset: realgrid
- Display Name: RDFlib
- Color: #f1c40f
