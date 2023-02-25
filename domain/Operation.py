class Operation:
    def __init__(self, operation, operands):
        self.__operation = operation
        self.__operands = operands

    def __repr__(self):
        return str(self)

    def __str__(self):
        operation = f"{self.__operands[0]}"

        for index in range(1, len(self.__operands)):
            operation += " "
            operation += f"{self.__operation}"
            operation += " "
            operation += f"{self.__operands[index]}"

        return operation
