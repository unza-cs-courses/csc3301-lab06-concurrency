#!/usr/bin/env python3
"""
Variant Generator for Lab 6: Concurrency and Parallelism
CSC3301 Programming Language Paradigms

Generates deterministic, student-specific variants for concurrency testing parameters.
Uses student ID hash to ensure reproducibility.
"""
import hashlib
import json
import sys
from pathlib import Path


def hash_student_id(student_id: str) -> int:
    """Generate a deterministic hash from student ID."""
    return int(hashlib.sha256(student_id.encode()).hexdigest(), 16)


def generate_variant(student_id: str) -> dict:
    """
    Generate a unique variant configuration based on student ID.

    Variants include:
    - Different thread counts for testing
    - Different iteration counts per thread
    - Different data sizes for processing
    - Different test parameters
    """
    seed = hash_student_id(student_id)

    # Thread count variants: 4-16 threads
    thread_counts = [4, 5, 6, 8, 10, 12, 15, 16]
    thread_count = thread_counts[seed % len(thread_counts)]

    # Iteration count variants: 100-1000 per thread
    iteration_counts = [100, 150, 200, 250, 300, 400, 500, 750, 1000]
    iterations_per_thread = iteration_counts[(seed >> 8) % len(iteration_counts)]

    # Data size variants for processing tasks: 50-500 items
    data_sizes = [50, 75, 100, 125, 150, 200, 250, 300, 400, 500]
    data_size = data_sizes[(seed >> 16) % len(data_sizes)]

    # Pipeline stage counts: 3-6 stages
    pipeline_stages = [3, 4, 5, 6]
    num_stages = pipeline_stages[(seed >> 24) % len(pipeline_stages)]

    # Workers per stage: 2-5 workers
    workers_per_stage = [2, 3, 4, 5]
    num_workers = workers_per_stage[(seed >> 32) % len(workers_per_stage)]

    # Queue size for producer-consumer: 5-20
    queue_sizes = [5, 10, 15, 20]
    queue_size = queue_sizes[(seed >> 40) % len(queue_sizes)]

    # Timeout values for tests: 5-15 seconds
    timeout_values = [5, 8, 10, 12, 15]
    test_timeout = timeout_values[(seed >> 48) % len(timeout_values)]

    # Number of URLs to fetch in web scraper task
    url_counts = [5, 8, 10, 12, 15, 20]
    num_urls = url_counts[(seed >> 56) % len(url_counts)]

    # Batch sizes for processing
    batch_sizes = [5, 10, 15, 20, 25]
    batch_size = batch_sizes[(seed >> 64) % len(batch_sizes)]

    # Calculate expected values for counter tests
    expected_counter_value = thread_count * iterations_per_thread

    variant = {
        "student_id": student_id,
        "variant_hash": hex(seed % (2**32)),

        # Thread-safe counter parameters (Task 1)
        "counter_tests": {
            "num_threads": thread_count,
            "iterations_per_thread": iterations_per_thread,
            "expected_value": expected_counter_value
        },

        # Web scraper parameters (Task 2)
        "scraper_tests": {
            "num_urls": num_urls,
            "timeout_seconds": test_timeout,
            "batch_size": batch_size
        },

        # Producer-consumer pipeline parameters (Task 3)
        "pipeline_tests": {
            "num_stages": num_stages,
            "workers_per_stage": num_workers,
            "queue_size": queue_size,
            "data_size": data_size
        },

        # Integration challenge parameters (Task 4)
        "integration_tests": {
            "data_size": data_size,
            "num_threads": thread_count,
            "processing_timeout": test_timeout
        },

        # General test configuration
        "test_config": {
            "timeout": test_timeout,
            "retry_count": 3
        }
    }

    return variant


def main():
    """Generate variant configuration file."""
    if len(sys.argv) < 2:
        print("Usage: python variant_generator.py <student_id>")
        print("Example: python variant_generator.py jsmith123")
        sys.exit(1)

    student_id = sys.argv[1]
    repo_root = Path(__file__).parent.parent

    # Generate variant
    variant = generate_variant(student_id)

    # Save configuration
    config_path = repo_root / ".variant_config.json"
    with open(config_path, "w") as f:
        json.dump(variant, f, indent=2)

    print(f"Generated variant for student: {student_id}")
    print(f"Configuration saved to: {config_path}")
    print(f"\nVariant summary:")
    print(f"  Thread count: {variant['counter_tests']['num_threads']}")
    print(f"  Iterations per thread: {variant['counter_tests']['iterations_per_thread']}")
    print(f"  Expected counter value: {variant['counter_tests']['expected_value']}")
    print(f"  Data size: {variant['pipeline_tests']['data_size']}")
    print(f"  Pipeline stages: {variant['pipeline_tests']['num_stages']}")
    print(f"  Workers per stage: {variant['pipeline_tests']['workers_per_stage']}")
    print(f"  Test timeout: {variant['test_config']['timeout']}s")


if __name__ == "__main__":
    main()
