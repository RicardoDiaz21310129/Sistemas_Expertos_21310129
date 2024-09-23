
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
    "Hola": "¡Hola! ¿Cómo estás?",
    "Como estas?": "Estoy bien, gracias por preguntar. ¿Y tú?",
    "de que te gustaría hablar?": "Podemos hablar de lo que quieras. ¿Tienes algo en mente?"
}

def chatbot():
    print("Chatbot activado. Puedes empezar a preguntar.")
    
    while True:
        # Input del usuario
        pregunta = input("Tú: ").strip()

        # Verificamos si la pregunta está en la base de datos (diccionario)
        if pregunta in conocimiento:
            # Si la pregunta existe, mostramos la respuesta
            print(f"Chatbot: {conocimiento[pregunta]}")
        else:
            # Si la pregunta no existe, solicitamos al usuario una nueva respuesta
            print("Chatbot: No conozco la respuesta a esa pregunta. ¿Qué debería responder en este caso?")
            nueva_respuesta = input("Por favor, ingresa la respuesta: ").strip()

            # Agregamos la nueva pregunta y respuesta a la base de datos
            conocimiento[pregunta] = nueva_respuesta
            print("Chatbot: ¡Gracias! He aprendido algo nuevo.")
        
        # Opción para salir del chat
        continuar = input("¿Deseas seguir hablando? (sí/no): ").strip().lower()
        if continuar != "sí":
            print("Chatbot: ¡Hasta pronto!")
            break

# Ejecutar el chatbot
chatbot()
