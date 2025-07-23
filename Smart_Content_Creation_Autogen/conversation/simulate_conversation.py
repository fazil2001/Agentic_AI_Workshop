from agents.creator_agent import ContentCreatorAgent
from agents.critic_agent import ContentCriticAgent

def simulate_conversation(max_turns=3):
    creator = ContentCreatorAgent()
    critic = ContentCriticAgent()

    draft = creator.create_draft()
    print(f"\nTurn 1 - Initial Draft:\n{draft}\n")

    for turn in range(2, max_turns + 1):
        feedback = critic.give_feedback(draft)
        print(f"\nTurn {turn} - Feedback:\n{feedback}\n")

        draft = creator.revise_draft(draft, feedback)
        print(f"\nTurn {turn} - Revised Draft:\n{draft}\n")

    with open("output/final_content.md", "w", encoding="utf-8") as f:
        f.write(draft)

    print("\nFinal refined content written to output/final_content.md.")
