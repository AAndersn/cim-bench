# cim-bench

Performance benchmarking suite for CIM (Common Information Model) parsers and serializers.

## Overview

This repository contains benchmarks for comparing the performance of different CIM parser and serializer implementations.

## Project Structure

```
cim-bench/
├── benchmarks/          # Benchmark test files
├── data/                # Sample CIM data files for testing
│   └── relicapgrid/     # ENTSO-E test grid data (git submodule)
├── parsers/             # Parser implementations or wrappers
└── results/             # Benchmark results and reports
```

## Getting Started

### Clone with Submodules

This repository uses git submodules for test data. Clone with:

```bash
git clone --recurse-submodules https://github.com/yourusername/cim-bench.git
```

Or if you already cloned without submodules:

```bash
git submodule update --init --recursive
```

### Installation

```bash
uv sync
```

### Running Benchmarks

Run all benchmarks:
```bash
uv run pytest benchmarks/ --benchmark-only
```

Run specific benchmark:
```bash
uv run pytest benchmarks/test_triplets_benchmark.py --benchmark-only
```

Save results to JSON:
```bash
uv run pytest benchmarks/ --benchmark-only --benchmark-json=results/output.json
```

Generate markdown report from results:
```bash
uv run python tools/generate_report.py results/output.json
```

## Benchmark Results

Latest results on AMD Ryzen AI 9 HX 370, 64GB RAM, Python 3.13.12:

### Comparison Summary

| Library | Version | Load Time | Memory | Query Speed | Use Case |
|---------|---------|-----------|--------|-------------|----------|
| **triplets** | 0.0.17 | 123.6 ms | 23 MB | 12.3 ms | RDF data extraction, low memory |
| **pypowsybl** | 1.14.0 | 437.8 ms | 924 MB | 163 μs | Power analysis, network model |

### Detailed Results: Svedala IGM Dataset (7.3 MB, CGMES EQ+SSH+SV+TP)

#### triplets - RDF/Pandas Parser
- **Load Time**: 123.6 ms
- **Memory**: 23 MB
- **Data Structure**: 94,861 triplets, 14,456 unique objects
- **Query Performance**: 12.3 ms (ACLineSegment type query)
- **Strengths**: Very fast loading, minimal memory, simple API
- **Use Case**: Data extraction, batch processing, RDF manipulation

#### pypowsybl - Power System Network Model
- **Load Time**: 437.8 ms (3.5x slower than triplets)
- **Memory**: 923.6 MB (40x more than triplets)
- **Network Elements**: 105 buses, 90 lines, 39 generators, 73 loads, 57 substations
- **Query Performance**: 163-290 μs (42-75x faster than triplets)
- **Strengths**: Rich network model, sub-millisecond queries, analysis-ready
- **Use Case**: Power flow analysis, network operations, TSO applications

### Trade-offs

**Choose triplets when**:
- Memory is limited
- Need fast parsing of many files
- Working with raw RDF/XML data
- Simple data extraction tasks

**Choose pypowsybl when**:
- Need complete power system network model
- Performing network analysis or power flow
- Query performance is critical
- Memory is not a constraint

See `tools/*/README.md` for detailed per-tool documentation and analysis.

## Parsers/Serializers

### Currently Tested
- **triplets** (v0.0.17) - Python, pandas-based, version-agnostic RDF parser
  - Fast loading, low memory footprint
  - Best for: Data extraction, RDF manipulation
- **pypowsybl** (v1.14.0) - Python binding for PowSyBl (Java)
  - Rich network model, fast queries
  - Best for: Power flow analysis, network operations

### Planned
- cimpy
- cimantic-graphs (PNNL)
- libcimpp (C++)
- rdflib
- Apache Jena

## Contributing

Add new benchmark cases in the `benchmarks/` directory following the existing patterns.
