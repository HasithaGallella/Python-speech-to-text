# Open your cmd and Install below libraries for windows machine before using the code

# $ pip3 install pydub
# $ pip3 install PyAudio
# $ pip3 install SpeechRecognition

#code; 

import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something....")
    audio = r.listen(source)
    print("I'm Recognizing your speech right Now .... ")


    # recognize using google
    try:
        speech= r.recognize_google(audio)
        string ="You have said \n" + speech
    except Exception as e:
        print("Error :  " + str(e))
    
    # Write to the terminal
    print(string)
    # Write to a txt file
    f1 = open("recorded.txt", "w+")
    f1.write(string)
    f1.close()
    # Write to a audio wav file
    with open("recorded.wav", "wb") as f2:
        f2.write(audio.get_wav_data())


