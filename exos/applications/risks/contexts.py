from exos.applications.portfolios.contexts import PortfolioContext


# Contexte borné RiskManagementContext
class RiskManagementContext:
    def __init__(self, portfolio_context: PortfolioContext):
        self.portfolio_context = portfolio_context

    def calculate_portfolio_risk(self) -> float:
        # to do
