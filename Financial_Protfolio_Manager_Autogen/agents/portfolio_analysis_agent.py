class PortfolioAnalysisAgent:
    def analyze(self):
        print("Portfolio Agent: Please provide your salary and portfolio details.")
        salary = float(input("Enter current salary: "))
        fd = float(input("Amount in Fixed Deposits: "))
        sip = float(input("Amount in SIPs: "))
        real_estate = float(input("Amount in Real Estate: "))
        
        total = fd + sip + real_estate
        ratio = sip / total if total > 0 else 0

        category = "growth" if ratio > 0.5 else "value"
        print(f"Portfolio Analysis Result: {category.upper()} investment preferred.")
        return {
            "salary": salary,
            "fd": fd,
            "sip": sip,
            "real_estate": real_estate,
            "category": category
        }

portfolio_analysis_agent = PortfolioAnalysisAgent()