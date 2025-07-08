# Smart Application Performance Monitoring and Auto-Scaling

## Overview

This project implements a modular system that **monitors application performance metrics**, **predicts future demand**, **detects anomalies**, and **automatically scales resources** across multiple tiers based on predicted traffic patterns.

The system aims to balance resource cost and user experience by proactively adjusting infrastructure to meet expected demand, handling seasonal trends, sudden load spikes, and multi-tier scaling challenges.

---

## Features

- **Metrics Monitoring:** Collects and processes application performance data (CPU, memory, request rate, latency, error rates)
- **Traffic Prediction:** Uses time series forecasting (Prophet) to predict future traffic demand
- **Anomaly Detection:** Identifies performance anomalies to trigger scaling or alerts
- **Scaling Decision Engine:** Implements multi-tier scaling logic to decide when and how to scale application tiers (web, database, cache)
- **Scaling Execution:** Simulates execution of scaling actions (can be extended to real cloud APIs)
- **Interactive Dashboard:** Streamlit-based dashboard for visualizing metrics, predictions, anomalies, and scaling decisions in real time

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Pip package manager

### Installation

1. Clone this repository:

```bash
git clone https://github.com/Pradeep-O/smart-application-performance-monitoring-and-auto-scaling.git
cd smart-auto-scaling
```

2. Install required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Run the auto-scaling pipeline  
This will simulate or load metrics, predict traffic, detect anomalies, decide scaling, and simulate scaling execution.
```bash
python main.py
```

### Step 2: Launch the monitoring dashboard  
Visualize metrics, predictions, anomalies, and scaling decisions.
```
streamlit run dashboard/app.py
```
Open the URL shown in the terminal in your browser.

---

## Notes

- `main.py` must be run before launching the dashboard to ensure fresh data is available  
- The dashboard currently uses simulated stats for predicted traffic and scaling actions—can be enhanced to read real outputs from the pipeline
