import requests

API_KEY = "gemini_api_ key"

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "parts": [{"text": "hi"}]
        }
    ]
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())