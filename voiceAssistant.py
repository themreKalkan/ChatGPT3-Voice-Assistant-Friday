import openai
import speech_recognition as sr
from gtts import gTTS
import os
import pygame
import time
import threading

oldTime = 0
#Your OpenAI API Key
openai.api_key = "Your-API-Key"

#Speech Recognition 
r = sr.Recognizer()
mod = 0

#A function for get response from ChatGPT
def get_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=128, n=1, stop=None, temperature=0.8
    )
    return response.choices[0].text.strip()


#Main Loop
while True:

    newTime = round(time.time())
    oldTime = newTime - oldTime

    with sr.Microphone() as source:
        print("Ask your question:")
        audio = r.listen(source)
        
    try:
        prompt = r.recognize_google(audio,language="tr-TR")
        print("Your uestion: " + prompt)
    except sr.UnknownValueError:
        print("Voice Not Understood")
        continue
    except sr.RequestError:
        print("Connection Error")
        continue
    promptLow = ""
    promptLow = str(prompt.lower())
    if(promptLow == "friday" and mod == 0):
        print(promptLow)
        file = 'frSong.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        mod = 1
        time.sleep(1.2)
        continue

    if (promptLow == "durdur" and mod == 1):
        print(promptLow)
        pygame.mixer.music.stop()
        file = 'lrSong.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        mod = 0
        time.sleep(0.6)
        continue

    #Play the response
    if(mod == 1):
        os.remove("gptOutput.mp3")
        response = get_gpt3_response(prompt)
        response = response.replace("\n"," ")
        print("Cevap: " + response)

        text = str(response)
        language = "tr"
        output = gTTS(text=text, lang=language, slow=False)
        output.save("gptOutput.mp3")
        file2 = 'gptOutput.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file2)
        pygame.mixer.music.play()



    if(mod == 1 and oldTime == 20):
        oldTime = newTime
        file = 'lrSong.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        mod = 0







