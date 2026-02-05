Forecasting Financial Inclusion in Ethiopia

10 Academy – Artificial Intelligence Mastery | Week 10 Challenge

📌 Project Overview

Ethiopia is experiencing rapid growth in digital financial services driven by mobile money platforms such as Telebirr and M-Pesa, regulatory reforms, and digital infrastructure expansion. However, despite this growth, overall financial inclusion—especially formal account ownership—has recently stagnated.

This project was conducted on behalf of a consortium of stakeholders, including:

Development Finance Institutions (DFIs) – to evaluate whether digital finance expansion is translating into real inclusion outcomes and to guide investment priorities.

Mobile Network Operators (MNOs) – to understand the gap between registered users and active financial participation.

National Bank of Ethiopia (NBE) – to assess policy effectiveness, guide regulatory decisions, and track progress toward national financial inclusion targets.

The goal is to build a data-driven forecasting system that explains past trends, models policy and market impacts, and forecasts Ethiopia’s financial inclusion trajectory for 2025–2027.

🎯 Core Objectives

Build a unified dataset combining financial indicators, national events, and policy targets

Analyze historical trends in financial access and usage

Model how events (policies, product launches, infrastructure) affect inclusion outcomes

Forecast financial inclusion for 2025–2027 under multiple scenarios

Present insights through an interactive dashboard for decision-makers

🌍 Financial Inclusion Framework

The project follows the World Bank Global Findex definitions:

🔹 Access – Account Ownership

Percentage of adults (15+) who:

Have an account at a bank or financial institution, or

Personally used a mobile money service in the past 12 months

🔹 Usage – Digital Payments

Percentage of adults who:

Made or received digital payments

Used mobile money, cards, or internet-based payments

🗂️ Repository Structure
ethiopia-fi-forecast/
│
├── data/
│   ├── raw/
│   │   ├── ethiopia_fi_unified_data.csv
│   │   └── reference_codes.csv
│   └── processed/
│
├── notebooks/
│   ├── task_1_data_exploration.ipynb
│   ├── task_2_eda.ipynb
│   ├── task_3_impact_modeling.ipynb
│   └── task_4_forecasting.ipynb
│
├── src/
│   ├── __init__.py
│   └── utils.py
│
├── dashboard/
│   └── app.py
│
├── reports/
│   ├── data_enrichment_log.md
│   └── figures/
│
├── tests/
├── requirements.txt
├── README.md
└── .gitignore

✅ Task 1: Data Exploration & Enrichment
Objective

To construct a unified dataset that integrates:

Historical indicators (observations)

Major national milestones (events)

Logical cause-effect relationships (impact links)

Key Activities

Explored the unified schema and reference codes

Reviewed record distribution by type, pillar, and confidence level

Identified temporal and indicator coverage gaps

Enriched the dataset with recent and relevant data

Key Data Additions

2025 Mobile Money Accounts: 139.5M registered accounts (NBE)

Fayda Digital ID: 33M+ registrations as a structural enabler

Mandatory Fuel Digitization (2024): Policy forcing digital payments

Added impact links connecting policies to access and usage indicators

Outputs

Enriched unified dataset

data_enrichment_log.md documenting sources, confidence, and rationale

📊 Task 2: Exploratory Data Analysis (EDA)
Objective

To understand historical patterns, structural bottlenecks, and early signals driving financial inclusion trends.

Key Findings

Stagnation Mystery: Account ownership grew only +3pp (46% → 49%) between 2021–2024 despite massive mobile money growth.

Registration Gap: Over 130M mobile money accounts vs. only 49% reported ownership.

Digital Leadership: Digital P2P transfers now exceed ATM cash withdrawals.

Policy Impact: Mandatory fuel digitization caused visible usage spikes.

Gender Gap: Men remain significantly more likely to own accounts than women.

Outputs

EDA notebook with visualizations

Summary of key insights and data limitations

🔗 Task 3: Event Impact Modeling
Objective

To model how and why events change financial inclusion indicators.

Approach

Used impact_link records to define:

Impact direction (positive/negative)

Impact magnitude (elasticity)

Time delay (lag)

Built an event–indicator association matrix

Used comparable-country evidence where Ethiopian data was limited

Outputs

Impact modeling notebook

Event–indicator matrix (table/heatmap)

Documented assumptions and uncertainty

🔮 Task 4: Forecasting Financial Inclusion (2025–2027)
Objective

To project future access and usage trends under uncertainty.

Methodology

Combined:

Historical trends

Event-driven impacts

Generated three scenarios:

Baseline

Optimistic

Pessimistic

Included confidence intervals and scenario ranges

Outputs

Forecast tables and visualizations

Scenario comparison charts

Written policy-relevant interpretation

🖥️ Task 5: Dashboard Development
Objective

To communicate insights and forecasts through an interactive interface.

Features

Built using Streamlit

Pages include:

Overview (key metrics & trends)

Trends (interactive time series)

Events (timeline overlays)

Forecasts (scenario selection & confidence intervals)

Data download functionality included

Output

Fully functional interactive dashboard (dashboard/app.py)

⚠️ Data Limitations

Sparse Time Series: Findex surveys every 3 years

Limited Regional Data: Incomplete rural vs. urban breakdown for 2024

Confidence Levels: Some event impacts marked Medium Confidence pending official updates

All limitations are explicitly documented and incorporated into uncertainty estimates.

🏁 Conclusion

This project demonstrates that Ethiopia’s financial inclusion challenge has shifted from access expansion to meaningful usage, trust, infrastructure readiness, and gender equity. By integrating data, events, and policy logic, the system provides forward-looking insights to support regulatory planning, investment decisions, and inclusive digital finance strategies for 2025–2027.
