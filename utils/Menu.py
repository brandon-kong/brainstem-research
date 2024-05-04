from typing import Dict, Callable

from utils.Printer import Printer
from utils.logger.LoggerFactory import LoggerFactory

type Options = Dict[str, Callable[[], None]]

class Menu:
    """
    The Menu class provides a way to create a menu that allows the user to select an option from a list of options.
    Ensure that the options are a dictionary where the key is the option and the value is the action to be performed.
    The key should be a string that also describes the action to be performed.

    Example:

    ```python
    options = {
        '1. Perform K-means clustering': lambda: print('Performing K-means clustering'),
        '2. Perform PCA': lambda: print('Performing PCA'),
        '3. Perform t-SNE': lambda: print('Performing t-SNE'),
    }

    menu = Menu(options)

    menu.run()
    ```

    """
    def __init__(self, options: Options):
        self.options = options

        self.printer = Printer()
        self.logger = LoggerFactory.make_logger('menu.log')

    def run(self):
        while True:
            self.printer.print('Please select an option from the menu below:\n')
            
            enumerated = enumerate(self.options)
            
            for index, option in enumerate(self.options):
                self.printer.print(f'{index + 1}. {option}')

            choice = input('Enter your choice: ')

            # Check if the choice is a number
            if not choice.isdigit():
                self.printer.error('Invalid option')
                continue

            choice = int(choice) - 1

            if choice < 0 or choice >= len(self.options):
                self.printer.error('Invalid option')
                continue

            choice = list(enumerated)[choice][1]

            action = self.options.get(choice)

            if action:
                action()
            else:
                self.printer.error('Invalid option')
