"""
Example benchmark for CIM parsers.

Add your actual parser implementations and benchmark cases here.
"""

import pytest


class ExampleParser:
    """Placeholder parser - replace with actual CIM parser implementations."""

    def parse(self, data: str):
        """Parse CIM data."""
        return {"parsed": True, "data": data}

    def serialize(self, obj: dict) -> str:
        """Serialize data to CIM format."""
        return str(obj)


@pytest.fixture
def sample_cim_data():
    """Provide sample CIM data for benchmarking."""
    # Replace with actual CIM data
    return """<cim:SampleData>
    <cim:value>test</cim:value>
</cim:SampleData>"""


@pytest.fixture
def parser():
    """Provide parser instance."""
    return ExampleParser()


def test_parse_benchmark(benchmark, parser, sample_cim_data):
    """Benchmark parsing performance."""
    result = benchmark(parser.parse, sample_cim_data)
    assert result is not None


def test_serialize_benchmark(benchmark, parser):
    """Benchmark serialization performance."""
    data = {"test": "value", "nested": {"key": "value"}}
    result = benchmark(parser.serialize, data)
    assert result is not None
