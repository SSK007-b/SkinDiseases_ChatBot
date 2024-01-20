import numpy as np
from utils.embeddings import embeddings

def find_closest_answer(query_vector, vectorized_data):
    closest_answer = None
    min_distance = float('inf')
    query_vector = np.array(query_vector)

    for question_vector, answer in vectorized_data:
        question_vector = np.array(question_vector)
        distance = np.linalg.norm(query_vector - question_vector)
        if distance < min_distance:
            min_distance = distance
            closest_answer = answer
    if min_distance > 1:
        closest_answer = "Sorry, I don't understand. Not in my database."

    return closest_answer

def get_chatbot_response(input_query, vectorized_data):
    query_vector = embeddings.embed_query(input_query)
    response = find_closest_answer(query_vector, vectorized_data)
    if response == "Sorry, I don't understand. Not in my database.":
        return f"🤖: Oops! It seems I don't have an answer to that question. Could you try asking something else?"
    else:
        return f"🤖: Here's what I found:\n {response}"