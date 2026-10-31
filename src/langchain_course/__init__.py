from dotenv import load_dotenv
import os 
load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))


main()