# pypowsybl

## Version Tested
- pypowsybl 1.14.0
- Python 3.13.12

## Description
pypowsybl is a Python binding for PowSyBl (Power System Blocks), an open-source framework written in Java for power system modeling and analysis. It provides comprehensive support for CGMES (Common Grid Model Exchange Standard) and other power system formats.

## Repository
- GitHub: https://github.com/powsybl/pypowsybl
- Documentation: https://pypowsybl.readthedocs.io/
- PowSyBl Core: https://www.powsybl.org/

## Installation
```bash
pip install pypowsybl
```

**Note**: pypowsybl currently supports Python up to 3.13 (as of version 1.14.0)

## Environment
- OS: Linux (Fedora 43)
- CPU: AMD Ryzen AI 9 HX 370
- RAM: 64 GB
- Python: 3.13.12

## Benchmark Results (2026-02-19)

### Test Dataset: Svedala IGM (ENTSO-E) + CommonData
Dataset location: `data/relicapgrid/Instance/Grid/IGM_Svedala/` + CommonData

**Total dataset size**: 7.3 MB (EQ + SSH + SV + TP + CommonData)

#### Network Loading Performance
- **Load time**: 437.8 ms (mean)
  - Min: 429.8 ms
  - Max: 450.0 ms
  - Std dev: 10.1 ms
- **Memory usage**: 923.6 MB
- **Network elements**:
  - Buses: 105
  - Lines: 90
  - Generators: 39
  - Loads: 73
  - Substations: 57

#### Query Performance (on loaded network)

| Operation | Mean Time | Description |
|-----------|-----------|-------------|
| **get_buses()** | 163.0 μs | Retrieve all bus data as DataFrame |
| **get_generators()** | 290.2 μs | Retrieve all generator data as DataFrame |
| **get_lines()** | 288.7 μs | Retrieve all line data as DataFrame |

## Performance Characteristics

### Strengths
- **Very fast queries**: Sub-millisecond query times (microseconds) for retrieving network elements
- **Rich data model**: Full power system network model with comprehensive attributes
- **Network analysis**: Built-in power flow calculations, security analysis, etc.
- **DataFrame output**: Returns pandas DataFrames for easy data manipulation
- **Production-ready**: Used in real TSO operations

### Trade-offs
- **Higher memory usage**: ~900 MB for 7 MB dataset (40x more than triplets)
- **Slower initial load**: 438 ms vs 124 ms for triplets (3.5x slower)
- **Java dependency**: Runs on JVM (via py4j), adds overhead
- **Requires CommonData**: CGMES loading needs boundary and common data files

## Comparison with triplets

| Metric | pypowsybl | triplets | Winner |
|--------|-----------|----------|--------|
| Load time | 437.8 ms | 123.6 ms | triplets (3.5x faster) |
| Memory | 923.6 MB | 23.0 MB | triplets (40x less) |
| Query speed | 163-290 μs | 12.3 ms | pypowsybl (42-75x faster) |
| Data model | Network model | RDF triplets | pypowsybl (richer) |
| Use case | Power analysis | Data processing | Different purposes |

## Use Cases

**Best for**:
- Power flow calculations and analysis
- Network topology operations
- TSO/DSO operational applications
- When you need a complete network model
- When query performance matters more than memory

**Not ideal for**:
- Memory-constrained environments
- Simple RDF data extraction
- Batch processing of many small files
- When you need raw RDF/XML access

## API Highlights

```python
import pypowsybl.network as pn

# Load CGMES network (from ZIP or directory)
network = pn.load("network.zip")

# Get network elements as DataFrames
buses = network.get_buses()
lines = network.get_lines()
generators = network.get_generators()
loads = network.get_loads()

# Access specific attributes
print(f"Total buses: {len(buses)}")
print(f"Line names: {lines['name'].tolist()}")

# Network analysis (not benchmarked)
# network.run_load_flow()
# results = network.get_security_analysis_result()
```

## Known Limitations
- High memory consumption for large networks
- Requires Java Virtual Machine (bundled, but adds overhead)
- CGMES import requires CommonData/Boundary files
- Python 3.14+ not yet supported (as of v1.14.0)
- Initial loading slower than lightweight parsers
