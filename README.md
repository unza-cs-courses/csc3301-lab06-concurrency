# Lab 6: Concurrency and Parallelism

**CSC3301 Programming Language Paradigms**
**Points:** 100

## Overview

This lab explores concurrent and parallel programming in Python, covering thread safety, synchronization primitives, and various concurrency models.

## Tasks

### Task 1: Thread-Safe Counter (20 points)
Fix the BrokenCounter race condition using Lock and RLock synchronization primitives.

### Task 2: Concurrent Web Scraper (30 points)
Implement URL fetcher using four approaches: sequential, ThreadPool, asyncio, and multiprocessing.
Benchmark and compare performance.

### Task 3: Producer-Consumer Pipeline (25 points)
Build a multi-stage processing pipeline with configurable workers per stage.

### Task 4: Integration Challenge (25 points)
Combine threading, functional transformations, and OOP in a real-time analytics system.

## Getting Started

1. Read your personalized `ASSIGNMENT.md` for specific test parameters
2. Implement solutions in the `src/` directory
3. Run tests with `pytest tests/visible/ -v`

## Variant System

This assignment uses a **variant-based system** to generate personalized test parameters for each student. This ensures academic integrity while maintaining consistent learning objectives.

### How It Works

1. **Automatic Generation**: When GitHub Classroom creates your repository, a GitHub Action automatically generates your unique variant based on your student ID.

2. **Deterministic Parameters**: The variant generator uses your student ID to deterministically generate:
   - Thread counts for concurrency tests
   - Iteration counts per thread
   - Data sizes for processing tasks
   - Pipeline stage configurations
   - Queue sizes and timeouts

3. **Personalized Assignment**: Your `ASSIGNMENT.md` file contains your specific test parameters. Use these values when implementing and testing your solutions.

### Variant Configuration

Your variant is stored in `.variant_config.json` and includes:

```json
{
  "student_id": "your_id",
  "counter_tests": {
    "num_threads": 10,
    "iterations_per_thread": 100,
    "expected_value": 1000
  },
  "scraper_tests": {
    "num_urls": 10,
    "timeout_seconds": 10
  },
  "pipeline_tests": {
    "num_stages": 4,
    "workers_per_stage": 3,
    "queue_size": 10,
    "data_size": 100
  }
}
```

### For Instructors

To manually generate a variant:

```bash
python scripts/variant_generator.py <student_id>
python scripts/generate_assignment.py
```

The variant system ensures:
- Each student has unique but consistent test parameters
- Tests remain compatible across all variants
- Plagiarism detection is simplified (different expected values)
- Fair grading (all variants have equivalent difficulty)

## Testing

The test suite uses pytest fixtures to load variant-specific parameters:

```python
def test_counter(num_threads, iterations_per_thread, expected_counter_value):
    # Test uses student-specific values from fixtures
    pass
```

Run visible tests:
```bash
pytest tests/visible/ -v
```

## File Structure

```
csc3301-lab06-concurrency/
├── src/
│   ├── __init__.py
│   └── task1_threadsafe.py      # Thread-safe counter implementations
├── tests/
│   ├── __init__.py
│   └── visible/
│       ├── __init__.py
│       ├── conftest.py          # Pytest fixtures with variant config
│       └── test_lab6.py         # Visible test cases
├── scripts/
│   ├── variant_generator.py     # Generate student variants
│   └── generate_assignment.py   # Generate personalized assignment
├── .github/
│   └── workflows/
│       ├── autograding.yml      # Run tests on push
│       └── generate-variant.yml # Generate variant on repo creation
├── ASSIGNMENT_TEMPLATE.md       # Template with placeholders
├── ASSIGNMENT.md                # Generated personalized assignment
├── .variant_config.json         # Generated variant configuration
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11+
- pytest >= 7.0.0
- aiohttp >= 3.0.0

Install dependencies:
```bash
pip install -r requirements.txt
```

## Submission

1. Complete all tasks in the `src/` directory
2. Ensure all visible tests pass
3. Push your changes to trigger autograding
4. Check the Actions tab for grading results
