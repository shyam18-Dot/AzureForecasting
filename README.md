# AzureForecasting

This project predicts cloud resource demand using time-series forecasting techniques.
It simulates real-world Azure infrastructure planning by analyzing usage patterns,
optimizing capacity allocation, and estimating operational costs.

# Problem Statement

Cloud service demand fluctuates daily. Incorrect capacity planning can lead to
over-provisioning (waste) or under-provisioning (downtime).
This project builds a forecasting model to improve infrastructure planning decisions.

It reduces the following:

- Financial wastes
- Service downtime

# Dataset Information

The dataset contains 26 months of daily time-series data including:

- timestamp
- region
- service_type
- usage_units
- provisioned_capacity
- cost_usd
- availability_pct
- is_weekend
- utilization_pct

# Features Implemented

- Data Cleaning & Missing Value Handling
- Feature Engineering (Lag, Rolling Average, Utilization)
- Time-Series Visualization
- Capacity Optimization Logic

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
  -Git & GitHub

# Project Structure

data/
scripts/
notebooks/
README.md
