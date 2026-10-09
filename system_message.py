from langchain_groq import ChatGroq     
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv      

# human, AI, system msg
# 
load_dotenv()

"""Chatbot with proper history"""
llm=ChatGroq(                       
    model="openai/gpt-oss-20b", max_tokens=200
)
print("My First Chatbot")
messages = [
    SystemMessage(content="You are Funny AI assistant, reply in funny way")    # set behavior ---> funny , angree
]
# system prompt --> You are Funny AI assistant, reply in funny way ---->You are Angry AI assistant, reply in Angry/arrogent way,----> You are Sad AI assistant, reply in Sadly

while True:
    prompt = input("Enter your prompt: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "exit":
        break
    response = llm.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print(response.content)
    
# print(messages)
