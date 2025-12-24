# 📊 Financial Analysis Agent Crew

A production-ready **Multi-Agent AI Financial Analysis System** that simulates a real financial research team.  
Autonomous AI agents collaborate to research market sentiment, analyze stock performance, and generate professional PDF reports.


## 🚀 Project Overview

This project demonstrates **Agentic AI architecture** where multiple specialized agents work together under an orchestration layer to produce end-to-end financial analysis.

### 🧠 Agents Involved
- **Market Researcher Agent** – Collects market news and sentiment
- **Data Analyst Agent** – Fetches stock price data and calculates KPIs
- **Report Writer Agent** – Generates a structured PDF financial report
- **Orchestration Layer** – Coordinates agents and maintains conversation logs

The system accepts a **stock ticker (e.g., AAPL)** and outputs a **complete financial report with insights and logs**.


## ✨ Key Features

- ✅ Multi-agent orchestration (agent collaboration)
- ✅ Real-time stock data using Yahoo Finance
- ✅ Financial KPIs & chart generation
- ✅ Professional PDF report generation
- ✅ Agent conversation logs for transparency
- ✅ Streamlit-based interactive dashboard
- ✅ CLI + UI execution support
- ✅ Graceful error handling & partial-data warnings


## 🏗️ Architecture Overview

User Input (Ticker)
│
▼
Orchestration Layer (crew.py)
│
├── Market Researcher Agent
├── Data Analyst Agent
└── Report Writer Agent
│
▼
PDF Report + Agent Logs


## 🛠️ Tech Stack

- **Programming Language:** Python
- **AI / LLM:** Gemini
- **Finance API:** Yahoo Finance
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib
- **PDF Generation:** fpdf2
- **UI:** Streamlit


## 📂 Project Structure

Financial_Analysis_Agent_Crew/
│
├── agents/
│ ├── market_researcher.py
│ ├── data_analyst.py
│ └── report_writer.py
│
├── orchestration/
│ └── crew.py
│
├── tools/
│ ├── pdf_generator.py
│ ├── ticker_utils.py
│ └── charts.py
│
├── reports/
│ └── .gitkeep
│
├── app.py
├── main.py
├── lambda_handler.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore


## ▶️ How to Run the Project

### 🔹 1. Install Dependencies
```bash
pip install -r requirements.txt