def speech_en():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        print("Lütfen konuşun")

        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        print("Sesler yazıya çeviriliyor...")
        return(recog.recognize_google(audio, language= "en-GB" + "   dediniz."))
    