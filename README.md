# Programming Assignments

Solutions for concurrent programming and data analysis assignments.

## Structure

```
assignment/
├── src/
│   ├── producer_consumer/
│   │   ├── buffer.py
│   │   ├── producer.py
│   │   ├── consumer.py
│   │   └── main.py
│   └── sales_analysis/
│       ├── models.py
│       ├── csv_reader.py
│       ├── analyzer.py
│       └── main.py
├── tests/
│   ├── test_producer_consumer.py
│   └── test_sales_analysis.py
├── data/
│   └── sales_data.csv
├── generate_data.py
├── setup.sh
└── run.sh
```

## Setup

```bash
chmod +x setup.sh run.sh
./setup.sh
```

## Usage

```bash
./run.sh          # Run both assignments
./run.sh 1        # Run Producer-Consumer
./run.sh 2        # Run Sales Analysis
./run.sh test     # Run tests
./run.sh generate # Generate new sales data
```

## Assignment 1: Producer-Consumer

Thread synchronization with bounded buffer:
- Condition variables for wait/notify
- Thread-safe put/get operations
- Blocking and non-blocking variants

## Assignment 2: Sales Data Analysis

Functional programming with CSV data:
- map, filter, reduce operations
- Lambda expressions
- Grouping and aggregation
- Stream-like processing
