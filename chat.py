import openai

openai.api_key = 'sk-sRn2GpKRDPm39Hko11EMaiLi3gqRSzdlA8IOMsiHETT3BlbkFJKv1p3Pjq8GKbxHxPpvARfRQMajRJ0iybacmbMm9KoA'  # Replace with your actual API key

def generate_response(user_input):
    # Create a message history
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]

    # Get response from the ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model for your application
        messages=messages
    )

    # Return the content of the assistant's response
    return response['choices'][0]['message']['content']
