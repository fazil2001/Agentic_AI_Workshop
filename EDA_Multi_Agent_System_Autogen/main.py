import os
from agents.admin_agent import AdminAgent
from dotenv import load_dotenv

load_dotenv()

def main():
    admin = AdminAgent()
    admin.run("data/sample_data.csv")

if __name__ == "__main__":
    main()
