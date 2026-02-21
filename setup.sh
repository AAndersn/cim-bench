#!/bin/bash
set -e

# Install uv if not present
command -v uv &> /dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize git submodules
[ -d ".git" ] && git submodule update --init --recursive

# Install dependencies
uv sync --extra visualization



echo "✓ Setup complete! Run: ./run_benchmarks.sh"
