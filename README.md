# AzureForecasting

Azure Demand Forecasting Capacity Optimization System is a data analytics project that predicts cloud resource demand and suggests optimal infrastructure capacity using a time-series dataset.

# Problem Statement

cloud service demand changes daliy based on region, workload, and user behaviour.
Incorrect capacity planning can lead to :

- Financial Waste
- Service downtime
  The goal of this project is to forrecast demand, estimate cost and recommend optimal capacity allocation.

# Dataset Description

A synthetic 26-month daily time-series dataset was created to simulate realistic cloud usage patterns across multiple regions and services. The dataset also includes controlled missing values for preprocessing practice.

## Dataset Columns

- **timestamp** – Date of usage (daily)
- **region** – Cloud region
- **service_type** – Compute / Storage
- **usage_units** – Demand units
- **provisioned_capacity** – Allocated infrastructure
- **cost_usd** – Estimated operational cost
- **availability_pct** – Service uptime percentage
- **is_weekend** – Weekend indicator
- **utilization_pct** – Capacity utilization efficiency

## Features Implemented

- Data Cleaning & Preprocessing
- Missing Value Handling (Interpolation, Forward Fill, Mean Imputation)
- Feature Engineering (Utilization Metrics, Time Flags)
- Trend Visualization by Region and Service Type
- Forecasting Preparation for ML Models
- Capacity Optimization Logic

## Tools & Technologies

- Python
- Pandas
- NumPy

# Project Workflow

1. Dataset Generation
2. Data Cleaning & Standardization
3. Feature Engineering
4. Exploratory Data Analysis
5. Forecast Model Preparation
6. Capacity & Cost Optimization Logic
7. Documentation & Version Control
