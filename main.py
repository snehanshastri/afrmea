from core.financial_evaluator import evaluate_company
from core.risk_memo_agent import generate_risk_memo
from core.pdf_generator import save_report_as_pdf

companies = ["AlphaBank", "BetaFinance", "GammaCapital"]

for company in companies:
    result = evaluate_company(company)
    memo = generate_risk_memo(result)

    if result["risk_score"] >= 70:
        action = "Escalate to Risk Committee"
    elif result["risk_score"] >= 40:
        action = "Monitor Closely"
    else:
        action = "No Immediate Action Required"

    print("\n=== FINANCIAL RISK REPORT ===")
    print(f"Company: {result['company']}")
    print(f"Risk Score: {result['risk_score']}/100")
    print(f"Risk Level: {result['risk_level']}")
    print(f"Recommended Action: {action}")
    print("\n--- Risk Memo ---")
    print(memo)

    save_report_as_pdf(result, memo, action, filename=f"{result['company']}_report.pdf")