from utils.Printer import Printer

printer = Printer()

class InputUtility:
    @staticmethod
    def get_int_input(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                printer.error("Invalid input. Please enter an integer.")

    @staticmethod
    def get_float_input(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                printer.error("Invalid input. Please enter a number.")

    @staticmethod
    def get_string_input(prompt: str) -> str:
        return input(prompt)
    
    @staticmethod
    def get_bool_input(prompt: str) -> bool:
        while True:
            try:
                return bool(input(prompt))
            except ValueError:
                printer.error("Invalid input. Please enter a boolean value.")

    @staticmethod
    def get_yes_no_input(prompt: str) -> bool:
        prompt += " (y/n): "
        while True:
            try:
                inp = input(prompt).lower().strip()
                print()
                if inp in ['y', 'yes']:
                    return True
                elif inp in ['n', 'no']:
                    return False
                else:
                    raise ValueError
            except ValueError:
                printer.error("Invalid input. Please enter 'y' or 'n'.\n")
