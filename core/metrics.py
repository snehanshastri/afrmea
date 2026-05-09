def calculate_revenue_growth(current_rev, previous_rev):
    if previous_rev == 0:
        return 0
    return ((current_rev - previous_rev) / previous_rev) * 100


def net_profit_margin(net_profit, revenue):
    if revenue == 0:
        return 0
    return (net_profit / revenue) * 100


def debt_to_equity(total_debt, equity):
    if equity == 0:
        return 0
    return total_debt / equity


def current_ratio(current_assets, current_liabilities):
    if current_liabilities == 0:
        return 0
    return current_assets / current_liabilities