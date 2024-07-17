import csv
import google.generativeai as genai
from dotenv import load_dotenv
import os

env_path = "C:/Users/Victoria/Gemini chatbot/LLM-Gemini-chatbot/.env"
load_dotenv(dotenv_path=env_path)
# Set up the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Load your CSV data
def load_data(csv_file):
    data = []
    with open(csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


# Initialize the model
model = genai.GenerativeModel("gemini-pro")

# Create a chat session
chat = model.start_chat(history=[])


# Function to get response from the model
def get_response(query, context):
    response = chat.send_message(f"Context: {context}\n\nQuestion: {query}")
    return response.text


# Main chatbot loop
def chatbot(csv_file):
    data = load_data(csv_file)
    context = str(data)  # Convert data to string for context

    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input, context)
        print("Chatbot:", response)


# Run the chatbot
chatbot("C:/Users/Victoria/Gemini chatbot/LLM-Gemini-chatbot/Updated_sales.csv")
