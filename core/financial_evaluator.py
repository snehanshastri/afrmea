import pandas as pd

from core.metrics import (
    calculate_revenue_growth,
    net_profit_margin,
    debt_to_equity,
    current_ratio
)

from core.risk_rules import (
    check_credit_risk,
    check_liquidity_risk,
    check_profitability_risk,
    calculate_risk_score
)

from core.trend_analysis import analyze_trend


def evaluate_company(company_name, data_path="data/company_financials.csv"):

    df = pd.read_csv(data_path)
    company_data = df[df["company"] == company_name].reset_index(drop=True)

    if len(company_data) < 2:
        raise ValueError("Not enough data to evaluate company.")

    # Last quarter vs previous quarter
    current = company_data.iloc[-1]
    previous = company_data.iloc[-2]

    revenue_growth = calculate_revenue_growth(
        current["revenue"], previous["revenue"]
    )

    profit_margin = net_profit_margin(
        current["net_profit"], current["revenue"]
    )

    debt_equity = debt_to_equity(
        current["total_debt"], current["equity"]
    )

    curr_ratio = current_ratio(
        current["current_assets"], current["current_liabilities"]
    )

    credit_flag = check_credit_risk(revenue_growth, debt_equity)
    liquidity_flag = check_liquidity_risk(curr_ratio, current["operating_cash_flow"])
    profit_flag = check_profitability_risk(profit_margin)

    revenue_trend = analyze_trend(company_data["revenue"].tolist())
    debt_trend = analyze_trend(company_data["total_debt"].tolist())
    cashflow_trend = analyze_trend(company_data["operating_cash_flow"].tolist())

    risk_score = calculate_risk_score(
        credit_flag,
        liquidity_flag,
        profit_flag,
        revenue_trend,
        debt_trend,
        cashflow_trend
    )

    return {
        "company": company_name,
        "risk_score": risk_score,
        "risk_level": (
            "High" if risk_score >= 70
            else "Moderate" if risk_score >= 40
            else "Low"
        ),
        "metrics": {
            "revenue_growth": float(revenue_growth),
            "profit_margin": float(profit_margin),
            "debt_equity": float(debt_equity),
            "current_ratio": float(curr_ratio)
        },
        "risk_flags": {
            "credit_risk": bool(credit_flag),
            "liquidity_risk": bool(liquidity_flag),
            "profitability_risk": bool(profit_flag)
        },
        "trend": {
            "revenue_trend": revenue_trend,
            "debt_trend": debt_trend,
            "cashflow_trend": cashflow_trend
        }
    }