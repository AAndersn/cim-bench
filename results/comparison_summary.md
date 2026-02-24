# Benchmark Comparison Report

## Environment

- **CPU**: AMD Ryzen AI 9 HX 370 w/ Radeon 890M
- **Cores**: 24
- **Python**: 3.13.12
- **System**: Linux 6.18.10-200.fc43.x86_64

## Performance Comparison

### Load Performance

| Library | Load Time (mean) | Memory (MB) | Elements | Notes |
|---------|------------------|-------------|----------|-------|
| cimgraph (Realgrid) | 34.55 s | 3037.3 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| cimgraph (Svedala) | 1.66 s | 277.1 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| pypowsybl (Realgrid) | 4.85 s | 4433.3 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 477.4 ms | 944.1 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| rdflib (Realgrid) | 34.76 s | 2765.0 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| rdflib (Svedala) | 1.70 s | 263.5 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.56 s | 515.6 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| triplets (Svedala) | 137.6 ms | 62.8 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| veragrid (Realgrid) | 17.84 s | 2681.1 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| veragrid (Svedala) | 1.50 s | 615.4 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |

### Query Performance

| Query Type | cimgraph (Realgrid) | cimgraph (Svedala) | pypowsybl (Realgrid) | pypowsybl (Svedala) | rdflib (Realgrid) | rdflib (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|---|---|---|---|
| get_generators | 2.14 s | 110.3 ms | 3.1 ms | 383.5 μs | 370.6 μs | 57.2 μs | 17.7 ms | 2.0 ms | 0.0 μs | 0.1 μs |
| get_lines | 2.13 s | 113.4 ms | 35.3 ms | 404.5 μs | 2.0 ms | 70.3 μs | 19.5 ms | 1.9 ms | 0.0 μs | 0.0 μs |
| get_loads | 6.34 s | 333.8 ms | 18.6 ms | 275.3 μs | 1.8 ms | 159.6 μs | 52.9 ms | 5.7 ms | 0.1 μs | 0.1 μs |
| get_substations | 2.12 s | 108.1 ms | 4.8 ms | 198.6 μs | 1.2 ms | 60.2 μs | 17.6 ms | 1.9 ms | 0.0 μs | 0.0 μs |

## Detailed Results

### cimgraph (Realgrid)

#### Cimgraph Load Realgrid

- **Mean**: 34.55 s
- **Min**: 33.26 s
- **Max**: 36.41 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 2.13 s
- **Min**: 2.11 s
- **Max**: 2.15 s
- **Rounds**: 5

#### Cimgraph Get Generators

- **Mean**: 2.14 s
- **Min**: 2.10 s
- **Max**: 2.21 s
- **Rounds**: 5

#### Cimgraph Get Loads

- **Mean**: 6.34 s
- **Min**: 6.28 s
- **Max**: 6.43 s
- **Rounds**: 5

#### Cimgraph Get Substations

- **Mean**: 2.12 s
- **Min**: 2.10 s
- **Max**: 2.13 s
- **Rounds**: 5

### cimgraph (Svedala)

#### Cimgraph Load Svedala

- **Mean**: 1.66 s
- **Min**: 1.60 s
- **Max**: 1.77 s
- **Rounds**: 5

#### Cimgraph Get Lines

- **Mean**: 113.4 ms
- **Min**: 109.1 ms
- **Max**: 128.4 ms
- **Rounds**: 9

#### Cimgraph Get Generators

- **Mean**: 110.3 ms
- **Min**: 108.3 ms
- **Max**: 113.1 ms
- **Rounds**: 9

#### Cimgraph Get Loads

- **Mean**: 333.8 ms
- **Min**: 325.1 ms
- **Max**: 343.5 ms
- **Rounds**: 5

#### Cimgraph Get Substations

- **Mean**: 108.1 ms
- **Min**: 106.9 ms
- **Max**: 111.5 ms
- **Rounds**: 9

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.85 s
- **Min**: 4.72 s
- **Max**: 5.03 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 35.3 ms
- **Min**: 34.4 ms
- **Max**: 36.2 ms
- **Rounds**: 28

#### Pypowsybl Get Generators

- **Mean**: 3.1 ms
- **Min**: 2.8 ms
- **Max**: 18.0 ms
- **Rounds**: 193

#### Pypowsybl Get Loads

- **Mean**: 18.6 ms
- **Min**: 17.9 ms
- **Max**: 22.1 ms
- **Rounds**: 43

#### Pypowsybl Get Substations

- **Mean**: 4.8 ms
- **Min**: 4.2 ms
- **Max**: 13.9 ms
- **Rounds**: 106

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 477.4 ms
- **Min**: 455.7 ms
- **Max**: 501.6 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 404.5 μs
- **Min**: 383.1 μs
- **Max**: 4.4 ms
- **Rounds**: 929

#### Pypowsybl Get Generators

- **Mean**: 383.5 μs
- **Min**: 360.1 μs
- **Max**: 640.0 μs
- **Rounds**: 1220

#### Pypowsybl Get Loads

- **Mean**: 275.3 μs
- **Min**: 259.2 μs
- **Max**: 468.6 μs
- **Rounds**: 1646

#### Pypowsybl Get Substations

- **Mean**: 198.6 μs
- **Min**: 186.4 μs
- **Max**: 370.8 μs
- **Rounds**: 2443

### rdflib (Realgrid)

#### Rdflib Load Realgrid

- **Mean**: 34.76 s
- **Min**: 33.29 s
- **Max**: 36.39 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 2.0 ms
- **Min**: 1.9 ms
- **Max**: 2.7 ms
- **Rounds**: 329

#### Rdflib Get Generators

- **Mean**: 370.6 μs
- **Min**: 358.9 μs
- **Max**: 641.6 μs
- **Rounds**: 1257

#### Rdflib Get Loads

- **Mean**: 1.8 ms
- **Min**: 1.7 ms
- **Max**: 4.9 ms
- **Rounds**: 293

#### Rdflib Get Substations

- **Mean**: 1.2 ms
- **Min**: 1.2 ms
- **Max**: 1.8 ms
- **Rounds**: 418

### rdflib (Svedala)

#### Rdflib Load Svedala

- **Mean**: 1.70 s
- **Min**: 1.60 s
- **Max**: 1.84 s
- **Rounds**: 5

#### Rdflib Get Lines

- **Mean**: 70.3 μs
- **Min**: 68.2 μs
- **Max**: 578.8 μs
- **Rounds**: 4568

#### Rdflib Get Generators

- **Mean**: 57.2 μs
- **Min**: 55.0 μs
- **Max**: 444.3 μs
- **Rounds**: 7097

#### Rdflib Get Loads

- **Mean**: 159.6 μs
- **Min**: 154.2 μs
- **Max**: 693.6 μs
- **Rounds**: 3563

#### Rdflib Get Substations

- **Mean**: 60.2 μs
- **Min**: 58.1 μs
- **Max**: 719.7 μs
- **Rounds**: 6686

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.56 s
- **Min**: 1.55 s
- **Max**: 1.56 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 19.5 ms
- **Min**: 18.2 ms
- **Max**: 24.3 ms
- **Rounds**: 59

#### Triplets Get Generators

- **Mean**: 17.7 ms
- **Min**: 16.4 ms
- **Max**: 34.3 ms
- **Rounds**: 52

#### Triplets Get Loads

- **Mean**: 52.9 ms
- **Min**: 49.1 ms
- **Max**: 77.8 ms
- **Rounds**: 20

#### Triplets Get Substations

- **Mean**: 17.6 ms
- **Min**: 16.3 ms
- **Max**: 26.1 ms
- **Rounds**: 48

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 137.6 ms
- **Min**: 129.1 ms
- **Max**: 161.0 ms
- **Rounds**: 8

#### Triplets Get Lines

- **Mean**: 1.9 ms
- **Min**: 1.8 ms
- **Max**: 2.5 ms
- **Rounds**: 361

#### Triplets Get Generators

- **Mean**: 2.0 ms
- **Min**: 1.8 ms
- **Max**: 6.3 ms
- **Rounds**: 459

#### Triplets Get Loads

- **Mean**: 5.7 ms
- **Min**: 5.5 ms
- **Max**: 9.8 ms
- **Rounds**: 159

#### Triplets Get Substations

- **Mean**: 1.9 ms
- **Min**: 1.8 ms
- **Max**: 3.2 ms
- **Rounds**: 472

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 17.84 s
- **Min**: 16.27 s
- **Max**: 19.83 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 103542

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 106519

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 172.9 μs
- **Rounds**: 182816

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 1.0 μs
- **Rounds**: 106304

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 1.50 s
- **Min**: 1.17 s
- **Max**: 1.74 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 115248

#### Veragrid Get Generators

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 5.9 μs
- **Rounds**: 168578

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 7.4 μs
- **Rounds**: 187970

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.9 μs
- **Rounds**: 116605
