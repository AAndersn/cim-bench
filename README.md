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

**Adding new benchmarks to the runner:**

Edit `run_benchmarks.sh` and add to the `BENCHMARKS` array:
```bash
BENCHMARKS=(
    "benchmarks/test_triplets_benchmark.py:triplets:Triplets"
    "benchmarks/test_pypowsybl_benchmark.py:pypowsybl:PyPowSyBl"
    "benchmarks/test_cimpy_benchmark.py:cimpy:CIMpy"  # Add new benchmark here
)
```

## Benchmark Results

Latest results on AMD Ryzen AI 9 HX 370, 64GB RAM, Python 3.13.12:

### Comparison Summary

| Library | Version | Load Time | Memory | Query Speed | Use Case |
|---------|---------|-----------|--------|-------------|----------|
| **triplets** | 0.0.17 | 109.0 ms | 22.5 MB | 8.8 ms | RDF data extraction, low memory |
| **pypowsybl** | 1.14.0 | 443.2 ms | 1320 MB | 151 μs | Power analysis, network model |

### Detailed Results: Svedala IGM Dataset (7.3 MB, CGMES EQ+SSH+SV+TP)

#### triplets - RDF/Pandas Parser
- **Load Time**: 109.0 ms
- **Memory**: 22.5 MB
- **Data Structure**: 94,861 triplets, 14,456 unique objects
- **Network Elements**: 97 lines, 39 generators, 73 loads, 56 substations
- **Query Performance**: 8.8 ms (ACLineSegment type query)
- **Strengths**: Very fast loading, minimal memory, simple API
- **Use Case**: Data extraction, batch processing, RDF manipulation

#### pypowsybl - Power System Network Model
- **Load Time**: 443.2 ms (4.1x slower than triplets)
- **Memory**: 1319.5 MB (59x more than triplets)
- **Network Elements**: 105 buses, 90 lines, 39 generators, 73 loads, 57 substations
- **Query Performance**: 151-292 μs (30-58x faster than triplets)
- **Strengths**: Rich network model, sub-millisecond queries, analysis-ready
- **Use Case**: Power flow analysis, network operations, TSO applications


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
| 📋 | **cim-graph** | Python | CIM graph library | Yes (graph-based) | CIM/CGMES | [PyPI: cim-graph](https://pypi.org/project/cim-graph/) | Alternative graph implementation |
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
| **NC Profiles** | ~50-100 MB | CGMES 3.0 | Medium (ENTSO-E) | TBD | 📋 Planned | Network Code validation, cross-border |
| **RealGrid** | ~500+ MB | CGMES 2.4 | Large (Pan-European) | 10,000+ elements | 📋 Planned | Scalability, real-world TSO scenarios |

**Comparison Targets**:
- **Small (Svedala)**: Fast parsing, edge case testing, CI/CD friendly
- **Large (RealGrid)**: Memory stress, scalability limits, production-scale performance

### 📈 Planned Visualizations

**Performance Comparison Graphs** (small vs large datasets):

**Metrics to visualize**:
- Load time vs dataset size (scaling curve)
- Memory usage vs element count
- Query performance degradation at scale
- Export fidelity (data loss %) across parsers

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
