def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm ChatBuddy, your virtual assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "machine learning" in user_input:
        return "Machine learning is a branch of artificial intelligence that enables computers to learn from data and improve their performance without being explicitly programmed. It uses algorithms to identify patterns and make predictions or decisions based on new data."
    else:
        return "I'm not sure I understand. Can you say that differently?"
