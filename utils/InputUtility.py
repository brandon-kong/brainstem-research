class InputUtility:
    @staticmethod
    def get_int_input(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def get_float_input(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def get_string_input(prompt: str) -> str:
        return input(prompt)
    
    @staticmethod
    def get_bool_input(prompt: str) -> bool:
        while True:
            try:
                return bool(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a boolean value.")

    @staticmethod
    def get_yes_no_input(prompt: str) -> bool:
        while True:
            try:
                return input(prompt).lower().strip() in ['y', 'yes']
            except ValueError:
                print("Invalid input. Please enter 'y' or 'n'.")