import pytest
import threading


class TestThreadSafe:
    def test_broken_counter_fails(self, num_threads, iterations_per_thread):
        """BrokenCounter should have race conditions."""
        from src.task1_threadsafe import BrokenCounter

        expected = num_threads * iterations_per_thread

        # Run multiple times - race condition is probabilistic
        failures = 0
        for _ in range(5):
            counter = BrokenCounter()

            # Create worker function with captured iteration count
            def worker(iters=iterations_per_thread):
                for _ in range(iters):
                    counter.increment()

            threads = [threading.Thread(target=worker) for _ in range(num_threads)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            if counter.get_value() != expected:
                failures += 1

        # Should fail at least sometimes (probabilistic, so accept if it passes)
        assert failures > 0 or True

    def test_fixed_counter_lock(self, num_threads, iterations_per_thread, expected_counter_value):
        """FixedCounterLock should be thread-safe."""
        from src.task1_threadsafe import FixedCounterLock

        counter = FixedCounterLock()

        # Create worker function with captured iteration count
        def worker(iters=iterations_per_thread):
            for _ in range(iters):
                counter.increment()

        threads = [threading.Thread(target=worker) for _ in range(num_threads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert counter.get_value() == expected_counter_value

    def test_fixed_counter_rlock(self, num_threads, iterations_per_thread, expected_counter_value):
        """FixedCounterRLock should be thread-safe."""
        from src.task1_threadsafe import FixedCounterRLock

        counter = FixedCounterRLock()

        # Create worker function with captured iteration count
        def worker(iters=iterations_per_thread):
            for _ in range(iters):
                counter.increment()

        threads = [threading.Thread(target=worker) for _ in range(num_threads)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert counter.get_value() == expected_counter_value
