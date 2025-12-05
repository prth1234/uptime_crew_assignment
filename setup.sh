#!/bin/bash

echo "Setting up Python environment..."

if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
else
    PYTHON_CMD=python
fi

echo "Using: $($PYTHON_CMD --version)"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Generating sales data..."
$PYTHON_CMD generate_data.py

echo ""
echo "Setup complete!"
echo ""
echo "Usage:"
echo "  ./run.sh          Run both assignments"
echo "  ./run.sh 1        Run Assignment 1 (Producer-Consumer)"
echo "  ./run.sh 2        Run Assignment 2 (Sales Analysis)"
echo "  ./run.sh test     Run tests"
echo "  ./run.sh generate Generate new sales data"
