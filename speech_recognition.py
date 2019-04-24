import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source,timeout=3, phrase_time_limit=3)
    try:
        text = r.recognize_google(audio)
        print("You said " + r.recognize_google(audio))
    except:
    	print("Sorry could not recognize what you said")
