def show_machine_description():
    """Presenta una descripción personalizada y detallada de la máquina de Turing."""
    print("\n--- 🌟 Mi Máquina de Turing Única 🌟 ---")
    print("Esta máquina está configurada para procesar cadenas compuestas por los símbolos 'a' y 'b'.")
    print("💡 Lenguaje aceptado: L(M) = { x ∈ {a, b}* | x contiene la subcadena 'bab' }\n")
    print("🔹 Conjunto de Estados (Q) = {q0, q1, q2, qloop, qaccept, qreject}")
    print("🔹 Alfabeto de Entrada = {a, b}")
    print("🔹 Alfabeto de la Cinta (Tau, Σ) = {a, b, _}\n")
    print("📜 Función de Transición (S):")
    print("""
        ➡️ S(q0, a) = (a, R, q1)     # Si está en q0 y lee 'a', escribe 'a', mueve a la derecha y va a q1
        ➡️ S(q0, b) = (b, R, qloop)  # Si está en q0 y lee 'b', escribe 'b', mueve a la derecha y va a qloop (bucle infinito)
        ➡️ S(q0, _) = (_, R, qreject) # Si está en q0 y lee '_', va al estado de rechazo

        ➡️ S(q1, a) = (a, R, q1)     # Si está en q1 y lee 'a', se queda en q1 y mueve a la derecha
        ➡️ S(q1, b) = (b, R, q2)     # Si está en q1 y lee 'b', escribe 'b', mueve a la derecha y va a q2
        ➡️ S(q1, _) = (_, R, qreject) # Si está en q1 y lee '_', va al estado de rechazo

        ➡️ S(q2, a) = (a, R, qaccept) # Si está en q2 y lee 'a', acepta
        ➡️ S(q2, b) = (b, R, qloop)  # Si está en q2 y lee 'b', escribe 'b', mueve a la derecha y va a qloop
        ➡️ S(q2, _) = (_, R, qloop)  # Si está en q2 y lee '_', sigue en el bucle infinito (qloop)

        ➡️ S(qloop, a) = (a, R, q1)  # Si está en qloop y lee 'a', va a q1
        ➡️ S(qloop, b) = (b, R, qloop) # Si está en qloop y lee 'b', permanece en qloop
        ➡️ S(qloop, _) = (_, R, qloop) # Si está en qloop y lee '_', sigue en el bucle infinito
    """)
    print("🔹 Estado Inicial: q0")
    print("🔹 Estado de Aceptación: qaccept")
    print("🔹 Estado de Rechazo: qreject")
    print("🔹 Estado de Bucle Infinito: qloop\n")
