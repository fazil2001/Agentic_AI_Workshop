import PyPDF2
from config import GOOGLE_API_KEY
from langchain.chat_models import ChatGooglePalm
from langchain.prompts import PromptTemplate


def extract_text_from_pdf(pdf_path: str) -> str:
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


def load_prompt(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def generate_summary(llm, content: str) -> str:
    template = load_prompt("prompts/summarizer_prompt.txt")
    prompt = PromptTemplate(input_variables=["content"], template=template)
    return llm.predict(prompt.format(content=content))


def generate_quiz(llm, summary: str) -> str:
    template = load_prompt("prompts/quiz_prompt.txt")
    prompt = PromptTemplate(input_variables=["summary"], template=template)
    return llm.predict(prompt.format(summary=summary))


def main():
    pdf_path = "docs/sample_study_material.pdf"
    print("📄 Reading PDF...")
    content = extract_text_from_pdf(pdf_path)

    llm = ChatGooglePalm(google_api_key=GOOGLE_API_KEY, temperature=0.5)

    print("📝 Generating summary...")
    summary = generate_summary(llm, content)
    print("\n✅ Summary:\n", summary)

    print("\n🧠 Generating quiz questions...")
    quiz = generate_quiz(llm, summary)
    print("\n📚 Quiz:\n", quiz)


if __name__ == "__main__":
    main()
