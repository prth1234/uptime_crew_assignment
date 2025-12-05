#!/bin/bash

if [ -d "venv" ]; then
    source venv/bin/activate
fi

if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
else
    PYTHON_CMD=python
fi

export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

case "$1" in
    1)
        echo "Running Assignment 1: Producer-Consumer"
        echo ""
        $PYTHON_CMD -m producer_consumer.main
        ;;
    2)
        echo "Running Assignment 2: Sales Analysis"
        echo ""
        $PYTHON_CMD -m sales_analysis.main
        ;;
    test)
        echo "Running Tests"
        echo ""
        $PYTHON_CMD -m unittest discover tests/ -v
        ;;
    generate)
        echo "Generating Sales Data (1000 records)"
        echo ""
        $PYTHON_CMD generate_data.py
        ;;
    *)
        echo "Running Assignment 1: Producer-Consumer"
        echo ""
        $PYTHON_CMD -m producer_consumer.main
        echo ""
        echo ""
        echo "Running Assignment 2: Sales Analysis"
        echo ""
        $PYTHON_CMD -m sales_analysis.main
        ;;
esac
