class CriticAgent:
    def review(self, insights):
        if "NaN" in insights:
            return "Consider handling missing values."
        return "Looks good."