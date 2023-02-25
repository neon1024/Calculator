class Console:
    def __init__(self, CalculatorService, CalculatorRepository):
        self.__CalculatorService = CalculatorService
        self.__CalculatorRepository = CalculatorRepository

        self.__console_options = {
            "add": self.__add,
            "sub": self.__sub,
            "mul": self.__mul,
            "div": self.__div,
            "mod": self.__mod,
            "show history": self.__show_history,
            "clear history": self.__clear_history,
            "x": exit
        }

        self.__symbols = {
            "add": "+",
            "sub": "-",
            "mul": "*",
            "div": "/",
            "mod": "%"
                    }

    def __add(self, operands):
        result = 0

        for operand in operands:
            result += float(operand)

        print(f"> {result}")

    def __sub(self, operands):
        result = 0

        for operand in operands:
            result -= float(operand)

        result += float(operands[0])*2

        print(f"> {result}")

    def __mul(self, operands):
        result = 1

        for operand in operands:
            result *= float(operand)

        print(f"> {result}")

    def __div(self, operands):
        result = operands[0]

        for _ in range(1, len(operands)):
            result /= float(operands[0])

        print(f"> {result}")

    def __mod(self, operands):
        result = operands[0]

        for _ in range(1, len(operands)):
            result %= float(operands[0])

        print(f"> {result}")

    def __show_history(self):
        history = self.__CalculatorRepository.get_history()

        for operation in history:
            print(operation)

    def __clear_history(self):
        self.__CalculatorRepository.clear_history()

    def __get_user_input(self):
        user_input = input("> ")

        # TODO: validate user input

        user_input = user_input.strip()

        tokens = user_input.split()

        if len(tokens) == 1:
            if tokens[0] != "x":
                print("[!] Invalid input")
                return -1, None

        if len(tokens) == 2:
            if tokens[0] == "show" and tokens[1] == "history":
                return tokens[0] + " " + tokens[1], None
            elif tokens[0] == "clear" and tokens[1] == "history":
                return tokens[0] + " " + tokens[1], None
            else:
                print("[!] Invalid input")
                return -1, None

        chosen_option = tokens[0]

        if chosen_option not in self.__console_options:
            print(f"[!] The option {chosen_option} doesn't exist")
            return -1, None

        operands = tuple(tokens[1:])

        return chosen_option, operands

    @staticmethod
    def __print_console_options():
        print("Add N numbers: add <op1> ... <opN>")
        print("Sub N numbers: sub <op1> ... <opN>")
        print("Mul N numbers: mul <op1> ... <opN>")
        print("Div N numbers: div <op1> ... <opN>")
        print("Mod N numbers: mod <op1> ... <opN>")
        print("Show  history: show history")
        print("Clear history: clear history")
        print("Exit: x")

    def run_console(self):
        while True:
            self.__print_console_options()

            chosen_option, operands = self.__get_user_input()

            if chosen_option != -1:
                if operands:
                    self.__console_options[chosen_option](operands)

                    symbol = self.__symbols[chosen_option]

                    self.__CalculatorRepository.add_operation_to_history(symbol, operands)

                else:
                    self.__console_options[chosen_option]()
