"""
storage_generator.py

Simulates storage telemetry for the Unified Observability & RCA Agent.
"""

import random
import time
from datetime import datetime, UTC

timestamp = datetime.now(UTC).isoformat()

from telemetry.fault_injector import get_fault_state


def generate_metrics():
    """
    Generate storage telemetry metrics based on fault state.
    """

    fault_state = get_fault_state()

    if fault_state.get("storage_latency_spike", False):
        latency = random.randint(200, 350)
        iops = random.randint(1000, 2000)
        status = "critical"
        severity = "high"

    else:
        latency = random.randint(10, 20)
        iops = random.randint(4500, 6000)
        status = "healthy"
        severity = "low"

    return {
        "tower": "storage",
        "component": "storage-cluster-a",
        "latency_ms": latency,
        "iops": iops,
        "status": status,
        "severity": severity,
        "timestamp": datetime.utcnow().isoformat()
    }


def print_metrics():

    metric = generate_metrics()

    print(
        f"[{metric['timestamp']}] "
        f"Storage Cluster A | "
        f"Latency={metric['latency_ms']}ms | "
        f"IOPS={metric['iops']} | "
        f"Status={metric['status']}"
    )


if __name__ == "__main__":

    print("\nStarting Storage Telemetry Generator...\n")

    while True:
        print_metrics()
        time.sleep(2)