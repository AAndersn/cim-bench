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

**Optional: Install visualization dependencies for performance graphs:**
```bash
pip install matplotlib
# or with uv:
uv pip install matplotlib
# or install all optional dependencies:
uv sync --extra visualization
```

### Running Benchmarks

**Quick Start - Run all benchmarks and generate reports:**
```bash
./run_benchmarks.sh
```

**Fast iteration mode (fewer rounds):**
```bash
./run_benchmarks.sh --quick
```

This will:
1. Run all configured benchmarks
2. Save JSON results to `results/`
3. Generate individual markdown reports
4. Create a comparison summary report
5. Generate performance visualization graphs (if matplotlib is installed)

**Manual benchmark execution:**

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
uv run python tools/generate_report.py results/output.json results/output_report.md
```

Generate comparison report:
```bash
uv run python tools/generate_comparison.py results/file1.json results/file2.json results/comparison.md
```

Generate performance visualization graphs:
```bash
uv run python tools/generate_graphs.py
```

This creates SVG graphs in `results/graphs/`:

**Per-dataset comparisons** (tools compared within each dataset):
- `svedala_comparison.svg` - Svedala: load time, memory, and query performance
- `svedala_detailed.svg` - Svedala: detailed metrics with network elements
- `realgrid_comparison.svg` - RealGrid: load time, memory, and query performance
- `realgrid_detailed.svg` - RealGrid: detailed metrics with network elements

**Cross-dataset comparisons** (both tools across both datasets):
- `import_comparison.svg` - Import/load time comparison
- `memory_comparison.svg` - Memory usage comparison
- `query_comparison.svg` - Query performance comparison

**Adding new benchmarks to the runner:**

Edit `run_benchmarks.sh` and add to the `BENCHMARKS` array:
```bash
BENCHMARKS=(
    "benchmarks/triplets_svedala_benchmark.py:triplets_svedala:Triplets-Svedala"
    "benchmarks/pypowsybl_svedala_benchmark.py:pypowsybl_svedala:PyPowSyBl-Svedala"
    "benchmarks/triplets_realgrid_benchmark.py:triplets_realgrid:Triplets-RealGrid"
    "benchmarks/pypowsybl_realgrid_benchmark.py:pypowsybl_realgrid:PyPowSyBl-RealGrid"
    "benchmarks/cimpy_svedala_benchmark.py:cimpy_svedala:CIMpy-Svedala"  # Add new benchmark here
)
```

## Benchmark Results

Latest results on AMD Ryzen AI 9 HX 370, 64GB RAM, Python 3.13.12:

### Comparison Summary

**Small Dataset (Svedala - 7.3 MB):**

| Library | Version | Load Time | Memory | Query Speed | Elements |
|---------|---------|-----------|--------|-------------|----------|
| **triplets** | 0.0.17 | 122.2 ms | 27.6 MB | 6.1-18.3 ms | 97 lines, 39 gen, 73 loads |
| **pypowsybl** | 1.14.0 | 479.1 ms | 894.2 MB | 287-319 μs | 97 lines, 39 gen, 73 loads |

**Large Dataset (RealGrid - 86.5 MB):**

| Library | Version | Load Time | Memory | Query Speed | Elements |
|---------|---------|-----------|--------|-------------|----------|
| **triplets** | 0.0.17 | 1.32 s | 516.9 MB | 62-190 ms | 7561 lines, 1347 gen, 6687 loads |
| **pypowsybl** | 1.14.0 | 4.84 s | 3956.0 MB | 4.8-49.9 ms | 7561 lines, 1347 gen, 6687 loads |

**Key Insights:**
- **Load Time Scaling**: Both libraries scale approximately linearly with dataset size (~11-12x increase for 12x larger dataset)
- **Memory Scaling**: Triplets: 19x increase; PyPowSyBl: 4.4x increase
- **Query Performance**: PyPowSyBl maintains sub-millisecond to low-millisecond performance even on large datasets
- **Use Cases**:
  - **triplets**: Fast loading, low memory, RDF data extraction, batch processing
  - **pypowsybl**: Rich network model, fast queries, power flow analysis, TSO applications

### Import Performance Comparison

![Import Performance](results/graphs/import_comparison.svg)

*Cross-dataset comparison showing how both tools scale from small (7.3 MB) to large (86.5 MB) datasets*

### Detailed Results: Svedala IGM Dataset (7.3 MB, CGMES 3.0)

#### triplets - RDF/Pandas Parser
- **Load Time**: 122.2 ms
- **Memory**: 27.6 MB
- **Data Structure**: ~95,000 triplets, ~14,500 unique objects
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 substations
- **Query Performance**: 6.1-18.3 ms (type-based queries)
- **Strengths**: Fast loading, minimal memory, simple API, pandas integration
- **Use Case**: Data extraction, batch processing, RDF manipulation, quick analysis

#### pypowsybl - Power System Network Model
- **Load Time**: 479.1 ms (3.9x slower than triplets)
- **Memory**: 894.2 MB (32x more than triplets)
- **Network Elements**: 97 lines (90 + 7 dangling), 39 generators, 73 loads, 56 substations
- **Query Performance**: 287-319 μs (20-60x faster than triplets)
- **Strengths**: Rich network model, sub-millisecond queries, analysis-ready, includes dangling lines
- **Use Case**: Power flow analysis, network operations, TSO applications, CGMES validation

### Detailed Results: RealGrid Dataset (86.5 MB, CGMES 2.4.15)

#### triplets - RDF/Pandas Parser
- **Load Time**: 1.32 s
- **Memory**: 516.9 MB
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads (EnergyConsumer), 4875 substations
- **Query Performance**: 62-190 ms (consistent with small dataset)
- **Strengths**: Linear scaling, handles large datasets efficiently
- **Use Case**: Large-scale data processing, European grid analysis

#### pypowsybl - Power System Network Model
- **Load Time**: 4.84 s (3.7x slower than triplets)
- **Memory**: 3956.0 MB (7.7x more than triplets)
- **Network Elements**: 7561 lines, 1347 generators, 6687 loads, 4791 substations
- **Query Performance**: 4.8-49.9 ms (significantly faster than triplets)
- **Strengths**: Fast queries even on large datasets, comprehensive network model
- **Use Case**: Pan-European grid analysis, large TSO networks, production systems


See `tools/*/README.md` for detailed per-tool documentation and analysis.

## Planned Test Additions

## Parsers/Serializers

| Status | Tool / Library | Language | Main Purpose / Strength | Triplet / Graph Access? | CGMES / CIM Support | GitHub / Source | Notes |
|--------|----------------|----------|-------------------------|------------------------|---------------------|-----------------|-------|
| ✅ | **triplets** | Python | Pandas-based RDF parser | Yes (DataFrame triplets) | Version-agnostic CIM/CGMES | [triplets](https://github.com/Haigutus/triplets) | Fast loading, low memory, simple API |
| ✅ | **pypowsybl** | Python | PowSyBl wrapper (network import/export) | Indirect (via network objects) | CGMES import/export | [powsybl/pypowsybl](https://github.com/powsybl/pypowsybl) | Grid-analysis oriented; rich network model |
| 📋 | **CIMantic Graphs** | Python | In-memory labeled property graph | Yes (strong, knowledge graph API) | CIM15–18, custom profiles | [PNNL-CIM-Tools/CIM-Graph](https://github.com/PNNL-CIM-Tools/CIM-Graph) | Modern API, SPARQL-like queries |
| 📋 | **cimpy** | Python | Import/export/modify CGMES XML/RDF | Yes (via RDFlib backend) | CGMES / IEC61970 focused | [sogno-platform/cimpy](https://github.com/sogno-platform/cimpy) | Battle-tested in European projects |
| 📋 | **libcimpp** | C++ | Fast serialize/deserialize CIM XML/RDF | Partial (object model) | CGMES / IEC61970/61968/62325 | [sogno-platform/libcimpp](https://github.com/sogno-platform/libcimpp) | Likely fastest/lowest memory |
| 📋 | **pycgmes** | Python | Dataclasses + RDF schema + SHACL | Yes (dataclass mapping) | CGMES 3.0+ | [alliander-opensource/pycgmes](https://github.com/alliander-opensource/pycgmes) | Strong SHACL validation |
| 📋 | **OpenCGMES** | Java | Suite for CGMES / CIM RDF parser | Yes (CIMXML parser) | CGMES / IEC61970-552 | [SOPTIM/OpenCGMES](https://github.com/SOPTIM/OpenCGMES) | Recent CIMXML-specific fixes |
| 📋 | **rdflib** | Python | Generic RDF parser/triple store | Excellent (native triples) | None (generic) | [RDFLib/rdflib](https://github.com/RDFLib/rdflib) | Baseline for speed/memory comparison |
| 📋 | **Apache Jena** | Java | RDF framework + CIMXML parser | Excellent | Potential via custom parser | [apache/jena](https://github.com/apache/jena) | Generic + 2025 CIMXML branch |
| 📋 | **CIMverter** | Java/C++ | Convert CIM RDF to Modelica | Partial | CGMES compatible | [cim-iec/cimverter](https://github.com/cim-iec/cimverter) | Round-trip fidelity testing |
| 📋 | **CIMDraw** | Web/JS | View/edit CGMES node-breaker models | Indirect | ENTSO-E CGMES profile | [danielePala/CIMDraw](https://github.com/danielePala/CIMDraw) | Visual completeness check |
| 📋 | **GraphDB** | Java | Graph database with RDF support | Excellent | Generic RDF | [Ontotext GraphDB](https://www.ontotext.com/products/graphdb/) | Enterprise SPARQL database |
| 📋 | **GridCal/VeraGrid** | Python | Power systems analysis with UI | Indirect (grid model) | CGMES import support | [SanPen/GridCal](https://github.com/SanPen/GridCal) | Academia/industry tool, 500+ stars |
| 📋 | **CIMbion** | TBD | CIM/CGMES data management | TBD | CGMES | [Veracity Store](https://store.veracity.com/cimbion) | Closed source, commercial |
| 📋 | **CIMdesk** | Various | CIM data management | TBD | CGMES | TBD | To be investigated |

**Legend:**
- ✅ Benchmarked
- 📋 Planned

### 📊 Additional Benchmarks

| Test Category | Description | Metrics | Why Important |
|---------------|-------------|---------|---------------|
| **Export/Serialization** | Write loaded CIM data back to RDF/XML | Time, file size, memory | Round-trip capability, data export use cases |
| **Round-trip Fidelity** | Load → Export → Load → Diff check | Time, diff count, data loss % | Data integrity, lossless conversion verification |
| **SHACL Validation** | Validate CIM models against SHACL shapes | Time, violations found, memory | Data quality, CGMES compliance checking |
| **SPARQL Queries** | Complex graph queries on loaded data | Query time, result count | Advanced data extraction, relationship queries |


### 📁 Planned Datasets

| Dataset | Size | CGMES Version | Network Type | Elements | Status | Purpose |
|---------|------|---------------|--------------|----------|--------|---------|
| **Svedala IGM** | 7.3 MB | CGMES 3.0 | Small (Sweden) | 97 lines, 39 gen, 73 loads, 56 subs | ✅ Active | Fast iteration, baseline tests |
| **RealGrid** | 86.5 MB (3.7 MB compressed) | CGMES 2.4.15 | Large (Pan-European) | 10,000+ elements | ✅ Active | Scalability, real-world TSO scenarios |
| **NC Profiles** | ~50-100 MB | CGMES 3.0 | Medium (ENTSO-E) | TBD | 📋 Planned | Network Code validation, cross-border |

**Comparison Targets**:
- **Small (Svedala)**: Fast parsing, edge case testing, CI/CD friendly
- **Large (RealGrid)**: Memory stress, scalability limits, production-scale performance

### 📈 Performance Visualizations

Performance graphs are automatically generated when running `./run_benchmarks.sh` (requires matplotlib).

**Visualization Types:**

#### Per-Dataset Comparisons
Graphs grouped by **dataset** showing tool comparisons side-by-side:

**Svedala Dataset (7.3 MB)**
- **Comparison**: Load time, memory, and average query performance for both tools
  - `results/graphs/svedala_comparison.svg`
- **Detailed**: Load time, memory, lines parsed, generators parsed
  - `results/graphs/svedala_detailed.svg`

**RealGrid Dataset (86.5 MB)**
- **Comparison**: Load time, memory, and average query performance for both tools
  - `results/graphs/realgrid_comparison.svg`
- **Detailed**: Load time, memory, lines parsed, generators parsed
  - `results/graphs/realgrid_detailed.svg`

#### Cross-Dataset Comparisons
Graphs showing both tools across both datasets for each metric:

- **Import Comparison**: Load/import time for both tools on both datasets
  - `results/graphs/import_comparison.svg`
- **Memory Comparison**: Memory usage for both tools on both datasets
  - `results/graphs/memory_comparison.svg`
- **Query Comparison**: Average query performance for both tools on both datasets
  - `results/graphs/query_comparison.svg`

**Metrics visualized**:
- Import/load time (ms)
- Memory usage (MB)
- Query performance (ms)
- Network elements parsed (lines, generators, loads, substations)

*All graphs are generated in SVG format for scalability and web compatibility*

### 🔧 Planned Infrastructure Changes

**Goal**: Isolated, reproducible benchmark environment per parser

#### Docker-based Testing
- **One container per parser/tool** with all dependencies pre-installed
- **Standardized test interface**: Same input datasets, same output format
- **Resource limits**: CPU/memory constraints for fair comparison
- **Version pinning**: Lock parser versions for reproducible results

#### Benefits
- ✅ No dependency conflicts between parsers
- ✅ Easy CI/CD integration
- ✅ Reproducible across different machines
- ✅ Clean test environment per run
- ✅ Support for Java/C++/Python/JS parsers without local installs

#### Structure
```
benchmarks/
├── docker/
│   ├── triplets/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── pypowsybl/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── cimpy/
│   ├── libcimpp/
│   └── ...
├── run_all_benchmarks.sh
└── collect_results.py
```

#### Execution Flow
```bash
# Run all benchmarks in containers
./benchmarks/run_all_benchmarks.sh

# Results collected to results/ with standardized JSON format
# Auto-generate comparison reports
```





## Contributing

Add new benchmark cases in the `benchmarks/` directory following the existing patterns.
