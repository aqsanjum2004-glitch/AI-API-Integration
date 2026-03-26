import requests

API_KEY = "COHERE_API_KEY"

def ask_cohere(prompt):
    response = requests.post(
        "https://api.cohere.com/v1/chat",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "command-r-plus-08-2024",
            "message": prompt
        }
    )
    data = response.json()
    
    if "text" in data:
        print("---- Cohere Response ----")
        print(data["text"])
        print("-------------------------")
    else:
        print("Error:", data)

user_prompt = input("Enter your prompt: ")
ask_cohere(user_prompt)