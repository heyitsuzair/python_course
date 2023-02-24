import win32com.client as wincom


speak = wincom.Dispatch("SAPI.SpVoice")

l=['Ahmed','Uzair','Ali']

for name in l:
    text = f"Shoutout To {name}"
    speak.Speak(text)
    

