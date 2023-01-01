import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Powered By OPENAI")
while True:
    prompt = input("Ask me anything -> ")
    completions = openai.Completion.create(prompt=prompt, engine="text-davinci-002",max_tokens=100)

    completion = completions.choices[0].text
    print(completion)
    
    
