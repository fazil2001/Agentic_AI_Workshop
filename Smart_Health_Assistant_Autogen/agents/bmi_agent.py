from vertexai.preview.generative_models import GenerativeModel

def analyze_bmi(bmi_score):
    model = GenerativeModel("gemini-pro")
    prompt = f"My BMI is {bmi_score}. What category does it fall under and what are your health recommendations?"
    response = model.generate_content(prompt)
    return response.text
