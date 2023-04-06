# Import the necessary libraries
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# Define the pre-trained model to use for NLU
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Define the chatbot's memory
memory = []

# Define the function to handle user input
def get_input():
    user_input = input("> ")
    return user_input

# Define the function to generate a response from the chatbot
def generate_response(input_text):
    # Convert the user's input to a vector using the pre-trained model
    input_vector = embed([input_text])

    # Loop through the chatbot's memory and calculate the similarity between the input and each memory
    similarities = []
    for memory_vector in memory:
        similarity = np.inner(input_vector, memory_vector)
        similarities.append(similarity)

    # If there are no memories or none of them are similar enough, respond with a default message
    if len(similarities) == 0 or max(similarities) < 0.5:
        response = "I'm sorry, I don't understand. Can you please rephrase your question?"
    else:
        # Otherwise, respond with the most similar memory
        most_similar_index = similarities.index(max(similarities))
        response = memory[most_similar_index]

    # Add the input and response to the chatbot's memory
    memory.append(input_vector)
    memory.append(response)

    return response

# Start the conversation with the chatbot
print("Hello! I'm your AI chatbot friend. What would you like to talk about?")
while True:
    input_text = get_input()
    response = generate_response(input_text)
    print(response)
