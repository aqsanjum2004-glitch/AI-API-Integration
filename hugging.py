import requests

API_KEY = "HUGGINGFACE_API_KEY"  # ← your token

def ask_huggingface(prompt):
    response = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/Llama-3.1-8B-Instruct:fastest",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )
    print("Status:", response.status_code)
    data = response.json()

    if "choices" in data:
        print("---- Hugging Face Response ----")
        print(data["choices"][0]["message"]["content"])
        print("-------------------------------")
    else:
        print("Error:", data)

user_prompt = input("Enter your prompt: ")
ask_huggingface(user_prompt)