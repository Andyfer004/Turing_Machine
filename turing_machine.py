class TuringMachine:
    def __init__(self, tape, transitions, initial_state, accept_state, reject_state, blank_symbol="_"):
        """
        Inicializa la máquina de Turing con la cinta de entrada, los estados y las transiciones.
        
        Parámetros:
            tape (str): La cinta de entrada de la máquina.
            transitions (dict): Un diccionario con reglas de transición, donde las claves son tuplas (estado_actual, símbolo_actual)
                                y los valores son tuplas (nuevo_símbolo, dirección, nuevo_estado).
            initial_state (str): El estado inicial de la máquina.
            accept_state (str): El estado de aceptación de la máquina.
            reject_state (str): El estado de rechazo de la máquina.
            blank_symbol (str): El símbolo en blanco para la cinta, por defecto es "_".
        """
        self.tape = list(tape)  # Convierte la cinta de entrada en una lista para fácil manipulación.
        self.head = 0  # Posición inicial del cabezal.
        self.transitions = transitions  # Diccionario con las reglas de transición.
        self.current_state = initial_state  # Estado en el que comienza la máquina.
        self.accept_state = accept_state  # Estado de aceptación.
        self.reject_state = reject_state  # Estado de rechazo.
        self.blank_symbol = blank_symbol  # Símbolo usado para celdas en blanco en la cinta.

    def step(self):
        """
        Ejecuta un paso único de la máquina de Turing.
        
        Retorna:
            bool: True si el paso se ejecutó y la máquina no está en estado de aceptación o rechazo.
                  False si la máquina alcanzó un estado de aceptación/rechazo o no tiene una transición válida.
        """
        # Verifica si la máquina ha alcanzado un estado de aceptación o rechazo.
        if self.current_state in [self.accept_state, self.reject_state]:
            return False  # La máquina no debe ejecutar más pasos.

        # Obtiene el símbolo actual bajo el cabezal. Usa el símbolo en blanco si el cabezal está fuera de la cinta.
        symbol = self.tape[self.head] if self.head < len(self.tape) else self.blank_symbol
        
        # Busca la transición correspondiente para el estado y símbolo actuales.
        action = self.transitions.get((self.current_state, symbol))
        
        # Si no hay una transición válida, la máquina pasa al estado de rechazo.
        if action is None:
            self.current_state = self.reject_state
            return False

        # Descompone la acción en nuevo símbolo, dirección de movimiento y nuevo estado.
        new_symbol, direction, new_state = action
        
        # Actualiza la cinta con el nuevo símbolo y mueve el cabezal.
        self.tape[self.head] = new_symbol
        self.move_head(direction)
        
        # Cambia al nuevo estado.
        self.current_state = new_state
        return True

    def move_head(self, direction):
        """
        Mueve el cabezal de la máquina en la dirección especificada.
        
        Parámetros:
            direction (str): "R" para mover a la derecha, "L" para mover a la izquierda.
        """
        if direction == "R":
            # Incrementa la posición del cabezal para moverse a la derecha.
            self.head += 1
            # Si el cabezal excede el tamaño de la cinta, agrega un símbolo en blanco al final.
            if self.head >= len(self.tape):
                self.tape.append(self.blank_symbol)
        elif direction == "L":
            # Decrementa la posición del cabezal para moverse a la izquierda.
            self.head -= 1
            # Si el cabezal es negativo, agrega un símbolo en blanco al inicio y ajusta la posición del cabezal.
            if self.head < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head = 0

    def display_tape(self):
        """
        Devuelve una representación visual de la cinta, mostrando el símbolo actual bajo el cabezal.
        
        Retorna:
            str: Una cadena donde el símbolo bajo el cabezal está entre corchetes [].
        """
        return " ".join([f"[{char}]" if i == self.head else char for i, char in enumerate(self.tape)])

    def run(self, step_limit=100):
        """
        Ejecuta la máquina de Turing en modo automático hasta alcanzar un estado de aceptación/rechazo o un límite de pasos.
        
        Parámetros:
            step_limit (int): Límite de pasos para evitar bucles infinitos. Por defecto es 100.
        
        Retorna:
            bool: True si la máquina termina en un estado de aceptación, False en caso contrario.
        """
        step_count = 0  # Inicializa el contador de pasos.
        
        # Ejecuta los pasos mientras no se alcance el límite y la máquina esté en modo activo.
        while self.step() and step_count < step_limit:
            print(self.display_tape())  # Muestra el estado actual de la cinta.
            step_count += 1  # Incrementa el contador de pasos.
        
        # Retorna True si la máquina terminó en estado de aceptación, False en caso contrario.
        return self.current_state == self.accept_state
