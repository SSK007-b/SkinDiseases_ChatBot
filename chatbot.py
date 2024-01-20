import chainlit as cl
from utils.responses import get_chatbot_response
from utils.embeddings import vectorize_data
from utils.loader import load_json_data
import dotenv

dotenv.load_dotenv()

data = load_json_data("data.json")
vectorized_data = vectorize_data(data)


@cl.on_message
async def chatbot_ui(message):
    user_input = message.content
    if user_input:
        response = get_chatbot_response(user_input, vectorized_data)
        await cl.Message(response).send()

if __name__ == "__main__":
    chatbot_ui()
