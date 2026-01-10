#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms - Lab 6: Concurrency
"""
import json
from pathlib import Path


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config
    config_path = repo_root / ".variant_config.json"
    if not config_path.exists():
        print("No variant config found. Run variant_generator.py first.")
        return

    with open(config_path) as f:
        variant = json.load(f)

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Extract values from variant config
    counter = variant.get("counter_tests", {})
    scraper = variant.get("scraper_tests", {})
    pipeline = variant.get("pipeline_tests", {})
    integration = variant.get("integration_tests", {})
    test_config = variant.get("test_config", {})

    # Replace placeholders
    assignment = template
    assignment = assignment.replace("{{STUDENT_ID}}", variant.get("student_id", "unknown"))

    # Counter test parameters
    assignment = assignment.replace("{{NUM_THREADS}}", str(counter.get("num_threads", 10)))
    assignment = assignment.replace("{{ITERATIONS_PER_THREAD}}", str(counter.get("iterations_per_thread", 100)))
    assignment = assignment.replace("{{EXPECTED_COUNTER_VALUE}}", str(counter.get("expected_value", 1000)))

    # Scraper parameters
    assignment = assignment.replace("{{NUM_URLS}}", str(scraper.get("num_urls", 10)))
    assignment = assignment.replace("{{SCRAPER_TIMEOUT}}", str(scraper.get("timeout_seconds", 10)))
    assignment = assignment.replace("{{BATCH_SIZE}}", str(scraper.get("batch_size", 10)))

    # Pipeline parameters
    assignment = assignment.replace("{{NUM_STAGES}}", str(pipeline.get("num_stages", 4)))
    assignment = assignment.replace("{{NUM_WORKERS}}", str(pipeline.get("workers_per_stage", 3)))
    assignment = assignment.replace("{{QUEUE_SIZE}}", str(pipeline.get("queue_size", 10)))
    assignment = assignment.replace("{{DATA_SIZE}}", str(pipeline.get("data_size", 100)))

    # Integration parameters
    assignment = assignment.replace("{{PROCESSING_TIMEOUT}}", str(integration.get("processing_timeout", 10)))

    # Test config
    assignment = assignment.replace("{{TEST_TIMEOUT}}", str(test_config.get("timeout", 10)))

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")


if __name__ == "__main__":
    main()
