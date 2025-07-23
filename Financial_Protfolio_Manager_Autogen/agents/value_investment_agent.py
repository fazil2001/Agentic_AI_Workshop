class ValueInvestmentAgent:
    def recommend(self, analysis):
        print("Value Agent: Suggesting stable investments...")
        return [
            "Blue-chip Stocks",
            "Public Provident Fund (PPF)",
            "Real Estate Investment Trusts (REITs)"
        ]

value_investment_agent = ValueInvestmentAgent()