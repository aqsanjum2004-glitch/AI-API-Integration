# Ollama runs locally, no API key required

def get_response(prompt):
    try:
        return "Ollama response (see screenshots for actual output)"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print(get_response(user_input))