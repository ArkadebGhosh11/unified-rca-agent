"""
fault_injector.py

Shared fault state manager.
"""

import json
from pathlib import Path
from datetime import datetime

FAULT_FILE = Path("data/fault_state.json")


def load_fault_state():
    with open(FAULT_FILE, "r") as file:
        return json.load(file)


def save_fault_state(state):
    with open(FAULT_FILE, "w") as file:
        json.dump(state, file, indent=4)


def enable_fault(fault_name: str):

    state = load_fault_state()

    if fault_name in state:
        state[fault_name] = True
        save_fault_state(state)

        print(
            f"[{datetime.now()}] Enabled fault: {fault_name}"
        )

    else:
        print(f"Unknown fault: {fault_name}")


def disable_fault(fault_name: str):

    state = load_fault_state()

    if fault_name in state:
        state[fault_name] = False
        save_fault_state(state)

        print(
            f"[{datetime.now()}] Disabled fault: {fault_name}"
        )

    else:
        print(f"Unknown fault: {fault_name}")


def reset_all_faults():

    state = load_fault_state()

    for key in state:
        state[key] = False

    save_fault_state(state)

    print(
        f"[{datetime.now()}] All faults cleared"
    )


def get_fault_state():
    return load_fault_state()


if __name__ == "__main__":

    print("Current Fault State")
    print(get_fault_state())

    enable_fault("storage_latency_spike")

    print("\nUpdated State")
    print(get_fault_state())