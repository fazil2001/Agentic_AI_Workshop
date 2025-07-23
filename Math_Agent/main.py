from agent import app

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = app.invoke({"query": user_input})
    print("Bot:", response.get("response", "Sorry, something went wrong."))
