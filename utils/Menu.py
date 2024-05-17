from typing import Dict, Callable

from utils.Printer import Printer, Color
from utils.logger.Logger import Logger

type Options = Dict[str, Callable[[], None]]


class Menu:
    """
    The Menu class provides a way to create a menu that allows the user to select an option from a list of options.
    Ensure that the options are a dictionary where the key is the option and the value is the action to be performed.
    The key should be a string that also describes the action to be performed.

    Example:

    ```python
    options = {
        'Perform K-means clustering': lambda: print('Performing K-means clustering'),
        'Perform PCA': lambda: print('Performing PCA'),
        'Perform t-SNE': lambda: print('Performing t-SNE'),
    }

    menu = Menu(options)

    menu.run()
    ```

    """

    def __init__(
            self, options: Options,
            start_message: str = 'Please select an option from the menu below:',
            include_exit: bool = False,
            include_back: bool = True
    ):

        self.options = options
        self.start_message = start_message
        self.include_exit = include_exit
        self.include_back = include_back

    def run(self):
        while True:
            Printer.print(f'\n{self.start_message}\n')

            if self.include_exit:
                self.options['Exit'] = lambda: 'back'

            if self.include_back:
                self.options['Back'] = lambda: 'back'

            enumerated = enumerate(self.options.keys())

            for i, option in enumerated:
                if option == 'Back':
                    Printer.custom(f'[back] {option}', color=Color.YELLOW)
                elif option == 'Exit':
                    Printer.custom(f'[exit] {option}', color=Color.RED)

                else:
                    Printer.print(f'[{i + 1}] {option}')

            # Print an extra line
            print()

            choice = input('Enter your choice: ')

            if choice.lower() == 'exit' and self.include_exit:
                break

            if choice.lower() == 'back' and self.include_back:
                return

            # Check if the choice is a number
            if not choice.isdigit():
                Printer.error('Invalid option')
                continue

            choice = int(choice) - 1

            if choice < 0 or choice >= len(self.options):
                Printer.error('Invalid option')
                continue

            choice = list(self.options.keys())[choice]

            action = self.options.get(choice)

            if action:
                action()
            else:
                Printer.error('Invalid option')
