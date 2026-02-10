"""
Task 3: Producer-Consumer Pipeline

This module implements a multi-stage processing pipeline where data flows through
different processing stages connected by queues.

Architecture:
- Each stage has one or more worker threads
- Data flows from one stage to the next via queues
- Stages operate concurrently, with data buffering between them

Use Cases:
- ETL (Extract, Transform, Load) pipelines
- Media processing (read -> resize -> compress -> save)
- Data validation (parse -> validate -> store)

Your implementation must handle:
- Thread-safe communication between stages
- Graceful shutdown
- Configurable workers per stage
"""

import queue
import threading
from typing import Callable, List, Any, Optional


class ProducerConsumer:
    """
    A simple producer-consumer queue wrapper.

    This class encapsulates queue.Queue and provides methods for producing
    and consuming items with optional timeouts.
    """

    def __init__(self, maxsize: int = 0):
        """
        Initialize the producer-consumer queue.

        Args:
            maxsize: Maximum queue size (0 = unlimited, which is recommended)
        """
        # TODO: Initialize a queue.Queue with the given maxsize
        pass

    def produce(self, item: Any, timeout: Optional[float] = None) -> None:
        """
        Add an item to the queue.

        Args:
            item: The item to add
            timeout: Optional timeout in seconds (None = block forever)

        Raises:
            queue.Full: If timeout expires and queue is full
        """
        # TODO: Put item on queue with optional timeout
        pass

    def consume(self, timeout: Optional[float] = None) -> Any:
        """
        Remove and return an item from the queue.

        Args:
            timeout: Optional timeout in seconds (None = block forever)

        Returns:
            The next item from the queue

        Raises:
            queue.Empty: If timeout expires before item is available
        """
        # TODO: Get item from queue with optional timeout
        pass

    def qsize(self) -> int:
        """
        Return the approximate size of the queue.

        Note: This is approximate because other threads may modify the queue
        between the call and when you use the value.

        Returns:
            Approximate number of items in the queue
        """
        # TODO: Return queue size
        pass


class PipelineStage:
    """
    A single stage in the processing pipeline.

    Each stage:
    - Consumes items from an input queue
    - Applies a transformation function
    - Produces items to an output queue
    - Runs in multiple worker threads for parallelism
    """

    def __init__(
        self,
        input_queue: ProducerConsumer,
        output_queue: ProducerConsumer,
        process_func: Callable,
        num_workers: int = 1,
        stage_name: str = "Stage",
    ):
        """
        Initialize a pipeline stage.

        Args:
            input_queue: ProducerConsumer to read items from
            output_queue: ProducerConsumer to write items to
            process_func: Callable that transforms items
            num_workers: Number of worker threads (default 1)
            stage_name: Name for logging purposes
        """
        # TODO: Store parameters and initialize workers
        # TODO: Create and start num_workers threads
        pass

    def _worker(self) -> None:
        """
        Worker thread function that processes items.

        Each worker:
        1. Consumes an item from input_queue
        2. Applies process_func to transform it
        3. Produces the result to output_queue
        4. Repeats until a sentinel value is received

        TODO: Implement this method
        """
        pass

    def shutdown(self, timeout: Optional[float] = None) -> None:
        """
        Shutdown all worker threads.

        Args:
            timeout: Optional timeout for joining threads
        """
        # TODO: Send sentinel values to signal workers to stop
        # TODO: Wait for all workers to finish
        pass


class Pipeline:
    """
    A multi-stage processing pipeline.

    This class orchestrates multiple PipelineStages connected by queues.
    """

    def __init__(self, stage_configs: List[dict]):
        """
        Initialize a pipeline with multiple stages.

        Args:
            stage_configs: List of dicts with keys:
                - 'func': Processing function
                - 'workers': Number of workers (default 1)
                - 'name': Stage name (optional)
        """
        # TODO: Create queues and pipeline stages
        # TODO: Connect stages with queues
        pass

    def feed(self, item: Any) -> None:
        """
        Add an item to the start of the pipeline.

        Args:
            item: Item to process
        """
        # TODO: Put item into first stage's input queue
        pass

    def get_results(self) -> List[Any]:
        """
        Get all results from the end of the pipeline.

        Returns:
            List of all processed items
        """
        # TODO: Consume all items from final stage's output queue
        pass

    def shutdown(self) -> None:
        """
        Shutdown all pipeline stages gracefully.
        """
        # TODO: Call shutdown on all stages
        pass
