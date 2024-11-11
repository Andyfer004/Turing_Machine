class TuringMachine:
    def __init__(self, tape, transitions, initial_state, accept_state, reject_state, blank_symbol="_"):
        self.tape = list(tape)
        self.head = 0
        self.transitions = transitions
        self.current_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol

    def step(self):
        """Ejecuta un paso de la máquina de Turing."""
        if self.current_state in [self.accept_state, self.reject_state]:
            return False

        symbol = self.tape[self.head] if self.head < len(self.tape) else self.blank_symbol
        action = self.transitions.get((self.current_state, symbol))

        if action is None:
            self.current_state = self.reject_state
            return False

        new_symbol, direction, new_state = action
        self.tape[self.head] = new_symbol
        self.move_head(direction)
        self.current_state = new_state
        return True

    def move_head(self, direction):
        """Mueve el cabezal en la dirección especificada."""
        if direction == "R":
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append(self.blank_symbol)
        elif direction == "L":
            self.head -= 1
            if self.head < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head = 0

    def display_tape(self):
        """Devuelve una representación de la cinta con el estado actual del cabezal."""
        return " ".join([f"[{char}]" if i == self.head else char for i, char in enumerate(self.tape)])

    def run(self, step_limit=100):
        """Ejecuta la máquina hasta el límite de pasos o hasta alcanzar un estado de aceptación/rechazo."""
        step_count = 0
        while self.step() and step_count < step_limit:
            print(self.display_tape())
            step_count += 1
        return self.current_state == self.accept_state
