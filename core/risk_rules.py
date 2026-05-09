def check_credit_risk(revenue_growth, debt_equity):
    """
    Credit risk occurs when revenue is falling significantly
    and leverage (debt) is high.
    """
    return revenue_growth < -15 and debt_equity > 2


def check_liquidity_risk(current_ratio, operating_cash_flow):
    """
    Liquidity risk occurs when short-term solvency is weak
    or operating cash flow is negative.
    """
    return current_ratio < 1.2 or operating_cash_flow < 0


def check_profitability_risk(profit_margin):
    """
    Profitability risk occurs when margins fall below threshold.
    """
    return profit_margin < 6


def calculate_risk_score(
    credit_flag,
    liquidity_flag,
    profit_flag,
    revenue_trend,
    debt_trend,
    cashflow_trend
):
    """
    Composite risk scoring using:
    - Current quarter flags
    - Multi-quarter trend signals
    """

    score = 0

    # Immediate risk signals
    if credit_flag:
        score += 30

    if liquidity_flag:
        score += 25

    if profit_flag:
        score += 20

    # Trend-based signals
    if revenue_trend["decrease_count"] >= 2:
        score += 15

    if debt_trend["increase_count"] >= 2:
        score += 10

    if cashflow_trend["decrease_count"] >= 2:
        score += 10

    return min(score, 100)