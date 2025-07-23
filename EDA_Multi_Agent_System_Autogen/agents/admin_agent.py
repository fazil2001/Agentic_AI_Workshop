from agents.data_preparation_agent import DataPreparationAgent
from agents.eda_agent import EDAAgent
from agents.executor_agent import ExecutorAgent
from agents.critic_agent import CriticAgent
from agents.report_generator_agent import ReportGeneratorAgent

class AdminAgent:
    def __init__(self):
        self.data_agent = DataPreparationAgent()
        self.eda_agent = EDAAgent()
        self.executor = ExecutorAgent()
        self.critic = CriticAgent()
        self.reporter = ReportGeneratorAgent()

    def run(self, filepath):
        cleaned_df = self.data_agent.clean_data(filepath)
        insights, visuals = self.eda_agent.analyze_data(cleaned_df)
        if self.executor.validate(insights):
            feedback = self.critic.review(insights)
            final_report = self.reporter.generate(cleaned_df, insights, visuals, feedback)
            print("EDA completed. Report saved at reports/eda_report.md")
