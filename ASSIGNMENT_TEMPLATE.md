# Lab 6: Concurrency and Parallelism

**CSC3301 Programming Language Paradigms**
**Student ID:** {{STUDENT_ID}}
**Points:** 100

---

## Your Personalized Assignment

This assignment has been customized for you based on your student ID. Your specific test parameters are:

- **Thread Count:** {{NUM_THREADS}} threads
- **Iterations per Thread:** {{ITERATIONS_PER_THREAD}}
- **Expected Counter Value:** {{EXPECTED_COUNTER_VALUE}}
- **Data Size:** {{DATA_SIZE}} items
- **Pipeline Stages:** {{NUM_STAGES}}
- **Workers per Stage:** {{NUM_WORKERS}}
- **Test Timeout:** {{TEST_TIMEOUT}} seconds

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

Your counter must handle **{{NUM_THREADS}} threads** each performing **{{ITERATIONS_PER_THREAD}} increments**.
The final value must be exactly **{{EXPECTED_COUNTER_VALUE}}**.

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

Your implementation will be tested with **{{NUM_URLS}} URLs** and must complete within **{{SCRAPER_TIMEOUT}} seconds**.

---

## Task 3: Producer-Consumer Pipeline (25 points)

Build a multi-stage processing pipeline with configurable workers.

### Requirements

In `src/task3_pipeline.py`, implement a pipeline with:

- **{{NUM_STAGES}} processing stages**
- **{{NUM_WORKERS}} workers per stage**
- **Queue size:** {{QUEUE_SIZE}}
- **Process {{DATA_SIZE}} items** through the pipeline

The pipeline must:
- Use `queue.Queue` for inter-stage communication
- Handle graceful shutdown
- Report processing statistics

---

## Task 4: Integration Challenge (25 points)

Combine threading, functional transformations, and OOP in a real-time analytics system.

### Requirements

In `src/task4_integration.py`, create an analytics system that:

- Processes **{{DATA_SIZE}} data points**
- Uses **{{NUM_THREADS}} worker threads**
- Completes within **{{PROCESSING_TIMEOUT}} seconds**
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
