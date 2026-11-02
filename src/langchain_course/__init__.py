from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama



import os 
load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    information = """ 
    Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded Zip2, a web software company. Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal. Musk also became an American citizen in 2002.

    In 2002, Musk founded and became CEO and chief engineer of SpaceX, a space technology company. Musk joined Tesla as an angel investor in 2004 and became its CEO and product architect in 2008. In 2015, Musk co-founded OpenAI to advance artificial intelligence (AI) research, but later left; his growing discontent with the organization's direction and leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired Twitter, a social networking service, and made significant changes, including rebranding it as X in 2023. His other businesses include Neuralink, a neurotechnology company that he co-founded in 2016, and the Boring Company, a tunneling company that he founded in 2017. In November 2025, Tesla approved a pay package worth $1 trillion for Musk, which he is to receive over 10 years if certain milestones are met, such as achieving a market capitalization of $8.5 trillion. Musk became the first US-dollar trillionaire upon the initial public offering of SpaceX in June 2026, though a SpaceX stock collapse brought him under the threshold by the next month.
 
    """
        
    summary_template = """
    You are given information about Elon Musk.

    Based ONLY on the information provided below,
    perform the following tasks:

    1. Write a short summary of Elon Musk.
    2. Provide two interesting facts about Elon Musk.

    Important instructions:
    - Do not invent any names or information.
    - Do not introduce another person.
    - Use only the information provided.
    - If something is not mentioned, do not assume it.

    Information:
    {information}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model='gpt-5')
    llm = ChatOllama(
    model="gemma3:270m",
    temperature=0
    )
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)


main()