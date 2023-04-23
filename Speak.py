import speech_recognition as sr

# Criando um objeto de reconhecimento de fala
r = sr.Recognizer()

# Usando o microfone como fonte de entrada de áudio
with sr.Microphone() as source:
    print("Fale algo...")
    # Escutando a fala e armazenando em uma variável de áudio
    audio = r.listen(source)

    try:
        # Reconhecendo a fala usando o Google Speech Recognition
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto)
    except sr.UnknownValueError:
        print("Não entendi o que você disse")
    except sr.RequestError as e:
        print("Não foi possível completar a requisição; {0}".format(e))
