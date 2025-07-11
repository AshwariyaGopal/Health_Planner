import google.generativeai as genai
genai.configure(api_key="YOUR_KEY_HERE")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Hello Gemini!")
print(response.text)