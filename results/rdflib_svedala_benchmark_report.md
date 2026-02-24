# Benchmark Report

**Generated from**: `results/rdflib_svedala_benchmark.json`

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Results

### Rdflib Load Svedala

- **Mean time**: 1.70 s
- **Min time**: 1.60 s
- **Max time**: 1.84 s
- **Std dev**: 111.1 ms
- **Rounds**: 5

**Metrics**:
- Memory Mb: 263.5
- Triples: 47710
- Lines: 97
- Generators: 39
- Loads: 73
- Substations: 56
- Total Size Mb: 7.3
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Lines

- **Mean time**: 70.3 μs
- **Min time**: 68.2 μs
- **Max time**: 578.8 μs
- **Std dev**: 8.9 μs
- **Rounds**: 4568

**Metrics**:
- Line Count: 97
- Query Type: get_lines
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Generators

- **Mean time**: 57.2 μs
- **Min time**: 55.0 μs
- **Max time**: 444.3 μs
- **Std dev**: 10.0 μs
- **Rounds**: 7097

**Metrics**:
- Generator Count: 39
- Query Type: get_generators
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Loads

- **Mean time**: 159.6 μs
- **Min time**: 154.2 μs
- **Max time**: 693.6 μs
- **Std dev**: 17.8 μs
- **Rounds**: 3563

**Metrics**:
- Load Count: 73
- Query Type: get_loads
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f

### Rdflib Get Substations

- **Mean time**: 60.2 μs
- **Min time**: 58.1 μs
- **Max time**: 719.7 μs
- **Std dev**: 10.2 μs
- **Rounds**: 6686

**Metrics**:
- Substation Count: 56
- Query Type: get_substations
- Library: rdflib
- Dataset: svedala
- Display Name: RDFlib
- Color: #f1c40f
