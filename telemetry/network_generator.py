"""
network_generator.py

Simulates network telemetry for the Unified Observability & RCA Agent.
"""

import random
import time
from datetime import datetime, UTC

from telemetry.fault_injector import get_fault_state


def generate_metrics():

    fault_state = get_fault_state()

    network_fault = fault_state.get(
        "network_latency_spike",
        False
    )

    if network_fault:

        latency = random.randint(
            150,
            300
        )

        packet_loss = round(
            random.uniform(5.0, 20.0),
            2
        )

        throughput = random.randint(
            200,
            500
        )

        status = "critical"
        severity = "high"

    else:

        latency = random.randint(
            5,
            15
        )

        packet_loss = round(
            random.uniform(0.0, 0.5),
            2
        )

        throughput = random.randint(
            800,
            1000
        )

        status = "healthy"
        severity = "low"

    return {
        "tower": "network",
        "component": "core-network",
        "latency_ms": latency,
        "packet_loss_percent": packet_loss,
        "throughput_mbps": throughput,
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
        f"Core Network | "
        f"Latency={metric['latency_ms']}ms | "
        f"PacketLoss={metric['packet_loss_percent']}% | "
        f"Throughput={metric['throughput_mbps']}Mbps | "
        f"Status={metric['status']}"
    )


if __name__ == "__main__":

    print(
        "\nStarting Network Telemetry Generator...\n"
    )

    while True:
        print_metrics()
        time.sleep(2)