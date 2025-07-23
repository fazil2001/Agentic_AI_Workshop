from vertexai.preview.generative_models import GenerativeModel

def plan_diet(bmi_analysis, dietary_pref):
    model = GenerativeModel("gemini-pro")
    prompt = (
        f"Based on this BMI report: {bmi_analysis}, and the dietary preference being {dietary_pref}, "
        "suggest a healthy 3-meal diet plan for one day."
    )
    response = model.generate_content(prompt)
    return response.text
