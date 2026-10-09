from langchain_groq import ChatGroq   # to use framework langchain we are import chatgroq
from dotenv import load_dotenv              #to make api key accessible

load_dotenv(override=True)
# every llm provider sathi classes astat
llm = ChatGroq(model="openai/gpt-oss-20b",temperature=0.8,max_tokens=300)            #create an object -->chatgroq is class name
# payground --> model="openai/gpt-oss-20b" , temperature=0.8 , max_tokens=300
# groq buy the openai model and provide it to us
# temperature 0 ---> normal responce--->temperature 0.9--->
# generally temperature range is 0-1 ---> it's not recommened but also have 1.2
# no max_tockens, max_tockens = 300 , max_tockens = 200 , max_tockens = 100 

prompt = input("User Input : ")
response = llm.invoke(prompt)           # .invoke-->prompt--->llm la gheun jato ani vapas response gheun yeto
print(response.content)

# max tocken is use to limit the response length, if we don't use max tocken then it will give us long response

