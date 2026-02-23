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
| pypowsybl (Realgrid) | 4.33 s | 4559.9 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| pypowsybl (Svedala) | 423.2 ms | 1021.9 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| triplets (Realgrid) | 1.37 s | 516.5 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| triplets (Svedala) | 116.6 ms | 60.8 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |
| veragrid (Realgrid) | 16.88 s | 2657.0 MB | 7561 lines, 1347 gen, 6687 loads | Dataset: 86.5 MB |
| veragrid (Svedala) | 1.41 s | 617.6 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.3 MB |

### Query Performance

| Query Type | pypowsybl (Realgrid) | pypowsybl (Svedala) | triplets (Realgrid) | triplets (Svedala) | veragrid (Realgrid) | veragrid (Svedala) |
|------------|---|---|---|---|---|---|
| get_generators | 2.7 ms | 319.7 μs | 12.8 ms | 1.7 ms | 0.0 μs | 0.0 μs |
| get_lines | 35.6 ms | 332.3 μs | 13.6 ms | 1.6 ms | 0.0 μs | 0.0 μs |
| get_loads | 22.3 ms | 225.7 μs | 38.0 ms | 4.9 ms | 0.1 μs | 0.1 μs |
| get_substations | 7.2 ms | 159.1 μs | 13.3 ms | 1.6 ms | 0.0 μs | 0.0 μs |

## Detailed Results

### pypowsybl (Realgrid)

#### Pypowsybl Load Realgrid

- **Mean**: 4.33 s
- **Min**: 4.24 s
- **Max**: 4.47 s
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 35.6 ms
- **Min**: 33.9 ms
- **Max**: 39.3 ms
- **Rounds**: 28

#### Pypowsybl Get Generators

- **Mean**: 2.7 ms
- **Min**: 2.5 ms
- **Max**: 4.9 ms
- **Rounds**: 151

#### Pypowsybl Get Loads

- **Mean**: 22.3 ms
- **Min**: 19.0 ms
- **Max**: 32.5 ms
- **Rounds**: 45

#### Pypowsybl Get Substations

- **Mean**: 7.2 ms
- **Min**: 3.7 ms
- **Max**: 64.4 ms
- **Rounds**: 131

### pypowsybl (Svedala)

#### Pypowsybl Load Svedala

- **Mean**: 423.2 ms
- **Min**: 409.5 ms
- **Max**: 439.2 ms
- **Rounds**: 5

#### Pypowsybl Get Lines

- **Mean**: 332.3 μs
- **Min**: 317.8 μs
- **Max**: 3.0 ms
- **Rounds**: 1025

#### Pypowsybl Get Generators

- **Mean**: 319.7 μs
- **Min**: 304.1 μs
- **Max**: 667.1 μs
- **Rounds**: 1604

#### Pypowsybl Get Loads

- **Mean**: 225.7 μs
- **Min**: 216.8 μs
- **Max**: 404.9 μs
- **Rounds**: 1840

#### Pypowsybl Get Substations

- **Mean**: 159.1 μs
- **Min**: 148.7 μs
- **Max**: 516.2 μs
- **Rounds**: 2361

### triplets (Realgrid)

#### Triplets Load Realgrid

- **Mean**: 1.37 s
- **Min**: 1.37 s
- **Max**: 1.37 s
- **Rounds**: 5

#### Triplets Get Lines

- **Mean**: 13.6 ms
- **Min**: 13.3 ms
- **Max**: 16.0 ms
- **Rounds**: 68

#### Triplets Get Generators

- **Mean**: 12.8 ms
- **Min**: 12.6 ms
- **Max**: 13.5 ms
- **Rounds**: 70

#### Triplets Get Loads

- **Mean**: 38.0 ms
- **Min**: 37.5 ms
- **Max**: 39.6 ms
- **Rounds**: 26

#### Triplets Get Substations

- **Mean**: 13.3 ms
- **Min**: 12.4 ms
- **Max**: 26.6 ms
- **Rounds**: 73

### triplets (Svedala)

#### Triplets Load Svedala

- **Mean**: 116.6 ms
- **Min**: 112.0 ms
- **Max**: 137.7 ms
- **Rounds**: 9

#### Triplets Get Lines

- **Mean**: 1.6 ms
- **Min**: 1.6 ms
- **Max**: 1.9 ms
- **Rounds**: 387

#### Triplets Get Generators

- **Mean**: 1.7 ms
- **Min**: 1.6 ms
- **Max**: 2.5 ms
- **Rounds**: 532

#### Triplets Get Loads

- **Mean**: 4.9 ms
- **Min**: 4.7 ms
- **Max**: 5.8 ms
- **Rounds**: 196

#### Triplets Get Substations

- **Mean**: 1.6 ms
- **Min**: 1.6 ms
- **Max**: 2.0 ms
- **Rounds**: 578

### veragrid (Realgrid)

#### Veragrid Load Realgrid

- **Mean**: 16.88 s
- **Min**: 15.14 s
- **Max**: 18.65 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.9 μs
- **Rounds**: 199641

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.8 μs
- **Rounds**: 122026

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.7 μs
- **Rounds**: 70642

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.7 μs
- **Rounds**: 121729

### veragrid (Svedala)

#### Veragrid Load Svedala

- **Mean**: 1.41 s
- **Min**: 1.08 s
- **Max**: 1.67 s
- **Rounds**: 5

#### Veragrid Get Lines

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.2 μs
- **Rounds**: 197668

#### Veragrid Get Generators

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.9 μs
- **Rounds**: 199641

#### Veragrid Get Loads

- **Mean**: 0.1 μs
- **Min**: 0.1 μs
- **Max**: 0.7 μs
- **Rounds**: 90327

#### Veragrid Get Substations

- **Mean**: 0.0 μs
- **Min**: 0.0 μs
- **Max**: 0.6 μs
- **Rounds**: 133441
