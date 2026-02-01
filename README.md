Forecasting Financial Inclusion in Ethiopia

10 Academy – AI Mastery | Week 10 Challenge

📌 Project Overview

This project focuses on analyzing and forecasting financial inclusion in Ethiopia using time series data, event analysis, and exploratory data analysis (EDA).

Financial inclusion is measured using the World Bank Global Findex framework, which defines two core dimensions:

Access – Account Ownership Rate

Usage – Digital Payment Adoption Rate

Ethiopia has experienced rapid growth in digital financial services (e.g., Telebirr, M-Pesa), yet overall financial inclusion growth has recently slowed. This project aims to understand why, identify key drivers, and prepare the ground for forecasting future trends.

🎯 Project Objectives

By completing Tasks 1 and 2, this project aims to:

Understand the structure and limitations of the provided unified dataset

Enrich the dataset with additional relevant financial inclusion data

Explore historical trends in financial access and usage

Identify patterns, gaps, and potential drivers of financial inclusion in Ethiopia

Generate insights that will inform later event-impact modeling and forecasting

🗂️ Repository Structure
ethiopia-fi-forecast/
│
├── data/
│   ├── raw/
│   │   ├── ethiopia_fi_unified_data.csv
│   │   └── reference_codes.csv
│   ├── processed/
│
├── notebooks/
│   ├── task_1_data_exploration.ipynb
│   ├── task_2_eda.ipynb
│
├── reports/
│   ├── data_enrichment_log.md
│
├── src/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore

📁 Dataset Description

The project uses a unified schema dataset, where all records share the same structure and are differentiated using the record_type field.

Record Types

observation – Measured indicators (e.g., account ownership, mobile money usage)

event – Policies, product launches, infrastructure developments

impact_link – Modeled relationships between events and indicators

target – Official policy targets (e.g., NFIS goals)

This design avoids bias by not pre-assigning events to financial inclusion pillars.

✅ Task 1: Data Exploration and Enrichment
Objective

To understand the starter dataset and enrich it with additional relevant data needed for forecasting financial inclusion.

Key Activities

Explored the unified data schema and reference codes

Analyzed record distribution by:

record type

pillar

source type

confidence level

Identified temporal coverage and data gaps

Added new records including:

Additional observations (financial inclusion indicators, infrastructure data)

Additional events (policy changes, product launches, market milestones)

New impact links connecting events to indicators

Outputs

Updated unified dataset following the original schema

data_enrichment_log.md documenting:

Data sources

Confidence levels

Rationale for inclusion

Clean commits and branch management using GitHub

📊 Task 2: Exploratory Data Analysis (EDA)
Objective

To analyze historical trends and identify factors influencing financial inclusion in Ethiopia.

Key Analyses
1. Dataset Overview

Summary by record type, pillar, and source

Confidence level distribution

Identification of sparse indicators

2. Access (Account Ownership)

Visualization of account ownership trends (2011–2024)

Growth rate analysis between survey years

Investigation of the slowdown between 2021 and 2024

Gender and urban–rural comparisons (where data permits)

3. Usage (Digital Payments)

Mobile money adoption trends

Digital payment usage patterns

Comparison between registered and active usage

4. Infrastructure & Enablers

Analysis of infrastructure indicators (e.g., mobile coverage, agent density)

Identification of leading indicators for financial inclusion

5. Event Timeline Analysis

Visualization of key events over time

Overlay of events on inclusion indicators

Preliminary insights into event-indicator relationships
