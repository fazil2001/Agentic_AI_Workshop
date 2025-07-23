class ReportGeneratorAgent:
    def generate(self, df, insights, visual_path, feedback):
        with open("reports/eda_report.md", "w") as f:
            f.write("# EDA Report\n\n")
            f.write("## Dataset Overview\n")
            f.write(df.head().to_markdown() + "\n\n")
            f.write("## Statistical Summary\n")
            f.write(insights + "\n\n")
            f.write("## Feedback\n")
            f.write(feedback + "\n\n")
            f.write("## Visualizations\n")
            f.write(f"![EDA Plot]({visual_path})\n")
        return "reports/eda_report.md"
