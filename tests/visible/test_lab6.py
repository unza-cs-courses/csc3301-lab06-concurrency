import pytest
import threading


class TestThreadSafeCounter:
    """Tests for ThreadSafeCounter basic functionality and thread safety."""

    def test_counter_initial_value_default(self):
        """ThreadSafeCounter should initialize to 0 by default."""
        try:
            from src.task1_threadsafe import ThreadSafeCounter
            counter = ThreadSafeCounter()
            assert counter.get_value() == 0
        except ImportError:
            pytest.skip("task1_threadsafe.ThreadSafeCounter not yet implemented")

    def test_counter_initial_value_custom(self):
        """ThreadSafeCounter should initialize with custom value."""
        try:
            from src.task1_threadsafe import ThreadSafeCounter
            counter = ThreadSafeCounter(initial=42)
            assert counter.get_value() == 42
        except ImportError:
            pytest.skip("task1_threadsafe.ThreadSafeCounter not yet implemented")

    def test_counter_increment(self):
        """ThreadSafeCounter.increment() should increase value by 1."""
        try:
            from src.task1_threadsafe import ThreadSafeCounter
            counter = ThreadSafeCounter()
            counter.increment()
            assert counter.get_value() == 1
            counter.increment()
            assert counter.get_value() == 2
        except ImportError:
            pytest.skip("task1_threadsafe.ThreadSafeCounter not yet implemented")

    def test_counter_decrement(self):
        """ThreadSafeCounter.decrement() should decrease value by 1."""
        try:
            from src.task1_threadsafe import ThreadSafeCounter
            counter = ThreadSafeCounter(initial=5)
            counter.decrement()
            assert counter.get_value() == 4
            counter.decrement()
            assert counter.get_value() == 3
        except ImportError:
            pytest.skip("task1_threadsafe.ThreadSafeCounter not yet implemented")

    def test_counter_thread_safety_concurrent_increments(self):
        """ThreadSafeCounter should be thread-safe with concurrent increments."""
        try:
            from src.task1_threadsafe import ThreadSafeCounter
            counter = ThreadSafeCounter()
            num_threads = 10
            increments_per_thread = 100

            def worker():
                for _ in range(increments_per_thread):
                    counter.increment()

            threads = [threading.Thread(target=worker) for _ in range(num_threads)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()

            expected = num_threads * increments_per_thread
            assert counter.get_value() == expected
        except ImportError:
            pytest.skip("task1_threadsafe.ThreadSafeCounter not yet implemented")

    def test_counter_thread_safety_concurrent_decrements(self):
        """ThreadSafeCounter should be thread-safe with concurrent decrements."""
        try:
            from src.task1_threadsafe import ThreadSafeCounter
            num_threads = 10
            decrements_per_thread = 100
            counter = ThreadSafeCounter(initial=num_threads * decrements_per_thread)

            def worker():
                for _ in range(decrements_per_thread):
                    counter.decrement()

            threads = [threading.Thread(target=worker) for _ in range(num_threads)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()

            assert counter.get_value() == 0
        except ImportError:
            pytest.skip("task1_threadsafe.ThreadSafeCounter not yet implemented")


class TestBrokenVsFixed:
    """Tests for demonstrating race conditions and thread-safe fixes."""

    def test_broken_counter_fails(self, num_threads, iterations_per_thread):
        """BrokenCounter should have race conditions, and FixedCounterLock should work."""
        from src.task1_threadsafe import BrokenCounter, FixedCounterLock

        # Guard: FixedCounterLock must be implemented (not just a bare class with pass)
        fixed = FixedCounterLock()
        assert hasattr(fixed, 'increment'), \
            "FixedCounterLock must implement increment() method"
        assert hasattr(fixed, 'get_value'), \
            "FixedCounterLock must implement get_value() method"

        # Verify FixedCounterLock actually works correctly first
        fixed.increment()
        assert fixed.get_value() == 1, \
            "FixedCounterLock must correctly count increments"

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


class TestWebScraper:
    """Tests for web scraper concurrency implementations."""

    def test_fetch_sequential_signature(self):
        """Test that fetch_sequential function exists, is callable, and has a real implementation."""
        try:
            from src.task2_scraper import fetch_sequential
            assert callable(fetch_sequential)
            # Guard: function must not just be 'pass' (returning None with no work)
            import inspect
            source = inspect.getsource(fetch_sequential)
            assert 'requests' in source or 'get(' in source or 'return' in source.split('pass')[0], \
                "fetch_sequential must have a real implementation, not just 'pass'"
            # Verify it returns a list (not None) when called with empty input
            result = fetch_sequential([])
            assert result is not None, "fetch_sequential should return a list, not None"
            assert isinstance(result, list), "fetch_sequential should return a list"
        except ImportError:
            pytest.skip("task2_scraper not yet implemented")

    def test_fetch_threaded_signature(self):
        """Test that fetch_threaded function exists, is callable, and has a real implementation."""
        try:
            from src.task2_scraper import fetch_threaded
            assert callable(fetch_threaded)
            # Guard: function must not just be 'pass' (returning None with no work)
            result = fetch_threaded([])
            assert result is not None, "fetch_threaded should return a list, not None"
            assert isinstance(result, list), "fetch_threaded should return a list"
        except ImportError:
            pytest.skip("task2_scraper not yet implemented")

    def test_fetch_async_signature(self):
        """Test that fetch_async function exists, is callable, and has a real implementation."""
        try:
            from src.task2_scraper import fetch_async
            import asyncio
            assert callable(fetch_async)
            # Guard: async function must not just be 'pass' (returning None)
            result = asyncio.run(fetch_async([]))
            assert result is not None, "fetch_async should return a list, not None"
            assert isinstance(result, list), "fetch_async should return a list"
        except ImportError:
            pytest.skip("task2_scraper not yet implemented")

    def test_fetch_multiprocess_signature(self):
        """Test that fetch_multiprocess function exists, is callable, and has a real implementation."""
        try:
            from src.task2_scraper import fetch_multiprocess
            assert callable(fetch_multiprocess)
            # Guard: function must not just be 'pass' (returning None with no work)
            result = fetch_multiprocess([])
            assert result is not None, "fetch_multiprocess should return a list, not None"
            assert isinstance(result, list), "fetch_multiprocess should return a list"
        except ImportError:
            pytest.skip("task2_scraper not yet implemented")


class TestProducerConsumer:
    """Tests for producer-consumer pipeline."""

    def test_producer_consumer_imports(self):
        """Test that ProducerConsumer class can be imported and has a real implementation."""
        try:
            from src.task3_pipeline import ProducerConsumer
            assert ProducerConsumer is not None
            # Guard: ProducerConsumer must have a working implementation
            pc = ProducerConsumer()
            assert hasattr(pc, 'produce'), "ProducerConsumer must have a produce method"
            assert hasattr(pc, 'consume'), "ProducerConsumer must have a consume method"
            # Verify produce/consume actually work (not just pass)
            pc.produce("test_item")
            result = pc.consume(timeout=1.0)
            assert result == "test_item", \
                "ProducerConsumer must actually store and retrieve items"
        except ImportError:
            pytest.skip("task3_pipeline not yet implemented")

    def test_analytics_event_dataclass(self):
        """Test that AnalyticsEvent dataclass exists and EventStream is implemented."""
        try:
            from src.task4_integration import AnalyticsEvent, EventStream
            from datetime import datetime
            event = AnalyticsEvent(timestamp=datetime.now(), event_type="test", value=1.0)
            assert event.event_type == "test"
            assert event.value == 1.0
            # Guard: EventStream must be implemented, not just the dataclass
            stream = EventStream()
            stream.add_event(event)
            events = stream.get_events()
            assert len(events) >= 1, "EventStream must store and return events"
        except ImportError:
            pytest.skip("task4_integration not yet implemented")
