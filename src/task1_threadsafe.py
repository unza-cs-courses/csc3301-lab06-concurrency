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


class ThreadSafeCounter:
    """
    A thread-safe counter that supports increment, decrement, and value retrieval.

    This counter uses a Lock to ensure all operations are atomic and thread-safe.
    Multiple threads can safely call increment(), decrement(), and get_value()
    concurrently without race conditions or data loss.

    Thread Safety Guarantees:
    - All operations (increment, decrement, get_value) are atomic
    - No lost updates from concurrent modifications
    - Consistent snapshots of counter state when reading
    """

    def __init__(self, initial=0):
        """
        Initialize the counter with an optional starting value.

        Args:
            initial (int): The starting value for the counter (default: 0)
        """
        # TODO: Implement initialization with lock
        raise NotImplementedError("Students should implement __init__")

    def increment(self):
        """
        Atomically increment the counter by 1.

        Thread-safe: This operation is protected and will not interfere with
        concurrent increments or decrements from other threads.
        """
        # TODO: Implement thread-safe increment
        raise NotImplementedError("Students should implement increment()")

    def decrement(self):
        """
        Atomically decrement the counter by 1.

        Thread-safe: This operation is protected and will not interfere with
        concurrent increments or decrements from other threads.
        """
        # TODO: Implement thread-safe decrement
        raise NotImplementedError("Students should implement decrement()")

    def get_value(self):
        """
        Get the current value of the counter.

        Thread-safe: Returns a consistent snapshot of the counter state.

        Returns:
            int: The current value of the counter
        """
        # TODO: Implement thread-safe value retrieval
        raise NotImplementedError("Students should implement get_value()")


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
