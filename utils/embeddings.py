# from langchain_community.embeddings import LLMRailsEmbeddings
from langchain_community.embeddings import GPT4AllEmbeddings

# Initialize Langchain embeddings
embeddings = GPT4AllEmbeddings()

# Function to vectorize data


def vectorize_data(data):
    vectorized_data = []
    for entry in data['data']:
        question = entry.get("question")
        answer = entry.get("answer")
        if question and answer:
            question_vector = embeddings.embed_query(question)
            vectorized_data.append((question_vector, answer))
    return vectorized_data
