class InvestmentAdvisorAgent:
    def generate_report(self, analysis, recommendations):
        print("\n--- Personalized Financial Report ---")
        print(f"Salary: ₹{analysis['salary']}")
        print("Portfolio:")
        print(f"  Fixed Deposits: ₹{analysis['fd']}")
        print(f"  SIPs: ₹{analysis['sip']}")
        print(f"  Real Estate: ₹{analysis['real_estate']}")
        print("\nRecommended Investments:")
        for rec in recommendations:
            print(f"- {rec}")

investment_advisor_agent = InvestmentAdvisorAgent()