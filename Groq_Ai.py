import requests

API_KEY = "GROQ_API_KEY"

def chat(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    if "error" in result:
        return f"Error: {result['error']['message']}"
    
    return result["choices"][0]["message"]["content"]

# --- Main ---
print("=" * 40)
print("     Groq AI Chat")
print("=" * 40)
print("Type 'exit' to quit\n")

while True:
    user_input = input("Enter your prompt: ")
    
    if not user_input.strip():
        continue
    
    if user_input.lower() in ["exit", "quit"]:
        print("Bye!")
        break
    
    print("\nGroq: thinking...")
    reply = chat(user_input)
    print(f"\nGroq: {reply}\n")
    print("-" * 40)