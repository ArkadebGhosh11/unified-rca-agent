"""
dashboard.py

Unified Observability & RCA Agent Dashboard
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(
    __file__
).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(
        str(PROJECT_ROOT)
    )

import streamlit as st

from telemetry.storage_generator import (
    generate_metrics
)

from telemetry.fault_injector import (
    enable_fault,
    reset_all_faults,
    get_fault_state
)

from backend.agents.anomaly_agent import (
    AnomalyAgent
)

from backend.agents.correlation_agent import (
    CorrelationAgent
)

from backend.agents.learning_agent import (
    LearningAgent
)

from backend.agents.rca_agent import (
    RCAAgent
)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Unified RCA Agent",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title(
    "⚙️ Fault Controls"
)

current_faults = (
    get_fault_state()
)

st.sidebar.subheader(
    "Current Fault State"
)

st.sidebar.json(
    current_faults
)

if st.sidebar.button(
    "Inject Storage Fault"
):
    enable_fault(
        "storage_latency_spike"
    )
    st.rerun()

if st.sidebar.button(
    "Inject Network Fault"
):
    enable_fault(
        "network_latency_spike"
    )
    st.rerun()

if st.sidebar.button(
    "Inject Compute Fault"
):
    enable_fault(
        "compute_resource_exhaustion"
    )
    st.rerun()

if st.sidebar.button(
    "Inject Application Fault"
):
    enable_fault(
        "application_errors"
    )
    st.rerun()

if st.sidebar.button(
    "Clear All Faults"
):
    reset_all_faults()
    st.rerun()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title(
    "🔍 Unified Observability & RCA Agent"
)

st.markdown(
    "AI-powered Root Cause Analysis Platform"
)

st.divider()

# --------------------------------------------------
# Initialize Agents
# --------------------------------------------------

anomaly_agent = AnomalyAgent()

correlation_agent = (
    CorrelationAgent()
)

learning_agent = (
    LearningAgent()
)

# Create RCA agent once
rca_agent = RCAAgent()

# --------------------------------------------------
# Generate Telemetry
# --------------------------------------------------

storage_metrics = (
    generate_metrics()
)

col1, col2 = st.columns(2)

with col1:

    st.subheader(
        "Storage Telemetry"
    )

    st.json(
        storage_metrics
    )

# --------------------------------------------------
# Detect Anomaly
# --------------------------------------------------

incident = (
    anomaly_agent.detect_anomaly(
        storage_metrics
    )
)

with col2:

    st.subheader(
        "Incident"
    )

    if incident:

        st.error(
            "Anomaly Detected"
        )

        st.json(
            incident
        )

    else:

        st.success(
            "No Active Incident"
        )

# --------------------------------------------------
# Correlation
# --------------------------------------------------

st.divider()

st.subheader(
    "Correlation Result"
)

correlation_result = None

if incident:

    incidents = [
        incident
    ]

    correlation_result = (
        correlation_agent.correlate(
            incidents
        )
    )

    st.json(
        correlation_result
    )

else:

    st.info(
        "No incidents available "
        "for correlation."
    )

# --------------------------------------------------
# Learning Context
# --------------------------------------------------

st.divider()

st.subheader(
    "Historical Learning Context"
)

learning_context = None

if incident:

    learning_context = (
        learning_agent
        .get_learning_context(
            "storage latency issue"
        )
    )

    st.json(
        learning_context
    )

else:

    st.info(
        "No learning context available."
    )

# --------------------------------------------------
# RCA
# --------------------------------------------------

st.divider()

st.subheader(
    "Generated RCA"
)

if (
    incident
    and correlation_result
):

    try:

        report = (
            rca_agent.generate_rca(
                correlation_result,
                incidents,
                learning_context
            )
        )

        st.markdown(
            report
        )

    except Exception as e:

        st.error(
            f"RCA Generation Failed: {e}"
        )

else:

    st.info(
        "No RCA generated."
    )