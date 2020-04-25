# needs pyaudio
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
         print("say!")
         audio = r.listen(source, timeout=5, phrase_time_limit=10)
         print ("recognizing")

BING_KEY ="ae653a62c0944c019b20a3f04b0f51db"
try:
         msg = r.recognize_bing(audio, key="ae653a62c0944c019b20a3f04b0f51db")
         print (msg)
except sr.UnknownValueError:
         print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
         print("check internet or validation ")

