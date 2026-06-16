# Unified Observability & RCA Agent

AI-powered observability platform that correlates telemetry across Storage, Network, Compute, and Application layers, learns from historical incidents, and automatically generates Root Cause Analysis (RCA) reports.

---

# Architecture

Telemetry Generators
↓
Anomaly Detection Agent
↓
Correlation Engine
↓
Incident Memory
↓
Learning Agent
↓
AI RCA Agent
↓
Streamlit Dashboard

---

# Prerequisites

* Python 3.11+
* OpenAI API Key
* Virtual Environment

---

# Installation

Clone the repository:

```bash
git clone https://github.com/ArkadebGhosh11/unified-rca-agent.git

cd unified-rca-agent
```

Create and activate virtual environment:

```bash
python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Verify Installation

Check OpenAI package:

```bash
python -c "import openai; print(openai.__version__)"
```

Expected:

```text
1.93.0
```

Run unit tests:

```bash
python -m tests.test_incident_memory

python -m tests.test_learning_agent

python -m tests.test_correlation_agent
```

---

# Start Dashboard

Always run Streamlit using the virtual environment:

```bash
python -m streamlit run frontend/dashboard.py
```

Open browser:

```text
http://localhost:8501
```

---

# Demo Scenario 1 – Storage Failure

Inject storage fault:

```python
from telemetry.fault_injector import enable_fault

enable_fault(
    "storage_latency_spike"
)
```

Expected Results:

* Storage telemetry becomes critical
* Application telemetry becomes critical
* Active incidents detected
* Root cause identified as storage-cluster-a
* RCA generated automatically

---

# Demo Scenario 2 – Network Failure

Inject network fault:

```python
from telemetry.fault_injector import enable_fault

enable_fault(
    "network_latency_spike"
)
```

Expected Results:

* Network telemetry becomes critical
* Network incident generated
* Correlation engine identifies core-network
* RCA generated automatically

---

# Demo Scenario 3 – Compute Failure

Inject compute fault:

```python
from telemetry.fault_injector import enable_fault

enable_fault(
    "compute_resource_exhaustion"
)
```

Expected Results:

* CPU utilization exceeds threshold
* Compute incident generated
* Root cause identified as worker-node-01
* RCA generated automatically

---

# Clear All Faults

Reset platform:

```python
from telemetry.fault_injector import reset_all_faults

reset_all_faults()
```

Expected Results:

* All telemetry returns to healthy state
* No active incidents
* No RCA generated

---

# Key Features

* Multi-Tower Telemetry Monitoring
* Fault Injection Framework
* Automated Anomaly Detection
* Cross-Tower Correlation Engine
* Historical Incident Memory
* Learning-Based Resolution Suggestions
* AI-Powered Root Cause Analysis
* Interactive Streamlit Dashboard

---

# Technology Stack

* Python
* Streamlit
* OpenAI GPT-4o
* ChromaDB
* Sentence Transformers

---

# Future Enhancements

* Multi-root-cause correlation
* Real-time streaming telemetry
* Kubernetes integration
* Service dependency graph
* Automated remediation workflows
