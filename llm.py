# Import necessary libraries
from langchain_openai import ChatOpenAI 
from langchain.prompts import ChatPromptTemplate

# Initialize the LLM with gpt-4o-mini
llm = ChatOpenAI(model_name='gpt-4o-mini')

# Define the chat prompt template for the therapy bot
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a therapy bot. Your goal is to provide supportive and empathetic responses to users who may be experiencing a variety of emotional and psychological challenges. Always be respectful, understanding, and provide helpful advice when appropriate."),
        ("user", "{user_input}")
    ]
)

# Function to generate a response from the therapy bot
def generate_response(user_input):
    prompt = chat_prompt_template.format(user_input=user_input)
    response = llm.generate(prompt)
    return response 