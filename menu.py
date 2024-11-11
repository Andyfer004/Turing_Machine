from turing_machine import TuringMachine
from utils import save_input_to_file, save_output_to_file
from description import show_machine_description

def run_predefined_test(input_string, output_dir, input_filename, output_filename, transitions, initial_state, accept_state, reject_state):
    """Ejecuta una prueba predefinida y guarda el archivo de entrada y salida."""
    save_input_to_file(output_dir, input_filename, input_string)
    tm = TuringMachine(input_string, transitions, initial_state, accept_state, reject_state)
    output_lines = []
    step_count = 0
    while tm.step() and step_count < 100:
        output_lines.append(tm.display_tape())
        step_count += 1
    save_output_to_file(output_lines, f"{output_dir}/{output_filename}")

def main_menu():
    """Menú principal para ejecutar la máquina de Turing."""
    transitions = {
        ("q0", "a"): ("a", "R", "q1"),
        ("q0", "b"): ("b", "R", "q0"),
        ("q0", "_"): ("_", "R", "qreject"),
        ("q1", "a"): ("a", "R", "q1"),
        ("q1", "b"): ("b", "R", "q2"),
        ("q1", "_"): ("_", "R", "qreject"),
        ("q2", "b"): ("b", "R", "q0"),
        ("q2", "a"): ("a", "R", "qaccept"),
        ("q2", "_"): ("_", "R", "qreject"),
    }
    initial_state = "q0"
    accept_state = "qaccept"
    reject_state = "qreject"

    while True:
        print("\n--- 🧩 Simulador de Máquina de Turing: Explora la Lógica 🧩 ---")
        print("1️⃣   Detalles completos sobre esta máquina de Turing")
        print("2️⃣   Ingresa tu propia cadena para simularla")
        print("3️⃣   Prueba una cadena de 'Aceptación'")
        print("4️⃣   Prueba una cadena de 'Rechazo'")
        print("5️⃣   Prueba una cadena para provocar 'Bucle Infinito'")
        print("6️⃣   Termina y cierra el simulador")
        choice = input("Tu elección: ")


        if choice == "1":
            show_machine_description()
        elif choice == "2":
            user_input = input("Ingrese la cadena a evaluar: ")
            tm = TuringMachine(user_input, transitions, initial_state, accept_state, reject_state)
            tm.run()
        elif choice == "3":
            run_predefined_test("babbbab", "Aceptación", "aceptación.txt", "resultado_aceptación.txt", transitions, initial_state, accept_state, reject_state)
        elif choice == "4":
            run_predefined_test("abbbaaaaaaa", "Rechazo", "input_rechazado_turing.txt", "output_rechazado_turing.txt", transitions, initial_state, accept_state, reject_state)
        elif choice == "5":
            run_predefined_test("aaaaaaa", "Infinito", "input_infinito_turing.txt", "output_infinito_turing.txt", transitions, initial_state, accept_state, reject_state)
        elif choice == "6":
            print("Gracias por usar la Máquina de Turing. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")