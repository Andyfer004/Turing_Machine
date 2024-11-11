from turing_machine import TuringMachine
from utils import save_input_to_file, save_output_to_file
from description import show_machine_description
import os
from colorama import init, Fore, Style

# Inicializa colorama para sistemas Windows
init(autoreset=True)
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
    """Menú principal para ejecutar la máquina de Turing con opciones predefinidas o ingresadas por el usuario."""
    transitions = {
        ("q0", "a"): ("a", "R", "q1"),
        ("q0", "b"): ("b", "R", "qloop"),
        ("q0", "_"): ("_", "R", "qreject"),
        ("q1", "a"): ("a", "R", "q1"),
        ("q1", "b"): ("b", "R", "q2"),
        ("q1", "_"): ("_", "R", "qreject"),
        ("q2", "a"): ("a", "R", "qaccept"),
        ("q2", "b"): ("b", "R", "qloop"),
        ("q2", "_"): ("_", "R", "qloop"),
        ("qloop", "a"): ("a", "R", "q1"),
        ("qloop", "b"): ("b", "R", "qloop"),
        ("qloop", "_"): ("_", "R", "qloop"),
    }
    initial_state = "q0"
    accept_state = "qaccept"
    reject_state = "qreject"

    while True:
        print(f"{Fore.MAGENTA}\n--- 🎛️ Menú Principal de la Máquina de Turing 🎛️ ---{Style.RESET_ALL}")
        print("Seleccione una de las opciones para explorar el funcionamiento de la máquina:\n")
        print(" 1️⃣  📜 Ver descripción de la máquina y el lenguaje aceptado")
        print(" 2️⃣  🔎 Ingresar y evaluar una cadena personalizada")
        print(" 3️⃣  ✅ Probar con cadena de ejemplo que resultará en 'Aceptación'")
        print(" 4️⃣  ❌ Probar con cadena de ejemplo que resultará en 'Rechazo'")
        print(" 5️⃣  🔁 Probar con cadena de ejemplo que provocará un 'Bucle Infinito'")
        print(" 6️⃣  🚪 Salir del simulador\n")
        
        choice = input("✨ Elija una opción y presione Enter: ")

        if choice == "1":
            show_machine_description()

        elif choice == "2":
            user_input = input("✍️  Ingrese la cadena que desea evaluar: ")
            print(f"{Fore.MAGENTA}\n--- Resultado para la cadena ingresada ---{Style.RESET_ALL}")
            tm = TuringMachine(
                user_input, transitions, initial_state, accept_state, reject_state
            )
            tm.run()

        elif choice == "3":
            print(f"{Fore.MAGENTA}\n--- Ejecutando prueba con cadena de 'Aceptación' ---{Style.RESET_ALL}")
            run_predefined_test(
                "aabba",               # Cadena de aceptación
                "simulation_outputs",
                "accept_input.txt",
                "accept_output.txt",
                transitions,
                initial_state,
                accept_state,
                reject_state,
            )

        elif choice == "4":
            print(f"{Fore.MAGENTA}\n--- Ejecutando prueba con cadena de 'Rechazo' ---{Style.RESET_ALL}")
            run_predefined_test(
                "bbbbba",              # Cadena de rechazo
                "simulation_outputs",
                "reject_input.txt",
                "reject_output.txt",
                transitions,
                initial_state,
                accept_state,
                reject_state,
            )

        elif choice == "5":
            print(f"{Fore.MAGENTA}\n--- Ejecutando prueba con cadena de 'Bucle Infinito' ---{Style.RESET_ALL}")
            run_predefined_test(
                "bababa",              # Cadena de bucle infinito
                "simulation_outputs",
                "infinite_input.txt",
                "infinite_output.txt",
                transitions,
                initial_state,
                accept_state,
                reject_state,
            )

        elif choice == "6":
            print(f"{Fore.GREEN}Gracias por usar el Simulador de Máquina de Turing. ¡Hasta pronto!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}⚠️  Opción no válida. Por favor, intente de nuevo.{Style.RESET_ALL}")
