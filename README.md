`🐍 Python 3.x` • `⚡ PySpark (Big Data)` • `🧱 Databricks Serverless` • `🗄️ Delta Lake` • `🌲 PySpark MLlib` • `✨ Google GenAI` • `🎈 Streamlit App` • `✅ Status: Active`




> 🛡️ **Intelligent FinTech Fraud Detection with Explainable GenAI**  
> A full-stack Data Engineering, Machine Learning, and Generative AI application that processes **6.36M+ financial transactions** in Databricks, predicts fraud risk with **98.90% ROC-AUC**, and generates automated compliance reports with transparency and live visualization.

---

## 🚀 Project Overview

The **FinTech Fraud Detection & GenAI Investigation System** is a cloud-backed data and AI application designed to automate high-volume transaction auditing, fraud risk scoring, and compliance investigation reporting.

It integrates distributed big-data processing with full-stack web visualization by combining a **Databricks & PySpark backend**, **Delta Lake storage**, **PySpark MLlib classification**, and an interactive **Streamlit dashboard**.

*The system not only predicts transaction fraud probability across millions of records, but also translates high-risk alerts into human-readable Suspicious Activity Reports (SARs) using Google GenAI—making it transparent and suitable for real-world banking compliance.*

---

## ✨ Key Features

* 📊 Audit and process **6.36M+ financial transactions** using distributed PySpark DataFrames
* 🔍 Uncover fraud patterns via **Spark SQL** (isolating 100% of fraud in `TRANSFER` & `CASH_OUT` types)
* 🤖 High-performance distributed **PySpark MLlib Random Forest** classifier (**0.9890 ROC-AUC**)
* 🚨 Automated **`>90%` risk threshold filtering** isolating **560 critical alerts** (\$980.37M+ flagged volume)
* 📝 **GenAI-based Suspicious Activity Report (SAR)** generation for instant compliance explainability
* 🗄️ Store cleaned datasets and model predictions in **Databricks Unity Catalog Delta Tables**
* 📈 Interactive **Streamlit web dashboard** with live Databricks SQL Warehouse connectivity & cached fallback

---

## 📊 Functional Capabilities

* Ingest and profile multi-million-row financial transaction logs with zero data loss
* Perform distributed feature engineering (`balance_drop`, `is_account_emptied`)
* Execute scalable ML training and probability scoring across unseen test data
* Filter alerts dynamically via an interactive risk threshold slider (`90%` to `99%`)
* Generate on-demand, plain-English compliance investigation reports for any flagged account

---

## 🛠️ Tech Stack

### ⚙️ Data Engineering & Cloud Platform
* 🧱 **Databricks Serverless** (Unity Catalog & SQL Warehouse)
* ⚡ **Apache Spark & PySpark** (Distributed DataFrames & Spark SQL)
* 🗄️ **Delta Lake** (ACID-compliant Lakehouse Storage)

### 🤖 Machine Learning & Generative AI
* 🌲 **PySpark MLlib** (`RandomForestClassifier`, `VectorAssembler`, `StringIndexer`)
* ✨ **Google GenAI SDK** (`gemma-4-26b-a4b-it` / `gemini-3.8-flash` with fallback resilience)

### 🎨 Frontend & Visualization
* 🎈 **Streamlit** (Interactive Web Dashboard & Sidebar Controls)
* 📊 **Streamlit Native Charts & DataFrames**
* 🔌 **Databricks SQL Connector** (Live HTTPS Lakehouse Querying)

### 🧮 Data Processing
* 🐍 **Python 3.x**
* 🐼 **Pandas**

---

## 🧠 System Architecture

```text
Raw Transaction Logs (Kaggle PaySim — 6.36M Rows)
                        │
                        ▼
Databricks & PySpark ETL Pipeline (Notebook 01)
   ├── Data Profiling & Integrity Audit (0 Nulls, 0 Duplicates)
   ├── Feature Engineering (balance_drop, is_account_emptied)
   ├── Spark SQL Exploratory Analytics
   └── Store Clean Tables in Delta Lake
                        │
                        ▼
Distributed ML Engine — PySpark MLlib (Notebook 02)
   ├── Filter High-Risk Types (TRANSFER & CASH_OUT — 2.77M Rows)
   ├── Train Random Forest Classifier (80/20 Split — 0.9890 ROC-AUC)
   └── Save >90% Risk Alerts to Delta Table (560 Critical Alerts)
                        │
                        ▼
Live Frontend & GenAI Investigator (Streamlit App + Notebook 03)
   ├── Query Live Databricks Delta Table via SQL Connector
   ├── Interactive Risk Slider & Payment Type Filtering
   └── Generate Plain-English SARs via Google GenAI API
                        │
                        ▼
Interactive Fraud Dashboard (KPIs + Alerts Table + GenAI Compliance Report)
```

---

## 🔗 Live Application & Notebooks

* 🌐 **Live Interactive Dashboard:** *[![Python](https://shields.io)
![Apache Spark](https://shields.io)
![Databricks](https://shields.io)
![Delta Lake](https://shields.io)
![MLlib](https://shields.io)
![Google GenAI](https://shields.io)
![Streamlit](https://shields.io)
![License](https://shields.io)
![Status](https://shields.io)

> 🛡️ **Intelligent FinTech Fraud Detection with Explainable GenAI**  
> A full-stack Data Engineering, Machine Learning, and Generative AI application that processes **6.36M+ financial transactions** in Databricks, predicts fraud risk with **98.90% ROC-AUC**, and generates automated compliance reports with transparency and live visualization.

---

## 🚀 Project Overview

The **FinTech Fraud Detection & GenAI Investigation System** is a cloud-backed data and AI application designed to automate high-volume transaction auditing, fraud risk scoring, and compliance investigation reporting.

It integrates distributed big-data processing with full-stack web visualization by combining a **Databricks & PySpark backend**, **Delta Lake storage**, **PySpark MLlib classification**, and an interactive **Streamlit dashboard**.

*The system not only predicts transaction fraud probability across millions of records, but also translates high-risk alerts into human-readable Suspicious Activity Reports (SARs) using Google GenAI—making it transparent and suitable for real-world banking compliance.*

---

## ✨ Key Features

* 📊 Audit and process **6.36M+ financial transactions** using distributed PySpark DataFrames
* 🔍 Uncover fraud patterns via **Spark SQL** (isolating 100% of fraud in `TRANSFER` & `CASH_OUT` types)
* 🤖 High-performance distributed **PySpark MLlib Random Forest** classifier (**0.9890 ROC-AUC**)
* 🚨 Automated **`>90%` risk threshold filtering** isolating **560 critical alerts** (\$980.37M+ flagged volume)
* 📝 **GenAI-based Suspicious Activity Report (SAR)** generation for instant compliance explainability
* 🗄️ Store cleaned datasets and model predictions in **Databricks Unity Catalog Delta Tables**
* 📈 Interactive **Streamlit web dashboard** with live Databricks SQL Warehouse connectivity & cached fallback

---

## 📊 Functional Capabilities

* Ingest and profile multi-million-row financial transaction logs with zero data loss
* Perform distributed feature engineering (`balance_drop`, `is_account_emptied`)
* Execute scalable ML training and probability scoring across unseen test data
* Filter alerts dynamically via an interactive risk threshold slider (`90%` to `99%`)
* Generate on-demand, plain-English compliance investigation reports for any flagged account

---

## 🛠️ Tech Stack

### ⚙️ Data Engineering & Cloud Platform
* 🧱 **Databricks Serverless** (Unity Catalog & SQL Warehouse)
* ⚡ **Apache Spark & PySpark** (Distributed DataFrames & Spark SQL)
* 🗄️ **Delta Lake** (ACID-compliant Lakehouse Storage)

### 🤖 Machine Learning & Generative AI
* 🌲 **PySpark MLlib** (`RandomForestClassifier`, `VectorAssembler`, `StringIndexer`)
* ✨ **Google GenAI SDK** (`gemma-4-26b-a4b-it` / `gemini-3.8-flash` with fallback resilience)

### 🎨 Frontend & Visualization
* 🎈 **Streamlit** (Interactive Web Dashboard & Sidebar Controls)
* 📊 **Streamlit Native Charts & DataFrames**
* 🔌 **Databricks SQL Connector** (Live HTTPS Lakehouse Querying)

### 🧮 Data Processing
* 🐍 **Python 3.x**
* 🐼 **Pandas**

---

## 🧠 System Architecture

```text
Raw Transaction Logs (Kaggle PaySim — 6.36M Rows)
                        │
                        ▼
Databricks & PySpark ETL Pipeline (Notebook 01)
   ├── Data Profiling & Integrity Audit (0 Nulls, 0 Duplicates)
   ├── Feature Engineering (balance_drop, is_account_emptied)
   ├── Spark SQL Exploratory Analytics
   └── Store Clean Tables in Delta Lake
                        │
                        ▼
Distributed ML Engine — PySpark MLlib (Notebook 02)
   ├── Filter High-Risk Types (TRANSFER & CASH_OUT — 2.77M Rows)
   ├── Train Random Forest Classifier (80/20 Split — 0.9890 ROC-AUC)
   └── Save >90% Risk Alerts to Delta Table (560 Critical Alerts)
                        │
                        ▼
Live Frontend & GenAI Investigator (Streamlit App + Notebook 03)
   ├── Query Live Databricks Delta Table via SQL Connector
   ├── Interactive Risk Slider & Payment Type Filtering
   └── Generate Plain-English SARs via Google GenAI API
                        │
                        ▼
Interactive Fraud Dashboard (KPIs + Alerts Table + GenAI Compliance Report)
```

---

## 🔗 Live Application & Notebooks
* 🌐 **Live Interactive Dashboard:** [Open Live Fraud Dashboard](https://fintech-fraud-pyspark-7s7tfqncz3dqbbiujwg3hm.streamlit.app/)

* 📓 `01_Data_Engineering_and_Analytics.ipynb` — PySpark data profiling, feature engineering, Delta Lake & Spark SQL
* 📓 `02_Fraud_Prediction_MLlib.ipynb` — Distributed Random Forest training, ROC-AUC evaluation & `>90%` filtering
* 📓 `03_GenAI_Fraud_Investigator.ipynb` — Automated Suspicious Activity Report (SAR) pipeline
* 🖥️ `app.py` — Full-stack Streamlit web application connected to Databricks SQL Warehouse
]*
* 📓 `01_Data_Engineering_and_Analytics.ipynb` — PySpark data profiling, feature engineering, Delta Lake & Spark SQL
* 📓 `02_Fraud_Prediction_MLlib.ipynb` — Distributed Random Forest training, ROC-AUC evaluation & `>90%` filtering
* 📓 `03_GenAI_Fraud_Investigator.ipynb` — Automated Suspicious Activity Report (SAR) pipeline
* 🖥️ `app.py` — Full-stack Streamlit web application connected to Databricks SQL Warehouse
