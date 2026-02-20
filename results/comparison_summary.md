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
| triplets | 112.3 ms | 22.9 MB | 97 lines, 39 gen, 73 loads | Dataset: 7.2 MB |
| pypowsybl | 434.0 ms | 899.5 MB | 90 lines, 39 gen, 73 loads | Dataset: 7.3 MB |

### Query Performance

| Query Type | triplets | pypowsybl |
|------------|---|---|
| ACLineSegment | 9.8 ms | N/A |
| get_buses | N/A | 150.5 μs |
| get_generators | N/A | 273.5 μs |
| get_lines | N/A | 280.9 μs |

## Detailed Results

### triplets

#### Triplets Load Eq Only

- **Mean**: 52.7 ms
- **Min**: 45.5 ms
- **Max**: 70.2 ms
- **Rounds**: 19

#### Triplets Load Full Model

- **Mean**: 112.3 ms
- **Min**: 105.4 ms
- **Max**: 116.3 ms
- **Rounds**: 9

#### Triplets Query Performance

- **Mean**: 9.8 ms
- **Min**: 7.1 ms
- **Max**: 13.2 ms
- **Rounds**: 103

### pypowsybl

#### Pypowsybl Load Network

- **Mean**: 434.0 ms
- **Min**: 421.8 ms
- **Max**: 455.6 ms
- **Rounds**: 3

#### Pypowsybl Get Lines

- **Mean**: 280.9 μs
- **Min**: 258.3 μs
- **Max**: 1.0 ms
- **Rounds**: 504

#### Pypowsybl Get Generators

- **Mean**: 273.5 μs
- **Min**: 252.0 μs
- **Max**: 1.7 ms
- **Rounds**: 1113

#### Pypowsybl Get Buses

- **Mean**: 150.5 μs
- **Min**: 142.8 μs
- **Max**: 385.1 μs
- **Rounds**: 497
