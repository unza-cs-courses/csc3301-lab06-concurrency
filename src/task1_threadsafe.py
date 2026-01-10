"""
Lab 6 Task 1: Thread-Safe Counter
Fix the race condition in BrokenCounter using three different approaches.
"""
import threading

class BrokenCounter:
    """This counter has a race condition - DO NOT MODIFY."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        current = self.count
        self.count = current + 1
    
    def get_value(self):
        return self.count


class FixedCounterLock:
    """Fix using threading.Lock."""
    # YOUR CODE HERE
    pass


class FixedCounterRLock:
    """Fix using threading.RLock (reentrant lock)."""
    # YOUR CODE HERE
    pass


def test_counter(counter_class, name, num_threads=10, increments_per_thread=1000):
    """Test a counter class for thread safety."""
    counter = counter_class()
    threads = []
    
    def worker():
        for _ in range(increments_per_thread):
            counter.increment()
    
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    expected = num_threads * increments_per_thread
    actual = counter.get_value()
    status = "PASS" if actual == expected else "FAIL"
    print(f"{name}: expected={expected}, actual={actual} - {status}")
    return actual == expected


if __name__ == "__main__":
    print("Testing thread safety:\n")
    test_counter(BrokenCounter, "BrokenCounter (expect FAIL)")
    test_counter(FixedCounterLock, "FixedCounterLock")
    test_counter(FixedCounterRLock, "FixedCounterRLock")
