import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say anything...")
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        print("Your text is : " + text)
    except:
        print("Some error is occured")
