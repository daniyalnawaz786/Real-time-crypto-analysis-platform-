# Real-Time Cryptocurrency Analytics Platform

A platform to fetch, process, and visualize live cryptocurrency data with automated ETL pipelines and interactive dashboards.

## Table of Contents
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)

## How It Works

The platform operates as a real-time data pipeline with three main components:

### 1. **Data Extraction (API Layer)**
- The `api/fetch_data.py` module fetches live cryptocurrency data from external APIs
- Data is retrieved in raw format with prices, volumes, and market information

### 2. **ETL Pipeline (Data Processing)**
The `etl/` module processes the data in three steps:
- **Extract** (`extract.py`): Fetches raw crypto data from the API
- **Transform** (`transform.py`): Cleans, validates, and structures the data for storage
- **Load** (`load.py`): Stores processed data in SQLite database

### 3. **Scheduler (Automation)**
- `scheduler/run_pipeline.py` runs the ETL pipeline automatically every 5 minutes
- Ensures continuous data collection without manual intervention

### 4. **Dashboard (Visualization)**
- `dashboard/app.py` is a Streamlit-based interactive dashboard
- Displays real-time crypto market metrics, trends, and visualizations using Plotly
- Data is queried from the SQLite database and rendered with charts and KPIs

### Data Flow
```
Crypto API → Extract → Transform → Load (SQLite) → Dashboard (Streamlit)
     ↑                                                      ↓
     └──────────────── Updated every 5 minutes ────────────┘
```

## Prerequisites

- **Python 3.10+** or **Docker & Docker Compose**
- **Git** (optional, for cloning the repository)

## Installation & Setup

### Option 1: Local Setup (Python Virtual Environment)

1. **Clone or navigate to the project directory**
   ```bash
   cd Real-time-crypto-analysis-platform-
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Docker Setup

1. **Ensure Docker and Docker Compose are installed**
   ```bash
   docker --version
   docker-compose --version
   ```

2. **Navigate to the project directory**
   ```bash
   cd Real-time-crypto-analysis-platform-
   ```

## Running the Project

### Local Execution (Recommended for Development)

**Terminal 1 - Start the ETL Scheduler:**
```bash
source env/bin/activate
python scheduler/run_pipeline.py
```
This will start collecting cryptocurrency data every 5 minutes.

**Terminal 2 - Start the Dashboard:**
```bash
source env/bin/activate
streamlit run dashboard/app.py
```
The dashboard will be available at `http://localhost:8501`

### Docker Execution (Recommended for Production)

Run both components together:
```bash
docker-compose up
```

This will:
- Start the scheduler container (`crypto_scheduler`) to fetch and process data
- Start the dashboard container (`crypto_dashboard`) accessible at `http://localhost:8501`
- Both services share the SQLite database file via volume mounts
- The dashboard waits for the scheduler to collect initial data

**To stop the services:**
```bash
docker-compose down
```

**To rebuild after code changes:**
```bash
docker-compose up --build
```

## Project Structure

```
Real-time-crypto-analysis-platform-/
├── api/                    # API data fetching module
│   ├── __init__.py
│   └── fetch_data.py      # Cryptocurrency API integration
├── etl/                    # Extract-Transform-Load pipeline
│   ├── __init__.py
│   ├── extract.py         # Data extraction from APIs
│   ├── transform.py       # Data cleaning and transformation
│   └── load.py            # Database storage
├── dashboard/             # Streamlit dashboard
│   ├── __init__.py
│   └── app.py            # Interactive visualization interface
├── scheduler/             # Automated job scheduling
│   ├── __init__.py
│   └── run_pipeline.py   # Pipeline orchestration (runs every 5 min)
├── utils/                 # Utility functions
│   ├── __init__.py
│   └── helpers.py        # Common helper functions
├── env/                   # Python virtual environment
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Multi-container Docker setup
└── README.md            # This file
```

## Quick Start Summary

**For quick testing:**
```bash
# Local
source env/bin/activate
python scheduler/run_pipeline.py &
streamlit run dashboard/app.py

# Docker
docker-compose up
```

Then open your browser to `http://localhost:8501` to see the dashboard.

**Note:** The dashboard requires data from the scheduler. Allow 1-2 minutes for the first data collection cycle.
