import os
from dotenv import load_dotenv
from vertexai import init

from agents.user_proxy_agent import collect_user_data
from tools.bmi_tool import calculate_bmi
from agents.bmi_agent import analyze_bmi
from agents.diet_planner_agent import plan_diet
from agents.workout_scheduler_agent import generate_workout_plan

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Vertex AI (Replace with your actual project info)
init(project="your-project-id", location="us-central1")

def main():
    user_data = collect_user_data()

    bmi_score = calculate_bmi(user_data["weight"], user_data["height"])
    print(f"\n✅ Calculated BMI: {bmi_score}\n")

    bmi_feedback = analyze_bmi(bmi_score)
    print("🏥 BMI Analysis & Health Advice:\n", bmi_feedback)

    diet_plan = plan_diet(bmi_feedback, user_data["dietary_preference"])
    print("\n🥗 Suggested Diet Plan:\n", diet_plan)

    workout_plan = generate_workout_plan(diet_plan, user_data["age"], user_data["gender"])
    print("\n💪 Weekly Workout Plan:\n", workout_plan)

if __name__ == "__main__":
    main()
