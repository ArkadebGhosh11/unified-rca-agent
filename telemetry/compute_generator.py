"""
compute_generator.py

Simulates compute telemetry for the Unified Observability & RCA Agent.
"""

import random
import time
from datetime import datetime, UTC

from telemetry.fault_injector import get_fault_state


def generate_metrics():

    fault_state = get_fault_state()

    compute_fault = fault_state.get(
        "compute_resource_exhaustion",
        False
    )

    if compute_fault:

        cpu = random.randint(
            90,
            99
        )

        memory = random.randint(
            85,
            98
        )

        node_health = "degraded"

        status = "critical"
        severity = "high"

    else:

        cpu = random.randint(
            30,
            60
        )

        memory = random.randint(
            40,
            70
        )

        node_health = "healthy"

        status = "healthy"
        severity = "low"

    return {
        "tower": "compute",
        "component": "worker-node-01",
        "cpu_percent": cpu,
        "memory_percent": memory,
        "node_health": node_health,
        "status": status,
        "severity": severity,
        "timestamp": datetime.now(
            UTC
        ).isoformat()
    }


def print_metrics():

    metric = generate_metrics()

    print(
        f"[{metric['timestamp']}] "
        f"Worker Node 01 | "
        f"CPU={metric['cpu_percent']}% | "
        f"Memory={metric['memory_percent']}% | "
        f"Health={metric['node_health']} | "
        f"Status={metric['status']}"
    )


if __name__ == "__main__":

    print(
        "\nStarting Compute Telemetry Generator...\n"
    )

    while True:
        print_metrics()
        time.sleep(2)