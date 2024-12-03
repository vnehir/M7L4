import speech_recognition as sr

# Argüman Oluşturmak
def speech_fnc(lang):
    #Mikrofon değerini bir değişkenin içerisine atamak
    mic = sr.Microphone()
    #Analog formatta ses Kaydının anlaşıldığı değer:
    recog = sr.Recognizer()


    # Bir mikrofon nesnesini (mic) alarak, bu nesneyi kullanarak ses kaydı yapacağımız bir ortam oluşturur
    # Bu sayede, kod bloğu tamamlandığında mikrofon otomatik olarak kapatılır.
    with mic as source:
        # Mikrofon üzerinden alınan ilk ses kayıtlarını kullanarak ortam gürültüsünü analiz eder. 
        # Bu sayede, daha sonraki ses kayıtlarında ortam gürültüsünün etkisi azaltılır.
        recog.adjust_for_ambient_noise(source)
        # Analog Formattan Sesin Dijital Ortama Aktarılması işidir.
        audio = recog.listen(source)
        # Bu satır, alınan ses kaydını Google'ın ses tanıma API'sini kullanarak metin formatına çevirir
        return recog.recognize_google(audio, language=lang)



