from agents.growth_investment_agent import growth_investment_agent
from agents.value_investment_agent import value_investment_agent
from agents.investment_advisor_agent import investment_advisor_agent

class StateFlow:
    def route(self, analysis_result):
        category = analysis_result["category"]
        if category == "growth":
            recommendations = growth_investment_agent.recommend(analysis_result)
        else:
            recommendations = value_investment_agent.recommend(analysis_result)

        investment_advisor_agent.generate_report(analysis_result, recommendations)

state_flow = StateFlow()