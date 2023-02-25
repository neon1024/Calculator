class Console:
    def __init__(self, CalculatorService, CalculatorRepository):
        self.__CalculatorService = CalculatorService
        self.__CalculatorRepository = CalculatorRepository

        self.__console_options = {"x": exit}

    def __get_console_option_from_user(self):
        user_input = input("> ")

        # TODO: validate user input

        user_input = user_input.strip()

        return user_input

    @staticmethod
    def __print_console_options():
        print("x: exit")

    def run_console(self):
        while True:
            self.__print_console_options()

            chosen_option = self.__get_console_option_from_user()

            try:
                self.__console_options[chosen_option]()
            
            except Exception as console_option_error:
                print(console_option_error)
