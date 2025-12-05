# Programming Assignments

Python solutions for concurrent programming and data analysis assignments.

## Requirements Checklist

### Assignment 1: Producer-Consumer Pattern
- [x] Thread synchronization using `threading.Condition`
- [x] Concurrent programming with multiple threads
- [x] Blocking queue implementation (BoundedBuffer)
- [x] Wait/Notify mechanism for thread coordination
- [x] Producer reads from source container
- [x] Consumer stores items in destination container

### Assignment 2: Sales Data Analysis
- [x] Functional programming patterns
- [x] Stream operations using `map`, `filter`, `reduce`
- [x] Data aggregation and grouping
- [x] Lambda expressions throughout
- [x] CSV file reading and parsing
- [x] Multiple analytical queries

## Project Structure

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
├── generate_data.py           
├── setup.sh                   
├── run.sh                     
└── README.md
```

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/prth1234/uptime_crew_assignment.git
cd uptime_crew_assignment

# Make scripts executable
chmod +x setup.sh run.sh
./setup.sh
```

## Usage

```bash
./run.sh          # Run both assignments
./run.sh 1        # Run Assignment 1 only
./run.sh 2        # Run Assignment 2 only
./run.sh test     # Run unit tests
./run.sh generate # Generate new sales data
```

## Sample Output

### Assignment 1: Producer-Consumer

```
==================================================
Producer-Consumer Pattern Demonstration
==================================================

Configuration:
  Items to transfer: 10
  Buffer capacity:   3
  Producer delay:    0.1s
  Consumer delay:    0.15s

Starting threads...

[Producer] Started
[Consumer] Started
[Producer] Produced: Item_1
[Consumer] Consumed: Item_1
[Producer] Produced: Item_2
[Consumer] Consumed: Item_2
...
[Producer] Finished - produced 10 items
[Consumer] Finished - consumed 10 items

==================================================
Results
==================================================

Items produced: 10
Items consumed: 10
Items in destination: 10
Time elapsed: 1.64s

SUCCESS: All items transferred correctly!
  Order preserved: Yes
```

### Assignment 2: Sales Analysis

```
Sales Data Analysis
--------------------------------------------------
Loaded 1000 sales records

==================================================
  Basic Statistics
==================================================
Total Records:       1000
Total Revenue:       $583,657.98
Average Order Value: $583.66
Total Quantity Sold: 5361

==================================================
  Sales by Category
==================================================

  Electronics
    Revenue:    $337,406.50 (57.8%)
    Orders:     245
    Avg Order:  $1,377.17

  Home & Garden
    Revenue:    $89,701.77 (15.4%)
    Orders:     241
    Avg Order:  $372.21
...

==================================================
  Top 5 Products by Revenue
==================================================
  1. Laptop Pro: $171,182.63
  2. Tablet 10inch: $46,681.35
  3. Monitor 27inch: $36,909.78
  4. Smart Watch: $29,094.30
  5. Air Purifier: $23,486.01

==================================================
  Monthly Sales Trends
==================================================
  2024-01: $55,401.86 (92 orders)
  2024-02: $58,620.02 (81 orders)
  ...

==================================================
  Analysis Complete
==================================================
```

## Running Tests

```bash
./run.sh test
```

Output:
```
Ran 25 tests in 0.005s
OK
```

## Technical Details

### Assignment 1: Thread Synchronization
- `BoundedBuffer`: Thread-safe queue using `threading.Condition`
- `put()`: Blocks when buffer is full (wait/notify)
- `get()`: Blocks when buffer is empty (wait/notify)
- `Producer`: Reads from source list, puts items in buffer
- `Consumer`: Gets items from buffer, stores in destination

### Assignment 2: Functional Programming
- `reduce()`: Calculates total revenue
- `map()`: Transforms sales data
- `filter()`: Filters by category, region, price
- `lambda`: Used for sorting, filtering, aggregation
- Grouping: By category, region, month, product
