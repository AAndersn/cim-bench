# Triplets

## Version Tested
- triplets 0.0.17
- pandas 3.0.1
- Python 3.14.2

## Description
Triplets is a Python library for parsing CIM RDF/XML data to pandas DataFrames. It's version and namespace agnostic and can handle both XML and ZIP files.

## Repository
- GitHub: https://github.com/Baltic-RCC/triplets
- Documentation: https://haigutus.github.io/triplets/

## Installation
```bash
pip install triplets
```

## Environment
- OS: Linux (Fedora 43)
- CPU: AMD Ryzen AI 9 HX 370
- RAM: 64 GB
- Python: 3.14.2

## Benchmark Results (2026-02-19)

### Test Dataset: Svedala IGM (ENTSO-E)
Dataset location: `data/relicapgrid/Instance/Grid/IGM_Svedala/`

#### EQ Profile Only (3.8 MB)
- **Load time**: 55.0 ms (mean)
- **Memory usage**: 17.4 MB
- **Triplets loaded**: 47,718
- **Unique objects**: 8,231

#### Full CGMES Model (EQ + SSH + SV + TP, 7.2 MB)
- **Load time**: 123.6 ms (mean)
- **Memory usage**: 23.0 MB
- **Triplets loaded**: 94,861
- **Unique objects**: 14,456
- **Profiles**: 4 files (EQ, SSH, SV, TP)

#### Query Performance (ACLineSegment)
- **Query time**: 12.3 ms (mean)
- **Results**: 97 objects

## Performance Characteristics
- Fast loading times for medium-sized datasets
- Low memory footprint
- DataFrame-based structure allows for efficient querying with pandas operations
- Scales linearly with file size

## Known Limitations
- Memory usage increases linearly with dataset size
- Large datasets (>100 MB) may require significant memory
- Query performance depends on pandas DataFrame operations

## API Highlights
```python
from triplets.rdf_parser import load_RDF_to_dataframe, type_tableview

# Load CIM file
df = load_RDF_to_dataframe("file.xml")

# Query by type
aclines = type_tableview(df, "ACLineSegment")

# DataFrame columns: [ID, KEY, VALUE, INSTANCE_ID]
```
