"""
application_generator.py

Simulates application telemetry for the Unified Observability & RCA Agent.
"""

import random
import time
from datetime import datetime, UTC

from telemetry.fault_injector import get_fault_state


def generate_metrics():
    fault_state = get_fault_state()

    storage_fault = fault_state.get(
        "storage_latency_spike",
        False
    )

    if storage_fault:
        response_time = random.randint(2500, 5000)
        error_rate = round(random.uniform(10.0, 25.0), 2)
        availability = round(random.uniform(95.0, 98.0), 2)

        status = "critical"
        severity = "high"

    else:
        response_time = random.randint(120, 250)
        error_rate = round(random.uniform(0.1, 1.0), 2)
        availability = round(random.uniform(99.9, 100.0), 2)

        status = "healthy"
        severity = "low"

    return {
        "tower": "application",
        "service": "checkout-service",
        "response_time_ms": response_time,
        "error_rate_percent": error_rate,
        "availability_percent": availability,
        "status": status,
        "severity": severity,
        "timestamp": datetime.now(UTC).isoformat()
    }


def print_metrics():
    metric = generate_metrics()

    print(
        f"[{metric['timestamp']}] "
        f"Checkout Service | "
        f"Response={metric['response_time_ms']}ms | "
        f"Errors={metric['error_rate_percent']}% | "
        f"Availability={metric['availability_percent']}% | "
        f"Status={metric['status']}"
    )


if __name__ == "__main__":
    print("\nStarting Application Telemetry Generator...\n")

    while True:
        print_metrics()
        time.sleep(2)