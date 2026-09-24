from langchain_groq import ChatGroq     
from dotenv import load_dotenv      

load_dotenv()

llm=ChatGroq(                       
    model="openai/gpt-oss-20b"
)

while True:
    prompt = input("Enter your prompt: ")
    if prompt == "exit":
        break
    response = llm.invoke(prompt)
    print(response.content)
