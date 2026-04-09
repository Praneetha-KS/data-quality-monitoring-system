# Data Quality Monitoring System

A lightweight system for checking dataset health and detecting common data issues in CSV files. It is designed to help teams track baseline quality, validate new data, and generate simple reports.

## Purpose

- Monitor data quality against a baseline.
- Identify issues such as missing values, invalid discounts, negative sales, and drift.
- Produce clear reports for analysis and review.

## Tech Stack

- Python 3
- pandas
- CSV files for input data
- Text reports for output

## Project Structure

```
.
├── baseline_stats.json
├── config.json
├── create_baseline.py
├── main.py
├── notifier.py
├── requirements.txt
├── simulate_issues.py
├── validator.py
├── data/
│   ├── baseline.csv
│   ├── drift.csv
│   ├── invalid_discount.csv
│   ├── missing_values.csv
│   ├── negative_sales.csv
│   └── sales_clean.csv
├── logs/ # generated during execution
└── reports/ # generated reports 
    
```

## Installation

1. Clone the repository.
2. Install Python 3 if needed.
3. Run:

```bash
pip install -r requirements.txt
```

## How to Run

From the project folder, run:

```bash
python main.py
```

If needed, update `config.json` before running to match your data paths.

## Features

- Baseline creation and comparison
- Data validation checks for missing or invalid values
- Drift detection over dataset changes
- Report generation in text format
- Sample issue simulation files for testing
