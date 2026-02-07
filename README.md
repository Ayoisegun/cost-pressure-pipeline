# Cost Pressure Data Pipeline

## Overview
This project implements an end-to-end data engineering pipeline that integrates
inflation, exchange rate, and climate data to analyze cost-of-living pressure
across countries.

The pipeline ingests historical data for the year 2023 and transforms it into
analytics-ready tables suitable for exploratory analysis and reporting.

## Data Sources
- **Exchange Rates:** World Bank API (exchange rates to USD)
- **Inflation:** World Bank API (CPI / inflation indicators)
- **Weather:** Open-Meteo (temperature and precipitation data)

## Scope and Design Choices
- The pipeline operates on historical data for 2023.
- Data ingestion is implemented as a batch backfill.
- The system is designed to support incremental or near–real-time ingestion
  with minimal changes.
- Weather data is aggregated to monthly granularity to align with inflation data.

## Architecture (High Level)
1. Raw data ingestion from external APIs
2. Standardization and cleaning of source data
3. Integration into country-level analytics tables

## Output
The final output is a set of analytics-ready tables that enable analysis of
cost-of-living pressure trends across countries and over time.

## Future Improvements
- Add orchestration (e.g. Airflow / Prefect)
- Introduce dbt for transformations
- Extend coverage beyond 2023
- Deploy pipeline in a cloud environment
