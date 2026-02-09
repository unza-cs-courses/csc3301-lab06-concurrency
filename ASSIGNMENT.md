# Lab 6: Concurrency and Parallelism

**CSC3301 Programming Language Paradigms**
**Student ID:** concurrency
**Points:** 100

---

## Your Personalized Assignment

This assignment has been customized for you based on your student ID. Your specific test parameters are:

- **Thread Count:** 10 threads
- **Iterations per Thread:** 250
- **Expected Counter Value:** 2500
- **Data Size:** 400 items
- **Pipeline Stages:** 6
- **Workers per Stage:** 3
- **Test Timeout:** 5 seconds

---

## Task 1: Thread-Safe Counter (20 points)

Fix the race condition in `BrokenCounter` using different synchronization approaches.

### Requirements

In `src/task1_threadsafe.py`, implement the following classes:

1. **FixedCounterLock** - Use `threading.Lock` to protect the counter
2. **FixedCounterRLock** - Use `threading.RLock` (reentrant lock) for thread safety

Each class must have:
- `__init__(self)` - Initialize counter to 0
- `increment(self)` - Thread-safe increment operation
- `get_value(self)` - Return current counter value

### Testing Your Implementation

Your counter must handle **10 threads** each performing **250 increments**.
The final value must be exactly **2500**.

```python
# Test your implementation:
python src/task1_threadsafe.py
```

---

## Task 2: Concurrent Web Scraper (30 points)

Implement a URL fetcher using multiple concurrency approaches.

### Requirements

In `src/task2_scraper.py`, implement:

1. **fetch_sequential(urls)** - Fetch URLs one at a time
2. **fetch_threaded(urls)** - Use `ThreadPoolExecutor`
3. **fetch_async(urls)** - Use `asyncio` and `aiohttp`
4. **fetch_multiprocess(urls)** - Use `ProcessPoolExecutor`

Your implementation will be tested with **20 URLs** and must complete within **5 seconds**.

---

## Task 3: Producer-Consumer Pipeline (25 points)

Build a multi-stage processing pipeline with configurable workers.

### Requirements

In `src/task3_pipeline.py`, implement a pipeline with:

- **6 processing stages**
- **3 workers per stage**
- **Queue size:** 20
- **Process 400 items** through the pipeline

The pipeline must:
- Use `queue.Queue` for inter-stage communication
- Handle graceful shutdown
- Report processing statistics

---

## Task 4: Integration Challenge (25 points)

Combine threading, functional transformations, and OOP in a real-time analytics system.

### Requirements

In `src/task4_integration.py`, create an analytics system that:

- Processes **400 data points**
- Uses **10 worker threads**
- Completes within **5 seconds**
- Combines functional transformations with concurrent processing

---

## Grading

| Task | Points | Criteria |
|------|--------|----------|
| Task 1 | 20 | Both counter implementations pass thread-safety tests |
| Task 2 | 30 | All four approaches work correctly and show performance differences |
| Task 3 | 25 | Pipeline processes all items correctly with proper synchronization |
| Task 4 | 25 | Integration works correctly with specified parameters |

---

## Submission

1. Complete all tasks in the `src/` directory
2. Run `pytest tests/visible/` to verify your solutions
3. Push your changes to trigger autograding

**Due Date:** See course schedule

---

*This is a personalized assignment. Do not share your specific parameters with other students.*
