import os

# Get API key from environment variable
api_key = os.getenv("HUGGINGFACE_API_KEY")

# Error handling if key is missing
if not api_key:
    print("Error: API key not found. Please set environment variable.")
    exit()

def get_response(prompt):
    try:
        # Replace this with actual API call
        response = "API response will come here"
        return response
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Response:")
    print(get_response(user_input))