import os

def save_input_to_file(directory="data_inputs", filename="example_input.txt", tape=""):
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, filename), "w") as file:
        file.write(tape)
    print(f"Archivo de entrada guardado en '{directory}/{filename}'.")

def save_output_to_file(output_lines, output_file="simulation_outputs/example_output.txt"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as file:
        file.write("\n".join(output_lines))
    print(f"Archivo de salida guardado en '{output_file}'.")
