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
| triplets (Svedala) | 124.8 ms | 27.6 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| pypowsybl (Svedala) | 474.4 ms | 887.4 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.31 s | 516.9 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| pypowsybl (Realgrid) | 4.79 s | 3371.9 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |

### Query Performance

| Query Type | triplets (Svedala) | pypowsybl (Svedala) | triplets (Realgrid) | pypowsybl (Realgrid) |
|------------|---|---|---|---|
| get_generators | 6.4 ms | 293.7 μs | 62.2 ms | 4.1 ms |
| get_lines | 6.0 ms | 318.4 μs | 67.5 ms | 40.2 ms |
| get_loads | 17.6 ms | 212.5 μs | 190.9 ms | 22.3 ms |
| get_substations | 6.0 ms | 129.9 μs | 62.6 ms | 5.5 ms |

## Detailed Results

### triplets (Svedala)

#### Triplets Load Full Model

- **Mean**: 124.8 ms
- **Min**: 114.9 ms
- **Max**: 148.4 ms
- **Rounds**: 9

#### Triplets Get Lines

- **Mean**: 6.0 ms
- **Min**: 4.4 ms
- **Max**: 8.2 ms
- **Rounds**: 90

#### Triplets Get Generators

- **Mean**: 6.4 ms
- **Min**: 4.4 ms
- **Max**: 10.3 ms
- **Rounds**: 166

#### Triplets Get Loads

- **Mean**: 17.6 ms
- **Min**: 13.5 ms
- **Max**: 24.7 ms
- **Rounds**: 64

#### Triplets Get Substations

- **Mean**: 6.0 ms
- **Min**: 4.5 ms
- **Max**: 9.0 ms
- **Rounds**: 197

### pypowsybl (Svedala)

#### Pypowsybl Load Network

- **Mean**: 474.4 ms
- **Min**: 464.6 ms
- **Max**: 491.7 ms
- **Rounds**: 3

#### Pypowsybl Get Lines

- **Mean**: 318.4 μs
- **Min**: 259.1 μs
- **Max**: 1.2 ms
- **Rounds**: 1043

#### Pypowsybl Get Generators

- **Mean**: 293.7 μs
- **Min**: 262.4 μs
- **Max**: 501.7 μs
- **Rounds**: 994

#### Pypowsybl Get Loads

- **Mean**: 212.5 μs
- **Min**: 196.0 μs
- **Max**: 367.8 μs
- **Rounds**: 1270

#### Pypowsybl Get Substations

- **Mean**: 129.9 μs
- **Min**: 117.7 μs
- **Max**: 312.6 μs
- **Rounds**: 1538

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.31 s
- **Min**: 1.31 s
- **Max**: 1.32 s
- **Rounds**: 3

#### Triplets Get Lines Realgrid

- **Mean**: 67.5 ms
- **Min**: 62.0 ms
- **Max**: 75.3 ms
- **Rounds**: 11

#### Triplets Get Generators Realgrid

- **Mean**: 62.2 ms
- **Min**: 61.3 ms
- **Max**: 63.3 ms
- **Rounds**: 17

#### Triplets Get Loads Realgrid

- **Mean**: 190.9 ms
- **Min**: 186.3 ms
- **Max**: 200.9 ms
- **Rounds**: 6

#### Triplets Get Substations Realgrid

- **Mean**: 62.6 ms
- **Min**: 61.2 ms
- **Max**: 64.3 ms
- **Rounds**: 17

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.79 s
- **Min**: 4.71 s
- **Max**: 4.91 s
- **Rounds**: 3

#### Pypowsybl Get Lines Realgrid

- **Mean**: 40.2 ms
- **Min**: 34.2 ms
- **Max**: 48.2 ms
- **Rounds**: 26

#### Pypowsybl Get Generators Realgrid

- **Mean**: 4.1 ms
- **Min**: 2.4 ms
- **Max**: 10.5 ms
- **Rounds**: 172

#### Pypowsybl Get Loads Realgrid

- **Mean**: 22.3 ms
- **Min**: 18.9 ms
- **Max**: 27.3 ms
- **Rounds**: 46

#### Pypowsybl Get Substations Realgrid

- **Mean**: 5.5 ms
- **Min**: 3.6 ms
- **Max**: 8.4 ms
- **Rounds**: 110
