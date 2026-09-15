# 🚀 Enterprise E-Commerce Data Platform & Analytics Suite

An end-to-end cloud data platform built using **Microsoft Fabric**, implementing a modern **Medallion Architecture (Bronze, Silver, Gold)**, PySpark data engineering pipelines, Delta Lake tables, and an executive-level Power BI reporting layer.

---

## 📸 Dashboard Preview
*(Once you upload your screenshot to your `screenshots/` folder, it will render right here!)*
![Enterprise E-Commerce Dashboard Preview](screenshots/dashboard_preview.png)

---

## 🏗️ Architecture & Tech Stack
* **Cloud Platform:** Microsoft Fabric, OneLake
* **Data Engineering:** PySpark, Spark SQL, Delta Lake tables, Automated Data Pipelines (`Pipeline_ecoma_ingestion`)
* **Medallion Architecture:**
  * **`lh_bronze`**: Ingests raw transactional and customer data streams.
  * **`lh_silver`**: Cleansed, schema-enforced, and deduplicated transformation layer.
  * **`lh_gold`**: Star Schema dimensional modeling (`dim_customers`, `fact_sales`) optimized for high-performance analytics.
* **BI & Reporting:** Power BI Semantic Model, DAX Measures, and Custom Executive Visualizations.

---

## 📊 Key Data Engineering & Analytics Features
* **Automated Ingestion & Transformations:** Built robust PySpark notebooks (`AK_silver_transformation`, `AK_Gold`) to handle multi-layered data cleaning, surrogate key generation, and relational modeling at scale.
* **Star Schema Optimization:** Modeled clean dimensional relationships between `dim_customers` and `fact_sales` to support sub-second query performance.
* **Executive KPIs & DAX Modeling:** Developed custom business logic in Power BI to track critical retail metrics:
  * `Total Orders` (1M+)
  * `Total Items Sold` (3M+)
  * `Average Quantity per Order`
  * `Active Customers` (50K+)
* **Interactive Visualizations:** Designed an executive suite featuring an Executive KPI banner, monthly Sales Trend analysis line chart, Geographic Demand Map, and Top Customer performance breakdown.

---

## 📁 Repository Structure
```text
enterprise_1/
├── AK_Gold.Notebook/              # Gold layer star schema transformation notebook
├── AK_silver_transformation.Notebook/ # Silver layer data cleansing notebook
├── Pipeline_ecoma_ingestion.DataPipeline/ # Automated Fabric data pipeline
├── generate_raw_data.Notebook/    # Synthetic enterprise data generation source
├── lh_bronze.Lakehouse/           # Bronze layer definitions
├── lh_silver.Lakehouse/           # Silver layer definitions
├── lh_gold.Lakehouse/             # Gold layer definitions
├── gold semantic model.SemanticModel/ # Power BI semantic model definition
├── myreport.Report/               # Power BI executive dashboard definition
└── screenshots/                   # Dashboard visual previews
