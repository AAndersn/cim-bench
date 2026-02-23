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
| triplets (Svedala) | 124.5 ms | 45.3 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| pypowsybl (Svedala) | 443.4 ms | 1251.5 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.37 s | 602.9 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| pypowsybl (Realgrid) | 4.41 s | 5463.5 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |

### Query Performance

| Query Type | triplets (Svedala) | pypowsybl (Svedala) | triplets (Realgrid) | pypowsybl (Realgrid) |
|------------|---|---|---|---|
| get_generators | 5.6 ms | 270.8 μs | 68.1 ms | 2.8 ms |
| get_lines | 6.0 ms | 301.8 μs | 72.8 ms | 37.5 ms |
| get_loads | 17.3 ms | 195.0 μs | 205.4 ms | 19.2 ms |
| get_substations | 5.8 ms | 125.0 μs | 65.5 ms | 3.7 ms |

## Detailed Results

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 124.5 ms
- **Min**: 114.8 ms
- **Max**: 129.9 ms
- **Rounds**: 10

#### Triplets Get Lines

- **Mean**: 6.0 ms
- **Min**: 5.7 ms
- **Max**: 7.1 ms
- **Rounds**: 77

#### Triplets Get Generators

- **Mean**: 5.6 ms
- **Min**: 5.0 ms
- **Max**: 7.7 ms
- **Rounds**: 159

#### Triplets Get Loads

- **Mean**: 17.3 ms
- **Min**: 16.4 ms
- **Max**: 19.0 ms
- **Rounds**: 53

#### Triplets Get Substations

- **Mean**: 5.8 ms
- **Min**: 5.4 ms
- **Max**: 7.0 ms
- **Rounds**: 175

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 443.4 ms
- **Min**: 425.3 ms
- **Max**: 460.3 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 301.8 μs
- **Min**: 267.1 μs
- **Max**: 23.3 ms
- **Rounds**: 1157

#### Pypowsybl Get Generators

- **Mean**: 270.8 μs
- **Min**: 258.1 μs
- **Max**: 725.8 μs
- **Rounds**: 1440

#### Pypowsybl Get Loads

- **Mean**: 195.0 μs
- **Min**: 180.7 μs
- **Max**: 403.7 μs
- **Rounds**: 1963

#### Pypowsybl Get Substations

- **Mean**: 125.0 μs
- **Min**: 118.6 μs
- **Max**: 325.0 μs
- **Rounds**: 3571

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.37 s
- **Min**: 1.20 s
- **Max**: 1.46 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 72.8 ms
- **Min**: 66.0 ms
- **Max**: 92.6 ms
- **Rounds**: 9

#### Triplets Get Generators

- **Mean**: 68.1 ms
- **Min**: 65.2 ms
- **Max**: 83.0 ms
- **Rounds**: 15

#### Triplets Get Loads

- **Mean**: 205.4 ms
- **Min**: 194.6 ms
- **Max**: 253.3 ms
- **Rounds**: 6

#### Triplets Get Substations

- **Mean**: 65.5 ms
- **Min**: 65.0 ms
- **Max**: 66.1 ms
- **Rounds**: 15

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.41 s
- **Min**: 4.28 s
- **Max**: 4.58 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 37.5 ms
- **Min**: 33.7 ms
- **Max**: 58.4 ms
- **Rounds**: 29

#### Pypowsybl Get Generators

- **Mean**: 2.8 ms
- **Min**: 2.3 ms
- **Max**: 7.5 ms
- **Rounds**: 165

#### Pypowsybl Get Loads

- **Mean**: 19.2 ms
- **Min**: 17.8 ms
- **Max**: 24.2 ms
- **Rounds**: 42

#### Pypowsybl Get Substations

- **Mean**: 3.7 ms
- **Min**: 2.8 ms
- **Max**: 84.3 ms
- **Rounds**: 206
