"""
Pytest fixtures for Lab 6: Concurrency and Parallelism
Loads variant configuration with sensible defaults for testing.
"""
import json
import pytest
from pathlib import Path


# Default configuration values (used when no variant config exists)
DEFAULT_CONFIG = {
    "student_id": "default",
    "variant_hash": "0x0",
    "counter_tests": {
        "num_threads": 10,
        "iterations_per_thread": 100,
        "expected_value": 1000
    },
    "scraper_tests": {
        "num_urls": 10,
        "timeout_seconds": 10,
        "batch_size": 10
    },
    "pipeline_tests": {
        "num_stages": 4,
        "workers_per_stage": 3,
        "queue_size": 10,
        "data_size": 100
    },
    "integration_tests": {
        "data_size": 100,
        "num_threads": 10,
        "processing_timeout": 10
    },
    "test_config": {
        "timeout": 10,
        "retry_count": 3
    }
}


def load_variant_config() -> dict:
    """Load variant configuration from file, with fallback to defaults."""
    # Try multiple possible locations for the config file
    possible_paths = [
        Path(__file__).parent.parent.parent / ".variant_config.json",
        Path.cwd() / ".variant_config.json",
    ]

    for config_path in possible_paths:
        if config_path.exists():
            with open(config_path) as f:
                return json.load(f)

    # Return default config if no variant file found
    return DEFAULT_CONFIG.copy()


@pytest.fixture(scope="session")
def variant_config():
    """Provide the full variant configuration dictionary."""
    return load_variant_config()


@pytest.fixture(scope="session")
def counter_config(variant_config):
    """Provide counter test configuration."""
    return variant_config.get("counter_tests", DEFAULT_CONFIG["counter_tests"])


@pytest.fixture(scope="session")
def num_threads(counter_config):
    """Provide the number of threads for counter tests."""
    return counter_config.get("num_threads", 10)


@pytest.fixture(scope="session")
def iterations_per_thread(counter_config):
    """Provide the number of iterations per thread."""
    return counter_config.get("iterations_per_thread", 100)


@pytest.fixture(scope="session")
def expected_counter_value(counter_config):
    """Provide the expected counter value after all threads complete."""
    return counter_config.get("expected_value", 1000)


@pytest.fixture(scope="session")
def scraper_config(variant_config):
    """Provide web scraper test configuration."""
    return variant_config.get("scraper_tests", DEFAULT_CONFIG["scraper_tests"])


@pytest.fixture(scope="session")
def num_urls(scraper_config):
    """Provide the number of URLs for scraper tests."""
    return scraper_config.get("num_urls", 10)


@pytest.fixture(scope="session")
def scraper_timeout(scraper_config):
    """Provide the timeout for scraper tests."""
    return scraper_config.get("timeout_seconds", 10)


@pytest.fixture(scope="session")
def batch_size(scraper_config):
    """Provide the batch size for processing."""
    return scraper_config.get("batch_size", 10)


@pytest.fixture(scope="session")
def pipeline_config(variant_config):
    """Provide pipeline test configuration."""
    return variant_config.get("pipeline_tests", DEFAULT_CONFIG["pipeline_tests"])


@pytest.fixture(scope="session")
def num_stages(pipeline_config):
    """Provide the number of pipeline stages."""
    return pipeline_config.get("num_stages", 4)


@pytest.fixture(scope="session")
def workers_per_stage(pipeline_config):
    """Provide the number of workers per stage."""
    return pipeline_config.get("workers_per_stage", 3)


@pytest.fixture(scope="session")
def queue_size(pipeline_config):
    """Provide the queue size for producer-consumer."""
    return pipeline_config.get("queue_size", 10)


@pytest.fixture(scope="session")
def data_size(pipeline_config):
    """Provide the data size for processing."""
    return pipeline_config.get("data_size", 100)


@pytest.fixture(scope="session")
def integration_config(variant_config):
    """Provide integration test configuration."""
    return variant_config.get("integration_tests", DEFAULT_CONFIG["integration_tests"])


@pytest.fixture(scope="session")
def test_timeout(variant_config):
    """Provide the general test timeout."""
    return variant_config.get("test_config", {}).get("timeout", 10)


@pytest.fixture(scope="session")
def student_id(variant_config):
    """Provide the student ID from variant config."""
    return variant_config.get("student_id", "default")
