# AI-Based Financial Risk Monitoring System

## Overview

This project is an AI-driven Financial Risk Monitoring System developed as part of the Bharat Unnati AI Fellowship internship program. The system analyzes company financial data, identifies financial risks, performs trend analysis, generates AI-based financial risk memos, and produces automated PDF reports.

The project simulates a simplified version of financial risk monitoring systems used in banking and financial institutions.

---

## Features

* Financial ratio analysis
* Rule-based risk detection
* Multi-quarter trend analysis
* Composite risk scoring
* AI-generated financial risk memo using Gemini API
* Automated PDF report generation
* Flask API integration
* n8n workflow automation support
* External API access using ngrok

---

## Financial Metrics Used

The system calculates and analyzes:

* Revenue Growth
* Net Profit Margin
* Debt-to-Equity Ratio
* Current Ratio
* Operating Cash Flow Trends

---

## Risk Categories Detected

* Credit Risk
* Liquidity Risk
* Profitability Risk

---

## Technologies and Tools Used

### Programming Language

* Python

### Libraries and Frameworks

* Pandas
* Flask
* ReportLab
* Google Gemini API

### Automation and Deployment Tools

* n8n
* ngrok

### Development Environment

* VS Code

---

## Project Workflow

Financial Data
      ↓
Financial Metrics Calculation
      ↓
Risk Detection Logic
      ↓
Trend Analysis
      ↓
Risk Score Generation
      ↓
AI-Based Risk Memo Generation
      ↓
PDF Report Generation
      ↓
Flask API Deployment
      ↓
n8n Workflow Automation
```

---

## Folder Structure

```
afrmea/
│
├── core/
│   ├── financial_evaluator.py
│   ├── metrics.py
│   ├── risk_rules.py
│   ├── trend_analysis.py
│   ├── risk_memo_agent.py
│   └── pdf_generator.py
│
├── data/
│   └── company_financials.csv
│
├── api.py
├── main.py
├── requirements.txt
└── README.md


## How to Run the Project

### 1. Clone the Repository


git clone <repository-link>
cd financial-risk-monitoring-system


---

### 2. Install Dependencies
pip install -r requirements.txt

---

### 3. Configure Gemini API Key

Create a `.env` file and add:

GEMINI_API_KEY=your_api_key_here

### 4. Run Main Project
python main.py

### 5. Run Flask API
python api.py

### 6. Expose API Using ngrok
ngrok http 5000

---

### 7. Integrate with n8n

Use the generated ngrok URL inside the HTTP Request node in n8n.

Example endpoint:


https://your-ngrok-url.ngrok-free.app/run-analysis


---

## Sample Output

The system generates:

* Structured financial risk evaluation
* AI-generated financial memo
* Professional PDF financial report
* JSON API response

---

## Learning Outcomes

* Financial data analysis
* Backend API development
* AI integration using LLMs
* Workflow automation
* Report generation
* Modular software design

---

## Program Outcomes (POs) Mapped

* PO1 – Engineering Knowledge
* PO2 – Problem Analysis
* PO3 – Design and Development of Solutions
* PO4 – Investigation of Problems
* PO5 – Modern Tool Usage
* PO10 – Communication
* PO12 – Life-long Learning

---

## Sustainable Development Goals (SDGs)

* SDG 8 – Decent Work and Economic Growth
* SDG 9 – Industry, Innovation and Infrastructure

---

## Internship Details

Developed as part of:

**Bharat Unnati AI Fellowship**
(CodeXpert + Expertpedia + Generative AI + Agentic AI)

Conducted under:
**Learner’s Byte Global InfoVision Pvt. Ltd.**

---

## Author

Sneha N Shastri
BMS College of Engineering
Department of Computer Science and Engineering
