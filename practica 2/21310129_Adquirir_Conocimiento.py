
"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
practica #2 "chatbox"
"""

# Diccionario precargado con algunas preguntas y respuestas
conocimiento = {
    "Hola": "�Hola! �C�mo est�s?",
    "Como estas?": "Estoy bien, gracias por preguntar. �Y t�?",
    "de que te gustar�a hablar?": "Podemos hablar de lo que quieras. �Tienes algo en mente?"
}

def chatbot():
    print("Chatbot activado. Puedes empezar a preguntar.")
    
    while True:
        # Input del usuario
        pregunta = input("T�: ").strip()

        # Verificamos si la pregunta est� en la base de datos (diccionario)
        if pregunta in conocimiento:
            # Si la pregunta existe, mostramos la respuesta
            print(f"Chatbot: {conocimiento[pregunta]}")
        else:
            # Si la pregunta no existe, solicitamos al usuario una nueva respuesta
            print("Chatbot: No conozco la respuesta a esa pregunta. �Qu� deber�a responder en este caso?")
            nueva_respuesta = input("Por favor, ingresa la respuesta: ").strip()

            # Agregamos la nueva pregunta y respuesta a la base de datos
            conocimiento[pregunta] = nueva_respuesta
            print("Chatbot: �Gracias! He aprendido algo nuevo.")
        
        # Opci�n para salir del chat
        continuar = input("�Deseas seguir hablando? (s�/no): ").strip().lower()
        if continuar != "s�":
            print("Chatbot: �Hasta pronto!")
            break

# Ejecutar el chatbot
chatbot()
