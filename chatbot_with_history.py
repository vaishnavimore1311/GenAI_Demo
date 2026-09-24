from langchain_groq import ChatGroq     
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv      

load_dotenv()

"""Chatbot with proper history"""
llm=ChatGroq(                       
    model="openai/gpt-oss-20b"
)
print("My First Chatbot")
history = []

while True:
    prompt = input("Enter your prompt: ")
    history.append(HumanMessage(content=prompt))
    if prompt == "exit":
        break
    response = llm.invoke(history)
    history.append(AIMessage(content=response.content))
    print(response.content)
    
print(history)
