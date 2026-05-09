from flask import Flask, jsonify
from core.financial_evaluator import evaluate_company
from core.risk_memo_agent import generate_risk_memo
from core.pdf_generator import save_report_as_pdf

app = Flask(__name__)

@app.route("/run-analysis", methods=["GET"])
def run_analysis():

    companies = ["AlphaBank", "BetaFinance", "GammaCapital"]
    results = []

    for company in companies:
        result = evaluate_company(company)
        memo = generate_risk_memo(result)

        if result["risk_score"] >= 70:
            action = "Escalate to Risk Committee"
        elif result["risk_score"] >= 40:
            action = "Monitor Closely"
        else:
            action = "No Immediate Action Required"

        save_report_as_pdf(result, memo, action,
                           filename=f"{result['company']}_report.pdf")

        results.append({
            "company": company,
            "risk_score": result["risk_score"],
            "risk_level": result["risk_level"],
            "action": action
        })

    return jsonify({"status": "success", "results": results})


if __name__ == "__main__":
    app.run(port=5000)