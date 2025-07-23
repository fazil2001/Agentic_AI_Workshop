from vertexai.preview.generative_models import GenerativeModel

def generate_workout_plan(diet_plan, age, gender):
    model = GenerativeModel("gemini-pro")
    prompt = (
        f"Based on the following diet plan: {diet_plan}, and for a {age}-year-old {gender}, "
        "generate a 7-day workout schedule tailored to the user."
    )
    response = model.generate_content(prompt)
    return response.text
