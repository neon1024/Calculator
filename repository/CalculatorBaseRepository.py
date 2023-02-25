from domain.Operation import Operation


class CalculatorBaseRepository:
    def __init__(self):
        self._history = []

    def get_history(self):
        return self._history

    def add_operation_to_history(self, symbol, operands):
        operation = Operation(symbol, operands)

        self._history.append(operation)

    def update_history(self, new_history):
        self._history = new_history

    def clear_history(self):
        self._history.clear()
