import openai

openai.api_key = "YOUR-API-KEY"


def generate_response():
    prompt = str(input(": "))
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
    )


    message = response.choices[0].text.strip()
    print(message)
    return message

while True:
    generate_response()
